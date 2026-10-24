# Exact stationary potential and homoclinic cocycle at the literal coupling

6 October 2026. Exact project proof with independent internal audit of H1–H10. tau=10^-80 throughout the final conclusions. Sources: the frozen
paired/locality/Frostman notes and the actual C² time-remainder certificate
in four_branch_parametrix.md Section4.

## 1. One fixed actual potential for every periodic action

Let u_j(z) be the unique bounded stationary correction with source s=0 in
(L8), and write u(z)=u_0(z). Shift covariance and uniqueness give
u_j(z)=u(S^j z). Here S=[[3,4],[2,3]], and lambda=3+2sqrt(2).
Let R_tau(x,y)=S_0(tau,x,y)-S_0(0,x,y). Define on the label torus

 V_tau(q,p)=R_tau(q+u(z),3q+4p+u(Sz))
                      -(3/4)u(z)^2+(1/4)u(z)u(Sz).                 (H1)

Integer gluing R_tau(x+a,y+3a+4b)=R_tau(x,y) and periodicity of u make this
well-defined on T². It is C^alpha, alpha=log(5.8)/loglambda. No label C1
regularity is used.

For z in G_m, uniqueness makes the infinite correction m-periodic after
integer gluing, identical to the finite stationary correction. Expanding
the quadratic cat action about its stationary point cancels every linear
term, including the winding terms. Its remaining contribution is
-1/2 u^T K_0 u. With K_0=(6I-P-P^T)/4 this is exactly
sum_j[-3u_j²/4+u_j u_(j+1)/4]. Therefore the REAL stationary correction is

 Delta_(tau,m)(z)=sum_(j=0)^(m-1) V_tau(S^j z).                     (H2)

This includes m=1 and m=2: self and repeated-neighbour terms are already
present in the displayed cyclic quadratic expression. No asymptotic error,
shrinking coupling, or leading-symbol replacement occurs in H1–H2.

## 2. Exact homoclinic decomposition and compatibility

Put d=(1/sqrt(2),-1/2) mod Z². The orbit S^j d has representatives bounded
by C lambda^(-|j|). Thus the following series is absolutely and uniformly
convergent by the Holder modulus of V_tau:

 C_tau(z,d)=sum_(j in Z)[V_tau(S^j(z+d))-V_tau(S^j z)].                (H3)

The actual defect from the bounded stationary equation satisfies

 D_(tau,infty)(z)=C_tau(z,d).                                        (H4)

Here is a proof that does not posit an infinite action. At finite m, H2
identifies D_m on G_m with the centered finite sum in H3 using d_m. The
canonical d_m tends to d with error O(lambda^-m). On the centered window,
the Holder estimate makes the replacement error O(m beta^(-m/2)), and the
omitted tails tend uniformly to zero. Hence those finite sums converge
uniformly on T² to H3. Independently, accepted locality gives D_m->D_infty
uniformly on G_m. The grids G_m have mesh tending to zero, and both limiting
functions are continuous; equality follows everywhere. This argument only
uses absolutely convergent DIFFERENCES, never an infinite stationary action.

For any homoclinic translations d,e, define C_tau(z,e) by H3 with e. Direct
reindexing and telescoping, justified by absolute convergence, give

 C_tau(z,d+e)=C_tau(z,d)+C_tau(z+d,e),
 C_tau(Sz,Sd)=C_tau(z,d),
 C_tau(z+e,d)-C_tau(z,d)=C_tau(z+d,e)-C_tau(z,e).                      (H5)

In particular the actual d and Sd cocycles commute compatibly, and S²d=6Sd-d.
These are exact nonlinear relations, not generic Holder bounds. They give a
concrete renormalization structure for the weighted-translation problem.

## 3. Quantitative actual orbit sum; no unspecified small-time argument

The parameter source certificate gives

 ||R_tau(x,y)-tau*g(x,(y-3x)/4)/(2*pi)||_(C²)
                                      <=5*10^49 tau².               (H6)

The beta-weighted resolvent proof, before integration in s, gives the safe
bounds ||u||infinity<=2eta and [u]_(C^alpha)<=10^9 eta; composition by S costs
at most a factor 10. Here eta<=2*10^10 tau. To make the remainder accounting
explicit, set Y0=(q,3q+4p), w=(u(z),u(Sz)). Then

 ||w||infinity<=4*10^10 tau,
 [w]_(C^alpha)<=2*10^20 tau,
 Lip(Y0)<=7

