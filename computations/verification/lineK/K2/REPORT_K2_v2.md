# Line K2 report: attacking H♮_mid (frozen R′, TRACE-206)

Box `/workspace/bgs-lineK/K2/`, 31 Oct 2026 (UTC+5). Nothing was pushed. This builds on REPORT_v2.md (Line K with the referee fixes). Labels: [P], [P-check], [CA], [N], [H], [assessment], plus **[P-cite]**: proved modulo a cited published theorem whose hypotheses I checked but whose proof I did not re-verify.

**v2 (31 Oct 2026, after referee DELTA):** fixes W-F1 (non-cyclic W2′), W-F2 (1.4742), W-F3 (C1 is [H]), W-F4 ([assessment] labels in §3), W-F5 (certified-computation wording), W-F6 (no self-hash in NOTES), and the step 6/7 nits. REPORT_K2.md is kept unchanged.

## 0. Summary

**Not achieved:** an unconditional proof of H♮_mid or H♮. Frozen R′ is still not refuted unconditionally.

**Achieved:**
1. **(c) The Z-bound input is settled [CA].**
   - P* = {(±2,8), (±2,16)} (TRACE-206 text, line 107).
   - S_Z ≤ 0.5000001 for m ≥ 495, from Line F and the J3 §1 certificates (`../code/k2_SZ.py`).
   - So Prop K2 (large levels) is [P + CA] (REPORT_v2 §3).
2. **Theorem W (explicit Weil range), [P] modulo one operator input (OP).** Fix k. For p ≥ p₀(k), every conductor c ∈ {q, 7q} with q prime, q | h_{3p}, q ≤ c_k·p² contributes o(ξ_lo^m) to O♮, and so do its inherited copies.
   - c_k > 0 is explicit in terms of the Fourier ℓ¹-norm of a block observable.
   - **(OP) is the only extra input:** the cat-map second moment I_k of the true twisted operator families must satisfy I_k^{1/2k} < 1.28359 for (±2,8), and < 1.4742 for (±2,16).
   - **Toy evidence for (OP) [N]:** for a toy single-disc Galerkin (not the certified two-disc operators), the exact (carry-automaton) I_k has per-step ratio I_{k+1}/I_k = 1 to within 10⁻¹⁰. The rate is 1, far below 1.28. This is consistent with the unitarity Σ|ĝ(n)|² = ΣJ_n(1.8)² = 1 (**Conjecture C1**, [H]).
3. **Bourgain extension [P-cite], effective, constants not computed** (§9, N-F6). Bourgain's Mordell-type bound (binomial sums over subgroups, JAMS 2005) and BGK give, for every fixed C, the same conclusion for prime levels q ≤ p^C, with p₀(C,k) effective, constants not computed. The explicit literature (Cochrane–Pinner, Heath-Brown–Konyagin explicit) does **not** beat Weil for the binomial sums needed here (§3); superseded by Line N1′ (§9, N-F10).
4. **Clean conditional theorem (Theorem K2′).** Assume (OP). Frozen R′ ⇒ for every large m ∈ S⁺ some *open-range* conductor c carries a **slow λ-orbit**: a β whose k-block HS-average along {βλ^i/c} is ≥ ((1−δ)·1.28359)^{2k}. The open range is c ∈ (c_kp², L_m), c prime or composite with ≥ 2 large primes. This is an explicit, checkable equidistribution failure.
5. **Negative findings:**
   - **(b) Counting levels cannot work.** A single level with the trivial bound already beats D7 by (μ*/1.2836)^m.
   - **The open range dominates in practice [N].** Most prime factors of h_{3p} lie in p² < q < √h (factorisations for p ≤ 43).
   - **Two global approaches fail:** positivity via periodic points of the cat map, and β-moment/Markov bounds (§5).
   - **(d) Composite primitive conductors** with two large primes are ≥ (2p+1)², outside every explicit range.
   - **Toy traces at real levels [N]:** Weil-range levels have rates 1.07–1.21 < 1.2836. Some open-range levels have slow β with max rate 1.29–1.36 at small m. That is a maximum over β, not the weighted sum.

