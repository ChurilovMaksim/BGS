"""Word-trace algebra rewriter (verification-suite copy).  QUARANTINED IN R108.

This copy crashes on re-execution ('word ('V','V') unresolved', line 244)
and several of its reduction rules (R*W = R, E*R = R, R*E = R) are
numerically FALSE (errors sqrt(2), 1, 1 -- found by R108 re-execution).
It is superseded by code/large_m/word_trace_proof.py (the load-bearing
RUN 91.17 engine) and by the independent exact check
code/referee/r108c_arcsine_thmB.py, which verifies Theorem 91.5
(Tr(M^{2s}) = binom(2s,s) m - beta_s) to machine precision at N = 53,
199 for s <= 6.  Do not use or cite this file; retained as history.

The algebra of the full-group matrix: M = V + V* with

    V V* = I - E,   V* V = I - F,          (partial isometry)
    E^2 = E, F^2 = F, E F = F E = 0,       (rank-1 projections)
    E V = V F = F V* = V* E = 0,           (annihilation)
    V E V* = R,  V* F V = S,               (rank-1, Tr R = Tr S = 1)
    Tr I = m,  Tr E = Tr F = Tr R = Tr S = 1,
    Tr(V^k) = 0, Tr(V E) = Tr(E V*) = Tr(F V) = Tr(V* F) = 0.

This engine rewrites every word in {V, V*} of length 2s into a linear
combination of normal-form atoms and sums the traces, proving
Tr(M^{2s}) = binom(2s,s) m - beta_s with beta_s measured exactly.

The rewriter: words are reduced by repeatedly applying the rules to
adjacent factors.  Normal forms are products of atoms from
{I, E, F, R, S, VE, EW, FV, WF} with the additional reduction rules
derived from the relations (R E = R?, R W = ?, etc. — pinned numerically).
"""
import sys
import os
import json
import time
from itertools import product

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "src", "large_m"))
sys.path.insert(0, os.path.join(ROOT, "src", "theorems"))

from fourth_mixed_moment import dlog_table, jacobi_matrix  # noqa: E402
from theorem_ii_twisted_jacobi import primitive_root  # noqa: E402

OUT_DIR = os.path.join(ROOT, "artifacts", "r91")


def full_mats(N, q):
    g = primitive_root(N)
    dlog = dlog_table(N, g)
    ks = np.arange(N - 1)
    xs = np.array([x for x in range(N) if x not in (0, 1)], dtype=np.int64)
    dl_x = dlog[xs]
    dl_xm1 = dlog[(xs - 1) % N]
    W = np.exp(-2j * np.pi * np.outer(ks, dl_x) / (N - 1))
    Vm = np.exp(2j * np.pi * np.outer(ks, dl_xm1) / (N - 1))
    ph = np.exp(2j * np.pi * (q * xs % N) / N)
    J = (W * ph) @ Vm.T
    return J / (N - 1)


def pin_atom_traces(N=37):
    """Numerically pin every atom trace used by the rewriter."""
    V = full_mats(N, 1)
    Wv = V.conj().T
    m = N - 1
    E = np.ones((m, m), dtype=complex) / m
    F = np.array([[(-1.0) ** (i + j) for j in range(m)]
                  for i in range(m)], dtype=complex) / m
    atoms = {
        "I": np.eye(m, dtype=complex),
        "E": E, "F": F,
        "R": V @ E @ Wv, "S": Wv @ F @ V,
        "VE": V @ E, "EW": E @ Wv, "FV": F @ V, "WF": Wv @ F,
        "V": V, "W": Wv,
    }
    traces = {k: complex(np.trace(v)) for k, v in atoms.items()}
    return V, Wv, E, F, traces


def reduce_word(w, max_iter=2000):
    """Rewrite a word (tuple of 'V'/'W') into a linear combination of
    normal forms.  Returns dict mapping normal-form tuples to coefficients.

    Normal-form atoms: 'I', 'E', 'F', 'R', 'S', 'VE', 'EW', 'FV', 'WF',
    and unreducible leftover words (trace 0 by charge, kept for safety).
    """
    # state: dict mapping tuple-of-atoms -> coefficient
    terms = {w: 1.0}
    for _ in range(max_iter):
        new_terms = {}
        changed = False
        for word, coef in terms.items():
            red = reduce_once(word)
            if red is None:
                new_terms[word] = new_terms.get(word, 0) + coef
            else:
                changed = True
                for nf, c in red:
                    new_terms[nf] = new_terms.get(nf, 0) + coef * c
        terms = new_terms
        if not changed:
            break
    return terms


