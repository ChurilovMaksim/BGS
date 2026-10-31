# Line J3 (v2): towards an unconditional refutation of frozen R′ (TRACE-206)

v2 (31 Oct 2026) applies the referee fixes J3-F1…F7 (`/workspace/audit/lineJ/REPORT.md`, section J3). v1 (`REPORT_J3.md`) is kept unchanged. No number changes. Changelog in §7.

31 Oct 2026. Work directory `/workspace/bgs-lineJ/J3/`; notes in `NOTES_J3.md`. Nothing was pushed.

**Labels.**
- [P] proved (pen and paper, written here or cited);
- [P-check] exact or arb verification of a proved identity;
- [CA] computer-assisted certificate (arb plus rigorous BLAS bounds);
- [N] numerical;
- [H] heuristic.

**Cited inputs, used as [P]:**
- Line J v2 (`../REPORT_v2.md`): Theorem J and its table M0(j), K_j, θ.
- TRACE-197: the lifted trace identity.
- TRACE-212 (Prop I2′), for every odd d | h.
- TRACE-213: the decomposition of W′.
- TRACE-216: the symmetries.
- TRACE-198/199: μ*, H₀, and the d = 7 cut-off for m ≥ 13.
- TRACE-203 (Line G, G2): the finite-alphabet law with the C^{b²} automaton.
- TRACE-207: the full-alphabet lifted identity with a finite monomial state factor, termwise per word.

## 0. Summary

**Not achieved: a fully unconditional refutation.** What is proved is a refutation along m = 3p (p prime) conditional on one analytic hypothesis, H♮, plus a mild Diophantine proviso, H_arg (§5).

**New results:**
1. **(±2,16) members: certified negligible [CA] (§1).**
   - The 64-state automaton splits exactly into 8 invariant 2-dimensional monomial blocks per operator case [P-check].
   - 32 distinct factors were built in arb, and all **576** rest certificates pass.
   - The rates are R_untw ≤ 1.6677 and R_tw ≤ 1.2587. The cross rate R_untw·R_tw ≤ 2.0991 is 0.854·ξ_lo, and the square rate is R_tw² ≤ 1.5843.
   - Their d = 7 contribution, including all composite-level copies, is ≤ 1 % of the Theorem J lower bound for every m ≥ 243.
   - The read-out identity that links these certificates to Z_ρ is Lemma L16 (§1), proved in v2 (J3-F1).
2. **Inheritance theorem [P] + [P-check] (§2).** In general form (J3-F5): for gcd(c, e) = 1, ce | h and β = eβ′,
   W_{ce,eβ′} = (n_e/e²)·W_{c,β′}, with n_e ≥ 0, and the twisted coefficient Ẑ is the level-c one. Case c = 7: d = 7D′, β = D′β′.
   - So every composite-level copy of the d = 7 term is a **positive multiple** of it. It reinforces D7 and never cancels it.
   - The square parts of every Dev_d are ≥ 0.
3. **Prime levels have complete character sums [P] (§3).** For a prime q ∥ h:
   - |W_{q,β}| ≤ 2/q² for every non-isotropic β;
   - |W_{q,β}| = n_q/q² for the 2(q−1) isotropic β.
   - This suggests [H] that the "slow-twist" danger is suppressed on m = 3p (J3-F4). It is not a proof.
4. **The subsequence is forced [N, H] (§4).**
   - Levels of small rank r(q) have twisted rates above the d = 7 rate 1.2836. Examples: 41, 239, 199, 353, 599, and the large primitive factors of h_17, …, h_53 in the slow-twist test.
   - Each such level dominates D7 along the multiples of its rank.
   - Only m = 3p avoids every fixed rank ≥ 5. On m = 3p all primes q ≠ 7 dividing h_m have rank p or 3p [P].
5. **Strongest proved / computer-assisted statement (Theorem J3, §5).** On S⁺ ⊂ {3p} the bound is
   W′_m ≥ −4m + 0.99·K_j·1.0184224^m + φ⁻¹O♮_m.
   - S⁺ is infinite under H_arg (Vinogradov). arg ξ/2π is certified not to be a rational with denominator < 1339 [CA].
   - O♮_m collects the twisted parts of conductor ∉ {1, 7} (J3-F5): prime(-power) levels of rank p or 3p, their inherited copies, and mixed 7q parts.
   - Hence: **R′ ⇒ φ⁻¹O♮_m ≤ −0.99K_j·1.0184^m + O(m) on S⁺**. Frozen R′ can hold only if the primitive large-conductor parts cancel D7 exponentially.

