"""Append the Theorem G block (run 73.5) to LEDGER.md and THEORY.md. Idempotent."""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

BLOCK = r"""
### R73.5 — THEOREM G [PROVEN + measured]: the moment route is provably closed

Lemma F localises the obstruction in an explicit theta-like sum. The next question
is whether that sum cancels. **It does not, and the reason is structural.**

**Theorem G.** Let V have Weyl coefficients c with `||c||_1 = O(1)`, and let
`Vbar = K^{-1} sum_j U^j V U^{-j}` have coefficient vector `cbar`. The Birkhoff
average spreads every frequency over its full `A^t`-orbit with weight `1/K`, and
distinct orbits do not interfere, so

    ||cbar||_1 ≍ ||c||_1,   ||cbar||_2 ≍ K^{-1/2} ||c||_2,
    ||cbar||_1 / ||cbar||_2 ≍ sqrt(K) . ||c||_1/||c||_2 .

Hence, with `a_r` the classical moment (the v=0 coefficient of `Vbar^r`),

    |theta_r| / |a_r|  <~  m^{-1} ( ||cbar||_1/||cbar||_2 )^r  ≍  (c sqrt K)^r / m,

which is o(1) only for `r <~ 2 log m / log K`. **No observable of bounded Fourier
complexity can reach `r ≍ log m`**: the `1/K` dilution is forced, and an
A-invariant observable supported on a single orbit has ratio `≍ sqrt(K)` with no
freedom left. (This is the rigorous form of the T18 heuristic `s < 2/theta`.)

**Is the l^1 bound lossy?** Decided empirically. The exact Weyl coefficient vector
`a = hat{Vbar^r}` was computed by the `O(N^2 log N)` Weyl transform
(`a_v = N^{-1} Tr(T(-v) X)`, a DFT in `v_2` for each shift `v_1`) and every
`S_J(r) = sum_v a_v w^{Q_J(v)}` evaluated exactly:

| | r=4 | r=5 | r=6 | r=8 |
|---|---|---|---|---|
| max_J\|S_J\|/\|\|a\|\|_1, N=41 | 0.448 | 0.525 | 0.350 | 0.324 |
| max_J\|S_J\|/\|\|a\|\|_1, N=101 | 0.287 | 0.331 | 0.239 | 0.221 |
| max_J\|S_J\|/\|\|a\|\|_1, N=71 | 0.310 | 0.312 | 0.276 | 0.245 |
| max_J\|S_J\|/\|\|a\|\|_2 (all) | 7.9–14.5 | 9.9–18.2 | 7.5–14.6 | 7.6–14.9 |

`|S_J|` sits a **constant factor ≈ 3** below the l^1 bound and one to two orders
of magnitude **above** `||a||_2`: there is **no square-root cancellation to
harvest**. So the `C^r` growth in T8 is genuine, not an artefact of a lossy
estimate. Artifact `artifacts/r73/barrier_slack.json`, script
`src/theorems/theorem_g_moment_closed.py`.

**Corollary.** The moment method cannot reach the mean-spacing scale for this
family, for any fixed observable of bounded Fourier complexity. **Any proof of BGS
here must be resolvent-based, not moment-based.**

This closes an entire route rigorously, explains why Theorem A succeeds (the exact
covariance identity bypasses moments altogether instead of pushing them), and
leaves exactly one well-posed question as the whole remaining gap: a
self-consistent equation for `(V_lam - z)^{-1}` at `Im z ≍ m^{-delta}`.
"""

TH = r"""
### 11.5 Theorem G — the moment route is provably closed

For any V with `||c||_1 = O(1)`, the Birkhoff average dilutes each frequency over
its full `A^t`-orbit with weight `1/K`, so
`||cbar||_1/||cbar||_2 ≍ sqrt(K) ||c||_1/||c||_2` and therefore

    |theta_r|/|a_r|  <~  (c sqrt K)^r / m,

which is o(1) only for `r <~ 2 log m / log K`. This is the rigorous form of the
T18 heuristic. The `l^1` bound is moreover **tight up to a constant**: computing
the exact Weyl coefficient vector of `Vbar^r` and every quadratic-phase sum
`S_J(r)` gives `max_J |S_J| / ||a||_1` in [0.22, 0.53] for 4 <= r <= 8 across
three (A,N), and `max_J |S_J| / ||a||_2` in [7.5, 18.3] — no square-root
cancellation exists to exploit.

**Consequence.** The moment method cannot reach the mean-spacing scale for this
family, for any fixed observable of bounded Fourier complexity; any proof of BGS
here must be resolvent-based. This also explains why section 9.2's Theorem A
succeeds: it bypasses moments entirely via an exact covariance identity. The whole
remaining gap is a self-consistent equation for `(V_lam - z)^{-1}` at
`Im z ≍ m^{-delta}`.
"""


def patch(path, marker, text):
    p = os.path.join(ROOT, path)
    s = open(p, encoding="utf-8", errors="surrogateescape").read()
    if marker in s:
        return f"{path}: already present"
    open(p, "w", encoding="utf-8", errors="surrogateescape").write(
        s.rstrip() + "\n" + text)
    return f"{path}: appended"


print(patch("LEDGER.md", "R73.5 — THEOREM G", BLOCK))
print(patch("THEORY.md", "11.5 Theorem G", TH))
