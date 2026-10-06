# Exact higher-ramified checks

Use the top-level ramified_higher_commutant.py normally and with Python -O.
Requires Python, NumPy and SymPy. No author implementation is imported.
Imports are silent; field-table initialization and every test occur at execution.
All assertions from the reviewed implementation are explicit exceptions in the
portable derivative, so optimization cannot remove a certificate condition.

Five independent modes are retained:
- bases: six literal effective-gauge 49-dimensional cyclic/rank witnesses
- unit_bases: six actual unit-upper-gauge witnesses, separately labeled
- dictionary: q-Lucas and endpoint blocks in the four reviewed finite regimes
- poles: shifted penultimate blocks at n=147 and all 36 pole/grid combinations
- grades: bounded recurrence supports and exact rational valuation inequalities

The only runtime input is the 5,922-byte, hash-pinned pole dictionary. Its
bytes equal the existing inherited canonical dictionary. The much larger
old degree-828 factorization and norm data are not duplicated or falsely
claimed as rerun by this checker; their completed original review is retained.

All field coefficients are residues 0..4 in F5[x]/Phi49, using int64 arrays.
A convolution coefficient has at most 42 products of size16; multiplication
by the 83-by-42 monomial table stays below 83*672*4. The largest Fourier
contraction sums 49*42 products of size16, also safely below signed64 range.
Modular reductions precede reuse. Polynomial Euclidean quotients use residue
coefficients, and valuation controls use arbitrary-precision Fraction/int.
No floating-point value is used in a mathematical comparison.

Each child has a 2GiB address-space cap, 180CPU-second cap and 240-second wall
timeout. Thread environment variables request one thread. These are per-child
limits, not a claim that the whole multi-mode run uses one core at OS level.
Optional output is an external/build directory; existing result files and
maintained-source destinations are rejected.

Finite regimes and complete results are pinned in original/execution_manifest.
The universal theorem also uses the reviewed normalized-lattice argument,
q-Lucas derivation, shifted-base proof and saturated-lattice conclusion.
Finite samples alone do not prove it. No Lean, all-N simplicity, full complex
scalar commutant of U, quantitative gap or BGS conclusion is certified here.
