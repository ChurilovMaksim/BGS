# Line K report: towards an unconditional refutation of frozen R′ (TRACE-206)

Box `/workspace/bgs-lineK/`, 31 Oct 2026 (times UTC+5). Inputs: Line J v2 and J3 v2 (`/workspace/bgs-lineJ`). Nothing was pushed.
Labels: **[P]** proved by hand; **[P-check]** exact/high-precision verification of a finite identity; **[CA]** computer-assisted, rigorous (arb or exact integer); **[N]** floating-point numerics; **[H]** heuristic.

## 0. Summary

1. **H_arg is removed [P + CA].** S⁺ ⊂ {m = 3p} is infinite **unconditionally** (§1). If arg ξ/2π is irrational, Vinogradov applies (J3 v2). If it is rational, a/b, then b ≥ 1339 (J3 `rat_excl`), and a finite exact gap check plus a sieve bound plus Dirichlet give infinitely many primes p with 3p ∈ S⁺.
   **Consequence (now unconditional dichotomy, [CA] modulo the referee check of Lemma L16 as in J3):** if frozen R′ holds, then φ⁻¹O♮_m ≤ −0.99K_j·1.0184224^m + 4m + o(m) on an infinite set S⁺ of m = 3p.
2. **Structural theorem for prime levels [P, algebra P-checked] (§2).** For q ∥ h, q ≠ 7, the conductor-q cross part is a *light-cone defect*:
   Σ_{β≠0} Ẑ_β W_{q,β} = D_iso(q) − E_b(q)/q.
   Here D_iso is the excess word mass whose λ-adic position x_w = Σ n_i λ^i lies in 𝔮 ∪ 𝔮̄ (the primes above q), relative to the uniform share (2q−1)/q². E_b is a single bad-dilation deviation. So H♮ at prime levels is exactly an equidistribution statement: *weighted words do not concentrate on the prime ideals above q*. Since λ has order r(q) ∈ {p, 3p} mod 𝔮, this is the vanishing of the folded polynomial Σ_r N_r ℓ^r at a primitive p-th root ℓ mod 𝔮.
3. **Large levels are negligible [P, given the Z-bound] (§3), but only asymptotically.** Every level d ≥ L_m = (μ*²/ξ)^{m(1+η_m)} with η_m → 0 (~1/log m) drops out by positivity and Rankin's trick over primes q ≥ 2p+1. Honest caveat: in the worst case for the factorisation of h_m, L_m < √h_m only for m ≳ 1.7·10⁹ (η = 0.59 at m = 501). That is enough for the refutation, which only needs infinitely many m.
4. **BGK range, numerical evidence [N] (§4).** For the toy Galerkin, block operator-norm rates along cat-map orbits are R_k^cat = 6.34, 2.26, 1.337, **1.131**, 1.037, 0.974 for k = 6, 12, 24, 36, 48, 64 (standard errors ≤ 0.004 in log). They drop below the d = 7 survivor 1.2836 from k ≈ 30. So *where orbits of the order-p subgroup equidistribute* (q ≤ p^C, Bourgain–Glibichuk–Konyagin range) the order-free product bound would beat D7 with room to spare. Making this rigorous needs (i) a Bourgain-type equidistribution input and (ii) certified block norms for the true operators. Neither is done.
5. **Not achieved:** an unconditional proof of H♮. **Single remaining hypothesis** (Theorem K, §5): **H♮_mid**, which covers only included levels d < L_m of conductor ∉ {1, 7}. With §2 and §4, the genuinely open part is the intermediate range p^C < q < L_m, where the orbit of λ (order p) in O/q may fail to equidistribute (sporadic relations; the slow-twist mechanism of J3 §3).

## 1. Removal of H_arg [P + CA]

**Lemma K3.** Let A = arccos(0.84431)/π (arb lower bound 0.18001064843). For every b′ ≥ 447 with b′ ∉ {504, 560, 616, 840}, and every unit class r mod g′ = gcd(56, b′), the set V(b′,r) = {v mod b′ : gcd(v,b′) = 1, v ≡ r (mod g′)} has maximal cyclic gap < A·b′.

