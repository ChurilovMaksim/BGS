#!/bin/bash
# usage: run_batch.sh batchfile ; lines: tag t0 ea eb kpar
cd /workspace/bgs-lineN/N9
while read tag t0 ea eb kp; do
  echo "KPAR=$kp OMP_NUM_THREADS=1 nice ../.venv/bin/python code/n9_cert.py $tag $t0 $ea $eb > logs/n9_cert_$tag.out 2>&1"
done < $1 | xargs -P 3 -I{} bash -c "{}"
echo BATCH_DONE $1
