> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round3_2026_10_21/arithmetic_flat_packet_obstruction_test.md`. Embedded SHA256: `58bcfa0d7db85583d23f16c8ab1e5327926e11221b102cb7c6d0128037abb1cc`.
> [Thematic guide](../../topics/arithmetic.md).

# Growing flat packets: an executed obstruction test

Date: 21 October 2026. Scope: the exact original matrices, all odd dimensions,
and the unaltered `tau=10^(-80)`.

## 1. Candidate and outcome

The candidate was to build many nearly stationary vectors from the weak
Jacobi couplings near their zeros, especially along `N=7^r`. If those vectors
were quasimodes of the full `U_N` with a common phase and width `o(1/N)`, a
packet of order `sqrt(N)` could affect a fixed factorial statistic.

The coordinate-packet version fails for a concrete reason: the original
metaplectic matrix transfers such a packet almost orthogonally to itself.
The estimate below proves that for every packet size `W=o(sqrt(N))`, every
unit vector supported in the indicated union of flat regions has

$$
\inf_{|\lambda|=1}\|(U_N-\lambda)v\|\ge\sqrt{2-o(1)}.
\tag{1.1}
$$

This is a uniform norm statement, not merely an exclusion of algebraic
eigenvectors. It does not exclude spectral clusters with delocalized
eigenvectors, or canonical arithmetic comb packets.

The proof uses only the matrix definitions and the coordinate formula (1.1)
of `arithmetic_seven_chain_cut_stability.md`, whose frozen SHA-256 is
`d6ddc0695d91441729852ea5fc89d6318a1297b22eb4837cd5d3e0c930c3d349`.
That formula is rechecked by the two Fourier modes `l=+1,-1`; no trace
foundation or universality input is used here.

## 2. All eight quadratic zeros and the packets

The hopping magnitude is

$$
|w_x|=r((x+h_N)/N)/200,\qquad h_N=(N+1)/2.
$$

The zero set of `r` on the circle is

$$
Z=\{0,1/7,2/7,3/7,1/2,4/7,5/7,6/7\}.
\tag{2.1}
$$

The point `1/2` is never on an odd grid, but is relevant for small hopping.
Every zero is quadratic. For `z=j/7`,
`r(z+u)<=196 pi^2 u^2`; for `z=1/2`,
`r(z+u)<=4 pi^2 u^2`. Thus the former, coarser bound applies to all eight.

For each `z` choose a nearest integer `y_z` to `Nz`; at `1/2` either choice
is permitted. Set `x_z=y_z-h_N mod N`, so
`|y_z-Nz|<=1/2`. For a positive integer `W`, let `P=P_(N,W)` be the coordinate
projection onto

$$
J_{N,W}=\bigcup_{z\in Z}
 \{x_z-W+1,\ldots,x_z+W\}\pmod N.
\tag{2.2}
$$

For `W=o(N)`, these eight intervals and their two boundary edges are disjoint
for sufficiently large `N`. The projection has exact rank `R=16W`.

The boundary edges of each interval are at `x_z-W` and `x_z+W`. Their
coefficients satisfy

$$
|w_{x_z\pm W}|\le\frac{49\pi^2}{50N^2}(W+1/2)^2.
\tag{2.3}
$$

The commutator `[A_N,P]` consists only of these edges, arranged into disjoint
skew-Hermitian two-by-two blocks. Hence

$$
\|[A_N,P]\|\le\frac{49\pi^2}{50N^2}(W+1/2)^2.
\tag{2.4}
$$

## 3. One-step survival and the quasimode lower bound

Let `E_N=exp(i tau N A_N)`. Duhamel differentiation gives

$$
\|[E_N,P]\|\le\tau N\|[A_N,P]\|.
$$

Using `P E_N M_N P=E_N P M_N P+[P,E_N]M_NP`, and the exact modulus
`|(M_N)_(xy)|=N^(-1/2)`, gives

$$
\begin{aligned}
\|P U_NP\|
&\le\|P M_N P\|+\|[P,E_N]\|\\
&\le\|P M_N P\|_{\rm HS}
 +\tau N\|[A_N,P]\|\\
&\le\frac{16W}{\sqrt N}
 +\frac{49\pi^2\tau}{50N}(W+1/2)^2
=:\rho_{N,W}.
\end{aligned}
\tag{3.1}
$$

There are `R^2` entries in `PM_NP`, explaining the Hilbert–Schmidt norm
`R/sqrt(N)`, not `sqrt(R/N)`. For a unit vector `v` in the range of `P`,

$$
\|(U_N-\lambda)v\|^2
=2-2\operatorname{Re}(\overline\lambda\langle v,U_Nv\rangle)
\ge2-2\rho_{N,W},\quad |\lambda|=1.
\tag{3.2}
$$

This proves (1.1) whenever `W=o(sqrt(N))`. At `W=c sqrt(N)+O(1)`, it gives
the still nontrivial fixed lower bound

$$
\liminf\inf_{v\in\operatorname{ran}P,\ \|v\|=1}
\inf_{|\lambda|=1}\|(U_N-\lambda)v\|^2
\ge2-32c-\frac{49\pi^2\tau}{25}c^2
\tag{3.3}
$$

whenever its right side is positive. A single chosen packet has `2W` in place
of `16W` in (3.1), so the same test applies to a wider individual packet.

No truncation of the exponential has been used. The commutator estimate
allows its physical time `tau N` to grow without bound.

## 4. A growing cutting window with the same local law

Delete every edge `x_z+v`, `-W<=v<=W`, around every zero in (2.1), and call the
resulting Hamiltonian `A_N^[W]`. The deleted edge sets are disjoint as sets
for large `N` if `W=o(N)`, but neighboring edges within each set need not
have disjoint vertex pairs. The triangle inequality for the trace norm and
the maximum row-sum bound for the operator norm nevertheless give

$$
\begin{aligned}
\|A_N-A_N^{[W]}\|_1
&\le\frac{16C_*}{N^2}
 \sum_{v=-W}^{W}(|v|+1/2)^2
\le\frac{16C_*}{N^2}(2W+1)(W+1/2)^2,\\
\|A_N-A_N^{[W]}\|
&\le\frac{2C_*}{N^2}(W+1/2)^2,
\qquad C_*:=49\pi^2/50.
\end{aligned}
\tag{4.1}
$$

These are respectively `O(W^3/N^2)` and `O(W^2/N^2)`.
Define `U_N^[W]=exp(i tau N A_N^[W])M_N`. The eigenphase path argument in the
frozen cutting note applies verbatim, so for fixed nonnegative
`f in C_c^1(R)` its local Laplace functional changes by at most

$$
\frac{\tau N}{2\pi}
\|A_N-A_N^{[W]}\|_1\,\|f'\|_1
=O_f(\tau W^3/N).
\tag{4.2}
$$

Consequently, for **every** integer sequence `W_N=o(N^(1/3))`, the growing
cut family and the original family have exactly the same possible local
weak limits. This retains the fixed `tau`; it does not replace it by a
dimension-dependent parameter.

The maximum microscopic displacement supplied by the same argument is only
`O(tau W_N^2)`. It need not be bounded. The full `H_diag` transfer theorem
with a single fixed majorant therefore does not automatically apply to
this growing modification. Equation (4.2) is a statement about bounded
Laplace observables, not unbounded factorial moments.

All coordinates in (2.2) are isolated for `A_N^[W]`, so they form an exactly
invariant diagonal subspace of that Hamiltonian. Nevertheless

$$
\|P U_N^{[W]}P\|=\|P M_NP\|\le16W/\sqrt N.
\tag{4.3}
$$

Thus even these exactly isolated growing Hamiltonian pieces do not produce
quasimodes of the full cut propagator when `W=o(sqrt(N))`. Equations
(3.1)–(4.3) rule out the proposed coordinate-flat-packet construction in
the full window `W=o(N^(1/3))` that preserves local Laplace laws.

## 5. Remaining arithmetic comb candidate and its exact unproved step

The preceding norm estimate cannot be applied to a canonical oldspace.
Along

$$
N_r=7^{4r},\qquad d_r=7^r,\qquad m_r=7^{2r}=\sqrt{N_r},
$$

the canonical oldspace has rank `m_r` and consists of vectors supported on
the multiples of `d_r`, periodic under shift `N_r/d_r`. The exact identity
`M_(N_r) J_r=J_r M_(m_r)` makes it invariant under `M_(N_r)`.
Its projection is not a small coordinate support projection, so the
Hilbert–Schmidt estimate (3.1) would be irrelevant.

The previous exact oldspace theorem proves
`H_old intersect U_(N_r) H_old={0}` at each finite `r`, and a generator
leakage bound. It does not give a uniform angle at the time `tau N_r`.
The previously checked uniform divisor estimates cover
`d<=N^(1/4096)`, whereas here `d=N^(1/4)`; their hypotheses do not cover
this sequence.

One necessary new estimate for a near-invariant comb construction would
therefore concern

$$
\|P_{d_r,N_r} e^{i\tau N_r A_{N_r}}P_{d_r,N_r}\|.
\tag{5.1}
$$

No bound away from one, or construction forcing this norm to approach one,
has been proved here. Even a near-invariant space would not by itself give
a spectral microcluster; it would still need a common eigenphase with error
`o(1/N_r)` on a sufficiently large subspace. Generator leakage, finite
nonintersection, and fixed-divisor mean escape do not supply either claim.

Thus this executed branch has ruled out coordinate packets quantitatively
and isolated the actual missing archimedean estimate for comb packets. It
has not produced fixed `k,b,epsilon` and an infinite discrepancy sequence,
and it has not established `H_diag`.
