#!/bin/bash
P=/workspace/bgs-derand/phase3/venv/bin/python
for mq in "15 41" "15 41 8 32 -1" "39 599 8 32 -1" "21 239 8 32 -1" "183 367" "123 2297" "111 6217" "183 7687" "123 9103" "87 13921" "57 14593" "129 19609" "237 34129" "111 37223" "123 54121"; do
  $P code/iso_survey.py $mq >> logs/iso_survey.jsonl 2>> logs/iso_survey.err
done
