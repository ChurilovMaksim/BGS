# Exact two-channel transmission, bounded eigenvector ratios and scalar delay

17 October 2026. Working derivation outside BGS. Author proof and self-review;
no independent review, formal certification, world-priority or BGS claim.
The identities below are finite-dimensional. The needed eigenvector limit
is NOT proved from the project's deterministic startup assumptions.

## 1. Objects and exact finite spectral averaging

Let U be ANY deterministic unitary N-by-N matrix, N>=2. Let
V=D U, D=diag(exp(i phi_a)), with independent uniform phases. Almost
surely V has simple eigenvalues; write its orthonormal eigenvectors psi_l
and weights w_la=|psi_l(a)|^2. Cases w_li=0 have weight zero below.

Open port i and put E={1,...,N}\{i}. With phases on E only define

    X_i=(I-D_E U_EE)^(-1) D_E U_Ei,
    H_i=U_ii+U_iE X_i, Q_i=1+||X_i||^2.                 (1)

All inverses exist almost surely: their determinant is a nonzero
multiaffine polynomial with constant coefficient 1, so its torus zero
set has measure zero. H_i is scalar unitary almost surely. Q_i is the
boundary angular delay of the complete scalar transfer function z H_i(z),
where all internal phases and the initial propagation are multiplied by z.

For every bounded Borel g on C^(N-1), exactly

    E_open g(X_i)
      = E_full sum_l w_li g((psi_l(a)/psi_l(i))_(a!=i)).   (2)

In particular, for j!=i, J_ij=|(X_i)_j|^2 and Y_ij=J_ij/(1+J_ij)
obey, for every bounded Borel f,

    E_open f(Y_ij)
      =E_full sum_l w_li f(w_lj/(w_li+w_lj)),              (3)

with zero contribution when both weights vanish. Also

    E_open f(Q_i/N)
      =E_full sum_l w_li f(1/(N w_li)).                   (4)

Proof of (2): condition on all phases except phi_i=alpha. On a simple
spectral branch, Feynman-Hellmann gives d theta_l/d alpha=w_li.
For a given theta, every eigenvector with psi_l(i)!=0 is proportional to

    (1, X_i(exp(-i theta))),

and the closure phase is uniquely fixed by
exp(i alpha) exp(-i theta) H_i(exp(-i theta))=1. Change variables from
alpha to theta on these branches with weight w_li. Eigenvectors
orthogonal to i contribute zero. Averaging the remaining phases makes
the law of X_i(exp(-i theta)) independent of theta, because multiplying
every internal phase by exp(-i theta) preserves their product Haar law.
Integration over theta therefore gives (2). This is a finite unitary
spectral-averaging argument, not an assumption that eigenvectors are Haar.

For (4), normalize the vector (1,X_i) to get w_li=1/Q_i. The delay
identity follows by differentiating the unitary colligation identity
z U (1,X_i(z))^T=(z H_i(z),D_E^* X_i(z))^T on the circle;
the terms involving the derivative of X cancel. With z=exp(i beta), it gives
-i conjugate(z H_i) d(z H_i)/d beta=1+||X_i||^2.

The simple spectral locus has full phase measure even for a nongeneric
starting U. Within any repeated eigenspace, compressed coordinate
rank-one forms give a positive spanning frame. A real diagonal
perturbation with successively separated coefficients on a spanning
subfamily has simple compression. Generic coefficients do this for all
finitely many repeated eigenspaces simultaneously. Hence the phase
discriminant is not identically zero, and its analytic zero set has
measure zero. Alternatively the weighted change of variables above may
be performed on its simple branches and extended by spectral measures.

## 2. The two-channel kernel

Retain i,j and eliminate all other ports first. Let the resulting unitary
S have entries a,b,c,d in that order and transmission

    T=|b|^2=|c|^2=1-|d|^2 in [0,1].

Eliminate j with its still-fresh uniform phase w. Solving its coordinate
equation gives

    (X_i)_j=w c/(1-d w),
    J_ij=T/|1-d w|^2,
    Y_ij=T/[2(1-sqrt(1-T)cos phi)].                       (5)

The phase of d is absorbed into uniform phi. At T=0 use J=Y=0 almost
surely; at T=1 use J=1,Y=1/2. These are the correct continuous weak
limits for the bounded variable Y, even though E[J|T>0]=1 is not
continuous at T=0.

For lambda>0, direct circle integration gives

    E[J/(lambda+J) | T=t]
       =sqrt(t)/sqrt(4lambda+(1-lambda)^2 t).             (6)

For each integer k>=1,

    E[Y^k | T=t]
       =t^(k/2) 2^(-k) P_(k-1)(1/sqrt(t)),              (7)

