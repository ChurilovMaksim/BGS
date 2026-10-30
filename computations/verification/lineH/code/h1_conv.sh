#!/bin/bash
P=/workspace/bgs-derand/phase3/venv/bin/python
cd /workspace/bgs-lineH/code; export OMP_NUM_THREADS=2
L="2:4:1,-2:4:3,3:5:1,-3:5:4,-4:6:1,4:6:5,1:1:0,-1:1:0"
nice -n 10 $P h1_lift.py 13 3 0.8 24 5 8 $L
nice -n 10 $P h1_lift.py 13 3 0.7 30 7 8 $L
echo H1CONV_DONE
