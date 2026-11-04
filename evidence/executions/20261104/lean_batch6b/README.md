# Lean batch 6b (4 November 2026)

Branch `lean-batch-6b` from `main` at `6440a447`. Two new modules under `formalization/Bgs`, wired into `formalization/Bgs.lean`;
10 new `theorem` declarations. No `sorry`, no `native_decide`; `#print axioms` for all 10 is within
{propext, Classical.choice, Quot.sound} (`Axioms.lean`, `axioms.log`). No claim state changed; no boundary changed; no frozen
or sealed row is involved. Parallel batches 6 and 6c own their claims; only the BGS-TRACE-214 and BGS-TRACE-218 rows were edited.

| Claim | Module(s) | Main theorems | Coverage |
|---|---|---|---|
| BGS-TRACE-214 | `LineIHorocycleSummable` (+ batch-5 `LineIHorocycle`) | `char_sumS`, `horocycle_allS`, `horocycle_unitsS` | **Full for the identities (a), (b).** For every kick with Σ\|Φ̂\| < ∞ (arbitrary index type, Z(θ) = Σ′Φ̂(n)e(−θP(n))) and Σ\|c_k\| < ∞: (a) Σ_{ν mod M}\|Z_ν\|²f(z_ν) = MΣ_k c_k C(k), C(k) an absolutely convergent pair series; (b) Σ_{ν unit}\|Z_ν\|²f(z_ν) = Σ_k c_k Σ′_{n,n′}Φ̂(n) conj Φ̂(n′) c_M(k − P(n) + P(n′)). Not formalized (remarks, not identities): diagonal class, the R′ use. |
| BGS-TRACE-218 | `LineIRegroupSummable` (+ batch 2–5 modules) | `regroup_tsum`, `pairs_eq_tsum_CZS`, `aliasing_CZS`, `FmS_CZS` | **Full for both identities.** Regrouping of absolutely convergent pair series Σ′_z a(z)1[q ∣ D(z)] = Σ′_j Σ′_z a(z)1[D(z) = jq] (Summable.tsum_comm on ℤ × κ, summability via the injective graph z ↦ (D(z)/q, z)); hence (1/q)Σ_ν\|Z(ν/q)\|² = Σ_j C_Z(jq) for every q ≥ 1 and F_m = φ(M)⁻¹Σ_{e∣M}μ(e)(M/e)Σ_j C_Z(jM/e) for Σ\|Φ̂\| < ∞. The heuristic assessment is not part of the claim. |
| BGS-TRACE-222 | — | — | **Skipped.** The remaining scope (sector operators on the disc lattices, reflection with symmetric rounding, RK as isometry, ℓ² trace class) has no small faithful finite kernel beyond batch 5's letter-weight and trace-of-word theorems; nothing added. |

Integration: `scripts/link_batch6b.py` (run once): `record/claims.json` links, scopes and receipt for TRACE-214/218 only; the
curated inventory mirror (`source_blob_sha`). Regenerated: `RESULTS.md` (`render_results.py`) and
`evidence/executions/20261101/lean_inventory/INVENTORY.md` (`make_inventory.py`; batch regex accepts `6b`, scopes starting
"Full" shown as full). Hand edits: README/README.ru Lean counts (after merging `main` with batch 6: 190 modules, 2426 declarations, 8897 build jobs), `formalization/README.md`
rows, `CHANGELOG.md`.

Files: `lake_build_Bgs.log` (full `lake build` via `build_lean_verified.sh`), `build_wrapper.out`, `Axioms.lean`, `axioms.log`,
`checks.log`, `unittests.log`, `scripts/`.

Tests: `repository_audit.py` PASS; `scientific_registry_audit.py` OK (419 claims); `render_*.py --check` and
`frozen_packets.py --check` OK (`checks.log`). Maintenance unittests (`unittests.log`): 266 run, 261 pass, 1 skipped,
4 errors, all environmental on a box shared with three concurrent Lean builds: `test_fractional_routing` (child
`check_routing.py` exceeded its 30 s timeout) and three `test_schur_portability` cases (repository copy failed on
`.lake` Mathlib build files changing during the copy). None touches files changed in this batch; a rerun of those two
modules under the same load gave the same 4 errors.

**Merge of `main` (4 November 2026, after PR #86).** `origin/main` (d4c9a360, batch 6 `LineI213Disjoint`) merged into this branch;
`link_batch6b.py` re-run on main's inventory (one 6b caveat, `source_blob_sha` refreshed), `RESULTS.md` and `INVENTORY.md`
regenerated (TRACE-214 kernel column: "summable kicks" instead of "finite"). `lake build` re-run in a checkout without a
prior `.lake/build` (packages shared): "Build completed successfully (8897 jobs)". The first attempt was OOM-killed (exit 137)
on `LineCEncounterExact13` under parallel lake jobs; the second invocation built it and completed. `lake_build_Bgs.log` is
that second pass; `checks.log` and `unittests.log` are re-runs after the merge.
After the merge: all 17 checks EXIT 0 (`checks.log`, pandoc 3.12.1 on PATH); maintenance unittests 266 run, OK (1 skipped).
