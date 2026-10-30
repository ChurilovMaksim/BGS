# Referee report: Line F and Line G (BGS, kicked cat map S = [[3,4],[2,3]], λ = 3+2√2)

Referee working tree: `computations/verification/lineFG/referee/` (`code/`, `logs/`, `NOTES.md`), backup `<backup-dir>/`.
Repo clone, read-only: `BGS/` at 1d9b6580 (PR #57, Line E, TRACE-183..196). **Note:** `origin/main` has since moved to e378ad11. That commit touches 2 files (`wave2_integration_audit.py`, `claim_integration_epochs.json`) and no claims, so the last claim ID is still TRACE-196 and new IDs start at **TRACE-197**. The integration branch must be rebased on e378ad11.
Nothing was pushed, commented or merged. No jobs belonging to others were touched: pids 716309, 716609, 507001, 552224 and polish2 are still running.

Status tags used below: **[P]** paper proof, **[CA]** computer-assisted (arb), **[Lean]**, **[N]** float numerics, **[C]** conjecture.

---------------------------------------------------------------------------------------------------------------------------------
## PART F — full-alphabet lift, certified η = 2 spectrum, all-m theorem

### F.0 Verdict in one paragraph
The headline is **correct**. The lifted vertex−edge trace identity (F1), the η = 2 certificate (F2) and the all-odd-m theorem (F3) survive a line-by-line audit. I also checked them independently:
* my own float implementation of the lift, written from the prose, reproduces the **physical** quantum traces |Tr U_N^m|² (Line E's direct chirp-DFT table, N = h_m − 4) to 1.4e-13 at m = 5 and 2.0e-11 at m = 7 and 8.0e-12 at m = 9. Those differences are at the table's printed digits;
* my own arb certifier, written from scratch with different discretisation parameters, certifies a simple isolated μ* with |μ*| ∈ [1.914473, 1.916474] at η = 2, k1, full alphabet, with all other spectrum in |z| < 1 (V and E sectors 4, 0, 2; sector 6 follows by a reflection symmetry). The resulting all-m bound is F_15/2m ≥ 6.65.

What blocks integration as written is **a set of unsafe-direction roundings** in the quoted constants. Several "≥" numbers are rounded **up** (e.g. "W̃rest_m/m ≥ 8.07" is false: the certified value is 8.0695). Some wording about H∞ and one [N] adjective also need fixing. All are mechanical (§F.6).

### F.1 Claim-by-claim verdicts

| # | Claim | Audit result | Recommended status |
|---|---|---|---|
| F1 | Lifted trace identity Σ_{n∈Z^m} Πw(n_j)e(c n_j s_j) = (1−λ^{−m})(Tr L_V^m − Tr L_E^m); hence Z_m(ν*) = (1−λ^{−m})Σ_a c_a(Tr L_{V,a}^m − Tr L_{E,a}^m), full alphabet | Re-derived (§F.2). Lean core builds. Independent numerics: own lift vs own brute-force Σ_n Φ̂(n)e(½nᵀH⁻¹n + κ(Σn)²/8) at m = 5, L = 12: 3.8e-11 (the brute-force truncation). Vs physical direct traces: m = 5: 1.4e-13, m = 7: 2.0e-11, m = 9: 8.0e-12 (m = 11, 13 still running, `logs/check2.log`) | **PROVED** [P] + [Lean core] + [N] |
| F2 | η = 2 certificate: L_{V,4} has exactly one eigenvalue (simple) in D(b11, 2e-6), \|μ*\| ∈ [1.9154712, 1.9154752]; all other spectrum (all sectors, both lattices) in \|z\| < 1; ‖L_V‖₁ ≤ 730.15, ‖L_E‖₁ ≤ 22.94 | Code audited (§F.3). All certs were produced by the final code. The skip bug is fixed. No float leakage. Independent weaker re-certification (§F.4). **Fix:** the upper end must read 1.9154753 (the JSON gives 1.91547520413) | **PROVED (computer-assisted)** after the rounding fix |
| F3 | All odd m ≥ 15: F_m(2)/2m ≥ 6.03, W̃rest_m(2)/m ≥ 8.07, ≥ 0.169·1.5197^m/m; k1 analogue of R false | Chain and constants re-derived (§F.5). 0.169 (true 0.16987), 1.5197 (true 1.51976) and 0.679 (true 0.67948) are safe. **"8.07" is unsafe and must be 8.06**, and several table entries are unsafe too (§F.6) | **PROVED (computer-assisted)** after the fixes. Supersedes the *conclusion* of TRACE-188 |
| F4 | f₇ corollary (3 ∤ m) | Immediate from TRACE-193 + F3 | **PROVED (computer-assisted)** |
| F5 | η grid {1.25, 1.5, 1.75, 2.25} fully certified; η = 2.5 partial | JSONs checked: every sector of both lattices is certified at 1.25, 1.5, 1.75, 2, 2.25. At 2.5, E sector 6 is still running (pid 552224). Rounding problems (§F.6), including "F/2m ≥ 2.928 from m = 31" at η = 1.25 (true 2.92798) and an inconsistent η = 1.25 enclosure between §3 and §5 | **PROVED (CA)** for η ∈ {1.25, 1.5, 1.75, 2, 2.25} after the fixes. η = 2.5: exclude, or close it with the reflection lemma (§F.3.6) |
| F6 | Growth window η ∈ (0.951, 3.212) | Float only, correctly labelled | **[N] record, open** (an interval certificate would be TRACE-191) |
| F7 | 49-state lift for the Line B kick: \|μ\| = 1.8839 / 1.8968, cluster 1.27–1.30 | Float, K = 14. "real, not a discretisation artefact" overstates a float observation; say "stable across two discretisations" | **[N] evidence attached to TRACE-196** (which stays CONDITIONAL) |
| F8 | TRACE-179 / H∞,7 | Correctly left open, with a correct reduction to a finite certificate | TRACE-196 **stays conditional**; add an annotation |
| F9 | Mechanism / generality | Discussion. The strip-width condition (w > c·0.6036, any β > 0) is consistent with §2 | Text only |

### F.2 F1: re-derivation (trace class and trace formula)
1. **Inclusions.**
   * Vertex: |ψ_n(s) − c′| ≤ |δ| + ρ/λ, with |δ| < ½ (ties are impossible because λ is irrational). This needs ρ_V > λ/(2(λ−1)) = 0.6036. ✓
   * Edge: I re-derived |δ_E| ≤ 1/(2λ). From |y−j| ≤ ½ and |y + 1/λ − j − 1| ≤ ½ we get y − j ∈ [½ − 1/λ, ½], so δ_E = (y−j) − ½ + 1/(2λ) ∈ [−1/(2λ), 1/(2λ)]. Hence ρ_E > 1/(2(λ−1)) = 0.1036. ✓
2. **Block bounds.** In normalised coordinates the composition is σ ↦ σ/λ + δ/ρ, so ‖e_l∘ψ‖_{H²} ≤ θ^l with θ = |δ|/ρ + 1/λ. This gives ‖C‖ ≤ (1−θ²)^{−1/2} by Cauchy–Schwarz and ‖C‖₁ ≤ 1/(1−θ) by the rank-one expansion. The multiplier norm on H² is its sup, W_n e^{2πc|n|ρ}. The weighted-space block norm carries the factor ω_c/ω_{c′}. ✓
3. **Trace class of L on the weighted ℓ²⊕H².**
   * Σ over all blocks of ‖·‖₁ is finite. Core and far rows are finite sums plus a Bessel tail.
   * For rows |c| > R, ω_c/ω_{c′} ≤ e^{−β(|c|−R)} + e^{−β(1−1/λ)|c|}e^{β(|n|/λ+½)}, which is summable in c for any β > 0 and in n given Σ W_n e^{(2πcρ+β/λ)|n|} < ∞.
   * β > 0 is genuinely needed: with β = 0 the far rows are not summable. That is correctly built into the hypothesis. ✓
4. **Trace formula.**
   * Tr L^m = Σ_c Tr (L^m)_{cc} is a sum over closed chains, and it converges absolutely: Σ_chains Π‖B_j‖ ≤ (Σ_blocks ‖B‖₁)^m. Along a closed chain the weights cancel.
   * Each closed chain is a single operator M_pC_ψ on H²(D(c₀,ρ)), with ψ affine of slope λ^{−m} mapping the closed disc into the open disc.
   * The Ruelle / Bandtlow–Jenkinson formula Tr = p(s*)/(1−ψ′) is therefore applied **only to single composite operators**, which is exactly its setting. The infinite alphabet is handled by the trace-class summation, not by the cited theorem. **Applicable as stated.** ✓
   * Lidskii and Weyl hold on the (Hilbert) weighted space. ✓
5. **Combinatorics.**
   * N_V(w) = #Fix F_w. N_E(w) = #{e : e, e+1 ∈ Fix F_w}: a degenerate step can never re-separate, so a closed edge chain means both endpoints are fixed.
   * F_w has increments in {0,1} and F(k)−k → ∓∞, so N_V − N_E = 1.
   * **Lean** (`LineF.lean`): rebuilt by me in `formalization` (Lean 4.33.1; `lake exe cache get`: "No files to download"; `lake env lean`: EXIT 0, 315 s, `logs/leanF.out`). No `sorry`, `admit` or `native_decide`. Axioms: propext, Classical.choice, Quot.sound. The statements match the prose:
     - `vertex_minus_edge` counts fixed points minus *adjacent fixed pairs* on [A,B], and `fix_outside` shows that these are global counts;
     - `edge_closed_iff` identifies adjacent fixed pairs with closed edge chains.
   * The glue (closed edge chain ↔ operator block of L_E^m) is prose. Real shifts are allowed, so the 49-state law is covered.
6. **Link to Z_m(ν*).** E1/E2 (TRACE-183/184) are termwise identities. I checked |c_a| = ½ (a even) and c_a = 0 (a odd) for κ ∈ {1, 3, 5, 7} (`logs/check1.log`), so the κ table being [N] is harmless. ✓
7. **Independent numerics** (`code/own_lift.py`, `own_fast.py`, `check1.py`, `check2.py`):
   * float spectra: sector 4 top eigenvalue 1.9154732041, next 0.7278; sectors 2/6: 0.8774; sector 0: 0.5742. The ghost eigenvalues 0.3624 and 0.2659 appear in both V and E;
   * brute force at m = 5 agrees to 3.8e-11;
   * physical finite-N traces: 1.4e-13 (m = 5) and 2.0e-11 (m = 7). For comparison, Line E's truncated L = 10 law reached about 1e-8.

### F.3 F2: audit of `cert_lift.py` (line by line)
1. **Galerkin exactness.**
   * M[l,j] = z^{l−j}/(l−j)! is lower triangular. C[j,k] = binom(k,j)λ^{−j}(δ/ρ)^{k−j} is upper triangular.
   * QCP = 0, so P(MC)P = (PMP)(PCP) exactly. ✓
2. **δ (Galerkin error).**
   * δ₁ = ‖A(I−P)‖: a column-wise Cauchy–Schwarz over per-block bounds W M θ^K/√(1−θ²). Valid. ✓
   * δ₂ = ‖(I−P)AP‖_HS: Taylor coefficients bounded by Cauchy on |σ| = 2. sup|p| = W e^{2πc|n|2ρ}, |e_l∘ψ| ≤ ((|δ| + 2ρ/λ)/ρ)^l, Σ_{i≥K}4^{−i} = 4^{−K}/(3/4). Aggregated per (c,c′) before squaring. Valid. ✓
3. **Δ and X.**
   * ‖·‖ ≤ (Σ_rows (Σ_{blocks in row}‖B‖)²)^{1/2}, using ‖Φ_{c′}‖ ≤ ‖Φ‖. Valid, though crude. ✓
   * Core rows: big letters and far targets are included. Far rows |c| ≤ Rmax: X versus Δ is split correctly.
   * Bessel tail: |J_n(x)| ≤ (x/2)^n/n! (DLMF 10.14.4), giving 2t^{N+1}/(N+1)!/(1 − t/(N+2)). ✓
   * Weight factors: e^{β(|c|/λ+½)}e^{β|n|/λ} for core rows (Rc ≥ 0), and ω_c times the same for far rows. ✓
   * Analytic rows |c| > Rmax: the formula for far2 / farT matches my derivation. The lattice starts at Rmax + ½ (E) or Rmax + 1 (V). Using cmin = Rmax + ½ for V over-counts, which is safe. There is no gap between the explicit rows and the analytic rows. ✓
   * Every block of L lies in exactly one of A, X, Δ. ✓
4. **Comparison operator and contours.**
   * T₀′ = [[PAP⊕0, 0],[X, 0]] is block lower triangular, so ‖R‖ ≤ (‖R_core‖ + 1/|z|)(1 + ‖X‖/|z|) + 1/|z|. ✓
   * The Householder H is built from an exact (midpoint) vector, so it is exactly unitary and Hermitian. B = HAH is enclosed by ball arithmetic, b21 is moved into the perturbation, and the 2×2 block-triangular resolvent bound is correct. ✓
   * Neumann bound in blocks of p via ‖Y^j‖_F. It is valid for all |z| ≥ r, so no z-sampling is needed. ✓
   * **Two contours suffice.** P_out = I − P_{|z|<r₂}, and finite-rank projections have constant rank under homotopy. So exactly one eigenvalue lies outside |z| = r₂, and it is the one in D(b11, r₁) (checked rlow > r₂). It is simple (rank 1). ✓
5. **Float leakage and the skip bug.**
   * The float eigenvector is used only to pick H, and every quantity used is a ball.
   * The current code aggregates blocks with `acb_mat` operations and has no `!= 0` test.
   * **All 33 cert JSONs postdate the final code.** start = mtime − `secs`: run 1 started 13:05:15, which is the mtime of `cert_lift.py` (13:05:15.0, box clock). Every other run started later (13:20–14:15). So no reported cert used the buggy draft. ✓
   * `bounds_lift.py` reads float(lower/upper) from the JSON and pads by 2^{−50} relative, which covers the ≤ 1 ulp error of float conversion. ✓
6. **Other sectors.**
   * The JSON checks pass: η = 2, V sector 0/2/6 F·R₂ = 7.0e-7 / 1.4e-6 / 1.4e-6; E sectors ≈ 1.0e-9.
   * **Reflection lemma (referee, [P]).** Define (UΦ)_c(s) = Φ_{−c}(−s). It is unitary on both lattices (rounding is odd away from ties, edge adjacency and targets are preserved, and the weights are symmetric). Since w_6(n) = w_2(−n), we get L_{·,6} = U L_{·,2} U⁻¹, so sectors 2 and 6 have identical spectra. This explains why the logs for sectors 2 and 6 are identical. It would close the pending η = 2.5 E sector 6 from the certified E sector 2, *if* the lemma is added to the text.

### F.4 Independent re-certification (referee's own code, `code/own_cert.py`, `logs/own_*`)
* **Implementation.** Written from scratch from my derivation in F.2–F.3. It uses the same mathematical framework but different code and parameters:
  - V: K0 = 4, ρ = 1.1, K = 40 (dimension 360), β = 2, Nmax = 50, Rmax = 30, Cauchy radius 1.8ρ, p = 36;
  - E: ρ = 0.7, K = 30 (dimension 240), p = 30.
* **Bounds.**
  - V: δ = 9.2e-7, Δ = 1.8e-10, ‖X‖ = 7.06, ‖L_V‖₁ ≤ 524.20;
  - E: δ = 5.5e-7, Δ = 5.6e-14, ‖X‖ = 0.40, ‖L_E‖₁ ≤ 18.53.
* **Results at η = 2, k1, full alphabet:**
  - **V sector 4: CERTIFIED.** Exactly one simple eigenvalue in D(b11, 1e-3), |μ*| ∈ [1.9144732, 1.9164733]. F·R₁ = 0.146, F·R₂ = 1.9e-3, with r₂ = 1. Consistent with Line F's [1.9154712, 1.9154752] and the float value 1.9154732.
  - **V sector 0: CERTIFIED** (|z| < 1, F·R₂ = 2.8e-4). **V sector 2: CERTIFIED** (F·R₂ = 5.5e-4, Frobenius root 0.928). Sector 6 follows by the reflection lemma.
  - E sectors: **E sectors 4, 0, 2: CERTIFIED** (|z| < 1; Frobenius root ≈ 0.380; F·R₂ = 4.5e-6). Sector 6 follows by reflection.
* **Referee's independent all-m consequence:** The same chain with my numbers (`code/own_bounds.py`, `logs/own_bounds.log`; μ_lo = 1.9144732, T_V ≤ 524.20, T_E ≤ 18.53, r₂ = 1) gives Z > 0 from m = 13, **F_m/2m ≥ 6.654 and W̃rest_m/m ≥ 9.308 at m = 15**, and growth rate μ_lo²/√λ ≥ 1.5181. So the qualitative F3 (all odd m ≥ 15, exponential growth) is **independently reproduced**. My numbers are slightly *stronger* at m = 15 because my trace-norm bound is smaller (ρ_V = 1.1).

### F.5 F3: inequality chain and constants
* |Z| ≥ ½(1−λ^{−m})(μ_lo^m − r₂^{m−1}·4(T_V + T_E)), using:
  - |c_a| = ½;
  - Lidskii;
  - Weyl, Σ_{k≠*}|μ_k|^m ≤ r₂^{m−1}‖L‖₁, applied to 1 (V₄, other eigenvalues) + 3 (V_{0,2,6}) + 4 (E) operators;
  - one sector-independent trace bound (it uses |w|). ✓
* F_m ≥ |Z(ν*)|²/φ(2h); h is odd, so φ(2h) = φ(h) ≤ h − 1. Then W̃rest ≥ F − 4m (TRACE-165, 170). ✓
* Closed form:
  - h² = (λ^m + λ^{−m} − 2)/4 < λ^m/4, so 2(h−1) < λ^{m/2};
  - (1 − 3012.29/μ_lo^15)² = 0.67948 and ¼(1−λ^{−15})²·0.67948 = 0.16987 ≥ 0.169;
  - μ_lo²/√λ = 1.519762 ≥ 1.5197;
  - g^m/m increases because g²·m/(m+2) > 1.
* The `bounds_lift.py` rows (exact h_m, m ≤ 199) are monotone at every η. ✓
* Hence "F_m/2m ≥ 6.03 for all odd m ≥ 15" is **true** (6.0347).
* "W̃rest_m/m ≥ 8.07" is **false as stated** (8.06947). It must be 8.06.

### F.6 Required fixes (F), blocking
1. **Unsafe roundings** (lower bounds rounded up, or enclosure ends rounded inward). Certified values are from `logs/bounds_eta*.json` and `certV_*`:
   * η = 2:
     - W̃rest/m: 8.07 → **8.06** (8.06947); 68.9 → **68.8** (68.869); 6.96e3 → **6.95e3** (6956.6); 3.46e5 → **3.45e5** (345923);
     - F/2m: 1.73e5 → **1.72e5** (172963.5); 5.7e15 → **5.6e15** (5.6618e15);
     - μ* upper end 1.9154752 → **1.9154753** (1.91547520413), in §0, §1 and §3. §5 table [1.915471, 1.915475] → **[1.915471, 1.915476]**;
     - T_V "730.1" in the §5 table → **730.15** (730.1421);
     - rate "1.5198" (§5 table) → **1.5197**.
   * η = 1.25:
     - "F/2m ≥ 2.928 from m = 31" (§1 F5) → **2.927** (2.92798);
     - "0.144" → **0.143** (0.14371);
     - §5 enclosure [1.708751, …] → **[1.708750, 1.710751]** (lower 1.70875096; §3 already has this right, so §3 and §5 currently disagree).
   * η = 1.5: "1.1" → **1.09** (1.0971); "7.32" → **7.31** (7.319); rate "1.3584" → **1.3583** (1.35836); upper end 1.812900 → **1.812901**.
   * Recheck every other printed bound by script. Easiest: have `grid_table.py` print with floor/ceil-based formatting.
2. **H∞ wording.** "Removes H∞ of TRACE-188" should read: "proves the **conclusion** of TRACE-188 (k1, η = 2) unconditionally (computer-assisted), on a different, explicit space. H∞ as stated (a single analytic domain ⊃ D_ρ) is neither proved nor needed." The report's §4 "Scope" already says this; make §0 and §1 match.
3. **η = 2.5 row.** Either wait for pid 552224 and run `bounds_lift.py`, or add the reflection lemma (§F.3.6) and derive E sector 6 from sector 2. Until one of these is done, η = 2.5 must not appear in any claim.
4. **F7 wording:** replace "real, not a discretisation artefact" with "stable under two discretisations [N]".
5. **Lean packaging.**
   * Move `LineF.lean` into `formalization/Bgs/` (namespace `Bgs.LineF`) and import it from `Bgs.lean` so CI builds it.
   * The prose should state exactly what is formalised: fixed-point / adjacent-pair counting and the edge-chain characterisation. It should state what is not: trace class, the trace formula, and all certificates.
6. **Theorem hypotheses.** State F1's hypotheses in the theorem itself: ρ_V > 0.6036, ρ_E > 0.1036, β > 0, Σ|w(n)|e^{α|n|} < ∞ with α > 2πcρ_V + β/λ (and likewise for E).

### F.7 Nits (F)
* Encode the closed-form all-m argument (m > 199) as an assertion in `bounds_lift.py`. Today it lives only in prose.
* Literature:
  - add Degli Esposti–Winn, J. Phys. A 38 (2005) 5895 (N-dependent quantum symmetries of perturbed cat maps; a different mechanism, and their Thm 2 gives s = 1 for this S). I verified the citation;
  - Manning 1971 (inclusion–exclusion for zeta functions) is the right ancestor;
  - Mayer, *The Ruelle–Araki transfer operator in classical statistical mechanics*, LNP 123 (1980).
  - The novelty claim ("no prior rigorous all-m result of this type that I know of; search not exhaustive") is appropriately modest. A quick search found nothing contradicting it.
* Add to "Reproduce" that the certs ran with python-flint 0.9.0 at 128 bits and took 5–30 min each at load ≈ 27.
* Internal times in NOTES (12:45–15:14) are box-clock times. They are consistent with file mtimes but not with the note headers ("CET"). Harmless.

---------------------------------------------------------------------------------------------------------------------------------
## PART G — general resonance law, dilution, classification, R′

### G.0 Verdict
The algebraic core is sound and builds in Lean: G1 (phase split), G1′ (automaton) and G2 (partial-trace law, finite alphabet). I verified G2 independently with my own code.

The rest is mixed:
* G3 (dilution) is a correct identity as far as tested, but has only a proof sketch.
* G6 is a trivial count.
* G7 is a heuristic dressed as [P].
* R′ is correctly tagged [C], but its definition is inconsistent between §0 and §3.
* There is one **substantive overclaim** about the original Conjecture R (§3), and it contradicts the report's own §8.

The m = 17 test is **not available**. The k1 m = 17 class-sum job (pid 507001) was at 160 000/1 607 521 after 2.6 h, so roughly a day remains. Nothing at m = 17 can be claimed.

### G.1 Claim-by-claim verdicts

| # | Claim | Audit result | Recommended status |
|---|---|---|---|
| G1 | Phase split −νP/2h ≡ −(2a/b)q − kP/b | Trivial algebra. Lean `phase_split` builds | **PROVED** [P][Lean] |
| G1′ | Automaton for P mod b | Lean `u_succ`, `w_succ`, `quad_form` build. I checked ψ(d) = 4h(H⁻¹)_{0d} = y′x_d − 2h·y_d for d < m (m = 5, 7). So P = Σψ(\|i−j\|)n_in_j holds **exactly** (Line E, TRACE-183 proof step 2) and the automaton is exact. The report's remark that the "cyclic boundary bookkeeping is checked numerically" is unnecessary and confusing: cite TRACE-183 instead | **PROVED** [P][Lean] |
| G2 | Z_m(ν) = (1−λ^{−m}) Tr_H[(I⊗⟨𝟙\|)𝓛^m(I⊗\|δ₀⟩)], finite alphabet | Proof correct (trace formula on single composite operators; P is reversal-invariant). **Referee's own code** (`code/g_law.py`, `logs/g_law.log`): random complex weights, \|n\| ≤ 2, m = 5, brute force over all units. Agreement is 1e-15 for every tested (a,b) with \|a\|/b ≤ 1 ((−4,6), (−3,5), (4,6), (−1,5), (−2,8)). Large-coupling cases degrade, as G itself says; that is Galerkin conditioning, not the law. **Fix:** "exponential polynomial" should read "exponential sum Σ c_μ μ^m" (trace-class, infinitely many μ). For k1 the infinite alphabet now needs a Line-F-type lift of the C^{b²}-extended operator; not done | **PROVED** [P][Lean core][N], finite alphabet |
| G3 | Dilution identity for d \| h | The check (`check_dilution.py`) is a genuine brute-force-vs-formula test, but only for **prime** d (7 at m = 9, 41 at m = 5) and alphabets \|n\| ≤ 1, 2; error ≤ 2.8e-14. Composite d (e.g. 217 at m = 15, which the text uses) is untested. The proof is a sketch, and the main-term error is unbounded (stated honestly) | **[P-sketch]+[N]**. "Proved" only after a full written proof, and ideally a composite-d check |
| G4 | Galois scaling | Equals TRACE-193; not new | No new claim (cross-reference) |
| G5 | h_d \| h_m for d \| m, m odd | Lean `nsw_dvd` builds. This is the classical divisibility-sequence property, so novelty is nil. Nit: Lean never proves nsw 17 = 1607521 (add `example : nsw 17 = 1607521 := by decide`) | **PROVED** [Lean], low novelty; fold in as a lemma |
| G6 | Sparsity \|𝓡\| ≤ 2\|𝓟\|τ(h)D | Correct but tautological for a fixed finite 𝓟 | Lemma inside the classification record |
| G7 | Moment hierarchy: relevant iff r > λ^{1/(4k)} | The heuristic is right for a *single* family. "iff" is not proved, since "irrelevant" also needs control of everything else, and the inputs (rates, O(h^{o(1)}) members, baseline) are assumptions. §6's "a CLT in moment form is false" rests on float rates 1.33–1.41 | Relabel **[heuristic]** (or [P] conditional on stated hypotheses); §6 → "expected to fail [N]" |
| Step 1 / tables | Classification of outliers at m = 7..15; rates (±4: 1.9154732; ±8: ≈1.615; ±2: ≈1.50); bulk; η-scan | Spot checks: the k1 F/2m values (4.839, 6.894, 11.197, 27.885) match Line E's referee class sums; the W′ arithmetic in the §3 table is consistent; r(±4) matches my full-alphabet float 1.9154732041. r(±8) and the others are not independently checked | **[N] record** |
| R′ | Corrected conjecture | Tagged [C] with an honest drift caveat ✓. But (i) §0 and §3 give **different** formulas: §3 subtracts RMT_m per member, §0 does not; (ii) n_d(ρ), RMT_m, the cut-off and Res_pred/Res_act are not defined precisely; (iii) the evidence is four points m = 9..15 with W′/m drifting upward by +0.27 per step, which is weak; (iv) the m = 17 pre-registration (sha256 fa8505f5…aa344, verified to match the file; file mtime 13:17 box clock, before any m = 17 output) is self-attested | **CONJECTURE (open)**, only after the definition is fixed. Commit `PREDICTIONS_m17.json` and its hash in the integration PR **before** the m = 17 outcome exists |

### G.2 Required fixes (G), blocking
1. **§3 overclaim.** "The original Conjecture R (F/2m → 2) is false for these kicks along all m (as already found in Line E)" is wrong on three counts:
   * R (TRACE-179) is max_η|W̃rest_m(η)| = o(m), not F/2m → 2;
   * for **k1**, asymptotic failure is established only by Line F's packet (computer-assisted). Line E had it conditionally (TRACE-188) or on a finite range (TRACE-187);
   * for the **full (Line B) kick**, it is only conditional on H∞,7 (TRACE-196), with |W̃rest| > m certified at m = 11 and 13 only (TRACE-195). **R is not disproved.**
   
   Rewrite accordingly and make §8 consistent. §8 currently says R′ "does not concern the original R, which is already refuted for k1 on a finite m-range": a finite range does not refute an o(m) statement.
2. **§0.1** "every outlier … explained … all proved as identities": G3 is a sketch, and "explained" means numerically, within the stated main-term tolerances (up to 37% at d = 287). Say so.
3. **R′ definition:** one formula, defined symbols, and a fixed cut-off and family list 𝓟*, frozen before m = 17.
4. **G7 / §6** relabelling as above. **G2** wording ("exponential sum"; cite TRACE-183 for exact P).
5. **Lean packaging** as for F (`formalization/Bgs/LineG.lean`, imported; my rebuild: EXIT 0, 80 s, std axioms, `logs/leanG.out`).

### G.3 Nits (G)
* "2k-th moment of |Z|²" (§0) vs "(1/φ)Σ|Z|^{2k}" (§1) is inconsistent: the latter is the k-th moment of |Z|².
* §1 G3: state |G_d| = d for odd d with gcd(t,d) = 1 (the discriminant of x² − 2y² is 8, so odd d is needed).
* Literature: the Degli Esposti–Winn citation is correct (verified). Novelty is stated modestly ✓.

---------------------------------------------------------------------------------------------------------------------------------
## Integration packet list (IDs continue after TRACE-196; rebase on e378ad11)

| ID | Content | State | Depends on |
|---|---|---|---|
| **TRACE-197** | F1: lifted vertex−edge trace identity, full alphabet (k1 and real-shift / 49-state form) | PROVED [P]+[Lean core]+[N] | 183, 184 |
| **TRACE-198** | F2: η = 2 k1 full-alphabet certificate: simple μ*, \|μ*\| ∈ [1.9154712, 1.9154753]; rest \|z\| < 1 (all sectors, V and E); ‖L_V‖₁ ≤ 730.15, ‖L_E‖₁ ≤ 22.94; plus the reflection lemma L₆ ≅ L₂ | PROVED (computer-assisted) | 197 |
| **TRACE-199** | F3: for every odd m ≥ 15, F_m(2)/2m ≥ 6.03, W̃rest_m(2)/m ≥ **8.06**, ≥ 0.169·1.5197^m/m; the k1-kick analogue of R fails at η = 2 (asymptotically, all odd m) | PROVED (computer-assisted) | 197, 198, 165, 170 |
| **TRACE-200** | F4: the same for f₇ = 0.9cos(2π·7q), odd m ≥ 15, 3 ∤ m | PROVED (computer-assisted) | 193, 199 |
| **TRACE-201** | F5: certified η grid {1.25, 1.5, 1.75, 2.25} with the corrected table; η = 2.5 only if completed | PROVED (computer-assisted), grid points only | 197 |
| **TRACE-202** | F6: growth window (0.951, 3.212), float | OPEN [N] (relates to TRACE-191) | 197 |
| **TRACE-203** | G1/G1′/G2: general (a,b) partial-trace law, finite alphabet | PROVED [P]+[Lean core]+[N] | 183, 184, 194 |
| **TRACE-204** | G3: dilution identity | OPEN (proof sketch + exact checks, prime d) until a full proof is written | 203 |
| **TRACE-205** | Classification record (Step 1, rates, G5–G7, η-scan) | OPEN [N] / heuristic; G5 as a Lean lemma | 203, 204 |
| **TRACE-206** | Conjecture R′ (fixed definition) + pre-registered m = 17 test (hash committed) | CONJECTURE / OPEN | 205, 179 |

**Annotations, states unchanged except where noted:**
* TRACE-188: "conclusion established unconditionally (computer-assisted) by TRACE-199 on a lifted space; H∞ as stated not proved and no longer needed". Either keep it CONDITIONAL with this annotation or mark it SUPERSEDED per repo conventions.
* TRACE-187: "extended to all odd m ≥ 15 at η = 2 by TRACE-199".
* TRACE-196: "the infinite-alphabet part is reduced by TRACE-197 to a finite (~24k-dimensional) certificate; float evidence F7". It stays **CONDITIONAL**.
* TRACE-179: **OPEN**, unchanged.
* TRACE-191: open (grid only).
