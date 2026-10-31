# Line K: H_arg removed (S⁺ infinite unconditionally), the light-cone identity, large levels by positivity, and the Weil range — towards an unconditional refutation of frozen R′

**Status.** Each result below is labelled:
* paper proofs [P];
* exact or high-precision checks of finite identities [P-check];
* computer-assisted results with exact integers or arb [CA];
* kernel-checked finite statements in Lean (§8);
* one cited external theorem [P-cite] (the Weil bound, EXT-WEIL-1948);
* floating-point numerics [N] and heuristics [H].

**Independent referee audit:** `computations/verification/lineK/referee/REPORT.md`.
* First round: all items ACCEPT AFTER FIXES.
* DELTA: REPORT_v2 ready to integrate; K2 ready after W-F1 and W-F2.
* DELTA2: REPORT_v2 and Lean READY; K2 v2 READY after the one-line fix W-F7. W-F7 was applied at integration (§10).

The packet is `computations/verification/lineK/` (author reports `REPORT_v2.md` and `K2/REPORT_K2_v2.md`, code, logs, Lean, referee
files). The integration record is `evidence/executions/20261031/lineK/INTEGRATION.md`.

**Registered claims** (`record/claims.json`):

| § | claim | content | label | state |
|---|---|---|---|---|
| §2 | BGS-TRACE-234 | Lemma K3 (gap lemma) | [P + CA]; finite part Lean-checked | proved |
| §2 | BGS-TRACE-235 | Theorem K3: S⁺ ∩ {3p : p ≡ p₀ (56)} infinite for every unit p₀ (H_arg removed) | [P + CA] + Dirichlet, Vinogradov | **proved, unconditional** |
| §2 | BGS-TRACE-236 | Corollary K3: the dichotomy on an infinite S⁺; refutation of frozen R′ conditional on H♮ | [CA] | proved (dichotomy) |
| §3 | BGS-TRACE-237 | Theorem K1: light-cone identity at prime levels q ∥ h (2 a square mod q) | [P + P-check] | proved |
| §4 | BGS-TRACE-238 | Prop K2: levels d ≥ L_m absorbed by positivity; S_Z ≤ 0.5000001; η_m ≤ (2.010 + o(1))/log(2p+1) | [P + CA] | proved |
| §5 | BGS-TRACE-239 | hypothesis H♮_mid (an alternative to H♮, not a weakening) | — | **open** |
| §5 | BGS-TRACE-240 | Theorem K: frozen R′ false under H♮ or H♮_mid | [P + CA] | conditional |
| §6 | BGS-TRACE-241 | Lemma W1 (Weil bound over the orbit subgroup; degeneracy criterion) | [P-cite] | proved |
| §6 | BGS-TRACE-242 | Lemma W2′ (non-cyclic block AM–GM, every bounded read-out) | [P] | proved |
| §6 | BGS-TRACE-243 | Lemma W3 (orbit average) | [P] | proved |
| §6 | BGS-TRACE-244 | operator input (OP_k, δ) | — | **open** |
| §6 | BGS-TRACE-245 | Theorem W (Weil range q ≤ c_k p²) | [P], conditional on OP | conditional |
| §6 | BGS-TRACE-246 | Theorem K2′ (frozen R′ ⇒ a slow λ-orbit at an open conductor) | [P], conditional on OP | conditional |
| §6 | BGS-TRACE-247 | Conjecture C1 (lim I_k^{1/k} = 1 for the true families) | [H] | **open** |

**Changed earlier claims:**
* **BGS-TRACE-231 (Theorem J3)** stays `conditional`. Its closure condition now depends only on H♮ (BGS-TRACE-232), because S⁺ is infinite
  by BGS-TRACE-235. The dependency on BGS-TRACE-233 is replaced by one on BGS-TRACE-235.
* **BGS-TRACE-233 (H_arg)** stays `open`. **H_arg is bypassed, not proved**: it is no longer needed for the conclusion of BGS-TRACE-231.
  Its irrationality statement remains undecided.
* **BGS-TRACE-206 (frozen R′) stays open.** No refutation is claimed. Only its boundary and ledger are annotated.

