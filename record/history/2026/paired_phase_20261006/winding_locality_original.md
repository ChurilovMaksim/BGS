# Exact nonlinear winding-defect locality and a finite-group Fourier reduction

Author theorem candidate, 6 October 2026; independent review pending.
Base and current source hashes: source_manifest.json. No canonical edits.
All phases are the actual fixed-tau HJ phases, tau=10^-80. This is not an
initial-jet approximation. Transport determinants and exact quantum box
integrals are explicitly outside the phase-only conclusion below.

## 1. Targeted displacement and conclusion

Let S=[[3,4],[2,3]], lambda=3+2sqrt(2), and G_m=Fix(S^m on T²).
The perfect pairing from paired_character_identity.md identifies the
particular displacement

d_m=(S^m-I)^-1(0,1) mod Z²

with the q-character: B_m(z,d_m)=q mod1 for z=(q,p). This is the label
change obtained by adding one to a single winding coordinate. It has a
homoclinic-type orbit displacement localized around that time coordinate.
For odd N this displacement is NEVER in ker N: its p-coordinate is -1/2.
The other resonant N-torsion sectors are not removed or estimated here.

Let Delta_(tau,m)(z) denote the exact stationary action minus its cat action,
and define its unit-winding defect

D_(tau,m)(z)=Delta_(tau,m)(z+d_m)-Delta_(tau,m)(z).

There is a continuous periodic function D_(tau,infty) on T², defined by the
actual infinite bounded stationary-correction equation below, such that

sup_(z in G_m)|D_(tau,m)(z)-D_(tau,infty)(z)|
 <=216 eta 2^-m,                                      (L1)

where eta=10^10 tau+10^50 tau²<2*10^-70 is a valid real per-edge C² bound
for S_r(tau)-S_r(0). Also

||D_(tau,infty)||infty<=2eta,
[D_(tau,infty)]_(C^alpha)<=10^4 eta,
alpha=log(2)/log(lambda)>0.                            (L2)

Constants are deliberately nonoptimal. Consequently the EXACT nonlinear
phase-only selected autocorrelation coefficient

K_(m,N)=|G_m|^-1 sum_(z in G_m)
 e(N B_m(z,d_m)) e(N D_(tau,m)(z))

satisfies

K_(m,N)=integral_(T²) e(N[q+D_(tau,infty)(q,p)])dqdp
              +O(N 2^(-m/2)),                        (L3)

uniformly in m and integer N>=1. In particular the error is exponentially
small through every fixed m~N band, with no exponential-in-m prefactor.
No coprimality or omission of a finite-group alias is used.

The remaining phase-only problem is Fourier decay of ONE explicit measure
mu_tau=(q+D_(tau,infty)(q,p) mod1)_*(dqdp):
K_(m,N)=muhat_tau(-N)+O(N2^(-m/2)). The fact that mu_tau is a small continuous
perturbation of uniform measure does NOT imply that these coefficients tend
to zero. No such Fourier-decay theorem is asserted here.

## 2. Weighted resolvent bounds, with m=1,2 included

Use K_0=B_m/4 and cyclic distance dist_m. For a matrix define

||A||_w=max_i sum_j 2^(dist_m(i,j)) |A_ij|.

The metric triangle inequality makes this norm submultiplicative.
For m>=2, the diagonal of K_0 is 3/2. The weighted off-diagonal row sum is
at most 1, including the repeated neighbour at m=2. Therefore its Neumann
series gives ||K_0^-1||_w<=2. For m=1, K_0=1 and the bound is immediate.
Its unweighted inverse row sum is exactly one.

Write R_tau=Phi_tau-Phi_0. The real source estimates give every edge derivative
through order two the bound eta above. The cyclic Hessian E=R_tau'' therefore
has weighted row norm <=6eta: its diagonal costs at most 2eta and the two
weighted neighbour entries cost at most 4eta. At m=1 the combined self-entry
costs only 4eta; at m=2 the combined neighbour gives the same 6eta bound.

For every real point, and likewise for every average of these Hessians,

G_tau=(K_0-E)^-1,
||G_tau||_w<=2/(1-12eta)<=3,
||G_tau-K_0^-1||_w<=36eta.                            (L4)

