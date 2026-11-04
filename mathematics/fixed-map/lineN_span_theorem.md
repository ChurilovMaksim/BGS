# The balanced ε-digit span on ℤ[√2] (span theorem) and its effect on Prop. K

Integrated 4 November 2026 (registry BGS-TRACE-337 to BGS-TRACE-341). Status per item is given
in brackets. Nothing in this note proves H1 (BGS-TRACE-336), H3, frozen R′ (BGS-TRACE-206), or
any BGS statement, and it changes no registered threshold.

**Sources and credit.**
- PR #85 (branch `research-grok46-1104`, `evidence/research/20261104_grok47/proofs/span_law.md`):
  Theorem A, Lemmas 1–9, the witnesses. Statement and lower bound are taken from there.
- Research note P2 `SPAN_LEMMA.md` (Lemma S): the two-lift proof of the upper bound (§3 below).
- PR #83 (branch `research-cloud-1104`, `evidence/research/20261104_cloud/proofs/01_span_bound.md`,
  `04_propK_sharp.md`): the floor-form upper bound (§4, secondary derivation), the census through
  shell 16 and the bare-activity crossover rows.
- Research note P2 `BACKGROUND_INTERPLAY.md` (Lemma BI): §8.
- Independent referee audit of PR #83 with PR #85 and P2 cross-checks (4 Nov 2026): every
  item below was marked CONFIRMED there, after the fixes applied in this note
  (red range, the 8 < ε⁴ step, the norm-form/shell-form equality wording, c_ε = 0.786440,
  Corollary B restricted to near-sharpness, BI reported at the minimal KP weight).
- Prior idea: N20 §3.4 already sketched "reductions occur only where |σ_i(μ)λ^{±t}| ≥ ½, giving
  span ≤ 0.787 j + O(1)" [P-sketch]. The result is the rigorous form of that sketch (the O(1)
  is 3, and 0.787 is c_ε = log 2/log ε); it is not new in idea.

Reproduction: `computations/verification/lineN_span/` (scripts and committed logs);
receipt `evidence/executions/20261104/span_theorem/receipt.json`.

## 1. Setting

ε = 1+√2, ε̄ = 1−√2 = −ε⁻¹, λ = ε² = 3+2√2. For α = a + b√2 ∈ ℤ[√2]∖{0},
N(α) = a² − 2b² = σ₊(α)σ₋(α). Shell j means 2^j ≤ |N(α)| < 2^{j+1}. The class of α is its
orbit under α ↦ ±ε^k α; the fundamental domain used by the project enumerators
(`lineN14/code/a_enum.py`) is σ₊(α) > 0, 1 ≤ σ₊(α)/|σ₋(α)| < λ.

Let μ = (√2/4)α and θ_k = σ₊(μ)ε^k, θ̄_k = σ₋(μ)ε̄^k. If αε^k = A + B√2 then
θ_k = B/2 + (A/4)√2 and T_k := θ_k + θ̄_k = B ∈ ℤ, and |θ_k θ̄_k| = |N(α)|/8.
Both θ and T satisfy z_k = 2z_{k−1} + z_{k−2}.

red(x) = x − ⌊x + ½⌋ ∈ **[−½, ½)**. Put n_k = ⌊θ_k + ½⌋, τ_k = θ_k − n_k = red(θ_k), and

  E_k = n_k − 2n_{k−1} − n_{k−2} = 2τ_{k−1} + τ_{k−2} − τ_k.

span(α) is the length of the word from the first to the last nonzero E_k (internal zeros
counted). L(α) := log_ε(|N(α)|/2), and c_ε := log 2/log ε = **0.7864397013573949…**
(the value 0.786448 in P2 was a typo).

## 2. Theorem A and corollaries [P]

**Lemma 1 [P].** E_k ∈ {−1, 0, 1}. (2τ_{k−1} ∈ [−1,1), τ_{k−2} ∈ [−½,½), −τ_k ∈ (−½,½]; the
sum lies in (−2, 2).)

