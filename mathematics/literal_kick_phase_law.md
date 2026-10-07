# Literal kick-phase law and post-wrapping cat-comparison obstruction

Author proof candidate, 7 October 2026. Base repository commit
`d37c92e563d10d25bb1d6ab85bedffc1f160f773`; exact inputs and their hashes
are frozen in `inputs/` and `manifest.json`. No canonical files changed.

The original deterministic BGS target TRACE-005 remains open. This is an
actual-model theorem excluding a specific arithmetic-resonance explanation,
not a counterexample to that target. It supplies the fixed-strength,
post-wrapping analogue of FM-005's pre-wrapping approximate-rank bound.

## 1. Exact target and statement

Keep the prescribed raw modular Weyl quantization, odd positive dimensions,
centered actual generator A_N, and literal fixed tau=10^(-80). Set

    Q_N = exp(i tau N A_N),       U_N = Q_N M_N.

The ordinary midpoint symbol of A_N is exactly

    r(q) = (1-cos(14 pi q))(1+cos(2 pi q)),
    g(q,p) = cos(14 pi q)+r(q)/10+r(q)sin(2 pi q)/100-1/10
             +r(q+1/2)cos(2 pi p-alpha)/100,
    cos(alpha)=-3/5, sin(alpha)=4/5.

In particular the ordinary half-shift is retained. Write ||X||_N for
(N^(-1)Tr(X*X))^(1/2). No hypothesis about U_N spectral simplicity is used.

**Theorem K1.** For every fixed nonzero integer m,

    N^(-1) Tr(Q_N^m) -> 0.                                      (K1)

Consequently the empirical eigenphase measure of Q_N converges weakly to
uniform probability on the circle. This holds through all odd N, including
every seven-divisible subsequence, at the unchanged fixed tau. There is no
rate uniform in m or effective startup assertion.

**Theorem K2.** Uniformly in scalar phases z with |z|=1, the empirical
singular-value distribution of U_N-z M_N converges to the chord distribution

    F(s) = (2/pi) arcsin(s/2),   0 <= s <= 2.                   (K2)

The convergence is uniform both in z and in s. In particular

    inf_(|z|=1) ||U_N-z M_N||_N -> sqrt(2),
    inf_(|z|=1) ||U_N-z M_N||_op -> 2.                         (K3)

More precisely, for integers 0<=r_N<N with r_N/N -> rho in [0,1),

    inf_(rank R<=r_N) ||U_N-z M_N-R||_N^2
        -> 2(1-rho)-(2/pi)sin(pi rho),                         (K4)

    inf_(rank R<=r_N) ||U_N-z M_N-R||_op
        -> 2 cos(pi rho/2),                                   (K5)

uniformly in |z|=1. Thus any rank-o(N) correction leaves exactly the same
limits sqrt(2) and 2. Conversely, to achieve error tending to zero in either
of these norms, the correction's rank must be N-o(N).

This is a direct comparison with the prescribed M_N. It says nothing about
arbitrary N-dependent conjugates of M_N, other comparison operators, or
the statistics of U_N itself.

## 2. No nonzero time of the actual Hamiltonian flow is the identity

Let X_g=(g_p,-g_q), and let Phi_g^s be its complete real Hamiltonian flow on
the torus. The flow exists for all real s because the vector field is smooth
on a compact manifold. For each fixed s it is real analytic in its initial
point: local analytic flow charts compose over any finite time interval.

At P=(0,0), direct differentiation of the displayed physical symbol gives

    dg(P)=0,
    Hess g(P)=diag(b,0),         b=-(19606/125) pi^2 != 0.       (K6)

This is also the first of the four exact Hessians in FM-001. For clarity,
cos(14 pi q) contributes -196 pi^2; r''(0)/10 contributes
196 pi^2/5; r(q)sin(2 pi q)/100 has zero second derivative at zero;
r(q+1/2)'' at zero equals 8 pi^2, and its coefficient at p=0 is
(-3/5)/100. Their sum is (-196+196/5-6/125)pi^2.
Both mixed and p-p derivatives vanish there. Therefore

    B := DX_g(P) = [[0,0],[-b,0]],      B^2=0, B!=0.

