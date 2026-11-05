#!/bin/bash
# research1105b: reduced tail of the main queue (replaces run_main.sh steps 7-9 after load from other box jobs made them too slow).
cd /workspace/research1105b/code; PY=/workspace/lineNgas/venv/bin/python; L=../logs/lvl
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1
while pgrep -f "level.py 33 1 8119 iu" > /dev/null; do sleep 20; done
echo "p11 iu finished (exact)" >> $L/run.log
$PY level.py 39 1 47321 ui $L/p13_s1 4000 >> $L/run.log 2>&1
$PY level.py 51 1 1607521 iu,ui,uu $L/p17_s1 3000 >> $L/run.log 2>&1
echo ALLDONE >> $L/run.log
