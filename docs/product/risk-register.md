# Risk register

| Risk                           | Impact                    | Mitigation / trigger                                                    | Owner      | State            |
| ------------------------------ | ------------------------- | ----------------------------------------------------------------------- | ---------- | ---------------- |
| Unvalidated learning demand    | Build wrong product       | Interview five learners before curriculum expansion                     | Product    | Open             |
| Untrusted code escapes         | Infrastructure compromise | No execution in API; isolated queue worker design before execution      | Security   | Deferred feature |
| Duplicate progression events   | Incorrect XP              | Idempotency and DB uniqueness before gamification                       | API        | Planned          |
| Sensitive analytics            | Privacy harm              | Allowlisted schemas; deletion and retention tests                       | Privacy    | Planned          |
| Cloud spend                    | Unsustainable operation   | Monthly budget alert at 80%, disable optional AI at cap                 | Operations | Planned          |
| Incomplete platform validation | False readiness           | Record actual checks, never equate config parsing with running services | Maintainer | Open             |