**Scope.** Everything concerns the single-cosine **k1** kick 0.9 cos 2πq at η = 2 (ĝ(n) = iⁿJ_n(1.8)), with:
* the map S = [[3,4],[2,3]] and λ = 3 + 2√2;
* m = 3p, p prime, m ≥ 495;
* the frozen definition of BGS-TRACE-206: 𝓟* = {(2,8), (−2,8), (2,16), (−2,16)}, `resonance_classification_lineG.md` line 107;
* notation as in `lineJ_d7_twisted_coefficient.md` §7: S⁺, O♮_m, K_j, ξ, ξ_lo = 2.4586893.

It says nothing about the Line B kick, Conjecture R (BGS-TRACE-179), R_NSW (BGS-TRACE-210) or BGS (BGS-BGS-001).

## 1. Starting point
Theorem J3 (BGS-TRACE-231) gives, on S⁺ = {m = 3p : cos(arg(B_jξ^m)) ≥ 0.84431}:

W′_m ≥ −4m + 0.99·K_j·1.0184224^m + φ⁻¹O♮_m.

So frozen R′ forces φ⁻¹O♮_m ≤ −0.99K_j·1.0184^m + 4m + o(m) along S⁺. Before Line K, S⁺ was known to be infinite only under
H_arg (arg ξ/2π irrational, BGS-TRACE-233). Line K removes that hypothesis (§2). It then studies O♮ by levels:
* prime levels exactly (§3);
* large levels by positivity (§4);
* the Weil range, conditionally on an operator input (§6).

## 2. H_arg removed — BGS-TRACE-234 [P + CA], BGS-TRACE-235 [P + CA], BGS-TRACE-236 [CA]
**Lemma K3 (BGS-TRACE-234).** Let A = arccos(0.84431)/π, with arb lower bound 0.18001064843. Let b′ ≥ 447 with b′ ∉ {504, 560, 616, 840},
and let r be any unit class modulo g′ = gcd(56, b′). Then V(b′, r) = {v mod b′ : gcd(v, b′) = 1, v ≡ r (mod g′)} has maximal cyclic
gap < A·b′.

*Proof.*
* **(a) 447 ≤ b′ ≤ 6000 [CA, exact integers].** Only b′ ∈ {504, 560, 616, 840} fail (`code/k3_harg.py`; the referee re-verified in
  exact rationals, `referee/ref/ref_k3.py`). Every other b′ has gap ≤ b′/6. The smallest margin is A − 1/6 = 0.01334, at b′ = 672.
* **(b) Sieve for all b′ [P].**
  * Write v = r + g′t, with n′ the part of b′ coprime to g′, R = rad n′ and k = ω(R). The primes 2 and 7 divide g′, so v is
    admissible iff gcd(r + g′t, R) = 1. This is periodic in t mod R, and R | b′/g′.
  * By inclusion–exclusion, X consecutive t contain ≥ Xφ(R)/R − (2^k − 1) admissible t. So consecutive admissible values satisfy
    t₂ − t₁ ≤ ⌊2^kR/φ(R)⌋ + 1 ≤ F + 1, with F = Π_{ℓ|R} 2ℓ/(ℓ−1).
  * A failure needs Π_{ℓ|R} 2/(ℓ−1) ≥ A − 1/R. Any prime ℓ ≥ 23 rules this out (2/22 < A − 1/23).
  * Over the subsets of {3, 5, 11, 13, 17, 19}, exactly nine survive: ∅, {3}, {5}, {11}, {13}, {17}, {3,5}, {3,11}, {3,13}. Each gives
    b′ ≤ 56(F+1)/A ≤ 2644.3, which lies inside the exact range. ∎

**Theorem K3 (BGS-TRACE-235).** For every p₀ ∈ (ℤ/56)*, S⁺ contains infinitely many m = 3p with p ≡ p₀ (mod 56). **No hypothesis
on arg ξ is needed.**

*Proof.* The proof splits on an unknown fact, and does not say which case holds.
* **Irrational case.** If arg ξ/2π is irrational, S⁺ has relative density 0.18001 in the class. This is the Line J3 argument:
  Vinogradov (EXT-VINOGRADOV-1937), the prime number theorem in progressions (EXT-DAVENPORT-1980) and the Weyl criterion
  (EXT-WEYL-1916), in BGS-TRACE-231 (3).
