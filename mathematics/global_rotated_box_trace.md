# Global rotated-box trace representation and conditional contour tails

**Status:** project analytic proof with fresh independent internal review,
6 October 2026; supporting constructive result for TRACE-017.
The conservative headline is the uniform actual-trace representation for
1<=m<=2N, for fixed J>=1, with error O_J(N^(3/2-J))+O_J(sqrt(N)e^(-4N/5)).
The local integrals are exact and have not been evaluated collectively.
No signed CUE comparison, all-band optimal remainder, or BGS conclusion follows.
The maintained model is the unchanged odd-dimensional quantization at tau=10^-80.

This note curates the two separately frozen contour/tail proofs and the
explicit estimates reconstructed by the independent review. Exact source
hash mappings, editorial changes and execution scope are in
[the review record](../archive/record/global_rotated_box_review_scope.md).
Generic norm-to-factorial trace telescoping is prior project work in
[Heisenberg trace support](heisenberg_trace_support.md), section 3; the
specific WKB instantiation is in [the factorial reduction](factorial_wkb_reduction.md).

## Part I. Global representation and conservative summed tail

## 1. Uniform finite-band representation

Fix a finite WKB order J. Write e(z)=exp(2pi i z) and set
h=(2pi N)^-1 throughout this note. The WKB polynomial remains in powers of
N^-1: a_(r,J)(h,x,y)=sum_(ell=0)^J (2pi h)^ell a_(r,ell)(tau,x,y).
Let B_m=6I-P_m-P_m^T with the cyclic shift P_m, D_m=det B_m,
Phi_r=sum_j S_(r_j)(tau,x_j,x_(j+1)), and
A_r=product_j a_(r_j,J)(h,x_j,x_(j+1)). Winding indices range over
Z^m/B_m Z^m. At m=1, B_1=4; at m=2 its off-diagonal entries are -2. In each global Fresnel integral of
[exact Gaussian reciprocity](exact_gaussian_reciprocity.md), (G6-G7), use its UNIQUE actual real stationary
point x*_(r,nu). Define the compact contour box

C_(r,nu)={x*_(r,nu)+(1-i)u : u in [-1,1]^m},

with the product orientation, and retain the FULL nonlinear phase and
finite-J amplitude. Put

S_(N,m,J)= e(3mN/8) N^(m/2)/8^m
 sum_(r in {0,1,2,3}^m) sum_(nu mod B_m)
 integral_(C_(r,nu)) e(N[Phi_r(tau,x)+nu.x]) A_r(x) dx.    (C1)

For every fixed 0<b<8pi/(5 log 7), uniformly for 1<=m<=bN,

|Tr V_(N,J)^m-S_(N,m,J)|
 <=C_(J,b) sqrt(N) exp[-(8pi/5-b log7)N].              (C2)

In particular, for every m<=2N, the right side is at most
C_J sqrt(N) exp(-4N/5). Combining with the separately proved one-step
operator telescoping, for J>=1 so that N||U_N-V_(N,J)||=o(1), gives

Tr U_N^m=S_(N,m,J)+O_J(N^(3/2-J))+O_J(sqrt(N)e^(-4N/5))
                                                         (C3)
uniformly for 1<=m<=2N. Negative traces use complex conjugation.

This is a uniform signed representation by EXACT rotated-box integrals,
not by their first-loop approximations. Each box is the one in the local
theorem with scaled radius rho=sqrt(2), after the normalization in section 6.
The local O(N^-1/2) relative first-loop error still cannot be summed absolutely
over exponentially many boxes. No CUE value is established.

## 2. Literal complex-strip certificate at tau=10^-80

The actual symbol has sum |c_(k,l)|<=52, |k|<=9, |l|<=1 and
|k|+|l|<=10. On the complex symbol strip |Im q|,|Im p|<=9/4,

|partial^d g|<=52 exp(45pi) 63^d, d=0,1,2,3.

Using pi<22/7, e<11/4 and 45pi<142 gives the explicit upper bounds

|g|<10^66,  max|partial²g|<10^70,
max|partial³g|<10^72.                                (C4)

Consequently B=10^73 bounds the characteristic vector field
(-g_p,g_q)/(2pi) and its first two induced max-norm derivatives on that
strip. Since B tau=10^-7, its complex flow for 0<=t<=tau moves by at most
2*10^-7, its first derivative differs from identity by at most 2*10^-7,
and its second derivative is bounded by 4*10^-7. These follow from the
integral equation and the first two variational equations, using
exp(3Btau)<2.