## 1. The Z-bound (direction (c)) [CA]

See REPORT_v2 §3 and `../code/k2_SZ.py`.
- (±2,8): Line F gives |Z| ≤ (1+λ^{−m})(½μ*^m + H₀), so C ≤ 0.5000001 for m ≥ 495.
- (±2,16): the J3 rest certificates give rate ≤ 1.6677 with coefficient sum ≤ 2.273·10⁵, so the effective C ≤ 3.8·10⁻²⁵ at m ≥ 495.
- Hence S_Z ≤ 0.5000001. Crossover of K2 non-vacuity: m ≈ 1.682·10⁹ [N].

## 2. Theorem W: the Weil range

**Setting.**
- m = 3p, q ≠ 7 prime, q | h_m, so r := r(q) ∈ {p, 3p} and q ≡ ±1 (mod 8).
- Let σ, σ̄ : O/q → F_q be the two embeddings, ℓ = σ(λ), so σ̄(λ) = ℓ^{−1}, and H = ⟨ℓ⟩ has order r.
- For a family F of twisted operators (L_τ^F)_{τ∈R/Z}, write P_k^F(y) = L^F_{Tr(λ^{k−1}y)}⋯L^F_{Tr(y)} for y ∈ T := (O⊗R)/O^∨. The families are:
  - for (±2,8): the lifted vertex/edge operators V_{a,τ}, E_{a,τ}, sectors a ∈ {0,2,4,6}, Line J v2 sector law;
  - for (±2,16): the block operators of L16.
- f_k^F(y) := ‖P_k^F(y)‖²_HS = Σ_{γ∈O} c_γ e(Tr(γy)). Here c_γ = Σ_{x_w−x_{w′}=γ} Tr(M_wM_{w′}^*), and A_k^F := Σ_{γ≠0}|c_γ| < ∞ (superexponential decay of ĝ).
- I_k^F := c_0 = ∫_T f_k^F.
- Ẑ_β is a fixed finite combination of Tr Π_{i∈Z/m} L^F_{τ_i(β)} with τ_i(β) = Tr(βλ^i)/q, plus finite-rank read-outs (Line J v2 sector law; L16).

**Lemma W1 (Weil) [P-cite: Weil bound for twisted Kloosterman sums and Gauss sums].** For A, B ∈ F_q not both 0: |Σ_{h∈H} e((Ah + Bh^{−1})/q)| ≤ 2√q, and ≤ √q if AB = 0.

*Proof.*
- 1_H = (1/e)Σ_{χ|_H=1} χ, with e = (q−1)/r characters.
- So Σ_{h∈H} ψ(Ah + B/h) = (1/e)Σ_χ Σ_{x∈F_q*} χ(x)ψ(Ax + B/x).
- For AB ≠ 0 each inner sum is a twisted Kloosterman sum, of modulus ≤ 2√q (Weil).
- For B = 0, A ≠ 0 it is a Gauss sum: modulus √q for χ ≠ 1, and −1 for χ = 1. Hence ≤ ((e−1)√q + 1)/e ≤ √q. ∎

- [N] instance check, `code/w1_weil_check.py`: 20 pairs (p, q) with r(q) ∈ {p, 3p}, exhaustive over A, B. Max ratio 1.19 (binomial) and 0.59 (linear).
- **Application.** For β ≠ 0 and γ ∈ O, Σ_{i<r} e(Tr(γβλ^i)/q) = Σ_{h∈H} e((σ(γβ)h + σ̄(γβ)h^{−1})/q). It is *degenerate* (A = B = 0) iff γβ ≡ 0 (mod q):
  - for β a unit mod q this needs γ ∈ qO, so |N(γ)| ≥ q²;
  - for isotropic β ∈ 𝔮̄ ∖ 0 it needs γ ∈ 𝔮, so |N(γ)| ≥ q.
- **Level 7q, conductor 7q.** Split i by residue mod 3 (λ has order 3 mod 7, and r(q) ∈ {p, 3p} with p ≠ 3). Each part is a sum over a coset of a subgroup of F_q*, so the bound is ≤ 6√q, with the same degeneracy condition at q.

