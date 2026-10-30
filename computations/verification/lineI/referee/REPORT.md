# Referee report: Line I (averaging across residues for R′; d = 7 twisted certificates)

Referee: independent adversarial audit, 2026-10-31, 00:10–00:40 UTC+5.
Object: `/workspace/bgs-lineI` (REPORT.md §0–4 and S3.0–S3.7, theory_E2.md, NOTES.md, cert/, code/, logs/, lean/LineI.lean).
I did not modify `/workspace/bgs-lineI`. All work is in `/workspace/audit/lineI/` (code/, out/, logs/, data/; hashes in
`logs/SHA256_audit.txt`). Nothing was pushed, and no foreign processes were touched.

## Overall verdict: **ACCEPT AFTER FIXES**

No mathematical error invalidates a certified statement. I found:
* one **unsafe rounding**: the headline constant of Theorem I6 is rounded **down**;
* one **sign error** (Lemma I5);
* one **hidden gap** (Lemma I5 applied to unit-restricted sums);
* one **quantifier gap** (Thm I4);
* several **overstatements**: "verdict", "[P]" on barrier assessments, "Lean-checked", and a wrong m-power.

All are fixable by rewording or one-line proofs. Blocking fixes: B1–B9 below. Recommended: R1–R7.

## 1. What I re-ran / checked independently