For endpoint variables |Im x|,|Im y|<=2, the initial momentum is
(y+r-3a)/4. The characteristic projection x=X_t(a,p_0(a,y)) differs from
a by at most 2*10^-7, and its a-derivative differs from one by at most
2*10^-7. Solving for a by contraction in a 4*10^-7 neighbourhood of x
therefore stays strictly inside the symbol strip of width 9/4. This gives
a holomorphic inverse uniformly over all real translates and r=0,1,2,3.
The first two implicit-derivative formulas bound the resulting momentum's
endpoint derivatives through order two by 100. For example a_y=-X_y/X_a;
second derivatives differentiate this formula, with denominator bounded
below by 1-2*10^-7 and numerators controlled by the flow estimates.

Differentiating S_t=g(x,p)/(2pi) through two endpoint derivatives now gives
max |partial_(x,y)^2 S_t|<=10^76. Hence, on the entire endpoint strip
|Im x|,|Im y|<=2,

max |partial²(S_r(tau)-S_r(0))|<=10^-4.               (C5)

The constant is deliberately loose: each composite second derivative has
at most a fixed handful of terms bounded by 10^70*(1+100)^2 or by a
first derivative of g times 100, all well below 10^76.

Thus the CYCLIC nonlinear phase has a symmetric matrix E of entrywise
Hessian suprema, supported on neighbours, with row sums at most 4*10^-4.
We use the weaker epsilon=1/10 in the contour proof. This includes m=1,2
with repeated derivatives combined correctly.

The leading amplitude solves a scalar transport with coefficient
(g_xp+g_pp S_xx)/(4pi), bounded by 10^73 on these complex characteristics.
Its modulus is at most exp(10^-7)<3/2, and on real points it is positive.
For the fixed-J derivative margin, repeat the inverse construction on endpoint
width 2+1/100, still strictly inside the symbol strip of width 9/4. The same
constants have ample slack. A finite collection of transport equations can
use nested strips between these widths, retaining a neighbourhood of the
closed width-2 strip. Thus every fixed finite collection of higher transport
amplitudes is holomorphic and uniformly bounded there. No J-uniform estimate
is inferred. The explicit leading exponential gives
exp(-gamma)<=|a_0|<=exp(gamma), gamma=10^-7.
For small h the higher terms are uniformly smaller than the leading term;
the logarithm is log(a_0)+log(1+(a_J-a_0)/a_0), not an inference from a
modulus bound alone.
Therefore, for each fixed J and all sufficiently large N,

sup_(|Im x|,|Im y|<=2)
 |sum_(ell=0)^J N^-ell a_(r,ell)(tau,x,y)|<=2.         (C6)

No bound uniform in J is asserted. The startup threshold can depend on J.
All these statements are uniform over real translates: the coefficients
and phase corrections have their exact four-periodic gluing.

## 3. A global M-matrix damping inequality

Fix a lifted class and translate its actual stationary point to zero.
The phase can be written

Psi(z)=Psi(0)-(1/2)z^T K_0 z+q(z),
K_0=B_m/4=I+(1/4)L_cycle,
q(0)=0, grad q(0)=0.

Here q is real on real coordinates and holomorphic on |Im z_j|<=2.
Its Hessian entrywise-supremum matrix E is symmetric and has row sums
<=epsilon=1/10, by (C5). Subtracting the stationary affine terms does not
change that Hessian bound.

Let f(u)=clip(u,-1,1) coordinatewise and z(u)=u-i f(u). Since f is
nondecreasing,

u^T K_0 f(u)
 =sum_j u_j f(u_j)+(1/4)sum_edges (u_j-u_k)(f(u_j)-f(u_k))
 >=sum_j min(u_j²,|u_j|).                            (C7)

To bound the nonlinear term, integrate its gradient along the vertical
segment u-i s f(u), and use grad q(0)=0. Symmetry of E and the elementary
rearrangement inequality

(a-b)(min(a,1)-min(b,1))>=0, a,b>=0,

show
sum_ij E_ij |f(u_i)||u_j|<=epsilon sum_j |u_j||f(u_j)|,
and the same estimate holds with |u_j| replaced by |f(u_j)|.
Therefore

|Im q(u-i f(u))|<=2epsilon sum_j min(u_j²,|u_j|).

