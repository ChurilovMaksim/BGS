#!/bin/bash
# Each control is a false variant of a Line F or Line G Lean statement; every one must be REJECTED,
# and for the expected reason: Lean must report the proposition false (`decide`) or leave
# an unsolved `False` goal (`norm_num`). A control that fails for any other reason (missing
# import, unknown identifier, timeout) counts as a FAILURE of this script, not a rejection.
# Run from the Lean project root (where Bgs/LineF.lean, Bgs/LineG.lean are built):
#   bash lean_controls.sh <dir-with-c*.lean>
# stderr/stdout of every `lake env lean` call is kept in the output.
D=${1:-.}; ok=0; n=0
for f in "$D"/c*.lean; do
  n=$((n+1))
  out=$(timeout 600 nice -n 10 lake env lean "$f" 2>&1); rc=$?
  echo "--- $(basename "$f") (lean exit $rc)"
  printf '%s\n' "$out"
  if [ "$rc" -ne 0 ] && printf '%s\n' "$out" | grep -qE "proved that the proposition|unsolved goals"; then
    echo "$(basename "$f"): rejected (expected reason)"; ok=$((ok+1))
  else
    echo "$(basename "$f"): NOT REJECTED FOR THE EXPECTED REASON (BAD)"
  fi
done
echo "$ok/$n false controls rejected for the expected reason"
[ "$ok" -eq "$n" ]
