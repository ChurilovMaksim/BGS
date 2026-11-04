# Hostile referee audit: PR #83 (research-cloud-1104), with PR #85 and research1104/P2 cross-checks

Auditor: Grok Bot (independent referee), 4 Nov 2026, ~19:45 CET. Read-only: nothing pushed and no PR comments.
Objects audited:
- **PR #83** head `717bfddc` (`evidence/research/20261104_cloud/`). RUN.md hashes verified: all 5 match.
- **PR #85** head `9be1dd46` (`evidence/research/20261104_grok47/`). Clone at `/workspace/audit/pr85`.
- `/workspace/research1104/P2/SPAN_LEMMA.md` (Lemma S) and `/workspace/research1104/P2/BACKGROUND_INTERPLAY.md` (Lemma BI).

The auditor code is my own. It does not import PR code. It lives in `AUDIT_code/` (untracked):
- `census.py`: exact integer ε-digits. The fundamental domain uses exact sign tests in ℤ[√2]. Floors use `isqrt`.
- `kp_xover.py`: mpmath Prop. K fixed point, and an mpmath re-implementation of the v5 crossover with its own h_p and prime sieve.
- `bi_j14.py`: the J₀ = 13/14 rows, plus my own implementation of Lemma BI's numerics.

Outputs: `census_J12/J16.json(l)`, `kp_xover.json`, `bi_j14.json`.

## Verdict summary

| # | Claim | Verdict |
|---|---|---|
| 83-1 | Span lemma: span ≤ ⌊log_ε(\|N\|/2)⌋ + 3; ≤ 2j for j ≥ 3; equality at α = 2 | **CONFIRMED (math)**, with 3 cosmetic fixes and 1 wording fix |
| 83-1n | Exact census through shell 16 (counts, histogram {2: 43304, 3: 38405}, 0 violations, 2182 truncated stored words) | **CONFIRMED**, reproduced exactly |
| 83-2 | Prop. F disjointness (U_n^† lies outside the bad set at g₀ = 4; ≥ ¼ of the Prop. F mass) | **CONFIRMED (math)**, with 2 small fixes |
| 83-3 | The uniform step norm N_H ≤ 2.91656 overshoots the H1 budget for every j ≥ 1 | **CONFIRMED**, scope wording fix |
| 83-4 | Conditional on H1: 3299 → 3067 at C ≤ 0.082; 3307 = slope-2 majorant at the 1.02-inflated weight; 1409 unchanged at C ≤ 8.8e-4; sensitivity table | **CONFIRMED** (all reproduced). Context: *bare* activities only. With Lemma BI it becomes 3389 (minimal a) / 3407 |
| 85-A | Two-sided span: L+1 < span < L+3; span = K_R − K_L + 3 except √2; digits in {−1,0,1} | **CONFIRMED** |
| 85-8 | Lemma 8: project word = digit word on fundamental-domain representatives | **CONFIRMED** |
| 85-B | Constants 1 and 3 are "best" | **NEEDS FIX**: only near-sharpness is shown |
| 85-W | Witnesses 116, 82√2, 118 | **CONFIRMED** (words, runs, defects to 15 digits) |
| 85-K | propk_tail numbers (3299 / 3067 / 1721 / 1409), Lemma 10 | **CONFIRMED** |
| P2-S | Lemma S: span ≤ 3 + log_ε(\|N\|/2) | **CONFIRMED**, 1 typo |
| P2-J14 | H1(J₀ = 14) is a weaker input; threshold 1787 (bare) | **CONFIRMED**, with stated caveats |
| P2-BI | Lemma BI: Z = Z_M·Z̃, KP for Z̃, κ ≈ 1.09e-3; 3407 / 1831 / 1409 | **CONFIRMED mod (M)**. NEEDS FIX: wording, and 3407 → 3389 if the minimal a is used |

No result contradicts the registered 3307 or 1409 **as arithmetic on their stated inputs**. Both are reproduced exactly from δ_eff = 3.4962e-4 and 7.4115e-6.

## 1. Span lemma: three derivations, line by line

