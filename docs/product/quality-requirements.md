# Quality attributes and initial SLOs

All figures are design targets, not measured production performance. Owner: maintainer.
Scope: authenticated API and first learning loop; exclude planned maintenance only if
communicated before the measurement window. Review after first representative load test.

| Stimulus / environment                       | Expected response                                    | Measurement                                                              |
| -------------------------------------------- | ---------------------------------------------------- | ------------------------------------------------------------------------ |
| Valid API traffic at 100 concurrent learners | p95 reads <300 ms, writes <500 ms                    | 30-minute load run with representative DB                                |
| Production traffic over rolling 30 days      | 99.5% eligible requests successful (no 5xx/timeouts) | Server counters; budget 0.5%; freeze releases on exhaustion              |
| Database unavailable                         | Readiness 503 within 5 seconds; liveness remains 200 | Dependency outage smoke test                                             |
| Lost API process                             | No committed progress lost                           | Restart and retry with same idempotency key                              |
| Regional outage                              | RTO 4 hours, RPO 24 hours initially                  | Monthly isolated restore drill                                           |
| Keyboard/screen reader use                   | WCAG 2.2 AA critical journeys                        | Automated checks plus manual audit                                       |
| Spend reaches 80% of $100 monthly pilot cap  | Alert owner; disable optional jobs at cap            | Daily budget reporting; infrastructure costs still require manual action |

## Threat scope

Assets: credentials, sessions, learner progress, staff privileges, curriculum, billing.
Boundaries: public client/API, API/DB, API/worker, staff/admin, future sandbox/provider.
Abuse: credential stuffing (rate limits), broken ownership (deny-by-default queries),
replay (idempotency), injection (parameterized SQL), unsafe code (isolated sandbox),
secret leakage (redaction). Each mitigation requires tests when its feature is introduced.
No claim is made that this design alone secures a deployed application.

## Data classification

Public: published curriculum. Internal: operational metrics. Personal: email, profile,
progress; delete within 30 days of verified request. Restricted: password hashes/session
secrets; never analytics or logs. Proposed raw analytics retention 90 days, aggregate 13
months; backups expire within 35 days and replay deletion ledger on restore. Legal review
required before production billing. Prototype collects nothing.
