#!/bin/bash
cd /workspace/bgs-lineN/N16/code
for E in 0 1 2 3; do nice -n 12 ../../.venv/bin/python g_scalar.py $E 6 > ../logs/g_scalar_E$E.out 2>&1; done
echo DONE >> ../logs/g_scalar_E3.out
