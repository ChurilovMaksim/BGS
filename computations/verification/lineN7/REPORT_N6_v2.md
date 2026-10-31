# REPORT_N6 v2: Line N6 with referee fixes N6-F1 … N6-F9 applied

*Written in N7. Asia/Yekaterinburg (UTC+5).*
- The referee report is `/workspace/audit/lineN6/REPORT.md`: N5 v2 READY; N6 READY-after-fixes, as a conditional theorem.
- N6 originals are untouched: REPORT_N6.md, code, logs, SHA256_N6.txt.
- This file lists the corrected statements. Everything in REPORT_N6.md not mentioned here stands.
- New inputs come from N7 (`/workspace/bgs-lineN/N7`, see REPORT_N7.md).

Labels:
- [P]: proved.
- [P-sketch]: argument complete in outline, details not written out.
- [CA]: computer-assisted, rigorous.
- [N]: numerics without error control.
- [H]: heuristic.

## Fixes

### N6-F1 (labels)
**Theorem R♯** is [P mod Ω♯, Prop X (P-sketch), the [CA] certificate n_cert, TRACE-199/213, and the (±2,16) rate].
- The pattern-lemma part of Prop X is now [P] (N6-F2 below).
- What keeps Prop X at [P-sketch]:
  - other-sector absorption;
  - the derivation of the η terms, in particular the use of sup_n‖R^n‖ ≤ R₂′ = 3224.8 on the Line F remainder in the collapse term coll.
- The (±2,16) rate input is now [CA] (F6 below).

### N6-F2 (pattern lemma) — now [P]
See REPORT_N7 §2, Lemma P / P′.
- **Setup.** p = 2k+1, q = h_p. Let γ = x_{k+1} + y_k√2 = (ε^{k+1} − ε′^k)/√2, so N(γ) = h_p (Binet), and 2q = ε^p − ε^{−p}.
- **Exact identity.** For every e ∈ O and every i ∈ Z:
  λ^i·eγ/(8q) = eε^{2i−k}/(4√2) + e[ε^{2i−3k−1} − (−1)^k ε^{2i−k}]/(8√2 q).
  - The first term lies in (1/(4√2))O.
  - Its class mod O^∨ is constant in i, because λ ≡ 1 mod 2O.
- **The family case** e = 2 (x = ¼ + γ/(4q)) gives exact closed forms for τ_i − ½:
  - two windows per period;
  - one A core (±a, a = ε^{−1}/(2√2) = (2−√2)/4) and one B core (b = 1/(2√2) = √2/4) per period;
  - geometric tails with errors O(λ^{−k}).
- **Exact checks:**
  - the formulas match the exact integer twists mod 1 to 1e-167 … 1e-390 for p = 5 … 163 (`N7/logs/b_pattern.out`);
  - general e: `N7/logs/g_patgen.out`;
  - the referee independently checked up to p = 1901.
- **Contamination bound.** The bound 2bλ^{−w}λ/(λ−1) used in q_propx is conservative: the exact tails are ±aλ^{−|j|} / ±bλ^{−|j|} with error ≤ |e|λ^{−k}.

### N6-F3 (constants)
- G_b ≤ **3.906e8**.
- E(290) = **1.4311e-4**. Use this value throughout; it replaces the 1.43e-4 / 1.44e-4 figures.
- The margin against Re w*_lo/2 = 1.44475e-4 is **below 1%**. Any widening of the w* box breaks p₀ = 1165.
- p₀ = 1163 is also admissible.

### N6-F4 (rounding)
- The (±2,16) relaxed target is μ*²/(1.6677·λ^{1/6}) = **1.639991**. Use 1.6399, not 1.640; the 16V margin is 1.1248.
- *Superseded anyway by F6:* with the N7 certificate |μ₁₆| ≤ 1.635413, the (±2,16) members no longer need a per-level target at all.

### N6-F5 (composite isotropic weight) — corrected here
- For composite h_p the isotropic weight is n_{h_p} = Π(q_i − 2), not h_p − 2.
- **The referee's loss bound 4/(2p−1) assumes ω(h_p) ≤ 2, which is not justified.** In general:
  Π(1 − 2/q_i) ≥ 1 − 2ω(h_p)/(2p−1), with q_i ≥ 2p−1 and ω(h_p) ≤ ln h_p/ln(2p−1) ≤ p·ln ε/ln(2p−1).
  This gives a worst-case loss ≤ 11.4% at p = 1165, decreasing slowly in p.
