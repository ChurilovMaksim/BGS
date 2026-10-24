# An actual high-dimensional LOCAL first-loop resummation

Project proof, independently internally reviewed with hash-specific v2
confirmation on 6 October 2026.
This theorem concerns a defined rotated saddle-box integral. Its connection
to the original trace is supplied separately by [the global contour theorem](global_rotated_box_trace.md)
with an explicit finite-band summed tail, conservatively for m<=2N.
The local first-loop errors are not thereby absolutely summable.

## Statement

Use the actual stationary phases and any fixed finite-order one-step WKB
amplitude from uniform_cluster_lemma.md. Let m vary, let x* be any real
stationary class, and put K=-Phi''(x*). The actual local bounds give
K>=I/2, a nearest-neighbour Hessian, inverse row sums <=5/4, and common
analytic neighbourhoods/derivative bounds independent of m and the class.
The leading amplitude is real and positive.

Put h=(2pi N)^-1. Rotate x-x*=exp(-i pi/4)sqrt(h)y, factor out the
stationary phase, leading amplitude and Gaussian determinant, and let R_h(y)
be the EXACT remaining local analytic exponent. Choose a sufficiently small
fixed rho>0, depending only on the common local analytic bounds. Write
B_h=[-rho/sqrt(h),rho/sqrt(h)]^m and let E_B denote the centered Gaussian
with covariance G=K^-1 conditioned on B_h. Define

Z_(m,h)=E_B exp(R_h(Y)).

This conditional expectation is the authoritative normalization. Dividing
an unnormalized rotated-box integral by the FULL Gaussian determinant instead
produces P_G(B_h) Z_(m,h). Here P_G(B_h)=1+O(m exp(-c/h)), but those two
objects are not declared exactly equal.

Let ell_(1,m) be the first formal connected coefficient from (B2). Then
for every fixed b<infinity, uniformly over m with mh<=b and all such
stationary classes,

Z_(m,h)=exp(h ell_(1,m)) [1+O_b(sqrt(h))].             (L1)

More explicitly the absolute error is bounded by
C_b[m h^(3/2)+h sqrt(m)]+C_b exp(-c/h), after decreasing c>0 to absorb
polynomial boundary factors. Since |h ell_1|<=C mh, this also gives the
relative error in (L1).

The exponent h ell_1 is generally O(1) when m~N; replacing its exponential
by 1 is not justified by fixed-dimensional stationary phase. This lemma
rigorously resums that first extensive correction ON THE ROTATED BOX.
Its algebraic per-class error cannot be summed absolutely over exponentially
many stationary classes. No exponential optimal remainder is asserted.

## 1. Local normal form and uniform bounds

Real analyticity and positivity of the leading amplitude give

R_h(y)=c sqrt(h) W(y)+h Q(y)+T_h(y),  c=exp(-i pi/4),   (L2)

where W is REAL, odd, and a sum of nearest-neighbour polynomials of degrees
one and three, while Q is a sum of complex local polynomials of degrees
zero, two and four. Coefficients are uniformly bounded. To check the common
phase of W, the cubic phase term contributes
 i exp(-3i pi/4) sqrt(h) Phi_3=c sqrt(h) Phi_3,
and the linear log-amplitude contributes c sqrt(h) L_1. The symbol-order-h
amplitude first enters Q, not W.

On B_h the exact analytic Taylor remainder obeys

|T_h(y)|<=C h^(3/2) sum_j(1+|y_j|^5+|y_(j+1)|^5).     (L3)

The exponent family used below includes R_h, c sqrt(h)W+hQ, pure
multiples t sqrt(h)W with |t|<=1, c sqrt(h)W+mu, and the straight
interpolants used between them. Constants such as mu=O(mh) do not affect
spatial derivatives. For the spatially varying parts of this family,

|partial_j R|<=C sqrt(h)(1+sum_(k near j)|y_k|²),
max_j sum_k |partial_j partial_k R|<=C rho+C h.        (L4)

The same bounds hold for the real parts of bounded scalar multiples.
These follow from the cubic vanishing of the phase remainder at x* and
from local analyticity; sqrt(h)|y_j|<=rho makes higher Taylor terms
geometrically bounded. Choose rho, then h small, so that real exponential
tilts of all expressions used below, with scalar modulus <=4, preserve
Hessian lower bound I/2. More specifically, by decreasing rho again to
account for the fixed local degree, for m>=2 one can arrange
1.3<=V_jj<=2 and sum_(k!=j) sup_(B_h)|V_jk|<=.7 for each real tilted
potential V. This is a SUM OF ENTRYWISE SUPREMA, not only a pointwise
row bound. It follows from the entrywise perturbation estimate and the
uniformly bounded number of neighbours. At m=1 its single curvature lies
in [.8,2]. Also |partial_j V(0)|<=C sqrt(h).
All constants are independent of m.

