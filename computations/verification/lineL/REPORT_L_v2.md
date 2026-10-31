# Line L report v2: OP certified without cancellation, Theorem W unconditional, open range reassessed

**v2 (31 Oct 2026, after referee report /workspace/audit/lineL/REPORT.md):** fixes F1–F5 (changelog at the end). REPORT_L.md is kept unchanged.

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
   q₀ = 10^{13.2} (validity of the T_k bound). The range is non-vacuous (c_W p² ≥ 2p+1) from **p ≳ 8.2·10²⁵**.
   The old figure was 10^{800}. **q₀ and c_W are explicit. The threshold m₁ beyond which the o(ξ_lo^m) conclusion
   holds is effective but not computed (F2).** W2′ is used in its corrected bounded-J form (W-F7, §3).
   - This is explicit but not realistic [assessment]: m = 3p ~ 10²⁶ is far beyond any direct computation.
4. **Theorem K2′ is unconditional on OP [P + CA].** Frozen R′ forces, for all sufficiently large m ∈ S⁺ (m ≥ m₁, effective, not computed), a slow λ-orbit at an open
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

This is a diagonal conjugation on lattice sites, so the traces in W2′ are unchanged [P]. **It commutes with J = I and with
J = I⊗J_B (F4)**, since J_B acts only on the internal (block/automaton) index and not on sites; hence Tr(J·D X D^{−1}) = Tr(J X).
Trace-class and the trace formula at the radii used (ρ_V = 0.75–0.9, ρ_E = 0.2) follow from the TRACE-197 hypotheses
(½/ρ_V + 1/λ < 1, ½/(λρ_E) + 1/λ < 1; referee-checked), a standing input. The sector phases e(an/8) and the chirp
e(C0n²/2) are unimodular, and none of the bounds below uses them. So one bound covers all sectors a ∈ {0,2,4,6}.

**Lemma O1 (word HS bound) [P].** For a k-word w = (n_0..n_{k−1}), the block M_w is a weighted composition operator with
an affine symbol of slope λ^{−k}. Its image disc has relative radius θ = (ρλ^{−k} + dev)/ρ < 1, where:
- dev ≤ λ/(2(λ−1)) = 0.6036 for V and 1/(2(λ−1)) = 0.1036 for E (geometric sum of roundings);
- so ρ_V > 0.6036 and ρ_E > 0.1036 are needed.

The bound is

‖M_w‖_HS ≤ |Φ̂_w|·Π_j e^{τ_j|n_j|}·(1−θ²)^{−1/2}·(NS·coth(β(1−λ^{−k}))·e^{2β(dev+1)})^{1/2},

with τ_j = 2πκρλ^{−j} + βλ^{−(k−j)}, where j = 0 is the **outermost** letter (the first one applied to the input disc).
**This τ assignment is essential (F3):** the referee's stress test (k ≤ 5, |n| ≤ 10) gives max HS/bound = 0.287 with it,
and 93.8 (bound fails) with the assignment reversed. The collision sums S_k, A_k, T_k are invariant under j → k−1−j
(X² − 6X + 1 is palindromic), so the ordering matters only in Lemma O1 itself. The factors come from:
- the multiplier: Im s_j = λ^{−j}Im s on the input disc;
- the H² HS norm of an affine composition: (1−θ²)^{−1/2};
- the ω ratio, using |c_out| ≤ λ^{−k}|c_0| + Σ_j|n_j|λ^{−(k−j)} + dev + 1, summed over input sites c_0.
  **Role of the "+1" (F3):** site-index rounding is ½ per step for both V and E, so the site drift is ≤ λ/(2(λ−1)) = 0.6036
  in both lattices. For V, dev + 1 = 1.6036 ≥ 0.6036 is pure slack. For E, dev_E = 0.1036 is only the *disc-centre*
  deviation, and the "+1" is **needed**: dev_E + 1 = 1.1036 ≥ 0.6036 covers the site drift;
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