**Lemma W2′ (non-cyclic block AM–GM) [P]** (replaces the cyclic W2 of REPORT_K2.md; referee W-F1).
*Setting.* Let X = L_{τ_{m−1}}⋯L_{τ_0} be the product over positions 0..m−1, with a **bounded** read-out J [W-F7]:
- the (±2,16) read-out I⊗J_B (L16). It is **not** of finite rank: I acts on the infinite-dimensional lattice space and J_B is rank one only in the 2-dimensional block factor, so ‖I⊗J_B‖₁ = ∞. It is bounded, with ‖I⊗J_B‖ = ‖J_B‖ ≤ ½ (as in J3 `assemble16`); or
- J = I (the pure-trace (±2,8) sector laws).

Let 1 ≤ k and m ≥ 4k. Put Q = ⌊(m−1)/k⌋. For i ∈ Z set P(i) = L_{τ_{i+k−1}}⋯L_{τ_i} (τ_i is defined for all i ∈ Z, periodic in the application). Then
|Tr(J·X)| ≤ C_J·max(1, sup_τ‖L_τ‖)^{2k}·e²·max(1, (1/m)Σ_{i<m}‖P(i)‖²_HS)^{(Q−1)/2},
where C_J = ‖J‖·sup_τ‖L_τ‖₁/sup_τ‖L_τ‖ for every bounded J (‖J‖ = 1 for J = I; ‖J‖ ≤ ½ for I⊗J_B) [W-F7].

*Proof.*
1. **One offset.** Fix o ∈ [0, k). The Q−1 blocks P(o+jk), j < Q−1, lie inside [0, m), since o+(Q−1)k < k+(m−1)−k. Write X = R_o·P(o+(Q−2)k)⋯P(o)·S_o, where S_o has length o and R_o has length m−o−(Q−1)k. The leftovers have total length m−(Q−1)k ≤ 2k, and that length is ≥ k ≥ 1.
2. **Bound for one offset** [W-F7]. For any bounded J, put one leftover factor in trace norm: |Tr(JX)| ≤ ‖J‖·‖X‖₁ ≤ ‖J‖·sup‖L‖₁·(sup‖L‖)^{len−1}·Π_{j<Q−1}‖P(o+jk)‖, where len ∈ [k+1, 2k] is the total leftover length. Since (sup‖L‖)^{len} ≤ max(1, sup‖L‖)^{2k}, this gives |Tr(JX)| ≤ C_J·max(1, sup‖L‖)^{2k}·Π_{j<Q−1}‖P(o+jk)‖. No cyclic rotation and no finite-rank assumption is used.
3. **Product over offsets.** Multiply over o ∈ [0, k). The block starts B = {o+jk} = [0, (Q−1)k) are each used exactly once, and |B| = (Q−1)k ≥ m−2k. So |Tr(JX)|^k ≤ (C_J·max(1, sup‖L‖)^{2k})^k·Π_{i∈B}‖P(i)‖.
4. **GM ≤ QM.** Using ‖·‖ ≤ ‖·‖_HS and B ⊂ [0, m), the geometric mean over B is ≤ ((m/|B|)·(1/m)Σ_{i<m}‖P(i)‖²_HS)^{1/2}.
5. **Constants.** (m/|B|)^{(Q−1)/2} ≤ (1−2k/m)^{−m/(2k)} ≤ e² for m ≥ 4k. Replacing the average by max(1, ·) absorbs the base < 1 case. ∎

*Effect.* Compared with the cyclic version, the exponent drops from Q/2 to (Q−1)/2 (Q−1 ≥ m/k − 2), and the constant grows by max(1, sup‖L‖)^{2k}·e². Both are e^{O(k)}, independent of m. With base b := (I_k+3η) ≥ 1 we get b^{(Q−1)/2} ≤ b^{m/(2k)}. For b < 1 the max(1, ·) gives 1, which is harmless because then the bound is O(1) = o(ξ_lo^m). **Theorem W and Theorem K2′ are unchanged**, up to the constant C′ in step 3, which stays e^{O(k)}.

