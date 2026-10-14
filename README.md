# Harness for Antigravity

Connect Antigravity to Harness to build and debug pipelines, manage deployments, investigate security findings, and use 71 bundled Harness workflows across nine categories.

## Install with hosted OAuth

This package defaults to `https://mcp.harness.io/mcp` with the public OAuth client `mcp-client`. No PAT or client secret is bundled. Hosted MCP must be enabled for your Harness account.

```sh
agy plugin validate /Users/rohangupta/code/harness-antigravity
agy plugin install /Users/rohangupta/code/harness-antigravity
agy plugin list --json
```

The paths above are local installation examples; the package itself is relocatable. Alternatively, use Antigravity's Customizations → Plugins → Install from URL/local path workflow from the publishing guide.

Authenticate the Harness server in Antigravity's Customizations settings. The HarnessID client must allow `https://antigravity.google/oauth-callback`, as required by Antigravity's OAuth documentation. This package cannot configure that server-side allowlist. If sign-in reports an invalid redirect, ask the HarnessID administrator to verify it; do not add a client secret to this public-client configuration.

Then provide your account, organization and project, and ask for a scoped read such as “List recent pipelines in this project.” A tool list or local schema lookup alone does not establish API access.

## Optional local/self-managed MCP with PAT

Before installation, select the PAT profile:

```sh
python3 scripts/select-connection.py local-pat
```

This runs `harness-mcp-v2@3.2.34` as a local stdio server using `npx`. Antigravity prompts for your PAT/SAT and Harness platform URL; for standard SaaS enter `https://app.harness.io`. The guide specifies keychain storage for secret variables. Supply credentials only through that UI. Node/npx is bundled with the Antigravity desktop app; standalone clients need it on PATH.

This profile connects the local MCP process directly to your selected Harness platform. It does not configure an existing remote HTTP MCP deployment. It requires network access to npm on first launch and the target Harness API. To return to OAuth:

```sh
python3 scripts/select-connection.py hosted-oauth
```

Select the profile in this source directory, then validate and install it. Do not edit Antigravity's read-only plugin cache. Only one profile is active; changing profiles never copies credentials.

## Included workflows

See [SKILLS.md](SKILLS.md) for all 71 workflows. Skills and shared references are copied unchanged from [harness/harness-skills](https://github.com/harness/harness-skills), with an exact revision and SHA-256 inventory in [skills-source.json](skills-source.json).

The Claude Code PR-attestation skill configures Claude Code, not Antigravity hooks. Some workflows require additional Harness modules, connectors, CLI tools or permissions as described in their prerequisites. Bundling a skill does not establish backend capability or access.

## Maintain and validate

```sh
python3 -m venv .venv
.venv/bin/pip install -r requirements-dev.txt
.venv/bin/python scripts/validate.py
```

Refresh from an already fetched local skills checkout (the script does not fetch or change that checkout):

```sh
python3 scripts/sync-skills.py ../harness-skills --ref origin/main
.venv/bin/python scripts/validate.py
```

Review changes and increment the plugin version before publishing an update. See [docs/PUBLISHING.md](docs/PUBLISHING.md) and [docs/VALIDATION.md](docs/VALIDATION.md) for remaining release checks. This source package has not been installed, authenticated, or submitted to the marketplace. Source repository: https://github.com/thisrohangupta/harness-antigravity (private).
