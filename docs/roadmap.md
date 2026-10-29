# EngineerQuest Production Engineering Roadmap

## 360 execution days to build and launch a company-grade learning platform

> **Outcome:** one deployable, observable, secure, tested product - not 12 disconnected tutorial projects. EngineerQuest becomes a gamified mobile learning platform for software engineers with learning worlds, executable challenges, progression, an AI mentor, an admin system, analytics, subscriptions, and a documented production launch.
>
> **Portfolio honesty:** describe this as an independently engineered product or open-source/startup project. Do not describe it as professional employment unless it actually becomes one.

## What “production level” means in this roadmap

Every feature must have an owner-facing requirement, an API or event contract, persistent data rules, authorization, failure behavior, tests, observability, documentation, and a rollback or disable path. “The happy path worked on my laptop” is not an acceptance criterion.

### Final product surface

- **Learner mobile app:** onboarding, skill tree, lessons, simulators, quests, streaks, XP, achievements, leaderboards, subscriptions, notifications, offline-safe progress, accessibility, and AI mentor.
- **Curriculum platform:** Git, Linux, SQL, DSA, Debugging, Networking, Security, Cloud, and DevOps worlds with versioned content and boss battles.
- **Admin web app:** curriculum authoring, preview, publishing, cohort analytics, moderation, feature flags, support tooling, and audit history.
- **Backend platform:** authenticated APIs, progression engine, entitlement service, content delivery, challenge execution, analytics events, background jobs, AI orchestration, and operational endpoints.
- **Production system:** infrastructure as code, CI/CD, staged environments, secrets, backups, dashboards, alerts, incident runbooks, privacy controls, app-store builds, and release management.

## Deliberate architecture

Start as a **modular monolith plus isolated workers**, not premature microservices. Keep domain boundaries explicit so high-risk components - code execution, notifications, analytics ingestion, and AI workloads - can be separated later without rewriting the product.

| Layer               | Chosen tools                                                                                                                            | Why they exist                                                                                                          |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| Mobile              | React Native, Expo, TypeScript, Expo Router, TanStack Query, Zustand, React Hook Form, Zod                                              | Cross-platform delivery, typed navigation and contracts, explicit separation of server state and local UI state         |
| Admin               | Next.js, TypeScript, TanStack Query, a small shared design system                                                                       | Server-capable operations UI, fast internal workflows, reusable types and components                                    |
| API                 | FastAPI, Pydantic, SQLAlchemy, Alembic, uv, Ruff, mypy, pytest                                                                          | Typed contracts, async Python services, reproducible packaging, migrations, and enforceable quality gates               |
| Data                | PostgreSQL, pgvector where justified, Redis                                                                                             | Transactional source of truth, analytics-friendly relational data, AI retrieval, caching, rate limits, and leaderboards |
| Async work          | SQS-compatible queue and a Python worker; transactional outbox                                                                          | Durable jobs without losing events between the database and queue                                                       |
| Challenge isolation | Rootless containers or Firecracker-grade sandbox service behind a queue                                                                 | Untrusted learner code must never execute inside the API process                                                        |
| AI mentor           | Provider interface with OpenAI Responses API as one adapter, Structured Outputs, prompt registry, eval datasets, and fallback responses | Replaceable models, schema-constrained answers, measured quality, controlled spend, and safe degradation                |
| Observability       | OpenTelemetry, Prometheus, Grafana, Sentry, structured JSON logs, correlation IDs                                                       | Trace a learner action across mobile, API, worker, database, and model calls                                            |
| Product analytics   | PostHog-compatible events plus warehouse-ready schemas                                                                                  | Funnels, retention, completion, cohort, and experiment analysis without mixing analytics with OLTP logic                |
| Delivery            | Docker, GitHub Actions, GHCR, Terraform, AWS ECS Fargate, RDS, ElastiCache, S3, CloudFront, SES, WAF                                    | Reproducible builds, reviewed infrastructure, staged deployments, secure managed primitives                             |
| Testing             | pytest, Testcontainers, Schemathesis, Hypothesis, Jest/Vitest, React Native Testing Library, Playwright, Maestro, k6                    | Unit, integration, contract, property, UI, E2E, resilience, and load coverage                                           |

## Repository shape established in Month 1

```text
engineerquest/
├── apps/
│   ├── mobile/
│   └── admin/
├── services/
│   ├── api/
│   ├── worker/
│   └── sandbox-runner/
├── packages/
│   ├── api-client/
│   ├── contracts/
│   ├── design-system/
│   └── telemetry/
├── curriculum/
├── infra/
│   ├── terraform/
│   └── observability/
├── tests/
│   ├── contract/
│   ├── e2e/
│   ├── load/
│   └── security/
└── docs/
    ├── adr/
    ├── api/
    ├── runbooks/
    └── evidence/
```

## Daily operating system

1. Open one scoped issue with acceptance criteria and link it to the current milestone.
2. Work on a feature branch; keep migrations, contracts, implementation, and tests in the same change.
3. Run the relevant local gate. Record the exact command and result in `docs/evidence/MxxDyy.md`.
4. Open a PR, complete a self-review, ensure CI is green, then merge. Never manufacture dozens of meaningless commits.
5. Update the decision log, changelog, risk register, or runbook when behavior or operations changed.
6. Publish externally only when the artifact is reproducible and useful: a release, architecture case study, benchmark, demo, incident write-up, or OSS contribution.

### Universal definition of done

- Requirements and non-goals are explicit.
- Data ownership, migrations, indexes, retention, and rollback are addressed.
- Authentication, authorization, input limits, abuse cases, and secrets are addressed.
- Unit tests cover business rules; integration or contract tests cover boundaries.
- Logs, metrics, traces, dashboards, and alerts exist in proportion to the risk.
- Failure behavior is tested: retry, timeout, duplicate, partial failure, cancellation, and dependency outage.
- User-facing copy, loading, empty, error, offline, and accessibility states are handled.
- The PR contains evidence, not only a screenshot of the happy path.

## Release train

| Month | Internal release        | Product proof                                                              |
| ----- | ----------------------- | -------------------------------------------------------------------------- |
| 1     | `v0.1-foundation`       | Reproducible monorepo, auth, profile, mobile shell, preview environment    |
| 2     | `v0.2-gamification`     | Transaction-safe XP, levels, streaks, achievements, quests, leaderboard    |
| 3     | `v0.3-learning-core`    | Versioned curriculum, five question types, skill graph, authoring workflow |
| 4     | `v0.4-git-world`        | Git curriculum, deterministic repository simulator, boss battle            |
| 5     | `v0.5-linux-world`      | Sandboxed terminal lessons, filesystem/process simulations, boss battle    |
| 6     | `v0.6-sql-world`        | Isolated SQL labs, AST validation, query plans, analytics, boss battle     |
| 7     | `v0.7-dsa-world`        | Multi-language code runner, judge, visualizations, DSA assessments         |
| 8     | `v0.8-debug-dungeon`    | Incident scenarios, log/trace explorer, scoring and postmortems            |
| 9     | `v0.9-network-security` | Packet-flow labs, auth/security labs, safe OWASP challenges                |
| 10    | `v0.10-cloud-devops`    | Cloud/DevOps simulations plus production AWS infrastructure                |
| 11    | `v0.11-ai-mentor`       | Grounded tutor, adaptive revision, interview mode, eval and safety gates   |
| 12    | `v1.0`                  | Admin, analytics, subscriptions, SLOs, app-store candidates, public launch |

## How to read each day

- **Decide / learn:** the engineering knowledge required before implementation.
- **Build:** the concrete production change to make that day.
- **Tools and why:** what is used and the reason it belongs in the system.
- **Prove:** the test, benchmark, fault injection, or product check that can disprove success.
- **Ship:** the reviewable artifact that must exist before the day is closed.

# Month 1 - Foundation and product architecture

**Monthly production goal:** Ship a reproducible vertical slice: account creation to authenticated dashboard, backed by PostgreSQL and deployed to a preview environment.

### M1D1 - Day 1 - Product charter and success metrics

- **Build / learn:** Write the PRD: personas, jobs-to-be-done, MVP/non-goals, north-star metric, guardrails, risks, and 12-month release map.
- **Tools and why:** GitHub Projects tracks scope; Markdown keeps decisions versioned; FigJam or Mermaid captures flows.
- **Prove:** Review every MVP story for a measurable acceptance criterion and remove features that cannot support the first learning loop.
- **Ship:** `docs/product/PRD.md`, roadmap board, risk register, and milestone `v0.1-foundation`.

### M1D2 - Day 2 - User research and competitive teardown

- **Build / learn:** Create interview script, recruit five target learners, and compare Duolingo, LeetCode, Codecademy, DataCamp, and certification products by learning loop rather than screenshots.
- **Tools and why:** Forms/spreadsheet organizes evidence; Notion or Markdown research log preserves raw observations and synthesis.
- **Prove:** Record source evidence, separate observations from assumptions, and turn the top three pains into testable hypotheses.
- **Ship:** Research repository, competitor matrix, interview schedule, and revised persona notes.

### M1D3 - Day 3 - Domain model and bounded contexts

- **Build / learn:** Map identity, learner profile, curriculum, attempts, progression, gamification, notifications, analytics, commerce, admin, sandbox, and mentor ownership.
- **Tools and why:** Domain-event map exposes coupling; ADRs capture boundary choices; Mermaid renders the context diagram.
- **Prove:** Walk three workflows across boundaries and identify the source of truth, transaction boundary, and eventual-consistency points.
- **Ship:** Context diagram plus ADR-001 modular monolith and ADR-002 data ownership.

### M1D4 - Day 4 - End-to-end user journeys

- **Build / learn:** Specify signup, class selection, first lesson, failure/retry, streak recovery, subscription, and account deletion journeys including empty/error/offline states.
- **Tools and why:** Figma creates wireframes; user-flow diagrams expose navigation and recovery paths.
- **Prove:** Run a cognitive walkthrough; every screen must have entry, exit, loading, error, accessibility, and analytics events.
- **Ship:** Clickable low-fidelity prototype and `docs/product/user-flows.md`.

### M1D5 - Day 5 - System quality attributes

- **Build / learn:** Define SLO candidates, threat model scope, privacy classification, capacity assumptions, RTO/RPO, accessibility target, and cost ceiling.
- **Tools and why:** Quality-attribute scenarios convert “scalable” into measurable behavior; OWASP threat modeling structures abuse cases.
- **Prove:** Each attribute gets stimulus, environment, expected response, and measurement; reject undefined “fast” or “secure” claims.
- **Ship:** Non-functional requirements and initial service-level objectives.

### M1D6 - Day 6 - Repository and engineering workflow

- **Build / learn:** Create monorepo directories, CODEOWNERS, issue/PR templates, conventional commits, changelog, license, contributing guide, and decision log.
- **Tools and why:** GitHub provides traceability; pre-commit, Ruff, mypy, ESLint, and Prettier block cheap defects early.
- **Prove:** Clone into a clean directory and run one bootstrap command; intentionally violate each gate and confirm CI fails.
- **Ship:** Green bootstrap PR and `make doctor` evidence.

### M1D7 - Day 7 - Local development platform

- **Build / learn:** Compose PostgreSQL, Redis, mail catcher, API, worker, mobile dependencies, and observability collector with health checks and seeded config.
- **Tools and why:** Docker Compose makes dependencies reproducible; `uv` and package-locking pin Python and Node graphs.
- **Prove:** Delete local volumes, rebuild from zero, run migrations and seed, then verify readiness without undocumented steps.
- **Ship:** `docker compose up` developer environment and onboarding runbook.

### M1D8 - Day 8 - FastAPI service skeleton

- **Build / learn:** Implement app factory, settings validation, lifespan, `/health/live`, `/health/ready`, `/version`, request IDs, error envelope, OpenAPI metadata, and dependency boundaries.
- **Tools and why:** FastAPI/Pydantic define typed HTTP contracts; Uvicorn serves; structlog emits machine-readable logs.
- **Prove:** Contract-test status codes and schemas; readiness must fail when required dependencies are unavailable.
- **Ship:** Deployable API container with unit and smoke tests.

### M1D9 - Day 9 - Database foundation

- **Build / learn:** Model users, profiles, engineer classes, sessions, audit events, timestamps, soft-delete policy, constraints, and indexes; create reversible Alembic migrations.
- **Tools and why:** PostgreSQL is the source of truth; SQLAlchemy maps transactions; Alembic versions schema changes.
- **Prove:** Test upgrade/downgrade on an empty database and upgrade from the previous revision; inspect query plans for login lookups.
- **Ship:** ERD, migration set, seed factory, and database conventions.

### M1D10 - Day 10 - Account registration

- **Build / learn:** Build normalized-email registration, Argon2 password hashing, email-verification token lifecycle, duplicate handling, password policy, and audit events.
- **Tools and why:** Passlib/Argon2 protects passwords; Pydantic validates boundaries; mail catcher enables local verification.
- **Prove:** Test enumeration resistance, Unicode/case variants, duplicate races, expired tokens, and transaction rollback.
- **Ship:** `POST /auth/register`, verification flow, tests, and API examples.

### M1D11 - Day 11 - Login and rotating sessions

- **Build / learn:** Implement access tokens, opaque rotating refresh tokens stored hashed, device sessions, reuse detection, logout-one, logout-all, and configurable TTLs.
- **Tools and why:** JWT limits API lookup cost; database sessions enable revocation; Redis rate-limits credential attacks.
- **Prove:** Replay an old refresh token, exceed login limits, revoke a device, and verify audit records never contain secrets.
- **Ship:** Auth session service, migration, threat-model update, and security tests.

### M1D12 - Day 12 - Password recovery and account protection

- **Build / learn:** Add request-reset, single-use reset completion, password-change session revocation, cooldowns, and security notifications.
- **Tools and why:** SES-compatible mail adapter separates provider; Redis cooldowns prevent abuse; audit events support support investigations.
- **Prove:** Prove identical public responses for known/unknown emails, token one-time use, expiry, and concurrent-reset behavior.
- **Ship:** Password recovery API, templates, integration tests, and abuse runbook.

### M1D13 - Day 13 - Authorization policy

- **Build / learn:** Define learner, content-editor, support, and admin roles; implement permission dependencies and object-level authorization with deny-by-default behavior.
- **Tools and why:** FastAPI dependencies centralize policy; policy tests prevent route-by-route drift.
- **Prove:** Generate a role-route matrix and test every protected endpoint for anonymous, wrong-role, and cross-user access.
- **Ship:** Authorization module, matrix, and negative test suite.

### M1D14 - Day 14 - Profile and onboarding API

- **Build / learn:** Create profile read/update, engineer-class selection, goals, timezone, locale, onboarding state machine, and optimistic concurrency version.
- **Tools and why:** PostgreSQL constraints protect state; ETags/version fields prevent silent lost updates.
- **Prove:** Test invalid state transitions, concurrent edits, timezone edges, and safe public/private response schemas.
- **Ship:** Profile/onboarding endpoints, OpenAPI examples, and state diagram.

### M1D15 - Day 15 - Mobile shell and design system

- **Build / learn:** Initialize Expo Router, environment/build profiles, error boundary, design tokens, dark mode, and accessible button/input/card/feedback primitives.
- **Tools and why:** Expo accelerates iOS/Android delivery; isolated component previews and accessibility APIs make the UI reviewable.
- **Prove:** Run both simulators; test cold start/deep link, contrast, dynamic type, screen readers, reduced motion, touch targets, and production config.
- **Ship:** Installable builds, component catalog, tokens, and mobile architecture ADR.

### M1D16 - Day 16 - Typed API client and server state

- **Build / learn:** Generate or hand-curate a client from OpenAPI, add auth headers, refresh mutex, timeouts, cancellation, error mapping, and query cache policy.
- **Tools and why:** TanStack Query manages server state; Zod guards runtime payloads; Zustand remains limited to local UI/session state.
- **Prove:** Simulate expired access tokens with ten concurrent requests and prove exactly one refresh occurs without a retry storm.
- **Ship:** Shared API client package, contract test, and caching ADR.

### M1D17 - Day 17 - Mobile signup and verification

- **Build / learn:** Build validated signup form, consent copy, verification pending/resend screens, deep-link completion, and analytics events.
- **Tools and why:** React Hook Form minimizes form churn; Zod shares constraints; Expo Linking handles verified callbacks.
- **Prove:** Test slow network, duplicate email, app restart mid-flow, expired link, screen reader, and double-submit prevention.
- **Ship:** Working registration journey on both platforms with Maestro test.

### M1D18 - Day 18 - Mobile login and secure storage

- **Build / learn:** Implement login, biometric-optional unlock, session restore, logout, device-session list, and protected route groups.
- **Tools and why:** Expo SecureStore protects refresh credentials; router guards prevent unauthorized screen access.
- **Prove:** Inspect logs/storage for token leakage, revoke the active device, test offline launch, and confirm no protected-screen flash.
- **Ship:** Authenticated mobile shell and security evidence.

### M1D19 - Day 19 - Onboarding experience

- **Build / learn:** Build class/goal/timezone selection, progress indicator, skip rules, resumable state, and first-lesson call to action.
- **Tools and why:** State machine prevents impossible steps; product analytics measures abandonment and completion.
- **Prove:** Kill/restart the app at each step, change devices, and test localization expansion and accessibility navigation.
- **Ship:** Completed onboarding funnel connected to backend.

### M1D20 - Day 20 - Dashboard vertical slice

- **Build / learn:** Build dashboard summary API and mobile cards for class, current level placeholder, continue learning, daily goal, and profile.
- **Tools and why:** One backend-for-frontend response reduces mobile waterfall; cache headers control freshness.
- **Prove:** Measure request count and p95 locally; test empty/new user, partial dependency failure, stale cache, and pull-to-refresh.
- **Ship:** First complete authenticated screen and demo recording.

### M1D21 - Day 21 - Configuration and secrets

- **Build / learn:** Create typed environment matrix for local/test/preview/prod, secret rotation procedure, `.env.example`, and startup fail-fast rules.
- **Tools and why:** AWS Secrets Manager holds production secrets; GitHub OIDC avoids static CI cloud keys; Gitleaks scans commits.
- **Prove:** Attempt startup with missing/invalid config, scan history, rotate a preview secret, and confirm no value appears in logs.
- **Ship:** Configuration reference, secret runbook, and passing secret scan.

### M1D22 - Day 22 - Test architecture

- **Build / learn:** Set unit/integration/contract/E2E boundaries, factories, isolated databases, deterministic clock, coverage policy, and flaky-test rules.
- **Tools and why:** pytest, Testcontainers, Hypothesis, Schemathesis, React Native Testing Library, and Maestro cover distinct risks.
- **Prove:** Seed ten randomized valid/invalid payloads, run tests twice from clean state, and quarantine zero failures without an owner.
- **Ship:** Test strategy and CI test pyramid baseline.

### M1D23 - Day 23 - Continuous integration

- **Build / learn:** Build path-aware jobs for Python and TypeScript lint/type/test, migration checks, OpenAPI drift, container build, dependency audit, and E2E smoke.
- **Tools and why:** GitHub Actions automates gates; BuildKit caches safely; Codecov shows change coverage rather than vanity totals.
- **Prove:** Break a migration, schema, type, secret, test, and lockfile deliberately; confirm the correct job blocks merge.
- **Ship:** Required branch checks and CI troubleshooting guide.

### M1D24 - Day 24 - Preview deployment

- **Build / learn:** Provision minimal preview API, database, Redis-compatible cache, object storage, TLS, DNS, and mobile preview configuration.
- **Tools and why:** Terraform makes infrastructure reviewable; ECS Fargate/RDS reduce operational burden; GitHub OIDC deploys without long-lived keys.
- **Prove:** Destroy/recreate preview, verify HTTPS/security headers, run migrations once, and execute remote smoke tests.
- **Ship:** Live private preview and infrastructure state/runbook.

### M1D25 - Day 25 - Telemetry baseline

- **Build / learn:** Instrument mobile/API with trace IDs, request latency, error counters, database spans, and release/environment tags; add privacy-safe log policy.
- **Tools and why:** OpenTelemetry standardizes signals; Sentry captures exceptions; Prometheus/Grafana visualize service health.
- **Prove:** Trace signup end to end, induce a database timeout, verify alert context, and ensure passwords/tokens/answers are redacted.
- **Ship:** Dashboard, sample trace, log schema, and alert-routing test.

### M1D26 - Day 26 - Security baseline

- **Build / learn:** Create data-flow diagram and STRIDE threat model; add secure headers, CORS allowlist, payload limits, dependency scanning, SAST, container scan, and rate limits.
- **Tools and why:** OWASP ASVS guides controls; Semgrep, Trivy, and Dependabot surface code/supply-chain risk.
- **Prove:** Run automated scans and manual abuse cases; every high finding must be fixed, accepted with rationale, or block release.
- **Ship:** Threat model, security CI, and vulnerability register.

### M1D27 - Day 27 - Foundation resilience day

- **Build / learn:** Add graceful shutdown, database/Redis timeouts, retry budgets with jitter, circuit-breaker policy, idempotency keys for mutation retries, and degraded readiness.
- **Tools and why:** Tenacity implements bounded retries; Toxiproxy injects latency and disconnects; correlation IDs connect failures.
- **Prove:** Kill dependencies during requests and prove no infinite retry, corrupt transaction, duplicate account, or hanging shutdown.
- **Ship:** Resilience tests and dependency-outage runbook.

### M1D28 - Day 28 - Foundation performance and cost day

- **Build / learn:** Establish mobile cold-start, API p50/p95/p99, database connection, memory, image size, and monthly preview-cost baselines.
- **Tools and why:** k6 drives load; Pyroscope/profilers locate hotspots; AWS budgets prevent accidental spend.
- **Prove:** Run a documented load profile, inspect query plans, and record capacity limits plus the first bottleneck.
- **Ship:** Baseline performance report with target budgets.