These are exact fixed-coupling bounds; no length m enters their constants.
The same proof works on Z, with distance |i-j|, and on principal intervals.

## 3. Finite-dimensional stationary-action identity

Allow real branch and winding parameters as an interpolation device only.
The actual phase S_r(t,x,y)=S_0(t,x,y+r) is defined for real r by HJ uniqueness.
For each (r,nu), the strictly concave lifted action has a unique stationary
point x_tau and stationary value F_tau(r,nu). Let F_0 and x_0 be their cat
counterparts. Differentiating the stationary equation and the envelope gives

partial_(nu_i) F_tau=x_(tau,i),
partial_(nu_j)x_(tau,i)=(G_tau)_ij.                   (L5)

The nonlinear correction u=x_tau-x_0 satisfies
K_0 u=grad R_tau(x_0+u). The inverse row sum one and
||grad R_tau||infty<=2eta imply ||u||infty<=2eta.
Thus

D_i(F_tau-F_0):=(F_tau-F_0)(r,nu+e_i)-(F_tau-F_0)(r,nu)
 =integral_0^1 u_i(r,nu+s e_i)ds.                    (L6)

In particular its absolute value is <=2eta. From (L4-L5),

|partial_(nu_j) D_i(F_tau-F_0)|<=36eta 2^(-dist_m(i,j)).

For branch parameters, the cat mixed derivative is the local vector
f_j=(1/4)e_j-(3/4)e_(j+1), with weighted matrix norm <=7/4. Its nonlinear
correction has weighted norm <=3eta. Hence

||partial_r x_tau-partial_r x_0||_w
 <=36eta*(7/4)+3*(3eta)=72eta,
|partial_(r_j) D_i(F_tau-F_0)|<=72eta 2^(-dist_m(i,j)). (L7)

These estimates prove exact locality in orbit-code coordinates. For example,
in a canonical cat lift r_j lies in {0,...,6} and nu_j in {0,...,4}.
Freezing only coordinates farther than R changes this action defect by at
most 1152eta 2^-R. At m~N a logarithmic window therefore controls its phase
to any specified polynomial precision. This does not claim a bounded C¹
norm after pulling the code back to initial torus coordinates.

## 4. Infinite bounded correction: no infinite action sum is required

On Z let K_0 have diagonal 3/2 and neighbours -1/4. Its Green kernel is

g_j=(1/sqrt(2))lambda^(-|j|),  sum_j g_j=1.

Let z=(q,p) on T² and take the unwrapped cat background x_j^0=(S^j z)_q.
For 0<=s<=1 set b_j=x_j^0+s g_j. Define u_s(z) in ell-infinity(Z) by

K_0 u_s=grad R_tau(b+u_s),                            (L8)

where R_tau is understood locally as the sum of edge corrections
S_0(tau,x_j,x_(j+1))-S_0(0,x_j,x_(j+1)); only its local gradient is used.
The right side has sup norm <=2eta and Lipschitz constant <=4eta in u.
Convolution with g is therefore a strict contraction on ell-infinity.
It has a unique bounded fixed point with ||u_s||infty<=2eta.
No convergence of an infinite stationary action is asserted or needed.

Set D_(tau,infty)(z)=integral_0^1 u_(s,0)(z)ds.
Integer changes of the initial lift give integer cat position/momentum
changes. The phase-correction gluing
R_0(x+a,y+3a+4b)=R_0(x,y), a,b integers,
makes the local equation and its solution unchanged. Thus D_infty is a
well-defined periodic function of z.

For z in G_m, the cat background coefficients are m-periodic after the
same integer gluing. The finite-cycle Green column is the exact periodization

g_j^(m)=sum_(ell in Z) g_(j+ell m).

Replacing g_j by g_j^(m) in (L8) gives an m-periodic fixed point by uniqueness;
it is exactly the correction in (L6) for the finite winding increment.
Interpolate between these two backgrounds. The derivative of u_0 with
respect to a background coordinate j is bounded by
18eta 2^(-|j|), from ||G_tau E||_w<=18eta. Therefore

|D_m(z)-D_infty(z)|
 <=18eta sum_j 2^(-|j|) sum_(ell!=0) g_(j+ell m).

