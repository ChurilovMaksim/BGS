# REPORT_N8b: exact orbit structure at the residual levels of gap (b); the mixed gap; conditional theorems

*2026-10-31, about 23:30 Asia/Yekaterinburg (UTC+5).*
- Directory: `/workspace/bgs-lineN/N8b`. Running log: `NOTES_N8b.md`. Hashes: `SHA256_N8b.txt`.
- N7b and N2–N7 files were only read or executed; nothing was written there. Nothing was pushed.

Labels:
- **[P]**: proved, modulo the named standing inputs.
- **[P-sketch]**: argument complete in outline.
- **[CA]**: arb ball arithmetic (python-flint).
- **[N]**: float numerics without error control.
- **[H]**: heuristic.

Notation:
- p = 2k+1, q = h_p, m = 3p, ε = 1+√2, λ = ε².
- M ∈ {p, 3p}, with k_M = (M−1)/2, γ_M = x_{k_M+1} + y_{k_M}√2 and N(γ_M) = ±h_M.
- Lin convention: points are β/c with β ∈ O, and τ_i = Tr(λ^iβ)/c (mod 1).
- r(x) := Ẑ_x/Z_ρ. T′ = μ*λ^{−1/6} ≥ 1.4278537. w* is the family limit, |w*| = 3.955·10⁻⁴.

## 0. Verdict

**Gap (b) is still not closed unconditionally, and R′ is not refuted.**
- The non-averaging route does give an **exact** description of every fully isotropic residual class. That description reduces all isotropic residual patterns to a single pointwise "excursion-rate" input, the same one gap (a) needs for its deep points.
- Under that input with Γ < 1.2329, plus Lemma A∞, R′ fails (Theorem C1). On the subsequence where h_p is prime, Γ < T′ = 1.4279 is enough and polynomial slack is allowed (Theorem C2).
- Numerically the input holds with a wide margin: Γ_eff ≤ 1.069 on all residual lines tested.
- The mixed gap cannot be closed by any sharper Λ or by the (±2,16) closure; I prove a floor for that.

