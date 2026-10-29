# Establish roadmap Days 1–7 foundation

EngineerQuest was an empty repository. This batch establishes the first learning-loop
requirements, architecture and a reproducible local platform for subsequent implementation.

## Changes

- PRD with six measurable MVP stories, release map, local backlog and risk register.
- Research script, competitor investigation matrix, five participant slots and testable hypotheses.
- Modular-monolith/data-ownership ADRs and three cross-boundary workflow walkthroughs.
- Clickable low-fidelity HTML prototype and screen/state/accessibility/event matrix.
- Measurable quality scenarios, initial SLO candidates, privacy/retention and threat scope.
- Monorepo boundaries, CODEOWNERS, MIT license, templates, contributing guide, change/decision logs.
- Frozen Python/Node locks, local hooks and CI for Ruff, mypy, pytest, ESLint, TypeScript and Prettier.
- Compose PostgreSQL/Redis/mail/API/worker/collector stack; idempotent metadata seed and functional smoke.
- Minimal Expo shell with verified Android JavaScript export; no native app/device claim.

## Validation

See docs/evidence/batch-001.md and M01D01–M01D07.md. Local gates pass with 5 pytest tests.
All six services healthy. Real Redis outage/recovery, repeatable seed and mobile export pass.
All six quality gates rejected intentional temporary defects. Clean-clone verification is
recorded in the batch report. Remote Actions must pass before merging.

## Scope limits

Research recruitment/interviews, primary competitive observations and human usability
validation remain pending. Remote issue/milestone/Project setup requires working API access.
This PR does not implement auth, curriculum, production infrastructure or code execution.
No recurring daily job has been scheduled. Deprecation warnings remain in third-party tooling.

## Rollback

Revert feature changes and stop this project's Compose services. Database volume deletion
is only for disposable local development data. No production schema changes are included.
