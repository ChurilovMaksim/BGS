#!/bin/bash
cd "$(dirname "$0")/.."
export OMP_NUM_THREADS=2 OPENBLAS_NUM_THREADS=2
P="nice -n 10 /workspace/bgs-derand/phase3/venv/bin/python"
$P code/rig_dom3b.py data/cert/V_2_s0 2 3 0.9 32 logs/cert/V_2_s0_b2_dom.json > logs/cert/V_2_s0_b2_dom.log 2>&1
$P code/rig_disc.py data/cert/V_2_s0 2 3 2.580264024 1e-9,1e-8,1e-7 32 logs/cert/V_2_s0_b2_disc.json > logs/cert/V_2_s0_b2_disc.log 2>&1
$P code/rig_dom3b.py data/cert/V_2_s4 1 3 0.8 32 logs/cert/V_2_s4_b1_dom.json > logs/cert/V_2_s4_b1_dom.log 2>&1
$P code/rig_disc.py data/cert/V_2_s4 1 3 0.07946484 1e-9,1e-8,1e-7 32 logs/cert/V_2_s4_b1_disc.json > logs/cert/V_2_s4_b1_disc.log 2>&1
$P code/rig_dom3b.py data/cert/V_2_s6 0 3 1.0 32 logs/cert/V_2_s6_b0_dom.json > logs/cert/V_2_s6_b0_dom.log 2>&1
$P code/rig_disc.py data/cert/V_2_s6 0 3 2.931230567 1e-9,1e-8,1e-7 32 logs/cert/V_2_s6_b0_disc.json > logs/cert/V_2_s6_b0_disc.log 2>&1
$P code/rig_dom3b.py data/cert/V_-2_s0 1 3 0.8 32 logs/cert/V_-2_s0_b1_dom.json > logs/cert/V_-2_s0_b1_dom.log 2>&1
$P code/rig_disc.py data/cert/V_-2_s0 1 3 -2.173859942 1e-9,1e-8,1e-7 32 logs/cert/V_-2_s0_b1_disc.json > logs/cert/V_-2_s0_b1_disc.log 2>&1
$P code/rig_dom3b.py data/cert/V_-2_s2 0 3 1.0 32 logs/cert/V_-2_s2_b0_dom.json > logs/cert/V_-2_s2_b0_dom.log 2>&1
$P code/rig_disc.py data/cert/V_-2_s2 0 3 1.257559638 1e-9,1e-8,1e-7 32 logs/cert/V_-2_s2_b0_disc.json > logs/cert/V_-2_s2_b0_disc.log 2>&1
$P code/rig_dom3b.py data/cert/V_-2_s4 2 3 0.9 32 logs/cert/V_-2_s4_b2_dom.json > logs/cert/V_-2_s4_b2_dom.log 2>&1
$P code/rig_disc.py data/cert/V_-2_s4 2 3 -2.580264024 1e-9,1e-8,1e-7 32 logs/cert/V_-2_s4_b2_disc.json > logs/cert/V_-2_s4_b2_disc.log 2>&1
echo TRACKED_DONE
