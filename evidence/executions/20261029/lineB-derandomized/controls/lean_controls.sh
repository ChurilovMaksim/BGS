#!/bin/bash
# Each control is a false variant of a Line B Lean statement; every one must be REJECTED.
# Run from the Lean project root (where Bgs/LineB*.lean are built): bash lean_controls.sh <dir-with-c*.lean>
D=${1:-.}; ok=0; n=0
for f in $D/c*.lean; do n=$((n+1)); if timeout 600 lake env lean $f >/dev/null 2>&1; then echo "$(basename $f): ACCEPTED (BAD)"; else echo "$(basename $f): rejected"; ok=$((ok+1)); fi; done
echo "$ok/$n false controls rejected"
