# Positive spectral-overlap form of the unresolved untwisted echo

Finite exact derivation; the model-specific asymptotic input is only the
accepted FM-028 quasimode annihilation and FM-021 flatness. This note does not
resolve the spectral concentration obstacle.

Let U v_alpha=lambda_alpha v_alpha, with an arbitrary orthonormal eigenbasis,
and K_b=Z_b U Z_b*. Define

    C_(alpha,beta)=(1/N)sum_b <v_alpha,K_b v_alpha>
                              conjugate(<v_beta,K_b v_beta>).

This C is a positive semidefinite Gram matrix. If
X_(alpha,beta)=|v_alpha><v_beta| has ordinary HS norm one, then

    C_(alpha,beta)=<X_(alpha,beta),D X_(alpha,beta)>_HS.

The identity is about DIAGONAL superoperator matrix entries at the
alpha,beta eigenoperator, not <P_alpha,D P_beta>. Those are different
quantities. In particular positivity of the Gram matrix is not positivity
of the full nonselfadjoint D.

The exact echo is

    E_N,m(0)=sum_(alpha,beta)lambda_alpha^(m-1)
          conjugate(lambda_beta^(m-1)) C_(alpha,beta).

Equivalently, for u_m(alpha)=conjugate(lambda_alpha)^(m-1),

    E_N,m(0)=u_m* C u_m >=0.

The conjugation in u_m fixes the orientation for the usual Hermitian
quadratic-form convention.

## Operator bound from flatness

Define F:End(C^N)->C^N by

    F(X)_c=sum_j X_(j+c,j) U_(j,j+c).

Cauchy--Schwarz shows ||F||_(HS->l2)^2<=C_flat under
max |U_jk|^2<=C_flat/N. The map J:a->sum_alpha a_alpha P_alpha,
P_alpha=|v_alpha><v_alpha|, is an HS isometry. Finite Fourier Parseval in b
identifies C, up to transpose/conjugation conventions, with the Gram matrix
of the columns F(P_alpha). Consequently

    ||C||<=C_flat.

No simplicity assumption is needed; the arbitrary eigenbasis gives a valid
isometric diagonal subspace. The trace of C is basis-dependent inside a
nontrivial eigenspace, but the stated estimates hold for any such choice.

## What actual compact quasimode annihilation adds

For alpha!=beta, X_(alpha,beta) is centered and an exact adjoint eigenvector.
FM-028 C1/C6 is uniform over every adjoint eigenphase, so

    sup_(alpha!=beta) |C_(alpha,beta)|=o(1).

For alpha=beta, P_alpha=I/N+Y_alpha with Y_alpha centered, commuting with U,
and ||Y_alpha||_HS<=1. Since D fixes I and preserves its orthogonal complement,

    C_(alpha,alpha)=1/N+<Y_alpha,D Y_alpha>=1/N+o(1)

uniformly. Positivity of C gives

    Tr C=o(N),  ||C||<=C_flat.

The 1/N identity contribution has been kept explicitly. These statements
supply no rate at scale 1/N in the eigenphase differences.

## Exact remaining positive estimate

For nonnegative w in C_c^infinity((a,b)), define

    H_N(w)=sum_m w(m/N) u_m u_m*,

so H_N(w)>=0 and the untwisted normalized echo is

    N^-2 Tr[C H_N(w)].

The missing action/spectral input is the absence of sufficient alignment
between the low-trace Gram matrix C and the high-eigenvalue directions of
this time-band Gram matrix H_N(w). A local spectral pair upper bound is one
sufficient route, as in the main lemma, but is not asserted necessary.

The generic period-six counterexample has D_N-J_H->0, hence even stronger
quasimode annihilation, and still has E_N,m(0)=N for every 6|m. Thus
||C||=O(1) and Tr C=o(N) alone cannot prove the needed normalized bound.
Repeated macroscopic eigenspace clusters concentrate the time-band energy.
The actual finite-support sine action excludes replacement of U by that
family, but a quantitative estimate using that action is still needed.
