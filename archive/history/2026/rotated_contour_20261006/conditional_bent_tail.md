# Conditional large-field estimate: removing the constant-to-the-dimension loss

Author continuation, 6 October 2026. No frozen or canonical file changed.
Depends on the corrected local convex-box estimates and the separately
stated global bent-contour/complex-strip arguments. Independent review pending.

## 1. Exact improvement being claimed

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

## 2. Uniform local assumptions, supplied by the actual strip certificate

Write the exact phase at its saddle as

Psi(z)=Psi(0)-(1/2)z^T K z+R_phi(z).

The nonlinear remainder is a sum of nearest-neighbour terms. Each comes
from the one-step phase correction delta S=S(tau)-S(0) after subtracting
its value, linear part and quadratic part at the saddle. The literal
complex-strip certificate of global_bent_contour.md gives, on |Im z|<=2,

max_(d=0,1,2)|partial^d delta S|<=eta=10^-4.           (D2)

The d=0,1 bounds are weaker than the direct bounds used there; d=2 is (C5).
In particular K has negative off-diagonal entries, diagonal dominance,
row mass at least 1-4eta, and off-diagonal absolute row sum at most .5+2eta.
At m=1 there is no off-diagonal entry; the same inequalities remain safe.
Repeated edges at m=2 are combined.

For each fixed J and small h, the local finite WKB amplitude factors obey
1/2<=|a_(r,J)(h,z_j,z_(j+1))|<=2 on that strip. This follows from the
nonvanishing exponential leading transport and uniform convergence of the
finite polynomial to it. All local logarithms and derivative bounds used
below are therefore uniform.

## 3. Partition by the ACTUAL large-coordinate set

For a subset S of {1,...,m}, integrate on the piece

|u_j|>1 for j in S,  |u_j|<=1 for j in T=S^c.

On T, z_j=(1-i)u_j and the Jacobian modulus is sqrt(2) per coordinate.
On S, z_j=u_j-i sign(u_j) and its Jacobian modulus is one.
This exact partition is the key: only the s=|S| large coordinates will
pay new constants. We never replace the core Hessian by a diagonal lower
bound on all m coordinates.

## 4. Keep the core Gaussian exactly

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

## 5. Nonlinear and amplitude changes touch only incident edges

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

## 6. Core integration uses the proved convex-box bound

Set z_S=0 and retain the actual local phase/amplitude on the T coordinates.
Its Gaussian is the principal covariance K_TT^-1, and its exponent beyond
the quadratic part is exactly of the type handled in sections 1--3 of the
corrected local first-loop proof. Deleting coordinates does not worsen the
uniform diagonal dominance or local degree. Its potential is stationary
at zero; its nonlinear phase starts at degree three. The finite amplitude
has O(h) constant log terms on at most m edges, which contribute O(mh).

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
radius-one core, as explained in global_bent_contour.md, section 6. Thus
no unproved large-radius extension of a local Taylor heuristic is used.

## 7. Determinant ratio costs only the large-coordinate count

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

## 8. What this improves and what remains

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
