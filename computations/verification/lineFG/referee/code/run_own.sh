#!/bin/bash
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1
P=python3
cd computations/verification/lineFG/referee/code
$P own_cert.py V 2 4 1.1 40 2.0 50 30 1.8 36 1e-3 1.0 4,0,2 ../logs/own_V_eta2.json > ../logs/own_V_eta2.out 2>&1
$P own_cert.py E 2 4 0.7 30 2.0 50 30 1.8 30 1e-3 1.0 4,0,2 ../logs/own_E_eta2.json > ../logs/own_E_eta2.out 2>&1
echo ALLDONE >> ../logs/own_V_eta2.out
