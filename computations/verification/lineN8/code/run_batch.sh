#!/bin/bash
# args per line: tag t0 ea eb kpar
cd /workspace/bgs-lineN/N8
while read tag t0 ea eb kp; do
  echo "KPAR=$kp OMP_NUM_THREADS=1 nice ../.venv/bin/python code/n8_cert.py $tag $t0 $ea $eb > logs/n8_cert_$tag.out 2>&1"
done < code/batch1.txt | xargs -P 3 -I{} bash -c "{}"
echo BATCH_DONE
