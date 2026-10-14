# Harness Antigravity plugin development

Target the user-provided Antigravity Plugin Marketplace Publishing Guide. The root plugin.json is the Antigravity manifest; do not generate Codex/Cursor manifests here.

Skills and shared references are vendored unchanged from the revision in skills-source.json. Preserve category directories and relative links. Update via scripts/sync-skills.py, review the upstream diff, then run scripts/validate.py. Developer validation needs Python 3 and requirements-dev.txt; runtime hosted OAuth needs neither.

Keep credentials out of the repository. Connection profiles are templates with one active server; do not enable both profiles simultaneously. Use the guide's variables array for PAT prompts.

Before publishing: run agy plugin validate, install locally, verify all skills are discovered, complete OAuth and a scoped read, and fill in docs/VALIDATION.md. Do not claim marketplace acceptance or authenticated success from static validation.
