# Shift-resultant / principal-subresultant transversality

Status: exact field-level identity and squarefree split-row application, with corrected hypotheses. Finite regressions are not the proof.

## Correction of the former statement

Squarefreeness of G=gcd(f,g) does not imply that a root of G is simple in f. The former field-level statement omitted this distinction. The counterexample

    f=X^2, g=X(X-1), G=X, g_t=g+t

has gcd degree one but Res(f,g_t)=t^2. The split-row application remains valid because the valid source row cofactor itself is squarefree.

## 1. Specialization-safe initial form

Let f=GA and g=GB have degrees n,m, with G monic of degree d. Put f_t=f+t phi, g_t=g+t psi, with the displayed degrees preserved. Then

    Res(f_t,g_t)
      =(-1)^(d(n-d)) Res(A,B) Res(G,A psi-B phi) t^d+O(t^(d+1)).

This coefficient identity does not require G to be squarefree. If G is the gcd, the order is exactly d when the displayed coefficient is nonzero.

To prove it first take generic characteristic-zero coefficients with G squarefree and coprime to A. A root y of G contributes t(A(y)psi(y)-B(y)phi(y))/A(y). The remaining roots contribute Res(A,G)Res(A,B), and Res(A,G)=(-1)^(d(n-d)) product A(y). Multiplying and cancelling proves the formula. Every coefficient below degree d vanishes. Both statements are polynomial identities with integer coefficients in the coefficients of monic G and A,B,phi,psi, so specialization proves them in arbitrary characteristic and for multiple roots. Since G is monic, the norm Res(G,A psi-B phi) is unaffected by a leading-degree drop of its second argument.

## 2. Corrected fixed-f shift theorem

Suppose f,g are monic of the same degree, G=gcd(f,g) is squarefree of degree d, f=GA, g=GB, gcd(A,B)=1. Assume additionally

    gcd(A,G)=1,
    psi(y)!=0 for every root y of G.

The first condition says precisely that the common roots are simple in f; squarefreeness of f is a sufficient stronger condition. For g_t=g+t psi+O(t^2),

    ord_t Res(f,g_t)=d,
    [t^d]Res(f,g_t)=Res(A,B)Res(A,G) product_(G(y)=0) psi(y).

In the fixed-degree monic subresultant convention this is, up to its fixed sign,

    psc_d(f,g) Res(A,G) product psi(y).

All factors are nonzero under the corrected hypotheses. Without gcd(A,G)=1 the formula for the degree-d coefficient remains valid, but it may vanish and is not necessarily the first nonzero coefficient.

More generally, with f fixed, let P contain the shared roots with their full multiplicities in f, and write f=P A0. When psi does not vanish at those roots, the exact order is deg P, with leading coefficient Res(A0,g)Res(P,psi). This follows from the root-product definition and does not replace multiplicities by a gcd degree.

## 3. Application to the fixed-degree product rows

For prime K=2m+1, use the specialization-safe maximal-real row cofactors P(T) and the target R_r(U). Normalize

    q_t(T)=alpha_r^(-m) R_r(alpha_r T+beta_r+t),
    psi(T)=alpha_r^(-m)R_r'(alpha_r T+beta_r).

At a maintained split embedding prime, alpha_r is nonzero, and both valid row cofactors are squarefree. At a common root y,

    q_0'(y)=alpha_r psi(y),

so psi(y)!=0. All hypotheses of the corrected theorem hold. Therefore

    ord_t Res(P,q_t)=deg gcd(P,q_0)=I_(1,r),

and the first nonzero shift coefficient is a nonzero residue-field multiplier of the first nonzero principal subresultant.

Consequently the order-three locus is equivalently

    psc_0=psc_1=psc_2=0

or vanishing of the first three shift coefficients. The statement is equality of split prime support, not equality of the integral contractions or of their valuations.

For the inverse-ratio half-degree problem, the derivative-division proof must also accommodate a common root multiple in one input. The corrected proof is recorded in cayley_inverse_resultant_transversality.md.

## 4. Evidence and boundary

The original finite tests in computations/verification/cayley_shift_psc_transversality.py remain finite controls for their actual squarefree examples. The new negative example above prevents reinstating the overbroad statement. The initial-form identity is also checked by explicit Sylvester determinants, independently of a resultant shortcut, in the current research packet.

These are local algebraic identities. They do not control the largest split rational prime dividing the lower coefficient ideal, do not remove the growing-K arithmetic bottleneck, and do not prove microscopic BGS universality.
