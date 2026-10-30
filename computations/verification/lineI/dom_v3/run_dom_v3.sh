#!/bin/bash
# Line I DF4 rerun: rig_dom3b v3 (gmax over exact upper ends) on the unchanged D=8064 matrices of dom/ (classes 1:3, 2:1)
cd "$(dirname "$0")"
export OMP_NUM_THREADS=3 OPENBLAS_NUM_THREADS=3
P=/workspace/bgs-derand/phase3/venv/bin/python
sha256sum certG_build.py gstates.py law.py rig_dom3b.py run_dom_v3.sh > logs/SHA256_dom_v3.txt
sha256sum ../dom/data/V36_1_3.json ../dom/data/V36_1_3_b0_mid.npy ../dom/data/V36_1_3_b0_rad.npy ../dom/data/V36_2_1.json ../dom/data/V36_2_1_b0_mid.npy ../dom/data/V36_2_1_b0_rad.npy > logs/SHA256_inputs.txt
for t in 1_3 2_1; do
  nice -n 10 $P rig_dom3b.py ../dom/data/V36_$t 0 3 1.22,1.24,1.25,1.262 32 logs/V36_${t}_dom3b_v3.json > logs/V36_${t}_dom3b_v3.log 2>&1
  echo "$t done $(date)" >> logs/dom_v3.progress
done
sha256sum logs/V36_1_3_dom3b_v3.json logs/V36_2_1_dom3b_v3.json >> logs/SHA256_dom_v3.txt
echo DOM_V3_DONE >> logs/dom_v3.progress
