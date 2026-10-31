#!/bin/bash
cd /workspace/bgs-lineN/N7
for r in $@; do /workspace/bgs-derand/phase3/venv/bin/python code/a_dom16.py $r; done; echo WORKER_DONE
