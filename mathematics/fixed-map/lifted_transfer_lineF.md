# Line F: full-alphabet resonance transfer operators on lifted Hardy spaces, and an all-m failure of the k1-kick analogue of Conjecture R

**Claims:** BGS-TRACE-197 to BGS-TRACE-202. **Annotated (states unchanged):** BGS-TRACE-187, BGS-TRACE-188, BGS-TRACE-191, BGS-TRACE-196. **BGS-TRACE-179 (Conjecture R) stays open.**

**Inputs** (cited, not re-claimed):
- Line E (`resonant_residue_lineE.md`): BGS-TRACE-183 (E1, the resonant residue N ≡ −4 mod h_m and the collapse of the phase), BGS-TRACE-184 (E2, the four-sector law with |c_a| = ½ for even a, c_a = 0 for odd a), BGS-TRACE-193 (E11, Z_{f7}(ν) = Z_{k1}(49ν) for 3 ∤ m), BGS-TRACE-194 (E12, the 49-state law).
- BGS-TRACE-165 (B^sym_m ≤ 2m) and BGS-TRACE-170 (W̃rest_m = F_m − B^sym_m − 2mχ_m, |χ_m| ≤ 1).
- Standard theorems: the Ruelle / Bandtlow–Jenkinson trace formula for a single weighted composition operator with a contracting holomorphic symbol; Lidskii's theorem; Weyl's inequality.

**Review state.**
- Written by the Line F author (`computations/verification/lineF/AUTHOR_REPORT.md`) and audited by an independent referee (`computations/verification/lineFG/referee/REPORT.md`, Part F). The referee re-derived F1–F3 line by line, reproduced the physical traces with an own float implementation of the lift, and re-certified the η = 2 spectrum with an own arb certifier (different code and parameters: |μ*| ∈ [1.914473, 1.916474], F_15/2m ≥ 6.65).
- All blocking fixes of the referee (§F.6) are applied below, marked **[RF1]**–**[RF6]**; nits are marked **[RFn]**.
- **Rounding convention [RF1].** Every certified quantity is quoted in the safe direction: lower bounds rounded down, upper bounds rounded up, enclosures rounded outward. All numbers in the tables below are printed by `computations/verification/lineF/code/safe_table.py` from the JSON logs (`computations/verification/lineF/logs/safe_table.md`), not typed by hand.

**Labels.** **[P]** proved here; **[CA]** computer-assisted rigorous (arb ball arithmetic, python-flint 0.9.0, 128-bit working precision, JSON logs); **[Lean]** kernel-checked in `formalization/Bgs/LineF.lean`; **[N]** floating-point numerics.

## 0. Scope and summary

Kicks are named as in Line E §0: **k1** is 0.9 cos 2πq, **f7** is 0.9 cos 2π·7q, **f_B** is the Line B / TRACE-179 kick. Everything rigorous in this document is about **k1** (and f7 by E11). Nothing here is a statement about f_B, i.e. about Conjecture R itself.

Line E proved an exact m-independent transfer-operator law at the resonant residue ν* (N ≡ −4 mod h_m), but only for kicks truncated to |n| ≤ L; the asymptotic statement for the untruncated k1 kick was conditional on H∞ (BGS-TRACE-188).

Line F replaces the single-disc operator by two trace-class operators L_V ("vertex") and L_E ("edge") on weighted ℓ²-direct sums of Hardy spaces over a lattice of discs. Their trace difference reproduces the full-alphabet sum exactly, for every m (F1). A ball-arithmetic certificate for these operators at η = 2 (F2) then gives, for **every** odd m ≥ 15 (F3):

  F_m(2)/2m ≥ 6.03,  W̃rest_m(2)/m ≥ 8.06,  F_m(2)/2m ≥ 0.169 · 1.5197^m / m.

So the k1-kick analogue of Conjecture R fails at η = 2 unconditionally (computer-assisted) and asymptotically. **[RF2]** This proves the *conclusion* of BGS-TRACE-188 (k1, η = 2) unconditionally (computer-assisted), on a different, explicit space. Hypothesis H∞ as stated in BGS-TRACE-188 (a single analytic domain containing D_ρ) is neither proved nor needed; BGS-TRACE-188 keeps its state and is annotated.

