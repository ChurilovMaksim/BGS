#!/bin/bash
P=/workspace/bgs-derand/phase3/venv/bin/python
for mq in "15 41" "33 23" "39 79" "51 103" "15 41 -1" "21 239"; do $P code/full_level.py $mq >> logs/full_level.jsonl 2>> logs/full_level.err; done