### Conventions, checked against the repository
The conventions were checked against `lineN14/code/digits.py` and `a_enum.py`:
- seed (ea, eb) = (2a, 2b);
- e₁(z_A) = (2b + a√2)/4 = σ₁((√2/4)α);
- e₁(z_B) = −(a−b)/2 + (a−2b)√2/4 = −σ₁(μ ε⁻¹).

So even sites are red(ξ_{2t}) and odd sites are −red(−ξ_{2t−1}), with E_k = n_k − 2n_{k−1} − n_{k−2}.

Two further points:
- The code's t > 0 branch red(−e₂λ^{−t}) agrees with red(ξ), because Tr(με^k) = b p_k + a q_k ∈ ℤ.
- The shell convention 2^j ≤ |N(α)| < 2^{j+1}, α = a + b√2, matches `a_enum`.

All three write-ups use this correct model. Independently of all three, the repo's own `digits.eps_digits` agrees with my exact words on 309 sampled classes (300 from j = 13–16, plus all of j ≤ 3): 0 mismatches.

### PR #83 `proofs/01_span_bound.md`
- **§1, the range of red: NEEDS FIX.** red(x) = x − ⌊x + ½⌋ lies in **[−½, ½)**, not (−½, ½].
- **§1, the odd branch: NEEDS FIX.** When red(ξ) = −½, the odd twist is +½. It lands in **(−½, ½]**, not [−½, ½).
  - Neither slip is used: the proof only uses the |·| < ½ regions.
  - Half-integers do occur. At α = √2, ξ₀ = ½ exactly, so the RUN.md phrase "never an equality for V ≠ 0" is right. V = 0 does happen.
- **§2: correct.**
  - k_R − k_L = log_ε(|N|/2) holds because |ξξ′| = |N|/8.
  - Left cut: k ≤ ⌈k_L⌉ − 1 puts all three indices below k_L.
  - Right cut: k ≥ ⌊k_R⌋ + 3, and n = T there.
  - Length bound: ⌊k_R⌋ − ⌈k_L⌉ ≤ ⌊k_R − k_L⌋.
  - The bound is uniform over parity and over the exceptional class.
- **§3: NEEDS FIX (algebra slip).** "8 < 17+12√2 iff 15 < 12√2" is wrong; it is −9 < 12√2. The conclusion is trivially true, and it also follows from 32 < ε⁴, which is correctly reduced to 225 < 288.
  - "≤ 2j for j ≥ 3" is correct. It even holds for j ≥ 2, since ⌊2θ⌋ + 3 = 4.
  - The 4/5 slope is correct.
- **§4: correct.** I recomputed n_k for α = 2: (0, 0, 1, 2, 4, 10, 24) at k = −2…4. The word is (1, 0, −1), span 3, and ⌊log_ε 2⌋ + 3 = 3.
- **FRONTIER wording: NEEDS FIX.** "In shell j … ⌊jθ⌋+3 … The additive 3 is achieved at α = 2" is ambiguous.
  - α = 2 attains the **norm form** ⌊log_ε(|N|/2)⌋ + 3.
  - The **shell form** ⌊jθ⌋ + 3 is attained in shell 2 by 3+√2 and 1+2√2 (span 4), not by α = 2.
  - Overall the shell form is attained in shells 2, 5–8, 10–13, 15, 16, and never in shells 0, 1, 3, 4, 9, 14 (my census).
  - Exact fix: "Equality in the norm form holds at α = 2; the shell form is attained, e.g., at α = 3+√2 in shell 2."
- **"Multiplying α by ε preserves the span."** This shifts parity, so it is not automatic on the half-integer classes. I tested every class with |N| = 2·square through shell 16 (501 classes), under shifts ε^k with |k| ≤ 3 and sign: 0 span or zr changes. True, but PR #85's Δ+3 formula is the actual proof.

### PR #85 `proofs/span_law.md`
- **Lemmas 1–6 and Theorem A: correct, every line checked.**
  - Lemma 4 left end: θ+½ ∈ (1, 1+√2/2) or (−√2/2, 0).
  - Lemma 4 right end: E_{K_R+2} = T_{K_R} − n_{K_R} = ±1.
  - Lemma 6 two-sided: |θ_{K_L}||θ̄_{K_R}| = |N|/(8ε^Δ) ∈ [¼, ε²/4), with equality only at √2.
  - The case Δ = −2 is handled: Δ > L − 2 ≥ −2.79 gives Δ ≥ −2.
