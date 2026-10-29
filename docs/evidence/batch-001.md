# Batch 001 — roadmap Days 1–7

Execution date: 2026-10-30 (Asia/Kolkata). Branch: feat/roadmap-days-01-07.
Source: user-provided production roadmap, preserved at docs/roadmap.md.

## Outcome

Foundation documents and a functioning local development stack are delivered. This batch
is **partially complete against all roadmap shipping criteria**: no research participants
were recruited, interviews conducted, external board created, human usability study run,
or remote CI/PR completed. No product authentication or production deployment is claimed.

## Delivered

| Day | Artifacts                                                                         | Evidence / limitation                                             |
| --- | --------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| 1   | PRD, measurable stories, release map, risk register, local board                  | M01D01.md; remote milestone/Project pending                       |
| 2   | Interview script, five recruitment slots, competitor matrix, hypotheses           | M01D02.md; no observed findings or recruited participants         |
| 3   | Domain context diagram, modular-monolith and data-ownership ADRs                  | M01D03.md; three boundary walkthroughs                            |
| 4   | Clickable HTML prototype, journey/state/event matrix                              | M01D04.md; desk review only                                       |
| 5   | SLO candidates, threat scope, privacy, recovery and cost targets                  | M01D05.md; targets are not production measurements                |
| 6   | Monorepo, locks, templates, CODEOWNERS, license, contributing guide, hooks, CI    | M01D06.md; local gates pass, remote CI unrun                      |
| 7   | PostgreSQL, Redis, Mailpit, API probe, heartbeat worker, collector and Expo shell | M01D07.md; functional local checks pass, native device test unrun |

## Validation executed

- `make bootstrap`: frozen uv and npm installation; repeat installation passes.
- `make check doctor`: Ruff, strict mypy, pytest **5 passed**, ESLint, contracts/mobile
  TypeScript, Prettier and tool/Docker checks pass. One third-party Starlette/AnyIO
  deprecation warning; npm reports deprecated transitive tooling packages.
- `docker compose -f compose.yaml -f compose.cloud.yaml up --build --wait --wait-timeout 180`:
  clean disposable volume startup succeeds; all six services healthy.
- `make smoke`: real API liveness and dependency readiness, Mailpit endpoint, seeded
  PostgreSQL metadata, expiring worker heartbeat, collector HTTP health pass.
- `docker compose exec -T postgres psql -U engineerquest -d engineerquest -f /docker-entrypoint-initdb.d/001-init.sql`:
  second seed application succeeds without duplicates.
- Redis outage experiment: `docker compose stop redis`; liveness remains 200, readiness
  becomes 503 with generic response. Redis and worker restarted; all services recover and smoke passes.
- `CI=1 npm exec -w @engineerquest/mobile -- expo export --platform android --output-dir /tmp/engineerquest-mobile-export`:
  succeeds, 570 modules, one Android Hermes bundle. This is not a native build/device run.
- Temporary defects were inserted and removed: Ruff exit 1; mypy exit 1; pytest exit 1;
  ESLint exit 1; TypeScript exit 2; Prettier exit 1. Each expected failure was observed.
- Clean-clone bootstrap: `git clone --no-hardlinks /workspace/EngineerQuest /tmp/engineerquest-clean-batch001`, then `make bootstrap check doctor` in that clone: passed, including all 5 pytest tests. This validates a clean local Git checkout, not restoration into a newly published cloud runtime.

## Failures diagnosed and corrected

Initial Python lint failed on formatting/imports; fixed and rerun. Strict mypy needed
Redis stubs; pinned stubs added, no assertions disabled. Container startup failed because
cloud-created source/config files were private to their owner: bind-mounted configs made
readable and Dockerfile grants non-root users read/execute access to copied service code.
Only this newly created project's disposable data volume was reset for a clean rebuild.
Expo's hoisted default entry resolved the wrong App path: replaced with explicit local
index.ts. Bundle subsequently succeeded. TLS/signature/checksum validation remained enabled.

## External blockers and next steps

Git read/push works using platform HTTPS authentication outside the command sandbox.
GitHub API returns Forbidden. An additive api.github.com allowlist entry was saved in the
environment draft; it is not proof of applied access or sufficient API authorization.
Until the required API operation succeeds, issues, milestone, Project, PR and merge remain
pending. Review/save network settings and publish the environment as required by the UI;
then recheck access before assuming it works. No new token has been requested.

Future daily execution is not scheduled: no scheduler capability is attached to this chat.
Each subsequent session can take the next seven roadmap days; do not mark blocked research
criteria done merely because a new batch begins.

## Risk and rollback

Local-only credentials and unauthenticated health endpoints are development scaffolding.
No production security audit, load test, native app verification or deployment was performed.
Remove the batch by reverting its feature changes and stopping the engineerquest Compose
project. `down -v` destroys local data; never use against existing valuable databases.

## Saved environment configuration

Saved install_script (`make bootstrap` in /workspace/EngineerQuest) and start_skill (Compose cloud startup, readiness smoke, mobile instructions and isolation guidance). The api.github.com network addition is saved for review. Draft persistence is confirmed; publication and fresh-runtime restoration have not been performed.