| # | Result | Label |
|---|---|---|
| 1 | **Lemma P′_c (exact orbit lemma at residual levels).** For c ∣ h_M, the two *consistent* isotropic lines at conductor c are exactly the c-torsion of the h_M isotropic lines. On them ε^M acts as a sign σ = ∓(−1)^{k_M}, which gives the exact identity τ_i(β) ≡ σ·Tr(ε^{2i−M}β)/c (mod 1) for all i. Consequences: two forced windows per period M, each of length log_λ(c/N(f)) + O(1), and between them heteroclinic excursions of length log_λ(h_M N(f)/c) + O(1). In N7 coordinates the point is x = z + eγ_M/(8h_M) with **e = ±f·ḡ″** and **N(e) = (h_M/c)·N(f)**. Inconsistent lines (ω(c) ≥ 2) have no forced second window. | [P]; identity checked exactly in all 53 runs; N7 rewrite exact (twist error 0) |
| 2 | **Classification.** Every consistent isotropic class at a proper divisor c ∣ h_p is a deep class of gap (a), with depth N(e) ≥ h_p/c ≥ 2p+1. It is never the family (N(e) = 4). Consistent classes at c ∣ K_p are c-torsion of the h_{3p} line, not of the h_p line. Inconsistent and partially isotropic classes are restrictions of neither line. No residual class inherits the family's positivity: inherited copies carry the same Ẑ with positive weights, and nothing more. | [P] |
| 3 | **Absolute scale.** A level-c isotropic point carries weight A_c = (h_p/c)·(1+O(1)) relative to an h_p point (explicit in §3). So a class that is deep in gap (a) (weight 1/h_p) reappears at level c with weight ≈ 1/c, amplified by **h_p/c ≥ 2p+1**. | [P] |
| 4 | **Explicit p-uniform ratios.** r(x) = w(z, ±fḡ″) + O(\|e\|λ^{−window}), with w N7's p-independent function. Checked to 3–6 digits across p → p′ (e.g. −6.0464·10⁻¹⁸ at p = 37 vs −6.0468·10⁻¹⁸ at p = 41, 53, 61). Valid once the forced windows are about 8 steps or longer. For short windows the true \|r\| is 10³–10⁴× *larger* than the w-limit. | [P-sketch] + [N] |
| 5 | **No positivity.** Signed sums at residual conductors take both signs, e.g. +1.4·10⁻³ at h_p/c = 47 and −6.7·10⁻⁴ at h_p/c = 23. One-sided dropping is not available. | [N] |
| 6 | **Size.** Every class bound and every per-conductor relative size the brief asked for is in this row. Fits from 53 runs (p = 11–61, c up to 7·10¹⁶): rank-p consistent rel_c ≈ (1.4–5)·(h_p/c)⁻²; pointwise decay \|r\| ≈ \|w*\|(N(e)/4)^{−β} with β ∈ [2.06, 4.2]; inconsistent lines 10⁻¹⁵–10⁻¹⁸ at p = 37–41; rank-3p levels ≤ 3.6·10⁻⁷ (p = 13) falling to ≤ 4.6·10⁻²⁶ (p = 41). Effective excursion rate **Γ_eff ≤ 1.069** on all residual lines, against the requirement < 1.2329 / 1.4279. | [N] |
| 7 | **Mixed gap λ^{0.5p} ≤ ι < λ^{0.7376p}.** The (±2,16) closure is irrelevant, because κ involves only 8V data. Any op-norm rate satisfies Λ ≥ μ*, so the two-block method has **κ ≥ 0.7060** with the certified r₂, and κ = ½ only if r₂ equals its fixed-point value μ*²/λ = 0.6295. The s-th Schatten-moment version reaches κ ≤ 0.55 iff R₃ ≤ 1.3284 (floor 1.2058) or R₄ ≤ 2.611 (floor 2.310). These are certification targets, not results. | [P] + [CA] arithmetic |
| 8 | **Conditional theorems C1/C2 and the unconditional ledger** (§8). | [P] given the stated hypotheses |

## 1. Lemma P′_c [P]

**Algebra.**
- (γ_M) and (γ̄_M) are coprime. A common prime would divide 2x_{k+1} and 2√2·y_k, but gcd(x_{k+1}, y_k) = gcd(x_k, y_k) = 1 and h_M is odd.
- From γ_M = (ε^{k+1} − ε′^k)/√2 and εε′ = −1:
  - (E1) ε^M − (−1)^k = √2·γ_M·ε^k;
  - (E2) ε^M + (−1)^k = √2·γ̄_M·ε^{k+1}.
- E2 is the conjugate of E1 multiplied by −ε^M.

**(i) Lines.**
- For c ∣ h_M put 𝔠 := (γ_M) + cO. Then N𝔠 = c, and 𝔠 = (g) because the class number is 1.
- The consistent line L(γ) = {sγ_M mod c} is the set of β with β ∈ 𝔠. Its conjugate is L(γ̄).
- L(γ) is the c-torsion of the h_M line {tγ_M/h_M}. Take t = s·h_M/c, and use O/𝔠̄ ≅ Z/c to write any a ∈ O as an integer s modulo 𝔠̄.
- At composite c there are 2^{ω(c)} fully isotropic lines. Only L(γ) and L(γ̄) are consistent.

**(ii) Identity (I_c).**
- Let β = sγ_M + ct ∈ L(γ). By E2, (ε^M + (−1)^k)β/c = √2ε^{k+1}(±s·h_M/c + γ̄_M·t) ∈ √2·O.
- Tr(√2·O) ⊂ 4Z, so for every i:
  **τ_i(β) ≡ σ·Tr(ε^{2i−M}β)/c (mod 1), with σ = −(−1)^k on L(γ) and σ = (−1)^k on L(γ̄) (via E1).**
