#!/bin/bash
# research1105b: independent recomputation of proper-level Devs (d33/d39 cross-check), spec 'a' = all betas mod D
cd /workspace/research1105b/code; PY=/workspace/lineNgas/venv/bin/python; L=../logs/prop; mkdir -p $L
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1
for sg in 1 -1; do
 for D in 7 23 353; do $PY level.py 33 $sg $D a $L/m33_s${sg}_D$D >> $L/run.log 2>&1; done
 $PY level.py 33 $sg 161 aa $L/m33_s${sg}_D161 >> $L/run.log 2>&1
 for D in 7 79 599; do $PY level.py 39 $sg $D a $L/m39_s${sg}_D$D >> $L/run.log 2>&1; done
 $PY level.py 39 $sg 553 aa $L/m39_s${sg}_D553 >> $L/run.log 2>&1
done
$PY level.py 69 1 47 a $L/m69_s1_D47 >> $L/run.log 2>&1
$PY level.py 69 -1 47 a $L/m69_s-1_D47 >> $L/run.log 2>&1
echo ALLDONE >> $L/run.log