### M1D29 - Day 29 - Foundation release candidate

- **Build / learn:** Freeze scope, run clean-room setup, migration rehearsal, full test matrix, accessibility pass, security scan, backup/restore, and demo script.
- **Tools and why:** Release checklist coordinates gates; semantic versioning and GHCR preserve reproducible artifacts.
- **Prove:** A fresh reviewer must install mobile build, register, verify, log in, complete onboarding, and open dashboard without help.
- **Ship:** Tagged `v0.1.0-rc1`, signed checklist, and known-issues list.

### M1D30 - Day 30 - Foundation release and retrospective

- **Build / learn:** Fix only release blockers, deploy `v0.1-foundation`, publish architecture/evidence page, close milestone, and prioritize debt by risk.
- **Tools and why:** GitHub Release bundles artifacts; MkDocs creates recruiter-verifiable documentation; retrospective data improves the next month.
- **Prove:** Post-deploy smoke, telemetry, rollback drill, and 24-hour error review must pass before promotion.
- **Ship:** Release `v0.1-foundation`, demo, retrospective, and Month 2 backlog.

# Month 2 - Gamification engine

**Monthly production goal:** Make progression rewarding without corruptible counters, timezone bugs, notification spam, or pay-to-win mechanics.

### M2D1 - Day 31 - Gamification product rules

- **Build / learn:** Define XP sources, level curve, streak rules, achievements, quests, rewards, anti-abuse limits, economy sinks, and fairness guardrails.
- **Tools and why:** Spreadsheets model curves; ADRs freeze business rules; feature flags allow safe tuning.
- **Prove:** Simulate novice/power/abusive user paths and verify time-to-level, reward frequency, and no impossible states.
- **Ship:** Gamification specification and parameter registry.

### M2D2 - Day 32 - Immutable XP ledger schema

- **Build / learn:** Create `xp_transactions` with source, idempotency key, actor, amount, reason, metadata, occurred/recorded times, reversal linkage, and constraints.
- **Tools and why:** PostgreSQL ledger preserves auditability; Alembic versions schema; partial unique indexes enforce deduplication.
- **Prove:** Replay duplicate awards concurrently, reverse an award, and prove balances reconcile from the ledger.
- **Ship:** Migration, ERD update, and ledger invariant tests.

### M2D3 - Day 33 - Transactional XP service

- **Build / learn:** Implement award/reverse APIs inside transactions, lock strategy, policy validation, event outbox, and balance projection.
- **Tools and why:** SQLAlchemy transaction boundaries protect invariants; outbox prevents lost domain events.
- **Prove:** Use Hypothesis and concurrent workers to prove balance equals valid ledger sum and duplicate commands award once.
- **Ship:** XP domain service with property/concurrency tests.

### M2D4 - Day 34 - XP integration contracts

- **Build / learn:** Emit lesson/quest/boss/achievement completion events; map each to versioned XP policy and expose statement/balance endpoints.
- **Tools and why:** Versioned event schemas decouple domains; JSON Schema/Pydantic validate producers and consumers.
- **Prove:** Contract-test old/new policy versions, out-of-order events, poison messages, and dead-letter behavior.
- **Ship:** XP event contracts and consumer integration tests.

### M2D5 - Day 35 - XP mobile experience

- **Build / learn:** Build animated gain receipt, balance, history, level progress, duplicate-safe optimistic UI, reduced-motion mode, and offline reconciliation.
- **Tools and why:** TanStack Query handles mutation reconciliation; Reanimated provides performant optional motion.
- **Prove:** Throttle network, retry taps, reorder responses, and compare displayed balance with ledger after reconnect.
- **Ship:** XP UI, accessibility test, and recorded failure recovery.

### M2D6 - Day 36 - Level curve and migration

- **Build / learn:** Implement parameterized level thresholds, cumulative XP lookup, prestige/future-proof fields, and curve-version migration plan.
- **Tools and why:** Pure functions make curves testable; spreadsheet and notebook visualize progression.
- **Prove:** Check monotonic thresholds, boundary XP values, large balances, curve change effects, and rollback mapping.
- **Ship:** Level engine, benchmark chart, and ADR on curve versioning.

### M2D7 - Day 37 - Level-up orchestration

- **Build / learn:** Create exactly-once user-facing level-up event, reward grants, notification, and timeline entry without coupling to XP transaction retries.
- **Tools and why:** Outbox plus idempotent consumers coordinates side effects; Redis deduplicates short-lived delivery.
- **Prove:** Crash between commit and publish, replay events, and prove one reward and one visible celebration.
- **Ship:** Level-up worker flow and fault-injection evidence.

### M2D8 - Day 38 - Level UI and progression preview

- **Build / learn:** Build current level, next threshold, unlock preview, progress animation, and level-up modal with interruption-safe navigation.
- **Tools and why:** Shared contracts prevent formula drift; feature flags enable staged animation rollout.
- **Prove:** Background/kill app during celebration, use reduced motion, and verify level state is correct on relaunch.
- **Ship:** Mobile level experience and E2E test.

### M2D9 - Day 39 - XP abuse controls

- **Build / learn:** Add per-source caps, suspicious velocity detection, server-authoritative completion, device/account signals, admin review reason, and reversible sanctions.
- **Tools and why:** Redis sliding-window limits fast abuse; SQL audit records durable decisions; rules remain explainable.
- **Prove:** Attempt client-forged awards, replay completions, clock changes, and rapid multi-device submissions.
- **Ship:** Abuse test suite and moderation playbook.

### M2D10 - Day 40 - XP and level release slice

- **Build / learn:** Integrate dashboard, profile, lesson stub, history, telemetry, and support query; benchmark ledger and projection reads.
- **Tools and why:** Materialized projection serves hot reads while ledger remains canonical; Grafana tracks award failures and lag.
- **Prove:** Run 10k mixed award/read commands, reconcile every account, and enforce latency/error budgets.
- **Ship:** Feature-flagged XP/level alpha and engineering review.

### M2D11 - Day 41 - Streak semantics and timezone model

- **Build / learn:** Define qualifying action, learner-local day, DST, grace period, freeze, repair, travel/timezone change, and maximum trusted clock skew.
- **Tools and why:** IANA timezone data avoids fixed-offset bugs; injectable clock makes calendar logic deterministic.
- **Prove:** Test DST gaps/folds, month/year boundaries, timezone jumps, delayed events, and leap day.
- **Ship:** Streak state machine and exhaustive date matrix.

### M2D12 - Day 42 - Streak persistence and evaluator

- **Build / learn:** Create streak status/history/freeze ledger; implement idempotent daily evaluation from canonical completion events.
- **Tools and why:** PostgreSQL range/unique constraints protect one decision per learner-day; background worker handles evaluation.
- **Prove:** Process late, duplicate, and out-of-order events; recomputation must reproduce stored result.
- **Ship:** Streak service, migrations, and replay command.

### M2D13 - Day 43 - Streak freeze economy

- **Build / learn:** Implement earn/use/expire/restore freeze rules, atomic consumption, caps, support override, and complete audit trail.
- **Tools and why:** Database transactions prevent double consumption; admin permissions separate support from policy changes.
- **Prove:** Race two devices at midnight, revoke a transaction, and prove freeze balance never becomes negative.
- **Ship:** Freeze ledger/API and concurrency tests.

### M2D14 - Day 44 - Streak mobile surfaces

- **Build / learn:** Build home flame, calendar history, timezone explanation, freeze inventory, recovery state, and non-shaming loss copy.
- **Tools and why:** Date utilities format local days; analytics events measure comprehension and recovery.
- **Prove:** Snapshot multiple locales/timezones, offline boundary crossing, and screen-reader announcement order.
- **Ship:** Streak UI and usability notes from five testers.

### M2D15 - Day 45 - Streak reminders

- **Build / learn:** Schedule reminder preferences, quiet hours, locale/timezone templates, dedupe keys, push-token lifecycle, and unsubscribe path.
- **Tools and why:** Expo Notifications delivers mobile push; worker queue schedules; Redis prevents duplicate sends.
- **Prove:** Simulate clock changes, invalid tokens, retry storms, opted-out users, and notification deep links.
- **Ship:** Reminder service, template catalog, and delivery dashboard.

### M2D16 - Day 46 - Achievement catalog model

- **Build / learn:** Define versioned criteria DSL, visible/hidden badges, tiers, assets, rarity, revocation, localization, and retroactive eligibility.
- **Tools and why:** JSON Schema validates catalog; S3/CDN hosts versioned assets; content review workflow prevents broken rules.
- **Prove:** Reject invalid/cyclic criteria and verify old app clients tolerate newly added achievements.
- **Ship:** Achievement schema, sample catalog, and lint command.

### M2D17 - Day 47 - Achievement evaluator

- **Build / learn:** Consume domain events, maintain counters, evaluate criteria idempotently, grant atomically, and support backfill/rebuild.
- **Tools and why:** Event consumer isolates evaluation; PostgreSQL unique constraints ensure one grant per version.
- **Prove:** Replay full event history, inject duplicates, and compare incremental grants with batch recomputation.
- **Ship:** Evaluator, backfill command, and invariant tests.

### M2D18 - Day 48 - Achievement reveal and collection

- **Build / learn:** Build reveal queue, collection filters, progress-to-badge, share card, reduced motion, and offline-safe acknowledgement.
- **Tools and why:** Reanimated powers optional reveal; image generation stays server-controlled to prevent tampering.
- **Prove:** Grant three badges at once, interrupt app, change locale, and confirm each reveal is acknowledged once.
- **Ship:** Achievement gallery/reveal E2E flow.

### M2D19 - Day 49 - Achievement operations

- **Build / learn:** Add admin preview, enable/disable, scheduled publishing, manual grant/revoke with reason, and audit diff.
- **Tools and why:** Admin Next.js form uses shared schema; RBAC and audit log protect privileged changes.
- **Prove:** Two-person approval for global rule edits, permission matrix tests, and rollback to prior catalog version.
- **Ship:** Admin achievement workflow and audit evidence.

### M2D20 - Day 50 - Achievement release slice

- **Build / learn:** Integrate telemetry, rarity aggregation, support lookup, rate budgets, and cohort rollout.
- **Tools and why:** Feature flags stage release; PostHog funnels measure discovery/reveal/collection engagement.
- **Prove:** Backfill a seeded cohort, compare counts, test consumer lag, and confirm p95 grant delay target.
- **Ship:** Achievement alpha, dashboard, and weekly review.

### M2D21 - Day 51 - Daily and weekly quest model

- **Build / learn:** Define quest templates, eligibility, objective counters, reward policy, recurrence, expiration, reroll, and localization.
- **Tools and why:** Rule schema keeps content data-driven; recurrence library handles calendar rules; flags control experiments.
- **Prove:** Validate impossible objectives, overlapping periods, timezone boundaries, and reward-budget caps.
- **Ship:** Quest contract, catalog, and product rules.

### M2D22 - Day 52 - Deterministic quest assignment

- **Build / learn:** Generate personalized assignments from eligible templates using stable randomness, exclusions, skill level, and anti-repetition windows.
- **Tools and why:** Deterministic hashing makes assignments reproducible; PostgreSQL stores assignments and policy version.
- **Prove:** Run the same learner/day twice, compare distribution fairness, and ensure no inaccessible-world quest is assigned.
- **Ship:** Assignment service plus distribution report.

### M2D23 - Day 53 - Quest progress consumer

- **Build / learn:** Map learning events to objective progress, enforce monotonic counters, complete once, award transactionally, and handle expiry.
- **Tools and why:** Outbox events integrate learning and XP; idempotent projection absorbs retries.
- **Prove:** Reorder/duplicate events, complete at expiry boundary, and verify reward and status consistency.
- **Ship:** Quest progress worker and property tests.

### M2D24 - Day 54 - Quest mobile experience

- **Build / learn:** Build daily/weekly cards, progress, claim behavior, expiry timer, reroll explanation, and empty/degraded states.
- **Tools and why:** TanStack Query streams authoritative status; local cache supports read-only offline display.
- **Prove:** Test background timer, offline completion then reconnect, duplicate claim taps, and locale expansion.
- **Ship:** Quest screens and E2E scenarios.

### M2D25 - Day 55 - Leaderboard architecture

- **Build / learn:** Define friends/global/weekly leagues, tie rules, privacy aliases, opt-out, season boundaries, anti-cheat eligibility, and rank pagination.
- **Tools and why:** Redis sorted sets serve hot ranks; PostgreSQL ledger/snapshots remain recoverable source.
- **Prove:** Compare Redis ranks with SQL recomputation, test ties, season rollover, and private accounts.
- **Ship:** Leaderboard ADR, schemas, and reconciliation job.

### M2D26 - Day 56 - Leaderboard API and mobile

- **Build / learn:** Implement around-me pagination, top ranks, previous-season results, cache policy, profile links, and accessible list UI.
- **Tools and why:** Redis pipelines reduce round trips; cursor pagination avoids offset drift; virtualization keeps mobile smooth.
- **Prove:** Load-test rank reads, ban an abuser, expire cache, and verify stable ordering and authorization.
- **Ship:** Leaderboard feature behind cohort flag.

### M2D27 - Day 57 - Gamification analytics

- **Build / learn:** Define exposure, award, progress, streak, quest, achievement, and leaderboard events plus retention cohorts and guardrail metrics.
- **Tools and why:** PostHog captures product funnels; warehouse-ready event schemas enable later analysis; dbt tests event quality.
- **Prove:** Check event uniqueness, schema conformance, missing-user handling, consent, and dashboard reconciliation to OLTP counts.
- **Ship:** Gamification dashboards and metric dictionary.

### M2D28 - Day 58 - Gamification adversarial test day

- **Build / learn:** Attack forged events, replay, concurrency, device clock, timezone, caps, rank manipulation, notification spam, and admin misuse.
- **Tools and why:** Schemathesis, Hypothesis, k6, and security scripts explore states beyond handpicked examples.
- **Prove:** No ledger mismatch, negative inventory, double reward, unauthorized grant, or cross-user read may survive.
- **Ship:** Adversarial report with fixed defects and accepted residual risks.

### M2D29 - Day 59 - Gamification release candidate

- **Build / learn:** Run migration/replay, full E2E loop, accessibility, performance, notification, observability, rollback, and support drills.
- **Tools and why:** Release flags separate XP, streak, achievement, quest, and leaderboard rollback; dashboards gate promotion.
- **Prove:** Pilot cohort completes three days of actions; reconcile every balance and investigate all alert noise.
- **Ship:** Tagged `v0.2.0-rc1`, pilot report, and operator checklist.

### M2D30 - Day 60 - Gamification release

- **Build / learn:** Promote `v0.2-gamification`, monitor cohorts, document algorithms and trade-offs, close debt, and publish a technical case study.
- **Tools and why:** GitHub Release/MkDocs make evidence reproducible; feature analytics drives the next iteration.
- **Prove:** Verify SLOs, ledger reconciliation, no notification duplication, and successful rollback drill after deploy.
- **Ship:** Release, demo, retrospective, and Month 3 prioritized backlog.

# Month 3 - Learning engine and curriculum platform

**Monthly production goal:** Ship versioned curriculum authoring and a reliable attempt-to-mastery pipeline supporting five interaction types.

### M3D1 - Day 61 - Curriculum information architecture

- **Build / learn:** Define worlds, modules, lessons, activities, attempts, prerequisites, mastery, drafts, versions, locales, and publication lifecycle.
- **Tools and why:** ER modeling clarifies ownership; JSON Schema defines content; ADRs record versioning rules.
- **Prove:** Walk edit/publish/rollback and in-progress learner flows; published content must be immutable and addressable.
- **Ship:** Curriculum domain model and content lifecycle diagram.

### M3D2 - Day 62 - Curriculum schema and migrations

- **Build / learn:** Implement normalized tables for world/module/lesson/activity/version/assets/tags/prerequisites with slugs, ordering constraints, and soft archive.
- **Tools and why:** PostgreSQL enforces consistency; Alembic manages rollout; S3 holds binary assets.
- **Prove:** Create, reorder, archive, and roll back a sample hierarchy; test uniqueness and foreign-key behavior.
- **Ship:** Migrations, models, indexes, and seed world.

### M3D3 - Day 63 - Content format and linter

- **Build / learn:** Design portable YAML/JSON lesson format with stable IDs, schema versions, localization keys, hints, rubrics, and asset references.
- **Tools and why:** Pydantic/JSON Schema validates; CLI linter catches broken references; Git provides curriculum review.
- **Prove:** Lint malformed, duplicated, cyclic, missing-asset, and unsupported-version fixtures with actionable errors.
- **Ship:** `eq-content lint` CLI and author guide.

### M3D4 - Day 64 - Publishing workflow

- **Build / learn:** Build draft, validate, preview, approve, publish, supersede, and rollback commands with content hashes and audit events.
- **Tools and why:** Database transactions atomically publish; RBAC gates approval; immutable versions keep attempts explainable.
- **Prove:** Race two editors, publish invalid content, roll back active content, and confirm learners remain pinned correctly.
- **Ship:** Publishing service/API and audit tests.

### M3D5 - Day 65 - Curriculum read API

- **Build / learn:** Expose catalog, world, module, lesson manifest, content version, localization, entitlement, ETag, and cache-control behavior.
- **Tools and why:** FastAPI serves typed contracts; CDN caches public manifests; Redis caches personalized unlock summaries.
- **Prove:** Contract-test stale ETags, locale fallback, archived versions, unauthorized premium content, and pagination.
- **Ship:** Documented curriculum API and generated client update.

### M3D6 - Day 66 - World map mobile UI

- **Build / learn:** Build world list/map with availability, progress, lock reason, download status, and accessible non-visual navigation.
- **Tools and why:** FlashList/virtualization controls memory; TanStack Query caches manifests; SVG/Reanimated render optional map motion.
- **Prove:** Test 100 worlds, low-memory device, offline cached view, reduced motion, and screen-reader order.
- **Ship:** World map connected to real catalog.

### M3D7 - Day 67 - Module progression service

- **Build / learn:** Compute module availability from prerequisites, entitlement, experiment, and published content; return explicit lock reasons.
- **Tools and why:** Graph algorithms evaluate prerequisites; versioned policy keeps progression auditable.
- **Prove:** Test branching paths, cycles, missing nodes, policy upgrades, and concurrent prerequisite completion.
- **Ship:** Progression engine and graph property tests.

### M3D8 - Day 68 - Module screen and resume state

- **Build / learn:** Build module overview, lesson sequence, mastery summary, locked states, resume CTA, and content download controls.
- **Tools and why:** Local persistence stores safe resume pointers; server remains authoritative for completion.
- **Prove:** Change content version mid-module, reinstall app, lose network, and confirm resume chooses a valid activity.
- **Ship:** Module UI and cross-device resume E2E.

### M3D9 - Day 69 - Attempt lifecycle model

- **Build / learn:** Define attempt started/answered/checked/completed/abandoned events, content pinning, duration, hints, score, integrity metadata, and retry policy.
- **Tools and why:** Append-only attempt events preserve audit; projection tables serve fast resume/analytics.
- **Prove:** Replay events to rebuild state, reject illegal transitions, and ensure duplicate submissions are idempotent.
- **Ship:** Attempt state machine, tables, and invariants.

### M3D10 - Day 70 - Lesson session API

- **Build / learn:** Implement start/resume, next activity, submit answer, request hint, abandon, and complete endpoints with server-owned sequencing.
- **Tools and why:** Idempotency keys make mobile retries safe; optimistic concurrency prevents two active writers.
- **Prove:** Use two devices, reordered requests, stale versions, and disconnects; prove one coherent attempt result.
- **Ship:** Lesson session API and contract suite.

### M3D11 - Day 71 - MCQ activity

- **Build / learn:** Implement single/multiple choice schema, randomized order with stable seed, explanations, partial-credit policy, and accessible controls.
- **Tools and why:** Shared schema powers admin/mobile/API; deterministic shuffle prevents answer-position leakage.
- **Prove:** Test duplicate labels, zero/multiple correct choices, retry consistency, keyboard/screen reader, and tampered answer IDs.
- **Ship:** MCQ authoring preview, renderer, evaluator, and fixtures.

### M3D12 - Day 72 - Fill-blank activity

- **Build / learn:** Support normalized text, multiple accepted answers, case/whitespace rules, regex only under strict review, feedback, and localization.
- **Tools and why:** Unicode normalization avoids false negatives; safe comparison rules avoid arbitrary code execution.
- **Prove:** Test accents, Unicode confusables, empty input, long input, regex denial-of-service, and locale variants.
- **Ship:** Fill-blank schema, evaluator, mobile component, and tests.

### M3D13 - Day 73 - Drag-and-drop activity

- **Build / learn:** Model draggable tokens/zones, order/group modes, keyboard alternative, touch feedback, and deterministic reset.
- **Tools and why:** Gesture Handler supports touch; accessible button-based fallback prevents exclusion.
- **Prove:** Test interrupted gesture, orientation change, small screens, duplicate tokens, and screen reader completion.
- **Ship:** Drag-drop activity across admin preview and mobile.

### M3D14 - Day 74 - Match-pair activity

- **Build / learn:** Implement pair IDs, distractors, shuffle seed, attempt state, mistake feedback, and scalable rendering.
- **Tools and why:** Virtualized lists handle large sets; stable IDs prevent text-based ambiguity.
- **Prove:** Test duplicate display text, 50 pairs, orientation changes, rapid taps, and offline resume.
- **Ship:** Match-pair schema/renderer/evaluator and E2E test.

### M3D15 - Day 75 - Typing challenge activity

