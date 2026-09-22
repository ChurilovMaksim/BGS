# Research operating protocol

**Status:** repository process specification, adopted 5 September 2026.

This file records the working discipline for the BGS research programme. It is
not a mathematical theorem and does not override `claim_ledger.md` on claim
status. Its purpose is to prevent research results, computations, formal
certificates, manuscript text and repository summaries from drifting apart.

## 1. Research objective

The programme keeps the full target in view: rigorous microscopic
Bohigas--Giannoni--Schmit/RMT universality for a mathematically natural chaotic
quantum family, with arithmetic quantum cat maps as the current structured
laboratory. Subproblems may be solved on the path to that target, but their
scope must never be silently promoted to the full conjecture.

Every research pass should end in at least one durable output: a proof or
precisely stated conditional theorem; a counterexample/obstruction; a better
bound; an exact reduction; a reproducible certificate/regression; a source-
audited literature boundary; or a concrete high-information next experiment.

## 2. Language and tool selection

No programming language is privileged. Choose the implementation that makes
the relevant claim easiest to verify and hardest to accidentally falsify.

### Python / SymPy
Use for symbolic algebra, exact small/medium finite-field experiments,
polynomial/resultant/subresultant work, rapid adversarial searches, data
reduction and independent reference implementations. Prefer exact integer,
rational or finite-field arithmetic for load-bearing claims.

### C++20
Use for high-volume exact enumeration, multiprecision arithmetic, large finite
searches, performance-sensitive independent implementations and negative
controls. A C++ implementation is especially valuable when it verifies a
Python/SymPy result through a mechanically different representation.

### Lean 4
Use for finite certificates, stable algebraic/combinatorial kernels, falsifiers
for delicate logical reductions, and gradually for symbolic theorems when the
library cost is justified. Formal status may be claimed only when a real
`lake build` succeeds.

### TeX
The active manuscript is a research artifact, not a retrospective marketing
document. Promoted theorems, corrected hypotheses, retractions and changed
closure conditions should be incorporated when they alter the scientific
story.

### Other languages and tools
Use Julia, Rust, C, shell tooling, computer algebra systems, Wolfram,
visualization libraries, SAT/SMT/proof tools, or other available languages when
they materially improve correctness, performance, independent verification or
communication. Do not rewrite a working algorithm merely to increase the
number of languages used.

## 3. Two-implementation rule for delicate finite claims

For finite computation that materially supports a theorem route, prefer two
mechanistically distinct implementations whenever feasible. Independence means
a different representation or algorithm, not two wrappers around the same
routine. Agreement is evidence about implementation, not proof of a growing-
parameter theorem.

## 4. Promotion checklist

A result is not fully integrated merely because a proof note or script exists.
Before promoting a substantive result, check as applicable:

1. complete statement/hypotheses/proof/gaps in `mathematics/`;
2. reproducible code in `computations/verification/` or `computations/analysis/`;
3. Lean modules when there is a useful formalizable kernel/certificate;
4. promoted compact evidence in `evidence/` rather than terminal/chat output;
5. correct status in `record/claim_ledger.md`;
6. theorem-index update in `mathematics/results.md`;
7. README status/frontier/verification-command update;
8. TeX manuscript update if the main mathematical narrative changes;
9. literature update when an external theorem becomes load-bearing;
10. research-route/retraction/provenance record update;
11. CI regression gate when future refactors could silently break evidence;
12. synchronization of generated PDFs/figures/tables whenever the available
    repository interface permits binary-safe updates; otherwise record the
    limitation explicitly rather than pretending synchronization occurred.

## 5. Main versus research branches

Direct work on `main` is acceptable when a change is small, independently
checked and cannot invalidate unrelated work. Use a research branch/PR when a
theorem is new and still under red-team review, the change spans several
scientific layers, CI must test a new implementation before promotion, `main`
is moving concurrently, or the result may need retraction without disturbing
authoritative files.

A branch should not become a long-lived second truth. Once mathematics, scope
and CI are satisfactory, reconcile it with current `main` and merge or close it.
Never force-update `main` merely to resolve concurrent movement.

## 6. Verification order

Use the cheapest falsifiers first: domains/types/signs/dimensions/normalization;
trivial/degenerate/boundary cases; exact small instances; invariants/symmetry;
independent implementation; broader/high-precision search; symbolic proof or
source-exact theorem application; Lean/formal verification when valuable; then
full repository regression.

Unexpected output competes first with the bug hypothesis. Numerical agreement
must never be described as proof of a universal theorem.

## 7. Research-code quality

Research code is mathematical evidence. It should state the finite assertion
it verifies; separate theorem proof from regression evidence; avoid hidden
randomness; use exact arithmetic for exact claims where feasible; expose
intermediate invariants; contain adversarial/known-exception controls; avoid
cache/generated clutter and duplicated data; and be appropriate for its CI tier
(or clearly marked extended/manual).

Optimization order is algorithm/representation first, then native/vectorized
libraries, profiling, JIT/compiled kernels and parallelism. Change language
after locating the actual bottleneck.

## 8. Figures, simulations and visual artifacts

When mechanisms are easier to inspect visually, create reproducible figures or
animations from committed scripts rather than hand-editing outputs: eigenphase
spacing/unfolding diagnostics, collision geometry, row-intersection heat maps,
discriminant/prime-support scaling, Frobenius orbits, trace convergence, or the
theorem/obstruction dependency graph. Visual evidence remains numerical unless
accompanied by proof.

## 9. Synchronization rule

No important result should live only in chat, a terminal log or one unindexed
Markdown note. Once promoted, proof, verification, claim status, theorem index,
README and manuscript should agree as applicable. If temporary divergence is
unavoidable, record exactly what is authoritative and what remains to sync.
`record/claim_ledger.md` remains final authority on mathematical status.

## 10. Current highest-value frontier

As of 5 September 2026:

- control split-prime support of canonical product-row coefficient ideals
  `D'_K^(3)` using their Chebyshev/cyclotomic-unit structure;
- exploit residue-degree/Frobenius amplification outside the split slice;
- close pointwise centered Cayley energy on all intended split designs;
- prove Heisenberg-scale joint trace comparison sufficient for microscopic
  local statistics (`mathematics/trace_to_local_statistics_bridge.md`);
- connect finite-field arithmetic to the required desymmetrized spectral traces
  in a natural quantum-map model.

The full microscopic BGS/GOE/COE statement remains **OPEN**.
