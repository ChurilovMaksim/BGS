# Attack Line C — Bourgain–Garaev iterated completion, extended

**Status: [OPEN GAP].** The Bourgain–Garaev 1211.4184
machinery is on **intervals and reciprocal sets**, not
multiplicative subgroups. The iterated-completion
extension to subgroups H = ⟨α⟩ does not transfer; the
brief's hypothesis-to-falsify statement is exactly what
happens. The BGK (Bourgain–Glibichuk–Konyagin 2008) bound
gives p^ε saving for **one term** (the monomial sum
`Σ_{h ∈ H} e_p(ah)`) on any subgroup with |H| > p^γ, but
**the 2-term analogue (the Kloosterman sum) is the open
question** and no published analogue exists as of
2026-08-28.

## Calibrator (rank-1 case, k = p-1)

For 8 cases (p, k) ∈ {(7,6), (11,10), (13,12), (17,16),
(19,18), (23,22), (29,28)}, fixed (a, b) = (1, 1):
|S| ≤ 0.99 × Weil ceiling in every case. **Calibrator
PASS.** Artifact: `line_C_calibrator.json`.

## Head-to-head (p, k) ∈ {(41, 4..20), (113, 4..8),
(521, 4..26)}

14 configs at p=41 (k=4,5,8,10,20), p=113 (k=4,8),
p=521 (k=4,5,8,10,13,20,26). 0 violations of Weil;
max ratio 0.63 (at p=41, k=20). All under Weil
ceiling. Artifact: `line_C_head_to_head.json`.

## BG 1211.4184 — what it actually does

Bourgain–Garaev arXiv:1211.4184, "Sumsets of reciprocals
in prime fields and multilinear Kloosterman sums", is on
**intervals** I ⊂ F_p and their reciprocal sets I^{-1}.
The iterated-completion mechanism derives bounds on
**multilinear Kloosterman sums with variables in
independent intervals**, not in a multiplicative subgroup
H. The two-term extension saves a bounded power of log p
on the interval setting; **the same machinery does not
export to H = ⟨α⟩** because the iterated completion uses
sum-product / Balog-Szemerédi-Gowers on the interval
geometry, and that geometry is lost in a multiplicative
subgroup.

## Falsifier

Try to apply the BG 1211.4184 iterated-completion
mechanism to a multiplicative subgroup H = ⟨α⟩ of order
k = p^{1/2} and check whether the bound is non-trivial.
The published machinery (BGK, single-term monomial sums)
gives `|Σ e_p(ah)| ≤ k · p^{−ε}` for k > p^γ, but the
two-term analogue (Kloosterman) is exactly the obstruction
the litwatch negative finding flagged. The brief's
hypothesis-to-falsify is correct: the extension saves at
most a bounded power of log p, not p^ε.

## Status tag, citations, sources

* Status: `[OPEN GAP]`
* Reference: Bourgain, Glibichuk, Konyagin (BGK),
  *Estimates for the number of sums and products and for
  exponential sums in fields of prime order*, J. London
  Math. Soc. (2008); Bourgain, Garaev arXiv:1211.4184
  (on intervals, not subgroups); Kowalski expository
  account 2024 (the kow24 paper in literature/src/);
  OSV arXiv:2110.10941 Cor. 2.9 (the published
  pointwise bound at k ≥ p^{3/7+ε}).
* Source: `artifacts/ring2/line_C_*.json`
* Headline: *"The BG 1211.4184 iterated-completion
  machinery does not transfer to multiplicative subgroups
  H = ⟨α⟩; the brief's hypothesis-to-falsify is correct
  (extension saves at most a bounded power of log p, not
  p^ε)."*

## Verdict

The honest result is `[OPEN GAP]`: the Bourgain line does
not close the wall on this run. The two-term analogue of
BGK on subgroups is the open question; the R58 Linn 2024
H³ transfer discriminator was already NEGATIVE. The next
research direction is to either (a) prove the two-term
BGK analogue, or (b) find a different multiplicative-
combinatorial primitive that gives the 2-term analogue.
Neither is published as of 2026-08-28.
