# Referee report: BGS Line K (towards an unconditional refutation of frozen R′, TRACE-206)

Referee: Grok Bot (independent, skeptical), 31 Oct 2026, from 10:18 UTC+5.
Object: `/workspace/bgs-lineK/REPORT.md`, sha256 `8fc2e9f1…0bb0b`. It matches `SHA256.txt`, and all 17 manifest entries verify.
I did not write into `/workspace/bgs-lineK` (the author is working in `K2/`).

Referee work lives in `/workspace/audit/lineK/`:
- `rerun/`: verbatim copies of the five scripts. Every output path is relative (`logs/…`). The only absolute path is a read-only import from `/workspace/bgs-lineI/code`.
- `bgs-lineJ/J3/logs/rat_excl.json`: a copy, so that K3's relative read resolves.
- `ref/`: independent referee scripts and their logs.

## Verdict table

| # | Claim | Verdict |
|---|---|---|
| 1 | Removal of H_arg (Lemma K3, Theorem K3) | **ACCEPT AFTER FIXES** (wording only; the mathematics is correct) |
| 2 | K1 light-cone identity at prime levels q ∥ h | **ACCEPT AFTER FIXES** (identity correct; one misprint; the interpretive paragraphs must be relabelled) |
| 3 | K2 large levels via positivity and Rankin | **ACCEPT AFTER FIXES**. [P] given an explicit Z-bound. The Z-bound is available from proved work but its constant S_Z is not extracted, and the result is non-vacuous only for m ≳ 1.7·10⁹ |
| 4 | K4 numerics (BGK range) | **ACCEPT AS [N]/[H] AFTER FIXES**. The labels in §4 are right, but §0.4, §0.5 and §5 overstate |
| 5 | Theorem K, "sole remaining hypothesis H♮_mid" | **ACCEPT AFTER FIXES**. Item 1 is a real unconditional result. "Sole hypothesis" is true only once the K2 constant is supplied, and H♮_mid is an *alternative* to H♮, not a weakening |

## Reproduction

- **k3_harg, k1_cone_check, k2_large, k4_normrate:** rerun output is byte-identical to the author's logs (diff empty; the seeds are deterministic).
- **k4_catrate:** byte-identical to the author's log (all six rows, k = 6…64).
- **rat_excl:** recomputed read-only from the Line J certificate (`ref/ref_rat_excl.py`, which chdirs to J3 and does not write).
  - Interval [0.887975909832077, 0.8879762669871324]; simplest fraction 1189/1339. Identical to the file K3 reads.
  - So K3 uses the certified, outward-rounded enclosure, and rounds it outward once more.

## 1. H_arg removal (Lemma K3, Theorem K3): ACCEPT AFTER FIXES

### Logic chain, checked step by step
1. **Arc.** cos(arg B_j + 2πx) ≥ 0.84431 is a closed arc in x mod 1 of length 2·arccos(0.84431)/2π = A = 0.180010648430009 (arb, 200 bits). The arc's position (arg B_j) is irrelevant. Its threshold 0.84431 > c_win, so it lies inside the Theorem J window.
2. **Reduction to b′.** Write θ = arg ξ/2π = a/b in lowest terms, with b ≥ 1339 from rat_excl [CA, accepted in the Line J audit].
   - Set b′ = b/gcd(3,b) and a′ = 3a/gcd(3,b). Then gcd(a′,b′) = 1 in both cases, and b′ ≥ ⌈1339/3⌉ = 447.
   - The candidate b for a given b′ is b′ (only if 3 ∤ b′) or 3b′. This split is correct.
3. **Dirichlet plus CRT.** p ≡ p₀ (mod 56) and p ≡ v (mod b′) are compatible iff v ≡ p₀ (mod g′), g′ = gcd(56,b′). The joint class is a unit mod lcm(56,b′) iff gcd(v,b′) = 1. So each v ∈ V(b′, p₀ mod g′) is hit by infinitely many primes. Correct.
4. **Phases.** {a′v : v ∈ V(b′,r)} = V(b′, a′r) **as sets**. Since Lemma K3 holds for *every* unit class, the phase set has all cyclic gaps < A·b′, so it meets every closed arc of length A. Correct, but see fix K3-F1.
5. **Gap lemma (a), exact range 447…6000.**
   - Re-verified independently in exact rational arithmetic against the arb lower bound of A (`ref/ref_k3.py`).
   - The failures are exactly b′ ∈ {504, 560, 616, 840}.
   - The smallest margin among passing cases is A − G/b′ = 0.01334, at b′ = 672, gap 112 = b′/6. So the author's float comparison cannot flip a case.
   - Remark: every non-exceptional b′ in the range has gap ≤ b′/6. This is a clean rational statement for Lean.
6. **Gap lemma (b), sieve. Correct.**
   - The primes 2 and 7 of b′ automatically divide g′, so a unit r mod g′ already avoids them.
   - The admissible t are periodic mod R = rad n′, and R | b′/g′, so the cyclic t-gap equals the periodic gap and the v-gap is g′ times it.
   - Inclusion–exclusion gives a count ≥ Xφ(R)/R − (2^k − 1). Consecutive admissible t₁ < t₂ satisfy t₂ − t₁ − 1 < X_t, so the gap is ≤ X_t ≤ F + 1.
   - Failure means g′X_t ≥ A·b′ ≥ A·g′R, which gives Π 2/(ℓ−1) ≥ A − 1/R.
   - Any ℓ ≥ 23 is excluded (2/22 < A − 1/23). Note that the factor for ℓ = 3 equals 1, which is why {3,…} sets survive.
   - The enumeration was redone in exact rationals. The surviving sets are ∅, {3}, {5}, {11}, {13}, {17}, {3,5}, {3,11}, {3,13}. The bound is b′ ≤ 56(F+1)/A ≤ 2644.29 < 6000. Correct.
   - Lower-rounding A is conservative everywhere it is used (the exact test, the subset test and the assert).