## 1. (±2,16) members [P-check, N, CA]

**Exact blocks [P-check].** `code/blocks16_exact.py` → `logs/blocks16_exact.{log,json}`, ALL EXACT CHECKS PASSED for all 16 cases (m mod 48 × a = ±2).
- Each case has 8 pairs (f₁, f₂) with entries in {0} ∪ ζ₁₆^ℤ, pairwise orthogonal (exact Z[ζ₁₆] arithmetic, unequal supports 32/64 handled).
- Each A_n acts monomially: diagonal or swap with ζ₁₆ phases.
- u lies in the span, so the read-out decomposes as Z = Σ_B tr(A_{B,w}J_B), with ‖J_B‖_F = ½ exactly.
- Float check [N] (`code/wordtest16.py`, `logs/wordtest16.log`): 3200 random words give max |diff| 1.1e−14.
- Deduplication by (sign, block action) leaves 32 distinct factors (`logs/blocks16_reps.json`).

**Certificates [CA].** Pipeline: `code/pipe16.py` and `run_pipe16.sh`.
- Builder: `code/certG_build16.py` = the Line J sector builder with a 2-state finite factor and phases /16 (`code/gstates16_block.py`).
  - V: K0=3, ρ=1.2, K=40, β=2.5.
  - E: K0=3, ρ=0.8, K=30.
- Certifier: `code/rig_spec.py`, the audited Line H v4, sha f346e22c, in "rest" mode with p = 64 and R = 1.02·top + 0.02.
- 32 factors × {V, E} × {untwisted, 8 d = 7 classes} = 576 certificates in `logs/cert/*_rest.json`, all `certified: true`.
- The .npy matrices were deleted after certification for disk reasons. Their sha256 are recorded in each certificate, and a rebuild is deterministic (about 1 min per factor).

Float tops [N]: untwisted max 1.61541 (= the twrad16 value), twisted max 1.21440, edge operators ≤ 0.336.

**Assembly [CA]** (`code/assemble16.py` → `logs/assemble16.{log,json}`).
- Per certificate, Cauchy and the certified resolvent give ‖T^{m−1}‖ ≤ R^m·fullR/(1−F). So |tr((J⊗P₀)T^m)| ≤ ½‖T‖₁R^m·fullR/(1−F).
- Crude weights: |W_C| ≤ 36/49, and sq ≤ 6((6/7)Σ|Ẑ_C|)² per ρ.
- Hence E16(m) ≤ 0.01·(K_min/2)·ξ_lo^m for m ≥ 213. Including the composite inheritance factor A ≤ σ(h)/h ≤ 1 + (m/2)ln λ, this holds for m ≥ 243.
- Here K_min = 0.009985, the minimum of K_j over the 28 residues.
- The read-out identity used here is Lemma L16 below (v2, J3-F1). In v1 it was a labelled modelling assumption.

### Lemma L16 (b = 16 lift restricted to exact blocks) [P] (J3-F1)

**Setting.**
- ρ = (a, 16) with a = ±2 and m ≡ 3 (mod 6).
- A_n (n mod 16) are the 64×64 monomial matrices of the G2 automaton (TRACE-203), restricted to the set S of states reachable from δ₀. This set is closed under every A_n by construction (`reach`).
- 𝟙 = Σ_{s∈S} e_s.
- (f₁^B, f₂^B), B = 1…8, are the exact block bases of `blocks16_exact`.
- J_B = (P_Bδ₀)(P_B𝟙)^*, written as a **coordinate matrix** in the block basis (f₁^B, f₂^B). That basis is orthogonal but **not normalised** (supports 32 and 64), so the coordinate matrix is J_B = G_B⁻¹F_B^*δ₀α_B^*G_B, where F_B = [f₁^B f₂^B], G_B = F_B^*F_B is the (diagonal) Gram matrix and α_B are the coordinates of P_B𝟙. All norms of J_B below (‖J_B‖ ≤ ‖J_B‖_F = ½) are **coordinate** operator/Frobenius norms, which is the basis in which the builder writes the 2×2 factors A_{B,n} (integration polish L16-b).
- A_{B,n} is the 2×2 monomial action on block B.

