#!/bin/bash
cd /workspace/bgs-lineN/N8b
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
cat $1 | xargs -P 7 -L 1 bash -c 'timeout 5400 /workspace/bgs-lineN/.venv/bin/python code/b_cline.py $0 $1 $2 $3 > /dev/null 2>> logs/b_cline2.err || echo "FAIL $0 $1 $2 $3" >> logs/b_cline2.err'
echo DONE >> logs/b_cline2.err
