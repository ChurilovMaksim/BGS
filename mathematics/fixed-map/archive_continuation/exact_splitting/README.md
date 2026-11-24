# Exact splitting on powers of seven

**Registry:** BGS-TRACE-360.

**Scope.** Let $N=7^k$, $k\ge2$, and use the literal frozen model from
[the maintained definition](../../fixed_map_resolvent_frontier.md).
This result concerns exact equality of eigenvalues at the fixed coupling
$\tau=10^{-80}$. It does not quantify gaps of order $1/N$ or assert
simplicity on all odd dimensions. The distinct family $N=7\cdot5^e$
in [BGS-FM-026](../../literal_time_multiplicity_bounds.md) already uses
related exact-time rank methods and should not be conflated with this one.

## Primitive doublets

After a common scalar rotation, the linear propagator has order
$m=3\cdot7^{k-1}$. On the two unit orbits there are $18N/49$ primitive
double nodes, indexed by the characters of full $7$-power conductor.
In the analytic family $e^{itA_N}M_N$ each splits at order one or two
near $t=0$. At the actual time $t=N10^{-80}$, the resulting lower
bound for the total number of simple eigenvalues is $36N/49$. This
statement counts eigenvalues at the exact time and does not identify
each as lying near its unperturbed node there.

The [full proof](BGS_Exact_Splitting.tex), §§1–3, uses the Schur
complement with $B=4000A_N$, $P$ the linear node projector,
$Q=I-P$, and
$$
J=PBQ(\lambda+M)(\lambda-M)^{-1}QBP,
$$
where the inverse is restricted to `ran Q`. For a scalar first-order
compression $PBP$, it suffices that $J$ be nonscalar. Roots of odd
order remain distinct modulo a prime over 2, so the fraction reduces
to 1 and the off-diagonal entry is detected by $PB^2P$. For
$k\ge4$, the certified stationary contribution isolated at phase 11
modulo 49 cannot cancel: the phase residues form a basis for the degree
49 extension of the reduced cyclotomic fields. The cases $k=2,3$ use
direct finite-field sums. First-order witnesses for the remaining
primitive classes are in the [supporting first-order proof](../earlier_routes/BGS_Spectrum.tex).

The transfer to an arbitrary nonzero real algebraic time uses
Lindemann–Weierstrass on the entries of exponential-polynomial minors.
In particular, the maximal rank of the trace Hankel matrix counts
distinct eigenvalues by Vandermonde factorization. The multiplicity
pattern is locally constant on the maximal-rank locus of the
one-complex-variable analytic family. That locus is connected, because
its complement is discrete. The lower bound established near zero
therefore holds at the exact nonzero algebraic time.

## Positive conductor depths and time-averaged trace

Combining the primitive doublets with the four simple branches at each
fixed positive depth and the separate depth-two calculation gives
$$
\liminf_{k\to\infty}s_{7^k}/7^k\ge18867/19208>0.9822 .
$$
At depth two the residual double block contributes two additional simple
branches in a fraction $17/96$ of such clusters in the limit. The proof
uses exact stationary phases and a $7$-adic square-density calculation;
finite-field checks audit the phase tables but do not formally verify that
asymptotic argument. For the same family the multiplicity calculation gives
$$
\limsup_{k\to\infty}\lim_{T\to\infty}
  \frac1{T7^k}\sum_{r=1}^{T}|\operatorname{Tr}U_{7^k}^r|^2
    \le58663/57624.
$$
The inner limit counts the sum of squares of exact multiplicities.
Neither statement identifies near coincidences at the microscopic scale.

[Original exact-splitting source](BGS_Exact_Splitting.tex) ·
[original supporting spectral source](../earlier_routes/BGS_Spectrum.tex) ·
[central checker](../../../../computations/verification/bgs_f_november/).
The exact characteristic-two verifier, `python exact_splitting/check.py --verify`
from the central checker directory, was rerun. The supporting source
has a wider scope than the items audited here.
