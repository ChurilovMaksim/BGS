# Line L + L2 + L3: the operator input OP certified without cancellation, Theorem W and K2′ without OP, and the open range c_W p² < q < L_m

**Status.** Each result below is labelled:
* paper proofs [P];
* computer-assisted results in arb ball arithmetic (python-flint, prec 128) [CA];
* kernel-checked finite numeric inequalities in Lean (§10; core `decide` only);
* floating-point numerics [N], heuristics [H] and opinions on strategy [assessment]. **[N], [H] and [assessment] items are notes only
  (§9); they are not registered as claims.**

**Independent referee audit:** `computations/verification/lineL/referee/REPORT.md`.
* Line L, first round: ACCEPT AFTER FIXES F1–F5. DELTA (REPORT_L_v2.md): all fixes applied, **READY**.
* Line L2: **READY after text fixes L2-F1–L2-F4**. The author was busy, so the fixes (and the Prop S block-count nit) were applied at
  integration as an errata section, §7 of `computations/verification/lineL/L2/REPORT_L2.md`; the author's file is
  `computations/verification/lineL/pre_polish/L2/REPORT_L2.md` (its sha256 6be0793b… is the one in the L2 manifest and the referee report).
* Line L3: **READY after fixes L3-F1–L3-F4**, applied at integration in the same way, §6 of `computations/verification/lineL/L3/REPORT_L3.md`
  (author file `computations/verification/lineL/pre_polish/L3/REPORT_L3.md`, sha256 f9b76e03…).

The packet is `computations/verification/lineL/` (author reports `REPORT_L.md` (v1), `REPORT_L_v2.md`, `L2/REPORT_L2.md`, `L3/REPORT_L3.md`,
code, logs, manifests `SHA256_L.txt`, `L2/SHA256_L2.txt`, `L3/SHA256_L3.txt`, referee files `referee/`, integration checks
`integration_checks/`). The integration record is `evidence/executions/20261031/lineL/INTEGRATION.md`.

**Standing inputs** (unchanged from Lines F, J, K; every "proved" below is relative to them): the Line F/J lattice trace representation and
its radius hypotheses (BGS-TRACE-197; ½/ρ_V + 1/λ = 0.838 < 1 at ρ_V = 0.75, ½/(λρ_E) + 1/λ = 0.6005 < 1 at ρ_E = 0.2), Theorem J
(BGS-TRACE-225), Lemma L16 (BGS-TRACE-226), the (±2,16) level-7 control (BGS-TRACE-227), S_Z / Prop K2 (BGS-TRACE-238), and the Weil bound
W1 (BGS-TRACE-241, EXT-WEIL-1948); **all proved**. Of Theorem J3 (BGS-TRACE-231, conditional) only the notation and its proved parts
(1) identity (BGS-TRACE-212, 213, 228) and (2) [CA] bounds (BGS-TRACE-225, 227) are used; the conditional conclusion of BGS-TRACE-231 and
the open hypotheses BGS-TRACE-232, 233, 239, 256 are not used. Theorem K (BGS-TRACE-240, conditional) enters 246 and 257 only through its
proved implication "O♮^{<L}_m = o(ξ_lo^m) along an infinite subset of S⁺ ⇒ W′_m/m → ∞", re-derived from its proved components
(BGS-TRACE-235, the proved parts of 231 with 238, and 237); 240 is not listed as a dependency of any proved claim here. H_mean
(BGS-TRACE-256, open) is the antecedent of the implication 257 and is likewise not listed as its dependency. No proved claim of this note
depends on a non-proved claim, except on BGS-TRACE-206 through its frozen definition (precedent BGS-TRACE-213, 225, 237, 238).

**Registered claims** (`record/claims.json`):