*Proof.*
- (a) **Exact enumeration for 447 ≤ b′ ≤ 6000 [CA, exact integers]** (`code/k3_harg.py`). Only b′ ∈ {504, 560, 616, 840} fail; the worst ratio is 2/9 at 504.
- (b) **Sieve for all b′ [P].** Let n′ be the part of b′ coprime to g′, with k = ω(n′). V(b′,r) = {r + g′t}. The primes of g′ (2 and 7) are automatically avoided because r is a unit mod g′, and admissibility is periodic in t mod b′/g′.
  - By inclusion–exclusion over squarefree e | rad n′, any X consecutive t contain at least X·φ(n′)/n′ − 2^k admissible t.
  - So the t-gap is ≤ X_t = ⌊2^k n′/φ(n′)⌋ + 1, and the v-gap is ≤ g′X_t.
  - Let F = Π_{ℓ|n′} 2ℓ/(ℓ−1) and R = rad n′. If g′X_t ≥ A·b′ ≥ A·g′R, then F + 1 ≥ A·R, i.e. Π_{ℓ|n′} 2/(ℓ−1) ≥ A − 1/R.
  - A prime ℓ ≥ 23 makes this impossible, since 2/22 < A − 1/23. Enumerating the subsets of {3, 5, 11, 13, 17, 19} leaves {3}, {5}, {11}, {13}, {17}, {3,5}, {3,11}, {3,13} (and R = 1). For each, b′ ≤ g′(F+1)/A ≤ 2644.3.
  - So every failure has b′ ≤ 2645, which is inside the exact range. ∎

**Theorem K3 [P + CA].** S⁺ = {m = 3p : cos(arg B_j + m·arg ξ) ≥ 0.84431} is infinite. More precisely, for each p₀ ∈ (Z/56)* it contains infinitely many m = 3p with p ≡ p₀ (mod 56).

*Proof.*
- **Irrational case:** Vinogradov (J3 v2 §5, density 0.18001).
- **Rational case:** arg ξ/2π = a/b in lowest terms.
  - J3 `rat_excl` [CA] gives b ≥ 1339.
  - Put b′ = b/gcd(3,b) ≥ 447 and a′ = 3a/gcd(3,b), so gcd(a′,b′) = 1 and m·arg ξ/2π ≡ a′p/b′ (mod 1).
  - By CRT and Dirichlet, primes p ≡ p₀ (mod 56) hit every v ∈ V(b′, p₀ mod g′) infinitely often.
  - Multiplication by the unit a′ maps V(b′, r) onto V(b′, a′r), preserving cyclic gaps. So the phases {a′p/b′} form a set with gaps < A, which meets the arc {cos(arg B_j + 2πx) ≥ 0.84431} of length A.
  - The four exceptional b′ are excluded exactly: for b ∈ {b′ (if 3 ∤ b′), 3b′}, no fraction with denominator b lies in the outward-rounded enclosure [0.88797591, 0.88797627] of arg ξ/2π (exact `Fraction` test, `logs/k3_harg.log`).
  - Finally, B_j is constant on the class p₀ (j = 3p mod 168), and m ≥ M0(j) holds for p large. ∎

**Corollary K3 (unconditional dichotomy) [CA, L16 caveat as in J3].** Frozen R′ ⇒ φ⁻¹O♮_m ≤ −0.99K_j·1.0184224^m + 4m + o(m) for infinitely many m = 3p. H♮ alone now refutes frozen R′.

## 2. Structural theorem: the light-cone formula [P; algebra P-checked]

**Setting.**
- q ≠ 7 is prime with q ∥ h_m. 2 is a square mod q, so q splits: qO = 𝔮𝔮̄.
- For a word w = (n_0, …, n_{m−1}), let x_w = Σ_i n_i λ^i ∈ O/q.
- By the definition of the twist (τ_i(β) = Tr(βλ^i)/q), Σ n_i τ_i = Tr(βx_w)/q. Grouping words by x_w (absolutely convergent, as in Lemma L16 steps 1–3) gives Ẑ_β = Σ_{x∈O/q} A(x)e(Tr(βx)/q), where A(x) is the complex mass of the words at position x and A_tot = Ẑ_0.

**Theorem K1.** Σ_{β≠0} Ẑ_β W_{q,β} = D_iso − E_b/q, where:
- D_iso = A(𝔮 ∪ 𝔮̄) − ((2q−1)/q²)·A_tot;
- E_b = Σ_x A(x)e(−N(x)t_b/q) − A_tot/q;
- t_b is the missing label.

Hence the level-q part of O♮ is Σ_ρ 2Re(conj Z_ρ·(D_iso − E_b/q)).

