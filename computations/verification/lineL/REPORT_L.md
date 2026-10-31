# Line L report: OP certified without cancellation, Theorem W unconditional, open range reassessed

31 Oct 2026. Labels: [P] proved here, [CA] computer-assisted (arb ball arithmetic, python-flint, prec 128),
[N] numerics (floating point), [H] heuristic, [assessment] opinion on strategy. REPORT_v2.md / REPORT_K2_v2.md are untouched.

## 0. Summary

1. **Theorem U (scalar unitarity) [P].** The autocorrelation of the TRACE-206 weights vanishes at every exact
   collision and at every collision mod h. Hence Σ_{x∈O}|A(x)|² = 1 and Σ_{β mod h}|Ẑ(β/h)|² = h².
2. **Theorem OP_abs [P] + certificate [CA].** The cat-map second moment I_k of the true lattice-lifted k1 families is
   bounded *without any cancellation* by a positive collision sum. That sum is a carry automaton with spectral radius
   r_abs = 1.0511 [N], so r_abs^{1/2} = 1.025 ≪ 1.28359. Certified bounds [CA] for the four families:

   | family | k | ρ | β | I_k ≤ | I_k^{1/2k} ≤ | target | A_k ≤ |
   |---|---|---|---|---|---|---|---|
   | (±2,8) V | 15 | 0.75 | 0.25 | 1095.97 | **1.26278** | 1.28359 | 1.75·10¹⁴ |
   | (±2,8) E | 14 | 0.20 | 0.30 | 35.90 | **1.13642** | 1.28359 | 7.24·10¹¹ |
   | (±2,16) V | 14 | 0.90 | 0.30 | 10608.6 | **1.39243** | 1.4742 | 2.55·10¹⁴ |
   | (±2,16) E | 14 | 0.20 | 0.30 | 1645.2 | **1.30276** | 1.4742 | 3.11·10¹³ |

   So **(OP_k, δ) holds** for every family, with its own k (δ ≥ 0.0162 on the binding family (±2,8) V).
3. **Theorem W is unconditional [P + CA]**, modulo the same standing inputs as before (Line F/J lattice trace
   representation, Theorem J/J3, L16). The explicit Weil range is q ≤ c_W p² with **c_W = 10^{−25.62}** and
   p₀ = 10^{13.2}/2. The range is non-vacuous (c_W p² ≥ 2p+1) from **p ≳ 8.2·10²⁵**. The old figure was 10^{800}.
   - This is explicit but not realistic [assessment]: m = 3p ~ 10²⁶ is far beyond any direct computation.
4. **Theorem K2′ is unconditional [P + CA].** Frozen R′ forces, for every large m ∈ S⁺, a slow λ-orbit at an open
   conductor c ∈ (c_W p², L_m).
5. **Open range c_W p² < q < L_m: still open.** Approaches (a)–(d) are evaluated in §5. Each one fails, and the
   failure factor is quantified. The (±2,16) part of the open range narrows to q < 1.1311^{m(1+η)} [P + CA].
   The remaining obstruction is stated in §6.

## 1. Theorem U (scalar L² unitarity) [P]

Notation is as in TRACE-206: w(n) = Φ̂(n)e(−ν₀P(n)/2h), Φ̂(n) = Π_j ĝ(n_j), ĝ(n) = iⁿJ_n(1.8), α_n = Σ_j n_jλ^j,
A(x) = Σ_{α_n = x} w(n), Ẑ(β) = Σ_n w(n)e(Tr(βα_n)/q).

**Lemma U1.** R(v) := Σ_n w(n)·conj w(n−v) = e(ν₀P(v)/2h)·Π_j κ(v_j, θ_j). Here
κ(d,θ) = Σ_a ĝ(a)conj ĝ(a−d)e(−aθ) and θ_j = ν₀y′Tr(λ^{−j}α_v)/(2h).

*Proof.*
- P is a quadratic form, so P(n) − P(n−v) = 2B(n,v) − P(v), and the cross term is linear in n.
- Its coefficient at n_j is (Ψv)_j = Σ_i ψ(|i−j|)v_i. Since ψ(d) = y′x_d − 2hy_d, we get
  (Ψv)_j ≡ y′Σ_i x_{|i−j|}v_i ≡ y′Tr(λ^{−j}α_v)/2 (mod 2h), because x_d = Tr(λ^d)/2.
- The sum over n then factorises coordinate-wise. ∎

**Theorem U.**
- If α_v = 0 or α_v ∈ hO, then all θ_j ∈ Z, and κ(d, 0) = Σ_a ĝ(a)conj ĝ(a−d) = δ_{d,0}. The last equality holds because
  Σ_a ĝ(a)conj ĝ(a−d) = i^d·Σ_a J_a(x)J_{a−d}(x) = i^d·J_d(x−x) = i^d·J_d(0) (Neumann/Graf addition theorem). Hence R(v) = δ_{v,0}·Σ|w|².
