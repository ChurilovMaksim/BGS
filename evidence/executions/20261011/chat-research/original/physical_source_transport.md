# From real spectral transport to the physical absorbed source

8 October 2026. Derived in this session, using the already proved real-flow theorem TRACE-056 and the self-contained covariance proof in source_covariance.md. No repository modifications. The statement is a scalar comparison, not an evaluation of the scalar reference law. External priority is not established.

## Statement

Let S_m be deterministic unitary, max_ij |(S_m)_ij|²=delta_m→0, and || |S_m|²−J_m ||≤rho<1. Let H_m>0 be deterministic, independent of the independent uniform diagonal phases D, with Tr H_m=m and Tr H_m²≤C_H m. The matrix H may be correlated with S. No uniform lower bound on its eigenvalues is assumed.

For Re t>0 define

A_m(t)=m^−1 Tr{H_m[(I−D S_m exp(−t H_m/m))^−1−I]},
B_m(t)=m^−1 Tr[(I−exp(−t/m)D S_m)^−1−I].

Then A_m−B_m→0 in L², locally uniformly in Re t>0. Every fixed complex t derivative has the same convergence. Consequently it also converges in every fixed L^p, 1≤p≤2, including those derivatives. Mixed products of two such sources, including complex conjugates and derivatives, have convergent expectations under this comparison.

This advances the normally absorbed real-flow result to the actual positive anisotropic exponential and its H-weighted source. It does not establish arbitrary higher products, CUE identification, or deterministic BGS. The quadratic conclusion is proved using the additional normal-source fourth-moment lemma below.

## 1. The input from real flow

For W_x=D S_m exp(ix H_m/m), V_x=exp(ix/m)D S_m and real x in a fixed compact interval, TRACE-056 gives, for real u>0,

E |m^−1 Tr[(I−exp(−u/m)W_x)^−1−(I−exp(−u/m)V_x)^−1]|
 ≤ |x| a_{m,R}/(2u),                                    (1)

where a_{m,R}=sqrt((C_H−1) beta_{m,R})→0. One can take beta_{m,R}=O(log log(1/delta_m)/log(1/delta_m)). Only convergence on each fixed interval is used below. The input is not assumed for complex x or for H-weighted sources.

## 2. Dimension-free estimates for logarithms

Use the Neumann branch of log det for every strict contraction. For s>0 and Im z≥0 put

L_{m,s}(z)=log det(I−exp(−s/m)D S_m exp(iz H_m/m))
          −log det(I−exp((−s+iz)/m)D S_m).

For a deterministic contraction V, the arbitrary-source covariance inequality gives

||m^−1 Tr[(I−exp(−v/m)D V)^−1−I]||_2²
 ≤ 1/[m(exp(2v/m)−1)] ≤ 1/(2v),  v>0.                  (2)

The corresponding estimate with source H is at most C_H/(2v), provided ||V||≤1 and Tr H²≤C_H m. Differentiating L_{m,s} with respect to z, and integrating along the segment from 0 to z in the closed upper half-plane, gives

||L_{m,s}(z)||_2 ≤ C |z|/sqrt(s),
C=(sqrt(C_H)+1)/sqrt(2).                               (3)

Here L_{m,s}(0)=0 exactly. The formula for its derivative is

partial_z L_{m,s}=−i m^−1 Tr(H Q_{s,z})+i m^−1 Tr(Q^0_{s,z}).

All these random variables are centered in phase expectation. Bounds (2)–(3) follow from the full resolvent covariance, not from independence of its powers.

## 3. Real boundary convergence for logarithms, including L²

For real x, partial_s L_{m,s}(x) is the unweighted trace difference in (1). For fixed 0<s<R', integration in s and (3) at R' yield

||L_{m,s}(x)||_1
 ≤ C |x|/sqrt(R') + |x| a_{m,R} log(R'/s)/2,   |x|≤R.     (4)

First let m→infinity at fixed s,R,R', and then let R'→infinity. This proves real-boundary L¹ convergence uniformly for |x|≤R. No integration to infinity of the nonintegrable bound 1/u has been made.

### The normal-source fourth-moment input

For any deterministic n-dimensional unitary V, independent uniform D, and Re u≥sigma>0,

sup_(n,V,Re u≥sigma) ||n^−1 Tr[(I−exp(−u/n)D V)^−1−I]||_4 ≤ C_sigma.    (4a)