**Statement.** With these definitions,

Z_ρ(m) = (1−λ^{−m}) Σ_B [ Tr((I⊗J_B)𝐕_B^m) − Tr((I⊗J_B)𝐄_B^m) ],

where 𝐕_B = Σ_n ĝ(n)e(Cn²/2)·V_n ⊗ A_{B,n} on the lifted vertex lattice, 𝐄_B likewise on the edge lattice, and C = −4ac₀/16.
- These are exactly the operators built by `certG_build16.py` with the finite factor `gstates16_block`.
- Twisted analogue: for the d = 7 class C the twist e(nτ_i(β)) has period 3 in i. Realise it by the cyclic 3-state lift and the read-out B = I⊗J_B⊗|e₀⟩⟨1_{i=0}|. Then Ẑ_{ρ,C} has the same form with the 6-state factors, as for b = 8 in Line I v2 (step 3).

**Proof.**
1. **Finite alphabet, |n| ≤ N (G2, TRACE-203 [P]).**
   - Z^{(N)}_ρ(m) = (1−λ^{−m}) Σ_{w∈[−N,N]^m} c_w·Tr_H(C_w)·⟨𝟙|A_w|δ₀⟩.
   - Here c_w is the product of the kick coefficients and the quadratic phases, C_w is the single-disc composite of the word, and A_w = A_{n_m}⋯A_{n_1}.
   - G2 is stated for every (a, b) with C^{b²} states. Restricting to S is exact, because A_wδ₀ ∈ span S and ⟨𝟙| is summed over S only.
2. **Lift, per word (TRACE-197 = Line F F1 [P]).**
   - For each word, Tr_H(C_w) = Tr(V_w) − Tr(E_w). Here V_w and E_w are the lifted vertex and edge composites. The chain decomposition is per word, and N_V − N_E = 1.
   - This is an identity of scalars, so multiplying by the scalar s_w = ⟨𝟙|A_w|δ₀⟩ preserves it: c_w s_w Tr_H(C_w) = c_w s_w [Tr V_w − Tr E_w]. This is the "termwise per word" argument of TRACE-207 and of Line I v2 (step 3), where it was used for the 49- and 16-state factors.
   - Hypotheses of TRACE-197 at the parameters used:
     - θ* = ½/ρ + 1/λ < 1 ⇔ ρ_V > 0.6036 (here 1.2), and ½/(λρ) + 1/λ < 1 ⇔ ρ_E > 0.1036 (here 0.8). Both are asserted in arb by the builder.
     - β = 2.5 > 0.
     - ĝ(n) = iⁿJ_n(1.8) is superexponentially decaying, so the weighted tail Σ|ĝ(n)|e^{α|n|} converges for every α, in particular α = 2π|C|ρ + β/λ with |C| = c₀/2. The builder bounds this tail (tailT ≤ 2e−200).
     - The α-condition is therefore satisfied for this |C| too. It is the same condition as for |C| = c₀ in Lines F/I, with a smaller α.
3. **Resummation.** Σ_w c_w s_w Tr V_w = Tr((I⊗|δ₀⟩⟨𝟙|)𝐕^m), where 𝐕 = Σ_n ĝ(n)e(Cn²/2)V_n⊗A_n.
   - The series converges absolutely for the full alphabet: |s_w| ≤ 1 (A_w maps δ₀ to a unimodular multiple of one basis state), and Σ_w|c_w|‖V_w‖₁ < ∞ under the TRACE-197 hypotheses. Explicitly (integration polish L16-a), with c_w = Π_k ĝ(n_k)e(Cn_k²/2) and ‖XY‖₁ ≤ ‖X‖₁‖Y‖ ≤ ‖X‖₁‖Y‖₁,
     Σ_{w∈ℤ^m} |c_w|·‖V_{n_m}⋯V_{n_1}‖₁ ≤ Σ_w Π_k |ĝ(n_k)|‖V_{n_k}‖₁ = (Σ_{n∈ℤ} |ĝ(n)|·‖V_n‖₁)^m < ∞,
     where finiteness of Σ_n|ĝ(n)|‖V_n‖₁ is step 1 (trace class) of the TRACE-197 proof at these parameters. The same bound holds with E_n.
   - Hence N → ∞ by dominated convergence, exactly as in the scalar case. ⊗ with a finite matrix preserves trace class, with ‖X⊗A‖₁ = ‖X‖₁‖A‖₁.
   - The same holds for E.
