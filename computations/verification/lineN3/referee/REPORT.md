# Referee report: Line N3 (/workspace/bgs-lineN/N3), with a check of N2 v2

Referee: Grok Bot. Date: 2026-10-31, Asia/Yekaterinburg (UTC+5). I only read the repo and its clones, and I pushed nothing.
Compared against: main e4042ef2 (`record/claims.json`), my Line N2 report (`/workspace/audit/lineN2/REPORT.md`), and the Line F code and certificates.

## Verdicts
- **N2 v2: fixes applied correctly in substance.** Two cosmetic residuals remain (§A).
- **N3: READY-after-fixes (N3-F1 … N3-F11).**
  - The isotropic structure is right. C3 is proved. C1 is proved *by the proof of* TRACE-222, but TRACE-222's registered statement does not cover it.
  - The exponents in Lemma I check out.
  - The Λ certificates reproduce byte-for-byte. My independent arb spot checks agree to about 1e-10.
  - The rounding analysis is sound Rump/Higham-style verification. It has three small non-a-priori steps, each about 1e-10 against a slack of 0.04.
  - Two scope gaps affect Theorem C′ and the "Net" statement: prime-power conductor weights, and the mixed level 7·h_p.

---

## A. N2 v2 (`N2/REPORT_N2_v2.md`)

| Fix | Applied? | Note |
|---|---|---|
| F1 representation | ✔ | §4 rewritten. Lemma I is in N3 (checked below). |
| F2 TRACE-266 at h_p | ✔ (§8) | Widening TRACE-266 to every c with ord_c λ = p is the right registry action. |
| F3 m ≥ m₁, Theorem A as an implication | ✔ (§8) | *Residual:* the Theorem A statement in §2 still lacks "m ≥ m₁"; edit it inline. |
| F4 families | ✔ | μ*·T = 2.458680 < ξ_lo is stated. |
| F5 all conductors | ✔ | |
| F6 Λ numerics | ✔ in §8 | *Residual:* the §0 row (c) and the "conditional result in plain terms" paragraph still present 1.98242 (Line F lift, K0=3) without the lower-estimate caveat. Mark them "superseded by N3 §2". |
| F7 barriers | ✔ (§6 ledger) | The §5 item labels are unchanged. Acceptable, since §6 now defines the meaning. |
| F8 (21,239) | ✔ | `SHA256_N2_v2.txt` verifies (37 entries) and includes `d_level_split.jsonl`. The original manifest is untouched. |
| F9 unit weights | ✔ mostly | The prime-level values match TRACE-229 / J3 §6 ("if q² \| h … 1/q² and (q−1)/q²"). *Residual:* weights at a **conductor** q^a with a ≥ 2 are not registered anywhere. "CRT products in general" does not supply them (same issue as N3-F8). |
| Prop E remark | ✔ | |

---

## B. Line N3

### Independent checks
Scripts are in `code/` and their output is in `logs/`.

| Check | Result |
|---|---|
| Author manifest SHA256_N3.txt | all OK |
| Rerun of `i_verify.py` E (NG=2000) and V (NG=4000), same inputs | Values identical: Λ^{8E} ≤ 1.6603374914, Λ^{8V} ≤ 1.9657358412, grid max 1.923268233865 at τ = 0.501375, Lip 339.69576, κ = 2965.54 (`rerun_i_cert_*.json`). For E, argmax differs (0.62775 vs 0.86525) because the E norm is τ-independent to 1e-15 (below). |
| **arb spot checks** (`ref_lambda_arb.py`, prec 96). Blocks rebuilt in acb; Y = R·A_τ·S formed in arb; ‖Y‖₂ bounded via G = Y*Y, float eigenvectors Q, Gershgorin on Q*GQ, ‖Q⁻¹‖² ≤ 1/(1−‖Q*Q−I‖_F); ‖(RS)⁻¹‖ ≤ 1/(1−‖RS−I‖_F) | **8V:** τ = 0.501375 → ≤ 1.92326823191; 0.5 → 1.92325321110; 0.498625 → 1.92320941071; 0.25 → 1.65185768236; 0 → 1.62098684576; 0.73 → 1.66307973309. ‖RS−I‖_F ≤ 7.3e-15. **arb Lipschitz** Σ2π\|n\|‖C_n‖_F ≤ 339.69575813 (author: 339.69575847). **8E (R = I):** 1.63659784340 at τ = 0.86525, 0.5, 0.25; Lip ≤ 94.958574. All are ≤ the author's float values plus their error terms. |
| Blocks vs Line F `lift.py` (an independent float construction) at τ = 0.3, 0.5, 0.501375, 0.9, Nmax = 60 (`ref_blocks_twist.py`) | max \|diff\| ≤ 6.6e-15 (V), 1.1e-15 (E). The author's own check (`i_check_blocks.py`) used only τ = 0 and Nmax = 20. |
| Line F error terms (`cert_lift.py`) | Every δ₁, δ₂, Δ and ‖X‖ bound uses \|J_n\| and Mn(n,ρ) only, plus Bessel tails for \|n\| > Nmax. So they are **uniform in the twist** ✔, and letters beyond 60 are accounted for ✔. |
| Lemma I numbers (`ref_n3_consts.py`; Lean) | V O1→F: θ = 0.9412, weight slope 0.25/λ = 0.0429. V F→O1 (two steps): θ = 0.5066, \|c\|-exponent −0.1764 (one step would be +0.179, which is why two are needed). E dev = 0.1036. E O1→F (two steps): θ = 0.6355 (one step 1.115 ✗). E F→O1 exponent −0.2264 (one step +0.129 ✗). All ✔ |
| Theorem C′ constants | (1.965736·1.052901)^{1/3} = 1.27440; (1.660338·1.051923)^{1/3} = 1.20428; κ = 1.02180, √κ = 1.01084 = λ^{0.00612}; δ = 0.00716 ✔ (Lean `rateV`, `rateE`, `margins`) |
| Numerics table vs logs | Matches `N2/logs/d_level_split.jsonl`, `d_level_split_N3.jsonl` and `f_iso_signed_*.json`, apart from small items (N3-F10). |
| Lean (`lean/LineN3Arith.lean`, v4.33.1) | λ > 5.828; the four Lemma I inequalities; the rate and margin inequalities. Compiles clean |

