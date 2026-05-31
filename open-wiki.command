#!/bin/zsh

set -e

cd "$(dirname "$0")"

URL="http://localhost:8080/topics/determinantial-modules"

(
  sleep 3
  open "$URL" || open "http://localhost:8080"
) &

npm run dev
