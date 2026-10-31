# REPORT N11b — unit-point gas inside Y (threat to the refutation?), N9b-F2/F3/F6, N11-F6
Labels: [P] · [P-sketch] · [CA] arb · [CA*] float+margin · [N] · [H]. Nothing pushed.
Earlier lines are untouched except NOTES_N9b.md (timestamp fix + erratum, as requested) and the new N9b/SHA256_N9b_v2.txt.
Dates are Asia/Yekaterinburg (UTC+5), 2026-10-31 23:35 → 2026-11-01, from `date`.

## 0. Answer
**The refutation survives.**
- **Unit points are in the same CS bracket as X.** Dev_h ≥ (n|Z|²/h²)(|1+X+Y|²−1) with Y = (1/n)Σ_{non-iso β} κ(Nβ)Ẑ(β)/Z, but each point carries the weight κ(Nβ)/n:
  - |κ| ≤ 2 at prime h_p (exact max 1.994 / 1.9998 at p = 5 / 7);
  - |κ| ≤ 2^{ω} for unit-unit points (3.96 at p = 11);
  - versus κ(0)/n = 1 for iso points.
- **The unit points do form a gas** [N, CA for the activities]. Its per-site activity is Λ_U = 1.0054e-3 − 1.8344e-3i (|Λ_U| = 2.09e-3, A_U = Σ|r| = 3.96e-3; identical at p = 29, 47, 59). Unweighted, it grows like (1+Λ+Λ_U)^p, faster than the iso gas because Re Λ_U > Re Λ.
- **The weight 2/(h_p−2) ≈ 4ε^{−p} kills that gas.** Y_U/X ~ e^{−0.880 p}.
- **Explicit growth exponent.**
  - |1+X+Y| ≥ 2(1+ReΛ_lo)^p − 1 − |X_tail| − |Y|, i.e. growth **ln(1+6.238e-4) = 6.236e-4 per p** (unchanged).
  - Error exponents per p:
    - unit gas −0.880 [N model; activities CA];
    - all unit points at squarefree h_p, via C′: −0.341 [P+CA mod C′ inputs];
    - mixed classes at composite h_p: 3 ln(Γ/T′) [P-sketch, conditional on G\*_gas(Γ)]. This is −0.146 at Γ = 1.36 and −0.369 at 1.2624, but **+9.4e-5 at Γ = T′ exactly**, so mixed needs Γ_out strictly below T′.

## 1. Same sum or separate terms? (MAIN QUESTION, structural) [P, bookkeeping from N6 G3]
- Every member t ∈ S_d has Z_t = (G_d(t)/d²)Σ_β e(t̄Nβ/d)Ẑ(β). Summing over t gives:
  - the iso points with κ(0) = n;
  - every other β with κ_d(Nβ) = Σ_{t∈S} e(t̄Nβ/d).
- So **unit and mixed points are in the same sum as X**, at the same level h_p, with the same Ẑ and the same Z normalisation. They need no separate floor: they only enter through |Y| in |1+X+Y| ≥ |1+X| − |Y|.
- Their relative weight:
  - prime h_p: |κ(u≠0)| ≤ 2 (κ = −1 − e(t̄₁u/h)), so weight ≤ 2/(h_p−2);
  - composite h_p, unit at every prime: |κ| ≤ 2^{ω(h_p)};
  - **mixed** (iso mod q_i, unit mod q_u): |κ| ≈ n_{q_i}·2. This is only polynomially small, ~2/q_u, as N11-F6(c) says. Exact max at p = 11: 695/7371 = 0.094 for q_u = 23.

## 2. Unit activities and the Y-gas generating function
| type | certified (u_cert.py, n9_cert machinery, single core ζ_U = 2β/ε, p→∞) | exact Zbatch p=47 |
|---|---|---|
| ±ε^{±1} | \|w\| ∈ [1.064e-3, 1.526e-3], Re w ∈ [4.14e-4, 7.31e-4] [CA] | 5.728e-4 − 1.1842e-3i |
| 6 | \|w\| ≤ 2.81e-4 [CA] | 2.16e-4 |
| 3ε | ≤ 2.11e-4 [CA] | 1.45e-4 |
| 2ε | ≤ 1.32e-4 [CA] | 9.0e-5 |
| 1 | ≤ 9.93e-5 [CA] | 6.46e-5 |
| √2 | ≤ 6.07e-5 [CA] | 3.63e-5 |

