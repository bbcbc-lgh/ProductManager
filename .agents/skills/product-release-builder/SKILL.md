---
name: product-release-builder
description: Select a release target, perform privacy and release-readiness audits, and create reproducible packaging and release evidence. Use after planned implementation phases are accepted and the user wants to ship.
---

# Product Release Builder

## Use when

Use after the required implementation phases pass their gates. First inspect the repository and present the release types it can realistically support, such as web deployment, desktop installer, mobile package, CLI distribution, library/package registry, container image, or static artifact. Ask the user to choose before packaging.

## Good output

For the selected target, create the release report from `.codex/agents/templates/RELEASE.md`. Cover build reproducibility, environment configuration, secrets, permissions, telemetry, personal-data collection and retention, third-party services, dependencies/licenses, user-facing privacy disclosures, rollback, and smoke verification. Create the package or deployment artifact and record exact commands, hashes where applicable, and a clean release checklist.

## Red lines

- Do not publish without an explicit target and owner-approved release decision.
- Do not expose secrets, personal data, debug endpoints, or development credentials in artifacts.
- Do not claim privacy compliance from a checklist alone; identify evidence and unknowns.
- Do not alter production or external systems without explicit authorization.
