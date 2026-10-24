# Single-anchor loop tests and logarithmic short-leg deletion

**Existing owner:** BGS-LOOP-001, extending the conditional mixed-hierarchy reduction in [loop_bridge.md](loop_bridge.md) and the maintained [frontier](../../../mathematics/fixed-map/fixed_map_resolvent_frontier.md). The existing registry ID is retained.

**Status:** exact project reductions, with independent internal proof review. The application of the characterization theorem remains conditional. Neither the actual long-long mixed residual nor the all-order hierarchy is proved. No external priority or full-source-proof audit is claimed.

## 1. Definitions, dependencies, and theorem statements

Let U_N be any deterministic N by N unitary sequence. For the actual family N runs through odd positive dimensions and U_N=exp(i tau N A_N)M_N, tau=10^-80, with unchanged quantization. Let alpha be uniform on [0,2pi), with expectations always over its **whole** probability space. Define

s_N(w)=N^-1 sum_j cot((theta_j-alpha)/2-w/N), w in C minus R,

and, for p>=1,

E_(p,N)(w_1,...,w_p)
=E[(s_N(w_1)^2+1) product_(j=2)^p s_N(w_j)]
 +sum_(j=2)^p E[T_N(w_1,w_j) product_(ell=2,ell!=j)^p s_N(w_ell)].

For a tuple w define D_(p,N)(w)=1+E max_(1<=j<=p)|s_N(w_j)|^(p+1). The existing hypothesis (H) is: for every fixed p>=1 and compact K subset C minus R, sup_(w in K^p)|E_(p,N)(w)|/D_(p,N)(w) ->0.

Here T_N(z,w)=partial_w[(s_N(z)-s_N(w))/(z-w)] and coincident arguments use its holomorphic extension, T_N(z,z)=s_N''(z)/2. Empty products are one. All traces and partial traces below are unnormalized.

**Theorem A (sufficient testing reduction).** Fix a countable dense D subset C minus R independent of N. The single-anchor relative conditions (A) and pointwise dense mixed conditions (B) below imply, for every fixed p and compact K subset C minus R,

sup_(w in K^p) |E_(p,N)(w)| ->0.

They therefore imply the existing compact-uniform relative hypothesis (H). All fixed compact-supremum moments of s_N are uniformly bounded. No uniformity in growing p or in compacts approaching the real axis is asserted.

**Theorem B (source-bound actual short-leg deletion).** Assume the FM-007 bound |Tr U_N^m|<=C N^(39/40) for 1<=m<=c_0 log N at all sufficiently large odd N. For any fixed 0<c<=c_0, K=floor(c log N), the normalized first mixed residual changes by O(N^(-1/40) log N) when its pair sum is restricted to m>K and its cubic sum to a,b>K. The denominator is the original full-resolvent denominator. Constants are uniform on each fixed positive compact height interval. No preliminary bound on the pair sum or microscopic moments is required.

**Identity C (tensor form).** For every N, unitary U, 0<q<1 and integer K>=0, the long pair and cubic sums are respectively Tr(F_K)/N^2 and Tr(F_K^2)/N^3, where

F_K=Tr_2[(q U tensor conjugate U)^(K+1)(I-q U tensor conjugate U)^(-1)].

