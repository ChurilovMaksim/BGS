#!/bin/bash
# two workers: reps W, W+2, ...
cd "$(dirname "$0")/.."
W=$1
export OMP_NUM_THREADS=2 OPENBLAS_NUM_THREADS=2 MKL_NUM_THREADS=2
for r in $(seq $W 2 31); do nice -n 10 /workspace/bgs-derand/phase3/venv/bin/python code/pipe16.py $r; done
echo WORKER_DONE $W
