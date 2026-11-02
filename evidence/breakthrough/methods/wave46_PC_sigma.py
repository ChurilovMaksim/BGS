#!/usr/bin/env python3
"""Wave 46, task 7, step 6: sigma realizability across components.

Take non-dihedral pairs at 81 and 512, sample permutations sigma with
y' = y o sigma, and compute V_q(sigma) = {y in ker_q : y o sigma in
ker_q} for every component q (brute force for small q; exact 2-dim
linear algebra over F_1153 for the slice s-component). A sigma with
nontrivial V at two restrictive components is a candidate global
permutation for a full pair; if none exists, that IS the compatibility
mechanism (up to the sampled sigmas).
"""
import random

D24 = []
for k in range(24):
    D24.append(tuple((i + k) % 24 for i in range(24)))
    D24.append(tuple((-i + k) % 24 for i in range(24)))

def kernel_small(q):
    out = []
    for y0 in range(q):
        for y1 in range(q):
            y = [0] * 26
            y[0], y[1] = y0, y1
            for n in range(24):
                y[n + 2] = (6 * y[n + 1] - y[n]) % q
            if y[24] == y0 and y[25] == y1:
                out.append(tuple(y[:24]))
    return out

def compose(y, sigma):
    return tuple(y[sigma[i]] for i in range(24))

def is_dihedral_pair(y, yp):
    return any(compose(y, d) == yp for d in D24)

def sample_sigmas(y, yp, n, seed):
    rng = random.Random(seed)
    valpos_y = {}
    for j, v in enumerate(y):
        valpos_y.setdefault(v, []).append(j)
    idxs_by_val = {}
    for i, v in enumerate(yp):
        idxs_by_val.setdefault(v, []).append(i)
    out = set()
    for _ in range(n):
        sigma = [0] * 24
        for v, idxs in idxs_by_val.items():
            js = valpos_y[v][:]
            rng.shuffle(js)
            for i, j in zip(idxs, js):
                sigma[i] = j
        out.add(tuple(sigma))
    return list(out)

def trace_seq(a, b, p):
    s = []
    ca, cb = a, b
    for _ in range(24):
        s.append((2 * ca) % p)
        ca, cb = (3 * ca + 4 * cb) % p, (2 * ca + 3 * cb) % p
    return tuple(s)

def V_1153_dim(sigma):
    """Dim of {s in T_1153 : s o sigma in T_1153}, T = trace space mod 1153.
    Cyclic recurrence equations, 2 unknowns over F_1153."""
    p = 1153
    s1 = trace_seq(1, 0, p)
    s2 = trace_seq(0, 1, p)
    eqs = []
    for n in range(24):
        ca = (s1[sigma[(n + 2) % 24]] - 6 * s1[sigma[(n + 1) % 24]]
              + s1[sigma[n]]) % p
        cb = (s2[sigma[(n + 2) % 24]] - 6 * s2[sigma[(n + 1) % 24]]
              + s2[sigma[n]]) % p
        if ca or cb:
            eqs.append((ca, cb))
    if not eqs:
        return 2
    ca1, cb1 = eqs[0]
    for (ca, cb) in eqs[1:]:
        if (ca * cb1 - cb * ca1) % p != 0:
            return 0
    return 1

def main():
    K = {q: kernel_small(q) for q in [25, 49, 81, 121, 289, 512]}
    Kset = {q: set(K[q]) for q in K}
    for q0 in [81, 512]:
        by_mult = {}
        for y in K[q0]:
            by_mult.setdefault(tuple(sorted(y)), []).append(y)
        pairs = []
        for ys in by_mult.values():
            for ii in range(len(ys)):
                for jj in range(ii + 1, len(ys)):
                    if not is_dihedral_pair(ys[ii], ys[jj]):
                        pairs.append((ys[ii], ys[jj]))
                    if len(pairs) >= 3:
                        break
                if len(pairs) >= 3:
                    break
            if len(pairs) >= 3:
                break
        print(f"=== non-dihedral pairs at q={q0}: using {len(pairs)} ===")
        for pi_, (y, yp) in enumerate(pairs):
            sigmas = sample_sigmas(y, yp, 300, seed=100 + pi_)
            print(f" pair {pi_}: sampled {len(sigmas)} distinct sigmas")
            best = []
            for sigma in sigmas:
                Vs = {}
                for q in [25, 49, 81, 121, 289, 512]:
                    Vs[q] = sum(1 for v in K[q]
                                if compose(v, sigma) in Kset[q])
                d1153 = V_1153_dim(sigma)
                restr = [q for q in [81, 121, 289, 512]
                         if Vs[q] > 1] + ([1153] if d1153 > 0 else [])
                if len(restr) >= 2:
                    best.append((sigma, Vs, d1153, restr))
            print(f"  sigmas with V nontrivial at >=2 restrictive comps: "
                  f"{len(best)}")
            for (sigma, Vs, d1153, restr) in best[:5]:
                print(f"    sigma={sigma} |V|={Vs} dim1153={d1153} restr={restr}")

main()
