# Line I — Session 4 report (2026-10-31, UTC+5)  [new file; REPORT.md v1 untouched; REPORT_v2.md = v1 with referee fixes]
Labels: [P] proved on paper, [L] Lean, [CA] computer-assisted certificate (arb + error-tracked binary64), [N] numerical, [C] conjecture,
[assessment] = an argument that a specific route fails (not an impossibility proof).

## S4.0 Bottom line
1. Referee verdict on Line I: ACCEPT AFTER FIXES.  All blocking fixes B1–B9 and recommendations R1–R7 are applied in NEW files
   (REPORT_v2.md, theory_E2_v2.md, cert_v2/, lean/LineI_v2.lean); v1 files kept for provenance.  See S4.4.
2. Item 1 [P]+[CA]: Theorem I6 (d = 7 square term) now holds for ALL m ≡ 3 (mod 6) and ρ = (±2,8), by EXACT symmetry (no new
   certificates needed), with an independent direct certificate of one transferred case as a cross-check.
3. Item 2 [CA, see S4.2]: for the two top classes 1:3 and 2:1, counting certificate "the twisted operator has exactly 3 eigenvalues in |z| > R" ⇒ r_tw > 1.262 > 1.260376 ≥ √λ/μ₀
   (μ₀ ≥ 1.9154712 certified by Line F, BGS-TRACE-198; DF3).
   The nonvanishing of the trace coefficient is NOT certified.
4. Item 3: the three suggested structural routes all reduce to the same additive quantity (aliasing collisions of the weighted
   difference set of P at modulus 2h); two small lemmas proved; no rigorous weakening of R′_A obtained (theory_session4.md).

## S4.1 Item 1: all operator cases by exact symmetry [P] (+ [CA] inputs of Session 3)
* sym/monomial_intertw.py (integer arithmetic mod 8; output sym/monomial_intertw.json, code sha c50ff00b…): for every case
  (m mod 24 ∈ {9,15,21,3}, represented by m = 9, 15, 21, 27) × (a = ±2) there is a monomial unitary X on the 16 reachable
  states (permutation × 8th-root-of-unity phases) with
    a = +2:  X A_n^{(9,2)} X⁻¹ = A_n^{(m,2)}  for all n mod 8;
    a = −2:  X (−1)ⁿ conj(A_n^{(9,2)}) X⁻¹ = A_n^{(m,−2)};
  and a monomial Y with Y A_{−n} Y⁻¹ = A_n (reflection).
* Lifted operators: L^{(m,2)}_β = U L^{(9,2)}_β U⁻¹ (U = I⊗X⊗I₃);  L^{(m,−2)}_β = J L^{(9,2)}_{−β} J⁻¹ with J = K⊗X⊗I₃ antiunitary
  (K = complex conjugation on the disc lattice; uses conj ĝ(n) = (−1)ⁿĝ(n), since ĝ(n) = iⁿJ_n(1.8) and J_n real, and K M_C K = M_{−C});
  L_{−β} = (R⊗Y⊗I₃) L_β (R⊗Y⊗I₃)⁻¹ (R: lattice reflection s → −s, c → −c; ĝ even).  These are identities between the TRUE
  (infinite-dimensional) lifted operators V, E; the certificates are statements about the true operators, so no claim about the
  Galerkin truncations is needed.  For Theorem I6 only these invariants enter: σ(L), sup_{|z|=R}‖(z−L)⁻¹‖, ‖L‖₁, and
  |Tr(B L′^m)| = |Tr((W⁻¹BW) L^m)| with ‖W⁻¹BW‖ = ‖B‖ = 4 (W = U, J or R⊗Y⊗I₃; for antiunitary J, Tr becomes its conjugate).
* Consequence [P]: operator norms, trace norms, ‖B‖, the perturbation budget and sup_{|z|=R}‖(z−L)⁻¹‖ are invariant (for the
  antiunitary J the circle |z| = R is mapped to itself by z ↦ z̄), and the set of β classes is mapped onto itself (β ↦ −β).
  Hence every Session-3 certificate (V: R = 1.45, E: R = 1.0, all 8 classes) transfers verbatim, and Theorem I6 v2 holds for
  all m ≡ 3 (mod 6), ρ = (±2,8) (REPORT_v2.md S3.4; constants 6.769·10⁶, 6.859·10⁴; < 0.01 for m ≥ 321; rate ≤ 0.87089^m).