**W2′ in bounded-J form (W-F7, F1) [P].** REPORT_K2_v2 treated I⊗J_B as finite rank; it is not (‖I⊗J_B‖₁ = ∞).
Corrected statement: let J be bounded (J = I, or J = I⊗J_B with ‖J_B‖ ≤ ½), and X = L_{τ_{m−1}}⋯L_{τ_0}. Then
|Tr(JX)| ≤ C_J·max(1, sup‖L‖)^{2k}·e²·max(1, (1/m)Σ_{i<m}‖P(i)‖²_HS)^{(Q−1)/2},  C_J = ‖J‖·sup_τ‖L_τ‖₁/sup_τ‖L_τ‖.
*Proof.* |Tr(JX)| ≤ ‖J‖·‖X‖₁. Put one leftover factor in trace norm and the rest in operator norm: the leftovers have
total length ℓ ∈ [k, 2k], so they contribute ≤ sup‖L‖₁·sup‖L‖^{ℓ−1} ≤ (sup‖L‖₁/sup‖L‖)·max(1, sup‖L‖)^{2k}.
Steps 3–5 of K2_v2 (product over offsets, GM ≤ QM, (m/|B|)^{(Q−1)/2} ≤ e²) are unchanged. ∎
It is applied to the β-conjugated families (§2), for which J still commutes with the conjugation (F4); C_J and sup‖L‖
are finite there (TRACE-197 + β > 0). The constants remain e^{O(k)}, independent of m. This is the W2′ (with W-F7 errata) now merged in the repo with Line K
(PR #63); a local copy of the errata is in `/workspace/bgs-lineK/K2/REPORT_K2_v3.md` (optional).

Theorem W of REPORT_K2_v2 §2, with this W2′, applies family by family. W2′ bounds each Ẑ_β^F separately, so k may depend on F [P].
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

**Theorem W (unconditional form).** Let c_W := 10^{−25.62} ≤ min_F c_F and q₀ := 10^{13.2}. There is an effective
(not computed) m₁ such that for every m = 3p ∈ S⁺ with m ≥ m₁ (in particular 2p+1 ≥ q₀), the total cross part of all conductors c ∈ {q, 7q} (q prime, q | h_m, q ≤ c_W p²), including inherited
copies, is o(ξ_lo^m).
- Per conductor, the bound is explicit: |Ẑ_β^F| ≤ C′_F·((1 − δ_F/2)·target_F)^m with C′_F = e^{O(k)}.
- The o(·) is the same asymptotic count (τ(h) = e^{O(m/log m)} levels) as in K2_v2. m₁ depends on sup‖L‖, sup‖L‖₁,
  C′_F = e^{O(k)}, the conductor count and the margins (δ_F/2 ≈ 0.004 for (±2,8) V); it is effective but **not computed** (F2).
  [assessment] Counting Weil-range conductors polynomially (≤ 2w of them, with the σ(h)/h factor) instead of via τ(h)
  would keep m₁ small; not done.
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

K2_v2 §4 with (OP) now certified (and W2′ in bounded-J form) gives the following. For all sufficiently large m = 3p ∈ S⁺
(m ≥ m₁, effective, not computed), frozen R′ implies that some
open conductor c | h_m, with c ∉ {1,7} ∪ {q, 7q : q ≤ c_W p²} and c < L_m, carries a slow β. Slow means: for some
family F, (1/r)Σ_{i<r} f_k^F(βλ^i/c) > ((1 − δ_F/2)·target_F)^{2k}, using the k_F, δ_F of §3.

## 5. The open range c_W p² < q < L_m: evaluation of (a)–(d)

**(a) Global identities: identities [P]; "insufficient" is [assessment].**
- Theorem U gives Σ over all β mod h of |Ẑ|² = h², and (1/q²)Σ_{β mod q}|Ẑ|² = Σ_{α_v∈qO}R(v).
- The right-hand side involves twists at level h/q, so it is again an open-range object (aliasing, TRACE-218).
- Parseval over all units bounds the *mean* of |Ẑ_β|² by ≈ 1. Over the ≤ q² β at level q this allows a few
  |Ẑ_β| ~ q, which is far too weak against |Z|/q ~ μ^m/q.
- Möbius over divisors does not separate a single level without per-level input.

**(b) Inclusion threshold [P + CA].** (η specified, F5.)
- With d ≤ |Z|/(2√m) and positivity absorption, the (±2,16) levels are absorbed for q ≥ (2.781/2.4587)^{m(1+η)} = 1.1311^{m(1+η)}.
- So the (±2,16) open range is c_W p² < q < 1.1311^{m(1+η)}.
- **η here (F5):** η = η_m^{(16)} is the Prop K2 exponent with Λ replaced by Λ₁₆ = log(1.6677²/ξ_lo) = log 1.1311 = 0.12319 and
  the (±2,16) constant C ≤ 3.8·10⁻²⁵ in place of S_Z. The proof of Prop K2 (s = 1/ℓ, ℓ = log(2p+1)) gives
  η_m^{(16)} ≤ (0.4043/Λ₁₆ + 1)/ℓ + O(log ℓ/m) = (4.282 + o(1))/log(2p+1). The smaller C only lowers κ₀ (helps).
  So η → 0 like 4.28/log(2p+1), e.g. η ≤ 0.43 for p ≈ 10⁴ up to the O(log ℓ/m) term [P + CA].
- For (±2,8) there is no narrowing: the range stays up to 1.4923^m.

**(c) D_iso + large sieve: the loss factors are computed [P]; "fails" is [assessment].**
- The large sieve over all prime ideals 𝔮 | h needs a box of volume λ^m to hold the orbit's Fourier support.
- It loses (λ^{1/2}/1.28359)^m = 1.88^m.
- N = 2 segment-Hölder with I_L reaches only q ≳ λ^{m/4} (≈ √h), and N = 4 fails (1.524^m).

**(d) Sign / positivity [H] (downgraded, F5: the deficit identity below is not proved or P-checked; it is used nowhere).**
- Claimed full-coset identity [H]: Dev_q = 2Re(Z̄δ₀) + qΣ|δ_u|² + |Z|²/q² − |Z_{t_b}|². Here:
  - δ₀ = (1/q)Σ_{iso β≠0}Ẑ_β − (1/q²)Σ_{β≠0}Ẑ_β;
  - Z_{t_b} is the sum at the non-unit ν ≡ 0 (mod q), with E_b = Z_{t_b} − Z/q.
- The only sign-indefinite terms are 2Re(Z̄δ₀) and −|Z_{t_b}|².
- Frozen R′ forces near-uniform Nm-pushforward at open levels, i.e. isotropic mass A(𝔮 ∪ 𝔮̄) ≈ Z/q, which is half
  the "expected" value. No positivity principle forces this to fail [assessment].

## 6. Remaining obstruction (precise) [assessment]

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
- `REPORT_L.md` (v1, unchanged), `REPORT_L_v2.md` (this file).
- `SHA256_L.txt` is the manifest; its own hash is in `SHA256_L.txt.sha256`.

## Changelog v2 (referee F1–F5)
| Fix | Change |
|---|---|
| F1 | W2′ cited in bounded-J form (W-F7): \|Tr(JX)\| ≤ ‖J‖‖X‖₁, C_J = ‖J‖·sup‖L‖₁/sup‖L‖, ‖J_B‖ ≤ ½, factor max(1, sup‖L‖)^{2k}; errata in K2/REPORT_K2_v3.md. |
| F2 | "p₀ explicit" → "q₀ and c_W explicit; m₁ effective but not computed"; K2′ "for all sufficiently large m". |
| F3 | Role of the "+1" (needed for E: 1.1036 ≥ 0.6036; slack for V) and essential τ ordering stated in Lemma O1. |
| F4 | β-conjugation commutes with J = I and J = I⊗J_B; TRACE-197 hypotheses at the radii used. |
| F5 | (b): η = η_m^{(16)} ≤ (4.282+o(1))/log(2p+1) specified; (d) deficit identity downgraded to [H]; (a),(c),§6 negatives labelled [assessment]. |
