# Near-flatness-scale joint delay barriers from a closed clock hierarchy

**VERIFICATION-PENDING.** Candidate continuation of BGS-TRACE-055.
Finite word identities do not certify the stopped asymptotic moment induction.
The all-time entry-flat event and microscopic cavity identification are unproved.


8 October 2026. Research continuation outside the repository. This strengthens delay_bootstrap.md. The entry-flatness hypothesis remains unproved here. The argument uses the exact same Schur process, original reused phases, fresh uniform coordinate selection, and positive incoming/outgoing delays. External priority is not established.

## Statement

Let ell=log(2N). Fix K and kappa>0 and put m=ceil(ell^(1+kappa)), m<N. Consider the all-time event A that every retained size u≥m satisfies max_ij |(S_u)_ij|²≤K ell/u. Let epsilon=ell^(−kappa/16). There is a joint stopping scheme such that

P(A intersect {some incoming or outgoing normalized diagonal delay exits [1−epsilon,1+epsilon] at a size u≥m})
 ≤ C_(K,kappa) ell^(−kappa/16),                           (1)

and every fixed killed normalized clock moment

M_k(u)=1_{alive at u} u^(k−1) Tr(T_u^k)/N^k

has expectation bounded by a constant C_k, uniformly in N and u≥m. In particular the sharper identities from delay_bootstrap.md still give E M_2≤2+o(1), E M_3≤6+o(1). No unrestricted high delay moments are claimed.

The auxiliary stop also includes a scale-dependent cap on one fixed sufficiently high moment M_p. Its exit probability has the same bound in (1). Thus the theorem supplies the full joint good event with that cap. The constants and the sufficiently-large-N threshold may depend on K,kappa,p. No limit with growing p is asserted.

## 1. Convex clock mechanism

For one elimination, let e be its coordinate, v=S*e, and q=w/(1−S_ee w). The delay congruence T'=K*TK satisfies

K K*=I+q e v*+conj(q) v e*=:R_w≥0,   E_w R_w=I.           (2)

Nonzero eigenvalues of K*TK and T^(1/2) R_w T^(1/2) agree. Convexity of X↦Tr X^k on positive matrices, k≥1, gives