(n9_cert's convention is the complex conjugate of Zbatch; |·| and Re agree.)

- **Gas structure** [N, p = 47, a_unit_two]: two unit bumps at gap g give r(u₁+s·u₂λ^g) → r(u₁)r(u₂). The ratio is 1.000 at g = 11, with ~0.4/step interaction. This is the same rank-one collapse as the iso gas.
- **Λ_U** (c_LambdaU.py; 102 λ-classes with |a| ≤ 6, |b| ≤ 5) = 1.005429e-3 − 1.834361e-3i [N].
  - Shell |N| = 1 dominates (1.27e-3 − 2.36e-3i); next are |N| = 36 (4.3e-4) and |N| = 9 (2.9e-4).
  - Tail beyond the box is < 1e-5 per shell for |N| ≥ 23.
  - Λ_U is stable to 1e-11 across p = 29, 47, 59.
- **Model** (e_model.py): Y_gas ≈ −(2/n)·2[(1+Λ+Λ_U)^p − (1+Λ)^p] (the κ ≈ −1 part; the phase part is bounded the same way), with |Y_gas| ≤ (4/n)[(1+|Λ|+A_U)^p − (1+|Λ|)^p].

## 3. Exact checks
| p | h_p | X (iso) | Y (all non-iso) | \|1+X+Y\| | \|1+X\| | model \|1+X+Y_gas\| | Dev/main ≥ \|1+X+Y\|²−1 |
|---|---|---|---|---|---|---|---|
| 5 | 41 (prime) | 0.003533+0.002496i | 0.010944+0.001375i | 1.01448 | 1.00354 | 1.00699 | 0.153 ≥ 0.029 ✓ |
| 7 | 239 (prime) | 0.010724+0.005761i | 0.001066+0.000328i | 1.01181 | 1.01074 | 1.01040 | 0.281 ≥ 0.024 ✓ |
| 11 | 8119 = 23·353 | 0.016493+0.008231i (N6) | see below | ≈ 1.0160 | 1.01652 | 1.01655 | — |

- **p = 5, 7** (b_exactXY.py): exact over all d² points, orbit-reduced, with exact S and κ [N].
  - At p = 5, |Y| > |X|: the bulk unit weight 2/n is 0.05. At p = 7, |Y|/|X| = 0.09 and falling.
  - Σ|r_unit| = 1.09 / 1.90 grows, but (2/n)Σ|r_unit| = 0.056 / 0.016 falls.
- **p = 11, composite** (d_mixed.py) [N]:
  - mixed iso mod 353 / unit mod 23: **exact, all 7766 orbit reps**. Y = −9.3e-7 + 4.08e-5i. The κ weight is 0.094 (polynomial), but max|r| = 4.2e-5, so the contribution is 0.2% of |X|.
  - iso mod 23 / unit mod 353: 2% sample, Y ≈ −4.6e-4 − 2.3e-4i (±~2e-4 sampling).
  - unit-unit: 0.2% sample, Y ≈ −2.0e-5. Gas points come on top, ≤ 2.2e-5 by the model.
  - Total |1+X+Y| ≈ 1.0160 vs |1+X| = 1.0165: tracks the model to 5e-4.
- **p = 29, 37, 47, 59**: a full level-h_p sum is infeasible (h_p² ≥ 4e21).

  | p | \|1+X\| | \|Y_gas\| bound | C′ bulk bound | rigorous floor 2(1+ReΛ_lo)^p − 1 |
  |---|---|---|---|---|
  | 29 | 1.044019 | 7.9e-12 | 5.1e-5 | 1.036498 |
  | 37 | 1.056369 | 8.9e-15 | 3.3e-6 | 1.046683 |
  | 47 | 1.071935 | 1.7e-18 | 1.1e-7 | 1.059486 |
  | 59 | 1.090799 | 5.7e-23 | 1.8e-9 | 1.074956 |

  The C′ bound applies to squarefree h_p; p = 37 is h = 223·37223·8761009, squarefree. Mixed classes at p = 37 have a polynomial weight ≤ 2/221 per class, handled as in §4.

## 4. Mixed classes (N11-F6(c)) [P-sketch, conditional on G\*_gas]
- Polynomial κ-suppression (~2/q_u) is compensated by exponential |r| suppression, because a unit component forbids long slow stays.
  - **Lemma S argument:** a stay of length ℓ means λ^iβ ≡ γ (mod h) with small γ; Nγ ≢ 0 (mod q_u) forces ℓ ≤ 2 log_λ(θq_u) + O(1) per stay.
  - Counting points: ≤ h·q_u. Weight ≤ 2/q_u.
  - Then |Y_mixed| ≲ 2·C^k·q_u^{2k·log_λ(μ\*/Γ)}·(ε(Γ/μ\*)³)^p, where k = number of stays per period. The exponent is ln ε + 3 ln(Γ/μ\*) = 3 ln(Γ/T′) because T′ = μ\*ε^{−1/3}.
- **Data:** at p = 11, q_u = 23, the exact mixed sum is 0.2% of X.
- **Status:** the referee's "Y ≤ poly(p)" is now replaced by an explicit exponent. It remains conditional on G\*_gas(Γ < T′) and on k = O(1) stays per period for unit components [P-sketch].

## 5. N9b fixes → REPORT_N9b_v2.md (this directory)
- **F2:**
  - G\*_gas(Γ, θ, L) is stated with stays of length ≥ L.
  - z(L) = C²C_θ q^L[(1+L)/(1−q) + q/(1−q)²] with q = μ\*/(λΓ), and the requirement is z < 2e-4.
  - L ≥ 14–16 (C = 57) or L ≥ 20–22 (C = 3246.8).
  - **With the N12 adapted norm: L ≥ 9–14.**
  - The excursion-only claim is withdrawn; it is not needed in modulus form.
- **F3:**
  - Γ_per is a lower bound, so Γ_out(1/8) ∈ [1.262, ~1.36] [N]. The margin is not established.
  - The a_per box is OPEN (dist ≥ θ counts as outside). Closed 1/16: n = 4 drops 1.4296 → 1.2407; Γ_per(1/16, closed, n ≤ 8) ∈ [1.2837, 1.3646].
  - Recommendation: closed, θ = 1/8.
- **F6:**
  - NOTES_N9b clock labels were invented. Headings are relabelled with stat evidence (22:16:06 first code … 22:52:29 last log … 23:02:11 REPORT/NOTES), and an ERRATUM with a real `date` was appended. The original is kept in logs/NOTES_N9b.orig.md. New manifest: N9b/SHA256_N9b_v2.txt.
  - **NOTES_N10b has the same defect** (labels to 23:55; files written 23:16:30). It is disclosed here, but the file is not edited.

## 6. D1 with the N12 adapted norm (steering 00:02) — pre-flight only [N]
- The N12 operator A(t) reproduces the a_per periodic rates exactly (1.2185, 1.2624).
- **k-block norms in ṽ = Tv (g_D1perorb_H.py, f_D1preflight_H.py):**
  - Along the worst outside periodic orbit (rate 1.2624), g_k = 5.51, 2.05, 1.54–1.80, 1.31–1.41, 1.30–1.42, 1.33–1.38, 1.27–1.30 for k = 1, 2, 4, 8, 12, 16, 48.
  - Random outside points (closed 1/8 box): 300 samples: max g_k = 5.51, 3.23, 1.80, 1.43, 1.14, 1.10 for k = 1, 2, 4, 8, 12, 16 (medians 3.42, 1.85, 1.20, 0.96, 0.88, 0.85).
- **Assessment:**
  - A pure k-block certificate needs k ≳ 12–16 to get below T′ (overhead ~5–10% over the orbit rate). Cells must then be ~λ^{−k}, which is infeasible.
  - At feasible k ≤ 3–4, ṽ block norms are ≥ 1.8 > T′.
  - So D1 still needs a cone-field (rank-one) certificate. The adapted norm's one-step 0.45 contraction is certified only at t = 0 (inside the box), not along outside orbits.
- **Not launched.** On 1 shared core it would compete with N13's arb jobs. Next step: the cone check in ṽ on a pseudo-orbit graph at k ≤ 3, with cells λ^{−2}·w.

## Files
- code: u_cert.py, a_unit_types.py, b_exactXY.py, c_LambdaU.py, d_mixed.py, e_model.py, f_D1preflight_H.py, g_D1perorb_H.py
- logs: u_cert_*.json, a_unit_{single_p29,p47,p59; two_p47}.json, b_exactXY_p{5,7}.json, c_LambdaU_p{29,47,59}.json, d_mixed_p11_*.json, e_model.json, f_D1preflight_H_th0.125.json, g_D1perorb_H_th0.125.json, NOTES_N9b.orig.md
- REPORT_N11b.md, REPORT_N9b_v2.md, NOTES_N11b.md, SHA256_N11b.txt (+ .sha256)
