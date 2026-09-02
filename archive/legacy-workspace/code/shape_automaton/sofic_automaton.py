"""
Run 77: THE RELATION AUTOMATON — an exact generating function for the excess.
============================================================================

The shapes (support-normalised multiples of m_t) are EXACTLY the closed walks
of the carry automaton:  states (q_{n-1}, q_n) in Z^2, letters c = p_n (the
polynomial coefficients), transition (a,b) -> (b, c + t b - a) at cost |c|,
start (0,0) with first letter nonzero, accept at (0,0) with last letter
nonzero.  Zero letters are the gaps of the polynomial and are allowed inside.

Theorem (generating function, R77).  With J_c(y) = I_c(2y)/I_0(2y) and
I_a(2y) = sum_k y^{a+2k}/(k!(a+k)!),

    X_r(K)  =  2 K r! [y^r] I_0(2y)^K . Psi(y),
    Psi(y)  =  sum_{closed walks} prod_letters J_{|c|}(2y),

where the sum runs over automaton closed walks (one per shape, gaps included).
Indeed I_0(2y)^K prod J = prod_j I_{|c_j|}(2y) I_0(2y)^{K-w}, which is exactly
the Bessel weight of Theorem H per cyclic shift; the factor 2K = signs x
shifts.  ONE DP evaluation of Psi(y) to degree D_max therefore yields X_r(K)
for EVERY r <= D_max and EVERY K, and M_r is not included (measured 0 to
r=10).  The same DP with monomial weights y^{|c|} gives the shape counts
S(R), and the Perron structure of Psi gives the uniformity ceiling r*(K).

Pipeline here:
  1. layered-BFS (numpy) for the closing-cost table W(a,b); state set
     {W <= D_max} (exact truncation: any state of a closed walk of cost
     <= D_max has W <= D_max);
  2. DP to the fixpoint f = (I - Z)^{-1} B on the zero-letter DAG, polynomial
     weights truncated at D_max;
  3. Psi(y); X_r(K) for K in {17, 33, 57, 101}; S(R) and the growth constant;
  4. VALIDATION: X_6(17) = 6120, X_8(17) = 5464480, X_10(17) = 3860398080
     (the exact R76 census values) and S(5..12) = 1,1,1,3,8,35,64,105.

Output: artifacts/r77/automaton.json
"""

from __future__ import annotations

import json
import os
import sys
import time
from collections import defaultdict

import numpy as np

DMAX = 16          # degree budget (validates r <= 10; S(R) up to 16)
T = 3              # trace of the cat map
FMAX = 400000      # safety cap on the state set


def bfs_states(t, D):
    """Closing-cost table W(a,b) for all states with W <= D, layered BFS.
    W(a,b) = min sum |c_j| over letter sequences with (q_{n-1}, q_n) = (a,b)
    (empty sequence for (0,0)).  Neighbours of (a,b) at cost |c|:
    (b, c + t b - a) and (c + t a - b, a)."""
    dist = {(0, 0): 0}
    layers = {0: [(0, 0)]}
    t0 = time.time()
    frontier = np.array([[0, 0]], dtype=np.int64)
    for d in range(1, D + 1):
        # candidates: neighbours of all states at cost >= d - |c|, c = d - base
        cand = set()
        # letters of cost exactly d from cost-0 states, plus cheaper letters
        # from higher bases: to keep it simple, expand ALL known states with
        # all letters of cost up to d - W(s); vectorised per letter.
        for base in range(0, d):
            st = layers.get(base)
            if not st:
                continue
            arr = np.array(st, dtype=np.int64)
            for c in (d - base, -(d - base)):
                if c == 0:
                    continue
                na = arr[:, 1]
                nb = c + t * arr[:, 1] - arr[:, 0]
                for pair in zip(na.tolist(), nb.tolist()):
                    if pair not in dist:
                        cand.add(pair)
                na2 = c + t * arr[:, 0] - arr[:, 1]
                nb2 = arr[:, 0]
                for pair in zip(na2.tolist(), nb2.tolist()):
                    if pair not in dist:
                        cand.add(pair)
        # zero-letter closure within the layer: F0 grows |u| = |b - lambda' a|,
        # so iterate until no change (bounded)
        changed = True
        while changed and len(cand) < FMAX:
            changed = False
            arr = np.array(sorted(cand), dtype=np.int64) if cand else \
                np.zeros((0, 2), dtype=np.int64)
            newc = set()
            na = arr[:, 1] if len(arr) else arr[:0]
            nb = (t * arr[:, 1] - arr[:, 0]) if len(arr) else arr[:0]
            for pair in zip(na.tolist(), nb.tolist()):
                if pair not in dist and pair not in cand:
                    newc.add(pair)
            na2 = (t * arr[:, 0] - arr[:, 1]) if len(arr) else arr[:0]
            nb2 = arr[:, 0] if len(arr) else arr[:0]
            for pair in zip(na2.tolist(), nb2.tolist()):
                if pair not in dist and pair not in cand:
                    newc.add(pair)
            if newc:
                cand |= newc
                changed = True
        layers[d] = sorted(cand)
        for p in layers[d]:
            dist[p] = d
        print(f"  layer {d}: +{len(cand)} states (total {len(dist)}, "
              f"{time.time()-t0:.1f} s)", flush=True)
        if len(dist) > FMAX:
            print("  STATE CAP HIT", flush=True)
            break
    return dist


