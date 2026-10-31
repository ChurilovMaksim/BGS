#!/bin/bash
# Line K integration reruns (isolated copy; author logs compared byte-for-byte)
PY=/workspace/bgs-derand/phase3/venv/bin/python
cd /tmp/lk/rerun/pkt
for s in k3_harg k1_cone_check k2_SZ k2_large_v2; do
  cp logs/$s.log /tmp/lk/rerun/$s.author.log; cp logs/$s.json /tmp/lk/rerun/$s.author.json
  ( time nice -n 10 $PY code/$s.py > /tmp/lk/rerun/$s.out 2>&1 ) 2> /tmp/lk/rerun/$s.time
  if cmp -s /tmp/lk/rerun/$s.out /tmp/lk/rerun/$s.author.log; then r=log_identical; else r=log_DIFF; fi
  if cmp -s logs/$s.json /tmp/lk/rerun/$s.author.json; then j=json_identical; else j=json_DIFF; fi
  echo "$s $r $j" >> /tmp/lk/rerun/summary.txt
done
(cd K2 && nice -n 10 $PY code/w1_weil_check.py > /tmp/lk/rerun/w1_weil_check.out 2>&1; cmp -s /tmp/lk/rerun/w1_weil_check.out logs/w1_weil_check.log && echo "w1_weil_check log_identical" >> /tmp/lk/rerun/summary.txt || echo "w1_weil_check log_DIFF" >> /tmp/lk/rerun/summary.txt)
echo DONE >> /tmp/lk/rerun/summary.txt
