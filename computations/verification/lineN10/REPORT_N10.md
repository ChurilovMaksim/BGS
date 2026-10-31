# Line N10 — modulus (Cauchy–Schwarz) route at level h_p + multi-bump gas for X; REPORT_N8_v2 fixes
Grok Bot, 2026-10-31 (Asia/Yekaterinburg, UTC+5). No push. Earlier lines are untouched: N2's `e_r2_cert.py` and N6's `twb.py` were run read-only, and all output went to N10/logs.
Labels: [P] proved, [P-sketch], [CA] computer-assisted rigorous, [N] numerical, [H] heuristic/model.
Convention: sg = +1 (n_cert conjugate), so w* = 3.43580e-4 + 1.95796e-4 i. sg = −1 is the complex conjugate, and Re and |·| are identical.

## 0. Answers in one paragraph
- **Gas model at finite p [N].** The multi-bump (polymer) picture is confirmed at finite p (p = 29, 47) with exact twists.
  - Two-bump classes α = 1 + s·β·λ^g have activity φ_β = w/w* that is flat in g to 3–4 digits and equal to the background-0 single-bump weights: φ_√2 = c₀ (near-0 class) and φ_2 = c₄ (class z = 0, e = 4) (rank-one collapse).
  - Interactions decay at ≈ 0.40 per λ-step.
  - Three odd bumps → w*³.
- **Resummed level-h_p sum [N/H].** X(p) = 2[e^{pR}(sinh(2p w*) + 1) − 1] with R = 2Σ_c φ_c = 6.185e-5 − 1.943e-5 i.
- **SIGN.** Re X first turns negative at **p = 4287** (4273–4303 under the close-range uncertainty). Over odd p ≤ 2·10⁵ it is negative for ≈ 51% of p. **The Lin/real-part route therefore fails for a positive density of large p** [H, model].
- **MODULUS.** min_p |1+X| = 1.0045, attained at p = 3, over all odd p ≤ 2·10⁵.
  - |X| ≥ 2 already from p = 1065, while Re X > 0 there (arg X = 0.54).
  - G(p) := (|1+X|² − 1)/(2·4p·Re(w*+c₀)) ≥ 1.005 for all p and grows like e^{1.5e-3·p}.
  - |X|/(4p|w*|) ≥ 1.058.
- **So the refutation survives via modulus and gets stronger [H, mod gas model + gap inputs].** The level-h_p deviation is ≥ G(p)·(the N6/N7 Lin value), and G ≥ 1. Under the gas model W′_{3p} cannot stay bounded along m = 3p. That outcome would need the gas model itself to fail at large p (KP tail, §3) or the other levels (gap (b)) to supply a negative term of size ~F_m·G(p).
- **Consistency with the m = 141 number.** At p = 47 the gas changes Re X by +0.61% (0.070637 vs 0.070208). In modulus form the gain is 2ReX + |X|² vs 2ReX, i.e. +4.4%. The +1.07e5 (W′/m at m = 141) moves to about +1.12e5, the same sign and order.
  - Caveat: that number is *not* a direct enumeration. N6 `k_scale` uses ReX = 4p·Re(w*+c₀) for p ≥ 17. The only full enumerations are p ≤ 13 (f_iso). At p = 13 the direct value 0.019429 lies between Lin (0.019419) and gas (0.019492). At p = 13 (k = 6) bumps cannot separate, so p = 13 does not test the gas.

## 1. Modulus form at level h_p [P]
- **Setup.** Dev_{h} = h⁻²Σ_t(|Z + E′_t|² − |Z|²), with E′_t = Z·X + U_t (isotropic phases are 1).
- **Bound.** By Cauchy–Schwarz over t, Dev_h ≥ (n|Z|²/h²)(|1+X+Y|² − 1), with Y = mean_t U_t / Z.
- **What it needs.** Only |1+X+Y| ≥ 1. It never needs Re X > 0.
- **Inclusion of level h_p.** Under the frozen definition (levels d | h with 1 < d ≤ √h are included iff |Z_ρ|²/d² ≥ 4m), level h_p is included for all large p: |Z|²/h_p² ~ (1.9155⁶/λ)^p = 8.5^p, and h_p ≤ √h_{3p}.
- **Cost (honest).**
  - The one-sided trick (dropping positive classes) is lost at level h_p. The uncertified A∞-tail now needs an **absolute** bound |X_tail| ≤ |1+X_gas| − 1 − |Y|.
  - For p ≲ 1000 this margin is ≈ 8p·Re(w*+c₀). Numerically the tail is about 0.6%, and the certified absolute classes total ≤ 0.43%.
  - For p ≳ 1300 the margin is ≥ |X| − 2, which grows exponentially. So the tail budget **loosens** with p.