- Consequences:
  - Σ_{x∈O}|A(x)|² = Σ_{α_v=0}R(v) = 1;
  - Σ_{c∈O/h}|A(c)|² = 1, i.e. Σ_{β mod h}|Ẑ(β/h)|² = h².
- At a level q | h, (1/q²)Σ_β|Ẑ_β|² = Σ_{α_v∈qO}R(v). For α_v = qγ the residual twist sits at the complementary
  level h/q, so this sum is **not** 1 in general.
- [N] check: logs/l1_unit_m5_L4.log (m = 5, h = 41, |n_j| ≤ 4). The level-h Parseval sum equals Σ|w|² = 0.99981127337
  (truncated mass) to 3·10⁻¹¹, while |Z|² = 182.15.

[assessment] Theorem U is the exact L² statement behind Conjecture C1. It gives *global* (all-units) Parseval
identities. It does **not** control individual levels q | h (§5a).

## 2. Theorem OP_abs (cancellation-free second moment)

**Setting.** These are the true lattice-lifted families of Line F/J (`bgs-lineF/code/lift.py`, Line J v2 sector law, L16):
- (L_τΦ)_c(s) = Σ_n w(n)e(nτ)e(κ n s)·ω(c)/ω(f_n(c))·Φ_{f_n(c)}((s+n)/λ), with κ = C0 for (±2,8) and C0/2 for (±2,16);
- vertex discs of radius ρ (V) or edge discs (E) on H²;
- weights ω(c) = e^{−β|c|}.

This is a diagonal conjugation, so the traces in W2′ are unchanged [P]. The sector phases e(an/8) and the chirp
e(C0n²/2) are unimodular, and none of the bounds below uses them. So one bound covers all sectors a ∈ {0,2,4,6}.

**Lemma O1 (word HS bound) [P].** For a k-word w = (n_0..n_{k−1}), the block M_w is a weighted composition operator with
an affine symbol of slope λ^{−k}. Its image disc has relative radius θ = (ρλ^{−k} + dev)/ρ < 1, where:
- dev ≤ λ/(2(λ−1)) = 0.6036 for V and 1/(2(λ−1)) = 0.1036 for E (geometric sum of roundings);
- so ρ_V > 0.6036 and ρ_E > 0.1036 are needed.

The bound is

‖M_w‖_HS ≤ |Φ̂_w|·Π_j e^{τ_j|n_j|}·(1−θ²)^{−1/2}·(NS·coth(β(1−λ^{−k}))·e^{2β(dev+1)})^{1/2},

with τ_j = 2πκρλ^{−j} + βλ^{−(k−j)}. The factors come from:
- the multiplier: Im s_j = λ^{−j}Im s on the input disc;
- the H² HS norm of an affine composition: (1−θ²)^{−1/2};
- the ω ratio, using |c_out| ≤ λ^{−k}|c_0| + Σ_j|n_j|λ^{−(k−j)} + dev + 1, summed over input sites c_0;
- NS = 64 internal states for L16.

**Theorem OP_abs [P].** Let f_k(y) = ‖P_k(y)‖²_HS = Σ_γ c_γ e(Tr γy). Then
- c_γ = Σ_{α_n−α_{n′}=γ} Tr(M_nM_{n′}^*), so |c_γ| ≤ Σ_{α_{n−n′}=γ}‖M_n‖_HS‖M_{n′}‖_HS;
- I_k = c_0 ≤ C_pair·S_k, with C_pair = NS·coth(β(1−λ^{−k}))·e^{2β(dev+1)}/(1−θ²);
- S_k = Σ_{v: α_v=0} Π_j ρ_j(v_j), where ρ_j(d) = Σ_a|J_a||J_{a−d}|e^{τ_j(|a|+|a−d|)};
- A_k := Σ_{γ≠0}|c_γ| ≤ C_pair·Π_j A(τ_j)², where A(s) = Σ_a|J_a(1.8)|e^{s|a|}.

*Proof.* Cauchy–Schwarz for the HS pairing, then Lemma O1, then summing over n with v = n − n′ fixed. ∎

