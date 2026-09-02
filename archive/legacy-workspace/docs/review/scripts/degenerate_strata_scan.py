"""DEGENERATE STRATA SCAN (audit follow-up F5).

Question (Cor-domination gap): do NON-Wick degenerate label patterns
have BOUNDED reduced resonance count N3 as p -> infinity at fixed
rho = k^2/p ?  Domination needs N3 = O(k^2/p + 1) = O(1) per class.

Classes: GEN baseline; WICK (absorbed, Theta(k)); SLOT13/CROSS12/
TWOCROSS/CHAIN = single/double proportionality families, non-Wick.
"""
import os as _os
_BGS_ROOT = _os.path.dirname(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))
import sys, json, math
import numpy as np


def prime_factors(n):
    d, fs = 2, []
    while d * d <= n:
        while n % d == 0:
            fs.append(d); n //= d
        d += 1
    if n > 1:
        fs.append(n)
    return sorted(set(fs))


def subgroup(p, k):
    fs = prime_factors(p - 1)
    g = 2
    while any(pow(g, (p - 1) // q, p) == 1 for q in fs):
        g += 1
    a = pow(g, (p - 1) // k, p)
    H, x = [], 1
    for _ in range(k):
        H.append(x); x = x * a % p
    assert x == 1
    return H


def n3_vec(p, H, a, b):
    Hn = np.array(H, dtype=np.int64)
    invH = np.array([pow(int(h), p - 2, p) for h in Hn], dtype=np.int64)
    Hs = np.sort(Hn)
    ia4 = pow(int(a[3]), p - 2, p)
    U2, U3 = np.meshgrid(Hs, Hs, indexing="ij")
    num = (int(a[0]) - int(a[1]) * U2 + int(a[2]) * U3) % p
    U4 = num * ia4 % p
    loc = np.clip(np.searchsorted(Hs, U4), 0, len(Hs) - 1)
    member = Hs[loc] == U4
    iu4 = np.where(member, invH[loc], 1)
    iu2 = invH[np.searchsorted(Hs, U2)]
    iu3 = invH[np.searchsorted(Hs, U3)]
    lhs = (int(b[0]) - int(b[1]) * iu2 + int(b[2]) * iu3) % p
    rhs = int(b[3]) * iu4 % p
    return int(np.count_nonzero(member & (lhs == rhs)))


def is_wick(a, b):
    idx = [(0, 1, 2, 3), (0, 2, 1, 3), (0, 3, 1, 2)]
    return any(a[i] == a[j] and b[i] == b[j] and
               a[m] == a[n] and b[m] == b[n] for i, j, m, n in idx)


def make_pattern(cls, rng, p):
    a = [int(rng.integers(1, p)) for _ in range(4)]
    b = [int(rng.integers(1, p)) for _ in range(4)]

    def L():
        return int(rng.integers(2, p))

    def bump(kind):
        if kind == "SLOT13":
            a[2] = a[0] * L() % p; b[2] = b[0] * L() % p
        elif kind == "CROSS12":
            a[1] = a[0] * L() % p; b[1] = b[0] * L() % p
        elif kind == "TWOCROSS":
            a[1] = a[0] * L() % p; b[1] = b[0] * L() % p
            a[3] = a[2] * L() % p; b[3] = b[2] * L() % p
        elif kind == "CHAIN":
            a[1] = a[0] * L() % p; b[1] = b[0] * L() % p
            a[2] = a[1] * L() % p; b[2] = b[1] * L() % p

    if cls == "WICK":
        a[1] = a[0]; b[1] = b[0]
        a[3] = a[2]; b[3] = b[2]
        return a, b
    if cls == "WICK3Q":
        # three of four Wick equalities hold, one broken: sharpest edge
        a[1] = a[0]; b[1] = b[0]
        a[3] = a[2]
        while b[3] == b[2]:
            b[3] = int(rng.integers(1, p))
        while is_wick(a, b):
            b[3] = int(rng.integers(1, p))
        return a, b
    if cls != "GEN":
        bump(cls)
        while is_wick(a, b):          # keep the class genuinely non-Wick
            a = [int(rng.integers(1, p)) for _ in range(4)]
            b = [int(rng.integers(1, p)) for _ in range(4)]
            bump(cls)
    return a, b


CLASSES = ["GEN", "WICK", "WICK3Q", "SLOT13", "CROSS12", "TWOCROSS", "CHAIN"]


def nearest_divisor(p, target):
    cands = [d for d in range(3, p) if (p - 1) % d == 0]
    return min(cands, key=lambda d: abs(d - target)) if cands else None


def main():
    rho = float(sys.argv[1]) if len(sys.argv) > 1 else 1.0
    TRIALS = int(sys.argv[2]) if len(sys.argv) > 2 else 250
    rng = np.random.default_rng(20260826)
    out = {"rho": rho, "trials": TRIALS, "configs": []}
    print(f"=== DEGENERATE STRATA SCAN rho={rho} trials={TRIALS} ===",
          flush=True)
    for p in [1009, 2003, 4001, 8009]:
        target = int(round(math.sqrt(rho * p)))
        k = nearest_divisor(p, target)
        if k is None or k < 6:
            continue
        H = subgroup(p, k)
        row = {"p": p, "k": k, "rho_actual": round(k * k / p, 3)}
        for cls in CLASSES:
            mx = mean_acc = nz = 0
            for _ in range(TRIALS):
                a, b = make_pattern(cls, rng, p)
                n = n3_vec(p, H, a, b)
                mx = max(mx, n)
                mean_acc += n
                nz += (n > 0)
            row[cls] = {"max": mx, "mean": round(mean_acc / TRIALS, 4),
                        "frac_nz": round(nz / TRIALS, 4)}
        out["configs"].append(row)
        print(json.dumps(row), flush=True)
        # growth verdict printed later by analysis
    with open(_BGS_ROOT + r"\artifacts"
              r"\audit_degenerate_strata.json", "w") as f:
        json.dump(out, f, indent=1)
    print("saved artifacts/audit_degenerate_strata.json")


if __name__ == "__main__":
    main()