### 1. Isotropic structure
- **Lemma 1.1 [P] ✔.**
  - For β ∈ 𝔮: y = β/q ∈ 𝔮̄⁻¹/O, and γ ↦ Tr(γy) mod 1 factors through O/𝔮̄ ≅ F_q. So τ_i = sℓ^i/q.
  - ℓ has order exactly p. The order divides p because λ^p − 1 = 2h_pε^p. It is not 1 because N(λ−1) = −4.
  - On the other line ℓ′ = ℓ⁻¹, since N(λ) = 1.
  - Ẑ is constant on ⟨ℓ⟩-cosets, by cyclicity of the trace.
- **Lemma 1.2 [P] ✔.**
  - The iso weight (q−2)/q² is exactly TRACE-229's registered value, and it is real, so it is the same for ±ρ.
  - With TRACE-255's D_q = (1/q)Σ_{ℓ(q)∖0}Ẑ, the iso part is ((q−2)/q)(D_𝔮 + D_𝔮̄). The two lines meet only at 0.
  - Notation: N3 writes Σ_{ℓ(𝔮)} = q·D_𝔮̄, while TRACE-255 has Σ_{ℓ(q)} = q·D_q. This is harmless because the two are summed, but align it (N3-F3).
  - "|D_𝔮| ≤ 4h/q gives rate λ^{1/3} > T" is consistent with TRACE-264.
- **C3 [P] ✔.**
  - 4ν₀ ≡ ±2 (mod h) with h odd gives ν₀(−ρ) ≡ −ν₀(ρ) (mod q).
  - The missing label is t_b = −ν₀(2h/q)⁻¹·(…), so it flips sign.
  - Hence W(−ρ) = conj W(ρ), which agrees with TRACE-221(ii)'s d = 7 statement. Composite levels follow via TRACE-228, since n_e does not depend on the sign.
- **C1: does TRACE-222 as registered cover it? No, only its proof does.**
  - The registered scope is "letter weight … e(n τ_i(β)/7)", with m ≡ 3 (mod 6) and level d = 7.
  - The proof (K: (C,a,τ) ↦ (−C, 4−a, −τ); R: n ↦ −n, s ↦ −s, c ↦ −c, rounding symmetric because λ is irrational) never uses the value of τ. Antiunitary conjugation is multiplicative, so the non-autonomous product statement follows.
  - So C1 is **[P, by the proof of TRACE-222]**. Registry action: widen TRACE-222 to arbitrary twist τ ∈ R/Z and arbitrary non-autonomous products (N3-F1).
- **C2 [P-sketch]: label agreed.**
  - TRACE-221(i) is registered for d = 7 only. The claim that the G2 automaton and the c_a table do not see the conductor is plausible: TRACE-266 builds Π_β with "the m = 3p automaton constants". But that needs a written proof, so leave the general-level M6 consequence as [P-sketch] (N3-F2).
- **§1.4.** The doubling algebra ({4}×{4}, s = −1,−1) is [P mod C2]. "Dominant isotropic orbits are slow" is [N], so label it split (N3-F11).
  - The "log_λ q + 0.76 steps" figure needs ε stated. With TRACE-268's maximal ε = 1/16 the bound is log_λ q + 1.02; 0.76 corresponds to ε ≈ 0.05 (N3-F4).
