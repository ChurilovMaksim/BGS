#!/bin/bash
cd /workspace/bgs-lineN/N15/code
while ! grep -q '^DONE' ../logs/a_certpost3.out 2>/dev/null; do sleep 15; done
nice -n 15 ../../.venv/bin/python g_carry.py 4 6 > ../logs/g_carry_E4.out 2>&1
echo DONE >> ../logs/g_carry_E4.out
