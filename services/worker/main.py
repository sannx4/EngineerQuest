"""Local platform worker heartbeat; durable job processing comes later."""

import os
import time

from redis import Redis


def main() -> None:
    client: Redis[bytes] = Redis.from_url(
        os.environ["REDIS_URL"], socket_connect_timeout=2, socket_timeout=2
    )
    while True:
        client.set("engineerquest:worker:heartbeat", "alive", ex=15)
        time.sleep(5)


if __name__ == "__main__":
    main()
