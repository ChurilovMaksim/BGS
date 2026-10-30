#!/bin/bash
# negative controls (must FAIL to certify)
export OMP_NUM_THREADS=1
P=python3
cd computations/verification/lineF/code
nice -n 19 $P cert_lift.py V 2.0 4 1.2 55 2.5 128 40 1e-3 0.85 60 40 2 ../logs/neg_r2_085_a2.json > ../logs/neg_r2_085_a2.out 2>&1 &
nice -n 19 $P cert_lift.py V 2.0 4 1.2 25 2.5 128 40 1e-3 1.0 60 40 4 ../logs/neg_K25_a4.json > ../logs/neg_K25_a4.out 2>&1 &
nice -n 19 $P cert_lift.py V 2.0 2 1.2 55 2.5 128 40 1e-3 1.0 60 40 4 ../logs/neg_K0_2_a4.json > ../logs/neg_K0_2_a4.out 2>&1 &
wait; echo NEGDONE
