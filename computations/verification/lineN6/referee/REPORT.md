# Referee report — BGS Line N5 v2 and Line N6
Grok Bot, 2026-10-31 (Asia/Yekaterinburg, UTC+5). Read-only audit: nothing in /workspace/bgs-lineN was modified and nothing was pushed.
Inputs: N5/REPORT_N5_v2.md (SHA256_N5_v2.txt OK), N6/REPORT_N6.md, NOTES_N6.md, code and logs (SHA256_N6.txt OK).
Audit artifacts:
- `code/ref_near0.py`, `code/ref_pattern.py`, `code/ref_wstar.py`
- `logs/*.json`
- `lean/LineN6Arith.lean` (builds clean; no sorry, no native_decide)

## Verdict
- **N5 v2:** READY. N5-F1..F10 are applied correctly.
- **N6:** READY-after-fixes as a **conditional** theorem (Theorem R♯ mod Ω♯). The required fixes are N6-F1, F4, F5, F6 and F7. It is **not** an unconditional refutation of frozen R′, and nothing in N6 claims it is.

## A. N5 v2: are N5-F1..F10 applied correctly? Yes.
- **F1 (sign):** fixed. Ẑ(½…½) = −Z_ρ, the family ratio is c*·e^{±0.518i}, and the cross part is positive.
- **F2:** constants 1.42785 and 2.7350 are now correct.
- **F3:** the bookkeeping section (family ∈ Dev) is present.
- **F4:** H_mean is flagged as numerically false.
- **F5:** N4 §3.3 is withdrawn.
- **F6:** the twlaw truncation is documented.
- **F7:** the spacing factor 7 at 7h_p is stated.
- **F8:** labels now read [CA] for c* and the phase (via N6), and [P-sketch] for Prop X.
- **F9:** completeness of X now cites the N6 near-0 family (about 8%, positive).
- **F10:** inherited copies are positive.
- **Remaining nit:** N5 v2 relies on N6 for [CA] (a forward reference). That is fine provided N6's labels are fixed as below.

**Self-correction (referee).** My N5 report stated "depth classes < 0.1%, X = 4pc*(1+3e-4)". That was wrong, because my depth sum only enumerated sector 4.
- N6's near-0 family is real. I re-verified it at (L,K) = (8,32) and (10,40) (`ref_near0`): ratio 2.98655e-5 − 6.598e-6i, 4p points, twist profile near 0, about 8% of Re X, and positive.
- The family ratio I got is 3.43578e-4 + 1.95798e-4i, which matches N6.
- This does not affect the sign conclusion of N5, and it helps positivity.

## B. N6 claims, independently checked
**(1) Positivity lemma [P]: correct.**
- The algebra holds: Dev_d = d⁻²Σ_t(2Re Z̄E_t + |E_t|²) ≥ Lin_d.
- |S_d| = n_d, and the non-resonant floor is ≥ −RMT.
- Choosing Dev or Lin level by level is legitimate.
- Dev_d ≥ −n_d|Z_ρ|²/d² is valid. Lin has no such floor, so levels above L* must use Dev, and N6 does this.

**(2) Family constants [CA]: reproduced** (`ref_wstar`, arb with the n_cert boxes rA = 0.175180+0.168374i ± 0.003225 and rB = −0.178594+0.243641i ± 0.003212).
- w* = −(rA·rB)³ gives Re w* ∈ [2.8896e-4, 3.9820e-4] and Im w* ∈ [−2.520e-4, −1.396e-4].
- arg w* ∈ [−0.7172, −0.3372]. These match the claims to every printed digit.
- Corner bounds give c* ∈ [3.572e-4, 4.370e-4], which lies inside the claimed [3.447e-4, 4.443e-4]. Lean `cstar_lo` and `cstar_hi` check this.
- The cross-checks are consistent: |rA| = 0.24298 and |rB| = 0.30209, as in N5 TW at p = 59. w* for ρ = (−2,8) is the conjugate of the (2,8) ratio.
- Certificate logic I read is sound in structure:
  - the resolvent on |z−s| = 0.6 is discretized at 512 points with a Neumann-series step correction;
  - the excursion cores follow the pattern lists (38 and 37 steps, KK = 18);
  - the tail uses the product-perturbation bound Cpow·(exp(Cpow·2πN1Σ|d|/|s|) − 1).
- Two inputs are imported and were not re-certified here (see F9): rank(Π_A) = 1 inside Γ, which needs the Line F spectral-gap certificate (other eigenvalues ≤ 0.769), and the float-BLAS-with-γ_n error model.

