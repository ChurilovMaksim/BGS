# REPORT_N6: a refutation program for frozen R′ along m = 3p (Line N6)

*2026-10-31, about 21:20 Asia/Yekaterinburg (UTC+5).*
- Directory: `/workspace/bgs-lineN/N6`. Running log: NOTES_N6.md.
- Nothing pushed. N2–N5 originals are untouched; the only addition there is the new file N5/REPORT_N5_v2.md, which applies the referee fixes F1–F10.

Labels:
- [P]: proved.
- [P-sketch]: argument complete in outline, details not written out.
- [CA]: computer-assisted, rigorous (arb or interval arithmetic).
- [N]: numerics without error control.
- [H]: heuristic.
- "mod X" means conditional on input X.

## 0. Summary
| # | Result | Label |
|---|---|---|
| 1 | **Positivity lemma.** W′_m ≥ −RMT_m + φ⁻¹ Σ_{ρ, d incl} Lin_d(ρ), where Lin_d(ρ) = (2/d²) Re( Z̄_ρ Σ_{β≠0} κ_d(Nβ) Ẑ(β) ) and κ_d(u) = Σ_{t∈S_d} e(t̄u/d). Also Dev_d ≥ −n_d\|Z_ρ\|²/d² trivially. | [P] |
| 2 | **Sign.** Ẑ(½,…,½) = −Z_ρ. The 16D = 1 family has ratio w* = −(r_A r_B)³ with **Re w* > 0**. | [P] (shift identity) + [N] (p = 19, 29, 59) |
| 3 | **[CA] constants, Line F certified representation (sector 4).** r_A = 0.175180 + 0.168374i ± 0.00323 and r_B = −0.178594 + 0.243641i ± 0.00321 (boxes). c* = \|r_A r_B\|³ ∈ [3.447e-4, 4.443e-4]. Re w* ∈ [2.890e-4, 3.982e-4]. arg w* ∈ [−0.717, −0.337] for (−2,8), conjugate for (2,8). | [CA] |
| 4 | **Prop X with explicit constants.** For p ≥ p₀ = 1165, Re(Ẑ_β/Z_ρ) ≥ Re w* − 1.44e-4 ≥ 1.45e-4 for every β in the family (4p points per ρ). | [P mod Line F certificates and the pattern lemma (P-sketch)] |
| 5 | **Bookkeeping.** The family lies in Dev (the frozen main term is β = 0 only). Its inherited copies at levels e·h_p are also ≥ 0. Nothing can cancel it except non-family terms. | [P] |
| 6 | **Size.** P_m/m (level h_p only, both (±2,8), φ ≤ h): 1.16 (m=51), 2.44 (57), 10.9 (69), 103 (87), 8.7e4 (141), 1.4e10 (237). Floor −RMT/m = −4; D7/m ≈ 0.05–0.3. | [N] |
| 7 | **Conditional theorem (§5).** If Ω♯ holds (a one-sided bound at the relaxed targets 1.42785 / 1.640 on the non-family Lin terms at levels d ≤ L*_m), then W′_m/m → +∞ along m = 3p, p ≥ 1165, and **frozen R′ is false**. | [P mod Ω♯ + item 4 inputs] |
| 8 | **Status of Ω♯ pieces.** Proved: unit points at h_p and 7h_p (Theorem C′), d = 7 ([CA] Line I/J), Weil-range prime levels (Theorem W/W⁺, as registered), and d > L* (trivial floor). **Open:** non-family isotropic points (index-loss barrier), and unit points at proper divisors of composite h_p, at K_p/ord-3p prime levels and at mixed levels outside the Weil range. | mixed, see §5 |
| 9 | **Squarefree.** Not needed for the driver (items 1–5). Prime powers q^a ∣ h_p only add terms of the open type (8): Ramanujan weights vanish off q ∣ Nβ. So the theorem can be stated for all large p, with Ω♯ including those terms. | [P] (reduction) |

## 1. Positivity lemma [P]
- Setup:
  - Member sums at level d (odd d ∣ h, TRACE-212/204): Z_t = (G_d(t)/d²) Σ_β e(t̄Nβ/d) Ẑ(β).
  - E_t := Z_t − (G_d(t)/d²) Z_ρ.
  - \|G_d(t)\|² = d² on the members (TRACE-212).
