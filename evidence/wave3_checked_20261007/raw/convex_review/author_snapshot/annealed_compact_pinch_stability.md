# Annealed complete-pinch stability from compactness and the universal Abel bound

7 October 2026. **Author theorem candidate; independent review requested.** This companion does not assume an occupation-uniform right-frame overlap theorem. Its inputs are the separately accepted ordinary-operator-norm compactness of D_N in `actual_charge_radial_shell.md` C4, ordinary displacement-slice flatness, and the universal phase-pair Abel bound in `uniform_phase_pair_abel_bound.md` (A). The source checkpoint supplies their current acceptance status. No actual-map stationary-phase proof is repeated.

## 1. Statement and inputs

Retain U_N, T=Ad(U), D, T_z and C from the conditional convex resummation packet. Let

    V_theta=Ad(Z_theta),  W_theta=Z_theta U,
    T_theta=V_theta T=Ad(W_theta),  D_theta=V_theta D,
    M_theta(z)=z T_theta+(1-z)D_theta.

Here theta has the original N independent uniform coordinate phases and E_theta is its normalized average. Define the complete positive annealed correction

    F_theta,m(z)=Tr_H M_theta(z)^m-z^m |Tr W_theta^m|^2>=0.

Assume ||C||^2<=C0 uniformly. Assume that for every epsilon>0 there are an integer R_epsilon and a threshold such that, for all N beyond that threshold, D_N has an approximation D_N^(epsilon) with

    rank D_N^(epsilon)<=R_epsilon,
    ||D_N-D_N^(epsilon)||<=epsilon.                        (1)

This is an ordinary operator-norm finite-rank approximation on H_N. It follows from accepted norm convergence to a compact operator in a common Weyl embedding: approximate the compact limit by finite rank, and compress the approximation back to the embedded H_N. Multiplying by V_theta or by a contraction preserves both rank and tail bounds. No compactness uniform in theta is needed.

For every bounded w supported in a fixed [a,b] contained in (0,infinity), and every 0<=u_N<=U_*<infinity with z_N=1-u_N/N,

    (1/N^2)sum_m |w(m/N)| E_theta F_theta,m(z_N) ->0,
    (1/N^2)sum_m |w(m/N)| z_N^(-m) E_theta F_theta,m(z_N) ->0. (2)

The finitely many N with z_N<=0 may be discarded. This is a COMPLETE unmasked theorem. It does not estimate any Hamming/path mask. Combining it with the conditional right-frame theorem gives bounded-u stability of the COMPLETE signed occupation subtraction under weak switch noise, including bounded-u deconvolution. It does not close the prescribed large-logarithmic T16 boundary.

## 2. Quantitative finite-rank/tail inequality

Choose a fixed nonnegative smooth g compactly supported in (0,B), B>b, with g>=1 on [a,b]. Let G=||g||_infinity. Choose a fixed smooth chi with 0<=chi<=1, chi(t)=0 for t<=1, chi(t)=1 for t>=2. For 0<eta<1 put chi_eta(t)=chi(t/eta). There is a constant K_g depending only on g, chi and B, not on N,z,theta,p,eta, such that any approximation of rank <=R and tail <=epsilon<=1 in (1) gives, for 0<z<=1 and M=floor(BN),

    (1/N^2)sum_m g(m/N) z^(-m) E_theta F_theta,m(z)
       <=(z^(-M)-1) [C0 G(2eta+1/N)
                     +K_g R/N+K_g(1+eta^(-1))epsilon].    (3)

In particular for 0<epsilon<1 choose eta=sqrt(epsilon) to obtain the sufficient bound

    <=K_(g,C0)(z^(-M)-1)[R/N+sqrt(epsilon)+1/N].            (4)

For bounded u_N, z_N^(-M) stays bounded. Take N->infinity at fixed epsilon, then epsilon->0, to prove the second statement of (2); the first follows from positivity and z^(-m)>=1. This proof uses no rate in compactness.

For u_N=A0 log N, a separate quantitative rank/tail hypothesis sufficient for (4) would be

    R_N/N+sqrt(epsilon_N)+1/N=o(N^(-B A0)),                (5)

or, separating terms, R_N=o(N^(1-B A0)) and epsilon_N=o(N^(-2B A0)), together with B A0<1 for the displayed 1/N term. These conditions are NOT supplied by ordinary compactness. More importantly, for the required actual-family A0>2/(kappa a), the COMPLETE unsigned deconvolved correction really diverges by Section 6a of the main packet. Thus no estimate of this type can prove its vanishing in that window; a successful signed argument must first remove the common identity contribution and preserve cancellation. Formula (5) is a conditional sufficient regime for the full positive observable, not a proposed solution to T16.

## 3. First-pinch orientation, positivity and short coherent runs

For every theta the exact noncommutative identity gives

    F_theta,m(z)=d sum_(n+p=m-1) z^n
                   Tr_H[T_theta^n D_theta M_theta(z)^p],  d=1-z.

Every summand is nonnegative: the operators are mixtures of unitary conjugations. For each remaining Kraus word B, averaging the distinguished charge gives

    (1/N)sum_b |Tr(W_theta^n Z_theta V_b B)|^2
      =sum_c |Tr(W_theta^n Z_theta A_c B)|^2
      =||C* (B W_theta^n Z_theta)||^2<=N C0.              (6)

All factors in the last vector are unitary. This is a POINTWISE column-norm estimate, not a fixed-lag frame estimate. It holds for arbitrary theta, n, p and adjacent pinches.

