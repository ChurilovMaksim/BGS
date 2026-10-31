# Line N12 — adapted norm (both gaps), interaction prefactor, N11_v2 fixes
Box clock Asia/Yekaterinburg (UTC+5), 2026-10-31. Labels: [P] proof, [P-sketch], [CA] arb-certified, [CA-float] float with explicit
rounding bounds (not interval), [N] numerics, [H] heuristic. Reusable artefact: `adapted/` (README, verify script, tables).

## 0. Summary
| # | Result | Label |
|---|---|---|
| 1 | **Adapted (Stein/Lyapunov) norm for the sector-4 core operator A0**: ‖A0/s‖_H ≤ 1+1e-8, **‖(A0/s)Q̃‖_H ≤ 0.45 in one step with constant 1**, cond(H) = 21.06, Galerkin→true error 2.1e-8. Replaces Cpow = 3246.8 / R₂′ = 3224.8 / C_A(0.8) = 10.65. | [CA-float] (`adapted/verify_adapted.py`, ALL_OK) |
| 2 | **One norm serves all four slow fixed twists** 0, ¼, ½, ¾: w_a(n) = w_4(n)e(n(a−4)/8), so sector a at τ is A(τ+(a−4)/8); slow twist b uses sector 4−8b, i.e. A0. | [P] (identity of the cert_core weights) |
| 3 | **Twist Lipschitz in H-norm: Lip_H = 167.2** (2-norm 484; old Cpow·2πN₁/μ ≈ 6e6). **Quadratic near the slow twist:** ψᵀA′(0)Φ = 0 (1e-16), and N_H(t) := ‖A(t)/s‖_H ≤ 1 + 3.19e3·t² for |t| ≤ 1/256 (measured 1 + 602t²). | [CA-float]/[P-sketch] |
| 4 | **D2 per-stay constant becomes O(10²)**: ‖∏L_i/s‖₂ ≤ 21.06·∏ min(1+3.19e3δ_i², N_H-table(δ_i)+0.0204); geometric stay ends give ≈ 2.31 (θ=1/16) / 3.68 (θ=1/8) per end. Old constant exp(6e6Σδ). | [CA-float table] + [P given V1–V4] |
| 5 | **Interaction prefactor solved at the level of numbers:** with constant 1, the merged list closes at G₀ = 16 (λ-steps): analytic tail Σ ≤ 1.3e-4 relative per type pair (3.3e-12 absolute). Explicit list: **1350 coded two-bump types** (ε-gap ≥ g₀ = 5, G ≤ 15). | [N/CA-float] |
| 6 | **Per-site interaction δ_int ≤ 5.14e-7**, i.e. 8.3e-4 of Re Λ_lo (target < 6.2e-4: met with factor 1200). Dominated by odd–odd at ε-gap 6–8 (dev 0.83 → 0.26, matches referee's r/w*² at n = 8). | [N, float]; arb of the 1350 types **pending** |
| 7 | (2) collective digit-transfer tail for short cores: **not done** (obstruction stated in §4). | — |

## 1. Adapted norm (gap (a) and gap (b))
- Definition (`code/f_adapted.py`): H = ωψ̄ψᵀ + Q̃*PQ̃, Q̃ = I − Φψᵀ, P = Σ_j kap^{−2j}(Bʲ)*Bʲ (Stein, B = Q̃A0Q̃/s), kap = 0.45, ω = 1.
  Then B*PB = kap²(P − I) ≤ kap²P, which is the one-step contraction. Φ is H-orthogonal to range Q̃, so ‖Q̃‖_H = 1.
- Verified a posteriori (`adapted/verify_adapted.py`): each X*HX ≤ c²H is checked as λ_min(c²H − X*HX) > (Higham γ-bound on forming it + eigvalsh backward error).
  V2 margin 2.0e-8 vs err 3.1e-10; V3b margin 0.102 vs 5e-11. Inputs: D·RAD = 4.0e-17 (cert_core radii), Pert = 1.90e-9 (n_cert).
  Rigour level: float with explicit error terms, not interval arithmetic. An arb replay is straightforward (one 495×495 Cholesky) and is the next step.
- Not certified: the eigenpair itself (only residuals ≤ 7e-15 are used, through the commutation residual 6.6e-15, which is inside the η margins).
- The off-dominant power profile ‖(A0/s)ⁿQ̃‖_H/0.45ⁿ = 0.998, 0.950, 0.817, … 0.177 (n=12) shows the true rate 0.380 [N].
- Far (non-Galerkin) part: inherited from Line F as an additive Pert; in H-norm it costs ≤ 2.1e-8 per step relative to |s| [CA-float]. The full extension of H to the far coordinates (‖(v_c,v_f)‖ = ‖v_c‖_H + c_f‖v_f‖) is [P-sketch].

## 2. Interaction prefactor (task 1)
- Gap splitting in H-norm: r_ij − r_i r_j = w_t Q̃ (A0/s)^m Q̃ v_t + (rank-one tail mismatch M_t). The first term is ≤ ‖w_tQ̃‖_{H*}‖Q̃v_t‖_H·0.45^m with **no transient constant** (`code/e_tail_H.py`).
  - Measured at the best cut: K ≤ 6e-16 (the Q̃ parts are negligible). The tail is dominated by M_t (bump j's twist tail on bump i's side, natural rate λ^{−1} = 0.172; the script charges 0.45^m) — this M-decay is [P-sketch].
  - Tail sums over G ≥ G₀: max per type pair 6.3e-3 (G₀ = 12), 1.3e-4 (G₀ = 16).
- Explicit merged types (`code/d_merged.py`, G ≤ 15, all ordered pairs of 𝒯 = {odd, √2, 2, 2√2, 4}, h ∈ {0,1}, ±): 1550 types; 1350 are coded (ε-gap n = 2G+h ≥ g₀ = 5).
  - Types with n < 5 are **not** two-bump polymers. Their composite seed equals another single type (e.g. 4√2 − 2ε = 2ε⁻¹) or is uncoded. This is why "dev" reaches 4.5e8 there: it is a relabelling, not an interaction. They belong to the single-type list or to (T).
- **δ_int** (`code/g_dint.py`, logs/g_dint.json): Σ over coded types of |w_i||w_j|·dev = 5.144e-7, plus the G ≥ 16 tail 3.3e-12. Both orderings are counted.
  Triple clusters are O(A³) ≈ 8e-11.
- Remaining for [CA]: an arb (or float-with-error) replay of the 1350 windows (~0.4 s each in float; arb ≈ 2–4 h on this 1-core box). The adapted norm makes the error propagation linear: e_{t+1} ≤ N_H(d_t)e_t + γ·c_hi‖|A||v|‖.

## 3. What gap (b) can use now (`adapted/README.md`)
- Files: `logs/adapted_norm_t0.0_k0.45.npz` (T, H, P, Φ, ψ, s, Q̃) + `.json`; `…_stepnorm_NG4096.json` (N_H on t = j/4096, cell add-on 0.0204);
  `logs/quad_stepbound.json`; scripts `code/f_adapted.py`, `adapted/verify_adapted.py`, `adapted/stepnorm_table.py`, `adapted/quad_stepbound.py`.
- D2: see row 4. D1 cone fields: work in ṽ = Tv, where every step is T A(t)T⁻¹/s with spectral norm N_H(t) ≤ 2.876 (max, at t ≈ 0.1436).
  The dominant/off-dominant split is Euclidean-orthogonal in these coordinates, with contraction 0.45 exactly at t = 0. This should raise N10b's 41–58% cone-invariance rate, but that is untested [H].
- Caveat: N_H is a single-step bound. Γ_out-type pressures need products over excursions, so it does not replace the D1 grid.

## 4. Task 2 (collective short-core tail): not done, and why
- A digit-transfer bound of Σ|w| by products of step norms ∏N_H(d_t) has growth λ·N̄ > 1 per step (class count λ^k against norms ≥ 1). It cannot be summable without cancellation.
- What does work collectively is ℓ² (Line F r₂ / HS²), and Cauchy–Schwarz back to ℓ¹ loses √(#classes) = λ^{k/2}.
- A usable route needs a signed/second-moment transfer: either (i) the r₂(k) table plus a per-shell count giving Σ|w| ≤ √(N_k·HS²_k), which needs HS²_k ≤ λ^{−k}·(budget)², i.e. r₂ < 1 relative to λ in the shell normalisation; or (ii) an automaton on (digit, H-coordinate cone) pairs.
- **Open.** The measured remainder (≈1.7e-6 phase-checked, N11-F1) is 1/370 of the budget, so there is room, but no proof.

## 5. REPORT_N11_v2 (referee /workspace/audit/lineN11/REPORT.md)
- **F1 (required) — applied.** The completeness remainder is **≈1.7e-6 phase-checked** (not 1.0e-7). It consists of short-range clusters: background 0 α′ = (1,±2), (0,3), (4,0), (10,0), (0,7); background q (3,0).
  - Units: a class-weight sum at p = 47, while Re Λ_lo is per site.
  - Still 1/370 of Re Λ_lo [N]. These clusters are exactly the n < 5 / close-range items of §2 here and of N11 §2; cross-referenced.
- **F2 (required) — applied.** In Lemma C(ii), |β − β′| ≤ 2B = 8, so the norm bound carries (2B)² = 64. Hence G₀ = 7 (not 6): injectivity holds for |Γ|+|Γ′| ≤ p/7.
  - Hypothesis "all gaps ≥ g₀ = 5" is now explicit in (ii). ± closure of 𝒯 handles ε^p ≡ −1.
  - Dense cutoff n₀ = p/14, giving e^{−0.23p}. Part (i) is unchanged.
- **F3 — applied.** Re Λ_lo script archived as `code/lambda_cert.py` (exact rationals on the stored arb bounds of N8 fam/near0 and N9 z0_e4/z0_e4s2): Re Λ_lo = 6.23837e-4.
  - The uncertified type-4 activity c₁₆ (|·| ≈ 2.2e-9) is charged ×10 per sign: **Re Λ_lo′ = 6.23397e-4**, used throughout.
  - [CA] means "≤ Re of the sum of the listed certified activities". Its identification with the gas Λ is model-level.
- **F4 — applied.** The bound now reads |1+X_gas| ≥ 2(1+Re Λ_lo)^p e^{−pδ_int} − 1, using (1+a)(1−δ), not (1+a)e^{−δ} ≥ 1+a−δ.
  - The bracket condition (·)² − 1 > 0.2 alone needs **p ≥ 75** (lambda_cert.json).
  - p ≥ 1289 is the provenance of the per-class finite-p error E ≤ τ = 1e-9 (N8 Prop X′, `N8/logs/q_propx2_all.out`: p₀ = 1197–1289, worst is the near-0 class). It is the range of the class certificates, not of the bracket.
- **F5 — noted.** g₁ ≈ 68 with 10 types. This is superseded by §2: with the adapted norm the list closes at G₀ = 16.
- **F6 (required) — applied.** "Prime h_p not needed for Y" is relabelled **[H, conditional]**. It is conditional on (I), (T), and G* with polynomial A, and further:
  - (a) G*'s reduction gives (C_out K_box)^{#stays+1}. §3's K_stay = O(10²) turns this into a stay-gas fugacity C²(μ*/(Γλ))^L, which still has to be closed by gap (b).
  - (b) The unit bumps ±ε^{±1} (|r| = 1.315e-3 > Re Λ) form their own gas inside Y; this is being studied by the other author.
  - (c) Mixed classes at small q₂ have only polynomial κ-suppression.
  - What is needed is an explicit growth exponent for Y against Re Λ_lo − δ_int (now 6.234e-4 − 5.1e-7 [N]). The squarefree C′ statement stands.
- **F7 — applied.** The referee's R included c₈ and c₁₆. The difference came from N11 using the p = 47 values of c₀ and c₄ instead of the plateau values; it is immaterial. N10_v2-F6 is withdrawn.

## 6. Status of gap (a) after N12
- (I) interaction: rate and **prefactor now O(1)** [CA-float norm], δ_int = 5.1e-7 [N]. Remaining: arb replay of the 1350 types, and the M-tail decay lemma [P-sketch].
- (T) absolute tail and short cores: OPEN (§4).
- Y: [H, conditional] (F6).