4. **Block restriction (exact).**
   - Each A_n is a unitary monomial matrix of finite order, so A_n^* = A_n^{−1} is a power of A_n.
   - Let U = span{f_i^B}. U is A_n-invariant (exact, `blocks16_exact`), hence so is U^⊥.
   - 𝟙 ∈ U (exact). So ⟨𝟙|A_w|δ₀⟩ = Σ_B⟨P_B𝟙|A_w|P_Bδ₀⟩ = Σ_B tr(A_{B,w}J_B), for every word.
   - Inserting this termwise in step 3 gives the statement.
5. **Twisted analogue.** Identical. The 3-cycle lift is again a finite monomial factor, and the block-0 read-out is rank one in the state space. ∎

**Checks.**
- [N] `wordtest16` checks step 4 for the finite part over 3200 random words, to 1.1e−14.
- The norm bound used in the assembly is |Tr((I⊗J_B)T^m)| ≤ ‖J_B‖·‖T‖₁·‖T^{m−1}‖, with ‖J_B‖ ≤ ‖J_B‖_F = ½.
- **Label.** With L16, X16 is [CA]. L16 is new written mathematics and should be checked by the referee.

## 2. Inheritance theorem [P]

**Theorem (general form, J3-F5).** Let c, e be coprime odd integers with ce | h and c > 1. Let d = ce, β′ ∈ O/c and β = eβ′ ∈ O/d. Then:
- (i) Ẑ^{(d)}_β = Ẑ^{(c)}_{β′};
- (ii) W_{d,β} = (n_e/e²)·W_{c,β′};

where n_e = #{j mod e : j unit mod e, and ν₀ + (2h/d)j ≢ 0 mod ℓ for every prime ℓ | e with v_ℓ(h) = v_ℓ(d)} ≥ 0. In particular n_e does not depend on c, β′ or the sign of ρ.

**Proof.** The proof below for c = 7 goes through verbatim with 7 replaced by c:
- CRT: x/d ≡ x·ē/c + x·c̄/e (mod 1);
- |G^{(e)}_u(0)|² = e² for units u, since x² − 2y² is non-degenerate mod odd e;
- the frozen exclusions are equivalent to j ∈ (Z/d)*, because 2h/d′ = (2h/d)(d/d′);
- mod c: (2h/d) ≡ (2h/c)·ē, so j′ = ēj reproduces the level-c member set and labels (t = jy′);
- the mod-e conditions are independent by CRT, which gives the factor n_e.

The P-check below compares class sums W_C, not individual β; the theorem itself is pointwise in β′. ∎

The case written out is c = 7:

**Setting.** d = 7D′ | h, 7 ∥ h (i.e. 21 ∤ m), gcd(7, D′) = 1, and β = D′β′ with β′ ∈ O/7.

**Twist.** τ_i(β) = Tr(D′β′λ^i)/(7D′) = Tr(β′λ^i)/7. So Ẑ^{(d)}_β = Ẑ^{(7)}_{β′} exactly, by the definition of the twisted lifted trace (TRACE-212).

**Gauss sums.** Let D̄′D′ ≡ 1 (mod 7) and 7̄·7 ≡ 1 (mod D′). Then x/d ≡ xD̄′/7 + x7̄/D′ (mod 1), and CRT on g ∈ O/d gives
G^{(d)}_t(D′β′) = G^{(7)}_{tD̄′}(β′)·G^{(D′)}_{t7̄}(0).
- For u a unit mod D′, |G^{(D′)}_u(0)|² = D′². The form x² − 2y² is non-degenerate mod odd D′, and gcd(t, D′) = 1 because y′ is a unit mod h (h² + 1 = 2y′²).
- Hence conj G^{(d)}_t(0)·G^{(d)}_t(D′β′) = D′²·conj G^{(7)}_{tD̄′}(0)·G^{(7)}_{tD̄′}(β′).

**Members.** Under the frozen rule M_d = {ν ∈ U : bν ≡ a (2h/d), bν ≢ a (2h/d′) for d′ | d, d′ < d}, the members are ν = ν₀ + (2h/d)j.
- The exclusions say exactly that j is a unit mod d.
- The label is t = jy′ (mod d), the Line I rule from TRACE-212 and `verify_coset`.
- Mod 7: (2h/d) ≡ (2h/7)D̄′, so with j′ = D̄′j the unit condition at 7 and the label tD̄′ = j′y′ are exactly the level-7 ones.
- The conditions mod D′ are independent by CRT: j a unit mod D′, and ν a unit at every prime ℓ | D′ with v_ℓ(h) = v_ℓ(d). Their count is n_{D′} ≥ 0. For a prime: n_q = q − 2 if q ∥ h, and q − 1 if q² | h.

