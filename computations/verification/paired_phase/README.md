# Exact paired-phase controls

Run the top-level paired_phase_reductions.py normally and with Python -O.
Python, NumPy and SymPy are required. Each bounded child has a 180-second
wall timeout. Imports are silent, failures explicit, and outputs use stdout
or an external/build directory. No OS memory cap is claimed for these controls.

Branch/winding fixtures cover m=1,...,4, with D<=1152 and 307,984 listed
classes, including exact 4^m duplicate multiplicity. They check 1,366,560
polarization pairs/perfect pairings and 16 cyclotomic Gauss norms at N=3,5,7,9,
including noncoprime resonances. The m=1 and m=2 repeated-neighbour cases and
the distinction between physical and winding Smith groups are retained.

NumPy int64 is exact on these fenced fixtures: |v_j|<=4607; the nonnegative
adjugate has row sum D/4<=288, hence |xnum_j|<=1,326,816. Every displayed
phase numerator is below 2^36 in absolute value; histograms have at most D²
counts. This is far below 2^63. Final cyclotomic divisions use exact SymPy
rationals. The routine is not an arbitrary-dimension int64 API.

Locality controls are exact rational matrices at m=1,...,12 and both Hessian
signs. Frostman constants use exact Fraction inequalities and 24 rational
Green cycles. Decimal logarithms are display only. Symbolic gluing controls
also check the missing iN derivative factor explicitly.

The original independent review additionally contains 80-digit finite physical
trace diagnostics; those are preserved as historical floating diagnostics,
not included in this exact replay or promoted as analytic/asymptotic proof.
The infinite nonlinear, monotonicity and Frostman results rely on their exact
reviewed proofs. No pointwise Fourier decay or complete quantum-weight
comparison follows from these controls.
