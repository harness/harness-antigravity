#!/usr/bin/env python3
"""Vendor a reviewed Git revision without changing the upstream checkout."""
import argparse, hashlib, json, subprocess
from pathlib import Path
p = argparse.ArgumentParser(description=__doc__)
p.add_argument("source", type=Path)
p.add_argument("--ref", default="origin/main")
a = p.parse_args()
root = Path(__file__).resolve().parent.parent
def git(*args):
    return subprocess.check_output(["git", "-C", str(a.source), *args])
sha = git("rev-parse", "--verify", a.ref + "^{commit}").decode().strip()
names = git("ls-tree", "-r", "--name-only", sha, "--", "skills", "references", "templates", "LICENSE").decode().splitlines()
previous = json.loads((root / "skills-source.json").read_text())
# Refuse to replace a modified upstream file; preserve local work.
for name, digest in previous["files"].items():
    path = root / name
    if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != digest:
        raise SystemExit("Local vendor change; review before sync: " + name)
data = {name: git("show", sha + ":" + name) for name in names}
for name in previous["files"].keys() - data.keys():
    (root / name).unlink()
for name, content in data.items():
    path = root / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(content)
previous.update(commit=sha, ref=a.ref, skillCount=sum(n.endswith("/SKILL.md") for n in names), files={n: hashlib.sha256(b).hexdigest() for n,b in data.items()})
(root / "skills-source.json").write_text(json.dumps(previous, indent=2) + "\n")
manifest = json.loads((root / "plugin.json").read_text())
manifest["skills"] = ["./skills/" + c["dir"] for c in json.loads((root / "skills/categories.json").read_text())["categories"]]
(root / "plugin.json").write_text(json.dumps(manifest, indent=2) + "\n")
print("Synced", previous["skillCount"], "skills from", sha, "— review diff, refresh SKILLS.md/counts, and validate.")
