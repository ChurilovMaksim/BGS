#!/bin/bash
cd /workspace/bgs-lineN/N16/code
P=../../.venv/bin/python
nice -n 10 $P conv_vec.py replay > ../logs/conv_vec_replay.out 2>&1
nice -n 10 $P ../../N14/code/f_post2.py ../logs/conv_vec_replay.jsonl ../logs/f_post_true.json > ../logs/f_post_true.out 2>&1
nice -n 10 $P conv_vec.py classes 10 > ../logs/conv_vec_classes.out 2>&1
echo DONE >> ../logs/conv_vec_classes.out