| § | claim | content | label | state |
|---|---|---|---|---|
| §2 | BGS-TRACE-248 | collision structure: α_v = 0 ⇔ (X² − 6X + 1) \| v; carries and Green's-function bound | [P] | proved |
| §2 | BGS-TRACE-249 | Lemma O1 (word HS bound; τ assignment with j = 0 outermost; "+1" needed for E) | [P] | proved |
| §2 | BGS-TRACE-250 | Theorem OP_abs: I_k ≤ C_pair·S_k, A_k ≤ C_pair·Π_j A(τ_j)² (no cancellation used) | [P] | proved |
| §2 | BGS-TRACE-251 | four-family certificate: I_k^{1/2k} ≤ 1.26278 / 1.13642 / 1.39243 / 1.30276 < targets | [CA] | proved |
| §2 | BGS-TRACE-252 | T_k bound and constants c_W = 10^−25.62, q₀ = 10^13.2; non-vacuous from p ≈ 8.3·10²⁵ | [P + CA] | proved |
| §5 | BGS-TRACE-253 | (±2,16) open range narrows to q < (1.6677²/ξ_lo)^{m(1+η)}, η ≤ (4.282 + o(1))/log(2p+1) | [P + CA] | proved |
| §3 | BGS-TRACE-254 | Theorem U (level-h scalar L² unitarity); linked to C1 (BGS-TRACE-247), does not imply it | [P] | proved |
| §6 | BGS-TRACE-255 | L2 decomposition: D_𝔮, D_iso through Ẑ_β | [P] | proved |
| §6 | BGS-TRACE-256 | hypothesis H_mean | — | **open** |
| §6 | BGS-TRACE-257 | H_mean ⇒ frozen R′ refuted (implication) | [P] | proved (implication) |
| §6 | BGS-TRACE-258 | Prop S (β = 1 slow at q ∥ h_m once log_λ q ≥ C_k + 6.1·10⁻⁶·m) and its L2-F4 consequence | [P] | proved |
| §7 | BGS-TRACE-259 | Lemma A1 (exact second moment; exact collisions contribute 0) | [P] | proved |
| §7 | BGS-TRACE-260 | Prop A2 (phase-blind barrier ≥ G^{2m}/q; thresholds 3.4074^m, 2.5832^m exceed h_m) | [P + CA] | proved |
| §7 | BGS-TRACE-261 | Lemmas B1–B3 (height/norm; B1/B2 for split q) | [P] | proved |
| §7 | BGS-TRACE-262 | the height zone and the open range are disjoint for all sufficiently large p | [P] | proved |
| §8 | BGS-TRACE-263 | L3 S1: A = χ·B_m, B̂_m(y) = Π_j g(Tr λ^j y), \|B̂_m\| ≡ 1 | [P] | proved |
| §8 | BGS-TRACE-264 | L3 S2: CRT split; \|D_𝔮\| ≤ 2h/q (when \|Z\| ≤ h), useful only for q ≳ 1.8808^m > L_m (after L3-F1) | [P] | proved |
| §8 | BGS-TRACE-265 | L3 S3: h_{3p} = h_p(4h_p² + 3); primes of K_p other than 7 have rank 3p; no Gauss-side folding (after L3-F2) | [P] | proved |
| §8 | BGS-TRACE-266 | L3 S4: Ẑ^{(3p)}_β = c_{3p}·Tr[R·Π_β³] at rank-p levels | [P given Line G/I] + [N] | proved |
| §8 | BGS-TRACE-267 | L3 Lemma Q (exact line quadrature) and the block-energy use | [P] | proved |
| §8 | BGS-TRACE-268 | L3 Lemma E (cusp excursions) | [P] | proved |

**Changed earlier claims (explicit state review, referee tables):**
* **BGS-TRACE-244 (OP): open → proved [P + CA].** (OP_k, δ) holds for the four k1 lattice-lifted families at the certified (k, ρ, β),
  δ ≈ 0.0162 for (±2,8)V (Lemma O1, Theorem OP_abs, certificate: BGS-TRACE-249, 250, 251).