**(3) Prop X constants: recomputed** from the printed upper bounds.
- E(290) = 1.43110e-4, versus Re w*_lo/2 = 1.44475e-4. The margin is only 0.95%. E(289) = 2.74e-4 fails, so w0 = 290 is sharp.
- η is dominated by coll = 2Gb²R2p·μ^{−145} = 1.156e-20. The other terms are ≤ 1e-78.
- Constants: Cpow = 3246.8 (≤ 3247 ✓), Gb = 3.905e8 (≤ 3.9e8 is **false** by 0.14%; it should read ≤ 3.906e8), T1 = 730.142/μ* = 381.18 ✓.
- F_m constant: 16(2.890e-4 − 1.4311e-4) = 2.3344e-3 ≥ 2.3e-3 (Lean `fm_const`).
- p0: the half-window ⌊((p−1)/2 − 1)/2⌋ already equals 290 at p = 1163, so p0 = 1163 also works. This is harmless.
- Lean checks `E290` and `coll290` (with μ^145 in exact rationals).

**Pattern lemma: much stronger than [P-sketch], and essentially exact.**
- I tested it with exact integer twists mod 4q for prime h_p at p = 19, 29, 47, 59, 163, 257, 421, 937, 947, 1493 and 1901 (`ref_pattern`, up to 728-digit q).
- In every case each period has exactly one A excursion (±a at two consecutive steps) and one B excursion (−b at one step), spaced (p∓1)/2 apart.
- All other |d_i| ≤ 0.0607.
- The deviation from the two-sided geometric pattern is **≤ λ^{−p/2−0.09}** (for example 7.8e-729 at p = 1901).
- This suggests a short proof. In a window, d_k = Tr(λ^kδ′) with conj(δ′) = ±a (or ±b) exactly, so d_k = ±aλ^{−k} ± (1/(16qa))λ^k. The identity 16qab = 2q/ε = ε^{p−1}(1+O(ε^{−2p})) makes the growing term coincide with the next excursion's tail up to relative error λ^{−p}.
- The contamination bound 2bλ^{−w}λ/(λ−1) used in q_propx is therefore conservative.

**(4) Theorem R♯: logic correct, modulo its inputs.**
- W′ ≥ −RMT + φ⁻¹(F_m − (1−2δ)F_m − δF_m) = −4m + δF_m/φ ✓.
- **F_m dominates 4m for every p ≥ 1165, not only asymptotically.** Using |Z₈| ≥ ½(1−λ^{−m})(μ^m − 3012.3) and φ ≤ h_m, the margin is log10[F_m·δ/(4mφ)] ≥ 185.6 at p = 1165 and grows by about 0.16 per unit of p. Any δ ≥ 1e-185 therefore works.
- **The trivial floor for d > L* is valid.** Σ_{d>L*} n_d/d² ≤ τ(h_m)/L*, so the loss is ≤ δ·2.3e-3·p|Z₈|²/h_p ≤ δF_m. It needs two things: Dev (not Lin) at those levels, and Σ_ρ|Z_ρ|² ≤ 4|Z₈|². The second relies on an explicit upper bound for |Z_(2,16)| (see F6).

**(5) Squarefree reduction: correct.**
- At a level q^a with excluded labels, κ is supported on q^{a−1} | u, so unit points get weight 0.
- Every q | h_p splits.
- h_{3p} = h_p(4h_p² + 3).

**(6) Ω♯ inventory.** Mostly complete, with one gap in the listing (F7).
- C′ rates: 1.27438 < 1.42785 and 1.45789 < 1.63999.
- Using W/W⁺ is legitimate but contributes essentially nothing (F8).
- I found no double counting:
  - F_m uses only the 4p 16D=1 points at h_p for ρ = (±2,8);
  - the near-0 family and the (±2,16) Lin terms at family β belong in Lin♯ (both are positive or rate-dominated);
  - inherited copies at e·h_p are either ≤ L* (Lin♯, positive) or > L* (Dev floor).

## C. Findings
- **N6-F1 (labels, required).** Theorem R♯ and the F_m bound are labeled [P mod Ω♯ + item 4 inputs]. The F_m bound also rests on:
  - Prop X, which is [P-sketch]: other-sector absorption, and the derivation of the η terms, in particular coll's use of a power bound on the Line F remainder, sup_n‖R^n‖ ≤ R2p;
  - the [CA] certificate.
  
  Fix: state "[P mod Ω♯, Prop X (P-sketch), [CA] n_cert, TRACE-199/213, |Z_(2,16)| rate]".
- **N6-F2 (upgrade, recommended).** Replace the [P-sketch] pattern lemma with the exact conjugate-component argument (§B3). The numerical residual ≤ λ^{−p/2} up to p = 1901 supports it.
- **N6-F3 (constants, minor).**
  - Gb ≤ 3.9e8 should read ≤ 3.906e8.
  - The text alternates between E ≤ 1.43e-4 and 1.44e-4; use 1.4311e-4.
  - State that the margin against Re w*_lo/2 is under 1%. Any widening of the w* box breaks p0 = 1165.
  - p0 = 1163 is also admissible.