where P_r is the Legendre polynomial and the value at t=0 is the
continuous limit zero. Formula (7) follows by differentiating the
elementary integral of (a-b cos phi)^(-1) with respect to a. Its first
three instances are sqrt(t)/2, sqrt(t)/4, (3-t)sqrt(t)/16.

For 0<t<1 the conditional density of Y is

    k(y|t)=sqrt(t)/[pi y sqrt(4y(1-y)-t)],
    (1-sqrt(1-t))/2 < y < (1+sqrt(1-t))/2.                (8)

Thus transmission is related to bounded eigenvector ratios by an Abel
integral, not by replacing a random denominator with its expectation.
For an arbitrary transmission measure mu, formula (8) describes the
continuous part of its mixture; endpoint atoms use the conventions above.

## 3. Exact characterization of the uniform transmission law

Let K mu denote the law of Y obtained from a transmission law mu via (5).
Then K is weakly continuous and injective on probability measures on [0,1].
Moreover

    mu_n => Uniform[0,1]
      if and only if K mu_n => Beta(1,2),                (9)

where the latter density is 2(1-y) on [0,1].

Proof: integrating (8) against dt on [0,1] gives
pi^(-1)y^(-1) integral_0^(4y(1-y)) sqrt(t)/sqrt(4y(1-y)-t)dt
=2(1-y). For injectivity, (6) determines all transforms
integral sqrt(t)/sqrt(t+z) mu(dt), z>0. Expansion for large z determines
every half-integer moment integral t^(r+1/2)mu(dt), r>=0. The measures
sqrt(t)mu(dt) are therefore identical by polynomial approximation on
[0,1]. This determines mu on (0,1], and normalization fixes its atom at
zero. Weak continuity follows from (5), including its endpoint limits.
Every subsequential weak limit of mu_n must consequently be uniform
whenever K mu_n tends to Beta(1,2). Compactness proves (9).

Equivalently, (9)'s limiting transform is

    E[J/(lambda+J)] ->
      (1-lambda^2+2lambda log(lambda))/(1-lambda)^3,       (10)

with continuous value 1/3 at lambda=1. Every test here is bounded.
This characterization avoids divergent boundary-delay moments entirely.

For densities, an explicit inversion is available. Set h=4y(1-y) and
A(h)=pi y p_Y(y). Then

    A(h)=integral_0^h sqrt(t)/sqrt(h-t) mu(dt),
    integral_[0,t] sqrt(s) mu(ds)
       =pi^(-1) integral_0^t A(h)/sqrt(t-h) dh.           (11)

The second formula holds at continuity points 0<t<1 of the weighted
measure. It is the beta-integral identity followed by Fubini; right limits
recover interior atoms. Endpoint atoms at T=0 and T=1 are read separately
from the Y-atoms at 0 and 1/2. They are not represented by a density in (8).

## 4. A quantitative sufficient input from eigenvector intensities

For each normalized eigenvector set

    mu_l=N^(-1)sum_a delta_(N w_la),
    epsilon_N=E_full N^(-1)sum_l W1(mu_l,Exp(1)).         (12)

Every mu_l has EXACT mean 1, and epsilon_N<=2. Let nu_N be the law of
Y for a uniform ordered pair i!=j and the independent feedback phases.
Then

    W1(nu_N,Beta(1,2))
      <= [2N/(N-1)] epsilon_N + 1/[4(N-1)].              (13)

Consequently epsilon_N->0 proves the two-channel uniform transmission
law in (9). This is a conditional sufficient theorem; (12)'s limit is
NOT derived here from flat entries, the initial intensity gap, reversal
suppression or the previous growing-u scattering-entry CLT.

Proof of (13): put K_f(x,y)=x f(y/(x+y)), extended by zero at (0,0).
For a 1-Lipschitz f on [0,1] with f(0)=0, K_f is separately
1-Lipschitz in x and y. For smooth f this follows from

    partial_x K_f=f(r)-r(1-r)f'(r),
    partial_y K_f=(1-r)^2 f'(r), r=y/(x+y),

using |f(r)|<=r. Approximation gives the assertion for every such f.
Also |K_f|<=min(x,y). Coupling two independent copies therefore gives

    |integral K_f d mu_l^2 - integral K_f d Exp(1)^2|
       <=2 W1(mu_l,Exp(1)).

By (3), after averaging the distinct coordinate pair,

    E_nu_N f
      =E_full N^(-1)sum_l
         [N/(N-1) integral K_f d mu_l^2-f(1/2)/(N-1)].    (14)

For independent exponentials x,y, r=y/(x+y) is uniform and independent
of x+y, which has mean 2. Hence integral K_f d Exp^2 equals the Beta(1,2)
mean of f. The finite correction has size at most
E_Beta(1,2)|Y-1/2|/(N-1)=1/[4(N-1)]. Take the supremum over f.

