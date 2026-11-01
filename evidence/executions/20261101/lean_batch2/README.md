# Lean batch 2 (1 November 2026)

Branch `lean-batch-2` from `main` at `6dbcc7a0` (after PR #75). Five new modules under `formalization/Bgs`, wired into
`formalization/Bgs.lean`; 31 new `theorem`/`lemma` declarations. No `sorry`, no `native_decide`; `#print axioms` for all 31
declarations is within {propext, Classical.choice, Quot.sound} (`Axioms.lean`, `axioms.log`). No claim state changed.

| Claim | Module | Main theorems | Coverage |
|---|---|---|---|
| BGS-TRACE-297 | `LineN4GaugeTwist.lean` (+ batch-1 `LineN4Gauge.lean`) | `twist_step`, `twist_product`, `endpoints`, `twist_product_up_to_scalar`, `T_cancel`, `G_cancel`, `T_cancel'`, `G_cancel'` | **Partial (algebraic content complete).** Both gauge identities, the commutation N4-F1 and now the geometric-twist corollary Π_{i<n} L_{τ_i} = T_{−λσ_{n−1}} G_{−bλ^{1−n}} L_{t₀}^n G_{λb} T_{σ_0} (τ_i = t₀ + aλ^i + bλ^{−i}, σ_i = −aλ^{i−1}/κ, ν_i = bλ^{1−i}), by induction from the gauge lemmas, for arbitrary weights, complex a, b, t₀, κ ≠ 0, λ ≠ 0 and all functions ℂ → ℂ (tsum form). With this composition order the scalar is exactly 1 (so unimodular); the e(νσ) factor appears only after reordering T and G. Not formalized: the disc-space (small-gauge) reading. |
| BGS-TRACE-211 | `LineIPhaseSplit.lean` | `phase_split`, `sigma_mass`, `e_shift`, `e_intCast` | **Partial.** Prop I1 Z(ν₀ + δ) = Z(ν₀)σ̂(δ) for every integer δ and total mass 1, any modulus M = 2h ≥ 1, any integer phases P(n), any complex ν₀ with Z(ν₀) ≠ 0 — for a *finitely supported* kick. Not formalized: the absolutely summable (infinitely supported k1) kick; the halo heuristic (not claimed). |
| BGS-TRACE-218 | `LineIAliasing.lean` | `aliasing_mean`, `geom_root_sum`, `Z_mul_conj`, `e_ne_one`, `e_nat_mul`, `conj_e_real` | **Partial.** First identity (1/q)Σ_{ν mod q}\|Z(ν/q)\|² = Σ_{n,n′}Φ̂(n)conj Φ̂(n′)1[q ∣ P(n) − P(n′)] for every q ≥ 1, finitely supported kick; the right side is Σ_j C_Z(jq) regrouped by j (regrouping stated in the module header, not as a Lean series). Not formalized: the Möbius formula for F_m; the absolutely summable case. |
| BGS-TRACE-229 | `LineJ3PrimeLevel.lean` | `sum_inv_all`, `sum_inv_units`, `W_nonisotropic`, `W_nonisotropic_norm`, `W_isotropic`, `Wfull_nonisotropic`, `Wfull_isotropic`, `card_units_erase`, `psi_ne_one`, `psi_norm` | **Partial.** The complete character sum over F_q (q prime) after completing the square: W = q⁻²Σ_{t∈F_q^*, t≠t_b} e(Nt̄/q) = q⁻²(−1 − e(Nt̄_b/q)), \|W\| ≤ 2/q² (N ≠ 0); (q − 2)/q² (N = 0); without a missing label −1/q² resp. (q − 1)/q². Not formalized: conj G_t(0)G_t(β) = q²e(N(β)t̄/q), the label covering (F_q^* minus exactly one t_b), the count 2(q − 1) of isotropic β, the float checks. |
| BGS-RES-023 | `ResonanceMarginConst.lean` | `B_bit_length`, `B_le_two_pow_714`, `nd10_of_margin` | **Partial (final arithmetic step).** The deposited integer B (verbatim from `resonance_nondegeneracy_margin.json`) has 712 binary digits (2^711 ≤ B < 2^712), B ≤ 2^714, and Γ ≥ (π²/41472)2^{−2B}X (X ≥ 0) implies the printed (ND.10) Γ ≥ (π²/41472)2^{−2^715}X. Not formalized: the radius-eight certificate replay (5,704 deductions) and the compilation of B. |

Integration: `scripts/link_batch2.py` (run once) sets `formalization`, `formalization_scope` and appends this receipt to
`evidence` in `record/claims.json`, and mirrors the rows into the curated `record/claim_verification_inventory.json`
(receipt counts, `lean_formalization` tag, `source_blob_sha`, caveat). None of the five claims is a sealed wave-2 row, so
`record/claim_integration_epochs.json` is unchanged. `RESULTS.md` regenerated with `render_results.py`; README/README.ru Lean
counts (156 claims, 167 modules, 2272 declarations, 8874 jobs), `formalization/README.md` rows and `CHANGELOG.md` edited by hand.

Not attempted in this batch (time-box): TRACE-259, 267, 263, 143 (class b) and TRACE-273, 317, 178, FM-026, 216 (class a); see the PR
for the recommended batch 3.

Files: `lake_build_Bgs.log` (full `lake build` via `computations/maintenance/build_lean_verified.sh`, "Build completed
successfully (8874 jobs)", exit 0), `build_wrapper.out`, `Axioms.lean`, `axioms.log`, `checks.log`, `unittests.log`.