**Not done:** the Line B kick f_B (TRACE-179 itself). The 49-state version of the lift is checked numerically (F7), but the rigorous certificate would need a ≈ 24 000-dimensional ball-arithmetic enclosure that was not run (§7). BGS-TRACE-196 stays conditional.

## 1. Results

| ID | # | statement | label | state |
|---|---|---|---|---|
| BGS-TRACE-197 | F1 | lifted vertex−edge trace identity, full alphabet (k1, and real shifts, e.g. the 49-state law) | [P] + [Lean] combinatorial core + [N] | proved |
| BGS-TRACE-198 | F2 | η = 2 certificate: simple μ*, \|μ*\| ∈ [1.9154712, 1.9154753]; rest of the spectrum in \|z\| < 1 (all sectors, both lattices); ‖L_V‖₁ ≤ 730.15, ‖L_E‖₁ ≤ 22.94; reflection lemma L_6 ≅ L_2 | [CA] + [P] | proved (computer-assisted) |
| BGS-TRACE-199 | F3 | all odd m ≥ 15: F_m(2)/2m ≥ 6.03, W̃rest_m(2)/m ≥ 8.06, F_m(2)/2m ≥ 0.169·1.5197^m/m; the k1 analogue of R fails at η = 2 | [CA] | proved (computer-assisted) |
| BGS-TRACE-200 | F4 | the same for f7, odd m ≥ 15 with 3 ∤ m | [P] + [CA] | proved (computer-assisted) |
| BGS-TRACE-201 | F5 | certified η grid {1.25, 1.5, 1.75, 2.25, 2.5} (table §5) | [CA] | proved (computer-assisted), grid points only |
| BGS-TRACE-202 | F6 | growth window: \|μ*(η)\| > λ^{1/4} for η ∈ (0.951, 3.212) | [N] | open |

F7 (the 49-state lift for f_B) and F8 (H∞,7) are evidence and an annotation for BGS-TRACE-196, not new claims.

## 2. The lift and the exact trace identity (F1, BGS-TRACE-197)

**Setting.** λ = 3 + 2√2 and c = 1/(λ − λ⁻¹) = 1/(4√2). A letter n ∈ Z acts by ψ_n(s) = (s + n)/λ with multiplier e(cns). For a periodic word the real periodic orbit s_{j+1} = (s_j + n_j)/λ gives ½nᵀH⁻¹n = c[Σ n_j s_j + ½Σ n_j²] (E2, TRACE-184).

**Vertex lattice.** States k ∈ Z with discs D(k, ρ_V). Letter n sends k to f_n(k) := ⌊(k + n)/λ + ½⌋, with δ = (k + n)/λ − f_n(k) ∈ (−½, ½) (no ties, λ is irrational).
  (L_V Φ)_k(s) = Σ_n w(n) e(cns) Φ_{f_n(k)}(ψ_n(s)),  s ∈ D(k, ρ_V).
ψ_n maps the closed disc D̄(k, ρ_V) into D(f_n(k), ρ_V) as soon as ½ + ρ_V/λ < ρ_V, i.e. ρ_V > λ/(2(λ−1)) ≈ 0.6036.

**Edge lattice.** States are pairs (e, e+1) with discs D(e + ½, ρ_E). A transition exists only if f_n(e+1) = f_n(e) + 1, and the target is the edge f_n(e). Then |δ_E| ≤ 1/(2λ) (re-derived by the referee: y − j ∈ [½ − 1/λ, ½]), and the inclusion holds for ρ_E > 1/(2(λ−1)) ≈ 0.1036.

**Space.** 𝓗 = {Φ = (Φ_k)} with ‖Φ‖² = Σ_k ω_k² ‖Φ_k‖²_{H²(D_k)}, ω_k = 1 on the core |k| ≤ R_c and ω_k = e^{−β(|k| − R_c)} outside; H²(D_k) has orthonormal basis ((s − k)/ρ)^i.

**Theorem F1 (BGS-TRACE-197) [P] [RF6].** Assume
- ρ_V > λ/(2(λ−1)) ≈ 0.6036 and ρ_E > 1/(2(λ−1)) ≈ 0.1036;
- β > 0;
- Σ_n |w(n)| e^{α|n|} < ∞ for some α > 2πcρ_V + β/λ (this also covers the edge lattice, since ρ_E < ρ_V in all uses; in general require α > 2πc·max(ρ_V, ρ_E) + β/λ).

