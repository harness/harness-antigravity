# Validation status

- PASS 2026-10-14: manifest and marketplace metadata, 71 skill frontmatter/discovery checks, 158 upstream SHA-256 checks, square 512px logo, and both connection profiles.
- PASS: 148 Markdown files; 316 links, 123 anchors and 174 path mentions checked; zero broken references. The 55 cross-skill warnings refer to bundled siblings.
- PASS: selecting PAT and restoring OAuth both passed validation; final default is hosted OAuth.
- Hosted protected-resource discovery: verified 2026-10-14; resource https://mcp.harness.io/mcp, issuer https://id.harness.io/idp/realms/HarnessIDP.
- PASS 2026-10-20: `agy plugin validate .` (agy 1.4.3) with both profiles: 71 skills, 1 rule, 1 MCP server; 5 warnings. Warnings: `category` and `mcpServers` manifest fields reported as unknown/ignored (server is still discovered from mcp_config.json); root AGENTS.md is not loaded as a rule; dbops-changeset (30232 B) and exempt-vuln (26483 B) SKILL.md bodies exceed the 24000-byte load limit and are truncated.
- PASS 2026-10-20: `agy plugin install .` and `agy plugin list --json` (CLI only): 71 skills and 1 MCP server registered. In-app discovery not checked.
- HarnessID callback allowlist: NOT VERIFIED.
- Interactive OAuth sign-in and scoped authenticated API read: NOT RUN.
- PAT prompt: NOT VERIFIED. `agy plugin install .` with stdin closed did not prompt for `variables`; the installed mcp_config.json kept the `${HARNESS_API_KEY}`/`${HARNESS_BASE_URL}` placeholders unresolved. App install-modal behavior not tested.
- PASS 2026-10-20: PAT server launch and authenticated read, run outside Antigravity. `harness-mcp-v2@3.2.34` was started directly over stdio with a user-supplied PAT and `https://app.harness.io`: initialize OK, 11 tools; listed organizations (13) and projects; scoped execution list in sandbox/mansong returned 0 items with no error.
- Installed state 2026-10-20: reinstalled with the hosted OAuth profile (source and installed mcp_config.json identical).
- Marketplace publication: NOT SUBMITTED.

Static checks validate packaging only. They do not establish runtime interoperability, permissions, hosted account enablement, or marketplace acceptance.