- Expansion: Dev_d(ρ) = Σ_t (\|Z_t\|² − \|Z_ρ\|²/d²) = d⁻² Σ_t ( 2Re(Z̄_ρ E′_t) + \|E′_t\|² ), with E′_t = Σ_{β≠0} e(t̄Nβ/d) Ẑ(β).
- Dropping the squares gives the inequality Dev_d ≥ Lin_d.
- Summing over t gives the weights κ_d. For β isotropic mod d (Nβ ≡ 0), κ_d = n_d.
- Non-resonant terms satisfy \|Z\|² − RMT ≥ −RMT.
- Combined with the TRACE-213 exact reduction W′ = φ⁻¹Σ_nonres(\|Z\|² − RMT) + φ⁻¹ΣDev, this gives row 1. ∎
- Cauchy–Schwarz refinement at level h_p: Dev ≥ (n\|Z\|²/d²)(\|1+X+Y\|² − 1). It is not needed below.

## 2. Sign [P] and the family term
- **Sign.** e(Σ n_i/2) is the shift ν₀ ↦ ν₀ + h. The sector coefficients satisfy c_{a+4} = −c_a (Line F gauge: L_{a,τ} = L_{0,τ+a/8}). Hence Ẑ(½…½) = −Z_ρ [P].
- **Numerical checks.** `g_sign.py`: the ratio is −1 to 1e-15 [N]. The family ratio is 3.43578e-4 ± 1.95798e-4i [N]. This matches w* = −(r_A r_B)³ from `l_lineF_r.py` (float) and `n_cert.py` ([CA], row 3).
- **Isotropic sum at level h_p:** X = Σ_{β iso≠0} Ẑ_β/Z_ρ ≈ 4p(w* + c₀), where c₀ ≈ 2.987e-5 − 6.60e-6i is the near-0 family [N]. Everything else is < 0.6%.

| p | X (exact or screened) | method |
|---|---|---|
| 11 | 0.016493 + 0.008231i | f_iso (full CRT orbits) |
| 13 | 0.019429 + 0.009762i | f_iso |
| 19 | 0.028554 + 0.014250i | i_screen (2733 orbits; slow ≥ 8/13 captures 99.95%) |

- Exact Dev/Lin at p = 5 and 7: `j_exactdev`, consistent with Lin.

## 3. [CA] certificate and the explicit Prop X
- **[CA] `n_cert.py`.** The setup is Line F certV_eta2_a4_tight, rebuilt verbatim in `cert_core.py`: dim 495, Δ = 1.856e-9, ‖X‖ = 6.1592, trace norm 730.142, N₁ = 573.594.
- **Twist independence.** The perturbation Pert = 1.901e-9 depends only on \|w(n)\|, so it is twist-independent.
- **Comparison operator** T = [[A,0],[X,0]]. Resolvent on Γ = {\|z−s\| = 0.6}: R_A ≤ 27.41, R_T ≤ 156.5. ‖Π − Π_T‖ ≤ 2.79e-5, ‖Π‖ ≤ 21.97, C_pow ≤ 3246.8.
- **Excursion cores** (n = 38, 37). Each is the product of the exact twisted operators.
  - Sub-product bound G ≤ Ĝ/(1 − Δmax) = 37.01.
  - Errors: projection 2.8e-6, perturbation 3.2e-3, tail (KK = 18) 2.4e-5.
  - Float BLAS with a-priori bounds γ_n\|A\|\|B\|.
  - Result: the boxes of row 3.
- **Prop X (explicit). Statement.** Let ρ = (±2,8), m = 3p, and β in the 16D = 1 family.
  - Then Ẑ_β/Z_ρ = w*·(1 + θ) + ε_other, with \|w*θ\| ≤ E(w) (`q_propx.py`, arb).
  - Constants: E(w) = 6(T₁G_b + 1)·η(w)·(‖Π‖r_max + η)⁵, with G_b ≤ 3.905e8 and T₁ ≤ 381.2.
  - η(w) collects four errors:
    - contamination from the other excursions, ≤ 2bλ^{−w}λ/(λ−1) per step via Gronwall;
    - rank-one collapse, 2G_b²R₂′μ^{−⌊w/2⌋} with R₂′ = 3224.8;
    - outer-step replacement;
    - truncation of the cores.
  - The half-window satisfies w ≥ ⌊((p−1)/2 − 1)/2⌋ (Lemma H: two windows per period, six blocks per m).
  - Result: E ≤ 1.43e-4 ≤ Re w*_lo/2 at w₀ = 290, so **p₀ = 1165**.
