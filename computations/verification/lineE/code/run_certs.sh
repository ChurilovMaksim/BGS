#!/bin/bash
# Regenerates the nine k1-kick IFS certificates (cert.py) and their final bounds (bounds.py) into ../logs/.
# Pinned environment used for the committed logs: python-flint 0.9.0, numpy 2.5.4, scipy, sympy (see ../README.md).
# Usage: PY=/path/to/python bash run_certs.sh   (BOUNDS_ONLY=1 reruns only bounds.py on existing certificates)
set -euo pipefail
here=$(cd "$(dirname "$0")" && pwd); out="$here/../logs"; mkdir -p "$out"; PY=${PY:-python3}
export OPENBLAS_NUM_THREADS=1
run(){ name=$1; shift; if [ -z "${BOUNDS_ONLY:-}" ]; then "$PY" "$here/cert.py" "$@" "$out/$name.json" > "$out/$name.out" 2>&1; fi; "$PY" "$here/bounds.py" "$out/$name.json" > "$out/${name}_bounds.out" 2>&1; }
#   name                 eta  L rho K   prec p  r1    r2
run cert_L6              2.0  6 2.0 100 700 40 1e-6  1.0
run cert_L8b_eta2        2.0  8 2.0 170 1200 60 0.05 1.0
run cert_L6_eta1.25      1.25 6 2.0 100 700 60 0.05 1.0
run cert_L6_eta1.5       1.5  6 2.0 100 700 60 0.05 1.0
run cert_L6_eta1.75      1.75 6 2.0 100 700 60 0.05 1.0
run cert_L6r145_eta2.25  2.25 6 2.0 100 700 60 0.05 1.45
run cert_L6r145_eta2.5   2.5  6 2.0 100 700 60 0.05 1.45
run cert_L6r145_eta2.75  2.75 6 2.0 100 700 60 0.05 1.45
run cert_L6r145_eta3.0   3.0  6 2.0 100 700 60 0.05 1.45
