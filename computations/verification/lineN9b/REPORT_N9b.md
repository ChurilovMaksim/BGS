# REPORT N9b — hypothesis G: reformulation, evidence, certification feasibility; R_s moments; primality in C2; N8b v2 fixes
Labels: [P] proved · [P-sketch] · [CA] arb certificate · [N] numerical · [H] heuristic.  Nothing pushed; N7b/N8b files untouched.
Times Asia/Yekaterinburg (UTC+5), 2026-10-31.  Inputs: N8b, N9 (REPORT_N9 §2-§5), referee /workspace/audit/lineN8/REPORT.md.

## 0. Summary
| # | Result | Label |
|---|---|---|
| 1 | **G as stated in N8b is false; replaced by G\*.** N8b's convention "s = 0 for unit points" fails: unit points with small β (β = a+b√2, \|a\|,\|b\| ≤ 3) have \|r\| = 1.32e-3 *independent of p* (p = 11…61), so Γ_raw = μ*\|r\|^{1/m} → μ*. Together with N9's multi-bump classes this forces **G\***: s(x) = *all* time spent in the θ-box of the slow fixed points (forced or not). | [N] (counterexample to G with s=0 is numerical but robust: flat in p over 13 values of p) |
| 2 | **Evidence for G\* on unit, small/medium-unit and mixed patterns, p = 11…61** (referee N8b-F7). Max over samples of Γ_eff(θ) = μ*\|r\|^{1/(m−s)}: θ = 1/8: ≤ 1.189 (all p), ≤ 1.131 for p ≥ 13, ≤ 1.11 for p ≥ 29; θ = 1/16: ≤ 1.248 (p = 13, one UM point), ≤ 1.142 for p ≥ 29. Random unit/mixed points: Γ_raw max decreases 1.31 (p=11) → ≤ 1.0 (p ≥ 37); medians 0.86–0.94. **A = 1 suffices for G\*(Γ = 1.25) on every sampled point; Γ = 1.2329 holds at θ = 1/8.** Sampled, not exhaustive. | [N] |
| 3 | **Dynamical part of G\*: Γ_out(θ) profile** (spectral rates of all 207,162 primitive periodic orbits of the twist cat map, period ≤ 8, 8V Line-F operator). Max rate over orbits avoiding the θ-box of (0,0): θ=1/16: 1.4296 (> T′ = 1.4279!), θ=1/8: **1.2624**, θ=3/16: **1.2185**, θ=1/4: 1.1675. | [N] |
| 4 | **Certification of Γ_out(1/8) < T′: not achieved.** Products are 140-dim, very non-normal (σ₁(L_τ) = 22–57 vs ρ ≤ 1.92) and rank-one after a few steps (σ₂/σ₁ = 0.43, 0.14, 0.0077 at k = 2, 4, 8). Fixed (adapted ellipsoidal) norms give ≥ 2.35; k-block norms give 1.75 (k = 6); a rank-one (cone-field) potential on a pseudo-orbit graph gives 1.534 / 1.419 / 1.357 at grid 128/256/512 (θ = 1/8), converging slowly to ~1.26–1.3. A rigorous cone-field graph certificate looks feasible in principle at grid ≳ 1024 with float+rounding-margin ([CA*]) but not in arb in this session. Rank-p target 1.2329 has essentially no margin (3/16-box: 1.2185) → do rank p via §5 instead. | [N] + design [H] |
| 5 | **R_s moments (task 2).** Periodic-orbit (zeta) estimates R_s = (Σ_{Fix Aⁿ} ρ(P_n)^s)^{1/n}/λ, n ≤ 7, stable: R₂ = 1.0002, **R₃ = 1.4055**, **R₄ = 2.4017**. So **R₃ ≤ 1.33 (κ ≤ 0.55) looks false**; R₃ = 1.41 would give κ₃ ≈ 0.57. **R₄ ≤ 2.611 holds with ~8% margin** (κ₄ ≈ 0.525) → a 4-fold (not 3-fold) automaton is the moment route to κ ≤ 0.55. No automaton certificate built. | [N] |
| 6 | **Primality of h_p in C2 (task 3).** Deep/proper-divisor classes cost nothing extra (windows at all depths, N9 §2; gas factor acts only on excursions of length log_λ(dN f)). The only obstruction is the divisor sum Σ_{d∣h_p,d>1} d^{1−β} with polynomial margin. **C2′:** "h_p prime" can be replaced by "ω(h_p) ≤ p^{δ}" (δ < β−1−a when A_p ≤ p^a), including prime powers. Unconditional removal needs β > 3/2 (Γ < 1.2329). The replacement is weaker but still unproven. | [P given G\*] + [H] (no known proof of the ω condition) |
| 7 | **N8b v2 fixes** (§6): F2 prime powers, F6 κ-floor scope, F7 G evidence (now §2), F8 C2 scope / infinitude, bonus composite loss ≤ 0.52%. Also flagged: C1/C2 assume Lemma A∞, which N9 shows is very likely false p-uniformly. | [P] / bookkeeping |