If τ_i(β) has period r | m, then (1/m)Σ_{i<m} = (1/r)Σ_{i<r}, and ‖P(i)‖²_HS = f_k(βλ^i/q).

**Lemma W3 (orbit average) [P].** For q ∥ h, β ≠ 0:
(1/r)Σ_{i<r} f_k(βλ^i/q) ≤ I_k + 2√q·A_k/r + T_k(q),
where T_k(q) := Σ_{γ≠0, |N(γ)|≥q} |c_γ| → 0 as q → ∞ (dominated convergence: each γ ≠ 0 has finite norm). For conductor 7q, replace 2√q by 6√q.

*Proof.* Expand f_k in its absolutely convergent Fourier series. The γ = 0 term gives I_k. Non-degenerate γ ≠ 0 are bounded by W1. Degenerate γ ≠ 0 have |N(γ)| ≥ q and are bounded trivially by |c_γ|. ∎

**Operator input (OP_k, δ).** For every family F of (±2,8): (I_k^F)^{1/2k} ≤ (1−δ)·1.28359. For every family of (±2,16): (I_k^F)^{1/2k} ≤ (1−δ)·1.4742, where 1.4742 < ξ_lo/1.6677 = 1.4742995 (the earlier 1.4743 was false; referee W-F2).

**Theorem W.** Assume (OP_k, δ). Choose η > 0 with (I_k + 3η)^{1/2k} ≤ (1−δ/2)·target. Let q₀ = q₀(k,η) satisfy T_k(q₀) ≤ η, and set c_k := (η/(6A_k))². Then there is p₀ such that for every m = 3p ∈ S⁺ with p ≥ p₀:

|Σ over conductors c ∈ {q, 7q : q prime, q | h_m, q ≤ c_kp²} of the cross parts, including their inherited copies| = o(ξ_lo^m).

*Proof.*
1. q ≥ 2p+1 ≥ q₀ for p ≥ q₀/2.
2. By W3, the orbit average is ≤ I_k + 3η for every β of conductor q or 7q.
3. By W2′ (bounded-J form, W-F7), |Ẑ_β^F| ≤ C_J·max(1, sup‖L‖)^{2k}e²·max(1, I_k + 3η)^{(Q−1)/2} ≤ C′·max(1, (1−δ/2)·target)^m, with C′ = e^{O(k)} independent of m.
4. Per level, Σ_β|W_β| < 4^{ω(d)}, with ω(d) ≤ 2 here. Inherited copies at levels d = ce carry the factor Σ_e n_e/e² ≤ σ(h)/h = O(log m).
5. The number of included levels is ≤ τ(h) = e^{O(m/log m)}.
6. |Z_ρ| ≤ C_ρμ^m. For (±2,8): μ·(1−δ/2)·1.28359 ≤ μ·1.28359 = 2.4586849 < ξ_lo = 2.4586893 (μ = upper end of |μ*|). For (±2,16): 1.6677·(1−δ/2)·1.4742 < ξ_lo.
7. Multiplying gives ≤ e^{o(m)}·((1−δ/2)ξ_lo)^m = o(ξ_lo^m). ∎

**Constants.**
- A_k ≤ (Σ_n‖M_n‖_HS)·(Σ_n‖M_n‖)^{2k−1} is finite but astronomically large.
- In the toy Galerkin basis sup‖L_τ‖ ≈ 1.8·10⁵, so for k ≈ 40, c_k ~ 10^{−800} and p₀ ~ 10^{800}. **Theorem W is asymptotic, not practical.** A better-adapted norm would shrink A_k. Not attempted.

