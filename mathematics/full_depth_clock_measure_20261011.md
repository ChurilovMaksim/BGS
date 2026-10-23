# Full-depth clock measure, exact rank atom and inverse-Jacobi comparison

**Stable claim:** BGS-TRACE-060, reference-measure and exact-rank components.
**State:** PROVED as an algebraic reference proposition and a pathwise rank
bound. Application as an actual random-Schur limit is CONDITIONAL on the
entry-flatness premise of [the all-fixed-order theorem](conditional_clock_universality_20261011.md).
**Review:** independent internal reconstruction, 11 October 2026, base
`b126cfb18f445b82358fc156632873082ac22503`.
The [review packet](../archive/evidence/executions/20261011/clock-universality/README.md)
preserves the exact input. Endpoint moments and the free-Jacobi family are
prior objects; no world-priority or actual matrix-freeness claim is made.

## 1. Reference moments and a probability measure

For x in [0,1] let M_x(z) be the formal root at z=0 of

 (1-xz) M_x(z)^2-[1-(1-x)z]M_x(z)+z=0,  M_x(0)=0.

Define f_r(x)=[z^r]M_x(z). They are fixed polynomials, and Lagrange
inversion gives the closed finite expression

 f_r(x)=(1/r)[t^(r-1)] ((1+t)(1-xt)/(1-t))^r.           (1)

The first five are 1, 2-x, 6-6x+x^2, 22-32x+12x^2-x^3 and
90-170x+100x^2-20x^3+x^4. At x=1 every f_r=1.

Put a_x=3-x-2 sqrt(2(1-x)), b_x=3-x+2 sqrt(2(1-x)).
For 0<=x<1 define

 mu_x(dh)=w_x delta_x(dh)
  +sqrt((b_x-h)(h-a_x))/(2 pi h(h-x)) 1_[a_x,b_x](h) dh,

 w_x=0 for x<=1/2, and w_x=2-1/x for x>1/2.           (2)

At x=1 put mu_1=delta_1; the continuous density has zero mass there.
For every x, (2) is a probability measure with moments f_r(x).

Proof. The transform determined by (1) is

 G_x(w)=[3w-1-x-sqrt(w^2-(6-2x)w+(1+x)^2)]/[2w(w-x)],
 G_x(w)=(1+M_x(1/w))/w.                               (3)

Choose the square root analytic off [a_x,b_x], asymptotic to w at infinity.
In particular it is negative below a_x on the real axis. The identity
a_x-x=(sqrt(2(1-x))-1)^2 proves a_x>=x. Stieltjes inversion on the
cut gives the positive density in (2). The point w=0 is removable;
at x=0 the double denominator is removable by Taylor expansion:
3w-1-s_0(w)=-4w^2+O(w^3). In fact G_x(0)=-2/(1+x) for every x,
so there is no atom at zero. For x>0 the atom test gives

 lim_(eta downarrow 0) i eta G_x(x+i eta)
                         =[2x-1+|2x-1|]/(2x)=w_x.

For x different from 1/2 this is the ordinary residue, after removing
any canceled pole. At x=1/2 it is a branch endpoint and the limit, rather
than a meromorphic residue, is the relevant notion. For x=1 the
root is w-2 and (3) is exactly 1/(w-1). At x=1/2 the merging pole
and branch endpoint produce an integrable inverse square-root density,
with no atom; explicitly its density is
sqrt(9/2-h)/(2 pi h sqrt(h-1/2)). There are no other singularities. The Cauchy reconstruction
of (3) from its jump and residues, together with G_x(w)~1/w, proves
total mass one and the asserted moments. The supports are uniformly
bounded by b_0=3+2 sqrt(2), so the moments determine the measure.

The formal characteristic relation is

 z=M(1-M)/[(1+M)(1-xM)].                              (4)

Differentiating at x=exp(-tau) verifies

 partial_tau M=M+z partial_z M[-1+2M/(1-M^2)],
 M(z,tau=0)=z/(1-z).

It follows that the moments solve

 partial_tau f_r=-(r-1)f_r+r[z^r]{-log(1-M^2)},
 f_r(1)=1.                                           (5)

This calculation identifies a reference measure, not a realization of the
ideal entry data by a finite matrix.

## 2. An exact finite-dimensional rank constraint

For the genuine feedback process starting with T_N=I, multiply the
successive embedding matrices K to obtain an N-by-u matrix L_u with
T_u=L_u^*L_u. For each original surviving label its row of L_u is the
corresponding retained coordinate row: no elimination changes that row.
After reordering the original surviving labels first, L_u=[I_u;X_u].
Consequently

 T_u=I_u+X_u^*X_u,
 rank(T_u-I_u)<=N-u,
 dim ker(T_u-I_u)>=max(0,2u-N).                       (6)

This does not assume flatness or a random-matrix law. The empirical
measure of H_u=uT_u/N has an atom at x=u/N of weight at least
max(0,2-1/x). It need not equal that bound for an arbitrary starting
unitary. The reference (2) saturates exactly this lower bound.
No finite-N equality of rank is inferred.

## 3. Exact comparison with the prior free-Jacobi family

For 0<x<=1, set p=x/(1+x), q=2x/(1+x). In a free-projection reference
space, let P,Q be free projections of traces p,q and let Y=PQP be
viewed in the normalized corner P. Its free-Jacobi density is

 sqrt((y-lambda_-)(lambda_+-y))/(2 pi p y(1-y)),
 lambda_+-=[sqrt(p(1-q)) +/- sqrt(q(1-p))]^2.

The primary-source convention is the full trace. Remove the zero mass
outside P and divide by p to obtain the normalized corner:

 nu_P=[nu_full-(1-p)delta_0]/p.

It has no atom at zero since q>=p and an atom at one of weight
max(p+q-1,0)/p. With these parameters lambda_-=x/b_x and
lambda_+=x/a_x. The transformation H=x/Y pushes that density and
atom precisely to (2); at x=1, q=1 and H=1.

The equilibrium free-projection distribution is a prior law. For source
comparison, Hamdi, arXiv:1711.07382v1 (2017), introduction, Theorem 1.1
and equations (3.1), (4.1), describe the full-trace atom conventions and the
equilibrium density; the corner normalization must be divided by p after
removing the outside-P zero mass. No freeness of actual Schur matrices is
proved by this dictionary. The inverse-Jacobi representation can supply
independent reference computations, but cannot establish the entry-flatness
probability or a CUE eigenphase law.


## 4. Application and checks

For the empirical law of uT_u/N, the all-fixed-order theorem identifies
all moments with this family uniformly over u>=m, on the stated
intersection with the entry-flat event. Its weak-law consequence uses
compact moment determinacy and higher fixed moments for tail control.
It does not prove the probability of the flat event. The exact rank bound
above is unconditional on every trajectory where feedback is defined.

The finite [reference verifier](../computations/verification/clock_reference_measure.py)
checks polynomial identities through order eight in exact rational
arithmetic, including the repaired positive-gap compensation count. A
separate 60-digit quadrature checks mass and moments zero through four at
eight fixed x values, including 0, 1/2 and 1. That quadrature is a numerical
diagnostic; it is not a certified integral bound or a proof of the measure.
The analytic Cauchy reconstruction above proves the measure for every x.

No edge law, growing-order estimate, freeness of actual matrices,
microscopic eigenphase law or global BGS follows from the dictionary.