- **Build / learn:** Support command/code/text typing, normalization policy, expected-output matcher, hints, mobile keyboard behavior, and safe size limits.
- **Tools and why:** Monaco is reserved for admin preview; native text editor handles mobile; server evaluator owns correctness.
- **Prove:** Test newline/quote/tab variants, huge paste, Unicode, keyboard dismissal, and client tampering.
- **Ship:** Typing challenge end-to-end.

### M3D16 - Day 76 - Unified evaluation engine

- **Build / learn:** Create evaluator interface, result schema, score/feedback/hint contract, activity registry, version routing, and deterministic pure evaluators.
- **Tools and why:** Strategy pattern isolates types; Pydantic discriminated unions keep contracts exhaustive.
- **Prove:** Golden-test all activity versions and prove adding a new type fails compilation/tests until every layer handles it.
- **Ship:** Evaluation package with golden fixture suite.

### M3D17 - Day 77 - Lesson completion transaction

- **Build / learn:** Atomically finalize attempt, update progress, emit XP/mastery/analytics events via outbox, and return stable result receipt.
- **Tools and why:** PostgreSQL transaction plus outbox protects cross-domain consistency; workers handle side effects.
- **Prove:** Crash at each boundary, replay requests/events, and verify one completion, one XP award, and reproducible score.
- **Ship:** Completion orchestration and fault tests.

### M3D18 - Day 78 - Feedback and hint framework

- **Build / learn:** Model authored hint levels, explanation visibility, mistake taxonomy, retry feedback, and content safety rules.
- **Tools and why:** Structured content avoids free-form inconsistency; analytics events reveal hint dependence.
- **Prove:** Verify no hint leaks final answer prematurely and every wrong answer has useful, localized feedback.
- **Ship:** Hint/feedback author standard and renderer support.

### M3D19 - Day 79 - Skill graph schema

- **Build / learn:** Represent skills, edges, lesson coverage, evidence weights, mastery thresholds, decay, and versioned graph releases.
- **Tools and why:** Directed acyclic graph tools validate prerequisites; PostgreSQL stores versioned graph.
- **Prove:** Detect cycles/orphans, compare coverage, and test old learner state across graph revision.
- **Ship:** Skill graph format, validator, and visualization.

### M3D20 - Day 80 - Mastery calculation

- **Build / learn:** Implement evidence-weighted mastery from attempts, recency, hints, retries, and boss performance with explainable components.
- **Tools and why:** Pure Python model remains interpretable; notebook validates behavior; feature flag versions the formula.
- **Prove:** Simulate strong/weak/inconsistent histories, check bounds/monotonicity, and compare against expert expectations.
- **Ship:** Mastery service, model card, and calibration report.

### M3D21 - Day 81 - Unlock engine integration

- **Build / learn:** Combine prerequisite graph, mastery, entitlement, cohort flags, and manual support overrides into one decision response.
- **Tools and why:** Policy engine centralizes decisions; reason codes make UI/support behavior explainable.
- **Prove:** Property-test no locked node is entered without an authorized override and no reachable node is falsely orphaned.
- **Ship:** Unlock API, policy matrix, and mobile lock explanations.

### M3D22 - Day 82 - Offline lesson package

- **Build / learn:** Design signed content bundles, version manifest, checksum, download/resume/delete, storage quota, and offline attempt queue.
- **Tools and why:** Expo FileSystem stores bundles; signatures/checksums detect corruption; sync queue retries safely.
- **Prove:** Corrupt a bundle, interrupt download, change version, exhaust storage, and submit twice after reconnect.
- **Ship:** Offline package manager and resilience evidence.

### M3D23 - Day 83 - Cross-device progress synchronization

- **Build / learn:** Implement sync cursor, conflict rules, attempt ownership, tombstones, retry backoff, and user-visible recovery.
- **Tools and why:** Server cursors make incremental sync efficient; vector/version fields detect stale writes.
- **Prove:** Create conflicting progress on two devices, change clocks, reinstall, and verify deterministic resolution with no XP duplication.
- **Ship:** Sync protocol, API, and multi-device E2E test.

### M3D24 - Day 84 - Learning analytics events

- **Build / learn:** Define exposures, starts, answers, hints, retries, completion, mastery, unlock, download, and sync events with consent and schema registry.
- **Tools and why:** Telemetry package enforces schemas; PostHog supports funnels; dbt tests completeness and uniqueness.
- **Prove:** Reconcile attempts to events, sample payloads for PII, and detect client/server duplicate emissions.
- **Ship:** Learning funnel dashboard and data-quality tests.

### M3D25 - Day 85 - Authoring admin foundation

- **Build / learn:** Create authenticated Next.js shell, curriculum list, draft editor, schema-driven forms, preview frame, validation panel, and role checks.
- **Tools and why:** Next.js serves internal workflows; shared contracts prevent editor/runtime drift; Monaco edits advanced JSON safely.
- **Prove:** Test unauthorized routes/actions, unsaved changes, large lesson, validation errors, and keyboard-only authoring.
- **Ship:** Admin authoring alpha deployed privately.

### M3D26 - Day 86 - Content review and localization

- **Build / learn:** Add reviewer assignment, comments, diff, approval checklist, locale completeness, translation status, and publish scheduling.
- **Tools and why:** Git-like version diff supports review; ICU message format handles pluralization and variables.
- **Prove:** Block self-approval where configured, missing critical locale strings, broken variables, and unreviewed changes.
- **Ship:** Review workflow and one fully localized sample lesson.

### M3D27 - Day 87 - Learning engine performance

- **Build / learn:** Profile catalog, lesson start, answer submit, completion, skill graph, mobile memory, offline bundle size, and admin editor.
- **Tools and why:** k6, EXPLAIN ANALYZE, mobile profiler, and compression tools expose bottlenecks.
- **Prove:** Meet defined p95 budgets under representative concurrency and document capacity/first saturation point.
- **Ship:** Performance report and optimized queries/bundles.

### M3D28 - Day 88 - Learning engine security and abuse

- **Build / learn:** Threat-model content injection, asset upload, answer scraping, tampered bundles, replayed attempts, admin compromise, and sandbox boundary.
- **Tools and why:** Signed URLs, MIME sniffing, AV scan hook, CSP, RBAC, and audit logs reduce attack surface.
- **Prove:** Run malicious fixtures and prove no executable upload, cross-user attempt access, unsigned bundle, or unauthorized publish.
- **Ship:** Security test report and remediations.

### M3D29 - Day 89 - Learning engine release candidate

- **Build / learn:** Run full author-publish-learn-offline-sync-complete flow, migration rehearsal, rollback, accessibility, analytics, and support lookup.
- **Tools and why:** Feature flags isolate new activity types; release checklist coordinates API/mobile/admin compatibility.
- **Prove:** A reviewer authors and publishes a lesson without database access; two devices complete it consistently.
- **Ship:** Tagged `v0.3.0-rc1` and signed acceptance report.

### M3D30 - Day 90 - Learning engine release

- **Build / learn:** Promote `v0.3-learning-core`, publish content/evaluator architecture case study, monitor completion errors, and close milestone.
- **Tools and why:** MkDocs and GitHub Release expose reproducible proof; dashboards watch attempts, latency, sync, and content failures.
- **Prove:** Post-deploy smoke, rollback drill, event reconciliation, and 24-hour error budget remain healthy.
- **Ship:** Release, demo, retrospective, and Git World backlog.

# Month 4 - Git World

**Monthly production goal:** Ship a technically accurate Git curriculum and a deterministic repository simulator that teaches state transitions, not command memorization.

### M4D1 - Day 91 - Git World curriculum map

- **Build / learn:** Define novice-to-advanced competencies, misconceptions, prerequisite graph, assessment blueprint, command safety policy, and boss narrative.
- **Tools and why:** Curriculum matrix maps skills to lessons and evidence; real Git repositories ground examples.
- **Prove:** Have two developers review technical accuracy and ensure every lesson measures an observable repository state.
- **Ship:** Git World curriculum RFC and coverage matrix.

### M4D2 - Day 92 - Repository fixture generator

- **Build / learn:** Create deterministic repositories with commits, branches, tags, authors, timestamps, remotes, and expected state manifests.
- **Tools and why:** Git CLI creates authentic objects; seed manifests make scenarios reproducible; containers isolate runs.
- **Prove:** Generate the same scenario twice and compare object graph, refs, working tree, and expected assertions.
- **Ship:** `eq-git-fixture` package and golden fixtures.

### M4D3 - Day 93 - Git state model and visualizer

- **Build / learn:** Parse commits, refs, HEAD, index, worktree, remotes, reflog, and status into a safe learner-facing graph.
- **Tools and why:** libgit2/pygit2 provides structured access; custom DTO prevents leaking host paths.
- **Prove:** Compare visual model against Git CLI across detached HEAD, unborn branch, conflicts, and deleted refs.
- **Ship:** Git state API and graph component prototype.

### M4D4 - Day 94 - Command policy and sandbox design

- **Build / learn:** Allowlist educational Git commands/options, set CPU/memory/time/file limits, block hooks/external helpers/network, and define reset lifecycle.
- **Tools and why:** Rootless container isolates execution; seccomp/AppArmor reduce syscall access; queue separates API from runner.
- **Prove:** Attempt command substitution, hooks, aliases, path traversal, fork bomb, network access, and oversized repository.
- **Ship:** Sandbox threat model and security acceptance suite.

### M4D5 - Day 95 - Git fundamentals lesson set

- **Build / learn:** Author repository, working tree, staging area, object model, init/status/add/commit/log lessons with real state snapshots.
- **Tools and why:** Content DSL versions lessons; fixture generator supplies authentic repos; simulator renders state differences.
- **Prove:** Fresh learners must predict state before commands and pass golden evaluator cases without memorized output strings.
- **Ship:** Published fundamentals module with reviewed assets.

### M4D6 - Day 96 - Commit challenge evaluator

- **Build / learn:** Evaluate tree/blob/commit relationships, staged content, message policy, author metadata, and exact/semantic acceptable end states.
- **Tools and why:** Git object IDs and tree diff make evaluation robust; rubric returns precise remediation.
- **Prove:** Accept alternate valid command sequences, reject client-reported success, and test amend/empty/binary cases.
- **Ship:** Commit evaluator and challenge pack.

### M4D7 - Day 97 - Branching lessons

- **Build / learn:** Teach branch refs, HEAD movement, switch/checkout, upstream tracking, deletion safety, and naming practices.
- **Tools and why:** Graph visualization connects commands to refs; scenario fixtures show diverging history.
- **Prove:** Test detached HEAD, uncommitted changes, branch collision, remote-tracking confusion, and alternate correct solutions.
- **Ship:** Branching module and mobile graph interactions.

### M4D8 - Day 98 - Merge mechanics lessons

- **Build / learn:** Teach fast-forward, three-way merge, merge base, strategies, conflicts, abort, and verification.
- **Tools and why:** Real Git merge operations preserve semantics; diff viewer explains base/ours/theirs.
- **Prove:** Generate text/binary/rename-delete conflicts and verify evaluator recognizes correctly resolved outcomes.
- **Ship:** Merge module and conflict fixtures.

### M4D9 - Day 99 - Interactive conflict resolver

- **Build / learn:** Build file list, base/ours/theirs panes, editable result, marker validation, stage/continue controls, and accessible simplified mode.
- **Tools and why:** Monaco powers web/admin demo; native diff UI supports mobile; sandbox executes final Git commands.
- **Prove:** Resolve conflicts with repeated lines, deleted files, Unicode, and app interruption; repository must remain recoverable.
- **Ship:** Conflict-resolution experience with E2E tests.

### M4D10 - Day 100 - Git collaboration workflow

- **Build / learn:** Teach clone/fetch/pull/push/remotes/upstream, protected branches, PR mental model, and non-fast-forward recovery using local fake remotes.
- **Tools and why:** Bare repositories emulate remotes without internet; audit trail records commands and state.
- **Prove:** Test stale clone, rejected push, force-with-lease, remote deletion, and no credential/network exposure.
- **Ship:** Collaboration module and remote simulator.

### M4D11 - Day 101 - Rebase conceptual lessons

- **Build / learn:** Teach replay model, interactive rebase plan, conflicts, abort/continue, rewritten identity, and when not to rebase.
- **Tools and why:** Commit graph animation reveals before/after topology; deterministic dates stabilize fixtures.
- **Prove:** Verify alternate valid histories, protected-public-history warning, conflict recovery, and reflog availability.
- **Ship:** Rebase lesson sequence and evaluators.

### M4D12 - Day 102 - Interactive rebase simulator

- **Build / learn:** Support pick/reword/edit/squash/fixup/drop plans in isolated repo with stepwise feedback and safe recovery.
- **Tools and why:** Git rebase executes truth; plan parser validates supported commands; timeouts protect runner.
- **Prove:** Test malformed plans, empty commits, conflicts, abort, continue, and identical final tree with different history.
- **Ship:** Interactive rebase challenge pack.

### M4D13 - Day 103 - Stash and worktree lessons

- **Build / learn:** Teach stash entries, staged/untracked inclusion, apply/pop conflicts, multiple worktrees, and context switching.
- **Tools and why:** Real repo fixtures preserve nuanced behavior; state visualizer exposes stash/worktree metadata.
- **Prove:** Test pop conflict, dropped stash recovery, untracked files, and branch already checked out elsewhere.
- **Ship:** Stash/worktree module and tests.

### M4D14 - Day 104 - Cherry-pick and revert lessons

- **Build / learn:** Teach patch replay, range picks, conflicts, mainline parent, revert versus reset, and public-history safety.
- **Tools and why:** Graph/diff views show semantic change independent of hash; evaluator checks final intent.
- **Prove:** Cover merge-commit revert, empty cherry-pick, conflict abort, and multiple valid histories.
- **Ship:** History-editing module and scenario suite.

### M4D15 - Day 105 - Reset, restore, and recovery

- **Build / learn:** Teach soft/mixed/hard reset, restore staged/worktree, reflog, fsck concepts, dangling commits, and recovery decision tree.
- **Tools and why:** Ephemeral sandbox makes destructive practice safe; snapshots allow instant restart.
- **Prove:** Recover from wrong reset, deleted branch, detached commit, and accidental restore; block unsafe host operations.
- **Ship:** Recovery module and guided decision tool.

### M4D16 - Day 106 - Git internals lab

- **Build / learn:** Let learners inspect `.git`, objects, refs, index concepts, packfiles, hashes, and plumbing commands using sanitized views.
- **Tools and why:** Git plumbing commands supply real evidence; binary viewer prevents unsafe/raw path access.
- **Prove:** Match porcelain actions to object/ref changes and test repository corruption handling without runner escape.
- **Ship:** Internals lab and mastery assessment.

### M4D17 - Day 107 - Simulator session API

- **Build / learn:** Implement create/execute/state/reset/submit endpoints, queued execution, idempotency, session TTL, output limits, and learner ownership.
- **Tools and why:** FastAPI fronts queue; Redis tracks ephemeral sessions; object storage persists approved snapshots; runner remains isolated.
- **Prove:** Test duplicate command, expired session, queue delay, runner crash, unauthorized session ID, and reset consistency.
- **Ship:** Versioned simulator API and contract tests.

### M4D18 - Day 108 - Mobile terminal and graph

- **Build / learn:** Build command input/history, output streaming, repository graph, state tabs, hints, reconnect, copy controls, and accessibility.
- **Tools and why:** WebSocket or SSE streams bounded output; virtualized lists protect memory; shared session cursor reconnects.
- **Prove:** Test large output, disconnect/reconnect, rotation, keyboard, screen reader, and malicious ANSI sequences.
- **Ship:** Git lab mobile experience and Maestro flow.

### M4D19 - Day 109 - Hint ladder and mistake taxonomy

- **Build / learn:** Create misconception codes, authored progressive hints, command-level feedback, state-based diagnosis, and reveal penalties.
- **Tools and why:** Rule engine provides deterministic help before AI; analytics measures hint effectiveness.
- **Prove:** For each challenge, inject common wrong states and verify hint helps without giving the final command immediately.
- **Ship:** Hint catalog and diagnostic evaluator.

### M4D20 - Day 110 - Git mastery and progression

- **Build / learn:** Map challenge evidence to Git skills, mastery updates, remediation lessons, unlock gates, XP policy, and achievement triggers.
- **Tools and why:** Learning core handles evidence; gamification events keep rewards idempotent.
- **Prove:** Replay attempts and confirm mastery/XP/unlocks match; failure and hint use must affect policy as specified.
- **Ship:** Integrated Git progression path.

### M4D21 - Day 111 - Boss battle design

- **Build / learn:** Design “Merge Conflict Monster”: timed incident brief, multi-step repo, branching mistake, conflict, recovery, rubric, hints, and post-battle review.
- **Tools and why:** Scenario manifest coordinates sandbox states; rubric scores outcomes and process evidence.
- **Prove:** Expert dry run establishes feasible time and alternate solutions; novice pilot identifies unclear instructions.
- **Ship:** Boss battle specification and playable alpha.

### M4D22 - Day 112 - Boss battle engine integration

- **Build / learn:** Implement checkpoints, objective graph, timer semantics, pause/reconnect, partial credit, failure recovery, and signed result receipt.
- **Tools and why:** State machine manages objectives; server clock prevents client manipulation; event log supports appeals.
- **Prove:** Kill app/runner, change client time, repeat submit, and use alternate correct sequence; scoring stays deterministic.
- **Ship:** End-to-end boss battle with fault tests.

### M4D23 - Day 113 - Git content technical review

- **Build / learn:** Run every command/challenge against supported Git versions, review wording, citations, platform differences, and safety warnings.
- **Tools and why:** CI matrix executes fixture/evaluator suite; content linter enforces references and IDs.
- **Prove:** Zero unreviewed command, broken fixture, stale expected output, or ambiguous rubric remains.
- **Ship:** Signed curriculum review and corrected content release.

### M4D24 - Day 114 - Git analytics and learning efficacy

- **Build / learn:** Build funnels for lesson start/completion, command errors, resets, hint levels, mastery, boss outcomes, and simulator failures.
- **Tools and why:** PostHog events plus warehouse queries separate learning difficulty from platform failure.
- **Prove:** Reconcile simulator commands with events and flag lessons whose failures are infrastructure-driven.
- **Ship:** Git World analytics dashboard and metric definitions.

### M4D25 - Day 115 - Git runner security review

- **Build / learn:** Perform container escape, resource exhaustion, filesystem, environment, output injection, dependency, and network tests; rotate runner images.
- **Tools and why:** Trivy scans image; seccomp/rootless runtime constrains; egress-deny validates isolation.
- **Prove:** All critical/high findings block release; record residual risks and emergency runner kill switch.
- **Ship:** Security report, hardened image, and containment runbook.

### M4D26 - Day 116 - Git runner load and capacity

- **Build / learn:** Measure queue wait, startup, command latency, concurrent sessions, memory, image pull, cleanup, and storage growth.
- **Tools and why:** k6 drives session load; Prometheus exposes saturation; autoscaling policy responds to queue age.
- **Prove:** Find maximum safe concurrency, verify cleanup after crashes, and keep API responsive when runner is saturated.
- **Ship:** Capacity report and autoscaling thresholds.

### M4D27 - Day 117 - Git World accessibility and device QA

- **Build / learn:** Audit terminal, graph, diff, conflict resolver, timers, motion, color, font scaling, and keyboard behavior on target devices.
- **Tools and why:** Maestro automates journeys; manual VoiceOver/TalkBack catches semantic issues.
- **Prove:** Complete core and boss flows without color-only cues, precise dragging, or visual graph dependence.
- **Ship:** Accessibility report and remediated components.

### M4D28 - Day 118 - Git World release candidate

- **Build / learn:** Run authoring-to-publish, fresh learner path, offline content, simulator, boss, analytics, support, rollback, and migration drills.
- **Tools and why:** Feature flags separate content, simulator, and boss rollout; release dashboard gates cohorts.
- **Prove:** Pilot learners finish the world; investigate every mismatch between rubric, repo state, and displayed result.
- **Ship:** Tagged `v0.4.0-rc1` and pilot findings.

### M4D29 - Day 119 - Git World documentation case study

- **Build / learn:** Write architecture, sandbox threat model, evaluator strategy, capacity benchmark, known limitations, and demo instructions.
- **Tools and why:** MkDocs embeds diagrams and evidence; release artifacts pin runner/content versions.
- **Prove:** A reviewer can reproduce one challenge and its failure tests from a clean clone.
- **Ship:** Recruiter-facing Git simulator case study.

### M4D30 - Day 120 - Git World release

- **Build / learn:** Promote `v0.4-git-world`, monitor SLOs and learning metrics, run rollback drill, close milestone, and prioritize Linux reuse.
- **Tools and why:** GitHub Release and dashboards complete evidence chain; retrospective converts lessons into platform improvements.
- **Prove:** No security, scoring, queue, or crash-rate release gate regresses during staged rollout.
- **Ship:** Release, demo, retrospective, and Linux World backlog.

# Month 5 - Linux World

**Monthly production goal:** Ship safe, realistic terminal labs covering filesystem, permissions, processes, networking, shell scripting, and operational diagnosis.

### M5D1 - Day 121 - Linux competency and safety map

- **Build / learn:** Define command progression, distro assumptions, misconceptions, destructive-command policy, lab boundaries, mastery map, and boss scenario.
- **Tools and why:** Curriculum matrix maps skills to evidence; ADR records the supported shell and Linux image.
- **Prove:** Review every objective for authentic terminal evidence and remove host-dependent or unsafe instructions.
- **Ship:** Linux World RFC, command allowlist, and coverage matrix.

### M5D2 - Day 122 - Deterministic Linux lab images