The inequality
sum_j 2^(-|j|)lambda^(-|j+L|)
 <=2^(-|L|) (1+2/lambda)/(1-2/lambda) <3*2^(-|L|)
and summation over nonzero ell bound the last expression by
216eta 2^-m. This proves (L1), including m=1,2.

## 5. Holder pullback instead of an exploding C¹ estimate

The local gradient in (L8), expressed in cat (q,p) variables, is periodic
and Lipschitz with constant at most a fixed numerical multiple of eta.
Both forward and backward cat iterates obey
||S^j||<=4lambda^|j|. Compare the fixed-point equations for z,z' and use
the weighted inverse (L4). With d=dist_T²(z,z'), this gives

|u_(s,0)(z)-u_(s,0)(z')|
 <=96eta sum_(j in Z)2^(-|j|) min(1,4lambda^|j|d).

Splitting the geometric sum at |j| approximately log(1/d)/log lambda yields
sum_j2^(-|j|)min(1,lambda^|j|t)<=10 t^alpha for 0<t<=1.
The trivial bounded estimate handles larger t. The numerical constant 10^4
therefore safely gives (L2) after integrating in s.

This avoids differentiating a growing symbolic cylinder partition. It does
not turn the limiting function into a C¹ or analytic torus function. The
actual-symbol first-response checks show why that stronger step is unsafe.

## 6. Exact finite-group grid and the Fourier quadrature bound

The periodic-grid/annihilator identities are prior project work in
mathematics/frozen_periodic_point_annihilator.md; they are reproduced here
only to check the normalization needed by the new Holder quadrature step.

Write S^m=[[a_m,2b_m],[b_m,a_m]], a_m²-2b_m²=1, and
U_m=gcd(a_m-1,b_m). Then

U_m=lambda^(m/2)-lambda^(-m/2),                  m odd,
U_m=(lambda^(m/2)-lambda^(-m/2))/sqrt(2),        m even.

U_m is a positive integer grid denominator, unrelated to the stationary
correction u_s.

For m=2r, use a_m-1=4b_r² and b_m=2a_r b_r. Since a_r is odd and
coprime to b_r, U_m=2b_r. For m=2r+1, write
(1+sqrt(2))lambda^r=P+Qsqrt(2), P²-2Q²=-1. Then
a_m-1=2P², b_m=2PQ and gcd(P,Q)=1, so U_m=2P.
These give the displayed formulas and U_m>=lambda^(m/2)/2.

In fact the physical fixed-point group is the rectangular coordinate grid

G_m=(U_m^-1 Z/Z)^2,                                  m odd,
G_m=(U_m^-1 Z/Z) x ((2U_m)^-1 Z/Z),                  m even.

For odd m, (S^m-I)/U_m has determinant -1. For even m it is
[[2b_r,2a_r],[a_r,2b_r]], determinant -2, and its entries verify the displayed
rectangle directly; its cardinality is D_m. Thus every finite-group alias
is retained, including all arithmetic resonances with N.

A uniform rectangular grid average of an alpha-Holder function differs
from its torus integral by at most C[f]_alpha U_m^-alpha, by comparing
each sample with its own cell. Applied to
f_N(z)=e(N[q+D_infty(z)]), whose Holder norm is O(N), this costs
O(N2^(-m/2)). Equation (L1) contributes only O(Neta2^-m).
This proves (L3). No derivative norm growing with m and no cylinder-count
prefactor enters this step.

## 7. Boundary of the result and next actual leaf

The localized displacement yields an explicit actual fixed-tau phase map
H_tau(q,p)=q+D_(tau,infty)(q,p) mod1 and the measure mu_tau in section 1.
Its Fourier decay is not established by the locality or Holder estimates.
Small C0 distance from q, positive variance of initial jets, and finite
Gauss cancellation do not establish the Rajchman property.

More importantly, the FULL alpha in paired_character_identity.md also has
leading transport, the actual determinant, Gaussian-box probability and the
exact local integral correction. No cancellation or locality theorem for
that entire weight is included in (L3). The result isolates an actual
nonlinear phase component with uniform error, while preserving these separate
obligations. It does not settle every displacement, N-torsion resonances,
the complete signed d,m sum, or TRACE-005.
