# A decaying initial term in the stopped gap theorem

TRACE-077 changes the variable used for the intensity chain. If
`G=(I-P+J)^(-1)-J` and `M=G-(I-J)`, classical coordinate elimination
is exactly an orthogonal compression of M. The original entry-flat matrix
therefore contributes at most `min(1/4, Bu/N)` at retained size u, rather
than a depth-independent initial singular bound.

Fresh quantum feedback produces a centered linear increment plus an
explicit quadratic remainder in these coordinates. All increments live
in the original N-dimensional space. Future retained projections occur
only outside their martingale sum, preserving conditional centering under
adaptive choices of the next port. Including the entire first violating
state avoids a future-flatness conditioning argument.

The [proof](../mathematics/green_compression_gap_20261013.md) gives failure
probability at most `1296 N^(2/p)(p-1)K²log(2N)²/(m eta²)` and remainder
`432K²log(2N)²/m`. With `m=ceil(log(2N)^(7+kappa))`, `eta=log(2N)^(-2)`
and even `p=2ceil(log(2N))`, the stopped singular norm is
`O(log(2N)^(-2))` throughout the reached interval
`m <= u <= floor(N/log(2N)²)`, with failure `O(log(2N)^(-kappa))`.
The correct three-step kernel there is `(1+O(1/log(2N)))/u` before entry
exit. This closes the corresponding deep-range forcing term in TRACE-075.

The interval can be empty because of an early entry exit. No survival
probability follows from this proof. The remaining dynamic problem is
entry control, including higher moments or accumulated two-step row–column
correlations. The original deterministic local process, signed TRACE-005
and BGS remain OPEN. Classical group-inverse and stochastic-complement
structures are credited; priority is not established.

The initial FM-021 singular bound is a fixed eventual bound, not a limit
to zero asserted by FM-021. The decaying factor `u/N` is what removes its
possible persistent contribution at sublinear depths. The actual-map
corollary inherits its odd-N, fixed-coupling regime and ineffective startup.