- **Census confirmation through j = 16 (81 709 classes):**
  - every letter is in {−1, 0, 1};
  - span = K_R − K_L + 3 on every non-exceptional class;
  - min(span − L) = 1.0000579 and max = 2.99994 (at 198√2, j = 16).
- **Lemma 8: correct.** αε^k = B√2 has ratio λ^{−k}, so a domain representative needs k = 0, which is even. The PR #85 finite comparison used KK = 8/12 and higher dps, not the production KK = 6 / dps 34. The production artifacts were checked here instead:
  - stored `a_enum` span and zr: all 5109 classes match;
  - `a_cert_ext` span and zr for j = 13, 14 (15 225 rows): all match my exact census;
  - every `coded` row has exact zr ≥ 6.
- **Corollary B: NEEDS FIX.** "1 and 3 are the best constants" is not proved. The witnesses show only that neither constant can be improved by about 3.4e-4 (my census gives 5.8e-5 at j = 16).
  - Exact fix: either "cannot be improved by more than 3.4·10⁻⁴ (5.8·10⁻⁵ through j = 16)",
  - or add a proof that the defect accumulates at 1 and 3. A sequence with |θ_{K_L}|, |θ̄_{K_R}| → ½⁺ would do; the √2·m families visible in the census are the natural candidates.
- **Witnesses: reproduced exactly.**

| α | span | zr | defect |
|---|---|---|---|
| 116 | 13 | 9 | 2.99966264991176 |
| 82√2 | 11 | 7 | 1.00033740024809 |
| 118 | 13 | 3 | 2.96087221277804 |

### P2 `SPAN_LEMMA.md` (Lemma S)
- **Steps 1–5: correct.** The two-lift argument works as follows:
  - x_k = σ₁(μ)ε^k and y_k = −σ₂(μ)ε̄^k, with x − y = Tr ∈ ℤ.
  - Both twist branches lie in [−½, ½] and are ≡ x mod 1.
  - So three consecutive |z| < ½ force τ = z and E = 0.
  - This handles both parities and half-integers without a separate lemma.
- **Typo: NEEDS FIX.** c_ε = 0.786448… should be **0.786440…** (0.7864397013573949).
- **Remark (i)** "sharp for the method" is vague. Replace it with "sharp: α = 2 attains ⌊L⌋+3; sup(span − L) ≥ 3 − 6·10⁻⁵ (census j ≤ 16)".
- §3 numbers are confirmed: the max defect − 3 is −0.0019655 on j ≤ 12, at α = 34√2. The only span > 2j case is α = 1.

### Do the three derivations agree, and which to integrate
They agree. All three give span < L + 3, which is equivalent to span ≤ ⌊L⌋ + 3 for |N| ≠ 2; at |N| = 2 the strict form gives 2 and the floor form gives 3. In the shell form all three give span ≤ ⌊κj⌋ + 3 with κ = log 2 / log ε. Only PR #85 adds the lower bound and the exact formula.

Recommendation for integration:
- **Statement:** PR #85 Theorem A + Corollary C/D + Lemma 1 (digits in {−1,0,1}) + Lemma 8. It is the most complete, with the exact span formula and the explicit identification with `eps_digits`. Apply the Corollary B fix.
- **Proof of the upper bound:** P2 Steps 1–3. This is the shortest, convention-proof argument (parity and half-integers are free).
- **Finite check:** the PR #83 / auditor census through j = 16, plus the production-artifact comparison above.
- **PR #83 01:** keep as the secondary derivation after the §1/§3 slips are fixed.

## 2. PR #83 `02_propF_disjoint.md`
- **Geometry: correct.**
  - On U_n, |x_k| ≤ δ for 0 ≤ k ≤ 2n, so the carries vanish there and E_k = 0 on [2, 2n].
  - On U_n^†, (δ/4)ε^{11} > 2.5 > 1. So |x_{2n+11}| > ½ and |x_{−11}| > ½.
  - Area ¼: the Prop. F bound is area × pointwise. I checked 2√2·δ²·0.502⁴ = 5.13e-7, so the ¼ transfers.
