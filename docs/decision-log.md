# Decision log

- Batch 001: use modular monolith with isolated workers; see ADR-001/002.
- Limit v0.1 to first learning loop; future journeys remain specifications.
- Never label planned research or unrun deployment checks completed.
- Use local-only dummy development database credentials; no production secrets in Git.
- Future daily batches require a new session or an external scheduler; no automatic schedule is installed.