Then L_V and L_E are trace class on their weighted spaces, and for every m ≥ 1

  Σ_{n∈Z^m} Π_j w(n_j) e(c n_j s_j) = (1 − λ^{−m})(Tr L_V^m − Tr L_E^m),

where s_j is the periodic orbit of the word n. Combined with E1/E2 (TRACE-183/184), whose algebra holds termwise for every n ∈ Z^m:

  Z_m(ν*) = (1 − λ^{−m}) Σ_{a∈{0,2,4,6}} c_a (Tr L_{V,a}^m − Tr L_{E,a}^m),  |c_a| = ½,

for the **full** (untruncated) alphabet, where L_{·,a} uses the weights w_a(n) = ĝ(n) e(cn²/2 + an/8). The same holds for real shifts x in place of integer letters (the 49-state law, x = n/7).

*Proof.*
1. *Trace class.* With W_n = |w(n)|, M_n = e^{2πc|n|ρ} (the supremum of the multiplier on a disc of radius ρ) and θ = |δ|/ρ + 1/λ < 1, a block Φ_{k′} ↦ w e(cn·)Φ_{k′}∘ψ_n has operator norm ≤ W_nM_n(1−θ²)^{−1/2} and trace norm ≤ W_nM_n/(1−θ) (rank-one expansion Σ_i ⟨·, e_i⟩ p·(e_i∘ψ), ‖e_i∘ψ‖ ≤ θ^i). On 𝓗 the block carries the factor ω_k/ω_{k′}; for |k| > R_c, |k′| ≤ (|k| + |n|)/λ + ½ gives ω_k/ω_{k′} ≤ e^{−β(|k|−R_c)} + e^{−β|k|(1−1/λ)+β/2} e^{β|n|/λ}. The sum of trace norms over all blocks is therefore finite by the hypothesis on α; β > 0 is needed for the rows far from the core. Lidskii and Weyl apply on these Hilbert spaces.
2. *Chains.* The diagonal block (k₀, k₀) of L^m is the trace-norm-convergent sum over closed chains k₀ → k₁ → … → k_m = k₀ of single weighted composition operators M_p C_ψ on H²(D(k₀, ρ)); ψ is affine with slope λ^{−m} and maps the closed disc into the open disc because the inclusions compose. The Ruelle / Bandtlow–Jenkinson formula Tr(M_p C_ψ) = p(s*)/(1 − ψ′(s*)) is applied only to these single composite operators, which is its setting; the infinite alphabet is handled by the trace-norm summation, not by the cited theorem. Off-diagonal blocks contribute nothing. Hence Tr L_V^m = Σ_{w∈Z^m} N_V(w) p_w(s*_w)/(1 − λ^{−m}), where N_V(w) is the number of closed vertex chains of the word w, and likewise for E.
3. *Counting.* For the composite F = f_{n_{m−1}}∘…∘f_{n_0}: F has increments in {0, 1} and F(k) − k → ∓∞ as k → ±∞, so Fix F is a non-empty finite integer interval; a closed edge chain at e is the same as e, e+1 ∈ Fix F (a degenerate step can never re-separate). Hence N_V(w) − N_E(w) = 1 for every word. This step is formalised (below).
4. Summing over words gives the identity; E1/E2 give the formula for Z_m(ν*). ∎

**Lean [RF5].** `formalization/Bgs/LineF.lean` (namespace `Bgs.LineF`, imported by `Bgs.lean`) proves the combinatorial step 3 for composites of rounding maps k ↦ ⌊(k + x)μ + ½⌋ with 0 ≤ μ < 1 and arbitrary real shifts x: `vertex_minus_edge` ((number of fixed points) − (number of adjacent fixed pairs) = 1, with all fixed points inside an explicit interval, `fix_outside`) and `edge_closed_iff` (adjacent fixed pairs are exactly the closed edge chains). **Not formalised:** trace class, the trace formula, the identification of closed chains with operator blocks (step 2, prose), and all certificates. No `sorry`, no `native_decide`; axioms propext, Classical.choice, Quot.sound.