- **Build / learn:** Build pinned rootless images, non-root learner account, fixture filesystem, fake services, expected-state manifests, and image provenance.
- **Tools and why:** Docker/BuildKit creates reproducible labs; Trivy scans packages; SBOM records supply chain.
- **Prove:** Rebuild twice, compare fixtures, scan image, and prove the learner cannot become root or access host mounts.
- **Ship:** Versioned lab image, SBOM, and golden manifest.

### M5D3 - Day 123 - Terminal session service

- **Build / learn:** Implement create/execute/stream/reset/destroy with queueing, TTL, output limits, cancellation, ownership, and audit metadata.
- **Tools and why:** Sandbox runner isolates commands; Redis tracks leases; SSE streams bounded output.
- **Prove:** Test expired/foreign sessions, disconnects, long output, timeouts, runner death, and idempotent reset.
- **Ship:** Linux session API and contract tests.

### M5D4 - Day 124 - Shell parser and command policy

- **Build / learn:** Parse command/arguments safely, disable expansion hazards where required, block redirection escapes, network, device files, and fork bombs.
- **Tools and why:** Shell AST parsing beats string blacklists; seccomp/cgroups enforce defense in depth.
- **Prove:** Run injection, substitution, traversal, symlink, resource, and environment leakage attacks.
- **Ship:** Policy engine, adversarial corpus, and threat-model update.

### M5D5 - Day 125 - Terminal mobile component

- **Build / learn:** Build prompt, history, output virtualization, ANSI sanitization, keyboard toolbar, reconnect, clear/reset, and screen-reader transcript.
- **Tools and why:** Virtualized lists protect memory; ANSI parser renders safe subsets; session cursor resumes streams.
- **Prove:** Test huge output, malicious control codes, rotation, app kill, hardware keyboard, and TalkBack/VoiceOver.
- **Ship:** Reusable terminal component and device QA evidence.

### M5D6 - Day 126 - Filesystem concepts module

- **Build / learn:** Author root, paths, inode/link concepts, files/directories, hidden files, globbing, and filesystem hierarchy lessons.
- **Tools and why:** Fixture generator creates real trees; state inspector visualizes path and metadata changes.
- **Prove:** Learners must achieve end state through alternate valid commands; evaluator cannot rely on output text alone.
- **Ship:** Published filesystem-concepts lessons and fixtures.

### M5D7 - Day 127 - Navigation and file operations

- **Build / learn:** Build pwd/cd/ls/find/touch/mkdir/cp/mv/rm challenges with explicit destructive-action guardrails and recovery.
- **Tools and why:** Real shell commands run in disposable lab; manifest evaluator checks resulting tree.
- **Prove:** Cover spaces, Unicode, hidden files, symlinks, recursive operations, and incorrect working directory.
- **Ship:** Navigation challenge pack and golden tests.

### M5D8 - Day 128 - Links and storage lessons

- **Build / learn:** Teach hard/symbolic links, inode behavior, du/df concepts, archives, compression, and safe extraction.
- **Tools and why:** Filesystem inspector exposes inode/link metadata; crafted archives test traversal prevention.
- **Prove:** Reject zip-slip paths, broken symlinks, disk exhaustion, and evaluator confusion between link and copy.
- **Ship:** Links/storage module with security fixtures.

### M5D9 - Day 129 - Text processing lessons

- **Build / learn:** Author cat/less/head/tail/cut/sort/uniq/tr/wc/grep/sed/awk pipelines using realistic public logs and config files.
- **Tools and why:** Pinned GNU tools preserve behavior; fixture datasets make results reproducible.
- **Prove:** Test locales, delimiters, empty/large files, regex edge cases, pipeline exit status, and multiple valid solutions.
- **Ship:** Text-processing module and evaluator suite.

### M5D10 - Day 130 - Filesystem checkpoint

- **Build / learn:** Integrate lessons, hints, mastery, XP, offline bundle, analytics, and support preview; pilot the first ten labs.
- **Tools and why:** Learning/gamification contracts reuse platform capabilities; feature flag limits exposure.
- **Prove:** Pilot users complete tasks without host access; reconcile attempts and categorize instruction versus platform failures.
- **Ship:** Filesystem alpha and usability report.

### M5D11 - Day 131 - Users and groups module

- **Build / learn:** Teach UID/GID, users, groups, ownership, `/etc/passwd` concepts, least privilege, and service accounts in simulated labs.
- **Tools and why:** Isolated namespaces enable safe identity changes; sanitized inspector shows permissions.
- **Prove:** Test supplementary groups, nonexistent users, numeric IDs, and blocked attempts to alter protected lab configuration.
- **Ship:** Users/groups lessons and fixtures.

### M5D12 - Day 132 - Permission evaluator

- **Build / learn:** Implement rwx, octal/symbolic chmod, chown/chgrp, umask, directory traversal permission, ACL concepts, and exact state checks.
- **Tools and why:** `stat`/ACL metadata provides truth; pure evaluator explains mismatches.
- **Prove:** Cover sticky/setuid/setgid examples safely, default umask, symlinks, and alternate correct commands.
- **Ship:** Permission challenge engine and tests.

### M5D13 - Day 133 - Process lifecycle module

- **Build / learn:** Teach processes, PIDs, parent/child, foreground/background, signals, jobs, exit codes, and zombies using controlled services.
- **Tools and why:** Supervisor starts deterministic fake processes; cgroups limit resources; process inspector sanitizes details.
- **Prove:** Test signal handling, race with exited process, job control, zombie observation, and cross-session isolation.
- **Ship:** Process lessons and lab services.

### M5D14 - Day 134 - Resource monitoring module

- **Build / learn:** Teach ps/top-like views, memory/CPU/load, file descriptors, lsof concepts, and interpreting saturation versus failure.
- **Tools and why:** Synthetic service workload is deterministic system fixture, not learner data; Prometheus supplies correlated metrics.
- **Prove:** Create CPU, memory, FD, and I/O pressure within quotas and verify diagnosis rubric.
- **Ship:** Monitoring challenges and metric overlays.

### M5D15 - Day 135 - Service and log management

- **Build / learn:** Teach service lifecycle, journal concepts, log locations, rotation, exit status, and safe restart through a simulated supervisor.
- **Tools and why:** Fake systemd-compatible API avoids privileged init; structured logs power challenges.
- **Prove:** Test crash loops, missing config, permission failure, stale PID, rotation, and restart storms.
- **Ship:** Service diagnosis module and evaluator.

### M5D16 - Day 136 - Networking command curriculum

- **Build / learn:** Teach ip/ss/ping/curl/dig/traceroute concepts with a private lab network and no public egress.
- **Tools and why:** Container network creates deterministic hosts; egress firewall prevents abuse; packet captures are sanitized.
- **Prove:** Diagnose DNS, refused port, timeout, routing, and TLS-like failures without internet access.
- **Ship:** Networking-command module and private topology fixtures.

### M5D17 - Day 137 - Network lab visualizer

- **Build / learn:** Render interfaces, routes, sockets, DNS answers, and request path alongside terminal actions.
- **Tools and why:** Structured lab topology feeds SVG/mobile views; tcpdump-derived events are bounded and redacted.
- **Prove:** Compare visual state to commands across route changes, closed ports, and DNS updates; support nonvisual descriptions.
- **Ship:** Network visualizer with accessibility alternative.

### M5D18 - Day 138 - Shell scripting basics

- **Build / learn:** Teach variables, quoting, tests, loops, functions, pipes, strict mode, and exit handling through small operational scripts.
- **Tools and why:** ShellCheck gives static feedback; sandbox runs scripts; golden I/O fixtures score behavior.
- **Prove:** Test spaces, empty variables, failed pipelines, signals, large input, and forbidden commands.
- **Ship:** Shell scripting module and rubric.

### M5D19 - Day 139 - Shell script evaluator

- **Build / learn:** Evaluate output plus filesystem/process side effects, enforce runtime quotas, return test-case feedback, and hide protected tests.
- **Tools and why:** Harness executes public/hidden cases in fresh containers; signed results prevent client forgery.
- **Prove:** Attempt hardcoded answers, environment discovery, infinite loops, output floods, and nondeterminism.
- **Ship:** Script judge and adversarial tests.

### M5D20 - Day 140 - Linux mastery integration

- **Build / learn:** Map lab evidence to skills, remediation, unlocks, XP, achievements, and progress explanations.
- **Tools and why:** Mastery engine consumes normalized evidence; event outbox keeps rewards atomic.
- **Prove:** Replay all attempts and confirm stable mastery; resets and hints affect score exactly as policy states.
- **Ship:** Complete Linux skill path and progression tests.

### M5D21 - Day 141 - Linux boss battle design

- **Build / learn:** Design “Production Server Rescue”: disk pressure, bad permissions, failed service, noisy log, and connectivity symptom with safe checkpoints.
- **Tools and why:** Scenario manifest coordinates filesystem, processes, logs, and network; rubric scores diagnosis and recovery.
- **Prove:** Expert and novice pilots validate time, clues, alternate recovery paths, and no destructive dead end.
- **Ship:** Playable boss alpha and assessment blueprint.

### M5D22 - Day 142 - Boss battle implementation

- **Build / learn:** Add timed objectives, snapshots, restore, reconnect, partial credit, investigation evidence, and post-battle explanation.
- **Tools and why:** State machine and immutable command log support scoring and appeals; server clock prevents manipulation.
- **Prove:** Kill app/runner, exceed time, restore checkpoint, and solve via alternate valid commands.
- **Ship:** End-to-end Linux boss with fault tests.

### M5D23 - Day 143 - Linux content review

- **Build / learn:** Validate commands against pinned image, clarify distro differences, review accessibility, citations, safety notes, and expected state.
- **Tools and why:** CI executes every lesson and golden solution on the release image.
- **Prove:** Zero broken command, ambiguous rubric, unsupported package, or stale output remains.
- **Ship:** Signed technical review and corrected bundle.

### M5D24 - Day 144 - Runner isolation audit

- **Build / learn:** Review namespaces, seccomp, capabilities, mounts, devices, environment, egress, quotas, cleanup, and image patching.
- **Tools and why:** Rootless runtime, Trivy, SBOM, and policy tests provide layered containment.
- **Prove:** Escape and exhaustion corpus produces no host read/write, privilege gain, network egress, or persistent cross-session state.
- **Ship:** Isolation report and emergency kill-switch runbook.

### M5D25 - Day 145 - Linux capacity benchmark

- **Build / learn:** Measure session start, command p95, stream lag, concurrent labs, cleanup, image pulls, queue age, and cost per active learner.
- **Tools and why:** k6, Prometheus, and autoscaling metrics reveal saturation.
- **Prove:** Document safe concurrency and confirm API degrades gracefully when runner capacity is exhausted.
- **Ship:** Capacity plan and tuned worker limits.

### M5D26 - Day 146 - Linux analytics and support

- **Build / learn:** Build funnels, command-error taxonomy, hint use, reset rate, infrastructure failures, and support session inspection with privacy controls.
- **Tools and why:** PostHog plus redacted command events separate learning problems from platform defects.
- **Prove:** Reconcile session/audit/analytics counts and prove support cannot view another user without permission and reason.
- **Ship:** Linux dashboard and support runbook.

### M5D27 - Day 147 - Linux accessibility and device QA

- **Build / learn:** Audit terminal transcript, visualizers, timer, diff, keyboard, font scaling, color, and reduced motion across target devices.
- **Tools and why:** Maestro plus manual assistive-tech passes cover automated and semantic behavior.
- **Prove:** Complete all core objectives without gestures, color-only signals, or inaccessible terminal output.
- **Ship:** Accessibility report and fixed issues.

### M5D28 - Day 148 - Linux release candidate

- **Build / learn:** Run clean author-publish-download-lab-boss flow, migrations, rollback, security, load, analytics, support, and offline content checks.
- **Tools and why:** Cohort flags isolate runner and content rollout; release dashboard aggregates gates.
- **Prove:** Pilot users finish the world while runner errors, scoring disputes, and data mismatches remain below thresholds.
- **Ship:** Tagged `v0.5.0-rc1` and pilot report.

### M5D29 - Day 149 - Linux architecture case study

- **Build / learn:** Document sandbox, command policy, state evaluation, threat model, benchmark, cost, limitations, and reproducible demo.
- **Tools and why:** MkDocs and pinned container artifacts let recruiters verify claims.
- **Prove:** A clean clone launches one lab and reproduces one blocked escape test from written steps.
- **Ship:** Public Linux lab case study and demo video.

### M5D30 - Day 150 - Linux World release

- **Build / learn:** Promote `v0.5-linux-world`, monitor rollout, rehearse rollback, close milestone, and extract reusable sandbox improvements for SQL/DSA.
- **Tools and why:** GitHub Release, dashboards, and retrospective complete the evidence chain.
- **Prove:** Security, queue, latency, crash, scoring, and completion gates remain healthy after staged promotion.
- **Ship:** Release, retrospective, and SQL World backlog.

# Month 6 - SQL World

**Monthly production goal:** Ship isolated PostgreSQL learning labs with semantic query validation, safe resource limits, explain plans, and an optimization boss battle.

### M6D1 - Day 151 - SQL curriculum and dataset policy

- **Build / learn:** Map relational concepts through optimization, select public/licensed datasets, define dialect/version, privacy, reset, grading, and boss scope.
- **Tools and why:** Curriculum matrix links concepts to evidence; dataset cards document provenance and license.
- **Prove:** Every lesson has a real schema/question and no synthetic portfolio claim or unlicensed dataset.
- **Ship:** SQL World RFC, dataset register, and skill matrix.

### M6D2 - Day 152 - Database lab isolation architecture

- **Build / learn:** Design per-session schema/database, restricted role, statement timeout, row/output limits, read-only versus mutation labs, and cleanup.
- **Tools and why:** PostgreSQL roles/RLS/resource settings isolate learners; queue prevents API-side execution.
- **Prove:** Attempt catalog access, file functions, extensions, locks, long queries, cross-session reads, and connection exhaustion.
- **Ship:** SQL sandbox threat model and architecture ADR.

### M6D3 - Day 153 - Dataset ingestion pipeline

- **Build / learn:** Download pinned public datasets, verify checksums/licenses, normalize types, create migrations/seeds, statistics, and data dictionary.
- **Tools and why:** ETL CLI makes imports reproducible; object storage retains source snapshots; dbt tests quality.
- **Prove:** Rebuild twice and compare row counts/checksums; reject schema drift, null/key violations, and oversized assets.
- **Ship:** Versioned datasets, cards, and validation report.

### M6D4 - Day 154 - SQL session API

- **Build / learn:** Implement create/query/explain/reset/submit, cancellation, pagination, bounded results, ownership, TTL, and audit fields.
- **Tools and why:** FastAPI fronts pooled PostgreSQL connections; async queue handles expensive grading; cursors bound responses.
- **Prove:** Test cancel, timeout, duplicate submit, expired/foreign session, invalid encoding, and pool saturation.
- **Ship:** Versioned SQL lab API and contract tests.

### M6D5 - Day 155 - Mobile SQL editor

- **Build / learn:** Build syntax highlighting, schema browser, query history, results grid, error location, explain tab, offline lesson content, and accessible table alternative.
- **Tools and why:** Editor component improves authoring; virtualized grid controls memory; query cursor paginates.
- **Prove:** Test 10k-row result cap, narrow screen, keyboard, screen reader, rotation, disconnect, and malicious error text.
- **Ship:** SQL lab mobile UI and E2E smoke.

### M6D6 - Day 156 - Relational model lessons

- **Build / learn:** Teach table/row/column, key, constraint, normalization, null, type, relationship, and transaction concepts on the selected dataset.
- **Tools and why:** ER diagram renderer connects schema to data; content DSL pins dataset version.
- **Prove:** Technical review checks every claim and activity against live PostgreSQL behavior.
- **Ship:** Published relational-foundations module.

### M6D7 - Day 157 - SELECT and projection evaluator

- **Build / learn:** Author SELECT, alias, expression, DISTINCT, LIMIT lessons and compare result semantics rather than SQL strings.
- **Tools and why:** AST parser validates structure; canonical result comparison accepts alternate correct queries.
- **Prove:** Test order-insensitive results, nulls, floats, aliases, duplicates, and hardcoded-output attacks.
- **Ship:** SELECT challenge pack and semantic grader.

### M6D8 - Day 158 - Filtering lessons

- **Build / learn:** Teach WHERE, boolean logic, comparison, IN, BETWEEN, LIKE, regex cautions, and null predicates.
- **Tools and why:** Real data surfaces messy cases; query-plan capture begins performance literacy.
- **Prove:** Cover null three-valued logic, case/collation, dates, Unicode, and equivalent predicates.
- **Ship:** Filtering module and golden solutions.

### M6D9 - Day 159 - Ordering and pagination

- **Build / learn:** Teach ORDER BY, multi-key ties, NULLS placement, LIMIT/OFFSET, and keyset pagination trade-offs.
- **Tools and why:** Deterministic tie-breakers stabilize grading; EXPLAIN shows offset cost.
- **Prove:** Create duplicate sort keys, page drift, large offset, and null cases; rubric requires deterministic output.
- **Ship:** Ordering/pagination lessons and evaluator.

### M6D10 - Day 160 - SQL foundations checkpoint

- **Build / learn:** Integrate skills, attempts, hints, XP, analytics, offline content, and support views for first module.
- **Tools and why:** Learning-core events reuse progression; feature flag limits pilot.
- **Prove:** Pilot learners complete with alternative queries; separate SQL errors from runner/product failures.
- **Ship:** Foundations alpha and pilot findings.

### M6D11 - Day 161 - Aggregation lessons

- **Build / learn:** Teach COUNT variants, SUM/AVG/MIN/MAX, null behavior, numeric precision, GROUP BY, and HAVING.
- **Tools and why:** Dataset statistics make problems realistic; semantic grader compares typed results.
- **Prove:** Test empty groups, duplicates, decimals, nulls, grouping errors, and alternate equivalent queries.
- **Ship:** Aggregation module and test matrix.

### M6D12 - Day 162 - Join fundamentals

- **Build / learn:** Teach inner/left/right/full/cross/self joins, keys, cardinality, duplicates, and missing relationships with ER context.
- **Tools and why:** Schema browser and join visualizer reveal row multiplication.
- **Prove:** Detect accidental Cartesian products, duplicate amplification, null-extended rows, and equivalent join syntax.
- **Ship:** Join module and cardinality diagnostics.

### M6D13 - Day 163 - Advanced join challenges

- **Build / learn:** Build multi-table business questions, anti/semi joins, duplicate-safe aggregation, and slowly changing relationship examples.
- **Tools and why:** EXPLAIN plans and row-count checkpoints provide process evidence beyond final output.
- **Prove:** Hidden cases defeat hardcoded IDs and assumptions about uniqueness or missing data.
- **Ship:** Advanced join pack and robust grader.

### M6D14 - Day 164 - Subqueries and CTEs

- **Build / learn:** Teach scalar/correlated/EXISTS subqueries, derived tables, CTE readability, recursion concepts, and materialization trade-offs.
- **Tools and why:** AST inspection provides targeted feedback; timeout prevents pathological recursion.
- **Prove:** Test multi-row scalar errors, null NOT IN trap, recursion limit, and equivalent EXISTS solutions.
- **Ship:** Subquery/CTE module.

### M6D15 - Day 165 - Views and data access

- **Build / learn:** Teach views, materialized views, permissions, security-barrier concepts, refresh, and stable analytical interfaces.
- **Tools and why:** Restricted roles demonstrate least privilege; migrations create disposable approved objects.
- **Prove:** Try privilege escalation, hidden-column access, stale materialized data, and unsafe updatable-view assumptions.
- **Ship:** Views/security lab module.

### M6D16 - Day 166 - Window functions

- **Build / learn:** Teach partition/order/frame, row_number/rank, lag/lead, running totals, moving averages, and tie behavior.
- **Tools and why:** Result visualizer highlights partitions and frames; semantic evaluator retains order.
- **Prove:** Test default frame surprises, ties, nulls, boundaries, and multiple valid formulations.
- **Ship:** Window-function challenge sequence.

### M6D17 - Day 167 - Transactions and concurrency labs

- **Build / learn:** Teach ACID, isolation, locks, deadlocks, lost update, optimistic control, and retry using coordinated sessions.
- **Tools and why:** PostgreSQL exposes authentic behavior; orchestrator synchronizes two learner transactions.
- **Prove:** Reproduce anomalies, deadlock victim, timeout, retry, and prove cleanup releases connections/locks.
- **Ship:** Concurrency lab engine and lessons.

### M6D18 - Day 168 - SQL mastery integration

- **Build / learn:** Map query evidence, hints, performance, and concurrency outcomes to skills, remediation, unlocks, XP, and achievements.
- **Tools and why:** Mastery service consumes normalized rubric components; outbox makes rewards safe.
- **Prove:** Replay attempts and verify consistent mastery/XP; alternate correct queries receive equivalent credit.
- **Ship:** Complete SQL progression path.

### M6D19 - Day 169 - Query-plan literacy

- **Build / learn:** Teach EXPLAIN/ANALYZE nodes, cost versus time, scans, joins, sorts, estimates, buffers, and safe interpretation.
- **Tools and why:** Plan JSON is parsed into a mobile visual; production-safe lab copies allow ANALYZE.
- **Prove:** Compare estimated/actual rows, cold/warm cache, and avoid declaring one run universally faster.
- **Ship:** Explain-plan viewer and curriculum.

### M6D20 - Day 170 - Index design labs

- **Build / learn:** Teach B-tree, composite order, selectivity, covering/partial/expression indexes, write cost, and unused indexes.
- **Tools and why:** Disposable schemas allow CREATE INDEX; pg_stat views and plans measure effects.
- **Prove:** Benchmark before/after with repeated trials and catch indexes that help one query while harming writes/storage.
- **Ship:** Index challenges and benchmark memo.