## 2. Uniform local moments under the real tilts

This step is needed; strong convexity alone is not silently substituted
for a bound on every coordinate mean.

Condition on all other coordinates; locality makes the conditional
potential depend only on neighbours. Its one-dimensional
conditional density is strongly log-concave on the interval defining B_h.
Its clipped mode a_j satisfies

|a_j| <= C sqrt(h)/1.3 +(1/1.3) sum_(k!=j) c_jk |y_k|,
where c_jk=sup_(B_h)|V_jk| and sum_(k!=j) c_jk<=.7.               (L5)

This follows by comparing partial_j V at (0,neighbours) with its value
at the origin and using conditional curvature >=1.3. Clipping to the
interval cannot increase the bound. For m=1 there is no neighbour term.

A one-dimensional density of curvature >=lambda on an interval has
uniform Lp distance from its clipped mode. On either side of that mode,
its density relative to a half-Gaussian exp(-lambda t²/2) is nonincreasing
in the distance t. Conditional on either side it is therefore stochastically
dominated in distance by that half-Gaussian. This also holds when the mode
is at an endpoint, since the one-sided derivative only strengthens decay.

Minkowski applied to (L5), with M_p=max_j ||Y_j||_Lp, gives

M_p <=(.7/1.3)M_p+C_p,

hence M_p<=C'_p for every fixed p. This holds for p>=1 for all the real tilted measures, uniformly in m,
h and the box radius. If 0<p<1 is desired, the p=1 bound implies it.
At m=2 use the combined off-diagonal row sum for the repeated neighbour.

## 3. Poincare on the hard box and exponential integrability

The required inequality is

Var_mu f <=2 E_mu |grad f|²                           (L6)

when the potential Hessian is >=I/2 on the convex box. Its exact-source
justification is Kolesnikov--Milman, arXiv:1310.2526v7, Theorem 3.1(1)
on printed p.13 and Eq. (3.2) on printed p.14, followed by smooth convex
exhaustion of the box.
The source and the boundary argument are recorded in
../literature/convex_box_poincare_check.md. No boundary condition on f is
required. This is the only external analytic inequality imported here.

For any one of the real exponents H used above, let
f(s)=log E_B exp(s H). By (L4), the local moment bound, and (L6),

f''(s)=Var_s(H)<=C mh.

Moreover f'(0)=E_B H=O(mh): the order-sqrt(h) part is odd and its
Gaussian-box expectation is zero; the remaining local terms have expectation
O(h) per site. Integrating in bounded s gives

E_B exp(p Re R)<=exp(C_p mh)                          (L7)

for the complete exponent family above and real tilt strengths in the
bounded range |p|<=4 certified by the chosen rho. This is not an all-real-p
claim at one fixed rho. In particular all required L2 weights are covered.
Constants mu=O(mh) add only O(mh) to their log normalizations.

## 4. Gaussian connected estimates

All expectations in this paragraph are for the unconditioned Gaussian G.
Wick's rule, exponential covariance decay, and the connected-tree summation
proved in uniform_cluster_lemma.md give

Var(W)<=C m,  Var(Q)<=C m.                            (L8)

The complex variance of Q here means E|Q-EQ|². Set
X=sqrt(h) W, beta=E X², mu=h E Q; then |beta|+|mu|<=C mh.
Gaussian box conditioning changes polynomial moments by a polynomial
factor times exp(-c/h), because each coordinate variance is <=5/4 and
P(B_h^c)<=C m exp(-c/h).

For clarity the next estimate uses an exact Gaussian integration-by-parts
identity, rather than an unquantified CLT. Decompose W into its first and
third Gaussian Hermite chaoses, W=W_1+W_3, and set P=W_1+W_3/3.
For the Gaussian Ornstein--Uhlenbeck generator L=Tr(G Hess)-y.grad,
-LP=W. Define

Gamma=h (grad W)^T G grad P.

Then E Gamma=beta and

E|Gamma-beta|²<=C m h².                              (L9)