The proofs follow below. Theorem A is an extension of the existing loop-bridge owner, using elementary Nevanlinna estimates and normal families. The conditional spectral conclusion uses P. Bourgade and J. Huang, *Loop Equations Characterize Random Matrix Statistics*, [arXiv:2607.07617v2](https://arxiv.org/abs/2607.07617v2), Theorem 1.9 and its moment estimates (2.14)–(2.24), with beta=2. It is a named external input, not a newly proved characterization. That theorem permits high-probability events and relative errors; this note uses the whole-space special case. It imposes no prescribed error rate or separate preliminary local law. FM-007 equation (9) in [frozen_seven_cut_reduction.md](../../../mathematics/fixed-map/frozen_seven_cut_reduction.md) supplies Theorem B's growing logarithmic trace input; its full upstream semiclassical chain is inherited, not independently recertified here.

## 2. Single-anchor sufficient criterion and moment bootstrap

Let N run through the intended sequence (odd N for the actual map). For each N let alpha be uniform on the circle, let

s_N(w)=N^(-1) sum_j cot((theta_j-alpha)/2-w/N),

and let E_{p,N} be exactly equation (3) of the companion [loop bridge](loop_bridge.md). All expectations in this note use the entire alpha space. Fix one countable dense D subset of C\R, independently of N.

(A) means: for every integer r>=2, at the one fixed tuple consisting of w_1=i, r-2 additional i's, and r copies of -i, there exists epsilon_{r,N}>=0 tending to zero such that

|E_{2r-1,N}| <= epsilon_{r,N}(1+E|s_N(i)|^(2r)).

No uniformity in r is assumed or obtained. (B) means: for every integer p>=1 and every fixed tuple in D^p that has both signs, 

|E_(p,N)(w_1,...,w_p)| / [1+E max_(1<=j<=p)|s_N(w_j)|^(p+1)] ->0.

No simultaneous or uniform convergence over D^p is assumed.

Set Z=s_N(i), M_t=E|Z|^t. For a Nevanlinna representation with measure mu and c>=0,

|s'(z)| <= Im s(z)/Im z <= |s(z)|/Im z,  Im z>0.

The differentiated divided difference is

T(z,w)=partial_w[(s(z)-s(w))/(z-w)]
      =integral [(x-z)^(-1)(x-w)^(-2)] dmu(x).

The linear coefficient c disappears. At z=i and w either i or -i, |T(i,w)|<=integral (1+x^2)^(-1)dmu(x)<=Im Z<=|Z|. The formula includes the diagonal value s''(i)/2. Reflection gives s(-i)=conjugate Z.

For the anchor tuple, the quadratic leading product is exactly Z^r conjugate(Z)^r=|Z|^(2r). The +1 term has absolute value |Z|^(2r-2). Each of the 2r-2 derivative terms has one factor bounded by |Z| and 2r-3 remaining resolvent factors. Hence, with no cancellation assumption,

M_(2r) <= |E_{2r-1,N}|+(2r-1)M_(2r-2).

Consequently (1-epsilon_{r,N})M_(2r) <= (2r-1)M_(2r-2)+epsilon_{r,N}. Young's inequality t^(2r-2)<=delta t^(2r)+C_{r,delta}, with delta chosen after r and before N, absorbs the lower moment. This directly gives sup_N M_(2r)<infinity, after including the finitely many early N whose moments are finite. No prior bound on M_(2r-2) is needed; there is no circular induction. Every positive finite moment follows by choosing 2r at least that exponent. The base r=2 is valid: it is the tuple (i,-i,-i) and yields a fourth-moment bound.

## 3. Compact comparison and dense-test convergence

For an upper-half-plane compact K, let eta=min(1,inf_K Im z)>0 and R=sup_K|z-i|. Along gamma_z(t)=i+t(z-i), the derivative inequality and Gronwall imply the deterministic bound

sup_(z in K)|s_N(z)| <= exp(R/eta)|s_N(i)|.

All segments remain in the upper half-plane. Reflection handles the lower half-plane, so the same assertion with a K-dependent constant holds for any compact K subset C\R. It follows that for every fixed t>0,

sup_N E sup_(z in K)|s_N(z)|^t < infinity.

These constants may depend on K and t; neither K approaching the real line nor growing order is covered.

Now fix p. The denominator in (B) is bounded at each fixed tuple (indeed uniformly on compact sets), so (B) implies ordinary residual convergence to zero on the mixed dense tuples. For finite N the expected residual is jointly holomorphic on each product sign component of (C\R)^p. Differentiation under expectation is justified locally by finite-N boundedness in alpha. Same-sign coincidences are removable analytic diagonals; opposite signs never coincide.

The residuals are uniformly locally bounded in N: bound products by compact suprema, and derivatives/divided differences by Cauchy estimates on a slightly enlarged compact subset of the same half-planes. For opposite-sign arguments the separation is bounded below. The resulting integrands are controlled by constants times compact-supremum powers of degrees p+1 and p-1. The moment estimates just established apply.

Montel's theorem in several complex variables now gives, on each of the finitely many sign components, locally uniformly convergent subsubsequences of any subsequence. In a mixed component, the limit vanishes at every point of D^p in that component, hence everywhere by continuity and density. No several-variable identity theorem for a thin set is being assumed: the test set is genuinely dense in the whole component. Every subsequential limit is therefore zero, implying locally uniform convergence of the full residual sequence.

On all-upper/all-lower components the residual is identically zero already at finite N. In the upper half-plane the Fourier expansion has constant i and strictly positive nonconstant alpha frequencies; s_N^2+1 and every differentiated divided difference have no constant term. Products cannot return to frequency zero. The lower argument is the reflected one. This includes p=1.

For any fixed K subset C\R, K^p meets finitely many components in compact sets, giving sup_(K^p)|E_{p,N}|->0. Since the relative denominator is >=1, (H) follows. This proves the claimed quantifier reduction. It does not supply (A) or (B) for the actual map, nor any convergence rate.

## 4. Normalization and conditional correlation transfer

Each cotangent term has local expansion 1/(x-w), with atom x=N(theta_j-alpha)/2+pi N ell. Thus masses are one, merged masses are positive integers, and the complex residues are -1 per label. The representing measure has N atoms per period pi N, so the random shift has stationary intensity 1/pi. At fixed N, cotangent tends to i as Im w->infinity and the Herglotz linear coefficient vanishes. Finite-N off-real compact moments exist even for repeated eigenangles.

Dividing positions by pi gives unit intensity. In those coordinates y_j=N theta_j/(2pi), t=N alpha/(2pi) is uniform over a period of length N. Integrating an anchored test h(u_k) phi(u_1-u_k,...), with integral h=1, and summing anchor-period lifts gives exactly the prefactor 1/N. For large N fixed compact support excludes different period lifts of one label within a tested tuple. Distinct eigenvalue labels at the same position remain correctly counted by factorial measures.

The local-count inequality mu_N([-B,B]) <= (1+B^2) Im s_N(i) gives every uniform count moment. Continuous compactly tested factorial functionals are continuous under vague convergence of integer-valued Radon measures, including multiplicities; one may see this by the finite partition/inclusion-exclusion formula in products of measures and diagonal identifications. Their magnitudes are bounded by fixed powers of local counts, hence are uniformly integrable. Thus the source's weak conclusion upgrades to the asserted compactly tested factorial convergence on the whole origin space. It gives neither pointwise densities nor a fixed deterministic-origin assertion.

## 5. Actual logarithmic short-leg deletion

Fix 0<s_0<=s<=s_1<infinity, q=exp(-2s/N), K=floor(c log N), with c within FM-007's permissible constant. Put p_m=Tr U_N^m and

L=N^(-2) sum_(m>=1) q^m |p_m|^2,
C=N^(-3) sum_(a,b>=1) q^(a+b) p_(-a)p_(-b)p_(a+b),
B=N^(-1) sum_(a=1)^K q^(a/2)|p_a|.

For any unitary, p_(-m)=conjugate p_m and all these series converge absolutely for q<1. Set x_b=q^(b/2)p_b. Then for each a>=1,

sum_(b>=1) q^(a+b)|p_b p_(a+b)|
=q^(a/2) sum_(b>=1)|x_b x_(a+b)|
<=q^(a/2)(sum_(b>=1)|x_b|^2)^(1/2)(sum_(b>=1)|x_(a+b)|^2)^(1/2)
<=q^(a/2) N^2 L.

Triangle inequality over the union {a<=K or b<=K} yields |C-C_long|<=2BL. Counting the overlap twice in this upper bound is harmless; it is not an erroneous algebraic decomposition. Also 0<=L-L_long<=N^(-2) sum_(m=1)^K |p_m|^2.

FM-007 supplies |p_m|<=C N^(39/40) uniformly for all 1<=m<=K and all sufficiently large odd N, not merely fixed m. Therefore B<=C K N^(-1/40) and L-L_long<=C^2 K N^(-1/20). Its proof's choice delta=N^(-1/20) in (12) produces powers N^(-1/20), N^(-1/10), N^(-1/2) before the e^(Cm) loss; sufficiently small logarithmic c makes the final N^(-1/40) estimate valid. This step uses the logarithmic Egorov input, not a local spectral law.

With Z_s=s_N(is/2), the upper Fourier series is i+(2i/N) sum_(m>=1) p_(-m)e^(im alpha)e^(-ms/N). Parseval gives exactly E|Z_s|^2=1+4L. Reflection makes the two-argument maximum exactly |Z_s|. Thus D=1+E|Z_s|^3 and Lyapunov gives

D>=1+(1+4L)^(3/2).

As L>=0, L/[1+(1+4L)^(3/2)] is globally bounded. Consequently

| (L+C)-(L_long+C_long) |/D
<= C^2 K N^(-1/20)+2C K N^(-1/40) L/[1+(1+4L)^(3/2)]
=O(N^(-1/40) log N).

Nothing here bounds or assumes bounded L. All constants are uniform in the fixed positive compact height interval, and even the displayed deletion inequality only uses 0<q<1. The denominator remains the ORIGINAL full resolvent denominator. Replacing it with a truncated object would require another argument and is not claimed.

Direct Fourier multiplication gives E[(Z_s^2+1)conjugate Z_s]=8i(L+C). The expected differentiated quotient is -2i/s^2, since E s_N(w)=i above and -i below. Thus the exact residual is 8i[L+C-1/(4s^2)], confirming the normalization, sign, factor eight, and retained possible imaginary part of C.

## 6. Exact tensor-resolvent form

All traces below are ordinary unnormalized traces. Let X=U tensor conjugate(U). Since U is unitary, ||X||=1 and q<1, the norm-convergent operator identity is

(qX)^(K+1)(I-qX)^(-1)=sum_(a>K)q^a(U^a tensor conjugate(U^a)).

The finite-dimensional partial trace is continuous and satisfies Tr_2(A tensor B)=A Tr B. Hence

F_K=Tr_2[(qX)^(K+1)(I-qX)^(-1)]
   =sum_(a>K)q^a p_(-a)U^a.

Tracing once gives Tr F_K=sum_(a>K)q^a|p_a|^2=N^2 L_long. Multiplying the two norm-convergent sums and using U^a U^b=U^(a+b) gives

Tr(F_K^2)=sum_(a,b>K)q^(a+b)p_(-a)p_(-b)p_(a+b)=N^3 C_long.

This is an algebraic square, not an adjoint square, and there is no missing factor N in the partial trace. It holds for arbitrary multiplicities and every N, not just a diagonal three-point example. It also explains why the cubic trace may be complex even though Tr F_K is nonnegative real.

For real t=tau N and U=exp(it A)M, complex conjugation gives conjugate U=exp(-it conjugate A)conjugate M. The tensor-factor generators commute, so exactly

X=exp(it[A tensor I-I tensor conjugate A])(M tensor conjugate M).

The order of the kick and metaplectic factor is retained. No commutation between those two factors, nor replacement of iterated ordered products by one transported-generator exponential, follows.

## 7. Exact remaining obligation and scope

Put q=exp(-2s/N) and K=floor(c log N). The first mixed condition is equivalent, up to the proved vanishing deletion error, to

[Tr F_K/N^2+Tr(F_K^2)/N^3-1/(4s^2)] / [1+E|s_N(is/2)|^3] ->0.

The complex numerator is retained, including its imaginary part. This is only one necessary mixed leaf of the proposed sufficient hierarchy. It is **OPEN for the actual map**. The single-anchor conditions (A) at every r and dense mixed conditions (B) at every p remain OPEN as well. Proving the r=2 anchor would yield fourth moments and hence bounded first-mixed denominators, but that anchor has not been established. The displayed identities and deletion estimate alone neither identify the pair limit nor prove BGS.

The corresponding invariant registry owner remains BGS-LOOP-001 with conditional status; TRACE-005 and BGS-BGS-001 remain open. No parameter average, changed noise law, changed quantization or different symmetry class is introduced.

## 8. Verification and provenance

The companion `computations/verification/loop_test_reductions.py` performs exact rational complex finite checks of pair/cubic normalizations, overlap accounting, and a nondiagonal tensor partial-trace identity. Its explicit error checks remain active under Python -O, and importing it performs no computation or writes. Tests cover deliberately corrupted identities in both execution modes. These checks support finite algebra only; Theorems A and B rest on the proofs and named inputs above, not on finite examples.

Independent internal review reconstructed the moment, normal-family, deletion and tensor arguments from the pinned author report. Curated review: `record/loop_test_reductions_review_20261006.md`. Accepted original hashes, curated sections 2–5, and input reconciliation are retained in the [provenance record](../../../evidence/loop_reductions_20261006/provenance.json). Untouched originals remain separately retained; public copies are explicitly curated. Source authentication does not certify the entire 147-page external theorem or all upstream FM-007 proofs. See the source-bound provenance manifest for exact content identities.
