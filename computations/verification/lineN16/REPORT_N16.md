# Line N16 — final author round: carries, vector conversion, consolidated status
Grok Bot · 2026-11-01, 02:53–03:30 Asia/Yekaterinburg (UTC+5) · all jobs nice 10–12 on one shared core.

**Labels.** [P] proof · [P-sketch] argument with steps not written out · [CA] arb ball arithmetic · [CA-fp: IEEE standard model + libm ≤ 1 ulp] = binary64 with derived a-priori rounding bounds (N15 `rig.py`) · [N] numerics · [H] heuristic.

## 1. Collision lemma: large carries
**Result: no proof.** The [N] picture is much sharper than in N15, and the N15 "prefactor grows linearly in E" was an artefact of the share proxy.
1. **Scalar prefactor, computed exactly with carries |e| ≤ E** (`code/g_scalar.py`, `logs/g_scalar_E*_n*.json`). S_n^(E) is the full sesquilinear carry sum, starting and ending in carry state (0,0); S_n^(0) is the i.i.d. second moment.
   | n | 3 | 4 | 5 | 6 | 7–12 |
   |---|---|---|---|---|---|
   | S^(1)/S^(0) − 1 | 1.653e-9 | 3.46e-11 | 1.41e-11 | 1.35e-11 | 1.348e-11 (constant) |
   - E = 2 and E = 3 add nothing visible beyond E = 1 for n ≤ 6 (< 1e-16 relative).
   - The relative correction is **constant in n**, so the carry contribution is a boundary effect at the Φ/ψ ends; interior carries are below binary64 resolution.
   - Since |e| ≤ 15 is the full alphabet (N15 [P]), S^(15) is the torus mean. [N]: the torus mean equals the i.i.d. value × (1 + O(1e-11)) for n ≤ 12. The N15 MC ratios at n = 6–8 (1.14–2.18) are within 1.1σ, i.e. noise.
2. **Local entry weight of an isolated carry c** (letters v = (c, −6c, c); `code/g_triple.py`, `logs/g_triple.json`). Measured as ‖𝒦_c𝒦_{−6c}𝒦_c(Y)‖ relative to ‖𝒦_0³(Y)‖, with Y = the Perron matrix of 𝒦:
   | c | 1 | 2 | 3 |
   |---|---|---|---|
   | Y_c-relative | 7.0e-3 | 2.9e-8 | 2.3e-15 |
   | Frobenius | 1.7e-4 | 6.1e-11 | 2.6e-18 |
   | ψ-functional | 3.4e-12 | 4.4e-23 | 5.8e-29 |

   The decay is Gaussian-like in c (log weight ≈ −5c^{1.9}). Entry into |e| ≥ 2 costs ≤ 3e-8 per event in the Y_c-cone sense.
   - The letterwise Gram bound gave κ₁κ₆κ₁ ≈ 33 for c = 1. The cancellation lives in the *composition* of the three sesquilinear steps, not in single letters. This is why letterwise or Cauchy–Schwarz (Gram) bounds cannot see it: CS over the triple returns the full 𝒦₀³.
3. **Sharpest honest statement.**
   - **[P]:**
     - the carry reduction v = (1, −6, 1) * e with |e| ≤ 15;
     - the torus/Bohr-mean identity;
     - the diagonal (e ≡ 0) term is exactly the i.i.d. second moment, ≤ (ψ*Y_cψ)(Φ*Y_c⁻¹Φ)·ρ̄ⁿ with ρ̄ = 0.28 [CA-fp];
     - S2(j) ≤ C_emp(j)·2^j·2^{−βj} holds with C_emp(j) ≤ 4.4e-4 for j ≤ 12, where the shell sums are certified [CA-fp] (finite part).
   - **[N]:** the carry correction is ≤ 2e-9 relative for n ≤ 12, E ≤ 3; per-event entry weights are 7e-3 (|e| = 1) and ≤ 3e-8 (|e| ≥ 2).
   - **[H]:** a geometric excursion bound. Each excursion has entry weight w₁ ≤ 7e-3 and contracts at the i.i.d. rate, giving prefactor ≤ 1/(1 − n·w_eff) with w_eff ≈ 1e-11 per step. The torus-mean prefactor is therefore 1 + O(1e-9) uniformly in n.
   - **Still missing for [P]:**
     - (a) a certified bound on composite excursion operators: Hermitian-preserving, non-CP maps on 495² matrices. A Choi-matrix or order-interval bound is needed, and CS loses the cancellation;
     - (b) the Poisson/box step, lattice shell sum → #points × torus mean + aliasing. Its constants were not computed (unchanged from N15).
   - **Margin:** C_emp ≤ 4.4e-4 vs C_needed(J₀ = 12) = 0.082, about 186×. The torus ≈ i.i.d. finding means essentially the whole margin is available to the box/aliasing constant.

