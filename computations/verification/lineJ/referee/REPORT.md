# Referee report — BGS Line J (d = 7 twisted coefficient in frozen R′, TRACE-206)

Referee: Grok Bot (independent, adversarial). Date 31 Oct 2026, 06:00–06:25 UTC+5.
Object: `/workspace/bgs-lineJ/` {REPORT.md, STRATEGY.md, NOTES.md, code/, logs/, data/cert/} as of 05:58 UTC+5.
Background used: Line I sources `/workspace/bgs-lineI/`, Line I referee reports `/workspace/audit/lineI/REPORT.md`,
`/workspace/audit/pr60/AUDIT.md`, Line F certificates (`/workspace/audit/pr60/computations/verification/lineF/`), and the repo at
main **195a24f9** (fresh read-only partial clone in `/workspace/audit/lineJ/repo`: TRACE-206 frozen definition, TRACE-212/213/215–220).
The author's tree was not modified (all three author SHA256 manifests still verify; the only files newer than my start are the
author's own new `J3/` directory, written by the author's running job, not by me). Nothing was pushed. All reruns ran with
nice -n 10 and 2 threads; outputs in `/workspace/audit/lineJ/rerun/` (manifest `rerun/SHA256_referee.txt`).

## Overall verdict: **ACCEPT AFTER FIXES** (F1–F11 below)

None of the fixes changes a number or the conclusion of Theorem J. The mathematics is correct. Every certificate I reran
reproduces. My independent code reproduces the per-residue table (M0, M1, K_j) exactly. The fixes are about rigour hygiene
(F1, F2), missing short proofs (F3, F4), and statements/wording (F5–F11).

| item | claim | verdict |
|---|---|---|
| 1 | Prop J-C: exact c(β); B_C formula; cancellation in s2/s6; doubling in s0/s4; W(−ρ)=conj W(ρ); sector antiunitary map; Q(ζ7) nonvanishing | **ACCEPT AFTER FIXES** F3, F4, F5 |
| 2 | Certificates [CA]: sector blocks, counts, rig_disc discs, 122 rest certs, \|μ₂:₁\| enclosure, \|ξ\| ≥ 2.4586893 > √λ | **ACCEPT** (fixes F1, F6 are cosmetic or documentation only) |
| 3 | Window lemma for θ = 168·arg ξ | **ACCEPT** |
| 4 | Theorem J, M0/M1/K_j table, completeness of the error budget in D7 | **ACCEPT AFTER FIXES** F1, F2, F7, F8 |
| 5 | §5: W′ = W′_A + φ⁻¹(D7+O_m), conditional and unconditional conclusions; 7\|m convention | **ACCEPT AFTER FIXES** (wording) F8–F10 |
| 6 | Numerics m = 201–453 | **ACCEPT** (F11 is a small wording fix) |

---

## 1. Exact part (Prop J-C) [P + P-check]

**Re-derivations (by hand).**
- *Sector law.* The 16-state monomial matrices A_n are unitary and 8-periodic in n. So the algebra they generate is a C*-algebra,
  and the orthogonal complement W of span{f_a} is invariant. If u ∈ span{f_a} then P_W u = 0, and
  ⟨u|X|e₀⟩ = Σ_a ⟨u|f_a⟩⟨f_a|X|f_a⟩⟨f_a|e₀⟩ for every X in the algebra tensored with the lattice and cycle factors.
  - The twist phase depends only on the cycle index, not on the automaton state (`gstates.finite`). So f_a ⊗ C³ is invariant, and
    V_{β,a} is exactly the operator with the automaton replaced by e(an/8) (`gstates_sector.py`, one state).
  - The cycle factor gives Tr(block 0) = ⅓ Tr V^m for 3 | m. V^m commutes with S = diag(ω^i), and its diagonal blocks are cyclic
    rotations of one product.
  - Consequence: c(β) = c_a with |c_a| = ½ (an 8th root of unity over 2). Correct.
  - Remark: the sector operators do not depend on the case (m mod 24) at all. Only C = −4a c₀/8 (the sign a = ±2) and β enter. So
    "the other cases follow by exact symmetry" is in fact trivial, and all case dependence sits in c_a(case, ρ).
- *Sector antiunitary map.* I re-derived the map directly on the sector operators.
  - Complex conjugation K: conj ĝ(n) = (−1)ⁿĝ(n), K M_C K = M_{−C}, and the composition part is real. The phase e(Cnc/2) is
    conjugated consistently, the twist goes to e(−nτ_i(β)/7) = e(nτ_i(−β)/7), and the sector scalar becomes e(−an/8).
    Hence K V^{(C)}_{β,a} K = V^{(−C)}_{−β,4−a}, using (−1)ⁿ = e(4n/8).
  - Reflection n → −n, u → −u, c → −c: ĝ(−n) = ĝ(n), rounding is symmetric (λ is irrational, so there are no ties), and the cores,
    weights and edge rule are symmetric. This sends (4−a, −β) to (a−4, β).
  - So σ(V^{(−2)}_{β,a+4}) = conj σ(V^{(+2)}_{β,a}), with multiplicities, and the same holds for E. This is exactly the report's
    claim, and it is consistent with TRACE-216 (X, Y, J) restricted to sectors.
- *B_C.* conj Z₊·Ẑ₊·W₊ + conj Z₋·Ẑ₋·W₋ at leading order equals c_m²[c₀ᶠc⁺ξ^mW₊ + conj(c₄ᶠ c⁻ ξ^m W₊)]. Its real part is
  c_m² Re(ξ^m W₊ (c₀ᶠc⁺ + c₄ᶠ conj c⁻)), and c₄ᶠ = −c₀ᶠ gives B_C = c₀ᶠ(c⁺ − conj c⁻)W₊. Correct.
  - s2/s6: c⁺ = c⁻ = ½, so B = 0.
  - s0/s4: c⁺ = −conj c⁻, so |B| = |W|/2.
  - This cancellation has to be **exact**: the 1:3 rate (|μ₁:₃| ≥ 1.2837142) exceeds the 2:1 rate (|μ₂:₁| ≤ 1.2835953). It is
    exact, because it comes from an identity between the true operators, not from the certificates.
- *W(−ρ) = conj W(ρ).* conj G_t(β) = G_{−t}(−β), and C = −C. I re-derived from the frozen rule that M₇(ρ) = {ν₀ + (2h/7)j : 1 ≤ j ≤ 6,
  ν unit}: 8ν ≡ a (mod 2h/7) ⇔ ν ≡ ν₀ (mod h/7), and odd ν forces an even multiple. Also ν₀(−ρ) = −ν₀(ρ) (mod 2h). Correct.

**Reruns / independent checks.**
- `sectors_exact.py` and `exact_B.py` (in copies, outputs redirected): both print ALL EXACT CHECKS PASSED, and the JSON content is
  identical to the author's.
- Own random-word test of the sector law, exact in Z[ζ₈] (`rerun/code/ref_exact.py`): 3200 words over all 8 (case, sign) pairs.
  ⟨u|A_{n_k}⋯A_{n_1}|e₀⟩ = Σ_a c_a e(a Σn/8) with 0 failures.
- |W_C| in arb from the exact Z[ζ₇] histograms: max relative difference to the author's doubles is 1.1e−15, against a margin of 1e−9.
  - The four values are exactly (12/49)cos(kπ/7) for k = 1, 2, 3, and 6/49 when 7 | m.
