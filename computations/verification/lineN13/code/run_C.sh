#!/bin/bash
# sequential: wait for b_arb.py to finish, then run the replay (resumable) at low priority
while pgrep -f "code/b_arb.py" >/dev/null; do sleep 20; done
cd /workspace/bgs-lineN/N13 && OMP_NUM_THREADS=1 nice -n 15 ../.venv/bin/python code/c_replay.py >> logs/c_replay.out 2>&1
