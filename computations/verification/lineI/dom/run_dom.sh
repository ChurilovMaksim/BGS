#!/bin/bash
# Line I session 4 item 2: counting certificates, classes 1:3 and 2:1 (m=9,a=2 case; transfers by sym/)
cd /workspace/bgs-lineI/dom
export OMP_NUM_THREADS=3 OPENBLAS_NUM_THREADS=3
P=/workspace/bgs-derand/phase3/venv/bin/python
sha256sum certG_build.py gstates.py law.py rig_dom3b.py run_dom.sh > logs/SHA256_dom.txt
while ! grep -q XCHECK_DONE ../cert2/logs/xcheck.progress 2>/dev/null; do sleep 30; done
for c in 1:3 2:1; do t=${c/:/_}
  nice -n 10 $P certG_build.py V 9 2 2 0.85 36 3.5 150 40 $c data/V36_$t 128 30 > logs/buildV36_$t.log 2>&1
  nice -n 10 $P rig_dom3b.py data/V36_$t 0 3 1.22,1.24,1.25,1.262 32 logs/V36_${t}_dom3b.json > logs/V36_${t}_dom3b.log 2>&1
  echo "$c done $(date)" >> logs/dom.progress
done
echo DOM_DONE >> logs/dom.progress
