#!/bin/bash
# two streams; N=120 per class
cd /workspace/bgs-lineN/N9b
export OMP_NUM_THREADS=1
( for p in 13 19 29 41 53 61; do /workspace/bgs-lineN/.venv/bin/python code/g_unitmix.py $p 120; done ) > logs/g_unitmix_s1.out 2>&1 &
( for p in 17 23 31 37 43 47 59; do /workspace/bgs-lineN/.venv/bin/python code/g_unitmix.py $p 120; done ) > logs/g_unitmix_s2.out 2>&1 &
wait
