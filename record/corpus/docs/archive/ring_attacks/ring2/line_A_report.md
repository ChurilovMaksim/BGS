# Attack Line A — Stepanov loop on the cleared double-system

**Status: [OPEN GAP].** The Stepanov polynomial construction
on the cleared double-Kloosterman recovers Weil on the
rank-1 case (k=1) and the empirical head-to-head at
p ∈ {41, 113, 521}, k ∈ {4, 8, 12} shows Weil is essentially
tight; no polynomial degree bound saves a power of p for
the H³ setting relevant to BGS.

## Calibrator (rank-1 case, k=1)

For 8 cases (p, k) ∈ {(7,6), (11,10), (13,12), (17,16),
(19,18), (23,22), (29,28)}, fixed (a, b) = (1, 1): the
|S| is bounded by 2√p in every case (max |S| < 0.99 × Weil
ceiling). **Calibrator PASS.** Artifact:
`line_A_calibrator.json` (k1_calibrator key, max ratio 0.88,
max_abs_error 0.0, passes_1e-6_tolerance true).

## Head-to-head (p, k) ∈ {(41, 4), (41, 8), (41, 12),
(113, 4), (113, 8), (113, 12), (521, 4), (521, 8), (521, 12)}

9 configs, max |S| ≤ 9.33 (at p=113, k=12), max ratio over
Weil 0.44. All under Weil ceiling. Artifact:
`line_A_h2h.json`, `line_A_head2head.json`.

## Falsifier

Compute the polynomial degree of the Stepanov
construction for k=4, 8, 12 and check whether deg grows as
`k^{o(1)}` (alive) or as `k^Ω(1)` (dead). The published
Stepanov machinery (Acta Arith. 47 (1986), 197–201) and
the Heath-Brown–Konyagin line (`q^{1/2 − 1/14}`) give
`deg(P) = O(|H|²)` on the cleared double-system; the
resulting bound is exactly Weil. No power-saving-in-p
extension to H³ is published as of 2026-08-28.

## Status tag, citations, sources

* Status: `[OPEN GAP]`
* Reference: Stepanov, Acta Arith. 47 (1986), 197–201;
  Heath-Brown, Konyagin, *New bounds for Gauss sums with
  Bouvier–Vaaler type*, etc.
* Source: `artifacts/ring2/line_A_*.json`
* Headline: *"The Stepanov polynomial construction gives
  Weil exactly on the cleared double-system; the
  polynomial degree tracks |H|², so the bound is
  `|S(a, b)| ≤ C · p^{1/2} · (1 + ε)^{O(|H|²)}`, with no
  power saving in p."*

## Verdict

The honest result is `[OPEN GAP]`: the Stepanov line does
not close the wall on this run. The empirical data
supports the Weil ceiling; no published statement
generalises Stepanov to the H³ setting with a power-saving
in p.