It suffices that a typical eigenvector's empirical intensity measure
converge WEAKLY in probability to Exp(1): exact mean 1 upgrades this to
W1 convergence, and the deterministic bound W1<=2 gives (12). To see
the mean upgrade directly, integral(x-R)_+ d mu_l
=1-integral min(x,R)d mu_l; at the proposed limit the right side is e^-R.
Thus no independent uniform-integrability hypothesis is hidden here.
Convergence of the POOLED intensity law alone cannot replace the typical
eigenvector condition in this two-coordinate statement, because mu_l^2
occurs in (14).

## 5. Scalar delay and joint sensitivities under the same input

Equation (4), after uniform i-averaging, becomes the exact identity

    E_open f(Q_i/N)
      =E_full N^(-1)sum_l integral x f(1/x) mu_l(dx).      (15)

The limiting density for an intensity density p(x) is therefore

    p_delay(t)=t^(-3) p(1/t), t>0.                       (16)

The delay/intensity reciprocal relation is PRIOR physics; see the exact
source comparison below. The finite independent-coordinate-phase identity
(15) is proved above for this model, rather than imported with a different
perfect-coupling or sigma-model hypothesis.

Under (12) with epsilon_N->0, for a fixed number r of distinct uniform
internal marked labels,

    (Q_i/N,J_i,j1,...,J_i,jr)
       => (1/A,E_1/A,...,E_r/A),                         (17)

where A has Gamma(2,1) density a exp(-a), and the E_j are independent
Exp(1), independent of A. The normalized scalar delay has density
t^(-3)exp(-1/t). Each J has density 2/(1+j)^3, and Y=J/(1+J) has
Beta(1,2) law. In particular E J^2 is infinite in this reference law;
bounded observables are essential in the argument.

Proof: spectral averaging selects source coordinate i with weight w_li.
Its rescaled intensity therefore has the SIZE-BIASED limiting law
x exp(-x)dx. Finitely many other coordinates, sampled without replacement,
have independent Exp(1) limits conditional on a typical empirical measure.
The collision correction is O_r(1/N); integration of the source weight
uses the exact first moment and its tail control. The maps in (17) are
continuous at A>0. No finite positive moments of high delay powers are
needed. For the marginal in (15), even convergence of the pooled intensity
law with its exact first moment suffices.

## 6. Two-channel data alone lose delay information

This is a statement about the ratio transform of possible intensity
distributions, not a constructed phase-stationary unitary counterexample.
Let X have mean-one law F. Independent source/target intensities drawn
from F, with the source sampled with weight X, give a ratio J whose
Mellin moments are M(s)M(1-s), M(s)=E X^s, whenever finite.
Replacing F by its size-biased reciprocal law replaces M(s) by M(1-s)
and leaves this entire one-ratio law unchanged.

Explicitly compare

    F_1(dx)=exp(-x)dx,
    F_2(dx)=x^(-3)exp(-1/x)dx.                           (18)

Both have mean 1. Under either source-weighted model, J has the identical
density 2/(1+j)^3 and Y has Beta(1,2). For F_1, the normalized scalar
delay 1/X_source has inverse-Gamma(2,1) law; for F_2 it is Exp(1).
Thus the ratio data encoded by two-channel transmission do not determine
the scalar delay marginal in this abstract intensity model. A second
joint ratio distinguishes the two: its Mellin transform is
M(s)M(t)M(1-s-t), which is not invariant under that reciprocal operation.

No claim is made that F_2 occurs for every eigenvector of a unitary phase
ensemble with the physical startup conditions. Its role is to prevent a
false implication from the one-ratio transform to the joint clock law.

## 7. Source boundary and actual remaining obligation

Rank-one spectral averaging and Poisson kernels are established mathematics.
Ossipov--Fyodorov, Phys. Rev. B 71,125133 (2005), arXiv:cond-mat/0411576v2,
equations (10)--(11), already state the scalar delay/intensity reciprocal
density relation. Their derivation discusses perfect coupling and the
nonlinear-sigma-model setting. This note does not claim that relation as new.
The present finite phase-model proof and the bounded two-channel mixture,
its inversion and the explicit W1 estimate have their own stated scope.
No world-priority verdict follows from a limited search.

Gnutzmann--Keating--Piotet, arXiv:1005.1026, derive eigenfunction statistics
through a saddle calculation. Their sections 7--8 explicitly distinguish
truncated correlations and Gaussian massive-mode approximations; their
stated full-universality criterion is conjectured. That source is not
used as an established theorem proving (12) for the present frozen core.

The concrete new target for the random-feedback subproblem is now (12),
or the still weaker direct bounded ratio condition (3),(9). The earlier
Gaussian limit for scattering entries at growing retained dimension does
NOT prove eigenvector intensity statistics of D U. Conditional eigenvector
overlaps at nearby energies, the microscopic radial law, frozen-phase
de-averaging and the original all-order BGS hierarchy remain open.