**Lemma 2 [P].** θ_k ∈ ℤ + ½ iff A = 0 and B is odd; |θ_k| = ½ iff αε^k = ±√2. So the class of
√2 (|N| = 2) is the only class on which |θ_k| or |θ̄_k| equals ½ (the exceptional class).

Let K_L = min{k : |θ_k| ≥ ½} and K_R = max{k : |θ̄_k| ≥ ½}.

**Lemma 3 [P].** n_k = 0 for k < K_L; n_k = T_k for k > K_R; hence E_k = 0 for k < K_L and for
k > K_R + 2.

**Lemma 4 [P].** On every non-exceptional class E_{K_L} = n_{K_L} = ±1 and
E_{K_R+2} = T_{K_R} − n_{K_R} = ±1; so span = K_R − K_L + 3. (Left end: θ_{K_L} ∈ (½, ε/2) or
(−ε/2, −½), so θ+½ ∈ (1, 1+√2/2) or (−√2/2, 0). Right end symmetric.)

**Lemma 5 [P].** For α = √2: K_L = K_R = 0, word [1, −1], span 2 (while K_R − K_L + 3 = 3).

**Lemma 6 [P].** Δ := K_R − K_L satisfies L − 2 < Δ ≤ L, with Δ = L only on the exceptional
class: |θ_{K_L}||θ̄_{K_R}| = |N|/(8ε^Δ) ∈ [¼, ε²/4). (Δ = −2 is possible and handled.)

**Theorem A [P] (BGS-TRACE-337).** For every α ∈ ℤ[√2]∖{0},

  L(α) + 1 < span(α) < L(α) + 3,

all letters lie in {−1, 0, 1}, and span(α) = K_R − K_L + 3 on every class except the class of √2,
where span = 2. The span is a class invariant.

**Corollary B [P, finite witnesses].** Neither constant 1 nor 3 in Theorem A can be improved by
more than 3.4·10⁻⁴ (witnesses 82√2 and 116 in §6). This note does **not** claim that 1 and 3 are
the best constants; that would need a sequence of classes whose defect span − L accumulates at
1 and at 3, which is not proved here.

**Corollary C [P], shell form.** In shell j, span(α) < c_ε j + 3 (since |N|/2 < 2^j). For
j ≥ 1, c_ε j is irrational, so span ≤ ⌊c_ε j⌋ + 3. For j ≥ 2, ⌊c_ε j⌋ + 3 ≤ 2j.

**Corollary D [P].** For every class in shell j and g₀ ≥ 0, ℓ = span + g₀ < c_ε j + 3 + g₀; in
particular for the bad classes of H1-shell. The N20 Prop. K majorant ℓ ≤ 2j + g₀ (j ≥ 5,
[P-sketch]) is therefore a theorem for j ≥ 2.

Equality cases. The norm form ⌊L⌋ + 3 is attained at α = 2 (n_k = 0, 0, 1, 2, 4, 10, 24 at
k = −2…4; word (1, 0, −1); span 3 = ⌊log_ε 2⌋ + 3). The shell form ⌊c_ε j⌋ + 3 is attained,
e.g., at α = 3+√2 (and 1+2√2) in shell 2 (span 4), not by α = 2. Through shell 16 it is
attained in shells 2, 5–8, 10–13, 15, 16 and in no class of shells 0, 1, 3, 4, 9, 14 [finite].

## 3. Proof of the upper bound (two-lift argument, P2 Lemma S) [P]

Put x_k = σ₊(μ)ε^k = θ_k and y_k = −σ₋(μ)ε̄^k = −θ̄_k. Both satisfy the recurrence, and
x_k − y_k = T_k ∈ ℤ (since Tr((√2/4)β) = v ∈ ℤ for β = u + v√2), so x_k ≡ y_k (mod 1).