- Hence **F_m ≥ 2.06e-3·p|Z₈|²/h_p** in the worst case: 2.3344e-3·(1 − 0.1138) = 2.0689e-3.
- With ω(h_p) ≤ 2 the bound is 2.330e-3.
- The margin over −4m (referee: 10^185.6) is unaffected in any material way.

### N6-F6 (hidden thresholds)
**(i) |Z_(±2,16)|, explicit, [CA]** (`N7/code/a_dom16.py`, `N7/code/d_Z16.py`):
- J3's `rig_spec.py` was re-run in 'dom' mode on the 8 untwisted V factors whose J3 rest certificate was only R = 1.6677.
- For all 8 (reps 0, 2, 9, 12, 16, 21, 24, 27): the dominant eigenvalue satisfies |μ₁₆| ∈ [1.59541, 1.63542]; the complement radius is < 0.95; F_R1 ≤ 6.11e-7 and F_R2 ≤ 1.58e-7.
- All other factors keep the J3 rest certificates (R ≤ 0.9298).
- Result: **|Z_(±2,16)(m)| ≤ C₁₆·1.6355^m with C₁₆ = 2.273e5**, for every m and every case. The read-out is J3 assemble16 / TRACE-226 L16.
- Hence **Σ_ρ|Z_ρ|² ≤ 4|Z₈|² for all m ≥ 51** (m₁ = 51), using TRACE-199 |Z₈| ≥ ½(1−λ^{−m})(1.9154712^m − 3012.3).
- The numerics (`N7/logs/h_rho16.out`) agree: the growth of |Z₁₆| is 1.6154 per step, against the certified upper bound 1.6355.

**(ii) Theorem W/W⁺: dropped from the inventory** (see also F8). With c_W = 10^{−25.62} the Weil range is empty for every p that matters, and W⁺ is conditional on OP. Those levels go to (b), so no threshold p₁ is needed.

**Threshold.** The theorem reads p ≥ 1165 (Prop X) and m ≥ 51. Both hold for p ≥ 1165.

### N6-F7 (inventory gap)
- At composite h_p (and at e·h_p) there are β that are isotropic, or 0, mod some q_i ∣ h_p and units mod the others.
- These **mixed classes are assigned to (b′)**, a sub-item of (b): they are partially isotropic points at a proper-divisor level, lifted by a unit component.
- [N] magnitudes at p = 11 (h = 23·353) and p = 13 (h = 79·599) are in REPORT_N7 §5.

### N6-F8
Item 3 ("Weil-range prime levels") currently removes nothing. It is dropped; see F6(ii).

### N6-F9 (certificate hygiene)
- **Key intervals, with endpoints** (outward-rounded from n_cert boxes; reproduced by the referee's `ref_wstar`):
  - Re w* ∈ [2.8896e-4, 3.9820e-4]
  - Im w* ∈ [−2.520e-4, −1.396e-4]
  - arg w* ∈ [−0.7172, −0.3372] for (−2,8), conjugate for (2,8)
  - c* ∈ [3.447e-4, 4.443e-4]; the referee's corner bound is [3.572e-4, 4.370e-4]
- rank(Π_A) = 1 inside Γ = {|z−s| = 0.6} rests on the **Line F spectral-gap certificate** `certV_eta2_a4_tight`: complement radius Yp_root = 0.76905, F_R1 = 0.2432 < 1.
- The linear algebra is **float BLAS with a-priori rounding bounds γ_n|A||B|**, not ball arithmetic. Scalar bookkeeping is in arb. This is [CA] in the Rump/Higham sense used throughout Lines F–N.

## Corrected Ω♯ inventory (supersedes N6 §5 list)
1. **Closed:**
   - Unit β at h_p and 7h_p: Theorem C′ [P+CA], for squarefree h_p; prime-power factors are routed to (b′).
   - d = 7: [CA], Line I/J.
   - d > L*: Dev floor [P].
   - **All (±2,16) members at all levels: closed for p ≥ 339 [CA+P].** This is new in N7: the Dev floor plus Robin's bound σ(n)/n ≤ e^γ ln ln n + 0.6483/ln ln n, together with C₁₆ and 1.6355 < √2.7350 = 1.6538 (REPORT_N7 §1).
2. **Open:**
   - **(a)** non-family isotropic β at h_p and at its inherited levels (focus of N7);
   - **(b)** all β at levels ≤ L* outside item 1 (proper divisors of h_p, K_p levels, mixed levels), together with **(b′)** the mixed iso/unit classes at composite h_p.
