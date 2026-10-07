# Global coercivity of the bare bosonic phase action

7 October 2026. Read-only BGS base observed at `d37c92e563d10d25bb1d6ab85bedffc1f160f773`, with an existing integration overlay. This report changes no canonical files. Author derivation with exact-source verification; independent review pending. No priority or universality claim.

## Verdict and exact claim

**A dimension-uniform global scalar-body coercivity inequality is proved, conditional only on the explicitly stated flatness and singular-gap inputs.** This is not full supersymmetric integral control.

Let U be any N by N unitary, P_ij=|U_ij|^2, and J_ij=1/N. Assume

- max P_ij <= C/N, with C>=1;
- ||P-J||_(2->2) <= rho < 1.

For diagonal Z=diag(z_1,...,z_N), with |z_j|<1 and sum z_j=0, define

S_U(Z) = log|det(I-U Z U* Z*)| - log det(I-Z Z*),
H(Z) = sum_j -log(1-|z_j|^2),
K = 1 + sqrt(C-1)/(1-rho).

Then, globally on this centered domain,

**S_U(Z) >= H(Z)/(2 K^2).**                                      (T)

The bound includes arbitrary unequal radii and arbitrary phases, all strict interior configurations, and every N for which its assumptions hold. For P=J it gives S>=H/2. The actual unchanged BGS family inherits some fixed C and eventual rho=1/2 from FM-021; its noneffective startup remains noneffective. This theorem does not assert this bound for excluded pre-startup dimensions using those eventual constants.

Without centering, no positive multiple of H can be controlled: Z=aI has S=0 for every |a|<1. Exact common disk-Mobius invariance and a unique global ordinary bosonic centering are established below.

## 1. Source, sign and scope of the action

Weidenmueller, *Massive Modes for Quantum Graphs*, arXiv:1812.00655v1, equations (7)--(10), printed pp.3--4, gives the diagonal phase fields, |Z_BB|<1, tilde Z_BB=conjugate Z_BB, and bare action

A_bare = -STr log(I-Z tilde Z) + STr log(I-U Z U* tilde Z).

The weight is exp(-A), with flat supermeasure before subsequent changes of variables; see the paragraph following (9). Setting Grassmann variables and the fermionic body to zero, and taking the real part, gives exactly S_U above, with the displayed sign. This uses the arbitrary-unitary algebra of the phase representation, not a graph universality theorem. Spectral increments and differentiated source factors in (8)--(9) are absent from the bare action and are not silently discarded in any full-integral claim.

Primary source: https://arxiv.org/pdf/1812.00655v1 . A previously authenticated local copy is `/workspace/shared/bgs_balanced_phase_bridge/sources/w18v1.pdf`; source hash is included in the provenance record.

## 2. Determinant and singular-value dictionary

For each j put

x_j = atanh(|z_j|) z_j/|z_j|, with x_j=0 when z_j=0,
W=diag(x_j), D=I-ZZ*, C_0=D^(-1/2),
X=[[0,W],[W*,0]], J_0=diag(I,-I), and K_U=diag(U,U).

Then

g=exp X=[[C_0,Z C_0],[Z* C_0,C_0]],
T=g^(-1) K_U g.

Both g and K_U are J_0-unitary. The upper blocks of T are

F=C_0(U-ZUZ*)C_0,
G=C_0(UZ-ZU)C_0.

Thus FF* - GG*=I and

|det F| = |det(I-U Z U* Z*)|/det D = exp S_U(Z),
exp(2S_U(Z)) = det(I+GG*).                                      (1)

For the determinant equality, det(I-U* Z U Z*) is the complex conjugate of det(I-U Z U* Z*) by taking adjoints and cycling determinant factors. Therefore the choice K_U=diag(U,U) is consistent with the specified orientation.

In particular S>=0. Formula (1) is the exact matrix-ball identity in coordinates: G_ij=U_ij(z_j-z_i)/sqrt((1-|z_i|^2)(1-|z_j|^2)). It is not a replacement of the whole action by its quadratic approximation.

Write the polar decomposition T=V exp L. From J_0(T*T)J_0=(T*T)^(-1), L=log|T| anticommutes with J_0; hence L=[[0,B],[B*,0]] for some B. Also V is unitary and J_0-unitary, so V is block diagonal. Let t_1>=...>=t_N>=0 be the singular values of B. The singular values of T are exp(t_j), exp(-t_j), and the singular values of F are cosh(t_j). Consequently

S_U(Z)=sum_j log cosh(t_j).                                     (2)

This proves the Cartan/singular-value relation directly, without an additional external Lie-group theorem.

## 3. Exact external input: generalized exponential metric increase

Bhatia, *On the exponential metric increasing property*, ISI preprint isid/ms/2002/14, dated May 10, 2002; Theorem 4, equations (15)--(16), printed p.5. The theorem holds for complex Hermitian A,B and **every unitarily invariant norm**, equivalently every symmetric gauge norm:

