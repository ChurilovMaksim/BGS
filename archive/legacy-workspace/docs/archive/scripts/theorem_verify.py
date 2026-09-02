"""RUN 11 / verify theorem prediction: actual relative error <= k^6/(2p^4)."""
import json, math, os, sys
from sympy import primitive_root

ART = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "artifacts")
rng = None  # not needed

def n_order(a, p):
    x, o = a, 1
    while x != 1:
        x = x * a % p; o += 1
        if o > p: raise ValueError("inf")
    return o

def count_sol(p, alpha, k):
    H, x = [], 1
    for _ in range(k): H.append(x); x = x * alpha % p
    inv = {h: pow(h, p-2, p) for h in H}
    L = {}
    for h1 in H:
        s = h1 % p; t = inv[h1]
        for h3 in H:
            kk = ((s+h3) % p, (t+inv[h3]) % p)
            L[kk] = L.get(kk, 0) + 1
    tot = 0
    for h2 in H:
        s = h2 % p; t = inv[h2]
        for h4 in H:
            kk = ((s+h4) % p, (t+inv[h4]) % p)
            if kk in L: tot += L[kk]
    return tot

def pairing_mass(p, k):
    """T17: 2k^2-k or 3k^2-3k depending on -1 in H."""
    # For single-orbit A=B=(1,...): check if -1 in H
    H, x = [], 1
    for _ in range(k): H.append(x); x = x*alpha%p
    has_neg1 = (p-1) in H
    return (3*k*k-3*k) if has_neg1 else (2*k*k-k)

# need alpha globally for pairing_mass
alpha = 0

def pairing_mass_fixed(p, k):
    global alpha
    H, x = [], 1
    for _ in range(k): H.append(x); x = x*alpha%p
    has_neg1 = any(x == p-1 for x in H)
    return (3*k*k-3*k) if has_neg1 else (2*k*k-k)

cases = []
for p in (101, 211, 4099):
    g = int(primitive_root(p))
    for k in (8, 16):
        if (p-1) % k != 0: continue
        alpha_val = pow(g, (p-1)//k, p)
        if n_order(alpha_val, p) != k: continue
        
        sol = count_sol(p, alpha_val, k)
        
        # compute pairing mass inline
        H_l, x = [], 1
        for _ in range(k): H_l.append(x); x = x*alpha_val%p
        has_m1 = (p-1) in H_l
        pm = (3*k*k-3*k) if has_m1 else (2*k*k-k)
        
        dev = abs(sol - pm)
        rel = dev / max(pm, 1)
        pred = k**6 / (2*p**4)
        
        status = "OK" if rel < max(pred, 0.01) else "CHECK"
        print(f"p={p} k={k}: sol={sol} pairings={pm} "
              f"dev/pm={rel:.5f} pred={pred:.5f} [{status}]")
        cases.append({"p": p, "k": k, "sol": sol, "pm": pm,
                     "rel_err": rel, "pred": pred})

from sympy import primitive_root as pr

# redo with proper primitive root
cases2 = []
for p in (101, 211, 4099):
    g = int(pr(p))
    for k in (8, 16):
        if (p-1) % k != 0: continue
        av = pow(g, (p-1)//k, p)
        if n_order(av, p) != k: continue
        H_l, x = [], 1
        for _ in range(k): H_l.append(x); x = x*av%p
        sol = count_sol(p, av, k)
        has_m1 = (p-1) in H_l
        pm = (3*k*k-3*k) if has_m1 else (2*k*k-k)
        rel = abs(sol-pm)/max(pm,1)
        pred = k**6/(2*p**4)
        cases2.append({"p":p,"k":k,"sol":sol,"pm":pm,"rel":round(rel,5),"pred":round(pred,5)})
        print(f"p={p} k={k}: |sol-pm|/pm={rel:.6f} pred_bound={pred:.6f}")

json.dump(cases2, open(os.path.join(ART, "theorem_verify.json"), "w"), indent=1)
print("saved artifacts/theorem_verify.json")
