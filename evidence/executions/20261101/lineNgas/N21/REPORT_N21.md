# REPORT N21: closing H4 (core→true conversion of the interaction constant)

Grok Bot, 2026-11-01, 09:00–09:55 (UTC+5). Work directory `/workspace/bgs-lineN/N21`. The repo `lineNgas/repo` was read only, and no other line's files were modified.
Tags: [P] proof, [P-sketch], [CA] arb-certified, [CA-fp] float with the IEEE standard rounding model, [N] numerical evidence, [H] heuristic.

## 0. Result

| item | value | label |
|---|---|---|
| **Lemma C**: two-sided vector-form core→true conversion per window, *including the second-order dPi² term* | statement and proof in §2 | **[P]** (inputs: N8/N13/N15 certificates) |
| δ_true, coded pairs G ≤ 15 (1350 pairs, N14 f_post2 formulas, arb) | **≤ 2.2101666e-6** (N16: 2.470e-6) | [P] lemma + [CA-fp] boxes |
| δ_true, 16 ≤ G ≤ 36 (box widening, 2100 pairs) | ≤ 2.7126552e-6 (flat ≈ 1.29e-7 per G) | [P] + [CA-fp] |
| **Lemma Q + Lemma D^T** (true-operator difference form), G ≥ 37 | ≤ 1.0842558e-7 (G = 37..60) + 3.04e-13 (G > 60, geometric, arb) | [P] + [CA] constants + [CA-fp] anchors; sums in arb |
| **δ_true (all G)** | **≤ 5.0313e-6** | [P] + [CA-fp] |
| crossover p₁ (N19b logic, exact K_p) | all integers p ≥ **1397**; **first prime 1399 (unchanged)**; no violations among primes up to 5000; monotonicity holds | [P-arith] |
| Lean `lean/LineN21Arith.lean` | 24 theorems, EXIT 0, no sorry, no native_decide | [P] arithmetic |

**H4 status: closed at the [P] + [CA-fp] level**, the same standard v4 already uses for H2 (δ_int^core). It is not closed at pure [CA]: the window chains are float with a rigorous rounding model, not arb. The proof still needs an independent referee audit (§7) before claim 322 can move to verified.

## 1. What changed relative to N16 (findings)

- **F21-1.** N15/N16 converted H-norm sub-product bounds to the 2-norm with √cond_H. The correct factor is cond = c_hi/c_lo = 21.103, because cond is already a ratio of norms and not of squared norms. In N16 this only touched a ~1e-20 term, and the N15 H-product route was vacuous anyway. Fixed in Lemma C (GA uses cond).
- **F21-2 (new, important for any G ≥ 22 work).** `N14/code/digits.py` sets `mp.dps = 34`. For pair windows with |e| ~ λ^G the twists lose precision. The relative error is 1.7e-16 at G = 22, 1.5e-11 at G = 30 and 6e-4 at G = 40 (checked against dps = 150). G ≤ 20 is exact, so all v4 numbers (G ≤ 15) are unaffected. N21 runs use dps = 160. The first G ≥ 16 run used dps = 34; it was discarded and kept in `logs/discarded_dps34/`.
- **F21-3 (N16 conv_vec, superseded by Lemma C):**
  - el/er were paired the wrong way round in err_proj, and ψ was unnormalised (|ψ| = 6.52). The effect is ~1e-11.
  - The per-step injection used ‖v̂_{k−1}‖, but the lifted far component depends on c_{k−2}.
  - err_dPi = 2·dPi·g·max F is not a valid vector bound. The correct form carries ‖ψ_T‖·‖Φ_T‖ ≈ 22 and a τ term.
  - The radius·scale term was missing, and so was the dPi² term.
- **F21-4.** N16-2 diagnosed the pair error as "93% per-step perturbation". That was an artefact of the one-sided (GA-weighted) injection bound. With the two-sided telescoping (C2) the per-step term is tiny: median 2.3e-8 per pair window. The binding term is now the first-order projector mismatch dPi·(‖ψ_T‖‖PΦ_T‖ + ‖Φ_T‖‖ψ_T P‖) + τ|Tr Π_T P|, with median 4.4e-4.
- Lemma C error E/|r|: singles 1.9e-3 to 3.7e-3; pair windows median 5.2%, max 3.1 (N16: 8% and 5.27).

## 2. Lemma C (two-sided vector conversion) [P]