**Collision structure [P].** α_v = 0 ⇔ v(X) = (X² − 6X + 1)E(X) (λ has minimal polynomial X² − 6X + 1). The
coefficients e_j of E are carries: v_j = e_j − 6e_{j−1} + e_{j−2}. Inverting gives |e_j| ≤ C0g·Σ_i|v_i|λ^{−|j+1−i|},
with C0g = 1/(λ − λ^{−1}) (Green's function). So S_k is a transfer-matrix sum over carry states (e_{j−1}, e_j).

**Certificate [CA]** (`code/l3_op_cert.py`, `code/l4_const.py`).
- S_k ≤ S_box + tail:
  - S_box is the exact arb enumeration over all carries with |e_j| ≤ E0 = 6;
  - tail is a Chernoff bound for max|e_j| > E0: Σ_j e^{−t(E0+1)/C0g}·Π_i A(τ_i + tλ^{−|j+1−i|})², with t = 2.
    It uses |v_i| ≤ |a| + |a − v_i| to drop the collision constraint.
- Bessel values: arb J_a(1.8) for |a| ≤ 60 (l3) or 200 (l4). The tail Σ_{|a|>AM} uses |J_a(x)| ≤ (x/2)^{|a|}/|a|!.
- Both versions give identical certified values.
- The tails are at most 2.5·10⁻¹⁴ (logs/final_op_cert.jsonl).
- Values: table in §0.
- Rates for k < 14 or 15 are *not* certified with these constants. Example: (±2,8) V at k = 14 has bound 1.2858.
  The asymptotic per-step rate is r_abs^{1/2} ≈ 1.025 [N]; the end factors (the C_pair and τ boundary layers) dominate at small k.

## 3. Theorem W (unconditional explicit Weil range) [P + CA]

Theorem W of REPORT_K2_v2 §2 applies family by family. W2′ bounds each Ẑ_β^F separately, so k may depend on F [P].
For each F:
- δ_F = (1 − rate_F/target_F)/2;
- η_F = (((1 − δ_F/2)·target_F)^{2k} − I_k)/3;
- c_F = (η_F/(6A_k))²;
- q₀ is a grid value with T_k(q₀) ≤ η_F, where T_k(q) := Σ_{γ≠0,|N γ|≥q}|c_γ|.

**T_k bound [P].**
- |N(α_v)| ≤ XY ≤ ((aX + Y/a)/2)², with X = Σ|v_j|λ^j and Y = Σ|v_j|λ^{−j}. Take a = λ^{−(k−1)/2}.
- Hence T_k(q) ≤ C_pair·e^{−2s√q}·Π_j A(τ_j + s(aλ^j + λ^{−j}/a))², for every s > 0 (Chernoff).
- This is evaluated in arb on an s-grid and a log₁₀q grid of step 0.1; the bound is monotone in q.

| family | δ | η | log₁₀ c_F | log₁₀ q₀ |
|---|---|---|---|---|
| (±2,8) V, k=15 | 0.00811 | 162.8 | **−25.62** | 13.2 |
| (±2,8) E, k=14 | 0.0573 | 148.4 | −20.93 | 12.3 |
| (±2,16) V, k=14 | 0.0277 | 8285 | −22.53 | 12.3 |
| (±2,16) E, k=14 | 0.0581 | 7102 | −20.84 | 12.2 |

**Theorem W (unconditional form).** Let c_W := 10^{−25.62} ≤ min_F c_F and p₀ := 10^{13.2}/2. For every m = 3p ∈ S⁺
with p ≥ p₀, the total cross part of all conductors c ∈ {q, 7q} (q prime, q | h_m, q ≤ c_W p²), including inherited
copies, is o(ξ_lo^m).
- Per conductor, the bound is explicit: |Ẑ_β^F| ≤ C′_F·((1 − δ_F/2)·target_F)^m with C′_F = e^{O(k)}.
- The o(·) is the same asymptotic count (τ(h) = e^{O(m/log m)} levels) as in K2_v2.
- *Inputs:* Line F/J lattice trace representation and Theorem J/J3 with L16 [CA, as accepted in REPORT_v2]; W1 [P-cite Weil];
  W2′, W3 [P]; Lemma O1 / OP_abs [P]; the certificate [CA].
- *Non-vacuity:* q ≥ 2p+1 forces p ≥ 2/c_W ≈ 8.2·10²⁵.

*Ways to shrink p₀ further [assessment].*
- A_k ≥ (Σ_a|J_a|)^{2k} = 2.369^{2k} is inherent to the ℓ¹ Fourier step of W3.
- The ratio η/A_k decays like (target²/G²)^k, so the smallest certifiable k is optimal (k = 15 is binding).
- Gains would need either of:
  - a sharper boundary layer (a smaller C_pair, e.g. a per-site ω rather than the global coth), which would allow k ≈ 10;
  - an ℓ²-type replacement of W3, e.g. Weil applied after Cauchy–Schwarz in γ.
- Even k = 10 gives c ~ 10^{−17} [H].
- With Bourgain/BGK [P-cite] the range extends to q ≤ p^C, but with an ineffective p₀.

## 4. Theorem K2′ (unconditional) [P + CA]

K2_v2 §4 with (OP) now certified gives the following. For every m = 3p ∈ S⁺ with p ≥ p₀, frozen R′ implies that some
open conductor c | h_m, with c ∉ {1,7} ∪ {q, 7q : q ≤ c_W p²} and c < L_m, carries a slow β. Slow means: for some
family F, (1/r)Σ_{i<r} f_k^F(βλ^i/c) > ((1 − δ_F/2)·target_F)^{2k}, using the k_F, δ_F of §3.

## 5. The open range c_W p² < q < L_m: evaluation of (a)–(d)

**(a) Global identities [P], insufficient [assessment].**
- Theorem U gives Σ over all β mod h of |Ẑ|² = h², and (1/q²)Σ_{β mod q}|Ẑ|² = Σ_{α_v∈qO}R(v).
- The right-hand side involves twists at level h/q, so it is again an open-range object (aliasing, TRACE-218).
- Parseval over all units bounds the *mean* of |Ẑ_β|² by ≈ 1. Over the ≤ q² β at level q this allows a few
  |Ẑ_β| ~ q, which is far too weak against |Z|/q ~ μ^m/q.
- Möbius over divisors does not separate a single level without per-level input.

**(b) Inclusion threshold [P + CA].**
- With d ≤ |Z|/(2√m) and positivity absorption, the (±2,16) levels are absorbed for q ≥ (2.781/2.4587)^{m(1+η)} = 1.1311^{m(1+η)}.
- So the (±2,16) open range is c_W p² < q < 1.1311^{m(1+η)}.
- For (±2,8) there is no narrowing: the range stays up to 1.4923^m.

**(c) D_iso + large sieve [P], fails.**
- The large sieve over all prime ideals 𝔮 | h needs a box of volume λ^m to hold the orbit's Fourier support.
- It loses (λ^{1/2}/1.28359)^m = 1.88^m.
- N = 2 segment-Hölder with I_L reaches only q ≳ λ^{m/4} (≈ √h), and N = 4 fails (1.524^m).

**(d) Sign / positivity [P reformulation].**
- Full-coset identity: Dev_q = 2Re(Z̄δ₀) + qΣ|δ_u|² + |Z|²/q² − |Z_{t_b}|². Here:
  - δ₀ = (1/q)Σ_{iso β≠0}Ẑ_β − (1/q²)Σ_{β≠0}Ẑ_β;
  - Z_{t_b} is the sum at the non-unit ν ≡ 0 (mod q), with E_b = Z_{t_b} − Z/q.
- The only sign-indefinite terms are 2Re(Z̄δ₀) and −|Z_{t_b}|².
- Frozen R′ forces near-uniform Nm-pushforward at open levels, i.e. isotropic mass A(𝔮 ∪ 𝔮̄) ≈ Z/q, which is half
  the "expected" value. No positivity principle forces this to fail [assessment].

## 6. Remaining obstruction (precise)

The refutation of frozen R′ is now reduced, unconditionally up to the standing Line F/J/J3/L16 inputs, to this:
**exclude slow λ-orbits at conductors c ∈ (10^{−25.62}p², L_m)**, for prime c and for composite c with ≥ 2 large prime factors.
- This is a per-level equidistribution statement for the binomial sums Σ_{h∈⟨ℓ⟩}e((Ah + B/h)/q) beyond the Weil range,
  with |⟨ℓ⟩| = r ∈ {p, 3p}, i.e. subgroups of size ≈ q^{1/2−ε} or smaller.
- Bourgain–Glibichuk–Konyagin covers q ≤ p^C, but ineffectively.
- Nothing known covers q up to L_m = e^{Θ(m)} = e^{Θ(p)}, where |H| ≈ log q [assessment].
- This is the real wall: a subgroup of logarithmic size, where only the specific structure of λ (a cat-map orbit)
  can help. Global (all-levels) identities (Theorem U) are available, but aliasing prevents isolating one level.

## 7. Files

- `code/l1_unitarity_check.py`, `logs/l1_unit_m5_L4.log`: Theorem U check [N].
- `code/l2_rabs.py`, `logs/l2_rabs*.{log,json}`: r_abs [N].
- `code/l3_op_cert.py`, `code/l3_scan.sh`, `logs/l3_scan.jsonl`, `logs/l3_op_*.json`, `logs/final_op_cert.jsonl`: OP certificate [CA].
- `code/l4_const.py`, `code/l4_scan.sh`, `logs/l4_scan.jsonl` (partial; scan stopped at k = 18 once the optimum was clear),
  `logs/l4_fine_8V15.jsonl`, `logs/final_constants.jsonl`: constants [CA].
- `NOTES_L.md`.
- `SHA256_L.txt` is the manifest; its own hash is in `SHA256_L.txt.sha256`.
