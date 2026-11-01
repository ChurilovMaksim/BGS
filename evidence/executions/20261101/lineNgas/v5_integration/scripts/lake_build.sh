#!/bin/bash
T="$1"; N="$2"
export PATH=$HOME/.elan/bin:$PATH
cd /workspace/lineNgas/repo/formalization
L=/workspace/lineNgas/v5int/logs
memof() { local s=0 a=0; for p in $(ps -eo pid,pgid | awk -v g=$1 '$2==g{print $1}'); do
   a=$((a + $(awk '/RssAnon/{print $2}' /proc/$p/status 2>/dev/null || echo 0)))
   s=$((s + $(awk '/^Pss:/{print $2}' /proc/$p/smaps_rollup 2>/dev/null || echo 0))); done; echo "$a $s"; }
{ date; echo "\$ lake build $T"; setsid nice -n 10 lake build $T > $L/lake_build_$N.body 2>&1 & P=$!
  sleep 0.5; PG=$P
  while kill -0 $P 2>/dev/null; do read a s < <(memof $PG); echo "$(date +%T) anon_kB=$a pss_kB=$s" >> $L/mem_$N.log
    if [ "$a" -gt 3800000 ]; then echo "MEMKILL anon $a" >> $L/mem_$N.log; kill -TERM -$PG; fi; sleep 1; done
  wait $P; echo "EXIT $?"; date; } > $L/lake_build_$N.head 2>&1
echo DONE >> $L/mem_$N.log