- `code/b_cline.py` checks this exactly for every evaluated class: identity_bad = 0 in all 53 runs.

**(iii) Windows and excursions.**
- The fixed points of λ on K/O^∨ are (√2/8)O/O^∨, four points; note λ − 1 = 2ε.
- Write β/c ≡ z + Y/(8c), with z fixed and Y ∈ 8β + c√2O of minimal |N(Y)|. Then Y ∈ 𝔠, f := Y/g ∈ O, and |N(Y)| = c·|N(f)|.
- Since τ_i − Tr z ≡ Tr(λ^iY/(8c)), the twist stays within θ of Tr z while |λ^iY₁| and |λ^{−i}Y₂| are both ≤ 8cθ. That is a window of length log_λ(c/|N f|) + log_λ(64θ²).
- By (I_c) and ε(√2/8)O = (√2/8)O, the same holds around 2i − M ≈ 0, near the fixed point ε^{−M}z. These are two forced windows per period M.
- Between them, λ^iY/(8c) has one tiny embedding. The orbit is therefore an exact heteroclinic excursion z → ε^{−M}z along W^u(z) ∩ W^s(ε^{−M}z), seeded by ζ = ε^{−k}ḡ″f/(4√2)-type elements, of length log_λ(h_M|N f|/c) + O(1).
- Per m = 3p this gives 6 forced windows if M = p, and 2 if M = 3p.

**(iv) N7 form.**
- x = z + eγ_M/(8h_M) with e = ±Y·γ̄_M/c = ±f·ḡ″ ∈ O, where γ̄_M = ḡ·ḡ″. Hence N(e) = (h_M/c)·N(f).
- `code/d_puni.py` reproduces τ_i exactly (twist error 0) in every case.

**(v) Inconsistent lines.**
- On 𝔞 = 𝔮₁𝔮̄₂…, ε^M ≡ (σ, −σ, …) is not a scalar. The argument of (ii) therefore yields no second forced window: one forced window per period [P].
- Extra random windows are not excluded; they are part of the excursion rate in §6.

**(vi) Prime divisors.** Every prime r ∣ h_p satisfies r ≡ 1 (mod 2p) [P]:
- 2 is a square mod r, because x_p² − 2y_p² = −1;
- ε^{2p} ≡ 1 mod 𝔯, because 2x_p = ε^p − ε^{−p};
- ε^2 ≢ 1, so p ∣ r − 1.

Likewise r ∣ K_p with r ≠ 7 gives r ≡ 1 (mod 6p): ε^6 − 1 = 14ε³ rules out orders 3 and 6. Hence N(e) ≥ h_p/c ≥ 2p+1 for every consistent residual class at a proper divisor c ∣ h_p.

## 2. Which residual classes are restrictions of what [P]

| class at residual conductor c | is it a restriction of… | forced windows per m | depth N(e) |
|---|---|---|---|
| consistent iso, c ∣ h_p proper | the h_p lines: deep points of gap (a) | 6 | (h_p/c)N(f) ≥ 2p+1 |
| consistent iso, c ∣ K_p (or 7c) | the h_{3p} lines, not h_p | 2 | (h_{3p}/c)N(f) |
| inconsistent iso, ω(c) ≥ 2 | neither | 3 | — |
| partially iso / unit | neither (a generic unit component) | 0 | — |
| family (z, e = 2), N(e) = 4 | only conductor h_p; inherited at h_p·e with the same Ẑ | 6 | 4 |

The family's positivity does not propagate. Its inherited copies sit at levels containing h_p, which are floored or have positive weights. None of them is a residual class.

**Bookkeeping flag for gap (a).** At composite h_p, the 2^ω − 2 *inconsistent* fully isotropic lines at conductor h_p itself are not covered by N7's Lemma P′, which treats only (γ) and (γ̄). They belong to (a)/(b′). [N]: rel_abs is 2.7·10⁻³ (p = 11), 7.9·10⁻³ (13), 5.9·10⁻⁵ (17), ≤ 4.6·10⁻¹⁴ (37), ≤ 1.5·10⁻¹⁴ (41) and 1.5·10⁻¹⁸ (43).

