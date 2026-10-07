# Separate extension: ordinary matrix-valued bosonic blocks

7 October 2026. This is an additional candidate theorem, separate from the frozen scalar report. Author derivation; independent review pending. It supplies no fermionic or source estimate.

## Exact claim

Let U be N by N unitary and let P=|U|^2 have max P_ij<=C/N and ||P-J||_2<=rho<1. Let each Z_j be an arbitrary complex k by k strict contraction, not necessarily normal, and set Z=diag(Z_1,...,Z_N), U_k=U tensor I_k. Assume sum_j Z_j=0. Define

S=log|det(I-U_k Z U_k* Z*)|-log det(I-ZZ*),
H=sum_j -log det(I-Z_j Z_j*),
K=1+sqrt(C-1)/(1-rho).

Then the same proof gives

S>=H/(2K^2),

with no dependence of the constant on k. It is a theorem about finite matrices and arbitrary strict contractions, not an assertion that the original full SUSY fields can be replaced by such blocks.

## Nonnormal polar convention and dilation

Use right polar form Z_j=V_j tanh R_j, R_j=atanh|Z_j|, and W_j=V_j R_j, where a unitary extension of the partial polar factor may be chosen. The product W_j is independent of that extension on the kernel. Then Z_j=V_j tanh|W_j|. Put W=diag(W_j) and X=[[0,W],[W*,0]].

Let C_L=(I-ZZ*)^(-1/2), C_R=(I-Z*Z)^(-1/2). The exact exponential is

g=exp X=[[C_L,Z C_R],[Z* C_L,C_R]],

using C_L Z=Z C_R. With K_U=diag(U_k,U_k) and T=g^(-1)K_U g, its upper blocks are

F=C_L(U_k-Z U_k Z*)C_L,
G=C_L(U_k Z-Z U_k)C_R.

Thus FF*-GG*=I and |det F|=exp S. No commutation of Z_j and Z_j* is assumed. The conjugate determinant identity relating U_k* and U_k orientations remains valid by cyclic permutation inside det(I-AB).

The elementary polar/J-unitary argument in the scalar report produces Nk parameters t_l with S=sum_l logcosh t_l. EMI and the Ky Fan argument give

S>=Phi(W-U_k W U_k*),
Phi(A)=Tr logcosh|A|.

Pinching onto the N site blocks yields

S>=sum_j Phi(W_j-sum_l P_jl W_l).                            (B1)

## Convexity and exact gradient

For any rectangular or square complex A, let H_A=[[0,A],[A*,0]] and f(s)=logcosh s. Then Phi(A)=one half Tr f(H_A). Since f is convex, the spectral trace functional is convex on Hermitian matrices; hence Phi is convex as a real function of A. It is even and unitarily invariant.

Under the real Hilbert--Schmidt inner product ReTr(A*B), its gradient is

grad Phi(A)=V tanh|A|, where A=V|A|.

Indeed the derivative of Tr f(H_A) is Tr f'(H_A)dH_A, and f'(H_A)=tanh H_A has upper-right block V tanh|A|. The two off-diagonal traces and the one-half factor cancel. This also holds at singular A by smoothness of the even analytic function f; tanh(0)=0.

Consequently grad Phi(W_j)=Z_j. Thus sum Z_j=0 makes B=0 minimize the convex function sum_j Phi(W_j-B). It does not assert sum W_j=0.

## Same inverse and Jensen estimate

Write W_j^0=W_j-N^(-1)sum_l W_l, and V_j=W_j-sum_l P_jl W_l. Then W^0=R V in the site index, with R=(I-P+J)^(-1) and the scalar row and column absolute bounds <=K from the scalar report.

Convexity, evenness, and Phi(0)=0 give

sum_j Phi(W_j^0/K)<=sum_j Phi(V_j).

The scalar inequality logcosh(s/K)>=K^(-2)logcosh s applies to singular values, so

S>=K^(-2)sum_j Phi(W_j^0)>=K^(-2)sum_j Phi(W_j)=H/(2K^2).

The second inequality is the preceding convex minimization. Finally H=2sum Phi(W_j) follows singular value by singular value from 1-tanh^2 r=sech^2 r.

## Boundary

No global matrix-valued Mobius centering theorem, its Jacobian, or a super-Berezinian is proved by this extension. Its centering condition is a stated finite-matrix hypothesis. The scalar gauge/Jacobian result cannot be substituted for a block or super-coordinate change. Source insertions, microscopic regulators, Grassmann integration, all-order signed cancellation and an N->infinity tail theorem remain open.