Here is the self-contained argument needed for this statement. If Z is the number of eigenvalues in a connected arc of normalized length p and mu=np, rank-one coordinate phase resampling gives E(Z)_k≤mu^k. The conditional spectral weight of the resampled coordinate averages to p: each nonzero positive Fourier moment of its scalar spectral measure has a strictly positive power of that coordinate phase and averages to zero; negative moments are conjugate. Rank-one cyclic interlacing gives |Z−Z'|≤1 for the original and resampled matrix. In the identity (Z)_k=sum_i <i,1_arc(DV)i> (Z−1)_(k−1), replace the nonnegative falling factorial on the support Z≥1 by (Z')_(k−1), average the original phase, and sum i. This yields the induction. It also gives E Z=mu and Var Z≤mu.

The finite factorial expansion implies E exp(t(Z−mu))≤exp(mu(exp(t)−1−t)) for t≥0. Its elementary Chernoff bound and integration give ||(Z−mu)_+||_4≤C(sqrt(mu)+1). Since (mu−Z)_+≤mu and its second moment is ≤mu, the negative part has fourth norm ≤mu^(3/4). Thus

||Z−mu||_4≤C(sqrt(mu)+1+mu^(3/4)).

Write the centered spectral measure using the centered counts of the arcs (0,v] and [−v,0), 0≤v≤pi. Integration by parts against f_r(theta)=r exp(i theta)/(1−r exp(i theta)), r=exp(−Re u/n), has cancelling boundary terms at pi and no mean term. Using |f'_r(theta)|≤C/(1−r+|theta|)² gives, by Minkowski,

||X_n(u)||_4 ≤ C[(n(1−r))^−1/2+(n(1−r))^−1+(n(1−r))^−1/4].

Indeed each term is the integral of the corresponding power of nv against n^−1(1−r+v)^−2. Since n(1−exp(−Re u/n))≥1−exp(−sigma), (4a) follows. Complex u is handled by the common-phase invariance. This proof uses no local universality. It is the p=4 part of complex_microscopic_phase_source_bounds.md; no broken documentation link is used as a proof dependency.

