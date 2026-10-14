# Harness workflows in Antigravity

Use the installed Harness MCP tools discovered in the current session. The plugin's server is namespaced as `harness-antigravity-harness`; tool display names may also be namespaced. Map upstream `harness_list`, `harness_get`, etc. to discovered tools, rather than inventing names or assuming availability.

Load the selected bundled SKILL.md before executing its workflow. Resolve skill-relative paths from that skill's directory; shared references live at `${PLUGIN_ROOT}/references`. Treat `/skill` and `/harness-category:skill` references as instructions to read the matching bundled workflow, not a requirement for a Claude-specific invocation tool.

Confirm account, organization and project scope before API operations. Follow the selected skill's write approval and validation requirements. Never broaden scope or switch credentials/transports to bypass a denial. Do not print or request tokens in chat.

For FME, read the applicable references plus `references/fme/tool-map.md`, `concepts.md`, and `write-safety.md` before writes. CLI support is limited to the verified operations declared by each skill. Hosted OAuth does not support legacy FME workspace credentials; use Harness-native scope where supported.

The upstream `configure-agent-pr-attestation` workflow targets Claude Code hooks. It is available as reference for configuring Claude Code projects, not as an implemented Antigravity hook. Do not install its hook into Antigravity or claim equivalent behavior.

Use read-only scoped calls for connection verification. Report actual tool/API results separately from drafts or generated YAML. No hooks run automatically in this plugin.