* Cross-check [CA]: cert2/run_xcheck.sh, a DIRECT certificate of the transferred case m = 15, a = −2, class 1:3:
  V R = 1.45 F = 0.356981, E R = 1.0 F = 0.013833 — the Session-3 values to 6 digits (cert2/logs/*_rest.json, SHA256_xcheck.txt).

## S4.2 Item 2: rigorous lower bound on the leading twisted eigenvalue  (dom/)
**Method [CA]** (dom/rig_dom3b.py v2, code sha dc6aec1f…; builder certG_build.py sha aa86c186…, gstates 05f55500…, law 877a95a5…;
all hashes in dom/logs/SHA256_dom.txt and in each output JSON's provenance block). Operator: lifted V lattice, case m ≡ 9 (24), a = 2,
K0 = 2, ρ = 0.85, K = 36/30, β = 3.5, Nmax = 150 (D = 8064; δ1 = 3.13e−4, δ2 = 3.1e−8, Δ = 6.25e−4, ‖X‖ = 0.684).
* Float dominant invariant subspace (ARPACK, k = 3) → Householder deflation H (κ ≤ 1 + 1.4e−14); exact similarity with
  a-posteriori residual ε_H = 1.12e−9, ‖b21‖ = 5.6e−15, moved into the perturbation: pertT = 9.375e−4.
* T0 = [[Λ, b12],[0, Y]]: the three eigenvalues of the 3×3 block Λ are isolated in arb (charpoly roots), |·| ∈ 1.2837143 ± 1.3e−8,
  all > R; σ(Y) ⊂ {|z| < R} by Neumann validity (‖Y^32‖ ≤ 130.4 < R^32).
* sup_{|z|=R}‖(z−T0)⁻¹‖ ≤ Rcore: pointwise bound ‖R_Λ‖ + ‖R_Λ M(z)‖ + ‖R_Y‖ on 4096 grid points, M(z) = Σ_{j<32}(b12Y^j)z^{−j−1}
  evaluated as a vector sum with rigorous error (err0 ≤ 0.01) + Neumann tail, then covering by the resolvent identity
  ‖R(z)‖ ≤ g/(1 − |z−z0|g) (h·g ≤ 0.32).  (v1, triangle-inequality bound: Rcore ≈ 6200 — not certifiable; v2: 280–470.)
* Homotopy (Line H): F = pertT·[(κRcore + 1/R)(1 + ‖X‖/R) + 1/R] < 1 ⇒ #σ(V_β) ∩ {|z| > R} = #σ(T0) ∩ {|z| > R} = 3.
**Result, class 1:3 (dom/logs/V36_1_3_dom3b.{json,log}):** certified at R = 1.22 (F = 0.4133), 1.24 (0.4292), 1.25 (0.4871),
1.262 (F = 0.6843).
**Result, class 2:1 (dom/logs/V36_2_1_dom3b.{json,log}):** certified at R = 1.22 (F = 0.3076), 1.24 (0.3689), 1.25 (0.4397), 1.262 (F = 0.6489);
Λ-block moduli 1.2835951 ± 4.2e−8.  So Theorem I9 holds for BOTH top classes 1:3 and 2:1 (r_tw > 1.262 for each).
**Theorem I9 [CA + P].** For the lifted twisted operator V_β, β in class 1:3 or 2:1 (and in every operator case m ≡ 3 (mod 6), ρ = (±2,8),
by S4.1): σ(V_β) ∩ {|z| > 1.22} = {μ, ωμ, ω²μ} (ω = e^{2πi/3}), each eigenvalue algebraically simple, with
  1.262 < |μ| < 1.45   (the CERTIFIED range; DF5),
and the rest of the spectrum lies in |z| < 1.22 (upper bound |μ| < 1.45 from the Session-3 rest certificate at R = 1.45 on the same true
operator).  The Λ-block moduli 1.2837143 (1:3) and 1.2835951 (2:1), and the float value 1.28371, are floating-point diagnostics of the
deflated 3×3 block / of Galerkin truncations, NOT enclosures of |μ|.  Hence the twisted spectral radius satisfies
  r_tw(β) = |μ_β| > 1.262 > 1.260376 ≥ √λ/μ₀.
**μ₀ (DF3).** μ₀ denotes the exponential growth rate of |Z_ρ| = |Z_m(ν_ρ)| (this is the quantity in the cross term 2Re(Z̄_ρδ₀)).
In Line I it was only a float (1.915473, top eigenvalue of the dense untwisted G2 operator).  Certified input: Line F, BGS-TRACE-198 (F2)
and BGS-TRACE-199 (F3), `computations/verification/lineF/logs/certV_eta2_a4_tight.json` (sector a = 4, mu_abs_lower = 1.91547120413…):
the lifted k1 operator L_{V,4} at η = 2 has one simple eigenvalue μ* with |μ*| ∈ [1.9154712, 1.9154753] (registered enclosure; the Line F
author report's upper end 1.9154752 was corrected to 1.9154753 by the Line F referee) and all other spectrum (all sectors, V and E) in
|z| < 1, so |Z_m(ν*)| = ½(1 − λ^{−m})(|μ*|^m + O(1)) and lim |Z_m(ν*)|^{1/m} = |μ*|, ν* the odd lift of −4⁻¹ mod h_m (N ≡ −4), i.e.
ρ = (−2, 8) (8ν* ≡ −2 mod 2h).  Identification: it is the same quantity, not literally the same operator — Line F's L_{V,4} (one-state
lattice, sector weights, K0 = 4, ρ_V = 1.2) and Line I's untwisted lifted G2 operator (16 automaton states ⊗ lattice, K0 = 2, ρ = 0.85) are
two trace representations of the SAME sequence Z_m(ν_ρ), so the growth rate is the same number; float values agree (Line I 1.915473,
Line F/G 1.9154732, both inside the enclosure).  ρ = (2, 8) (ν = −ν*): conj ĝ(n) = (−1)ⁿĝ(n) for k1 (J_n real) and TRACE-183 gives the
phase −q/2 − κ(Σn)²/8 at −ν*, so conj Z_m(−ν*) = Σ_n Φ̂(n) e(q/2 + κ(Σn)²/8 + (Σn)/2); the factor e(4s/8) only shifts the sector
coefficients of TRACE-184 (c_a ↦ c_{a−4}, still |·| = ½ for even a), so the sector-4 coefficient is c_0 ≠ 0 and the TRACE-199 bound holds
verbatim: |Z_m(ν_{(2,8)})| ≥ ½(1 − λ^{−m})(1.9154712^m − 3012.30).  Hence for both ρ = (±2, 8): μ₀ = |μ*| ≥ 1.9154712 and
√λ/μ₀ ≤ (1+√2)/1.9154712 = 1.2603758… ≤ 1.260376 (arb).  (Numerically both growth rates are 1.9154732, Line G growth_law.json.)
Proof of the orbit structure [P]: S V_β S⁻¹ = ωV_β (S = ω^i on cycle component i, exact), so the multiset σ(V_β) ∩ {|z| > R} is
invariant under z ↦ ωz; a 3-element invariant multiset not containing 0 is one free orbit, hence 3 distinct simple eigenvalues.  ∎
**What this implies [P, given I9].** With P = P_0+P_1+P_2 the Riesz projections of the three eigenvalues, for m ≡ 0 (mod 3)
  Ẑ(β) = c_m·c(β)·μ^m + O_β(1.22^m),   c(β) = Σ_i Tr(B P_i),
with an explicit (certifiable) O-constant from the resolvent bound on |z| = 1.22 and E's radius < 1. Hence EITHER c(β) = 0, OR
limsup |Ẑ(β)|^{1/m} = |μ| > 1.262 > √λ/μ₀, in which case the operator-radius route to the d = 7 cross term (D) is impossible: no proof of
(D) at d = 7 can go through r_tw < √λ/μ₀.
**What is NOT certified / NOT implied.** (1) c(β) ≠ 0 (float value ≈ 0.5): a projection-perturbation bound needs
pert·Rcore² ≪ |c|, i.e. pert ~ 1e−6 at D ~ 8000 — out of reach here; a feasible route is a rigorous enclosure of Ẑ(β) at one m
of a few hundred against the explicit O(1.22^m) error, or a Turán-type power-sum argument. (2) The sign/size of the frozen d = 7
term in W′ also needs the Z₀ (double-eigenvalue) coefficients, the combination of the 8 classes in δ₀, and the two ρ's.
(3) Frozen R′ is NOT disproved: the bulk, the (±2,16) members and the other levels are uncontrolled (bulk control still missing),
so W′/m could still be compensated. TRACE-206 stays OPEN; the statement "frozen d = 7 term contributes ≫ 1.0187^m/m to W′/m
along a subsequence" remains HEURISTIC (it would need (1) and (2)).


## S4.3 Item 3: structural attempts at R′_A — see theory_session4.md
* S4.1′ [P] Poisson/aliasing identity with the unit restriction: F = (1/φ(2h)) Σ_{e|2h} μ(e)(2h/e) Σ_j C_Z(j·2h/e), C_Z(k) the
  weighted count of P(n) − P(n′) = k in Z.  (DF6) The e > 2 Möbius terms are sums of |Z_m|² at EXACT rationals of denominator
  dividing 2h/e (non-unit residues, subtracted out); the TRACE-206 resonant residues are UNITS near (not at) small-denominator
  rationals, related to these terms through the G2 law, not identical to them.  Reading the bulk as the e ∈ {1,2}, j ≠ 0 aliasing
  sum is a heuristic [assessment].
* S4.2′ [P, citing Bilu–Hanrot–Voutier 2001 / Carmichael 1913; DF7] for every m ≥ 16, h_m has an odd prime factor dividing no earlier h_m′,
  so every finite set S of primes misses a prime factor of h_m for all large m; hence no transfer operator
  on a FIXED S-arithmetic space can make the residue sum a single trace for all m; the full-adelic version is non-nuclear and
  its "trace" is literally the Parseval sum S4.1′ [assessment].
* Hecke-equivariance and L²-in-m averaging reduce to the same aliasing sum; no cancellation mechanism found [assessment].
* No rigorous weakening of R′_A (O(m), average in m, or positive density) obtained.

## S4.4 Referee fixes (B1–B9, R1–R7) — where
B1 cert_v2/bounds_sq_v2.py (outward rounding, CV = 6 768 179.601… → 6.769e6; CE → 6.859e4; q = 0.8708840… → ≤ 0.87089) and REPORT_v2 S3.4.
B2 REPORT_v2 §0.  B3 REPORT_v2 Prop I2 (non-unit t = 2; member Dev = 900.47).  B4 REPORT_v2 S3.1 symmetries.
B5 REPORT_v2 Thm I4 (one Y(m) for (E″) and (T″) / diagonal choice; units, 1/φ(2h)).
B6 theory_E2_v2.md Lemma I5′ (C(k) sign; units via Ramanujan sums; further correction found while fixing: the diagonal meets every
   c_{2hj}, not only c_0, so it is not invisible even for all ν; it equals C(0) × an unweighted horocycle sum).
B7 theory_E2_v2 Prop I8 (disjointness, RMT ≤ 4m, N_res ≤ φ; "reduces to").  B8 REPORT_v2 I6 chain step 3 (c_m = 1−λ⁻ᵐ, TRACE-197,
   referee checks, scope) and theory_E2_v2 (ii).  B9 REPORT_v2 S3.0/S3.5/S3.6 and theory_E2_v2 Routes A/B ([assessment]); TRACE-206 stays OPEN.
R1 bounds_sq_v2 tail (m ≥ 1425 bound decreasing; ≤ 4.7e−69 at 1425).  R2 cert_v2/gstates.py imports law from its own dir; run_sq.sh
sha 49dee38c… recorded (cert_v2/logs/SHA256_run_sq_sh.txt).  R3, R4, R5 REPORT_v2 (P ≡ y′Nm mod 2h; case reduction; ε = +1) and
lean/LineI_v2.lean docstring (compiles, EXIT 0, axioms propext/Classical.choice/Quot.sound: logs/lean_LineI_v2.out).
R6 the referee's matrices /workspace/audit/lineI/data/{V,E}_1_3_b0_{mid,rad}.npy are the stored copy (sha == provenance,
cert_v2/logs/R6_stored_matrices.txt).  R7 REPORT_v2 S3.4 wording (F at radius R).

## S4.5 Classification (Session 4)
* [P] Exact intertwiners between all 8 operator cases and the β ↦ −β reflection (sym/; integer mod-8 witnesses) ⇒ Theorem I6 v2 for all
  m ≡ 3 (mod 6), ρ = (±2,8).  Orbit structure of the top twisted eigenvalues (Z/3 symmetry).  theory_session4 S4.1 (Poisson/aliasing
  identity with units); S4.2 (unbounded prime support of h_m; citing Bilu–Hanrot–Voutier).  Lemma I5′ (corrected), Prop I8 with explicit
  hypotheses, cyclic invariance, P ≡ y′Nm (mod 2h), case reduction, 7 | h ⟺ m ≡ 3 (6), ε = +1 (REPORT_v2).
* [L] lean/LineI_v2.lean (docstring fix only; same 5 theorems; EXIT 0; standard axioms).
* [CA] Theorem I6 v2 (constants 6.769e6 / 6.859e4, outward rounded; < 0.01 for m ≥ 321, rigorous tail); direct cross-check of the
  transferred case m = 15, a = −2, class 1:3; Theorem I9 (r_tw > 1.262 for classes 1:3 and 2:1, three simple eigenvalues in |z| > 1.22 each).
* [N] c(β) ≈ 0.5 (float); |μ| = 1.2837143 (float/Λ-block value, not a certified enclosure of the true eigenvalue); envelope data of v1.
* [C]/heuristic: frozen R′ fails for m ≳ 300–400 (TRACE-206 OPEN); conjectured R′_A; W′^A = O(1) (weak evidence).
* [assessment] adelic single operator / Hecke trace / L²-in-m: reduce to the aliasing collisions; no weakening of R′_A.

## S4.6 Referee files (Session 4, all new; v1 files unchanged)
* REPORT_session4.md (this file), REPORT_v2.md (+ generator cert_v2/mk_report_v2.py), theory_E2_v2.md, theory_session4.md, NOTES.md (appended).
* sym/: monomial_intertw.py, monomial_intertw.json (sha c50ff00b…), intertw.py (numerical nullspace check).
* cert2/: run_xcheck.sh, copies of certG_build/gstates/law/rig_spec; logs/{E,V}15m_1_3_rest.{json,log}, build*.log, SHA256_xcheck.txt.
* cert_v2/: bounds_sq_v2.py, gstates.py (R2), law.py; logs/bounds_sq_v2.{json,log}, SHA256_v2.txt, SHA256_run_sq_sh.txt, R6_stored_matrices.txt.
* dom/: rig_dom3b.py (v2, used), rig_dom3.py (v1, crude, superseded), run_dom.sh, builder copies; logs/V36_{1_3,2_1}_dom3b.{json,log},
  buildV36_*.log, SHA256_dom.txt, dom.progress; pilot logs/pil_dom3{,b}.json (D = 3456, not certified, pert 0.33; debugging only).
  The D = 8064 matrices in dom/data/ regenerate deterministically with the argv in run_dom.sh.
* lean/LineI_v2.lean, logs/lean_LineI_v2.out.

## S4.7 Delta-review fixes DF1–DF7 (referee delta review, /workspace/audit/lineI/REPORT.md "DELTA REVIEW"; applied 2026-10-31 02:2x UTC+5)
Pre-fix bytes: pre_delta/ (sha256 in pre_delta/SHA256_pre_delta.txt).
DF1 REPORT_v2 Thm I4: "Equivalent alternative" → "Alternative sufficient hypothesis".
DF2 no hard-coded absolute paths: cert_v3/bounds_sq_v3.py (= bounds_sq_v2 with CERT_DIR/OUT relative to the script; rerun: log
    byte-identical to cert_v2/logs/bounds_sq_v2.log, JSON identical except version/code_sha256) and sym_v3/monomial_intertw.py
    (imports gstates/law from ../cert_v2 relative to the script, writes next to itself; rerun JSON identical except code_sha256).
DF3 Theorem I9 cites the certified μ₀ of Line F (BGS-TRACE-198/199; registered enclosure [1.9154712, 1.9154753]) with the identification
    above (same growth rate of |Z_m(ν_ρ)|, ρ = (−2,8) directly, ρ = (2,8) by conjugation); √λ/μ₀ ≤ 1.260376 < 1.262.
DF4 dom_v3/rig_dom3b.py (v3): gmax over the exact upper ends g.upper(); rerun on the unchanged D = 8064 matrices (input sha256 =
    provenance of v2, dom_v3/logs/SHA256_inputs.txt), classes 1:3 and 2:1, R = 1.22, 1.24, 1.25, 1.262: all CERTIFIED, count 3;
    F(1.262) = 0.6842758739 (1:3; v2 0.6842758739), 0.6489779088 (2:1; v2 0.6488989, referee rerun 0.6489779088 — ARPACK basis order).
    Logs dom_v3/logs/V36_{1_3,2_1}_dom3b_v3.{json,log}, SHA256_dom_v3.txt.
DF5 Theorem I9 states the certified range 1.262 < |μ| < 1.45; 1.28371 / Λ-block moduli are float diagnostics only.
DF6 theory_session4 S4.1 and S4.3′ above: "exactly" removed; Möbius e-terms = non-unit exact rationals, resonances = units near rationals;
    the bulk reading is [assessment].
DF7 theory_session4 S4.2: "p ~ h^c" removed; the proved statement (new odd prime of h_m for every m ≥ 16; every finite S fails for all
    large m) with BHV Theorem 1.4 / Carmichael 1913; Lean Bgs.LineIArith (integration) formalises the deduction with BHV as hypothesis.