* **BGS-TRACE-245 (Theorem W): conditional → proved [P + CA].** The OP condition is dropped (BGS-TRACE-244 is proved). Still relative to the
  standing inputs: for m = 3p ∈ S⁺, m ≥ m₁ (effective, not computed), c_W = 10^−25.62, q₀ = 10^13.2. **No explicit p₀ is claimed.**
* **BGS-TRACE-246 (K2′): conditional → proved [P + CA],** same inputs, for m ≥ m₁ (effective, not computed). Caveat (Prop S,
  BGS-TRACE-258): K2′ is true, but it is not a refutation route for the m covered by Prop S.
* **BGS-TRACE-247 (Conjecture C1) stays open.** Theorem U (BGS-TRACE-254) is its exact L² version and does not imply it; OP is now proved
  without C1.
* **BGS-TRACE-206 (frozen R′) stays OPEN.** Nothing here refutes it: the refutation is reduced to H_mean (BGS-TRACE-256, open).

## 1. Setting

As in BGS-TRACE-206 and the Line K note (`lineK_harg_removal.md`): k1 kick 0.9 cos 2πq at η = 2 (ĝ(n) = iⁿJ_n(1.8)), S = [[3,4],[2,3]],
λ = 3 + 2√2 (minimal polynomial X² − 6X + 1), frozen definition P* = {(2,8),(−2,8),(2,16),(−2,16)}, m = 3p, S⁺, O♮_m, ξ_lo = 2.4586893,
μ* = 1.9154712, targets 1.28359 ((±2,8)) and 1.4742 ((±2,16)). Families: the true lattice-lifted operators of Line F/J
((L_τΦ)_c(s) = Σ_n w(n)e(nτ)e(κns)·ω(c)/ω(f_n(c))·Φ_{f_n(c)}((s+n)/λ), κ = C0 or C0/2, vertex discs of radius ρ (V) or edge discs (E) on
H², weights ω(c) = e^{−β|c|}). The β-weighting is a diagonal conjugation on lattice sites: traces are unchanged and it commutes with J = I
and J = I⊗J_B (referee F4).

## 2. OP without cancellation (BGS-TRACE-248..252)

**Collision structure [P] (BGS-TRACE-248).** α_v := Σ_j v_jλ^j = 0 ⇔ v(X) = (X² − 6X + 1)E(X); the coefficients e_j of E are carries,
v_j = e_j − 6e_{j−1} + e_{j−2}, and |e_j| ≤ C0g·Σ_i|v_i|λ^{−|j+1−i|} with C0g = 1/(λ − λ^{−1}). So the collision sum S_k is a transfer-matrix
sum over carry states.

**Lemma O1 [P] (BGS-TRACE-249).** For a k-word w, ‖M_w‖_HS ≤ |Φ̂_w|·Π_j e^{τ_j|n_j|}·(1−θ²)^{−1/2}·(NS·coth(β(1−λ^{−k}))·e^{2β(dev+1)})^{1/2},
τ_j = 2πκρλ^{−j} + βλ^{−(k−j)}, **j = 0 the outermost letter** (essential: the referee stress test gives max HS/bound 0.287 with this
assignment and 93.8 with it reversed); θ = (ρλ^{−k} + dev)/ρ < 1, dev_V = λ/(2(λ−1)) = 0.6036, dev_E = 1/(2(λ−1)) = 0.1036; the "+1" is slack
for V and **needed** for E (1.1036 ≥ 0.6036 covers the site drift); NS = 64 internal states for L16.

**Theorem OP_abs [P] (BGS-TRACE-250).** With f_k(y) = ‖P_k(y)‖²_HS = Σ_γ c_γ e(Tr γy): I_k = c_0 ≤ C_pair·S_k,
S_k = Σ_{α_v=0} Π_j ρ_j(v_j), ρ_j(d) = Σ_a|J_a||J_{a−d}|e^{τ_j(|a|+|a−d|)}, and A_k = Σ_{γ≠0}|c_γ| ≤ C_pair·Π_j A(τ_j)², A(s) = Σ_a|J_a(1.8)|e^{s|a|}.
No cancellation is used (Cauchy–Schwarz for the HS pairing).

