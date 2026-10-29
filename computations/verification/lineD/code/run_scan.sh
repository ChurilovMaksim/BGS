#!/bin/bash
# K-scan Monte Carlo (deterministic seeds)
P=$1; ETA=$2; S=$3; shift 3
for K in "$@"; do ../venv/bin/python mc_band.py flat $P $K $ETA 1.0 $S 11 8; done
