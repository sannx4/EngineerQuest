# Local platform onboarding

Use the existing isolated checkout. Requires Python 3.12+, Node 22+, uv 0.12.23 and Docker
with Compose v2. Run `make bootstrap check doctor` from repository root. Bootstrap is
repeatable and uses frozen Python and npm locks. Python and JS gates run locally and in CI.

Run `docker compose up --build --wait --wait-timeout 180`, then `make smoke`.
Cloud sessions with a proxy CA use `docker compose -f compose.yaml -f compose.cloud.yaml up --build --wait --wait-timeout 180`.
The cloud override mounts the trusted system bundle for networked build steps without
persisting certificates. Do not disable TLS verification or change proxy configuration.

PostgreSQL and Redis are private to Compose. Mail UI and API bind to loopback only.
Credentials in Compose are development-only and must never be reused in production.
Collector validates configuration; its HTTP health extension is on internal port 13133.
Worker heartbeat expires after 15 seconds if worker stops. This is not a durable queue.
Mobile has locked Expo/React Native dependencies and a minimal shell. Native simulator/device validation is pending. Run `npm run start -w @engineerquest/mobile` for Metro.

`docker compose down` preserves data; `docker compose down -v` DESTROYS LOCAL DATA.
Only use volume deletion against disposable development data. Init SQL is a local platform
metadata seed, not the product migration system. After reset, verify seed with
`docker compose exec -T postgres psql -U engineerquest -c "SELECT * FROM platform_metadata"`.
Run init SQL again using psql to verify idempotency. Domain Alembic migrations are Day 9.

Outage check: stop Redis; readiness must become 503 while liveness stays 200; restart
Redis and worker, then rerun smoke. Never stop other projects' services.
Rollback: stop this Compose project and revert its feature commit. No deployed user data exists.

PR creation requires GitHub API access in addition to Git push access. If API policy blocks
`api.github.com`, review the saved environment network addition and apply it in settings.
