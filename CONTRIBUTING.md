# Contributing

Use a scoped issue with acceptance criteria, a feature branch and a PR linked to evidence.
Commit format: `type(scope): summary` (feat, fix, docs, test, build, ci, chore, refactor).
Run `make bootstrap check doctor`. Changes must include relevant tests, migration/rollback
notes and risk review. Never commit secrets or participant contact information.
Keep each task in its existing isolated checkout; do not create worktrees by default.
CI is required before merge. Keep failed and unrun checks explicit in evidence.