Because P is an equilibrium, its exact flow derivative is

    D Phi_g^s(P)=exp(sB)=I+sB.                                (K7)

For every real s!=0 this differs from the identity. Hence Phi_g^s is not
the identity torus map for any nonzero real s. Notice that this is an exact
all-real-time argument, not a small-s expansion or a bound valid only while
tau N is small.

For any fixed s!=0, let a_1,...,a_4 be the embedding coordinates
cos(2 pi q), sin(2 pi q), cos(2 pi p), sin(2 pi p). The function

    f_s(x)=sum_j [a_j(Phi_g^s(x))-a_j(x)]^2

is real analytic, nonnegative, and not identically zero by (K7). Its zero set,
which is exactly Fix(Phi_g^s), has area zero. The elementary analytic fact
used here follows by applying the one-variable identity theorem to slices
and induction/Fubini on analytic coordinate charts; no uniform quantitative
sublevel estimate is asserted.

## 3. Actual quantum Egorov for each fixed flow time

Put Op_N(g)=A_N in the exact midpoint convention and

    V_N(s)=exp(i 2 pi s N A_N).

The finite Fourier support of g and the exact Weyl multiplication formula
give, for each smooth a,

    i N[A_N,Op_N(a)]
       = Op_N(X_g a/(2 pi)) + O_op(N^(-2)||a||_(H5)).           (K8)

The third-order sine remainder proves this estimate, with a constant
depending only on the fixed g. Duhamel, using the finite Sobolev growth of
composition by Phi_g^s over a fixed compact real time interval, gives

    V_N(s)* Op_N(a) V_N(s)
       = Op_N(a composed with Phi_g^(-s))+o_op(1).             (K9)

The sign agrees with the maintained convention; only the fixed-point set
will matter below. For each fixed s the error tends to zero. The constants
may grow with |s|, which does not affect the fixed-moment conclusion.
The symbol product law and normalized Hilbert-Schmidt law are

    Op_N(a)Op_N(c)=Op_N(ac)+o_op(1),
    ||Op_N(a)||_N^2 -> integral |a|^2.                         (K10)

Both follow by finite Fourier truncation, exact Weyl phases, and smooth
Fourier tails. All limits are on the actual odd-dimensional matrices.
These are the already maintained FM-016 overlap inputs and FM-018 sine
calculus; this note does not assume a Heisenberg-time Egorov estimate.

## 4. Trace overlap, with the cutoff limit in the right order

We include the fixed-time deduction to state precisely what is inherited.
Let V_N quantize Phi_g^(-s), with s!=0 fixed. Define

    t_N(c)=N^(-1)Tr(V_N Op_N(c)),
    b_j=a_j composed with Phi_g^(-s)-a_j,
    f=sum_j b_j^2.

Egorov, cyclic trace, and (K10) give t_N(c b_j)=o(1) for every fixed
smooth c. For epsilon>0 fixed choose smooth chi_epsilon(f), equal to one
near f=0 and supported where f<=2epsilon. Away from f=0,

    1-chi_epsilon(f)=sum_j c_(j,epsilon) b_j,
    c_(j,epsilon)=(1-chi_epsilon(f)) b_j/f,

and each c_(j,epsilon) extends smoothly by zero. Thus
t_N(1-chi_epsilon(f))->0 at each fixed epsilon. Since V_N is unitary,

    limsup_N |t_N(1)| <= ||chi_epsilon(f)||_(L2).

Let epsilon decrease to zero after N tends to infinity. The right side
tends to zero because Fix(Phi_g^(-s)) has area zero, proved in Section 2.
Hence N^(-1)Tr V_N(s)->0 for every fixed real s!=0.

