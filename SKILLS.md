# Bundled Harness workflows

Source: `bc2236daceeaffec358d9276806820b3ec441eef`. All 71 skill files are unchanged from upstream.

## Harness Pipelines & Execution

| Skill | Description |
| --- | --- |
| [create-pipeline](skills/pipelines/create-pipeline/SKILL.md) | Generate v0 pipeline YAML (CI, CD, combined, approvals) |
| [create-pipeline-v1](skills/pipelines/create-pipeline-v1/SKILL.md) | Generate v1 simplified pipeline YAML |
| [create-template](skills/pipelines/create-template/SKILL.md) | Create reusable step, stage, pipeline, and step group templates |
| [create-trigger](skills/pipelines/create-trigger/SKILL.md) | Create webhook, scheduled, and artifact triggers |
| [debug-pipeline](skills/pipelines/debug-pipeline/SKILL.md) | Diagnose pipeline execution failures |
| [manage-freeze-windows](skills/pipelines/manage-freeze-windows/SKILL.md) | Create, toggle, and manage deployment freeze windows and the project-level global freeze |
| [migrate-pipeline](skills/pipelines/migrate-pipeline/SKILL.md) | Convert v0 pipelines to v1 format |
| [run-pipeline](skills/pipelines/run-pipeline/SKILL.md) | Execute and monitor pipeline runs |

## Harness Infrastructure & Resources

| Skill | Description |
| --- | --- |
| [create-connector](skills/infrastructure/create-connector/SKILL.md) | Create connectors (GitHub, AWS, GCP, Azure, Docker, K8s) |
| [create-environment](skills/infrastructure/create-environment/SKILL.md) | Create environments (PreProduction, Production) with overrides |
| [create-infrastructure](skills/infrastructure/create-infrastructure/SKILL.md) | Define infrastructure (K8s, ECS, Serverless) |
| [create-secret](skills/infrastructure/create-secret/SKILL.md) | Manage secrets (SecretText, SecretFile, SSHKey, WinRM) |
| [create-service](skills/infrastructure/create-service/SKILL.md) | Define services (Kubernetes, Helm, ECS) with artifact sources |

## Harness Access Control & Users

| Skill | Description |
| --- | --- |
| [manage-roles](skills/access-control/manage-roles/SKILL.md) | RBAC roles, assignments, permissions, and resource groups |
| [manage-users](skills/access-control/manage-users/SKILL.md) | Manage users, user groups, and service accounts |

## Harness FME (Feature Flags & Experimentation)

| Skill | Description |
| --- | --- |
| [choose-metric](skills/fme/choose-metric/SKILL.md) | Recommend primary/guardrail metrics for an experiment or rollout, judged against a good-metric checklist |
| [cleanup-feature-flags](skills/fme/cleanup-feature-flags/SKILL.md) | Remove a launched FME flag from code and open a PR; archive is handed to manage-flag-lifecycle |
| [create-experiment](skills/fme/create-experiment/SKILL.md) | Creation-only entry point to the manage-experiments workflow |
| [create-feature-flag](skills/fme/create-feature-flag/SKILL.md) | Create an FME flag that follows project conventions, with safe-default definitions |
| [create-metric](skills/fme/create-metric/SKILL.md) | Design and create an FME metric, with intent-to-config guidance, traffic type, events, cap, and owners |
| [discover-feature-flags](skills/fme/discover-feature-flags/SKILL.md) | Inventory, targeting-pattern search, promotion-aware rollout report, and stale-flag audit (read-only) |
| [explain-flag](skills/fme/explain-flag/SKILL.md) | Explain one flag's purpose, treatments, and per-environment targeting, flagging inconsistencies (read-only) |
| [feature-flag-onboarding](skills/fme/feature-flag-onboarding/SKILL.md) | Set up and verify a first feature flag in an existing project; resume partial onboarding |
| [fme-pipeline](skills/fme/fme-pipeline/SKILL.md) | Generate FME pipelines for rollout scenarios, gates, and flag lifecycle |
| [instrument-feature-flag](skills/fme/instrument-feature-flag/SKILL.md) | Gate application code through an extensible flag abstraction, after stack detection and clarification |
| [instrument-metric](skills/fme/instrument-metric/SKILL.md) | Wire up a track() call for a metric's event, placed at the real outcome, and verify it arrives |
| [manage-experiments](skills/fme/manage-experiments/SKILL.md) | Feature-flag experiment design/lifecycle; delegates metrics and states CLI update limitations |
| [manage-flag-lifecycle](skills/fme/manage-flag-lifecycle/SKILL.md) | Flag metadata, archive readiness, archive/unarchive, and delete |
| [manage-segments](skills/fme/manage-segments/SKILL.md) | Segment metadata, STANDARD membership, and RULE_BASED editor workflows with mandatory pre-write reference checks |
| [review-experiment-results](skills/fme/review-experiment-results/SKILL.md) | Explain experiment results, including winner, significance, guardrail impact, and data-quality caveats |
| [update-flag-targeting](skills/fme/update-flag-targeting/SKILL.md) | Ramp, rules, individual targets, allocation, treatments, kill/restore, env-to-env copy, and initializing definitions |

## Harness Database DevOps

| Skill | Description |
| --- | --- |
| [dbops-changeset](skills/database/dbops-changeset/SKILL.md) | Generate, refine, review, and execute Liquibase changesets with Harness DBOPS |

## Harness Platform Operations

