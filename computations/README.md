# Computations

The maintained computational surface is deliberately compact and independently
cross-checked. Historical language ports and exploratory work are not kept as
parallel source trees.

## C++20 — exact/exhaustive kernels

- `cpp/fourth_moment_pair_key_verifier.cpp` — independent corrected pair-key,
  coupling-total and fourth-moment finite verifier.
- `cpp/cayley_energy_verifier.cpp` — exact mixed Cayley-energy verifier with
  generic/exceptional controls for `K=11,13` plus `(461,23)`.
- `cpp/cayley_direct_energy_verifier.cpp` — independent finite verifier for the
  direct bilinear Cayley-fiber theorem on five subgroup designs with `K>100`.
- `cpp/cayley_fibonacci_verifier.cpp` — arbitrary-precision independent check of
  the 28-digit `K=131` Fibonacci exceptional-prime certificate.
- `cpp/cat_map_order.cpp` — exact order/split-prime utility and regression for
  the old Julia order/comment mismatch.

Every `.cpp` file here must occur in `CMakeLists.txt`; the repository audit
enforces that invariant.

## Python — checked arithmetic and orchestration

`python/bgs/` contains finite-field, discrete-log, pair-key and twisted-Jacobi
primitives with fail-fast design validation. In particular,
`jacobi_matrix` accepts a validated annihilator sub-sector (such as a parity
sector) and rejects characters outside it.

`verification/` contains the maintained gates:

- `current_regression.py` — fast exact anchors and API contracts;
- `mixed_cayley_energy.py` — 720 matching systems, exact cyclotomic resultants
  for `K=11,13`, finite reductions and the `K=23` witness;
- `cayley_uniform_cutoff_regression.py` — finite exact checks for the original
  prime-order resultant cutoff;
- `cayley_resultant_fibonacci.py` — exact square-resultant, Fibonacci and
  28-digit certificate producer;
- `cayley_resultant_mass_budget.py` — exact normalized Galois-orbit,
  common-root and `p`-adic resultant-valuation regression for the global
  split-prime collision-mass theorem on the complete `K=11,13` exceptional
  sets;
- `cayley_jacobi_trace_regression.py` — finite complex128 comparison of the
  exact ordinary full-annihilator identity `1_Ahat(r)=K Tr M_S(2r)` against an
  independent direct Cayley Fourier transform; all frequencies are checked at
  `(53,13)` and `(199,11)`, with deterministic larger checks at `(461,23)`, and
  the exact-energy second/fourth trace-moment formulas are separately regressed;
- `twisted_jacobi_regression.py` — maintained producer for preserved finite
  twisted-Jacobi regressions;
- `repository_audit.py` — whole-tree structure, no-Julia, duplicate,
  provenance, Markdown-link, Lean-placeholder/import and CMake-coverage checks.

The Cayley/Jacobi trace regression is intentionally labelled
**FINITE-REGRESSION**: complex128 agreement checks phase and normalization but
is not evidence for Bombieri--Vinogradov, the double-averaged asymptotic, a
Gaussian distribution theorem, or microscopic BGS.

`analysis/spectral_diagnostics.py` keeps the useful finite spectral experiments
with corrected semantics. It diagonalizes the full complex Hermitian sector
matrix `M+M^*`, never an entrywise-real projection. Its `verify` mode
recomputes the complete committed spacing and matched-window JSON records and
is run in CI. The outputs remain descriptive only: no IID-KS or stationary
number-variance claim is attached.

## Language policy

- **C++20:** expensive exact enumeration and independent finite verifiers.
- **Python:** symbolic/exact orchestration, transparent reference
  implementations and finite numerical analysis.
- **Lean 4:** formal finite certificates and falsifiers.
- **TeX:** manuscript source.
- **Fortran:** introduce only if profiling identifies a genuine dense numerical
  hot path that benefits from it.
- **Julia:** zero tracked `.jl` sources. All 31 historical Julia paths have a
  final disposition in `../record/julia_migration.md`.

The goal is not a language percentage. It is one maintained implementation per
scientific role, with independent checks where they materially increase
confidence.
