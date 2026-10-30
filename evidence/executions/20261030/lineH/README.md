# Evidence: Line H (2026-10-30)
* `receipt.json`: sha256 of every packet file, the proposed IDs, the referee verdict, and the code hashes of the certificate runs.
* `lean_axioms_LineH_standalone.log`: `lake env lean` on `formalization/Bgs/LineH.lean`, with `#print axioms` for all 9 declarations.
  Only propext, Classical.choice and Quot.sound appear. There is no sorry and no native_decide.
* `AxiomsLineH.lean`: the axioms check to run after `import Bgs.LineH` has been added to `Bgs.lean` (see `formalization/Bgs.lean.patch`).
  The integrator should run `lake build Bgs` and store the logs here.
