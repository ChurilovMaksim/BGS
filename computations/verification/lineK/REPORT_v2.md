# Line K report v2: towards an unconditional refutation of frozen R′ (TRACE-206)

v2 (31 Oct 2026, UTC+5) applies the referee report `/workspace/audit/lineK/REPORT.md` (verdict: all items ACCEPT AFTER FIXES). REPORT.md (v1, sha 8fc2e9f1…) is kept unchanged. The changelog is in §7. New work after Line K (Theorem W etc.) is in `K2/REPORT_K2.md`, not here. Nothing was pushed.

Labels:
- **[P]** proved by hand;
- **[P-check]** exact or high-precision verification of a finite identity;
- **[CA]** computer-assisted, rigorous (arb or exact integer);
- **[N]** floating-point numerics;
- **[H]** heuristic or interpretation;
- **[assessment]** an opinion on a strategy.

## 0. Summary

1. **H_arg is removed [P + CA].** S⁺ ∩ {3p : p ≡ p₀ (mod 56)} is infinite for every p₀ ∈ (Z/56)*, **unconditionally** (§1). The proof is a case split on an unknown fact:
   - arg ξ/2π irrational: Vinogradov;
   - rational a/b: b ≥ 1339 by J3 `rat_excl` [CA], then the gap lemma K3 and Dirichlet with CRT.

   No density is claimed in the rational case.
   - **Corollary K3 [CA]**, via Theorem J/J3 with Lemma L16 *accepted* in the Line J audit (DELTA3 §D3.3): frozen R′ ⇒ φ⁻¹O♮_m ≤ −0.99K_j·1.0184224^m + 4m + o(m) on an infinite set of m = 3p. So **frozen R′ is false under H♮ alone**. Unconditionally, frozen R′ forces exponential cancellation of D7 by conductor-∉{1,7} parts on an infinite set of m = 3p.
2. **Theorem K1 [P; exact P-check]:** the light-cone identity at prime levels q ∥ h, q ≡ ±1 (mod 8). The congruence is automatic for q | h_m. The level-q cross part depends only on the push-forward of the word mass under x ↦ N(x) mod q (§2).
3. **Prop K2 [P + CA]:** levels d ≥ L_m are absorbed by positivity, with the explicit constant S_Z ≤ 0.5000001 (m ≥ 495) extracted from Line F and the J3 §1 certificates. Here P* = {(±2,8), (±2,16)} (TRACE-206 frozen mask), L_m = (μ*²/ξ)^{m(1+η_m)} and η_m ≤ (2.010 + o(1))/log(2p+1) (s = 1/ℓ; optimised constant ≈ 1.988).
   - **K2 is vacuous for m below ≈1.68·10⁹ [N, bisection]:** there, no included level satisfies d ≥ L_m, and O♮^{<L} := O♮.
4. **K4 [N, toy only]:** block operator-norm rates of a toy single-disc Galerkin along cat-map orbits fall below 1.2836 from k ≈ 30. **Nothing about the range q ≤ p^C is proved.** All of d < L_m is open. Toy numerics suggest the small-q part is benign *if* a BGK-type equidistribution input holds [H], and *if* the toy reflects the true two-disc operators (unverified).
5. **Not achieved:** an unconditional proof of H♮, or of any substitute. Theorem K (§5) gives frozen R′ false under **either** H♮ (Corollary K3) **or** the *alternative* sufficient hypothesis H♮_mid. H♮_mid is not a weakening of H♮: neither implies the other (§5).

## 1. Removal of H_arg [P + CA]

**Lemma K3.** Let A = arccos(0.84431)/π (arb lower bound 0.18001064843). For every b′ ≥ 447 with b′ ∉ {504, 560, 616, 840}, and every unit class r mod g′ = gcd(56,b′), the set V(b′,r) = {v mod b′ : gcd(v,b′) = 1, v ≡ r (mod g′)} has maximal cyclic gap < A·b′.

*Proof.*

**(a) Exact enumeration, 447 ≤ b′ ≤ 6000 [CA, exact integers].** `code/k3_harg.py`, re-verified by the referee in exact rationals (`audit/lineK/ref/ref_k3.py`).
- Only b′ ∈ {504, 560, 616, 840} fail.
- Every other b′ in the range has maximal gap ≤ b′/6. The smallest margin is A − 1/6 = 0.01334, at b′ = 672 (referee).

