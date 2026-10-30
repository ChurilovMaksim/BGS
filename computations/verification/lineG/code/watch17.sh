#!/bin/bash
# wait for batch_orb to finish each m=17 file, then evaluate (detached)
cd computations/verification/lineG/code; PY=python3
for k in k1 full; do
  until grep -q "done $k 17" ../logs/batch_orb.log; do sleep 120; done
  sha256sum ../logs/Torb_${k}_m17.bin >> ../logs/eval17_$k.log
  nice -n 10 $PY eval17.py $k >> ../logs/eval17_$k.log 2>&1
  nice -n 10 $PY formula_table.py $k 17 >> ../logs/eval17_$k.log 2>&1
  cp ../logs/eval17_$k.* <backup-dir>/
done
