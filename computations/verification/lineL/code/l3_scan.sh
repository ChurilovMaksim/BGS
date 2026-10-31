#!/bin/bash
# scan parameters of the OP_abs certificate
P=/workspace/bgs-derand/phase3/venv/bin/python
for fam in 8 16; do for typ in V E; do
 if [ $typ = V ]; then RH="0.7 0.8 1.0 1.2"; else RH="0.15 0.2 0.3 0.5"; fi
 for k in 24 30 40; do for r in $RH; do for b in 0.2 0.4 0.8; do
  $P code/l3_op_cert.py $fam $typ $k $r $b 6 2
 done; done; done
done; done
