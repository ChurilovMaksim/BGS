#!/bin/sh
# False-variant controls: each variant is appended alone to a copy of the certificate and must be REJECTED by decide.
set -u
SRC=${SRC:-formalization/Bgs/RevivalClosureRational.lean}  # run from the repository root
LEAN=${LEAN:-$HOME/.elan/bin/lean}
fail=0
run() { name=$1; body=$2
  f=$(mktemp /tmp/ctrlXXXX.lean); sed '$d' "$SRC" > "$f"; printf '%s\nend Bgs.RevivalClosureRational\n' "$body" >> "$f"
  if "$LEAN" "$f" >/tmp/ctrl.out 2>&1; then echo "CONTROL $name: ACCEPTED (BAD)"; fail=1
  else grep -q "proved that the proposition" /tmp/ctrl.out && echo "CONTROL $name: rejected by decide (good)" || { echo "CONTROL $name: other error (BAD)"; cat /tmp/ctrl.out; fail=1; }; fi; rm -f "$f"; }
run wrong_order_41   'theorem c1 : ordIs 41 10 = true := by decide'
run wrong_order_1189 'theorem c2 : ordIs 1189 5 = true := by decide'
run wrong_kappa_41   'theorem c3 : kappaIs 41 5 5 = true := by decide'
run wrong_half_101   'theorem c4 : isMinusOne 101 (powMod 101 50) = true := by decide'
run wrong_count_7    'theorem c5 : (Z7.foldl (fun acc a0 => Z7.foldl (fun acc a1 => Z7.foldl (fun (acc : Nat) a2 => if closes 7 a0 a1 a2 then acc + 1 else acc) acc) acc) 0) = 8 := by decide'
run wrong_phase_sign 'theorem c6 : Z7.all (fun a0 => Z7.all (fun a1 => Z7.all (fun a2 => phaseOk 7 3 a0 a1 a2))) = true := by decide'
run window_violated  'theorem c7 : (coeffRange 7).all (fun c0 => (coeffRange 7).all (fun c1 => (coeffRange 7).all (fun c2 => implies 41 (red3 c0 c1 c2)))) = true := by decide'
[ $fail -eq 0 ] && echo "ALL CONTROLS REJECTED: PASS" || echo "CONTROLS: FAIL"
