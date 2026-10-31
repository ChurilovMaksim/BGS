#!/bin/bash
# float survey: sector blocks, case m=9 (a=+2) and m=15 (a=-2), K0=2 K=36/30
cd "$(dirname "$0")/.."
P=/workspace/bgs-derand/phase3/venv/bin/python
CL=1:3,2:1,0:1,1:2,1:5,0:3,1:0,0:2
for A in 2 -2; do M=9; [ $A = -2 ] && M=15
for S in 0 2 4 6; do
  BGS_SECTOR=$S nice -n 10 $P code/certG_build_sector.py V $M $A 2 0.85 36 3.5 150 40 $CL data/sec/V_${A}_s$S 128 30 > logs/build_V_${A}_s$S.log 2>&1
  BGS_SECTOR=$S nice -n 10 $P code/certG_build_sector.py E $M $A 2 0.85 22 3.5 150 40 $CL data/sec/E_${A}_s$S 128 18 > logs/build_E_${A}_s$S.log 2>&1
done; done
echo DONE