- **N6-F4 (rounding, required).** The target "1.640 = μ*²/(1.6677·λ^{1/6})" is rounded **up**. The true value is 1.639991. Lean `rate16_rounded_up` proves that 1.640 exceeds it. Use 1.6399. The 16V margin is still 1.1248.
- **N6-F5 (required, small).** F_m uses (h_p − 2). For composite h_p the isotropic weight is n_{h_p} = Π(q_i − 2). The loss is ≤ 4/(2p−1) ≤ 0.17% for p ≥ 1165, so 2.3e-3 survives (2.3344 → 2.330). Say so explicitly.
- **N6-F6 (hidden thresholds, required).** Two inputs are only stated "for large m":
  - Σ_ρ|Z_ρ|² ≤ 4|Z₈|², which needs an explicit constant C in |Z_(2,16)| ≤ C·1.6677^m (h_rho16.py was not run);
  - Theorem W/W⁺, which holds only for m ≥ m₁ (not computed).
  
  "p ≥ 1165" should read "p ≥ max(1165, p₁)", with p₁ stated or flagged as uncomputed.
- **N6-F7 (inventory gap, required).** At composite h_p (and at e·h_p), the inventory omits β that are isotropic mod some q_i | h_p and units mod others:
  - item 1 (C′) covers fully unit β;
  - (a) covers "isotropic" β.
  
  Fix: state explicitly that these mixed classes belong to (a) or (b).
- **N6-F8 (exaggeration, minor).** Item 3 lists "Weil-range prime levels" as proved. With c_W = 10^−25.62 the range is empty for any realistic p, and W⁺ is conditional on OP. Say that this item currently removes nothing.
- **N6-F9 (certificate hygiene).**
  - n_cert.json prints the key intervals at too low a precision: "w": "[+/- 3.99e-4] …" and "arg_w": "[+/- 0.718]" are unreadable. Print endpoints. My recomputation gives the claimed intervals.
  - Cite the Line F spectral-gap certificate for rank(Π_A) = 1 on |z−s| = 0.6.
  - State that the linear algebra is float with a priori γ_n bounds, not ball arithmetic. That is acceptable for [CA] but should be said.
- **N6-F10 (referee self-correction).** My N5 completeness claim is withdrawn (see §A). N6's near-0 family is confirmed: about 8% of Re X, and positive.
- **N6-F11 (coverage).** o_levels was run only at p = 5, and h_rho16 was not run. N6 discloses both honestly. Evidence for (b) is therefore thin beyond the N5 referee runs (mixed classes ≤ 4.4e-12 relative).

## D. How close is this to an unconditional refutation?
- **What is now proved or certified:**
  - the sign and size of the family term, F_m ≳ 2.3e-3·p|Z₈|²/h_p, which is [CA] + P-sketch, and the P-sketch parts look routine;
  - the reduction of "frozen R′ is false" to a **one-sided** estimate Ω♯ with a relaxed target;
  - a 10^185 margin over −4m.
- **What remains** is two genuine analytic estimates: (a) non-family isotropic β at h_p, and (b) all β at the remaining levels ≤ L*. Numerically both are tiny or positive: the near-0 family is +8%, everything else is < 0.6%, and mixed classes are ~1e-12. But neither has a proof route that avoids the index-loss barrier.
- Honest estimate: a **conditional** refutation that is complete up to two well-posed lemmas. That is real progress, but it is not near-unconditional.

**Most tractable: (a).** It lives on a single level with exact arithmetic structure. Concrete attack:
1. **Parametrize.** Write each isotropic point at h_p as y = (q + γα)/(4q), α ∈ O/(q), and generalize Lemma H plus the exact pattern argument of §B3. Each orbit's twist sequence is then two excursion cores per period, determined by α only through a finite p-independent "depth" datum (conj-components ±a_α, ±b_α), with exact geometric tails.
2. **Reduce.** Ẑ/Z_ρ = −(r_A(α)·r_B(α))³·(1 + O(λ^{−p/2})). Bound (a) by the p-independent series Σ_α κ-weight·|r_A r_B|³.
3. **Converge.** Prove the series converges, with a sum bounded well below Re w*·(1−2δ), using:
   - a Theorem-C-type average over α of norm ≈ k: excursion cores of length ≈ log_λ k behave like level-~4k orbit segments, rate 1.274 < μ*, giving decay ~k^{−c};
   - a [CA] certificate for finitely many small depths, starting with the near-0 family, which can be certified exactly as w* was in n_cert.
   
   Because the target is one-sided, positive classes such as the near-0 family can simply be dropped.

(b) is harder: infinitely many unrelated levels (proper divisors of composite h_p, and rank-3p primes of 4h_p² + 3) with no common orbit structure.

## Lean
`lean/LineN6Arith.lean` builds clean (no sorry, no native_decide). It contains:
- fm_const and fm_const_144;
- E_half, E290 and coll290;
- p0_1165, p0_1163 and p0_1161;
- rate1, rate2 and rate2′;
- lam_bracket;
- rate16_rounded_up (the F4 finding), rate16_ok and rate16_real;
- cstar_lo and cstar_hi.