E_w Tr(T'^k)≥Tr(T^k).                                  (3)

This supplies a nonnegative submartingale for every frozen raw trace power, not just k=2. The trace-power convexity follows, for example, because Tr X^k=||X||_k^k and the Schatten norm satisfies the triangle inequality; composing that norm with the increasing convex power preserves convexity.

## 2. Closed upper recurrence before a joint diagonal exit

Assume both T_ee and Q_ee=(STS*)_ee are ≤L_u=A0 N/u, A0=1+epsilon, for every live e. Also assume delta_u≤1/4; this holds eventually above m. Then |q|≤2.

Expand Tr[(T R_w)^k]. A term with r≥2 rank-one insertions is a cyclic word with powers T^{n_1},...,T^{n_r}, n_i≥1, sum n_i=k. Each inserted rank-one factor has endpoints in {e,v}. Positivity and Cauchy–Schwarz bound its absolute trace by a product of diagonal moments of e and v. Put l=k−r+1. Log-convexity of scalar spectral moments gives, for 1≤n≤l and l>1,

<x,T^n x>≤<x,T x>^((l−n)/(l−1)) <x,T^l x>^((n−1)/(l−1)), x=e,v.

In the product, the total exponent on the first moments is r−1 and the total exponent on the l-th moments is 1. Weighted arithmetic–geometric mean therefore bounds the word by

L_u^(r−1) [lambda (T^l)_ee+(1−lambda)(Q^l)_ee]

for some 0≤lambda≤1 depending only on the word. For l=1, the same bound follows directly by weighted AM–GM of the first moments. Neither T nor S is assumed to commute, and the moments in the outgoing vector are Q^l=S T^l S*.

There are binomial(k,r) placement choices and at most 2^r choices of rank-one orientation. Each phase monomial has modulus at most 2^r. The linear term averages to zero because E q=0. Averaging the uniform eliminated coordinate gives the explicit rough bound

E[Tr(T'^k) | past]
 ≤ Tr(T^k)+sum_(r=2)^k binomial(k,r) 4^r L_u^(r−1) Tr(T^(k−r+1))/u.       (4)

This is an upper estimate, not a limiting moment recursion. It retains all noncommuting cyclic words.

Kill normalized moments at the first flatness, either diagonal, or auxiliary moment-cap failure. Dropping the positive crossing contribution, (4) gives

E[M_k(u−1) | past]
 ≤ (1−1/u)^(k−1) M_k(u)
   +(1−1/u)^(k−1)/u sum_(r=2)^k binomial(k,r)4^r A0^(r−1) M_(k−r+1)(u).  (5)

The killed first moment has expectation at most 1. Since A0≤2 eventually, induction works with C_1=1 and

C_k=max(1,sum_(r=2)^k binomial(k,r)4^r 2^(r−1) C_(k−r+1)).               (6)

Indeed 1−(1−1/u)^(k−1)≥1/u. All these constants are deliberately rough, finite for each fixed k, and independent of the auxiliary cap. For k=2,3 use the sharper exact identities in the earlier note instead of (6).

## 3. Freeze the crossing state and vary the cap with size

Fix a moment order p≥2 and an exponent 0<zeta<p−1. Define the live cap

B_u=B (u/m)^zeta,   B≥1,

on Y_p(u)=u^(p−1) Tr(T_u^p)/N^p. Stop at its first exit too.

Freeze Z_p=Tr(T^p) at the FULL crossing state and then keep it constant. By (3) it is a nonnegative submartingale. Summing (4) and using the killed lower-moment bounds (5) yields

E Z_p(frozen, size v)≤C_p N^p/v^(p−1).                  (7)

This uses only pre-exit moments: each increment bound is multiplied by the indicator of survival before that transition. A later exit caused by any other barrier is frozen in exactly the same way.

In a dyadic block u in [v/2,v], a first cap crossing forces

Z_p≥c_zeta B (v/m)^zeta N^p/v^(p−1).

Doob's nonnegative-submartingale maximal inequality and (7) bound its probability by C_p B^−1(m/v)^zeta. Summing dyadic blocks down to m gives

P(any cap exit before the other stop)≤C_(p,zeta)/B.      (8)

There is no factor log N in (8). The scale-dependent cap is larger in the large cavity, and its growth exponent is smaller than the available variance decay.

## 4. Variance from the p-th clock moment

For a live normalized input diagonal x_j=uT_jj/N, the exact drift and fixed-label freezing convention are as in delay_bootstrap.md. On a block starting at v, keep only the v labels then alive; each is frozen when eliminated, and all are frozen at the joint stop. Before an exit,

(T²)_jj≤||T|| T_jj≤A0 N² B_u^(1/p)/u^(2−1/p).

The same holds for Q. The previously derived scalar increment estimates therefore give

|xi_(u,j)|≤C_K sqrt(ell/u),
E[xi_(u,j)² | past]≤C_K ell B_u^(1/p)/u^(2−1/p).          (9)

Consequently the block predictable variance is bounded by

V_v≤C_K ell B^(1/p) m^(−zeta/p) v^(−(p−1−zeta)/p),
J_v≤C_K sqrt(ell/v).                                  (10)

These bounds include the crossing increment. They are conditioned only on the past, not on next-step survival or on the full future flatness event.

## 5. Count only live labels in each block

For any fixed r0>0, choose

h_v=C_(r0)[sqrt(V_v log(2v))+J_v log(2v)].               (11)

Freedman's two-sided maximal bound makes the failure probability at most v^(−r0−3) per scalar label, after enlarging the constant. Conditional on the block's starting history there are only 2v active input/output labels. A union bound followed by summation of dyadic blocks yields a total failure probability O(m^(−r0−2)). Removed labels from earlier blocks have no increments and must not be counted as new martingales in this block.

The same pathwise drift argument as in delay_bootstrap.md gives no N/m amplification. Because zeta<p−1, summing (11) over blocks gives

sup_j,u |normalized delay−1|
 ≤ C [sqrt(ell B^(1/p) log(2m)/m^(1−1/p))
       +sqrt(ell/m) log(2m)+ell/m]                      (12)

outside the preceding exceptional martingale event, until the first flatness or cap exit. The homogeneous propagation norm is at most exp(C_K ell/m), and within each block the sum of drift-matrix norms is bounded. The summation of logarithms times geometrically decreasing powers is bounded by a fixed constant times the endpoint expression in (12).

## 6. Parameter choice at depth ell^(1+kappa)

Take a=b=eta=kappa/16, epsilon=ell^−a, B=ell^b, and fix p so large that

(p+2ap+b+p eta)/(p−1)<1+kappa.

For example any integer p with p−1>4(1+kappa/4)/kappa suffices. Fix zeta=(p−1)/2. The first term of (12) is o(epsilon), because

m^(1−1/p)≥ell^(1+2a+b/p+eta)

eventually and the spare ell^eta dominates log(2m). The second term is also o(epsilon), since the displayed depth exponent exceeds 1+2a. The deterministic drift is smaller still. Thus diagonal exits on A require a cap exit or a martingale exception. Equations (8) and (11) yield (1), including the auxiliary cap, with O(ell^−b)+O(m^−r0).

This proof is a conditional delay theorem: no bound for P(A^c) has been established. If such a bound p_N is available, it must be added. In particular the manuscript's unproved all-time entry-flatness statement only claims a deeper cutoff; this note cannot extend that flatness theorem below its own range. It shows that delay concentration can in principle run down to arbitrarily small fixed powers above log N once the corresponding entry flatness is given.

## Verification status

The proof is being independently checked. The earlier square/cubic identities were checked separately by Python phase quadrature and by exact Gaussian-rational C++ arithmetic. Those computations do not certify (1), (4) or the asymptotic concentration theorem. No Lean formalization is claimed.
