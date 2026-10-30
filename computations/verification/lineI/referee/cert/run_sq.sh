#!/bin/bash
# Line I (2): certify twisted d=7 operators (rho=(2,8), m≡9 mod 24 case) spectra in |z|<R (V: R<=1.55 < lam^{1/4}; E: R=1.0)
P=/workspace/bgs-derand/phase3/venv/bin/python
cd /workspace/bgs-lineI/cert
export OMP_NUM_THREADS=3 OPENBLAS_NUM_THREADS=3
sha256sum certG_build.py gstates.py law.py rig_spec.py > logs/SHA256_run_sq.txt
for c in 1:3 2:1 0:1 1:2 1:5 0:3 1:0 0:2; do
  t=${c/:/_}
  nice -n 10 $P certG_build.py E 9 2 2 0.85 22 3.5 150 40 $c data/E_$t 128 18 > logs/buildE_$t.log 2>&1
  nice -n 10 $P rig_spec.py data/E_$t 0 rest 1.0,1.2 0 20 logs/E_${t}_rest.json > logs/E_${t}_rest.log 2>&1
  rm -f data/E_${t}_b0_*.npy
  nice -n 10 $P certG_build.py V 9 2 2 0.85 30 3.5 150 40 $c data/V_$t 128 24 > logs/buildV_$t.log 2>&1
  nice -n 10 $P rig_spec.py data/V_$t 0 rest 1.45,1.5,1.55 0 24 logs/V_${t}_rest.json > logs/V_${t}_rest.log 2>&1
  rm -f data/V_${t}_b0_*.npy
  echo "$c done $(date)" >> logs/run_sq.progress
done
echo ALL_DONE >> logs/run_sq.progress
