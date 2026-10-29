"""Minimal local-platform probe. Product API follows in roadmap Day 8."""

import os

import psycopg
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from redis import Redis

app = FastAPI(title="EngineerQuest local platform")


def dependencies_ready() -> bool:
    try:
        with psycopg.connect(
            os.environ["DATABASE_URL"], connect_timeout=2
        ) as connection:
            connection.execute("SELECT 1")
        client: Redis[bytes] = Redis.from_url(
            os.environ["REDIS_URL"], socket_connect_timeout=2, socket_timeout=2
        )
        try:
            return bool(client.ping())
        finally:
            client.close()
    except (KeyError, psycopg.Error, ConnectionError, OSError):
        return False
    except Exception:
        # Readiness must fail closed without returning credentials or driver messages.
        return False


@app.get("/health/live")
def live() -> dict[str, str]:
    return {"status": "alive"}


@app.get("/health/ready")
def ready() -> JSONResponse:
    healthy = dependencies_ready()
    return JSONResponse(
        {"status": "ready" if healthy else "unavailable"},
        status_code=200 if healthy else 503,
    )