**(b) Sieve for all b′ [P].**
- *Setting.* Let n′ be the part of b′ coprime to g′, R = rad n′ and k = ω(R). Write v = r + g′t.
  - The primes 2 and 7 of b′ divide g′, and r is a unit mod g′, so they never divide v.
  - Hence v is admissible iff gcd(r + g′t, R) = 1. This condition is periodic in t mod R, and R | b′/g′.
  - So the cyclic gap of V(b′,r) in v equals g′ times the periodic gap in t.
- *Count.* By inclusion–exclusion over e | R, any X consecutive t contain at least Xφ(R)/R − (2^k − 1) admissible t. Each of the 2^k − 1 non-trivial terms has rounding error < 1, and the e = 1 term is exact.
- *Gap.* Let t₁ < t₂ be consecutive admissible values. The t₂ − t₁ − 1 values strictly between them contain none, so (t₂ − t₁ − 1)φ(R)/R − (2^k − 1) < 1, i.e. t₂ − t₁ − 1 < 2^k R/φ(R). Hence t₂ − t₁ ≤ X_t := ⌊2^k R/φ(R)⌋ + 1 ≤ F + 1, where F = Π_{ℓ|R} 2ℓ/(ℓ−1).
- *Failure condition.* If g′X_t ≥ A·b′ ≥ A·g′R, then F + 1 ≥ A·R, i.e. Π_{ℓ|R} 2/(ℓ−1) ≥ A − 1/R.
  - A prime ℓ ≥ 23 makes this impossible (2/22 < A − 1/23).
  - Enumerating the subsets of {3, 5, 11, 13, 17, 19} (redone by the referee in exact ℚ) leaves ∅, {3}, {5}, {11}, {13}, {17}, {3,5}, {3,11}, {3,13}. For each, b′ ≤ 56(F+1)/A ≤ 2644.3.
  - So every failure has b′ ≤ 2645, which is inside the exact range. ∎

**Theorem K3 [P + CA].** For every p₀ ∈ (Z/56)*, S⁺ = {m = 3p : cos(arg B_j + m·arg ξ) ≥ 0.84431} contains infinitely many m = 3p with p ≡ p₀ (mod 56).

*Proof.*
- **Irrational case:** Vinogradov (J3 v2 §5; density 0.18001).
- **Rational case:** arg ξ/2π = a/b in lowest terms.
  - J3 `rat_excl` [CA] gives b ≥ 1339 (simplest fraction in the enclosure: 1189/1339).
  - Put b′ = b/gcd(3,b) ≥ 447 and a′ = 3a/gcd(3,b). Then gcd(a′,b′) = 1 and m·arg ξ/2π ≡ a′p/b′ (mod 1).
  - **CRT.** The congruences p ≡ p₀ (mod 56) and p ≡ v (mod b′) are compatible iff v ≡ p₀ (mod g′). The joint class is a unit mod lcm(56,b′) iff gcd(v,b′) = 1. So by Dirichlet, every v ∈ V(b′, p₀ mod g′) is hit by infinitely many primes p ≡ p₀ (mod 56).
  - **Phases.** The phase set is {a′v/b′ : v ∈ V(b′,r)}, r = p₀ mod g′. As sets, a′·V(b′,r) = V(b′, a′r), because multiplication by the unit a′ permutes the units mod b′ and maps the class r mod g′ onto a′r mod g′. Lemma K3 holds for every unit class, so this set has all cyclic gaps < A·b′ and therefore meets every closed arc of length A, in particular the arc {x : cos(arg B_j + 2πx) ≥ 0.84431}.
  - **Exceptions.** For b′ ∈ {504, 560, 616, 840}, the candidate denominators are b ∈ {b′ (if 3 ∤ b′), 3b′} = {1512, 560, 1680, 616, 1848, 2520}. None has a fraction in the outward-rounded enclosure [0.88797591, 0.88797627] of arg ξ/2π. This is an exact `Fraction` test, rechecked by the referee for all nearby numerators. 560 and 616 are excluded anyway by b ≥ 1339.
  - **Remaining conditions.** B_j is constant on the class p₀, since j = 3p mod 168. m ≥ M0(j) holds for p large. ∎

**Corollary K3 [CA].** Assume Theorem J/J3 (Lemma L16 accepted). Then frozen R′ ⇒ φ⁻¹O♮_m ≤ −0.99K_j·1.0184224^m + 4m + o(m) for infinitely many m = 3p (for each p₀). So H♮ alone refutes frozen R′.