**Evidence for (OP) [N]** (`code/n1_collision.py`; exact Fourier integration by a carry automaton).
- Collision pairs satisfy Σ_j(n_j − n′_j)λ^j = 0 ⇔ D(X) = (X² − 6X + 1)E(X). The carries are e_j = d_j + 6e_{j−1} − e_{j−2}, with states (e_{j−1}, e_j, parity) and |e| ≤ EMAX. The sectors a = 0, 4 and a = 2, 6 differ by (−1)^{E(1)}.
- Toy single-disc K = 40 (reproduces 1.2837 and μ*), (±2,8)-type b = 8: log I_k → 20.575 (constant), with ratio I_{k+1}/I_k = 1 − 1·10⁻¹⁰ for k ≥ 10.
- Stable under K = 24/40, NMAX 7/9 and EMAX 6/8. For b = 16: ratio 1 − 1·10⁻¹⁰.
- Hence I_k^{1/2k} = e^{20.575/2k}·1^{…}: < 1.2836 from k ≈ 41, and = 1.108 at k = 100.
- **Control [N]:** scaling ĝ by 1.1 (breaking unitarity) gives I_{k+1}/I_k = 1.2100000 = 1.1² exactly (`logs/n1_b8_K24_E6_N7_s1.1.log`). So the toy growth rate of I_k is exactly Σ|ĝ|²·(scale)².
- **Conjecture C1 [H/conjecture]** (the toy numerics above are its [N] evidence). For the true families, lim_k I_k^{1/k} = 1. Heuristic reason: the scalar word weights satisfy |a_w| = Π|ĝ(n_j)| with Σ|ĝ|² = 1 (unitarity), and the exact collisions add no growth.
- **Not proved.** Absolute-value bounds fail, because in the H²(D_ρ) norm the letter weights grow like e^{2π|coef||n|ρ}. A [CA] proof would certify the spectral radius of the true collision superoperator (lifted lattices ⊗ automaton ⊗ carries). Not attempted here.

## 3. Beyond Weil: Bourgain [P-cite], and the explicit literature

**Relation to the frozen-R′ boundary remark (TRACE-179).** The first three bullets are [P] (W1) or [P-cite]. Statements about what is or is not known in the literature are **[assessment]**. The frozen text says Korobov/Bourgain/BGK-type bounds "do not apply" because ord_h λ = m is minimal. This is correct for the composite modulus h as a whole, and here is the precise sense in which they still enter.
- **The relevant subgroup is small.** For a prime q | h_m, the orbit subgroup is H = ⟨λ⟩ ⊂ (O/q)*, of order r(q) = ord_q λ ∈ {p, 3p} (rank lemma; 7 contributes r = 3). This is order ~p inside a group of order ~q².
- **Weil range.** Weil (Theorem W1) is non-trivial only when |H| ≫ √q, i.e. q ≲ p².
- **Bourgain/BGK range.** The sum-product bounds of Bourgain (JAMS 2005) and BGK (JLMS 2006) need |H| ≥ q^ε, i.e. q ≤ p^{1/ε} = p^C. They give a saving q^{−δ(ε)} with δ effective, constants not computed (or astronomically small) (§9, N-F6).
- **Beyond p^C.** For q > p^C we have |H| < q^{1/C}, so no fixed power saving is available. Prime factors of h_{3p} reach size ≈ λ^{p} (q² ≤ |N(λ^r−1)|), where |H| = r is only a constant multiple of log q (r ≥ log_λ q). This is the short-orbit regime the frozen remark refers to. [assessment] No non-trivial bound for Σ_{h∈H}e(Tr(xh)/q) with |H| ≍ log q is known to me in general. [P] For slow β (by definition) no uniform bound of the needed strength can hold.
- **What K2 adds [assessment].** BGK helps exactly for prime levels q ≤ p^C and nowhere else. The remaining obstruction lives in p^C < q < L_m. It cannot be removed by any known exponential-sum technology over subgroups, which is why Theorem K2′ isolates it as an explicit equidistribution failure.

**Prime levels q ≤ p^C, any fixed C.**
- Write e = (q−1)/r, so r ≥ p ≥ q^{1/C}. Then Σ_{h∈H} ψ(Ah + B/h) = (1/e)Σ_{x∈F_q*} ψ(Ax^e + Bx^{q−1−e}).
- The exponent conditions of Bourgain's Mordell-sum theorem (J. Bourgain, *Mordell's exponential sum estimate revisited*, JAMS 18 (2005) 477–499) hold with ε < 1/C:
  - gcd(e, q−1) = e < q^{1−ε};
  - gcd(q−1−e, q−1) = e;
  - gcd(2e − (q−1), q−1) ≤ 2e.