**Certificate [CA] (BGS-TRACE-251)** (`code/l3_op_cert.py`, `code/l4_const.py`, `logs/final_op_cert.jsonl`, `logs/final_constants.jsonl`):
S_k ≤ S_box (exact arb enumeration over carries |e_j| ≤ 6) + Chernoff tail (t = 2, ≤ 2.5·10⁻¹⁴); Bessel values in arb with a factorial tail.

| family | k | ρ | β | I_k ≤ | I_k^{1/2k} ≤ | target | δ_OP = 1 − rate/target |
|---|---|---|---|---|---|---|---|
| (±2,8) V | 15 | 0.75 | 0.25 | 1095.97 | **1.26278** | 1.28359 | **0.0162** |
| (±2,8) E | 14 | 0.20 | 0.30 | 35.90 | 1.13642 | 1.28359 | 0.115 |
| (±2,16) V | 14 | 0.90 | 0.30 | 10608.6 | 1.39243 | 1.4742 | 0.055 |
| (±2,16) E | 14 | 0.20 | 0.30 | 1645.2 | 1.30276 | 1.4742 | 0.116 |

Rates at smaller k are not certified with these constants (e.g. (±2,8)V at k = 14: 1.2858 > target). The integrator reran the four final
cases in a scratch copy (paths repointed): output identical except timing (evidence §INTEGRATION).

**T_k bound and constants [P + CA] (BGS-TRACE-252).** |N(α_v)| ≤ ((aX + Y/a)/2)², X = Σ|v_j|λ^j, Y = Σ|v_j|λ^{−j}, a = λ^{−(k−1)/2}; hence
T_k(q) ≤ C_pair·e^{−2s√q}·Π_j A(τ_j + s(aλ^j + λ^{−j}/a))² for every s > 0, evaluated in arb on a grid. Per family δ_F = (1 − rate_F/target_F)/2 = δ_OP/2
(0.00811 for (±2,8)V), η_F = (((1 − δ_F/2)target_F)^{2k} − I_k)/3, c_F = (η_F/(6A_k))², log₁₀ c_F = −25.62 / −20.93 / −22.53 / −20.84,
log₁₀ q₀ = 13.2 / 12.3 / 12.3 / 12.2. **c_W := 10^−25.62 ≤ min_F c_F, q₀ := 10^13.2.** The Weil range q ≤ c_W p² is non-vacuous
(c_W p² ≥ 2p + 1) only from p ≈ 2/c_W ≈ 8.3·10²⁵ (the report rounds to 8.2·10²⁵).

## 3. Theorem U (BGS-TRACE-254)

**Lemma U1 / Theorem U [P].** R(v) := Σ_n w(n)·conj w(n−v) = e(ν₀P(v)/2h)·Π_jκ(v_j, θ_j), κ(d,θ) = Σ_aĝ(a)conj ĝ(a−d)e(−aθ),
θ_j = ν₀y′Tr(λ^{−j}α_v)/(2h). If α_v = 0 or α_v ∈ hO then all θ_j ∈ Z and κ(d,0) = i^d J_d(0) = δ_{d,0} (Neumann/Graf addition theorem),
so R(v) = δ_{v,0}Σ|w|². Hence Σ_{x∈O}|A(x)|² = 1 and Σ_{β mod h}|Ẑ(β/h)|² = h². At a level q | h the analogous sum is **not** 1 (the twist sits
at h/q). Theorem U is the exact L² statement behind Conjecture C1 (BGS-TRACE-247); **it does not imply C1** and controls no individual level.
Referee caveat: the congruence form of the TRACE-206 phase P(n) (the ψ_d coefficients) is taken as given (supported numerically, [N] at
m = 5, 7, 9).

