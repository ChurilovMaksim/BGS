#!/bin/bash
# Line F certificate batch 1: k1 kick eta=2, full alphabet lifted operators
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1
P=python3
cd computations/verification/lineF/code
for a in 4 0 2 6; do
  $P cert_lift.py V 2.0 4 1.2 55 2.5 128 40 1e-3 1.0 60 40 $a ../logs/certV_eta2_a$a.json > ../logs/certV_eta2_a$a.out 2>&1 &
done
$P cert_lift.py E 2.0 4 0.8 40 2.5 128 30 1e-3 1.0 60 40 4,0,2,6 ../logs/certE_eta2.json > ../logs/certE_eta2.out 2>&1 &
wait
echo ALLDONE
