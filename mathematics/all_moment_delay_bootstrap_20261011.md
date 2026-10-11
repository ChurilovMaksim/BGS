# All fixed clock moments and near-flatness-scale joint delay barriers

**Stable claim:** BGS-TRACE-060, strengthened conditional scope.
**State:** CONDITIONAL on the displayed all-time entry-flatness event.
**Review:** the near-flatness bootstrap was independently reconstructed on
11 October 2026 from its preserved 8 October candidate. No flatness
probability, growing-order uniformity, unrestricted high moments, equality
law above order three, scalar microscopic law or BGS conclusion is asserted.
The second/third equality extension in Section 7 was independently reconstructed
separately on the same date. Both reviews cover analytic arguments; the
finite computations have narrower scope.

The original candidate and its exact review input are preserved in the dated
[cavity packet](../evidence/executions/20261011/cavity-continuation/README.md).
Use the process and first-delay formulas of
[the preceding bootstrap](delay_bootstrap_20261011.md). Constants and the
threshold N0 may depend on fixed K, kappa, p, zeta and concentration exponents.

## Statement

Let ell=log(2N). Fix K and kappa>0 and put m=ceil(ell^(1+kappa)), m<N. Consider the all-time event A that every retained size u≥m satisfies max_ij |(S_u)_ij|²≤K ell/u. Let epsilon=ell^(−kappa/16). There is a joint stopping scheme such that

P(A intersect {some incoming or outgoing normalized diagonal delay exits [1−epsilon,1+epsilon] at a size u≥m})
 ≤ C_(K,kappa) ell^(−kappa/16),                           (1)

and every fixed killed normalized clock moment

M_k(u)=1_{alive at u} u^(k−1) Tr(T_u^k)/N^k

has expectation bounded by a constant C_k, uniformly in N and u≥m. In particular the sharper identities from delay_bootstrap.md still give E M_2≤2+o(1), E M_3≤6+o(1). No unrestricted high delay moments are claimed.

The cap is tested on the un-killed normalized trace, including a crossing simultaneous with another barrier. The auxiliary stop also includes a scale-dependent cap on one fixed sufficiently high moment M_p. Its exit probability has the same bound in (1). Thus the theorem supplies the full joint good event with that cap. The constants and the sufficiently-large-N threshold may depend on K,kappa,p. No limit with growing p is asserted.

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

## Review boundary

A separate internal reviewer reconstructed the noncommuting word estimate,
the killed-moment induction, the complete crossing-state submartingale,
the scale-dependent cap, the live-label union bound, the adapted pathwise
drift estimate and the parameter choice. The verdict was proved as written
for this conditional theorem. It is internal review, not external refereeing.
Exact finite words are supplementary controls, not the universal proof.

## 7. Uniform second and third equality laws

This continuation does not use the unproved diagonal-square or fourth-law
induction. Its separate independent internal reconstruction passed; the
exact reviewed input is retained in the dated evidence packet.
Write Y_k(u)=u^(k-1)Tr(T_u^k)/N^k for the un-killed quantity and
f_2(x)=2-x, f_3(x)=6-6x+x^2. At m=ceil(ell^(1+kappa)), the separately reviewed stronger
conclusion is

$$\mathbb P\left(\mathcal A_m\cap
 \left\{\max_{N\ge u\ge m,\,k=2,3}|Y_k(u)-f_k(u/N)|
                         >C_{K,\kappa}\ell^{-\kappa/32}\right\}\right)
 \le C_{K,\kappa}\ell^{-\kappa/16}.\tag{13}$$

It is still an intersection-probability theorem. If additionally
P(A_m^c)->0, it yields actual convergence in probability and convergence
of the corresponding killed expectations; it does not bound unrestricted
moments on the exceptional event.

### A trace-noise estimate from the complete word bound

On a pre-exit step set H=uT/N and V=uQ/N. All incoming/outgoing first
diagonals are at most A0=1+epsilon. The rank-two expansion of
Tr[(H R_w)^k]-Tr H^k contains words with r>=1 insertions, whose positive
gaps have sum k. After squaring their absolute values, positivity gives a
product of 2r diagonal spectral moments with total degree 2k. Interpolate
between order one and l=2k-2r+1. For r<k, the total high-moment exponent
is (2k-2r)/(l-1)=1 and the first-moment exponent is 2r-1. Weighted AM-GM,
followed by uniform-coordinate averaging, gives at most
A0^(2r-1) Tr H^l/u. For r=k use first-moment AM-GM directly. The fixed
number of words and |q|<=2 are absorbed into C_k.

