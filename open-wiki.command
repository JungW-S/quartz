#!/bin/zsh

set -e

cd "$(dirname "$0")"

URL="http://localhost:8080/"

(
  for _ in {1..60}; do
    if nc -z 127.0.0.1 8080 >/dev/null 2>&1; then
      open "$URL" || open "http://localhost:8080"
      exit 0
    fi
    sleep 1
  done
  open "http://localhost:8080"
) &

npm run dev
