#!/usr/bin/env python3
"""Generate the data lines of formalization/Bgs/LineNSpanArith.lean (balanced floors n_k on a window).
The Lean module re-checks every floor by an exact integer sign test; this script only supplies the values."""
import pathlib, sys
HERE = pathlib.Path(__file__).parent
lines = []
print_ = print
def print(*a): lines.append(" ".join(map(str, a)))
src = (pathlib.Path(__file__).parent / 'span_census.py').read_text().split('def defect')[0]
ns = {'__file__': str(pathlib.Path(__file__).parent / 'span_census.py')}
exec(src.replace('J = int(sys.argv[1]) if len(sys.argv) > 1 else 16', 'J = 16').split('def classes')[0], ns)
for name, a, b in [('w116', 116, 0), ('w82s2', 0, 82), ('w118', 118, 0), ('w2', 2, 0), ('w3s2', 3, 1)]:
    w, zr, first, KL, KR, n = ns['word'](a, b)
    k0, k1 = KL - 4, KR + 4
    print(f"-- {name}: alpha = {a} + {b} sqrt2, K_L = {KL}, K_R = {KR}, span = {len(w)}, zr = {zr}")
    print(f"def {name}_k0 : Int := {k0}")
    print(f"def {name}_ns : List Int := {[n[k] if k in n else ns['n_k'](a, b, k) for k in range(k0, k1 + 1)]}")
    print(f"def {name}_word : List Int := {w}")

body = "\n".join(l for l in lines if not l.startswith("--"))
print_("\n".join(lines))
if "--write" in sys.argv:
    out = HERE.parents[3] / "formalization/Bgs/LineNSpanArith.lean"
    out.write_text((HERE / "lean_head.txt").read_text() + body + "\n" + (HERE / "lean_tail.txt").read_text())
    print_("wrote", out.relative_to(HERE.parents[3]))