**Setting** (N8 [CA], N13 [CA]):
- ℋ = core ⊕ far, with L_d = T_d + E_d, T_d = [[A_d, 0], [X_d, 0]], ‖E_d‖ ≤ Pert = 1.901e-9 and ‖X_d‖ ≤ Xn = 6.159.
- L_0 has a simple Perron eigenvalue μ with |μ − s| ≤ mus = 2e-6. Its projector is Π, with ‖Π − Π_T‖ ≤ dPi = 2.7938e-5, where Π_T is the spectral projector of T_0 at s.
- A window has twists d_1..d_n. Write ℒ_k = L_{d_k}/s, 𝒯_k = T_{d_k}/s, ℰ_k = E_{d_k}/s (so ‖ℰ_k‖ ≤ Fs = Pert/|s|), P = ℒ_n⋯ℒ_1, P^T = 𝒯_n⋯𝒯_1, and 𝒜 = Â_n⋯Â_1 with Â = A/s.
- True window value: r_true = ψ_μ R₊ (s/μ)^n P R₋ Φ_μ, where Π = Φ_μψ_μ and R± are the outside products of L_d/μ.
- Core value: r̂, with |r̂ − ψ̃𝒜Φ̃/(ψ̃Φ̃)| ≤ rad (N15 c3 recursion, [CA-fp]).

**Statement.**

  |r_true − r̂| ≤ rad + C1 + C2 + C3 + TrΠ·C4 + (1 + C4)·C5

with:
- C1 = (EL·F_n + B_0·ER + EL·ER·GA)/den1 + (|r̂| + rad)‖ψ̃‖ER/den1
- C2 = (Fs/den1) Σ_{k=1}^n β_k φ_k
- C3 = [dPi‖ψ_T‖·VPf + dPi‖Φ_T‖·VPb + **dPi²‖ψ_T‖‖Φ_T‖·GL** + τ·TP]/(den1 − τ), where τ = dPi‖ψ_T‖‖Φ_T‖ < 6.1374e-4 (Lean `tau_lt`)
- C4 = (1 + mus/(|s| − mus))^n − 1
- C5 = η‖ψ_μ‖‖PΦ_μ‖ + η‖ψ_μP‖‖Φ_μ‖ + η²‖ψ_μ‖‖Φ_μ‖·GL, with η = expm1(Cpow·2πN1·tail/|μ|)

and:
- TP = |r̂| + rad + C1 + C2 and TrΠ = TP + C3
- F_k ≥ ‖𝒜_{≤k}Φ̃‖ and B_k ≥ ‖ψ̃𝒜_{>k}‖ (c3 forward and dual recursions)
- GA = cond·∏ max(1, N_H(d_k)), which bounds every contiguous core sub-product
- GT = (1 + xs)GA and GL = GT(1 + Fs·GT)^n
- b_k = B_k + EL·GA and β_k = b_k + max(b)·((1 + Fs·GT)^{n−k} − 1)
- u_k = F_k + GA·ER and φ_k = (u_{k−1}² + xs²u_{k−2}²)^{1/2}, with φ_1 = (1 + xs²)^{1/2}u_0
- VPf = φ_{n+1} + Fs·GL·Σφ_k and VPb = β_0

**Proof.**
1. *T-structure.* 𝒯_k(v_c, v_f) = (Â_k v_c, X̂_k v_c), so P^T ignores far input. ψ_T = (ψ_A, 0) and Φ_T = (Φ_A, X̂_0Φ_A) are the left and right s-eigenvectors of T_0. Hence ψ_T P^T Φ_T = ψ_A𝒜Φ_A and Tr(Π_T P^T) = Tr(Π_A𝒜) exactly.
2. *(C1)* Normalise Φ_A = Π_AΦ̃ and ψ_A = ψ̃Π_A, so Π_A = Φ_Aψ_A/(ψ̃Π_AΦ̃). Then:
   - ψ_A𝒜Φ_A − ψ̃𝒜Φ̃ = −(ψ̃ − ψ_A)𝒜Φ̃ − ψ_A𝒜(Φ̃ − Φ_A);
   - ‖Φ̃ − Φ_A‖ ≤ ER and ‖ψ̃ − ψ_A‖ ≤ EL (N15 residual formula, [P]);
   - |ψ̃Π_AΦ̃ − ψ̃Φ̃| ≤ ‖ψ̃‖ER, and den1 ≤ |ψ̃Π_AΦ̃|.
   The quotient rule gives C1.
3. *(C2)* P − P^T = Σ_k P_{>k} ℰ_k P^T_{<k}. Then:
   - ‖P^T_{<k}Φ_T‖ ≤ φ_k: the core part is ≤ u_{k−1} and the far part ≤ xs·u_{k−2}.
   - ‖ψ_T P^T_{>k}‖ ≤ b_k.
   - The true covectors satisfy ‖ψ_T P_{>k}‖ ≤ b_k + Σ_{j>k} ‖ψ_T P_{>j}‖·Fs·GT, with ‖𝒯-sub-product‖ ≤ (1 + xs)GA. Discrete Gronwall gives β_k: induction using Σ_{j>k}(q − 1)q^{n−j} = q^{n−k} − 1.
