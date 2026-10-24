# Actual phase-map monotonicity, Frostman bound and averaged Fourier squares

This maintained extract contains only the independently reviewed Sections1-3
of the frozen transversality source. The full original remains historical
provenance, not blanket acceptance of later conditional or literature claims.
It concerns the actual fixed-tau stationary action, not complete quantum
weights. The independent reviewer supplies the explicit constant112 below.

## 1. Sharper actual Holder exponent without a C1 claim

The factor 2 in the weighted resolvent can be replaced by beta=29/5.
For the infinite cat Green function g_j=(1/sqrt(2))lambda^(-|j|),

L_beta=sum_j beta^|j| g_j
 =(1/sqrt(2))(1+beta/lambda)/(1-beta/lambda)<300.

The same bound holds on finite cycles by periodization and cyclic distance.
The weighted nonlinear Hessian norm is at most
2eta(1+beta)<14eta. Since eta<2*10^-70,

||G_tau||_beta <=300/(1-4200eta)<=301,
||G_tau-G_0||_beta <=1,264,200 eta.

Every interpolation and infinite-chain argument of the frozen locality proof
therefore holds with beta weights. In particular

|D_m-D_infty|<=4*10^6 eta beta^-m,
[D_infty]_(C^alpha_beta)<=2*10^7 eta,
alpha_beta=log(29/5)/log(3+2sqrt(2)) approximately 0.99722634.

The constants follow explicitly: ||G_tau E||_beta<=4214eta; the shifted
Green convolution costs at most 300 beta^-L; its nonzero-period sum costs
at most 725 beta^-m. For the Holder split the geometric sum constant 500
suffices, and 9632*500*4<2*10^7. These are conservative fixed-tau estimates,
not a passage to beta=lambda. The associated quadrature error improves to
O(N beta^(-m/2)). No uniform C1 conclusion follows.

## 2. Exact order geometry of H_tau=q+D_infty

Let X_(s,j)(q,p)=(S^j(q,p))_q+s g_j+u_(s,j)(q,p), for 0<=s<=1.
The infinite corrected stationary equation is

K_0 X_s-grad R_tau(X_s)=s e_0.

This is an identity of local equations, not an infinite action sum.
If q is increased by delta>0 with p fixed, the difference W_j of the two
solutions satisfies

(K_0-E_bar)W=0,
W_j=a_j delta+O(eta),  a_j=(lambda^j+lambda^-j)/2,

where E_bar is an averaged actual Hessian. The matrix has negative
neighbour entries and row mass at least 1-4eta>0. Moreover W_j tends to
positive infinity at both ends. A negative minimum would contradict its
homogeneous equation; a zero minimum would propagate to every neighbour.
Therefore W_j>0 for every j.

Since H_tau(q,p)=integral_0^1 X_(s,0)(q,p)ds-(1/2)g_0,
H_tau is strictly increasing in q at every fixed p. It has the lift rules
H_tau(q+1,p)=H_tau(q,p)+1 and H_tau(q,p+1)=H_tau(q,p).
The same comparison gives monotonicity in the open cone
Delta q>sqrt(2)|Delta p|, since the cat background increment then tends
to positive infinity in both time directions.

## 3. Quantitative inverse bound and an actual Frostman estimate

This section is a result about mu_tau, not merely a small-Holder-perturbation
heuristic. Let 0<delta<=1. If delta>=8eta, the direct correction bound gives
W_0>=delta-4eta>=delta/2. Otherwise choose the least L with
a_L delta>=8eta. Then W_L>=4eta and

L<=1+log(16eta/delta)/log lambda.

All W_j are nonnegative. The local homogeneous equation gives

W_j>=[(1/4-eta)/(3/2+2eta)] W_(j+1)>=(1/7)W_(j+1).

Thus W_0>=4eta 7^-L. Put p_*=log7/log lambda>1.
Because eta<=1/16, both delta regimes imply

H_tau(q+delta,p)-H_tau(q,p)>=(1/28)delta^p_* .         (T1)

For the small-delta regime use
(4eta/7)(16eta)^(-p_*)=(1/28)(16eta)^(1-p_*)>=1/28.
This proof is uniform in the matching parameter s and then integrates in s.

Each q-fibre is a circle homeomorphism. If I is an arc of length |I|,
its preimage has q-length at most (28|I|)^gamma, where

gamma=1/p_*=log(3+2sqrt(2))/log7 approximately 0.9059.

Integrating over p proves the ACTUAL measure estimate

mu_tau(I)<=(28|I|)^gamma.                             (T2)

In particular mu_tau has no atoms. It is not claimed to have a density.

A direct Fejer-kernel argument then gives

sum_(1<=n<=M)|muhat_tau(n)|²<=112 M^(1-gamma),
M^-1 sum_(1<=n<=M)|muhat_tau(n)|²<=112 M^-gamma.         (T3)

Indeed the Fejer kernel is bounded by C M/(1+M||x||)^2. Integrating its
convolution against mu_tau twice and applying (T2) on dyadic annuli yields
O(M^(1-gamma)); using the kernel of width 2M bounds the unweighted sum.
This is an averaged square bound, not pointwise decay at every integer N.
It cannot replace the unaveraged all-odd-dimension TRACE-005 target.


## Explicit Fejer constant and retained boundary

For F_K(x)=K^-1|sum_(j=0)^(K-1)e(jx)|², use
F_K<=min(K,1/(4K||x||²)) and the ball bound (56r)^gamma.
Dyadic annuli give integral F_K(x-y)dmu(y)<=2*56^gamma K^(1-gamma).
With K=2M, the unweighted positive-frequency square sum is at most
4*28^gamma M^(1-gamma)<=112 M^(1-gamma), since 0<gamma<1.
This is the independent review's constant, not a new external theorem.

The average is over Fourier index/dimension cutoff M, not over times m at
a fixed N. It does not imply pointwise decay at each integer or each odd
dimension, eliminate sparse exceptional frequencies, or control the full
transport/determinant/quantum-integral weights. Sections4-5 of the original
source, one-sided analyticity, first-response obstruction, external Fourier
decay inputs and unreviewed aggregation notes are not promoted here.
The complete signed trace hierarchy and BGS remain open.
