"""Check the exact phase law against the Line B integer phase for random n (float compare of mod-1 phases; exact parts exact)."""
import random, sys
from lawlib import *
random.seed(1)
bad = 0
for a in (1, 7, 17, 23):
    for m in range(5, 26, 2):
        h = mdata(m)['h']
        for s in (+1, -1):
            if math.gcd(a, 2*h) != 1: print(f'a={a} m={m}: a not coprime to h (skip, no residue)'); break
            try: P = law_params(m, a, s)
            except AssertionError as e: print(f'a={a} m={m} s={s}: {e}'); continue
            for r in sqrt2_mod(a*a) if a > 1 else [None]:
                P = law_params(m, a, s, root=r) if a > 1 else P
                worst = 0
                for t in range(25):
                    n = [random.randint(-9, 9) for _ in range(m)]
                    p1 = float(phase_exact(m, P['nu'], n)); p2 = law_phase(m, a, s, n, P)
                    dlt = abs((p1 - p2 + 0.5) % 1 - 0.5); worst = max(worst, dlt)
                ok = worst < 1e-9; bad += (not ok)
                print(f'a={a:2d} m={m:2d} s={s:+d} root={r} nu={P["nu"]} kappa={P["kappa"]} gamma={P.get("gamma")} max|dphase|={worst:.1e} {"OK" if ok else "FAIL"}', flush=True)
print('FAILURES', bad)