- **§1.6** is a sound assessment. BGK/Bourgain need |⟨ℓ⟩| ≥ q^δ, but here |⟨ℓ⟩| = p ≍ log q. This is consistent with my Line N report on (4).

### 2. Λ certificate
**Lemma I [P]: exponents checked ✔.**
- The V and E disc and weight inequalities are as tabulated above. The letter sums converge against |J_n(1.8)|, and the twist is a unimodular factor, so the bounds are uniform in τ. Schur column multiplicity is ≤ ⌈λ⌉.
- Gaps to fix (N3-F5):
  - (i) The text says "V: one step in, two out", but the displayed formula drops two steps at each end. Both are valid, since an extra step costs sup_τ‖L_τ‖_F, which is uniform, but make them consistent.
  - (ii) Say explicitly that the O1 operators of TRACE-249 are the ω-conjugated ones on the unweighted sum, i.e. the same as L on H(ρ,β).
  - (iii) Say that Line F's weights e^{−β(|c|−Rc)₊} are equivalent to e^{−β|c|} up to e^{βRc}, which is absorbed in κ_F.
  - (iv) Apply Lemma I *once* to the whole p-step product, giving ‖M‖_{O1} ≤ C_I·κ·Λ^{p−3}. This is cleaner than (C_I κ)^{1/k′} per block.

**(−2,8) coverage (N3-F6).** The certificates use w₀ with chirp +c₀. The (−2,8) families have the conjugate chirp and shifted sector. Because τ is free, Λ_free(−2) = Λ_free(+2) exactly, provided RK is an isometry of the Line F space. It is: the weights are symmetric in |c|, the discs have real centres, and K and R preserve H². State this explicitly (it is C1 again).

**Is the rounding analysis rigorous?** Mostly yes.
- **Sound parts:**
  - a priori product bounds γ-type 2(n+4)u, generous for a standard complex GEMM (not Strassen or 3M);
  - block radii from arb;
  - residual + Ostrowski + Weyl for λ_max(Y*Y);
  - the 1/(1−‖RS−I‖) factor;
  - the Lipschitz cell term;
  - the core-perturbation norm |||·||| argument. I checked |||T||| ≤ f, since b‖X(u+t)‖ ≤ b‖X‖(‖R⁻¹‖+1)|||v||| = f|||v|||, and |||E||| ≤ ε·max(‖R‖,1,b)(‖R⁻¹‖+1+1/b).
- **Not a priori (N3-F7):**
  - ‖R‖₂ is computed by float SVD times (1+1e-6). It enters only the penalty and κ; use ‖R‖_F, or compute it in arb.
  - Twiddle factors np.exp(2πinτ) have absolute error up to about 1e-13 per n. They are not bounded separately; the "generous" summation term is of the same order and was not shown to dominate.
  - The float grid points τ_g are not exactly (g+½)/NG; inflate the cell radius by 1 ulp.
- All three are ≤ ~1e-10 against a cell slack of 0.042 and a margin of 0.043. My arb spot checks, including the argmax cell and the Lipschitz constant, agree with the float values to within their error terms.
- **Verdict:** [CA*] as labelled is justified. The upgrade to [CA] is mechanical. My arb pipeline takes about 13 s per τ at D = 495, so 4000 cells is about 15 CPU-hours (parallelisable), or fewer cells with a second-order cell bound.

**Interpretation ✔.**
- sup_τ |||L_τ||| ≤ Λ bounds every product of the *free* family, which contains every cat-map twist sequence.
- So this is an upper bound for the torus Λ, which settles N2-F6.
- μ* ≤ 1.9154752 ≤ 1.9233 (grid max) ≤ 1.965736, which is consistent.

### 3. Theorem C′
- The implication chain holds (Theorem C + Lemma I + Λ [CA*] + r_2 [CA, independently reproduced]), and the rates 1.27440 (V) and 1.20428 (E) are correct.
- **Scope gaps:**
  - **N3-F8, prime-power conductors.** If q^a ∥ h_p with a ≥ 2, the conductor h_p contains q^a. J3 registers weights only at *prime* levels (TRACE-229: 1/q², (q−1)/q² when q² | h), not at conductor q^a. Either add the hypothesis "h_p squarefree" (whether this holds for all p is unknown, a Wieferich-type question) or derive the q^a weights. Until then, Theorem C′ is proved only for p with h_p squarefree.
  - **N3-F6:** (−2,8) via RK (above).

