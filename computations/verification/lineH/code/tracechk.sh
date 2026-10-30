#!/bin/bash
P=/workspace/bgs-derand/phase3/venv/bin/python
cd /workspace/bgs-lineH/code
export OMP_NUM_THREADS=2
nice -n 10 $P cert49_build.py V -1 2 0.85 16 3 150 40 0,2,4,6 ../data/tchkV 128 12
nice -n 10 $P cert49_build.py E -1 2 0.85 16 3 150 40 0,2,4,6 ../data/tchkE 128 12
nice -n 10 $P tracechk.py ../data/tchkV ../data/tchkE
rm -f ../data/tchk*_rad.npy
echo TRACECHK_DONE