### M6D21 - Day 171 - Query optimization challenges

- **Build / learn:** Create slow-query cases for missing index, bad join, non-sargable predicate, over-fetch, N+1, and stale statistics.
- **Tools and why:** pg_stat_statements and plan comparison identify root cause; rubric scores reasoning and result correctness.
- **Prove:** Learner change must improve a defined workload, preserve results, and avoid forbidden hints/hardcoding.
- **Ship:** Optimization module and workload harness.

### M6D22 - Day 172 - SQL boss battle design

- **Build / learn:** Design “Database on Fire”: latency spike, lock contention, wrong report, index trade-off, and safe remediation under an incident brief.
- **Tools and why:** Scenario orchestrator controls workload; rubric weighs diagnosis, correctness, performance, and safety.
- **Prove:** Expert/novice pilots validate clues, duration, alternate fixes, and recovery path.
- **Ship:** Playable boss alpha and assessment blueprint.

### M6D23 - Day 173 - Boss battle implementation

- **Build / learn:** Add checkpoints, query/workload evidence, timer, partial credit, reset, reconnect, signed score, and postmortem.
- **Tools and why:** Server event log supports deterministic grading and appeals; snapshots restore database.
- **Prove:** Kill session/app, exceed limits, use alternate fix, and confirm no persistent shared-state corruption.
- **Ship:** End-to-end SQL boss and fault tests.

### M6D24 - Day 174 - SQL sandbox security audit

- **Build / learn:** Review roles, functions, extensions, COPY, large objects, locks, temp objects, query complexity, output, network, and cleanup.
- **Tools and why:** Restricted PostgreSQL config, proxy limits, SAST/DAST, and adversarial SQL corpus provide layers.
- **Prove:** No cross-tenant read, host file/network access, superuser action, unbounded resource use, or durable escape survives.
- **Ship:** Security report and containment runbook.

### M6D25 - Day 175 - SQL performance and capacity

- **Build / learn:** Measure session provisioning, query p95, plan parsing, grading, pool/CPU/I/O saturation, reset time, and cost per lab.
- **Tools and why:** k6, pg_stat_statements, Prometheus, and EXPLAIN ANALYZE expose limits.
- **Prove:** Document safe concurrency and graceful rejection/cancellation behavior beyond capacity.
- **Ship:** Capacity report and tuned quotas.

### M6D26 - Day 176 - SQL analytics and content review

- **Build / learn:** Review every query/solution, instrument error taxonomy/hints/resets/boss, reconcile events, and identify ambiguous questions.
- **Tools and why:** CI executes golden/alternate/negative solutions; dashboards distinguish curriculum from infrastructure failure.
- **Prove:** Zero broken fixture, ambiguous expected result, unlicensed data, or unowned high-failure lesson remains.
- **Ship:** Signed review and SQL learning dashboard.

### M6D27 - Day 177 - SQL accessibility and device QA

- **Build / learn:** Audit editor, schema tree, result grid, plans, timer, errors, font scaling, keyboard, and screen-reader alternatives.
- **Tools and why:** Maestro plus manual VoiceOver/TalkBack validates full journeys.
- **Prove:** Core lessons and boss can be completed without relying on color, wide tables, or precise gestures.
- **Ship:** Accessibility report and remediations.

### M6D28 - Day 178 - SQL release candidate

- **Build / learn:** Run ingest-author-publish-download-query-grade-progress-boss flow plus migrations, rollback, security, load, analytics, and support drills.
- **Tools and why:** Feature flags separate datasets, sandbox, and boss; release dashboard aggregates gates.
- **Prove:** Pilot completes world with correct grading and no data, isolation, or event reconciliation defect.
- **Ship:** Tagged `v0.6.0-rc1` and pilot report.

### M6D29 - Day 179 - SQL architecture case study

- **Build / learn:** Document data provenance, isolation, semantic grading, plan visualization, benchmark protocol, risks, and reproducible demo.
- **Tools and why:** MkDocs and pinned database/image artifacts let reviewers verify the system.
- **Prove:** Clean clone reproduces one query, alternative solution, timeout, and blocked privilege attack.
- **Ship:** Public SQL lab case study and demo.

### M6D30 - Day 180 - SQL World release

- **Build / learn:** Promote `v0.6-sql-world`, monitor staged cohorts, rehearse rollback, close milestone, and carry judge lessons into DSA.
- **Tools and why:** GitHub Release, dashboards, and retrospective complete evidence.
- **Prove:** Security, query, queue, grading, crash, and completion gates remain healthy after promotion.
- **Ship:** Release, retrospective, and DSA backlog.

# Month 7 - DSA World

**Monthly production goal:** Ship a multi-language code judging platform with deterministic tests, visual explanations, complexity evidence, and interview-grade assessments.

### M7D1 - Day 181 - DSA curriculum and judge RFC

- **Build / learn:** Map arrays through graphs/DP, difficulty rubric, languages, integrity policy, hidden tests, complexity expectations, and boss scope.
- **Tools and why:** Curriculum matrix links skills to problems; ADR records language/runtime support and grading philosophy.
- **Prove:** Review problems for originality/licensing, solvability, edge cases, and evidence beyond final output.
- **Ship:** DSA World RFC, problem schema, and coverage map.

### M7D2 - Day 182 - Problem package format

- **Build / learn:** Define statement, constraints, examples, starter code, function signature, public/hidden tests, oracle, limits, editorial, tags, and versions.
- **Tools and why:** JSON Schema/Pydantic validates packages; Git review versions problems and editorials.
- **Prove:** Reject ambiguous signatures, weak tests, impossible limits, leaked answers, duplicate IDs, and broken locales.
- **Ship:** Problem linter and authoring guide.

### M7D3 - Day 183 - Language runner images

- **Build / learn:** Build pinned Python, JavaScript/TypeScript, Java, and C++ images with non-root users, compilers, quotas, no egress, and SBOMs.
- **Tools and why:** Rootless containers isolate execution; cgroups/seccomp enforce limits; Trivy scans images.
- **Prove:** Attempt filesystem/network/process escapes, fork bombs, huge compile/output, and cross-run residue.
- **Ship:** Signed runner images and security baseline.

### M7D4 - Day 184 - Submission pipeline

- **Build / learn:** Implement submit, queue, compile, run cases, aggregate result, cancel, retry, TTL, idempotency, ownership, and signed receipt.
- **Tools and why:** SQS-compatible queue absorbs bursts; worker pool isolates languages; outbox records durable submissions.
- **Prove:** Test duplicate submit, worker crash, poison job, cancellation, queue saturation, and result replay.
- **Ship:** Submission API/worker and fault tests.

### M7D5 - Day 185 - Judge correctness model

- **Build / learn:** Create verdicts, exact/tolerant/unordered/custom comparison, stdout/stderr limits, per-case timing/memory, and deterministic environment.
- **Tools and why:** Comparator library centralizes truth; monotonic clock measures execution; schema versions preserve old results.
- **Prove:** Golden-test whitespace, float, Unicode, nondeterminism, timeout, memory, runtime, compile, and wrong-answer cases.
- **Ship:** Judge core and verdict matrix.

### M7D6 - Day 186 - Mobile code editor

- **Build / learn:** Build editor, language selector, starter reset, custom input, run versus submit, result panes, reconnect, drafts, keyboard controls, and accessibility fallback.
- **Tools and why:** Syntax editor provides mobile coding; local drafts prevent loss; TanStack Query tracks submissions.
- **Prove:** Test large code, app kill, offline draft, rotation, hardware keyboard, screen reader, and malicious output.
- **Ship:** Code challenge mobile experience.

### M7D7 - Day 187 - Arrays and strings lessons

- **Build / learn:** Author traversal, two pointers, sliding window, prefix sums, sorting, binary search, and string parsing with real constraints.
- **Tools and why:** Versioned problem packages and visual traces connect code to state changes.
- **Prove:** Run oracle/property tests and alternate solutions; hidden cases cover empty, duplicate, overflow, Unicode, and worst case.
- **Ship:** Arrays/strings module and reviewed problems.

### M7D8 - Day 188 - Hashing problems

- **Build / learn:** Teach sets/maps, counting, lookup trade-offs, collisions conceptually, and prefix-hash patterns.
- **Tools and why:** Judge cases include adversarial distributions; complexity rubric captures expected behavior.
- **Prove:** Reject quadratic solutions where constraints demand linear behavior using calibrated stress tests without flakiness.
- **Ship:** Hashing lesson/problem pack.

### M7D9 - Day 189 - Stack and queue problems

- **Build / learn:** Teach LIFO/FIFO, monotonic structures, parsing, BFS queues, and deque applications.
- **Tools and why:** Trace events display structure state; hidden tests cover deep inputs and boundary conditions.
- **Prove:** Test recursion/stack limits, empty operations, duplicates, and worst-case sequences.
- **Ship:** Stack/queue module and visual traces.

### M7D10 - Day 190 - Linked-list labs

- **Build / learn:** Teach pointer movement, reversal, cycle detection, merging, dummy nodes, and ownership pitfalls with node-ID visualization.
- **Tools and why:** Custom serializers build lists/cycles safely; visualizer renders identity rather than values alone.
- **Prove:** Test empty/single/cycle/shared-tail cases and ensure serializers never hang.
- **Ship:** Linked-list module and golden cases.

### M7D11 - Day 191 - Tree representation and traversal

- **Build / learn:** Teach binary/n-ary trees, DFS/BFS, recursion/iteration, height, BST invariants, and serialization.
- **Tools and why:** Tree visualizer consumes bounded traces; property generators create valid/invalid trees.
- **Prove:** Test skewed/deep/duplicate/empty trees, recursion limits, and stable serialization.
- **Ship:** Tree foundations module.

### M7D12 - Day 192 - Tree challenge set

- **Build / learn:** Build LCA, path, validation, construction, balancing concepts, and heap/trie comparisons at appropriate levels.
- **Tools and why:** Hypothesis validates oracle invariants; stress tiers check expected complexity.
- **Prove:** Cross-check two independent reference solutions and mutate tests to confirm hidden cases catch defects.
- **Ship:** Reviewed tree problem set and editorial.

### M7D13 - Day 193 - Complexity evidence engine

- **Build / learn:** Estimate operation growth from calibrated input tiers, combine with static expectations, and report uncertainty instead of fake Big-O proof.
- **Tools and why:** Benchmark harness and profiler collect runtime/memory; rubric stores declared complexity.
- **Prove:** Repeat across noisy runs, detect regressions, and avoid penalizing correct solutions due to infrastructure variance.
- **Ship:** Complexity report feature and methodology ADR.

### M7D14 - Day 194 - Graph data model and visualization

- **Build / learn:** Define directed/undirected, weighted, labeled graphs, adjacency forms, stable layout, traversal events, and accessible table view.
- **Tools and why:** Graph library validates fixtures; canvas/SVG renders; deterministic seed stabilizes screenshots/tests.
- **Prove:** Test disconnected, cyclic, parallel-edge, self-loop, large, and directed cases.
- **Ship:** Graph renderer and fixture generator.

### M7D15 - Day 195 - BFS and DFS lessons

- **Build / learn:** Teach visited state, traversal order, components, shortest unweighted path, cycle detection, and recursion/iteration trade-offs.
- **Tools and why:** Trace-enabled references explain frontier and visited sets; judge accepts valid order variants where appropriate.
- **Prove:** Hidden tests cover disconnected graphs, alternate valid traversal, deep graph, and duplicates.
- **Ship:** Traversal module and problem pack.

### M7D16 - Day 196 - Shortest path and spanning concepts

- **Build / learn:** Teach Dijkstra, Bellman-Ford concepts, topological shortest paths, union-find, MST, and applicability constraints.
- **Tools and why:** Weighted graph fixtures and trace viewer expose relaxations; oracle cross-checks outputs.
- **Prove:** Test negative edges/cycles, overflow, disconnected graphs, equal paths, and invalid algorithm choice.
- **Ship:** Weighted-graph module.

### M7D17 - Day 197 - Dynamic programming foundations

- **Build / learn:** Teach state, transition, base case, order, memoization/tabulation, reconstruction, and space optimization.
- **Tools and why:** DP table visualizer renders state/evidence; trace caps prevent huge payloads.
- **Prove:** Test off-by-one, impossible state, negative values, reconstruction ties, and complexity limits.
- **Ship:** DP foundations module.

### M7D18 - Day 198 - DP challenge set

- **Build / learn:** Build knapsack, subsequence, grid, interval, and tree-DP problems with progressive hints and editorials.
- **Tools and why:** Oracle/brute-force generators validate small cases; optimized references validate constraints.
- **Prove:** Differential-test optimized solutions against brute force on randomized small inputs.
- **Ship:** DP problem pack and differential tests.

### M7D19 - Day 199 - Greedy reasoning module

- **Build / learn:** Teach exchange argument, invariants, interval scheduling, heaps, and when greedy fails through paired counterexamples.
- **Tools and why:** Counterexample generator and visual timelines make proof obligations concrete.
- **Prove:** Each greedy task includes a failing naive rule and tests that expose it.
- **Ship:** Greedy lessons, problems, and proof rubrics.

### M7D20 - Day 200 - DSA mastery and recommendations

- **Build / learn:** Map problem evidence, attempts, hints, complexity, topic/difficulty, and recency to mastery and next-problem selection.
- **Tools and why:** Mastery engine stays explainable; recommendation policy uses constraints before personalization.
- **Prove:** Replay histories, test cold start, avoid repetition/locked content, and audit difficulty fairness.
- **Ship:** DSA progression integration.

### M7D21 - Day 201 - Integrity and abuse controls

- **Build / learn:** Add rate limits, hidden-test secrecy, plagiarism-signal hooks, suspicious timing, result signing, and appealable review without invasive surveillance.
- **Tools and why:** Audit logs and explainable rules support moderation; secrets remain only in worker boundary.
- **Prove:** Try test extraction, forged verdict, rapid replay, code/output exfiltration, and cross-user submission access.
- **Ship:** Integrity threat model and adversarial suite.

### M7D22 - Day 202 - DSA boss battle design

- **Build / learn:** Design interview gauntlet with clarification, two problems, complexity explanation, tests, trade-off memo, timer, and partial credit.
- **Tools and why:** Assessment state machine captures process; rubric scores correctness, testing, reasoning, and communication.
- **Prove:** Expert/novice pilots calibrate time/difficulty and validate alternate optimal solutions.
- **Ship:** Playable DSA boss alpha.

### M7D23 - Day 203 - Boss battle implementation

- **Build / learn:** Implement timed stages, autosaved code, run budget, reconnect, judge integration, rubric, feedback embargo, and signed result.
- **Tools and why:** Server clock prevents manipulation; immutable events support scoring and appeals.
- **Prove:** Kill app/worker, exceed run budget, reconnect, and solve through alternate languages/approaches.
- **Ship:** End-to-end boss battle with resilience tests.

### M7D24 - Day 204 - Judge security audit

- **Build / learn:** Review images, compilers, syscalls, filesystem, network, secrets, output, artifact cleanup, queue permissions, and patch cadence.
- **Tools and why:** Seccomp/rootless runtime, egress deny, Trivy/SBOM, and attack corpus enforce containment.
- **Prove:** No host/cross-user access, persistence, secret read, privilege gain, or unbounded resource use survives.
- **Ship:** Security report and runner incident runbook.

### M7D25 - Day 205 - Judge capacity and cost

- **Build / learn:** Benchmark compile/run/queue p95, cold images, concurrency per language, memory, cleanup, autoscaling, and cost per submission.
- **Tools and why:** k6 plus Prometheus profiles mixed workloads; queue age drives scaling.
- **Prove:** Document safe capacity, noisy-neighbor behavior, and graceful overload with retry guidance.
- **Ship:** Capacity report and autoscaling policy.

### M7D26 - Day 206 - DSA analytics and quality review

- **Build / learn:** Instrument funnel, verdicts, attempts, hint use, runtime, problem discrimination, infrastructure errors, and mastery; review every problem.
- **Tools and why:** PostHog/warehouse queries and CI golden/mutation tests expose weak content.
- **Prove:** Reconcile submissions/events and remove ambiguous, leaky, discriminatory, or infra-dominated problems.
- **Ship:** DSA dashboard and signed content review.

### M7D27 - Day 207 - DSA accessibility and device QA

- **Build / learn:** Audit editor, results, visualizers, timers, tables, keyboard, font scaling, color, and assistive-technology flow.
- **Tools and why:** Maestro plus manual VoiceOver/TalkBack validates core and boss journeys.
- **Prove:** Users can solve without animation, drag gestures, color-only status, or inaccessible canvas content.
- **Ship:** Accessibility report and remediations.

### M7D28 - Day 208 - DSA release candidate

- **Build / learn:** Run author-publish-solve-judge-progress-boss plus migrations, rollback, security, load, analytics, support, and multi-language compatibility.
- **Tools and why:** Feature flags isolate languages, judge, and boss; release dashboard gates cohorts.
- **Prove:** Pilot completes world with stable grading and no isolation, lost-code, or event mismatch blocker.
- **Ship:** Tagged `v0.7.0-rc1` and pilot report.

### M7D29 - Day 209 - DSA architecture case study

- **Build / learn:** Document judge pipeline, sandbox threat model, semantic verdicts, complexity methodology, benchmarks, limitations, and clean demo.
- **Tools and why:** MkDocs plus pinned images/problem versions make claims reproducible.
- **Prove:** Clean clone reproduces accepted/wrong/timeout verdicts and one blocked escape test.
- **Ship:** Public DSA judge case study and demo.

### M7D30 - Day 210 - DSA World release

- **Build / learn:** Promote `v0.7-dsa-world`, monitor staged rollout, drill rollback, close milestone, and plan Debug Dungeon reuse of telemetry.
- **Tools and why:** GitHub Release and dashboards complete proof.
- **Prove:** Security, queue, judge, lost-draft, crash, and completion gates remain healthy.
- **Ship:** Release, retrospective, and Debug Dungeon backlog.

# Month 8 - Debug Dungeon

**Monthly production goal:** Ship incident-based learning where users correlate logs, metrics, traces, code, and changes to diagnose realistic failures and write postmortems.

### M8D1 - Day 211 - Debug curriculum and incident model

- **Build / learn:** Define observe-hypothesize-test-fix-verify loop, incident taxonomy, evidence rules, scoring, safe simulations, and boss scope.
- **Tools and why:** Incident schema versions symptoms, telemetry, topology, changes, root cause, remediations, and distractors.
- **Prove:** Experts review realism; every incident must have sufficient evidence and no single magic-string answer.
- **Ship:** Debug Dungeon RFC and incident catalog.

### M8D2 - Day 212 - Telemetry fixture pipeline

- **Build / learn:** Create deterministic JSON logs, metrics, traces, deploy events, configs, and topology fixtures with aligned clocks and correlation IDs.
- **Tools and why:** OpenTelemetry format keeps artifacts realistic; generator seeds preserve replayability.
- **Prove:** Validate cross-signal timestamps, trace/log links, PII redaction, and corruption/error fixtures.
- **Ship:** Telemetry generator and golden incidents.

### M8D3 - Day 213 - Incident session state machine

- **Build / learn:** Implement briefing, evidence exploration, hypothesis, action, verification, resolution, timeout, reset, and postmortem states.
- **Tools and why:** Append-only event log supports replay/scoring; server clock and idempotency protect integrity.
- **Prove:** Reject illegal transitions, duplicate actions, stale clients, clock changes, and cross-user sessions.
- **Ship:** Incident service/API and property tests.

### M8D4 - Day 214 - Log explorer mobile UI

- **Build / learn:** Build search, filters, severity/service/time facets, context expansion, correlation links, saved evidence, and accessible text views.
- **Tools and why:** Virtualized list handles volume; structured query grammar avoids arbitrary backend queries.
- **Prove:** Test 100k fixture lines through pagination, malicious log text, locale/timezone, offline bundle, and screen reader.
- **Ship:** Log explorer and E2E scenario.

### M8D5 - Day 215 - Metrics and trace explorer

- **Build / learn:** Build chart panels, exemplars, trace waterfall, span detail, deployment markers, annotations, and nonvisual summaries.
- **Tools and why:** OpenTelemetry data model aligns signals; lightweight charts render bounded series.
- **Prove:** Test missing/out-of-order points, high cardinality, broken traces, clock skew, and accessible data tables.
- **Ship:** Metrics/trace explorer with correlation flow.

### M8D6 - Day 216 - Stack-trace fundamentals

- **Build / learn:** Teach exception chains, frames, source maps, async traces, cause versus symptom, and redaction using Python/JS examples.
- **Tools and why:** Source viewer maps sanitized frames to repository snapshots.
- **Prove:** Learners identify first relevant application frame across wrappers, retries, and multiple exceptions.
- **Ship:** Stack-trace lesson pack and rubric.

### M8D7 - Day 217 - Structured logging lessons

- **Build / learn:** Teach levels, fields, context, correlation IDs, sampling, redaction, and querying without regex-only habits.
- **Tools and why:** JSON log fixtures and query builder provide authentic practice.
- **Prove:** Hidden incidents require field joins and distinguish absent events from filtered/sampled events.
- **Ship:** Logging module and challenges.

### M8D8 - Day 218 - Exception-handling challenges

- **Build / learn:** Build swallowed error, broad catch, lost context, retry masking, async cancellation, and user-safe error scenarios.
- **Tools and why:** Runnable code snapshots and tests let learners patch behavior in sandbox.
- **Prove:** Fix must preserve contracts, logging, cancellation, and sensitive-data rules across hidden tests.
- **Ship:** Exception challenge set.

### M8D9 - Day 219 - Debug foundations checkpoint

