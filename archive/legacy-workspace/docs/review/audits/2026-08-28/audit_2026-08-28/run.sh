#!/usr/bin/env bash
# usage: run.sh <logname> <timeout_seconds> <command...>
LOG="C:/Users/churi/Desktop/BGS/_audit/logs/$1.log"
TMO="$2"
shift 2
cd "C:/Users/churi/Desktop/BGS/BGS_portable_20260827/BGS" || exit 99
start=$(date +%s%3N)
timeout "$TMO" "$@" > "$LOG" 2>&1
ec=$?
end=$(date +%s%3N)
ms=$((end-start))
echo "CMD: $*"
echo "EXIT_CODE=$ec"
echo "WALL_SECONDS=$((ms/1000)).$((ms%1000))"
echo "LOG=$LOG"
echo "----- OUTPUT BEGIN -----"
cat "$LOG"
echo "----- OUTPUT END -----"