To see the volume bound, Gamma is a sum of pairs of local polynomial
vertices connected by one G edge. Subtracting its mean-square removes
disconnected Wick diagrams. Every surviving diagram is connected after
including those two G edges. Sum its site labels along a spanning tree;
the covariance row-sum bound leaves one free root, hence O(m), exactly
as in the proof of (B3). Only finitely many degrees occur here, so all
combinatorial constants are fixed.

## 5. Boundary terms and a quantitative complex MGF comparison

Put F(t)=E_B exp(t X), for complex t on the segment from 0 to c. Gaussian
integration by parts on B_h gives the exact identity

F'(t)=t beta F(t)+t E_B[(Gamma-beta)exp(tX)]-Flux(t),   (L10)

Flux(t)=sqrt(h)/P_G(B_h) integral_(partial B_h)
 exp(tX) [n.G.grad P] p_G d sigma,

where n is the OUTWARD normal and p_G is the full Gaussian density.

The signed boundary contribution is minus this outward flux. By (L7),(L9), the middle
term is at most C_b h sqrt(m).

Here is a dimension-uniform boundary bound, rather than assuming that
an oscillatory boundary is small. Under the REAL tilt Re(t)X the potential
is local, has the convexity and conditional-moment bounds above, and its
normalization is bounded by exp(C_b). Its one-coordinate marginal density
at +/-rho/sqrt(h) is <=C exp(-c/h).

One can verify this last density claim directly using (L6). If q_j is
the marginal negative log density, differentiation under the integral gives
q_j''=E V_jj-Var(V_j). Conditional Poincare on the other coordinates gives
Var(V_j)<=2 sum_(k!=j)sup|V_jk|²<=.98. Thus for m>=2,
.32<=q_j''<=2; the one-dimensional case is immediate. Its mean is bounded
by section 2, and the one-dimensional mode-distance argument then bounds
its mode as well. The upper curvature bound bounds the density at the mode
by a constant; the lower bound gives the asserted Gaussian boundary decay.
For small h the mode is uniformly far from the endpoints.

On the box ||G.grad P||_infinity<=C(1+rho²/h), because P has degree at most three
and G has bounded row sums. Only one normal component is used on each
face; no dimension-free Euclidean-norm bound is asserted. Summing its 2m
faces therefore bounds the
boundary term by C_b m h^-1/2 exp(-c/h). This also accounts for conditioning
normalization, since P(B_h) tends to one uniformly when mh<=b.

Integrate (L10) along the complex segment, using beta=O_b(1). It follows that

E_B exp(c X)=exp(c² beta/2)+O_b(h sqrt(m))+O_b(exp(-c'/h)). (L11)

This does not rely on a real cubic Gaussian MGF existing without a cutoff;
it generally does not. The box, convex real tilts and explicit face estimate
are essential.

## 6. Completing the local resummation

By Gaussian fixed moments and (L3),
||T_h||_L2(B)<=C m h^(3/2).
By (L8), ||hQ-mu||_L2(B)<=C h sqrt(m)+O(exp(-c/h)).
For complex A,B, use
|exp A-exp B|<=|A-B|(exp(Re A)+exp(Re B)),
then Cauchy--Schwarz and (L7). This first removes T_h and then replaces
hQ by its mean mu, costing
C_b[m h^(3/2)+h sqrt(m)]+O_b(exp(-c/h)).
Equation (L11) now gives

Z_(m,h)=exp(mu+c² beta/2)
 +O_b(m h^(3/2)+h sqrt(m))+O_b(exp(-c/h)).

The exponent mu+c² beta/2 is exactly h ell_(1,m), by the first connected
Wick coefficient. Its modulus is bounded by C mh, so division by its
exponential is harmless for mh<=b. This proves (L1).

## Scope, checks and remaining work

This is a uniform, quantitative, actual integral statement about the
ROTATED BOX defined in the theorem. It upgrades the formal extensive
first-loop observation to a local analytic resummation.

The separate [global contour theorem](global_rotated_box_trace.md) now gives
a finite-band representation by exact boxes with an exponentially small
summed contour tail. A local O(N^-1/2) relative first-loop error remains
insufficient after absolute summation over exponentially many classes.
Signed evaluation, optimal local remainders and unrestricted bands remain open.

The algebraic identities underlying (L8-L9) use the same connected-Wick
mechanism tested by computations/verification/heisenberg_wkb/cluster_checks.py. No numerical simulation verifies
(L1); it is a project analytic proof with an exact-source Poincare input and
independent internal review. No external-referee or formalization claim.
