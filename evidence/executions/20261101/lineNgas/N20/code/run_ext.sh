#!/bin/bash
# N20 queue: shells 13-14 running; then shell 15 (resumable, same output file)
cd /workspace/bgs-lineN/N20/code
while ! grep -q '^DONE' ../logs/a_cert_ext.out; do sleep 15; done
nice -n 10 ../../.venv/bin/python a_cert_ext.py 15 15 > ../logs/a_cert_ext15.out 2>&1