|||A-B||| <= |||log(exp(-B/2) exp(A) exp(-B/2))|||.                (EMI)

The downloaded primary author preprint is cached in `sources/bhatia_emi_2002.pdf`, with extracted text and SHA-256 in provenance.json. The published paper is Linear Algebra Appl. 375 (2003), 211--220, DOI 10.1016/S0024-3795(03)00647-5. The verified theorem numbering is the 2002 preprint numbering; no uninspected published numbering is substituted.

Primary URL: https://www.isid.ac.in/~statmath/2002/isid200214.pdf . Publication metadata: https://doi.org/10.1016/S0024-3795(03)00647-5 .

Apply EMI with A=2Y, B=2X, where Y=K_U X K_U*. Since T K_U*=exp(-X)exp(Y), the positive matrix on the right is TT*. The singular values of X-Y are the singular values of W-UWU*, each repeated twice. The absolute eigenvalues of log(TT*) are 2t_j, each repeated twice. Taking the Ky Fan 2k norm gives

sum_(j<=k) s_j(W-UWU*) <= sum_(j<=k) t_j, 1<=k<=N.              (3)

All factors of two cancel: both sides before cancellation equal four times the corresponding partial sum. Thus s(W-UWU*) is weakly majorized by t. For the convex increasing function phi(s)=log cosh(s), phi(0)=0, (2)--(3) imply

S_U(Z) >= sum_j phi(s_j(W-UWU*)).

Diagonal pinching weakly decreases singular values, and the diagonal of W-UWU* is v=(I-P)x. Therefore

**S_U(Z) >= sum_j phi(|v_j|), v=(I-P)x.**                       (4)

For completeness, the weak-majorization implication follows by expressing a convex increasing function vanishing at zero as a nonnegative linear term plus a positive integral of (s-a)_+. The Ky Fan inequalities control each such positive-part sum. Diagonal pinching is an average of diagonal-unitary conjugations; Ky Fan norm convexity establishes the required pinching inequality.

Using only trace norm and phi(t)>=t-log 2 would instead give an additive -N log 2. Retaining all Ky Fan inequalities and the convex log-cosh function avoids that loss exactly.

## 4. Flatness plus singular gap gives a uniform Orlicz inverse

Set A=P-J and R=(I-P+J)^(-1)=I+sum_(k>=1) A^k. Each row and each column of A has squared Euclidean norm at most (C-1)/N. Hence for k>=1 every absolute row or column sum of A^k is at most sqrt(C-1) rho^(k-1). This follows by Cauchy--Schwarz and one smoothing step; no normality, eigenbasis, reversibility or pointwise lower bound is required. Thus

||R||_(1->1), ||R||_(infinity->infinity) <= K.                  (5)

For x^0=x-(N^(-1)sum x_j)1 and v=(I-P)x, we have x^0=Rv. The constant component is treated exactly; R is not the reduced inverse with an unnecessary extra I-J norm loss.

For any complex v, row-wise Jensen using weights |R_ij|/K (with the remaining weight at zero), followed by the column bound, gives

sum_i phi(|(Rv)_i|/K) <= sum_j phi(|v_j|).                       (6)

For K>=1, phi(s/K)>=K^(-2)phi(s). To verify this, phi(s)/s^2 decreases on s>0 because 2 log cosh s - s tanh s>=0; its derivative is tanh s-s sech^2 s>=0, whose derivative is 2s sech^2 s tanh s>=0. Hence (4)--(6) imply

S_U(Z) >= K^(-2) sum_j phi(|x_j^0|).                            (7)

## 5. Why the linear disk centering is enough

Do not identify sum z=0 with sum x=0. They are different gauges. Instead consider the ordinary convex function of a complex scalar b,

F(b)=sum_j phi(|x_j-b|).

Its gradient at b=0 is -sum_j tanh(|x_j|)x_j/|x_j|=-sum_j z_j=0. Since phi is convex and increasing, F is convex and b=0 is a global minimizer. Therefore

sum_j phi(|x_j^0|)=F(mean x)>=F(0)=sum_j phi(|x_j|)=H(Z)/2.

Combining with (7) proves (T). This is a direct argument in the requested conformal/linear disk gauge; it does not change to hyperbolic-log centering, introduce a new integration measure, or compare two conjectural slices.

## 6. Exact scalar Mobius gauge and ordinary real Jacobian

For a in the unit disk let m_a(z)=(z-a)/(1-conjugate(a)z). The matrix determinant cocycle

I-m_a(A)m_a(B)*=(1-|a|^2)(I-conjugate(a)A)^(-1)(I-AB*)(I-aB*)^(-1)

holds for strict contractions A,B. Substituting A=UZU*, B=Z and taking determinants shows

S_U(m_a(Z))=S_U(Z).                                             (8)

This is a bare-action identity only. Rotations are also invariant.

Every tuple of strict disk points z_j has a unique a such that w_j=m_a(z_j) obeys sum w_j=0. One elementary proof minimizes

