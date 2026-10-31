#!/bin/bash
# rerun of OOM-killed (exit 137) chunks 1647..2645 with smaller chunks
cd /workspace/bgs-lineK/lean
while pgrep -f run_gaps.sh >/dev/null; do sleep 10; done
lo=1647
while [ $lo -le 2645 ]; do
  n=20; if [ $((lo+n-1)) -gt 2645 ]; then n=$((2645-lo+1)); fi
  f=K3Gaps_$lo.lean
  { cat K3Gaps.lean; echo "theorem gaps_$lo : okRange $lo $n = true := by decide +kernel"; echo "#print axioms gaps_$lo"; } > $f
  s=$(date +%s); lean $f > logs_gaps_$lo.txt 2>&1; ex=$?; echo "lo=$lo n=$n exit=$ex sec=$(( $(date +%s)-s ))" >> gaps_summary2.txt
  lo=$((lo+n))
done
echo DONE >> gaps_summary2.txt