Together with (C7),

Im(Psi(z(u))-Psi(0)) >=(4/5)sum_j min(u_j²,|u_j|).    (C8)

This is a GLOBAL bound on R^m, not a Taylor estimate on a small real box.
It uses the exact small complex Hessian and the cyclic quadratic M-matrix.
The same inequality with a factor s holds on u-i s f(u), 0<=s<=1.

## 4. Legitimate deformation of the Abel/Fresnel integral

Start with the exact regularization in (G7), with positive Gaussian damping.
Use the holomorphic regulator exp(-pi eta_reg sum_j(z_j+d_j)^2), where d is
the real displacement between the cat center and actual stationary point.
For eta_reg>0, the real integral is absolutely convergent, as are all bounded
imaginary contour translates. Piecewise linear coordinate contours can be
deformed from the real axes by Cauchy's theorem. At finite eta_reg the Gaussian
regulator dominates their at-most-linear growth at real infinity; boundary
faces tend to zero. Equivalently, apply the product-contour argument on
finite boxes and then increase the boxes. Corners have measure zero.

On the final graph z(u)=u-i f(u), (C8) supplies an integrable bound
independent of eta_reg near zero. The regulator has modulus at most
exp(pi eta_reg m), and tends pointwise to one. Thus dominated convergence
removes eta_reg for each finite m,N and identifies the original Abel integral
with the integral on this global bent contour. No compact analytic cutoff
or cancellation of unidentified real-chart side faces is assumed.

The product Jacobian has modulus at most 2^(m/2). Within [-1,1]^m the
contour is exactly x*+(1-i)u, the desired rotated box. Outside it, (C8)
and (C6) give the explicit tail bound in the next section.

## 5. Summing the tail WITH the branch and winding counts

Set c=8pi/5 and define

I_N=integral_R exp[-cN min(u²,|u|)]du
 <=sqrt(5/(8N)) +(5/(4pi N))exp(-cN),
J_N=integral_(|u|>1) exp[-cN |u|]du
 =(5/(4pi N))exp(-cN).

For ONE global class, the absolute contour tail is at most

m *2^m *2^(m/2) J_N I_N^(m-1),                       (C9)

where 2^m is the amplitude bound (C6), and 2^(m/2) is the Jacobian bound.
The exact trace prefactor is N^(m/2)/8^m. There are 4^m branches and
D_m<=6^m winding representatives. Thus the TOTAL trace tail is at most

m N^(m/2) (6 sqrt(2))^m J_N I_N^(m-1).               (C10)

Indeed 4^m*6^m/8^m=3^m, which multiplies the amplitude and Jacobian factors.
Write I_N<=sqrt(5/(8N))(1+eta_N), with
eta_N=O(N^-1/2 exp(-cN)). Formula (C10) becomes

<=C (m/sqrt(N)) (3sqrt(5))^m exp(-cN)(1+eta_N)^m.

For m<=bN, the last factor is bounded. Since 3sqrt(5)<7, this proves (C2).
For m<=2N, pi>3 and log7<2 give c-2log7>4/5, proving the simple bound
stated in section 1. The factor sqrt(N) is retained.

There is no claim for every compact Heisenberg band from this particular
radius-one estimate. The exact reciprocity formula remains valid at all m;
(C2) has the explicit bandwidth restriction shown. A larger certified strip
or a different signed tail argument would be needed to extend this bound.

## 6. Relation to the accepted local theorem and the remaining signed task

On the retained box put y=sqrt(2/h)u. Then
z=(1-i)u=exp(-i pi/4)sqrt(h)y and |y_j|<=sqrt(2)/sqrt(h).
The actual quadratic Hessian is K=-Psi''(0). After factoring the stationary
phase, leading amplitude and FULL Gaussian determinant, the box integral
contains P_G(B_h) Z_(m,h), not merely Z_(m,h), where G=K^-1.