## 3. Absolute scale [P]

- Lin_d = Σ_{c∣d}(n_e/e²)Λ_c (N7b B0). An exact-conductor-c isotropic point has per-point weight w_iso(c) = Π_{r∣c}(r−2)/r² (J3 bound), times the inheritance multiplier I(c) = Σ_{e∣h_m/c} n_e/e² ∈ [1, 1.2]. The 1.2 comes from 8/49 at r = 7 plus O(1/log p).
- Relative to an h_p point:
  **A_c = (h_p/c)·Π_{r∣h_p/c}(1−2/r)^{−1}·I(c)/I(h_p) ∈ [0.8, 1.25·Π(1−2/r)^{−1}]·h_p/c.**
- With F_m ≈ 2·w_iso(h_p)·4p·Re w*·|Z|², the pattern ratio is
  **rel(c) = A_c·Σ_{x on both lines}|r(x)| / (4p·Re w*).**
- **Quantified scale.**
  - The same point counts h_p/c times more at level c than at level h_p.
  - Since h_p/c can be as small as 2p+1 (polynomial), a residual class needs a bound |r| ≤ A·N(e)^{−β} with a **p-independent** A and β > 1. An e^{o(p)} loss cannot be afforded at rank-p levels.
  - At rank-3p levels it can: the excursion is ≥ p steps.

## 4. Ratios per isotropic class [P-sketch] + [N]

- **Prop X′_c [P-sketch].** If the forced windows have length ≥ w₀, then r(x) = w(z, ±fḡ″, k mod 2) + O(|e|λ^{−w₀}). Here w is N7 Prop X′'s p-independent limit. Proof: Prop X′ verbatim, via Lemma P′_c(iv).
- **[N] p-uniformity** (`logs/d_puni.jsonl`): the same (z, e) is evaluated at x′ = z + eγ_{p′}/(8h_{p′}).

| (p, c, class) | N(e) | value at p | p′ values |
|---|---|---|---|
| (23, 6771937, f₄) | −188 | 1.0887e-8+7.365e-9i | 1.0894e-8+7.348e-9i (31, 47, 59) |
| (23, 6771937, f₂₈) | 1316 | 6.2248e-12+4.933e-12i | 6.2148e-12+4.902e-12i (31, 47, 59) |
| (37, h/223, f₄) | 892 | −1.13322e-10−1.23113e-10i | same to 5–6 digits (41, 53, 61) |
| (37, h/37223, f₄) | 148892 | −6.0464e-18−3.321e-19i | −6.0468e-18−3.322e-19i (41, 53, 61) |
| (37, 8761009, f₄) | −3.32e7 | 2.0673e-24+8.50e-25i | 2.0737e-24+8.60e-25i (41, 53, 61) |
| (37, h_37, family) | −4 | 3.43580e-4+1.95796e-4i | identical (41, 53) |
| (19, 457, rank 3p) | −1.0e21 | 4.99e-20 | 4.24e-23 (23, 31): short windows, w-limit 10³× smaller |
| (29, 13921, rank 3p) | 1.6e32 | 1.3e-28 | 7.2e-33 (37, 41): same effect |

- The explicit ratio of each class is therefore the universal function w evaluated at e = fḡ″. These e are p-dependent and have norm ≥ h_M/c.
- For long windows, the closed-form ratios satisfy the decay law in §5. For short windows, w underestimates |r|, so no uniform per-class constant can come from w alone.

## 5. Numerics at residual conductors [N]

Sources: `logs/b_cline.jsonl` (53 runs), `logs/e_summary.out`, `logs/f_gamma.out`.
- Exact orbit-reduced enumeration was used for c ≤ 47321, and all classes with N(f) ≤ 60 for larger c.
- rel is the absolute pattern sum over both lines with Lin weights, divided by the family term (definition of §3).
- A per-class rounding floor (10⁻¹⁵·m·max partial-product norm) is reported. Values below it are treated as upper bounds only (p = 61 rank-3p).