* **Rational case.** Suppose arg ξ/2π = a/b in lowest terms.
  * J3 `rat_excl` [CA] gives b ≥ 1339. Put b′ = b/gcd(3, b) ≥ 447 and a′ = 3a/gcd(3, b). Then gcd(a′, b′) = 1, and m·arg ξ/2π ≡ a′p/b′
    (mod 1).
  * The congruences p ≡ p₀ (56) and p ≡ v (b′) are compatible iff v ≡ p₀ (mod g′). The joint class is a unit mod lcm(56, b′) iff
    gcd(v, b′) = 1. So by Dirichlet (EXT-DIRICHLET-1837) every v ∈ V(b′, p₀ mod g′) is hit by infinitely many primes p ≡ p₀ (56).
  * As sets, a′·V(b′, r) = V(b′, a′r). Lemma K3 holds for every unit class, so the phase set {a′v/b′} has all cyclic gaps < A·b′. It
    therefore meets the closed arc {x : cos(arg B_j + 2πx) ≥ 0.84431}, which has length A.
  * **Exceptional b′.** For b′ ∈ {504, 560, 616, 840}, the candidate b ∈ {1512, 560, 1680, 616, 1848, 2520} have no fraction in the
    outward-rounded enclosure [0.88797591, 0.88797627]. This is an exact test, rechecked by the referee and in Lean (§8).
  * B_j is constant on the class (j = 3p mod 168), and m ≥ M0(j) holds for p large. ∎

No density is claimed in the rational case.

**Corollary K3 (BGS-TRACE-236).** Assume Theorem J/J3 (BGS-TRACE-225, 227, 231; Lemma L16 accepted in the Line J audit, DELTA3
§D3.3). Then, for each unit p₀, frozen R′ ⇒ φ⁻¹O♮_m ≤ −0.99K_j·1.0184224^m + 4m + o(m) on an infinite set of m = 3p.

Integration wording (referee): *S⁺ ⊂ {3p} is infinite unconditionally (H_arg removed). Hence frozen R′ is false under H♮ alone.
Unconditionally, frozen R′ forces exponential cancellation of D7 by the conductor ∉ {1, 7} parts on an infinite set of m = 3p.* The dichotomy
is proved. The refutation is **conditional on H♮** (BGS-TRACE-232, open).

## 3. Theorem K1: the light-cone identity — BGS-TRACE-237 [P + P-check]
**Hypotheses.** q ≠ 7 is prime, q ∥ h_m, and **2 is a square mod q** (q ≡ ±1 mod 8). The last condition is automatic for q | h_m,
since 2y′² ≡ 1 (mod q). Then qO = 𝔮𝔮̄ splits.

**Word grouping.** Group the words w by x_w = Σ_i n_iλ^i ∈ O/q. This is legitimate by absolute convergence (L16 step 3 / Line F).
It gives Ẑ_β = Σ_x A(x)e(Tr(βx)/q), with A_tot = Ẑ_0.

**Theorem K1.** Σ_{β≠0} Ẑ_β W_{q,β} = D_iso − E_b/q, where:
* D_iso = A(𝔮 ∪ 𝔮̄) − ((2q−1)/q²)A_tot;
* E_b = Σ_x A(x)e(−N(x)t_b/q) − A_tot/q;
* t_b is the missing label.

*Proof.*
1. W_{q,β} = q⁻²Σ_{t≠t_b}e(N(β)t̄/q) (BGS-TRACE-229).
2. Complete the square. The Gauss sum is Σ_β e(uN(β)/q) = G(u)G(−2u) = (2/q)·q = q. **This uses (2/q) = +1.**
3. Sum over t ≠ t_b.
4. Subtract the β = 0 term (q−2)A_tot/q², and use #{N(x) ≡ 0} = 2q − 1. ∎

**Checks.**
* [P-check] Author: random complex A, 40 digits, q = 7, 17, 23, 31; error ≤ 2·10⁻³⁹ (`code/k1_cone_check.py`).
* Referee: exact in ℤ[ζ_q] for every δ-mass and every t_b, q = 7, 17, 23, 31, 41, 47. There are 0 mismatches in 214,240 cases
  (`referee/ref/ref_k1_exact.py`).
* Control: for q = 11 and 13 (2 a non-square) every case fails.

**Reformulation [P].** D_iso and E_b depend on A only through its push-forward A_N(u) = Σ_{N(x)≡u}A(x). So the level-q cross
part vanishes iff D_iso = E_b/q.

