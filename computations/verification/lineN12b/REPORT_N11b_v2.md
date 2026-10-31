# REPORT_N11b_v2 — minor fixes from referee /workspace/audit/lineN11b/REPORT.md (F1–F5) and N12-F3
Written by Line N12b, 2026-11-01 (UTC+5). This supersedes the indicated sentences of N11b/REPORT_N11b.md; that file is unchanged.

- **F1.** The "+9.4e-5 at Γ = T′ (marginal!)" came from rounding μ\* and T′.
  - Exactly, ln ε + 3 ln(T′/μ\*) = 0, because T′ = μ\*ε^{−1/3}.
  - The mixed-class exponent is 3 ln(Γ/T′) < 0 for every Γ < T′.
  - The meaningful comparison is this margin plus the gas term against the budget growth ln(1+ReΛ_lo) = 6.236e-4 per p.
  - "Marginal" is withdrawn.
- **F2.** The mixed-point count is ≈ 2h·q_u (± and conjugates), not h·q_u. This is a factor 2, absorbed in constants.
  - "k = O(1) stays per period for unit components" is labelled **[P-sketch]**.
- **F3.** The C′ bound for all unit points at squarefree h_p is |Y_unit| ≤ (2/(h−2))·e^{o(p)}·h²(1.2744/μ\*)^{3p}.
  - The prefactor is e^{o(p)}, from Theorem C′ (N3: "for all p ≥ p₀, p₀ effective, not computed").
  - The exponent −0.341 per p therefore holds for p ≥ p₀. An explicit C′ constant/p₀ remains open.
  - The exact p = 7 value (0.016) is consistent with the numeric bound 0.092.
- **F4.** At p ≤ 7 the gas model is only qualitative (2× off at p = 5: 0.0047 vs 0.0099). The evidence at p = 5, 7 is the **exact** full sums: |1+X+Y| = 1.014484 and 1.011808, independently confirmed by the referee. Y_U/X ~ e^{−0.880p} is [N] asymptotics.
- **F5.** For squarefree h_p, the unit-gas analysis (Λ_U, certified activities) is a **cross-check**, not a load-bearing input: C′ already gives an exponentially small unit Y.
  - The load-bearing open item is the mixed class at composite h_p. It stays **conditional on Γ_out < T′** (G\*), together with the explicit C′ constant and a rigorous k = O(1)-stays lemma.
- **N12-F3 / N12b.**
  - The N12 stepnorm table, Lip_H and the quadratic constants are [N]. A rigorous D1 needs interval step bounds.
  - N12b found that the cone certificate is infeasible at k ≤ 3, and that G\*_gas at θ = 1/8 is inconsistent (REPORT_N12b §2–§3).
  - The mixed-class bound therefore rests on an open item that probably has to be reformulated as a restricted-pressure bound (REPORT_N12b §4).
