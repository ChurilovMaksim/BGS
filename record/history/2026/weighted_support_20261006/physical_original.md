# Physical homoclinic phase and the actual leading-weight dictionary

6 October 2026. Author candidate, requires independent review. No canonical
edits. Coupling, quantizer and phase conventions are unchanged. The exact
finite-h box factor is displayed and is not silently discarded.

## 1. Exact leading transport and cyclic Hill identity

At a real stationary orbit write, for the actual one-step generating phase,

 a_j=-S_xx, b_j=S_xy, c_j=-S_yy.

All b_j are positive at the prescribed tiny time. The linearized forward
map, defined by p=S_x(x,y), P=-S_y(x,y), is

 M_j=[[a_j/b_j,1/b_j],[(a_j c_j-b_j²)/b_j,c_j/b_j]], det M_j=1.        (W1)

Let M=M_(m-1)...M_0. The cyclic Hessian K has edge contributions a_j and c_j
on the endpoint diagonals and -b_j on both off-diagonal entries. Then

 det K=(tr M-2) product_j b_j.                                      (W2)

For m=1 this reads a+c-2b=b(tr M-2). For m=2 both off-diagonal edge
contributions add; they are not treated as distinct matrix positions.
A proof for every m uses a Floquet multiplier z in the cyclic boundary
condition. The determinant is C-(product b_j)(z+z^-1), directly by the two
cyclic permutation terms (the same identity holds for m=1,2 with the stated
combined entries). Its zero set is precisely det(M-zI)=0, since the Jacobi
recurrence is equivalent to W1. Comparing coefficients gives W2 at z=1.

The actual leading transport is exactly a_(r,0)(tau,x,y)=2 sqrt(S_(r,xy)).
Indeed differentiation of the HJ equation yields, for b=S_xy,

 b_t=(g_p/(2*pi)) b_x +(g_qp+g_pp S_xx)b/(2*pi).

The square root solves the leading WKB transport
(a0)_t=(g_p/(2*pi))(a0)_x +(g_qp+g_pp S_xx)a0/(4*pi),
and agrees with a0=1 at b=1/4. This uses the actual Weyl symbol, whose
subprincipal term is zero in the frozen transport recursion.

After factoring e(NDelta_m) from the paired-identity coefficient alpha,
its leading stationary factor is therefore

 w_(0,m)(z)=sqrt(D_m) 2^-m product a0 / sqrt(det K)
           =sqrt(D_m/|det(I-DF^m(chi(z)))|).                          (W3)

Here F=G_(tau/(2*pi)) is the actual classical map and chi is the bounded
stationary conjugacy described next. Absolute values in W3 retain the sign:
tr M>2, while det(I-M)=2-tr M<0.

Exact rational controls in check_hill_weight.py verify W1–W2 for m=1,...,12
and seven unrelated rational edge arrays per m. They test the algebra, not
replace the all-m Floquet proof.

## 2. The physical stationary conjugacy and leaf-intersection formula

The s=0 stationary construction gives

 chi(z)=(q+u(z), S_(0,x)(tau,q+u(z),3q+4p+u(Sz))) mod Z².             (W4)

The Euler equation implies F chi=chi S. Integer gluing makes W4 periodic
as a torus map. It is uniformly close to the identity. If chi(z)=chi(w),
choose lifts so the equality holds on R². The conjugacy equation and bounded
corrections make S^j(z-w) bounded for all integers j, forcing z=w. Degree one
(or invariance of domain and compactness) gives surjectivity. Thus W4 is the
actual near-identity structural homeomorphism, not an assumed smooth one.

There is a useful regularity distinction. In eigen-coordinates of S, the
actual F and F^-1 differ from diag(lambda,lambda^-1) and its inverse in C³
by at most delta=10^30 tau=10^-50. This conservative bound follows from the
published characteristic ODE derivative bounds through order three, the
fixed linear coordinate changes and |tau/(2*pi)|<tau.

The unstable slope graph transform is

 v(x)=[c(y)+d(y)v(y)]/[a(y)+b(y)v(y)], y=F^-1 x,                     (W5)

where DF in those coordinates is [[a,b],[c,d]]. In a C^(1,1/2) ball about zero,
the constant-map linear contraction is lambda^-2 lambda^(3/2)=lambda^-1/2
<0.415. Differentiating the displayed rational expression once and taking
one half-Holder difference changes this by at most 10^12 delta on the ball
||v||_(C^(1,1/2))<=10^8 delta: denominators exceed 5, inverse derivative norms
are below 6, and every nonconstant coefficient derivative through order two
is O(delta). The forcing norm is below 10^6 delta. Thus the transform maps
that ball into itself and has contraction constant below 1/2. The stable
transform for F^-1 is identical with coordinates interchanged.

Consequently both physical slope fields are C^(1,1/2), with distance at most
10^10 delta from the constant slopes +1/sqrt(2) and -1/sqrt(2). These are
physical bundle/foliation bounds; they assert no C1 regularity of chi.
The numerical constants above deliberately dominate the finite product and
chain-rule factors; the source ODE bounds are global because the symbol is
periodic.

Let p_u(Q;x) and p_s(Q;x) be the lifted unstable and stable leaf graphs through
physical x=(q,p), normalized to equal p at Q=q. On |Q-q|<=2 they solve the
ordinary differential equations given by those slope fields. Differentiating
the ODE and using Gronwall gives C^(1,1/2) closeness, with constant at most
10^22 delta, to p±(Q-q)/sqrt(2), including dependence on the initial x.
For 0<=s<=1 the equation

 p_u(Q_s;x)-p_s(Q_s;x)=s                                             (W6)

