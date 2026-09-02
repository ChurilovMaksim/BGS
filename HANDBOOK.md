# HANDBOOK — The BGS Programme Mathematical Reference

This is the guide to what is proven, where each result lives, and how
to verify it.  For the full derivations see THEORY.md (§0–§19.36).

## §1 The three spectral regimes

| System | Characters | Spectrum | Status |
|---|---|---|---|
| Full character group | m = N−1 | arcsine | PROVEN (Thm 91.5) |
| Parity-odd coset | m₊ = (N−1)/(2K) | GOE (Wigner-Dyson) | NUM (3 designs) |
| Single orbit | m = 1 | point mass | trivial |

The transition from arcsine to Wigner is the desymmetrisation
mechanism: the full group contains both parity sectors whose
superposition gives classical (arcsine) statistics; the parity-odd
projection isolates the quantum-chaotic sector.

## §2 The theorems of rank 1 (cat map)

### Theorems A–E: the symmetry foundation
- Thm A: Gaussian observable ⇒ exact √N·GUE_m; time-reversal ⇒ √(N/2)·GOE_m
- Thm B: subgroup Kloosterman moments exactly p²P(s,k) balanced
- Thm C: Θ² = +1 unconditional (no GSE)
- Thm D: parity dichotomy (block-diagonal off the degenerate locus)
- Thm E: Hecke torus antiunitary ⇒ β = 1 off the degenerate locus

### Theorems F–H: the moment route
- Lemma F: Tr(T(v)U^J) = Tr(U^J)·w^{Q_J(v)} (quadratic phase)
- Thm G: moment route closed — l1/l2 ≍ √K
- Thm H: cyclic shape decomposition D_r(N) = pairings + shapes + M_r

### Theorems I–II: the one-parameter curve
- Thm I: observable V_n depends on n only through Q(n) = n₁²−n₁n₂−n₂²
- Thm II: matrix elements = twisted Jacobi sums J(χ,ψ;q)

### Theorems 91–96: the fluctuation chain
- Thm 91.2: full-group moments = binom(2s,s)(N−2) + c_s (arcsine)
- Thm 92.1: k=2 layer = exact combinatorics (|P| = (K−1)(K−2))
- Thm 92.3: uniform even-k factorization A_{2s} = m²·Σ_{2s}
- Thm 95.1: twist identity B(t) = (1/m²)Σ(A⋆A)(t)
- Thm 95.2: flatness c(d) = N−2 + O(1)
- Thm 96.2 / M1: Möbius-fiber bound |δ| ≤ 16/K² = o(1)  ← THEOREM

## §3 The theorems of rank 2 (Sp₄)

- Thm 105.1: Sp₄ diagonal = phase-free dilation, exact covariance
- Thm 105.2: coupled energy F(n) flat off-diagonal (~1.7%)
- Thm 105.3: rank-2 diagonal identity sum_χ |⟨χ|U_D T(n)|χ⟩|² = 1
- Thm 105.6: rank-2 coset flatness A_S = |coset|/G exact
- Thm 105.7: coset-sector theorem (position-only, exact)
- Thm 107.1: rank-2 Weil constant std ~ 0.88√N

## §4 The G0 hypothesis (the general mechanism)

For any kernel whose difference fibers are rational-function orbits
of bounded degree D over an abelian group:

    E_c = E_flat/m⁴ · (1 + δ),  δ = δ_explicit + δ_remainder

The cat map is the D = 4 rank-1 case.  The Sp₄ diagonal is the first
rank-2 confirmation (flatness exact, no Weil correction needed for
the diagonal case; the genuine mixed-sector test is the next step).
R108 correction: the earlier o(1) bound is retracted (see
docs/REVIEW_R108.md, docs/CROSS_TERM_LAW_R108.md) — δ_explicit is the
closed-form diagonal-key artifact, δ_remainder is measured ≤ 0.3% for
K ≥ 40 and is the open analytic estimate.

## §5 How to verify

1. Lean certificates: `cd formal && lake build`
   - K2Reduction.lean: |P| = (K−1)(K−2), parametrisation bijection
   - K4Variety.lean: |V₄| = 423879, pair-key injectivity
   - ScaleLaw.lean: c² = t²−4
2. Python verification: `python code/verification/baseline_r82.py`
3. GOE spacing: `python code/verification/goe_spacing_test.py`
4. Number variance: `python code/verification/number_variance_goe_control.py`

## §6 The remaining open steps

1. Cross-term remainder estimate: |Rem| ≤ E_unc/m⁴ · O(K^{−3/2})
   (measured from K ≈ 40 upward; the explicit diagonal term has closed
   form — derive and verify at all 16 sweep designs)
2. M3: ESY deterministic assembly (conditional on 1; the rel₄ ≈ 2.2/m
   calibration is measured exactly)
3. M4d: non-diagonal Sp₄ Hecke operator (Bruhat assembly)
4. k ≥ 6 layers: template generalises, computational work
5. General BGS: NOT claimed — family-specific verification required
