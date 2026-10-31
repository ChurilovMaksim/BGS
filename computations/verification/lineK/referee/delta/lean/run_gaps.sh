#!/bin/bash
# kernel-decide chunks for Lemma K3(a) on 447..2645 (sieve covers b' > 2644.3)
cd /workspace/bgs-lineK/lean
lo=447
while [ $lo -le 2645 ]; do
  n=100; if [ $((lo+n-1)) -gt 2645 ]; then n=$((2645-lo+1)); fi
  f=K3Gaps_$lo.lean
  { cat K3Gaps.lean; echo "theorem gaps_$lo : okRange $lo $n = true := by decide +kernel"; echo "#print axioms gaps_$lo"; } > $f
  s=$(date +%s); lean $f > logs_gaps_$lo.txt 2>&1; ex=$?; echo "lo=$lo n=$n exit=$ex sec=$(( $(date +%s)-s ))" >> gaps_summary.txt
  lo=$((lo+n))
done
echo DONE >> gaps_summary.txt
