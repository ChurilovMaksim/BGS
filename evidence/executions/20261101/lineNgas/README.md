# Evidence: Lines N5–N19b integration, the polymer-gas route (1 November 2026)

Branch `lineN-gas-conditional` from origin/main. Integration note: `mathematics/fixed-map/lineN5N18_gas_conditional.md`.

## What is integrated
* **Author packets.** N5 … N18b and N19b go under `computations/verification/lineN<k>/`. THEOREM_DRAFT v1–v4 go under
  `computations/verification/lineN_theorem_draft/`, with **v4 canonical** and v1–v3 kept as history.
* **Referee reports.** lineN5 … lineN16 go under `computations/verification/lineN<k>/referee/`; lineN16 is the final pass. The
  coverage table is in the note.
* **Lean.**
  * `formalization/Bgs/LineN{5,6,7,8,10,11,12,13,14,15,16}Arith.lean` are the referee files, verbatim inside `Bgs.LineN<k>`, with
    `#print axioms` added for each of the 168 theorems.
  * They are imported in `Bgs.lean`.
  * `lake exe cache get` exits 0. `lake build Bgs` exits 0 ("Build completed successfully", see `lake_build_Bgs.log`).
  * No sorry and no native_decide. The axioms are within {propext, Classical.choice, Quot.sound}: 143 theorems use all three, 17 use
    propext only and 8 use none.
* **Registry.**
  * New claims BGS-TRACE-299..324 were added by editing `record/claims.json`. The inventory, epochs and renders are regenerated.
  * The state counts are conditional 1, open 7, proved 14, verification-pending 4.
  * Gate: `computations/verification/lineN_theorem_draft/integration_checks/proved_deps_gate_Ngas.py` → GATE_OK, strict for 244..324.
* **Bibliographic snapshot.** `evidence/source_metadata/registry_metadata_20261101_lineNgas.json` is the new snapshot, with its
  review at `record/audits/metadata_cache_refresh_20261101_lineNgas/report.md`. It changes transitive impact sets only.
* **Excluded files.** These are listed with sha256 in `EXCLUDED.md` / `excluded.json`.
* **Manifests.** The verification results are in `manifests.log`.

## Owner wording fix in the repo copy of THEOREM_DRAFT_v4
The author original is `/workspace/bgs-lineN/THEOREM_DRAFT_v4.md`, sha256 6d6c88ed97e0c1f5892cffb32132c7f44c95e994bc6c5bdb62beceabff616207.
* In the §2 p₁ row and the §3 crossover row, the file reference "N18b a_crossover_v2.py with robin() corrected/fixed" now reads
  "N19b a_crossover_v3.py (robin() corrected; v2 in N18b had the bug)".
* A one-line note under v4's header records the change.
* Nothing else differs (diff: 2 rows + the note).

## Not mapped to claims
These are listed in the note under "Not registered":
* [N] numerics;
* the negative results (D1 + G*_gas, the automaton, letterwise CP, the H-product);
* the superseded items of draft §6;
* the N15b and N16b author notes (not refereed);
* the N5 v2 family statement, which enters only as T′ = 1.42785 in H7*.