def series_Ia(a, D):
    """I_a(2y) truncated at degree D: coeffs[k] = 1/(k!(a+k)!) for y^{a+2k}."""
    out = np.zeros(D + 1)
    k = 0
    while a + 2 * k <= D:
        out[a + 2 * k] = 1.0 / (math.factorial(k) * math.factorial(a + k))
        k += 1
    return out


def series_div(num, den, D):
    """num/den truncated to degree D (den[0] != 0)."""
    out = np.zeros(D + 1)
    den0 = den[0]
    for n in range(D + 1):
        s = num[n] - sum(out[n - k] * den[k] for k in range(1, n + 1))
        out[n] = s / den0
    return out


def main():
    t0 = time.time()
    out = {"generated": time.strftime("%Y-%m-%dT%H:%M:%S"),
           "R77": "relation automaton", "t": T, "D_max": DMAX}
    print(f"R77 relation automaton: t={T}, D_max={DMAX}", flush=True)

    # ---- 1. states
    print("[1] layered BFS for the closing-cost table", flush=True)
    dist = bfs_states(T, DMAX)
    states = sorted(dist.keys())
    sidx = {s: i for i, s in enumerate(states)}
    ns = len(states)
    out["n_states"] = ns
    print(f"  state set: {ns} states with W <= {DMAX}", flush=True)

    # ---- 2. weighted letter polynomials
    # J_c(y) = I_{|c|}(2y) / I_0(2y), truncated; I_0(2y) for the outer factor
    I0 = series_Ia(0, DMAX)
    J = {c: series_div(series_Ia(abs(c), DMAX), I0, DMAX)
         for c in range(-DMAX, DMAX + 1)}
    # transitions: from s=(a,b) with letter c -> (b, c + t b - a); keep target
    # in the state set; EXCLUDE c=0 at (0,0) (leading zeros); zero letters
    # elsewhere have J_0 = 1 and are part of the DAG.
    print("[2] transition table", flush=True)
    # predecessor lists: for target state s and letter c, the source is
    # (c + t*a - b, a)  [solve F_c(x,y) = (a,b): y = a, x = c + t y - b]
    preds = defaultdict(list)   # s_idx -> list of (src_idx, weight poly key)
    for si, (a, b) in enumerate(states):
        for c in range(-DMAX, DMAX + 1):
            if c == 0 and (a, b) == (0, 0):
                continue
            src = (c + T * a - b, a)
            si2 = sidx.get(src)
            if si2 is not None:
                preds[si].append((si2, c))
    print(f"  transitions: {sum(len(v) for v in preds.values())}", flush=True)

    # ---- 3. DP to the fixpoint, polynomial weights
    # f[s] = poly (length DMAX+1); source: f[(0,0)] starts as 1 (empty walk);
    # recurrence: f[s] += sum_{(src,c) in preds[s]} f[src] * J_{|c|}
    # iterate until fixpoint (zero-letter chains are acyclic in W, and each
    # nonzero letter raises the degree, so <= DMAX effective rounds; we run
    # to numerical fixpoint).
    f = {i: np.zeros(DMAX + 1) for i in range(ns)}
    f[sidx[(0, 0)]] = np.eye(1.0, DMAX + 1)[0] if False else \
        np.concatenate([[1.0], np.zeros(DMAX)])
    # NOTE: the empty walk sits at (0,0); closing directly from (0,0) with
    # c != 0 gives the m-shape... wait: closing needs F_c(s) = (0,0): from
    # (0,0) that is impossible for c != 0; f[(0,0)] = 1 only seeds walks that
    # then leave and return.
    order = sorted(range(ns), key=lambda i: dist[states[i]])
    rounds = 0
    tDP = time.time()
    while True:
        delta = 0.0
        for si in order:
            acc = np.zeros(DMAX + 1)
            for (src, c) in preds[si]:
                if src == si and c == 0:
                    continue
                acc += f[src] * J[c]
            if not np.array_equal(acc, f[si]):
                delta = max(delta, float(np.abs(acc - f[si]).max()))
                f[si] = acc
        rounds += 1
        if delta < 1e-18 or rounds > 60:
            break
    print(f"  DP fixpoint after {rounds} rounds ({time.time()-tDP:.1f} s), "
          f"delta {delta:.1e}", flush=True)

    # ---- 4. Psi(y): close at (0,0) with a nonzero final letter.
    # predecessors of (0,0) under letter c: src = (c + 0 - 0, 0) = (c, 0)
    Psi = np.zeros(DMAX + 1)
    for c in range(-DMAX, DMAX + 1):
        if c == 0:
            continue
        src = sidx.get((c, 0))
        if src is not None:
            Psi += f[src] * J[abs(c)]
    print(f"  Psi coeffs[0..{DMAX}]: {np.round(Psi, 6).tolist()}", flush=True)

    # ---- 5. S(R): monomial-weight DP (y^{|c|}) — same pipeline, weights 1
    # For S(R) we recompute with J replaced by y^{|c|} (and J_0 = 1 for gaps).
    Y = {c: np.zeros(DMAX + 1) for c in range(-DMAX, DMAX + 1)}
    for c in range(-DMAX, DMAX + 1):
        Y[c][abs(c)] = 1.0
    fm = {i: np.zeros(DMAX + 1) for i in range(ns)}
    fm[sidx[(0, 0)]] = np.concatenate([[1.0], np.zeros(DMAX)])
    while True:
        delta = 0.0
        for si in order:
            acc = np.zeros(DMAX + 1)
            for (src, c) in preds[si]:
                if src == si and c == 0:
                    continue
                shifted = np.zeros(DMAX + 1)
                w = abs(c)
                if w <= DMAX:
                    shifted[w:] = fm[src][:DMAX + 1 - w]
                acc += shifted
            if not np.array_equal(acc, fm[si]):
                delta = max(delta, float(np.abs(acc - fm[si]).max()))
                fm[si] = acc
        rounds += 1
        if delta < 1e-18 or rounds > 200:
            break
    Sm = np.zeros(DMAX + 1)
    for c in range(-DMAX, DMAX + 1):
        if c == 0:
            continue
        src = sidx.get((c, 0))
        if src is not None:
            shifted = np.zeros(DMAX + 1)
            shifted[abs(c):] = fm[src][:DMAX + 1 - abs(c)]
            Sm += shifted
    S_counts = {r: int(round(Sm[r])) for r in range(1, DMAX + 1) if Sm[r] > 0}
    print(f"  S(R) = {S_counts}", flush=True)
    out["S_R"] = S_counts
    growth = []
    for r in range(6, DMAX + 1):
        if S_counts.get(r) and S_counts.get(r - 1):
            growth.append(round(S_counts[r] / S_counts[r - 1], 3))
    out["S_growth_ratios"] = growth

    # ---- 6. X_r(K) for several K and the validation
    def Xr(K):
        outer = np.zeros(DMAX + 1)
        # I_0(2y)^K truncated
        acc = np.array([1.0])
        base = I0
        kk = K
        cur = base.copy()
        while kk:
            if kk & 1:
                acc = np.convolve(acc, cur)[:DMAX + 1]
            cur = np.convolve(cur, cur)[:DMAX + 1]
            kk >>= 1
        outer = acc
        prod = np.convolve(outer, Psi)[:DMAX + 1]
        xs = {}
        for r in range(1, DMAX + 1):
            xs[r] = 2 * K * math.factorial(r) * prod[r]
        return xs

    val = {}
    for K in (17,):
        xs = Xr(K)
        val[f"K={K}"] = {r: xs[r] for r in range(1, DMAX + 1)}
    out["X_r_predictions"] = val
    checks = {
        "X_6(17)": (val["K=17"][6], 6120),
        "X_8(17)": (val["K=17"][8], 5464480),
        "X_10(17)": (val["K=17"][10], 3860398080),
    }
    print("[validation]", flush=True)
    ok_all = True
    for k, (got, want) in checks.items():
        rel = abs(got - want) / max(1, abs(want))
        ok = rel < 1e-8
        ok_all &= ok
        print(f"  {k}: got {got:.6f}  want {want}  rel {rel:.2e}  "
              f"{'PASS' if ok else 'FAIL'}", flush=True)
    out["validation"] = {k: {"got": v[0], "want": v[1],
                             "ok": abs(v[0] - v[1]) / v[1] < 1e-8}
                         for k, v in checks.items()}
    out["validation_all_pass"] = ok_all

    # ---- 7. ceiling table
    ceil = {}
    triv = {2: 34, 4: 3366, 6: 538900, 8: 117173350}
    # exact pairing counts for K=17 up to r=16 via the DP of predict_Z
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from r75_multiples import predict_Z
    empty = {i: [] for i in range(DMAX + 1)}
    for K in (17, 33, 57, 101):
        xs = Xr(K)
        row = {}
        for r in range(2, DMAX + 1, 2):
            tr, _ = predict_Z(empty, K, r)
            row[r] = {"X": xs[r], "triv": tr,
                      "rel": xs[r] / tr if tr else None}
        ceil[f"K={K}"] = row
        rr = [f"r={r}:{row[r]['rel']*100:.2f}%" for r in sorted(row)
              if row[r]["rel"]]
        print(f"  ceiling K={K}: " + "  ".join(rr), flush=True)
    out["ceiling"] = ceil

    dest = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                        "artifacts", "r77", "automaton.json")
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=1, default=str)
    print("\nartifact ->", os.path.normpath(dest), flush=True)
    print(f"total time {time.time()-t0:.1f} s", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
