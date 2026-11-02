"""Wave 42, task 5: F1-F4 at m=252. Blind-component verification.

For each candidate q0 | D_84 (odd part): enumerate kernel sequences of
M^252 - I mod q0 (vectorized seed solve), then check, for all nonzero o:
  (i)   seed count == q0,
  (ii)  84-periodicity (v3(period o) <= 1) -- top-digit-law criterion,
  (iii) direct collision across the 729 free pair (b,bp) with locked a,
  (iv)  split-ness: every fiber (sorted multiset) is a single dihedral orbit.
Saves 5 random nonzero sequences per component to wave42_samples.npz.
Usage: python3 wave42_blind_m252.py q1 q2 ...   (default: the 8 feasible q0)
"""
import math, sys, json, pickle
import numpy as np
from collections import defaultdict

M = 252
d = pickle.load(open("wave42_ab.pkl", "rb"))
A_ARR, B_ARR, BP_ARR = (np.array(d["a"], dtype=np.int64),
                        np.array(d["b"], dtype=np.int64),
                        np.array(d["bp"], dtype=np.int64))

def mat_pow(Mm, e, q):
    def mul(X, Y):
        return [(X[0]*Y[0]+X[1]*Y[2]) % q, (X[0]*Y[1]+X[1]*Y[3]) % q,
                (X[2]*Y[0]+X[3]*Y[2]) % q, (X[2]*Y[1]+X[3]*Y[3]) % q]
    R = [1, 0, 0, 1]; B = Mm[:]
    while e:
        if e & 1: R = mul(R, B)
        B = mul(B, B); e >>= 1
    return R

def gamma_perms(m):
    perms, seen = [], set()
    for k in range(m):
        for p in (tuple((j + k) % m for j in range(m)),
                  tuple((k - j) % m for j in range(m))):
            if p not in seen:
                seen.add(p); perms.append(p)
    return np.array(perms, dtype=np.int64)

PERMS = gamma_perms(M)

def kernel_seeds(q, chunk=20000):
    """Return (y0s, y1s) arrays of all kernel seeds mod q (chunked)."""
    Mm = mat_pow([6, q - 1, 1, 0], M, q)
    a = (Mm[0] - 1) % q; b = Mm[1] % q; c = Mm[2] % q; dd = (Mm[3] - 1) % q
    g = math.gcd(a, q)
    gb = math.gcd(b, g); step0 = g // gb
    a1, q1 = a // g, q // g
    inv_a1 = pow(a1, -1, q1) if q1 > 1 else 0
    step = q // g
    y0_all, y1_all = [], []
    for st in range(0, q, chunk):
        y0 = np.arange(st, min(st + chunk, q), step0, dtype=np.int64)
        if len(y0) == 0:
            continue
        rhs = ((-(b * y0) // g) % q1) if q1 > 1 else np.zeros(len(y0), dtype=np.int64)
        y1_0 = (inv_a1 * rhs) % q1 if q1 > 1 else np.zeros(len(y0), dtype=np.int64)
        # candidates y1_0 + k*step, k = 0..g-1 ; keep (c*y1 + d*y0) % q == 0
        # (chunk x g) array; g <= 337 for the feasible components
        cand = y1_0[:, None] + step * np.arange(g, dtype=np.int64)[None, :]
        mask = (c * cand + dd * y0[:, None]) % q == 0
        ii, jj = np.nonzero(mask)
        y0_all.append(y0[ii]); y1_all.append(cand[ii, jj])
    return np.concatenate(y0_all), np.concatenate(y1_all)

def build_seqs(y0s, y1s, q):
    Y = np.empty((len(y0s), M), dtype=np.int64)
    Y[:, 0] = y0s; Y[:, 1] = y1s
    for i in range(2, M):
        Y[:, i] = (6 * Y[:, i - 1] - Y[:, i - 2]) % q
    return Y

def check_component(q, rng):
    y0s, y1s = kernel_seeds(q)
    nseeds = len(y0s)
    Y = build_seqs(y0s, y1s, q)
    nonzero = np.any(Y != 0, axis=1)
    Yn = Y[nonzero]
    # (ii) 84-periodicity for all nonzero rows
    per84 = np.all(Yn[:, :168] == Yn[:, 84:], axis=1)
    n_per_fail = int(np.sum(~per84))
    # (iii) direct collision for all nonzero rows
    n_col_fail = 0
    for o in Yn:
        key = A_ARR * q + o
        o1 = np.lexsort((B_ARR, key)); o2 = np.lexsort((BP_ARR, key))
        if not (np.array_equal(key[o1], key[o2]) and
                np.array_equal(B_ARR[o1], BP_ARR[o2])):
            n_col_fail += 1
    # (iv) split-ness: fibers vs dihedral orbit sizes
    srt = np.sort(Y, axis=1)
    _, fib_ids = np.unique(srt, axis=0, return_inverse=True)
    fib_ids = np.asarray(fib_ids).reshape(-1)
    n_fib = int(fib_ids.max()) + 1
    order = np.argsort(fib_ids, kind="stable")
    fs, cnts = np.unique(fib_ids, return_counts=True)
    multi = fs[cnts >= 2]
    n_split = 0
    for f in multi:
        rows = Y[fib_ids == f]
        orb = set(map(tuple, rows[0][PERMS].tolist()))
        if len(orb) != len(rows):
            n_split += 1
    # samples
    idx = rng.choice(len(Yn), size=min(5, len(Yn)), replace=False)
    samples = Yn[idx]
    res = {"q": q, "seeds": int(nseeds), "nonzero": int(len(Yn)),
           "per84_fail": n_per_fail, "col_fail": n_col_fail,
           "fibers": n_fib, "multi_fibers": int(len(multi)),
           "split_fibers": int(n_split)}
    print(json.dumps(res), flush=True)
    return res, samples

def main():
    qs = [int(x) for x in sys.argv[1:]] or [25, 121, 6889, 12769, 28561, 57121, 63001, 113569]
    rng = np.random.default_rng(20261102)
    out, samples = {}, {}
    for q in qs:
        res, smp = check_component(q, rng)
        out[q] = res; samples[q] = smp
    np.savez("wave42_samples.npz", **{f"q{q}": samples[q] for q in qs})
    with open("wave42_blind_results.json", "w") as f:
        json.dump(out, f, indent=1)
    print("DONE", flush=True)

if __name__ == "__main__":
    main()
