# Source-bound acceptance after the local repairs

Primary verdict: **proved as written**, within the scoped matrix hypotheses and separately reviewed computer-assisted classification dependency stated in the canonical proofs. No remaining mathematical consolidation gap identified. This supersedes only the TRACE-016 definition blocker in review.md; all boundaries and collateral integration cautions there remain applicable.

## TRACE-016 repair

Accepted current canonical proof SHA256:
2dca5b084377b22cdabe074678113bd133fef35b0a8d9795ce8714c5b6004c37

I read the changed definitions and compared the complete current proof against the preserved prior source (0953f512784c2ac7c640f2417f9b9441ebd441c9eaf794f72801303601ad60d8). Replacing precisely the two previously identified definition sentences reproduces the current file byte-for-byte. Both now require pairwise distinct cyclic length-K vertex substrings, equivalently equality of K-words forces equality of starts. This is exactly the injectivity used by primitivity and localization. Nothing else in the proof changed. The accepted corrected U/V arguments, local-overlap correction, multiplicities, estimates and formalization boundary therefore remain as reviewed.

## TRACE-015 entry wrapper

Analytic canonical proof remains unchanged and accepted:
7fd5b03f4cbc28e8daa30518e223b35f8962d9cae9a8309f9c43704f31390893

Current verifier:
19e5959e1719c57b4c1729008b099f154204118300300aabc34fb057c26de870

The complete old executable body and the new main() body (excluding its added return 0) have identical location-independent Python ASTs. The wrapper introduces local function scope, but changes no tested predicate, arithmetic, loops, seed, counts or output statement. Fresh execution in both normal and optimized Python exits zero, emits no stderr, and is byte-identical to the original results.json. Both outputs hash to 0f2f2a2f6557156b72dbb8f056c71a43c30f7c8f8c05fb8aec1470c217114362. A fresh non-main run_path import is silent. These checks address the wrapper change only; finite controls remain finite controls and do not certify the asymptotic theorem.

## Other current accepted canonical source

FM-023 remains unchanged:
4aa4da166331c02d0e527b68b1354827ef7011b67ec7d178ed1c3d71703f9881

## Evidence and remaining integration constraints

repair_checks.json records source hashes, exact-replacement/AST checks and new runs. wrapper_normal.json and wrapper_optimized.json preserve fresh outputs. No full unchanged mathematical review or Lean compilation was repeated; no repository or source artifact was modified.

Promotion should use the current TRACE-016 proof and current TRACE-015 verifier hashes, preserving old sources as historical provenance. Reconcile destination hashes after copying, preserve retrievable accepted inputs, resolve the minor historical-SymPy attribution ambiguity in the curated FM-023 review, and run registry/manuscript/full-build integration checks separately. The fixed-family claims and bounded Lean trust boundary remain unchanged; deterministic BGS and the full signed hierarchy remain open.
