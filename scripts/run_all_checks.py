#!/usr/bin/env python3
"""Run all basic wiki checks and build Quartz when npm is available."""

from pathlib import Path
import shutil
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]

CHECKS = [
    [sys.executable, "scripts/validate_frontmatter.py"],
    [sys.executable, "scripts/validate_claims.py"],
    [sys.executable, "scripts/validate_edges.py"],
    [sys.executable, "scripts/validate_links.py"],
    [sys.executable, "scripts/generate_mermaid_maps.py"],
]
BUILD = ["npm", "run", "quartz", "--", "build"]


def run(command):
    print(f"$ {' '.join(command)}", flush=True)
    completed = subprocess.run(command, cwd=ROOT)
    if completed.returncode != 0:
        sys.exit(completed.returncode)


def main():
    for command in CHECKS:
        run(command)

    if shutil.which("npm") is None:
        print("Quartz build skipped: npm is not available.")
        return

    run(BUILD)


if __name__ == "__main__":
    main()