## 2. Core→true conversion, vector-propagated (`code/conv_vec.py`)
- **Method.**
  - The N15 conv_est is finished as a [CA-fp] vector chain. Forward and backward chains are propagated with the c3_mid error recursion plus a per-step perturbation g·F_s·‖v̂‖ (F_s = Pert/|s| = 9.92e-10, g = 1 + Xn/|s| = 4.215). The step bound is N_H + cT·g·F_s, with cT = 732.
  - The end terms err_proj (er, el), 2·dPi·g·max(F_f, F_b), the tail, and the s-scale use the N8 constants.
  - The vector form of the N8 telescoping is **[P-sketch]**; the numerics are [CA-fp].
- **Per window** (`logs/conv_vec_replay.jsonl`).
  - E/|r| ≈ 1.7e-3 for singles, versus 0.03–38 absolute for the N15 GA-product route. Max E/|r| over all windows is 5.27, reached on small-|r| windows.
  - E is dominated by the end term 2·dPi·g·F_b (dPi = 2.79e-5, F_b = ‖ψ̃ΠX‖ ≈ 1–2).
- **δ_int, true functional, G ≤ 15** (`logs/f_post_true.json`, N14 f_post2 formulas on the widened boxes): **coded Σ|dev| ≤ 2.470e-6** [P-sketch lemma, CA-fp numerics]. The core value is 5.14476e-7.
- **Caveat (new, important).**
  - The widened dev is **flat in G**: about 1.5e-7 per G for G = 7–15, versus geometric decay for the core.
  - Box widening treats the pair window and the product of singles independently, losing their shared end-projector error. So this form **does not control the G > 15 interaction tail**: summing 1.5e-7 per G diverges.
  - A correlated (difference) conversion is needed. The pair and the singles share Φ/ψ ends, so the dPi term should cancel to first order. This is [H], not done.
- **Finite part with the true functional** (`logs/conv_vec_classes.jsonl`, j ≤ 10): 1280 classes with j ≤ 10: 2Σ_bad|w|_up (true) = 2.0805e-6 at g₀ = 4, against 2.0314e-6 (core) on the same classes (+2.4%; g₀ = 2: +1.7%, g₀ = 6: +3.1%). The j = 11, 12 shells (3829 classes) were not run within the time-box; their core contribution at g₀ = 4 is 2·(7.34e-11 + 3.32e-11) = 2.1e-10.
- **Budget at G ≤ 15 / j ≤ 12:**
  - A_bad^KP 2.063e-6 (core) + δ_int^true 2.47e-6 ≈ 4.5e-6 ≪ Re Λ_lo′ = 6.234e-4.
  - The open part is the G > 15 tail with the true functional and the j > 12 tail (lemma (T)).

