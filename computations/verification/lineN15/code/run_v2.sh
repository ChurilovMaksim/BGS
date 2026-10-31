#!/bin/bash
cd /workspace/bgs-lineN/N15/code
while ! grep -q '^max' ../logs/nh_table_rig_2048.out; do sleep 10; done
nice -n 10 ../../.venv/bin/python b_cp3.py > ../logs/b_cp3_0.28.out 2>&1
nice -n 10 ../../.venv/bin/python c3_mid.py > ../logs/c3_mid.out 2>&1
echo DONE >> ../logs/c3_mid.out