## 2. Theorem K1: the light-cone identity [P; exact P-check]

**Setting.**
- q ≠ 7 is prime, q ∥ h_m, and **2 is a square mod q** (q ≡ ±1 (mod 8)). This is automatic for q | h_m, since 2y′² ≡ 1 (mod q) (J3 §3). Then qO = 𝔮𝔮̄ splits.
- For a word w, let x_w = Σ_i n_iλ^i ∈ O/q.
- Grouping words by x_w is legitimate: the series is absolutely convergent, Σ_w|c_w|(‖V_w‖₁ + ‖E_w‖₁) < ∞ by L16 step 3 / Line F, and the automaton read-outs have modulus ≤ 1. This gives Ẑ_β = Σ_x A(x)e(Tr(βx)/q) with A_tot = Ẑ_0.

**Theorem K1.** Σ_{β≠0} Ẑ_β W_{q,β} = D_iso − E_b/q, where:
- D_iso = A(𝔮 ∪ 𝔮̄) − ((2q−1)/q²)A_tot;
- E_b = Σ_x A(x)e(−N(x)t_b/q) − A_tot/q;
- t_b is the missing label.

*Proof.*
1. By J3 §3, W_{q,β} = q⁻²Σ_{t∈F_q*, t≠t_b} e(N(β)t̄/q).
2. With u = t̄: uN(β) + Tr(βx) = uN(β + x̄/u) − N(x)t. The Gauss sum is Σ_β e(uN(β)/q) = G(u)G(−2u) = (−2/q)(−1/q)q = (2/q)q = q. **This uses (2/q) = +1.**
3. Summing over t ≠ t_b, with Σ_{t∈F_q*} e(cN(x)t/q) = q·1_{N(x)=0} − 1:
   Σ_{all β} Ẑ_βW_{q,β} = q⁻¹Σ_x A(x)[q·1_{N(x)=0} − 1 − e(−N(x)t_b/q)].
4. The β = 0 term is A_tot·W_{q,0} = **(q−2)A_tot/q²**. Subtract it and use #{N(x) ≡ 0} = 2q − 1. ∎

**Checks.**
- [P-check] Author: `code/k1_cone_check.py`, random complex A, 40 digits, q = 7, 17, 23, 31; error ≤ 2·10⁻³⁹.
- Referee: `audit/lineK/ref/ref_k1_exact.py`. Exact in Z[ζ_q] for every δ-mass and every t_b, q = 7, 17, 23, 31, 41, 47: 0 mismatches out of 214,240 cases.
- Control: q = 11 and 13 (2 not a square) fail in every case, so the hypothesis is necessary.

**Exact reformulation [P].** D_iso and E_b depend on A only through its push-forward A_N(u) := Σ_{N(x)≡u} A(x), u ∈ F_q. So the level-q cross part vanishes iff A_N satisfies D_iso = E_b/q.

**Interpretation [H] (not proved).**
- x_w ∈ 𝔮 ⇔ the folded polynomial Σ_s N_s ℓ^s vanishes at ℓ = λ mod 𝔮, of order r(q) ∈ {p, 3p}.
- One may speak of "trivial" zeros (all N_s equal) and "sporadic" zeros (q | Norm). It is *not* proved that trivial zeros are exactly the words with x_w ∈ ∩𝔮, nor that sporadic zeros are unavoidable for q ≲ C^p.
- E_b is bounded a priori only by the total-variation mass Σ_x|A(x)|, so it is not negligible a priori. "H♮ at prime levels ⇔ equidistribution on 𝔮 ∪ 𝔮̄" is therefore only an interpretation.

## 3. Prop K2: large levels by positivity [P + CA]

**Frozen primaries.** P* = {(2,8), (−2,8), (2,16), (−2,16)} (N ≡ ±4, ±8). Sources:
- the TRACE-206 text, `mathematics/fixed-map/resonance_classification_lineG.md` line 107, repo commit fa172e82;
- Line I implementation `bgs-lineI/code/base.py`, `PSTAR['k1']`.

