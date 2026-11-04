# Lean batch 6 (4 November 2026)

Branch `lean-batch-6` from `main` at `6440a447`. One new module under `formalization/Bgs`, wired into
`formalization/Bgs.lean`; 7 new `theorem`/`lemma` declarations. No `sorry`, no `native_decide`; `#print axioms` for all 7 is
within {propext, Classical.choice, Quot.sound} (`Axioms.lean`, `axioms.log`). No claim state changed; no boundary changed;
no sealed, frozen or hash-pinned packet is touched.

| Claim | Module(s) | Main theorems | Coverage |
|---|---|---|---|
| BGS-TRACE-213 | `LineI213Disjoint` (+ batch-5 `LineIReduction`) | `disjoint`, `same_rho`, `diff_rho`, `core`, `arith_of_nsw`, `dvd_iff`, `reduction_congr` | **Partial (gap closure).** From the congruence definition of BGS-TRACE-206 (ρ = (a, b) ∈ 𝓟*, ν_ρ: bν ≡ a mod 2h as the level d = 1, M_d(ρ): bν ≡ a mod 2h/d and not mod 2h/d′ for d′ ∣ d, d′ < d; d ∣ h, d² ≤ h): for h > 1 with h² + 1 = 2y² (h = h_m, m ≥ 5) the classes {ν_ρ} and the M_d(ρ) are pairwise disjoint; `reduction_congr` is the exact identity W′_m = φ⁻¹Σ_{non-res}(\|Z_ν\|² − RMT_m) + φ⁻¹ΣDev_d(ρ) with the member sets defined by the congruences, so the disjointness hypothesis of batch 5 is discharged. Not formalized: (E″), (T″), (D) ⇒ R′. |

Proof route note: the paper sketch for two different ρ bounds the common modulus by 2h/max(d,d′) ≥ 2√h; the Lean proof
instead combines the two congruences into 2h ∣ dd′·r with r ∈ {±2, ±4, ±6} and uses that h_m is odd and 3 ∤ h_m (both from
h² + 1 = 2y′²), which forces d = d′ = √h and then h = 1. (Without the arithmetic of h_m the statement can fail: for a
hypothetical h = 105 the unit ν = 163 lies in M_5((2,8)) and M_7((−2,16)); 3 ∣ 105, so this h is not an h_m.)

Not done in this batch (time-box; reported to the owner):
* BGS-TRACE-226: a data export and Lean development (`LineJ226Blocks` + 4 data modules: invariant monomial blocks,
  orthogonality, coordinate ‖J_B‖ ≤ 1/2 for all 16 cases by `decide +kernel`) was written; the generic part and one case
  were kernel-checked, but the full 16-case build did not complete within the time box on the shared box (memory), so it is
  not included.
* BGS-TRACE-228 (+ TRACE-293 scope): not attempted (needs the Gauss-sum/CRT model of Ẑ^{(d)}_β and W_{d,β}).
* BGS-TRACE-214/218/222: handled by a parallel batch (branch `lean-batch-6b`), not here.

Integration: `scripts/link_batch6.py` (run once): `record/claims.json` (formalization paths, scope, receipt of TRACE-213
only) and the curated inventory mirror (`source_blob_sha`). Regenerated: `RESULTS.md` (`render_results.py`) and
`evidence/executions/20261101/lean_inventory/INVENTORY.md` (`make_inventory.py`); all other `render_*.py --check` pass
unchanged. Hand edits: README/README.ru Lean counts (171 claims, 188 modules, 2416 declarations, 8894 → 8895 jobs),
`formalization/README.md` row, `CHANGELOG.md`.

Files: `lake_build_Bgs.log` (full `lake build` via `build_lean_verified.sh`, "Build completed successfully (8895 jobs)",
exit 0), `build_wrapper.out`, `Axioms.lean`, `axioms.log`, `checks.log`, `unittests.log`, `scripts/`.

Test status: the audits in `checks.log` pass (exit 0). The maintenance unittest run (`unittests.log`) was stopped by a
600 s timeout on the shared, memory-constrained box (exit 124) after ~170 tests, with one error (E) recorded before the
cut-off; it is not a complete pass and must be re-run by CI.