For fixed real x and u in [s,R'], (1) plus (4a) gives L² convergence of the trace difference by ||Y||_2≤||Y||_1^(1/3)||Y||_4^(2/3). It is uniform on fixed x,u compacts. Integrating over this finite absorption interval shows

limsup_m ||L_{m,s}(x)||_2≤C |x|/sqrt(R').

Letting R'→infinity proves the real-boundary convergence in L², uniformly for bounded real x. The fourth moment is used only for the normally absorbed unitary endpoints, where its assumptions hold.

## 4. Analytic propagation into the upper half-plane

Fix s>0. The L²-valued analytic function

G_{m,s}(z)=L_{m,s}(z)/(z+i)²

has the upper-half-plane Cauchy representation

G_{m,s}(z)=(2 pi i)^−1 integral_R G_{m,s}(x)/(x−z) dx.      (5)

For each m this follows by upper semicircle contours, or directly as a Bochner integral. The semicircle contribution tends to zero by (3): ||G||_2=O(1/R) on a radius-R arc. The real-line majorant C_s |x|/[(1+x²)|x−z|] is integrable and uniform for z in a compact subset of Im z>0. The L² refinement of (4), dominated convergence, and (5) therefore imply

L_{m,s}(z)→0 in L², locally uniformly for Im z>0.          (6)

The varying phase probability spaces cause no problem: (5) is proved on each space, and its norm bound is an ordinary scalar dominated-convergence estimate.

## 5. Removing the auxiliary scalar absorption

For Im z>0, F_z=S_m exp(iz H_m/m) is strictly contractive because H_m>0. No lower eigenvalue bound uniform in m is required. Write L_{m,0} for the same two log determinants without exp(−s/m). For fixed m the logarithms are continuous down to s=0. Integrating their s derivatives and applying (2) gives the crucial uniform estimate

||L_{m,s}(z)−L_{m,0}(z)||_2
 ≤ 2 integral_0^s (2v)^−1/2 dv
 = 2 sqrt(2s).                                        (7)

The singularity v^−1/2 is integrable. This is why it is legitimate to remove scalar absorption at the logarithm level even though a direct unweighted resolvent estimate near v=0 is not uniform. Equation (7) is uniform in z in the upper half-plane, in m, and in the smallest eigenvalue of H_m.

Combining (6) and (7), taking m→infinity before s→0, gives L_{m,0}→0 in L² locally uniformly. Banach-valued Cauchy estimates then imply convergence of every fixed z derivative. Since

i partial_z L_{m,0}(z)=A_m(−iz)−B_m(−iz),

the asserted physical-source comparison follows, as do all its fixed t derivatives.

## 6. Quadratic observables and smaller L^p exponents

The anisotropic source bound, with F=S_m exp(−tH_m/m), gives

E |A_m(t)|²
 ≤ m^−2 Tr[H_m²/(exp(2 Re(t) H_m/m)−I)]
 ≤ Tr H_m/[2 Re(t) m]=1/[2 Re(t)].                      (8)

In the first line the factor order is justified because F*F=exp(−2 Re(t)H_m/m) commutes with H_m; S need not commute with H_m. The same bound holds for B_m. The already established L² convergence implies L^p convergence for 1≤p≤2. Cauchy contours give local L² bounds and convergence for fixed derivatives as well. For example,

|E[A_m(t) conjugate(A_m(v))−B_m(t) conjugate(B_m(v))]|
 ≤ ||A_m(t)−B_m(t)||_2 ||A_m(v)||_2
   +||B_m(t)||_2 ||A_m(v)−B_m(v)||_2 →0.

The same Cauchy–Schwarz argument handles unconjugated products and fixed derivatives.

The new L² convergence relies on the normal-source fourth-moment argument, not merely on the boundedness in (8). This identifies the physical quadratic source with its scalar-ensemble counterpart, but does not evaluate that counterpart or control products of three or more sources.

## Exact dependency and scope

Dependencies are: (i) the averaged-pinching/real-flow theorem already reconstructed as TRACE-053/056; (ii) the fully proved arbitrary complex source covariance in source_covariance.md; (iii) the normal-source fourth-moment proof in Section 3; (iv) elementary complex analysis and interpolation. There is no use of the unreconstructed cavity-flatness assertion or a conditional stopping event inside a circle-integrated jet estimate. Applying the theorem to a random cavity requires its endpoint flatness/gap and suitable moment control after conditioning on the revealed past; these hypotheses are not proved by this note.

## 7. Random-cavity version with only tight clock moments

The deterministic theorem is uniform on fixed C_H,rho classes with delta_m bounded by a sequence tending to zero, as follows from the uniform real-flow input and the same fixed-contour estimates. It therefore applies after conditioning on the revealed cavity data.

Here is a precise useful corollary. Let (S_m,H_m) be random past-measurable data, independent of the remaining diagonal phases D. Assume H_m>0, write alpha_m=Tr H_m/m, and suppose:

1. E alpha_m=1.
2. There are past-measurable events E_m of probability tending to one on which alpha_m→1 uniformly, max|S_ij|²≤delta_m→0 and || |S_m|²−J ||≤rho<1.
3. On E_m, the second normalized clock moment is tight: for example E[1_{E_m} Tr H_m²/m]≤C.

Then the physical A_m(t) and the scalar B_m(t) above still converge to each other in L², including fixed derivatives and pair products.

Proof. On E_m intersect {Tr H_m²/m≤M}, normalize H by alpha_m. The deterministic theorem applies with a fixed moment bound (eventually at most 4M). Its reference source is alpha_m B_m(alpha_m t), which tends to B_m(t) in L² uniformly as alpha_m→1 by normal-source Cauchy bounds. The probability of the removed moment tail is at most C/M. Conditional on past data the energy inequality gives E_D|A_m(t)|²≤alpha_m/[2 Re t] and E_D|B_m(t)|²≤1/[2 Re t]. On E_m the factor alpha_m is bounded, so the contribution of that tail to the squared L² error is O(1/M). On E_m^c its contribution is at most a constant times E[(1+alpha_m)1_{E_m^c}]. But

E[alpha_m 1_{E_m^c}]=1−E[alpha_m 1_{E_m}]→0

by assumptions 1 and 2. First let m→infinity at fixed M, then let M→infinity. Derivatives follow by fixed contours. No conditional independence between S_m and H_m is required.

For a Schur cavity at retained size m, H_m=m T_m/N gives alpha_m=Tr T_m/N. The exact one-step trace identity makes alpha a mean-one martingale, when the feedback process is almost surely nondegenerate at every step. The joint diagonal barrier makes alpha_m→1 on the good event, and the killed square estimate supplies assumption 3. Thus, if the remaining all-time-flatness and endpoint-gap probabilities are proved, the delay bootstrap from this session supplies the other inputs for this physical-to-scalar comparison. This corollary does not establish those flatness/gap probabilities, the comparison of the original-radius cavity with its exponential approximation, or the scalar limiting law.

## Independent review

An independent internal reviewer reconstructed the analytic continuation, source factor orders, scalar-absorption removal, and the normal fourth-moment upgrade. The reviewer confirmed L² convergence and pair-product comparison, while identifying a missing old documentation link; Section 3 above gives the necessary resampling argument directly. The random-cavity corollary has been checked by the author; the earlier independent review covered the deterministic theorem and its L² strengthening. This is not external peer review or Lean formalization.