**Interpretation [H] (not registered as P).** These statements are not proved:
* that "trivial zeros are exactly ∩𝔮";
* that "sporadic zeros are unavoidable";
* that "H♮ at prime levels ⇔ equidistribution on 𝔮 ∪ 𝔮̄". This one omits E_b, which is bounded a priori only by the total-variation
  mass.

## 4. Prop K2: large levels by positivity — BGS-TRACE-238 [P + CA]
**Z-bound [CA]** (`code/k2_SZ.py`). For m ≥ 495, |Z_ρ(m)| ≤ C_ρμ^m with μ = 1.9154753:
* (±2,8), from Line F (BGS-TRACE-198, 199): C ≤ (1 + λ^{−495})(½ + 1506.18·1.9154712^{−495}) ≤ 0.5000001;
* (±2,16), from the J3 rest certificates and L16 (BGS-TRACE-226, 227): coefficient sum ≤ 2.273·10⁵ at rate ≤ 1.6677, so the
  effective C ≤ 3.8·10⁻²⁵.

Hence S_Z = Σ_ρ C_ρ² ≤ 0.5000001. The JSON stores the float 0.5; the registered bound is 0.5000001.

**Proposition K2 (BGS-TRACE-238).** For m = 3p ≥ 495 and every included d, Dev_d(ρ) ≥ −n_d|Z_ρ|²/d² ≥ −|Z_ρ|²/d. Let
w = ⌊log h_m/log(2p+1)⌋, using the r(q) lemma and 49 ∤ h. By Rankin, Σ_{d|h, d≥L} 1/d ≤ L^{s−1}(1−7^{−s})^{−1}(1−(2p+1)^{−s})^{−w}.
Hence Σ_{ρ, d≥L} Dev_d ≥ −0.01(K_min/2)ξ_lo^m whenever log L ≥ L*(m) = min_s [E(s) − T_m]/(1−s), with
* E(s) = −log(1−7^{−s}) − w·log(1−(2p+1)^{−s});
* T_m = log(0.01K_min/(2S_Z)) − mΛ, where Λ = log(μ²/ξ_lo) = 0.40030.

With s = 1/log(2p+1) this gives L_m = (μ²/ξ)^{m(1+η_m)}, where η_m ≤ (2.010 + o(1))/log(2p+1) [P].

**Notes.**
* 2.010 is the bound for s = 1/ℓ. The optimised asymptotic constant is ≈ 1.988 (c ≈ 1.164).
* **Non-vacuity [N].** K2 has content only when L_m < √h_m. Bisection gives m ≈ 1.682·10⁹ (m ∈ [1.6821, 1.6823]·10⁹); the referee
  got [1.672, 1.683]·10⁹. **For m below about 1.68·10⁹ no included level satisfies d ≥ L_m, so K2 changes nothing there
  (O♮^{<L} := O♮).** The crossover is numerical only and is not part of the proved statement.
* **Compatibility with J3.** Levels d ≥ L are absorbed whole. For d < L the X7 copies keep A^{<L} ≥ 1, |X16^{<L}| ≤ |X16|, and
  Q^{<L} ≥ 0.

## 5. Theorem K and H♮_mid — BGS-TRACE-239 (open), BGS-TRACE-240 [conditional]
**Theorem K (BGS-TRACE-240).** For m ∈ S⁺ with m ≥ 495 and m ≥ M0(j) [CA]:

W′_m ≥ −4m + 0.99K_j·1.0184^m + φ⁻¹(O♮_m^{<L} − 0.01(K_min/2)ξ_lo^m).

The loss term is absent when no included level is ≥ L_m. At each prime level q ∥ h in O♮^{<L} the contribution is
Σ_ρ 2Re(conj Z_ρ (D_iso(q) − E_b(q)/q)) (Theorem K1). Two hypotheses are each sufficient:
* **H♮** (BGS-TRACE-232): for some δ > 0 and infinitely many m ∈ S⁺, O♮_m ≥ −(1−δ)·0.99(K_j/2)ξ_lo^m;
* **H♮_mid** (BGS-TRACE-239): for some δ > 0 and infinitely many m ∈ S⁺, O♮_m^{<L} ≥ −(1−δ)·0.98(K_j/2)ξ_lo^m.