The small-radius local theorem is not simply imported at this larger radius.
For the exact rotated exponent, the phase-remainder Hessian row bound is
at most 8eta, eta=10^-4; tilts of modulus at most 4 cost at most 32eta.
The scaled log-amplitude Hessian costs C_J h. For the polynomial tilt family,
apply Cauchy to each edge Hessian on the bidisk of radius R=7/4 about the
real saddle. On |z_j|<=sqrt(2), its linear and quadratic Taylor pieces have
per-entry bound eta*(2sqrt(2)/R+6/R^2)<4eta. The resulting cubic/quartic
truncations, pure cubic tilts and interpolants still have row perturbation
below 0.1 after the bounded tilt factor. Leading log-amplitude quadratic
terms cost O(h), and its linear truncation has zero Hessian. Hence for small
h all required real tilts satisfy 1.3<=V_jj<=2 and the sum of off-diagonal
entrywise suprema <=.7 for m>=2; at m=1 the curvature lies in [.8,2].
Cauchy on an interior strip around the rotated points (imaginary parts at
most 1) supplies the local Taylor remainders. This verifies the complete
finite family required by [the local theorem](rotated_local_first_loop.md).

Even with this identification, replacing each exact Z by exp(h ell_1)
has only an algebraic relative error. The exponentially numerous saddle
weights prevent absolute summation of that error at m~N. Therefore (C3)
closes a GLOBAL REPRESENTATION/Tail subproblem, while leaving the complete
signed comparison among these exact local integrals OPEN.

For fixed factorial order and compact Fourier weights whose block sums
satisfy |n_B|<=2N, the trace table in (C3) can be inserted into the exact
Möbius transform. Its operator error is O(N^(k-J-1/2)); its additional tail
error is polynomial times exp(-4N/5). This is a representation reduction,
not a CUE evaluation. Other compact supports retain the all-band exact
Gaussian-operator representation of the earlier note.


## Part II. Conditional large-field estimate

### 1. Exact improvement being claimed

For one global Fresnel integral, let x* be its actual stationary point,
h=(2pi N)^-1, K=-Psi''(x*), and let a*=product_j a_(r_j,0)(tau,x*_j,x*_(j+1))>0.
Normalize by the absolute full Gaussian prefactor

a* (2pi h)^(m/2)/sqrt(det K).

Use the same coordinatewise bent contour z=u-i clip(u,-1,1), after translating
x* to zero. Then its part outside the fully rotated box has normalized
absolute integral bounded by

exp(C mh) [(1+C sqrt(h) exp(-2/(5h)))^m-1].            (D1)

In particular, for mh<=b this is at most
C_b m sqrt(h) exp(-2/(5h)), for sufficiently small h.

There is NO extra C^m multiplying this per-integral bound. Constants depend
on fixed finite WKB order and actual symbol, not on m or the stationary class.
The exponential number of winding classes is still a separate loss. (D1)
does not establish collective cancellation or a CUE trace comparison.

### 2. Uniform local assumptions, supplied by the actual strip certificate

Write the exact phase at its saddle as

Psi(z)=Psi(0)-(1/2)z^T K z+R_phi(z).

The nonlinear remainder is a sum of nearest-neighbour terms. Each comes
from the one-step phase correction delta S=S(tau)-S(0) after subtracting
its value, linear part and quadratic part at the saddle. The literal
complex-strip certificate of Part I of this note gives, on |Im z|<=2,

max_(d=0,1,2)|partial^d delta S|<=eta=10^-4.           (D2)

The d=0,1 bounds are weaker than the direct bounds used there; d=2 is (C5).
In particular K has negative off-diagonal entries, diagonal dominance,
row mass at least 1-4eta, and off-diagonal absolute row sum at most .5+2eta.
At m=1 there is no off-diagonal entry; the same inequalities remain safe.
Repeated edges at m=2 are combined.

Here a_(r,J)(h,z,w)=sum_(ell=0)^J (2pi h)^ell a_(r,ell)(tau,z,w),
so the h notation never drops the factor 2pi from the original N^-ell.
For each fixed J and small h, the local finite WKB amplitude factors obey
1/2<=|a_(r,J)(h,z_j,z_(j+1))|<=2 on that strip. This follows from the
nonvanishing exponential leading transport and uniform convergence of the
finite polynomial to it. All local logarithms and derivative bounds used
below are therefore uniform.

### 3. Partition by the ACTUAL large-coordinate set

For a subset S of {1,...,m}, integrate on the piece

|u_j|>1 for j in S,  |u_j|<=1 for j in T=S^c.

On T, z_j=(1-i)u_j and the Jacobian modulus is sqrt(2) per coordinate.
On S, z_j=u_j-i sign(u_j) and its Jacobian modulus is one.
This exact partition is the key: only the s=|S| large coordinates will
pay new constants. We never replace the core Hessian by a diagonal lower
bound on all m coordinates.