def reduce_once(word):
    """Apply one rewrite rule; return list of (normal_form, coeff) or None."""
    w = list(word)
    n = len(w)
    for i in range(n):
        # binary rules
        if i + 1 < n:
            a, b = w[i], w[i + 1]
            if a == 'V' and b == 'W':
                rest = w[:i] + w[i + 2:]
                return [(tuple(rest + ['I']), 1.0), (tuple(rest + ['E']), -1.0)]
            if a == 'W' and b == 'V':
                rest = w[:i] + w[i + 2:]
                return [(tuple(rest + ['I']), 1.0), (tuple(rest + ['F']), -1.0)]
            if a == 'E' and b in ('V', 'F'):
                rest = w[:i] + w[i + 2:]
                return [(tuple(rest), 0.0)]
            if a == 'F' and b in ('W', 'V'):
                rest = w[:i] + w[i + 2:]
                return [(tuple(rest), 0.0)]
            if a == 'V' and b == 'F':
                rest = w[:i] + w[i + 2:]
                return [(tuple(rest + ['VE']), 1.0)]
            if a == 'E' and b == 'W':
                rest = w[:i] + w[i + 2:]
                return [(tuple(rest + ['EW']), 1.0)]
            if a == 'W' and b == 'E':
                rest = w[:i] + w[i + 2:]
                return [(tuple(rest), 0.0)]
            if a == 'F' and b == 'V':
                rest = w[:i] + w[i + 2:]
                return [(tuple(rest + ['FV']), 1.0)]
            if a == 'E' and b == 'E':
                rest = w[:i] + w[i + 1:]
                return [(tuple(rest), 1.0)]
            if a == 'F' and b == 'F':
                rest = w[:i] + w[i + 1:]
                return [(tuple(rest), 1.0)]
            if a in ('E', 'F') and b in ('E', 'F') and a != b:
                return [(tuple(w[:i] + w[i + 2:]), 0.0)]
            # atoms: VE / V? R handling below
        # ternary rules
        if i + 2 < n:
            a, b, c = w[i], w[i + 1], w[i + 2]
            if a == 'V' and b == 'E' and c == 'W':
                rest = w[:i] + w[i + 3:]
                return [(tuple(rest + ['R']), 1.0)]
            if a == 'W' and b == 'F' and c == 'V':
                rest = w[:i] + w[i + 3:]
                return [(tuple(rest + ['S']), 1.0)]
    # atom-adjacent reductions: R E = R (E absorbed), E R = ?, R W = ?
    for i in range(n - 1):
        a, b = w[i], w[i + 1]
        if a == 'R' and b == 'E':
            return [(tuple(w[:i] + w[i + 1:]), 1.0)]
        if a == 'E' and b == 'R':
            return [(tuple(w[:i] + w[i + 1:]), 1.0)]  # E R = R? pinned numerically
        if a == 'S' and b == 'F':
            return [(tuple(w[:i] + w[i + 1:]), 1.0)]
        if a == 'F' and b == 'S':
            return [(tuple(w[:i] + w[i + 1:]), 1.0)]
        if a == 'R' and b == 'W':
            rest = w[:i] + w[i + 2:]
            return [(tuple(rest + ['R']), 1.0)]  # R W = R (VEV* V* = V E (V*V*)...)
        # R V: V E V* V = V E (I - F)... = V E - V E F = VE. trace 0.
        if a == 'R' and b == 'V':
            rest = w[:i] + w[i + 2:]
            return [(tuple(rest + ['VE']), 1.0)]
        if a == 'V' and b == 'S':
            rest = w[:i] + w[i + 2:]
            return [(tuple(rest + ['WF']), 1.0)]  # V V* F V = (I-F) F V = 0... pinned
    return None


def atom_trace(t):
    return {"I": None, "E": 1.0, "F": 1.0, "R": 1.0, "S": 1.0,
            "VE": 0.0, "EW": 0.0, "FV": 0.0, "WF": 0.0,
            "V": 0.0, "W": 0.0}[t]


def word_trace(w):
    terms = reduce_word(w)
    total_m = 0.0
    total_1 = 0.0
    for nf, coef in terms.items():
        # normal form is a product of atoms; trace factors only if atoms
        # multiply to trace-1 pieces — but products like (E)(F) are 0, and
        # (E)(R)=R etc. were reduced. Any remaining product with >=2 atoms
        # that isn't reduced has trace handled by the pinning table only if
        # it is a single atom.  For safety, assert single-atom normal forms.
        if len(nf) == 0:
            total_m += coef  # empty word = I
        elif len(nf) == 1:
            t = nf[0]
            if t == 'I':
                total_m += coef
            else:
                total_1 += coef * atom_trace(t)
        else:
            # product of atoms — reduce further or zero; treat as unresolved
            raise RuntimeError(f"unresolved normal form {nf}")
    return total_m, total_1


def main():
    t0 = time.time()
    V, Wv, E, F, traces = pin_atom_traces(37)
    print("pinned atom traces at N=37:")
    for k, v in traces.items():
        print(f"  Tr({k}) = {v:.6f}")
    # verify R W = R etc.
    m = 36
    RN = V @ E @ Wv
    print("  ||R W - R|| =", np.linalg.norm(RN @ Wv - RN))
    print("  ||E R - R|| =", np.linalg.norm(E @ RN - RN))
    print("  ||R E - R|| =", np.linalg.norm(RN @ E - RN))

    results = []
    for s in range(1, 7):
        tot_m = 0.0
        tot_1 = 0.0
        for w in product(['V', 'W'], repeat=2 * s):
            # cyclic: the trace of a word equals the trace of any rotation;
            # try each rotation until one reduces cleanly
            got = False
            for r in range(2 * s):
                ww = tuple(w[r:] + w[:r])
                try:
                    a_m, a_1 = word_trace(ww)
                    tot_m += a_m
                    tot_1 += a_1
                    got = True
                    break
                except RuntimeError:
                    continue
            if not got:
                raise RuntimeError(f"word {w} unresolved")
        tr_pred = tot_m * m + tot_1
        # numeric check
        M = V + Wv
        ev = np.linalg.eigvalsh(M)
        tr_meas = float((ev ** (2 * s)).sum())
        ok = abs(tr_pred - tr_meas) < 1e-8
        results.append({"s": s, "a_m": tot_m, "a_1": tot_1,
                        "pred": tr_pred, "meas": tr_meas, "ok": ok})
        print(f"s={s}: {tot_m:.0f}*m + {tot_1:.0f} -> pred {tr_pred:.4f} "
              f"meas {tr_meas:.4f} {'OK' if ok else 'MISMATCH'}")
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(os.path.join(OUT_DIR, "word_trace_proof.json"), "w") as fh:
        json.dump({"results": results, "pinned_traces":
                   {k: float(v) for k, v in traces.items()}}, fh, indent=1)
    print("walltime", time.time() - t0)


if __name__ == "__main__":
    main()
