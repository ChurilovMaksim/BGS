#!/bin/bash
P=/workspace/bgs-derand/phase3/venv/bin/python
for k in 14 15 16 17 18 20; do for fam in 8 16; do for typ in V E; do
 if [ $typ = V ]; then RH="0.65 0.7 0.8 0.9"; else RH="0.12 0.15 0.2 0.3"; fi
 for r in $RH; do for b in 0.1 0.2 0.3 0.4; do $P code/l4_const.py $fam $typ $k $r $b 6 2; done; done
done; done; done