### 4. Keep the core Gaussian exactly

Let s_j=sign(u_j) on S. The imaginary part of the quadratic phase is

u_T^T K_TT u_T+u_T^T K_TS s_S+u_S^T K_ST u_T+u_S^T K_SS s_S.

Because |u_T|<=1, K has negative off-diagonal entries, and the row mass is
at least 1-4eta, this is bounded below by

u_T^T K_TT u_T
 +sum_(j in S)[(1-4eta)|u_j|-(.5+2eta)].              (D3)

Indeed internal S--S terms cost their off-diagonal row sums times |u_j|;
the two cross terms cost the cross-row sum times |u_j|+1. The |u_j| part
of that cross cost cancels exactly against the extra cross-row contribution
in the diagonal-dominance bound, leaving only the displayed boundary constant.

The core quadratic form K_TT is retained in full. Its Gaussian determinant
is NOT estimated by a constant to the power |T|.

### 5. Nonlinear and amplitude changes touch only incident edges

Compare R_phi(z_T,z_S) to R_phi(z_T,0). Only edges incident to S change.
For one such edge, its analytic delta S value changes in imaginary part
by at most 2eta. Its subtracted linear term costs at most eta per large
endpoint. The imaginary parts of its subtracted quadratic terms are bounded
by a constant times eta times |u_j|+1 for large endpoints: on S, Im(z_j²)
has magnitude 2|u_j|, while a mixed product costs at most |u_j|+1 when
the other endpoint is in T. If both endpoints are in S it costs
|u_j|+|u_k|. Summing the at-most-two incident edges per large coordinate gives

|Im[R_phi(z_T,z_S)-R_phi(z_T,0)]|
 <=20eta sum_(j in S)(|u_j|+1).                       (D4)

Using eta=10^-4, (D3)-(D4) imply the lower bound

u_T^T K_TT u_T
 +sum_(j in S)[.9|u_j|-.5]
 +Im R_phi(z_T,0)                                   (D5)

for the imaginary part of the FULL phase. For example the exact retained
linear expression is (1-24eta)|u|-(.5+22eta); it is at least .9|u|-.5 for
|u|>=1. This leaves a positive 2/5 at each large-coordinate threshold.

Similarly the amplitude ratio between (z_T,z_S) and (z_T,0) has modulus
at most 4 per changed local factor, hence at most 16^s. No factor depending
on |T| arises in this comparison.

### 6. Core integration uses the proved convex-box bound

Set z_S=0 and retain the actual local phase/amplitude on the T coordinates.
Its Gaussian is the principal covariance K_TT^-1, and its exponent beyond
the quadratic part is exactly of the type handled in sections 1--3 of the
[local first-loop proof](rotated_local_first_loop.md). Deleting coordinates does not worsen the
uniform diagonal dominance or local degree. Its potential is stationary
at zero; its nonlinear phase starts at degree three. The finite amplitude
has O(h) constant log terms on at most m edges, which contribute O(mh).

For clarity, the exact real exponent is
H_T(y)=Re[log(A(h,z_T,0)/a*)+i R_phi(z_T,0)/h],
where z_T=exp(-i pi/4)sqrt(h)y_T. Its base covariance is K_TT^-1,
not the T-by-T restriction of K^-1. The base Gaussian is conditioned on
|y_j|<=sqrt(2/h). Principal deletion only improves diagonal dominance.
The radius certificate in Part I gives the required bounds for
V_t=(1/2)y^T K_TT y-t H_T throughout the bounded real tilt range.
Conditional clipped-mode contraction gives raw coordinate moments;
convex-box Poincare then gives
f''(t)=Var_t(H_T)<=2 E_t|grad H_T|^2<=Cmh,
for f(t)=log E_B exp(tH_T). At t=0 the leading linear/cubic terms are
odd on the symmetric centered box and vanish exactly. The remaining
expectation is O(mh), including constants on edges with deleted endpoints.
Therefore f(1)<=Cmh. This proves the needed absolute exponential bound,
without a first-loop approximation or a formal-series assumption.

Consequently the ABSOLUTE core integral obeys

integral_(|u_T|<=1) exp[-u_T^T K_TT u_T/h]
 |A(h,z_T,0) exp(i R_phi(z_T,0)/h)| du_T
 <=a* (pi h)^(|T|/2)/sqrt(det K_TT) *exp(C mh).        (D6)