## 4. Theorem W and K2′ without OP (BGS-TRACE-245, 246)

W2′ is used in its bounded-J form (BGS-TRACE-242; W-F7, in `computations/verification/lineK/K2/REPORT_K2_v2.md` §8; REPORT_L_v2 cites a
local copy `K2/REPORT_K2_v3.md`, which is not in the repository; the content is the same). It is applied family by family, so k may depend
on F. **Theorem W:** under the standing inputs, there is an effective (not computed) m₁ such that for every m = 3p ∈ S⁺ with m ≥ m₁ (in
particular 2p+1 ≥ q₀) the total cross part of all conductors c ∈ {q, 7q} (q prime, q | h_m, q ≤ c_W p²), including inherited copies, is
o(ξ_lo^m); c_W = 10^−25.62, q₀ = 10^13.2. **K2′:** for m = 3p ∈ S⁺, m ≥ m₁ (effective, not computed), frozen R′ implies a slow λ-orbit at
an open conductor c ∉ {1, 7} ∪ {q, 7q : q ≤ c_W p²}, c < L_m (for (±2,16), c < (1.6677²/ξ_lo)^{m(1+η)}). Caveat: by Prop S (§6) the
conclusion holds anyway at the m covered there, so K2′ is not a refutation route for them.

## 5. (±2,16) narrowing (BGS-TRACE-253) [P + CA]

With d ≤ |Z|/(2√m) and positivity absorption (Prop K2 with Λ₁₆ = log(1.6677²/ξ_lo) and the (±2,16) constant C ≤ 3.8·10⁻²⁵ in place of
S_Z), the (±2,16) levels are absorbed for q ≥ (1.6677²/ξ_lo)^{m(1+η)}, η = η_m^{(16)} ≤ (0.4043/Λ₁₆ + 1)/log(2p+1) + O(log ℓ/m) =
(4.282 + o(1))/log(2p+1). **Integration note:** 1.6677²/ξ_lo = 1.13118… and Λ₁₆ = 0.12326; the reports quote 1.1311 and 0.12319 (rounded
down, which slightly understates the open range). The claim is registered in the exact form; 4.282 remains valid (0.4043/0.12326 + 1 =
4.27999). For (±2,8) there is no narrowing (L_m = 1.4923^{m(1+η_m)}).

## 6. L2: what has to be bounded (BGS-TRACE-255..258)

**Decomposition [P] (BGS-TRACE-255).** ℓ(𝔞) ⊂ O/q the annihilator of 𝔞 ⊇ qO; A(𝔞) = [O:𝔞]^{−1}Σ_{β∈ℓ(𝔞)}Ẑ_β;
D_𝔮 := A(𝔮) − A_tot/q = (1/q)Σ_{β∈ℓ(𝔮)∖0}Ẑ_β; D_iso = D_𝔮 + D_𝔮̄ − (A(qO) − A_tot/q²); A(qO) − A_tot/q² = (1/q²)Σ_{β≠0}Ẑ_β. With
Theorem K1 (BGS-TRACE-237) the level contributes 2Re(conj Z_ρ·(D_iso − E_b/q)): averages over β, not per-β bounds.

**H_mean (open, BGS-TRACE-256).** For some δ > 0 and infinitely many m ∈ S⁺: |D_iso(q) − E_b(q)/q| ≤ ((1−δ)·target)^m at every open prime
level q, together with the analogue at open composite levels.

**H_mean ⇒ frozen R′ refuted [P] (BGS-TRACE-257).** By Theorem K1, Prop K2 and Theorem W the open part of O♮ is then o(ξ_lo^m), so
H♮_mid holds along these m and the proved implication of Theorem K (BGS-TRACE-240; see §1, standing inputs) refutes frozen R′. This is an implication; H_mean is not proved.

