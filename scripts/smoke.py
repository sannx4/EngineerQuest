"""Exercise actual dependency readiness and local mail endpoint."""

import json
import subprocess
import urllib.request

for url, expected in [
    ("http://127.0.0.1:8000/health/live", "alive"),
    ("http://127.0.0.1:8000/health/ready", "ready"),
]:
    with urllib.request.urlopen(url, timeout=10) as response:
        assert response.status == 200
        assert json.load(response)["status"] == expected
with urllib.request.urlopen(
    "http://127.0.0.1:8025/api/v1/info", timeout=10
) as response:
    assert response.status == 200
print("API liveness, dependency readiness and mail endpoint passed")

# Verify the actual seeded database, expiring worker heartbeat and collector endpoint.


def compose(*args: str) -> str:
    return subprocess.check_output(
        ["docker", "compose", "exec", "-T", *args], text=True
    ).strip()


assert (
    compose(
        "postgres",
        "psql",
        "-U",
        "engineerquest",
        "-d",
        "engineerquest",
        "-Atc",
        "SELECT value FROM platform_metadata WHERE key='schema_version'",
    )
    == "local-1"
)
assert int(compose("redis", "redis-cli", "TTL", "engineerquest:worker:heartbeat")) > 0
compose(
    "api",
    "python",
    "-c",
    "import urllib.request; "
    "r=urllib.request.build_opener(urllib.request.ProxyHandler({}))"
    ".open('http://collector:13133', timeout=5); assert r.status == 200",
)
print("Database seed, worker heartbeat and collector HTTP health passed")
