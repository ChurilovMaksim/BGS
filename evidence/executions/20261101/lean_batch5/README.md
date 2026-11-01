# Lean batch 5 (1 November 2026)

Branch `lean-batch-5` from `main` at `dc1dda85` (after PR #78). Five new modules under `formalization/Bgs`, wired into
`formalization/Bgs.lean`; 23 new `theorem`/`lemma` declarations. No `sorry`, no `native_decide`; `#print axioms` for all 23 is
within {propext, Classical.choice, Quot.sound} (`Axioms.lean`, `axioms.log`). No claim state changed; no boundary changed (none
of the batch-5 boundaries says "not formalised"); no sealed wave-2 row is involved.

| Claim | Module(s) | Main theorems | Coverage |
|---|---|---|---|
| BGS-TRACE-222 | `LineJSectorConj` | `K_weight`, `R_weight`, `RK_weight`, `e_half_int`, `trace_conj`, `prod_conj`, `trace_prod_conj` | **Partial.** Letter weight w_{C,a,τ}(n) = ĝ(n)e(Cn²/2)e(an/8)e(nτ), with conj ĝ(n) = (−1)ⁿĝ(n) and ĝ(−n) = ĝ(n) as hypotheses: K: (C, a, τ) ↦ (−C, 4 − a, −τ), R: (C, a, τ) ↦ (C, −a, −τ), RK: (C, a, τ) ↦ (−C, a − 4, τ) for every real τ; for matrices, V′_i = U conj(V_i) U⁻¹ for every factor ⇒ Tr∏V′_i = conj Tr∏V_i for every finite word. Not formalized: the lattice operators, the reflection with symmetric rounding, RK as an isometry of the Line F spaces, the ℓ² trace-class setting, the Galerkin check. |
| BGS-TRACE-214 | `LineIHorocycle` (+ `LineIAliasing`) | `char_sum`, `pair_char`, `interchange`, `horocycle_all`, `horocycle_units` | **Partial.** Finitely supported kicks, f(z_ν) = Σ_k c_k e(kν/M) with Σ\|c_k\| < ∞: (a) Σ_{ν mod M}\|Z_ν\|²f(z_ν) = MΣ_k c_k C(k); (b) Σ_{ν unit}\|Z_ν\|²f(z_ν) = Σ_k c_k Σ_{n,n′}Φ̂(n) conj Φ̂(n′) c_M(k − P(n) + P(n′)). Not formalized: infinite-support kicks; the diagonal-class and R′ remarks. |
| BGS-TRACE-213 | `LineIReduction` | `reduction` | **Partial.** From the frozen definitions of F_m, Res_m and W′_m: W′_m = φ⁻¹Σ_{ν unit, non-res}(\|Z_ν\|² − RMT_m) + φ⁻¹Σ_{ρ, d incl.}Dev_d(ρ), assuming that {ν_ρ} and the M_d(ρ) are pairwise disjoint sets of units. Not formalized: the disjointness from the congruence definition; (E″), (T″), (D) ⇒ R′. |
| BGS-TRACE-317 | `LineIReduction` | `reduction`, `rmt_le`, `NR_ge`, `Dev_ge` | **Partial.** The bookkeeping identity (as for TRACE-213), NR ≥ −RMT_m (RMT_m ≥ 0), RMT_m ≤ 4m, and the level floor Dev_d(ρ) ≥ −n_d\|Z_ρ\|²/d². Not formalized: the floor −(h_p/d)S_ρ with its constants; the m₀ = 15 inclusion (its inclusion step is TRACE-273, `LineMInclusion`). |
| BGS-TRACE-218 | `LineIMoebiusSummable` (+ batch 2–4 modules) | `FmS_moebius` | **Partial (gap closure).** The Möbius formula F_m = φ(2h)⁻¹Σ_{e∣2h}μ(e)(2h/e)Σ′_{pairs}1[(2h/e) ∣ P(n) − P(n′)] for kicks with Σ\|Φ̂\| < ∞. Still not formalized: the regrouping of absolutely convergent pair series into Σ_j C_Z (done for finite support in `LineIRegroup`). |
| BGS-TRACE-293 | `LineN3SignConjComposite` (+ batch-4 `LineN3SignConj`) | `inherit_conj`, `prime_inherit_conj` | **Partial (extension).** Composite levels ce: W_{ce}(−ρ) = conj W_{ce}(ρ) from the inheritance W_{ce,eβ′} = (n_e/e²)W_{c,β′} with the same real n_e for both signs; with c = q prime it combines with the prime-level theorem. BGS-TRACE-228 is a hypothesis. |

Not attempted in this batch (time-box): BGS-TRACE-226 (its exact content is the block decomposition of the 16 automaton
cases and the bound ‖J_B‖ ≤ 1/2 on exported data; it needs a data export like batch 3's `gen_monomial_data.py`).

Integration: `scripts/link_batch5.py` (run once): `record/claims.json` links, scopes and receipt; the curated inventory mirror
(boundary, evidence, verifiers, formalization; `source_blob_sha`). Regenerated: `RESULTS.md` (`render_results.py`) and
`evidence/executions/20261101/lean_inventory/INVENTORY.md` (`make_inventory.py`, text updated to batches 1-5); all other
`render_*.py --check` pass unchanged. Hand edits: README/README.ru Lean counts (171 claims, 187 modules, 2409 declarations,
8889 → 8894 jobs), `formalization/README.md` rows, `CHANGELOG.md`.

Files: `lake_build_Bgs.log` (full `lake build` via `build_lean_verified.sh`, "Build completed successfully (8894 jobs)", exit 0),
`build_wrapper.out`, `Axioms.lean`, `axioms.log`, `checks.log`, `unittests.log`, `scripts/`.