This is the exponential-weight inequality (L7), after y=sqrt(2/h)u_T,
not the first-loop approximation and not a formal cumulant estimate.
The Gaussian conditioning probability is at most one, so it can be omitted
for this upper bound. If T is empty, (D6) just bounds the O(mh) amplitude
constants, with the empty determinant equal to one.

The direct small complex Hessian estimate ensures convexity on this full
radius-one core, as explained in Part I of this note, section 6. Thus
no unproved large-radius extension of a local Taylor heuristic is used.

### 7. Determinant ratio costs only the large-coordinate count

Combine (D5)-(D6), the Jacobian 2^(|T|/2), and the amplitude ratio 16^s.
For each large coordinate,

integral_(|u|>1) exp[-(.9|u|-.5)/h]du
 =(20h/9) exp(-2/(5h)).                              (D7)

The remaining ratio to the full Gaussian prefactor is controlled by

(det K)/(det K_TT)=det(K_SS-K_ST K_TT^-1 K_TS).

The positive Schur complement is bounded above by K_SS<=2.1 I, hence
sqrt(det K/det K_TT)<=2.1^(s/2). This is C^s, not C^m.
The powers of pi,h and the core Jacobian cancel exactly, leaving the
normalized contribution of this particular subset bounded by

exp(C mh)[C sqrt(h) exp(-2/(5h))]^s.

For example C=100 safely absorbs 16*(20/9)*sqrt(2.1/(2pi)). Summing over
all nonempty subsets S gives (D1) by the binomial theorem. No independence
assumption on the Gaussian coordinates has been used.

### 8. What this improves and what remains

This proves the conditional-integration mechanism requested by the parent:
all rotated core coordinates are integrated with their true principal
Gaussian and controlled nonlinear exponential weight. Only actual large
coordinates and incident edges incur additional constants.

Compared with the cruder completely absolute product-Gaussian bound, the
per-Fresnel estimate now has exp(O(mh)) rather than C^m. The conservative
large-field exponential rate here is smaller; no claim is made that every
numerical bandwidth constant improves. Its structural benefit is removing
the artificial volume cost, which is necessary for further high-order
cluster/remainder analysis.

Absolute summation over genuine or overcomplete winding classes still has
exponential mass. The complete signed winding-class sum and an optimally
accurate replacement of each exact local integral remain open. This lemma
alone does not solve either.

## 9. Separate sharper summed corollary from the conditional bound

This optional corollary is distinct from the conservative m<=2N statement.
Keep eta=10^-4 and gamma=10^-7, and put
kappa=log(1+sqrt(2))+gamma-(1/2)log(1-4eta).
For each fixed beta<(4pi/5)/kappa, the conditional bound gives total tail
C_(J,beta) sqrt(N) exp[-(4pi/5-beta*kappa)N] for m<=beta N.
The endpoint is strict. At beta=2 this rate is weaker than the headline
4/5 rate, although its admissible bandwidth is larger.

Proof: each Gaussian-normalized error must be multiplied by its leading
trace weight a*/(8^m sqrt(det K)). Since K_0>=I and ||K-K_0||<=4eta,
K>=(1-4eta)K_0 and det K>=(1-4eta)^m D_m/4^m.
Also a*<=exp(gamma*m). Summing the 4^m D_m classes therefore costs at most
exp(gamma*m)(1-4eta)^(-m/2)sqrt(D_m)<=exp(kappa*m),
using D_m<(3+2sqrt(2))^m and sqrt(3+2sqrt(2))=1+sqrt(2).
The per-class exponential exp(-2/(5h)) is exp(-4pi N/5), proving the claim.
Neither the amplitude nor determinant correction may be omitted.

## Verification and remaining obligation

The portable verifier `computations/verification/global_rotated_box_trace.py`
checks the literal rational constants, exact conditional quadratic corners,
perturbed Schur determinants, h/Jacobian factors and a counterexample to
unrestricted core completion. Its explicit checks survive Python -O and
imports are silent. Coverage and hashes are in the execution receipt.
Finite controls do not prove analytic deformation or an asymptotic trace law.

The exact saturated contour, its finite-band summed tail and the conditional
per-integral bound are proved here. Uniform signed evaluation of the exact
box sum, entropy-compatible optimal local remainders, unrestricted compact
Heisenberg bands and TRACE-005 remain open. In particular, never sum the
algebraic first-loop errors absolutely over the winding classes.
