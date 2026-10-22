# Whole quadratic occupation sector: true projection and signed trace

6 October 2026. Separate continuation. Every earlier scalar/source/resolvent
report and manifest remains frozen. The result below is an exact sector
identity plus an actual-symbol aggregate estimate, with self-review and
finite tensor checks. It has not yet received a fresh independent proof review.

## Result

Let U be any N-by-N unitary, N>=3, P_ij=|U_ij|^2, J_ij=1/N, and
T=(P-J)|_(1-perp). For every replica order m>=2, let P_quad be the TRUE
orthogonal projection onto the collectively embedded centered quadratic
occupation sector after removing its full U(N)-invariant component.
Its exact cyclic trace is

    Theta_N(U):=Tr(R_m P_quad C_U)
      =1/2[(Tr T)^2+Tr(T^2)]
         +||T||_HS^2/[N(N-1)]-1/N.                         (1)

The expression is independent of m. No nonorthogonal frame trace is used.
The full finite-dimensional construction and its Gram inverse are below.

For the ACTUAL fixed-tau map, the established entry bound P_ij<=C/N
implies |Theta_N(U_N)|<=C^2+C+1 for all sufficiently large odd N.
Consequently every fixed smooth compact positive-time weight satisfies

    N^-2 sum_m w(m/N) Tr(R_m P_quad C_(U_N))=O_w(N^-1).       (2)

This controls the ENTIRE specified quadratic sector, uniformly at m~N,
and not just one slow vector. It cannot supply an order-N-per-time plateau
correction by itself. The other replica sectors remain unestimated.

If “quadratic occupation” means all degrees at most two, after Haar removal
one additionally has the orthogonal additive sector. Its trace is Tr T,
so the corresponding exact total is Tr T+Theta_N(U), with the same O(1)
pointwise and O_w(N^-1) aggregate bounds. Constants are removed by Haar
projection. Both meanings are thus covered explicitly.

For the prescribed initial metaplectic M, P=J, hence Theta_N(M)=-1/N.
The entire quadratic source map has singular values

    N^-1/2, multiplicity (N-3)/2;
    N^-1,   multiplicity 1;
    0,      multiplicity (N-1)^2/2,                           (3)

for odd N. These are the source map's singular values on the truly
orthonormalized quadratic sector, independent of m>=2. In particular
||Pi C_M^*Y||<=N^-1/2||Y|| for every Y in this sector.
At actual time tau the exact bound becomes

    ||Pi K_m(tau)^*Y||<=N^-1/2||Y||+|tau|N||H_mY||.         (4)

No all-degree assertion or positive-memory closure follows.

## 1. Sector, multiplicities and full Haar subtraction

Work on operators over (C^N)^(tensor m), with ordinary unnormalized
Hilbert-Schmidt inner product. C_U denotes conjugation by U^(tensor m).
Pi is the equal-occupation projection. R_m is simultaneous cyclic slot
conjugation. Let D_0 be the traceless diagonal operators, dimension d=N-1.
Choose a real orthonormal diagonal basis D_alpha, alpha=1,...,d. Its
complexification is understood for the operator space.

For A in Sym^2 D_0, define the collective pair embedding

    J_m A=sum_(r<s) A_rs.

Every A has zero partial trace in either slot. Distinct pair embeddings
are therefore HS-orthogonal, even if they share one slot. Exactly

    <J_m A,J_m B>=b_m N^(m-2)<A,B>,
    b_m=binomial(m,2).                                      (5)

The sector is cyclically fixed pointwise because every permutation of
the slots permutes the complete set of unordered slot pairs.

Put r=sum_alpha D_alpha tensor D_alpha in Sym^2 D_0, so ||r||^2=d.
For one pair, Haar twirling gives

    P_0 A=<r,A>/(N^2-1) (Swap-I/N).                         (6)

This follows by the two traces against I and Swap: the first is zero
and the second is <r,A>. The twirl's coefficients are consequently fixed.
Embedded in all pairs, (6) computes the FULL collective Haar projection
of J_m A, since the unoccupied slots carry identity throughout.

Define F_m=(I-P_0)J_m/sqrt(b_m N^(m-2)). The Gram matrix of this embedding is

    F_m^*F_m=G=I-c|r><r|,  c=1/(N^2-1),
    G^-1=I+|r><r|/[N(N-1)].                                (7)

Its eigenvalue on r is N/(N+1)>0, and its other eigenvalues are one.
Thus F_m is injective and the sector has dimension N(N-1)/2 for every
m>=2. The true orthogonal projection is

    P_quad=F_m G^-1 F_m^*.                                  (8)

This is the normalization that a sum of individual vector pairings would
miss. The sector lies in ran Pi and is orthogonal to the full invariant
space. R_m acts identically on it.

The diagonal functions of occupation numbers of degree at most two split
as constants, additive traceless diagonal functions, and J_m(Sym^2D_0).
Zero partial traces make their centered embeddings orthogonal. Removing
Haar invariants removes the constant and replaces the last summand by
ran F_m; the additive summand is already Haar-orthogonal. This proves
the degree-at-most-two scope stated above.

## 2. Exact actual-unitary signed trace

Compression of one-copy conjugation to D_0 is the real matrix T in the
chosen real diagonal basis: its entries are Tr(D_alpha U D_beta U^*).
It is P restricted to the zero-sum subspace; subtracting J gives the same
restriction. Pair-slot orthogonality from (5), valid also after C_U,
gives the exact block

    F_m^* C_U F_m=Sym^2 T-c|r><r|.                           (9)

