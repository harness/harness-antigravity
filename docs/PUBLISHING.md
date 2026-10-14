# Publishing handoff

The supplied Antigravity Plugin Marketplace Publishing Guide is the manifest authority for this package. It supports marketplace fields and custom skill roots. The public plugins documentation currently shows a narrower manifest schema, so this package deliberately does not advertise that JSON schema as its validator. Confirm against the publisher's target Antigravity build with `agy plugin validate .`.

1. Run `python3 scripts/validate.py`, then `agy plugin validate .` in the target Antigravity version.
2. Install locally. Verify 71 skills across nine roots and one Harness server are discovered. Confirm logo appearance on light/dark themes.
3. Verify the HarnessID `mcp-client` allows Antigravity's callback. Complete OAuth and a read in an explicitly selected project. Record the result in VALIDATION.md.
4. Separately test the PAT profile if distributing it; confirm the credential prompt and a scoped read. Restore the intended published default afterward.
5. Review upstream workflow prerequisites, especially the Claude-specific attestation skill. Resolve any validator or discovery differences before submission.
6. Source repository: https://github.com/thisrohangupta/harness-antigravity (private). Confirm repository visibility and publisher ownership requirements before marketplace submission.
7. Submit through the marketplace publisher process provided by Google. The supplied guide describes packaging and local validation but does not specify a submission endpoint or review SLA.
8. Increment version for each subsequent published update.

Sources:
- User-provided Antigravity Plugin Marketplace Publishing Guide.pdf, read 2026-10-14.
- https://www.antigravity.google/docs/mcp (OAuth `clientId`, remote `serverUrl`, callback).
- https://www.antigravity.google/docs/plugins (installation and CLI).
- https://github.com/harness/mcp-server (hosted enablement and public OAuth client).