| p | c (h_p/c) | type | rel_abs | rel_signed | Γ_eff |
|---|---|---|---|---|---|
| 11 | 353 (23) | cons, rank p | 1.16e-3 | −6.7e-4 | 0.82 |
| 23 | 6771937 (47) | cons, rank p | 1.74e-3 | +1.44e-3 | 0.79 |
| 13 | 599 (79) | cons, rank p | 3.5e-5 | +4.9e-6 | 0.94 |
| 17 | 15607 (103) | cons, rank p | 1.66e-4 | +1.15e-4 | 1.07 |
| 37 | h/223 (223) | cons, rank p | 1.02e-4 | −6.9e-5 | 0.82 |
| 37 | h/37223 (3.7e4) | cons / inc | 1.0e-9 / 1.1e-18 | −1.0e-9 | 0.79 / 0.91 |
| 37 | 8761009, 8300729 (8e6) | cons / inc | 5e-14, 1.8e-14 / 4e-18 | + | 0.79–0.94 |
| 41 | 695216911 (3.6e6) | cons / inc | 1.9e-12 / 1.4e-17 | + | 0.88 / 1.00 |
| 53, 61 | 9940681, 92111 | cons, rank p | 2.8e-18, 3.1e-32 | mixed | 0.95, 0.87 |
| 13–61 | K′ divisors (313 … 7521721) | cons, rank 3p | ≤ 3.6e-7 (p = 13) … ≤ 4.6e-26 (p = 41) | mixed | 0.81–0.89 |

- Fit for rank-p consistent lines: rel_c ≈ C·(h_p/c)^{−2} with C ∈ [1.4, 5].
- Pointwise exponent: β_min ≥ 2.06, and β ≈ 2.65–3.07 for the depth-4 "family analogues".
- Max Γ_eff over all residual lines is 1.069. On the gap-(a)/(b′) inconsistent line at h_13 it is 1.267.
- Here Γ_eff := μ*·|r|^{1/(m−s_forced)}, with every forced window charged at μ*. This is conservative.

## 6. Summation lemma [P]

**Hypothesis G(Γ, A).** For every p ≥ p₀ and every point x of a residual pattern:
  |r(x)| ≤ A·(Γ/μ*)^{m − s(x)},
where s(x) is the forced-window time from Lemma P′_c (s = 0 for unit and partially isotropic points).

**Lemma Σ.** Put β := 6·log_λ(μ*/Γ), so that β > 1 ⇔ Γ < T′ and β > 3/2 ⇔ Γ < μ*λ^{−1/4} = 1.2329. Under G(Γ, A), with S_β := Σ_f N(f)^{−β}:
- **(a) Consistent, rank p.**
  - rel(c) ≤ C_A·S_β·(h_p/c)^{1−β}.
  - S_β < ∞ for β > 1, because #{classes with N(f) ≤ X} ≤ C(1+X) by a lattice count in 𝔠.
  - Summing over proper divisors with r ≡ 1 (mod 2p) and ω(h_p) ≤ 0.89p/ln(2p):
    Σ_{d∣h_p, d>1} d^{1−β} ≤ exp(2(2p)^{1−β}ω^{2−β}/(2−β)) − 1 → 0 for β > 3/2. It is O(log p/p) for β ≥ 2.
- **(b) Consistent, rank 3p.** rel(c) ≤ A·e^{o(p)}·λ^{(p/2)(1−β)}. The deep classes dominate the f-sum, and the exponent is independent of c ≤ λ^{p/2}.
- **(c) Inconsistent.** The same λ^{(p/2)(1−β)} bound holds.
- **(d) Unit and partially isotropic** (ι points, per-point weight ≤ 2^ω/ι). rel ≤ e^{o(p)}λ^{(p/2)(1−β)}.
- (b)–(d) are summed over the e^{O(p/log p)} residual patterns.