- **Index slip: NEEDS FIX.** On the left, the nonzero letter forced by the first |x_{k₋}| ≥ ½ (going left) is **E_{k₋+2} = −n_{k₋}**, not E_{k₋}. The conclusion is unaffected because k₋ + 2 ≤ 1 < 2.
- **Measure-zero slip: NEEDS FIX.** "The first k₊ with |x| ≥ ½ has E = n ≠ 0" fails if x = −½ exactly (the even branch gives n = 0). Exact fix: "if all E_k vanished on (2n, 2n+11], recursion would give n_{2n+11} = 0, contradicting |x_{2n+11}| > ½."
- **Ratio statement: NEEDS FIX.** FRONTIER's "≫ the i.i.d. product out to 10¹⁰" and SELF_REFEREE's "still outgrows" rest on TRACE-329's **[N]** ratio (the float 3.45). That ratio is ≥ 4.31e-8·2.1884ⁿ, which is > 1 for 22 ≤ n ≤ 10¹⁰. After the ¼ factor it is > 1 only for **24 ≤ n ≤ 10¹⁰**. Tag this [N] and state the range.
- The lemma is otherwise **[P]** as stated. It does not bound the bad sum, as the PR says.

## 3. PR #83 `03_uniform_norm_obstruction.md`
- **Arithmetic confirmed.**
  - log₁₀R(1) = 6·0.46487 + 1.0862 + 0.1337 = 4.009.
  - R(6) = 8.397 and R(11) = 12.785.
  - For all j, R(j) ≥ N^{2(θj+2)}/(C·2^{j(1−β)}) > 1, because N⁴/C > 1 and the slope is positive. So "every j ≥ 1" is proved, not just j ≤ 40.
- **Scope: NEEDS FIX (wording).** It obstructs only the *uniform-max* charging. TRACE-323 is a cellwise table for |t| > 1/256, and a cellwise or phase-keeping estimate is not covered. The PR says "uniform"; FRONTIER item 3 should say "charging the table maximum on every factor".

## 4. Prop. K / crossover (PR #83 04, PR #85 propk_tail) — independent recomputation (mpmath)

β = 1.4442975085259294268 and q = 0.63005677283423193771, both as in N20. There are 4460 finite bad rows (j ≤ 12, g₀ = 4, non-model).

| Case (C = 0.082, J₀ = 12 unless noted) | a | S₀ | δ_eff | first prime |
|---|---|---|---|---|
| slope 2, minimal a | 2.63452e-3 | 3.43900e-4 | 3.48931e-4 | **3299** |
| slope 2, N20 ×1.02 iteration | 2.69249e-3 | 3.44564e-4 | 3.49596e-4 | **3307** |
| θ, +3, minimal a | 1.52315e-3 | 3.24040e-4 | 3.29071e-4 | **3067** |
| θ, +3, ×1.02 | 1.55452e-3 | 3.24228e-4 | 3.29260e-4 | 3067 |
| slope 4/5, +3 | 1.53686e-3 | 3.24221e-4 | — | 3067 |
| θ, C = 8.8e-4 | 7.054e-6 | 2.37971e-6 | 7.41101e-6 | **1409** |
| θ, C = 4.4e-4 | 5.994e-6 | 2.15471e-6 | 7.18601e-6 | 1409 |
| θ, C = 0.04 | 5.128e-4 | 1.09701e-4 | — | 1721 |

- **Sensitivity** (factor on S₀: 0.99 / 1 / 1.01 / 1.03 / 1.10): 3037 / 3067 / 3109 / 3181 / 3463. This equals PR #83's table.
- **Published inputs:** 3.4962e-4 → 3307 (first integer 3305); 7.4115e-6 → 1409 (1402); 1.1691e-4 → 1733. No violations up to 5000.
- **Conclusions:**
  - PR #83's "3307 = slope-2 majorant at a 2% inflated weight; 3299 at the fixed point" is **CONFIRMED**. N20's iterate gives δ 3.49596e-4, which the register rounds up to 3.4962e-4.
  - PR #85's 3299/3067 rows are **CONFIRMED**. It uses a coarser finite majorant (W₀e^{16.44a}), which shows in a at C = 8.8e-4 (1.035e-5 vs 7.05e-6) but not in the primes.
  - Lemma 10 (log K_p < (2p+1) log ε via u_n < (ε/2)λⁿ and √λ − 1 = √2) is correct.