*Proof.*
1. By J3 §3, W_{q,β} = q⁻²Σ_{t∈F_q*, t≠t_b} e(N(β)t̄/q).
2. Completing the square in β = b₁ + b₂√2 gives Tr(βx) + uN(β) = uN(β + x̄-shift) − N(x)/u. So Σ_β e((Tr(βx) + uN(β))/q) = g·e(−N(x)ū/q), with g = G(u)G(−2u) = (−2/q)G(1)² = (2/q)·q = q.
3. Sum over t ≠ t_b, using Σ_{t∈F_q*} e(cN(x)t/q) = q·1_{N(x)=0} − 1 and #{N(x) = 0} = 2q − 1.
4. Subtract the β = 0 term, (q−2)A_tot. ∎

**Check.** [P-check] `code/k1_cone_check.py`: random complex A, q = 7, 17, 23, 31 and two values of t_b; |lhs − rhs| ≤ 2·10⁻³⁹ at 40 digits. "K1 IDENTITY VERIFIED".

**Folding.**
- Let ℓ = λ mod 𝔮, so ℓ has order r(q) ∈ {p, 3p}.
- x_w ∈ 𝔮 ⇔ P_w(ℓ) = 0, where P_w(X) = Σ_{s<r} N_s X^s and N_s = Σ_{i≡s (mod r)} n_i.
- Trivial zeros (all N_s equal) occur for every q. They are exactly the words with x_w ∈ ∩_{q of rank r} 𝔮, and their excess is common to all levels.
- Sporadic zeros (q | Norm P_w) are unavoidable for q ≲ C^p. This is the arithmetic form of the slow-twist mechanism.

**Meaning.** H♮ at prime levels ⇔ the λ-adic positions of weighted words are equidistributed modulo the primes above q, to precision |Z|⁻¹ξ^m relative to the trivial share.

## 3. Large levels by positivity [P, given the Z-bound]

**Input.** For every ρ ∈ P*, |Z_ρ(m)| ≤ C_ρ μ^m with μ = |μ*|_up = 1.9154753. For (±2,8) this is Line F [CA]: |Z| ≤ |c_m|(½μ*^m + H₀). For (±2,16) the rate is smaller. If P* contains other primaries, their bounds are an input. Let S_Z = Σ C_ρ².

**Proposition K2.**
- For any included level d, Dev_d(ρ) = Σ_{ν∈M_d}(|Z_ν|² − |Z_ρ|²/d²) ≥ −n_d|Z_ρ|²/d² ≥ −|Z_ρ|²/d.
- On m = 3p the primes of h are 7 (49 ∤ h) and primes q ≥ 2p+1 (rank lemma). There are at most w = ⌊log h/log(2p+1)⌋ of the latter, counted with multiplicity.
- Rankin: for 0 < s < 1, Σ_{d|h, d≥L} 1/d ≤ L^{s−1}(1−7^{−s})^{−1}(1−(2p+1)^{−s})^{−w}.
- Hence Σ_{ρ, d≥L} Dev_d ≥ −0.01·(K_min/2)ξ_lo^m as soon as log L ≥ min_s [E(s) − log(0.01K_min ξ^m/(2S_Z μ^{2m}))]/(1−s). This gives L_m = (μ²/ξ)^{m(1+η_m)}, with η_m = O(1/log m) as m → ∞ (μ²/ξ = 1.49228).

**Numbers [CA, arb]** (`code/k2_large.py`, `logs/k2_large.log`). With S_Z = 10⁸ or 10¹⁴ (insensitive), l = L^{1/m} is:

| m | 501 | 3027 | 3·10⁵ | 3·10⁷ |
|---|---|---|---|---|
| l | 1.889 | 1.704 | 1.603 | 1.570 |

against √h rate 1.5538. The first grid point with l < √h is m ≈ 1.73·10⁹. **So K2 is asymptotic only:** for every practically computable m, the worst-case large-level range is empty. A sharper input (actual factorisations of h_m, which have few large primes) would lower this, but it is not proved for all m.

## 4. BGK range: order-free norm route [N, H]

- Along a prime level, a k-block of twists is a function of y = βλ^i ∈ O/q ≅ T² (the cat map y ↦ λy).
- If the orbit of β under ⟨λ^k⟩ (order ~p/k) equidistributes in O/q, then ‖Π_i L_{τ_i}‖ ≤ exp(p(log R_k^cat + o(1))), where R_k^cat = exp(E_y log‖L_{τ_{k−1}(y)}⋯L_{τ_0(y)}‖/k).
- The number of β per level and of levels contributes only e^{o(m)} (the weights 2/q² and 1/q against q² and 2(q−1) β).