4. *(C3)* Π has rank one and c := ψ_TΠΦ_T ≠ 0, so Π = ΠΦ_Tψ_TΠ/c and Tr(ΠP) = ψ_TΠPΠΦ_T/c. Write Π = Π_T + Δ with ‖Δ‖ ≤ dPi. Then:
   - N − ψ_TPΦ_T = ψ_TΔPΦ_T + ψ_TPΔΦ_T + **ψ_TΔPΔΦ_T**;
   - |c − ψ_TΦ_T| ≤ τ;
   - ‖PΦ_T‖ ≤ VPf (same telescoping), ‖ψ_TP‖ ≤ VPb and ‖P‖ ≤ GL.
   The quotient rule gives C3. The third term is the second-order term that the claim-322 closure condition requires; here it appears as dPi²‖ψ_T‖‖Φ_T‖‖P‖.
5. *(C4)* |(s/μ)^n − 1| ≤ (1 + |s − μ|/|μ|)^n − 1.
6. *(C5)* Duhamel on each tail, using ψ_μ(L_0/μ)^k = ψ_μ and sup_k‖(L_0/μ)^k‖ ≤ Cpow [CA, N8], gives ‖ψ_μR₊ − ψ_μ‖ ≤ ‖ψ_μ‖η, and the same for R₋Φ_μ. Also ‖Φ_μ‖ ≤ ‖Φ_T‖(1 + dPi) and ‖ψ_μ‖ ≤ ‖ψ_T‖(1 + dPi)/(den1 − τ).
7. Summing the chain r̂ → ψ̃𝒜Φ̃/ψ̃Φ̃ → Tr Π_A𝒜 = Tr Π_TP^T → Tr Π_TP → Tr ΠP → Tr Π(s/μ)^nP → r_true gives the statement. ∎

Implementation: `code/conv_c.py` (constants printed at the top of every log). Numerics are [CA-fp]: IEEE standard model, libm ≤ 1 ulp, as in N15.

## 3. G ≤ 15 and box widening [P + CA-fp]

- `conv_c.py replay` reruns all 1560 N15 jobs (logs `convC_replay_p{0,1}.jsonl`). `f_postC.py` applies the N14 f_post2 formulas in arb, giving **Σ_{G≤15}|dev| ≤ 2.2101666e-6**.
- `conv_c.py ext 16 60` gives box values for G = 16..44, 100 pairs each. Sum for 16..36: 2.7126552e-6. This is flat at ≈ 1.29e-7 per G, the floor set by the C3 box widths, so box widening alone cannot control G → ∞.

## 4. Lemma Q and Lemma D^T (true-operator difference form) [P]

**Lemma Q.** For k ≥ 0 and Q = I − Π:

  ‖(L_0/μ)^k Q‖ ≤ m(k) := |s/μ|^k m_T(k) + Rem·|μ|^{−k}

where:
- m_T(k) = cond(κ'^k + xs·κ'^{k−1}) for k ≥ 2, m_T(1) = cond·κ' + xs‖Q_A‖, and m(0) = 1 + ‖Π‖;
- κ' = 0.45(1 + η) + (1 + η)·cond·δ_Q < 0.45000047. This uses N13 V3b [CA] with Q̃ → Q_A, ‖Π_A − Φ̃ψ̃‖ ≤ δ_Q = 8.87e-10;
- Rem = S_T²·Pert/(1 − Pert·S_T) < 1.591e-3 and S_T = sup_{|z|=1}‖(z − T_0)^{−1}‖ < 914.8.

*Proof.*
1. (T_0/s)^kQ_T acts as ((A/s)^kQ_A v_c, X̂(A/s)^{k−1}Q_A v_c), and ((A/s)Q_A)^k is ≤ κ'^k in the H-norm (×cond for the 2-norm).
2. R_A = Π_A/(z − s) + Σ_k A^kQ_A z^{−k−1}, with |s|κ' < 0.862. This gives ‖R_A‖ < 146.44; then ‖R_T‖ ≤ (‖R_A‖² + (Xn‖R_A‖ + 1)²)^{1/2}.
3. Line F (F2 [CA]): L_0 has no spectrum in |z| ≥ 1 besides μ. Hence L_0^kQ − T_0^kQ_T = (2πi)^{−1}∮_{|z|=1} z^k R_T E R_L dz, with ‖R_L‖ ≤ S_T/(1 − Pert·S_T). ∎
4. Constants: K_0 = sup_k‖(L_0/μ)^k‖ ≤ ‖Π‖ + max_k m(k) < 56.78. Lean: `kap_up` … `K0_up`.

