#!/bin/bash
# direct certificate of a symmetry-transferred case, as a consistency check: m=15, a=-2, class 1:3 (V and E)
P=/workspace/bgs-derand/phase3/venv/bin/python
cd /workspace/bgs-lineI/cert2
export OMP_NUM_THREADS=3 OPENBLAS_NUM_THREADS=3
sha256sum certG_build.py gstates.py law.py rig_spec.py > logs/SHA256_xcheck.txt
nice -n 10 $P certG_build.py E 15 -2 2 0.85 22 3.5 150 40 1:3 data/E15m_1_3 128 18 > logs/buildE15m_1_3.log 2>&1
nice -n 10 $P rig_spec.py data/E15m_1_3 0 rest 1.0 0 20 logs/E15m_1_3_rest.json > logs/E15m_1_3_rest.log 2>&1
rm -f data/E15m_1_3_b0_*.npy
nice -n 10 $P certG_build.py V 15 -2 2 0.85 30 3.5 150 40 1:3 data/V15m_1_3 128 24 > logs/buildV15m_1_3.log 2>&1
nice -n 10 $P rig_spec.py data/V15m_1_3 0 rest 1.45 0 24 logs/V15m_1_3_rest.json > logs/V15m_1_3_rest.log 2>&1
rm -f data/V15m_1_3_b0_*.npy
echo XCHECK_DONE $(date) >> logs/xcheck.progress
