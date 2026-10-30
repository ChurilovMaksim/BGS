#!/bin/bash
# Line F batch 2: eta grid + tight r1 at eta=2
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1
P=python3
cd computations/verification/lineF/code
$P cert_lift.py V 2.0 4 1.2 55 2.5 128 40 2e-6 1.0 60 40 4 ../logs/certV_eta2_a4_tight.json > ../logs/certV_eta2_a4_tight.out 2>&1 &
for eta in 1.25 1.5 1.75 2.25 2.5 2.75 3.0; do
  case $eta in 1.25|1.5|1.75) K0=4; R2=1.0;; *) K0=5; R2=1.45;; esac
  for a in 4 0 2 6; do
    $P cert_lift.py V $eta $K0 1.2 55 2.5 128 40 1e-3 $R2 70 40 $a ../logs/certV_eta${eta}_a$a.json > ../logs/certV_eta${eta}_a$a.out 2>&1 &
  done
  $P cert_lift.py E $eta $K0 0.8 40 2.5 128 30 1e-3 $R2 70 40 4,0,2,6 ../logs/certE_eta${eta}.json > ../logs/certE_eta${eta}.out 2>&1 &
  wait
done
echo ALLDONE
