# Line F: an unconditional asymptotic disproof of the k1-kick analogue of Conjecture R, using full-alphabet resonance transfer operators on lifted Hardy spaces

Working tree: `computations/verification/lineF/` (`code/`, `logs/`, `lean/`, `NOTES.md`). Backup: `<backup-dir>/`.
I did not modify `computations/verification/lineE`, `computations/verification/lineE/referee` or `<integration-clone>`. Nothing was pushed or posted.
Context: PR #57 (Line E, TRACE-183..196). This line addresses **TRACE-188** (E6, the conditional hypothesis H∞) and **TRACE-196** (E14, H∞,7 for the 49-state law).

Status labels:
* **[P]** proved on paper, with cited standard theorems.
* **[CA]** computer-assisted rigorous: arb ball arithmetic via python-flint 0.9.0, with JSON logs.
* **[Lean]** kernel-checked in Lean 4.33.1 + Mathlib, using `lake exe cache get` (no Mathlib build), no `sorry`, no `native_decide`.
* **[N]** numerical.
* **[open]** not done.

## 0. What is new, in one paragraph

Line E proved an exact m-independent transfer-operator law for the resonant residue ν* (N ≡ −4 mod h_m), but only for a kick truncated to |n| ≤ L. The 2.37^m alphabet tail meant that the physical (untruncated) kick was controlled only for finitely many m. The asymptotic statement was conditional on H∞ (TRACE-188).