**Results (toy Galerkin, the same family that reproduces 1.2837 and μ*).**
- `code/k4_catrate.py` (y exact at q = 2¹²⁷−1): R_k^cat = 6.338, 2.255, 1.337, 1.131, 1.037, 0.974 for k = 6, 12, 24, 36, 48, 64. The SE of log R is ≤ 0.005.
- iid τ (`code/k4_normrate.py`): almost identical, 6.37, 2.25 at k = 6, 12. The single-step norm is useless (sup ≈ 1.8·10⁵, a non-normal basis). The limit is the Lyapunov exponent e^γ ≈ 0.81.
- **Conclusion [N]:** the order-free product bound beats the d = 7 survivor 1.2836 from k ≈ 30, with margin (1.131 at k = 36).
- **Not rigorous.** It needs (i) equidistribution of {(ℓ^i b₁, ℓ^{−i} b₂)} ⊂ F_q² for an order-p subgroup with p ≥ q^ε. That is Bourgain's sparse/Mordell-type exponential sums over subgroups (Bourgain–Glibichuk–Konyagin; Bourgain 2005); the applicability to this binomial (exponents 1 and p−1 on H) still has to be checked [H]. (ii) It also needs certified k ≈ 36 block norms for the true two-disc operators, with an upper-semicontinuous majorant for log‖·‖.

## 5. Theorem K (strongest statement)

Let m = 3p, j = m mod 168, and S⁺ as in J3. Then:
1. **[P + CA]** S⁺ is infinite (Theorem K3; no H_arg).
2. **[CA, L16 caveat]** On S⁺: W′_m ≥ −4m + 0.99K_j·1.0184^m + φ⁻¹(O♮_m^{<L} − 0.01(K_min/2)ξ_lo^m), for m ≥ m_K2. Here O♮^{<L} collects the conductor-∉{1,7} cross parts at included levels d < L_m (Prop. K2; levels d ≥ L_m are absorbed whole, and the inherited D7 copies at d < L_m still have positive coefficient).
3. **[P]** At each prime level q ∥ h in O♮^{<L}, the contribution is Σ_ρ 2Re(conj Z_ρ(D_iso(q) − E_b(q)/q)) (Theorem K1).

**Remaining single hypothesis, H♮_mid.** For some δ > 0 and infinitely many m ∈ S⁺: O♮_m^{<L} ≥ −(1−δ)·0.98·(K_j/2)ξ_lo^m.

Under H♮_mid, frozen R′ is false (W′_m/m → +∞ along S⁺). By (3) and §4, H♮_mid is [N]-supported in the range q ≤ p^C. The genuinely open part is p^C < q < L_m and the composite levels in that range.

**Evaluation of the owner's ideas.**
1. **Averaging over p with the d = 7 phase:** fails standalone. W′_A and Q are controlled from one side only, so averaging cannot isolate O♮. Under R′ it only re-derives Corollary K3.
2. **Unconditional per-level bound:** realised as K1 + K2. The Parseval/Cauchy–Schwarz form of the per-level bound gives |Σ_β Ẑ W| ≤ (2/q²)·q·‖Ẑ‖₂ ~ ‖A‖₂/… which is no better than the trivial mass bound, so it was not pursued.
3. **Galois/Chebotarev:** the Galois action ℓ ↦ ℓ^a permutes the 𝔮 of rank p. Averaging D_iso over conjugates only isolates the trivial zeros, so it does not control a single q. Not pushed further.

## 6. Files

- `code/k3_harg.py`, `logs/k3_harg.{log,json}`: Lemma K3, "K3 CLAIM PROVED (exact + sieve)".
- `code/k1_cone_check.py`, `logs/k1_cone_check.{log,json}`.
- `code/k2_large.py`, `logs/k2_large.{log,json}`.
- `code/k4_normrate.py`, `code/k4_catrate.py`, `logs/k4_*.{log,json}`.
- `NOTES.md`, `SHA256.txt`.
- Python: `/workspace/bgs-derand/phase3/venv/bin/python` (python-flint, mpmath, numpy). K3 reads `../bgs-lineJ/J3/logs/rat_excl.json`.
