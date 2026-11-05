#!/bin/bash
# research1105b main numerics (sequential jobs, 7 workers each). Logs in ../logs/lvl/
cd /workspace/research1105b/code; PY=/workspace/lineNgas/venv/bin/python; L=../logs/lvl; mkdir -p $L
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1
$PY level.py 33 1 8119 ii,ui $L/p11_s1 >> $L/run.log 2>&1
$PY level.py 33 1 8119 uu $L/p11_s1 4000 >> $L/run.log 2>&1
$PY level.py 33 -1 8119 ii,ui $L/p11_sm1 >> $L/run.log 2>&1
$PY level.py 39 1 47321 ii $L/p13_s1 >> $L/run.log 2>&1
$PY level.py 39 1 47321 iu,uu $L/p13_s1 4000 >> $L/run.log 2>&1
$PY level.py 33 1 8119 iu $L/p11_s1 >> $L/run.log 2>&1
$PY level.py 39 1 47321 ui $L/p13_s1 >> $L/run.log 2>&1
$PY level.py 51 1 1607521 iu,ui,uu $L/p17_s1 4000 >> $L/run.log 2>&1
$PY level.py 51 1 1607521 ii $L/p17_s1 >> $L/run.log 2>&1
echo ALLDONE >> $L/run.log
