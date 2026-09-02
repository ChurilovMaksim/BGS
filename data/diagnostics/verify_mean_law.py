"""
RUN 46: VERIFY EXACT ensemble-mean formula
    <N3> = k^3 * (p^2-3p+3)^2 / (p-1)^6
against direct Monte-Carlo over random labels.
"""
import sys, os, json
import numpy as np
from sympy import primitive_root

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from reduced_resonance import n3_count

ART = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir,
                   "artifacts")


def exact_mean(p, k):
    return k**3 * (p*p - 3*p + 3)**2 / (p-1)**6


def main():
    rng = np.random.default_rng(20260825)
    print("=== RUN 46 exact-mean verification ===")
    rows = []
    for (p, k, trials) in [(101, 10, 40000), (101, 20, 20000),
                           (211, 15, 20000), (211, 21, 15000),
                           (401, 20, 15000)]:
        g = int(primitive_root(p))
        alpha = pow(g, (p-1)//k, p)
        H = set(); x = 1
        for _ in range(k):
            H.add(x); x = x*alpha % p
        tot = 0
        for t in range(trials):
            a = [int(rng.integers(1, p)) for _ in range(4)]
            b = [int(rng.integers(1, p)) for _ in range(4)]
            tot += n3_count(p, H, a, b)
        mc = tot/trials
        ex = exact_mean(p, k)
        # Poisson-scale standard error of the count sum (audit note:
        # paper A.2 wording aligned to this convention 2026-08-26)
        sigma = (ex/trials)**0.5 if ex > 0 else 0
        z = (mc-ex)/sigma if sigma > 0 else 0
        ok = abs(z) < 3
        print(f"p={p} k={k}: MC={mc:.5f} exact={ex:.5f} "
              f"z={z:+.2f} {'OK' if ok else 'DEVIATION'}")
        rows.append(dict(p=p, k=k, trials=trials, mc=mc, exact=ex,
                         z=z))
    json.dump(rows, open(os.path.join(ART, "run46_exact_mean.json"),
                         "w"), indent=1)


if __name__ == "__main__":
    main()