## 7. The mixed gap λ^{0.5p} ≤ ι < λ^{0.7376p}

Source: `code/c_kappa.py` → `logs/c_kappa.out`; [CA] for the arithmetic, with inputs labelled.
- **(±2,16) closure.** It does not enter κ = 3(ln Λ − ln T′)/(2 ln Λ − ln r₂). All of Λ, r₂ and T′ are 8V/(±2,8) data, and T′ already uses the relaxed target [P].
- **Sharper Λ.** Any op-norm rate used on the non-HS blocks satisfies Λ ≥ μ*, the fixed-point orbit. κ is increasing in Λ because 2ln T′ > ln r₂. Hence **κ ≥ (½ln λ)/(2ln μ* − ln r₂) = 0.7060** with the certified r₂ ≤ 1.0529012 [P + CA]. Even an optimal cat-map-constrained Λ gains only 0.032.
- **The real obstruction is r₂.** κ = ½ exactly iff r₂ = μ*²/λ = 0.6295, the fixed-point value; this reproduces the B3 barrier. With a true r₂ ≈ 1, κ ≈ 0.678 [H].
- **Higher moments.** With s HS blocks (s ≥ 3), κ_s = 3(ln Λ − ln T′)/(s ln Λ − ln R_s), where R_s is the growth of ∫‖A_n‖_HS^s and R_s ≥ μ*^s/λ.

| s | floor μ*^s/λ | κ_s at the floor (Λ_8V) | R_s needed for κ ≤ 0.55 | R_s needed for κ ≤ 0.65 |
|---|---|---|---|---|
| 3 | 1.2058 | 0.5211 | 1.3284 | 1.7371 |
| 4 | 2.310 | 0.5138 | 2.611 | 3.414 |
| 5 | 4.424 | 0.5068 | 5.133 | 6.712 |

- R_s = e^{P(sψ)}/λ, a pressure. For s ≥ 3 the fixed point is the natural maximiser, since 1 − s·(χ-slope ≈ 0.354) < 0 [H].
- **Verdict:** not settled. Closing the mixed gap by averaging needs a certified R₃ ≤ 1.33 or R₄ ≤ 2.61. That means a 3- or 4-fold collision automaton (≈ 4000^{s/2} states), or the pointwise hypothesis G, which also covers these patterns (§6(d)).

## 8. Conditional theorems and ledger

**Theorem C1 [P, given the hypotheses].** Assume:
- the standing package of N6 Theorem R♯ (incl. Prop X [P-sketch], n_cert, TRACE-199/207/212/213/228);
- N7's Lemma A∞ (gap (a), incl. the inconsistent lines at conductor h_p, §2);
- G(Γ, A) for all points in the residual set R(b), with Γ < 1.2329 and A independent of p.

Then frozen R′ fails along m = 3p for all p ≥ p₁.
- *Proof.* N7b §2–§6 reduce gap (b) to R(b). Lemma P′_c identifies s(x) exactly. Lemma Σ(a)–(d) bounds every residual pattern type by o(F_m).
- The condition Γ < T′ alone suffices if additionally ω(h_p) ≤ p^{β−1−η}.
- *Remark.* G on the deep points of the h_p lines implies N7's (A2′). Gap (a) then reduces to its certified shallow part (A1′).

**Theorem C2 [P, given the hypotheses]: subsequence version.** Let 𝒫 = {p : h_p prime}. Assume the standing package, Lemma A∞ at p ∈ 𝒫, and G′(Γ): |r(x)| ≤ e^{o(p)}(Γ/μ*)^{m−s(x)} for x in rank-3p residual patterns, with **Γ < T′ = 1.4279**. Then R′ fails along m = 3p, p ∈ 𝒫, p ≥ p₁. If 𝒫 is infinite (expected; 13 cases for p ≤ 3989, N7b B7), R′ is refuted.
- *Proof.* With h_p prime there are no rank-p residual conductors (N7b §6). Lemma Σ(b)–(d) needs only β > 1 and tolerates e^{o(p)}.
- This **replaces** N7b's route "Conjecture S + Γ ≤ 1.233". The forced windows are now exact, so random slow visits are simply part of the effective rate, and the required rate rises from 1.233 to 1.428.