Either one implies that frozen R′ is false. For H♮ this is Corollary K3. For H♮_mid:
0.99K_j/2 − 0.01K_min/2 − (1−δ)0.98K_j/2 ≥ 0.98δK_j/2, and φ⁻¹ ≥ 2λ^{−m/2}, so W′_m ≥ 0.98δK_j·1.0184^m − 4m → ∞.

**H♮_mid is not a weakening of H♮.**
* For m ≲ 1.68·10⁹ it is slightly stronger, with constant 0.98 against 0.99.
* Beyond that it drops the top levels but pays the 0.01 loss.
* O♮^{≥L} has no sign, so neither hypothesis implies the other.

Neither H♮ nor H♮_mid is proved. **Theorem K is conditional, and frozen R′ is not refuted.**

## 6. The Weil range (K2 report) — BGS-TRACE-241…247
**Setting.** m = 3p, q ≠ 7 prime, q | h_m, r = r(q) ∈ {p, 3p}. H = ⟨ℓ⟩ ⊂ F_q* has order r, with ℓ = σ(λ). P_k^F(y) is the k-block
of the twisted operator family F:
* the (±2,8) sector-law vertex/edge operators;
* the (±2,16) L16 block operators.

Also:
* f_k = ‖P_k‖²_HS = Σ_γ c_γ e(Tr(γy)), and A_k = Σ_{γ≠0}|c_γ| < ∞;
* I_k = c_0, the cat-map second moment.

**Lemma W1 (BGS-TRACE-241) [P-cite: Weil, EXT-WEIL-1948].** For A, B ∈ F_q not both 0: |Σ_{h∈H} e((Ah + Bh⁻¹)/q)| ≤ 2√q, and ≤ √q
if AB = 0.
* Proof: the characters trivial on H detect H; the twisted Kloosterman sums satisfy the Weil bound, and Gauss sums are used when
  AB = 0.
* **Degeneracy.** For a unit β the sum is degenerate iff γ ∈ qO. For β ∈ 𝔮̄∖0 it is degenerate iff γ ∈ 𝔮.
* Conductor 7q: ≤ 6√q, by splitting i mod 3.
* [N] Instance check: `K2/code/w1_weil_check.py`, maximum ratio 1.19 (binomial) and 0.59 (linear).

**Lemma W2′ (BGS-TRACE-242) [P], every bounded read-out (after W-F7).** Let 1 ≤ k, m ≥ 4k, Q = ⌊(m−1)/k⌋, and P(i) the k-blocks.
For a bounded read-out J:

|Tr(JX)| ≤ C_J·max(1, sup‖L‖)^{2k}·e²·max(1, (1/m)Σ_{i<m}‖P(i)‖²_HS)^{(Q−1)/2}, with C_J = ‖J‖·sup‖L‖₁/sup‖L‖.

The read-outs are J = I (‖J‖ = 1) and the (±2,16) read-out I⊗J_B. The latter is **not** of finite rank (‖I⊗J_B‖₁ = ∞), but
‖I⊗J_B‖ = ‖J_B‖ ≤ ½.

*Proof.* Use non-cyclic offsets o ∈ [0, k) and the Q−1 blocks inside [0, m), then |Tr(JX)| ≤ ‖J‖·‖X‖₁ with one leftover factor in
trace norm. Take the product over offsets (block starts B = [0, (Q−1)k), |B| ≥ m − 2k), then GM ≤ QM, and
(m/|B|)^{(Q−1)/2} ≤ (1 − 2k/m)^{−m/2k} ≤ 4 ≤ e².

**Lemma W3 (BGS-TRACE-243) [P].** For q ∥ h and β ≠ 0:

(1/r)Σ_{i<r} f_k(βλ^i/q) ≤ I_k + 2√q·A_k/r + T_k(q),

where T_k(q) = Σ_{γ≠0, |N(γ)|≥q}|c_γ| → 0 by dominated convergence. Use 6√q for conductor 7q.

**(OP_k, δ) (BGS-TRACE-244, open).** The required bounds are:
* (I_k^F)^{1/2k} ≤ (1−δ)·1.28359 for every (±2,8) family;
* (I_k^F)^{1/2k} ≤ (1−δ)·1.4742 for every (±2,16) family.

