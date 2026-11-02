"""Wave 4 task 3 follow-up: dense X grid, deviation bound, brute-force cross-check.

Reuses the Orbits/CK code from wave4_task3_exact_constant.py (same pinned
sources) by exec'ing only its definition part; the window computation here
is new (dense grid), and the cross-check below averages Btup directly over
N without the count aggregation.
Numerical check only, not a proof.
"""
import math, json
import numpy as np

src = open("/home/hatch/workspace/bgs-breakthrough/numerics/wave4_task3_exact_constant.py").read()
defs = src.split("# ---- window counts")[0]
exec(defs, globals())

def window_counts(D, gp, X):
    counts = {}
    W = 0
    for N in range(X+1, 2*X+1):
        if math.gcd(N, D) == 1:
            W += 1
            nu = pow(N, -1, gp)
            counts[nu] = counts.get(nu, 0) + 1
    return counts, W

SELECT = {3: [10.0, 25.0], 4: [1.0, 10.0], 5: [2.0, 10.0], 6: [10.0, 200.0]}
X_DENSE = list(range(10000, 30001, 1000)) + list(range(40000, 100001, 10000))
out = {}
for m, etas in SELECT.items():
    O = Orbits(m)
    D, gp = O.D, O.gp
    pgp = len(O.units())
    print(f"\nm={m} D={D} gp={gp} phi(gp)={pgp}")
    for eta in etas:
        Z = O.Z_all(eta)
        Btup = {int(u): float(abs(Z[u])**2) for u in O.units()}
        nuAvg = float(np.mean(list(Btup.values())))
        S = pgp * nuAvg
        devsum = sum(abs(v - nuAvg) for v in Btup.values())
        vals = []
        for X in X_DENSE:
            counts, W = window_counts(D, gp, X)
            winAvg = sum(c*Btup[nu] for nu, c in counts.items())/W
            diff = winAvg - nuAvg
            maxdev = max(abs(c - W/pgp) for c in counts.values())
            if len(counts) < pgp:
                maxdev = max(maxdev, W/pgp)
            bound = X*maxdev/W*devsum
            vals.append((X, X*abs(diff), bound, maxdev))
        xs = [v[1] for v in vals]
        print(f"  eta={eta}: nuAvg={nuAvg:.4f} S={S:.2f} sum|Btup-nuAvg|={devsum:.2f} "
              f"dense X|diff|: min={min(xs):.2f} max={max(xs):.2f} mean={np.mean(xs):.2f} "
              f"last={xs[-1]:.2f} dev-bound(max)={max(v[2] for v in vals):.2f} "
              f"ratio max/bound={max(xs)/max(v[2] for v in vals):.3f}")
        print(f"    curve: " + ", ".join(f"{X}:{v:.1f}" for X, v, _, _ in vals))
        out[f"m{m}_eta{eta}"] = dict(nuAvg=nuAvg, S=S, devsum=devsum,
                                     curve=[(X, v, b) for X, v, b, _ in vals])

# brute-force cross-check (no count aggregation) at two points
print("\nBrute-force cross-check:")
for m, eta, X in [(5, 2.0, 20000), (6, 200.0, 50000), (3, 10.0, 10000)]:
    O = Orbits(m)
    Z = O.Z_all(eta)
    Btup = {int(u): float(abs(Z[u])**2) for u in O.units()}
    nuAvg = float(np.mean(list(Btup.values())))
    tot, W = 0.0, 0
    for N in range(X+1, 2*X+1):
        if math.gcd(N, O.D) == 1:
            tot += Btup[pow(N, -1, O.gp)]; W += 1
    winAvg = tot/W
    print(f"  m={m} eta={eta} X={X}: W={W} winAvg={winAvg:.6f} nuAvg={nuAvg:.6f} "
          f"X|diff|={X*abs(winAvg-nuAvg):.2f}")

json.dump(out, open("/home/hatch/workspace/bgs-breakthrough/numerics/wave4_task3_dense.json", "w"), indent=1)
print("saved wave4_task3_dense.json; DONE")