- This gives |Σ_H| ≤ r·q^{−δ(C)}. For AB = 0 use Bourgain–Glibichuk–Konyagin (J. London Math. Soc. 73 (2006)).
- So W3 holds with error A_k·q^{−δ(C)} + T_k(q), and Theorem W extends to all prime conductors q ≤ p^C (and 7q), with p₀(C,k) **effective, constants not computed** (§9, N-F6).

**Explicit versions do not help for the binomial (non-isotropic) sums.** (Superseded by Line N1′, see §9, N-F10.)
- Cochrane–Pinner, *Explicit bounds on monomial and binomial exponential sums*, Thm 1.3: |Σ_x e_q(ax^k + bx^l)| ≤ (k−l, q−1) + 2.292·d^{13/46}q^{89/92}.
- With k = e, l = −e and d = e this gives |Σ_H| ≤ 2 + 2.292·r^{33/46}q^{1/4}. That is non-trivial only for q ≲ r^{1.13}, which is worse than Weil (q ≲ r²).
- For the linear (isotropic) sums, the explicit Heath-Brown–Konyagin bounds (Cochrane–Pinner Thm 1.2) reach q ≲ r³. They do not cover the binomial part.
- **The explicit range is therefore q ≤ c_kp².**

**Composite primitive conductors** d = q₁q₂⋯ (two primes ≥ 2p+1, so d ≥ 4p²):
- Weil over (Z/d)* gives 2^{ω}√d ≥ 4p > r, which is trivial.
- Bourgain's composite-modulus results (J. Anal. Math. 97 (2005); J. Anal. Math. 101 (2007)) might apply, but I have **not** checked their hypotheses for binomial sums over a diagonally embedded subgroup of order p [H].

## 4. Direction (b): counting levels [negative, P + N]

- **Trivial bound per level.** Σ_β|W_β||Ẑ_β| ≤ 4·max_β|Ẑ_β|. The maximum includes slow β of rate up to the untwisted μ₀. So the trivial level-q bound is ~|Z|·μ*^m, which already exceeds D7 ~ |Z|·1.2836^m for a *single* level.
- **Consequence.** The number of open-range levels (at most 2.64p/(C log p) primes > p^C divide h_{3p}) is irrelevant. Choosing p in a positive-density set does not help: no unconditional control of the factorisation of the primitive part of h_{3p} is known (comparable to primality of primitive divisors).
- **Factorisations [N]** (`code/n2_factor_h.py`, `logs/n2_factor_h.log`, p ≤ 43+). Apart from 7, the prime factors of h_{3p} mostly lie in p² < q ≤ √h, with log_p q between 2 and 15. Only 0–1 per m lie below p². The Weil range catches few levels in practice.
- **Toy traces at real levels [N]** (`code/n3_levels_toy.py`), per-step max_β rate, threshold 1.28359:

| p | q | log_p q | rate | β set |
|---|---|---|---|---|
| 13 | 79 | 1.7 | 1.211 | all |
| 13 | 313 | 2.24 | 1.089 | all |
| 13 | 599 (rank 13) | 2.49 | 1.381 | all |
| 13 | 4088137 | 5.94 | 1.356 | sampled, slow β |
| 37 | 223 | 1.5 | 1.071 | all |
| 37 | 6217 | 2.42 | 0.926 | sampled |
| 37 | 37223 | 2.91 | 1.134 | sampled |
| 37 | 8761009 | 4.43 | 1.292 | sampled, slow β (1,0) |

- Weil-range levels are benign. Open-range levels can have individual slow β above threshold at small m. These are maxima; the weighted sum carries weight 2/q² per β [H: weighted benign].

## 5. The open range p^C < q < L_m: attempted global arguments (negative)