Note 1.4742 < ξ_lo/1.6677 = 1.4742995. The earlier constant 1.4743 was false (W-F2). **Not proved.**

**Theorem W (BGS-TRACE-245), conditional on (OP).** Fix k, with η and q₀ as in the K2 report and c_k = (η/(6A_k))². For p ≥ p₀ and
m = 3p ∈ S⁺, the cross parts of all conductors c ∈ {q, 7q : q prime, q | h_m, q ≤ c_kp²}, including their inherited copies, sum to
o(ξ_lo^m).
* The constants are astronomically large (c_k ~ 10^{−800}, p₀ ~ 10^{800} in the toy basis). **Theorem W is asymptotic only.**
* Step 6 uses 1.6677·1.4742 = 2.458523 < ξ_lo and 1.9154753·1.28359 = 2.4586849 < ξ_lo.

**Theorem K2′ (BGS-TRACE-246), conditional on (OP).** Frozen R′ ⇒ for all large m ∈ S⁺ (an infinite set, BGS-TRACE-235), some
**open** conductor c of h_m carries a **slow** λ-orbit.
* An open conductor is c ∉ {1, 7} ∪ {q, 7q : q ≤ c_kp²} with c < L_m. The condition c < L_m is vacuous for m ≲ 1.68·10⁹.
* A β is slow if its k-block HS orbit average exceeds ((1−δ/2)·target)^{2k}.
* For given m, c and β this is checkable in principle by a certified operator computation (truncation with rigorous error).

**Conjecture C1 (BGS-TRACE-247, open) [H/conjecture].** For the true families, lim_k I_k^{1/k} = 1.
* The heuristic is unitarity, Σ|ĝ(n)|² = ΣJ_n(1.8)² = 1.
* The toy evidence [N] is the exact carry-automaton I_k of a toy single-disc Galerkin, with per-step ratio 1 − 10⁻¹⁰ (K = 24/40, two
  truncations each). Scaling ĝ by 1.1 gives the ratio 1.21 exactly.
* This is **not** the certified two-disc operator, and C1 is not proved.

**Not registered.** The Bourgain extension to q ≤ p^C is [P-cite], ineffective and conditional on (OP) (K2 report §3); it is not in the
registration list for this integration. The literature assessments in K2 §3 are [assessment].

## 7. Numerics, negative findings and assessment (not claims)
* **K4 [N, toy only].** Cat-map block operator-norm rates of a toy single-disc Galerkin are R_k^cat = 6.338, 2.255, 1.337, 1.131, 1.037,
  0.974 for k = 6, 12, 24, 36, 48, 64 (`code/k4_catrate.py`; referee rerun byte-identical). **Nothing about q ≤ p^C is proved, and all
  of d < L_m is open.** Toy numerics suggest the small-q part is benign *if* a BGK-type equidistribution input holds [H].
* **Negative findings (K2 report §4, §5).**
  * (b) A single level with the trivial bound already beats D7 by (μ*/1.2836)^m, so counting levels cannot work.
  * (d) Composite primitive conductors with two large primes are ≥ (2p+1)², outside every explicit range.
  * Periodic-point positivity and β-moment/Markov bounds both fail.
  * The segment-Hölder route is blocked by non-normal constants.

  These are recorded findings, not theorems about R′.
* **Factorisations [N]** (p ≤ 43). Most prime factors of h_{3p} lie in p² < q < √h, the open range.
* **Toy level traces [N].** Weil-range levels have rates 1.07–1.21 < 1.2836. Some open-range levels have slow β with rate 1.29–1.36.
  These are maxima over β, not the weighted sum.
* **[assessment]** The author's evaluation of the owner's ideas (REPORT_v2 §5), and the literature remarks in K2 §3.

## 8. Lean
`formalization/Bgs/LineKFinite.lean` (namespace `Bgs.LineK`) is part of `lake build Bgs`. It is core Lean with `decide` and
`decide +kernel` only: no `native_decide`, no `sorry`.

| theorem | content | axioms |
|---|---|---|
| `no_small_denominator`, `exceptions_excluded` | no a/b in the widened enclosure [0.88797590, 0.88797628] for 1 ≤ b < 1339, or for the six exceptional b | none |
| `noFrac_sound` | soundness of the ceiling test | propext, Quot.sound |
| `sieve_enumeration`, `sieve_survivors`, `big_prime_excluded` | finite part of the K3(b) sieve | none |
| `bprime_ge` | 3 ∣ b → 1339 ≤ b → 447 ≤ b/3 | propext, Quot.sound |
| `sixth_lt_A` | 1/6 < 18001/100000 | none |
| `gaps_447` | Lemma K3(a), gap ≤ b′/6, for 447 ≤ b′ ≤ 466 only | none |