- Galerkin-level check of the sector map (`rerun/code/ref_conj.py`): for all 64 pairs (V and E, 4 sectors, 8 classes), V^{(−2)}_{s+4}
  and conj V^{(+2)}_s have identical sorted |entries| (difference ≤ 2e−41), equal Frobenius norms (difference ≤ 1.8e−15), and top-6
  eigenvalues conjugate to ≤ 7.7e−15. The disc centres of the −2 blocks are conj(ω^k ·) of the +2 centres to ≤ 1.7e−10, far inside
  2r = 2e−7.
- The cancellation is also confirmed against data that does not use the sector theory. With B₁:₃ = 0, `model_lead.py` reproduces the
  Line I exact-law cross term (zpred). The relative error is 3e−7 at m = 123, 1.7e−5 at m = 63 and 6.6e−4 at m = 39 (subleading terms).
  At these m the 1:3 and 2:1 rates are equal to 1e−4, so a non-cancelling 1:3 term would be an O(1) error.

**Fixes.**
- **F3 (periodicity is asserted, not proved).** W and the member sets are checked only on 3 periods (`exact_B`; my extension covers 16
  periods, 894 checks, 0 mismatches). A proof is two lines, so add it:
  - (h_m, y′_m) are the coordinates of (1+√2)^m (verified; h_m = V_m/2, TRACE-219).
  - The order of 1+√2 modulo 49 is 42 (computed), so (h mod 49, y′ mod 7) has period dividing 42.
  - ν₀ ≡ ±2 (mod 7) is constant, so the excluded j and the labels t = jy′ (mod 7) have period dividing 42.
  - The sector constants depend only on m mod 24. κ depends only on m mod 8 (my check covers m ≤ 3999, and κ is not needed; see F4).
  - Hence everything entering B_C has period dividing 168.
- **F4 (source of c₄ᶠ = −c₀ᶠ).** Cite it from the exact sector table, not from the κ formula:
  - c₄^{(case,−2)} = −c₀^{(case,−2)} in all 4 cases (`sectors_exact.log`), and Line F's top sits in sector 4 (−2) and sector 0 (+2,
    after conjugation; pr60 AUDIT item 4).
  - Hence c₀ᶠ = conj c₀^{(case,+2)} = −c₄^{(case,−2)} = −c₄ᶠ [P-check].
  - `check_z0.py` (rerun) confirms this numerically for all four κ ∈ {1,3,5,7}, with ratios 1 ± 1.2e−7.
