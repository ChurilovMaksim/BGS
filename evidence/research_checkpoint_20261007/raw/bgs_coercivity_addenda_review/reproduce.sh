#!/bin/sh
set -eu
ROOT=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
cd "$ROOT"
OUT=${1:-controls_replay}
python3 run_experiment.py --root "$ROOT" --contract "$ROOT/contract.json" --input checks.py --output "$OUT" --result "$OUT/results.json" --timeout 120 --max-output-bytes 1048576 --max-memory-bytes 2147483648 --max-cpu-seconds 90 --max-cores 1 --max-threads 1 -- python3 checks.py "$OUT/results.json"
python3 validate_manifest.py "$OUT/manifest.json" --root "$ROOT"