### 4. Blocking list and "Net"
- Items 1–4 are correct as an assessment, and the barrier items keep their N2 meaning (method majorant). **But N3-F9:** the mixed level **7·h_p** (rank 3p, size ≈ λ^{m/6} < L_m = λ^{0.227m}) is not absorbed by Prop K2, even in the best case where h_p and K_p/7 are prime. So "Net" ("what remains is exactly the isotropic lines at q = h_p plus the (±2,16) Λ") omits it.
  - Its unit points are very likely covered by the same proof. The level-7 component adds a period-3 modulation of the twists: the free-family Λ covers any twist sequence, and the r_2 collision majorant is cancellation-free, so the extra unimodular phases drop out. State and prove this as part of Theorem C′, or list 7·h_p.
  - Its h_p-isotropic β belong to item 1, so extend item 1 to "d | h_p or 7d".
- Item 2's analysis (index loss (h_p/d)² against κ^{p/2}) is correct, given κ = 1.0218.

### 5. Numerics table (N3-F10)
- The (33,23) "iso weighted signed" entry is "—", but `f_iso_signed_m33_q23_s1.json` exists: signed 0.8473 = absolute 0.8473. Fill it in.
- The (27,199) max iso point is 1.0602 in the log and 1.0601 in the table.
- Two different "absolute iso" rates are in play: per point from d_level_split (1.1604) and per line from f_iso_signed (1.1600, and 1.0523 vs 1.0559 at (15,41)). Define both.
- Otherwise the table matches the logs, and "no trend claim" is respected.

## Fixes (N3)
- **N3-F1.** C1 holds by TRACE-222's proof. Registry: widen TRACE-222 to arbitrary τ and non-autonomous products.
- **N3-F2.** C2 stays [P-sketch]. Write out the conductor-independence of the G2 sector law before widening TRACE-221(i).
- **N3-F3.** Align D_𝔮 / D_𝔮̄ notation with TRACE-255.
- **N3-F4.** State ε for "log_λ q + 0.76" (TRACE-268 with ε = 1/16 gives +1.02).
- **N3-F5.** Lemma I: make the step counts consistent; state the ω-conjugation equivalence and the Line F weight-equivalence constant; apply it once per p-product.
- **N3-F6.** State that Λ for the (−2,8) families equals that for (+2,8) via the RK isometry (C1).
- **N3-F7.** Certificate hygiene: ‖R‖ via Frobenius or arb; an explicit twiddle-error term; ulp-inflated cells. Optionally upgrade to [CA] by running arb on all cells.
- **N3-F8.** Theorem C′: add the h_p-squarefree hypothesis, or derive the conductor-q^a weights. The same applies to the N2 v2 F9 residual.
- **N3-F9.** Add level 7·h_p: its unit points via the modulated-twist argument (then they are in Theorem C′), its isotropic part in item 1. Correct "Net".
- **N3-F10.** Table fixes (above).
- **N3-F11.** §1.4 labels: algebra [P mod C2], dominance [N].

## Suggested registry states
| Item | State |
|---|---|
| Lemma 1.1 (geometric twist sequences), Lemma 1.2 (iso part = ((q−2)/q)(D_𝔮+D_𝔮̄)) | proved |
| C3 (W(−ρ) = conj W(ρ) at every prime level; composite levels via TRACE-228) | proved |
| C1 | proved, by widening TRACE-222 (its proof is twist-independent) |
| C2 / general-level M6 | open (P-sketch); TRACE-221(i) widening pending a written proof |
| Lemma I | proved (constants finite, not computed, p- and τ-independent) |
| Λ^{8V} ≤ 1.965736, Λ^{8E} ≤ 1.660338 (free family, Line F space) | computer-assisted, **verified floating point [CA*]**. Referee arb spot checks agree. Register as [CA] only after an all-cell arb run. |
| Theorem C′ (unit points at h_p, (±2,8), rates 1.27440 / 1.20428) | proved mod the [CA*] certificates, **for p with h_p squarefree** (or after the q^a weights are derived); (−2,8) after N3-F6 |
| New open items | isotropic part at q \| h_p (and 7·h_p); (±2,16) Λ < 3.04; level 7·h_p unit points unless added to C′ |
| TRACE-206 (R′) | unchanged: open, not refuted |

No merged claim in main e4042ef2 is contradicted. Registry actions are widenings: TRACE-222 (now), TRACE-266 (from N2-F2), and TRACE-221(i) (after the C2 proof).

## Cheap Lean targets
- **Done:** `lean/LineN3Arith.lean`.
- The ⟨ℓ⟩-orbit count: ord_{𝔮̄} λ = p, from λ^p − 1 = 2h_pε^p (Line M `lam_pow_eq`) and N(λ−1) = −4.
- C3's label arithmetic: 4ν₀ ≡ ±2 (mod h), h odd ⇒ ν₀(−) ≡ −ν₀(+).
- The TRACE-229 isotropic weight count 2(q−1).
- The Schur multiplicity bound #{c : round((c+n)/λ) = c′} ≤ 6.
