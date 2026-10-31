#!/bin/bash
# J3: arb-certified Galerkin blocks for the 32 distinct (sign, block-action) 2-state factors of the (±2,16) automaton.
# V: K0=5 rho=1.2 K=60 beta=2.5; E: K0=4 rho=0.8 K=40 (as Line J). untwisted ('none') and the 8 d=7 classes.
cd "$(dirname "$0")/.."
export OMP_NUM_THREADS=2 OPENBLAS_NUM_THREADS=2
P=/workspace/bgs-derand/phase3/venv/bin/python
CL=1:3,2:1,0:1,1:2,1:5,0:3,1:0,0:2
python3 -c "import json;[print(i,c.split(',')[0],c.split(',')[1],b) for i,(c,b,n) in enumerate(json.load(open('logs/blocks16_reps.json'))['reps'])]" | while read I M A B; do
  for T in V E; do
    if [ $T = V ]; then PAR="5 1.2 60 2.5 150 40"; K2=60; else PAR="4 0.8 40 2.5 150 40"; K2=40; fi
    BGS16_CASE=$M,$A BGS16_BLOCK=$B nice -n 10 $P code/certG_build16.py $T $M $A $PAR none data/cert/${T}_r${I}_u 128 $K2 > logs/cert/build_${T}_r${I}_u.log 2>&1
    BGS16_CASE=$M,$A BGS16_BLOCK=$B nice -n 10 $P code/certG_build16.py $T $M $A $PAR $CL data/cert/${T}_r${I}_t 128 $K2 > logs/cert/build_${T}_r${I}_t.log 2>&1
  done
done
echo BUILD_DONE
