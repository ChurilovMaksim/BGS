#!/bin/bash
cd /workspace/bgs-lineN/N15/code
while ! grep -q '^DONE' ../logs/c3_mid.out; do sleep 10; done
nice -n 10 ../../.venv/bin/python ../../N14/code/f_post2.py ../logs/c3_mid.jsonl ../logs/f_post3.json > ../logs/f_post3.out 2>&1
nice -n 10 ../../.venv/bin/python a_cert3.py 12 > ../logs/a_cert3.out 2>&1
nice -n 10 ../../.venv/bin/python a_certpost3.py > ../logs/a_certpost3.out 2>&1
echo DONE >> ../logs/a_certpost3.out
