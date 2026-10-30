#!/bin/bash
# Line H referee fixes: certificate re-runs with archived rig_spec v4 (sha in logs/SHA256_code_v4_runs.txt)
P=/workspace/bgs-derand/phase3/venv/bin/python
cd /workspace/bgs-lineH/code
export OMP_NUM_THREADS=3
nice -n 10 $P rig_spec.py ../data/prodV 0 dom 1.5,1.55,1.6 0.05,0.08,0.1,0.13 32 ../logs/v4_V0_dom.json > ../logs/v4_V0_dom.log 2>&1 &
( nice -n 10 $P cert49_build.py V -1 2 0.85 30 3.5 150 40 2,4,6 ../data/prodVr 128 24 > ../logs/v4_prodVr_build.log 2>&1
  for b in 0 2 4 6; do nice -n 10 $P rig_spec.py ../data/prodE $b rest 1.0,1.2 0 20 ../logs/v4_E${b}_rest.json > ../logs/v4_E${b}_rest.log 2>&1; done
  for b in 4 2 6; do nice -n 10 $P rig_spec.py ../data/prodVr $b rest 1.45,1.5,1.55 0 24 ../logs/v4_V${b}_rest.json > ../logs/v4_V${b}_rest.log 2>&1; done
  echo SEQ_DONE ) &
wait; echo RUNV4_DONE
