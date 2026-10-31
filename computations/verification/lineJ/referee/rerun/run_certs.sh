#!/bin/bash
# referee reruns: outputs only under /workspace/audit/lineJ/rerun/cert ; author tree read-only
export OMP_NUM_THREADS=2 OPENBLAS_NUM_THREADS=2 PYTHONDONTWRITEBYTECODE=1
P="nice -n 10 /workspace/bgs-derand/phase3/venv/bin/python"
J=/workspace/bgs-lineJ; O=/workspace/audit/lineJ/rerun/cert
cd $J
# all 6 disc certs, author args
$P code/rig_disc.py $J/data/cert/V_2_s4 1 3 0.07946484 1e-9,1e-8,1e-7 32 $O/V_2_s4_b1_disc.json > $O/V_2_s4_b1_disc.log 2>&1
$P code/rig_disc.py $J/data/cert/V_2_s0 2 3 2.580264024 1e-9,1e-8,1e-7 32 $O/V_2_s0_b2_disc.json > $O/V_2_s0_b2_disc.log 2>&1
$P code/rig_disc.py $J/data/cert/V_2_s6 0 3 2.931230567 1e-9,1e-8,1e-7 32 $O/V_2_s6_b0_disc.json > $O/V_2_s6_b0_disc.log 2>&1
$P code/rig_disc.py $J/data/cert/V_-2_s0 1 3 -2.173859942 1e-9,1e-8,1e-7 32 $O/V_-2_s0_b1_disc.json > $O/V_-2_s0_b1_disc.log 2>&1
# disc with different radius / larger p (robustness) and the other Z/3 orbit member as target
$P code/rig_disc.py $J/data/cert/V_2_s4 1 3 2.17385994 5e-8,2e-7 48 $O/V_2_s4_b1_disc_alt.json > $O/V_2_s4_b1_disc_alt.log 2>&1
# count certs
$P code/rig_dom3b.py $J/data/cert/V_2_s4 1 3 0.8 32 $O/V_2_s4_b1_dom.json > $O/V_2_s4_b1_dom.log 2>&1
$P code/rig_dom3b.py $J/data/cert/V_2_s6 0 3 1.0 32 $O/V_2_s6_b0_dom.json > $O/V_2_s6_b0_dom.log 2>&1
$P code/rig_dom3b.py $J/data/cert/V_-2_s4 2 3 0.9 32 $O/V_-2_s4_b2_dom.json > $O/V_-2_s4_b2_dom.log 2>&1
# rest certs sample (incl. largest R=1.247 and slowest)
for a in "V_2_s6 3 1.247 64" "V_2_s6 4 1.247 64" "V_2_s2 4 0.606 64" "V_2_s2 5 0.78 64" "V_2_s4 0 1.176 64" "V_-2_s0 0 1.176 64" "V_-2_s2 3 1.247 64" "V_2_s0 6 1.02 64" "V_2_s4 2 0.699 64" "E_2_s4 1 0.45 24" "E_-2_s6 0 0.45 24" "E_2_s0 7 0.45 24"; do
  set -- $a; pre=$1; b=$2; R=$3; p=$4
  # use the author's actual R from their json
  R=$(/workspace/bgs-derand/phase3/venv/bin/python -c "import json;print(json.load(open('$J/logs/cert/${pre}_b${b}_rest.json'))['R'])")
  $P code/rig_spec.py $J/data/cert/$pre $b rest $R 0 $p $O/${pre}_b${b}_rest.json > $O/${pre}_b${b}_rest.log 2>&1
done
echo ALLDONE
