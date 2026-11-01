# Lean batch 4 (1 November 2026)

Branch `lean-batch-4` from `main` at `bffff98c` (after PR #77). Seven new modules under `formalization/Bgs`, wired into
`formalization/Bgs.lean`; 39 new `theorem`/`lemma` declarations. No `sorry`, no `native_decide`; `#print axioms` for all 39 is
within {propext, Classical.choice, Quot.sound} (`Axioms.lean`, `axioms.log`). No claim state changed; no boundary changed (none
of the batch-4 boundaries says "not formalised"); no sealed wave-2 row is involved.

| Claim | Module(s) | Main theorems | Coverage |
|---|---|---|---|
| BGS-TRACE-204 | `LineGDilution` | `square_identity`, `completing_square`, `dilution`, `sum_neg_invariant` | **Partial.** On O/d = ℤ/d × ℤ/d for every modulus d (prime or composite), t a unit: t Nm γ + Tr βγ = t Nm(γ + t̄ conj β) − t̄ Nm β, G_t(β) = e(t̄ Nm β/d) G_d(t), and d⁻²Σ_β Ẑ(β)G_t(β) = (G_d(t)/d²)Σ_β e(t̄ Nm β/d)Ẑ(β) for any Ẑ. Prop I2′ (BGS-TRACE-212) is the input; \|G_d(t)\| = d only at primes (`LineJ3GaussSquare`); brute-force checks not formalized. |
| BGS-TRACE-293 | `LineN3SignConj` (+ batch-2 `LineJ3PrimeLevel`) | `nu0_neg`, `label_neg`, `W_neg_label`, `W_sign_conj`, `isotropic_equal` | **Partial.** Prime levels: ν₀(−ρ) = −ν₀(ρ), t_b(−ρ) = −t_b(ρ), W(N, −t_b) = conj W(N, t_b) for every N, equal isotropic weights. Not formalized: composite levels via inheritance (TRACE-228), the comparison with TRACE-221(ii), the label covering. |
| BGS-TRACE-267 | `LineL3Quadrature` (+ batch-3 `LineLLineOrth`) | `nm_eq_zero_iff`, `q_le_abs_nm`, `lemmaQ_c0` | **Partial (closure).** Nm γ = a² − 2b² ≠ 0 for γ ≠ 0 (irrationality of √2), so \|Nm γ\| ≥ q on 𝔮∖0, and the line average is exactly c₀ when F has no frequency γ ≠ 0 with \|Nm γ\| ≥ q. Not formalized: the block-energy band for F = f_k. |
| BGS-TRACE-254 | `LineLCollisionForm` | `collision_form`, `collision_split`, `theoremU_consequence`, `orth`, `parseval_level`, `theoremU_level` | **Partial.** Finite support s ⊇ supp w, any additive f: Σ_u\|A(u)\|² = Σ_{v∈s−s, f v = 0} R(v); vanishing of R at all collisions v ≠ 0 gives Σ\|A\|² = Σ\|w\|²; Parseval on (ℤ/h)² for odd h; hence Σ_x\|A(x)\|² = 1 and Σ_β\|Ẑ_β\|² = h². Theorem U itself (Lemma U1, the Bessel/Neumann vanishing of R, Σ J_n(1.8)² = 1) enters as hypotheses. |
| BGS-TRACE-259 | `LineLCollisionForm` (+ batch-3 `LineLLineOrth`) | `Acoset_Aw`, `Cq_collision`, `Cq_collision_exact` | **Partial (closure).** Collision form Σ_u\|A(u + 𝔮)\|² = Σ\|w\|² + Σ_{v≠0, α_v∈𝔮} R(v); with R = 0 at exact collisions and Σ\|w\|² = 1, C_𝔮 = 1 + Σ_{α_v∈𝔮∖0} R(v) − \|Z\|²/q. Theorem U is a hypothesis. |
| BGS-TRACE-255 | `LineL2Decomp` | `A_ideal_line`, `A_qO`, `Dq_eq`, `A_qO_sub`, `inter_eq`, `Diso_eq`, `Diso_fourier` | **Partial.** In O/q = 𝔽_q × 𝔽_q, 𝔮 = ker φ_s, 𝔮̄ = ker φ_{−s}: A(𝔮) = q⁻¹Σ_{ℓ(𝔮)}Ẑ, A(qO) = q⁻²Σ_βẐ, D_𝔮 = q⁻¹Σ_{ℓ(𝔮)∖0}Ẑ, A(qO) − A_tot/q² = q⁻²Σ_{β≠0}Ẑ, 𝔮 ∩ 𝔮̄ = qO, D_iso := A(𝔮 ∪ 𝔮̄) − ((2q−1)/q²)A_tot = D_𝔮 + D_𝔮̄ − (A(qO) − A_tot/q²). The Theorem K1 use is not formalized. |
| BGS-TRACE-218 | `LineIRegroup` (+ `LineIAliasing`, `LineIMoebius`, `LineISummable`) | `regroup_pairs`, `pairs_eq_tsum_CZ`, `aliasing_CZ`, `Fm_CZ` | **Partial (gap closure).** Finite support: (1/q)Σ_ν\|Z_m(ν/q)\|² = Σ_{j∈ℤ} C_Z(jq) for every q ≥ 1 and F_m = φ(2h)⁻¹Σ_{e∣2h}μ(e)(2h/e)Σ_j C_Z(j·2h/e) — both displayed identities. Not formalized: the summable Möbius case and the summable regrouping. |
| BGS-TRACE-273 | `LineMInclusion` | `included_of_bound`, `included_all` | **Partial (inclusion step only).** \|Z_ρ\|² ≥ 4mh ⇒ \|Z_ρ\|²/d² ≥ 4m for every d ∣ h with 1 < d ≤ √h. Not formalized: the certified Line F bound, the interval check m ∈ [15, 20001], monotonicity, the m = 9, 11, 13 remarks. |

Not attempted in this batch (time-box): BGS-TRACE-317 (its finite content is the bookkeeping of TRACE-213 plus numerical
floors; nothing exact beyond the identity of TRACE-213 is stated), TRACE-213, TRACE-214, TRACE-222, TRACE-226.

Integration: `scripts/link_batch4.py` (run once): `record/claims.json` links, scopes and receipt; the curated inventory mirror
(boundary, evidence, verifiers, formalization; `source_blob_sha`). Regenerated: `RESULTS.md` (`render_results.py`) and
`evidence/executions/20261101/lean_inventory/INVENTORY.md` (`make_inventory.py`, text updated to batches 1-4); all other
`render_*.py --check` pass unchanged. Hand edits: README/README.ru Lean counts (167 claims, 182 modules, 2386 declarations,
8882 → 8889 jobs), `formalization/README.md` rows, `CHANGELOG.md`. The existing module `LineLCollision` (BGS-TRACE-248) is
untouched; the new collision-form module is `LineLCollisionForm`.

Files: `lake_build_Bgs.log` (full `lake build` via `build_lean_verified.sh`, "Build completed successfully (8889 jobs)", exit 0),
`build_wrapper.out`, `Axioms.lean`, `axioms.log`, `checks.log`, `unittests.log`, `scripts/`.
