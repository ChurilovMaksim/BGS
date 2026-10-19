# Consolidated all-moment window and positive-clock proof

17 October 2026. Review and continuation outside BGS. The linear-k upper
bound is ALREADY present in attachment lines 1202--1266. Its final QC7
appendix unnecessarily uses k^2 instead. This note consolidates the sharper
bound, proves it independently from clock positivity, and states the improved
joint regime. No evaluation of the remaining window mass is asserted.

Let S in U(N), A any nonempty retained set, E=A^c, r=|E|. Its Schur transfer
F_A(Z) is a contractive holomorphic matrix on the polydisk with unitary
boundary values almost everywhere. For a fixed entry f=F_ab and integer k>=1,
write

    f(Z)^k=sum_alpha c_alpha^(k) Z^alpha,
    q_L^(k)=sum_(|alpha|=L)|c_alpha^(k)|^2.

## Exact degree bound

For every finite unitary input, including cases with dark internal states,

    sum_(L>=1) L q_L^(k)<=k r.                          (1)

One proof is rational degree plus the area formula, given in the attachment.
Here is an independent proof from the positive matrix clock. Fix internal
relative phases and let G(z)=F_A(z Lambda). This is a rational inner matrix.
On the circle set

    H(theta)=-i G(e^(i theta))* dG(e^(i theta))/dtheta.

The unitary-colligation kernel identity gives H(theta)>=0. If the colligation
has an unobservable unitary part, remove that reducing part; it cancels out
of G. The resulting rational inner function is smooth on the circle and

    integral Tr H(theta) dtheta/(2pi)
      =degree(det G)<=r.                               (2)

Let g(z)=G_ab(z). For an analytic scalar function smooth on the closed disk,
boundary Parseval yields

    D(g^k)=integral conjugate(g^k) z(g^k)' dtheta/(2pi)
          =k integral |g|^(2k-2) conjugate(g) z g'
                   dtheta/(2pi),

where D is sum_L L |Taylor coefficient_L|^2, a real nonnegative number.
Since zG'=G H on the circle, G is unitary and H>=0,

    |z g'|<=||G H||op=||H||op<=Tr H,
    |g|<=1.

Taking the modulus of the integral therefore proves D(g^k)<=k r. Average
over the relative phases; character orthogonality separates all multiindices
of the same total degree. This proves (1). Complete escape, flatness and
either spectral gap are unnecessary for this upper bound.

## Low-degree bound and the sharpened window

Suppose max|S_ij|^2<=C0/N. For distinct external a,b, grouping paths by their
internal occupation vectors and Cauchy--Schwarz give

    sum_(l<=L)q_l^(1)<=(C0/N) sum_(l=0)^L l!.

The Hardy projection identity
Pi_<=L(f^k)=Pi_<=L[(Pi_<=L f)f^(k-1)] and |f|<=1 imply the same bound
for EVERY integer k>=1, with no k-dependent factor. Combining it with (1),
for 0<=L_-<L_+,

    0<=E|f|^(2k)-sum_(L_-<l<=L_+)q_l^(k)
      <=(C0/N)sum_(l=0)^L_- l! + k(N-|A|)/L_+.          (3)

For two channels, L_-=floor((1-delta)log N/loglog N) and
L_+=ceil(N log N), this gives uniformly for 1<=k<=K_N,

    error <=N^(-delta+o(1))+K_N/log N ->0
       whenever K_N=o(log N).                         (4)

The attachment's final appendix stated only K_N=o(sqrt(log N)) because
it reverted to k^2. Equation (4) uses its stronger earlier result together
with its later k-independent low-frequency projection argument. The fixed-k
claims remain valid; the change strengthens and synchronizes their scope.

## Quantitative radial moment bias

For 0<=rho<1, uniform phase Z, the same positive coefficients also give

    0<=E|f(Z)|^(2k)-E|f(rho Z)|^(2k)
       =sum_L (1-rho^(2L))q_L^(k)
       <=2k r(1-rho).                                 (5)

The corresponding amplitude error is

    E|f(Z)^k-f(rho Z)^k|^2<=k r(1-rho).                 (6)

Indeed, (1-rho^L)^2<=L(1-rho). These are unregularized-to-radial bounds
at the exact microscopic scale: a regulator must satisfy
k N(1-rho)->0 to make (5) vanish. They do not justify replacing a
mesoscopic regulator by the boundary value without an additional estimate.

The still missing theorem is evaluation of the positive window mass in
(3) as 1/(k+1), not its existence or truncation. The signed interference
inside each occupation coefficient remains uncontrolled on lengths O(N).