- **Build / learn:** Integrate attempts, hints, mastery, XP, analytics, offline incident bundles, and support replay for first incidents.
- **Tools and why:** Existing learning/event contracts prevent special-case scoring.
- **Prove:** Pilot learners solve incidents using evidence; separate unclear clues from UI/platform defects.
- **Ship:** Debug alpha and pilot report.

### M8D10 - Day 220 - HTTP failure taxonomy

- **Build / learn:** Teach DNS/connect/TLS/request/response timeouts, status semantics, retries, idempotency, rate limits, and client/server ownership.
- **Tools and why:** Private fault proxy injects delays, resets, malformed responses, and codes deterministically.
- **Prove:** Learners distinguish failure phase and choose bounded retry/timeout behavior without causing storms.
- **Ship:** HTTP debugging module and fault fixtures.

### M8D11 - Day 221 - API contract failures

- **Build / learn:** Create schema drift, wrong content type, pagination bug, partial response, version mismatch, and backward-compatibility incidents.
- **Tools and why:** OpenAPI diff and Schemathesis generate contract evidence; trace explorer shows failure propagation.
- **Prove:** Fixes pass old/new clients and negative contract tests; no “just make field optional” shortcut.
- **Ship:** API incident pack.

### M8D12 - Day 222 - Distributed retry incident

- **Build / learn:** Simulate timeout plus retry amplification across mobile/API/worker/provider, with queue and dependency saturation.
- **Tools and why:** Toxiproxy and load generator create controlled faults; metrics expose retry volume.
- **Prove:** Learner must cap retries, add jitter/idempotency, and prove recovery without duplicates.
- **Ship:** Retry-storm scenario and benchmark.

### M8D13 - Day 223 - Cache incident module

- **Build / learn:** Teach stale data, stampede, key collision, TTL, invalidation, negative caching, and consistency trade-offs.
- **Tools and why:** Redis fault fixtures and database truth enable comparison.
- **Prove:** Learner diagnoses from hit rate/latency/data mismatch and verifies safe cache repair.
- **Ship:** Cache debugging incidents.

### M8D14 - Day 224 - Database query incidents

- **Build / learn:** Create missing index, N+1, poor plan, pool exhaustion, long transaction, and lock-wait scenarios.
- **Tools and why:** pg_stat views, traces, and plans provide evidence; workload harness reproduces safely.
- **Prove:** Fix must improve defined workload, preserve correctness, and not merely raise limits.
- **Ship:** Database performance incident pack.

### M8D15 - Day 225 - Deadlock and isolation incidents

- **Build / learn:** Build deadlock, lost update, serialization failure, and stale-read cases with coordinated transactions.
- **Tools and why:** PostgreSQL locks and deterministic orchestrator make behavior reproducible.
- **Prove:** Learner identifies wait graph, changes transaction/lock strategy, and passes concurrency regression tests.
- **Ship:** Concurrency incident module.

### M8D16 - Day 226 - Migration failure incident

- **Build / learn:** Simulate blocking DDL, incompatible app/schema versions, partial backfill, bad default, and rollback constraints.
- **Tools and why:** Expand-contract migrations and preview traffic replay teach safe rollout.
- **Prove:** Learner writes repair/roll-forward plan and proves old/new versions coexist during migration.
- **Ship:** Migration incident and runbook exercise.

### M8D17 - Day 227 - Memory leak lesson

- **Build / learn:** Teach heap growth, retention, cache leaks, listener leaks, file handles, and allocation versus RSS using bounded services.
- **Tools and why:** Python/Node profilers and metrics produce controlled evidence.
- **Prove:** Learner locates retaining path, fixes it, and demonstrates flat memory under repeated workload.
- **Ship:** Memory leak scenario and before/after profile.

### M8D18 - Day 228 - CPU and event-loop incident

- **Build / learn:** Create hot loop, expensive serialization, regex backtracking, blocking async call, and lock contention.
- **Tools and why:** Profilers/flamegraphs reveal hotspots; k6 recreates latency.
- **Prove:** Fix reduces CPU/p95 without changing results; regression benchmark runs in CI with tolerance.
- **Ship:** CPU incident pack and benchmark.

### M8D19 - Day 229 - Resource exhaustion incident

- **Build / learn:** Simulate file descriptors, connections, disk, queue, threads, and worker starvation with quotas.
- **Tools and why:** cgroups and service limits keep simulations safe; dashboards expose saturation.
- **Prove:** Learner identifies finite resource, leak/admission issue, and proves cleanup/backpressure.
- **Ship:** Resource incident module.

### M8D20 - Day 230 - Production incident boss design

- **Build / learn:** Design “Launch-Day Outage”: deploy change, latency, retries, database contention, misleading alert, rollback decision, communication, and postmortem.
- **Tools and why:** Scenario orchestrator coordinates faults and evidence timeline.
- **Prove:** SRE review validates realism, safe actions, alternate diagnosis paths, and grading fairness.
- **Ship:** Playable outage boss alpha.

### M8D21 - Day 231 - Incident action engine

- **Build / learn:** Implement approved actions such as inspect, compare, flag-disable, rollback, restart, scale, query, and patch with consequences/cooldowns.
- **Tools and why:** Typed command catalog prevents arbitrary infrastructure access; event sourcing records causal sequence.
- **Prove:** Attempt unauthorized/destructive actions, replay, stale action, and invalid sequence; state remains recoverable.
- **Ship:** Action engine and authorization tests.

### M8D22 - Day 232 - Postmortem workflow

- **Build / learn:** Require impact, timeline, detection, root cause, contributing factors, resolution, corrective actions, owners, and blameless language.
- **Tools and why:** Structured template and rubric assess engineering communication; admin review supports feedback.
- **Prove:** Compare against evidence timeline, reject invented facts, and ensure actions are specific and testable.
- **Ship:** Postmortem editor, rubric, and example.

### M8D23 - Day 233 - Debug mastery and rewards

- **Build / learn:** Map evidence quality, hypothesis discipline, action safety, resolution, time, hints, and postmortem to skills/XP/unlocks.
- **Tools and why:** Explainable scoring engine separates learning performance from platform faults.
- **Prove:** Replay sessions, test alternate valid paths, and prevent speed-only or risky actions from gaming score.
- **Ship:** Integrated Debug progression.

### M8D24 - Day 234 - Debug analytics and efficacy

- **Build / learn:** Track evidence views, hypotheses, actions, resets, hints, time-to-diagnose/mitigate, rubric dimensions, and simulator failures.
- **Tools and why:** Warehouse queries distinguish curriculum difficulty from infrastructure/UI problems.
- **Prove:** Reconcile incident events and review high-failure points with session replays stripped of secrets.
- **Ship:** Debug Dungeon dashboards.

### M8D25 - Day 235 - Scenario authoring admin

- **Build / learn:** Build incident editor, topology/telemetry upload, timeline preview, action graph, rubric, validation, review, and publish.
- **Tools and why:** Next.js shared schema prevents runtime drift; fixture generator creates preview data.
- **Prove:** Block missing clues, impossible action graph, PII, invalid timelines, and self-approved critical changes.
- **Ship:** Incident authoring workflow.

### M8D26 - Day 236 - Debug security and privacy audit

- **Build / learn:** Review logs/traces/source for secrets/PII, query limits, injection, session access, admin uploads, sandbox actions, and retention.
- **Tools and why:** Redaction scanner, MIME checks, RBAC, CSP, rate limits, and audit logs reduce exposure.
- **Prove:** Malicious telemetry cannot execute UI content, reveal secrets, cross users, or trigger unapproved actions.
- **Ship:** Security/privacy report and retention rules.

### M8D27 - Day 237 - Debug performance and capacity

- **Build / learn:** Benchmark large logs, chart points, trace spans, concurrent sessions, event replay, scenario load, and cost.
- **Tools and why:** k6, mobile profiler, Prometheus, and pagination/downsampling reveal limits.
- **Prove:** Meet interaction and API p95 budgets and degrade by sampling/pagination rather than crashing.
- **Ship:** Capacity report and optimized explorers.

### M8D28 - Day 238 - Debug accessibility and device QA

- **Build / learn:** Audit log/trace/metric explorers, charts, timelines, actions, timers, postmortem, keyboard, color, and font scaling.
- **Tools and why:** Maestro plus manual assistive-tech tests cover complete incident flow.
- **Prove:** Boss can be solved through tables/text without color-only charts or precision gestures.
- **Ship:** Accessibility report and remediations.

### M8D29 - Day 239 - Debug release candidate

- **Build / learn:** Run author-publish-download-investigate-act-resolve-postmortem flow plus rollback, security, load, analytics, and support drills.
- **Tools and why:** Feature flags isolate explorers, actions, and boss; release dashboard aggregates gates.
- **Prove:** Pilot solves representative incidents with deterministic scoring and no telemetry/privacy blocker.
- **Ship:** Tagged `v0.8.0-rc1` and pilot report.

### M8D30 - Day 240 - Debug Dungeon release

- **Build / learn:** Promote `v0.8-debug-dungeon`, monitor staged rollout, drill disable/rollback, close milestone, and reuse fault platform in later phases.
- **Tools and why:** GitHub Release and dashboards complete evidence.
- **Prove:** Privacy, simulator, scoring, p95, crash, and completion gates remain healthy.
- **Ship:** Release, retrospective, and Network/Security backlog.

# Month 9 - Networking and Security Worlds

**Monthly production goal:** Ship private packet-flow simulations and safe security labs that teach diagnosis and defense without exposing real targets.

### M9D1 - Day 241 - Networking curriculum and topology model

- **Build / learn:** Define IP/subnet/DNS/routing/TCP/UDP/HTTP/TLS/load-balancing skills, private topology schema, safe actions, and boss.
- **Tools and why:** Graph schema models hosts/interfaces/routes/services; ADR fixes simulation fidelity and limitations.
- **Prove:** Network engineers review correctness; every lab has observable packets/state, not trivia alone.
- **Ship:** Networking RFC, topology schema, and skill map.

### M9D2 - Day 242 - Subnet calculator and visual lab

- **Build / learn:** Build IPv4/CIDR parsing, network/broadcast/range, subnet allocation, validation, and accessible visualization.
- **Tools and why:** Python `ipaddress` provides correct primitives; property tests cover address spaces.
- **Prove:** Test boundaries, invalid masks, overlapping allocations, reserved ranges, and randomized round trips.
- **Ship:** Subnet engine, mobile lab, and property tests.

### M9D3 - Day 243 - Packet event simulator

- **Build / learn:** Model ARP-like resolution, routing hops, TTL, TCP/UDP packets, drops, latency, NAT concepts, and deterministic clock.
- **Tools and why:** Discrete-event simulation provides safe repeatability; typed events feed visualizer.
- **Prove:** Golden-test routes, loops, TTL expiry, unreachable networks, drops, and seeded replay.
- **Ship:** Packet simulator core and trace fixtures.

### M9D4 - Day 244 - Packet-flow mobile UI

- **Build / learn:** Render topology, hop timeline, packet detail, filters, play/step, and text/table alternative.
- **Tools and why:** Canvas/SVG visualizes paths; virtualized event list and reduced motion keep it accessible.
- **Prove:** Test large traces, zoom, narrow devices, color blindness, screen readers, and malicious labels.
- **Ship:** Packet-flow lab UI and E2E test.

### M9D5 - Day 245 - IP addressing lessons

- **Build / learn:** Author binary/prefix concepts, private/public, loopback, link-local, subnetting, gateways, and troubleshooting tasks.
- **Tools and why:** Realistic private fixtures connect calculations to routing state.
- **Prove:** Alternate valid subnet plans pass constraints; hidden cases catch overlap and wasted-space errors.
- **Ship:** IP/subnet module.

### M9D6 - Day 246 - DNS resolver simulation

- **Build / learn:** Implement zones, records, recursion, caching, TTL, negative caching, CNAME chains, split horizon, and failures.
- **Tools and why:** Deterministic resolver avoids public DNS; cache state is inspectable.
- **Prove:** Test loops, stale/negative cache, missing record, propagation-like version changes, and poisoned input rejection.
- **Ship:** DNS simulator and lessons.

### M9D7 - Day 247 - Routing labs

- **Build / learn:** Teach tables, longest-prefix match, default route, asymmetric path, NAT concepts, and traceroute interpretation.
- **Tools and why:** Topology engine computes routes; packet timeline exposes decisions.
- **Prove:** Test equal routes, loops, blackholes, wrong gateway, and alternate repair actions.
- **Ship:** Routing module and challenges.

### M9D8 - Day 248 - TCP and UDP labs

- **Build / learn:** Teach handshake, sequence/ack concepts, retransmission, flow/congestion concepts, connection states, and UDP trade-offs.
- **Tools and why:** Discrete events visualize behavior without packet injection privileges.
- **Prove:** Simulate loss, reordering, duplicate, reset, timeout, and verify state transitions.
- **Ship:** Transport module and trace tests.

### M9D9 - Day 249 - HTTP TLS load-balancing labs

- **Build / learn:** Teach request lifecycle, TLS trust concepts, proxies, health checks, algorithms, sticky sessions, and failure modes.
- **Tools and why:** Private services/fault proxy generate authentic logs and traces; certificates are lab-only.
- **Prove:** Diagnose expired cert, unhealthy target, retry storm, uneven load, and header trust issue.
- **Ship:** Application-networking module.

### M9D10 - Day 250 - Networking checkpoint

- **Build / learn:** Integrate progression, hints, XP, analytics, offline topology bundles, and support replay.
- **Tools and why:** Existing learning contracts keep scoring consistent; feature flag controls pilot.
- **Prove:** Pilot learners diagnose five faults; simulator replay and displayed path must match.
- **Ship:** Networking alpha and pilot report.

### M9D11 - Day 251 - Networking boss battle

- **Build / learn:** Design and implement “The Unreachable Service” across subnet, DNS, route, TLS, and load balancer with checkpoints and rubric.
- **Tools and why:** Scenario state machine coordinates topology and evidence; server clock signs results.
- **Prove:** Expert/novice pilots validate clues, alternate fixes, reconnect, reset, and deterministic score.
- **Ship:** End-to-end networking boss.

### M9D12 - Day 252 - Network simulator security/load review

- **Build / learn:** Audit input sizes, graph complexity, label injection, session access, resource limits, then benchmark large topologies/concurrency.
- **Tools and why:** Property tests, k6, CSP, quotas, and Prometheus cover abuse and capacity.
- **Prove:** No cross-user access/UI injection/unbounded computation; document safe scale and overload behavior.
- **Ship:** Security and capacity report.

### M9D13 - Day 253 - Security curriculum and ethics gate

- **Build / learn:** Define defensive scope, OWASP concepts, legal/ethical rules, private targets, disclosure guidance, safe payloads, and boss.
- **Tools and why:** Threat-model matrix links vulnerability to control and verification.
- **Prove:** Security reviewer confirms no task targets public systems or teaches uncontrolled exploitation.
- **Ship:** Security World RFC and learner conduct gate.

### M9D14 - Day 254 - Authentication lessons

- **Build / learn:** Teach password storage, MFA concepts, sessions, tokens, refresh rotation, revocation, enumeration, and recovery using EngineerQuest examples.
- **Tools and why:** Instrumented mock app exposes safe auth traces; attack actions are allowlisted.
- **Prove:** Labs cover replay, fixation, brute force, weak reset, and secure remediation without real credentials.
- **Ship:** Authentication module.

### M9D15 - Day 255 - Authorization lessons

- **Build / learn:** Teach RBAC/ABAC, least privilege, object/function-level access, tenant isolation, deny-by-default, and policy testing.
- **Tools and why:** Mock API and policy matrix create IDOR/BOLA scenarios safely.
- **Prove:** Learner must fix cross-user/object access and pass complete negative role matrix.
- **Ship:** Authorization module and tests.

### M9D16 - Day 256 - JWT lab

- **Build / learn:** Build inspect/sign/verify simulation for claims, algorithms, issuer/audience, expiry, key rotation, and storage risks with lab keys.
- **Tools and why:** JWT library performs real verification; private JWKS fixture avoids external systems.
- **Prove:** Test alg confusion defenses, expired/not-before, wrong audience, key rollover, and token leakage.
- **Ship:** JWT security lab.

### M9D17 - Day 257 - OWASP threat-model lab

- **Build / learn:** Teach data-flow diagrams, trust boundaries, STRIDE, abuse cases, risk ranking, controls, and verification.
- **Tools and why:** Threat-model template and attack trees structure reasoning.
- **Prove:** Learner model must cover mobile/API/admin/runner/AI boundaries and link risks to tests.
- **Ship:** Threat-model lesson and scored artifact.

### M9D18 - Day 258 - Injection labs

- **Build / learn:** Create safe SQL/command/template injection scenarios in disposable mock services and require parameterization/allowlists.
- **Tools and why:** Private containers isolate vulnerable code; SAST rules reinforce fixes.
- **Prove:** Payloads cannot reach host/network; fixes pass positive/negative tests and retain functionality.
- **Ship:** Injection module and containment evidence.

### M9D19 - Day 259 - XSS and content injection labs

- **Build / learn:** Teach stored/reflected/DOM concepts, contextual encoding, sanitization, CSP, and mobile WebView risk using local pages.
- **Tools and why:** Browser test harness and CSP reports show behavior; sanitizer handles approved rich text.
- **Prove:** Mutation payload corpus cannot execute after remediation; accessibility/content remains intact.
- **Ship:** XSS/content module.

### M9D20 - Day 260 - CSRF CORS SSRF lessons

- **Build / learn:** Teach browser credentials, anti-CSRF, SameSite, origin policy, CORS, server-side fetch allowlists, and metadata-service risk.
- **Tools and why:** Mock origins and private URL service reproduce behavior safely.
- **Prove:** Test preflight, credentialed origins, token binding, redirects, DNS rebinding concept fixtures, and blocked private ranges.
- **Ship:** Web boundary module.

### M9D21 - Day 261 - Secrets and supply-chain lessons

- **Build / learn:** Teach secret lifecycle, Git leaks, dependency pinning, SBOM, provenance, vulnerable packages, and rotation response.
- **Tools and why:** Gitleaks, Dependabot, Trivy, and SBOM tools provide real defensive evidence.
- **Prove:** Seed lab-only secret/vulnerability, detect it, rotate/remove it, and verify clean history/build.
- **Ship:** Supply-chain module and response exercise.

### M9D22 - Day 262 - Rate limiting and abuse defense

- **Build / learn:** Teach quotas, token bucket/sliding window, identity dimensions, distributed limits, challenge escalation, and false positives.
- **Tools and why:** Redis implements lab limiter; k6 generates controlled abuse.
- **Prove:** Test burst, distributed clients, proxy headers, clock/Redis outage, and legitimate recovery.
- **Ship:** Abuse-defense lab and benchmark.

### M9D23 - Day 263 - Audit logging and detection

- **Build / learn:** Teach security event schemas, tamper evidence concepts, alerts, privacy, retention, investigation, and response.
- **Tools and why:** Structured audit stream and SIEM-like queries power scenarios.
- **Prove:** Detect credential stuffing/IDOR/admin misuse while redacting secrets and avoiding noisy alerts.
- **Ship:** Detection module and alert rules.

### M9D24 - Day 264 - Security boss battle design

- **Build / learn:** Design “Compromised Learning Platform”: auth anomaly, IDOR, secret leak, malicious content, containment, recovery, and report.
- **Tools and why:** Scenario orchestrator reuses Debug Dungeon evidence/action engine.
- **Prove:** Blue-team review validates clues, safe actions, scoring, and alternate containment paths.
- **Ship:** Playable security boss alpha.

### M9D25 - Day 265 - Security boss implementation

- **Build / learn:** Implement triage, containment actions, evidence preservation, remediation tests, communication, and post-incident report.
- **Tools and why:** Immutable event log supports scoring; allowlisted actions prevent destructive behavior.
- **Prove:** Test reconnect/reset, unauthorized action, alternate fix, and deterministic recovery/score.
- **Ship:** End-to-end security boss.

### M9D26 - Day 266 - Security platform penetration test

- **Build / learn:** Assess mobile/API/admin/runners/simulators for auth, authorization, injection, upload, secrets, dependencies, and business logic.
- **Tools and why:** OWASP ASVS/MASVS checklists, Semgrep, DAST, Trivy, and manual tests provide coverage.
- **Prove:** Critical/high issues block release; residual risk requires owner, rationale, and due date.
- **Ship:** Pen-test report and remediation PRs.

### M9D27 - Day 267 - Network/security analytics and review

- **Build / learn:** Instrument lab failures, hints, mastery, simulator errors, suspicious abuse, and learning outcomes; technically review all content.
- **Tools and why:** Dashboards and CI golden scenarios expose ambiguity or platform-driven failures.
- **Prove:** Reconcile events and remove unsafe, inaccurate, flaky, or unfair tasks.
- **Ship:** Signed content review and dashboards.

### M9D28 - Day 268 - Accessibility and device QA

- **Build / learn:** Audit topology, packet timelines, security forms, evidence, boss actions, keyboard, color, motion, and screen readers.
- **Tools and why:** Maestro and manual assistive-tech testing validate complete paths.
- **Prove:** Worlds remain completable via text/table alternatives without color-only or precision gestures.
- **Ship:** Accessibility report and remediations.

### M9D29 - Day 269 - Release candidate

- **Build / learn:** Run publish-download-simulate-diagnose-secure-boss plus rollback, privacy, security, load, analytics, and support drills.
- **Tools and why:** Feature flags isolate each simulator/world; release dashboard gates cohorts.
- **Prove:** Pilot shows deterministic state/scoring with no ethical, isolation, or data blocker.
- **Ship:** Tagged `v0.9.0-rc1` and pilot report.

### M9D30 - Day 270 - Network and Security release

