# Continuation after the Floquet network interruption

Date: 2026-09-05.

## Mathematical delta

The continuation derives an abstract theorem connecting a normalized trace
of order one at an integer time q_D=o(D) to an obstruction for uniformly
unfolded microscopic second factorial statistics. The proof uses exact
Parseval and Poisson identities and positivity of the Fourier transform of
a Gaussian test; no high-frequency trace estimate is assumed.

The detailed argument is prepared as
`mathematics/resonance_microscopic_obstruction.md`. The independent finite
checker is prepared as
`computations/verification/resonance_pair_variance_regression.py`.

For the proposed Pell Floquet construction, the application explicitly
retains two hypotheses: the normalized Hilbert--Schmidt normal-form bound
12 epsilon^2/sqrt(K), and the Gaussian empirical law of the averaged
observable. These are the prior analytic obligations, not consequences of
the new regression program. Subject to them, at
epsilon_K sqrt(2K) -> tau != 0 the variance coefficient is bounded below by

    chi(tau) = 2 sum_(m>=1) exp(-m^2 tau^2).

The microscopic interval variance has liminf at least chi(tau)L^2. At tau=0
it diverges for every fixed L>0. A fixed Gaussian Schwartz test gives a
direct contradiction with the orthogonal reference pair correlation, not
merely a comparison of global spectral moments. Thus
|epsilon_K| sqrt(K) -> infinity is necessary for the indicated uniformly
unfolded random-matrix second-correlation limit; it is not sufficient.

## Additional algebraic check: global uniformity is compatible with this obstruction

On the odd space the unperturbed U_0 has each K-th root of unity with the
same multiplicity (N-1)/(2K). If epsilon_K -> 0 and ||B||_op<=2, then for
every fixed positive integer r,

    |D^(-1)Tr(U_epsilon^r)-D^(-1)Tr(U_0^r)|
        <= ||U_epsilon^r-U_0^r||_op <= 2r|epsilon_K| -> 0.

For K>r the second normalized trace is exactly zero. Negative powers are
handled by adjoints. Therefore the full eigenphase empirical measure tends
to uniform measure on the circle. This conclusion is unconditional within
the finite construction and uses no Gaussian limit.

At the critical scale the spectrum is consequently globally uniform, yet
has the moving resonance at r=K and the microscopic obstruction above.
The order of limits matters: fixed-frequency equidistribution does not
exclude nonvanishing Fourier coefficients at a frequency tending to
infinity but remaining o(D).

## Symmetry and ensemble checks

The physical centered-Weyl kernel for T=((3,2),(4,3)) is, up to a global
phase and N^(-1/2),

    U(x,y)=exp_N((3x^2-2xy+3y^2)/8).

N is odd, so 8 is invertible. The odd-space cosine diagonal is simple and
the kernel entry U_-(x,1) is nonzero for every odd-basis index x. Thus the
common linear commutant of B and U on this space consists only of scalars.
This is not a claim that every individual U_epsilon has a simple spectrum.

The kernel is symmetric in x,y. Hence the symmetrically kicked unitary
exp(i epsilon B/2) U exp(i epsilon B/2) is symmetric, and complex
conjugation in the real odd basis is an antiunitary reversal squaring to
+1. It is isospectral to exp(i epsilon B)U. The orthogonal, rather than
only the unitary, reference comparison is therefore relevant. No absence
of antiunitary symmetry is claimed.

The new lower bounds depend on absolute squared traces. A different global
phase convention for the quantum propagator does not change them.

## Verification and publication status

This continuation has not obtained a verified runtime response for new
Python execution, Lean compilation, or remote commit confirmation. No
successful-run certificate, numerical measurement, current commit hash,
or updated PDF is asserted here. The checker source contains assertions
and will emit an execution report only after a successful actual run.

The checker has two independent exact rational variance calculations
(circular interval intersections and a sweep of the count process), a
Fourier partial-sum lower bound, direct/Fourier Gaussian factorial-statistic
comparisons, repeated-eigenvalue controls, and a periodic-replication trace
identity. These are finite identity checks, not tests proving H1 or H2.

A full-text literature/priority comparison also remains unconfirmed in
this continuation. The abstract Fourier identities are standard tools;
no claim that their use here has established a new general mathematical
principle or a prize-level result is made.

## Boundaries that must remain in summaries

Uniform mean-density unfolding is essential to the statement. Unfolding
by the mesoscopic density modulation changes the tested statistic, and
its resulting local law has not been derived. The classical perturbation
corresponding to this quantum kick vanishes with N; this is not a theorem
about a fixed nonzero classical perturbation. A full microscopic two-point
function is not obtained, only an obstruction and a necessary strength
scale. Full BGS remains a separate objective.