**Prop S [P, given the Line F spectral data ρ₀ ≥ μ*] (BGS-TRACE-258).** For the (±2,8) family F with k = k_F there is C_k (effective, not
computed) such that β = 1 is slow at every prime q ∥ h_m with log_λ q ≥ C_k + r(T/ρ₀)^{2k}, T = (1−δ/2)·1.28359; C_k = log_λ(2/ε_k) + k/2 + 1.
The number of good blocks is **min(r, 2I − k + 2)** (indices cyclic mod r; referee nit). With k = 15, (1.28359/1.9154712)^30 = 6.09·10⁻⁶ ≤
6.1·10⁻⁶ and r ≤ m, the threshold is log_λ q ≥ C_k + 6.1·10⁻⁶·m. **Consequence [P] (L2-F4 wording):** for every m ∈ S⁺ such that h_m has a
prime q ∥ h_m in (max(c_W p², λ^{C_k + 6.1·10⁻⁶·m}), L_m), the conclusion of K2′ holds without assuming frozen R′, so K2′ gives no contradiction at
such m. That this covers all or most m is **[H]** (not registered).

## 7. L2: cancellation-free and height methods (BGS-TRACE-259..262)

**Lemma A1 [P] (BGS-TRACE-259).** Σ_{β∈ℓ(𝔮)}|Ẑ_β|² = q·Σ_u|A(u+𝔮)|²; |D_𝔮|² ≤ (1 − 1/q)C_𝔮, C_𝔮 = Σ_u|A(u+𝔮)|² − |Z|²/q
= 1 + Σ_{α_v∈𝔮∖0}R(v) − |Z|²/q (exact collisions contribute 0 by Theorem U).

**Prop A2 [P + CA] (BGS-TRACE-260).** Any phase-blind collision bound is ≥ Σ_uM(u)² ≥ G^{2m}/q, G = Σ_n|J_n(1.8)| = 2.3693986 [CA]; it
certifies |D_𝔮| ≤ T^m only for q ≥ (G/T)^{2m} = 3.4074^m ((±2,8)) or 2.5832^m ((±2,16)). **L2-F1:** h_m ≈ ½·2.4142^m (so √h ≈ 1.5538^m); both
thresholds exceed h_m itself, so no level dividing h_m qualifies.

**Lemmas B1–B3 [P] (BGS-TRACE-261)** (stated for **split** q; for inert q the lattice has index q² and B2 gives ‖F‖_∞ ≤ q^{2/r}).
B1: F ∈ Z^r, F(λ) ∈ 𝔮∖0 ⇒ q ≤ 1.4571·λ^{r−1}·‖F‖²_∞ ((λ/(λ−1))² = 1.45711). B2: Λ_𝔮 has index q, so it contains F ≠ 0 with ‖F‖_∞ ≤ q^{1/r}
(Minkowski); for q < L_m, r ≥ p: q^{1/r} < 3.3233^{1+η}. **L2-F2:** "height ≤ 4 sporadic collisions exist" needs 3.3233^{1+η} < 5, i.e.
η < 0.340 (large p only); such F is genuinely sporadic: a nonzero F with ‖F‖_∞ ≤ 4 cannot vanish at λ (Cauchy root bound: roots have modulus
< 5 < λ = 5.83). B3: summing over the prime ideals above h, Σ_𝔮 log N𝔮 (Coll^{abs}_𝔮 − exact) ≤ (1 + o(1))·m log λ·G^{2m}.

**Disjointness [P] (BGS-TRACE-262).** The height argument excludes sporadic collisions only for q > 1.457·λ^{p−1}H² (growth λ^{m/3} =
1.7996^m). (±2,8): 0.40030(1+η_m) < 0.58758 ⇔ η_m < 0.4678, true for all large p (η_m ≤ (2.010 + o(1))/log(2p+1)). (±2,16):
η^{(16)} < 3.77 (exact Λ₁₆: 3.767), true **for all sufficiently large p** (L2-F3; the bound carries o(1) and O(log ℓ/m) terms). So for large p
the height zone does not meet (c_W p², L_m); the height argument closes no part of the open range.

