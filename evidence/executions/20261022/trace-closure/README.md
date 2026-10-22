# Trace dependency closure: actual verification scope

22 October 2026; base main `2271f00b17b2480f8f833fe55754a55c1b8c8bde`.
[Mathematical review](../../../../record/trace_closure_20261022.md).

- `finite_checks.json`: actual `python3 -O` exact rational execution, four stationary aliases, 2,737 exact Gauss entries in 49 odd dimensions, canonical Hessians and error exponents; no asymptotic certification.
- `source_check.json`: Bowen--Ruelle primary PDF hash, exact locators and hypothesis mapping. The copyrighted PDF is not tracked.
- `maintenance_checks.json`: actual generator, reconstruction, registry, source/link and mandatory finite-orbit synchronization results; a known authenticated tree supplies paths absent from this partial overlay.
- `math_parse.json`: explicit math parser coverage and limits.
- `manuscript_build.json`: the new three-pass build and rendered-page inspection scope.
- `receipt.json`: final source hashes, execution scope and open-claim boundary.

The mathematical proofs have adversarial self-review. No new external referee,
agent review, Lean compilation, Wolfram or C++ execution is asserted. The
historical 56-check evidence packet and original archive are unchanged.
An initial verifier draft accidentally used floating signs for negative integer
powers; its exact equality check rejected that version. The final source uses
integer parity and passes under `-O`; this correction changes no theorem.

The selected bibliography snapshot is
`evidence/source_metadata/registry_metadata_20261022.json`, authenticated by
its sibling SHA256 file and selected by `literature/metadata_audit.json`.
Reproduce the offline metadata guard with
`python3 computations/verification/bibliographic_metadata_audit.py --self-test`.
The new guard run checks 52 source identities and 470 deliberate mutations;
only the new source had fresh primary-source inspection in this pass.

Rebuild the manuscript with three runs of `pdflatex -interaction=nonstopmode
-halt-on-error BGS_unified.tex` from `manuscript/`, using a temporary output
directory. The current accepted build is 324 pages with zero horizontal
overflows and no unresolved references/citations; three new-section pages
and the final bibliography page were inspected. The log archives preserve
actual execution output, not a blanket proof certification.
