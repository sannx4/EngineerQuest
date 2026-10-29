# ADR-002: Data ownership and consistency

Status: accepted. Each module owns writes to its tables; cross-module writes use explicit
application services in the same transaction or versioned domain events after commit.

| Context       | Source of truth                                 | Other consumers |
| ------------- | ----------------------------------------------- | --------------- |
| Identity      | users, credentials, sessions, deletion requests | Profile, admin  |
| Profile       | class and preferences                           | Learning        |
| Curriculum    | versioned lessons and prerequisites             | Attempts        |
| Attempts      | immutable submissions and outcomes              | Progression     |
| Progression   | completions and XP ledger                       | Gamification    |
| Gamification  | awards, streaks and rankings                    | Profile         |
| Notifications | delivery state                                  | Support         |
| Analytics     | consented derived events                        | Admin           |
| Commerce      | verified entitlements                           | API             |
| Admin         | audit records and staff permissions             | Operations      |
| Sandbox       | execution jobs and bounded results              | Attempts        |
| Mentor        | prompt versions and consented interactions      | Analytics       |

## Boundary walkthroughs

Signup: identity commits user and outbox event atomically; profile provisioning consumes
idempotently. Profile can show provisioning until eventual delivery; identity remains authoritative.
Lesson completion: attempt and completion recorded once within one DB transaction via
application service; unique attempt ID protects retries. Leaderboard updates asynchronously.
Account deletion: identity revokes sessions and commits deletion request/outbox; each owner
purges or de-identifies its data and acknowledges. Completion recorded after all owners ack;
legal retention exceptions are explicit. Analytics cannot recreate erased identity.

No migrations for domain data are introduced in this batch. Future changes require reversible
migrations, retention policy, unique constraints and migration tests in their feature PR.