**Line F removes H∞ for the k1 kick (and, by the auditor's Galois corollary, for the pure 7-mode kick when 3 ∤ m).** The tool is a new lift:
* The untruncated operator, whose letters translate without bound and so cannot act on any single Hardy space of a disc, is replaced by two trace-class operators.
* Each acts on a weighted ℓ²-direct sum of Hardy spaces over a lattice of discs: a "vertex" lattice and an "edge" lattice.
* Their trace difference reproduces the physical trace **exactly, for every m**. This is a holomorphic Manning-type inclusion–exclusion; its combinatorial core is in Lean.

The infinite alphabet then enters only through operator-norm and trace-norm perturbation bounds. These are summable because |J_n| decays superexponentially and the multiplier cost e^{2πc|n|ρ} is only exponential, with ρ ≈ 1 and not ρ ∝ L.

Certified result at η = 2 (k1 kick, full alphabet):
* The sector-4 lifted operator has a simple isolated eigenvalue |μ*| ∈ [1.9154712, 1.9154752], above λ^{1/4} = 1.5538.
* Everything else, in all sectors and in both lattices, has |z| < 1.

Consequence, for **every** odd m ≥ 15: F_m(2)/2m ≥ 6.03 and W̃rest_m(2)/m ≥ 8.07, with F_m/2m ≥ 0.169·(1.5197)^m/m.

So the k1 analogue of Conjecture R fails, unconditionally (computer-assisted) and asymptotically. The same holds at η = 1.25, where Line E could show no violation at all, and at further certified η (§5).

**Not done:** the real Line B 14-mode kick (TRACE-179 itself; TRACE-196). The method applies verbatim and I checked it numerically. The rigorous certificate, however, needs a ~24 000-dimensional ball-arithmetic spectral enclosure, which was beyond this box (§7).

## 1. Results table

| # | Statement | Label |
|---|---|---|
| F1 | **Lifted trace identity.** For every weight sequence w with Σ\|w(n)\|e^{α\|n\|} < ∞ (α > 2πcρ_V + β/λ), every m ≥ 1: Σ_{n∈Z^m} Π_j w(n_j)e(c n_j s_j) = (1−λ^{−m})(Tr L_V^m − Tr L_E^m), with L_V, L_E trace class (§2). Hence Z_m(ν*) = (1−λ^{−m}) Σ_{a∈{0,2,4,6}} c_a (Tr L_{V,a}^m − Tr L_{E,a}^m), \|c_a\| = ½, **full alphabet**. | [P] + [Lean] combinatorial core + [N] checks to 1e-15 / 1e-13 |
| F2 | **Certified spectrum, η = 2, k1, full alphabet.** L_{V,4}: exactly one eigenvalue (algebraic multiplicity 1) in D(b11, 2·10⁻⁶), \|μ*\| ∈ [1.9154712, 1.9154752]; no other spectrum in \|z\| ≥ 1. L_{V,0}, L_{V,2}, L_{V,6} and L_{E,a} (all a): spectrum in \|z\| < 1. Trace norms ‖L_V‖₁ ≤ 730.15, ‖L_E‖₁ ≤ 22.94. | [CA] |
| F3 | **Main theorem.** k1 kick, η = 2. For every odd m ≥ 13: \|Z_m(ν*)\| ≥ ½(1−λ^{−m})(μ_lo^m − 4(T_V+T_E)) > 0. For every odd m ≥ 15: F_m/2m ≥ 6.03 and W̃rest_m/m ≥ 8.07, increasing, ≥ 0.169·1.5197^m/m. The k1 analogue of Conjecture R (W̃rest_m = o(m)) is **false**. This removes H∞ of TRACE-188 for k1. | [CA] |
| F4 | **Pure 7-mode kick f₇ = 0.9cos(2π·7q).** F_m(f₇) = F_m(k1) when 3 ∤ m (auditor's Galois identity, Z_{f₇}(ν) = Z_{k1}(49ν)). So F3 holds verbatim for f₇ for odd m ≥ 15 with 3 ∤ m. | [P] + [CA] |
| F5 | **Other η.** η = 1.25: all sectors and lattices certified. Exponential growth for all odd m ≥ 13, rate (μ²/√λ) ≥ 1.209 per step; F/2m ≥ 2.928 from m = 31 (\|W̃rest\| > m, i.e. violation of the quantitative form, for all odd m ≥ 31, versus none in Line E). Further η: §5 table. | [CA] |
| F6 | **Growth window.** Sector-4 \|μ*(η)\| > λ^{1/4} exactly for η ∈ (0.951, 3.212). Sector 0 crosses again near η ≈ 4.6. | [N] (float, two discretisations) |
| F7 | **Full Line B kick (49-state law, a = 7).** The lifted 49-state operators reproduce the law. Leading \|μ\| = 1.8839 (s=+1, b=4) and 1.8968 (s=−1, b=0); next cluster 1.27–1.30 (real, not a discretisation artefact); edge radius 0.37. | [N] |
| F8 | TRACE-179 itself (Line B kick), i.e. H∞,7 (TRACE-196). | **[open]**: reduced to a finite certificate (§7); not certified |
| F9 | Mechanism and generality (§8). | discussion and [N] |

## 2. The lift and the exact trace identity (F1) [P]

**Setting.**
* c = 1/(λ−λ⁻¹).
* Letters n ∈ Z act by ψ_n(s) = (s+n)/λ.
* The multiplier is e(cns).
* For a periodic word, s_j is the real periodic orbit, s_{j+1} = (s_j+n_j)/λ. These are Line E's s_j, and ½nᵀH⁻¹n = c[Σn_js_j + ½Σn_j²] (E2, TRACE-184).

**Vertex lattice.**
* States c ∈ Z, with discs D(c, ρ_V).
* Letter n sends state c to c′ = f_n(c) := ⌊(c+n)/λ + ½⌋, with δ = (c+n)/λ − c′ ∈ (−½, ½).
* (L_VΦ)_c(s) = Σ_n w(n) e(cns) Φ_{f_n(c)}(ψ_n(s)), s ∈ D(c, ρ_V).
* ψ_n(D̄(c,ρ_V)) ⊂ D(c′,ρ_V) as soon as ½ + ρ_V/λ < ρ_V, i.e. ρ_V > λ/(2(λ−1)) = 0.6036.

**Edge lattice.**
* States are pairs (e, e+1), with discs D(e+½, ρ_E).
* A transition exists only if f_n(e+1) = f_n(e)+1; the target is the edge f_n(e).
* Then \|δ_E\| ≤ 1/(2λ), and the inclusion holds for ρ_E > 1/(2(λ−1)) = 0.1036.

**Space.**
* 𝓗 = {Φ = (Φ_c)}, with ‖Φ‖² = Σ_c ω_c² ‖Φ_c‖²_{H²(D_c)}.
* Weights: ω_c = 1 on the core (\|c\| ≤ R_c) and ω_c = e^{−β(\|c\|−R_c)} outside.
* Each H²(D_c) has orthonormal basis ((s−c)/ρ)^i.

**Trace class.** Write W_n = \|w(n)\|, M_n = e^{2πc\|n\|ρ} (the supremum of the multiplier on any disc), and θ = \|δ\|/ρ + 1/λ < 1.
* A block Φ_{c′} ↦ w e(cn·)Φ_{c′}∘ψ_n has ‖·‖ ≤ W_nM_n(1−θ²)^{−1/2} and ‖·‖₁ ≤ W_nM_n/(1−θ). This uses the rank-one expansion Σ_i⟨·,e_i⟩ p·(e_i∘ψ) and ‖e_i∘ψ‖ ≤ θ^i.
* As an operator on 𝓗 the block is multiplied by ω_c/ω_{c′}.
* For \|c\| > R_c: \|c′\| ≤ (\|c\|+\|n\|)/λ + ½, so ω_c/ω_{c′} ≤ e^{−β(\|c\|−R_c)} + e^{−β\|c\|(1−1/λ)+β/2}e^{β\|n\|/λ}.
* Summing over all c ∈ Z and n ∈ Z converges. So L_V and L_E are trace class on Hilbert spaces, and Lidskii's and Weyl's theorems apply.

**Chains and the Ruelle trace formula.**
* The block (c₀,c₀) of L^m is the absolutely convergent (in trace norm) sum over closed chains c₀ → c₁ → … → c_m = c₀ of single weighted composition operators M_{p_w}C_{ψ_w} on H²(D(c₀,ρ)).
* ψ_w maps D̄(c₀,ρ) into D(c₀,ρ), because the inclusions compose.
* By the Ruelle / Bandtlow–Jenkinson trace formula, Tr(M_pC_ψ) = p(s*)/(1−ψ′(s*)). Here s* is the unique fixed point, which is the real periodic orbit point, and ψ′ = λ^{−m}. (Proof sketch: the kernel representation gives Tr = (2πi)⁻¹∮p(ζ)/(ζ−ψ(ζ))dζ; ζ−ψ(ζ) has a single simple zero in the disc; take the residue.)
* Off-diagonal blocks contribute nothing to the trace.
* Hence Tr L_V^m = Σ_{w∈Z^m} N_V(w)·p_w(s*_w)/(1−λ^{−m}), where N_V(w) is the number of closed vertex chains. Likewise for E with N_E(w).

**Combinatorial lemma [Lean] (`lean/LineF.lean`, `LineF.vertex_minus_edge`, `LineF.edge_closed_iff`).** For each word, let F = f_{n_{m−1}}∘…∘f_{n_0}.
* F has increments in {0,1} (`step_round`, `comp_step`).
* F(k)−k → ∓∞ as k → ±∞ (`round_below/above`, `evBelow_comp'`…).
* So Fix F is a nonempty finite integer interval [a,b].
* A closed edge chain at e is the same thing as e, e+1 ∈ Fix F (`edge_closed_iff`, via `edgeOK_iff`).
* Hence N_V − N_E = (b−a+1) − (b−a) = 1 (`count_identity`, `fix_outside`).

The Lean statement allows real shifts (`roundMap μ x`), so it also covers the 49-state law (x = n/7). `#print axioms`: propext, Classical.choice, Quot.sound. Log: `logs/lean_LineF.out`.

Therefore Σ_{w∈Z^m} p_w(s*_w) = (1−λ^{−m})(Tr L_V^m − Tr L_E^m). This is exact for every m and for the full alphabet. Combined with E1 and E2 (TRACE-183/184), whose algebra holds termwise for every n ∈ Z^m, this gives F1. ∎

**Numerical checks of F1.**
* Brute-force finite-alphabet sums (L = 3, m = 1..5) vs Tr L_V^m − Tr L_E^m: relative 1e-15 (`logs/spec_float.log`).
* Against the referee's **exact full-alphabet class sums** \|Z_m(ν*)\|² (independent code, `computations/verification/lineE/referee/logs/classes.jsonl`), m = 5..15: relative error ≤ 9.0e-14 (`code/xcheck_class.py`, `logs/xcheck_class.log`). Line E's truncated H²(D_ρ) law reached about 1e-8.
* Ghost eigenvalues: 0.3624 and 0.2659 appear in both L_V and L_E and cancel in the trace difference, as the lemma predicts.

## 3. The certificate (F2) [CA]

`code/cert_lift.py typ η K0 ρ K β prec p r1 r2 Nmax Rmax sectors out`, arb at 128 bits.

**Splitting of the operator.** L = A + X + Δ, where:
* **A** consists of the core←core blocks. The core is \|c\| ≤ K0 = 4: 9 vertex discs, 8 edge discs.
* **X** consists of the far←core blocks (core input, far output). Its norm is bounded by row sums: ‖X‖ ≤ 6.16 (V) and 0.32 (E).
* **Δ** contains everything else: big letters into core rows, far←far blocks, all rows \|c\| > Rmax = 40 (bounded analytically with geometric series), and every letter \|n\| > Nmax = 60 (Bessel tail \|J_n(x)\| ≤ (x/2)^n/n!). Bounds: ‖Δ‖ ≤ 1.86e-9 (V) and 7.5e-14 (E).

**Galerkin step.** A is truncated to degree K per disc: K = 55, ρ_V = 1.2, so 495 dimensions; K = 40, ρ_E = 0.8, so 320 dimensions. The section P(MC)P = (PMP)(PCP) is exact because the multiplier matrix is lower triangular and the composition matrix upper triangular. The truncation error δ = δ₁ (column tails) + δ₂ (Cauchy estimate on the doubled disc) is 4.5e-11 (V) and 1.2e-10 (E).

**Comparison operator.** T₀′ = [[H T₀ H ⊕ 0, 0], [X, 0]] is block lower triangular, so spec T₀′ = spec T₀ ∪ {0}. Its resolvent satisfies
  ‖R‖ ≤ (‖R_{T₀}‖ + 1/\|z\|)(1 + ‖X‖/\|z\|) + 1/\|z\|.
* Sector 4: T₀ is the Householder deflation [[b11, b12], [0, Y]], with b21 ≤ 1.1e-25 moved into the perturbation.
* Other sectors: T₀ is the Galerkin matrix itself.
* ‖R_Y‖ and ‖R_A‖ come from Neumann series bounds with ‖Y^j‖_F, j ≤ 40, valid for all \|z\| ≥ r. No sampling of z is needed.

**Conclusion.** If (δ + ‖Δ‖ + b21)·sup_Γ‖R‖ < 1 on the contours, then for all t ∈ [0,1] the Riesz projections of T₀′ + t(L − T₀′) have constant rank. This gives the same eigenvalue counts as T₀′.

| run | η | F·R on circle 1 | F·R on \|z\| = r₂ = 1 | result |
|---|---|---|---|---|
| V a=4 (r₁ = 2e-6) | 2 | 0.243 | 6.1e-6 | simple μ*, \|μ*\| ∈ [1.9154712, 1.9154752] |
| V a=0 / 2 / 6 | 2 | — | 7.0e-7 / 1.4e-6 / 1.4e-6 | spectrum \|z\| < 1 (Y-root 0.62 / 0.93 / 0.93) |
| E a=0,2,4,6 | 2 | — | 1.0e-9 | spectrum \|z\| < 1 |
| V a=4 (r₁ = 1e-3) | 1.25 | 3.4e-8 | 2.4e-10 | \|μ*\| ∈ [1.708750, 1.710751] |
| V a=0,2,6; E all | 1.25 | — | ≤ 1e-10 | \|z\| < 1 |

Logs: `logs/certV_eta2_a{0,2,4,6}.json`, `certV_eta2_a4_tight.json`, `certE_eta2.json`, `certV_eta1.25_*`, `certE_eta1.25.json`.


**Negative controls** (each must fail):
* K = 25 (Galerkin too coarse), sector 4, η = 2: δ₂ = 0.045, F·R₁ = 1.15e4, F·R₂ = 145. **Not certified**, as expected (`logs/neg_K25_a4.json`).
* r₂ = 0.85 for sector 2, η = 2 (spectral radius 0.877 > 0.85): **not certified, as predicted** (the Neumann/Frobenius root bound for the comparison operator is 0.932 > r₂, so the annulus test fails and no enclosure is output) (`logs/neg_r2_085_a2.out`).
* Earlier stress test with K0 = 3: ‖Δ‖ = 1.8e-5, and with K = 20 the sector-4 certificate failed (F·R₁ = 5.9e5) (`logs/test_V.json`). Truncating the far field too aggressively is detected.

**Consistency.**
* Float eigenvalue of the full operator: 1.9154733, inside the certified interval.
* Line E's truncated L = 6 enclosure is [1.9154751, 1.9154771], which is disjoint from ours. This is expected: truncation shifts μ by about 3e-6.

**Bug caught before any result was used.** The first draft skipped Galerkin entries with `Mx[i,j] != 0`. For arb balls that test means "certainly nonzero", so balls containing 0 would have been dropped. It was replaced by C-level block aggregation with no skipping, before any certificate run that I use.

## 4. Main theorem (F3) [CA]

By F1, Lidskii, and Weyl (Σ_{k≠*}\|μ_k\|^m ≤ r₂^{m−1}‖L‖₁ for \|μ_k\| ≤ r₂):
  \|Z_m(ν*)\| ≥ ½(1−λ^{−m})(μ_lo^m − r₂^{m−1}·4(T_V+T_E)),  with μ_lo = 1.9154712, r₂ = 1, 4(T_V+T_E) ≤ 3012.4.

This is positive for every odd m ≥ 13. Then:
* F_m ≥ \|Z_m(ν*)\|²/φ(h_m), since all terms are nonnegative.
* φ(h_m) ≤ h_m − 1, using exact integers h_m.
* W̃rest_m ≥ F_m − 4m (TRACE-165 B^sym ≤ 2m; \|χ_m\| ≤ 1, TRACE-170).

From `code/bounds_lift.py` (`logs/bounds_eta2.json`; rows for every odd m ≤ 199):

| m | 15 | 17 | 19 | 21 | 25 | 31 | 41 | 61 | 101 |
|---|---|---|---|---|---|---|---|---|---|
| F_m/2m ≥ | 6.03 | 16.4 | 36.4 | 77.6 | 350 | 3.48e3 | 1.73e5 | 5.0e8 | 5.7e15 |
| W̃rest_m/m ≥ | 8.07 | 28.8 | 68.9 | 151 | 696 | 6.96e3 | 3.46e5 | 1.0e9 | 1.1e16 |

**All m.** Using 2(h_m−1) < λ^{m/2} and (1 − 3012.4/μ_lo^m)² ≥ 0.679 for m ≥ 15:
  F_m/2m ≥ 0.169·(μ_lo²/√λ)^m/m,  with μ_lo²/√λ = 1.5197.

This lower bound increases in m, so it holds for **all** odd m ≥ 15 and tends to ∞.

**Sanity check against exact values.** The bounds are below the exact values: m = 13: F/2m is 11.20 exact versus a bound of 0.56; m = 15: 27.89 exact versus 6.03.

**Scope.**
* This disproves, unconditionally (computer-assisted), the k1-kick analogue of Conjecture R at η = 2, and at η = 1.25 as well.
* It removes TRACE-188's hypothesis H∞ for k1, in the lifted form. Our operator is not literally the "weighted H^∞ on D_ρ ∪ strip" of the original proposal. It is a different, explicit space that makes the conclusion of H∞ (isolated simple \|μ\| > λ^{1/4} and the trace formula) true.
* It is **not** a statement about the Line B kick, and not a BGS counterexample (§9).

## 5. η grid (F5) [CA]

The same pipeline is used: K0 = 4, r₂ = 1 for η ≤ 1.75; K0 = 5, r₂ = 1.45 for η ≥ 2.25. Results are in `logs/certV_eta*`, `certE_eta*`, `bounds_eta*.json`.

| η | K0, r₂ | \|μ*\| certified ∈ | T_V, T_E | μ²/√λ | first odd m with Z>0 | F/2m at m=15 / 21 / 31 | first m with F/2m ≥ 2.5 (all larger m) |
|---|---|---|---|---|---|---|---|
| 1.25 | 4, 1.00 | [1.708751, 1.710751] | 215.3, 12.39 | 1.2094 | 13 | 0.144 / 0.63 / 2.93 | 31 |
| 1.5 | 4, 1.00 | [1.810900, 1.812900] | 324.8, 15.23 | 1.3584 | 13 | 1.1 / 7.32 / 107 | 19 |
| 1.75 | 4, 1.00 | [1.880799, 1.882799] | 487.7, 18.67 | 1.4652 | 13 | 3.66 / 36 / 1.12e+03 | 15 |
| 2 | 4, 1.00 | [1.915471, 1.915475] | 730.1, 22.93 | 1.5198 | 13 | 6.03 / 77.6 / 3.48e+03 | 15 |
| 2.25 | 5, 1.45 | [1.909830, 1.911830] | 1336.5, 37.59 | 1.5108 | 31 | — / — / 193 | 31 |
| 2.5 | 5, 1.45 | [1.866602, 1.868602] (V sector 4 certified) | — | — | pending | pending | pending (E sector 6) |
| 2.75 | — | not finished | | | | | |
| 3.0 | — | not finished | | | | | |

All rows with numbers are fully certified: every sector of both lattices. The lower bound on F/2m is increasing in m, so "first m with F/2m ≥ 2.5" means the bound holds for all larger odd m. At η = 1.25, 1.5 and 1.75 this gives |W̃rest_m| > m (since W̃rest/m ≥ 2·F/2m − 4) for all odd m from that point on; Line E showed no violation at η = 1.25 at all. η = 2.5 is **partial**. Certified: the V-lattice sector-4 enclosure |μ*| ∈ [1.866602, 1.868602] (F·R1 = 2.9e-3), V sectors 0, 2, 6 below r₂, and E sectors 4, 0, 2. E sector 6 is **pending**. They are in the detached job `cert_lift.py E 2.5 …` (pid 552224), whose output goes to `logs/certE_eta2.5.out` / `logs/certE_eta2.5.json`. After it finishes, run `code/bounds_lift.py 2.5 …` and then `code/grid_table.py` to complete the row. Until then, no all-m statement is claimed for η = 2.5. η = 2.75 and 3.0 were not run: I stopped them because of box load. They need K0 = 5 and r₂ = 1.45, the same as η = 2.25.

## 6. Growth window (F6) [N]

Float spectra of the lifted operators (`logs/eta_curve.log`, `eta_thresh.log`) give the sector-4 leading \|μ*\|:

| η | 0.25 | 0.5 | 0.75 | 1.0 | 1.25 | 1.5 | 1.75 | 2.0 | 2.25 | 2.5 | 2.75 | 3.0 | 3.5 | 4.0 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| \|μ*\| | 1.131 | 1.280 | 1.435 | 1.581 | 1.710 | 1.812 | 1.882 | 1.915 | 1.911 | 1.868 | 1.787 | 1.673 | 1.365 | 1.000 |

Bisection puts \|μ*\| = λ^{1/4} at η = 0.9511 and η = 3.2115. At η = 5, sector 0 has 1.585 > λ^{1/4}, a second regime.

Interpretation: along the resonant subsequence, the per-step "free energy" 2log\|μ*\| exceeds ½log λ, which is half the Lyapunov exponent paid by the 1/φ(h_m) dilution. Exponential failure of the k1-R therefore holds for η ∈ (0.951, 3.212) at the float level. It is certified on the grid of §5.

## 7. The real Line B kick (F7, F8): what is and is not done

**What carries over.**
* The 49-state law (TRACE-195, step 2 of Line E): (Lφ)(u,σ) = Σ_n ĝ(n) e(sc(xu + x²/2) + bn/8 + γ(nσ + n²/2)/49) φ((u+x)/λ, λ₇⁻¹(σ+n)), with x = n/7, 3 ∤ m, γ = 11 (s = +1) and 38 (s = −1).
* γ does not depend on m: checked for m = 5..31.
* It lifts in the same way: real shifts x in the Lean lemma; the C⁴⁹ factor rides along; the trace over C⁴⁹ is the phase at the unique σ-fixed point when 3 ∤ m.

**Float exploration** (`code/lift49.py`, K0 = 2, K = 14, `logs/lift49_K0_2_K14.log`):
* s=+1, b=4: 1.883926. This matches Line E step 2's 1.884, from a different discretisation.
* s=−1, b=0: 1.896835.
* All other V eigenvalues are ≤ 1.30; there is a dense cluster at 1.27–1.30, present in both discretisations.
* E radius ≈ 0.367.

**Exact check of the lifted 49-state trace identity.** I compared (1−λ^{−m})Σ_b c_b(Tr V_b^m − Tr E_b^m) with the referee's exact full-alphabet class sums for the Line B kick (`computations/verification/lineE/referee/logs/T_full_*.npy`). This is coarse (K = 14), float only.

| m | 5 | 5 | 7 | 7 | 11 | 11 | 13 | 13 |
|---|---|---|---|---|---|---|---|---|
| s | +1 | −1 | +1 | −1 | +1 | −1 | +1 | −1 |
| \|Z\|² exact | 133.337 | 188.708 | 1929.45 | 1772.74 | 290544.6 | 309515.8 | 3628100.5 | 4203360.9 |
| relative difference | 5.9e-7 | 3.3e-9 | 4.3e-8 | 1.2e-7 | 1.2e-7 | 6.1e-9 | 1.2e-7 | 2.5e-8 |

So the lifted identity also holds for the real Line B kick, numerically (the 49-state version of F1).

**Why there is no certificate.**
* The full kick's ĝ(n), as a function of x = n/7, decays like k1's. That means the same geometry: K0 ≈ 4 and K ≈ 55. Times 49 states, that is ≈ 24 000 dimensions per operator, for 8 V and 8 E operators.
* r₂ must be about 1.4 (above the 1.30 cluster), and the trace norm grows by the C⁴⁹ factor (≈ 49×). The expected m0 is about 45.
* Dense ball-arithmetic power or resolvent bounds at 24k dimensions are out of reach on this box: 8 cores, load 20–35 from other jobs.
* I did not find an exact symmetry reduction of the 49-dimensional factor. Mod 7, σ₀ ↦ 4σ₀ decouples for the 7k letters, but the satellite letters 7k±1 (weights about 0.06) mix the classes.
* **So H∞,7 (TRACE-196) remains open.** The infinite-alphabet part of it is solved by F1 and the Δ bounds. What remains is a purely finite-dimensional (large) verification, which could be run on a bigger machine with the same `cert_lift.py` logic plus the 49-state tensor factor.

## 8. Why the mechanism is principled, and how general it is

1. **Arithmetic collapse (E1).** At N ≡ −4 (mod h_m), the Gauss-sum phase of Tr U_N^m collapses to the classical action form ½nᵀH⁻¹n, up to a mod-8 correction and the factor (1 + 4/N). The quantum trace at this residue class is a *classical* partition function, with no quantum phase randomisation. The Pell identities (x_d ≡ (−1)^d mod 4, y_d ≡ d mod 2, h² + 1 = 2y′², h_{m−2}y_{(m−1)/2} ≡ 1 mod h_m) make this exact. This is a systematic, explicit obstruction to derandomisation: within each m, a thin class of N (density 1/φ(h_m)) sees no phase cancellation at all.
2. **Statistical-mechanics structure.** H⁻¹ is the Green function of the hyperbolic linear map, with entries ∝ λ^{−\|i−j\|}. So Z_m is the partition function of a 1D ring of Z-valued spins, with single-site weights ĝ(n) and complex exponentially decaying pair couplings c n_i n_j λ^{−\|i−j\|}. This is exactly the setting of the Ruelle / Mayer transfer operator for lattice gases with exponential interactions (Ruelle 1968; Mayer 1980). Growth of F_m is the statement that the "free energy" 2log\|μ*\| beats ½log λ.
3. **The lift.** Unbounded spins break the usual single-disc Hardy-space setting. The vertex/edge lift is a holomorphic, 1-D, Manning-type inclusion–exclusion (Manning 1971; Bowen). It works for any IFS of affine maps x ↦ (x+t)/λ with arbitrary real translations t, and weights with Σ\|w(t)\|e^{α\|t\|} < ∞ for α above the multiplier cost.
4. **Generality.**
   * *Kicks:* any kick analytic in a strip of width > (2πc·0.6036 + ε)/(2π) qualifies for F1. For trigonometric-polynomial kicks e^{iηf}, which are entire, there is no restriction.
   * *Other hyperbolic S:* the transfer-operator part depends only on λ and c = 1/(λ−λ⁻¹). The resonance E1 must be re-derived for each S (its Pell structure). I did not do this for other S: it is open.
   * *Coupling:* whether \|μ*\| > λ^{1/4} is a quantitative, η-dependent question. For k1 it holds on η ∈ (0.951, 3.212) (F6).

## 9. Non-claims and honesty notes

* Not a BGS counterexample. Nothing is claimed about eigenvalue statistics beyond the second moment of Tr U^m over residues. TRACE-179 (the Line B kick) is **not** disproved.
* F2, F3 and F5 are computer-assisted. They rely on python-flint/arb correctness and on the cited trace formula (Ruelle 1976; Bandtlow–Jenkinson 2008), Lidskii, and Weyl. The far-field and Bessel-tail bounds are analytic and are written out in `cert_lift.py`, with comments.
* Lean covers only the combinatorial core of F1. The analytic parts (trace class, trace formula) and the certificates are not formalised.
* Novelty: the exact identity for the resonance (E1, E2) is Line E's. The new contributions are:
  - the lift with its exact trace identity;
  - the first **unconditional, all-m** exponential lower bound for F_m (k1 at η = 2 and 1.25, plus the η grid of §5) and the f₇ corollary;
  - the growth window (float).
  
  I know of no prior rigorous asymptotic result of this type for a fixed nonlinear kick of a quantised cat map, but I have not done an exhaustive literature search.
* Related work: Keating–Mezzadri (2000) concerns arithmetic deviations from RMT (an analogy only; see audit F4). Faure–Nonnenmacher–De Bièvre and Kurlberg–Rudnick have different regimes and mechanisms. Mauldin–Urbański infinite IFS require maps into a bounded set, which does not hold here. Jenkinson–Pollicott-style rigorous transfer-operator spectra are a related method family.

## 10. Reproduce

```
P=python3   # python-flint 0.9.0, numpy 2.5.4, scipy 1.18.1
cd computations/verification/lineF/code
$P spec_float.py ; $P xcheck_class.py ; $P eta_curve.py ; $P eta_thresh.py ; $P lift49.py 2 14 70
./run1.sh ; ./run2.sh          # certificates (cert_lift.py), detached; ~5–30 min per operator
$P bounds_lift.py 2.0 ../logs/certV_eta2_a4_tight.json ../logs/certV_eta2_a{0,2,6}.json ../logs/certE_eta2.json ../logs/bounds_eta2.json
cd formalization && lake exe cache get && lake env lean formalization/Bgs/LineF.lean
```
