#!/bin/bash
cd /workspace/audit/lineI/delta/code
export OMP_NUM_THREADS=3 OPENBLAS_NUM_THREADS=3
P=/workspace/bgs-derand/phase3/venv/bin/python
nice -n 10 $P certG_build.py V 9 2 2 0.85 36 3.5 150 40 2:1 ../data/V36_2_1 128 30 > ../logs/buildV36_2_1.log 2>&1
sha256sum ../data/V36_2_1_b0_mid.npy ../data/V36_2_1_b0_rad.npy > ../logs/sha_V36_2_1.txt
nice -n 10 $P rig_dom3b.py ../data/V36_2_1 0 3 1.262 32 ../logs/V36_2_1_dom3b_rerun.json > ../logs/V36_2_1_dom3b_rerun.log 2>&1
echo DONE >> ../logs/sha_V36_2_1.txt
