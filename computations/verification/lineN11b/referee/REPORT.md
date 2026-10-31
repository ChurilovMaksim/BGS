# Referee report — Line N11b (unit/mixed points, REPORT_N11b.md + REPORT_N9b_v2.md)
Referee: Grok Bot · completed 2026-11-01 (Asia/Yekaterinburg, UTC+5) · SHA self-hash a95f9227…acfa matches, all listed files OK · nothing modified/pushed.
Lean items are in /workspace/audit/lineN12/lean/LineN12Arith.lean (built, exit 0, no sorry/native_decide).

## Verdict: **READY after minor fixes** (F1–F5, none affecting conclusions)
The κ bookkeeping and the exact small-p sums are independently confirmed. The mixed-class bound is correctly labelled as conditional on Γ_out < T′.

## Independent checks
**Exact full sums p = 5, 7.** Own code: `code/ref_exactXY.py`. It uses its own twist map τ_i = 2Re(λⁱβ)/d mod 1 and its own κ(u) = Σ_{t∈S} e(t̄u/d), with S from the N6 rule. The reduction uses λ-orbits only.

| | X | Y | \|1+X+Y\| | \|1+X\| | CS lower | Dev/main | max\|κ\| | Σ\|r_unit\| |
|---|---|---|---|---|---|---|---|---|
| p=5 (d=41, n=39, 337 orbits) | 0.0035328+0.0024964i | 0.0109436+0.0013749i | 1.014484 | 1.003536 | 0.029177 | 0.153184 | 1.99413 | 1.08654 |
| p=7 (d=239, n=237, 8161 orbits) | 0.0107238+0.0057607i | 0.0010658+0.0003282i | 1.011808 | 1.010740 | 0.023755 | 0.281084 | 1.99983 | 1.89837 |

- Both rows agree with N11b to all printed digits.
- Invariance under β→−β and complex conjugation holds to ≤ 3e-19 relative. So N11b's ± and conjugation reduction is valid.

**κ bookkeeping.** For prime d, S is the set of all nonzero residues minus one, so n = d−2.
- κ(u) = −1 − e(·), hence |κ| ≤ 2 (Lean: `kappa_le_two`).
- The unit/mixed weight is therefore κ(Nβ)/n ≤ 2/(d−2), e.g. 2/39 at p=5 and 2/237 at p=7.
- The same sum as X with weight κ(Nβ)/n is confirmed: it is the structure of my independent code.

**Exponents (Lean).**
- C′ bulk ratio per p: ε(1.2744/μ*)³ < 0.7111 ≈ e^{−0.341} ✓.
- Unit-gas ratio: |1+Λ+Λ_U| / (ε|1+Λ|) < 0.4148 ≈ e^{−0.880} ✓.
- λ⁵ − 1 = 2·41·ε⁵ ✓.

## Findings
**N11b-F1 (minor): the "+9.4e-5 at Γ = T′ (marginal!)" is a rounding artifact.** It comes from rounding μ* (1.9154732 vs 1.9154712) and T′ (1.4279). Exactly, ln ε + 3ln(T′/μ*) = 0 by the definition T′ = μ*ε^{−1/3}. The meaningful comparison is the margin against the budget growth of 6.236e-4 per p. Remove "marginal" or restate it that way.

**N11b-F2 (minor): mixed-point count.** The count is ≈ 2h·q_u, not h·q_u, because of ± signs/conjugates. This is a factor 2 and immaterial. The "k = O(1) stays" assumption is [P-sketch]; label it.

**N11b-F3 (minor): the C′ bound needs its prefactor.**
- The bound (2/n)h²(1.2744/μ*)^{3p} uses C′ as a *sum* bound, with the constant prefactor dropped ("mod C′ inputs").
- It is consistent with the exact p=7 value (0.092 ≥ 0.016) and with the US points.
- State the constant, or the p from which it is absorbed.

**N11b-F4 (minor): the model is crude at small p.**
- At p=5 the gas model for Y (κ ≈ −1 central value) differs by about 2× from the exact κ-weighted value (0.0047 vs 0.0099).
- Do not cite the model at p ≤ 7 as quantitative. The exact sums are the evidence there.
- The weighted Y_U/X ~ e^{−0.880p} is [N] asymptotics and is fine as such.

**N11b-F5 (scope).**
- For squarefree h_p, the unit-gas analysis is redundant given C′. Say so: it is a cross-check, not a load-bearing input.
- Λ_U = 1.0054e-3 − 1.8344e-3i is correctly [N], and the |w| for ±ε^{±1} are correctly [CA].
- The mixed-class bound stays **conditional on Γ_out < T′**, and this must remain in the remaining-items list.

## REPORT_N9b_v2 (fixes against my N11 report's N9b-F#)
- F2, F3 and F6 (required) are applied ✓.
- The NOTES_N9b timestamp fix and erratum were edited in N9b's directory by N11b. This is disclosed, and the original is preserved at N11b/logs/NOTES_N9b.orig.md, so it is acceptable.
- The invented timestamps in NOTES_N10b are disclosed ✓.
- The claim that C2′ is superseded via e^{o(p)} rank-p divisor sums cites N10b §1. I did not re-verify it, so it is to be checked in a later round.

## Remaining (N11b part of the refutation chain)
- An unconditional bound on Γ_out < T′ for the mixed class.
- An explicit C′ constant.
- A rigorous treatment of k = O(1) stays.
- Everything else is as listed in /workspace/audit/lineN12/REPORT.md §Remaining.
