#!/bin/bash
cd computations/verification/lineG/code
P=python3
for k in k1 full; do $P run_orb.py $k 15 2.0 ../logs/Torb_${k}_m15.bin 7; $P -c "
import numpy as np; A=np.fromfile('../logs/Torb_${k}_m15.bin',np.complex128); B=np.load('computations/verification/lineE/referee/logs/T_${k}_eta2.0_m15.npy'); print('m15 $k maxdiff',np.max(abs(A-B)), np.max(abs(B)))"; done
for k in k1 full; do $P run_orb.py $k 17 2.0 ../logs/Torb_${k}_m17.bin 7; sha256sum ../logs/Torb_${k}_m17.bin; date; done
echo ALLDONE