**Lemma D^T.**
1. *Twist splitting* [P]. For a pair (i, j, G, h, σ), the composite twist satisfies d_t ≡ d^i_t + d^j_{t+G} (mod 1), where d^j is the single chain of σe_jε^h. Proof: the seeds are linear in e, conj(λ) = λ^{−1}, and both window conventions agree mod 1 because Tr(zλ^t) ∈ ℤ.
2. *Cut.* Cut at c = −D_i, with D_i = ⌊G/2⌋ and D_j = G − D_i. Let R, L be the composite products for t ≥ c and t < c, and R^i, L^j the single products. With a_i = ψ_μR^iΦ_μ, α_i = ψ_μR^i(L^i − I)Φ_μ, b_j = ψ_μL^jΦ_μ, β_j = ψ_μ(R^j − I)L^jΦ_μ:

   r_ij − r_i r_j = ψ_μR^i Q L^jΦ_μ + ψ_μ(R − R^i)LΦ_μ + ψ_μR^i(L − L^j)Φ_μ − (α_i b_j + a_iβ_j + α_iβ_j)

3. *Main term.* |·| ≤ Y_i(D_i)·X_j(D_j). Duhamel from an anchor D0 (minimised per seed) gives:

   Y(D) ≤ W^R(D0)·[m(D − D0) + K_0e^{K_0σ}ℓ|e1| Σ_{t=−D}^{−D0−1} λ^t m(t + D)]

   and similarly for X. Here ℓ = 2πN1/|μ|. The anchors W^R = ‖ψ_μR_{≥−D0}‖ and W^L = ‖L_{<D0}Φ_μ‖ come from the Lemma C arrays (β_k and φ_k, plus the dPi, GL·η and scale corrections).
4. *Cross and normalisation terms.* Each carries σ_δ ≤ ℓ|e|λ^{−G/2}/(1 − 1/λ). They are bounded by Gronwall with:
   - covector and vector sup bounds Ψ^max and Φ^max from the chains, rather than operator norms;
   - Γ = K_0²e^{K_0σ}GL(1 + C4) used only inside the factors 1/(1 − Γσ_δ) and Y·Γσ_δ.

   The term crossL is bounded on the covector side, ψ_μR^i = a_iψ_μ + ψ_μR^iQ. This removed a Γ_j that had made the first version 70× worse.
5. *dev.* dev = |x³ − y³| ≤ |x − y|(|x|² + |x||y| + |y|²), where |x − y| ≤ Δ_A|y_B| + |y_A|Δ_B + Δ_AΔ_B. It uses W(σe) = W(e) [P, N6 symmetry], as in f_post2.
6. *Remainder for G > GMAX.* m(k) ≤ M_ρρ^k with ρ = 0.5225, because 1/|μ| < ρ, |s/μ|κ' < ρ and λρ > 1 (Lean `rho_*`, `lam_rho`). Every cross term scales like ≤ λ^{−(G−GMAX)/2}. Both geometric sums are evaluated in arb.

Results (`code/tail_DT.py`, arb, prec 80):
- Anchors with KK = 16 (`logs/tail_DT_36_60_KK16.json`): T(37) = 6.17e-8, T(38) = 2.69e-8, T(39) = 1.10e-8, T(40) = 4.94e-9; ratio ≈ 0.44 per G. Σ_{37..60} ≤ 1.0843e-7 and remainder ≤ 3.04e-13.
- Cross-check with KK = 18 for G = 40..200 (`tail_DT_40_200.json`): Σ = 8.83e-9 and remainder 1.0e-52; the per-G values agree with KK = 16 to 4 digits.
- The analytic bound beats the box for G ≥ 37 (T(36) = 1.83e-7 > 1.29e-7).

**Sanity check [N]** (`logs/sanity_mid.json`): the float midpoint interaction decays at rate 0.38 (8.1e-13 at G = 16, 1.1e-18 at G = 30), reaching the float floor ~1e-20 at G ≥ 35. All certified bounds lie above it: analytic 4.9e-9 at G = 40, box 1.29e-7.

## 5. Final δ_true and crossover

`code/final_delta.py 36` (arb sum of stored upper bounds) and Lean `delta_true_sum`:

  δ_true ≤ 2.2101666e-6 + 2.7126552e-6 + 1.0842558e-7 + 3.04e-13 < **5.0313e-6**

