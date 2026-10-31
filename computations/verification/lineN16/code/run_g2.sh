#!/bin/bash
cd /workspace/bgs-lineN/N16/code
while ! grep -q '^DONE' ../logs/g_scalar_E3.out 2>/dev/null; do sleep 10; done
nice -n 12 ../../.venv/bin/python g_scalar.py 1 12 > ../logs/g_scalar_E1_n12.out 2>&1
echo DONE >> ../logs/g_scalar_E1_n12.out