Finally Q_N^m=V_N(m tau/(2 pi)). Every fixed nonzero integer m supplies a
fixed nonzero real flow time, so (K1) follows. Fourier approximation on
the circle then proves its stated weak eigenphase law. This last passage
uses one fixed Fourier moment at a time, not a growing-power trace bound.

## 5. Uniform arcs and the complete approximate-rank law

Write the Q_N eigenvalues as exp(i theta_j). Weak convergence to the
continuous uniform measure implies uniform discrepancy over circular arcs:

    sup_(circular arcs I) |N^(-1)#{theta_j in I}-|I|/(2pi)| ->0. (K11)

One elementary proof chooses a finite equally spaced mesh and uses weak
convergence at its endpoints; each arc lies between mesh arcs differing by
at most two cells. First let N grow for the fixed mesh and then refine it.
Endpoints, including multiplicities at endpoints, cause no issue because
the limit measure has no atoms. This proves K11 for open or closed arcs.

Right multiplication by M_N* preserves singular values and rank. Since
Q_N is normal, the singular values of U_N-zM_N are exactly
|exp(i theta_j)-z|. For |z|=1, the event that this is at most s is a circular
arc of length 4arcsin(s/2) when 0<=s<=2. K11 proves K2 uniformly in z,s.

Let 0<=s_(1,N)(z)<=...<=s_(N,N)(z) be the increasing singular values.
Uniform convergence of their distribution functions to the continuous,
strictly increasing F gives uniform quantile convergence on compact
subintervals of (0,1). The endpoints are controlled by boundedness 0<=s<=2
and by the positive limiting mass of every fixed neighborhood of 0 or 2.
Consequently (with r_N/N->rho<1), uniformly in |z|=1,

    s_(N-r_N,N)(z) -> F^(-1)(1-rho)=2cos(pi rho/2),
    N^(-1)sum_(j<=N-r_N) s_(j,N)(z)^2
        -> integral_0^(1-rho) [2sin(pi u/2)]^2 du
         = 2(1-rho)-(2/pi)sin(pi rho).                         (K12)

The finite-dimensional singular-value variational principle identifies
the first expression with the best rank-r_N operator-norm residual and
the second with its best squared normalized HS residual. It can be proved
directly by truncating an SVD for the upper bounds and using a kernel
dimension argument / the min-max principle for the lower bounds. Thus
no hypothesis on how R depends on N or z is used. This proves K4-K5.

Their rho=0 case includes K3. If an error tends to zero but rank(R_N)/N
does not tend to one, pass to a subsequence with ratio bounded by a fixed
rho<1; the strictly positive K4 or K5 lower bound is a contradiction.

## 6. Scope, prior attribution, and remaining route

The semiclassical overlap argument is inherited from FM-016. The concrete
new application is that the nilpotent equilibrium forbids every nonzero
global period of the actual integrable kick flow, giving all fixed kick
moments and the uniform singular-value/approximate-rank formulas after
wrapping. The exact raw-symbol Hessian is an FM-001 input. FM-005 already
excluded exact low-rank correction and controlled a finite pre-wrapping
range. No general-method or external-priority claim is made.

This eliminates a direct infinite-subsequence mechanism in which the
literal kick rephases near a scalar and leaves U_N close to its arithmetic
cat factor, even modulo a subextensive-rank correction. It does not exclude
near-scalar behavior on selected low-dimensional subspaces; a dense
operator can have special vectors. It does not exclude hidden microscopic
spectral clusters, N-dependent conjugacy to a cat-like model, or an exact
quantum antiunitary constructed in U_N's own eigenbasis.

In particular macroscopic kick equidistribution is not microscopic BGS for
the product Q_N M_N. TRACE-005's complete signed factorial Fourier sums,
at powers of order N and with modulus outside the whole sum, are unchanged
and open. No model, coupling, quantization, averaging, or normalization has
been substituted.