**Conclusion.** W_{d,D′β′} = (n_{D′}D′²/(7⁴D′⁴))·Σ_{level-7 t}(…) = (n_{D′}/D′²)·W_{7,β′}. ∎
- The cross part of the inherited β at level d is therefore (n_{D′}/D′²)·cross₇, the same for ρ and −ρ, so the 1:3 cancellation persists.
- Summing over the included levels gives A_m·cross₇ with A_m = 1 + Σ n_{D′}/D′² ∈ [1, σ(h)/h].

**Checks.**
- [P-check] `code/inherit_proof_check.py`: exact integer Gauss-sum histograms evaluated in arb (200 bits) for (m, a, q) = (15, 2, 41), (15, −2, 31), (33, 2, 23). Max |diff| ≤ 9e−56. ALL CHECKS PASSED. It compares the class sums W_C (sufficient for the use in X7).
- [N] `code/inherit7q.py`: the ratio is a positive real (39/41, 30/31, 21/23) and identical for all 8 classes.
- **Square parts.** Dev_d = Σ_t(2Re(conj(ω_tZ/d)Δ_t) + |Δ_t|²) with |ω_t| = 1. So every square part is ≥ 0 [P] and can be dropped on the positive side.

## 3. Prime levels: complete sums [P]

**Claim.** For q prime with q ∥ h, completing the square gives tN(g) + B(β,g) = tN(g + β̃/t) − N(β)/t. Hence conj G_t(0)G_t(β) = q²·e(N(β)·t̄/q).

**Proof.**
- The labels t = jy′ run over all of F_q* except one value t_b (the one with ν ≡ 0 mod q).
- Hence W_{q,β} = q⁻²·(−1 − e(N(β)t̄_b/q)) if N(β) ≢ 0, and W_{q,β} = (q−2)/q² if N(β) ≡ 0.
- 2 is a square mod q because 2y′² ≡ 1, so there are 2(q−1) isotropic β.
- If q² | h there is no missing label: |W| = 1/q² and (q−1)/q². ∎

**Checks.** [N] `code/primelevel_W.py` at q = 41: max q²|W| = 1.994 (non-isotropic) and 39 (isotropic, 80 β). At q = 31: 1.000 and 30.

**Consequence [H].**
- Slow β (|β| ~ 1, τ_i ≈ 0 for i < log_λ q from both ends of the period) can have per-step twisted radius up to 1.83 [N]. Example: the primitive q ≈ 4.9e17 of h_47 (`code/slowtwist.py`, `logs/slowtwist.log`).
- Such β are non-isotropic, so they carry weight ≤ 2/q². On m = 3p with q | h_p, this costs λ^{−2ρ/3} per step, where ρ = log_λ q/p.
- The effective rate is then ≈ 1.83·0.56 ≈ 1.03 (and ≈ 1.0 at ρ = 0.25, 0.32), well below 1.2836.
- Isotropic β have weight 1/q each and are ≥ √q in size. Their slow fraction is halved, and their effective rate is ~1.0 [H].

## 4. Which m: small-rank levels dominate [N]

**Surveys** (`code/levels_survey{,2}.py`, logs). These use a toy single-disc Galerkin, K = 40, which reproduces the certified 1.2837 and μ* = 1.9155. They give per-step max twisted radii:

| rank r(q) | level q | max twisted radius |
|---|---|---|
| 5 | 41 | 1.510 |
| 7 | 239 | 1.566 |
| 9 | 199 | 1.470 |
| 11 | 353 | 1.396 |
| 13 | 599 | 1.381 |

- All of these exceed the d = 7 survivor rate 1.2836.
- The ranks 17…53 have large primitive factors whose slow-β radius exceeds 1.2836 as well (§3).
- At a *fixed* level the weight 2/q² is constant, so such a level dominates D7 along multiples of its rank.
- Long periods are generic: r_max ≤ 1.06 for periods ≥ 35, and the Lyapunov exponent is e^γ ≈ 0.81 (`lyap.py`).