7. **Exceptions.** For b ∈ {1512, 560, 1680, 616, 1848, 2520}, no a/b lies in the enclosure. I checked every numerator in a ±1 neighbourhood with exact Fractions. Brute force confirms that the least denominator with a fraction in the enclosure is 1339. Correct.
   - The test uses the certified enclosure (item "Reproduction").
   - 560 and 616 as b are already excluded by b ≥ 1339, which is harmless.
8. **Irrational case.** Vinogradov plus the 56-character detector and Weyl, as accepted in DELTA3 of the Line J audit.

**Conclusion.** S⁺ ∩ {3p : p ≡ p₀ (56)} is infinite for every p₀ ∈ (Z/56)*, **unconditionally**.
- The proof is a case split on an unknown fact (rational or irrational), so it does not identify which case holds.
- No density is claimed in the rational case, which is correct.

### Required fixes
- **K3-F1.** §1, proof bullet 4: "Multiplication by the unit a′ … preserving cyclic gaps" is false as worded. Unit multiplication permutes Z/b′ but is not an isometry. Replace it with the set identity a′·V(b′,r) = V(b′,a′r), plus "Lemma K3 holds for every unit class".
- **K3-F2.** Write out the CRT compatibility condition (item 3 above) and the step "error ≤ 2^k − 1 ⇒ gap ≤ X_t" (item 6).
- **K3-F3.** Corollary K3 and §0.1 still say "[CA] modulo the referee check of Lemma L16 as in J3". L16 was ACCEPTED (Line J audit, DELTA3 §D3.3, with editorial nits L16-a/b). Cite that acceptance instead of a caveat.
- **K3-F4 (optional).** Record the min-margin fact (gap ≤ b′/6 off the four exceptions) and the referee's exact-rational recheck.

## 2. K1 light-cone identity: ACCEPT AFTER FIXES

### Proof re-derived
- **Twist.** τ_i(β) = Tr(βλ^i)/q (J3 §2), so Σ_i n_iτ_i = Tr(βx_w)/q mod 1.
- **Grouping.** Grouping words by x_w is legitimate: Σ_w|c_w|(‖V_w‖₁ + ‖E_w‖₁) < ∞ (L16 step 3 / Line F), and |s_w| ≤ 1 for the (±2,16) factor. So A(x) is well defined and Ẑ_β = Σ_x A(x)e(Tr(βx)/q).
- **Completing the square.** uN(β) + Tr(βx) = uN(β + x̄/u) − N(x)/u, and with u = t̄ we have −N(x)/u = −N(x)t.
- **Gauss sum.** Σ_β e(uN(β)/q) = G(u)G(−2u) = (−2/q)(−1/q)q = (2/q)q = q. Here **(2/q) = +1 is essential**. It holds for every q | h because 2y′² ≡ 1 (J3 §3).
- **Assembly.** Σ_{all β} ẐW = q⁻¹Σ_x A(x)[q·1_{N=0} − 1 − e(−N(x)t_b/q)]. Subtracting the β = 0 term (q−2)A_tot/q² gives A(cone) − (2q−1)q⁻²A_tot − E_b/q.
- **Cone.** {N(x) ≡ 0} = 𝔮 ∪ 𝔮̄ has 2q − 1 elements. Correct.

### Checks
- Author's 40-digit random-A check reproduced: max 1.9·10⁻³⁹.
- **Referee exact check** (`ref/ref_k1_exact.py`).
  - The identity is linear in A, so I verified it for every δ-mass A = δ_x and every t_b, exactly in Z[ζ_q]: integer exponent histograms, with equality meaning the difference is a constant vector.
  - q = 7, 17, 23, 31, 41, 47: 0 mismatches out of 214,240 cases. This is a complete finite verification for these q.
  - Control: q = 11 and 13 (2 a non-square) fail in every case. The split hypothesis is genuinely used.