Every lower normalized moment is bounded by a constant times
1+Y_(2k-1), by interpolation of the positive empirical spectral measure;
also Y_k^2<=Y_1 Y_(2k-1)<=A0 Y_(2k-1). The normalization change from u
to u-1 contributes at most C_k Y_k^2/u^2. Consequently the FULL increment,
before testing next-step survival, satisfies

$$\mathbb E[(\Delta Y_k)^2\mid\mathcal F_u]
 \le\frac{C_k[1+Y_{2k-1}(u)]}{u^2}.\tag{14}$$

Use one joint stop containing flatness, the first-diagonal and high-moment
barriers, and auxiliary bounds Y_2<=4, Y_3<=10. Freeze each normalized
trace at its complete crossing value, with the normalization of the crossing
size permanently fixed thereafter. This frozen quantity is distinct from
both the original Y_k and the killed M_k. For its martingale differences xi_k,
the killed fixed-order hierarchy bounds the EXPECTED predictable variation:

$$\mathbb E\sum_{u=m+1}^N\mathbb E[\xi_{k,u}^2\mid\mathcal F_u]
 \le C_k\sum_{u=m+1}^N u^{-2}\le C_k/m.\tag{15}$$

Only survival BEFORE the increment occurs in this sum. After the stop the
increment is zero. Doob's scalar L2 maximal inequality gives
E max |sum xi_k|^2<=4 C_k/m. It follows directly from the usual stopping
proof and Cauchy-Schwarz: E M*^2<=2 E[M*|M_final|].
No deterministic predictable-variance bound is inferred from an expectation.

### Stable drifts from the exact square/cube identities

The preceding bootstrap's exact identities, uniform coordinate selection,
|a|^2<=delta_*=K ell/m, and the first-diagonal barriers give

$$\mathbb E[Y_2(u-1)\mid\mathcal F_u]
 =(1-1/u)Y_2(u)+2(u-1)/u^2+O((\epsilon+\delta_*)/u),\tag{16}$$

$$\mathbb E[Y_3(u-1)\mid\mathcal F_u]
 =(1-1/u)^2Y_3(u)+6(u-1)^2Y_2(u)/u^3
                         +O((\epsilon+\sqrt{\delta_*})/u).\tag{17}$$

For (17), t_e and s_e each equal (N/u)(1+O(epsilon)), so averaging
t_e(Q^2)_ee+s_e(T^2)_ee gives 2N Tr T^2/u^2 with the displayed relative
error. Positivity gives |(ST)_ee|<=sqrt(t_e s_e); therefore the remaining
cubic coherent term has normalized size at most C sqrt(delta_*)/u.
The auxiliary Y_2 bound makes the drift errors absolute constants times
the displayed quantities.

The exact residuals are R_2(u)=2/u^2 and
R_3(u)=18/u^2-12/u^3-6/(uN)+6/(u^2N), both uniformly O(u^-2)
for u<=N. The reference curves satisfy -x f_2'=-f_2+2 and -x f_3'=-2f_3+6f_2, with f_2(1)=f_3(1)=1.
Their Euler factors are deterministic, nonnegative and contractive.
For z_(u-1)=a_u z_u+e_u+xi_u, 0<=a_u<=1, the filtered noise is bounded
by twice the maximum of the raw partial martingale, by summation by parts.
An error bounded by eta/u costs O(eta), since
1-a_u is comparable to 1/u. Thus, pathwise until the stop,

$$\max|Y_2-f_2|\le C(\epsilon+\delta_*+m^{-1}+M_2^*),$$
$$\max|Y_3-f_3|\le
 C(\epsilon+\sqrt{\delta_*}+m^{-1}+M_2^*+M_3^*),\tag{18}$$

where M_k* is the maximal raw partial martingale. Formula (18) includes
the transition causing the first auxiliary trace exit. Since f_2<=2 and
f_3<=6, neither trace cap can be the first exit outside the small martingale
event. Extra stops only reduce killed moments and do not invalidate the
earlier diagonal/cap estimates.

Take eta=ell^(-kappa/32). Then epsilon=ell^(-kappa/16)=o(eta),
sqrt(delta_*)=O(ell^(-kappa/2))=o(eta), and
P(M_2*+M_3*>eta)<=C/(m eta^2)=O(ell^(-1-15kappa/16)). Add the previously
proved joint cap/diagonal exceptional probability O(ell^(-kappa/16)).
This proves (13), with constants enlarged to include small initial sizes.
For fixed sufficiently large N the required m<N and flatness pre-exit
conditions hold.

On survival Y_k^2<=A0 Y_(2k-1), whose killed expectation is bounded.
This supplies uniform integrability. Hence if P(A_m^c)->0 is separately
proved, the killed second and third expectations converge to f_2(u/N)
and f_3(u/N), uniformly over the planned sizes. The fourth equality law and
all-order Schroeder law require further diagonal-power/coherence control.