**Rank (J3-F2).** For an odd prime q, define r(q) := ord_q(λ), λ = 3 + 2√2, the order in (Z[√2]/qZ[√2])*.

**Lemma [P].** For odd m: q | h_m ⇔ r(q) | m.
- *Proof.* Let ε = 1 + √2, so ε̄ = −ε⁻¹ and h_m = (ε^m + ε̄^m)/2. For odd m this is (ε^m − ε^{−m})/2.
- So q | h_m ⇔ ε^{2m} ≡ 1 ⇔ λ^m ≡ 1 (mod q) ⇔ r(q) | m. Note that ε is a unit and 2 is invertible mod q. ∎
- h is the companion (V-type) sequence, so this is not the standard U-type rule, which is why the lemma is stated directly.
- r(q) agrees with the "least odd m with q | h_m" used in `ranks.py` whenever q divides some h_m (then r(q) is odd).

**Corollary.** If r(q) = p is an odd prime, then q ≡ 1 (mod 2p).
- 2 is a square mod q (from 2y′² ≡ 1), so √2 ∈ F_q and λ ∈ F_q*. Hence p | q − 1, and q is odd.

**Consequence: m = 3p (p prime) is essentially forced [N, H for "forced"].**
- [P] By the Lemma, the primes dividing h_m are exactly those with r(q) | m.
- On m = 3p the only ranks are 3 (q = 7) and p or 3p. Every other prime q | h_m has r(q) ∈ {p, 3p}. Then q ≡ 1 (mod 2p), so q ≥ 2p + 1, and its twist period is r(q) ≥ p.
- 49 ∤ h, since ord₄₉(λ) = 21 and 21 ∤ m.

## 5. Theorem J3 (strongest proved / computer-assisted statement, modulo the referee check of Lemma L16)

**Definitions.**
- m = 3p, p prime, m ≥ 495. The residue j = m mod 168 lies in 3·(Z/56)*.
- B_j, ξ = μ*μ₂:₁ and K_j are as in Theorem J (v2 table; K_j ≥ K_min = 0.009985).
- S⁺ = {m = 3p : cos(arg(B_jξ^m)) ≥ 0.84431} (the window arc of Theorem J).
- O♮_m = Σ_{ρ∈P*} Σ_{d included} 2Re(conj Z_ρ Σ_{β∈B♮_d} Ẑ_β W_{d,β}). Here B♮_d is the set of β ≠ 0 mod d that are *not* inherited from level 7 (β ∉ (d/7)O when 7 ∥ d).
  - Equivalently, these are the β of conductor ∉ {1, 7} (J3-F5).
  - This includes β inherited from other conductors c ≠ 7 (e.g. β ∈ 7O at level 7q). By the general theorem of §2 these are positive multiples (n_e/e²) of level-c parts.

**Theorem J3.**
1. **[P] Identity:** W′_m = W′_A + φ⁻¹[A_m·X7_m + X16_m + Q_m + O♮_m], where:
   - X7 is the d = 7 cross part of ρ = (±2,8);
   - X16 is the d = 7 part of (±2,16), including its inherited copies;
   - Q_m ≥ 0 collects all square parts;
   - A_m ≥ 1.
2. **[CA, Theorem J]:** X7_m ≥ (K_j/2)ξ_lo^m on S⁺, using cos ≥ 0.8443, m ≥ M0(j) and the certified error budget.
3. **[CA, §1, via Lemma L16]:** |X16_m| ≤ 0.01·(K_min/2)ξ_lo^m for m ≥ 243.
4. **[P, Prop I8]:** W′_A ≥ −4m.

Hence, on S⁺ (using φ < λ^{m/2}/2):
**W′_m ≥ −4m + 0.99·K_j·(1.0184224)^m + φ⁻¹O♮_m.**

