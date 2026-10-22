# Supplement to the frozen physical dictionary: graph-transform constants

This expands W5's finite estimate without changing its frozen bytes. Work in
fixed cat eigen-coordinates, delta=10^30 tau. Both F−diag(lambda,lambda^-1)
and its inverse counterpart have periodic C³ remainders bounded by delta.
Let R=10^8 delta and ||v||_(C^(1,1/2))<=R, with the norm defined as the maximum
of the sup, first-derivative sup and first-derivative half-Holder seminorms.
Changing to their sum only changes fixed harmless constants/ball radius.

Set M(x,t)=(c(x)+d(x)t)/(a(x)+b(x)t). The symplectic determinant is one.
For |t|<=R, denominators exceed 5.8, and

 |M_t|=1/(a+bt)^2<0.03,
 |M_tt|=2|b|/|a+bt|^3<delta,
 ||M_x||,||M_xx||,||M_xt||,||M_xxt|| <=100 delta,

with the same coarse bounds on the half-Holder differences on the compact
base domain. These follow by at most two spatial differentiations of the
rational expression; every nonconstant matrix-coefficient derivative is at
most delta and every denominator is >5.8. Bounds 100 delta may harmlessly
be replaced by 10^4 delta without changing any conclusion.

For y=F^-1x, ||Dy||<=6, while ||D²y|| and its half-Holder norm are O(delta).
The composition estimate for T(v)=M(y,v(y)) has highest-order difference
term M_t(y,v(y)) [D(v1-v2)](y) Dy. Its half-Holder coefficient is at most

 0.03 * 6^(3/2) <0.441.

All other difference terms contain a spatial derivative of a nonconstant
coefficient, a derivative of Dy, or M_tt times a bounded derivative of v.
The product/Hölder inequalities bound their combined coefficient by
10^12 delta times ||v1-v2||_(C^(1,1/2)). Thus the contraction factor is
<0.441+10^12 delta<1/2. The pure linear-map exact factor lambda^-1/2 quoted
in W5 is slightly sharper; this coarse proof is sufficient.

The forcing T(0)=c(F^-1x)/a(F^-1x) has norm <10^6 delta. Therefore
||T(v)||<=10^6 delta+(1/2)R<R, proving invariance of the ball. Iteration from
zero gives a unique C^(1,1/2) invariant unstable slope there. The stable
slope follows from F^-1 and interchanged eigencoordinates. Converting back
to p-versus-q slopes is a fixed rational map on a uniformly transverse cone,
so the 10^10 delta bound in W5 safely absorbs that conversion.

This is regularity of the tangent fields. Dependence of finite lifted leaf
graphs on their initial (q,p) is obtained separately from their ODE, on a
bounded Q-interval; no global all-time holonomy estimate is inferred just
from the field regularity.