**Z-bound [CA]** (`code/k2_SZ.py`, `logs/k2_SZ.json`). For m ≥ 495, |Z_ρ(m)| ≤ C_ρ μ^m with μ = 1.9154753:
- **(±2,8), Line F:** Z = c_m(c^f μ*^m + ε), |c^f| = ½, |ε| ≤ H₀ = 1506.18, |c_m| ≤ 1 + λ^{−m}. Hence C ≤ (1 + λ^{−495})(½ + 1506.18·1.9154712^{−495}) ≤ 0.5000001.
- **(±2,16), J3 §1 + L16:** per operator case, the sum over the 8 blocks and V/E of ½‖T‖₁·fullR/(1−F)·R^m. R ≤ 1.6677, and the coefficient sum is ≤ 2.273·10⁵. Since (1.6677/μ)^{495} is tiny, the effective C ≤ 3.8·10⁻²⁵.
- **Result:** S_Z = Σ_ρ C_ρ² ≤ 0.5000001.

**Proposition K2 [P + CA].** For m = 3p ≥ 495 and every included d, Dev_d(ρ) ≥ −n_d|Z_ρ|²/d² ≥ −|Z_ρ|²/d (n_d ≤ φ(d) < d). Let w = ⌊log h_m / log(2p+1)⌋ ≥ (number of prime factors ≠ 7 of h_m, with multiplicity), using the rank lemma and 49 ∤ h. Then, for every s ∈ (0,1),
Σ_{d|h, d≥L} 1/d ≤ L^{s−1}(1−7^{−s})^{−1}(1−(2p+1)^{−s})^{−w}.
Hence Σ_{ρ, d≥L} Dev_d ≥ −0.01(K_min/2)ξ_lo^m whenever log L ≥ L*(m) := min_s [E(s) − T_m]/(1−s), where:
- E(s) = −log(1−7^{−s}) − w·log(1−(2p+1)^{−s});
- T_m = log(0.01K_min/(2S_Z)) − mΛ, with Λ = log(μ²/ξ_lo) = 0.40030.

**η_m = O(1/log m) [P].** Let ℓ = log(2p+1) and take s = 1/ℓ, so (2p+1)^{−s} = e^{−1}.
- w ≤ m·log(1+√2)/ℓ = 0.8814m/ℓ.
- 1 − 7^{−s} ≥ s·log 7/2 for s ≤ 1/2, so −log(1−7^{−s}) ≤ log(2ℓ/log 7) = O(log ℓ).
- Therefore E(s) ≤ O(log ℓ) + (0.8814m/ℓ)·log(1/(1−e^{−1})) = O(log ℓ) + 0.4043m/ℓ.
- With κ₀ = −log(0.01K_min/(2S_Z)): log L_m/m ≤ (Λ + 0.4043/ℓ + (O(log ℓ) + κ₀)/m)/(1 − 1/ℓ) = Λ(1 + η_m), where η_m ≤ (0.4043/Λ + 1)/ℓ + O(log ℓ/m) = (2.010 + o(1))/log(2p+1).
- Numerically [N], with the optimised s: η·log(2p+1) = 2.77, 2.39, 2.19, 2.13, 2.11 at m = 501, 3027, 3·10⁵, 3·10⁷, 3·10⁸. These decrease toward the optimal asymptotic constant min_c[c + 2.2018·(−log(1−e^{−c}))] ≈ 1.988 (at c ≈ 1.164, s = c/ℓ). The proven 2.010 is the bound for the particular choice s = 1/ℓ (`code/k2_large_v2.py`).

**Non-vacuity [N].** K2 is non-empty iff L_m < √h_m. With S_Z ≤ 0.5000001, continuous s, and the *lower* bound h_m ≥ ((1+√2)^m − 1)/2, bisection gives a crossover at **m ≈ 1.682·10⁹** (m ∈ [1.6821, 1.6823]·10⁹). The referee independently got [1.672, 1.683]·10⁹.
- For m below this, K2 changes nothing: O♮^{<L} = O♮. The table values l = L^{1/m} and the √h rate are floats taken from arb endpoints [N].

**Compatibility with J3** (referee-checked):
- levels d ≥ L are absorbed whole;
- for d < L the X7 copies keep A^{<L} ≥ 1 (level 7 < L);
- |X16^{<L}| ≤ |X16| (positive multiples);
- Q^{<L} ≥ 0.

## 4. K4: toy numerics [N] and the BGK route [H]