F_z(a)=sum_j log|1-conjugate(a)z_j|^2 - N log(1-|a|^2).

It is proper at the boundary because each z_j is strictly interior. Along every disk geodesic it is strictly convex: after moving a point to zero by a disk isometry, the second derivative in a unit-speed parameter a(t)=e^(i theta)tanh t at t=0 is

2 sum_j [1-Re(e^(-2i theta) w_j^2)]>0.

The transformation law of F_z adds only a constant when coordinates are jointly changed, so the same positivity holds at every point along the geodesic. Its critical equation is precisely sum m_a(z_j)=0. Properness gives a minimizer, strict geodesic convexity gives uniqueness. This also covers N=1, where a=z_1.

For w_N=-sum_(j<N)w_j and z_j=(a+w_j)/(1+conjugate(a)w_j), the ordinary real Jacobian relative to d^2a product_(j<N)d^2w_j and product_j d^2z_j is

**(N^2-|sum_j w_j^2|^2)(1-|a|^2)^(2N-2) / product_j |1+conjugate(a)w_j|^4.**  (9)

To derive it, divide dz_j by q_j=(1-|a|^2)/(1+conjugate(a)w_j)^2. The sum of these divided differentials is

[N da-(sum w_j^2)d conjugate(a)]/(1-|a|^2),

because sum dw_j=sum w_j=0. The real determinant of alpha da+beta d conjugate(a) is |alpha|^2-|beta|^2. Multiplication by all |q_j|^2 yields (9). The factor is strictly positive, since |sum w_j^2|<=sum|w_j|^2<N. There is no residual scalar rotation ambiguity because m_a itself has been fixed by its displayed convention.

N=1 calibrates to Jacobian one. N=2, a=0, w=(u,-u) calibrates to 4(1-|u|^4). Formula (9) is the ordinary real bosonic Jacobian only, not a super-Berezinian.

## 7. Cheap boundary and sharpness controls

- Scalar fields z_j=a refute uncentered positive-H coercivity exactly.
- Rank-one boundary field Z=r E_ii has exp S=(1-P_ii r^2)/(1-r^2). Its action grows logarithmically unless P_ii=1. It is not centered as written, but (8) centers it without changing S.
- On the centered common-radius slice z_j=r v_j, |v_j|=1, sum v_j=0, put V=diag(v_j), Q=UVU*V*. Then ReTr Q<=rho N. For each eigenphase theta, log|1-r^2 exp(i theta)| is a concave function of cos theta. Its chord between -1 and 1 gives

S_U(rV) >= [N(1-rho)/2] log((1+r^2)/(1-r^2)).                  (10)

This confirms the stronger restricted-slice formula, including its constants. It is not needed to prove (T).
- The universal constant 1/2 for P=J is asymptotically sharp in even-dimensional auxiliary controls. Take U=F_4 and V=diag(1,-1,1,-1). Then Q has eigenvalues (1,1,-1,-1), and S_U(rV)=2 log((1+r^2)/(1-r^2)), while H=4 log(1/(1-r^2)); S/H tends to 1/2. Tensor with any flat Fourier matrix to get an unbounded even-dimensional family. This is a general-lemma sharpness example, not the actual odd-dimensional quantum map.

## 8. What this does not prove

The theorem supplies genuine global suppression in centered scalar bosonic coordinates: exp(-S)<=product_j(1-|z_j|^2)^(1/(2K^2)). It closes the specific bare-body coercivity question, including noncompact unequal-radius tails.

It does not by itself make a complete SUSY tail small. Still required are:

1. an exact admissible super-coordinate/gauge transformation, including its Berezinian and any boundary terms;
2. a uniform estimate after Grassmann integration, where derivatives of inverse factors can change boundary powers and dimension dependence;
3. the microscopic regulators and differentiated source factors in the actual correlation observable;
4. appropriate signed cancellation, entropy/normalization and all-order control as N grows.

The scalar ordinary Jacobian (9) does not settle item 1. A scalar bound with a small fixed boundary exponent does not automatically dominate source poles or an effective invariant noncompact measure. No claim of annealed universality, the plateau, deterministic off-charge cancellation, or BGS follows. The actual full radial/torus observable remains subject to those missing implications.

## 9. Evidence boundary

The proof above is analytic and uses precisely the verified EMI theorem plus elementary finite-dimensional identities. Exact symbolic controls and bounded floating-point diagnostics are recorded separately in checks.py/checks.json and diagnostic.py/diagnostic.json. Floating-point sampling is not used as proof. The exploratory diagnostic initially failed only while serializing complex values; the script was corrected and rerun. No failed run is relabeled as a successful theorem check.

Prior search: the canonical current authorities, the balanced-phase report/addendum, and targeted canonical searches for this action, coercivity, Bhatia and exponential metric increase were inspected. No assertion of global novelty follows from those searches. The resolvent smoothing mechanism is prior elementary material in the balanced-phase report; the theorem here uses its uniform row/column form in a different nonlinear modular argument.