- **Build / learn:** Promote `v0.9-network-security`, monitor, drill rollback/kill switches, close milestone, and open cloud readiness gaps.
- **Tools and why:** GitHub Release and dashboards complete evidence.
- **Prove:** Isolation, security, latency, scoring, crash, and completion gates stay healthy.
- **Ship:** Release, retrospective, and Cloud/DevOps backlog.

# Month 10 - Cloud and DevOps World plus production infrastructure

**Monthly production goal:** Teach cloud/DevOps through safe simulations while building the real staged AWS platform with IaC, CI/CD, SLOs, and disaster recovery.

### M10D1 - Day 271 - Cloud curriculum and real-infra boundary

- **Build / learn:** Define IAM/compute/storage/network/database/container/Kubernetes/IaC skills, simulation fidelity, cost ceiling, account boundaries, and boss.
- **Tools and why:** AWS Well-Architected questions frame trade-offs; ADR separates lab simulation from production credentials.
- **Prove:** Review for current terminology, least privilege, no learner cloud keys, and measurable outcomes.
- **Ship:** Cloud/DevOps RFC, cost budget, and skill map.

### M10D2 - Day 272 - AWS organization and identity baseline

- **Build / learn:** Create separate environments/accounts where available, GitHub OIDC, least-privilege deploy roles, MFA/root protections, budgets, and audit trail.
- **Tools and why:** IAM and OIDC remove static CI keys; CloudTrail and budgets detect misuse/spend.
- **Prove:** Attempt denied actions, rotate trust, trigger budget alarm, and document break-glass access.
- **Ship:** Identity baseline and access runbook.

### M10D3 - Day 273 - Terraform foundation

- **Build / learn:** Create modules/state backend/locking, provider pinning, validation, plan review, drift policy, tagging, and cost checks.
- **Tools and why:** Terraform makes infrastructure reviewable; tfsec/Checkov and Infracost catch risk/cost before apply.
- **Prove:** Apply/destroy preview, simulate drift, restore lock/state, and ensure destructive plans require approval.
- **Ship:** `infra/terraform` baseline and ADRs.

### M10D4 - Day 274 - Production network

- **Build / learn:** Provision VPC, public/private subnets across zones, routes, endpoints, security groups, NAT decision, ALB, DNS, TLS, and WAF baseline.
- **Tools and why:** AWS managed networking supplies availability; Terraform captures exact topology.
- **Prove:** Reachability tests prove only ALB is public, databases/caches are private, and egress matches policy.
- **Ship:** Network stack, diagram, and validation evidence.

### M10D5 - Day 275 - Production data services

- **Build / learn:** Provision encrypted RDS PostgreSQL, backups/PITR, parameter groups, connection strategy, ElastiCache Redis, and secret rotation.
- **Tools and why:** Managed services reduce undifferentiated operations; Secrets Manager controls credentials.
- **Prove:** Restore backup to new instance, fail cache safely, test encryption/access, and benchmark connection limits.
- **Ship:** Data stack and restore runbook.

### M10D6 - Day 276 - Container registry and images

- **Build / learn:** Create multi-stage non-root API/worker/admin images, GHCR/ECR promotion, SBOM, signing/provenance, and patch policy.
- **Tools and why:** BuildKit reduces images; Trivy scans; artifact signing verifies promotion.
- **Prove:** Rebuild reproducibly, run as read-only/non-root, block critical CVEs, and verify signature.
- **Ship:** Hardened images and supply-chain policy.

### M10D7 - Day 277 - ECS application platform

- **Build / learn:** Deploy API/worker/admin to ECS Fargate with task roles, health checks, autoscaling, rolling strategy, logs, and graceful shutdown.
- **Tools and why:** Fargate limits cluster operations; ALB routes traffic; CloudWatch/OpenTelemetry emits signals.
- **Prove:** Kill tasks, deploy bad readiness, saturate CPU/queue, and verify replacement without request corruption.
- **Ship:** Preview/staging service deployment.

### M10D8 - Day 278 - Object delivery and email

- **Build / learn:** Configure private S3 assets, signed uploads/downloads, CloudFront, lifecycle, MIME checks, SES domain/templates, bounces, and rate controls.
- **Tools and why:** S3/CloudFront serve content efficiently; SES handles transactional email.
- **Prove:** Test unauthorized object access, malicious upload, cache invalidation, expired URL, bounce, and duplicate mail.
- **Ship:** Asset/email services and runbooks.

### M10D9 - Day 279 - Cloud fundamentals lessons

- **Build / learn:** Author IAM, EC2/containers, S3, shared responsibility, regions/AZs, elasticity, and cost lessons using simulated resource graphs.
- **Tools and why:** Policy simulator and architecture canvas teach without provisioning learner resources.
- **Prove:** Validate least-privilege policy tasks, failure domains, storage choices, and cost trade-offs.
- **Ship:** Cloud foundations module.

### M10D10 - Day 280 - VPC RDS load-balancer lessons

- **Build / learn:** Build subnet/routing/security-group, database availability, connection, health check, and scaling simulations.
- **Tools and why:** Topology simulator reuses Networking World; production diagrams provide sanitized examples.
- **Prove:** Hidden cases catch public database, single-AZ assumptions, unsafe rules, and health-check mistakes.
- **Ship:** Cloud architecture labs.

### M10D11 - Day 281 - Cloud boss battle

- **Build / learn:** Design/implement resilient architecture scenario with IAM breach risk, traffic spike, database failure, cost constraint, and recovery.
- **Tools and why:** Architecture rubric scores security/reliability/performance/cost; simulator runs fault cases.
- **Prove:** Expert review and fault simulation validate multiple acceptable designs and trade-off explanations.
- **Ship:** End-to-end Cloud boss.

### M10D12 - Day 282 - Docker curriculum

- **Build / learn:** Teach images/layers, Dockerfile, build context, cache, runtime config, volumes, networks, health, non-root, and Compose.
- **Tools and why:** Real disposable builds make lessons authentic; Hadolint/Trivy provide feedback.
- **Prove:** Learner image must build, pass functional/security tests, and meet size/user/health constraints.
- **Ship:** Docker module and labs.

### M10D13 - Day 283 - CI/CD curriculum

- **Build / learn:** Teach pipeline stages, artifacts, caches, secrets, environments, approvals, migrations, rollbacks, and supply chain.
- **Tools and why:** GitHub Actions simulator plus real repository pipelines connect theory to proof.
- **Prove:** Broken workflows test permissions, cache poisoning, flaky gates, migration order, and rollback.
- **Ship:** CI/CD module.

### M10D14 - Day 284 - Kubernetes curriculum

- **Build / learn:** Teach pods/deployments/services/config/secrets/probes/resources/autoscaling/jobs/ingress and failure diagnosis in simulated manifests.
- **Tools and why:** Schema validation and policy engine score manifests without granting a public cluster.
- **Prove:** Catch missing resources/probes, privileged pods, mutable tags, secret exposure, and bad rollout.
- **Ship:** Kubernetes module and manifest grader.

### M10D15 - Day 285 - Terraform curriculum

- **Build / learn:** Teach state, plan/apply, modules, variables, lifecycle, dependencies, drift, imports, policy, and safe destroy through local simulations.
- **Tools and why:** Terraform plan JSON enables semantic grading; local providers avoid cloud spend.
- **Prove:** Test drift, state lock, destructive plan, secret output, invalid dependency, and rollback reasoning.
- **Ship:** IaC module and labs.

### M10D16 - Day 286 - DevOps boss battle

- **Build / learn:** Design/implement broken delivery pipeline spanning Docker, CI, Kubernetes manifest, Terraform plan, observability, and rollback.
- **Tools and why:** Scenario engine combines artifacts and approved actions; rubric scores safe recovery.
- **Prove:** Pilot validates alternate fixes, deterministic artifacts, reconnect, and no real credential use.
- **Ship:** End-to-end DevOps boss.

### M10D17 - Day 287 - Deployment pipeline

- **Build / learn:** Build PR preview, main-to-staging, signed-artifact promotion, manual production approval, migration job, smoke, canary/blue-green choice, and rollback.
- **Tools and why:** GitHub Actions with OIDC and immutable image digests preserves chain of custody.
- **Prove:** Inject failed migration/health/metrics and confirm automatic stop or rollback without mixed versions.
- **Ship:** Production-grade CI/CD workflow.

### M10D18 - Day 288 - Database migration operations

- **Build / learn:** Adopt expand-migrate-contract, online index/backfill patterns, compatibility window, backup gate, and migration observability.
- **Tools and why:** Alembic plus one-shot ECS tasks separates schema change from app startup.
- **Prove:** Rehearse large-table backfill, old/new app coexistence, failure, resume, and rollback/roll-forward.
- **Ship:** Migration playbook and rehearsal evidence.

### M10D19 - Day 289 - Feature flags and release control

- **Build / learn:** Create typed flags, cohorts, kill switches, config ownership, expiry dates, audit history, and safe defaults.
- **Tools and why:** OpenFeature-compatible interface avoids vendor lock-in; admin permissions control rollout.
- **Prove:** Test provider outage, stale config, unauthorized edit, cohort consistency, and emergency disable.
- **Ship:** Release-control service and runbook.

### M10D20 - Day 290 - Production observability

- **Build / learn:** Complete traces/metrics/logs across mobile, ALB, API, DB, Redis, queue, worker, sandbox, and AI placeholder; define RED/USE dashboards.
- **Tools and why:** OpenTelemetry standardizes correlation; Grafana/Sentry support operations.
- **Prove:** Trace one lesson completion, induce faults, verify redaction/cardinality budgets, and page with actionable context.
- **Ship:** Production dashboards and alert catalog.

### M10D21 - Day 291 - SLOs and error budgets

- **Build / learn:** Set availability/latency/correctness/freshness SLI queries, objectives, burn-rate alerts, maintenance policy, and release freeze rule.
- **Tools and why:** Prometheus recording rules make SLOs executable; runbooks link each alert to action.
- **Prove:** Replay historical/fault data, test fast/slow burn alerts, and remove non-actionable pages.
- **Ship:** SLO document, dashboards, and alerts.

### M10D22 - Day 292 - Load and autoscaling

- **Build / learn:** Model learner journeys, runner bursts, notifications, admin publishing, and read peaks; tune tasks, DB pools, Redis, queue, and limits.
- **Tools and why:** k6 generates workloads; autoscaling uses CPU/request/queue signals; Infracost tracks trade-offs.
- **Prove:** Find saturation, demonstrate graceful overload, verify scale-out/in, and record cost per active learner.
- **Ship:** Capacity and cost report.

### M10D23 - Day 293 - Backup and disaster recovery

- **Build / learn:** Automate RDS/S3/config backups, restore verification, dependency inventory, RTO/RPO, regional outage decision, and communications.
- **Tools and why:** AWS Backup/PITR plus Terraform rebuild data/platform; runbook coordinates recovery.
- **Prove:** Game day restores into isolated environment and validates critical flows/data counts within objectives.
- **Ship:** DR report and corrected runbook.

### M10D24 - Day 294 - Cloud security review

- **Build / learn:** Assess IAM, network, encryption, secrets, WAF, images, logging, backups, CI trust, admin, and public assets.
- **Tools and why:** CloudTrail/Config/Security Hub where available plus IaC scanners provide evidence.
- **Prove:** No critical/high unowned finding; public exposure and privilege paths are explicitly tested.
- **Ship:** Cloud security report and remediations.

### M10D25 - Day 295 - FinOps and sustainability

- **Build / learn:** Create budgets, tags, unit economics, idle cleanup, storage lifecycle, right-sizing, scaling schedules, and cost anomaly alerts.
- **Tools and why:** Cost Explorer/Infracost connect architecture to spend; dashboards track cost per learner/action.
- **Prove:** Compare forecast to measured load, delete orphan resources safely, and prove alerts before overrun.
- **Ship:** Cost model and optimization memo.

### M10D26 - Day 296 - Cloud/DevOps content review

- **Build / learn:** Execute every lab/solution against pinned tools, review safety/current terminology, analytics, hints, and scoring.
- **Tools and why:** CI matrices and policy tests catch drift; technical reviewers sign off.
- **Prove:** Zero real credential, destructive ambiguity, broken fixture, or unverifiable claim remains.
- **Ship:** Signed curriculum review.

### M10D27 - Day 297 - Cloud/DevOps accessibility QA

- **Build / learn:** Audit architecture canvases, policy editors, manifests, pipelines, boss actions, keyboard, color, motion, and screen-reader alternatives.
- **Tools and why:** Maestro plus manual assistive-tech review validates full learning journeys.
- **Prove:** All core labs and bosses remain completable without color-only diagrams, dragging, or inaccessible code panes.
- **Ship:** Accessibility report and remediations.

### M10D28 - Day 298 - Release candidate

- **Build / learn:** Run real deployment plus Cloud/DevOps learning flows, migrations, rollback, DR, security, load, cost, analytics, and accessibility.
- **Tools and why:** Release dashboard combines product and infrastructure gates; flags isolate worlds.
- **Prove:** Pilot and 24-hour staging soak pass SLO/error-budget and cost thresholds.
- **Ship:** Tagged `v0.10.0-rc1` and readiness report.

### M10D29 - Day 299 - Infrastructure case study

- **Build / learn:** Document modular monolith deployment, IaC, CI/CD, SLOs, load/cost, DR game day, security, and trade-offs.
- **Tools and why:** MkDocs, sanitized dashboards, and reproducible Terraform plans substantiate claims.
- **Prove:** Reviewer can plan preview infra and reproduce load/rollback evidence without production secrets.
- **Ship:** Public production-platform case study.

### M10D30 - Day 300 - Cloud and DevOps release

- **Build / learn:** Promote `v0.10-cloud-devops`, monitor staged cohorts and production, close milestone, and open AI-specific risk/cost budgets.
- **Tools and why:** GitHub Release, SLOs, and retrospective complete evidence.
- **Prove:** Product, infra, security, deployment, DR, and cost gates remain healthy.
- **Ship:** Release, retrospective, and AI Mentor backlog.

# Month 11 - AI Mentor and adaptive learning

**Monthly production goal:** Ship a grounded, evaluated, safe, cost-controlled mentor that helps learners think without leaking answers or replacing deterministic grading.

### M11D1 - Day 301 - AI mentor product contract

- **Build / learn:** Define allowed jobs, non-goals, hint levels, answer-leak policy, tone, age assumptions, escalation, privacy, latency/cost budgets, and success metrics.
- **Tools and why:** AI product RFC and risk register prevent “chatbot” scope drift; threat modeling covers prompt/data/model boundaries.
- **Prove:** Review 100 representative requests and label desired behavior, refusal, grounding, and unacceptable outcomes.
- **Ship:** Mentor specification, taxonomy, and eval seed set.

### M11D2 - Day 302 - Provider-neutral AI gateway

- **Build / learn:** Create model adapter interface, request/response schema, timeout, retry, idempotency, streaming, usage capture, fallback, and kill switch.
- **Tools and why:** OpenAI Responses API is one adapter; fake deterministic adapter powers tests; circuit breaker protects outages.
- **Prove:** Contract-test success, refusal, timeout, 429/5xx, malformed output, stream interruption, and fallback.
- **Ship:** AI gateway service and provider ADR.

### M11D3 - Day 303 - Structured mentor outputs

- **Build / learn:** Define schema for explanation, hint ladder, misconception, follow-up question, citations, confidence, safety action, and UI blocks.
- **Tools and why:** Structured Outputs constrain response shape; Pydantic validates at the boundary.
- **Prove:** Fuzz prompts and model responses; invalid/partial outputs must retry within budget or degrade safely.
- **Ship:** Versioned mentor-response contract and parser tests.

### M11D4 - Day 304 - Prompt registry

- **Build / learn:** Store system/task prompts with version, owner, rationale, variables, model settings, change review, rollout, and rollback.
- **Tools and why:** Git plus database registry makes prompts auditable; feature flags stage versions.
- **Prove:** Reject missing variables, unsafe interpolation, unreviewed production prompt, and incompatible schema version.
- **Ship:** Prompt registry, lint command, and ADR.

### M11D5 - Day 305 - Learning context builder

- **Build / learn:** Assemble minimum necessary lesson, activity, authored hints, learner attempt history, mastery, locale, and policy without secrets or other users’ data.
- **Tools and why:** Typed context DTO and allowlist minimize data; token counter enforces budget.
- **Prove:** Test cross-user IDs, hidden answers, oversized context, stale content, and PII redaction.
- **Ship:** Context service and privacy tests.

### M11D6 - Day 306 - Grounded retrieval corpus

- **Build / learn:** Chunk/version curriculum explanations, editorials, concepts, and policies with provenance, access level, content version, and deletion path.
- **Tools and why:** PostgreSQL pgvector keeps retrieval near source data; embeddings are cached and versioned.
- **Prove:** Measure retrieval recall on labeled queries, test entitlement filtering, deleted content, and citation integrity.
- **Ship:** Retrieval index pipeline and dataset card.

### M11D7 - Day 307 - Hybrid retrieval and reranking

- **Build / learn:** Combine lexical/vector candidates, metadata filters, reranking, diversity, and no-result threshold; expose traceable citations.
- **Tools and why:** PostgreSQL full text plus pgvector balances exact terms and semantics; evaluation selects weights.
- **Prove:** Benchmark recall/MRR/latency on labeled set and compare lexical, vector, and hybrid baselines.
- **Ship:** Retrieval benchmark and chosen-policy ADR.

### M11D8 - Day 308 - Progressive hint generator

- **Build / learn:** Generate level-1 question, level-2 concept cue, level-3 worked step, and final explanation only when policy permits.
- **Tools and why:** Prompt templates use authored hint/retrieved context; deterministic grader remains truth.
- **Prove:** Eval answer leakage, relevance, progression, factuality, tone, and schema compliance across worlds.
- **Ship:** Hint endpoint, UI cards, and eval report.

### M11D9 - Day 309 - Mistake explanation

- **Build / learn:** Convert deterministic evaluator result/misconception code into grounded explanation, example, and next action without changing score.
- **Tools and why:** Tool-like access to evaluator facts prevents model from inventing correctness.
- **Prove:** Adversarially provide false learner claims and prompt injection; explanation must follow authoritative result.
- **Ship:** Explanation flow and disagreement handling.

### M11D10 - Day 310 - AI mentor mobile chat

- **Build / learn:** Build contextual entry, streaming blocks, stop/retry, citations, feedback, copy policy, offline/unavailable state, and accessibility.
- **Tools and why:** SSE streams server-controlled responses; local state never stores hidden prompt/context.
- **Prove:** Test backgrounding, reconnect, duplicate send, slow tokens, refusal, screen reader, and content overflow.
- **Ship:** Mentor chat alpha behind staff flag.

### M11D11 - Day 311 - Prompt-injection defenses

- **Build / learn:** Separate instructions/data, sanitize retrieved content, deny unapproved tools, enforce entitlement, output schema, moderation, and canary tests.
- **Tools and why:** Policy layer and allowlisted tool calls create defense in depth; red-team corpus runs in CI.
- **Prove:** Attack via lesson text, user input, citations, code blocks, role claims, and encoded instructions.
- **Ship:** Injection threat model and red-team report.

### M11D12 - Day 312 - AI privacy and retention

- **Build / learn:** Define what prompts/responses/context/usage/feedback are stored, redacted, encrypted, retained, deleted, and exportable; add consent.
- **Tools and why:** Data classification and TTL jobs enforce minimization; audit logs record privileged access.
- **Prove:** Delete/export a user, sample logs/traces, and prove no credentials, hidden tests, or cross-user content persist.
- **Ship:** AI privacy policy and deletion tests.

### M11D13 - Day 313 - Offline evaluation harness

- **Build / learn:** Build versioned JSONL cases, fixtures, model/prompt config, deterministic graders, rubric graders with calibration, regression thresholds, and reports.
- **Tools and why:** OpenAI Evals-compatible concepts plus pytest runner make quality reviewable; W&B/MLflow records runs.
- **Prove:** Re-run fixed cases, estimate variance, calibrate human agreement, and block regressions on critical slices.
- **Ship:** `make eval-mentor` and baseline report.

### M11D14 - Day 314 - Evaluation dataset expansion

- **Build / learn:** Curate real curriculum questions, anonymized opt-in failure patterns, adversarial cases, locales, accessibility, beginner/expert, and world slices.
- **Tools and why:** Labeling rubric and dual review improve quality; dataset card records provenance/limitations.
- **Prove:** Measure agreement, resolve conflicts, remove leakage/PII, and maintain untouched holdout.
- **Ship:** Versioned eval dataset and card.

### M11D15 - Day 315 - LLM observability

- **Build / learn:** Trace gateway, retrieval, prompt/model version, tokens, latency, cost, schema retry, safety action, feedback, and outcome without logging sensitive text by default.
- **Tools and why:** OpenTelemetry and AI trace metadata connect behavior to releases; dashboards track quality/operations.
- **Prove:** Trace a request end to end, test sampling/redaction/cardinality, and alert on cost/latency/schema spikes.
- **Ship:** AI operations dashboard and alert runbooks.

### M11D16 - Day 316 - Model and prompt selection

- **Build / learn:** Compare at least two eligible model/config/prompt combinations on quality slices, latency, cost, consistency, and safety.
- **Tools and why:** Evaluation harness replaces intuition; Pareto analysis makes trade-offs explicit.
- **Prove:** Use repeated runs and confidence intervals; choose policy by thresholds, not one aggregate score.
- **Ship:** Model-selection memo and rollout configuration.

### M11D17 - Day 317 - Caching and cost controls

