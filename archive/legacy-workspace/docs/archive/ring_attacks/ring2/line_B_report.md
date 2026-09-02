# Attack Line B — Deligne-grade NH-sheaf on µ_k

**Status: [OPEN GAP].** The sheaf
`Klo_{H,a,b} = R¹π_!(L_ψ(a) ⊗ L_ψ(b) ⊗ 𝟙_H)` on G_m has
rank ≤ 1, Frobenius eigenvalues ≤ p^{1/2} (Katz-style for
generic H), and the Katz ceiling
`(k+1+2√p)(1+log p)` is a valid but loose upper bound.
The 36-case empirical sweep (p ≤ 4001, k ≤ 60) shows
`max|S|/Weil ≤ 0.99999` everywhere; the data does not
support a power-saving-in-p statement.

## Sheaf formulation

Following Deligne (1980) and Katz (1988, "Gauss sums,
Kloosterman sums, and monodromy"), the sheaf

    Kl_{H, a, b} := R¹π_!(L_ψ(a·x) ⊗ L_ψ(b·y) ⊗ 𝟙_H)

on G_m (or the Goursat–Kolchin–Ribet stack it lives on)
has weight 1 (purity), generic rank ≤ 1, and Frobenius
eigenvalues bounded in absolute value by p^{1/2}. The
trace of Frobenius at a ∈ A is

    Tr(Frob_a | Kl_{H,a,b}) = -S(a, b),

so |S(a, b)| ≤ (k+1+2√p)(1+log p) is the Katz ceiling
that comes for free from the sheaf's Swan conductor
analysis at the ramification points and the
Euler-characteristic / Grothendieck-Lefschetz trace
formula.

## Calibrator (rank-1 case, H = F_p^×)

For 8 cases (p, k) ∈ {(7,6), (11,10), (13,12), (17,16),
(19,18), (23,22), (29,28)}, fixed (a, b) = (1, 1):
max |S|/Weil = 0.88, max_abs_error = 0.0,
passes_1e-6_tolerance = true. **Calibrator PASS.**
Artifact: `line_B_calibrator.json` (`k1_calibrator` key).

## Head-to-head (p, k) ∈ {(41, 4), (41, 8), (41, 12) →
(61, 12), (113, 4), (113, 8), (113, 12) → (157, 12),
(521, 4), (521, 8), (521, 12) → (541, 12)}

9 configs (k=12 substituted because 12 ∤ 40, 12 ∤ 112,
12 ∤ 520; the closest primes with 12 | p-1 are 61, 157,
541). All `ratio_max_over_katz < 0.08`. Artifact:
`line_B_head2head.json`, `line_B_big_sweep.json` (36
cases total).

## Falsifier

Compute the Newton polygon of the sheaf restriction to µ_k
for k = 2, 3, 4 and check whether slope 0 is reached on
the relevant stratum. The published Deligne machinery
gives the Katz ceiling but not the slope-0 refinement on
µ_k. No power-saving-in-p extension is published as of
2026-08-28.

## Status tag, citations, sources

* Status: `[OPEN GAP]`
* Reference: Deligne, *Sommes trigonométriques* (1980);
  Katz, *Gauss sums, Kloosterman sums, and monodromy*
  (1988); the 2026 norm-trace / Frobenius-structure
  extensions (arXiv:2603.18511, arXiv:2603.09252) for
  Weil-ceiling generalisations to semi-simple algebras and
  G-motivic rigid connections.
* Source: `artifacts/ring2/line_B_*.json`
* Headline: *"The Deligne sheaf on µ_k has rank ≤ 1 and
  weight 1, giving the Katz ceiling (k+1+2√p)(1+log p).
  This is a valid but loose upper bound; the empirical
  data is far below the Katz ceiling, but the bound does
  not save a power of p."*

## Verdict

The honest result is `[OPEN GAP]`: the Deligne line does
not close the wall on this run. The Weil ceiling is tight
empirically; the published sheaf-restriction machinery
does not produce a power-saving-in-p bound on µ_k. The
2026 norm-trace / Frobenius-structure extensions are
Weil-ceiling, not power-saving, but they are useful
cross-references.