## 2. Gas at finite p [N] (`code/a_gas.py`, logs a_gas_p29_G10.*, a_gas_p47_G19.*)
- **Setup.** z = ¼, α = 1 + s·β·λ^g with β ∈ {√2, 2, 2±√2, 2√2, 4}, s = ±1, g ≤ 10 (p = 29) and g ≤ 19 (p = 47), plus six 3-odd-bump classes. Twists are exact and Ẑ/Z is computed from TW (L = 8, K = 16).
- **Plateau activities φ = w/w*** (g = 8..12, p = 47; p = 29 agrees):

  | type | φ |
  |---|---|
  | √2 | 2.9869e-5 − 6.606e-6 i |
  | 2 | 1.0445e-6 − 3.119e-6 i |
  | 2√2 | 1.38e-8 + 1.11e-8 i |
  | 4 | −2.03e-9 − 9.1e-10 i |

  - These equal the background-0 single-bump weights c₀ = 2.9866e-5 − 6.599e-6 i and c₄ = 1.0413e-6 − 3.1164e-6 i: rank-one collapse, *same activity in both backgrounds*.
  - The 2±√2 types are √2 at odd ε-positions.
- **Interaction.** |φ(g) − φ∞|/|φ∞| falls 9.0e-3 → 3.6e-3 → 1.44e-3 (g = 6, 7, 8): ratio 0.40 per step, matching (0.769/1.915) = 0.4016.
  - At g = 1–3 it is O(1). These are merged classes, e.g. 1 − √2λ = −3ε, which is a new odd single bump.
  - The close-range correction to the odd activity is S = −4.3e-4 − 1.84e-3 i (|S| = 1.9e-3).
- **Three odd bumps.** φ_tri/w*² = 0.95 at (4,9) and 0.92 at (5,15), tending to 1, so w → w*³. At gap 3 the factor is ≈ 1.8.
- **Position count.** g runs over Z/p (λ^p ≡ 1 on the line, ε^p ≡ σ). Per line there are p ε-positions with signed coefficients, which gives 2p family points per line and 4p on the two lines (as in N6).

## 3. Generating function and KP [H; structure P-sketch]
- **Generating function.** Per line, X_line = ½σ[(1+R+2φ₁)^p − (1+R−2φ₁)^p] + [(1+R)^p − 1], with φ₁ = σw*. This gives **X = 2[e^{pR}(sinh(2p w_o) + 1) − 1]**, where w_o = w*(1+S) and R = 2Σφ_c.
  - The sinh part is background ¼ with parity "odd number of odd bumps".
  - The e^{pR} − 1 part is background 0.
  - Small p gives 4p(w* + c₀ + c₄), which matches the N6 p ≤ 13 enumerations to ≤ 3e-3 relative.
- **Results** (`code/b_genfun.py`, logs/b_genfun.json, b_genfun_ext.out; rows for nominal and w_o = w*(1±S)):

  | p | X | |X| | G |
  |---|---|---|---|
  | 1165 | 1.89 + 1.18i | 2.23 | 2.5 |
  | 4221 | 0.60 + 23.5i | | 44 |
  | 5001 | −11.4 + 40.3i | | 116 |
  | 8001 | −394 + 65i | | 6.6e3 |
  | 10001 | −1497 − 983i | | 1.1e5 |

  Re X < 0 first at p = 4287 (4273 / 4303).
- **Analytic half [P mod model].** |X+2| = 2e^{pReR}|sinh(2pw_o) + 1| ≥ 2e^{pReR}(sinh(2p·Re w_o) − 1). This gives |1+X| ≥ 1 for all p ≳ 1270. Below that, arg X < π/2 [N], so Re X > 0.
- **KP convergence.**
  - Per-position activity Σ|φ| ≈ 6.8e-5 (even) + 2|w*| (odd). Pair interactions are ≤ C·0.40^g with C = O(20) at g ≤ 3 (merged classes are counted as their own polymers).
  - The KP criterion Σ_{polymers ∋ 0}|z_γ|e^{a|γ|} ≤ a then holds with a = 1e-2 **for the measured polymer types** [N].
  - **Open:** KP needs Σ over *all* single-bump types c (arbitrary depth/norm) of |φ_c|e^{a·len(c)} < ∞, uniformly in p, together with the interaction bound for deep bumps.
    - This is exactly the A∞-tail / hypothesis-G input (absolute form, all slow time counted).
    - N8b's caveat applies too: at short windows |r| exceeds the w-limit by 10³–10⁴.
  - Not proved here. Status: KP convergence is [H].

