#!/bin/sh
cd /workspace/bgs-lineN/N14
while pgrep -f "code/run_q.sh" >/dev/null; do sleep 20; done
nice -n 8 ../.venv/bin/python code/g_carry.py 2 8 > logs/g_carry_E2.out 2>&1
