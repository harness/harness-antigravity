# Harness for Antigravity

Connect Antigravity to Harness to build and debug pipelines, manage deployments, investigate security findings, and use 71 bundled Harness workflows across nine categories.

## Install in Antigravity

### 1. Get the plugin

You need Antigravity with plugin support and access to this **private GitHub repository**. GitHub access and Harness authentication are separate: cloning the repository does not sign you in to Harness.

Clone using an authenticated Git client. With the [GitHub CLI](https://cli.github.com/):

```sh
gh auth login
gh repo clone thisrohangupta/harness-antigravity
cd harness-antigravity
```

If you already have a checkout, open that directory instead. On the original development machine it is `/Users/rohangupta/code/harness-antigravity`.

### 2. Install the local folder

From the checkout, with `agy` available in your terminal:

```sh
agy plugin validate .
agy plugin install .
agy plugin list --json
```

In the app, you can instead open **Customizations → Plugins**, choose **+ Install from URL**, and select/enter the local checkout path if your build offers local-path installation. Select the folder containing `plugin.json`. Cloning first avoids relying on the app's GitHub authentication for a private URL.

See [Antigravity plugin installation](https://www.antigravity.google/docs/plugins) for supported installation surfaces. If `agy` is not found, use the app flow or follow the [CLI installation guide](https://www.antigravity.google/docs/cli/install/). If validation rejects marketplace fields or custom skill roots, check the target build's publishing-guide support; do not remove fields blindly. See [publishing compatibility notes](docs/PUBLISHING.md).

### 3. Connect Harness with OAuth (default)

The default profile connects to `https://mcp.harness.io/mcp` using the public OAuth client `mcp-client`. Hosted MCP must be enabled for your Harness account; no API key or client secret is needed in this profile.

1. Open Antigravity **Settings → Customizations**.
2. Find the plugin's Harness MCP server (`harness-antigravity-harness`) and select **Authenticate**.
3. Complete Harness sign-in in your browser and follow Antigravity's prompts to finish authorization.
4. Confirm the server connects, then provide your Harness account, organization and project.

HarnessID must allow `https://antigravity.google/oauth-callback` for `mcp-client`. If you see an invalid redirect error, ask the HarnessID administrator to verify this allowlist. Do not add a client secret to this public-client configuration. See [Antigravity OAuth setup](https://www.antigravity.google/docs/mcp).

### 4. Verify the installation

Confirm the plugin is enabled and exposes **71 skills** and **one MCP server**. Try this read-only prompt with your actual scope:

```text
In Harness account <account>, organization <org>, project <project>,
list the five most recent pipeline executions and summarize their status.
Do not make changes.
```

You can also select `/debug-pipeline` or `/create-pipeline` from skill autocomplete. A successful scoped API read verifies access; seeing skills or tool schemas alone does not. Installation and signed-in operation have not yet been tested for this package; see [validation status](docs/VALIDATION.md).

## Alternative: local MCP with a PAT

Use this profile when you want a local MCP process connecting directly to Harness SaaS or your own Harness environment. It does not configure an existing remote HTTP MCP deployment.

From the cloned source folder, **before installing**, run:

```sh
python3 scripts/select-connection.py local-pat
agy plugin validate .
agy plugin install .
```

During setup, supply the prompted values:

| Setting | Value |
| --- | --- |
| Harness API key | Your PAT or SAT with permission for the intended resources |
| Harness platform URL | `https://app.harness.io`, or your Harness environment's HTTPS base URL |

Enter the token only in Antigravity's credential UI, not in chat or committed files. This profile launches `npx -y harness-mcp-v2@3.2.34 stdio`; it needs Node/npx and network access to npm and Harness. The publishing guide specifies bundled Node/npx in the desktop app and keychain storage for secret variables. Python 3 is only needed to select the profile.

If the plugin is already installed, change the profile in the source checkout and reinstall that local folder; confirm only one Harness server is enabled. Never edit the installed cache. To return to OAuth:

```sh
python3 scripts/select-connection.py hosted-oauth
agy plugin validate .
agy plugin install .
```

After either setup, repeat the scoped read above.

## Troubleshooting

| Symptom | Next step |
| --- | --- |
| GitHub says repository not found | Confirm your GitHub identity has access to this private repository; clone locally before installing. |
| Skills or server do not appear | Confirm the plugin is enabled and the installed folder contains `plugin.json`; inspect `agy plugin list --json` and reopen the conversation. |
| OAuth reports invalid redirect | Have the HarnessID administrator verify the Antigravity callback for `mcp-client`. |
| Harness returns 401 | Reauthenticate OAuth, or check the PAT entered through the credential UI for the PAT profile. |
| Harness returns 403 | Check the selected account/org/project and your Harness RBAC permissions. |
| PAT server cannot start | Check Node/npx availability and npm access; inspect Antigravity's MCP logs without sharing credentials. |


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
