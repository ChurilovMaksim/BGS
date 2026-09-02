# Ring 2 synthesis — 3 attack lines on the p^{3/7} wall (2026-08-28)

## Bottom line

**The Bourgain-2005 / OSV-2021 wall is unchanged as of
2026-08-28.** All three attack lines recover Weil on the
rank-1 case (H = F_p^×) and produce empirical data
consistent with Weil being the tight bound on the rank-1
sheaf restriction to µ_k ⊂ F_p^×. **No line closes the
gap below `k < p^{3/7+ε}`; the unconditional local law at
the mean-spacing scale remains OPEN.**

## Lines in summary

| Line | Approach | Calibrator | Head-to-head | Status | Falsifier |
|---|---|---|---|---|---|
| A — Stepanov | Stepanov-polynomial construction on the cleared double-system | PASS (k=1, fixed a, b at p=7,11,13,17,19,23,29; max |S|/Weil < 1.0 across 8 cases) | `line_A_h2h.json` (9 configs, 0 violations) | `[OPEN GAP]` | polynomial degree > k^ε for any fixed ε — falsifier: compute deg(P) for k=4,8,12 and check growth |
| B — Deligne | Klo_{H,a,b} = R¹π_!(L_ψ(a) ⊗ L_ψ(b) ⊗ 𝟙_H) NH-sheaf on G_m; weight-1 purity; Katz ceiling | PASS (max ratio 0.88 on rank-1, 0 violations across 8 calibrator cases) | `line_B_head2head.json` (9 configs at p∈{41,113,521}, k∈{4,8,12}; 12 substituted 41→61, 113→157, 521→541 because 12∤40) | `[OPEN GAP]` | sheaf restricts to µ_k but Newton polygon does not reach slope 0 — falsifier: compute Newton polygon for k=2,3,4 subgroups and check slope at 0 |
| C — Bourgain | Bourgain–Garaev 1211.4184 (intervals + multilinear Kloosterman) iterated-completion extension to subgroups | PASS (8 rank-1 cases at p=7,11,13,17,19,23,29 — all under Weil) | `line_C_head_to_head.json` (14 configs at p∈{41,113,521}, k∈{4,5,8,10,13,20,26}; 0 violations; max ratio 0.63) | `[OPEN GAP]` | iterated-completion saves p^ε on subgroups — falsifier: replicate the additive-combinatorics / BSG machinery on H=⟨α⟩ and check the bound is non-trivial |

**All three lines: [OPEN GAP].** None produces a
[CONJECTURED] claim with a runnable discriminator.

## Empirical data summary (all 3 lines)

Across 14 + 9 + 9 = 32 distinct (p, k) configs at
p ∈ {41, 61, 113, 157, 521, 541}, k ∈ {4, 5, 8, 10, 12, 13,
20, 26}, the maximum |S(a, b)| over (a, b) coprime to p is
**uniformly under the Weil ceiling 2√p**. The Weil bound
is essentially tight: the worst empirical ratio
`max|S|/(2√p) ≈ 0.99999` (Deligne big sweep at p=4001, k=4)
and the most common ratio is 0.2-0.5 (Bourgain head-to-head
at intermediate k). **No finite-k power-saving-in-p is
observed below p^{3/7+ε}.**

The Bourgain–Garaev 1211.4184 machinery was re-checked: it
is on **intervals and reciprocal sets**, not multiplicative
subgroups. The additive-combinatorial iterated-completion
gives p^ε savings for one term (BGK, single term monomial
sums) on **any** subgroup H with |H| > p^γ, but the
extension to two terms (the Kloosterman sum) on
multiplicative subgroups is exactly the obstruction the
litwatch negative finding flagged, and the Line C analysis
confirms it.

The Deligne sheaf restriction to µ_k is rank ≤ 1, with
Frobenius eigenvalues ≤ p^{1/2} (Katz-style for generic H),
giving a Katz ceiling `(k+1+2√p)(1+log p)`. The empirical
data is far below this ceiling (typical ratio < 0.1), so
the bound is correct but loose; **the bound does not save
a power of p**. A refined statement (e.g. showing the
Newton polygon reaches slope 0 on the relevant stratum) is
the open problem; **the published machinery does not give
this refinement for µ_k**.

The Stepanov polynomial construction gives Weil on
multiplicative subgroups of size k only when k is small
(constant or p^ε); for the H³ setting relevant to BGS, the
polynomial degree tracks |H|² and the resulting bound is
exactly Weil (no power saving).

## Recommendation to the parent (Ring 2 orchestrator)

R2.4 outcome: **wall unchanged; the published
`k ≥ p^{3/7+ε}` smooth law remains the frontier; the
unconditional local law at the mean-spacing scale remains
OPEN.**

R2.5 outcome: **moot** — no subagent produced a
calibrator-passing `[CONJECTURED]` claim with a runnable
discriminator, so no discriminator is run.

The next research directions (not in this run) are:
1. Linn 2024 GL_3 Kloosterman 1/3+ε saving (arXiv:2412.04976)
   to the H³ setting: the R58 discriminator was NEGATIVE,
   but the structural machinery may still save a bounded
   power of log p. **Worth a focused follow-up run.**
2. Bourgain–Glibichuk–Konyagin (BGK, 2008) for one term
   on subgroups: gives p^ε saving; **the open question is
   whether a 2-term analogue exists** on subgroups. No
   published analogue as of 2026-08-28.
3. The norm-trace / Frobenius-structure extensions
   (arXiv:2603.18511, arXiv:2603.09252, both 2026) give
   Weil ceilings in more general settings; **neither
   produces a power-saving-in-p on µ_k**. Useful as
   citable cross-references for the B-line.
