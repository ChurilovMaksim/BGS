#!/usr/bin/env python3
"""Wave 46, task 7, step 4: compatibility analysis for slice mates.

For a slice mate pair (base, mate) with mate = base o sigma, and S =
Pi_289 ∩ Pi_1153^2 (slice common pi-set), check whether component
choices y_q in V_q(sigma) = {y in ker_q : y o sigma in ker_q} can make
the total intersection S ∩ (∩_q Pi_q) empty. A hit is an exact
compatibility counterexample: the y_q choices are printed.
Components: 25, 81, 121, 512 (49 is always full, contributes nothing).
"""
import sys
import itertools
import random
from collections import Counter

D4 = []
for b in range(4):
    D4.append(tuple((r + b) % 4 for r in range(4)))
    D4.append(tuple((-r + b) % 4 for r in range(4)))
D4 = sorted(set(D4))

def name(pi):
    if all(pi[r] == (r + pi[0]) % 4 for r in range(4)):
        return f"s{pi[0]}"
    b = pi[0] % 4
    if all(pi[r] == (-r + b) % 4 for r in range(4)):
        return f"f{b}"
    return str(pi)

def trace_seq(a, b, p):
    s = []
    ca, cb = a, b
    for _ in range(24):
        s.append((2 * ca) % p)
        ca, cb = (3 * ca + 4 * cb) % p, (2 * ca + 3 * cb) % p
    return tuple(s)

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

def prof(y):
    return tuple(tuple(sorted(y[i] for i in range(24) if i % 4 == r))
                  for r in range(4))

def pi_set(p, pp):
    return frozenset(name(pi) for pi in D4
                     if all(pp[r] == p[pi[r]] for r in range(4)))

def compose(y, sigma):
    return tuple(y[sigma[i]] for i in range(24))

def enum_sigma(base, mate, cap=50000):
    """All sigma with mate[i] == base[sigma[i]]; backtracking, capped."""
    cand = []
    for i in range(24):
        cand.append([j for j in range(24) if base[j] == mate[i]])
    order = sorted(range(24), key=lambda i: len(cand[i]))
    out = []
    used = [False] * 24
    cur = [0] * 24
    def bt(k):
        if len(out) >= cap:
            return
        if k == 24:
            out.append(tuple(cur))
            return
        i = order[k]
        for j in cand[i]:
            if not used[j]:
                used[j] = True
                cur[i] = j
                bt(k + 1)
                used[j] = False
    bt(0)
    return out, len(out) >= cap

def sample_sigma(base, mate, n=2000, seed=1):
    rng = random.Random(seed)
    valpos = {}
    for j, v in enumerate(base):
        valpos.setdefault(v, []).append(j)
    out = set()
    for _ in range(n):
        sigma = [0] * 24
        for v, js in valpos.items():
            idxs = [i for i in range(24) if mate[i] == v]
            perm = js[:]
            rng.shuffle(perm)
            for i, j in zip(idxs, perm):
                sigma[i] = j
        out.add(tuple(sigma))
    return list(out)

def main():
    mates = []
    base = None
    for line in open("wave46_PC_slicemates.log"):
        if line.startswith("MATE"):
            parts = line.split()
            C = tuple(int(x) for x in parts[1][3:-1].split(","))
            D = tuple(int(x) for x in parts[2][3:-1].split(","))
            mates.append((C, D))
    C0, D0 = (1, 2), (3, 5)
    t0 = trace_seq(*C0, 17)
    s0 = trace_seq(*D0, 1153)
    base_pairs = tuple(zip(t0, s0))
    K = {q: kernel_small(q) for q in [25, 81, 121, 512]}
    Kset = {q: set(K[q]) for q in K}
    print(f"mates: {len(mates)}")
    for (C, D) in mates:
        t = trace_seq(*C, 17)
        s = trace_seq(*D, 1153)
        mate_pairs = tuple(zip(t, s))
        assert sorted(mate_pairs) == sorted(base_pairs), "mate multiset mismatch"
        S = pi_set(prof(t0), prof(t)) & pi_set(prof(s0), prof(s))
        print(f"\nMATE C={C} D={D}: S={sorted(S)}")
        if not S:
            print("  !!! S EMPTY — contradicts wave 44 slice PC; check code")
            continue
        sigmas, capped = enum_sigma(base_pairs, mate_pairs)
        if capped:
            print(f"  Sigma_s capped at 50000, sampling instead")
            sigmas = sample_sigma(base_pairs, mate_pairs)
        print(f"  |Sigma_s| used: {len(sigmas)}")
        n_examined = 0
        for sigma in sigmas:
            # realizable Pi sets per component
            opts = {}
            for q in [25, 81, 121, 512]:
                V = [y for y in K[q] if compose(y, sigma) in Kset[q]]
                pis = {}
                for y in V:
                    ps = pi_set(prof(y), prof(compose(y, sigma)))
                    pis.setdefault(ps, y)
                opts[q] = (len(V), pis)
            # counterexample search: choose one E_q = S - Pi_q per component
            # with union covering S
            comp_opts = []
            for q in [25, 81, 121, 512]:
                Esets = {}
                for ps, y in opts[q][1].items():
                    Esets.setdefault(S - ps, y)
                comp_opts.append([(E, y) for E, y in Esets.items()])
            hit = None
            for combo in itertools.product(*comp_opts):
                union = set()
                for E, _ in combo:
                    union |= E
                if union >= set(S):
                    hit = combo
                    break
            n_examined += 1
            if hit:
                print(f"  COUNTEREXAMPLE sigma={sigma}")
                for q, (E, y) in zip([25, 81, 121, 512], hit):
                    print(f"    q={q}: y={y} avoids {sorted(E)}")
                return
            if n_examined <= 3:
                vs = {q: opts[q][0] for q in opts}
                print(f"  sigma ok (first 3 shown): |V|={vs}")
        print(f"  examined {n_examined} sigma(s), no counterexample")

main()
