"""Fail when local platform prerequisites are missing."""

import shutil
import subprocess
import sys

failed = False
for command in (
    ["uv", "--version"],
    ["node", "--version"],
    ["npm", "--version"],
    ["docker", "compose", "version"],
    ["docker", "info", "--format", "{{.ServerVersion}}"],
):
    if not shutil.which(command[0]):
        print(f"MISSING: {command[0]}")
        failed = True
        continue
    result = subprocess.run(command, check=False)
    failed |= result.returncode != 0
sys.exit(1 if failed else 0)
