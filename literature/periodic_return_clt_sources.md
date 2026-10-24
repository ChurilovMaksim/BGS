# Classical input for arithmetic return traces

Checked 2026-09-11: Guy Cohen and Jean-Pierre Conze,
*Central limit theorem for commutative semigroups of toral endomorphisms*,
[arXiv:1304.4556](https://arxiv.org/pdf/1304.4556).
The downloaded PDF header identifies **v2, 16 May 2013**.

Theorem 2.18, printed pages 23–24, supplies the Haar central limit
theorem for totally ergodic actions and real mean-zero functions with
absolutely convergent Fourier series. The function class is defined on
page 16; footnote 3 includes the degenerate point-mass limit.
We use one generator and ordinary interval sums. Hyperbolicity verifies
total ergodicity; smoothness verifies Fourier convergence.
No Berry–Esseen rate or periodic-point CLT is imported.
Theorem 2.31, page 31, also gives the continuous-coboundary criterion
under polynomial Fourier decay of order greater than the torus dimension.

PDF SHA-256:
54f363fad81492e79684488d57e75321b414df004c07c2a6bbdfa15029ef9bd5.
Extracted text SHA-256:
e78124655b7ecf9f5e7cbc691ed2f8505d2fac5272bbbb72040f88926996ae9d.
The public source is retained in the ignored literature cache.

The centered-cell coupling and the even-period quantum comparison are
derived in [the working note](../mathematics/returns/periodic_point_trace_comparison.md).
The replica argument adapts the project's earlier finite unitary
normal form; it is not a newly claimed general averaging principle.
External priority and microscopic BGS universality remain unestablished.

## Related short-period work checked during the continuation

Robert Koirala, *Equidistribution of Eigenfunctions of Quantum Cat Maps*,
[arXiv:2605.06569v1](https://arxiv.org/html/2605.06569v1).
The HTML version accessed during the September 11–12 continuation
was inspected at its introduction and Theorem 1.1.
That theorem concerns smooth-observable expectations in a specified
short-period eigenfunction family, with an error of order $1/\log N$.
Its map assumptions include $\gcd(b,c)=1$.

The claims in [the general cat-map note](../mathematics/returns/general_cat_return_laws.md)
instead concern full normalized return traces and the empirical spectrum
of period-averaged observables. The eigenfunction theorem is neither
a proof input nor an equivalent statement of these claims.
Its complete proof has not been audited here.
This comparison with one related paper is not a comprehensive
literature search and does not establish priority.