- **Inputs.**
  - (a) The Line F certificates (sector 4 here). Other sectors: certV_eta2_a0/a2/a6 and certE_eta2 all certify, with ‖A′‖^{1/2} ≤ 0.932 and R ≤ 102.3, so their contributions are ≤ 0.932^m·poly relative to sector 4 and are absorbed for p ≥ p₀ [P-sketch: same bookkeeping as sector 4].
  - (b) The **pattern lemma**: on each period the twist sequence of a family point is the excursion pattern a = (2−√2)/4, b = √2/4 (window values 0 or ½) up to O(λ^{−dist}). Status: [P-sketch] (Lemma H plus the expansion of Tr(λ^iβ)/h_p) and [N] (checked p ≤ 59).
  - (c) The TRACE-197/207 twisted identity linking Ẑ to the Line F operator.
- **Uniformity over the family.** Ẑ(λβ) = Ẑ(−β) = Ẑ(β̄) = Ẑ(β) [P] (cyclic shift, P(n) parity, reversal; checked numerically in `t_sym.py`). So all 4p family points share the bound.
- **Consequence [P mod inputs].** For p ≥ 1165:
  - F_m := Σ_{ρ=(±2,8)} Lin^{fam}_{h_p}(ρ) ≥ 2·(2(h_p−2)/h_p²)·\|Z₈\|²·4p·(Re w*_lo − E) ≥ 2.3e-3·p\|Z₈\|²/h_p.
  - TRACE-199 [CA] gives \|Z₈\| ≥ ½(1−λ^{−m})(1.9154712^m − 3012.3).
  - Hence, in the TRACE-206 φ-normalisation, F_m/(mφ) grows like (μ*²λ^{−1/6}/λ^{1/2})^m/m = 1.1330^m/m → ∞ (this matches the referee's ~1.133^m).
  - Inherited copies at e·h_p are ≥ 0 (κ = n_d on them), so F_m is a lower bound for the whole family contribution.

## 4. Numerics: P_m/m (level h_p, both (±2,8)) versus D7 and the floor [N]
| p | m | Re X | P_m/m | D7/m |
|---|---|---|---|---|
| 13 | 39 | 0.0194 | 0.259 | 0.052 |
| 17 | 51 | 0.0254 | 1.155 | 0.050 |
| 19 | 57 | 0.0284 | 2.44 | 0.050 |
| 23 | 69 | 0.0344 | 10.9 | 0.051 |
| 29 | 87 | 0.0433 | 103 | 0.056 |
| 41 | 123 | 0.0613 | 9.2e3 | 0.077 |
| 47 | 141 | 0.0702 | 8.7e4 | 0.093 |
| 79 | 237 | 0.118 | 1.4e10 | 0.319 |

- These figures are consistent with the referee's (W′/m from the h_p levels: +2.95 at m = 57, +125 at 87, +1.07e5 at 141; the referee includes inherited levels and the exact φ).
- The family overtakes the floor of −4 at p ≈ 21 [N].

## 5. Conditional refutation theorem and Ω♯
- **Setup.** L*_m := 4·τ(h_m)·h_p/(δ·2.3e-3·p).
- **Trivial floor [P].** Σ_ρ Σ_{d∣h_m, d>L*} n_d\|Z_ρ\|²/d² ≤ Σ_ρ\|Z_ρ\|²·τ(h_m)/L* ≤ δF_m/… ≤ δ·F_m (using Σ_ρ\|Z_ρ\|² ≤ 4\|Z₈\|² for large m).
- **Hypothesis Ω♯_m.** Σ_ρ Σ_{d∣h_m, d ≤ L*} \|Lin♯_d(ρ)\| ≤ (1 − 2δ)·F_m.
  - Lin♯ means Lin with the family β and their inherited copies removed.
  - Equivalently, per piece, at the relaxed per-level rates: < 1.42785 for (±2,8), and < 1.640 = μ*²/(1.6677·λ^{1/6}) for (±2,16), with subexponential constants.
- **Theorem R♯ [P mod Ω♯, the §3 inputs (a)–(c), and TRACE-213].** For p ≥ 1165 with Ω♯_{3p}: W′_{3p} ≥ −4m + δF_m/φ. This tends to +∞ faster than any power of m. If Ω♯ holds for infinitely many p, then **frozen R′ (W′_m = o(m), or the TRACE-206 bound) is false.**
- **Status of the pieces of Ω♯:**
  1. **Non-isotropic (unit) β at d = h_p and 7h_p: [P+CA]** via Theorem C′ (N2/N3), assuming h_p squarefree (see 6). Rates are 1.27438 (8V), 0.80266 (8E), 1.45789 (16V) and 0.77812 (16E), against targets 1.42785 / 1.640. All meet them; 16V against 1.640 has margin 1.125. At 7h_p the spacing factor is 7 (N5-F7).
  2. **d = 7: [CA]** (Line I/J; dominant \|μ\| ≤ 1.2837144 < 1.42785; (±2,16) level-7 members per TRACE-227). Constants come from the TRACE-217/221 certificates.
  3. **Prime q (and 7q) with q ≤ max(c_W p², c_N p^{7/3}):** Theorem W/W⁺ (Line L / N1). Per-level budget ε_F; its status is as registered (TRACE-244/245, conditional on OP).
  4. **d > L*:** trivial floor [P].
  5. **OPEN (a): non-family isotropic β at h_p and at its inherited levels.** [N]: < 0.6% of F_m for p ≤ 19 (row 2); referee Monte Carlo: generic ≤ 5e-12 each. A proof needs an isotropic-coset version of Theorem C′; this is the index-loss barrier, since the isotropic line has density 2/q.
  6. **OPEN (b): all β at levels d ≤ L* outside 1–3.** These are proper divisors of composite h_p beyond the Weil range, K_p/ord-3p prime factors of h_m/h_p = 4h_p² + 3, and mixed composites. Same barrier: Theorem C′ averages over G_{h_p}, and a sub-level d loses index (h_p/d)². [N]: referee mixed classes ≤ 4.4e-12 relative; N6 `o_levels` p = 5 only (the run was interrupted).
- **What was attempted on 5 and 6.**
  - The positivity lemma removes every two-sided requirement and the Prop K2 range: only upper bounds on \|Lin♯\| are needed, at the relaxed rate.
  - For 5, the family-free isotropic sum is a T-invariant coset average. The N5 §3 Bowen-ball argument bounds it by the level-h_p rate **times the index loss q/2**. That is enough only if log q/m < log(1.42785/1.27438)/1 — it fails, since q ≈ λ^p gives a loss of λ^{1/3} per step.
  - So 5 and 6 remain genuine open estimates. **No proof is claimed.**

## 6. Squarefree [P reduction]
- **The driver needs no squarefree hypothesis.**
  - I2′/G3 holds for every odd d.
  - κ_d(0) = n_d.
  - Every q ∣ h_p splits (2 is a square mod q, because q ≡ ±1 mod 8), so a cyclic ideal 𝔞 of norm h_p exists. The family β = (h_p + γ)/4 with (γ) = 𝔞 is defined.
  - Lemma H and the pattern lemma do not use squarefreeness.
- **Where it enters.** For q^a ∥ h_p, a ≥ 2, the weight factor at q is the Ramanujan sum c_{q^a}(Nβ): it is 0 unless q^{a−1} ∣ Nβ, and \|c\| ≤ q^{a−1} on the partially isotropic shell.
  - Unit points therefore get weight **0** (better than in the squarefree case).
  - Partially isotropic points are cosets β₀ + q^{a−1}O, which is exactly the proper-divisor/isotropic type of OPEN (a)/(b).
- **Consequence.** Theorem R♯ is stated for **all** p ≥ 1165, with Ω♯ including those terms. Infinitely many squarefree h_p are **not needed**, and the question is folded into the open estimates 5 and 6.

## 7. Ledger and artefacts
- **[P]:**
  - positivity lemma;
  - sign identity;
  - bookkeeping;
  - symmetries;
  - trivial floor;
  - squarefree reduction;
  - Theorem R♯ as an implication.
- **[CA]:**
  - r_A, r_B, c*, Re w* and arg w* (`n_cert.py`, logs/n_cert.json and n_cert.out; arb at 128 bits plus rigorous float-BLAS bounds);
  - p₀ arithmetic (`q_propx.py`, logs/q_propx.json).
- **[P-sketch]:** pattern lemma; the other-sector bookkeeping in Prop X.
- **[N]:** X tables; P_m/m; near-0 family; screened totals.
- **Not done:** `h_rho16.py` (\|Z_(2,16)\| growth check) was not run; the target 1.640 uses the N2 rate 1.6677. `o_levels.py` ran only for p = 5.
- **Withdrawn (via N5 v2):** N4 §3.3; N5 v1 §0 rows 3 and 5 and §4.
- **Hashes:** SHA256_N6.txt (all of code/, logs/, NOTES_N6.md, REPORT_N6.md), with a self-hash in SHA256_N6.txt.sha256.
