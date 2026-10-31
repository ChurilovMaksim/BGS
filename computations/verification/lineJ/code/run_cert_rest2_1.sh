#!/bin/bash
cd "$(dirname "$0")/.."
export OMP_NUM_THREADS=2 OPENBLAS_NUM_THREADS=2
P="nice -n 10 /workspace/bgs-derand/phase3/venv/bin/python"
$P code/rig_spec.py data/cert/V_-2_s0 2 rest 0.752 0 64 logs/cert/V_-2_s0_b2_rest.json > logs/cert/V_-2_s0_b2_rest.log 2>&1
$P code/rig_spec.py data/cert/V_-2_s0 4 rest 0.836 0 64 logs/cert/V_-2_s0_b4_rest.json > logs/cert/V_-2_s0_b4_rest.log 2>&1
$P code/rig_spec.py data/cert/V_-2_s0 6 rest 0.628 0 64 logs/cert/V_-2_s0_b6_rest.json > logs/cert/V_-2_s0_b6_rest.log 2>&1
$P code/rig_spec.py data/cert/V_-2_s2 1 rest 0.768 0 64 logs/cert/V_-2_s2_b1_rest.json > logs/cert/V_-2_s2_b1_rest.log 2>&1
$P code/rig_spec.py data/cert/V_-2_s2 3 rest 1.247 0 64 logs/cert/V_-2_s2_b3_rest.json > logs/cert/V_-2_s2_b3_rest.log 2>&1
$P code/rig_spec.py data/cert/V_-2_s2 5 rest 0.78 0 64 logs/cert/V_-2_s2_b5_rest.json > logs/cert/V_-2_s2_b5_rest.log 2>&1
$P code/rig_spec.py data/cert/V_-2_s2 7 rest 0.901 0 64 logs/cert/V_-2_s2_b7_rest.json > logs/cert/V_-2_s2_b7_rest.log 2>&1
$P code/rig_spec.py data/cert/V_-2_s4 1 rest 0.816 0 64 logs/cert/V_-2_s4_b1_rest.json > logs/cert/V_-2_s4_b1_rest.log 2>&1
$P code/rig_spec.py data/cert/V_-2_s4 4 rest 0.808 0 64 logs/cert/V_-2_s4_b4_rest.json > logs/cert/V_-2_s4_b4_rest.log 2>&1
$P code/rig_spec.py data/cert/V_-2_s4 6 rest 1.066 0 64 logs/cert/V_-2_s4_b6_rest.json > logs/cert/V_-2_s4_b6_rest.log 2>&1
$P code/rig_spec.py data/cert/V_-2_s6 0 rest 0.711 0 64 logs/cert/V_-2_s6_b0_rest.json > logs/cert/V_-2_s6_b0_rest.log 2>&1
$P code/rig_spec.py data/cert/V_-2_s6 2 rest 0.895 0 64 logs/cert/V_-2_s6_b2_rest.json > logs/cert/V_-2_s6_b2_rest.log 2>&1
$P code/rig_spec.py data/cert/V_-2_s6 4 rest 0.606 0 64 logs/cert/V_-2_s6_b4_rest.json > logs/cert/V_-2_s6_b4_rest.log 2>&1
$P code/rig_spec.py data/cert/V_-2_s6 6 rest 1.042 0 64 logs/cert/V_-2_s6_b6_rest.json > logs/cert/V_-2_s6_b6_rest.log 2>&1
$P code/rig_spec.py data/cert/V_2_s0 0 rest 0.718 0 64 logs/cert/V_2_s0_b0_rest.json > logs/cert/V_2_s0_b0_rest.log 2>&1
$P code/rig_spec.py data/cert/V_2_s0 3 rest 0.808 0 64 logs/cert/V_2_s0_b3_rest.json > logs/cert/V_2_s0_b3_rest.log 2>&1
$P code/rig_spec.py data/cert/V_2_s0 5 rest 0.98 0 64 logs/cert/V_2_s0_b5_rest.json > logs/cert/V_2_s0_b5_rest.log 2>&1
$P code/rig_spec.py data/cert/V_2_s0 7 rest 0.977 0 64 logs/cert/V_2_s0_b7_rest.json > logs/cert/V_2_s0_b7_rest.log 2>&1
$P code/rig_spec.py data/cert/V_2_s2 1 rest 1.03 0 64 logs/cert/V_2_s2_b1_rest.json > logs/cert/V_2_s2_b1_rest.log 2>&1
$P code/rig_spec.py data/cert/V_2_s2 3 rest 0.606 0 64 logs/cert/V_2_s2_b3_rest.json > logs/cert/V_2_s2_b3_rest.log 2>&1
$P code/rig_spec.py data/cert/V_2_s2 5 rest 0.78 0 64 logs/cert/V_2_s2_b5_rest.json > logs/cert/V_2_s2_b5_rest.log 2>&1
$P code/rig_spec.py data/cert/V_2_s2 7 rest 0.901 0 64 logs/cert/V_2_s2_b7_rest.json > logs/cert/V_2_s2_b7_rest.log 2>&1
$P code/rig_spec.py data/cert/V_2_s4 2 rest 0.752 0 64 logs/cert/V_2_s4_b2_rest.json > logs/cert/V_2_s4_b2_rest.log 2>&1
$P code/rig_spec.py data/cert/V_2_s4 4 rest 0.836 0 64 logs/cert/V_2_s4_b4_rest.json > logs/cert/V_2_s4_b4_rest.log 2>&1
$P code/rig_spec.py data/cert/V_2_s4 6 rest 0.628 0 64 logs/cert/V_2_s4_b6_rest.json > logs/cert/V_2_s4_b6_rest.log 2>&1
$P code/rig_spec.py data/cert/V_2_s6 1 rest 0.768 0 64 logs/cert/V_2_s6_b1_rest.json > logs/cert/V_2_s6_b1_rest.log 2>&1
$P code/rig_spec.py data/cert/V_2_s6 3 rest 1.247 0 64 logs/cert/V_2_s6_b3_rest.json > logs/cert/V_2_s6_b3_rest.log 2>&1
$P code/rig_spec.py data/cert/V_2_s6 5 rest 0.78 0 64 logs/cert/V_2_s6_b5_rest.json > logs/cert/V_2_s6_b5_rest.log 2>&1
$P code/rig_spec.py data/cert/V_2_s6 7 rest 0.901 0 64 logs/cert/V_2_s6_b7_rest.json > logs/cert/V_2_s6_b7_rest.log 2>&1
echo REST2_1_DONE