## 4. Does the refutation survive? (the question as asked)
- **Lin route.** Dead for p ≥ 4287 (density ≈ ½) [H, model]. A p-uniform A∞ in real-part form is false under the gas model.
- **Modulus route.** Survives. Dev_{h_p} ≥ F_m·G(p)·(1 − tail − Y), with G ≥ 1.005 and G → ∞; F_m ≥ 2.32e-3·p|Z₈|²/h_p (N8b-F2 improvement, composite loss ≤ 0.52%).
- **Can W′_{3p} stay bounded?** Under the gas model, no. R′ along m = 3p would need one of two things:
  - (i) gas/KP failure at large p, meaning the deep-bump activities are not summable, which contradicts all measured decay; or
  - (ii) a negative contribution of size ~F_m·G(p) from other levels. The trivial floor bounds levels d > L* by δF_m [P], so this would have to come from gap-(b) levels.
- **Form of R′.** Disproof = W′_m/m bounded away from 0 along a subsequence (parent, TRACE-206). The modulus bound holds for *every* odd p in the model, not just a sparse set. So "infinitely many p" costs nothing extra here, and prime h_p is not needed for F_m.
- **Overall status.** [H] for the large-p behaviour. [P] for the CS inequality. [N] for the activities.

## 5. REPORT_N8_v2 (referee /workspace/audit/lineN8/REPORT.md)
- **F6 (required).** Short-block r₂(k), certified with N2's e_r2_cert (arb, Collatz–Wielandt, prefactor included) [CA]. Log: `logs/e_r2_cert.jsonl`.

  | k | 8V | 8E | 16V | 16E |
  |---|---|---|---|---|
  | 8 | 2.456 | 1.548 | 3.195 | 2.478 |
  | 10 | 2.072 | 1.432 | 2.558 | 2.087 |
  | 12 | 1.851 | 1.360 | 2.206 | 1.862 |
  | 16 | 1.607 | 1.275 | 1.833 | 1.614 |
  | 20 | **1.4759** | 1.226 | 1.640 | 1.4813 |
  | 30 | 1.318 | 1.165 | 1.414 | 1.321 |
  | 50 | 1.204 | 1.118 | 1.256 | 1.206 |
  | 100 | 1.125 | 1.084 | 1.149 | 1.126 |

  - **Corrected claim.** The r₂ input is < 1.481 only for blocks of k ≥ 20 (8V), ≥ 10 (8E), ≥ 30 (16V) and ≥ 21–30 (16E; 1.48126 at k = 20 is marginally above).
  - Cores shorter than this (N(e) ≲ λ^{10} ≈ 4e7 for 8V, i.e. about 10⁷ classes) need another route, such as the sup-norm majorant. They cannot be handled by individual certificates.
  - "r₂ is not the bottleneck" is withdrawn.
- **F8.** p16 = 339 with the two-term bound 706·1.63541^m + 2.27e5·0.95^m. The figure 498 is dropped; it applies only to the crude single-constant form.
- **F3.**
  - R₂(a) recomputed directly as Line F full_R(RA_r2, 1) = (RA+1)(1+‖X‖)+1 (`code/f3_r2direct.py`, logs/f3_r2direct.json). For a = 0/2/6 this gives 369.36 / 739.9077 / 739.9077, within 1e-9 relative of N8's (conservative) values.
  - Sector 4 uses the two-block b21 route (unchanged).
  - The E-family (certE) absorption was not run: [P-sketch].
- **F7 (derivation).**
  - (i) Line Parseval: Σ_{x∈line}|Ẑ_x|² equals q times a coset sum, with q = h_p ≈ λ^{p/2}/2. The normalisation per λ-step is therefore λ^{1/2}.
  - (ii) The family core sits at the dominant eigenvalue (Prop X′), so its |Ẑ|² grows by μ*² per step.
  - The aliased family mass per step is μ*²/λ^{1/2} = 3.66903/2.41421 = **1.5198**. The threshold μ*³/(Λλ^{1/2}) = 1.4810 is smaller by exactly μ*/Λ = 0.9745.
  - Hence family/threshold = Λ/μ* = 1.026 > 1, and shells must exclude the family [P-sketch].
- **F9.** The bases z = √2/8 and ¼+√2/8 (mixed backgrounds) are negligible: shallowest classes have N = 14, |r| ≤ 1e-24 at p = 29 and ≤ 7e-39 at p = 47 [N, N9 a_bases; referee 8.6e-25]. They lie in the A∞-tail by definition. The base-0/¼ numerics are unaffected.
- **Adopted.** F_m ≥ 2.32e-3·p|Z₈|²/h_p (every prime r | h_p has r ≡ 1 mod 2p [P], so the composite loss is ≤ 0.52%).

## 6. Open items (unchanged in kind, sharpened)
- (a) KP tail = absolute summability of deep single-bump activities, which is the absolute A∞-tail / G for bumps.
- (a′) Short cores (8V, k < 20) for the shell route.
- (b) Gap (b)/(b′). Its budget loosens by G(p) at large p.
- Y (unit points) must satisfy |Y| < |1+X| − 1. That is Theorem C′-small for p ≲ 1000 and trivially satisfied beyond.
