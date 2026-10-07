#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
# These validate the sealed existing runs without altering their provenance.
python3 validate_manifest.py runs/replay/manifest.json --root .
python3 validate_manifest.py runs/algebra/manifest.json --root .
# Fresh reruns require new output directories. Replace the names below when used.
# python3 run_experiment.py --root . --contract replay_contract.json --input controls/block_controls.py --input controls/write_result.py --input inputs/matrix_block_extension.md --input inputs/scalar_report.md --input inputs/scalar_audit.md --output runs/replay_fresh --result runs/replay_fresh/results.json --timeout 120 --max-output-bytes 1048576 --max-memory-bytes 4294967296 --max-cpu-seconds 60 --max-cores 1 --max-threads 1 -- python3 controls/write_result.py controls/block_controls.py runs/replay_fresh/results.json
# python3 run_experiment.py --root . --contract algebra_contract.json --input controls/exact_algebra.py --input controls/write_result.py --input inputs/matrix_block_extension.md --input inputs/scalar_report.md --input inputs/scalar_audit.md --output runs/algebra_fresh --result runs/algebra_fresh/results.json --timeout 120 --max-output-bytes 1048576 --max-memory-bytes 4294967296 --max-cpu-seconds 60 --max-cores 1 --max-threads 1 -- python3 controls/write_result.py controls/exact_algebra.py runs/algebra_fresh/results.json
