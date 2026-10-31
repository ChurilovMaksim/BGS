#!/bin/sh
# sequential queue (N14); waits on a_enum by pid file-free check of its log footer
cd /workspace/bgs-lineN/N14
nice -n 8 ../.venv/bin/python code/d_decay2.py 16 > logs/d_decay2_G16.out 2>&1
while [ "$(tail -1 logs/a_enum.out | cut -d' ' -f1)" != "12" ]; do sleep 20; done
nice -n 6 ../.venv/bin/python code/a_cert.py 12 > logs/a_cert.out 2>&1
nice -n 8 ../.venv/bin/python code/b_cp2.py 0.28 1e-4 400 > logs/b_cp2_0.28.out 2>&1
