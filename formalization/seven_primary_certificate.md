# Seven-primary executable GF(5) predicates

Claim ID: **BGS-FORMAL-003**. Status: compiled Lean 4.33.1 certificate with independent semantic/code review.

The unchanged [Lean source](Bgs/SevenPrimary.lean), SHA-256 `431e5d111238a962ec2bb994f21d4cb1ac17df250379651aa4e8fcd065604cb4`, proves exactly 22 executable-array predicates: seven product checks, seven all-factor Rabin computational checks, seven degree-exclusion checks, and the finite order-of-5-modulo-49 predicate. There are 46 factor occurrences, including factor degrees 246 and 366; the largest polynomial degree is 828.

The isolated full source compiled successfully in 136.58 seconds and emitted an olean. The [original receipt](../evidence/formalization/seven_primary_20261006/build_receipt.json) and axiom log preserve that exact execution. The independent [semantic audit](../archive/record/seven_primary_semantic_review.md) checked coefficient binding and fresh GF(5) replay; 1,896 additional Lean reference/negative controls compiled. The subsequent [aggregate build](../evidence/formalization/seven_primary_20261006/aggregate-build.json) passed all 19 active modules in 22 Lake jobs; existing modules were replayed, SevenPrimary was freshly compiled and Bgs rebuilt. This is distinct from the original isolated compilation.

These proofs use native_decide and explicitly trust native compilation/evaluation, in addition to printed standard axioms where present. No generic array-to-polynomial correctness, Rabin theorem, finite-field/root-order bridge, two-row proof, rank lift, actual commutant theorem or BGS theorem is formalized. The abstract mathematical interpretation remains a separately reviewed argument. See [actual commutant proof](../mathematics/actual_seven_primary_commutant.md).
