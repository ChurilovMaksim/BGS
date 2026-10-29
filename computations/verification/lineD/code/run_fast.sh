#!/bin/bash
# R-collapse scans (deterministic seeds 21 / 41)
for K in 7 10 13 17 20 26 40; do ../venv/bin/python mc_fast.py flat 211 $K 2.0 1.0 60000 21 7; done
for K in 11 16 21 26 31 41; do ../venv/bin/python mc_fast.py flat 401 $K 2.0 1.0 100000 41 7; done