**Numerical checks [N].**
- Brute-force finite-alphabet sums (L = 3, m = 1…5) versus Tr L_V^m − Tr L_E^m: relative error ≤ 4.2e-15 (`logs/spec_float.log`).
- Against the exact full-alphabet class sums |Z_m(ν*)|² of the Line E referee (`computations/verification/lineE/referee/logs/classes.jsonl`), m = 5…15: relative error ≤ 9.1e-14 (`code/xcheck_class.py`, `logs/xcheck_class.log`).
- Referee, own code (`computations/verification/lineFG/referee/code/own_lift.py`, `check2.py`): own lift versus own brute force at m = 5, L = 12: 3.8e-11 (the brute-force truncation); versus the *physical* finite-N traces |Tr U_N^m|² at N = h_m − 4: ≤ 1.5e-13 (m = 5), 2.1e-11 (m = 7), 8.0e-12 (m = 9), 9.0e-12 (m = 11), 4.3e-12 (m = 13; the referee's script finished after the referee report) (`computations/verification/lineFG/referee/logs/check2.log`).
- Ghost eigenvalues 0.3624 and 0.2659 appear in both L_V and L_E and cancel in the trace difference, as the counting lemma predicts.

## 3. The certificate (F2, BGS-TRACE-198) [CA]

`code/cert_lift.py typ η K0 ρ K β prec p r1 r2 Nmax Rmax sectors out` (arb, 128 bits).

**Splitting.** L = A + X + Δ:
- **A**: core←core blocks; the core is |k| ≤ K0 = 4 (9 vertex discs, 8 edge discs).
- **X**: far←core blocks, ‖X‖ ≤ 6.16 (V) and 0.33 (E) by row sums.
- **Δ**: everything else — big letters into core rows, far←far blocks, all rows |k| > Rmax = 40 (geometric series) and all letters |n| > Nmax = 60 (Bessel tail |J_n(x)| ≤ (x/2)^n/n!, DLMF 10.14.4): ‖Δ‖ ≤ 1.86e-9 (V), 7.5e-14 (E).

**Galerkin.** A truncated to degree K per disc (K = 55, ρ_V = 1.2: 495 dimensions; K = 40, ρ_E = 0.8: 320 dimensions). P(MC)P = (PMP)(PCP) is exact (multiplier matrix lower triangular, composition matrix upper triangular). Truncation error δ = δ₁ + δ₂ ≤ 4.5e-11 (V), 1.3e-10 (E).

**Comparison operator and contours.** T₀′ = [[H T₀ H ⊕ 0, 0], [X, 0]] is block lower triangular, so spec T₀′ = spec T₀ ∪ {0} and ‖R‖ ≤ (‖R_{T₀}‖ + 1/|z|)(1 + ‖X‖/|z|) + 1/|z|. Sector 4: T₀ is the Householder deflation [[b11, b12], [0, Y]] (H built from an exact midpoint vector, so exactly unitary), with b21 ≤ 1.1e-25 moved into the perturbation; other sectors: T₀ is the Galerkin matrix. ‖R_Y‖, ‖R_A‖ come from Neumann bounds with ‖Y^j‖_F, valid for all |z| ≥ r, so no z-sampling. If (δ + ‖Δ‖ + b21)·sup_Γ‖R‖ < 1 on both contours, the Riesz projections of T₀′ + t(L − T₀′) have constant rank for t ∈ [0, 1].

| run | η | F·R on circle 1 (must be < 1) | F·R on \|z\| = r₂ = 1 | result |
|---|---|---|---|---|
| V a=4 (r₁ = 2e-6) | 2 | ≤ 0.244 | ≤ 6.2e-6 | exactly one eigenvalue (simple) in D(b11, 2e-6); \|μ*\| ∈ [1.9154712, 1.9154753] **[RF1]** |
| V a = 0 / 2 / 6 | 2 | — | ≤ 7.1e-7 / 1.5e-6 / 1.5e-6 | spectrum in \|z\| < 1 |
| E a = 0, 2, 4, 6 | 2 | — | ≤ 1.1e-9 | spectrum in \|z\| < 1 |
| V a=4 (r₁ = 1e-3) | 1.25 | ≤ 3.4e-8 | ≤ 2.5e-10 | \|μ*\| ∈ [1.708750, 1.710751] **[RF1]** |
| V a = 0, 2, 6; E all | 1.25 | — | ≤ 1.1e-10 | spectrum in \|z\| < 1 |

Trace norms (η = 2, safe): ‖L_V‖₁ ≤ 730.15 (all four vertex sectors), ‖L_E‖₁ ≤ 22.94. Logs: `logs/certV_eta2_a{0,2,4,6}.json`, `certV_eta2_a4_tight.json`, `certE_eta2.json`, `certV_eta1.25_*`, `certE_eta1.25.json`. The exact JSON upper end of the η = 2 enclosure is 1.91547520413, hence the quoted 1.9154753.

**Reflection lemma (referee, §F.3.6) [P].** Let (UΦ)_k(s) = Φ_{−k}(−s) on the vertex lattice and (UΦ)_e(s) = Φ_{−e−1}(−s) on the edge lattice. Then U is unitary on 𝓗 and, for every weight sequence w, U L_w U⁻¹ = L_{w̃} with w̃(n) = w(−n). In particular L_{·,6} = U L_{·,2} U⁻¹ for the k1 kick, so the sectors 2 and 6 have identical spectra and traces.
*Proof.* s ↦ −s maps D(k, ρ) onto D(−k, ρ) (vertex) and D(e + ½, ρ) onto D(−e − ½, ρ) (edge) and preserves the H² norms; the weights ω are symmetric, so U is unitary (U = U⁻¹). Rounding is odd away from ties: f_{−n}(−k) = ⌊(−k − n)/λ + ½⌋ = −f_n(k), because (k + n)/λ + ½ is never an integer (λ is irrational, and 0 + ½ ∉ Z). Also ψ_{−n}(−s) = −ψ_n(s) and e(c(−n)(−s)) = e(cns). Hence
  (U L_w U⁻¹ Φ)_k(s) = Σ_n w(n) e(−cns) Φ_{−f_n(−k)}(−ψ_n(−s)) = Σ_{n′} w(−n′) e(cn′s) Φ_{f_{n′}(k)}(ψ_{n′}(s)) = (L_{w̃}Φ)_k(s),
substituting n = −n′. The edge condition f_n(e+1) = f_n(e) + 1 is mapped to f_{−n}(−e) = f_{−n}(−e−1) + 1, so edges and their targets are preserved. For k1, ĝ(−n) = i^{−n}J_{−n} = i^n J_n = ĝ(n) and e(c(−n)²/2) = e(cn²/2), while e(a(−n)/8) = e((8 − a)n/8); so w_{6}(n) = w_{2}(−n) (and sectors 0 and 4 are self-reflected). ∎
The certificate logs for sectors 2 and 6 are identical at every η, as the lemma predicts.

**Negative controls** (each must fail, and does): K = 25, sector 4, η = 2 (δ₂ = 0.045, F·R₁ = 1.15e4: not certified, `logs/neg_K25_a4.json`); r₂ = 0.85 for sector 2 (spectral radius 0.877 > 0.85; Neumann root 0.932 > r₂, annulus test fails, `logs/neg_r2_085_a2.out`); K0 = 3 with K = 20 (‖Δ‖ = 1.8e-5, F·R₁ = 5.9e5, `logs/test_V.json`).

**Provenance.** The first draft of `cert_lift.py` skipped Galerkin entries with `Mx[i,j] != 0` (for arb balls: "certainly non-zero"); it was replaced by block aggregation without skipping before any run used here. The referee checked that all certificate JSONs post-date the final code (run 1 started at the mtime of `cert_lift.py`).

**Independent re-certification (referee).** Own code `computations/verification/lineFG/referee/code/own_cert.py` (V: K0 = 4, ρ = 1.1, K = 40, β = 2, Nmax = 50, Rmax = 30; E: ρ = 0.7, K = 30): V sector 4 simple μ* with |μ*| ∈ [1.914473, 1.916474]; V sectors 0, 2 and E sectors 4, 0, 2 in |z| < 1 (6 by reflection); ‖L_V‖₁ ≤ 524.20, ‖L_E‖₁ ≤ 18.53. With these numbers the chain of §4 gives F_15/2m ≥ 6.654 and W̃rest_15/m ≥ 9.308 (`referee/logs/own_bounds.log`).

**Consistency.** Float eigenvalue of the full operator 1.9154733, inside the enclosure. Line E's truncated L = 6 enclosure [1.9154750, 1.9154771] (TRACE-185) is a different (truncated) operator; the truncation shifts μ by about 3e-6.

## 4. Main theorem (F3, BGS-TRACE-199) [CA]

By F1, Lidskii and Weyl (Σ_{k≠*}|μ_k|^m ≤ r₂^{m−1}‖L‖₁ for the eigenvalues |μ_k| ≤ r₂, applied to V₄ without μ*, V_{0,2,6} and the four E operators, each with the sector-independent trace-norm bound):

  |Z_m(ν*)| ≥ ½(1 − λ^{−m})(μ_lo^m − r₂^{m−1}·4(T_V + T_E)),  μ_lo = 1.9154712, r₂ = 1, 4(T_V + T_E) ≤ 3012.30.

This is positive for every odd m ≥ 13. Then F_m ≥ |Z_m(ν*)|²/φ(2h_m) with φ(2h_m) = φ(h_m) ≤ h_m − 1 (h_m odd), and W̃rest_m ≥ F_m − 4m (TRACE-165: B^sym ≤ 2m; TRACE-170: |χ_m| ≤ 1).

**Theorem F3 (BGS-TRACE-199).** For the k1 kick at η = 2 and every odd m ≥ 15: F_m/2m ≥ 6.03 and W̃rest_m/m ≥ 8.06; the bounds increase with m and F_m/2m ≥ 0.169·1.5197^m/m → ∞. In particular |W̃rest_m(2)| > m for all odd m ≥ 15, and the k1-kick analogue of Conjecture R (max_η |W̃rest_m(η)| = o(m)) is false.

Safe-direction values (`logs/bounds_eta2.json`, printed by `code/safe_table.py`) **[RF1]**:

| m | 13 | 15 | 17 | 19 | 21 | 25 | 31 | 41 | 61 | 101 |
|---|---|---|---|---|---|---|---|---|---|---|
| F_m/2m ≥ | 0.560 | 6.03 | 16.4 | 36.4 | 77.6 | 350 | 3480 | 1.72e5 | 5.02e8 | 5.66e15 |
| W̃rest_m/m ≥ | — | 8.06 | 28.8 | 68.8 | 151 | 696 | 6950 | 3.45e5 | 1.00e9 | 1.13e16 |

(At m = 13 the lower bound on W̃rest is negative, i.e. nothing is certified there.)

**All m.** h_m² = (λ^m + λ^{−m} − 2)/4 < λ^m/4 gives 2(h_m − 1) < λ^{m/2}; with (1 − 3012.30/μ_lo^m)² ≥ 0.679 for m ≥ 15:
  F_m/2m ≥ ¼(1 − λ^{−15})²·0.679·(μ_lo²/√λ)^m/m ≥ 0.169·1.5197^m/m,
and g^m/m increases because g²m/(m + 2) > 1 for g = 1.5197. **[RFn]** These steps are now asserted in `code/bounds_lift.py` (closed-form constants C ≥ 0.169, g ≥ 1.5197 from m = 15, checked against every explicit row m ≤ 199, and the rows checked to increase), not only stated in prose.

**Sanity.** The bounds lie below the exact values: m = 13, exact F/2m = 11.20 versus the bound 0.560; m = 15, 27.89 versus 6.03.

**Scope [RF2].** This proves the conclusion of BGS-TRACE-188 (k1, η = 2) unconditionally (computer-assisted), on a different, explicit space (the lifted weighted Hardy-space sums of §2). H∞ as stated in TRACE-188 is neither proved nor needed. It is not a statement about the Line B kick f_B and not a BGS counterexample.

**F4 (BGS-TRACE-200).** For f7 = 0.9 cos 2π·7q: Z_{f7}(ν) = Z_{k1}(49ν) when 3 ∤ m (TRACE-193), so F_m(f7) = F_m(k1) and W̃rest_m(f7) = W̃rest_m(k1) for 3 ∤ m, and F3 holds verbatim for f7 at η = 2, odd m ≥ 15, 3 ∤ m.

## 5. η grid (F5, BGS-TRACE-201) [CA]

Same pipeline: K0 = 4, r₂ = 1 for η ≤ 2; K0 = 5, r₂ = 1.45 for η ≥ 2.25. Every row is certified in every sector of both lattices. Printed by `code/safe_table.py` **[RF1]**:

| η | K0, r₂ | \|μ*\| ∈ | T_V ≤, T_E ≤ | μ_lo²/√λ ≥ | first odd m with Z > 0 | F/2m ≥ at m = 15 / 21 / 31 | first odd m with W̃rest/m > 1 (and all larger) |
|---|---|---|---|---|---|---|---|
| 1.25 | 4, 1 | [1.708750, 1.710751] | 215.28, 12.40 | 1.2094 | 13 | 0.1437 / 0.6303 / 2.927 | 31 |
| 1.5 | 4, 1 | [1.810900, 1.812901] | 324.85, 15.24 | 1.3583 | 13 | 1.097 / 7.319 / 107.1 | 19 |
| 1.75 | 4, 1 | [1.880799, 1.882800] | 487.67, 18.67 | 1.4652 | 13 | 3.662 / 36.03 / 1121 | 15 |
| 2 | 4, 1 | [1.915471, 1.915476] | 730.15, 22.94 | 1.5197 | 13 | 6.034 / 77.60 / 3480 | 15 |
| 2.25 | 5, 1.45 | [1.909830, 1.911831] | 1336.51, 37.60 | 1.5108 | 31 | — / — / 193.2 | 31 |
| 2.5 | 5, 1.45 | [1.866601, 1.868602] | 1990.37, 47.00 | 1.4432 | 35 | — / — / — (m = 35: 92.80) | 35 |

At η = 1.25 this gives F_m/2m ≥ 2.927 at m = 31 and |W̃rest_m| > m for all odd m ≥ 31; Line E showed no violation at η = 1.25 at all. For every row the lower bound on F/2m increases in m; the closed form F_m/2m ≥ C·g^m/m is asserted by `bounds_lift.py` (`closed_form` in each `bounds_eta*.json`).

**η = 2.5 [RF3].** The last pending certificate (E lattice, sector 6, pid 552224 in the author's run) finished after the referee's audit and is certified (`logs/certE_eta2.5.out`); its output is identical to sector 2, as the reflection lemma of §3 predicts, so η = 2.5 is covered both by the direct certificate and by the lemma. `bounds_lift.py 2.5` was then run with the same code (`logs/bounds_eta2.5.json`). This row was **not seen by the referee**; it uses the same code path as the audited rows. η = 2.75 and 3.0 were not run.

## 6. Growth window (F6, BGS-TRACE-202) [N]

Float spectra of the lifted operators (`logs/eta_curve.log`, `logs/eta_thresh.log`), sector-4 leading |μ*|:

| η | 0.25 | 0.5 | 0.75 | 1.0 | 1.25 | 1.5 | 1.75 | 2.0 | 2.25 | 2.5 | 2.75 | 3.0 | 3.5 | 4.0 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| \|μ*\| | 1.131 | 1.280 | 1.435 | 1.581 | 1.710 | 1.812 | 1.882 | 1.915 | 1.911 | 1.868 | 1.787 | 1.673 | 1.365 | 1.000 |

Bisection gives |μ*| = λ^{1/4} at η ≈ 0.9511 and η ≈ 3.2115 (float, two discretisations). At η = 5 sector 0 has 1.585 > λ^{1/4}, a second regime. Interpretation: along the resonant subsequence the per-step "free energy" 2 log|μ*| exceeds ½ log λ, half the Lyapunov exponent paid by the 1/φ(h_m) dilution. An interval certificate of the window would be BGS-TRACE-191 (open).

## 7. The Line B kick f_B (F7, F8): evidence for BGS-TRACE-196, not a claim

**What carries over.** The 49-state law (TRACE-194) (Lφ)(u, σ) = Σ_n ĝ(n) e(sc(xu + x²/2) + bn/8 + γ(nσ + n²/2)/49) φ((u + x)/λ, λ₇⁻¹(σ + n)), x = n/7, 3 ∤ m, γ = 11 (s = +1) and 38 (s = −1), lifts in the same way: real shifts are allowed in the Lean lemma, and the C⁴⁹ factor rides along.

**Float exploration [N]** (`code/lift49.py`, K0 = 2, K = 14, `logs/lift49_K0_2_K14.log`): leading |μ| = 1.8839 (s = +1, b = 4) and 1.8968 (s = −1, b = 0), matching Line E step 2 from a different discretisation; all other vertex eigenvalues ≤ 1.30, with a cluster at 1.27–1.30 that is **stable under two discretisations [N]** **[RF4]**; edge radius ≈ 0.37. The lifted 49-state trace identity agrees with the Line E referee's exact full-kick class sums at m = 5, 7, 11, 13, both signs, to relative ≤ 5.9e-7 (K = 14, float; `logs/lift49_K0_2_K14.log`).

**Why there is no certificate.** The geometry is the same as for k1 (K0 ≈ 4, K ≈ 55), times 49 states: ≈ 24 000 dimensions per operator, 8 V and 8 E operators, r₂ ≈ 1.4 above the 1.30 cluster, and a trace norm about 49 times larger (expected m0 ≈ 45). Dense ball-arithmetic resolvent bounds at that size were out of reach on the machine used. No exact symmetry reduction of the 49-dimensional factor was found.

**Consequence for BGS-TRACE-196.** It stays **conditional**. Its infinite-alphabet part is reduced by F1 (and the Δ bounds) to a finite, ≈ 24k-dimensional certificate; F7 is float evidence only.

## 8. Mechanism and generality (discussion, F9)

1. *Arithmetic collapse (E1).* At N ≡ −4 (mod h_m) the Gauss-sum phase collapses to the classical action ½nᵀH⁻¹n up to a mod-8 correction; within each m a class of N of density 1/φ(h_m) sees no phase cancellation.
2. *Statistical-mechanics structure.* H⁻¹ has entries ∝ λ^{−|i−j|}, so Z_m is the partition function of a ring of Z-valued spins with single-site weights ĝ(n) and complex exponentially decaying pair couplings — the setting of Ruelle–Mayer transfer operators (Ruelle 1968; Mayer, *The Ruelle–Araki transfer operator in classical statistical mechanics*, LNP 123, 1980). Growth of F_m is the statement 2 log|μ*| > ½ log λ.
3. *The lift.* A holomorphic, one-dimensional, Manning-type inclusion–exclusion (Manning 1971; Bowen) for any IFS of affine maps x ↦ (x + t)/λ with real translations t, and weights with Σ|w(t)|e^{α|t|} < ∞ for α above the multiplier cost (strip-width condition w > c·0.6036, any β > 0).
4. *Other hyperbolic S.* The transfer-operator part depends only on λ and c; the resonance E1 must be re-derived for each S (open).

## 9. Non-claims

- Not a BGS counterexample; nothing about eigenvalue statistics beyond the second moment of Tr U^m over residues. **TRACE-179 (the Line B kick) is not disproved.**
- F2, F3, F5 are computer-assisted: they rely on python-flint/arb, the cited trace formula, Lidskii and Weyl; the far-field and Bessel-tail bounds are analytic and written out in `cert_lift.py`.
- Lean covers only the combinatorial core of F1.
- F6 and F7 are floating-point.
- Novelty: the exact identity at the resonance (E1, E2) is Line E's. New here: the lift with its exact trace identity; an unconditional (computer-assisted), all-m exponential lower bound for F_m for k1 at η = 2 and on the certified η grid; the f7 corollary. No prior rigorous asymptotic result of this type for a fixed nonlinear kick of a quantised cat map is known to the author or the referee; the literature search was not exhaustive.
- Related work: Keating–Mezzadri (2000), pseudo-symmetries (analogy only); Degli Esposti–Winn, J. Phys. A 38 (2005) 5895, N-dependent quantum symmetries of perturbed cat maps (a different mechanism; their Theorem 2 gives s = 1 for this S) **[RFn]**; Faure–Nonnenmacher–De Bièvre and Kurlberg–Rudnick (different regimes); Mauldin–Urbański infinite IFS (maps into a bounded set, not the case here); Jenkinson–Pollicott-style rigorous transfer-operator spectra (method family).

## 10. Reproduce

Paths are relative to `computations/verification/lineF/`. Python with python-flint 0.9.0, numpy, scipy.
```
cd code
python3 spec_float.py; python3 xcheck_class.py; python3 eta_curve.py; python3 eta_thresh.py; python3 lift49.py 2 14 70
./run1.sh; ./run2.sh        # certificates (cert_lift.py); 128-bit arb; 5–30 min per operator at machine load ≈ 27 [RFn]
python3 bounds_lift.py 2 ../logs/certV_eta2_a4_tight.json ../logs/certV_eta2_a{0,2,6}.json ../logs/certE_eta2.json ../logs/bounds_eta2.json
python3 safe_table.py > ../logs/safe_table.md
```
The run scripts set the interpreter in a variable `P`; set it to a Python with python-flint. Lean: `cd formalization && lake exe cache get && lake build Bgs.LineF`.
