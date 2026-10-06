# Exact finite Heisenberg controls

Requires Python 3, SymPy and NumPy. Run each script normally and with `-O`.
Imports are silent and do not execute checks or write files. Failures raise
exceptions and return nonzero exit status, including under optimization.

- check_independent.py: rational nonnormal trace-table bounds, inverse telescopes,
  complete partitions, Laurent distinct-index identities and adjoint counterexample.
- check_raw_gauss.py: raw/midpoint phases, initial Gauss sums, modular closure.
- cluster_checks.py: exact rational covariance and toy connected cumulants;
  formal combinatorial factors only, not the local analytic theorem.
- exact_controls.py: independent complete-branch reciprocity versus raw modular trace.
- exact_branch_modes.py: independent individual-branch 4-periodic mode reciprocity.

The last two print their JSON certificates to stdout when executed (redirect
stdout to an explicit build/evidence output location if needed), and use bounded
NumPy int64 histograms followed by arbitrary-precision integer cyclotomic
polynomial division. Inputs are fenced to m,N=(1,3),(2,3),(3,7),(4,3),(4,9)
and integer frequencies of absolute value at most 9. D<=1152, every HNF
representative coordinate <1152, |adj(B)_ij|<=D/4<=288, |t_j|<=9,
and |t+4nu|<=4613. Direct triangle bounds on displayed numerators are
<10^15; histogram counts and radical multipliers are <10^12, safely below
2^63. Largest lattice is 36^4; largest conductor is 82944. These are
finite fixtures, not arbitrary-input exact-arithmetic routines.

No floating diagnostic is part of this certificate. Earlier floating
Gaussian/metaplectic diagnostics are auxiliary and deliberately not promoted.
No finite test establishes the WKB analytic norm estimate, box asymptotics,
contour deformation, signed ensemble comparison or BGS.
