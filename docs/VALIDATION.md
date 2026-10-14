# Validation status

- PASS 2026-10-14: manifest and marketplace metadata, 71 skill frontmatter/discovery checks, 158 upstream SHA-256 checks, square 512px logo, and both connection profiles.
- PASS: 148 Markdown files; 316 links, 123 anchors and 174 path mentions checked; zero broken references. The 55 cross-skill warnings refer to bundled siblings.
- PASS: selecting PAT and restoring OAuth both passed validation; final default is hosted OAuth.
- Hosted protected-resource discovery: verified 2026-10-14; resource https://mcp.harness.io/mcp, issuer https://id.harness.io/idp/realms/HarnessIDP.
- Antigravity CLI validation and component discovery: NOT RUN; agy is not installed on the build machine.
- HarnessID callback allowlist: NOT VERIFIED.
- Interactive OAuth sign-in and scoped authenticated API read: NOT RUN.
- PAT prompt, local server launch and authenticated API read: NOT RUN.
- Marketplace publication: NOT SUBMITTED.

Static checks validate packaging only. They do not establish runtime interoperability, permissions, hosted account enablement, or marketplace acceptance.