| Item | Method | Result |
|---|---|---|
| `bounds_sq.py` | rerun on copied inputs (`bsq/`) | `bounds_sq.json` **byte-identical** (sha afafc3ac…); log identical. First m ≡ 9 (24) with bound < 0.01: **321** (0.00457). Every table entry for m ≥ 321 is < 0.01, and the table decreases monotonically. **But CV = 6 768 179.6 > 6.768e6** (B1). CE = 68 586.2 ≤ 6.859e4 OK |
| Deterministic rebuild of the deleted matrices | `certG_build.py V … 1:3` and `E … 1:3` (author's argv) | mid/rad sha256 **identical** to the provenance in `V_1_3_rest.json` (3ac1d0a5…, b5e0fc2b…) and `E_1_3_rest.json` (f5a03424…) |
| **Independent re-certification of the top class 1:3 (V)** | own code `code/own_rig.py`. It does not use rig_spec. Rest mode: own power recursion with √2·γ_{2n+2}, ‖M‖₂ ≤ min(‖M‖_F, √(‖M‖₁‖M‖_∞)), JSON inputs padded by 1+1e−12, float norms by 1+1e−6, p = 24 | **certified**: R = 1.45: F = 0.3227; R = 1.5: F = 0.1908 (author 0.3570 / 0.2292, more conservative). Own trace constant for 1:3: 5.81e6 ≤ the author's 6.77e6 (`out/own_V_1_3.json`) |
| Builder conventions, end-to-end and exact | (a) `code/brute.py`: brute force over all 5⁹ words (\|n\| ≤ 2) of Ẑ(β) = Σ Φ̂(n)e(−νP(n)/2h)e(Tr βα_n/7) **from the definitions** (P via ψ(d) = y′x_d − 2hy_d), m = 9, ν = 1045. (b) `certG_build.py` run with Nmax = 2, K = 20 (tail assertion disabled in a TEST-ONLY copy; the core matrix code is unchanged). (c) Own partial trace `code/ptrace.py` | **(1−λ⁻⁹)(Tr BV⁹ − Tr BE⁹) = brute Ẑ(β) to 1e−12…5e−14 relative** for classes 1:3, 0:1, 1:0, 0:2. Without the factor (1−λ⁻ᵐ) the error is 1.3e−7. So C = −c₀, w(n) = ĝ(n)e(Cn²/2), the gstates phases e(−k(ψ₀n²+2nu)/8), the twist e(nτ_i), the 3-cycle, the row/column convention, B, V−E, and c_m = 1−λ⁻ᵐ are all right |
| trchk at m = 9, full alphabet | author's `trchk.py` on the rebuilt E_1_3 (top \|eig\| 0.358). Own partial trace on the rebuilt V_1_3 + E_1_3 (K = 30/22, Nmax = 150) vs zpred Ẑ(1,3) | (1−λ⁻⁹)(TrV − TrE) = 0.688183+5.448942i vs zpred 0.688183+5.448942i: **rel 1.1e−8** (`logs/trfull_m9.log`). Float top \|eig\| of V_1_3 (ARPACK): 1.283714 (×3), next 1.09647 (×3); this confirms r_tw [N] |
| zpred vs exact class sums, m = 9 | rerun `zpred.py 40 2.6 10 9` in a copy | maxrel_vs_act **2.595e−8** (2,8) and **2.04e−8** (−2,8); Dev = 900.47, rel +0.29374 (reproduced) |
| zpred vs brute force | `zpred.py 41 2.6 2 9` (kick truncated at \|n\| ≤ 2) vs `brute.py` | all 49 Ẑ(β) agree to **1.2e−12** relative |
| Prop I2 (a)–(d) | rerun `verify_coset.py` (copy) | MAXERR 1.4957e−12, N(u) law all True (reproduced) |
| Prop I2′ per member | `code/i2prime.py` (brute data, m = 9) | member formula to 7e−14. \|ω_t\| = 1 and \|G_t(β)\| = 7 for all β. \|Δ_t\| ≤ S/d. Exactly 1 of 6 dilations is a non-unit (j = 2), so there are 5 members |
| 8 classes cover all β ≢ 0 | orbit computation under β ↦ ±λβ in (Z/7)[√2] | 8 orbits, each of size 6, union = 48. The 8 representatives lie in distinct orbits. Ẑ is constant on orbits to ≤ 4e−13 (brute) |
| Case map / 7 \| h | `code/cases.py`, m < 700 | 7 \| h ⟺ m ≡ 3 (6). (k, ψ₀, ψ₁) depends only on m mod 24: m ≡ 9 → (3,1,1) for all tested m. k ≡ 3h⁻¹ (8) always. (1+√2)ᵐ mod 8 has period 8 |
| Builder diff vs Line H `cert49_build.py` (sha 2b5d693f) | line-by-line review (§2.3) | correct |
| rig_spec | sha f346e22c = Line H v4. gc = √2·γ_{2D+2}, PAD = 1+2⁻⁴⁰, per-run provenance present | OK |
| Provenance | all 16 build JSONs: code aa86c186, gstates 05f55500; all 16 rest JSONs: rig_spec f346e22c; all certified (V: R = 1.45/1.5/1.55, E: 1.0/1.2) | consistent; see R2 |
| Lean | `lake env lean` on an unmodified copy, in `/workspace/bgs-int/BGS/formalization` (Lean 4.33.1, Mathlib cache). The worktree is at fa172e82, and toolchain/lake files are identical to origin/main 4f5056b8 | **EXIT 0**, no errors or warnings. Axioms of all 5 theorems: propext, Classical.choice, Quot.sound. The only grep hit for sorry/native_decide is the docstring |

## 2. Claim-by-claim verdicts

### Prop I1 (relative phase split): **ACCEPT**
This is a definitional identity: σ_ρ = Z_ρ⁻¹ Σ_n w(n) δ_{P(n) mod 2h}. State that it requires Z_ρ ≠ 0.

### Prop I2 (dilation-coset L² law): **ACCEPT AFTER FIXES** (B2, B3, R3, R5)
* I re-derived (a)–(d):
  * Parseval;
  * ΣN = d², hence Σδ_u = 0;
  * ΣN(u)δ_u = εdδ₀;
  * ΣN² = d³+d²−d;
  * Σ_{t≠0}|Z_t|² = |Z₀|²(1/d−1/d²) + 2εRe(Z̄₀δ₀) + dΣ|δ_u|².

  All correct. The numerics reproduce.
* The congruence used for Z_t = Z(ν₀+2hj/d) is labelled [N]. It is in fact a one-line [P]: Nm(α_n) = Σ n_in_j x_{|i−j|} (because λ⁻ᵈ = λ̄ᵈ), and ψ(d) = y′x_d − 2hy_d ≡ y′x_d (mod 2h). So P(n) ≡ y′Nm(α_n) mod **2h** (R3).
* Hidden imprecision: the sum over t ≠ 0 includes exactly one non-unit dilation, which is not a member of M_d(ρ). The quoted "cross 877.61, square 319.51" are over all 6 values of t. The member deviation is Dev = 900.47, which gives the quoted +0.2937. Say so (B3).
* §0 says the law is "proved and Lean-checked". Only the algebraic core (cross_term, sum_N_sq, coset_decomp, two norm counts) is in Lean. The Fourier step and the identification are paper + numerics (§1 says this correctly; fix §0, B2).
* Remark (R5): for odd m every prime d | h splits, since h²+1 = 2y′² gives (2/d) = 1. So ε = +1 always and the inert branch is vacuous. Also, the Lean docstring names `norm_count_23`, but the theorem is `norm_count_23_zero` (zero count only).

### Prop I2′ (members = ω_t Z_ρ/d + Δ_t): **ACCEPT**
* Proof checked:
  * Fourier inversion on (Z/d)² with the nondegenerate pairing Tr(βγ) = 2(b_x g_x + 2b_y g_y), valid for odd d;
  * the two-variable Gauss sum of the nondegenerate form t·Nm (disc 8, coprime to d) has |G_t(β)| = d for gcd(t,d) = 1, including composite d via CRT and odd prime powers.
* Under the frozen membership rule, members of level d are exactly j with gcd(j,d) = 1, so t = jy′ is always a unit (y′ is a unit mod h). The lemma therefore applies to every member, including d = 287.

### Symmetries Ẑ(λβ) = Ẑ(β), Ẑ(−β) = Ẑ(β): **ACCEPT AFTER FIX** (B4)
* Verified numerically (brute force, ≤ 4e−13).
* The paper proof "cyclic shift" omits the key fact. Add one line: λᵐ = x_m + 2y_m√2 with x_m = 2h²+1 and 2y_m = 2hy′, so λᵐ ≡ 1 (mod 2h). Hence x_{m−d} ≡ x_d (mod 2h), so P is a cyclic quadratic form mod 2h (and Φ̂ is cyclic). With λᵐ ≡ 1 (mod 7) (3 | m), the shift multiplies α_n by λ.
* Ẑ(−β): ĝ(−n) = ĝ(n) (iⁿJ_n even), P(−n) = P(n), α_{−n} = −α_n. Correct.

### Operator case depends only on (1+√2)ᵐ mod 8; 7 | h ⟺ m ≡ 3 (mod 6): **ACCEPT** (R4: write out the proofs)
* (1+√2)³ ≡ 5√2 (mod 7), so (1+√2)⁶ ≡ 1 and h_m ≡ 0 only for m ≡ 3 (mod 6).
* m ≡ 9 (24) ⇒ m ≡ 1 (8) ⇒ (h, y′) ≡ (1, 1) (mod 8) ⇒ k ≡ 3h⁻¹ ≡ 3, ψ₀ = 1, ψ₁ = 3y′ − 2h ≡ 1.
* Also 3 | m, so the 3-cycle closes. Verified for m < 700.

### Thm I4 (reduction R′ ⇐ (E″)+(T″)+(D)): **ACCEPT AFTER FIX** (B5)
The partition argument is elementary, but the quantifiers do not match:
* (E″) is stated "for each compact K", i.e. for fixed K.
* (T″) is stated for the cusp y ≥ Y(m) with Y(m) unspecified, presumably → ∞.

Fixed-K statements do not cover the growing region {y < Y(m)}. Either:
* state (E″) uniformly for K_m = {y ≤ Y(m)} with the same Y(m) as in (T″); or
* require (T″) for every Y(m) → ∞ and use a diagonal argument (Y(m) growing slowly enough for (E″)).

Also say explicitly that the sum is over units ν and the normalisation is 1/φ(2h).

### Lemma I5 (diagonal invisibility): **ACCEPT AFTER FIXES** (B6)
* **Sign error.** With Z(ν) = Σ Φ̂(n)e(−νP(n)/2h), f(x+iy) = Σ c_k(y)e(kx) and z_ν = (ν+i)/2h:
  * Σ_{ν mod 2h}|Z_ν|²f(z_ν) = 2h Σ_k c_k(1/2h) C(k), with C(k) = Σ Φ̂(n)Φ̂(n′)‾ 1[P(n) − P(n′) ≡ k].
  * So it is c_{[P(n)−P(n′)]}, not c_{[P(n′)−P(n)]}, and C(k), not C(−k) (theory_E2 "I5 restated"). For odd Maass forms (c_{−k} = −c_k) the wrong sign flips the off-diagonal term.
* **Hidden gap.** The identity is over **all** ν mod 2h. R′ and (E″) are over **units** ν. For the unit-restricted sum the diagonal is (Σ|Φ̂|²)·Σ_{ν unit} f(z_ν) = Σ_k c_k(1/2h) c_{2h}(k), where c_{2h} is the Ramanujan sum. That is **not** zero for cusp forms, so "(E″) is purely an off-diagonal statement" is false as written.
* Correct statement: the diagonal reduces to the **unweighted** primitive-horocycle sum (Σ|Φ̂|² = 1), which must be controlled by an equidistribution input (to be cited with its rate), or else formulate (E″) over all ν mod 2h and treat non-units separately. The qualitative message (the real content is off-diagonal) survives.

### Prop I8 (W′/m ≥ −4 + ΣDev/(mφ)): **ACCEPT AFTER MINOR FIX** (B7)
Re-derived: W′ ≥ −RMT_m(1 − N_res/φ) + φ⁻¹Σ Dev. It uses three facts that should be stated:
* (i) The sets {ν_ρ} and M_d(ρ) are pairwise disjoint. This is true by the frozen rule: a common member of levels d, d′ lies at level gcd(d,d′) | d and is excluded. Different ρ ∈ P* differ mod h/d ≥ √h.
* (ii) RMT_m = 4m − m²/h ≤ 4m.
* (iii) N_res ≤ φ.

Also replace "is exactly the statement" (theory_E2 (i)) by "is implied by / reduces to".

### Theorem I6 [CA]: **ACCEPT AFTER FIXES** (B1, B8, R1, R2)
The certificates are valid:
* all 16 rest JSONs are certified by rig_spec v4 with correct provenance;
* class 1:3 V was **independently re-certified** (F = 0.323 at R = 1.45);
* bounds_sq reproduces byte-identically.

Line-by-line review of the chain:
1. Cauchy: ‖Lⁿ‖ ≤ R^{n+1}G/(1−F). Correct.
2. |Tr(BLᵐ)| ≤ ‖B‖‖L‖₁‖L^{m−1}‖ ≤ 4‖L‖₁RᵐG/(1−F). Here ‖B‖ = ‖e₀‖‖1_{i=0}‖ = 1·√16, and the state factor carries the unweighted Euclidean norm. Correct. The trace norm uses NS = 48 (monomial unimodular factor). Correct.
3. Lifted identity Ẑ = (1−λ⁻ᵐ)(Tr BVᵐ − Tr BEᵐ). TRACE-197 hypotheses: ρ = 0.85 > 0.6036 (V) and > 0.1036 (E); β > 0; ĝ superexponential. Here |C| = c₀ = 1/(4√2) exactly, so the α-condition is identical. The state factor is a finite monomial matrix and B is rank one in state space, so the identity holds termwise per word, as in TRACE-207. Confirmed exactly by the referee's brute-force test (1e−14).
4. Class invariance: see the symmetries section.
5. d Σ|δ_u|² ≤ (max N/d) Σ_{β≠0}|Ẑ|² with max N = 2d−1 = 13. I re-derived it: Cauchy–Schwarz on the norm fibres, then Parseval. Correct.
6. φ(2h) = φ(h) (h odd), and Rosser–Schoenfeld Thm 15. Its unique exception n = 223092870 is even, so it cannot occur. Correct.

Builder adaptation (diff vs cert49_build):
* x = n;
* Mn = e^{2π|C||n|R};
* a_tail = 2π|C|ρ + β/λ, tailB0 = 2π|C|ρ;
* B1 uses e^{β|n|/λ};
* the Bessel tail Σ_{|n|>N}|J_n(x)|e^{α|n|} ≤ 2tᴺ⁺¹/(N+1)!/(1−t/(N+2)) with t = xe^α/2 is correct (|J_n(x)| ≤ (x/2)ⁿ/n!);
* J_{−n} = (−1)ⁿJ_n and iⁿ via n%4 are correct;
* `arb.bessel_j(n)` = J_n(self) (checked);
* the composition/multiplier Galerkin blocks are unchanged from the audited Line H code.

All correct.

Required fixes:
* **B1 (unsafe rounding).** CV = 6 768 179.6. "6.768·10⁶ (constants rounded up)" is rounded **down**: write **6.769·10⁶** in S3.4, S3.0 and wherever else it is quoted. bounds_sq prints with %.4g (round-to-nearest): print outward-rounded values. CE: 6.859e4 is correct. The m ≥ 321 conclusion is unaffected (computed with the exact CV: 0.00457 at m = 321). Also write the decay rate as ≤ 0.87089ᵐ, not 0.87088ᵐ (exact 0.8708840…).
* **B8 (citation and scope).**
  * In proof-chain step 3, write c_m = 1−λ⁻ᵐ explicitly, cite **TRACE-197** with the remark on |C| = c₀ and the finite state factor, and replace "checked numerically to 1e−6" by the referee check (exact brute force 1e−14 at Nmax = 2; full alphabet 1.1e−8).
  * State the scope (square term only; ρ = (2,8); m ≡ 9 mod 24; m ≥ 321) wherever I6 is invoked. In particular, theory_E2 (ii) "give the square part of Dev_7 exactly and rigorously small" must carry this scope.
  * Note that the members' square parts Σ_{t∈M}|Δ_t|² ≤ Σ_{t≠0}|Δ_t|² = dΣ|δ_u|² (Parseval, Δ₀ = 0). That is what makes I6 relevant to Dev.

### Heuristic: frozen R′ (TRACE-206) fails at m ≈ 300–400; amendment R′_A: **ACCEPT AFTER FIXES (wording)** (B9)
* The ingredients check out:
  * μ = 1.915473;
  * r_tw = 1.283714 (float; referee ARPACK confirms);
  * √λ/μ = 1.26038;
  * growth (μr/√λ)ᵐ = 1.0185ᵐ.
* A referee envelope fit of |Dev₇|/(mh) over m = 21..123 gives slope e^{0.0190}. Extrapolated: ≈ 0.2 (m = 300), ≈ 1 (m = 400), ≈ 6 (m = 500), consistent with the REPORT's 0.3 / 8.
* S3.5 ("Status: heuristic") and S3.6 ([C]) label it conjectural. But:
  * (a) The S3.0 headline "**it does not survive asymptotically; amend**" is a verdict. Change it to "is expected (heuristically) not to survive; we propose an amendment".
  * (b) "contributes ≈ C·1.0187ᵐ/m² to W′/m" is wrong. The contribution to W′/m is Dev/(mφ) ~ 1.0187ᵐ/**m**. The 1/m² belongs to Dev/(m²h), and the 0.3/8 extrapolation itself uses 1/m.
  * (c) Say that the data m ≤ 123 do **not** show the growth: the envelope is flat, and the predicted change over 21..123 is only ×1.1. The extrapolation rests entirely on the float spectral rate r_tw = 1.2837 > 1.2604, a 1.9% margin, uncertified (no lower-bound certificate).
  * (d) Add the missing caveats:
    * only the (±2,8) primaries were modelled at d = 7; the (±2,16) d = 7 members and other levels are not;
    * the two ρ partly cancel at some m (e.g. m = 33, 51, 105);
    * the leading twisted coefficient must be nonzero;
    * W′_A must not compensate.
  * (e) S3.6 "[C] … R′_A holds; W′^A = O(1)" should read "conjectured: R′_A; W′^A = O(1) (weak evidence)".
  * (f) "0.007–0.021 for m = 21..45" holds for the larger of the two ρ only; (−2,8) gives 0.0007 (m = 33) and 0.003 (m = 45). Say "up to 0.021".
  * (g) This is not a disproof under TRACE-206's closure condition. The registry state of TRACE-206 must stay **open**. R′_A is a proposal for the maintainers, not a replacement of the frozen pre-registered definition.

### theory_E2 Routes A/B/C: **ACCEPT AFTER FIX** (B9 cont.)
* The numbers check out: Σ_j|J_j(1.8)| ≈ 2.37, so 2.37² ≈ 5.6ᵐ; log√λ = 0.881.
* "barrier [P]" labels are overstatements. They show that one specific inequality chain fails, not that no proof exists. Relabel as [assessment].

### Lean `lean/LineI.lean`: **ACCEPT**
* Compiles, EXIT 0, no warnings. No sorry, native_decide, axiom, or extern.
* Axioms: propext, Classical.choice, Quot.sound.
* Indexing caveat: the Lean `d` is p−1 (Fin (d+1)). Nprof is not tied to ZMod-p counts except via `norm_count_7` / `norm_count_23_zero`. The REPORT says this.

### Empirical [N] claims (W′_act table, halo, shape space): not re-run beyond m = 9
They are labelled [N]. Wording: "the bulk is RMT to 0.1%" means "the mean of |Z|²/RMT on the 'rest' set is 0.999 at m = 17". Say that.

## 3. Required fixes (blocking)
1. **B1** I6 constant: 6.768e6 → **6.769e6** (true 6 768 179.6). Print outward-rounded constants in bounds_sq; rate ≤ 0.87089ᵐ.
2. **B2** §0: "proved and Lean-checked" → "proved; algebraic core Lean-checked".
3. **B3** Prop I2: state that Σ_{t≠0} includes one non-unit dilation. Give member Dev = 900.47 next to cross/square 877.61/319.51.
4. **B4** Add the one-line proof of cyclic invariance (λᵐ ≡ 1 mod 2h ⇒ x_{m−d} ≡ x_d) for Ẑ(λβ) = Ẑ(β).
5. **B5** Thm I4: fix the quantifiers (same Y(m) in (E″) and (T″), or uniformity), and state the unit normalisation.
6. **B6** Lemma I5: fix the sign (C(k), c_{[P(n)−P(n′)]}). Restrict to all ν mod 2h, or add the unit-restricted diagonal term Σ_k c_k c_{2h}(k) and drop "purely off-diagonal / invisible" for unit sums.
7. **B7** Prop I8: state disjointness, RMT_m ≤ 4m and N_res ≤ φ. Change "exactly" to "reduces to".
8. **B8** I6 proof chain: c_m = 1−λ⁻ᵐ; cite TRACE-197 (+ the TRACE-207-style finite-state remark); update the numeric check; carry the scope into theory_E2 (ii) and S3.0.
9. **B9** Heuristic wording (a)–(g) above. Route A/B labels [P] → [assessment]. TRACE-206 stays open.

## 4. Recommended (non-blocking)
* **R1** I6 tail beyond m = 1425: add the one-line monotonicity argument, e.g. (CV·1.45ᵐ+CE)² ≤ (CV+CE)²·1.45^{2m}, h_m ≥ (1+√2)ᵐ/2 − 1, and lnln h ≤ ln m.
* **R2** Provenance:
  * `gstates.py` hard-codes `sys.path.insert(0,'/workspace/bgs-lineI/code')` and imports law from there, while the build JSON records the sha of `cert/law.py`. They are identical now (877a95a5), but this is fragile: import from its own directory.
  * Record the sha of `run_sq.sh`. It was edited at 21:29:34; the first build started at 21:29:35, so this is consistent.
* **R3** Upgrade "P(n) ≡ y′Nm(α_n) mod h [N]" to [P] mod 2h (one line, §2).
* **R4** Write out the proofs of the case reduction and of 7 | h ⟺ m ≡ 3 (6) (§2).
* **R5** Note ε = +1 for every d | h_m (odd m). Fix the Lean docstring (`norm_count_23` → `norm_count_23_zero`).
* **R6** Keep or regenerate one V matrix: the referee's regenerated V_1_3/E_1_3 matrices are byte-identical and stored in `/workspace/audit/lineI/data/`.
* **R7** S3.4 writes "F·R" for what is F at radius R. Harmonise with Line H notation.

## 5. Files (`/workspace/audit/lineI/`)
* code/:
  * `own_rig.py` (independent rest certificate);
  * `brute.py` (definition-level Ẑ);
  * `ptrace.py`, `trfull.py` (partial traces);
  * `i2prime.py`;
  * `cases.py`;
  * `topeig.py`.
* cert/: author copies (sha in `logs/SHA256_author_copies.txt`). `certG_small_TESTONLY.py` is a tail-assert-disabled copy used only for the Nmax = 2 comparison.
* out/: `own_V_1_3.json`, `brute_m9_L2_nu1045.{npy,json}`, `bruteW_*.npy`.
* logs/:
  * rebuild_*, own_rig_V_1_3, trfull_m9, trchk_E_1_3_m9, zpred_m9_rerun, zpred_m9_L2, verify_coset_rerun, topeig_V_1_3, bounds_sq_rerun;
  * lean.out, lean_clean.out, lean_clean2.out (EXIT=0);
  * SHA256_audit.txt.
* bsq/: bounds_sq rerun (identical JSON).
* data/: rebuilt V_1_3 / E_1_3 matrices (sha-identical to the author's provenance).

---------------------------------------------------------------------------------------------------------------
# DELTA REVIEW (session 4) — referee, 31 Oct 2026, ~02:05 UTC+5

Objects: REPORT_session4.md, REPORT_v2.md, theory_E2_v2.md, theory_session4.md, NOTES.md (after 00:40), sym/, dom/, cert_v2/, cert2/,
lean/LineI_v2.lean.  All re-runs in /workspace/audit/lineI/delta/ (nice -n 10; /workspace/bgs-lineI untouched; copies + sha in
delta/logs/SHA256_copies.txt).

## D-1. Application of first-round fixes B1–B9, R1–R7 — ACCEPT
* B1: CV 6 768 179.601… → 6.769e6, CE 68 586.18 → 6.859e4, q = 0.8708840… → ≤ 0.87089: outward everywhere (REPORT_v2 S3.4, cert_v2).
  No stale "6.768e6" anywhere in the v2 files.
* B2–B5, B8, B9 (Thm I4 quantifiers, Lemma I5 sign/unit restriction, heuristic labels, /m not /m²): applied in REPORT_v2 / theory_E2_v2.
* Lemma I5′: checked. (a) all ν: Σ_{ν mod 2h} e(kν/2h) = 2h·1[2h|k], so the diagonal (P ≡ P′) part is C(0)·2h·Σ_j c_{2hj};
  (b) units: Σ_{ν unit} e(ν(k−P+P′)/2h) = c_{2h}(k−P+P′) (Ramanujan sum). Both correct.  The author's extra withdrawal
  ("diagonal meets every c_{2hj}, not invisible") is CORRECT and was a defect my first report missed; the stated remaining inputs
  (equidistribution with a rate; C(0) = O(m)) are the right ones and are correctly labelled unproved.
* R2: cert_v2/gstates.py inserts its own directory on sys.path before `from law import mdata` — applied.
  R6: cert_v2/logs/R6_stored_matrices.txt designates /workspace/audit/lineI/data/{V,E}_1_3 with shas = provenance — applied.
  R1, R3, R4, R5, R7 applied. Lean: LineI_v2.lean differs from v1 only in the docstring (norm_count_23 → norm_count_23_zero);
  recompiled against bgs-int formalization: EXIT=0, axioms {propext, Classical.choice, Quot.sound} only (delta/logs/lean_v2.out).
* Wording nit: REPORT_v2 l.49 "Equivalent alternative: (T″) for EVERY Y(m)… (E″) for each fixed K, diagonal choice" — this is an
  alternative SUFFICIENT hypothesis, not an equivalent one (→ fix DF1).

## D-2. Monomial intertwiners (sym/) and Theorem I6 v2 — ACCEPT
* Symbolic: with K = complex conjugation on the (real-centred) weighted Hardy space, conj ĝ(n) = (−1)^n ĝ(n) gives
  K(ĝ e(Cn²/2) M_{Cn} C_n)K = (−1)^n ĝ e(−Cn²/2) M_{−Cn} C_n, i.e. K M_C K = M_{−C} up to the diagonal sign absorbed by X;
  the d=7 twist is conjugated β ↦ −β; the reflection R H_n R = H_{−n} with symmetric rounding and |c|-dependent weights.
  These are identities between the TRUE (infinite) operators, not Galerkin artefacts: every ingredient (Hardy weights, disc
  centres, rounding rule, alphabet) is invariant under the monomial map; finite sections are mapped onto finite sections of the
  same K-cut, so the Galerkin identity is the restriction of the exact one.
* Transfer: unitary ⇒ spectrum, resolvent norms, trace norms identical; antiunitary J ⇒ spectrum conjugated (moduli, counts,
  multiplicities preserved), ‖J R(z) J⁻¹‖ = ‖R(z̄)‖, trace norms preserved. Hence all Session-3 certificates transfer.
* Re-runs: sym/monomial_intertw.py → JSON identical to the author's (all 8 mod-24 cases have linear + antilinear witnesses,
  reflection exists). Own Galerkin check (delta/code/galcheck*.py, K=8, full alphabet): (15,−2) 1:3 = U·conj((9,2) 6:4)·U⁻¹,
  (21,2) linear, (27,−2) both orientations, reflection R⊗Y — all to ≤ 1.2e-16; negative controls (linear in place of antilinear;
  unsigned reflection) deviate by 1.16 / 1.13.
* m=15, a=−2 direct cross-check (cert2/): independent build + rest certificate gives F(V,1.45) = 0.356981366179695,
  F(E,1.0) = 0.0138326 — equal to the m=9 values, as the exact intertwiner predicts.
* bounds_sq_v2 (redirected copy): log identical, JSON identical except code sha; outward rounding confirmed; first m with all
  bounds < 0.01 is 321 (0.004574; m=315 gives 0.01046). Tail m ≥ 1425 ≤ 4.611e-69 (claimed ≤ 4.7e-69, safe): argument checked
  (h ≥ (1+√2)^m/3, lnln h ≤ ln m, monotonicity ln q + 1/(m ln m) < 0). Theorem I6 v2 for all m ≡ 3 (mod 6), ρ = (±2,8): ACCEPT.
* Fragility (non-blocking): bounds_sq_v2.py writes to a hard-coded absolute path in the author's tree (→ DF2).

## D-3. Theorem I9 [CA] (dom/rig_dom3b.py) — ACCEPT AFTER FIXES (DF3–DF5; none changes the result)
* Grid argument: rigorous. The resolvent at grid points z_f (the exact float points actually used, evaluated in arb) is bounded by
  ‖R_Λ‖ + ‖R_Λ M‖ + ‖R_Y‖ with M = b12 R_Y (float vector sum, error err0 incl. Neumann tail rows[p]·SY/Rm^p); between grid points
  the first resolvent identity gives ‖R(z)‖ ≤ g/(1 − |z−z_f| g), with covering radius hcov = Rπ/Ng(1+1e-6)+1e-12 and the check
  hg = hcov·gmax < 1 (0.302 at R=1.262); monotonicity in g makes the use of gmax valid. Neumann on Y at Rm = R(1−1e-13) puts σ(Y)
  inside. This is exactly the Lipschitz/second-resolvent control required.
* Deflation: Householder basis, κ = Π max(1,|1−τ_n|)/(1−dev), residual E = HA − B̃H with (1+2u) cover of the float subtraction —
  correct. Λ (3×3) roots isolated by acb_poly (hence simple, all |·| > R); homotopy F < 1 counts as in Line H.
* Z/3 argument: S = diag(ω^i) on the 3 cyclic components gives S V S⁻¹ = ωV exactly (incl. the wrap block 2→0, ω^{−2} = ω),
  so σ is ω-invariant with multiplicities; a 3-element invariant multiset avoiding 0 is a single free orbit {μ, ωμ, ω²μ}, all simple.
  Correct; it transfers to all m ≡ 3 (mod 6), ρ = (±2,8) via D-2 (antiunitary case gives the conjugate orbit).
* Upper bound |μ| < 1.45 comes from the Session-3 rest certificate on the same true operator (same K0, ρ, β) — fine.
* RE-RUN (class 2:1, R = 1.262): rebuilt V36_2_1 mid/rad sha identical to the author's (5fd0d9c6…/0f3e8114…). rig_dom3b:
  certified, count = 3, F = [0.6489779088 ± 3.6e-12] (author 0.6488989), hg = 0.3023, err0 = 8.0e-8, 520 s. The small F difference
  comes from a different ARPACK eigenvector ordering → a different Householder basis, so this is a semi-independent confirmation.
* Gaps:
  - μ₀ = 1.915473 is a float in Line I. The conclusion "1.262 > √λ/μ₀" needs a certified μ₀ > √λ/1.262 = 1.91300. Line F (F2)
    certifies |μ*| ∈ [1.9154712, 1.9154752] ⇒ √λ/μ₀ ≤ 1.260378 < 1.262 — must be CITED with the identification that Line F's μ*
    is the leading eigenvalue of the same untwisted (±2,8) operator (→ DF3).
  - `if g > gmax` uses arb comparison, which is False on overlapping balls, so a ball with a larger upper end can be skipped.
    Effect ≤ ball radius (~1e-30 relative), but it is on the unsafe side (→ DF4).
  - Λ-block moduli 1.2837143 / 1.2835951 are NOT certified enclosures of |μ| (they are eigenvalues of the deflated 3×3 block);
    the certified statement is 1.262 < |μ| < 1.45. Session4 S4.2 says this once; make it explicit in the theorem (→ DF5).
* Implications: as stated in S4.2 ("EITHER c(β) = 0 OR limsup|Ẑ(β)|^{1/m} = |μ| > 1.26038 along m ≡ 0 (3)"; "no proof of (D) at
  d=7 via r_tw < √λ/μ₀"; c(β) ≠ 0 not certified; frozen R′ not disproved) — NOT overstated. Keep exactly this wording.

## D-4. theory_session4.md — Möbius identity ACCEPT; prime support ACCEPT AFTER FIXES (DF6, DF7)
* Aliasing identity [P]: (1/q)Σ_{ν′ mod q}|Z_m(ν′/q)|² = Σ_j C_Z(jq) (orthogonality, absolute convergence from Σ|Φ̂| < ∞), and
  Möbius over units: F = (1/φ(2h)) Σ_{e|2h} μ(e)(2h/e) Σ_j C_Z(j·2h/e). Verified line by line: correct.
* Overstatement (l.13–14): "the dilation/resonance terms of TRACE-206 are EXACTLY the large-e (small q) aliasing sums". The e > 2
  Möbius terms are sums of |Z_m| at exact rationals of denominator dividing 2h/e (i.e. NON-unit residues, subtracted out), whereas
  the TRACE-206 resonant residues are units ν with bν ≡ a (mod 2h), i.e. ν/2h = k/b + a/(2hb): near, not at, small-denominator
  rationals. Related through the G2 law, not identical. Also the "bulk = e=1,2 sum minus RMT" sentence is heuristic under a [P]
  heading (→ DF6).
* Prime support: h_m = V_m/2 for the Lucas pair α,β = 1 ± √2 ((P,Q) = (2,−1); α+β = 2, αβ = −1 coprime, α/β not a root of unity),
  U_{2m} = U_m V_m. BHV (2001): U_n has a primitive divisor for every n > 30, no exceptions — applies. A primitive p | U_{2m} does
  not divide U_m nor (α−β)² = 8, so p is odd and p | h_m; and p ∤ h_{m′} for m′ < m (h_{m′} | U_{2m′}). Hence every m ≥ 16 gives a
  NEW prime of h_m; infinitely many primes occur; for any finite S, h_m has a prime ∉ S for all but finitely many m. (Carmichael
  1913 already suffices for real Lucas pairs.) Numerically: every m = 2..60 has a new prime in h_m.
* What does NOT follow: "for m with a primitive prime p ~ h^c" (l.22–23) — existence of primitive primes of size h^c is not
  known (only p ≡ ±1 mod 2m, p ≥ 2m−1; Stewart-type lower bounds are far below h^c). It is also unnecessary: if h_m has any
  prime ∉ S then EVERY unit residue has reduced denominator 2h, which is not S-smooth. The S-arithmetic "obstruction" remains
  [assessment] (→ DF7).

## Numbered fixes (delta)
DF1  REPORT_v2 l.49: "Equivalent alternative" → "Alternative sufficient hypothesis".
DF2  cert_v2/bounds_sq_v2.py: output path via argument/relative to script (not hard-coded absolute).
DF3  Theorem I9 / S4.2: cite Line F F2 certified |μ₀| ∈ [1.9154712, 1.9154752] (⇒ √λ/μ₀ ≤ 1.260378) and state that it is the
     leading eigenvalue of the same untwisted ρ = (±2,8) operator; write "1.262 > 1.260378 ≥ √λ/μ₀".
DF4  rig_dom3b.py: replace `if g > gmax` by gmax = max of upper bounds (e.g. compare g.upper()) ; rerun not needed for acceptance
     (effect ~1e-30), but fix before the code is frozen.
DF5  State in Thm I9: certified |μ| ∈ (1.262, 1.45); Λ-block moduli 1.28371 / 1.28360 are floating diagnostics only.
DF6  theory_session4 S4.1: drop "exactly"; describe Möbius e-terms as non-unit (exact-rational) subtractions and resonances as units
     near rationals; mark the bulk sentence [assessment].
DF7  theory_session4 S4.2: remove "p ~ h^c"; state the proved consequence (new odd prime in h_m for every m ≥ 16; any finite S
     fails for all large m); optionally cite Carmichael 1913 alongside BHV.

## Verdict
(1) ACCEPT.  (2) ACCEPT (Theorem I6 v2 for all m ≡ 3 mod 6, ρ = (±2,8)).  (3) Theorem I9 ACCEPT AFTER FIXES DF3–DF5 (DF3 is
required for the "> √λ/μ₀" clause; the counting result itself is certified and independently reproduced for 2:1).
(4) Möbius identity ACCEPT [P]; prime-support ACCEPT AFTER FIXES DF6–DF7.
Delta artefacts: delta/logs/{bounds_sq_v2_rerun.*, monomial_intertw_rerun.log, galcheck*.log, sha_V36_2_1.txt,
V36_2_1_dom3b_rerun.{log,json}, lean_v2.out, SHA256_copies.txt}.