- **F5 (scope of "cancels").** B = 0 is exact for every orbit in sector 2 or 6. That the *tops* of 1:2 and 1:5 lie in s6 is float-only
  [N]; it is not certified and not used, since those classes are handled by rest certificates. Say so in §0.1 and §3.
  - Also write out the sector-level K/R derivation above in the report. It is currently three lines and is the crux of the
    cancellation (the author's caveat 2).

## 2. Certificates [CA]

**rig_disc.py: line-by-line review (diff vs the audited rig_dom3b v3).** Sound.
- *Contour.* |z − c| = r, with c the float midpoint of an arb charpoly root of Λ.
  - `ins` and `outs` are arb comparisons (True only when decided). They require exactly one Λ root inside and k−1 outside.
  - The charpoly roots are isolated by acb_poly, so they are simple.
- *σ(Y) outside the disc.* Neumann validity N[p]/zmin^p < 1 at zmin = (|c|−r)(1−1e−13) gives ρ(Y) < zmin. The disc lies in
  {|z| ≥ |c|−r}.
  - All Neumann-derived bounds (SY, err0 including the rows[p] tail) decrease in |z|, so evaluating them at zmin is valid at every
    grid point.
  - The slack 1.28e−13 exceeds the float error of the grid points (~3e−16).
- *Resolvent bound.* The pointwise bound g = ‖R_Λ‖ + ‖R_Λ b₁₂R_Y‖ + ‖R_Y‖ is evaluated at the exact float points.
  - KM = (‖R G R^H‖_F + …)^{1/2} bounds the operator norm, since ‖P‖₂ ≤ ‖P‖_F.
  - The resolvent identity is used with hcov = πr/Ng(1+1e−6) + 1e−14, and 1e−14 ≫ the float misplacement of the grid points.
  - gmax is taken over exact upper ends (DF4 fixed).
- *Homotopy.* fullR(Rc, zmin): the 1/|z| terms (the zero block of the comparison operator, Xn) are bounded at zmin ≤ |z|. The 0
  eigenvalue lies outside the disc.
  - pertT = Galerkin (δ₁+δ₂+Δ+ε_A) + κ(ε_H + ‖b₂₁‖), and F = pertT·fullR < 1.
  - Hence exactly one eigenvalue with multiplicity in the disc. Together with the count certificate (|c|−r > R checked) and Z/3 this
    gives σ ∩ {|z|>R} = {μ, ωμ, ω²μ}, all simple. Correct.
- *Builder.* `certG_build_sector.py` differs from Line I dom_v3 `certG_build.py` (audited) only in the import and the provenance.
  - The trace norm uses NS = 3 (one sector state × 3-cycle), which is correct for a unimodular scalar factor.
  - The Galerkin bounds do not depend on the state factor.
  - `rig_dom3b.py` (e4ff0f7f) and `rig_spec.py` (f346e22c) are byte-identical to the audited versions.
- *Provenance.* All 402 build-JSON, mid and rad hashes recorded in the 134 certificate JSONs match the current files.

**Reruns** (`rerun/cert/`):

| certificate | referee result | author |
|---|---|---|
| disc 2:1 (+, s4) r=1e−7 | certified, F = 0.193706, \|μ\| ∈ [1.2835950326, 1.2835952326] | F = 0.193707, same enclosure |
| disc 2:1 (−, s0) | certified, F = 0.193811 | 0.193810 |
| disc 0:1 (+, s0) | certified, F = 0.198117 | 0.198116 |
| disc 1:3 (+, s6) | certified, F = 0.198264 | 0.198264 |
| disc 2:1 (+, s4), **other orbit member**, r = 5e−8, p = 48 (referee variant) | certified, F = 0.389, \|μ\| ∈ [1.28359508, 1.28359518] (tighter, consistent) | — |
| count 2:1 (+) R=0.8; 1:3 (+) R=1.0; 0:1 (−) R=0.9 | certified, k = 3, F = 5.16e−7 / 1.16e−6 / 9.14e−7 | same to 1e−5 rel. (ARPACK basis) |
| 12 rest certs (9 V at p=64 incl. both R = 1.247 cases and the two slowest; 3 E) | all certified, F_R2 bit-identical | identical |

- Negative control built in: r = 1e−9 is refused (roots not separated), and r = 1e−8 fails (F ≈ 2). So the test is not vacuous.
- The rest-cert JSONs used by `assemble.py` are the p = 64 reruns: 58 V certs at p = 64, plus 64 E certs.
- **F6 (documentation).** "Galerkin pert ~7e−13" is the builder error only. In the count and disc certificates the total
  perturbation is pertT ≈ 2.37e−10, dominated by the deflation residual ε_H ≈ 2.36e−10. The F ≈ 0.19 values already include it.
  Quote pertT in the §2 table.
- |ξ| ≥ 1.9154712 × 1.2835950326 = 2.458689323 > √λ = 2.414213562, and growth ≥ 1.018422463. Reproduced in arb.

## 3. Window lemma [P] — ACCEPT
- A closed arc of length L ≥ θ cannot be jumped by steps of length θ. Starting outside it, the first entry happens after
  ≤ ⌈(2π−L)/θ⌉ ≤ ⌈2π/θ⌉ − 1 steps, so N = ⌈2π/θ_lo⌉ consecutive k suffice. The same works around π. Correct for θ ∈ (0, π].
- B₂:₁ is constant along m ≡ j (mod 168) (F3). So α = arg(B ξ^{m₀}) is fixed and the phase advances by 168·arg ξ.
- θ ∈ [1.130677114, 1.131054118] and cos(θ_up/2) ≥ 0.8443062873, N = 6. Reproduced with arb, using arg error asin(r/(|z|−r)) for
  both discs and the Line F centre taken **from its decimal string** (cf. F1).

## 4. Theorem J and the assembly — ACCEPT AFTER FIXES

**Completeness of the error budget (re-derived).** D7 = Σ_ρ(cross_ρ + sq_ρ) exactly, by Prop I2′ (|ω_t| = 1). cross_ρ =
2Re(conj Z_ρ Σ_C Ẑ_C W_C) runs over all 8 classes (48 β ≠ 0). With conj Z = c_m(L₁ + ε₁) and Ẑ_C = c_m(L₂ + ε₂), every
non-leading product is bounded by (|L₁|+|ε₁|)(|L₂|+|ε₂|) − |L₁||L₂|. That is exactly `errp`, and it covers:
- Z₀ subleading: |ε| ≤ H₀ = 2(T_V+T_E) = 1506.18, uniformly in m, because Line F has r₂ = 1 (TRACE-199: ½·4·r₂^{m−1}(T_V+T_E)).
- All non-top eigenvalues of all 64 V and 64 E (class, sector, sign) blocks: Lidskii + Weyl, Σ|λ|^m ≤ R^{m−1}‖·‖₁, with factor
  |c_a|·⅓ = 1/6.
- The leading 2:1 and 0:1 terms; and 1:3 exactly cancelled (only its cross products with ε remain, and they are included).
- Classes 1:2 and 1:5 are treated as rest (R = 1.247), which is conservative.
- sq ≤ Σ_ρ 6((6/7)Σ_C|Ẑ_C|)², from |Δ_t| ≤ 7⁻²·7·6Σ|Ẑ_C| and |G_t| = 7.
- Galerkin errors are inside every certificate.

Nothing in D7 is missing. Monotonicity of bracket/ξ_lo^m holds because every subtracted rate is below ξ_lo:
0.98351375 (0:1), 0.97149223 (MSU·1.247), 0.52211330 (μ₁:₃, the H₀ term), and 0.67024436 (square). Reproduced. The bounds
φ(2h) = φ(h) < h < λ^{m/2}/2 hold: h is odd since h² + 1 = 2y′², and 4h² = λ^m + λ^{−m} − 2. Checked for m ≤ 2997.

**Independent reproduction** (`rerun/code/ref_assemble.py`, my own arb code reading the certificate JSONs; W from exact
histograms; Line F centre from strings). All 28 residues give **identical M0(j) and M1(j)**. My K_j⁺ are ≥ the author's table
values, which carry the 10⁻³ margin; for example j = 3: 0.27385 vs 0.2736, and j = 129: 0.042041 vs 0.042. The author's
`assemble.py`, rerun in a redirected copy (`rerun/code/assemble_redirect.py`, output path changed only), reproduces its log
byte-identically, and the JSON residues, summary and rates are identical.

**Fixes.**
- **F1 (outward rounding).** `assemble.py` l.18 builds μ* from Python float literals (error ≲ 1.1e−16) and then uses
  r = 2e−6 + 1e−30. Use strings, as I did, or r = 2e−6 + 1e−15. The effect on θ is ~2e−14, so nothing changes.
- **F2 (W in double).** Compute |W| in arb from the exact histograms (as above) or quote the closed form with its proof. The
  reproduction shows the 1e−9 margin is safe (actual error 1.1e−15).
- **F7 (m⁻ statement).** §3 item 2 states the m⁻ bound as "≤ −K_j·1.0184^m/m + sq/(mφ)". That is not the form claimed in §0,
  and sq/(mφ) is not controlled (there is no lower bound on φ).
  - The correct manipulation: 2c_m²·bracket − sq < 0, then divide by φ < λ^{m/2}/2.
  - With sq absorbed, K_j⁻ = 2(2c²·bracket − sq)/ξ^{M0}. It equals K_j⁺ to 5 digits for every j (sq rate 0.670) and is ≥ the table K_j.
  - So the symmetric statement "D7(m^±)/(mφ) ≷ ±K_j·1.0184224^m/m" is TRUE as tabulated. Restate item 2 accordingly, noting that
    (2c²·bracket − sq)/ξ_lo^m is also increasing.
- **F8 (hypotheses to state).** In Theorem J / Corollary J, state:
  - (i) The frozen cut-off includes level 7 (|Z_ρ|²/49 ≥ 4m). This holds for all m ≥ 13 by TRACE-199.
  - (ii) The inputs used as [P] from earlier lines: TRACE-197 lifted trace identity, TRACE-212 (I2′), the TRACE-216 symmetries,
    and TRACE-198/199 (μ*, H₀).

## 5. Section 5 and STRATEGY — ACCEPT AFTER FIXES (wording)
- The identity W′ = W′_A + φ⁻¹(D7 + O_m) is correct: TRACE-213 together with §9.3 of the Line I note gives W′ − W′^A = φ⁻¹ΣDev
  over included (ρ, d).
  - O_m contains the other levels (including d = 49, 7p, … when present), all (±2,16) levels, and their square parts.
  - W′_A ≥ −4m, since RMT ≤ 4m and |Z|² ≥ 0 (Prop I8). So Corollary J follows: W′/m ≥ D7/(mφ) − C − 4 along m⁺. Correct.
  - The unconditional statement (R′ ∧ R′_A ⇒ φ⁻¹O_m/m unbounded in both directions) is correct.
  - The report does **not** claim a refutation of R′. TRACE-206 must stay open; the report says this correctly.
- *7 | m residues.* When 49 | h the six dilations are all units (ν ≡ ν₀ ≢ 0 mod 7). Under the frozen rule M_d(ρ) (d′ = 1 the only
  proper divisor), the d = 7 level has exactly these 6 members. So this is not a "convention" but the frozen definition itself.
  Say so (caveat 5 can be closed). Prop I2′ is stated for every odd d | h, so it applies.
- **F9.** §0.3: "Equivalently: frozen R′, R′_A and O_m = o(mφ) cannot all hold" should read "In particular"; it is weaker than the
  one-sided corollary.
  - §3 last sentence: "grows at rate ≥ 1.0184224^m/m" should read "is ≥ K_j·1.0184224^m/m in absolute value, with each sign, for at
    least one m in every 6 consecutive terms of each class j ≥ M0(j)". It is not a statement for every m.
- **F10 (STRATEGY).**
  - §1 "any proof of R′ must exhibit **exact** cancellation between levels" should read "must show that O_m compensates D7 up to
    o(mφ)". Exact cancellation is not required.
  - "Frozen R′ should be regarded as false [H, strongly supported]" should be "[assessment]". The uncontrolled O_m has unbounded
    prime support (TRACE-219).
  - The other [H] items are correctly labelled.

## 6. Numerics [N] — ACCEPT
- `numerics_large_m.py`, rerun in a redirected copy, gives a log **byte-identical** to the author's.
- Independent spot recomputation (`rerun/code/ref_numerics.py`) at m = 201, 249, 333, 375, 381, 435, 441, 447. It uses:
  - my own ARPACK spectra of all 128 D = 1980 blocks;
  - Z₀ from the exact sector constants (no κ);
  - my own Gauss sums and member sets in mpmath.

  Results: D7/(mh) = −0.0022816, +0.16361, −0.40942, +0.96901, −0.93932, +1.38147, −1.42615, +2.17538. These agree with the author
  to all printed digits. The square term is 1.7e−35 … 1.2e−76 relative.
- Leading-term amplitude check at m = 447: 2|B|(ξ/√λ)^m·2/m ≈ 2.39, against the observed 2.18. Consistent.
- The model checks reproduce (`check_model`, `check_z0`, `model_lead`).
- **F11.**
  - REPORT §1: "10⁻⁷ relative" should be "≤ 4e−7" (the maximum in check_model is 3.8e−7).
  - NOTES 06:20: "model matches exact cross to 1e−6 rel at m = 39..123" is 6.6e−4 at m = 39 and ≤ 2e−5 from m = 63 on.

## Numbered fixes
- F1 assemble.py: μ* centre from strings (or inflate radius by 1e−15); rerun (no change expected).
- F2 |W| in arb or closed form (12/49)|cos(kπ/7)|, 6/49 with proof.
- F3 Add the periodicity proof: ord_{49}(1+√2) = 42, (h, y′) = coords of (1+√2)^m, ν₀ ≡ ±2 (mod 7); hence period 42 | 168.
- F4 Cite c₄ᶠ = −c₀ᶠ from the exact sector table (+ Line F sector placement); make it [P-check].
- F5 Write out the sector-level K/R map proof. Mark the s6 placement of the 1:2 and 1:5 tops as [N] (not used).
- F6 Quote pertT ≈ 2.37e−10 (deflation-dominated) in the §2 certificate table.
- F7 Restate the m⁻ bound with sq absorbed (K_j unchanged; referee K_j⁻ ≥ table).
- F8 State the frozen cut-off for d = 7 and list the cited [P] inputs in Theorem J / Corollary J.
- F9 "Equivalently" → "In particular"; subsequence wording of the final proved statement.
- F10 STRATEGY: "exact cancellation" → "compensation up to o(mφ)"; "[H, strongly supported]" → "[assessment]".
- F11 Precision figures in §1 / NOTES.

## Referee artefacts (`/workspace/audit/lineJ/rerun/`)
- `code/ref_exact.py`, `code/ref_D.py`, `code/ref_kappa.py` → `logs/ref_exact.log`, `logs/ref_kappa.log` (sector law,
  W in arb, periodicity, h odd, κ).
- `code/ref_conj.py` → `logs/ref_conj.log` (Galerkin-level antiunitary map, 64 pairs).
- `code/ref_assemble.py` → `logs/ref_assemble.{log,json}` (independent Theorem J table).
- `code/ref_numerics.py` → `logs/ref_numerics.{log,json}`; `nl/logs/numerics_large_m.log` (byte-identical rerun).
- `run_certs.sh` → `cert/*.json|log` (6 disc, 3 count, 12 rest).
- `logs/sectors_exact.*`, `logs/exact_B.*`, `logs/check_z0.log`, `logs/model_lead.log`, `logs/check_model.log`.
- `SHA256_referee.txt`.

---

# DELTA2 (fixes F1–F11) and J3 — referee, 31 Oct 2026, from 08:02 UTC+5
(Work in progress; sections are appended as they are completed. Reruns in `/workspace/audit/lineJ/delta2/`.)

## DELTA2 — verification of F1–F11 (REPORT_v2.md, STRATEGY_v2.md, assemble_v2.py, fixes_checks.py)

`logs/SHA256_v2.txt` verifies. v1 files are unchanged (v1 manifests still OK).

Reruns, all in `delta2/`:
- `assemble_v2.py` in a redirected copy: its log is byte-identical to the author's.
- `fixes_checks.py`: its log is identical (ALL CHECKS PASSED).
- M0(j) and M1(j) are identical to v1 and to my independent `ref_assemble` for all 28 residues.
- K_plus and K_minus equal my K_j⁺/K_j⁻ to 5 digits, and both are ≥ the table K_j.
- The summary differs from v1 only in θ and c_window, at the 1e−14 level. This is the expected effect of F1, in the conservative direction (θ_up increases by 8e−15).

| fix | status |
|---|---|
| F1 | **Done.** μ* is built from the decimal strings. r = 2e−6 + 1e−30 is enough, since the Line F ball radius of b₁₁ is ≤ 5.5e−35. |
| F2 | **Done.** \|W_C\| = (Re² + Im²)^{1/2}/7⁴ in arb from exact integer histograms, with no margin. \|W(−ρ)\| = \|W(+ρ)\| is asserted to 1e−30, and the conj identity is exact in exact_B. |
| F3 | **Done.** Proof in §3 is correct: (h, y′) = coords of (1+√2)^m, ord₄₉ = 42, ν₀ ≡ ±2 (mod 7). fixes_checks verifies it for m < 400. |
| F4 | **Done.** c₄^{(case,−2)} = −c₀^{(case,−2)} exactly in 4 cases, with the sector placement from the pr60 AUDIT. |
| F5 | **Done.** The written K/R proof (§1) matches my derivation. The s6 placement of 1:2 and 1:5 is marked [N] and unused. |
| F6 | **Done.** pertT ≈ 2.37e−10 is quoted (§2 builder and table header). |
| F7 | **Done.** Symmetric statement; K_j⁻ = 2(2c²·bracket − sq)/ξ_lo^{M0}; monotonicity argued by rates. The code spot-check at M0+1008 is only a sanity check, which is fine. |
| F8 | **Done.** The cut-off (m ≥ 13 by TRACE-199) and the [P] inputs are listed. |
| F9 | **Done.** §0.3 now says "In particular", and §3 has the subsequence wording. |
| F10 | **Done.** STRATEGY_v2 §1 has both changes. |
| F11 | **Done.** REPORT_v2 says ≤ 4e−7, and NOTES has a dated correction entry (the original line is kept and flagged, which is acceptable). |

Residual nits (non-blocking, **DF8–DF10**):
- **DF8.** REPORT_v2 §5 "Caveats" 1 and 4 are stale. rig_disc *was* audited (referee REPORT §2), and W is no longer double precision. Mark both closed, as was done for item 5.
- **DF9.** Theorem J points to `logs/assemble.json` and `code/assemble.py`. It should point to the v2 files (the table is unchanged). The §5 file tables omit the v2 files, and §0.5 still points to STRATEGY.md rather than STRATEGY_v2.md.
- **DF10.** The window-lemma proof still writes ⌈(2π−θ)/θ⌉. It is correct, but ⌈(2π−θ_up)/θ⌉ is the sharper and more natural form. Optional.

**DELTA2 verdict: ACCEPT.** All of F1–F11 are applied correctly. Theorem J (Line J v2) is accepted, with DF8–DF9 as editorial fixes.

## J3 — review of `/workspace/bgs-lineJ/J3/` (written incrementally)

**Integrity.** `SHA256_J3.txt` verifies (1495 files).

**Incident (referee side, repaired).** `code/theta_big.py` writes to an **absolute** path, `/workspace/bgs-lineJ/J3/logs/theta_big.json`.
- At 08:05:40 UTC+5 my first rerun (in a mirror copy, with no arguments) overwrote the author's file with `{}`.
- I restored it from the byte-identical pre-run mirror copy within minutes. The manifest re-verifies: sha a6919288…, MANIFEST OK.
- I then reran it in the mirror with the path made relative and arguments 168 504 2520 27720 360360. The output is byte-identical to the author's.
- No other J3 script writes outside its cwd (checked by grep). See fix J3-F7.

**Reruns.** All in `/workspace/audit/lineJ/j3/` (`mirror/` is a copy of J3; logs are in `rerunlogs/`).
- `rat_excl`, `assemble16`, `primelevel_W`, `ranks`, `theta_big` and `inherit_proof_check`: json/log byte-identical to the author's.
- `inherit7q` finished (exit 0).
- Results for `blocks16_exact` and `wordtest16`, and the certificate sample, are given below.

### J3.1 (±2,16) blocks [P-check] and 576 rest certificates [CA]
- **Dedup check (referee, own code).**
  - The 32 representatives cover all 16×8 = 128 (case, block) pairs.
  - Every member has the same sign and an identical 2×2 monomial action table as its representative, and there are exactly 32 distinct keys.
  - The builder uses m only via g2params/reach, and these are not used by `gstates16_block`. c₀ = 1/(λ−λ⁻¹) and C = −4ac₀/16 are m-independent. So one build per (sign, action) is legitimate.
- **Conventions.** `gstates16_block.finite` gives A_n f_i = z^{ex} f_{perm(i)} via e(−ph/16), ph = −ex. This is consistent with the audited sector builder (e(−ph8/8) = e(SEC·n/8)). The builder diff against `certG_build_sector.py` is limited to b = 16, the finite factor, and /16.
- **Assembly (referee, independent mpmath code `ref/ref_assemble16.py`).**
  - Rates: R_u = 1.6677 and R_t = 1.2587. R_uR_t/ξ_lo = 0.85376 and R_t²/ξ_lo = 0.64438.
  - Thresholds: |X16| ≤ 1%·(K_min/2)ξ_lo^m for m ≥ 213, and for m ≥ 243 with the inheritance factor 1 + (m/2)ln λ. This is the same as the author.
  - The ratio is 8.2e−3 at m = 243 and 8e−20 at m = 495.
- **Logic of the bound is correct.**
  - The resolvent bound fullR/(1−F) is the quantity `rig_spec` rest mode certifies, with F = pert·fullR(SY_R, R).
  - Cauchy gives ‖T^{m−1}‖ ≤ R^m sup‖(z−T)⁻¹‖.
  - |W_C| ≤ 6·7·42/7⁴ = 36/49.
  - Monotonicity beyond the 8-step check window holds because every term is (positive)·(ratio < 1)^m, times a linear factor that is decreasing for m ≳ 6.
  - σ(h)/h ≤ 1 + ln h ≤ 1 + (m/2)ln λ.
  - The square part is included, which is conservative.
- **Gap (J3-F1).** §1 calls the read-out identity for b = 16 a "modelling assumption". Line G's G2 (TRACE-203) is [P] only for a finite alphabet, and it says explicitly that the infinite-alphabet lift of the C^{b²}-extended operator is "not done". The Line F lift (TRACE-197) is stated for scalar weights.
  - The extension is routine: tensor with a finite monomial state factor; trace class is preserved; the chain decomposition is per word; N_V − N_E = 1 is independent of the state factor; then restrict to the exact invariant blocks. It is the same step Lines I/J use for b = 8.
  - It must nevertheless be **stated and proved as a lemma** (or cited, if Line I's write-up covers general b). Otherwise, Theorem J3(3) and §0.1 must carry it as a hypothesis. As written, §0.1 and Theorem J3(3) say [CA] with no caveat, which is a labelling inconsistency.

### J3.2 Inheritance theorem [P]
- **The proof was re-derived and is correct.**
  - CRT phase splitting: D̄′D′ + 7̄·7 ≡ 1 (mod 7D′).
  - The linear term vanishes mod D′ for β = D′β′.
  - |G^{(D′)}_u(0)|² = D′² for a unit u and odd D′. This includes prime powers, since x² − 2y² is non-degenerate with unit discriminant.
  - The frozen exclusions mean exactly that j is a unit mod d: 2h/d′ = (2h/d)(d/d′) and d/d′ is odd.
  - The 7-part of the label is tD̄′ = j′y′ with j′ = D̄′j, and (2h/d) ≡ (2h/7)D̄′ (mod 7), so the level-7 member set is reproduced.
  - The summand is independent of j mod D′, so the count n_{D′} factors out.
  - n_q = q − 2 for q ∥ h, and q − 1 for v_q(d) < v_q(h). This is independent of ρ, because ν₀ is a unit, so the bad j is ≢ 0.
  - The same factor applies to ±ρ, and |Z_{+ρ}| = |Z_{−ρ}| makes the cut-off identical, so the 1:3 cancellation persists.
- **The general form** W_{ce,eβ′} = (n_e/e²)W_{c,β′} with gcd(c, e) = 1 follows verbatim, but it is only in NOTES. Write it out (J3-F5).
- **P-check.** The arb check uses exact integer Z[ζ_d] histograms; I reran it and got max diff 2.5e−56. Note that it compares the class sums W_C, not individual β, which is sufficient for the use made of it.
- **A_m ≥ 1 reinforces D7: ACCEPT.** The inherited copies are positive multiples of X7, and X7 > 0 on S⁺, which is the only place it is used.
- **Square parts ≥ 0: trivially correct.**

### J3.3 Prime levels [P]
- **Re-derived.** Completing the square gives conj G_t(0)G_t(β) = q²·e(t̄N(β)/q).
  - The labels jy′ cover F_q* minus exactly one value, because ν₀ is a unit, so the excluded j is ≠ 0.
  - Hence W = q⁻²(−1 − e(t̄_bN/q)), which gives ≤ 2/q² for non-isotropic β and (q−2)/q² for isotropic β.
  - 2 is a square, from 2y′² ≡ 1, so the number of nonzero isotropic β is 2(q−1). For q² | h there is no missing label, giving 1/q² and (q−1)/q².
- **Rerun.** Matches the author's figures: 1.994 and 39 for 80 β at q = 41; 1.000 and 30 for 60 β at q = 31.
- **ACCEPT.** The "Consequence" paragraph is [H] and correctly labelled. But §0.3's "This kills the slow-twist danger" is too strong for [H] (J3-F4).

### J3.4 rat_excl [CA] and the S⁺ density
- **Independent check** (`ref/ref_rat.py`, exact Fractions with outward rounding at 256 bits).
  - Enclosure: arg ξ/2π ∈ [0.88797591, 0.88797627], width 3.57e−7.
  - No a/b with b < 1339 lies inside. The least denominator is 1339 (1189/1339). **ACCEPT.**
  - Minor: the author's `Fraction(float(lo.lower()))` is not outward-rounded. This is harmless here, since 1189/1339 is interior and no smaller-denominator fraction is within 1e−12, but use outward rounding.
- **Vinogradov.**
  - The needed statement is that for irrational α, (pα) is equidistributed mod 1 over primes p ≡ p₀ (mod 56). This follows from Vinogradov's theorem Σ_{p≤x} e(pα) = o(π(x)) for all irrational α. Insert 1_{p≡p₀(56)} = (1/56)Σ_k e(k(p−p₀)/56) and apply it to hα + k/56, which is irrational for h ≠ 0. The Weyl criterion then gives the result.
  - The step angle is 3·arg ξ, which is irrational/2π iff arg ξ/2π is.
  - j = 3p mod 168 and B_j are fixed on each class p₀.
  - Density = arccos(0.84431)/π = 0.18001 per class: arccos = 0.565520 = θ_up/2, so this equals 2·0.5655/2π. **Correct.**
  - The 0.84431 threshold exceeds c_win = 0.8443063, so S⁺ lies inside the window used by Theorem J.
  - J3-F3: write this derivation out with a reference, and say "relative density among primes p ≡ p₀ (56), p ≥ 167".

### J3.5 Theorem J3: identity and inequality
- **Identity [P]. ACCEPT.** W′ = W′_A + φ⁻¹[A_mX7 + X16 + Q + O♮].
  - Each included level's Dev splits into cross + square, by Prop I2′ (TRACE-212) and TRACE-213.
  - The nonzero β at a level 7∥d split into inherited (β ∈ (d/7)O), which gives A_m·X7 or the X16 copies, and the rest, which is O♮.
  - On m = 3p with p ≠ 7, 7 ∥ h holds.
  - Note: O♮ also contains β inherited from conductors c ≠ 7 (for example at level 7q, β ∈ 7O). These are positive multiples of level-c primitive parts, by the general inheritance theorem. "Primitive" in §0.5 should read "of conductor ≠ 1, 7" (J3-F5).
- **Inequality. ACCEPT, re-derived.**
  - On S⁺ (cos ≥ 0.84431 > c_win) with m ≥ 495 = max M0(j) over j ∈ 3·(Z/56)*, the pointwise growth step of Theorem J gives X7 ≥ (K_j⁺/2)ξ_lo^m ≥ (K_j/2)ξ_lo^m.
  - The remaining terms: A_m ≥ 1, Q ≥ 0, and |X16| ≤ 0.01(K_min/2)ξ_lo^m ≤ 0.01·X7 for m ≥ 243.
  - φ = φ(2h) ≤ h < ε^m/2 = λ^{m/2}/2, since ε̄^m < 0 for odd m.
  - ξ_lo/√λ = 1.01842245.
  - Hence W′ ≥ −4m + 0.99K_j·1.0184224^m + φ⁻¹O♮.
- **Caveat.** Item 3, X16, is [CA] only modulo J3-F1.

### J3.6 §4 claims
- **"q | h_m iff r(q) | m" [P]: true, but state it precisely (J3-F2).**
  - For odd m, h_m = (ε^m + ε̄^m)/2 with ε̄ = −ε⁻¹, so q | h_m ⇔ λ^m ≡ 1 ⇔ ord_q(λ) | m.
  - Define r(q) := ord_q(3+2√2). "For a Lucas sequence" is imprecise: h is a companion (V-type) sequence, and its divisibility rule is not the standard U-rule.
- **The remaining §4 statements are correct.**
  - On m = 3p, ranks ∈ {3, p, 3p}, and rank 3 ⇒ q = 7.
  - q ≡ ±1 (mod p) holds. In fact q ≡ 1 (mod 2p), since 2 is a QR mod q, so λ ∈ F_q*.
  - 49 ∤ h ⇔ 21 ∤ m holds, since ord₄₉ λ = 21.
  - The rank examples check out: 41 | h₅, 239 = h₇, 199 | h₉ = 7·199, 353 | h₁₁ = 23·353, 599 | h₁₃ = 79·599.
- **"Dominates" / "forced".** These rest on a toy Galerkin survey and are labelled [N, H]. This is acceptable.

### J3.7 Dichotomy, H♮, H_arg
- **Dichotomy: ACCEPT.** R′ (TRACE-206) is W′_m = o(m) through odd m, so the corollary follows directly from J3.5.
- **H♮: correctly formulated.**
  - H♮ ⇒ W′ ≥ −4m + δ·0.99K_j·1.0184^m, so W′/m → ∞.
  - The sufficient form |O♮| ≤ e^{o(m)}r^m with r < ξ_lo is fine.
  - Optional: H♮ is needed only for infinitely many m ∈ S⁺, not for all of them.
  - H♮ is a substantive hypothesis: it requires uniform-in-q twisted rate bounds at unboundedly many conductors. The report says so honestly.
- **H_arg.** It is correctly stated as a hypothesis, but one sentence overstates (J3-F6). A "sharper μ* enclosure" can **never** remove H_arg: it only raises the excluded denominator bound.
  - The other route is plausible but not done, and I make no claim about it here. If arg ξ/2π = a/b with b ≥ 1339, use Dirichlet for p mod 56b, then a Jacobsthal/Kanold-type bound g(n) ≤ 2^{ω(n)}, then a finite check for small b, to place a residue 3au/b in the 18% arc.

### J3.8 Labelling and overstatement
- **No unconditional refutation is claimed.** §0 says "Not achieved" in bold, and the Corollary and §5 are explicitly conditional. **Good.**
- **[N]/[H] are labelled throughout §3–§4 and §1 float tops.** Exceptions:
  - §0.1 and Theorem J3(3) state "[CA]" without the b = 16 lift caveat (J3-F1).
  - §0.3 says "This kills the slow-twist danger", which is too strong for an [N, H] item (J3-F4).
  - The §5 heading "strongest proved statement" should read "proved + computer-assisted, modulo J3-F1".

### J3.9 Certificate sample: 90 of the 576 (reps [5, 13, 18, 27, 31], cases ['15,2', '21,-2', '3,-2', '3,2', '9,-2'], both signs, V/E, untwisted plus all 8 classes)
Each sampled certificate was rebuilt from scratch in the referee area with the author's builder, and `rig_spec` (f346e22c) was rerun at the recorded R. Result: **90/90 pass**.
- The rebuilt mid/rad .npy sha256 equal the hashes recorded in every certificate. So the builds are deterministic, and deleting the .npy files is harmless.
- Build JSON trace_norm, Xnorm, Δ, δ₁ and D are identical.
- certified is true, and F_R2 and SY_R are bit-identical.
- Checks: ALL PASS. Script: `j3/certs/ref_cert16.py`; per-cert results: `ref_cert16.json`.
- All 576 author JSONs carry `certified: true` with mode rest (asserted again by my `ref_assemble16.py`).

### J3 fixes (numbered)
- **J3-F1 (needed for the [CA] label).** Add a lemma: TRACE-197 lift + G2 (TRACE-203) for (a, b) = (±2, 16) with the 64-state automaton, restricted to the exact invariant 2-dimensional blocks. It gives Z_ρ = (1−λ^{−m})Σ_B[tr((J_B⊗·)V_B^m) − tr((J_B⊗·)E_B^m)], plus the twisted analogue.
  - Proof: termwise per word, as for b = 8 in Lines I/J. Trace class is preserved under ⊗ with a finite monomial matrix; the chain decomposition is per word; N_V − N_E = 1 is independent of the state factor; the block restriction is exact because the monomial A_n are unitary, so the complement of the block span is invariant too.
  - Alternatively, carry this as a named hypothesis in §0.1 and Theorem J3(3).
- **J3-F2.** §4: define r(q) := ord_q(3+2√2) and state "q | h_m ⇔ r(q) | m for odd m", with the one-line proof (h is V-type, not U-type). Optionally: q ≡ 1 (mod 2p).
- **J3-F3.** §5 "Size of S⁺": write out the Vinogradov ⇒ equidistribution of 3pα over p ≡ p₀ (mod 56) derivation (additive characters plus Weyl). Cite Vinogradov 1937 or a textbook. Give the density arccos(0.84431)/π = 0.1800 relative to primes p ≡ p₀ (mod 56), p ≥ 167.
- **J3-F4.** Tone down §0.3 "This kills the 'slow-twist' danger" to "suggests [H] that…". Rename the §5 title to "strongest proved/computer-assisted statement (modulo J3-F1)".
- **J3-F5.** Write out the general inheritance theorem W_{ce,eβ′} = (n_e/e²)W_{c,β′} for gcd(c, e) = 1 in §2; it is currently only in NOTES. In the O♮ description, replace "primitive" with "conductor ∉ {1, 7}". Note that the P-check compares class sums.
- **J3-F6.** §5, last bullet: remove "or by a sharper μ* enclosure". That only raises the 1339 bound; it cannot prove irrationality. The Dirichlet/Jacobsthal route is the only removal path offered.
- **J3-F7 (hygiene).**
  - `theta_big.py` writes to an absolute path inside the tree. Make it relative, as in the other scripts; it clobbered the log when I reran it (repaired, see the top of the J3 section).
  - `rat_excl.py`: round the enclosure outward (`Fraction(float(...))` is nearest-rounded). This is harmless here.
  - List `blocks16_reps.json`'s generator: no script in §6 produces it. The referee verified its content independently.

### J3.10 Remaining reruns (completed by 08:56 UTC+5)
- `blocks16_exact.py` (16 cases) gives **ALL EXACT CHECKS PASSED**, and `wordtest16` gives max diff 1.15e−14 (PASS).
- The block *bases*, and hence the exponent tables, differ from the author's JSON. The script picks a random element of the commutant via float null-space, which is BLAS/thread dependent. Each run's tables are exactly verified for its own basis, so this is harmless: bases differ by diagonal phases/ordering, which gives unitarily equivalent block operators.
- Provenance consequence: the certificates depend on the author's specific `blocks16_exact.json`. Builds record only the sha of `gstates16_block.py`, not of that JSON.
  - The manifest covers the JSON, and my bit-identical rebuilds used the author's JSON.
  - Recommendation J3-F8: record the JSON sha in the build provenance, and seed or canonicalise the basis.
- An exact-structure float test of the **author's** JSON (wordtest16) is running; see DELTA3.

**J3 verdict (first pass): ACCEPT AFTER FIXES J3-F1…F7 (+F8).** The mathematics is correct, and all reruns and the 90-certificate sample reproduce. J3-F1 was the only substantive item.

# DELTA3 — DF8–DF10, J3-F1…F8, Lemma L16 (referee, from 08:56 UTC+5; written incrementally)

**Integrity.**
- `J3/SHA256_J3_v2.txt` verifies (run from `J3/`).
- `logs/SHA256_v2.txt` verifies; it was regenerated because REPORT_v2.md was edited in place.
- The pre-edit sha is noted in NOTES.md:52. I did not keep a pre-edit copy, so the DF items were checked on the current text.
- v1 `J3/SHA256_J3.txt` now mismatches exactly on NOTES_J3.md, rat_excl.{py,json} and theta_big.py. This is declared "by design" in NOTES:54.
- All referee reruns are in `/workspace/audit/lineJ/delta3/`; the mirror is `delta3/mirror/`, and nothing was written to the author's tree.

### D3.1 DF8–DF10 (REPORT_v2.md)
- **DF8: done.** §5 caveats 1 and 4 are marked "(Closed, DF8)".
- **DF9: done.**
  - The Theorem J header (l.163) points to `assemble_v2.{json,py}`.
  - §0.5 points to STRATEGY_v2.md.
  - The file tables list assemble_v2, fixes_checks and the v2 manifest.
- **DF10: done.** ⌈(2π−θ_up)/θ⌉ ≤ N−1: (2π−1.131054)/1.130677 = 4.557, so the bound is 5 = N−1. The old form is kept as also valid.
- **Verdict: Line J v2, ACCEPT (final).**

### D3.2 J3-F2…F8 (non-L16 items)
- **F2, the r(q) lemma: ACCEPT.** This is the same proof I gave.
  - For odd m, ε̄ = −ε⁻¹ gives h_m = (ε^m − ε^{−m})/2. So q | h_m ⇔ ε^{2m} ≡ 1 ⇔ λ^m ≡ 1. The case q = 2 is excluded (q odd), and ε is a unit.
  - Corollary q ≡ 1 (mod 2p): 2y′² ≡ 1 shows √2 ∈ F_q, so λ ∈ F_q* and p | q − 1. Since q is odd and p is odd, 2p | q − 1.
  - The consistency remark with `ranks.py` is correct: if q | h_m for some odd m, then r(q) is odd.
- **F3, Vinogradov derivation: ACCEPT.**
  - The additive-character detector over k mod 56 is correct. Hα + k/56 is irrational for H ≠ 0, so Vinogradov gives o(π(x)) for each of the 56 sums.
  - Dirichlet gives π(x; 56, p₀) ~ π(x)/24 > 0. Weyl's criterion then gives equidistribution.
  - The arc measure is 2·arccos(0.84431)/2π = 0.18001, which I recomputed.
  - Citation nit: I cannot verify from here that IK "Thm 13.6" is the exact theorem number. Vinogradov's prime exponential-sum theorem is in IK Ch. 13 and Vaughan Ch. 3, but please check the number or cite only the chapter.
- **F4 (tone): done.**
- **F5: done.** The general form W_{ce,eβ′} = (n_e/e²)W_{c,β′} is stated with n_e independent of c, β′ and ρ, and the proof is correct as transcribed. O♮ is now "conductor ∉ {1, 7}".
- **F6: done.**
- **F7: done and rerun.**
  - `theta_big.py` with no arguments exits 1 with usage, and the author's file is untouched (sha a6919288…). With the 5 moduli its output is byte-identical.
  - `rat_excl.py` v2 uses an outward nextafter on the floats of the arb bounds, inside one unit interval (asserted). Its output is byte-identical: b_min = 1339.
  - `make_reps16.py` regenerates `blocks16_reps.json` byte-identically.
- **H♮ "for infinitely many m ∈ S⁺": correct.** That suffices to contradict W′ = o(m).
- **J3-F8 (block-basis provenance, raised in J3.10): still open, minor.** Builds still record only the `gstates16_block.py` sha, not the `blocks16_exact.json` sha. The JSON is in the manifest, and my rebuilds are bit-identical, so this is hygiene only.

### D3.3 Lemma L16 (b = 16 lift restricted to exact blocks): careful check
1. **Step 1, G2 (TRACE-203). Correct.** Only the per-word identity is used: c_w·Tr_H(C_w)·⟨𝟙|A_w|δ₀⟩·(1−λ^{−m}) equals the word's summand of Z_m(ν_ρ).
   - Tr of a single composite depends only on its fixed point, so the disc radius plays no role per word.
   - Z_m(ν) = Σ_{n∈Z^m} is absolutely convergent (Σ|ĝ| < ∞), so the truncation N → ∞ is harmless on the left-hand side.
   - Restricting to the reachable set S is exact: A_wδ₀ is supported in S, and S is closed under every A_n.
2. **Step 2, the per-word lift (TRACE-197 proof). Correct.**
   - For a word w, Tr V_w − Tr E_w = (N_V − N_E)·p_w(s*)/(1−λ^{−m}) = Tr_H C_w. The fixed point s* and the multiplier are the same on every closed chain, and the counting N_V − N_E = 1 does not see the multiplier constant or the state factor. Multiplying by the scalar s_w is trivially fine.
   - *Remark:* TRACE-197 is stated for the multiplier constant c₀. Here |C| = c₀/2 and there is an extra unimodular e(Cn²/2). The F1 proof is uniform in the real constant: it enters only through M_n = e^{2π|C||n|ρ} and the α-condition. The lemma says this explicitly. **Accept.**
   - Hypotheses at the parameters used (`certG_build16.py`):
     - θ* = ½/ρ_V + 1/λ < 1 with ρ_V = 1.2, and ½/(λρ_E) + 1/λ < 1 with ρ_E = 0.8, both `assert`ed in arb (l.54–55);
     - the per-block θ = |δ|/ρ + 1/λ < 1 is asserted per transition (l.78);
     - β = 2.5 > 0;
     - α = 2π|C|ρ + β/λ, with the Bessel tail bounded rigorously (|J_n(x)| ≤ (x/2)^n/n!, tailT ≤ 2e−200);
     - ĝ = iⁿJ_n(1.8) gives Σ|ĝ(n)|e^{α|n|} < ∞ for every α.
   - **All hypotheses hold.**
3. **Step 3, resummation / dominated convergence. Correct.** The domination actually needed is Σ_w|c_w|‖V_w‖₁ ≤ (Σ_n|ĝ(n)|‖V_n‖₁)^m < ∞, using ‖XY‖₁ ≤ ‖X‖₁‖Y‖ ≤ ‖X‖₁‖Y‖₁. The finiteness of Σ_n|ĝ(n)|‖V_n‖₁ is exactly step 1 of the F1 proof.
   - Together with ‖X⊗A‖₁ = ‖X‖₁‖A‖₁ and |s_w| = 1, this gives trace-norm convergence of 𝐕^m = Σ_w c_wV_w⊗A_w, and continuity of Tr.
   - The tensor ordering (V_{n_m}⋯V_{n_1}) ⊗ (A_{n_m}⋯A_{n_1}) matches G2, which is proved for 𝓛^m itself.
   - The lemma's phrase "Σ_w|c_w|‖V_w‖₁ < ∞ under the TRACE-197 hypotheses" is right. Editorial nit L16-a: write the one-line product bound.
4. **Step 4, exact block restriction. Correct**, and verified independently on the **author's** `blocks16_exact.json` with `delta3/ref_L16_blocks.py`:
   - A_nF_B = F_BY_{B,n} for all n mod 16, all 16 cases and 8 blocks, to 9e−16. The entries are 16th roots of unity, so this is effectively exact.
   - The blocks are mutually orthogonal, to 2e−14.
   - 𝟙 ∈ span, to 8e−16.
   - I recomputed J_B from first principles as G_B⁻¹F_B^*δ₀α_B^*G_B, which gives tr(Y_wJ_B) = ⟨u_B|A_wP_Bδ₀⟩. It equals the stored coordinate J to 5e−16.
   - The coordinate ‖J_B‖₂ is at most 0.5000000000000001, so the assembly bound ‖J_B‖ ≤ ½ is right *in the coordinate basis the builder uses*. This matters because the f_i have unequal supports (32 vs 64), and the bound must refer to the coordinate norm. The stored coordinate J_B and Y_{B,n} are unitary monomial matrices, so this is consistent.
   - The unitarity argument for the invariance of U^⊥ is correct: A_n is finite-order monomial, so A_n U = U. So is the identity ⟨𝟙|A_w|δ₀⟩ = Σ_B tr(Y_{B,w}J_B).
   - `wordtest16` rerun on the author's JSON gives a log byte-identical to the author's (max 1.14e−14).
   - Editorial nit L16-b: the statement writes J_B = (P_Bδ₀)(P_B𝟙)^* "in the block basis". Say explicitly that this is the coordinate matrix G⁻¹F^*δ₀α^*G (the basis is orthogonal but not normalised), and that ½ is its coordinate operator norm.
5. **Twisted 3-cycle lift. Correct.**
   - The twist e(Σ_i n_iτ_i) is a per-word scalar. The 3-state cyclic factor (i → i+1, phase e(nτ_i)) with read-out |e₀⟩⟨e₀| reproduces it exactly when 3 | m, which holds for m ≡ 3 (mod 6).
   - The read-out is rank one with norm ≤ ½.
   - It is the same construction as for b = 8 (Line I v2 step 3; Line J sectors, audited), and `gstates16_block.finite` implements it as stated.
- **L16 verdict: ACCEPT, with editorial nits L16-a and L16-b.** X16 is thereby [CA].

## FINAL OVERALL VERDICT (Line J v2 + J3 v2), 31 Oct 2026, 09:00 UTC+5

**Ready to integrate.** Blocking items: none.

| part | verdict |
|---|---|
| Line J v2: Theorem J (d = 7 twisted contribution ≥ K_j·1.0184224^m/m with each sign in every 6 consecutive terms of a class from M0(j)) | **ACCEPT** (F1–F11, DF8–DF10 done) |
| J3 §1 (±2,16): exact blocks [P-check], 576 rest certificates [CA] (90 rebuilt and re-certified bit-identically), Lemma L16 [P], \|X16\| ≤ 1 % for m ≥ 243 (independently recomputed) | **ACCEPT** |
| J3 §2 inheritance theorem (general form) [P]; A_m ≥ 1; square parts ≥ 0 | **ACCEPT** |
| J3 §3 prime-level complete sums [P] | **ACCEPT** |
| J3 §4 r(q) lemma [P]; "forced" [N, H] | **ACCEPT** (labels correct) |
| J3 §5 Theorem J3 identity and inequality; rat_excl [CA]; Vinogradov density 0.1800 [P]; dichotomy corollary; H♮ (infinitely many m) and H_arg | **ACCEPT**: conditional statements, correctly labelled. No unconditional refutation is claimed. |

**Non-blocking polish:**
- J3-F8: record the `blocks16_exact.json` sha in the build provenance, or seed the basis.
- L16-a: write the product domination bound.
- L16-b: say that J_B is a coordinate matrix in a non-normalised basis.
- Check the IK theorem number, or cite only the chapter.

**Integration wording:** "frozen R′ (TRACE-206) is false along m = 3p under H♮ and H_arg; unconditionally, any validity of R′ forces exponential cancellation of the d = 7 term by conductor ∉ {1, 7} parts on S⁺".
