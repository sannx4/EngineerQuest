.PHONY: bootstrap check doctor smoke
bootstrap:
	chmod a+r scripts/init.sql infra/observability/collector.yaml
	uv sync --frozen
	npm ci --ignore-scripts
	uv run --frozen pre-commit install
check:
	uv run --frozen ruff check .
	uv run --frozen mypy
	uv run --frozen pytest
	npm run lint
	npm run typecheck
	npm run format:check
doctor:
	python scripts/doctor.py
smoke:
	python scripts/smoke.py
