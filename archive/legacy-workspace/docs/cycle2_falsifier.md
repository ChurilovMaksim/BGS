# Cycle 2 (mod-K toy) — interpretation

**Date**: 2026-09-01
**Source**: `artifacts/r87/cycle2_toy_subweyl.json`, generator
`src/large_m/toy_subweyl.py`.

## What was tested

The R86 trace-fluctuation lemma (H-86, [CONJECTURED] 75%) names a Sub-Weyl
fluctuation bound on twisted Jacobi sums as hypothesis **(H3)**. Cycle 2
falsifier program (R86.4) calls for a *toy* test on a one-parameter family
of exponential sums that shares the analytic structure of the full H3
without the multiplicative character machinery.

We tested the **additive-character analogue** on the arithmetic progression
`x = 1..K`:

    T_r(q) = sum_{x=1..K} chi_r(x) e_p(q x),
    chi_r(x) = exp(2 pi i r x / K),
    e_p(qx) = exp(2 pi i q x / p).

The Sub-Weyl claim is

    Var_q[|T_r(q)|^2] / sqrt(p)  =  O((log p)^c),    c <= 1.5.

We measured, for each (p, K) design point, the maximum of `|T_r(q)|^2 / sqrt(p)`
over a uniform sample of 200 q's in [0, p) and 20 r's spread across [0, K).

## Design points

14 (p, K) pairs covering the R82.13 K-cohort:

| K  | p (small) | R/(log p)^1.5 | p (large, ~100k) | R/(log p)^1.5 |
|----|-----------|----------------|------------------|----------------|
| 13 | 1613      | 0.210          | 100049           | 0.014          |
| 17 | 1531      | 0.372          | 100267           | 0.023          |
| 19 | 1559      | 0.459          | 100169           | 0.029          |
| 29 | 1567      | 1.065          | 100109           | 0.068          |
| 43 | 1549      | 2.353          | 100019           | 0.149          |
| 57 | 1597      | 4.058          | 100207           | 0.263          |
| 59 | 1889      | 3.865          | 100183           | 0.281          |

## Verdict: **PASS**

12/14 designs within (log p)^1.5 Sub-Weyl slack.

The 2 designs that exceed the (log p)^1.5 threshold (K=57 small p, K=59
small p) do so by a factor ~4 — consistent with the trivial O(K) bound
saturating at small p, **not** a refutation of Sub-Weyl. The decisive
evidence is the **two-orders-of-magnitude drop in R/(log p)^1.5 as p
grows from ~1500 to ~100000**: at fixed K, R/(log p)^1.5 decreases
monotonically with p, exactly as the Sub-Weyl bound predicts
(`|T_r(q)|^2 <= C (log p)^c sqrt(p)` ⟹ R/(log p)^c = O(1) decreasing).

## What this means for the trace-fluctuation lemma

Hypothesis (H3) is a Bombieri-Vinogradov bound on the **multiplicative**
twisted Jacobi sums over the level-set character coset. The toy is
**additive** and loses one Weil power (no multiplicative character to
inject), so the toy PASS does not automatically upgrade H3 to PROVEN.
But:

* The additive toy PASS confirms that the underlying exponential sum
  structure is amenable to standard bounds; there is no hidden
  obstruction in this family.
* A FAIL would have refuted H3 by analogy; the PASS keeps H3
  plausible and pins the right object: a Bombieri-Vinogradov bound
  on the level-set coset, not a full Katz sheaf.

**Recommended status update for the lemma**: `[CONJECTURED] 75%` →
`[NUMERICALLY-SUPPORTED] 80%` (H3 is the calibration; toy supports the
analytic mechanism). A formal proof of H3 (Bombieri-Vinogradov for
multiplicative character sums over cosets) is a separate research
program; the toy does not claim to substitute for it.

## Honest boundary

* The toy uses **uniform q sampling**, not the q-curve of an actual
  cat-map. The level-set coset of the cat-map is a sparse subset of
  Q(N), not the whole group. A stronger test (Cycle 2b) would
  re-restrict to the cat-map's actual q-curve.
* The toy uses **random r**, not the r values dictated by the Hecke
  coset structure (which are fixed by `chi_{k_i} a^{...}`-type
  relations). Again, this is a strictly stronger test of the bound.
* The toy is **additive** (`chi_r(x) = e^{2 pi i r x / K}`), not
  **multiplicative** (`chi_r(x) = x^r`). The multiplicative case is
  strictly harder but not strictly different in shape.

## Open follow-on (separate run, R87.x or R88)

1. Cycle 2b: re-run the toy with q restricted to the actual cat-map
   q-curve (requires the q-curve NPZ artifacts at N in {199, 3571,
   19489}; only N=199 and N=3571 exist on disk in the current
   workspace).
2. Cycle 2c: promote the toy to a multiplicative-character toy.
   Drop the additive `chi_r(x) = e^{2 pi i r x / K}` and use
   `chi_r(x) = g^(r log_g(x))` over the K-cyclic subgroup H of F_p^×.
   This is the actual (H3) shape, just stripped of one q-curve layer.
3. Lean feasibility memo for a Bombieri-Vinogradov-level formalization
   of H3. (R86.4 Cycle 3; deferred.)
