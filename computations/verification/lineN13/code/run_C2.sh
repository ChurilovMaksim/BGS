#!/bin/bash
while pgrep -f "code/run_C.sh" >/dev/null; do sleep 30; done
cd /workspace/bgs-lineN/N13 && OMP_NUM_THREADS=1 nice -n 15 ../.venv/bin/python code/c_replay.py >> logs/c_replay.out 2>&1
