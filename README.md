# Harness for Antigravity

Connect Antigravity to Harness with hosted MCP and 71 bundled workflow skills for pipelines, deployments, security, feature flags, and platform operations.

## Install using the Antigravity app

1. Open **Customizations** in Antigravity's left sidebar.
2. Select **Plugins**.
3. Click **+ Install from URL**.
4. Enter this repository URL:

   ```text
   https://github.com/harness/harness-antigravity.git
   ```

5. Follow the installation prompts, then check **Installed** for **Harness**.

You can also install from a local path:

```sh
git clone https://github.com/harness/harness-antigravity.git
cd harness-antigravity
```

Enter the full path of that checkout in the app's local-path installation flow, selecting the folder containing `plugin.json`.

## Connect to Harness

The default [MCP configuration](mcp_config.json) uses:

- Endpoint: `https://mcp.harness.io/mcp`
- OAuth client ID: `mcp-client`

Hosted MCP must be enabled for your Harness account. The profile does not contain a PAT or client secret.

To sign in, open **Settings → Customizations**, find the Harness MCP server, select **Authenticate**, and complete the browser authorization prompts. See Google's [MCP authentication documentation](https://www.antigravity.google/docs/mcp) for details.

## Try it

Provide your Harness scope and try a read-only request:

```text
In Harness account <account>, organization <org>, project <project>,
list the five most recent pipeline executions and summarize their status.
Do not make changes.
```

## CLI installation

From a local checkout:

```sh
agy plugin validate .
agy plugin install .
agy plugin list
```

Or directly from the repository URL:

```sh
agy plugin install https://github.com/harness/harness-antigravity.git
```

See the [Antigravity plugin documentation](https://www.antigravity.google/docs/plugins) for more CLI options.

## Optional PAT profile

This repository includes an alternative [local PAT configuration](config/local-pat.json). It launches `harness-mcp-v2@3.2.34` through `npx` as a local stdio process that connects to your Harness platform.

Before installing a local checkout, select the profile:

```sh
python3 scripts/select-connection.py local-pat
```

Then install that checkout using one of the local installation methods above. Antigravity prompts for two values during installation:

| Input | Value |
| --- | --- |
| Harness API key | A PAT or SAT with access to the intended resources |
| Harness platform URL | `https://app.harness.io` or your Harness environment's HTTPS base URL |

Do not put credentials in chat or commit them to the repository.

This profile needs Node/npx and access to npm and the Harness API. Python 3 is needed only for the profile-selection helper. To restore the OAuth configuration:

```sh
python3 scripts/select-connection.py hosted-oauth
```

## Included workflows

See [SKILLS.md](SKILLS.md) for the 71 workflows. Skills, references, and templates are copied from [harness/harness-skills](https://github.com/harness/harness-skills); [skills-source.json](skills-source.json) records the exact revision and file hashes.

The `configure-agent-pr-attestation` skill targets Claude Code hooks, not Antigravity hooks. Other workflows may require additional Harness modules, connectors, tools, and permissions stated in their prerequisites.

## Development

```sh
python3 -m venv .venv
.venv/bin/pip install -r requirements-dev.txt
.venv/bin/python scripts/validate.py
```

To refresh skills from a local harness-skills checkout:

```sh
python3 scripts/sync-skills.py /path/to/harness-skills --ref origin/main
.venv/bin/python scripts/validate.py
```

See [publishing notes](docs/PUBLISHING.md) before release.

## Resources

- [Antigravity plugins](https://www.antigravity.google/docs/plugins)
- [Antigravity MCP authentication](https://www.antigravity.google/docs/mcp)
- [harness/mcp-server](https://github.com/harness/mcp-server)
