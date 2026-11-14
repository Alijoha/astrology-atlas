#!/usr/bin/env bash
set -e
cd -- "$(dirname -- "${BASH_SOURCE[0]}")"
if ! command -v npm >/dev/null 2>&1; then
  echo "Node.js is needed. Install the LTS version from https://nodejs.org/, then run this file again."
  exit 1
fi
if command -v curl >/dev/null 2>&1 && curl -fsS --max-time 1 http://localhost:5173/ >/dev/null 2>&1; then
  echo "An app is already running on port 5173."
  echo "In the Terminal running your old Astrology Atlas, press Control+C. Then run this file again."
  echo "Using the same port keeps your saved charts in the same browser storage."
  exit 1
fi
if [ ! -d node_modules ]; then
  echo "Installing Astrology Atlas. This is needed only the first time in this folder."
  npm ci
fi
echo "Starting Astrology Atlas 4.1. Keep this Terminal window open."
echo "When Vite says ready, open http://localhost:5173 or refresh the existing page."
npm run dev