**Periodic-point positivity [P lemma, negative outcome].**
- Since λ^r ≡ 1 (mod q), (1/q)O/O ⊂ Fix(T^r) for the cat map T.
- For F ≥ 0: Σ_{β∈O/q} F(β/q) ≤ Σ_{y∈Fix(T^r)} F(y). The right side is a periodic carry-automaton count.
- This loses the index |N(λ^r−1)|/q².
  - Rank 3p: non-trivial only if q > (λ^{1/2}/1.2836)^m = 1.88^m > √h, i.e. never.
  - Rank p: needs a sixth-moment pressure bound and only helps near q ~ λ^{p/2} [H].

**β-moments.**
- E_β of the block average equals I_k exactly once q² exceeds the Fourier support, but Markov with a fixed moment gives only a constant fraction of bad β.
- Moments of order s ~ log_λ q / k are controllable, but the bad β then need q > 1.72^m > √h.

**Scalar L² mod q with absolute values.** Fails: the ℓ¹ word mass is 2.35^m, against aliasing 1/q².


**Segment-Hölder route for the upper open range [P reduction, H input, blocked].**
1. Before the GM step, W2′ gives |Ẑ_β| ≤ C·Π_{i∈B}‖P_k(βλ^i)‖^{1/k}, with C = e^{O(k)}. Over the orbit this is ≈ Π_{i<r}‖P_k(βλ^i)‖^{Q/r}, up to the boundary loss of 2k positions (e^{O(k)}).
2. Split the orbit into n_s segments of length L = Q/2 and apply Hölder over the segments (λ-invariance of uniform β). This gives
   (1/q²)Σ_β|Ẑ_β| ≤ C·E_β Π_{i<L} f_k(βλ^i/q) = C·J_{L,k} := C·E_cat Π_{i<L} f_k(T^i y).
   - The equality with the cat-map expectation is exact: the segment's Fourier frequencies do not alias once L + k ≤ 2log_λ q − O(1), i.e. q ≳ λ^{m/(4k)}.
   - The weighted non-isotropic sum is then ≤ 2C·J_{L,k}. Isotropic β are similar, with log_λ q in place of 2log_λ q.
3. This would settle conductors q ≳ λ^{m/(4k)} if π_k := limsup (1/L)log J_{L,k} < 2k·log 1.28359.
   - For k = 1 the threshold λ^{m/4} is the √h boundary, so nothing is gained.
   - For k ≥ 2 the range λ^{m/(4k)} < q < √h is new (k = 2: q > 1.2465^m).
4. **Obstacle [N].** In the toy Galerkin basis the per-block constant e^{20} enters J_{L,k} once per segment step, so π_k ≥ 20, which forces k ≥ 41. But then π_k/2k ≈ Λ(2k)/2k approaches log(sup rate) ≈ 0.61 > 0.2497. The route needs an adapted norm in which ‖L_τ‖ is close to spectral size. Not available.
5. **Recorded as a reduction only.** The lower bound Λ(4)/4 ≥ log(μ₀⁴/λ)/4 = 0.169, from the slow region, is compatible with the condition, but nothing is verified.

**[assessment]** What the open range needs is a *β-weighted* large-deviation estimate for twisted products along λ-orbits mod q of length ~log q. Single-orbit equidistribution there is false for slow β, so the weights must be used. I see no available tool.

## 6. Theorem K2′ (strongest clean statement)

Assume (OP_k, δ). Let p₀ be as in Theorem W. For m = 3p ∈ S⁺ with p ≥ p₀, call a conductor c | h_m **open** if c ∉ {1, 7} ∪ {q, 7q : q ≤ c_kp²} and c < L_m. (For m ≲ 1.68·10⁹, "c < L_m" is vacuous.) Call β at an open conductor c **slow** if (1/r)Σ_{i<r} f_k^F(βλ^i/c) > ((1−δ/2)·target_F)^{2k} for some family F.

**Then:** if no open conductor of h_m has a slow β, the open part of O♮_m is o(ξ_lo^m). By REPORT_v2 Theorem K and Theorem W, W′_m/m → ∞ along such m. Hence:

> **Frozen R′ ⇒ for all large m ∈ S⁺ (an infinite set, Theorem K3), some open conductor c of h_m (with c < L_m) carries a slow λ-orbit.**