After deconvolution, z^(-m)z^n=z^(-p-1). For each p there are at most ceil(2eta N)<=2eta N+1 terms with 1-chi_eta(n/N) nonzero. Bounding g by G and (6) by N C0, their entire normalized contribution is at most

    C0 G(2eta+1/N) d sum_(p=0)^(M-1) z^(-p-1)
       =C0 G(2eta+1/N)(z^(-M)-1).                         (7)

This includes the n=0 endpoint. No lower bound on another coherent run is imposed.

## 4. Smooth long-run kernel and its trace norm

For fixed p define the scalar Laurent polynomial (only nonnegative powers occur)

    f_p(lambda)=sum_(n>=0) a_p(n/N) lambda^n,
    a_p(t)=g(t+(p+1)/N) chi_eta(t).

The amplitude is smooth and compactly supported, with uniform bounds

    sum_n |a_p(n/N)|<=K_g N,
    integral |a_p''(t)|dt<=K_g(1+eta^(-1)).                 (8)

Indeed the chi_eta'' term has L1 norm O(eta^-1), while its first derivative has uniformly bounded L1 norm. Translating g by (p+1)/N changes no derivative bounds. Since chi_eta vanishes on a neighborhood of every nonpositive t, extending the sequence to all integers introduces no n=0 boundary term. Since g is smooth compactly supported, the upper-time endpoint also has no omitted summation-by-parts term.

Twice applying the finite-difference identity and using

    sum_n |Delta^2 a_p(n/N)|<=N^(-1) integral |a_p''(t)|dt

gives, for lambda=e^(i phi),

    |f_p(e^(i phi))|
       <=min{K_g N, K_g(1+eta^(-1))/(N|1-e^(i phi)|^2)}
       <=K_g(1+eta^(-1)) P_(exp(-1/N))(phi).               (9)

Here P_r(phi)=(1-r^2)/|1-r e^(i phi)|^2. The last inequality is a uniform elementary comparison with N/[1+N^2 sin^2(phi/2)]. It covers phi=0 by the first bound. Define F_p=f_p(T_theta) by the normal functional calculus. Then

    ||F_p||<=K_g N,
    ||F_p||_1<=K_g(1+eta^(-1)) Tr_H P_(exp(-1/N))(T_theta). (10)

The trace norm is on the N^2-dimensional Hilbert space H. This is not a claim that D converges in trace norm.

For r=exp(-1/N), the accepted universal Abel estimate gives exactly

    E_theta Tr_H P_r(T_theta)
       =N^2+2 sum_(j>=1) r^j E_theta |Tr W_theta^j|^2
       <=N^2+N(1+r)/(1-r)
       <=4N^2.                                           (11)

The Fourier series is absolutely convergent at finite N; Tr_H T_theta^j=|Tr W_theta^j|^2. The last inequality follows from coth(1/(2N))<=2N+1. Hence the expected trace norm in (10) is O(K_g(1+eta^-1)N^2), uniformly in p and all deterministic U_N. No independence between F_p and the remaining theta-dependent factor is used.

## 5. Rank/tail estimate and the limiting order

The long-run part of the deconvolved sum is exactly

    d sum_(p=0)^(M-1) z^(-p-1)
          E_theta Tr_H[F_p V_theta D M_theta(z)^p].

The orientation V_theta D is essential; the theta factors inside T_theta remain there and are handled by (11). Since M_theta is a convex combination of contractions, ||M_theta^p||<=1. Split D=D^(epsilon)+E. The finite-rank factor

    V_theta D^(epsilon) M_theta^p

has rank <=R and norm <=1+epsilon<=2. Thus its trace pairing has absolute value <=2 R ||F_p||<=2K_g R N. The tail pairing has absolute value <=epsilon ||F_p||_1, so (11) bounds its expectation by 4K_g epsilon(1+eta^-1)N^2. Sum the exact scalar weights

    d sum_(p=0)^(M-1) z^(-p-1)=z^(-M)-1.

After division by N^2 this gives the last two terms of (3); (7) supplies the first. All identities and interchange steps are finite before the single convergent Poisson Fourier series in (11).

At bounded u, the rigorous order is: fix epsilon and eta, use the corresponding fixed rank and threshold, let N->infinity; then let epsilon->0 with eta=sqrt(epsilon). One can equivalently take N first, epsilon second and eta third. There is no hidden rate in R_epsilon or the threshold.

## 6. Consequence for the complete signed offcharge observable

Let

    G_m(z)=Tr_H T_z^m-E_theta Tr_H M_theta(z)^m,
    G_m(1)=|Tr U^m|^2-E_theta |Tr W_theta^m|^2.

Then the exact identity is

    z^(-m)G_m(z)-G_m(1)
       =z^(-m)[F_(N,m)(z)-E_theta F_theta,m(z)].            (12)

Both complete corrections in brackets satisfy vanishing normalized bounded-u bands when the conditional RIGHT-frame hypothesis is combined with (2). Therefore (12) proves weak-noise stability of this complete signed observable for bounded u_N. The theta averaging is exactly the occupation projector, including repeated labels. No Hamming or high-switch cutoff has been inserted.

At the prescribed large-logarithmic window both positive deconvolved corrections diverge with the same leading identity contribution. Bounding them separately is invalid for T16; (12) does not estimate the cancellation of their centered remainders. Thus the strongest proved consequence here is bounded-u COMPLETE stability, with an explicit quantitative rank/tail sufficient regime and a sharp unsigned logarithmic obstruction.

## 7. Verification boundary

This companion's main analytical input is accepted norm compactness, not a new Schatten assertion. Its Poisson majorant and rank/tail proof are author-level until independent review completes. The exact controls in the main packet verify the finite first-pinch identities and show why occupation-uniform fixed-lag overlaps cannot be assumed; they do not verify compactness or this asymptotic theorem. Source hashes are recorded in `source_bindings.json`.
