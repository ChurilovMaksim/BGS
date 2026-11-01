# Lean batch 3 (1 November 2026)

Branch `lean-batch-3` from `main` at `d87dce0d` (after PR #76). Eight new modules under `formalization/Bgs`, wired into
`formalization/Bgs.lean`; 75 new `theorem`/`lemma` declarations. No `sorry`, no `native_decide`; `#print axioms` for all 75 is
within {propext, Classical.choice, Quot.sound} (`Axioms.lean`, `axioms.log`). No claim state changed. Docstrings of the
batch-2 modules `LineIPhaseSplit`, `LineIAliasing`, `LineJ3PrimeLevel` were updated only to point to the batch-3 closures.

| Claim | Module(s) | Main theorems | Coverage |
|---|---|---|---|
| BGS-TRACE-259 | `LineLLineOrth` | `lemmaA1_parseval`, `lemmaA1_CS`, `mem_ell_iff`, `sum_ell`, `card_ell` | **Partial.** Lemma A1 in the model `O/q = 𝔽_q × 𝔽_q` (q odd split prime, s² = 2, 𝔮 = ker(a + b√2 ↦ a + sb), ℓ(𝔮) = annihilator under e(Tr(βx)/q), defined literally): Σ_{β∈ℓ(𝔮)}\|Ẑ_β\|² = qΣ_u\|A(u+𝔮)\|² and \|D_𝔮\|² ≤ (1 − 1/q)C_𝔮, for A on O/q. Not formalized: the collision form C_𝔮 = 1 + Σ R(v) − \|Z\|²/q (Theorem U). |
| BGS-TRACE-267 | `LineLLineOrth` | `lemmaQ`, `line_orth`, `line_sum`, `norm_dvd_of_mem` | **Partial.** Lemma Q (1/q)Σ_{β∈ℓ(𝔮)}F(β/q) = Σ_{γ∈𝔮}c_γ for absolutely summable c on O = ℤ × ℤ; γ ∈ 𝔮 ⇒ q ∣ Nm γ. Not formalized: Nm γ ≠ 0 for γ ≠ 0, the block-energy use for F = f_k. |
| BGS-TRACE-218 | `LineIMoebius`, `LineISummable` (+ batch-2 `LineIAliasing`) | `Fm_moebius`, `sum_units_moebius`, `sum_moebius_divisors`, `LineISummable.aliasing_mean`, `Zq_mul_conj` | **Partial (gap closures).** Möbius formula F_m = φ(2h)⁻¹Σ_{e∣2h}μ(e)(2h/e)Σ_{pairs}1[(2h/e) ∣ P(n) − P(n′)] (finite support); first identity for Σ\|Φ̂\| < ∞ (pair series). Not formalized: regrouping into Σ_j C_Z(jq); the summable Möbius case. |
| BGS-TRACE-211 | `LineISummable` (+ batch-2 `LineIPhaseSplit`) | `phase_split`, `sigma_mass`, `summable_term`, `norm_e_real` | **Full registered identity.** Prop I1 and total mass 1 now for every kick with Σ\|Φ̂\| < ∞ (real ν₀, integer δ); the halo description is a heuristic and not part of the claim. |
| BGS-TRACE-229 | `LineJ3GaussSquare` (+ batch-2 `LineJ3PrimeLevel`) | `completing_square`, `g_normSq`, `gauss_normSq`, `conj_G_mul_G`, `W_eq`, `two_isSq`, `card_isotropic` | **Partial (gap closures).** With G_t(β) = Σ_γ e(−(t Nm γ + Tr βγ)/q) (BGS-TRACE-212): G_t(β) = e(t̄ Nm β/q)G_t(0), \|G_t(0)\|² = q², conj G_t(0)G_t(β) = q²e(Nm(β)t̄/q), the Gauss-sum weight equals the batch-2 W (values and bound), 2y′² = 1 ⇒ 2 is a square, #{β ≠ 0 : Nm β = 0} = 2(q − 1). Not formalized: the label covering (frozen labels cover 𝔽_q^* minus one t_b), the float checks. |
| BGS-TRACE-216 | `LineIMonomial` | `case_m15p`, `case_m21p`, `case_m27p`, `case_m9n`, `case_m15n`, `case_m21n`, `case_m27n`, `reflection`, `conj9_spec`, `neg9_spec`, `pi_bijective`, `monomial_intertwines`, `X_mul_star`, `matrix_*`, `unitary_*` | **Partial.** Automaton tables of the eight cases (m ∈ {9, 15, 21, 27}, a = ±2) exported from the verifier `sym_v3/monomial_intertw.py` (generator `scripts/gen_monomial_data.py`, which reuses the verifier's `fam`/`search` and reproduces the committed data byte for byte); all witness relations by `decide`; matrix form X A = A′X with X Xᴴ = 1. Not formalized: the table derivation from the G2 operators, the infinite-dimensional consequences, the Galerkin and direct certificates. Boundary: dated Lean note appended. |
| BGS-TRACE-143 | `LineCDFTStar` | `M_eq`, `P_F_eq`, `conj_DFT`, `PDelta_unitary`, `P_mul_star`, `Delta_mul_star` | **Partial.** Theorem 1 matrix identities for odd N: M_N = ΔF_{1/4}Δ, PF_{1/4}P⁻¹ = F, (PΔ)(D_θM_N) = (D_θ′F)(PΔ) with PΔ unitary. Not formalized: the measure-preserving property / eigenvalue law, Remark 1′, the p ≡ 1 mod 4 statement, the numerics. Boundary: dated Lean note appended (supersedes "Not formalized in Lean" for these identities). |
| BGS-FM-026 | `Fm026Counts` | `count_integral`, `special_4375`, `special_109375`, `core_875` | **Partial (bookkeeping only).** 25 ∣ N, 625 ∣ N, 24N/25 = 600N/625; 4200 + 18·7 + 7 = 4333 ≥ 612N/625 + 7 at N = 4375; 105000 + 324·7 + 175 = 107443 ≥ 612N/625 + 175 at N = 109375; 875 = 840 + 35. Not formalized: the multiplicity bound and every splitting certificate. Sealed row: link admitted via its `historical_claim_amendments` row (fields `formalization`, `evidence`); no `formalization_scope` key. |
| BGS-TRACE-178 | `LineBTorsionSplit` | `torsion_split` | **Partial.** F = F_gen + F_tor for the Prop C double sum over norm classes mod h, any pair weight (hence μ(q_rr′)/φ(q_rr′)), F_gen = pairs with r, r′ ≢ 0 mod p. Not formalized: Prop C itself, the numerical values. |

Integration: `scripts/link_batch3.py` (run once): `record/claims.json` links, scopes, receipt and the two boundary notes; the FM-026
amendment row in `record/claim_integration_epochs.json`; the curated inventory mirror. Regenerated: `RESULTS.md`
(`render_results.py`), `record/claim_registry.md` (`render_claim_registry.py`, boundary notes), and
`evidence/executions/20261101/lean_inventory/INVENTORY.md` (`make_inventory.py`, now with a current-status column and current
totals). Hand edits: README/README.ru Lean counts (162 claims, 175 modules, 2347 declarations, 8874 → 8882 jobs),
`formalization/README.md` rows, `CHANGELOG.md`.

Files: `lake_build_Bgs.log` (full `lake build` via `build_lean_verified.sh`, "Build completed successfully (8882 jobs)", exit 0),
`build_wrapper.out`, `Axioms.lean`, `axioms.log`, `checks.log`, `unittests.log`, `scripts/`.