**Setup.**
- Along a prime level, a k-block of twists is a function of y = βλ^i ∈ O/q (cat map y ↦ λy).
- If the orbit of β equidistributes for the block observable, then ‖Π_{i<m} L_{τ_i}‖ ≤ exp(**m**(log R_k^cat + o(1))) for the m = 3p factors. If r(q) = p, the period repeats 3 times.
- The number of included levels is ≤ τ(h) = e^{O(m/log m)}, and the weight per level is Σ_β|W_{q,β}| ≤ (2/q²)q² + 2(q−1)(q−2)/q² < 4. So these factors are e^{o(m)}.

**Results [N], toy single-disc Galerkin K = 40 only.**
- R_k^cat = 6.338, 2.255, 1.337, 1.131, 1.037, 0.974 for k = 6, 12, 24, 36, 48, 64 (`code/k4_catrate.py`, byte-identical on the referee rerun).
- iid τ: 6.37 and 2.25 at k = 6 and 12 (`code/k4_normrate.py`).

**No claim** about the true two-disc operators, and **no claim** that the range q ≤ p^C is settled. The BGK applicability to {(ℓ^i b₁, ℓ^{−i} b₂)} is [H] here. A rigorous Weil-range version (q ≤ c_k p²) is developed in `K2/REPORT_K2.md` (Theorem W). It is conditional on an operator input.

## 5. Theorem K

Let m = 3p, j = m mod 168, and S⁺ as in J3.
1. **[P + CA]** S⁺ ∩ {3p : p ≡ p₀ (56)} is infinite for every unit p₀ (Theorem K3).
2. **[CA]** For m ∈ S⁺ (m ≥ 495, m ≥ M0(j)):
   W′_m ≥ −4m + 0.99K_j·1.0184^m + φ⁻¹(O♮_m^{<L} − 0.01(K_min/2)ξ_lo^m).
   - O♮^{<L} collects the conductor-∉{1,7} cross parts at included levels d < L_m (Prop K2).
   - If no included level is ≥ L_m (every m ≲ 1.68·10⁹), then O♮^{<L} := O♮ and the 0.01 loss term is absent.
3. **[P]** At each prime level q ∥ h in O♮^{<L}, the contribution is Σ_ρ 2Re(conj Z_ρ(D_iso(q) − E_b(q)/q)) (Theorem K1).

**Two alternative sufficient hypotheses.**
- **H♮** (J3): for some δ > 0 and infinitely many m ∈ S⁺, O♮_m ≥ −(1−δ)·0.99(K_j/2)ξ_lo^m.
- **H♮_mid** (new): for some δ > 0 and infinitely many m ∈ S⁺, O♮_m^{<L} ≥ −(1−δ)·0.98(K_j/2)ξ_lo^m.

Each one alone implies that frozen R′ is false. Under H♮_mid: 0.99K_j/2 − 0.01K_min/2 − (1−δ)0.98K_j/2 ≥ 0.98δK_j/2, and φ⁻¹ ≥ 2λ^{−m/2}, so W′_m ≥ 0.98δK_j·1.0184^m − 4m → ∞. H♮_mid is **not a weakening** of H♮:
- For m ≲ 1.68·10⁹ it is slightly *stronger* (constant 0.98 vs 0.99).
- Beyond that it drops the top levels but pays the 0.01 loss.

O♮^{≥L} has no sign, so neither hypothesis implies the other.

**[assessment] The owner's ideas.**
1. **Averaging over p with the d = 7 phase:** fails standalone, because W′_A and Q are controlled from one side only.
2. **Per-level bounds:** realised as K1 + K2. The Parseval/Cauchy–Schwarz form is no better than the trivial mass bound.
3. **Galois/Chebotarev:** averaging over conjugates isolates only the trivial zeros. Not pushed further.

## 6. Files (v2 additions)

- `code/k2_SZ.py`, `logs/k2_SZ.{log,json}`: explicit S_Z (K2-F1).
- `code/k2_large_v2.py`, `logs/k2_large_v2.{log,json}`: continuous s, correct rounding, bisection crossover (K2-F4).
- `lean/K3Finite.lean` (core Lean 4.33, no Mathlib; `decide` only, no `native_decide`; `#print axioms` shows no axioms for the decided statements), log in `lean/lean_check.log`. It covers:
  - no fraction a/b in the widened enclosure [0.88797590, 0.88797628] ⊇ the certified one for 1 ≤ b < 1339, nor for b ∈ {1512, 560, 1680, 616, 1848, 2520} (with a proved soundness lemma for the ceiling test);
  - the sieve enumeration over subsets of {3,5,11,13,17,19} (exactly 9 survivors, all with 56(F+1)/A_low ≤ 2645, A_low = 0.18001);
  - the ℓ = 23 exclusion inequality;
  - b ≥ 1339 ⇒ b′ ≥ 447.