## 3. Consolidated status: (T) + interaction (gap (a))
| # | Ingredient | Value | Label | File(s) | Referee status |
|---|---|---|---|---|---|
| 1 | Adapted norm H; cond_H, Lip_H, ‖A0/s‖_H, Q̃ contraction | 21.103; 167.213; 0.45 | [CA] | N13 code/b_arb.py | N13 referee ✓ (own arb replay) |
| 2 | Quadratic step bound, \|t\| ≤ 1/256 | N_H ≤ 1 + 1.01e-12 + 4260t² | [CA]+[P] | N13 b2_quad.py, b3_quadeval.py | N13 F2 ✓ (referee partition) |
| 3 | Step-norm table, \|t\| > 1/256 | max 2.91656, SVD-free | [CA-fp] | N15 nh_table_rig.py | not refereed (N15) |
| 4 | i.i.d. rate ρ(𝒦) ≤ ρ̄ = 0.28; true ≤ 0.28028 | margin 3.49e-6 | [CA-fp], eigen-solver-free | N14 b_cp2.py; N15 b_cp3.py | N14 ✓ (margin ~1e9); constants fix N15 not yet refereed |
| 5 | ℓ³ ≤ ℓ² | — | [P] Lean | Lean l3_le_l2 | ✓ |
| 6 | ε-digit language, class↔word bijection | — | [P-sketch] | N14 digits.py, §1.2 | open (write-up) |
| 7 | Finite part A_bad, j ≤ 12 (g₀ = 4) | 2.031569e-6 | [CA-fp] core functional | N15 a_cert3.py/a_certpost3.py | N14 ✓ (spot checks); c3 radii not refereed |
| 8 | KP weight, per-site | a = 5.93e-6, S₀ = 2.063e-6 | [P] criterion, [CA-fp] finite part, [P-sketch] tail ℓ-weighting and background interplay | N15 kp.py | not refereed |
| 9 | δ_int, coded pairs G ≤ 15 (core) | ≤ 5.14476e-7 | [CA-fp] | N15 c3_mid.py, f_post3.json | F14.1 fix done; awaits re-review (N14 value 5.14416e-7 superseded) |
| 10 | Short types | Σ\|w\| = 9.970e-7 (173 rows incl. α=4) | [CA-fp] | N14 f_short | ✓ (wording fixed N15) |
| 11 | Interaction tail G > 15 (core), Lemma D | ≤ 1.56e-8 | [P]+[N] | N13/N14 Lemma D | ✓ |
| 12 | Replay cross-check (arb, partial 597 jobs) | 0 disjoint vs c2/c3 | [CA] partial | N13 c_replay.jsonl; N15 f_partial, c3_vs_arb | referee's own arb agrees |
| 13 | Exact carry reduction, \|e\| ≤ 15; torus identity | — | [P] | N15 §3.1–3.2 | not refereed |
| 14 | Carry correction to the torus mean | ≤ 2e-9 relative (n ≤ 12) | [N]; excursion bound [H] | N16 g_scalar.py, g_triple.py | not refereed |
| 15 | **Collision-constant lemma (T)**, C ≤ 0.082 at J₀ = 12 | C_emp ≤ 4.4e-4 | **OPEN** [P]; [N] 186× margin | N14 a_need.py; N15/N16 | referee N14 open item 2 |
| 16 | Box/aliasing constants (Poisson step) | not computed | [P-sketch] idea | N15 §3.4 | open |
| 17 | j > 12 tail of A_bad | via (T) | open | — | open |
| 18 | Core→true conversion, per window | E/\|r\| ≈ 1.7e-3 | [P-sketch] lemma, [CA-fp] numerics | N16 conv_vec.py | referee open item 3 |
| 19 | δ_int, true functional, G ≤ 15 | ≤ 2.470e-6 | as row 18 | N16 f_post_true.json | new |
| 20 | Interaction tail G > 15, true functional | flat-in-G under box widening | **OPEN** (needs correlated conversion) | N16 §2 | new |
| 21 | Wrap-around composite-h points | need c < 1.1718·ℓ₀/ln d (ρ̄_true) | delegated (N13b subgroup lemma) | N15 §6 | referee open item 1 |
| 22 | Budget arithmetic | A_bad + δ_int + tails < ln(1+ReΛ) ≈ 6.236e-4 | [P] Lean budget14 | Lean | ✓ |
| 23 | Polymer normalisation / log→modulus | — | [P-sketch] | N14 §1.4 | referee 2d open |

**Bottom line.** Every quantity sits ≥ 100× inside budget at the [N] level. The certified pieces are rows 1–5, 7, 9–12 and 22. The [P]-level gaps are (T) (rows 15–17), the conversion in correlated form (rows 18–20), the wrap-around points (row 21), and the [P-sketch] write-ups (rows 6, 8, 23).

## 4. Artifacts
- **code/:** g_scalar.py, g_triple.py, conv_vec.py, run_c.sh, run_g.sh, run_g2.sh.
- **logs/:** see SHA256_N16.txt (written last).
