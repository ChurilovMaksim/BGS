# Reproduce the exact controls

These commands are for this standalone research directory. They do not
operate on the BGS repository. Use new run-directory names for each execution.

## Jack and independent C++ controls

    python3 audit_tools/run_experiment.py --root . --contract contract.json \
      --input scripts/run_controls.py --input scripts/exact_checks.py \
      --input scripts/schur_ssyt_control.cpp --input audit_tools/run_experiment.py \
      --input audit_tools/validate_manifest.py \
      --output runs/exact_reproduction \
      --result runs/exact_reproduction/results.json \
      --result runs/exact_reproduction/cpp_results.json \
      --result runs/exact_reproduction/subcommands.json \
      --timeout 60 --max-output-bytes 1048576 --max-memory-bytes 1073741824 \
      --max-cpu-seconds 50 --max-cores 1 --max-threads 1 \
      -- python3 scripts/run_controls.py runs/exact_reproduction

    python3 audit_tools/validate_manifest.py \
      runs/exact_reproduction/manifest.json --root .

## Direct density and CSE trace-log controls

    python3 audit_tools/run_experiment.py --root . --contract pfaffian_contract.json \
      --input scripts/pfaffian_controls.py --input audit_tools/run_experiment.py \
      --input audit_tools/validate_manifest.py \
      --output runs/pfaffian_reproduction \
      --result runs/pfaffian_reproduction/results.json \
      --timeout 60 --max-output-bytes 1048576 --max-memory-bytes 1073741824 \
      --max-cpu-seconds 50 --max-cores 1 --max-threads 1 \
      -- python3 scripts/pfaffian_controls.py runs/pfaffian_reproduction/results.json

    python3 audit_tools/validate_manifest.py \
      runs/pfaffian_reproduction/manifest.json --root .

The Wolfram source can be submitted to a Wolfram Language kernel separately.
Its remote receipt is preserved, and is not re-executed by the local commands.

Lean source compilation requires installing a compatible Lean 4/Mathlib
environment. No successful compilation is asserted by this package.

## Exact cumulants, critical blocks and sixth moments

    python3 audit_tools/run_experiment.py --root . --contract cumulant_contract.json \
      --input scripts/cumulant_formula_controls.py \
      --input scripts/pfaffian_controls.py --input audit_tools/run_experiment.py \
      --input audit_tools/validate_manifest.py \
      --output runs/cumulant_reproduction \
      --result runs/cumulant_reproduction/results.json \
      --timeout 60 --max-output-bytes 1048576 --max-memory-bytes 1073741824 \
      --max-cpu-seconds 50 --max-cores 1 --max-threads 1 \
      -- python3 scripts/cumulant_formula_controls.py runs/cumulant_reproduction/results.json

    python3 audit_tools/validate_manifest.py \
      runs/cumulant_reproduction/manifest.json --root .