- `lean/K3Gaps.lean` with `lean/run_gaps.sh`: Lemma K3(a) in the form "maximal cyclic gap ≤ b′/6", for every non-exceptional b′ ∈ [447, 2645] and every unit class, by `decide +kernel` (kernel reduction only, no native code). Status: **complete, all exit 0, and each `gaps_<lo>` theorem "does not depend on any axioms"**.
- Chunks of 100 cover 447..1646 (`lean/gaps_summary.txt`).
- The chunks of 100 above 1646 were killed for memory (exit 137). They were redone in chunks of 20 over 1647..2645 (`lean/run_gaps2.sh`, `lean/gaps_summary2.txt`).
- Logs are in `lean/logs_gaps_*.txt`. 1/6 < 0.18001 ≤ A uses the arb bound on A [CA].
- v1 files are unchanged. The manifest `SHA256_v2.txt` covers everything.

## 7. Changelog v1 → v2

| Fix | Change |
|---|---|
| K3-F1 | "unit multiplication preserves gaps" replaced by the set identity a′V(b′,r) = V(b′,a′r) plus "Lemma K3 holds for every unit class". |
| K3-F2 | CRT compatibility condition and the sieve step (error ≤ 2^k − 1 ⇒ gap ≤ X_t) written out. |
| K3-F3 | L16 caveat dropped; L16 is accepted (Line J audit, DELTA3 §D3.3). |
| K3-F4 | Min-margin fact (gap ≤ b′/6, margin 0.01334 at b′ = 672) and the referee's exact recheck recorded. |
| K1-F1 | β = 0 term corrected to (q−2)A_tot/q². |
| K1-F2 | Hypothesis "2 is a square mod q" stated (automatic for q \| h_m); referee control q = 11, 13. |
| K1-F3 | Folding/Meaning relabelled [H]; exact push-forward reformulation added. |
| K1-F4 | Loose "precision \|Z\|⁻¹ξ^m" phrase dropped. |
| K2-F1 | S_Z extracted: ≤ 0.5000001 for m ≥ 495 (Line F + J3 §1 certificates); Prop K2 is now [P + CA]. |
| K2-F2 | P* = the four frozen primaries, cited from the TRACE-206 text and base.py; the "other primaries" sentence deleted. |
| K2-F3 | Proof of η_m ≤ (2.01 + o(1))/log(2p+1) written (s = 1/log(2p+1)). |
| K2-F4 | Correct rounding (lower bound on √h); table and crossover labelled [N]; crossover ≈1.682·10⁹ by bisection. |
| K2-F5 | Vacuity below the crossover stated in §0, §3 and §5 (O♮^{<L} := O♮). |
| K4-F1 | Overclaims removed from §0, §4 and §5: nothing in q ≤ p^C is proved; the toy has no bearing on the true operators without verification. |
| K4-F2 | exp(m·(log R + o(1))) for the m = 3p factors. |
| K4-F3 | e^{o(m)} justified (τ(h) and per-level weight < 4). |
| Lean | Finite K3 checks formalised (decide / decide +kernel), see §6. |
| Theorem K | H♮_mid restated as an alternative sufficient hypothesis, not a weakening; owner-ideas section labelled [assessment]. |


## 8. Errata (after referee DELTA, 31 Oct 2026)
| Item | Change |
|---|---|
| η wording (D1 nit) | §3: 2.010 is the s = 1/ℓ upper bound. The optimised asymptotic constant is ≈ 1.988 (c ≈ 1.164). The numbers decrease toward 1.988, not "toward 2.01 from above". No statement of Prop K2 changes. |
| L-F1 (Lean) | `bprime_ge` is restated as `3 ∣ b → 1339 ≤ b → 447 ≤ b / 3` (the old disjunctive form was vacuous). The 3 ∣ b hypothesis is essential: the conclusion fails at b = 1339, 1340 under floor division. Recompiled, exit 0 (`lean/lean_check_v2.log`). `bprime_ge` uses propext and Quot.sound (from `omega`). The four decided theorems still use no axioms. |
| W2 (cross-ref) | The cyclic block lemma W2 is used only in K2. It is replaced by the non-cyclic W2′ in `K2/REPORT_K2_v2.md` (referee W-F1). Nothing in this report depends on it. |
