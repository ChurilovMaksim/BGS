#!/bin/bash
# Line J: arb-certified sector blocks (V: K0=5 rho=1.2 K=60 beta=2.5; E: K0=4 rho=0.8 K=40), a=+2 (case m=9), a=-2 (case m=15)
cd "$(dirname "$0")/.."
export OMP_NUM_THREADS=2 OPENBLAS_NUM_THREADS=2
P=/workspace/bgs-derand/phase3/venv/bin/python
CL=1:3,2:1,0:1,1:2,1:5,0:3,1:0,0:2
for A in 2 -2; do M=9; [ $A = -2 ] && M=15
for S in 0 2 4 6; do
  BGS_SECTOR=$S nice -n 10 $P code/certG_build_sector.py V $M $A 5 1.2 60 2.5 150 40 $CL data/cert/V_${A}_s$S 128 60 > logs/cert/build_V_${A}_s$S.log 2>&1
  BGS_SECTOR=$S nice -n 10 $P code/certG_build_sector.py E $M $A 4 0.8 40 2.5 150 40 $CL data/cert/E_${A}_s$S 128 40 > logs/cert/build_E_${A}_s$S.log 2>&1
done; done
echo BUILD_DONE