| Skill | Description |
| --- | --- |
| [create-sbom](skills/platform/create-sbom/SKILL.md) | Add SBOM Orchestration (generation/attestation) to existing pipelines |
| [enforce-sbom](skills/platform/enforce-sbom/SKILL.md) | Add SBOM Policy Enforcement (verify attestation + OPA policy sets) |
| [manage-artifacts](skills/platform/manage-artifacts/SKILL.md) | Artifact registry setup, security scanning, and cross-region replication |
| [manage-cde](skills/platform/manage-cde/SKILL.md) | Cloud development environments, workspace templates, and auto-hibernation |
| [manage-delegates](skills/platform/manage-delegates/SKILL.md) | Monitor delegate health and manage registration tokens |
| [manage-iacm](skills/platform/manage-iacm/SKILL.md) | Terraform workspaces, drift detection, cost estimation, and approval workflows |
| [manage-pull-requests](skills/platform/manage-pull-requests/SKILL.md) | List, create, update, merge, review, and comment on Harness Code pull requests |
| [manage-supply-chain](skills/platform/manage-supply-chain/SKILL.md) | SBOM generation, artifact signing, and supply chain policy enforcement |

## Harness Security Testing & Supply Chain

| Skill | Description |
| --- | --- |
| [approve-exempt](skills/security/approve-exempt/SKILL.md) | Approve pending STO exemptions at current scope or elevate to Project, Org, or Account |
| [configure-agent-pr-attestation](skills/security/configure-agent-pr-attestation/SKILL.md) | Install and configure the Claude Code PR attestation hook for signed in-toto attestations to the Harness Evidence Vault |
| [configure-container-scan](skills/security/configure-container-scan/SKILL.md) | Add container image scanning to pipelines using Harness STO scanners (Trivy, Grype, Snyk, and more) |
| [configure-dast-scan](skills/security/configure-dast-scan/SKILL.md) | Add DAST scanning to pipelines for runtime application security testing (Traceable, Burp Suite, ZAP, Nikto, Nmap) |
| [configure-repo-scan](skills/security/configure-repo-scan/SKILL.md) | Configure code scanning in pipelines with STO security scanners |
| [configure-secret-scan](skills/security/configure-secret-scan/SKILL.md) | Add secret detection scanning to pipelines to find exposed credentials and API keys (Gitleaks, Semgrep, Snyk, and more) |
| [enforce-slsa](skills/security/enforce-slsa/SKILL.md) | Add SLSA Verification (verify attestation + OPA policy sets on provenance) to pipelines |
| [exempt-vuln](skills/security/exempt-vuln/SKILL.md) | Create STO vulnerability exemptions (waivers) scoped to Project, Pipeline, or Target |
| [generate-slsa](skills/security/generate-slsa/SKILL.md) | Add SLSA Generation (provenance + optional Cosign attestation) to existing pipelines |
| [sign-artifact](skills/security/sign-artifact/SKILL.md) | Add Artifact Signing (Cosign sign + optional .sig upload) to existing pipelines (SSCA) |
| [verify-sign](skills/security/verify-sign/SKILL.md) | Add Artifact Verification (verify Cosign signature) to existing pipelines (SSCA) |

## Harness Observability & Governance

| Skill | Description |
| --- | --- |
| [ai-operations](skills/observability-governance/ai-operations/SKILL.md) | Predictive failure analysis and intelligent alert correlation (AIDA) |
| [analyze-costs](skills/observability-governance/analyze-costs/SKILL.md) | Cloud cost analysis, recommendations, and anomaly detection |
| [audit-report](skills/observability-governance/audit-report/SKILL.md) | Audit trails and compliance evidence (SOC2, GDPR, HIPAA) |
| [chaos-dr-test](skills/observability-governance/chaos-dr-test/SKILL.md) | Create and edit DR Test pipelines with chaos steps |
| [chaos-experiment](skills/observability-governance/chaos-experiment/SKILL.md) | Create, edit, and reference chaos experiments (faults, probes, actions) |
| [create-policy](skills/observability-governance/create-policy/SKILL.md) | Create OPA governance policies for supply chain security |
| [deployment-readiness](skills/observability-governance/deployment-readiness/SKILL.md) | Pre-deployment readiness checks, environment drift, and canary decisions |
| [dora-metrics](skills/observability-governance/dora-metrics/SKILL.md) | DORA metrics and engineering performance reports |
| [gitops-status](skills/observability-governance/gitops-status/SKILL.md) | GitOps application health, sync status, and pod logs |
| [incident-response](skills/observability-governance/incident-response/SKILL.md) | Deployment-incident correlation, blast radius analysis, and postmortems |
| [manage-idp](skills/observability-governance/manage-idp/SKILL.md) | Service catalog, self-service workflows, documentation, and developer onboarding (IDP) |
| [manage-slos](skills/observability-governance/manage-slos/SKILL.md) | SLO definition, error budgets, incident detection, and operational runbooks |
| [optimize-pipeline](skills/observability-governance/optimize-pipeline/SKILL.md) | Pipeline speed optimization, parallel testing, caching, and monorepo builds |
| [pr-analysis](skills/observability-governance/pr-analysis/SKILL.md) | PR pipeline impact, security review, and PR-to-production tracking |
| [scorecard-review](skills/observability-governance/scorecard-review/SKILL.md) | IDP scorecards and service maturity review |
| [security-report](skills/observability-governance/security-report/SKILL.md) | Security vulnerabilities, SBOMs, and compliance reports |
| [sei-analytics](skills/observability-governance/sei-analytics/SKILL.md) | Sprint analytics, investment allocation, capacity forecasting, and release readiness |
| [template-usage](skills/observability-governance/template-usage/SKILL.md) | Template dependency tracking, impact analysis, and adoption |

## Harness AI Agents

| Skill | Description |
| --- | --- |
| [create-agent](skills/agents/create-agent/SKILL.md) | Create and update Harness AI agent instances for agentic pipeline workflows |
| [create-agent-template](skills/agents/create-agent-template/SKILL.md) | Generate AI agent templates (metadata.json, pipeline.yaml, wiki.MD) |
