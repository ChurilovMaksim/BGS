# Litwatch summary (R2.1, 2026-08-28)

Searched the period 2026-01-01 → 2026-08-28 (today) on the
queries listed in the brief. Two search providers failed
mid-run; the most informative queries that did return
results are listed below with their five most load-bearing
NEW results.

## Five most load-bearing NEW results

1. **Vinogradov's sieve and an estimate for an incomplete
   Kloosterman sum**, Sb. Math. 2026 (Karatsuba–Bourgain–Garaev
   bounds applied to double sums; same machinery as
   1211.4184, no new pointwise subgroup statement). Status:
   **ALREADY_KNOWN** (no advance on the p^{3/7} wall). URL:
   https://iopscience.iop.org/article/10.1070/SM9572/pdf

2. **Bounds on bilinear sums of generalized Kloosterman sums
   over arbitrary** (sum-product phenomenon, barrier
   `MN > p^{3/4}`), J. Number Theory 2026. Status:
   **ALREADY_KNOWN** (the barrier p^{3/4} is the classical
   additive-combinatorics wall, not a new subgroup statement).
   URL:
   https://www.sciencedirect.com/science/article/pii/S0022314X25002884

3. **Sums of kloosterman sums over square-free and smooth
   integers** (Shao–Shparlinski–Wijaya), Bull. Austral.
   Math. Soc. 113 (2026), 404–416. Status: **ALREADY_KNOWN**
   (twists by arithmetic functions, not the H³ pointwise
   bound relevant to BGS). URL:
   https://uknowledge.uky.edu/math_facpub/53/

4. **Norm-Trace and Kloosterman sums in finite semi-simple
   algebras** (square-root estimate over semi-simple
   algebras), arXiv:2603.18511, 7 Apr 2026. Status:
   **NEW (informative; not a wall-breaker)** — extends the
   Weil/Deligne machinery to semi-simple algebras with a
   square-root estimate; this is the right kind of
   generalisation that the **B Line (NH-sheaf)** would
   need, but the result is the Weil ceiling, not a
   power-saving-in-p statement. **Recommend B-subagent
   cross-checks the purity argument with the new norm-trace
   result for any Kloosterman sheaf restriction that lands
   on a semi-simple quotient.** URL:
   https://arxiv.org/abs/2603.18511

5. **Frobenius structure on rigid connections and arithmetic
   applications** (ℓ-adic generalized Kloosterman sheaf
   Kl_{G}^ℓ), arXiv:2603.09252, 10 Mar 2026. Status:
   **NEW (informative; not a wall-breaker)** — generalised
   Kloosterman sheaf on G-motivic connections; gives a
   uniform framework that the **B Line** can lean on, but
   the explicit bound is the Weil ceiling. URL:
   https://arxiv.org/abs/2603.09252

## Searches that did NOT return new advances

* "Stepanov method Kloosterman 2026" — no new Stepanov
  results on the double-system. The classical Stepanov
  (Acta Arith. 1986) and the Heath-Brown–Konyagin line are
  still the only published Stepanov-style bounds, and
  neither addresses the multiplicative-subgroup setting.
* "Linn 2024 GL3 Kloosterman 1/3 power saving 2026
  follow-up" — **no published follow-up to Linn
  arXiv:2412.04976**. The R58 discriminator (H³ transfer
  to the subgroup setting) remains the load-bearing
  result, and it was NEGATIVE: |sum|/k^{2/3} grows 3→18 as
  k grows 5→34 across 12 configs. **The OSV obstruction is
  *strengthened*, not weakened.**
* "Bourgain-Garaev improvement 2026" — Bourgain Problem 5
  literature (SlopDotCash 2026-06-15) is a github knowledge
  base that documents the published state: the prize is
  still thinner than `p^{1/4}` (square-root vs
  power-saving). No 2026 advance on the multiplicative-
  subgroup setting. URL:
  https://github.com/SlopDotCash/proximityprize/blob/main/docs/kb/bourgain-problem5-literature-gleaning-2026-06-15.md
* "Hecke eigenfunction QUE 2026 explicit improvement" —
  Helfgott's "Optimal bounds for sums of arithmetic
  functions" (Number Theory Web Seminar 2026-06-19) is
  tangential; no 2026 result closes the BGS-relevant gap.
  The closest is "Soft bounds for local triple products and
  the subconvexity-QUE" (LMS Proc., Oct 2025) but the
  smoothing/φ-type is polynomial, not the H³ setting
  relevant to BGS. URL:
  https://londmathsoc.onlinelibrary.wiley.com/doi/10.1112/mtk.70053

## Verdict for the Ring 2 attack

**The Bourgain-2005 / OSV-2021 wall is unchanged as of
2026-08-28.** No 2026 publication produces a pointwise
explicit power-saving-in-p bound on the multiplicative-
subgroup Kloosterman `S(a,b) = Σ_{h ∈ H} e_p(ah + b/h)`
below `k < p^{3/7+ε}`. The two 2026 norm-trace /
Frobenius-structure extensions (arXiv:2603.18511 and
arXiv:2603.09252) are Weil-ceiling, not power-saving. The
2026 bilinear-Kloosterman line (Springer GAFA 2026, BIRS
26w5546) hits the `p^{3/4}` additive-combinatorics wall,
not the `p^{3/7}` multiplicative-subgroup wall.

**Recommendation to the parent (Ring 2 orchestrator):**
the three R2.2 attack lines (Stepanov / Deligne /
Bourgain) are unlikely to move the wall on this run. The
honest R2.4 outcome is "wall unchanged; the published
`k ≥ p^{3/7+ε}` smooth law remains the frontier; the
unconditional local law at the mean-spacing scale remains
OPEN." Discriminator (R2.5) is moot unless a subagent
produces a calibrator-passing `[CONJECTURED]` claim with
a runnable test.