- A_bad^KP + δ_true ≈ 7.1e-6 < Re Λ_lo′/87 (Lean `budget`).
- `code/crossover_N21.py 5.0313e-6` (verbatim N19b logic; `logs/crossover_N21_d5.031300e-06.json`):
  - first integer with gas > Robin envelope: **1397** (was 1390 with the G ≤ 15 part only, 1386 core);
  - first prime (exact K_p): **1399**, with no violation for primes ≤ 5000;
  - monotonicity at p* = 1397: G′ ≥ 0.02195 > envelope slope 0.00127 (Lean `env_slope_1397`: < 0.002);
  - margin at p = 1399: 13.0564 vs 12.9939.

So **the crossover stays near 1390: p₁ moves 1390 → 1397, and the first prime 1399 is unchanged.**

## 6. Lean

`lean/LineN21Arith.lean` was compiled in the lineN12 lake project after `lake exe cache get` ("No files to download"), so Mathlib was not rebuilt. Result: EXIT 0 (`lean/build.log`, 09:52 UTC+5), no sorry, no native_decide.

It checks:
- τ and den1 − τ;
- |s|;
- κ', |s|κ', R_A, S_T, Pert·S_T and Rem;
- |s/μ|, m(1), m(2) and K_0;
- the ρ conditions and λ^{−1/2} < 1/2;
- the final δ sum, the budget and the crossover slope.

Honest note: Lean uses decimal roundings of the inputs that are up to ~1e-5 relative coarser than the arb values in tail_DT (e.g. K_0: Lean < 56.78, arb 56.7776). It checks the inequality chain. It does not recompute the per-G window values; those are [CA-fp] and arb sums.

## 7. Impact on THEOREM_DRAFT_v4 and what remains

**H4 → met at [P] + [CA-fp].** What is still not at [CA] / referee level:
1. The window chain numerics, both the boxes and the D^T anchors, are [CA-fp] (float with a rigorous rounding model), not arb. This is the same standard as H2.
2. Lemma C, Lemma Q and Lemma D^T are written proofs by one author and need an independent audit, especially C3 and the cross-term Gronwall steps in §4.
3. Inputs taken as certified: N8 (Pert, Xn, dPi, N1, Cpow, mus, RA, normPi), N13 V1/V3b, N15 N_H table and residual formula, Line F F2, and the N6 symmetry.
4. Pure arb windows would mean recomputing 5k chains, roughly 10× the cost. Not done.

**Claims (proposals only, repo not touched):**
- 322: verification-pending → [P] lemma + [CA-fp].
- 302: closure conditions met (difference form = Lemma D^T, G > 15 tail = box + D^T).
- 318: crossover 1397 / 1399.

**Proposed v5 diff (NOT applied):**
```
- | H4 (CT) core→true conversion | OPEN; now = "difference-form ... + G > 15 true-functional tail" ...
+ | H4 (CT) core→true conversion | met [P lemma (N21 Lemma C, incl. dPi² term) + CA-fp]: δ_true ≤ 5.0313e-6 =
+ |   2.2102e-6 (G ≤ 15) + 2.7127e-6 (16 ≤ G ≤ 36, box) + 1.0843e-7 (G ≥ 37, Lemma Q + D^T, arb sums) | N21 |
- δ_true(G ≤ 15) ≤ 2.470e-6 [CA-fp numerics, P-sketch lemma]
+ δ_true(G ≤ 15) ≤ 2.2102e-6; δ_true(all G) ≤ 5.0313e-6 [P + CA-fp] (N21)
- p₁: all p ≥ 1386 (core) / 1390 (δ = 2.470e-6, G ≤ 15 part only; increases once the G > 15 tail is added); first prime 1399
+ p₁: all p ≥ 1386 (core) / 1397 (δ_true = 5.0313e-6, all G); first prime 1399 [P-arith] (N21 crossover_N21.py)
+ Errata: F21-1 (√cond → cond), F21-2 (digits.py mp.dps=34 invalid for G ≥ 22; v4 numbers unaffected), F21-3/4 (N16 conv_vec).
```

## 8. Files
- `code/`: conv_c.py, f_postC.py, tail_DT.py, final_delta.py, crossover_N21.py, sanity_mid.py
- `logs/`: convC_replay_p*.jsonl, convC_ext_16_60_p*.jsonl (G 16–47; G ≥ 45 partial, unused), f_postC.json, tail_DT_*.json, final_delta.json, crossover_N21_*.json, sanity_mid.json, discarded_dps34/
- `lean/`: LineN21Arith.lean, build.log
- `NOTES_N21.md`, `SHA256_N21.txt`
