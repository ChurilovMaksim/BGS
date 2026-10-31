# Line N report: sum-product / subgroup exponential sums in place of Weil (Theorem W), and what stays open

31 Oct 2026 (Asia/Yekaterinburg, UTC+5). Work dir /workspace/bgs-lineN. Nothing was pushed.

**v2 (integration copy).** The integrator wrote this version on 31 Oct 2026 (UTC+5). It applies the referee fixes N-F1 … N-F10
(`referee/REPORT.md`, verdict READY-after-fixes) and five integration notes I-1 … I-5 (I-1 amended and I-5 added after the owner audit of PR #65). The author's text is `REPORT_N.md`, kept
unchanged (sha256 b740bc392982b9dc81caa200b2599f01543497364301779c3be13bdb4c22b883, listed in `SHA256_N.txt`). Every change is listed in §12. The author was not consulted.
Labels: [P] proved here; [P-cite] proved from a cited theorem whose statement I read (hypotheses checked, proof not re-verified);
[CA] computer-assisted; [N] numerics; [H] heuristic; [assessment] opinion. "Standing inputs" = Line F/J/J3/L16 + the Line L
certificate, exactly as in REPORT_L_v2.

## 0. Verdict

**No refutation of frozen R′.** Line N proves two new results: one explicit positive result and one structural negative result.
The negative one shows that no range extension of Theorem W, however strong, can close the argument in its present
(K2′) form.

| # | Statement | Label |
|---|---|---|
| N0 | Reduction: the only arithmetic input of Theorem W is a uniform bound for the matrix-power sums S(x) = (1/τ)Σ_{h∈H}e((Ah+B/h)/q) (= OSV sums Σ ψ(aSⁱb) for the cat matrix mod q). No kick phases survive. The per-level budget is a constant ε_F, independent of m: ε = 10^{−12.51} (binding family (±2,8)V, Line-L convention) | [P] |
| N1 | **Explicit beyond-Weil range (Theorem W⁺).** Theorem W holds (m ≥ m₁, effective, not computed) for all prime conductors q ≠ 7, and for 7q, with q ≤ max(c_W p², c_N p^{7/3}), where c_N = 10^{−113.80}. Proof: an elementary moment inequality plus explicit additive energies J₂ ≤ 2τ² − τ, J₃ ≤ 17.31τ^{11/3} (Voloch point count). It beats Weil only for p ≥ 10^{264.5} | [P + P-cite] |
| N1′ | This corrects K2 §3, which said "explicit literature does not beat Weil for binomial sums". Ostafe–Shparlinski–Voloch (IMRN 2023) do beat it, with exponent 7/3 instead of 2; the constants are made explicit here. This supersedes REPORT_K2_v2.md:134–137 ("explicit versions do not help for the binomial sums") (N-F10) | [P-cite] |
| N2 | Qualitative: Bourgain (JAMS 2005) + BGK give prime conductors q ≤ p^C for every fixed C, with p₀(C) **effective, constants not computed** (N-F6) | [P-cite] |
| N3 | **Scarred conductors always carry slow β** (the extension of L2 Prop S, TRACE-258, from prime levels to composite c, chiefly h_p, with an explicit θ; N-F1). Every conductor c with log_λ c ≥ θ_F·r/2 + t_F (r = ord_c λ, F = (±2,8)V, θ_F = 5.39·10⁻⁶) has the slow β = 1. This includes c = h_p for every p ≥ p₀ (effective, not computed; N-F3), and every prime of K_p above λ^{8.1·10⁻⁶p+O(1)}. **So the conclusion of K2′ holds without assuming frozen R′, and "exclude slow orbits in the open range" (REPORT_L_v2 §6) is false as a target.** | [P] on the per-family [CA] spectral bound of TRACE-198 (N-F2) |
| N4 | At c = h_p, the twisted sums are periodic-orbit sums of the cat map: the conductor-h_p points are a subgroup of index 4 in Fix(T^p) (N-F8; the author's 32 was wrong). So the inherited-level problem is a cocycle pressure estimate, not an exponential-sum problem. Heuristically it has a large margin (1.064^m against 1.284^m) | [P] identification, [H] margin |
| N5 | Factorisations: p ≤ 173 (complete apart from 5 cofactors), and the p³-smooth part for p ≤ 2000. h_{3p}/7 is p³-smooth only for p = 5. For p > 1000 the mean log-share of primes ≤ p³ is 0.8% | [N] |

**Answers to the three questions.**
1. Yes. The reductions OP / lattice lifts / T_k lead exactly to *linear additive-character sums over the cyclic group ⟨λ⟩ in the
   ring O/c*: binomial (Kloosterman-type) sums over H ≤ F_q* for split q, which is every q | h_m, q ≠ 7. The chirp, the sector phases and
   the Jacobi–Anger coefficients enter only through c_γ (absolute values). No polynomial phase of degree ≥ 2 survives.
2. The demand is a **fixed constant per level**, independent of m and of the number of levels. Any power saving q^{−δ} suffices
   once q^δ ≥ 1/ε_F, i.e. p ≥ 10^{12.5/(2δ)}. The D7 rate 1.0184^m and the level count enter only through the exponential margin
   (1−δ_F/2)^m of Theorem W, for m ≥ m₁ (effective, not computed; N-F7).
3. No, and this is now **proved** (N3). Extending the covered range shrinks the *prime* open range to (c_N p^{7/3}, L_m)
   explicitly, or to (p^C, L_m) non-explicitly. But for p ≥ p₀ (effective, not computed) K2′'s open set contains conductors that provably carry slow orbits, e.g. h_p.
   So K2′/U-type conclusions cannot become unconditional for *any* m along this route. The subsequence idea fails twice:
   - h_p is an open conductor regardless of how its prime factors are distributed;
   - numerically, all prime factors are ≤ p^C essentially never (N5).

## 1. N0: the reduction [P]

From K2_v2 §2 (W1/W3) and REPORT_L_v2 §3 (both verified line by line):
- f_k^F(y) = ‖P_k^F(y)‖²_HS = Σ_{γ∈O} c_γ e(Tr γy), with Σ_{γ≠0}|c_γ| ≤ A_k.
- The orbit average at conductor q is (1/r)Σ_{i<r} f_k(βλⁱ/q) = I_k + Σ_{γ≠0} c_γ·S(γβ), where
  S(x) = (1/r)Σ_{i<r} e(Tr(xλⁱ)/q) = (1/r)Σ_{h∈H} e((σ(x)h + σ̄(x)h⁻¹)/q), with H = ⟨σ(λ)⟩ ≤ F_q* of order r ∈ {p, 3p}.
- Every q | h_{3p}, q ≠ 7, is ≡ ±1 (mod 8), hence split; and q ≡ 1 (mod 2p) [P: r | q−1, r odd]. [N] check:
  0 failures over 192 prime factors, p ≤ 173 (logs/n4_summary.log).
- The chirp e(C₀n²/2), the sector phases e(an/8) and the kick Fourier coefficients ĝ(n) = iⁿJ_n(1.8) are absorbed into c_γ. OP_abs
  bounds |c_γ| without using them. **No Gauss-type (quadratic) phase appears in the sum that has to be estimated.**
- S(x) is exactly the OSV sum S_{2,q}(a,b;A) = Σ_x ψ(aAˣb) for A = diag(ℓ, ℓ⁻¹) ~ S mod q, a = (σx, σ̄x), b = (1,1)ᵗ.
  - Non-isotropic x (σx·σ̄x ≠ 0) corresponds to OSV's independence hypothesis on (a, aA).
  - Isotropic x gives the linear Gauss-period sum Σ_{h∈H} e(Ah/q).
- **Budget.** Theorem W needs I_k + A_k·sup_{x nondeg}|S(x)| + T_k(q) ≤ I_k + 3η with T_k ≤ η for q ≥ q₀, for m ≥ m₁ (effective, not computed; N-F7). Line L used the stricter
  A_k·sup|S| ≤ η/3, i.e. ε_F := η_F/(3A_k^F). The same convention is used throughout here, so that the Weil range reproduces
  c_W = 10^{−25.615} exactly (logs/n2_constants.log). ε_F = 10^{−12.51} (8V), 10^{−10.17} (8E), 10^{−10.96} (16V), 10^{−10.12} (16E).
  Using the full budget 2η/A_k would gain about 7 orders in c_N; this is not used.
- The 7q conductors split into 3 cosets of a subgroup H′ of order p. A coset sum Σ_{h∈gH′}ψ(Ah+B/h) is the H′ sum with
  (Ag, B/g), so every bound below applies with τ = p.

## 2. Literature: exact statements checked (web, 31 Oct 2026)

| Source | Exact statement used | Applies? |
|---|---|---|
| Weil (K2 W1) | \|Σ_H ψ(Ah+B/h)\| ≤ 2√q | yes, range q ≤ c_W p² |
| Bourgain–Konyagin, CRAS 337 (2003) | \|Σ_{x∈G}e_p(xξ)\| ≲ \|G\|p^{−γ}, γ = exp(−c₁/δ^{c₂}), for \|G\| ≳ p^δ; c₁, c₂ unspecified absolute constants | linear (isotropic) only; not numerically explicit |
| BGK, JLMS 73 (2006) 380–398 | ∀ε ∃δ(ε): \|G\| ≥ p^ε ⇒ max_{a≠0}\|Σ_{x∈G}e_p(ax)\| ≤ \|G\|p^{−δ} | linear only; δ not explicit |
| **Bourgain, JAMS 18 (2005) 477–499, Thm 1 / Cor (1.21)** | ord(θ_i) > p^ε and ord(θ_iθ_j⁻¹) > p^ε ⇒ max_{a_i∈F_p*}\|Σ_{s=1}^{p−1}e_p(Σ a_iθ_iˢ)\| < p^{1−δ(ε)}. **Both a_i must be nonzero** | yes: θ = ℓ, ℓ⁻¹ with orders r and r (r odd) ⇒ non-isotropic sums, for q ≤ p^C; δ not explicit |
| Cochrane–Pinner, QJM 62 (2011), Thm 1.1 | for a subgroup A: \|Σ_{x∈A}e_p(ax)\| ≤ λ\|A\|^{5/8}p^{1/8} for 3p^{1/3} < \|A\| ≤ p^{1/2}, ≤ λ\|A\|^{3/8}p^{1/4} for p^{1/2} < \|A\| ≤ p^{2/3}/3, ≤ p^{1/2} for \|A\| > p^{2/3}/3; λ = 2/3^{1/4} = 1.519671… (explicit Heath-Brown–Konyagin; ranges as in the author preprint of 5 Oct 2009, I-1) | isotropic sums, explicit; the 3/8 (middle) branch is needed in the W⁺ range (I-1) |
| Cochrane–Pinner Thm 1.3 | \|Σ e_p(axᵏ+bxˡ)\| ≤ (k−l,p−1) + 2.292d^{13/46}p^{89/92} | binomial; worse than Weil here (K2 correct) |
| Di Benedetto–Garaev–García–González-Sánchez–Shparlinski–Trujillo, JNT (2020), arXiv 2003.06165, Thm 3.1 | \|S_a(H)\| ≲ H^{2689/2880}p^{1/72} for p^{1/4} < H < p^{1/2} (≲ hides p^{o(1)}) | linear only; o(1) losses not explicit |
| Bourgain–Garaev, Math. Proc. Camb. 146 (2009) | H ~ p^{1/4}: H^{1−175/9437184+o(1)} | linear only |
| Macourt–Shkredov–Shparlinski, Canad. J. Math. (2018), Thm 1.5 | trinomial bounds in gcds d, e, f | not useful: both our exponents generate the **same** subgroup |
| **Ostafe–Shparlinski–Voloch, IMRN 2023 (16) 14196–14238, arXiv 2110.10941**, Thm 2.7 / Cor 2.9 | A ∈ SL(2,p) split, (a,aA), (b,Ab) independent: S_{2,p}(a,b;A) ≪ min(τ^{23/36}p^{1/6}, τ^{20/27}p^{1/9}); K_p(G;a,b) same. Absolute implied constants, not stated | **yes, non-isotropic; nontrivial for τ > q^{3/7}**. Their Remark 2.11 also says Bourgain's δ "is not explicit and it is not obvious how to get such an explicit result" |
| OSV, Lemma 4.3 | (Xˢ+Yˢ+a)(Xˢ+Yˢ+bXˢYˢ) − XˢYˢ is absolutely irreducible if gcd(s,q) = 1 and ab(ab−1) ≠ 0 | used in N1 |
| Voloch, Acta Arith. 52 (1989) Thm (i), in the form of Ostafe–Shparlinski–Voloch, "Weil sums over small subgroups" (Math. Proc. Camb., arXiv 2211.07739), Lemma 2.1 | F absolutely irreducible over F_p, deg d < p ⇒ #{F = 0} ≤ 4d^{4/3}p^{2/3} + 3p | used in N1. [P-cite via secondary source: the original was not retrieved. The IMRN Lemma 4.4 omits "+3p", which is false for tiny d; the corrected form is used] |
| Bourgain, J. Anal. Math. 97 (2005) | H < Z_q* (q arbitrary), \|H\| > q^ε ⇒ max_{ξ∈Z_q*}\|Σ_H e_q(ξx)\| < q^{−δ}\|H\| | linear, composite; we need binomial |
| Bourgain, J. Anal. Math. 101 (2007) 325–355 (finite commutative rings) | per zbMATH review: H < R*, \|H\| > \|R\|^ε, R with few divisors ⇒ nontrivial bound unless H is largely in a proper subring or H−1 in a proper ideal | would cover composite c ≤ p^C via R = O/c. **Paper not read; hypotheses not verified** [H] |
| Stewart, Acta Math. 211 (2013) | P(Φ_n(α,β)) > n·exp(log n/(104 log log n)) for Lucas/Lehmer sequences, n large | lower bound on the largest prime of h_{3p} (h_m = Q_m/2, half companion Pell); far below p^C |

## 3. N1: explicit beyond-Weil bound and Theorem W⁺

**Lemma N1.1 (moment inequality) [P].** Let q be prime, H = ⟨ℓ⟩ ≤ F_q* of odd order τ, v_x = (ℓˣ, ℓ⁻ˣ), and
S(a) = Σ_{x mod τ} e(a·v_x/q). For k, l ≥ 1, let J_k be the number of (x₁..x_{2k}) with Σ_{i≤k}v_{x_i} = Σ_{i≤k}v_{x_{k+i}} in F_q².
If a₁a₂ ≠ 0, then |S(a)|^{2kl} ≤ q²·τ^{2kl−2k−2l}·J_k·J_l.

*Proof.*
1. ν_k(w) := #{x : Σv_{x_i} = w} is invariant under w ↦ D^u w with D = diag(ℓ, ℓ⁻¹). So
   S(a)^k = τ⁻¹Σ_w ν_k(w)·S(a⊙w).
2. Hölder with exponents (l/(l−1), 2l, 2l) on ν = ν^{1−1/l}·ν^{1/l} gives
   |S|^k ≤ τ⁻¹(Σν)^{1−1/l}(Σν²)^{1/2l}(Σ_w|S(a⊙w)|^{2l})^{1/2l}.
3. Σν = τ^k and Σν² = J_k. Since w ↦ a⊙w is bijective when a₁a₂ ≠ 0, Parseval gives Σ_w|S(a⊙w)|^{2l} = q²J_l. ∎

This is (6.6) of OSV, re-derived in the diagonal form, with no constants.

**Lemma N1.2 (energies) [P + P-cite].**
- **(a)** J₂ ≤ 2τ² − τ, since −1 ∉ H for τ odd [P]. If u₁+u₂ = u₃+u₄ =: σ and 1/u₁+1/u₂ = 1/u₃+1/u₄, then σ ≠ 0 (because −1 ∉ H),
  so u₁u₂ = u₃u₄ and {u₁,u₂} = {u₃,u₄}. [N]: equality J₂ = 2τ²−τ in all 17 tested levels.
- **(b)** J₃ ≤ τ³·[4·3^{4/3}(qτ/(q−1))^{2/3} + 3qτ²/(q−1)²] + 12τ³. For q ≥ c_W p² and τ ≥ 10⁴⁵ this gives J₃ ≤ 17.31τ^{11/3} (N-F4: the author's "q ≥ τ²" fails in the range 10^{264.5} ≤ p < 10^{344} where W⁺ beats Weil, since
  there q ≤ c_N p^{7/3} < τ²; the term 3qτ²/(q−1)² is ≤ 3τ^{2/3}·τ^{4/3}/q, negligible as soon as q ≥ τ^{4/3+δ}, which q ≥ c_W p², τ ≥ 10⁴⁵ ensure; the referee
  verified the constant 17.31 over the whole W⁺ range).
  This follows OSV Thm 2.2 with every constant tracked:
  - Fix u₃, u₄, u₅ and put a = u₃−u₄−u₅, b = u₃⁻¹−u₄⁻¹−u₅⁻¹. Then (u₁+u₂+a)(u₁⁻¹+u₂⁻¹+b) = 1 must hold, and u₆ is determined.
  - **Degenerate (a,b), i.e. ab(ab−1) = 0.**
    - The equation is a quadratic in u₂ with leading coefficient 1+bu₁, middle coefficient (u₁+a)(1+bu₁) and constant term u₁(u₁+a).
      It vanishes identically only if u₁ = −a and ab = 1. So it has ≤ 3τ solutions (x₁, x₂).
    - The number of degenerate triples is ≤ τ² + τ² + 2τ². For ab = 1, the u₃-quadratic −du₃² + cdu₃ − c vanishes identically
      only if u₄ = −u₅, which is impossible.
    - Contribution ≤ 12τ³ [P].
  - **Non-degenerate (a,b).**
    - Put s = (q−1)/τ. The count is R/s², where R counts F_q-points on F = (Xˢ+Yˢ+a)(Xˢ+Yˢ+bXˢYˢ) − XˢYˢ.
    - F is absolutely irreducible [P-cite OSV Lemma 4.3], of degree d = 3s < q.
    - So R ≤ 4d^{4/3}q^{2/3} + 3q [P-cite Voloch/OSV Lemma 2.1].
  - [N] check: J₃ is within the bound in all 17 levels. In fact J₃/(6τ³) = 0.73–1.5 except at q < τ^{1.2}, where the random
    term τ⁶/q² dominates (logs/n3_check.log).

**Proposition N1.3 [P + P-cite].** Let x ∈ O/q be non-isotropic and let H′ be a subgroup or coset of ⟨λ mod q⟩ of order τ ≥ p.
For (2,3) and (3,3) assume also τ ≥ 10⁴⁵ and q ≥ c_W p² (the J₃ hypothesis after N-F4). Then the following bounds hold.
- (2,2): |S|/τ ≤ (2q/τ²)^{1/4}. This never beats Weil.
- (2,3): |S|/τ ≤ (34.62)^{1/12}·q^{1/6}τ^{−13/36}.
- (3,3): |S|/τ ≤ 17.31^{1/9}·(q/τ^{7/3})^{1/9}.

For isotropic x: |S|/τ ≤ min(√q/τ, λq^{1/4}τ^{−5/8}, λq^{1/8}τ^{−3/8}), λ = 2/3^{1/4} = 1.519671… [Cochrane–Pinner Thm 1.1], each branch only in its range:
√q (Gauss period) for every τ; λτ^{3/8}q^{1/4} for q^{1/2} < τ ≤ q^{2/3}/3; λτ^{5/8}q^{1/8} for 3q^{1/3} < τ ≤ q^{1/2}. A coset gH′ has the same bounds (replace a by ag).
(I-1, amended after the owner audit of PR #65: the report's 1.51967 rounds λ down. The middle branch is needed: for c_W p² < q < τ² the 5/8
bound does not apply and √q/τ > ε_F once q > ε_F²τ², which happens inside the W⁺ range for p ≥ 10^{266.4} (τ = p). With the three branches the
isotropic case is covered on the whole W⁺ range for every p: Gauss for q ≤ ε_F²τ²; the middle branch for ε_F²τ² < q < τ², since there
λq^{1/4}τ^{−5/8} < λτ^{−1/8} ≤ ε_F for τ ≥ 10^{101.6} and τ ≤ q^{2/3}/3 for τ ≥ 10^{51.5}; the 5/8 branch for τ² ≤ q ≤ c_N p^{7/3}, since there
τ ≥ p > 3q^{1/3} and λq^{1/8}τ^{−3/8} ≤ λc_N^{1/8}p^{−1/12} < ε_F. Grid and case-split check: integration_checks/iso_coverage.py, all four families,
10^{264.5} ≤ p ≤ 10^{400} and larger p.)

[N] check: all three inequalities hold, with room, on the 17 real levels q | h_{3p} with q ≤ 6000 (exact 2D FFT; logs/n3_check.log).

**Theorem W⁺ [P + P-cite + CA].** Theorem W of REPORT_L_v2 (same standing inputs, same effective m₁, now with the same "not computed"
caveat) holds with the Weil range replaced by
  q ≤ max(c_W p², c_N p^{7/3}), c_W = 10^{−25.62}, c_N = 10^{−113.80},
for prime conductors q and 7q. Hypotheses restated (N-F4): the part beyond Weil is c_W p² < q ≤ c_N p^{7/3}, which is non-empty only for
p ≥ 10^{264.5}; there τ ≥ p ≥ 10⁴⁵ and q ≥ c_W p², so the J₃ constant 17.31 applies. The binding family is (±2,8)V. The other families give c_N between 10^{−99.9} and 10^{−92.3}.
- (3,3) beats Weil exactly when p ≥ 10^{264.5}.
- (2,3) gives 10^{−75.8}p^{13/6} and is never the best option once (3,3) beats Weil.
- The isotropic part is covered on the whole range for every p by the three branches of N1.3 (I-1; the 5/8 branch alone reaches 10^{−101.5}p³ but does not cover c_W p² < q < τ²), so the non-isotropic sums are binding.
- *Proof.* Insert N1.3 in W3 in place of W1, with τ ≥ p and budget ε_F. Then apply Theorem W unchanged. The constants are in
  logs/n2_constants.log.

**Assessment.** N1 is a genuine new *explicit* result: the exponent of the covered range improves from 2 to 7/3. It is not a
realistic one. Like Theorem W (p ≥ 8·10²⁵), it only matters at astronomically large m.

## 4. N2: the qualitative extension, prime and composite [P-cite]

- **Primes.** Fix C. For q | h_{3p} prime with q ≤ p^C, the Bourgain JAMS Corollary (θ₁ = ℓ, θ₂ = ℓ⁻¹; the orders of θ₁, θ₂ and
  θ₁θ₂⁻¹ are all ≥ p ≥ q^{1/C}) gives |S(x)| ≤ (q/(q−1))q^{−δ(C)} for non-isotropic x. BGK gives the same for isotropic x.
  So Theorem W holds for q, 7q ≤ p^C, p ≥ p₀(C) := ε_F^{−1/δ(C)} and m ≥ m₁ (effective, not computed; N-F7).
  - δ(C) is not numerically available. The bound is **effective, constants not computed**: Bourgain §5(1) gives δ_r > exp(−C₃r(ε^{−C₂} + log r))
    with absolute constants not computed (referee). So p₀(C) is effective, constants not computed (N-F6). "Ineffective" in K2 and in
    lineK_harg_removal.md is corrected accordingly in the repository. (I-2: for the isotropic sums the registry cites Bourgain's Theorem 1
    with r = 1, which his Remark (1) attributes to Bourgain–Konyagin; BGK is cited as context, its theorem text was not read.)
- **Composite c ≤ p^C** (≥ 2 primes ≥ 2p+1). Here Weil/completion is trivial [P, K2]. In the N1 method the energy J₃(c) ≤ J₃(q_max)
  loses the main term τ⁶/q_max², so it gives no uniform saving [P sketch].
  - Bourgain's finite-ring theorem (J. Anal. Math. 101) plausibly applies to H = ⟨λ⟩ ≤ (O/c)*: H−1 lies in no proper ideal since
    ord_{𝔮}λ = r ≠ 1, and the subrings of F_q×F_q containing 1 are the diagonal and the whole ring.
  - I did **not** read the theorem, so composites ≤ p^C are **not** claimed [H].

## 5. Question 2: does a tiny saving suffice? [P]

Yes, per level.
- The quantity to beat is the constant ε_F = 10^{−12.51}. Neither m nor D7 (1.0184^m) enters.
- Theorem W turns "orbit average ≤ I_k+3η at every conductor in the range" into a bound C′((1−δ_F/2)target)^m per conductor, for
  m ≥ m₁ (effective, not computed; N-F7). The
  number of conductors is ≤ τ(h_m) = e^{O(m/log m)}, which the margin (1−δ_F/2)^m absorbs.
- So a saving q^{−δ} works for all q ≥ ε_F^{−1/δ}. On the prime range c_W p² < q ≤ p^C this means p ≥ 10^{12.5/(2δ)}.
- The bottleneck is never the count of levels. It is (i) the explicit value of δ, and (ii) the range limit q ≤ p^{1/ε} inherent to
  |H| ≥ q^ε.

## 6. N3: scarred conductors carry slow orbits [P, on the per-family [CA] bound of TRACE-198]

N3 is the extension of L2 Prop S (TRACE-258, proved: β = 1 is slow at primes q ∥ h_m above λ^{C_k + 6.1·10⁻⁶ m}) from prime and
inherited prime levels to composite conductors, chiefly c = h_p, with an explicit θ (N-F1). The mechanism is the same.

**Theorem N3.**
- *Setting.* Let c ≥ 2 with λ^r ≡ 1 (mod cO), r = ord_c λ. Let F = (±2,8)V be the vertex family of Line L. Its untwisted operator has
  the certified eigenvalue μ*, |μ*| ≥ 1.9154712 (TRACE-198 [CA], for the vertex operator L_{V,4}; the nonzero spectrum of these
  trace-class operators is determined by the traces, which are invariant under the β-weight conjugation, L_v2 §2), so
  ρ(L₀^F) ≥ μ := 1.9154712 (N-F2). Put θ_F := ((1−δ_F/2)·target_F/μ)^{2k_F}; θ_F = 5.39·10⁻⁶ for k_F = 15 (logs/n6_theta.log; Lean
  `Bgs.LineN.theta8V`). (I-3: the author also computed θ = 6.01·10⁻⁶ for (8E). TRACE-198 places the spectrum of L_E in |z| < 1, so the
  edge family does not have ρ ≥ μ*, and that value is not used. Slowness needs only some family F.)
- *Claim.* There is t_F = O(k_F), effective but not computed (rough estimate t_F ≈ 25 + k ≈ 40 [H, referee estimate]; N-F3), such that the
  following holds. If r > 2(N + k) with N := log_λ c − t_F (needed for the min(r, ·) truncation; N-F2) and
  log_λ c ≥ θ_F(1+κ)·r/2 + t_F + k for some κ > 0, then β = 1 is **slow** at conductor c:
  (1/r)Σ_{i<r} f_k^F(λⁱ/c) > ((1−δ_F/2)target_F)^{2k}.
- *Consequences:*
  - c = h_p (r = p, log_λ h_p = p/2 − O(1), from λ^p − 1 = 2h_pε^p, Lean `lam_pow_eq`) is slow for every p ≥ p₀ (effective, not
    computed; with t_F ≈ 40, roughly p ≳ 110 [H]).
  - So is every prime q | K_p with q ≥ λ^{(8.1·10⁻⁶+o(1))p + t_F}, and every q | h_p with q ≥ λ^{(2.7·10⁻⁶+o(1))p + t_F}.

*Proof.*
1. **Periodicity.** λ^r − 1 ∈ cO, so Tr(λ^{n+r})/c ≡ Tr(λⁿ)/c (mod 1). Hence the twist sequence τ_n = Tr(λⁿ)/c is r-periodic, and
   n can be taken in (−r/2, r/2].
2. **Small twists.** For |n| ≤ N := log_λ c − t, |Tr(λⁿ)/c| ≤ 2λ^{|n|}/c ≤ 2λ^{−t}. Every block P_k(λⁿ/c) with |n|, |n+k−1| ≤ N uses
   twists of size ≤ 2λ^{−t}. Since r > 2(N + k), these 2(N − k) + 1 blocks are distinct modulo r.
3. **Continuity.** f_k is a Fourier series with Σ_γ|c_γ|(|σγ|+|σ̄γ|) =: A′_k < ∞ (the c_γ decay superexponentially, OP_abs).
   So |f_k(y) − f_k(0)| ≤ 2πA′_k·λ^{|n|+k}/c on those blocks.
   Choose t = t_F so that this is ≤ κ′f_k(0).
4. **Untwisted size (N-F2).** f_k(0) = ‖L₀^k‖²_HS ≥ ρ(L₀^F)^{2k} ≥ μ^{2k}, by the per-family bound above (TRACE-198 [CA]). No
   standing input and no change of family is needed.
5. **Average.** f_k ≥ 0. The proportion of n with a fully small block is ≥ (2(N−k)+1)/r. Hence the average is
   ≥ (2(log_λ c − t_F − k)/r)·(1−κ′)μ^{2k}, which exceeds the threshold under the hypothesis. ∎

**Corollary N3′ [P, on TRACE-198 [CA]; p₀ effective, not computed].**
- For all m = 3p ∈ S⁺ with p ≥ p₀ (effective, not computed; N-F3), the open set of K2′ contains c = h_p (M3), and c = h_p carries a slow
  β. **So the conclusion of K2′ ("frozen R′ ⇒ some open conductor carries a slow λ-orbit") holds without assuming frozen R′.**
- It cannot be contradicted. Strengthening Theorem W (Weil → OSV → Bourgain → any hypothetical bound for all primes < L_m) cannot
  make K2′- or U-type conclusions unconditional for **any** m. The scarred conductors are not reached by any exponential-sum bound:
  at c = h_p the same computation gives |S(1)| ≥ (1−O(t/p))·r, i.e. no cancellation at all (at a general scarred c a fixed fraction of S(1) stays uncancelled).
- The "remaining obstruction" of REPORT_L_v2 §6 ("exclude slow λ-orbits at conductors c ∈ (c_W p², L_m)") is therefore **false** on
  c ≥ λ^{θr/2+t}. It must be replaced by a **β-weighted** statement, which K2 §5 already anticipated as an [assessment].
- [N] Toy illustration (K2 single-disc model, logs/n5_slow_toy.log). At c = h_p, m = 3p, the trace rate for β = 1 is 1.43, 1.50,
  1.59, 1.62, 1.67, 1.71 for p = 11…29 (untwisted 1.9155). For β = 1+√2 it is 1.57–1.77. For random β it is 0.81–1.18. The threshold is
  1.28359. This also explains K2's "slow β (1,0)" at q = 8761009 (p = 37, near-0 fraction 0.49).

## 7. N4: what the inherited level really is [P identification, H estimate]

- **[P]** On the torus T = (O⊗R)/O^∨, Fix(T^p) = (λ^p−1)⁻¹O^∨/O^∨ = (4√2·h_p·ε^p)⁻¹O/O^∨, which has 4h_p² points. The
  conductor-h_p points ((1/h_p)O + O^∨)/O^∨ (h_p² points) form a subgroup of index **4** = N(4√2)/[O^∨ : O] = 32/8 (N-F8; the author's
  "index N(4√2) = 32" forgot [O^∨ : O] = N(2√2) = 8; brute force p = 3, 5, 7 and Lean `Bgs.LineN.fix3/fix5/fix7`, `idx`).
  - So the twisted sums Ẑ_β at level h_p are twisted traces Tr(M_y³) along the cat map's period-p orbits, with
    M_y = Π_{i<p} L_{τ(Tⁱy)} and m = 3p. Up to the bounded index 4, the sum over β is a sum over all period-p periodic points. (The heuristic margin below does not use
    the index; rechecked after N-F8.)
  - This is exactly where K2 §5's periodic-point positivity loses nothing. It identifies M §8's "cubic functions Tr[R·Π_β³]" as a
    **periodic-orbit (thermodynamic) sum** for the operator cocycle y ↦ L_{Tr y} over the cat map.
- **[H] margin.** In the weights of the L_v2 §5d identity (itself [H]):
  - units carry 1/c² and isotropic β carry 1/c;
  - β whose orbit spends a fraction φ near 0 have archimedean size ≈ λ^{(1−φ)p/2}, so there are ≈ λ^{(1−φ)p} of them;
  - near 0 the rate is μ*, elsewhere a "typical" rate ρ_tw.
  - The weighted contribution is then ≲ ((μ*³/λ)^{φ/3}·ρ_tw^{1−φ})^m ≤ 1.0644^m·max(1, ρ_tw)^m.
  - With ρ_tw ≈ 0.9 (toy random β) this is far below the target 1.2836^m (and isotropic β give ≤ 0.98^m). So scarring at h_p is
    *plausibly harmless after weighting* [H].
- A proof needs a pressure bound: limsup_p (1/p) log Σ_{y∈Fix T^p}|Tr M_y³| < log λ + 3 log((1−δ)·1.28359) = 2.512 (unit weights).
  - This is a subadditive-cocycle pressure over a hyperbolic toral automorphism.
  - It is amenable in principle to a Markov-partition / transfer-operator computer-assisted bound [assessment]. It is not an
    exponential-sum problem.

## 8. N5: factorisations [N]

**PARI factorisation of h_p and K_p = 4h_p²+3** (h_{3p} = h_pK_p) for primes 5 ≤ p ≤ 173 (code/n1_factor.py).
- The run was stopped at p = 173; 5 K_p cofactors of 83–124 digits are unfactored.
- **Congruences.** Every prime q ≠ 7 has q ≡ 1 (mod 2p) and q ≡ ±1 (mod 8), with rank p (h_p) or 3p (K_p): 0 failures.
- **Bands** (192 prime levels, excluding 7):

  | band | ≤ p² | (p², p^{7/3}] | (p^{7/3}, p³] | (p³, p¹⁰] | > p¹⁰ |
  |---|---|---|---|---|---|
  | count | 30 | 10 | 19 | 80 | 53 |

  - Unfactored composites are counted by size.
  - **c_W p² < 1 and c_N p^{7/3} < 1 for all these p, so no level is covered by Theorem W or W⁺ at any computable m.**
- h_p is prime for p ∈ {5, 7, 19, 29, 47, 59, 163}.
- 96 of 187 prime levels have near-0 orbit fraction 2log_λq/r ≥ 0.25. That is far above θ_F, but N3's additive offset t_F = O(k)
  makes it asymptotic.

**p³-smooth part of h_{3p}/7** for all primes p ≤ 2000 (code/n4_smooth.py, trial division over q ≡ 1 mod 2p).
- It is p³-smooth only for p = 5.
- The mean log-share of primes ≤ p³ is 2.7% overall and 0.8% for p > 1000 (max 2.5%).
- 41 of 301 p have no prime factor ≤ p³ at all.

**[H]** The expected log-share of primes ≤ p^C is ≍ C log p/p, so "all open primes ≤ p^C" should happen for only finitely many p.
- **[P-cite]** Unconditionally only P⁺(h_{3p}) > 6p·exp(log 6p/(104 log log 6p)) (Stewart) is known, for large p.
  Infinitude of such p is neither provable nor plausible.
- **[P]** In any case it would not help, by N3′.

## 9. What remains open, precisely

After Line N, the refutation of frozen R′ (via the K-L route, standing inputs) needs control of the signed cross functional at:
1. **Prime conductors** q | h_m with c_N p^{7/3} < q < L_m (explicit). Non-explicitly this shrinks to p^C < q < L_m.
2. **Composite conductors** c | h_m (≥ 2 primes ≠ 7), c < L_m. Nothing is proved below p^C here either (N2 caveat).
3. Within these, the **scarred range** log_λ c ≥ θ_F r/2 + t_F, which contains h_p always. There, **no orbit-uniform statement is true
   (N3)**. Only a β-weighted / periodic-orbit-pressure statement (N4) can work.

The intermediate range p^C < c < λ^{θr/2} is not touched by N3. It has no tools either: |H| < q^{1/C}, and there is no scarring
from near-0 orbits.

**Is there a genuine new proved result?** Yes, two, but neither refutes R′:
- **(N1)** an explicit Theorem W⁺, with range exponent 7/3, constants made explicit from OSV + Voloch. It only matters for p ≥ 10^{264}.
- **(N3)** a proved structural theorem: the K2′/L §6 slow-orbit formulation is satisfied without assuming frozen R′ (at h_p, p ≥ p₀) and hence useless as
  a refutation lever. Any refutation must prove a weighted periodic-orbit (pressure) bound at scarred conductors, h_p first.

## 10. Recommended next step [assessment]

1. Re-state K2′ in weighted form: for each open conductor c, bound Σ_β|W_β|·(orbit-average excess)_β instead of excluding slow β.
2. At c = h_p, use N4: certify a pressure bound for the cocycle y ↦ L_{Tr y} over the cat map. Compare with the heuristic margin
   1.064 vs 1.284.
3. Verify Bourgain's ring theorem before using it for composites.

## 11. Files

- code/n1_factor.py → logs/n1_factor_P5_107.jsonl, logs/n1_factor_P109_400.jsonl (stopped at p = 173),
  logs/n1_factor_P60.jsonl/.log (first pilot), logs/n1_factor_P5_107_crashed_at_109.log (crash fixed: alarm exception).
- code/n2_constants.py → logs/n2_constants.{log,json}: ε_F, c_W, c_N, crossover p.
- code/n3_check.py → logs/n3_check.{log,json}: exact J₂, J₃, max|S| vs the bounds on 17 real levels [N].
- code/n4_smooth.py → logs/n4_smooth_P{1000,2000}.{log,jsonl}; code/n4_summary.py → logs/n4_summary.{log,json}.
- code/n5_slow_toy.py → logs/n5_slow_toy.{log,json} [N] toy illustration of N3.
- code/n6_theta.py → logs/n6_theta.log.
- Literature copies (for audit, in the author's work directory only; third-party papers are **not** copied into the repository):
  logs/osv2110.{pdf,txt} (IMRN OSV), logs/wss2211.{pdf,txt} (OSV Weil sums), logs/mss1701.*, logs/cp.* (Cochrane–Pinner).
  logs/voloch.pdf (also in the manifest) is an **unrelated paper** (certificateless signatures), not Voloch 1989; it is not used, and
  Voloch's point count stays [P-cite via OSV], Math. Proc. Camb. Lemma 2.1 (N-F5).
- NOTES_N.md (resumption); SHA256_N.txt (manifest; its hash in SHA256_N.txt.sha256).

## 12. Errata (v1 → v2, integration; referee N-F1 … N-F10 and integration notes)

| Fix | Where | Change |
|---|---|---|
| N-F1 | §0 N3, §6 | N3 presented as the extension of L2 Prop S (TRACE-258) to composite c, chiefly h_p, with an explicit θ |
| N-F2 | §0 N3, §6 step 4 | Line F "|Z_ρ| ≥ (½−o(1))|μ*|^m" standing input and the family switch replaced by the per-family [CA] bound of TRACE-198 for F = (±2,8)V; r > 2(N + k) added |
| N-F3 | §6 | t_F effective, not computed (rough estimate ≈ 25 + k ≈ 40, p ≳ 110 [H]); p₀ of Corollary N3′ effective, not computed |
| N-F4 | §3 N1.2(b), N1.3, Theorem W⁺ | hypothesis "q ≥ τ², τ ≥ 10²⁵" → "q ≥ c_W p², τ ≥ 10⁴⁵"; W⁺ hypothesis restated; constant 17.31 unchanged (referee verified) |
| N-F5 | §11 | logs/voloch.pdf is an unrelated paper; not used; Voloch stays [P-cite via OSV] |
| N-F6 | §0 N2, §4 | "ineffective"/"not explicit" → "effective, constants not computed"; the repository copies of lineK_harg_removal.md:249 and REPORT_K2_v2.md:20 (and :132) are amended in the same integration |
| N-F7 | §0, §1, §4, §5 | m₁ of Theorem W stated as effective, not computed wherever "for all large m" is used |
| N-F8 | §0 N4, §7 | index 4 (not 32): ((1/h_p)O + O^∨)/O^∨ has h_p² points, Fix(T^p) has 4h_p²; downstream N4 statements rechecked (the margin heuristic does not use the index) |
| N-F9 | §0 N1 | table harmonised with the body: J₂ ≤ 2τ² − τ, J₃ ≤ 17.31τ^{11/3} |
| N-F10 | §0 N1′ | N1′ supersedes REPORT_K2_v2.md:134–137 ("explicit versions do not help for the binomial sums"); pointer added there |
| I-1 | §2, §3 N1.3, W⁺ | Cochrane–Pinner Thm 1.1 ranges stated as 3q^{1/3} < τ ≤ q^{1/2} (5/8 branch) and q^{1/2} < τ ≤ q^{2/3}/3 (3/8 branch); the §2 phrase "valid for every subgroup A" removed; the isotropic bound uses all three branches (Gauss, 3/8, 5/8), which cover the W⁺ range for every p (iso_coverage.py); constant 2/3^{1/4} = 1.519671… (1.51967 rounds down). Amended after the owner audit of PR #65 (R1, R2) |
| I-2 | §4 | the isotropic case of N2 cites Bourgain JAMS Theorem 1 with r = 1; BGK as context only (not read) |
| I-3 | §6 | θ_F only for F = (±2,8)V; the (8E) value 6.01·10⁻⁶ is not used (TRACE-198: spectrum of L_E in \|z\| < 1) |
| I-4 | §0, §6, §9 | "holds unconditionally" → "holds without assuming frozen R′" (wording as in the registry, PR #64 R2) |
| I-5 | registry | owner audit of PR #65: TRACE-278 budget sentence A_k sup\|S\| ≤ η_F/3, i.e. sup\|S\| ≤ ε_F (as in §1 here, R3); family scope "open for the (±2,8) families; slow orbit in (±2,8)V" and θ = θ_(±2,8)V added to TRACE-246/247/258/284 (S1); TRACE-284 names K2′ (TRACE-246), Theorem U (TRACE-254) and Lemma E (TRACE-268) (S2); the TRACE-283 edge of 246/258 marked annotational (S3) |
