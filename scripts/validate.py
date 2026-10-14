#!/usr/bin/env python3
"""Static packaging checks against the supplied publishing guide; not agy validation."""
import hashlib, json, re, struct, subprocess, sys
from pathlib import Path
import yaml
root = Path(__file__).resolve().parent.parent
def read(name): return json.loads((root / name).read_text())
def require(ok, message):
    if not ok: raise SystemExit('FAIL: ' + message)
def local(path):
    resolved = (root / path).resolve()
    require(resolved.is_relative_to(root) and resolved.exists(), 'Missing/escaping path: ' + path)
    return resolved
m = read('plugin.json')
require(m['name'] == root.name and re.fullmatch(r'[a-z0-9]+(-[a-z0-9]+)*',m['name']) and len(m['name']) <= 64, 'Plugin name')
require(re.fullmatch(r'\d+\.\d+\.\d+',m['version']), 'Semantic version')
for field in ['description','displayName','author','license','logo']:
    require(bool(m.get(field)), 'Required marketplace metadata: ' + field)
require(1 <= len(m['suggestedPrompts']) <= 3 and all(m['suggestedPrompts']), 'Starter prompts')
png = local(m['logo']).read_bytes()
require(png[:8] == b'\x89PNG\r\n\x1a\n', 'PNG logo')
w,h = struct.unpack('>II',png[16:24]); require(w == h and w >= 128, 'Square logo >=128px')
source = read('skills-source.json')
for path,digest in source['files'].items():
    require(hashlib.sha256(local(path).read_bytes()).hexdigest() == digest, 'Upstream hash mismatch: '+path)
names=set(); discovered=set()
for folder in m['skills']:
    for path in sorted(local(folder).glob('*/SKILL.md')):
        data = yaml.safe_load(path.read_text().split('---',2)[1])
        name=data['name']; desc=data['description']
        require(name == path.parent.name and re.fullmatch(r'[a-z0-9]+(-[a-z0-9]+)*',name) and len(name)<=64, 'Skill name: '+str(path))
        require(isinstance(desc,str) and 1<=len(desc)<=1024, 'Skill description: '+name)
        require(name not in names, 'Duplicate skill: '+name)
        names.add(name); discovered.add(path)
require(discovered == set((root/'skills').rglob('SKILL.md')), 'Undiscoverable skills')
require(len(names)==source['skillCount'], 'Skill inventory count')
profiles=[read('config/hosted-oauth.json'),read('config/local-pat.json')]
active=read(m['mcpServers']); require(active in profiles, 'Unknown active profile')
for profile in profiles:
    require(list(profile['mcpServers'])==['harness'], 'Exactly one active server')
    variables={v['name']:v for v in profile.get('variables',[])}
    refs=set(re.findall(r'\$\{([A-Z_]+)\}',json.dumps(profile['mcpServers'])))
    require(refs == set(variables), 'Undeclared/unused variables')
host=profiles[0]['mcpServers']['harness']
require(host == {'serverUrl':'https://mcp.harness.io/mcp','oauth':{'clientId':'mcp-client'}}, 'Hosted OAuth without PAT or secret')
pat=profiles[1]['mcpServers']['harness']
require(pat['command']=='npx' and pat['args']==['-y','harness-mcp-v2@3.2.34','stdio'], 'Pinned local server')
require(pat['env']['HARNESS_API_KEY']=='${HARNESS_API_KEY}' and pat['env']['HARNESS_MCP_MODE']=='single-user','PAT via variable')
require(next(v for v in profiles[1]['variables'] if v['name']=='HARNESS_API_KEY')['secret'] is True,'PAT marked secret')
require(not (root/'hooks.json').exists(), 'No automatic hooks')
subprocess.run([sys.executable,str(root/'scripts/upstream/check_links.py'),'--root',str(root),'skills','references','templates'],check=True,cwd=root)
print(f'PASS: manifest, {len(names)} skills, {len(source["files"])} upstream hashes, reference links, logo, and both connection profiles.')
print('NOT TESTED: agy validation/install, OAuth callback/sign-in, or authenticated API calls.')