has a unique solution near q+s/sqrt(2), with
||Q_s-q-s/sqrt(2)||_(C^(1,1/2))<=10^25 delta, uniformly in s.
The derivative in Q in W6 is sqrt(2)+O(delta), so this is the quantitative
implicit-function theorem on a fixed interval, not a long-time differentiation.

The stationary source-s chain lies on the unstable leaf of chi(z) in the
past and the stable leaf in the future: its difference from the zero-source
chain decays exponentially in both time directions by the weighted inverse.
The Euler equation at site zero says p^- - p^+=s. Therefore its central
position is EXACTLY Q_s(chi(z)). It follows that

 B(x):=H_tau(chi^-1 x)=integral_0^1 Q_s(x)ds-1/(2sqrt(2)),
 ||B-q||_(C^(1,1/2))<=10^25 delta,  partial_q B>=1/2.                (W7)

The physical homoclinic map corresponding to d=(1/sqrt(2),-1/2) is

 Psi_d(x)=(Q_1(x),p_s(Q_1(x);x)) mod Z²=chi R_d chi^-1(x).            (W8)

At s=1 the two momenta differ by an integer, so the broken lifted orbit is
one genuine torus orbit. W8 is C^(1,1/2)-close to translation by d; its
Jacobian J_d is positive, C^(0,1/2), and uniformly close to one.

## 3. The geometric mean is a half-density, not one Gibbs weight

Define the exact leading periodic weights

 rho_m(z)=|det(I-DF^m(chi(z)))|^-1,  Z_m=sum_(G_m)rho_m(z).

For a unit pulse the LEADING paired coefficient is exactly

 sum_(z in G_m) rho_m(z) sqrt(rho_m(z+d_m)/rho_m(z))
                        e(N[Q_m(d_m)+q+D_m(z)]).                    (W9)

This retains the geometric-mean ratio. Let phi=log J^u F. Since F preserves
area, its periodic unstable multiplier is Lambda_m=exp(S_m phi), and

 rho_m=e^(-S_m phi)/(1-e^(-S_m phi))².                               (W10)

The denominator differs from one exponentially in m, uniformly in the class.
The finite ratio in W9 converges uniformly, at an exponential rate, to

 exp{-sum_(j in Z)[phi(F^j Psi_d x)-phi(F^j x)]}=J_d(x).              (W11)

For the convergence, pull phi back by the Holder chi, use the centered
homoclinic difference series and d_m-d=O(lambda^-m), and then W10.
For the equality to J_d, differentiate stable holonomy along unstable leaves
and unstable holonomy along stable leaves. The respective Jacobians are the
convergent forward and backward products of unstable/stable expansions.
Multiplying them, the angle between the bundles cancels using area invariance.
This gives the displayed bilateral unstable-potential ratio. The required
leaf holonomies are C1 by the graph construction in Section2.

Thus the candidate limiting marked integrand in physical area coordinates is

 sqrt(J_d(x)) e(N A(x)),  A(x)=B(x)+1/(2sqrt(2)).                    (W12)

It is a genuine half-density: f->sqrt(J_d) f∘Psi_d is unitary on L²(area).
It is NOT legitimate to replace sqrt(J_d) by one without an estimate.
By W7–W8 and the change of variable t=B(q,p), W12 satisfies the proved
oscillatory integral bound

 |integral sqrt(J_d(x))e(N A(x)) dx| <= C N^-1/2.                    (W13)

Indeed the transformed density is C^(0,1/2) with a uniform norm; its N-th
Fourier coefficient is bounded by that norm times N^-1/2 using a half-period
translation difference. This is a physical-area integral, not yet a statement
about the finite weighted sum W9.

## 4. Exact inherited and missing measure-transfer inputs

The prior project proof nonlinear_bracket_pressure.md Section2 identifies
physical area as the unique Gibbs equilibrium state for -phi, with pressure
zero. Under chi its pullback is the S-invariant Gibbs measure for -phi∘chi.
It is NOT automatically Haar measure. The same note's distinct fixed-point
unstable multipliers show why replacing the unstable potential by a constant
coboundary would be false for this actual map.

To pass W9 to W12 one needs the NORM-UNIFORM weighted periodic estimate

 sum_(Fix F^m) a(x)/|det(I-DF^m(x))| = integral a dx
                                     +O(e^-cm ||a||_(C^sigma)).      (EQ)

The earlier shadow_tube_history_bridge.md explicitly leaves the geometric
version of this input conditional. It cannot be imported here as established.
A separate primary-source check is examining the exact transfer-operator
statement, coding-boundary multiplicities and test-norm dependence. If EQ
holds with sigma<=1/2, W11 and the accepted defect convergence would give
W9=W12+O(N^C e^-c'm), because the marked integrand has only polynomial-in-N
Holder norm. An unquantified weak convergence theorem would not suffice.

## 5. The exact quantum factor remains visible

For the actual rotated box, the full coefficient after e(NDelta_m) is

 w_(0,m)(z) * P_(G_z)(B_h) * Z_(m,h,J)(z),  h=(2*pi*N)^-1.           (W14)

The Gaussian box probability must not be confused with the conditioned
expectation Z. The accepted first-loop theorem bounds and approximates Z
uniformly for mh bounded, but its per-class error is not absolutely summable
across the full trace family. Replacing W9 by the full paired coefficient
inserts the factor

 P_(G_(z+d))(B_h)P_(G_z)(B_h)
                  Z_(m,h,J)(z+d) conjugate(Z_(m,h,J)(z)).             (W15)

No locality, derivative bound, or harmlessness of W15 in the marked weighted
sum is asserted in this note. Its actual homoclinic ratio is the next quantum
leaf. Even a successful one-pulse W15 estimate would leave exponentially many
other displacements, their torsion sectors, and the signed TRACE-005 aggregate
uncontrolled. The normalization is the original outer SUM of displacements,
not their average.
