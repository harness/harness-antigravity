# Harness for Antigravity

Connect Antigravity to Harness with hosted MCP and 71 bundled workflow skills for pipelines, deployments, security, feature flags, and platform operations.

## Install using the Antigravity app

The following app flow comes from the **Antigravity Plugin Marketplace Publishing Guide**, Part 1, “Managing Plugins by Surface.” It has not yet been tested end to end with this plugin.

1. Open **Customizations** in Antigravity's left sidebar.
2. Select **Plugins**.
3. Click **+ Install from URL**.
4. Enter this repository URL:

   ```text
   https://github.com/harness/harness-antigravity.git
   ```

5. Follow the installation prompts, then check **Installed** for **Harness**.

The guide also supports installing from a local path. To obtain a local copy:

```sh
git clone https://github.com/harness/harness-antigravity.git
cd harness-antigravity
```

Enter the full path of that checkout in the app's local-path installation flow. Select the folder containing `plugin.json`. If GitHub requires authentication, use an account with access to the repository; this is separate from Harness sign-in.

## Connect to Harness

The default [MCP configuration](mcp_config.json) uses:

- Endpoint: `https://mcp.harness.io/mcp`
- OAuth client ID: `mcp-client`

Hosted MCP must be enabled for your Harness account. The profile does not contain a PAT or client secret.

The publishing guide mentions OAuth support but does not describe the sign-in screens. Google's [MCP authentication documentation](https://www.antigravity.google/docs/mcp) provides that procedure: open **Settings → Customizations**, find the MCP server, select **Authenticate**, and complete the browser authorization prompts.

That documentation lists `https://antigravity.google/oauth-callback` as the required redirect for manually configured OAuth clients. The HarnessID administrator must confirm that `mcp-client` permits it. **The callback allowlist and successful sign-in for this plugin have not been verified.** If authentication fails, record the error before changing configuration.

## Check that it works

The package contains **71 skills** and **one MCP server**. Check what Antigravity actually discovers after installation. Then provide your Harness scope and try a read-only request:

```text
In Harness account <account>, organization <org>, project <project>,
list the five most recent pipeline executions and summarize their status.
Do not make changes.
```

A successful API response verifies that read in the selected scope. The presence of skill files, a server entry, or a local schema response does not establish authenticated access. See [validation status](docs/VALIDATION.md) for checks completed so far.

## CLI installation from a local clone

These commands are specified in the supplied publishing guide, Part 1, “Step 3: Validate & Install Locally.” Run them from the checkout with a version of `agy` that supports those commands:

```sh
agy plugin validate .
agy plugin install .
agy plugin list
```

The public [Antigravity plugin documentation](https://www.antigravity.google/docs/plugins) separately documents CLI installation from a repository URL:

```sh
agy plugin install https://github.com/harness/harness-antigravity.git
```

The public reference currently shows a narrower manifest schema than the supplied marketplace guide. This package follows the supplied guide, including marketplace metadata and category-specific skill roots. If your installed CLI rejects the manifest or lacks `plugin validate`, check the supported Antigravity version with the publisher; do not treat the package's Python validator as equivalent to native CLI validation.

## Optional PAT profile

This repository includes an alternative [local PAT configuration](config/local-pat.json). It launches `harness-mcp-v2@3.2.34` through `npx` as a local stdio process that connects to your Harness platform. It is not a connection profile for an existing remote HTTP MCP server.

Before installing a local checkout, select the profile using this repository's helper:

```sh
python3 scripts/select-connection.py local-pat
```

Then install that checkout using one of the local installation methods above. The configuration declares two inputs:

| Input | Value |
| --- | --- |
| Harness API key | A PAT or SAT with access to the intended resources |
| Harness platform URL | `https://app.harness.io` or your Harness environment's HTTPS base URL |

The publishing guide, Part 2 §3.2, describes an installation configuration modal for declared variables and OS-keychain storage for secret values. This profile uses that format, but the prompt and token storage have not been tested in Antigravity. Do not put credentials in chat or commit them to the repository.

This profile needs Node/npx and access to npm and the Harness API. Python 3 is needed only for the profile-selection helper. To restore the source checkout's OAuth configuration before installation:

```sh
python3 scripts/select-connection.py hosted-oauth
```

Changing the source file does not itself update an installed plugin. Installed-plugin profile switching and reinstall behavior have not been verified. Do not edit the installed cache or assume that rerunning an install command replaces the active configuration.

## Included workflows

See [SKILLS.md](SKILLS.md) for the 71 workflows. Skills, references, and templates are copied from [harness/harness-skills](https://github.com/harness/harness-skills); [skills-source.json](skills-source.json) records the exact revision and file hashes.

The `configure-agent-pr-attestation` skill targets Claude Code hooks, not Antigravity hooks. Other workflows may require additional Harness modules, connectors, tools, and permissions stated in their prerequisites.

## Developer validation

Static packaging checks:

```sh
python3 -m venv .venv
.venv/bin/pip install -r requirements-dev.txt
.venv/bin/python scripts/validate.py
```

To refresh skills from a fetched local source checkout, substitute its actual path:

```sh
python3 scripts/sync-skills.py /path/to/harness-skills --ref origin/main
.venv/bin/python scripts/validate.py
```

Static checks cover package structure, skill metadata, reference links, and recorded upstream hashes. They do not prove Antigravity installation, OAuth/PAT interoperability, or marketplace acceptance. See [publishing notes](docs/PUBLISHING.md) and [validation status](docs/VALIDATION.md) before release.

## Sources and verification status

- **Supplied publishing guide:** *Antigravity Plugin Marketplace Publishing Guide.pdf*, Part 1 (app/local installation and CLI validation) and Part 2 §3.2 (MCP configuration and variable prompts). This guide was supplied to the maintainers; it is not bundled here.
- **Public Google documentation:** [Plugins](https://www.antigravity.google/docs/plugins) and [MCP authentication](https://www.antigravity.google/docs/mcp). These describe general client behavior, not a successful test of this plugin.
- **Harness server:** [harness/mcp-server](https://github.com/harness/mcp-server), for hosted enablement and OAuth configuration.

Antigravity installation, skill discovery in the app, interactive authentication, and authenticated Harness calls remain unverified. The plugin has not been submitted to the Antigravity marketplace.
