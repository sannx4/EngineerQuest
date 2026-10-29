# EngineerQuest

A gamified learning platform for software engineers, currently at the foundation stage.

## Development

Requires Python 3.12+, uv, Node 22+, npm, Docker Engine and Compose v2.

```sh
make bootstrap
make check
make doctor
docker compose up --build -d
make smoke
```

See [onboarding](docs/runbooks/onboarding.md), [PRD](docs/product/PRD.md), and
[batch evidence](docs/evidence/batch-001.md). Mobile has a minimal Expo shell; admin is a placeholder;
no learner authentication or learning features are implemented yet.
