# First-order splitting in actual cat eigenspaces

Status: finite exact candidate, pending fresh independent audit. Canonical files are untouched. This is a discriminator for a possible bounded-block uniform route, not an all-depth theorem.

## Candidate finite result

For N=35 and175, every eigenspace of the actual M_N has a simple Hermitian compression P_lambda A_N P_lambda. Consequently exp(itA_N)M_N has simple spectrum for every nonzero real algebraic t, including the literal coupling. The N35 conclusion has a different accepted leading-minor proof already; N175 is new in this candidate. N7 fails this first-order condition exactly.

No statement about all N=7*5^e follows from these two certificates. In particular the already accepted simple A theorem is not the justification for this U conclusion.

## 1. Exact finite-order decomposition, without a square-root phase choice

Use the prescribed raw kernel G=sqrt(N)M,

    G_xy=q^(-8^(-1)(3x²-2xy+3y²)).

It has the same eigenspaces as M. Exact raw Weyl conjugation is by S=[[3,4],[2,3]]. For the tested dimensions, S has order R=6*(N/35) moduloN; N7 has order3. Therefore G^R=cI by irreducibility of the Weyl matrices, with c nonzero and algebraic. This argument needs no choice of Weil phase or square root of N.

Choose the primes p=2521 for N35 and p=4201 for N175, both split for the required q and i. All actual A,G entries and their inverses where needed are integral at this prime, since p does not divide1000N. The program explicitly checks the primitive root orders, the S order, and Gbar^R=cbar I. It finds R distinct nonzero residue roots lambda of X^R-cbar. As p does not divideR, they lift to distinct algebraic roots of X^R-c over a finite p-adic extension. The characteristic-zero projectors are

    P_lambda=(1/R)sum_(j=0)^(R-1)lambda^(-j)G^j.

They are integral idempotents and reduce to the same formula over F_p. Their images are direct summands of the integral lattice; hence their ranks and the ranks of their reductions agree. This is a projector-lattice argument, not an unsupported rank lift for a generic singular matrix.

## 2. The actual compression certificate

The verifier assembles A directly from its unchanged diagonal and upper/lower Jacobi entries, before any gauge change. It computes a basis V_lambda of ker(Gbar-lambda I) by exact modular row reduction. The free-coordinate rows are the identity. Then it computes

    C_lambda=(Pbar_lambda Abar V_lambda)_(free rows).

It checks Gbar Pbar Abar V=lambda Pbar Abar V and V C=Pbar Abar V, so C is the actual restriction of Pbar Abar to the projector image. Each characteristic polynomial is computed exactly and its gcd with its derivative is checked to have degree zero.

The completed finite certificates are:

- N35, p2521: six nonzero eigenspaces, dimensions7,7,7,5,5,4 in some order; every compression is simple.
- N175, p4201: twenty-seven nonzero eigenspaces, twenty-four of dimension7 and three of dimensions3,2,2; every compression is simple.
- N7, p337: dimensions3,2,2; the derivative-gcd degrees are2,1,1, as expected because A7=.9I.

The record includes every modular basis pivot/free-row set, compressed matrix, characteristic polynomial, and derivative-gcd degree. It also checks all matrix identities used for interpreting the compression. Integer matrix products are bounded strictly below signed64-bit overflow; no floating-point values are used for acceptance.

Each characteristic-zero projector lattice admits a basis lifting V_lambda: lift the residue vectors and apply the integral projector. The free-row minor remains a unit. In this basis, the characteristic polynomial of P_lambda A restricted to its eigenspace reduces to the recorded squarefree polynomial. Its discriminant is therefore nonzero in characteristic zero. Since M is unitary and A Hermitian in the physical complex embedding, this is precisely a simple Hermitian compression.

## 3. Why this gives a nonzero exponential discriminant

Near an eigenvalue mu of M, choose the orthogonal decomposition into its eigenspace and complement. For U(t)=exp(itA)M,

    U(t)=M+it A M+O(t²).

Set the local spectral variable z=mu(1+it x). The complementary block stays invertible for small t. Its Schur determinant, divided by the nonzero scalar factor (it mu)^m, tends to

    det(xI-P_mu A P_mu).

The m roots are distinct by the preceding certificate. Disjoint small root discs and the elementary argument used in the maintained imaginary-time proof give exactly one simple branch near each root for sufficiently small nonzero t. Different M eigenvalues have disjoint initial neighborhoods. Hence U(t) has simple spectrum for at least one t, and its exponential discriminant is not identically zero.

Every coefficient of that discriminant is a finite exponential polynomial with algebraic coefficients and algebraic real frequencies, since A has algebraic spectral projectors. The registered Lindemann–Weierstrass coefficient-separation result in frozen_arithmetic_trace_rigidity.md then implies nonvanishing at EVERY nonzero real algebraic t. This last external input is inherited and remains separately attributed.

## 4. Reproduction and next uniform input

Run exact_projector_certificate.py from any directory. It writes its declared JSON alongside the script. NumPy supplies integer arrays only; SymPy supplies exact prime, primitive-root and characteristic-polynomial arithmetic. Disabled assertions are rejected. The numerical screen is separate and is not proof evidence.

The general next input is simplicity of these compressed blocks for every pure-family dimension, together with an exact uniform multiplicity description. The observed block sizes are at most7, but this file does not promote that observation to a theorem. Proving a finite-character/CRT coefficient formula for the compressed blocks is more specific than assuming genericity of the pair or of A alone.