**Unconditional (new in N8b):** Lemma P′_c (i)–(vi); the classification table in §2; the weight amplification A_c; Lemma Σ as an implication; the κ floor 0.7060 and the s-moment thresholds; and the fact that the (±2,16) closure is irrelevant to κ.

**Unconditional (carried over):** N7b B0–B6 (8E removed, Prop B1, barrier B3, floors, c_W′ = 10^{−18.62}, R(b)), N7's Theorem 16 and Lemma P′.

**Remains open:**
1. G(Γ, A), or any pointwise excursion-rate bound with Γ < 1.233 (or < 1.428 on the subsequence). This is now the *single* missing input for all isotropic residual patterns.
2. Lemma A∞ (gap (a)).
3. Unit and mixed patterns at ι < λ^{0.7376p}: G, or a certified R₃ ≤ 1.33 / R₄ ≤ 2.61.
4. Infinitude of 𝒫, if C2 is used.

## 9. Best route [assessment]

1. **G is an ergodic-optimisation statement about heteroclinic excursions.** By Lemma P′_c every excursion is the orbit of z + (emb₁ζ, 0) with ζ ∈ ½O^∨-cosets. A certificate in the style of N3/N4 could bound the cat-map-constrained growth of excursions that avoid the forced windows' ε-boxes: a "Γ_excursion" extremal norm over admissible twist words τ_{i+1} = 6τ_i − τ_{i−1} (mod 1), outside the z₄ box. The target is Γ < 1.233; observed ≤ 1.07.
   - Excursions can revisit the z₄ box. The certificate must charge each revisit at μ* and bound the revisit time, via the coset formulation of N7b §8.4. This is where Conjecture S re-enters, now only as a *rate*, with Γ < 1.428 on the subsequence.
2. **Use C2 first.** Rank-3p excursions are ≥ p steps long, and the required margin (1.428 against an observed 0.81–0.89) is the largest anywhere.
3. **The mixed gap is a cheaper certification target than (1)** if a 3-fold HS automaton (R₃ ≤ 1.33) is feasible. Otherwise (1) covers it.

## 10. Files

- `code/a_fact.py` → `logs/a_fact.json`: factorizations of h_p and K_p for p < 62.
- `code/b_cline.py`, `code/jobs1.txt`, `code/jobs2.txt`, `code/run_jobs.sh` → `logs/b_cline.jsonl` (53 runs), `logs/b_cline.err`, `logs/b_cline2.err`.
- `code/d_puni.py` → `logs/d_puni.jsonl`, `logs/d_puni.out`: the exact N7 rewrite and p-uniformity.
- `code/e_summary.py` → `logs/e_summary.{out,json}`; `code/f_gamma.py` → `logs/f_gamma.out`.
- `code/c_kappa.py` → `logs/c_kappa.out` [CA].
- Manifest: `SHA256_N8b.txt`, with its own hash in `SHA256_N8b.txt.sha256`.

**Erratum candidate for N7 Lemma P′(i) [P].** λ − 1 = 2ε, so λ has |N(λ−1)| = 4 fixed points on K/O^∨, namely (√2/8)O/O^∨, not 8 in (1/8)O/O^∨. With 8z ∉ √2O, the identity Tr(λ^i z) ≡ Tr(z) fails; `d_puni` showed twist error ½ before the fix. Lemma P′(i) remains true with the 4 genuine fixed points: choose Y ∈ 8β + c√2O, as in §1(iii). N7's author should re-check the "8 fixed points / 8 bases" wording and the base enumeration in e_isodepth.