**Size of S⁺.**
- [P, Vinogradov] **Derivation (J3-F3).** Let α = 3·arg ξ/2π. It is irrational iff arg ξ/2π is.
  - Vinogradov's theorem (equidistribution of (pγ) mod 1; I. M. Vinogradov, *The Method of Trigonometrical Sums in the Theory of Numbers*, Ch. XI, recorded in Kuipers–Niederreiter, *Uniform Distribution of Sequences*, Ch. 1 §2, Notes; registered as EXT-VINOGRADOV-1937): for irrational γ, Σ_{p≤x} e(pγ) = o(π(x)). (Integration polish: v2 cited "Iwaniec–Kowalski Thm 13.6". IK Theorem 13.6 is Vinogradov's minor-arc estimate for Σ Λ(n)e(αn), which several citing papers confirm. On its own it does not give o(π(x)) for every irrational γ; the major arcs (Siegel–Walfisz) are also needed. So the citation now names the equidistribution theorem itself. IK Ch. 13 and Vaughan, *The Hardy–Littlewood Method*, Ch. 3 are cited only as chapter-level expositions.)
  - Fix p₀ mod 56 with gcd(p₀, 56) = 1. Then 1_{p≡p₀ (56)} = (1/56)Σ_{k mod 56} e(k(p−p₀)/56).
  - For every integer H ≠ 0, Σ_{p≤x, p≡p₀} e(pHα) = (1/56)Σ_k e(−kp₀/56) Σ_{p≤x} e(p(Hα + k/56)) = o(π(x)), because each Hα + k/56 is irrational. The prime number theorem for arithmetic progressions (Davenport, *Multiplicative Number Theory*, 2nd ed., §§20, 22; EXT-DAVENPORT-1980) gives #{p ≤ x : p ≡ p₀} ~ π(x)/24 (Dirichlet's theorem alone gives only infinitude).
  - By the Weyl criterion (Weyl 1916; Kuipers–Niederreiter Ch. 1, Theorem 2.1; EXT-WEYL-1916), (pα mod 1) is equidistributed over primes p ≡ p₀ (mod 56).
  - On this class j = 3p mod 168 is fixed, so B_j is fixed. The condition cos(arg B_j + 2π·pα) ≥ 0.84431 defines an arc of relative length arccos(0.84431)/π = 0.18001. So S⁺ has relative density 0.1800 among primes p ≡ p₀ (mod 56), p ≥ 167, and in particular it is infinite.
  - Also 0.84431 > c_win = 0.8443063, so S⁺ lies inside the window used by Theorem J.
- [CA] `code/rat_excl.py` (v2: outward rounding): arg ξ/2π lies in [0.88797591, 0.88797627] and is **not** a rational with denominator < 1339.
- The modulus-168 window lemma does not apply, because {3p} is not an arithmetic progression. The modulus 360360, which would fix m mod 5, 7, 9, 11, 13, is too coarse for the certified enclosure (`theta_big.py`: its θ-interval contains 0). The modulus 27720 works.

**Corollary (dichotomy).** Assume H_arg (arg ξ/2π ∉ ℚ). If frozen R′ holds, then along the infinite set S⁺ ⊂ {3p}:
φ⁻¹O♮_m ≤ −0.99K_j·1.0184^m + 4m + o(m).
So the primitive conductor-≠7 parts would have to cancel the d = 7 term exponentially.

**The remaining hypothesis.**

> **H♮:** For some δ > 0, O♮_m ≥ −(1−δ)·0.99·(K_j/2)·ξ_lo^m for infinitely many m ∈ S⁺. A sufficient form: |O♮_m| ≤ e^{o(m)}·r^m with r < ξ_lo = 2.4587.

Under H♮ and H_arg, **frozen R′ is false**: W′_m/m → +∞ along S⁺.

**What H♮ amounts to.**
- O♮_m runs over primitive conductors c | h_{3p}, c ≠ 7: prime powers of rank p or 3p, their products, and mixed 7·c parts.
- Using |W| ≤ 2/q² (§3), H♮ reduces to a uniform bound on weighted averages of twisted lifted traces Ẑ_β along cat-map orbits τ_i = Tr(βλ^i)/q, for all large q.
- Evidence [N/H]: the slow-twist survey gives effective ≈ 1.0, generic radii are ≤ 1.06, and e^γ ≈ 0.81. All of these are far below 1.2836 (μ*-normalised).
- Why it is not proved:
  - the set of conductors is unbounded (TRACE-219);
  - a Parseval approach gives Σ_β|Ẑ_β|² in terms of bulk moments of Z(ν) at that level, which is circular with R′_A;
  - a uniform certificate over infinitely many q needs an equidistribution theorem for twisted transfer-operator products along hyperbolic toral orbits. That is not available.