in local maximum-norm charts, with integer gluing on overlaps. The smooth
function f(x,y)=g(x,(y-3x)/4)/(2*pi) has C² norm below 10^10. The integral
identity f(Y0+w)-f(Y0)=integral_0^1 Df(Y0+t*w)w dt bounds its C^alpha norm
by 10^33 tau. Composing the H6 remainder with Y0+w costs less than 10^53 tau².
The quadratic terms of H1 cost less than 10^33 tau². Thus, very conservatively,

 ||V_tau-tau*g/(2*pi)||_(C^alpha) <=10^60 tau².                       (H7)

All these constants are independent of m and are evaluated at the prescribed
tau; they do not use an asymptotic O(tau²) with unspecified constant.

For v=(1,0), write k_j=(S^T)^j v=(a_j,sign(j)*2b_|j|). The actual Fourier
support meets this oriented orbit only at v, with coefficient c_v=(10-i)/200.
Moreover |k_j|>=lambda^|j|/2. A standard translation-difference estimate
bounds a nonzero Fourier coefficient of a C^alpha function by its Holder
seminorm times |k|^-alpha. Therefore the absolutely convergent orbit sum

 A_v=sum_(j in Z) Vhat_tau(k_j)

obeys

 |A_v-tau*c_v/(2*pi)|<=3*10^60 tau²,
 |A_v|>=tau/1000>0 at tau=10^-80.                                  (H8)

The factor 3 bounds 2*(1+2/(beta-1)), beta=5.8. The isolated-support fact is
the exact one checked in ../archive/history/2026/homoclinic_20261006/first_response_support_original.md; the quantitative
remainder H7 is what upgrades that first-response discriminator to fixed tau.

## 4. Exact Fourier factorization and the additive-gauge obstruction

For any nonzero integer frequency k whose hyperbolic orbit sum converges,
Fourier transformation of the uniformly convergent H3 gives

 Dhat_infty(k)=[e(k dot d)-1] sum_(j in Z) Vhat_tau((S^T)^j k).         (H9)

On the isolated orbit k_j this is simply [e(k_j dot d)-1] A_v. None of these
factors vanishes: k_j dot d is congruent to lambda^(-|j|)/sqrt(2).
If an L² function F solved D_infty=F(z+d)-F(z)+constant, H9 would force
Fhat(k_j)=A_v for infinitely many distinct j. This contradicts Bessel's
inequality by H8. Thus the ACTUAL fixed-tau defect has no L² additive gauge
of this form. The critical small divisors cancel exactly, leaving a nonzero
constant orbit coefficient.

There is also a literal-coupling regularity consequence. Along j->+infinity,

 2*pi*i*a_j Dhat_infty(k_j) -> -sqrt(2)*pi²*A_v !=0.                  (H10)

Hence the distributional q-derivative of D_infty cannot be an L¹ function
on T² (Riemann–Lebesgue), and in particular D_infty is not C1 or W^(1,2).
The accepted monotonicity says d_q H is a positive finite measure; H10 proves
that this measure has a nonzero singular component. This does NOT imply that
the pushforward mu_tau=(H mod1)_*Leb is singular or lacks Fourier decay:
that is a different measure, involving the inverse fibre homeomorphisms.

## 5. Prior-work and exact remaining relation

The orbit-sum coboundary criterion and the constant-Fourier-tail L² obstruction
are PRIOR project methods: see periodic_point_trace_comparison.md Section10,
pell_smooth_resonance.md, and resonance-cohomology/extremal_resonance_nondegeneracy.md Corollary2.
The present object is different: it is the actual nonlinear stationary
potential H1 and its homoclinic translation cocycle, with a literal-tau
remainder certificate. No novelty claim is made for the general methods.

H5 supplies a genuine two-generator homoclinic compatibility/renormalization
identity. It does not evaluate the high-frequency spectral measure of T_N.
The failed additive gauge does not exclude a measurable MULTIPLICATIVE gauge
for e(ND_infty), which can involve integer-valued winding jumps; no uniform
control of those jumps or of the transformed full quantum weights is known.
That, or a direct oscillatory use of H5, is an exact changed leaf. Full finite
aliases and the exponentially large displacement range remain required.

## Review and replay boundary

The scoped independent audit is [record/homoclinic_review.md](../archive/record/homoclinic_review.md).
Exact finite controls support the analytic arguments and do not replace their
all-time conclusions. Original proof, review and source hashes are retained
in [the promotion mapping](../archive/record/homoclinic_promotion_mapping.json).
The derivative measure is distinct from the inverse-fibre pushforward; no
multiplicative-gauge obstruction, pointwise decay or BGS claim is made.
