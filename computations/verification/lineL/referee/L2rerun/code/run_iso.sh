#!/bin/bash
P=/workspace/bgs-derand/phase3/venv/bin/python
for mq in "33 353" "39 313" "33 23" "39 79" "51 103" "39 599" "51 409" "57 457" "21 4663" "51 15607"; do
  $P code/iso_survey.py $mq >> logs/iso_survey.jsonl 2>> logs/iso_survey.err
done