If |z_i| < ½ for i ∈ {k−2, k−1, k}, with z = x or z = y, then τ_i = red(z_i) = z_i (the
representative in (−½, ½) is unique and congruent), and E_k = 2z_{k−1} + z_{k−2} − z_k = 0. For
z = x this happens whenever |σ₊(μ)|ε^k < ½; for z = y whenever |σ₋(μ)|ε^{−(k−2)} < ½. Hence a
nonzero letter needs k ∈ [k₁, k₂] with k₁ = log_ε(1/(2|σ₊(μ)|)), k₂ = 2 + log_ε(2|σ₋(μ)|), and

  span ≤ k₂ − k₁ + 1 = 3 + log_ε(4|σ₊(μ)σ₋(μ)|) = 3 + log_ε(|N(α)|/2),

since |N(μ)| = |N(√2/4)|·|N(α)| = |N(α)|/8. Strictness: the first and last nonzero letters are
integers in [k₁, k₂]; if k₂ − k₁ + 1 were attained, both endpoints k₁, k₂ would be integers with
|θ_{k₁}| = ½, which by Lemma 2 forces the exceptional class, where span = 2 < 3 = L + 3. So
span < L + 3 for every class. The argument handles both parities and half-integer values
without a separate lemma, because it uses only |z| < ½ regions. ∎