## 8. L3: the structural/recursive route (BGS-TRACE-263..268)

Errata L3-F1–F4 applied at integration (§6 of `L3/REPORT_L3.md`). Notation of BGS-TRACE-254: w(n) = Φ̂(n)e(−ν₀P(n)/2h).

**S1 [P] (BGS-TRACE-263).** From P(n) = y′·Nm(α_n) − 2h·Σ y_{|i−j|}n_in_j (TRACE-212): w(n) = Φ̂(n)χ(α_n), χ(x) = e(−ν₀y′Nm x/2h)
(2hO-periodic), A = χ·B_m with B_m(x) = Σ_{α_n=x}Φ̂(n), and B̂_m(y) = Π_{j<m} g(Tr λ^j y), g(t) = e^{i·1.8 cos 2πt} (Jacobi–Anger), so
|B̂_m| ≡ 1 (the Fourier side of Theorem U).

**S2 [P] (BGS-TRACE-264, after L3-F1).** For an odd prime q ∥ h, M′ = 2h/q (even, ≡ 2 mod 4), aM′ + bq = 1: χ splits into a level-q and a
level-M′ factor, the level-q factor is 1 on 𝔮 ∪ 𝔮̄, and A(𝔮) = Σ_z F̂(z)B̂_m(z/2h) with F = 1_𝔮 ⊗ ψ′ (characters indexed by O^∨).
|F̂_{M′}| = 2/M′ on M′²/4 points, Σ|F̂_{M′}| = M′/2, so |A(𝔮)| ≤ h/q and |D_𝔮| ≤ h/q + |Z|/q ≤ 2h/q **when |Z| ≤ h** (true for m ≥ 495 by
Prop K2's Z-bound, μ = 1.9155 < 1 + √2; case by case below). This gives |D_𝔮| ≤ T^m only for q ≳ (λ^{1/2}/T)^m = 1.8808^m, above
L_m = 1.4923^{m(1+η_m)} once η_m < 0.578 (all large p).

**S3 [P] (BGS-TRACE-265, after L3-F2).** h_{3p} = h_p(4h_p² + 3) (V_{3n} = V_n³ + 3V_n, V = 2h, odd n), gcd(h_p, K_p) | 3 with
K_p = 4h_p² + 3; every prime of K_p other than **7 (rank 3)** has rank 3p (exceptions divide 2h_1 = 2 or 2h_3 = 14); 7 | K_p for p = 5…23.
By S2 the phase has a factor at level K_p where λ^p ≢ 1, so the Gauss side does not fold to m = p (B_{3p} ≡ B_p^{∗3} only mod 2h_p).
Lean checks the finite instances p = 5…23.

**S4 [P given the Line G/I transfer law] + [N] (BGS-TRACE-266).** If r(q) = p the twists have period p, and the Line G/I transfer law
(BGS-TRACE-203, 216) gives Ẑ^{(3p)}_β = c_{3p}·Tr_K[(I_K ⊗ ⟨1|)Π_β³(I_K ⊗ |0⟩)], Π_β the p-step twisted operator built with the m = 3p
automaton constants. [N] error ≤ 1.7·10⁻¹³ at (5, 41) and (7, 239).

**Lemma Q [P] (BGS-TRACE-267).** For absolutely convergent F(y) = Σ_γ c_γe(Tr γy) and a degree-1 prime 𝔮 | q:
(1/q)Σ_{β∈ℓ(𝔮)}F(β/q) = Σ_{γ∈𝔮}c_γ. For F = f_k the isotropic-line mean block energy lies in [I_k − T_k(q), I_k + T_k(q)], with no Weil input
and no upper limit on q. (The Remark on Hölder decoupling is [H], L3-F3.)

**Lemma E [P] (BGS-TRACE-268).** For 0 < ε ≤ 1/16 and β ≠ 0 in O/q with dist(Tr(βλ^j)/q, Z) ≤ ε for k ≥ 3 consecutive j:
λ^{k−1} ≤ 264ε²q if β is isotropic, and λ^{k−1} ≤ 264ε²q² for every β ≠ 0. At ε = 0.05: isotropic runs ≤ log_λ q + 0.76,
others ≤ 2log_λ q + 0.76.

None of S1–S4, Lemma Q, Lemma E closes the open range; H_mean (BGS-TRACE-256) stays open.

## 9. Notes only (not registered)

* [N] r_abs = 1.0511 (spectral radius of the absolute collision automaton; `code/l2_rabs.py`), so r_abs^{1/2} ≈ 1.025.
* [N] Theorem U checks (m = 5, h = 41: level-h Parseval to 3·10⁻¹¹; referee m = 7, 9).
* [N] L2 level survey (`L2/logs/iso_survey.jsonl`, `L2/logs/full_level.jsonl`): 23 isotropic cases (m = 15..183, q ≤ 19609) and 6 full
  levels (m ≤ 51, q ≤ 239), only (2,8) and (−2,8); worst full K1 rate |D_iso − E_b/q|^{1/m} = 1.178 < 1.28359 at (21, 239). (±2,16) not
  tested; extrapolation from m ≤ 51 is not reliable.
* [H] The deficit identity of REPORT_L_v2 §5(d) (not proved, not P-checked, used nowhere); the slow-orbit model ("inherited levels
  harmless"); "Prop S covers most m".
* [assessment] The negatives of REPORT_L_v2 §5(a), (c), §6 (global identities and the large sieve do not isolate a level; the "real wall"
  is equidistribution on subgroups of logarithmic size) and of REPORT_L2 §0.6, §5 (signed sporadic-collision reformulation; Weil, BGK,
  large sieve, phase-blind counting, height and per-β bounds do not close the open range).
* [N] L3: S4 spectral identity to ≤ 1.7·10⁻¹³ at (p, q) = (5, 41), (7, 239); |Ẑ^{(p)}_β|³ does not track |Ẑ^{(3p)}_β|; rank-p vs full-rank
  level behaviour; Lemma E run lengths (`L3/logs/`).
* [H] L3: the Lemma Q Remark (Hölder ⇒ positivity threshold); the cost bound G^{3p}/q (no precise class of bounds stated).
* [assessment] L3: "the structural route is blocked"; Reasons 2–3 for inherited levels; "iterating the CRT is not a descent"; H_mean is an
  equidistribution statement beyond the Ehrenfest time; by analogy with Faure–Nonnenmacher–De Bièvre (CMP 239, 2003), principles valid
  for all cat-map quantizations at minimal period cannot suffice, and kick-specific input seems necessary (L3-F4 wording).

## 10. Lean

`formalization/Bgs/LineLConst.lean` (namespace `Bgs.LineL`, in `lake build Bgs`, core `decide` on natural numbers, no `native_decide`, no
`sorry`; `#print axioms` shows no axioms) checks scaled integer forms of: (L3) h_{3p} = h_p(4h_p² + 3), gcd(h_p, K_p) = 1, 7 ∣ K_p for p = 5…23, 49 ∣ K_7 and (1+√2)/1.28359 ≥ 1.8808; (L, L2) (1.28359/1.9154712)^30 ≤ 6.1·10⁻⁶ (Prop S); the certificate upper
ends < targets and δ_OP(8V) ≥ 0.0162; (G/T)² ≥ 3.4074 and ≥ 2.5832 from the arb lower bound G ≥ 2.3693985; 2.5832 > 1 + √2 and the h_m values
h_9 = 1393, h_21 = 54608393 (L2-F1); (λ/(λ−1))² ≤ 1.4572 and λ > 5 (B1, Cauchy bound) from 1.4142135 < √2; 1.4923³ ≤ 3.3234 (B2). The arb
certificates, the analytic lemmas and the Bessel sums are not formalised.
