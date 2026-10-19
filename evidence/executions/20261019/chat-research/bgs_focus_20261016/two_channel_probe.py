#!/usr/bin/env python3
"""Bounded exploratory probe of the OPEN two-channel law, not evidence of BGS."""
import hashlib
import json
import sys
import numpy as np

SEED = 2026101602
REPEATS = 150


def fourier(n):
    x = np.arange(n)
    return np.exp(2j*np.pi*np.outer(x, x)/n) / np.sqrt(n)


def symplectic(q):
    x = np.array([(a, b) for a in range(q) for b in range(q)])
    omega = np.outer(x[:, 0], x[:, 1]) - np.outer(x[:, 1], x[:, 0])
    return np.exp(2j*np.pi*(omega % q)/q) / q


def run(s, rng):
    n = len(s)
    t = np.empty(REPEATS)
    unit_error = 0.
    for rep in range(REPEATS):
        order = rng.permutation(n)
        work = s[np.ix_(order, order)].copy()
        for v in range(n, 2, -1):
            w = np.exp(2j*np.pi*rng.random())
            q = w/(1-work[v-1, v-1]*w)
            c = work[:v-1, v-1].copy()
            b = work[v-1, :v-1].copy()
            work[:v-1, :v-1] += q*np.outer(c, b)
        terminal = work[:2, :2]
        unit_error = max(unit_error, float(np.linalg.norm(terminal@terminal.conj().T-np.eye(2))))
        t[rep] = abs(terminal[0, 1])**2
    assert unit_error < 2e-9, unit_error
    assert t.min() >= -1e-10 and t.max() <= 1+1e-10
    order_t = np.sort(t)
    ks = max(float(np.max(np.arange(1, REPEATS+1)/REPEATS-order_t)),
             float(np.max(order_t-np.arange(REPEATS)/REPEATS)))
    return {"repeats": REPEATS, "mean": float(np.mean(t)),
            "second_moment": float(np.mean(t*t)),
            "third_moment": float(np.mean(t*t*t)),
            "ks_to_uniform": ks, "max_terminal_unitarity_error": unit_error,
            "samples": t.tolist()}


def main():
    rng = np.random.default_rng(SEED)
    results = []
    for q in (7, 11, 15):
        n = q*q
        f = fourier(n)
        row_order = np.random.default_rng(SEED+n).permutation(n)
        for name, s, scope in (
                ("symmetric_fourier", f, "excluded reversal-gap control"),
                ("row_permuted_fourier", f[row_order, :], "finite frozen unitary, no asymptotic hypothesis certificate"),
                ("symplectic_involution", symplectic(q), "existing project construction, analytic reversal norm=1/q")):
            b = s*s.T.conj()
            reversal_norm = float(np.max(np.abs(np.linalg.eigvalsh(b))))
            initial_error = float(np.linalg.norm(s@s.conj().T-np.eye(n)))
            assert initial_error < 1e-9
            result = run(s, rng)
            result.update(family=name, N=n, initial_reversal_norm=reversal_norm,
                          initial_unitarity_error=initial_error, scope=scope,
                          initial_complex128_sha256=hashlib.sha256(s.tobytes()).hexdigest())
            results.append(result)
            print(json.dumps({k: result[k] for k in ("family", "N", "mean", "second_moment", "ks_to_uniform")}))
    out = {"status": "completed", "arithmetic": "IEEE-754 binary64, complex128",
           "numpy": np.__version__, "generator": "numpy PCG64", "seed": SEED,
           "cases": results,
           "non_claims": ["Finite exploratory samples, not an asymptotic theorem.",
                          "The symmetric Fourier control violates the reversal gap.",
                          "No assertion that cutoff estimates are effective at these dimensions.",
                          "No physical BGS inference; the two-channel law remains open."]}
    with open(sys.argv[1], "w", encoding="utf-8") as stream:
        json.dump(out, stream, indent=2)
        stream.write("\n")


if __name__ == "__main__":
    main()