- **Build / learn:** Add exact safe cache where appropriate, prompt caching support, token ceilings, per-user quotas, budgets, response truncation, and cheaper fallback.
- **Tools and why:** Redis and provider usage metadata control spend; budget alerts protect production.
- **Prove:** Test privacy-safe keys, stale content versions, cache poisoning, quota races, and provider cost anomaly.
- **Ship:** Cost dashboard, quota service, and ADR.

### M11D18 - Day 318 - Weak-topic detector

- **Build / learn:** Compute explainable weakness from mastery, recency, repeated misconceptions, hint reliance, speed, and assessment confidence with minimum evidence.
- **Tools and why:** SQL feature pipeline and pure scoring model stay interpretable; model card records limitations.
- **Prove:** Backtest against labeled learner histories, test cold start/missing data, and audit world/cohort bias.
- **Ship:** Weak-topic service, model card, and validation report.

### M11D19 - Day 319 - Revision scheduler

- **Build / learn:** Implement spaced-repetition state, due dates, prerequisite constraints, fatigue caps, streak compatibility, and reason codes.
- **Tools and why:** Deterministic scheduling algorithm remains testable; injectable clock handles timezones.
- **Prove:** Simulate months of activity, DST/travel, missed days, content changes, and ensure no overload/starvation.
- **Ship:** Revision queue API and property tests.

### M11D20 - Day 320 - Personalized recommendation policy

- **Build / learn:** Rank next lessons/reviews from goals, prerequisites, mastery, difficulty, freshness, availability, and exploration with transparent reasons.
- **Tools and why:** Constraint-first ranking prevents inaccessible recommendations; feature flags version weights.
- **Prove:** Offline replay compares baseline/personalized policy; audit repetition, cold start, and cohort fairness.
- **Ship:** Recommendation service and decision memo.

### M11D21 - Day 321 - Adaptive plan mobile UX

- **Build / learn:** Build “why this,” edit goal, snooze, due review, weak-topic summary, progress confidence, and safe opt-out.
- **Tools and why:** Typed reason codes become understandable copy; analytics measures acceptance/completion.
- **Prove:** Test sparse data, rapidly changing mastery, offline view, accessibility, and user control.
- **Ship:** Adaptive dashboard and E2E journey.

### M11D22 - Day 322 - Interview-mode design

- **Build / learn:** Define role/topic/difficulty, timed stages, clarification, code/system questions, rubric, integrity, feedback embargo, and AI limitations.
- **Tools and why:** Assessment blueprint separates measured skills from AI conversation quality.
- **Prove:** Expert review calibrates questions/timing and confirms deterministic scoring wherever possible.
- **Ship:** Interview mode RFC and question set.

### M11D23 - Day 323 - Interview session engine

- **Build / learn:** Implement start, question sequence, timer, autosave, code/judge integration, AI follow-ups, reconnect, submit, and signed result.
- **Tools and why:** State machine and immutable events preserve reliability; server clock prevents manipulation.
- **Prove:** Kill app/provider/worker, reconnect, exceed time, retry submit, and confirm coherent result.
- **Ship:** Interview session API and mobile flow.

### M11D24 - Day 324 - Interview feedback generator

- **Build / learn:** Ground narrative feedback in rubric dimensions, evidence, code verdicts, and citations; prohibit invented observations and sensitive inferences.
- **Tools and why:** Structured output ties every claim to evidence IDs; deterministic scores remain authoritative.
- **Prove:** Eval evidence faithfulness, actionability, tone, contradiction, and unsupported claims.
- **Ship:** Feedback report feature and eval slice.

### M11D25 - Day 325 - AI safety and abuse review

- **Build / learn:** Test prompt injection, answer extraction, hidden-test leakage, self-harm/escalation boundaries, harassment, PII, model outage, denial-of-wallet, and admin misuse.
- **Tools and why:** Moderation/policy checks, quotas, red-team suite, RBAC, audit, and kill switches provide layers.
- **Prove:** Critical safety/privacy/leakage failures block release; residual risks get owners and monitoring.
- **Ship:** AI safety report and incident playbooks.

### M11D26 - Day 326 - AI load and reliability

- **Build / learn:** Benchmark concurrent streams, retrieval, provider latency, queue/backpressure, cancellations, timeouts, fallbacks, token/cost, and mobile reconnect.
- **Tools and why:** k6 and mocked/provider-safe load profiles expose bottlenecks without uncontrolled spend.
- **Prove:** Demonstrate graceful provider outage and enforce p95/cost/error budgets under planned concurrency.
- **Ship:** Capacity, reliability, and cost report.

### M11D27 - Day 327 - Human evaluation and pilot

- **Build / learn:** Run blinded rubric review with instructors/learners on hint usefulness, correctness, leakage, tone, and recommendation relevance.
- **Tools and why:** Annotation form and calibrated rubric provide evidence beyond automated graders.
- **Prove:** Measure agreement, analyze failures by slice, fix blockers, and preserve holdout cases.
- **Ship:** Human-eval report and revised prompts/policies.

### M11D28 - Day 328 - AI release candidate

- **Build / learn:** Run mentor/retrieval/adaptation/interview flows plus eval, red team, privacy deletion, load, cost, observability, rollback, and fallback drills.
- **Tools and why:** Prompt/model/feature flags permit independent rollback; release dashboard gates promotion.
- **Prove:** All critical eval slices pass thresholds and pilot users complete tasks without score corruption or answer leakage.
- **Ship:** Tagged `v0.11.0-rc1` and AI readiness report.

### M11D29 - Day 329 - AI architecture case study

- **Build / learn:** Document gateway, structured outputs, RAG benchmark, eval design, safety, adaptive algorithm, latency/cost, failures, and limitations.
- **Tools and why:** MkDocs and versioned eval reports make AI claims verifiable.
- **Prove:** Reviewer can run fake-provider tests and a bounded live eval using documented configuration.
- **Ship:** Public AI Mentor case study and demo.

### M11D30 - Day 330 - AI Mentor release

- **Build / learn:** Promote `v0.11-ai-mentor` gradually, monitor quality/safety/cost/SLOs, rehearse kill switch, close milestone, and freeze v1 scope.
- **Tools and why:** GitHub Release, dashboards, and retrospective complete evidence.
- **Prove:** No critical regression, leakage, privacy incident, runaway spend, or grading inconsistency appears.
- **Ship:** Release, retrospective, and v1 launch backlog.

# Month 12 - Operations, monetization, and public launch

**Monthly production goal:** Close the operating gaps, validate the product with real pilot users, and release a supportable v1 rather than a demo that cannot survive launch day.

### M12D1 - Day 331 - V1 scope freeze and launch command

- **Build / learn:** Freeze must/should/won't scope, owners, go/no-go criteria, severity definitions, communication channels, rollback authority, and launch calendar.
- **Tools and why:** GitHub milestone tracks blockers; launch checklist makes decisions explicit.
- **Prove:** Every v1 item has evidence and owner; unowned or unmeasurable work is cut or deferred.
- **Ship:** V1 release plan, RACI, and blocker board.

### M12D2 - Day 332 - Admin identity and shell

- **Build / learn:** Harden separate admin authentication, MFA requirement, session timeout, route/action permissions, navigation, environment banner, and audit context.
- **Tools and why:** Next.js admin uses shared contracts; RBAC and step-up auth protect privileged work.
- **Prove:** Test anonymous/wrong-role/cross-environment actions, session expiry, CSRF, and audit completeness.
- **Ship:** Production admin shell and permission matrix.

### M12D3 - Day 333 - Curriculum operations

- **Build / learn:** Finish search, draft, diff, preview, approval, scheduling, rollback, bulk validation, asset management, and publication history.
- **Tools and why:** Schema-driven forms and content linter prevent runtime drift; S3 signed upload controls assets.
- **Prove:** An editor publishes/rolls back a world without database access; invalid or unapproved content cannot ship.
- **Ship:** Complete curriculum console and operator guide.

### M12D4 - Day 334 - Learner support console

- **Build / learn:** Build privacy-aware learner lookup, sessions, progress, ledger reconciliation, notification status, entitlement, safe overrides, and reason-required actions.
- **Tools and why:** Read models protect OLTP; field masking/RBAC/audit control support access.
- **Prove:** Support cannot see secrets/raw AI context or alter state without permission, reason, and reversible record.
- **Ship:** Support console and audited workflows.

### M12D5 - Day 335 - Feature and incident controls

- **Build / learn:** Add flag/cohort editor, kill switches, maintenance message, job replay/DLQ tools, incident banner, and two-person approval for high-risk actions.
- **Tools and why:** OpenFeature interface and queue admin APIs enable safe operations.
- **Prove:** Simulate bad flag, poison job, AI outage, runner incident, and emergency disable with complete audit.
- **Ship:** Operations console and emergency runbook.

### M12D6 - Day 336 - Product metric dictionary

- **Build / learn:** Finalize activation, lesson completion, D1/D7/D30 retention, streak, mastery, conversion, churn, AI helpfulness, reliability, and guardrail definitions.
- **Tools and why:** Versioned SQL/dbt metrics prevent dashboard disagreement.
- **Prove:** Reconcile source events to metric outputs, document exclusions/timezones, and test schema freshness.
- **Ship:** Metric catalog and data contracts.

### M12D7 - Day 337 - Executive and product dashboards

- **Build / learn:** Build acquisition/activation/retention/revenue/learning funnels, cohort slices, experiment views, and data-quality indicators.
- **Tools and why:** PostHog plus warehouse/BI dashboards serve product decisions; dbt tests transformations.
- **Prove:** Compare dashboard totals to OLTP samples and flag late/duplicate/missing events.
- **Ship:** Launch analytics suite and interpretation guide.

### M12D8 - Day 338 - Experimentation framework

- **Build / learn:** Implement exposure assignment, stable cohorts, hypothesis/primary/guardrail metrics, sample rules, stop criteria, and analysis template.
- **Tools and why:** Feature flags record exposures; warehouse queries estimate effects without dashboard peeking.
- **Prove:** A/A test checks assignment and metric bias; overlapping experiments follow exclusion rules.
- **Ship:** Experiment platform and first A/A report.

### M12D9 - Day 339 - Privacy operations

- **Build / learn:** Complete consent, analytics opt-out, data export/delete, retention jobs, account deletion grace, subprocessor register, and privacy contact workflow.
- **Tools and why:** Data inventory maps stores; scheduled deletion and audit evidence make policy executable.
- **Prove:** Run export/delete for a test user across DB/cache/object/analytics/AI/backups per documented limits.
- **Ship:** Privacy runbook, data map, and verification report.

### M12D10 - Day 340 - Analytics and admin release slice

- **Build / learn:** Deploy admin/metrics/experiments/privacy tools to staging, train an operator, and close permission/data-quality gaps.
- **Tools and why:** Playwright tests admin; audit dashboard monitors privileged actions.
- **Prove:** Independent operator completes five core workflows from runbooks without developer/database access.
- **Ship:** Admin/analytics readiness sign-off.

### M12D11 - Day 341 - Full regression matrix

- **Build / learn:** Run unit, integration, contract, property, migration, mobile, admin, E2E, sandbox, AI eval, and compatibility suites on release commits.
- **Tools and why:** CI matrix and test reports give one release evidence index.
- **Prove:** No flaky retry hides failure; all quarantines have owner/expiry and no critical path is quarantined.
- **Ship:** V1 regression report and fixed blockers.

### M12D12 - Day 342 - Real-device and accessibility QA

- **Build / learn:** Test supported iOS/Android devices, screen sizes, poor networks, backgrounding, deep links, push, biometric, dark mode, locale, and assistive tech.
- **Tools and why:** EAS device builds, Maestro, VoiceOver/TalkBack, and accessibility checklists cover real use.
- **Prove:** Critical journeys pass WCAG-aligned criteria and no device-specific blocker remains.
- **Ship:** Device/accessibility matrix and remediation evidence.

### M12D13 - Day 343 - Security release review

- **Build / learn:** Re-run threat models, SAST/DAST/dependency/container/IaC/mobile checks, authorization matrix, secrets scan, and manual business-logic tests.
- **Tools and why:** OWASP ASVS/MASVS and cloud controls structure coverage.
- **Prove:** Critical/high findings block launch unless explicitly accepted by accountable owner with mitigation/date.
- **Ship:** V1 security report and signed risk register.

### M12D14 - Day 344 - Resilience game day

- **Build / learn:** Inject database/cache/queue/provider/runner/email/object/CDN failure, latency, task loss, bad deploy, and region/AZ symptom in staging.
- **Tools and why:** Toxiproxy, fault toggles, load tests, and runbooks exercise recovery.
- **Prove:** Measure detection/mitigation/recovery; no silent data corruption or duplicate rewards/subscriptions.
- **Ship:** Game-day timeline, gaps, and corrective PRs.

### M12D15 - Day 345 - Production infrastructure rehearsal

- **Build / learn:** Recreate staging from Terraform, rotate secrets, migrate, deploy, scale, back up, restore, and destroy ephemeral resources.
- **Tools and why:** Terraform/OIDC/CI/CD prove environment reproducibility.
- **Prove:** Manual console drift is detected; a new environment reaches smoke-test green from documented automation.
- **Ship:** Infrastructure readiness report.

### M12D16 - Day 346 - Production deployment rehearsal

- **Build / learn:** Perform signed artifact promotion, expand-contract migration, canary, automated smoke, SLO observation, rollback, and forward fix.
- **Tools and why:** Immutable digests and release workflow preserve provenance.
- **Prove:** Deliberately bad canary stops before full rollout and restores compatible service/data state.
- **Ship:** Deployment rehearsal and corrected release runbook.

### M12D17 - Day 347 - App-store build engineering

- **Build / learn:** Configure production bundle IDs, signing ownership, permissions, privacy manifests, icons/splash, deep links, update policy, and release channels.
- **Tools and why:** Expo EAS builds reproducible iOS/Android artifacts; secure credential ownership avoids personal-machine dependency.
- **Prove:** Install release builds, test upgrades from prior build, permissions, links, crash symbols, and API environment.
- **Ship:** Signed internal release candidates.

### M12D18 - Day 348 - Store listing and review package

- **Build / learn:** Prepare accurate descriptions, screenshots, privacy answers, support URL, account-deletion path, reviewer credentials, age/content rating, and release notes.
- **Tools and why:** Store consoles receive only truthful product/data declarations; checklist prevents rejection.
- **Prove:** Cross-check listing against actual permissions/data behavior and run reviewer path from a fresh account.
- **Ship:** Submission-ready store metadata and review guide.

### M12D19 - Day 349 - Subscription architecture

- **Build / learn:** Define products, entitlements, trials, grace, restore, refunds, cancellation, regional pricing ownership, and free learning guarantees.
- **Tools and why:** RevenueCat or store server notifications normalize platforms; backend entitlement ledger remains authoritative.
- **Prove:** Model purchase/retry/refund/renewal/grace/chargeback events and prevent paywall from corrupting progress.
- **Ship:** Commerce RFC, product catalog, and entitlement schema.

### M12D20 - Day 350 - Purchase and entitlement flow

- **Build / learn:** Implement mobile paywall, purchase/restore, webhook signature/idempotency, entitlement API/cache, receipt history, and support view.
- **Tools and why:** Store SDK handles checkout; webhook worker/outbox preserves eventual consistency.
- **Prove:** Replay/out-of-order webhooks, switch devices/accounts, go offline, refund, and verify one entitlement transition.
- **Ship:** End-to-end sandbox purchase flow.

### M12D21 - Day 351 - Commerce security and reconciliation

- **Build / learn:** Add signed webhooks, secret rotation, event ledger, daily reconciliation, anomaly alerts, tax/invoice boundary note, and least-privilege support.
- **Tools and why:** Provider reports and database ledger detect missed/duplicate events.
- **Prove:** Reconcile test purchases, forge webhook, lose/replay event, and confirm no unauthorized premium access.
- **Ship:** Commerce control report and runbook.

### M12D22 - Day 352 - Beta cohort launch

- **Build / learn:** Recruit consented real pilot users, define cohorts/tasks/support channel, deploy RC, observe without coaching, and triage by severity.
- **Tools and why:** TestFlight/Play internal tracks distribute safely; feedback form links release/device/session IDs.
- **Prove:** Measure activation, completion, crashes, support issues, and qualitative confusion; do not cherry-pick feedback.
- **Ship:** Beta report and prioritized blocker list.

### M12D23 - Day 353 - Performance and cost sign-off

- **Build / learn:** Run forecast load across mobile/API/DB/cache/queue/runners/AI/CDN, verify autoscaling, rate limits, and monthly unit economics.
- **Tools and why:** k6, Grafana, cloud cost tools, and AI usage dashboards quantify capacity.
- **Prove:** Meet p95/p99/error/cost budgets or reduce launch cohort; record bottleneck and headroom.
- **Ship:** Final capacity and cost plan.

### M12D24 - Day 354 - Support and incident readiness

- **Build / learn:** Define severity/on-call expectations, alert ownership, status updates, escalation, customer support macros, postmortem SLA, and vendor contacts.
- **Tools and why:** Pager/notification system and status page route incidents; runbooks reduce improvisation.
- **Prove:** Tabletop auth outage, data issue, payment issue, sandbox abuse, and AI safety report end to end.
- **Ship:** Operations handbook and contact tree.

### M12D25 - Day 355 - Documentation and clean-room audit

- **Build / learn:** Finish architecture, setup, APIs, ERD, ADRs, runbooks, security/privacy, contribution guide, demo, and evidence index.
- **Tools and why:** MkDocs and CI link checking keep documentation usable.
- **Prove:** A fresh reviewer clones, starts local stack, runs tests, deploys preview, and completes a learner flow without private help.
- **Ship:** Versioned documentation portal and audit report.

### M12D26 - Day 356 - Portfolio evidence package

- **Build / learn:** Create concise case studies for product architecture, ledgers, sandboxes, AI evals, SLOs, security, incident game day, and measured outcomes.
- **Tools and why:** GitHub Pages, releases, diagrams, demos, and benchmark files make claims inspectable.
- **Prove:** Every resume claim links artifact, validation, trade-off, limitation, and evidence; remove logo-only skills.
- **Ship:** Recruiter evidence index and truthful resume bullets.

### M12D27 - Day 357 - Go no-go review

- **Build / learn:** Review product, quality, security, privacy, accessibility, SLO, capacity, cost, support, stores, commerce, data, and rollback gates.
- **Tools and why:** Decision record captures evidence and accountable sign-off.
- **Prove:** Any failed critical gate means delay or reduced cohort; document rationale, not optimism.
- **Ship:** Go/no-go ADR and final launch checklist.

### M12D28 - Day 358 - Staged production launch

- **Build / learn:** Deploy immutable v1, migrate, canary, enable staff then small cohorts, watch SLOs/business/security signals, and expand only within budgets.
- **Tools and why:** Feature flags, canary deployment, dashboards, alerts, and status page control blast radius.
- **Prove:** Smoke each cohort, reconcile core ledgers/events/purchases, and exercise immediate rollback if a gate fails.
- **Ship:** Production `v1.0.0` and timestamped launch log.

### M12D29 - Day 359 - Store submission and communication

- **Build / learn:** Submit approved binaries/listings, publish release notes/status/help content, notify beta users, and track reviewer questions.
- **Tools and why:** App Store/Play workflows distribute; support knowledge base gives consistent answers.
- **Prove:** Reviewer account and deletion/purchase/core-learning paths work; all claims match shipped behavior.
- **Ship:** Store submissions and public launch package.

### M12D30 - Day 360 - Post-launch watch and v1.0.1

- **Build / learn:** Operate launch watch, triage signals/feedback, fix highest-severity defects, produce post-launch review, and plan v1.0.1 without scope panic.
- **Tools and why:** SLO/error budgets and incident process guide action; release branch keeps fixes controlled.
- **Prove:** Reconcile first cohorts, examine crashes/security/cost/conversion/learning, and verify fixes through full gates.
- **Ship:** Post-launch report, v1.0.1 backlog, and 90-day roadmap.

## Monthly review template

At the end of every month, answer with links and numbers:

1. What user capability shipped and who tested it?
2. Which reliability, security, privacy, accessibility, performance, and cost gates passed or failed?
3. What architecture decision changed, and what evidence caused the change?
4. What incident or induced failure occurred, what was the root cause, and what prevents recurrence?
5. Which metrics improved, which were harmed, and what uncertainty remains?
6. Which debt blocks the next release, and which debt is consciously accepted?
7. Which artifacts are strong enough for GitHub, a case study, LinkedIn, or a resume claim?

## Portfolio publishing cadence

- **Daily:** meaningful GitHub issue/branch/PR, green evidence, short engineering worklog.
- **Weekly:** one engineering review; do not post filler.
- **Monthly:** tagged release, demo, architecture update, benchmark/eval/security evidence, and retrospective.
- **Quarterly:** one polished long-form case study and one external contribution related to technology actually used.
- **Final:** live product, public documentation, eight deep case studies, incident/game-day evidence, honest resume bullets, and a five-minute recruiter demo.

## Reference documentation

- [Expo documentation](https://docs.expo.dev/)
- [FastAPI deployment in containers](https://fastapi.tiangolo.com/deployment/docker/)
- [PostgreSQL documentation](https://www.postgresql.org/docs/)
- [OpenTelemetry documentation](https://opentelemetry.io/docs/)
- [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html)
- [OpenAI Structured Outputs](https://developers.openai.com/api/docs/guides/structured-outputs)
- [OpenAI Evals](https://developers.openai.com/api/docs/guides/evals)
- [OpenAI production best practices](https://developers.openai.com/api/docs/guides/production-best-practices)

## Final warning

Finishing tasks mechanically will not create a company-grade product. The proof is in the gates: real users, reproducible builds, measured quality, defended boundaries, safe failure, operational readiness, and honest evidence. If a day’s acceptance test fails, carry the defect forward as an explicit blocker; do not mark the day complete because code was committed.