The lower bound span > L + 1 is Lemmas 4–6 (PR #85).

## 4. Secondary derivation (PR #83 `01_span_bound.md`), with the referee's fixes [P]

- **Range of red.** red(x) ∈ [−½, ½) (not (−½, ½]). The project's odd-site twist −red(−x)
  lands in (−½, ½]; it differs from red(x) only when red(x) = −½. Neither slip is used: the proof
  only uses the regions |·| < ½.
- **Support cut.** With real k_L, k_R defined by |θ_{k_L}| = ½ = |θ̄_{k_R}|, k_R − k_L = L. For
  k ≤ ⌈k_L⌉ − 1 the three indices lie below k_L (n = 0); for k ≥ ⌊k_R⌋ + 3 they lie above k_R
  (n = T). So the nonzero letters lie in [⌈k_L⌉, ⌊k_R⌋ + 2] and span ≤ ⌊L⌋ + 3.
- **Shells and the comparison with 2j.** ε⁴ = 17 + 12√2, and 32 < 17 + 12√2 ⇔ 15 < 12√2 ⇔
  225 < 288. Hence 8 < 32 < ε⁴, so c_ε < 4/5 < 4/3, and span ≤ ⌊4j/5⌋ + 3 and
  ⌊c_ε j⌋ + 3 ≤ 2j for j ≥ 3 (indeed for j ≥ 2). (PR #83 wrote "8 < 17+12√2 iff 15 < 12√2";
  the correct reduction is −9 < 12√2, and the step is replaced here by 8 < 32 < ε⁴.)
- **Equality.** α = 2 attains the norm form ⌊L⌋ + 3 (it has |N| = 4 and span 3). The shell form
  ⌊c_ε j⌋ + 3 is attained first in shell 2, by 3+√2 (and 1+2√2), with span 4.
- **ε-shift.** "Multiplying α by ε preserves the span" is true (class invariance, Theorem A /
  Lemma 4), but the proof is PR #85's K_R − K_L + 3 formula, not the index shift alone, because the
  shift changes parity.

The floor form span ≤ ⌊L⌋ + 3 and the strict form span < L + 3 agree for |N| ≠ 2; at |N| = 2
the strict form gives 2.

## 5. Lemma 8: project word = digit word [P] + production check [finite]

`digits.eps_digits` (lineN14) uses seeds (2a, 2b), even sites red(θ_{2t}) and odd sites
−red(−θ_{2t−1}) (the B-embedding is −θ_{−1}, PR #85 Lemma 7).

**Lemma 8 [P] (BGS-TRACE-338).** On a fundamental-domain representative, θ_k is never a half-integer at an odd
index. Consequently the project twist equals red(θ_k) at every k and the project word equals the
digit word of §1. (A half-integer θ_k forces αε^k = B√2, whose ratio σ₊/|σ₋| is 1; the
representative α = ε^{−k}B√2 has ratio λ^{−k}, which lies in [1, λ) only for k = 0, even.)

Production check (`code/production_match.py`, `logs/production_match.json`):
- `lineN14/logs/a_enum.jsonl` (5109 classes, j ≤ 12): span and zr equal the exact census on all
  5109 classes.
- N20 `a_cert_ext*.jsonl` (j = 13, 14; 5100 + 10225 classes): span and zr equal the exact census
  on all 14987 rows that store them (15325 rows in all, j = 13, 14); the 338 `coded` rows all have exact zr ≥ 6.
- The stored integer `word` of `a_enum.jsonl` differs from the exact word on 2182 classes, in
  each case letter-wise exact − sign(exact) (int()-truncated floats). span and zr are exact, so
  the finite bad set of Thm A (BGS-TRACE-331) is unaffected.
(PR #85's own finite comparison used KK = 8/12 and higher dps, not the production KK = 6 /
dps 34; the check above uses the production files.)

## 6. Examples [P] (BGS-TRACE-339)

| α | N | shell | word | internal zero run | span − L |
|---|---:|---:|---|---:|---|
| 116 | 13456 | 13 | [1,−1,0⁹,1,1] | 9 | 2.99966264991176 |
| 82√2 | −13448 | 13 | [1,1,0⁷,−1,1] | 7 | 1.00033740024809 |
| 118 | 13924 | 13 | [1,−1,0³,1,0,−1,0³,1,1] | 3 | 2.96087221277804 |

Words, spans and runs are exact integer computations; the defects are mpmath (40 digits) values
of span − log(|N|/2)/log ε, printed to 15 digits. 118 is a bad class at g₀ = 4 (run 3 < 4);
116 is not (run 9). The Lean module `formalization/Bgs/LineNSpanArith.lean` checks the norms, the
shells, ε⁴ = 17 + 12√2, 225 < 288, and integer floor certificates for the words of 116, 82√2,
118, 2 and 3+√2 on a window (kernel `decide +kernel`); it does not formalise Theorem A, the real
sign test, or the vanishing of the digits outside the window.

## 7. Finite census [finite, exact]

`code/span_census.py 16` enumerates every fundamental-domain class with |N| < 2^17 (81709
classes; shells 0–16: 1, 1, 3, 4, 11, 20, 42, 78, 161, 316, 643, 1274, 2555, 5100, 10225, 20430,
40845), with exact integer digits. Results (`logs/span_census_J16.json`): span − ⌊L⌋ ∈ {2, 3}
with histogram {2: 43304, 3: 38405}; 0 letters outside {−1, 0, 1}; span = K_R − K_L + 3 on every
non-exceptional class; the strict two-sided bound checked exactly on every class; 0 violations of
the floor and shell forms; 0 classes with span > 2j for j ≥ 2; min and max of span − L are
1.00005788517 (α = 280) and 2.99994211631 (α = 198√2). This is a check of the proof, not the
proof.

## 8. Effect on Prop. K and the crossover [P-arith, CONDITIONAL] (BGS-TRACE-341)

All numbers in this section are conditional on H1-bad (BGS-TRACE-336, open) through its constant
C, use the V5 crossover logic with its idealised additive terms, and are reproduced by
`code/crossover_sharp_bi.py` (mpmath, dps 40; `logs/crossover_sharp_bi.json`, `.log`). They do
**not** change Theorem v5, the registered thresholds 3307 / 1409 of BGS-TRACE-333, or the state of
BGS-TRACE-301, 332, 336 or 206.

**Bare activities (sharp span, interplay not charged).** Replacing ℓ ≤ 2j + g₀ by Corollary D
in the Prop. K tail (C = 0.082, J₀ = 12): the slope-2 fixed point at the minimal KP weight gives
first prime 3299 (the registered 3307 is the same slope-2 majorant at the N20 ×1.02 iterate,
δ_eff 3.4962e-4), and the sharp span gives **3067** (a = 1.52315e-3, S₀ = 3.24040e-4). This is a
**bare-activity majorant only**: the model–background interplay is not charged in it.
Sensitivity of 3067 to S₀ × (0.99, 1, 1.01, 1.03, 1.10): 3037, 3067, 3109, 3181, 3463.
C = 0.04: 1721. C = 8.8e-4: **1409** (unchanged).

**Lemma BI (P2 `BACKGROUND_INTERPLAY.md`) [P mod (M)] (BGS-TRACE-340).** Under hypothesis (M) — the level-h_p
coded gas is a hard-core product-activity polymer system on ℤ/p with model polymers (support
≤ 3, ℓ_M ≤ 7, per-site anchored activity A_M ≤ 1.03e-3) and bad polymers, with **bad–model gap
interactions absent or inside δ**, wrap-around polymers excluded — one has the exact factorisation
Z = Z_M·Z̃ (Z̃ a polymer system of decorated bad polymers; Ueltschi 2004 Thm 1), decorated
activities bounded by u(γ)e^{κ(ℓ(γ)+7)}, and, when S* + (S₁* + 12κ)/5 ≤ a, the bound
|ln Z̃| ≤ p·S̃₀, i.e. |Z| ≥ |Z_M|e^{−pS̃₀}. **Not proved:** (M) itself (a residual [P-sketch]
not covered by δ_true as registered), and the per-site / factor-2 normalisation of A_M relative
to S₀'s factor 2. Numbers (C = 0.082, J₀ = 12): **3389** at the minimal KP weight
(a = 4.318e-3, κ = 1.1112e-3, S̃₀ = 3.51054e-4) and **3407** at the N20-style ×1.02 iterate
(a = 4.409e-3, S̃₀ = 3.51654e-4); both are valid sufficient primes under the stated hypotheses.
C = 0.04: 1753; J₀ = 13: 2237; J₀ = 14: 1831; A_M × 2: 3907; ℓ_M ≤ 8: 3433;
C = 8.8e-4: **1409** (unchanged). Like-for-like, the charge moves 3.240e-4 → 3.511e-4 (+8.3%),
i.e. +1.9% against the registered 3.4457e-4. The registered 3307 is not supported once the
interplay is charged by BI; 3389–3407 are the BI values, and none of these numbers is registered
as a replacement of 3307.

**Boundary note on H1 ⇒ H3 (BGS-TRACE-332).** With Theorem A, the H3 step of Prop. K needs only
the shell-law half H1-bad of H1, not H1-ali, and the step is proved modulo hypothesis (M) and
the unproved per-site normalisation above (it is not an unconditional [P] implication). H1
itself stays open.

**J₀ = 14 (bare, for information).** H1-shell(C, 12) implies H1-shell(C, 14), and shells 13–14 are
certified for the core functional by BGS-TRACE-331; the bare sharp-span threshold at J₀ = 14 is
1787 (C = 0.15: 3019). Restating BGS-TRACE-325/333 at J₀ = 14 is a registry change that is not
made here.

## 9. Non-claims

- No bound on |r_A r_B|, no proof of H1, H3, R′ or BGS universality.
- Corollary B is near-sharpness by explicit witnesses only.
- The crossover numbers are conditional, use the idealised additive terms of V5, and are
  mpmath recomputations, not interval certificates.
- The registered values 3307 and 1409 (BGS-TRACE-333) and the states of BGS-TRACE-301, 332, 336
  and 206 are unchanged.

## 10. Registry rows

| ID | State | Content |
|---|---|---|
| BGS-TRACE-337 | proved | Theorem A with Corollaries B (near-sharpness only), C, D |
| BGS-TRACE-338 | proved | Lemma 8 and the production-file comparison |
| BGS-TRACE-339 | proved | Examples 116, 82√2, 118 (and α = 2) |
| BGS-TRACE-340 | conditional | Lemma BI, conditional on (M) and the A_M normalisation |
| BGS-TRACE-341 | conditional | Sharp-span crossover rows (bare 3067; BI 3389 / 3407; 1409), conditional on H1-bad |
