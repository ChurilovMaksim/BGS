"""Post-rebrand smoke test for the workspace's canonical src/ tree.

Checks that the load-bearing modules import from their post-R82 topic
subfolders and that the exact-mean-law machinery still computes.  Run from
anywhere:  py -3 review/scripts/smoke_test_src.py
"""
import os as _os
_BGS_ROOT = _os.path.dirname(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))
import sys
for _sub in ("core", "theorems", "diagnostics", "kloosterman", "shape_automaton", "large_m", "utils"):
    sys.path.insert(0, _os.path.join(_BGS_ROOT, "src", _sub))

ok = []
def t(name, fn):
    try:
        fn(); ok.append(name); print(f"  OK  {name}")
    except Exception as e:
        print(f"  FAIL {name}: {e}")

t("core: catmap_core", lambda: __import__("catmap_core"))
t("theorems: master_formula_strong (find_orbit_H)",
  lambda: __import__("master_formula_strong").find_orbit_H)
t("core: reduced_resonance.n3_count",
  lambda: __import__("reduced_resonance").n3_count)
t("diagnostics: audit_tail_bound import",
  lambda: __import__("audit_tail_bound"))
t("diagnostics: diag_conditional_prob import",
  lambda: __import__("diag_conditional_prob"))

# functional micro-check of the exact-mean law machinery
from reduced_resonance import n3_count
from sympy import primitive_root
p, k = 101, 10
g = int(primitive_root(p))
a = pow(g, (p-1)//k, p)
H = set(); x = 1
for _ in range(k):
    H.add(x); x = x*a % p
rng = __import__("numpy").random.default_rng(0)
tot = 0
for _ in range(300):
    A = [int(rng.integers(1, p)) for _ in range(4)]
    B = [int(rng.integers(1, p)) for _ in range(4)]
    tot += n3_count(p, H, A, B)
mean = tot/300
exact = k**3*(p*p-3*p+3)**2/(p-1)**6
functional_ok = abs(mean-exact) < 0.15
print(f"  mean={mean:.4f} vs exact={exact:.4f} "
      f"({'OK' if functional_ok else 'CHECK'})")

print(f"\n{len(ok)}/5 module smoke tests passed"
      + ("" if functional_ok else "; functional micro-check FLAGGED"))
sys.exit(0 if len(ok) == 5 and functional_ok else 1)