Indeed the raw pair block is Sym^2 T, and the invariant part is fixed
pointwise by C_U, so orthogonal subtraction removes its Gram contribution.
Since R_m fixes ran F_m, cyclic insertion does not change (9). Taking
the trace with the TRUE projection (8) yields

    Tr(R_m P_quad C_U)
       =Tr[G^-1(Sym^2 T-c|r><r|)].                          (10)

The three contractions needed to evaluate this expression are

    Tr(Sym^2 T)=1/2[(Tr T)^2+Tr(T^2)],
    <r,Sym^2 T r>=Tr(T T^T)=||T||_HS^2,
    c<r,G^-1r>=1/N.                                        (11)

The first follows from the symmetric projector (I+Swap)/2 on D_0 tensor
D_0. The second uses the real matrix T; it is not Tr(T^2) unless T is
symmetric. The last uses ||r||^2=N-1 and (7). Equations (10)--(11) prove
(1), including nonnormal and nonsymmetric P.

No independent phase average is imposed on U. Pi and Haar twirling here
define exact finite-dimensional orthogonal subspaces; all origin-neutral
replicas and every coordinate multiplicity remain in the ambient operator.
This construction does not identify these replicas with the stationary
labels or homoclinic displacements of the separate physical-weight table.

## 3. Actual flatness closes this whole sector on the target normalization

The maintained `BGS/mathematics/position_chain_mixing.md`, Sections 3--4,
supplies max|U_ij|^2=O(N^-1) at the literal fixed tau, from the actual
four-branch parametrix. The startup is not made effective. Its mixing gap
is not needed for the estimate here.

For any doubly stochastic P with max P_ij<=C/N, C>=1,

    0<=Tr P<=C,
    0<=Tr(P^2)=sum_ij P_ij P_ji<=C,
    0<=||P-J||_HS^2=sum_ij P_ij^2-1<=C-1.

Since Tr T=Tr P-1 and Tr(T^2)=Tr(P^2)-1, these inequalities imply directly
from (1) that |Theta_N(U)|<=C^2+C+1. The same bound plus C applies after
adding the degree-one sector. All bounds are independent of m.

For m>=2 the summand in (2) is exactly the SAME Theta_N(U_N). There are
O_w(N) terms on a compact Heisenberg band, proving (2). In particular this
whole sector has vanishing contribution on the N^-2 pair normalization.
At the flat metaplectic point its exact negative trace -1/N is much smaller
than its dimension; multiplying a chosen scalar coefficient by the dimension
would give the wrong sector trace.

## 4. Entire metaplectic source singular spectrum

Use the complex orthonormal Fourier-diagonal basis

    D_k=N^-1/2 diag(e_N(kj)),  k=1,...,N-1.

Metaplectic conjugation maps each D_k to one nonzero Weyl shift divided by
sqrt(N); its coordinate shift is +/-4k modulo N, with the sign set by the
conjugation direction. Balanced projection on two copies retains only pairs
of shifts summing to zero, hence only symmetrized pairs {k,-k}.
Because N is odd, k and -k are distinct.

Let E be the span of these paired Fourier tensors. Its dimension is
h=(N-1)/2. Each normalized paired tensor has two disjoint difference
supports after projection, with N entries on each support and magnitude
1/(sqrt(2)N). Its squared output norm is 1/N. Different pairs have disjoint
supports. Thus the raw source A_0 satisfies

    A_0^*A_0=(1/N)P_E.

The contraction vector r belongs to E: in this basis it is sqrt(2) times
the sum of all normalized {k,-k} tensors. Removing the Haar component
changes the source Gram to

    A^*A=(1/N)P_E-c|r><r|.                                  (12)

The input metric is G, not identity. The actual squared singular values
therefore are those of G^-1/2 A^*A G^-1/2. On E perpendicular to r the
eigenvalue is 1/N. On r it is

    [1/N-c(N-1)]/[1-c(N-1)]=1/N^2.

On E-perp it is zero. This proves (3), with the precise multiplicities.
The common factor b_m N^(m-2) cancels on both sides by (5). The additive
sector, if included, has zero metaplectic balanced image and only adds
zero singular values. For N=3 the 1/sqrt(N) multiplicity is zero, so the
exact source norm is 1/N; the stated upper bound remains valid.

Finally, K_m(t)^*=C_m^*exp(-itNH_m), and the spectral-theorem Duhamel bound
||(exp(-itNH_m)-I)Y||<=|t|N||H_mY|| proves (4) for every real t. It is not
an expansion in a shrinking parameter.

## 5. Checks, provenance and remaining boundary

`check_sector.py` builds the entire sector in the full tensor operator
space at (N,m)=(3,2),(3,3),(3,4),(5,2),(5,3),(7,2),(9,2). It uses a real
Helmert basis for D_0, explicitly constructs F_m, applies G^-1/2, and checks
orthonormality of the resulting columns. It then computes the direct cyclic
trace at t=0,.001,.137 and compares it to (1). The source singular spectrum
is computed from the full balanced projection and compared with (3).

All checks passed in float64/complex128 arithmetic. Maximum trace residual
was 2.3e-16 and source-spectrum residual 2.5e-16. The numerical times test
the finite identity; the actual fixed-tau aggregate follows from the proof
and the inherited actual flatness theorem. No interval or asymptotic
numerical certification is claimed.

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python check_sector.py > checks.json

The separate manifest records source hashes and execution scope. All earlier
frozen output hashes were checked unchanged. No canonical file was edited.
The result controls degree at most two only. Higher occupation degrees,
non-balanced replica sectors, the complete signed trace, and BGS remain open.
