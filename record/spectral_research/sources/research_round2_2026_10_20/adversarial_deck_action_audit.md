> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round2_2026_10_20/adversarial_deck_action_audit.md`. Embedded SHA256: `9b9dca3ae8e238a2a4e0b0106d9d5adb3e37f50138e725901cca694d678da902`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/classical_trace.md).

# Independent audit of actual deck-action sensitivity

Input: `fermionic_deck_action_differencing.md`, SHA-256
`8202c59cbe0b9eb69a022ac1997dccaf00b1ae99fc611cf95308a926f7b2b140`.
The exact phase and principal quantum-amplitude inputs were checked in
the earlier all-time and twisted-pressure audits.

**Verdict: Sections 2--5 pass.** The uniform displacement derivative
estimates, persistent actual mixed curvature, and stated limitation of
termwise additive differencing are correct. They do not evaluate the
signed quantity needed for H_diag.

## 1. The cyclic inverse and all period lengths

For the unperturbed phase F_0(Q,q)=-(3Q^2-2Qq+3q^2)/8, the cyclic
position Hessian is -3I/2+(R+R^-1)/4. This formula also works for m=1,
where it is -I, and m=2, where the two closing-neighbor contributions
give off-diagonal entry 1/2. The perturbation Hessian has row and
column sums at most 4g_2.

Writing -H=(3/2)(I-B), the row and column norms of B are below 0.34.
Consequently the inverse norm is at most (2/3)/(1-0.34)=100/99<1.011.
Nearest-neighbor support gives a zero (i,j) entry of B^k when k is
less than cyclic distance. Summing the remaining series proves the
claimed exponential locality uniformly in m and the real displacement.
Negative definiteness and the bounded perturbation of a negative
quadratic form give existence and uniqueness of the critical point.

The explicit displacement forcing is -e_0 for nu_p, and
F_QQ e_0+F_Qq e_(m-1) for nu_q. When m=1 both terms are added in the
same coordinate; the l1 upper bound 1+2g_2 remains valid. Multiplication
by the inverse gives ||q_a||_1<1.02. Summing over oriented edge
coordinates counts each position derivative twice and adds at most
one explicit derivative of q_m=q_0+nu_q. Thus the first edge-derivative
sum is less than 2*1.02+1<4.

On differentiating stationarity twice, only third derivatives of the
perturbation occur in the forcing, since F_0 is quadratic. An edge
contributes a two-component vector of l1 norm at most
2g_3 |Y_a|_1 |Y_b|_1. Its embedding into cyclic positions has l1
operator norm one, including coincident positions. The total forcing
is at most 32g_3; inverse multiplication gives ||q_ab||_1<33g_3.
Every position second derivative appears twice among the edges, so
their sum is below 66g_3. These are uniform estimates derived from
finite-dimensional implicit differentiation, without a hidden uniform
implicit-function theorem.

## 2. Uniform action derivatives and real deck periodicity

Interpolate the fixed phase by F_sigma=F_0+sigma G for this derivative
calculation. The envelope identity gives
Phi_m(nu)=integral_0^1 sum_j G(Y_j^sigma(nu)) d sigma.
The preceding edge bounds give, respectively,

|Phi_m|<=m g_0,
|partial_a Phi_m|<=4g_1,
|partial_ab Phi_m|<=16g_2+66g_1g_3.

There is also a direct check of the asserted real-displacement
periodicity. For an integer w, shift the critical path at time j by
L^j w. This sends its endpoint displacement to nu+(L^m-I)w. The
exact deck law of G makes every edge perturbation G unchanged under
this integer edge shift, and F_sigma has the same critical-path
covariance for every sigma. The envelope integral is therefore
unchanged. This proves the periodicity of Phi_m for every real nu;
it does not require reducing a phase exponential modulo an integer.

## 3. Exact mixed curvature and its sign

The closing action is sum F(q_(j+1),q_j)-nu_p(q_0+nu_q/2).
Its envelope derivatives are exactly

partial_(nu_q) Scrit = p_0+nu_p/2,
partial_(nu_p) Scrit = -q_0-nu_q/2.

For A^m=((a,b),(c,d)) at the repeated origin, the endpoint derivative
is (A^m-I)^-1. Since its determinant is 2-a-d, the action Hessian is

1/(a+d-2) * [[c,(d-a)/2],[(d-a)/2,-b]].

In the linear reference L^m its diagonal entries agree, so the mixed
entry is zero. In the actual derivative
A=[[3,-4],[3s-2,3-4s]], s=-(9803 pi/125)tau, they differ by -4s.
Cayley--Hamilton gives
d_m-a_m=-4s sinh(m ell)/sinh ell,
tr A^m-2=4 sinh^2(m ell/2), ell=log Lambda_0.
The mixed perturbation curvature is therefore

-2s / sqrt((6-4s)^2-4) * coth(m ell/2).

It is positive. The denominator is less than 6 at the specified exact
tau, and pi>3 gives the strict lower bound 78 tau. Both critical
actions have zero displacement gradient at the origin. The mixed
derivative of exp(2 pi i N[Phi_m(nu)-Phi_m(0)]) consequently has
modulus exactly 2 pi N partial_(qp)Phi_m(0)>156 pi N tau.
No growing-time perturbative expansion is used in this computation.

## 4. Signed differencing and the precise limitation

The function a(n) on the finite deck group is well-defined by the
exact odd deck law, and its cyclic invariance under n -> L n comes
from re-starting the periodic orbit. For any M distinct shifts H,
translation of the complete sum and Cauchy--Schwarz give

|sum_n a(n)|^2 <= (D_m/M^2) sum_n |sum_(h in H) a(n+h)|^2
 = (D_m/M^2) sum_(h,k in H) C(h-k).

The diagonal C(0) is 1+O_C(1/N)+O(theta^(cN)) when cN<=m<=CN.
Indeed the exact amplitude modulus is Lambda_m^-1 exp(O(mh^2));
mh^2=O_C(1/N), and the difference between the already controlled
classical positive trace and sum Lambda_m^-1 is exponentially small,
using Lambda_m>=5^m.

If the off-diagonal autocorrelations in this Cauchy--Schwarz bound
are bounded individually in absolute value, even ideal zero values
leave D_m C(0)/M. For polynomial M this is exponentially large at
m comparable to N. This is a floor of that particular upper-bound
procedure, not a lower bound on the true trace. Signed negative
off-diagonal contributions can still cancel the diagonal; no
impossibility claim about that mechanism is made.

The persistent curvature rules out a uniformly C2-small multiplier
comparison with the unperturbed action at quantum frequency N.
It does not itself estimate a complete exponential sum. In particular
the required weighted distinct-orbit sum for the fixed admissible
test b_* remains unproved, exactly as the source records.