### Required fixes
- **K1-F1.** Proof step 4: the β = 0 term is (q−2)A_tot/**q²**, not (q−2)A_tot.
- **K1-F2.** State in Theorem K1 that 2 is a square mod q, i.e. q ≡ ±1 (mod 8), and that it is automatic for q | h_m. The identity is false for inert q (referee control).
- **K1-F3.** "Folding" and "Meaning" are **not [P]**. Label them [H/interpretation], or prove them:
  - (a) "Trivial zeros … are *exactly* the words with x_w ∈ ∩𝔮" is unproved. P_w(ℓ) = 0 for all conjugates is about the element P_w(λ), not polynomial divisibility. Even then it needs an argument for r = 3p.
  - (b) "sporadic zeros unavoidable for q ≲ C^p" is heuristic.
  - (c) "H♮ at prime levels ⇔ equidistribution on 𝔮 ∪ 𝔮̄" omits E_b/q. E_b is bounded only by the total-variation mass Σ_x|A(x)|, which can far exceed |A_tot|, so it is not negligible a priori.
  - Correct and sharper statement: both D_iso and E_b depend only on the push-forward of A under x ↦ N(x) mod q. The level-q cross part vanishes iff that push-forward is "uniform" in the sense D_iso = E_b/q. I suggest stating it this way.
- **K1-F4 (minor).** The "precision |Z|⁻¹ξ^m" phrase is loose. Write the exact needed inequality, summed over the relevant levels, or drop it.

## 3. K2 large levels: ACCEPT AFTER FIXES ([P] given an explicit Z-bound; asymptotic only)

### Correct parts
- **Dev bound.** Dev_d ≥ −n_d|Z_ρ|²/d² follows from |Z_ν|² ≥ 0. And n_d ≤ φ(d) < d, since the members ν₀ + (2h/d)j have j a unit mod d (J3 §2).
- **Rankin.** Σ_{d|h, d≥L} 1/d ≤ L^{s−1}Σ_{d|h} d^{−s}.
- **Euler factors.** Only 7 (with 49 ∤ h) and primes ≥ 2p+1 divide h (r(q) lemma, accepted). Counting prime factors with multiplicity and bounding each factor by (1 − (2p+1)^{−s})^{−1} is conservative. h ≤ ε^m gives w.
- **Splitting by level** is compatible with the J3 identity:
  - levels d ≥ L are absorbed whole;
  - at d < L the X7 copies keep A^{<L} ≥ 1, since level 7 itself is < L;
  - |X16^{<L}| ≤ |X16| because the copies are positive multiples;
  - Q^{<L} ≥ 0.
- **η_m → 0.** Take s = c/log(2p+1). Then E(s)/m = O(1/log p), −log(1−7^{−s}) = O(log log p), and 1/(1−s) = 1 + O(1/log p), so η_m = O(1/log m). My recomputation gives η·log(2p+1) = 3.42, 2.53, 2.19 at m = 501, 3027, 3·10⁵ (decreasing, consistent).
- **Non-vacuity.** It needs (μ²/ξ)^{1+η} < √ε, i.e. η < 0.4407/0.4003 − 1 = 0.1009.
  - Bisection with continuous s (`ref/ref_k2.py`) gives a crossover m ∈ [1.672, 1.683]·10⁹ for both S_Z = 10⁸ and 10¹⁴.
  - The author's 1.73·10⁹ is a ×1.5 grid point. "≈1.7·10⁹" is correct.

### Is the Z-bound proved?
- **What P* is.** Line I's implementation of the frozen TRACE-206 mask (`bgs-lineI/code/base.py`, `PSTAR['k1']`) has P* = {(±2,8), (±2,16)}, and nothing else. Please confirm this against the TRACE-206 text and cite it. The sentence "If P* contains other primaries, their bounds are an input" should then be deleted.
- **(±2,8).** Line F [CA, audited] gives |Z| ≤ |c_m|(|c₀ᶠ|μ*^m + H₀), with |c₀ᶠ| = ½ and H₀ ≤ 1506.18. So C ≤ ½ + 1506.18·μ^{−m} (plus |c_m| ≤ 1 + λ^{−m}). **Proved.**
- **(±2,16).** J3 §1 certificates plus L16 [CA, accepted] give the untwisted rate ≤ 1.6677 < μ*. **The rate is proved, but the constant C₁₆ is not recorded.** `assemble16.json` stores only rates. ½‖T‖₁·fullR/(1−F) per block, summed over the 8 blocks and V/E, is computable from the stored certificates.
- **Verdict.** The Z-bound is not an extra hypothesis in substance, but as written S_Z = 10⁸ or 10¹⁴ is a **placeholder**.

### Required fixes
- **K2-F1.** Extract S_Z rigorously from Line F and the J3 §1 certificates, and replace the placeholder. The result is insensitive to S_Z (verified), so this is bookkeeping, but it is required before K2 is [CA].
- **K2-F2.** Replace "if P* contains other primaries…" with the frozen P* (TRACE-206 / base.py).
- **K2-F3.** Write out the η_m = O(1/log m) proof (the choice s = c/log(2p+1)). It is currently only asserted.
- **K2-F4.** Table labels: l and the √h rate are computed in floats from arb endpoints. The √h rate uses an *upper*-rounded log h where a lower bound on √h is needed; the effect is negligible (~10⁻³⁰ relative). Label the table and the crossover [N], or round correctly. Report the crossover as ≈1.68·10⁹ (bisection) rather than as a grid point.
- **K2-F5.** State prominently that for m below ~1.7·10⁹ no included level satisfies d ≥ L_m, so K2 changes nothing there. Theorem K should define O♮^{<L} := O♮ in that case.

## 4. K4 numerics: labels in §4 correct; ACCEPT as [N]/[H] AFTER FIXES

- **Reproduced:** k4_normrate and k4_catrate are both byte-identical.
- **K4-F1, overclaim (needs fixing).** These passages present the q ≤ p^C range as essentially settled:
  - §0.4: "the order-free product bound would beat D7 with room to spare";
  - §0.5 / §5: "the genuinely open part is the intermediate range p^C < q < L_m";
  - §5: "H♮_mid is [N]-supported in the range q ≤ p^C".

  The evidence is a **toy single-disc Galerkin** (not the certified two-disc operators). It also depends on an unverified equidistribution input: BGK applicability to {(ℓ^i b₁, ℓ^{−i} b₂)} is [H], as the author admits. Nothing in q ≤ p^C is proved. Rewrite as: "all of d < L_m is open. Toy-model numerics [N] suggest that the small-q part is benign *if* a BGK-type equidistribution input holds [H]."
- **K4-F2.** §4 writes ‖Π_i L_{τ_i}‖ ≤ exp(p(log R_k + o(1))). The product has m = 3p factors, and the comparison with the per-step rate 1.2836 needs exp(**m**(…)). If r(q) = p, the period repeats 3 times. Correct it, or explain the p.
- **K4-F3.** "weights … contribute only e^{o(m)}": say why. The number of levels is ≤ τ(h) = e^{O(m/log m)}, and the per-level weight is (2/q²)·O(q²).

## 5. Theorem K and hidden dependencies: ACCEPT AFTER FIXES

- **Item 1 [P + CA]: correct and genuinely unconditional.**
  - Dependencies: Lemma K3 (exact computation plus a hand sieve), rat_excl [CA], Dirichlet, and Vinogradov (literature; the DELTA3 citation nit on the IK theorem number still applies).
  - **Corollary K3** (H♮ alone refutes frozen R′) is correct, given Theorem J3 [CA] with L16 accepted.
- **Item 2.** Correct given K2. Hidden dependency: the explicit S_Z (K2-F1) and P* = 4 primaries (K2-F2). Also Theorem J, Line F, J3 §1/§2, Prop I8 (W′_A ≥ −4m), and the r(q) lemma, all accepted earlier.
- **Item 3.** [P] after K1-F1/F2.
- **"Single remaining hypothesis H♮_mid" needs two corrections.**
  - **(i)** It is single only after K2-F1.
  - **(ii)** H♮_mid is **not a weakening** of H♮. For m ≲ 1.7·10⁹, O♮^{<L} = O♮ and the constant is 0.98 instead of 0.99, so H♮_mid is slightly *stronger* there. For larger m it drops the top levels but adds the 0.01 loss. Neither implies the other, because O♮^{≥L} has no sign. Call it an alternative sufficient hypothesis (NOTES says "H♮ → H♮_mid"; reword).
- **Arithmetic check of the conclusion.** Under H♮_mid, 0.99K_j/2 − 0.01K_min/2 − (1−δ)·0.98·K_j/2 ≥ 0.98δK_j/2 > 0. Then φ⁻¹ ≥ 2λ^{−m/2} gives ≥ 0.98δK_j·1.0184^m ≫ 4m. **Correct.**
- **Title and §0.5** are honest. The summary must keep "not achieved: unconditional proof of H♮".
- **"Evaluation of the owner's ideas" (§5)** is [assessment]. Label it so.

## What is safe to register now

| Claim | Label | State |
|---|---|---|
| Lemma K3 (gap lemma, b′ ≥ 447, exceptions 504/560/616/840) | P + CA (exact integers) | **proved** (after K3-F1/F2 wording) |
| Theorem K3: S⁺ ∩ {3p : p ≡ p₀ mod 56} infinite for every unit p₀; H_arg removed | P + CA (+ Dirichlet, Vinogradov) | **proved, unconditional** |
| Corollary K3: frozen R′ ⇒ φ⁻¹O♮_m ≤ −0.99K_j·1.0184224^m + 4m + o(m) on an infinite S⁺; H♮ alone refutes frozen R′ | CA (via Theorem J/J3, L16 accepted) | **proved** (the dichotomy). The refutation is **conditional on H♮** |
| Theorem K1 (q ∥ h, 2 square mod q): Σ_{β≠0}Ẑ_βW_{q,β} = D_iso − E_b/q | P (+ exact P-check for q ≤ 47) | **proved** after the K1-F1 misprint fix |
| K1 "Folding/Meaning" (trivial zeros exactly ∩𝔮, sporadic zeros, ⇔ equidistribution) | H | **open / interpretation**. Do not register as P |
| Prop K2 (levels d ≥ L_m absorbed; η_m = O(1/log m); non-vacuous for m ≳ 1.7·10⁹) | P given Z-bound | **conditional on the S_Z extraction (K2-F1)**. It becomes [P + CA] once S_Z is certified. Register as conditional now |
| K4 block rates R_k^cat (toy Galerkin) | N | **numerical observation only**, with no claim about the true operators |
| BGK-range route | H | **open** |
| Theorem K: frozen R′ false under H♮_mid | CA + P (conditional) | **conditional** on H♮_mid and on K2-F1. H♮_mid is an alternative to H♮, not a weakening |
| Unconditional refutation of frozen R′ | — | **open** (not claimed; correct) |

Integration wording: "S⁺ ⊂ {3p} is infinite unconditionally (H_arg removed). Hence frozen R′ is false under H♮ alone; unconditionally, frozen R′ forces exponential cancellation of D7 by conductor ∉ {1,7} parts on an infinite set of m = 3p."

## Lean-formalizable small lemmas (quality gate)

1. **Lemma K3(a):** for all b′ ∈ [447, 6000] other than the four exceptions, and every unit r mod gcd(56,b′), the cyclic gap of V(b′,r) is ≤ b′/6 (referee observation: the max ratio is exactly 1/6). Also, 1/6 < 18001/100000 ≤ A, where the last inequality needs an arccos bound: cite [CA] or prove via a cos Taylor bound. Feasible with `decide`/`native_decide` over ~5.5k moduli.
2. **Lemma K3(b), enumeration:** over subsets S of {3,5,11,13,17,19}, Π_{ℓ∈S} 2/(ℓ−1) ≥ A − 1/R ⇒ S is in the list and 56(F+1)/A ≤ 2645, together with the ℓ ≥ 23 exclusion. Pure ℚ arithmetic (`norm_num`/`decide`).
3. **Lemma K3(b), sieve inequality:** #{t ∈ [x, x+X) : gcd(r + g′t, R) = 1} ≥ Xφ(R)/R − (2^{ω(R)} − 1). Moderate effort: inclusion–exclusion / Möbius in Mathlib.
4. **Fraction test:** no a/b in [L,H] (exact dyadics) for b ∈ {1512, 560, 1680, 616, 1848, 2520} or b < 1339. `decide`.
5. **Bookkeeping:** b ≥ 1339 ⇒ b′ ≥ 447; gcd(a′,b′) = 1; the b ∈ {b′, 3b′} split; and a′V(b′,r) = V(b′,a′r). Easy.
6. **K1 identity:** for fixed small q as a finite ZMod/cyclotomic computation, or in general via Mathlib quadratic Gauss sums (`gaussSum_sq`). Medium.
7. **K2:** Rankin's inequality Σ_{d|h, d≥L}1/d ≤ L^{s−1}Σ_{d|h}d^{−s}, and n_d ≤ φ(d). Easy.
8. **The final inequality chain of Theorem K** (constants 0.99/0.98/0.01, φ < λ^{m/2}/2). Easy (`norm_num`).

## Referee files
- `ref/ref_k3.py` + `ref_k3.log`: exact-rational K3 check.
- `ref/ref_rat_excl.py`: read-only recomputation of the enclosure.
- `ref/ref_k1_exact.py` + `ref_k1_exact.log`: exact Z[ζ_q] K1 check.
- `ref/ref_k2.py` + `ref_k2.log`: K2 bisection and η check.
- `rerun/`: copies of the author's scripts, with logs in `rerun/logs/`.

---

# DELTA (v2 + K2), referee, 31 Oct 2026, from 12:14 UTC+5

Objects:
- `REPORT_v2.md` (sha `badaafd8…`). `SHA256_v2.txt` (154 files) verifies.
- `K2/REPORT_K2.md` (sha `b8d14b60…`). `K2/SHA256_K2.txt` (25 files, current sha `18867758…`) verifies.
- v1 `REPORT.md` is unchanged (`8fc2e9f1…`).

Referee work is in `/workspace/audit/lineK/delta/` (`rerun/`, `lean/`). Nothing was written into the author's directories.

## D1. REPORT_v2: are the fixes applied?

All 15 v1 fixes are applied correctly: K3-F1…F4, K1-F1…F4, K2-F1…F5, K4-F1…F3, and the Theorem K / H♮_mid wording. Checked line by line against §7.

- **K2-F2 citation verified.** `mathematics/fixed-map/resonance_classification_lineG.md:107` at repo commit fa172e82 (`/workspace/bgs-int/BGS`) reads 𝓟* = {(2,8), (−2,8), (2,16), (−2,16)}.
- **K2-F1, S_Z.** `k2_SZ.py` was rerun from a copy and is byte-identical. Its inputs are certified:
  - **Line F:** |c^f| = ½, H₀ = 1506.18, and the lower end of |μ*|, 1.9154712, is used for the H₀ term (conservative). (±2,8) has C₈ ≤ 0.5000001.
  - **(±2,16):** the J3 untwisted `rest` certificates (asserted `certified` and `mode=rest`, F < 1), with exactly the formula in J3 `assemble16.py` (lines 3–5 and 20–23 are identical). The case-wise sum over blocks and V/E gives C₁₆ ≤ 2.273·10⁵, and R ≤ 1.6677 < μ.
  - The effective C₁₆(R/μ)^{495} ≤ 3.8·10⁻²⁵ is valid for m ≥ 495 because R < μ.
  - So S_Z = 2C₈² + 2C₁₆,eff² ≤ 0.5000001. **Correct.**
- **K2-F3, η proof.** Re-derived with s = 1/ℓ, ℓ = log(2p+1):
  - 1 − 7^{−s} ≥ s·log7/2, since s·log 7 ≤ 0.98;
  - w·(−log(1 − e^{−1})) ≤ 0.8814·0.45868·m/ℓ = 0.4043m/ℓ;
  - κ₀ = 9.21 > 0;
  - 1/(1 − 1/ℓ) = 1 + 1/ℓ + O(ℓ⁻²).
  - This gives η ≤ (1 + 0.4043/0.40030)/ℓ + O(ℓ⁻²) + O(log ℓ/m) = (2.010 + o(1))/ℓ. **Correct.**
  - Nit: "the numbers approach the proven constant 2.01 from above" is slightly off. With optimised s = c/ℓ the asymptotic constant is min_c [c + 2.2018·(−log(1−e^{−c}))] ≈ **1.988** (c ≈ 1.164). 2.01 is only the s = 1/ℓ upper bound.
- **K2-F4.** `k2_large_v2.py` rerun is byte-identical. The crossover is m ∈ [1.6821, 1.6823]·10⁹ [N], inside the referee's [1.672, 1.683]·10⁹. The lower bound h ≥ (ε^m − 1)/2 is correct.
- **K1/K3/K4 text: correct.**

## D2. Lean

Toolchain: Lean 4.33.1, core only, no Mathlib.
- **No escape hatches.** No `native_decide`, `sorry`, `admit`, `axiom`, `implemented_by`, `extern` or `unsafe` in code; the only hits are in comments.
- **K3Finite.lean** compiles (exit 0). The four decided theorems depend on no axioms. `noFrac_sound` uses only propext and Quot.sound.
  - **noFrac** correctly encodes "no a with Lo·b ≤ aD ≤ Hi·b", and soundness is proved.
  - **Widened interval.** [0.88797590, 0.88797628] ⊇ the certified enclosure, which is conservative for exclusion. It covers b < 1339 and the six exceptional b.
  - **Sieve encodings** match the math: possibleFail ⇔ F + 1 ≥ A_low·R, and bounded ⇔ 56(F+1)/A_low ≤ 2645, with A_low = 0.18001 ≤ A, which is conservative.
  - **big_prime_excluded** is the correct cross-multiplication. The monotonicity step for ℓ > 23 is by hand, as stated.
- **K3Gaps chunks.**
  - **Coverage:** parsing every chunk's `okRange lo n` gives contiguous coverage 447…2645, with no holes.
  - **Spot-compiled from copies:** 447 (n = 100), 1647, 2147, 2627, plus 1547 (n = 100; see the addendum). All exit 0, and every `gaps_*` "does not depend on any axioms".
  - **Negative control:** the same machinery over 502..506 with the exceptions removed is rejected by `decide` ("proved that the proposition … is false"). So the kernel really evaluates the gap computation.
  - **Statement matches the math:**
    - `okB` quantifies over **every r < g′ with gcd(r, g′) = 1** (all unit classes, including r = 0 when g′ = 1);
    - `maxGap` is the maximal cyclic gap (with wrap-around; an empty or singleton set returns b′ and fails);
    - 6·gap ≤ b′ together with `sixth_lt_A` (1/6 < 0.18001 ≤ A [CA]) gives gap < A·b′.
  - The Lean range 447..2645 suffices because the sieve shows every failure is ≤ 2644.3. The Python range up to 6000 is extra.
- **L-F1 (nit).** `bprime_ge : 1339 ≤ b → 447 ≤ b/3 ∨ 447 ≤ b` is vacuous (the right disjunct is trivial). State it as `3 ∣ b → 1339 ≤ b → 447 ≤ b / 3`. Plain `447 ≤ b/3` would be false at b = 1339 and 1340 with floor division, so the 3 ∣ b hypothesis is essential.
- **Not formalized:** the inclusion–exclusion sieve inequality, the passage from the arb bound on A to 0.18001, and the CRT/Dirichlet/Vinogradov steps. All remain [P] or [CA], as stated.

## D3. K2/REPORT_K2.md

- **W1 (Weil) [P-cite]: correct.**
  - The character detector over the e = (q−1)/r characters trivial on H is right. The twisted Kloosterman bound 2√q applies when AB ≠ 0, and the Gauss sum case gives ((e−1)√q + 1)/e ≤ √q.
  - **Application.** Tr = σ + σ̄ and σ̄(λ) = ℓ⁻¹ give the binomial form.
  - **Degeneracy.** It occurs iff γβ ∈ qO. For unit β that means γ ∈ qO (|N(γ)| ≥ q²). For β ∈ 𝔮̄∖0 it means γ ∈ 𝔮 (|N(γ)| ≥ q). **Correct.**
  - **7q case.** Split i mod 3; each part is a coset of ⟨ℓ³⟩ of order p, giving ≤ 6√q. Correct.
- **W3 [P]: correct.**
  - f_k = ‖P_k‖²_HS = Σ_γ c_γ e(Tr(γy)) with c_γ = Σ_{x_w − x_w′ = γ} Tr(M_wM_w′^*), and ∫ e(Tr(γy)) dy = 0 for γ ≠ 0.
  - T_k(q) → 0 by dominated convergence, which is pointwise in γ. Note that infinitely many γ (e.g. units) have small norm, so the convergence is not "finitely many γ".
- **W2 [P]: proof gap (repairable).**
  - The argument rotates the offset o inside Tr(J·X). This is valid only when the read-out is a pure trace (J = I). That covers the (±2,8) sector-law traces of Line J v2.
  - The (±2,16) read-out Tr((I⊗J_B)𝐕_B^m) has J_B ≠ I (rank one, L16), and Tr(JX) is not invariant under rotating X. Blocks that straddle the position of J are not P(i).
  - **Fix W-F1.** Use the non-cyclic variant:
    - |Tr(JX)| ≤ ‖J‖₁·‖X‖ (J has finite rank);
    - take offsets o ∈ [0, k) and only the Q−1 blocks inside [0, m);
    - the block starts cover ≥ m − 2k positions, so GM ≤ QM costs a factor (m/(m−2k))^{(Q−1)/2} = e^{O(1)} plus (sup‖L‖)^{2k}.
  - The conclusion of Theorem W is unchanged (constants e^{O(k)}).
- **(OP) and Theorem W.**
  - (OP_k, δ) is clearly stated as a hypothesis ("only extra input", "Not proved"). Theorem W is stated as "Assume (OP_k, δ)".
  - The Weil-range bookkeeping is correct: with √q ≤ √c_k·p, the term 2√q·A_k/r ≤ η/3, and 6√q·A_k/r ≤ η for 7q.
  - **W-F2 (numerical error).** "1.4743 < ξ_lo/1.6677" is **false**: ξ_lo/1.6677 = 1.4742995 < 1.4743, and 1.6677·1.4743 = 2.4586901 > ξ_lo = 2.4586893. Use 1.4742 in (OP) and step 6. Harmless after the (1−δ/2) factor, but the stated inequality must be correct.
  - **Nits.** Step 6 "(±2,8) once δ/2 > 2.2·10⁻⁶" is unnecessary, since μ·1.28359 = 2.4586849 < ξ_lo already. Step 7 "((1−δ/2)ξ_up)^m … after shrinking δ" should read "≤ ((1−δ/2)ξ_lo)^m·e^{o(m)}"; shrinking δ is the wrong direction.
  - The constants (p₀ ~ 10^{800}) are honestly reported as asymptotic only.
- **Evidence for OP and Conjecture C1.** The toy values are labelled [N]. **W-F3:** "Conjecture C1 [N]" should be [H/conjecture]; a conjecture is not a numerical result.
- **§3 Bourgain [P-cite, ineffective].** The exponent conditions (gcd(e, q−1) = e < q^{1−ε}, and gcd(2e, q−1) ≤ 2e) are plausibly checked, and the result is correctly marked ineffective.
  - **W-F4.** The paragraph "Relation to … TRACE-179 [P, explicit]" mixes facts with literature claims: "no non-trivial bound … is known", "cannot be removed by any known exponential-sum technology", "BGK helps exactly … and nowhere else". Label those sentences [assessment].
  - Cochrane–Pinner exponent arithmetic: 2.292·r^{33/46}q^{1/4} is non-trivial iff q ≲ r^{1.13}. Correct as computed.
  - The Bourgain composite-modulus remark is correctly [H].
- **Negative results.**
  - (b): a single level's trivial bound exceeds D7. Correct, [P]. The factorisation-control remark is an [assessment].
  - (d): d ≥ (2p+1)² makes the Weil bound 2^ω√d > r. Correct, trivial.
  - The periodic-point and β-moment items are correctly labelled negative/[H]. Factorisations and toy traces are [N].
- **Theorem K2′: correctly conditional.**
  - It is labelled "[P] given (OP_k, δ), Theorem J/J3 [CA], Prop K2 [P+CA]".
  - **Logic.** If, for infinitely many m ∈ S⁺, no open conductor has a slow β, then W2 bounds the open part directly by the non-slow definition, and Theorem W bounds the Weil part. That gives O♮^{<L} = o(ξ_lo^m) ⇒ H♮_mid ⇒ refutation. Hence frozen R′ ⇒ a slow orbit exists for all large m ∈ S⁺. **Correct**, after W-F1.
  - Conductors c ≥ L_m occur only at absorbed levels, and prime powers and composites are included in "open". Correct.
  - **W-F5 (wording).** "checkable by a finite computation" should read "checkable in principle by a certified operator computation (truncation with rigorous error)".
- **W-F6 (cosmetic).** NOTES_K2 records the K2 manifest sha `fd7f…`. The manifest hashes NOTES_K2 itself, so this is circular and is now stale (current `18867758…`). Do not record a manifest's own hash inside a file it covers. Keep it in a separate file, or say "see SHA256_K2.txt".

## D4. Verdict

- **REPORT_v2 (Line K): READY TO INTEGRATE.** Optional nits: L-F1 in Lean, and the "1.988 vs 2.01" wording.
- **K2/REPORT_K2: READY TO INTEGRATE AFTER FIXES W-F1 (W2 proof for non-trivial read-out) and W-F2 (1.4743 → 1.4742).** W-F3…W-F6 are labels and wording only. None changes a conclusion.

## D5. Claims safe to register

| Claim | Label | State |
|---|---|---|
| Lemma K3 (gap lemma; exceptions 504/560/616/840) | P + CA; finite part **Lean-checked** (decide/kernel, 447..2645; fraction tests; sieve enumeration) | proved |
| Theorem K3: S⁺ ∩ {3p : p ≡ p₀ (56)} infinite for every unit p₀ (H_arg removed) | P + CA (+ Dirichlet, Vinogradov) | **proved, unconditional** |
| Corollary K3: frozen R′ ⇒ φ⁻¹O♮ ≤ −0.99K_j·1.0184224^m + 4m + o(m) on an infinite S⁺; H♮ alone refutes frozen R′ | CA | proved (dichotomy); refutation **conditional on H♮** |
| Theorem K1 (q ∥ h, 2 a square mod q): light-cone identity, plus the push-forward reformulation | P (+ exact P-check q ≤ 47) | proved |
| Prop K2: levels d ≥ L_m absorbed; S_Z ≤ 0.5000001 (m ≥ 495); η_m ≤ (2.010 + o(1))/log(2p+1) | P + CA | proved |
| K2 non-vacuity crossover m ≈ 1.682·10⁹ | N | numerical |
| Theorem K: frozen R′ false under H♮ **or** under the alternative H♮_mid | P + CA | **conditional** (H♮ or H♮_mid; neither proved) |
| W1 (Weil bound over subgroup H; degeneracy criterion), W3 (orbit average) | P-cite / P | proved |
| W2 (cyclic block AM–GM) | P | proved for pure-trace read-outs; **after W-F1** for (±2,16) |
| Theorem W (Weil range q ≤ c_kp², conductors q, 7q, o(ξ_lo^m)) | P, conditional | **conditional on OP_k** (after W-F1, W-F2) |
| Bourgain extension to q ≤ p^C | P-cite, ineffective | conditional on OP_k |
| Theorem K2′ (frozen R′ ⇒ a slow λ-orbit at an open conductor for all large m ∈ S⁺) | P, conditional | **conditional on OP_k** (after W-F1) |
| OP, Conjecture C1 (lim I_k^{1/k} = 1) | H (toy evidence N) | open |
| Negative results (b), (d), periodic-point, β-moment | P / N / assessment | recorded as negative findings, not theorems about R′ |
| K4 toy rates, factorisations, toy level traces, W1 instances | N | numerical only |
| H♮, H♮_mid, unconditional refutation of frozen R′ | — | **open** |

Referee files: `delta/rerun/` (`k2_SZ`, `k2_large_v2` logs, byte-identical) and `delta/lean/` (compiled copies, `Neg504.lean` control, `summary.txt`).

Addendum (D2): chunk `K3Gaps_1547` (n = 100) compiled too: exit 0 in 123 s, and `gaps_1547` does not depend on any axioms. All spot-checks pass.

---

# DELTA2 (K2 v2 + REPORT_v2 §8 errata), referee, 31 Oct 2026, from 12:26 UTC+5

Objects: `K2/REPORT_K2_v2.md` (sha `c9f58c24…`). `SHA256_v2.txt` and `K2/SHA256_K2.txt` verify. `K2/SHA256_K2.sha256` matches `4ceaa0d1…`.

## REPORT_v2 §8 errata and Lean: READY
- **η wording:** corrected to the optimised constant ≈ 1.988 versus the s = 1/ℓ bound 2.010. Correct.
- **`bprime_ge`:** now `3 ∣ b → 1339 ≤ b → 447 ≤ b/3` (by omega). I recompiled `K3Finite.lean` from a copy in `delta2/`: exit 0, with no `native_decide`, `sorry` or `admit`.
  - The four decided theorems depend on no axioms.
  - `noFrac_sound` and `bprime_ge` use only propext and Quot.sound.
  - This matches `lean/lean_check_v2.log`.
- **W2 cross-reference:** fine.

## K2 v2

**Lemma W2′ (non-cyclic), checked step by step:**
- **Blocks fit.** For o < k, o + (Q−1)k ≤ Qk − 1 ≤ m − 2, so the Q−1 blocks lie in [0, m).
- **Leftover length.** It is between k+1 and 2k, using Qk ≥ m−k.
- **Block starts.** B = [0, (Q−1)k) is covered once each, and |B| ≥ m − 2k.
- **GM ≤ QM.** GM_B^{Q−1} ≤ ((m/|B|)·avg)^{(Q−1)/2} is correct.
- **Constant.** (1−x)^{−1/x} with x = 2k/m ≤ ½ is ≤ 4 ≤ e², so the stated e² is valid (4 would also do).
- **Exponent.** Q−1 ≤ m/k gives b^{(Q−1)/2} ≤ b^{m/2k} for b ≥ 1, and max(1, ·) handles b < 1. Correct.
- **W-F7 (new, one-line, required).** The (±2,16) read-out I⊗J_B is **not** of finite rank.
  - I acts on the infinite-dimensional lattice space; J_B is rank one only in the 2-dimensional block factor (L16, J3 line 91). So ‖I⊗J_B‖₁ = ∞ and the "finite rank" branch, C_J = ‖J‖₁, does not apply.
  - **Fix:** use the J = I argument for any bounded J. Put one leftover factor in trace norm: |Tr(JX)| ≤ ‖J‖·‖X‖₁. Then C_J = ‖J‖·sup‖L‖₁/sup‖L‖, with ‖I⊗J_B‖ = ‖J_B‖ ≤ ½. This is exactly the J3 `assemble16` bound.
  - Conclusions unchanged.
- **Nit.** (sup‖L‖)^{len} ≤ (sup‖L‖)^{2k} needs sup‖L‖ ≥ 1. Write max(1, sup‖L‖)^{2k}; this is true in the toy (1.8·10⁵) but should be stated.

**Theorem W and Theorem K2′ still follow** (after W-F7), with C′ = e^{O(k)} independent of m:
- **Step 3** now uses W2′ with max(1, ·)^{(Q−1)/2}.
- **Step 6:**
  - 1.6677·1.4742 = 2.458523 < ξ_lo;
  - μ·1.28359 = 2.4586849 < ξ_lo.
- **Step 7:** now reads e^{o(m)}·((1−δ/2)ξ_lo)^m = o(ξ_lo^m). Correct.
- **K2′ logic:** unchanged, and it now cites W2′. Still correctly "[P] given (OP_k, δ)".

**W-F2…W-F6: all applied correctly.**
- W-F2: 1.4742, with the false 1.4743 inequality acknowledged.
- W-F3: Conjecture C1 is [H/conjecture].
- W-F4: §3 literature statements are marked [assessment].
- W-F5: "certified operator computation (truncation with rigorous error)".
- W-F6: manifest hashes are kept in side files, and NOTES_K2 no longer self-cites.

## Verdict
- **REPORT_v2 (Line K) + Lean: READY TO INTEGRATE.**
- **K2/REPORT_K2_v2: READY TO INTEGRATE after the one-line fix W-F7** (bounded-J form of W2′; no conclusion changes). With W-F7 applied, the DELTA §D5 registration table stands, with W2 replaced by W2′ [P] (all read-outs).