- **Context (NEEDS FIX in PR #83 FRONTIER, wording only).** 3067 uses **bare** activities, with background interplay still [P-sketch]. PR #83 says so in SELF_REFEREE §1, but the FRONTIER headline "crossover moves to 3067" should carry the qualifier "(bare activities; with an interplay charge of +8.5% in S₀ the same arithmetic gives ≈3390–3410, see Lemma BI)".

## 5. P2 J₀ = 14 and TRACE-332 "H1 ⇒ H3"

- **The J₀ = 14 input is logically weaker:** H1-shell(C, 12) implies H1-shell(C, 14).
  - The finite part j = 13, 14 exists and is complete: a_cert_ext has 5100 and 10225 classes, equal to my counts. 100 / 238 classes are `coded` (exact zr ≥ 6, never bad at g₀ ≤ 6).
  - Spans and zr match.
  - It is certified [CA-fp, core functional] by TRACE-331 (proved).
- **My bare recomputation (sharp span):**
  - J₀ = 13: 2129.
  - J₀ = 14: a = 6.382e-4, S₀ = 1.27904e-4, **1787**.
  - J₀ = 14 with slope 2: 1801, matching lineN22's 1800/1801 "for information".
  - J₀ = 14, C = 0.15: **3019**.
- **Caveats to carry:**
  1. Shells 13–14 are certified for the core functional only. This is the same standard as j ≤ 12, and N16's ~2.4% true-functional correction is outside both.
  2. Restating TRACE-325/336 at J₀ = 14 is a registry change and needs the usual referee pass.
  3. H1-ali is untouched.
  4. The numbers are not new (lineN22 has them). The new point is only that adopting J₀ = 14 is legitimate.
- **"H3 is implied by H1" (TRACE-332):**
  - What H3 needs is only **H1-bad** (the shell law), not H1-ali.
  - With the span theorem now [P], the implication is [P + CA mod H1-bad], except for the background-interplay / log→modulus step and the polymer normalisation (factor 2, per-site anchoring).
  - Lemma BI (below) proves the interplay step mod hypothesis (M). It does not close bad–model gap interactions or the normalisation.
  - So "H1 ⇒ H3" is still **not** unconditional [P]. It is [P mod (M) + normalisation].

## 6. P2 `BACKGROUND_INTERPLAY.md` (Lemma BI)

### BI.1, the factorisation: correct
- It is the cluster-expansion identity Z(𝒫_M(B))/Z_M = exp(−Σ_{C≁B}Ψ(C)).
- Expanding ∏(1+f_C) works because F is a set with each C ≁ B.
- The component bijection holds. A cluster shared by two components, or a cluster of Γ ≁ a bad polymer of Γ′, makes them incompatible, so the decomposition is unique and the activities multiply.
- The incompatibility of Z̃ is pairwise.

### (U), Ueltschi 2004 Thm 1, as used: correct
- The hypothesis is Σ_{X′≁Y}|w|e^{c+d} ≤ c(Y), including for external Y. The conclusion is Σ_{C≁Y}|Ψ|e^{d(C)} ≤ c(Y).
- |Ψ(C)| ≤ 7c′ follows (X ∈ C ≁ X), and so does |f_C| ≤ |Ψ|e^{7c′}.

### BI.2 / BI.3: correct
- The tree bound uses an injective canonical spanning tree and drops constraints.
- The children sums are ≤ ℓ_M S* + S₁* by the ℓ + ℓ′ − 1 anchor count.
- The fixed point θ = κ(ℓ+7) holds with κ = e^{7c′}A_M e^{7c′+7(a+S*)+S₁*}.
- The three incompatibility routes are complete. Cluster–cluster overlap is not an incompatibility.
- The KP condition S* + (S₁* + 12κ)/5 ≤ a is right: the worst case is ℓ = 5, where θ/ℓ ≤ 12κ/5.
- |ln Z̃| ≤ Σ_γ T(γ) = p·S̃₀.
- The lemma also supplies the log→modulus sentence |Z| ≥ |Z_M|e^{−pS̃₀} (given (M)).

### Hypotheses that remain
Labelled correctly in its §6:
- **(M):** a hard-core product-activity polymer gas, with **bad–model gap interactions assumed absent or inside δ**. This is a residual [P-sketch], not covered by δ_true as registered.
- **A_M = 1.03e-3:** N11 Σ_types|φ|, [P given certified boxes]. The per-site / factor-2 convention is not proved consistent with S₀'s factor 2.
- **Wrap-around polymers:** excluded.

### Numbers (my own implementation)

| Case | a | κ | S̃₀ | first prime |
|---|---|---|---|---|
| C = 0.082, J₀ = 12 | 4.318e-3 | 1.1112e-3 | 3.51054e-4 | **3389** |
| C = 0.04 | — | — | — | 1753 |
| C = 8.8e-4 | 2.617e-3 | — | 2.48683e-6 | **1409** |
| J₀ = 13 | — | — | — | 2237 |
| J₀ = 14 | 3.328e-3 | — | 1.39008e-4 | **1831** |
| A_M × 2 | — | — | — | 3907 |
| ℓ_M ≤ 8 | — | — | — | 3433 |

- My figures are at the **minimal a**. P2 reports 3407 / 3923 because its solver keeps the N20 ×1.02 iteration (a = 4.409e-3). That is the same 2% bookkeeping that turns 3299 into 3307.
- **NEEDS FIX:** quote 3389 (minimal KP weight), or state that 3407 is at the ×1.02 iterate. Both are valid sufficient primes.
- 1753, 2237, 1831 and 1409 agree with P2.

### Wording fixes (NEEDS FIX)
- "A_bad^KP rises from 3.446e-4 to 3.517e-4 (with Lemma S)" compares against the *old-span* value. The like-for-like change is **3.240e-4 → 3.511e-4 (+8.3%)**, net +1.9% versus the registered 3.4457e-4.
- "Registered 3307 had no proof of this step" is fair. The registered 3307 is not supported once interplay is charged: 3389–3407 under BI.

### Reconciling 3067 (PR #83) with 3407 (P2)
There is no contradiction; they are different charges.
- 3067 = sharp span + **bare** activities (interplay unproved).
- 3389 / 3407 = sharp span + BI decorations. These are e^{κ(ℓ+7)} on each activity and +12κ/5 in the KP condition, which pushes a from 1.5e-3 to 4.3e-3 and S₀ up by 8.3%.
- PR #83's own sensitivity table predicts the move: ×1.085 falls between 3181 (×1.03) and 3463 (×1.10).
- At C = 8.8e-4 all routes give 1409. The robust threshold is unaffected.

## 7. Consistency with the register and existing Line N evidence
- `record/claims.json` is untouched by PR #83 (and by PR #85).
- TRACE-332's A_bad^KP values (3.4457e-4, 2.3798e-6, 2.1548e-6) and a = 8.25e-6 at 8.8e-4 are all reproduced.
- TRACE-333's 3305/3307, 1726/1733 and 1402/1409 are reproduced.
- The span result is the rigorous form of N20 §3.4's sketch "span ≤ 0.787j + O(1)" (the O(1) is 3; N20 measured max(span − 0.787j) = 2.77 on j ≤ 14, mine 2.776). It is not new in idea, but new as [P]. All three write-ups say so (PR #83 implicitly).
- Nothing contradicts TRACE-325/336/301 boundaries:
  - H1 stays [H];
  - H3 stays conditional;
  - H5–H8 are untouched;
  - R′ and BGS-BGS-001 stay open.
- The PR #83 SELF_REFEREE §3 point is confirmed: stored `a_enum` `word` integers are `int()`-truncated floats on 2182/5109 classes. Every mismatch is exact − sign(exact). span and zr are exact, so the Thm A bad set is unaffected.