- H_arg is a side condition. A sharper μ* enclosure would only raise the excluded-denominator bound 1339; it can never prove irrationality (J3-F6).
- The only removal route offered is not done: for a rational a/b with b ≥ 1339, use Dirichlet for p mod 56b plus a Jacobsthal/Kanold-type gap bound g(n) ≤ 2^{ω(n)}, together with a finite check for small b, to place a residue in the 18 % arc.

## 6. Files (SHA256 in `SHA256_J3_v2.txt`; v1 manifest `SHA256_J3.txt`)

**Code (`code/`):**
- `blocks16_exact.py`, `wordtest16.py`, `gstates16_block.py`, `certG_build16.py`, `pipe16.py`, `run_pipe16.sh`, `rig_spec.py` (f346e22c), `assemble16.py`;
- `inherit7q.py`, `inherit_proof_check.py`, `primelevel_W.py`;
- `levels_survey.py`, `levels_survey2.py`, `slowtwist.py`, `lyap.py`, `ranks.py`;
- `theta_big.py` (v2: relative paths; refuses an empty run), `rat_excl.py` (v2: outward rounding);
- `make_reps16.py` (v2: generator of `logs/blocks16_reps.json`; regenerates it byte-identically) (J3-F7);
- exploratory: `sector16*.py`, `validate16.py` (abandoned: OOM-prone, about 6.5 GB; replaced by wordtest16), `run_build16.sh` (superseded), `ftop16.py`.

**Logs (`logs/`):** the corresponding `.log`/`.json` files, and `cert/` (576 certificates plus build logs).

**Line J v2** (referee fixes F1–F11): `../REPORT_v2.md`, `../STRATEGY_v2.md`, `../logs/SHA256_v2.txt`.

## 7. Changelog v1 → v2 (referee J3-F1…F7)

| fix | change |
|---|---|
| J3-F1 | Lemma L16 (G2 + TRACE-197 lift for (±2,16), termwise per word, restricted to the exact blocks; twisted analogue) written and proved. X16 is [CA] via L16. |
| J3-F2 | r(q) := ord_q(3+2√2); Lemma q \| h_m ⇔ r(q) \| m for odd m, with proof; corollary q ≡ 1 (mod 2p). |
| J3-F3 | Vinogradov ⇒ equidistribution over p ≡ p₀ (mod 56), written out with citations; density arccos(0.84431)/π = 0.1800 for p ≥ 167. |
| J3-F4 | "kills the slow-twist danger" → "suggests [H]"; §5 title qualified. |
| J3-F5 | General inheritance theorem (gcd(c,e) = 1) in §2; O♮ described as conductor ∉ {1, 7}; P-check noted to compare class sums. |
| J3-F6 | "sharper μ* enclosure" removed as a route to remove H_arg. |
| J3-F7 | theta_big.py relative paths plus empty-run guard (output byte-identical); rat_excl.py outward rounding (b_min 1339 unchanged); make_reps16.py added (byte-identical reps file). |
| H♮ | Stated for infinitely many m ∈ S⁺ (referee's optional remark). |

## 8. Integration polish (31 Oct 2026, after the referee's final DELTA3 verdict; integration branch line-J-rprime-d7)
This copy was edited at integration. The author's file before the edits is `pre_polish/REPORT_J3_v2.md`, with its sha256 in
`pre_polish/SHA256_pre_polish.txt`. No number or conclusion changed.

| item | change |
|---|---|
| L16-a | Step 3 now writes the domination bound Σ_w|c_w|‖V_w‖₁ ≤ (Σ_n|ĝ(n)|‖V_n‖₁)^m < ∞. |
| L16-b | J_B is the coordinate matrix G⁻¹F^*δ₀α^*G in the orthogonal, non-normalised block basis; ½ is its coordinate norm. |
| IK citation | "IK Thm 13.6" is replaced by Vinogradov's equidistribution theorem (Ch. XI; Kuipers–Niederreiter notes), keeping IK Ch. 13 and Vaughan Ch. 3 as chapter-level references. "Dirichlet" for the density is replaced by the PNT in arithmetic progressions (Davenport §§20, 22). The Weyl criterion is located (KN Thm 2.1). |
| J3-F8 | The sha256 of the block basis `logs/blocks16_exact.json` used by every (±2,16) build is recorded in `logs/SHA256_blocks16_basis.txt`. The check is `../integration_checks/lineJ_J3F8_basis_provenance.py`. The builders were not changed, so the recorded code hashes stay valid. |

