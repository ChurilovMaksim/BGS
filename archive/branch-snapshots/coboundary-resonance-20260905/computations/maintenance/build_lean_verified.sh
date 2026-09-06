#!/usr/bin/env bash
# Fail closed on compiler errors even when retaining the complete log.
set -euo pipefail
if [[ $# -ne 1 ]]; then
  echo 'Usage: build_lean_verified.sh LOG_PATH' >&2
  exit 2
fi
log=$(realpath -m "$1")
mkdir -p "$(dirname "$log")"
# A negative control for the exact failure mode found in run 33971705529.
if bash -c 'set -o pipefail; (exit 9) | tee /dev/null' >/dev/null 2>&1; then
  echo 'Pipeline failure propagation is broken' >&2
  exit 1
fi
cd "$(dirname "$0")/../../formalization"
lake build 2>&1 | tee "$log"
if grep -Eq '^error:|build failed|Tactic .* failed' "$log"; then
  echo 'Compiler error found despite a zero command exit status' >&2
  exit 1
fi
echo 'Verified Lean build: command status and error-free log agree.'