## 1. Hypothesis G\* (all slow time counted)  [statement; reduction P-sketch]
Fix θ and the slow fixed points F = {(0,0),(½,½)} of the twist pair map (τ_i,τ_{i+1}) ↦ (τ_{i+1}, 6τ_{i+1}−τ_i).
s_θ(x) := #{i < m : (τ_i,τ_{i+1}) within sup-distance θ of F}.  
**G\*(Γ, A, θ):** |r(x)| ≤ A·(Γ/μ*)^{m − s_θ(x)} for every residual point x (isotropic, unit, mixed).
- Why: (i) N9 §3 multi-bump classes have w ≈ ∏ bump factors independent of gaps; (ii) §2 below, unit points with small β have \|r\| = 1.32e-3 flat in p. Both violate G with s = forced-window time only and p-independent A.
- **Reduction to dynamics [P-sketch].** Split the orbit into stays (maximal runs in the θ-box) and outside segments.
  - (D1) outside segments: ‖P_n‖ ≤ C_out Γ_out(θ)^n;
  - (D2) a stay of length ℓ: ‖P_ℓ‖ ≤ K_box μ*^ℓ. In a stay, Σ|τ_i| = O(θ) (geometric in both directions), so D2 follows from ‖L₀^ℓ‖ ≤ K₀μ*^ℓ (μ* a simple dominant eigenvalue) plus a Duhamel perturbation bound. Elementary, certifiable.
  - Then |r(x)| ≤ (C_out K_box)^{#stays+1}·Γ_out^{m−s}μ*^{s}.
  - The factor C^{#stays} is a gas fugacity. A stay of length ℓ costs a factor ~λ^{−ℓ} in the class count and gains (μ*/Γ)^ℓ, with μ*/T′ = 1.34 ≪ λ. So stays form a dilute gas of fugacity z per unit time; Lemma Σ acquires e^{z·(excursion time)}. That is harmless where the margin is exponential (rank 3p, inconsistent, unit: λ^{(p/2)(1−β)}). On rank-p lines it acts only on excursions of length log_λ(dN f), shifting β by O(z). This is consistent with N9's e^{O(1e-4 p)} gas factor.
- So G\* follows from: Γ_out(θ) < target (D1), plus D2, plus a stay-counting lemma (a lattice count of points with a run of length ℓ in a box, area ~θ²λ^{−ℓ}) [P-sketch].

## 2. Evidence for G\* on unit and mixed patterns (`code/g_unitmix.py`, `logs/g_unitmix.jsonl`, `logs/g_unitmix_s{1,2}.out`)  [N]
Twists τ_i = 2·Re(λ^iβ mod h_p)/h_p (as N7 f_mixed), r = Z(β)/Z(0) by N6 twb.Zbatch (L2 TW law, L = 8, K = 16), m = 3p.
Classes: U random unit (N=120; 200 at p=11); US all small units |a|,|b| ≤ 3 (48); UM |a|,|b| ≤ h_p^{1/4}; M_q iso-or-0 mod q, unit at the other primes.
Γ_raw = μ*·max|r|^{1/m} (G with A=1, s=0); Γ_eff(θ) = max μ*|r|^{1/(m−s_θ)}.

| p | class | n | max\|r\| | Γ_raw max | Γ_raw med | Γ_eff(1/16) (s) | Γ_eff(1/8) (s) |
|---|---|---|---|---|---|---|---|
| 11 | U | 200 | 3.53e-06 | 1.309 | 0.937 | 1.189 (3) | 1.189 (3) |
| 11 | US | 48 | 1.31e-03 | 1.567 | 1.338 | 1.141 (15) | 1.102 (21) |
| 11 | M23 | 200 | 3.77e-05 | 1.407 | 0.935 | 1.179 (12) | 1.179 (12) |
| 11 | M353 | 200 | 2.60e-07 | 1.210 | 0.931 | 1.154 (3) | 1.128 (0) |
| 13 | U | 120 | 4.00e-09 | 1.167 | 0.915 | 1.137 (0) | 1.087 (0) |
| 13 | US | 48 | 1.32e-03 | 1.616 | 1.414 | 1.142 (21) | 1.102 (27) |
| 13 | UM | 120 | 1.46e-04 | 1.527 | 1.226 | 1.248 (15) | 1.088 (18) |
| 13 | M79 | 120 | 3.49e-09 | 1.163 | 0.932 | 1.163 (0) | 1.115 (3) |
| 13 | M599 | 120 | 1.17e-09 | 1.130 | 0.928 | 1.130 (0) | 1.130 (0) |
| 17 | U | 120 | 1.31e-12 | 1.120 | 0.908 | 1.120 (0) | 1.083 (3) |
| 17 | US | 48 | 1.32e-03 | 1.682 | 1.518 | 1.142 (33) | 1.102 (39) |
| 17 | UM | 120 | 9.01e-05 | 1.596 | 1.292 | 1.142 (33) | 1.102 (30) |
| 17 | M103 | 120 | 4.41e-12 | 1.147 | 0.898 | 1.147 (0) | 1.111 (3) |
| 17 | M15607 | 120 | 3.57e-12 | 1.142 | 0.902 | 1.128 (0) | 1.128 (0) |
| 19 | U | 120 | 1.35e-14 | 1.094 | 0.901 | 1.094 (0) | 1.084 (0) |
| 19 | US | 48 | 1.32e-03 | 1.705 | 1.556 | 1.142 (39) | 1.102 (45) |
| 19 | UM | 120 | 1.32e-03 | 1.705 | 1.319 | 1.164 (33) | 1.102 (45) |
| 23 | U | 120 | 1.16e-18 | 1.053 | 0.889 | 1.053 (0) | 1.025 (3) |
| 23 | US | 48 | 1.32e-03 | 1.740 | 1.613 | 1.142 (51) | 1.102 (57) |
| 23 | UM | 120 | 3.31e-05 | 1.649 | 1.377 | 1.186 (36) | 1.131 (39) |
| 23 | M47 | 120 | 4.85e-19 | 1.040 | 0.892 | 1.040 (0) | 0.962 (0) |
| 23 | M6771937 | 120 | 3.62e-18 | 1.070 | 0.886 | 1.070 (0) | 1.042 (3) |
| 29 | U | 120 | 7.90e-24 | 1.039 | 0.873 | 1.039 (0) | 0.968 (0) |
| 29 | US | 48 | 1.32e-03 | 1.775 | 1.672 | 1.142 (69) | 1.102 (75) |
| 29 | UM | 120 | 3.32e-08 | 1.571 | 1.400 | 1.059 (51) | 1.040 (54) |
| 31 | U | 120 | 1.01e-25 | 1.032 | 0.871 | 1.011 (3) | 0.942 (3) |
| 31 | US | 48 | 1.32e-03 | 1.784 | 1.686 | 1.142 (75) | 1.102 (81) |
| 31 | UM | 120 | 3.25e-09 | 1.552 | 1.423 | 1.059 (60) | 1.003 (60) |
| 31 | M424577 | 120 | 5.96e-23 | 1.105 | 0.875 | 1.105 (0) | 1.105 (0) |
| 31 | M865087 | 120 | 1.44e-25 | 1.036 | 0.879 | 1.004 (0) | 0.944 (6) |
| 37 | U | 120 | 5.69e-33 | 0.981 | 0.873 | 0.959 (0) | 0.941 (3) |
| 37 | US | 48 | 1.32e-03 | 1.804 | 1.722 | 1.142 (93) | 1.102 (99) |
| 37 | UM | 120 | 3.47e-10 | 1.574 | 1.433 | 1.101 (69) | 0.982 (72) |
| 37 | M223 | 120 | 5.32e-32 | 1.001 | 0.870 | 0.973 (3) | 0.923 (6) |
| 37 | M37223 | 120 | 3.21e-32 | 0.997 | 0.875 | 0.997 (0) | 0.979 (3) |
| 37 | M8761009 | 120 | 2.88e-32 | 0.996 | 0.870 | 0.980 (0) | 0.980 (0) |
| 41 | U | 120 | 1.82e-36 | 0.981 | 0.866 | 0.946 (0) | 0.913 (6) |
| 41 | US | 48 | 1.32e-03 | 1.815 | 1.740 | 1.142 (105) | 1.102 (111) |
| 41 | UM | 120 | 7.45e-11 | 1.585 | 1.431 | 1.099 (81) | 1.002 (87) |
| 41 | M2297 | 120 | 9.01e-36 | 0.994 | 0.867 | 0.955 (0) | 0.906 (9) |
| 41 | M302663 | 120 | 5.71e-35 | 1.009 | 0.869 | 0.972 (3) | 0.915 (12) |
| 41 | M3553471 | 120 | 1.10e-36 | 0.977 | 0.872 | 0.977 (0) | 0.961 (3) |
| 43 | U | 120 | 1.02e-34 | 1.044 | 0.858 | 1.014 (6) | 0.998 (9) |
| 43 | US | 48 | 1.32e-03 | 1.819 | 1.747 | 1.142 (111) | 1.102 (117) |
| 43 | UM | 120 | 1.83e-10 | 1.610 | 1.441 | 1.032 (81) | 1.009 (90) |
| 43 | M19609 | 120 | 7.06e-35 | 1.041 | 0.867 | 0.998 (3) | 0.949 (12) |
| 43 | M153511 | 120 | 1.50e-37 | 0.993 | 0.869 | 0.961 (6) | 0.910 (15) |
| 43 | M4783321 | 120 | 6.42e-39 | 0.969 | 0.872 | 0.953 (3) | 0.920 (9) |
| 47 | U | 120 | 1.09e-40 | 0.997 | 0.861 | 0.944 (0) | 0.893 (12) |
| 47 | US | 48 | 1.32e-03 | 1.827 | 1.761 | 1.142 (123) | 1.102 (129) |
| 47 | UM | 120 | 3.68e-12 | 1.589 | 1.457 | 1.067 (96) | 0.971 (99) |
| 53 | U | 120 | 1.26e-48 | 0.957 | 0.860 | 0.944 (3) | 0.890 (15) |
| 53 | US | 48 | 1.32e-03 | 1.837 | 1.778 | 1.142 (141) | 1.102 (147) |
| 53 | UM | 120 | 1.13e-14 | 1.565 | 1.450 | 0.981 (111) | 0.914 (114) |
| 53 | M9940681 | 120 | 1.54e-49 | 0.945 | 0.862 | 0.932 (3) | 0.892 (12) |
| 53 | M9742382798081 | 120 | 9.27e-48 | 0.969 | 0.859 | 0.930 (3) | 0.885 (6) |
| 59 | U | 120 | 7.36e-55 | 0.947 | 0.853 | 0.940 (0) | 0.893 (12) |
| 59 | US | 48 | 1.32e-03 | 1.845 | 1.791 | 1.142 (159) | 1.102 (165) |
| 59 | UM | 120 | 6.11e-14 | 1.613 | 1.466 | 1.090 (123) | 1.016 (129) |
| 61 | U | 120 | 2.01e-55 | 0.962 | 0.852 | 0.923 (6) | 0.866 (12) |
| 61 | US | 48 | 1.32e-03 | 1.847 | 1.795 | 1.142 (165) | 1.102 (171) |
| 61 | UM | 120 | 8.79e-16 | 1.585 | 1.475 | 1.037 (126) | 0.976 (123) |
| 61 | M92111 | 120 | 4.99e-57 | 0.943 | 0.854 | 0.932 (3) | 0.905 (9) |
| 61 | M1213319877845761591 | 120 | 7.89e-57 | 0.946 | 0.850 | 0.923 (6) | 0.906 (6) |

Reading:
- US: \|r\| = 1.32e-3 for every p (heteroclinic to the slow fixed point), Γ_raw → μ*. Γ_eff(1/16) = 1.142, Γ_eff(1/8) = 1.102, flat.
- Random U/M: Γ_raw decreases with p and is ≤ 1.0 for p ≥ 37 (no slow time needed).
- Worst G\* value: Γ_eff(1/16) = 1.248 (p = 13, UM); at θ = 1/8 every sampled point has Γ_eff ≤ 1.189.
- Caveat: sampled points (≤ 528 per p), not a max over the ~h_p² points; the adversarial direction (small β) is covered by US/UM.
- The referee's p = 11 mixed max (\|r\| = 1.4e-4 → Γ_raw 1.46) is reproduced in kind (here 3.8e-5, Γ_raw 1.41, s = 12 → Γ_eff 1.18).

## 3. Dynamical profile and certification feasibility
**3a. Periodic-orbit profile** (`code/a_per.py`, `logs/a_per_a4.jsonl`, `logs/a_per_68.out`) [N]: all periodic points of A = [[0,1],[−1,6]] for n ≤ 8 (D_n = 4, 32, 196, 1152, 6724, 39200, 228484, 1331712 points; assert #points = |det(Aⁿ−I)|), spectral rate ρ(P_n)^{1/n} of the 140-dim 8V Line-F operator (K0=3, r=1.2, K=20, β=2.5, N0=10, sector a = 4).

| n | θ=0 | 1/64 | 1/16 | 1/8 | 3/16 | 1/4 |
|---|---|---|---|---|---|---|
| 1 | 1.9155 | 0.8774 | 0.8774 | 0.8774 | 0.8774 | 0.8774 |
| 2 | 1.2517 | 1.2517 | 1.2517 | 1.2517 | 1.2185 | 1.1062 |
| 3 | 1.2837 | 1.2837 | 1.2836 | 1.2624 | 1.0965 | 0.9436 |
| 4 | 1.4296 | 1.4296 | 1.4296 | 1.2278 | 1.1675 | 1.1675 |
| 5 | 1.5096 | 1.4336 | 1.2179 | 1.1994 | 1.1178 | 1.0152 |
| 6 | 1.5683 | 1.4211 | 1.2845 | 1.2229 | 1.1392 | 1.1392 |
| 7 | 1.6141 | 1.3646 | 1.3646 | 1.2174 | 1.1515 | 1.0487 |
| 8 | 1.6493 | 1.4101 | 1.3319 | 1.2278 | 1.1317 | 1.1317 |
(Primitive orbits of exact period n; the θ = 0 column is unrestricted, and the fixed point (0,0) itself is the n = 1 entry 1.9155.)
- A 1/16 box is too small (1.4296 > T′ at n = 4). With a 1/8 box: Γ_per ≤ 1.2624, margin 0.165 to T′. Rank-p target 1.2329 needs the 3/16 box (1.2185), with no margin for a rigorous method.

**3b. Norm experiments** [N]: `code/d_svals.py`, `code/b_mmc.py` (logs/b_mmc_*.json), `code/c_wnorm.py` (logs/c_wnorm.out), `code/e_cone.py` (logs/e_cone_*.json/out).
- k-block norm potential + graph max-mean, θ = 1/8: k = 6 → 1.752. k = 12 is centre-sampling-invalid: cells are stretched by λ^{11}, and the max grid value 1.50 < μ*.
- Adapted ellipsoid (averaged Lyapunov Q, J = 3), k = 1: 2.349.
- Rank-one potential φ(y) = log|L_{τ₀}u(y)| (u = 8-step pushed direction):

| grid | θ=1/16 | 1/8 | 3/16 |
|---|---|---|---|
| 128 | 1.612 | 1.534 | 1.392 |
| 256 | 1.501 | 1.419 | 1.315 |
| 512 | 1.497 | 1.357 | 1.293 |

- These are centre-sampled, so not rigorous. The pseudo-orbit graph allows one-cell jumps, and u is only Hölder (exponent ≈ log(1/0.43)/log λ ≈ 0.48), so convergence is slow.
- **Certificate design [H]:**
  - cone field 𝒦_C = {x : ‖x − ⟨x,u_C⟩u_C‖ ≤ a|⟨x,u_C⟩|} on grid cells;
  - check L_τ𝒦_C ⊂ 𝒦_{C′} for all τ ∈ π₁(C) and all edges C→C′;
  - weights f(C) = sup log‖L_τx‖/‖x‖ over the cone, rigorous via Lipschitz in τ;
  - Howard/Karp max-mean cycle with a potential check;
  - plus a k-step absorption of off-cone vectors (rank-one collapse).
- Cost at grid 1024: ~10⁶ cells × 9 edges × a 140-dim cone check. That is feasible in float with an a-priori rounding margin ([CA*], N9-style), hours. It is not feasible in arb here.
- Expected outcome: rigorous Γ_out(1/8) somewhere in 1.30–1.42, if the grid-512 trend continues. That is enough for T′ (rank 3p, C2-type) but not for 1.2329.

## 4. Moments R_s (task 2) (`code/f_Rs.py`, `logs/f_Rs_a4.jsonl`, `logs/f_Rs_67.out`)  [N]
R_s(n) = (Σ_{x∈Fix Aⁿ} ρ(P_n(x))^s)^{1/n}/λ (periodic-orbit/zeta estimate of e^{P(sψ)}/λ):

| n | R₂ | R₃ | R₄ |
|---|---|---|---|
| 3 | 1.039 | 1.460 | 2.451 |
| 4 | 1.007 | 1.410 | 2.406 |
| 5 | 1.0002 | 1.402 | 2.398 |
| 6 | 1.0005 | 1.4049 | 2.4010 |
| 7 | 1.0002 | 1.4055 | 2.4017 |

- R₂ ≈ 1.000, consistent with the certified r₂ ≤ 1.0529 and with N8b's "true r₂ ≈ 1" [H].
- Targets: R₃ ≤ 1.3284 (floor 1.2058) and R₄ ≤ 2.611 (floor 2.310), both for κ ≤ 0.55.
- **R₃ fails the target by ~6%, while R₄ passes with ~8% margin.** κ₃(1.4055) ≈ 0.57 by interpolation of the N8b table (0.55 at 1.3284, 0.60 at 1.5361).
- Caveat: this uses ρ instead of the HS norm of the actual blocks, and the 8V operator in sector 4 only. Pressure from ρ-sums equals norm pressure for dominated cocycles; this cocycle is numerically rank-one dominated (§3b) [H].
- The collision automaton itself (≈ 4000^{s/2} states) was not attempted. If attempted, use s = 4.

## 5. Avoiding "h_p prime" in C2 (task 3), coordinated with N9 §2
- **Deep classes.** N9 §2 shows that windows exist at all depths (balanced representatives), so the proper-divisor classes at c = h_p/d (N(e) = d·N(f)) need no separate regime.
  - Under G\* their gas factor acts on excursions of length log_λ(dN f) only (Lemma P′_c), shifting β by O(z) [P-sketch].
- **Divisor sum [P].** With prime powers allowed (F2), Σ_{d∣h_p,d>1} d^{1−β} ≤ exp(Σ_{r∣h_p} r^{1−β}/(1−r^{1−β})) − 1.
  - The distinct primes satisfy r_j ≥ 2pj+1, so the sum is ≤ exp((1−(2p)^{1−β})^{−1}(2p)^{1−β}Σ_{j≤ω} j^{1−β}) − 1.
- **C2′ [P given G\*(Γ, A_p) with Γ < T′, Lemma A∞ and the standing package].** R′ fails along m = 3p for p in 𝒫′ = {p : A_p·ω(h_p)^{2−β}(2p)^{1−β} → 0}.
  - 𝒫′ contains {p : h_p prime}, all p with ω(h_p) bounded, and (if A_p ≤ p^a) all p with ω(h_p) ≤ p^{(β−1−a)/(2−β)−η}.
  - Unconditionally (ω ≤ 0.89p/ln 2p) this needs β > 3/2, which is C1.
- **Assessment [H].** The arithmetic input drops from "infinitely many prime h_p" to "infinitely many p with few prime factors of h_p", which is far more plausible (data p < 62: ω ∈ {1, 2, 3}). It is still unproven; no sieve result is known to me for Lucas-type sequences.
  - It requires A_p to be polynomial, not merely e^{o(p)}. G\* via D1/D2 gives p-independent A up to the gas factor.

## 6. REPORT_N8b_v2 — required fixes (referee /workspace/audit/lineN8/REPORT.md)
- **F2 (prime powers) [P].**
  - Lemma Σ(a): replace Σ_{d∣h_p} by the Euler product above. Each prime contributes 1 + r^{1−β}/(1−r^{1−β}) instead of 1 + r^{1−β}, and r ≡ 1 (mod 2p) is unchanged for every prime factor. The thresholds β > 3/2 (C1) and β > 1 + ω-condition (C2′) are unchanged.
  - Lemma Σ(b)–(d), and the K_p route: the number of divisors of K_p (or of any level) is τ(n) ≤ exp(O(log n/log log n)) = e^{o(p)} whatever the multiplicities (31² ∣ K_5 and 7² ∣ K_7 are allowed), and (b)–(d) only use e^{o(p)}. The statement "every prime r ∣ K_p, r ≠ 7, is ≡ 1 mod 6p" is about primes, so it stays true; drop any implicit squarefreeness.
  - In N8b §1(vi), "N(e) ≥ h_p/c ≥ 2p+1" still holds, since any d > 1 dividing h_p has a prime factor ≥ 2p+1.
- **F6 (scope).** κ ≥ 0.7060 is a floor for the **two-block op·HS² method** with the certified r₂. It is not an impossibility statement about the mixed gap. §4 here adds: with s = 4 blocks, the [N] R₄ = 2.40 < 2.611 would give κ ≤ 0.55.
- **F7 (G evidence).** G must hold for every residual point, and in N8b's form (s = forced time only) **it is false** for small-β unit points (§2) and for multi-bump classes (N9). Use G\* (§1).
  - Evidence for G\* on unit and mixed points at p = 11…61 is in §2: Γ_eff(1/8) ≤ 1.189 with A = 1. Labelled [N], sampled.
  - The h_13 inconsistent line (Γ_eff = 1.267, forced windows only) was not recomputed with all slow time counted. Under G\* it is expected to drop, but this is untested.
- **F8 (C2 scope).** C2 needs infinitely many p, because the disproof of R′ per TRACE-206 needs W′_m/m bounded away from 0 along a subsequence. One p does not suffice unless R′ is an explicit inequality at each m (the parent must state which form R′ takes). With C2′ (§5) the arithmetic input weakens to infinitely many p with small ω(h_p).
- **Bonus (adopt).** Since the j-th prime factor of h_p is ≥ 2pj+1, Σ 2/r_i ≤ H_ω/p ≤ 6/1165 < 0.52%. So F_m ≥ 2.32e-3·p\|Z₈\|²/h_p (referee Lean `fm_improved`) [P].
- **Flag.** C1 and C2 assume Lemma A∞. N9 §3–4 shows that A∞ in p-uniform form is very likely false (multi-bump gas, threshold p ≳ 6·10³ [H]). C1/C2 must be restated with N9's §5 replacement, a modulus bound |1+X+Y|, once it exists. G\* does not repair A∞.

## 7. What is proved / what remains
- **[P]:** F2 Euler-product version of Lemma Σ(a); C2′ as an implication; bonus 0.52%.
- **[P-sketch]:** reduction G\* ⇐ D1 + D2 + stay count.
- **[N]:**
  - Γ_per(θ) profile, n ≤ 8;
  - G\* evidence on U/US/UM/M classes, p ≤ 61;
  - R₃ ≈ 1.405, R₄ ≈ 2.402;
  - cone-potential convergence.
- **Not done:** no [CA] in this line. Specifically:
  - no certificate for D1 (Γ_out);
  - no R₄ automaton;
  - D2 constants not computed.
- **Best route:**
  1. Cone-field graph certificate of Γ_out(1/8) < 1.4279 at grid ≥ 1024 ([CA*]); then D2 and the stay count. That gives G\* for rank-3p, inconsistent and unit/mixed classes.
  2. Rank-p lines via C2′, not via 1.2329.
  3. The mixed gap via R₄ (4-fold automaton), or via G\* (which covers §6(d) points directly).
  4. A∞ (N9 §5) remains the blocking input for any theorem.

## 8. Files
- code: a_per.py, b_mmc.py, c_wnorm.py, d_svals.py, e_cone.py, f_Rs.py, g_unitmix.py, run_g.sh
- logs: a_per_a4.jsonl, a_per_68.out, b_mmc_G64_k6.json, b_mmc_G64_k12.json, c_wnorm.out, e_cone_G{128,256,512}_j8.json, e_cone_512.out, f_Rs_a4.jsonl, f_Rs_67.out, g_unitmix.jsonl, g_unitmix_s{1,2}.out
- NOTES_N9b.md; hashes SHA256_N9b.txt (+ .sha256)