**Full range 447 ≤ b′ ≤ 2645.** This is covered by the author's 62 chunk files `computations/verification/lineK/lean/K3Gaps_*.lean`,
using `decide +kernel`: chunks of 100 up to 1646, and chunks of 20 above. They are **not** part of `lake build Bgs`, because a chunk of
100 needs 12 GB or more of memory and the author's chunks of 100 above 1646 were killed for memory. At integration `K3Finite.lean`
and the chunks were recompiled sequentially with the project toolchain (Lean 4.33.1). 61 chunks exit 0. The 100-modulus chunk
`K3Gaps_1547` was killed for memory twice on the 15 GB box (exit −9, about 12.2 GB); the referee had compiled it (exit 0, 123 s). Its
range 1547..1646 was therefore re-checked as five 20-modulus chunks with identical definitions (only `okRange lo 20` changed), all
exit 0. Every `gaps_*` depends on no axioms. Logs are in `evidence/executions/20261031/lineK/lean_gaps/`.

**Not formalised:**
* the inclusion–exclusion sieve inequality;
* the monotonicity step for ℓ > 23;
* the arb bound 0.18001 ≤ A;
* CRT, Dirichlet and Vinogradov;
* everything analytic (Theorem K1, Prop K2, W1–W3, Theorems K, W, K2′).

## 9. Integration checks
`computations/verification/lineK/integration_checks/lineK_checks.py` was written at integration from the definitions and ends
`ALL_OK`. It checks:
* A ≥ 0.18001;
* its own implementation of the Lemma K3(a) gap check on 447..2645 (failures exactly {504, 560, 616, 840}, all others ≤ b′/6);
* the sieve survivors;
* the enclosure tests and the least denominator 1339;
* Λ = 0.40030 and the non-vacuity threshold η < 0.1009;
* the Theorem K arithmetic;
* the Theorem W step-6 constants (including that 1.4743 fails);
* the W2′ constant ≤ e²;
* (2/q) = +1 for the prime factors of small h_m.

The author reruns at integration (isolated copy) are recorded in `INTEGRATION.md`.

## 10. Review record and W-F7
The referee report, with its first round, DELTA and DELTA2, is `computations/verification/lineK/referee/REPORT.md`.
* **W-F7, DELTA2.** In Lemma W2′ the (±2,16) read-out I⊗J_B is not of finite rank. It is replaced by the bounded-J argument,
  |Tr(JX)| ≤ ‖J‖·‖X‖₁ with C_J = ‖J‖·sup‖L‖₁/sup‖L‖ and ‖J_B‖ ≤ ½, and the constant is written max(1, sup‖L‖)^{2k}.
* W-F7 was applied at integration in the packet copy `K2/REPORT_K2_v2.md` (§8 "Errata W-F7"). The author's file is in
  `pre_polish/K2/REPORT_K2_v2.md`; its sha256 c9f58c24… matches `K2/SHA256_K2.txt`.
* The conclusions of Theorem W and K2′ are unchanged (C′ = e^{O(k)}, independent of m).

## 11. Dependencies
* **Earlier claims:**
  * BGS-TRACE-198/199: Line F Z-bound (|c^f| = ½, H₀ = 1506.18);
  * 206: frozen R′, 𝓟*;
  * 212, 213: I2′, decomposition, W′_A ≥ −4m;
  * 221: sector law;
  * 223: ξ;
  * 225: Theorem J, K_j, M0;
  * 226, 227: L16, (±2,16);
  * 228: inheritance;
  * 229: prime-level W;
  * 230: r(q) lemma;
  * 231: Theorem J3;
  * 232: H♮;
  * 233: H_arg, rat_excl.
* **External:**
  * EXT-DIRICHLET-1837, EXT-VINOGRADOV-1937, EXT-DAVENPORT-1980 and EXT-WEYL-1916 (Theorem K3);
  * EXT-WEIL-1948 (Lemma W1).
