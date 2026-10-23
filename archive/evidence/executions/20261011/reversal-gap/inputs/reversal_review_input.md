# General contraction censoring and reverse-channel gap

Draft analytic extension of TRACE-073; independent reconstruction pending.

Let C be any complex matrix with ||C||op<=1, A retained, D deleted, I-C_DD
invertible, and Cc=C_AA+C_AD(I-C_DD)^(-1)C_DA. For arbitrary x on A,
t=(I-C_DD)^(-1)C_DA x, z=(x,t). Then Cz=(Cc x,t). For 0<=s<=1,

||Cz||^2-s^2||z||^2=||Cc x||^2-s^2||x||^2+(1-s^2)||t||^2.

The lift is injective. Positive inertia of C*C-s²I transfers every strict
singular-value subspace of Cc above s to C. Hence sigma_j(Cc)<=sigma_j(C)
for every 1<=j<=|A|. This proves ||Cc||p<=||C||p after zero padding for all
p>=1, including arbitrary nonnormal contractions. No mean subtraction is used.

For a unitary S=[[A,c],[b,a]], define reversal matrix R_ij=S_ij conj(S_ji).
It is Hermitian and ||R||op<=1: |R_ij|=sqrt(P_ij P_ji), so row and column
absolute sums are <=1 by CS and unitarity. Note that |R_ij| is generally NOT
bounded pointwise by P_ij; the direct CS row/column proof is essential.

For q=w/(1-aw), d=1-|a|² and fresh uniform w, S'=A+cqb. Put
C0=diag(c) conj(A)^T diag(b), v_i=c_i conj(b_i). Exact expansion gives

R(S')=R_AA+q C0+conj(q) C0*+|q|² v v*.

Since R_Ae=v, R_eA=v*, R_ee=|a|² and E q=0, E|q|²=1/d,
E R(S')=R_AA+v v*/d=Rc, the classical algebraic Schur complement of R.
Its entire singular spectrum contracts by the general lift theorem.

Let delta=max|S_ij|²<=1/4. ||C0||op<=delta and
||v||²=sum_i |c_i|² |b_i|²<=delta d.
The centered Hermitian increment M=qC0+conj(q)C0*+(|q|²-1/d)vv* has E M=0
and ||M||op<=4delta/(1-sqrt(delta))<=8delta, exactly the constant in the
intensity proof.

Under the same all-time entry-flatness event A_m, m>=4Kell, initial
||R_N||op<=rho_R and even p>=2, for g>N^(1/p)rho_R:

P(A_m intersect {max_{u>=m}||R_u||op>=g})
 <=64 N^(2/p)(p-1)K²ell²/[m(g-N^(1/p)rho_R)²].

Use the same stopped Schatten-p potential F_r, with r=N^(1/p)rho_R, now
on R_u itself padded to dimension N. Every mean Schur complement contracts
F_r, the fresh phase linear term has zero mean, and the same noise bound
sums to 64 N^(2/p)(p-1)K²ell²/m. Stop at the full first flatness/reversal-gap
crossing; include its complete value and simultaneous exits. No centering
by J is appropriate for this channel.

FM-022 proves ||R_N||op->0 for the exact original map. Choosing a fixed
sufficiently small rho_R, p=2ceil(ell), m=ceil(ell^(3+kappa)) and any fixed
g>sqrt(e)rho_R gives the same O(ell^(-kappa)) exceptional intersection
probability. The intensity/reversal gap bounds can be united by a finite
union bound. No probability of A_m, full microscopic law or BGS follows.
