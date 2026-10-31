#!/bin/bash
cd /workspace/audit/lineK/delta/lean
for f in K3Finite.lean Neg504.lean K3Gaps_447.lean K3Gaps_2627.lean K3Gaps_1647.lean K3Gaps_2147.lean K3Gaps_1547.lean; do
  s=$(date +%s); nice -n 10 lean $f > out_${f%.lean}.txt 2>&1; ex=$?; echo "$f exit=$ex sec=$(( $(date +%s)-s ))" >> summary.txt
done
echo DONE >> summary.txt