This is an explicit equidistribution failure. For given m, c, β it is checkable in principle by a certified operator computation (truncation with rigorous error), given the operator families. With Bourgain [P-cite], "q ≤ c_kp²" may be replaced by "q ≤ p^C" for any fixed C (effective, constants not computed; §9, N-F6). Labels: [P] given (OP_k, δ), Theorem J/J3 [CA] and Prop K2 [P + CA].

## 7. Files

- `code/w1_weil_check.py`, `logs/w1_weil_check.{log,json}` [N]: Weil instances.
- `code/n1_collision.py`, `logs/n1_*.{log,json}` [N]: exact toy I_k.
- `code/n2_factor_h.py`, `logs/n2_factor_h.{log,json}` [N]: factorisations of h_{3p}.
- `code/n3_levels_toy.py`, `logs/n3_*.{log,json}` [N]: toy traces at real levels.
- `REPORT_K2_v2.md` (this file) and `REPORT_K2.md` (v1, unchanged), plus `NOTES_K2.md`.
- `SHA256_K2.txt` is the manifest. Its own hash is in `SHA256_K2.sha256`, which is not covered by the manifest.
- Related:
  - `../code/k2_SZ.py`, `../code/k2_large_v2.py` (S_Z, crossover);
  - `../lean/K3Finite.lean` (decide-only Lean checks for K3: fraction tests, sieve enumeration) and `../lean/K3Gaps*.lean` (kernel-decide gap lemma, 447 ≤ b′ ≤ 2645), see REPORT_v2 and `../lean/gaps_summary.txt`.

## 8. Errata W-F7 (referee DELTA2, 31 Oct 2026; applied at integration)

Applied in the repository copy at integration, because the author was busy elsewhere. The author's file before this change is
`../pre_polish/K2/REPORT_K2_v2.md` (sha256 `c9f58c24…`, which matches `SHA256_K2.txt`). The only changes are in Lemma W2′, its *Effect*
paragraph, and Theorem W step 3.

| Item | Change |
|---|---|
| W-F7 (required) | The (±2,16) read-out I⊗J_B is **not** of finite rank (‖I⊗J_B‖₁ = ∞). The finite-rank branch C_J = ‖J‖₁ is replaced by the bounded-J argument already used for J = I: |Tr(JX)| ≤ ‖J‖·‖X‖₁, so C_J = ‖J‖·sup‖L‖₁/sup‖L‖, with ‖I⊗J_B‖ = ‖J_B‖ ≤ ½ (as in J3 `assemble16`). |
| Nit | (sup‖L‖)^{len} ≤ (sup‖L‖)^{2k} needs sup‖L‖ ≥ 1. The constant is now written max(1, sup‖L‖)^{2k}. |

The conclusions of W2′, Theorem W and Theorem K2′ are unchanged: the constant is still C′ = e^{O(k)}, independent of m. W2′ is [P] for every bounded read-out.

## 9. Errata N-F6, N-F10 (Line N referee, 31 Oct 2026; applied at integration of Lines M/N)

Applied in the repository copy at the Lines M/N integration (`evidence/executions/20261031/lineMN/INTEGRATION.md`), on the referee's
instruction in `computations/verification/lineN/referee/REPORT.md`. As with §8, `SHA256_K2.txt` records the author's file
(`../pre_polish/K2/REPORT_K2_v2.md`), not this copy.

| Item | Where | Change |
|---|---|---|
| N-F6 | §0 item 3, §3 (twice), §5 Bourgain/BGK range, §6 | "ineffective" → "effective, constants not computed". Bourgain's §5(1) gives δ_r > exp(−C₃r(ε^{−C₂} + log r)) with absolute constants not computed, so p₀(C,k) is effective (BGS-TRACE-281) |
| N-F10 | §0 item 3, §3 "Explicit versions do not help …" | Superseded by Line N1′ (REPORT_N_v2 §0; BGS-TRACE-279, 280): OSV's method with Voloch's point count, made explicit, beats Weil for the binomial sums when q ≤ c_N p^{7/3}, c_N = 10^{−113.80} (non-empty beyond Weil only for p ≥ 10^{264.5}) |
