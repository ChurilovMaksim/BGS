# Actual scalar commutant on the unramified higher-seven-primary family

Base: BGS d4132ccee82849b644520d88c953cb9b33382a59, read-only. New candidate proof; independent review required. Earlier frozen overlays remain unchanged. The finite polynomial certificates referenced below are part of the proof dependency, not samples in N.

## Theorem and boundary

For every odd N with49|N and5∤N, the actual prescribed pair A_N,M_N has complex common commutant C I.

This is an infinite actual-model family, not a theorem merely about an upper-bond surrogate. It does not cover5|N or7|N with49∤N. FM-008 separately covers7∤N. N7 remains genuinely exceptional. The full all-odd-N claim, seven-divisible spectral simplicity, quantitative gaps, signed Heisenberg comparison and microscopic BGS are not asserted.

## 1. Direct reduction of the actual pair

Use the field K=F_(5^f), f=ord_N(5), with q a primitive Nth root and w=q^(N/7) primitive seventh root. Reduce i to2 at the Gaussian prime over5. Since5∤N, the order of q is exactly N. The actual integral matrix1000A reduces to its weighted upper-bond part B: diagonal coefficients vanish, -3+4i vanishes, and -3-4i becomes4. Every internal bond is nonzero because q^(7u)≠1 for1<=u<L=N/7 and an odd-order root cannot equal-1. The raw kernel G=sqrt(N)M remains invertible and integral.

The detailed actual formula and rank-lifting statement are in actual_mod5_bridge.md. Normalize the seven upper chains by the unit diagonal D, obtaining J=J_L tensor I_7 and simultaneously Gtilde=D^(-1)GD. A scalar common commutant over K produces a nonzero (N²−1)-minor of the actual commutator map, which lifts to characteristic zero. Thus it is enough to prove scalar common commutant of J,Gtilde over K.

## 2. Two bounded endpoint conditions force scalar C_0

A commuter with J has upper block-Toeplitz coefficients C_0,...,C_(L−1). The last row, column depths0,...,6, consists of nonzero rank-one blocks

E_s=gamma_s u_s v_s^T,
u_s=D_(L−1)^(-1) f_(4+2s),
v_s^T=f_(s+3)^T D_s,
f_b(j)=w^(bj).

The columns u_s are independent. Up to nonzero row scalars, the right-row matrix is

V_(s,j)=w^(j(2s+3))/product_(u=1)^s(1+q^u w^j)^2.

The verified Casoratian certificate proves V invertible over K: its integer coefficient determinant P has degree113 and gcd_F5(P,q^(5^84)−q)=q²+1. A root with order divisible by49 would have degree divisible by42=ord_49(5), impossible for those factors. Denominators are units. This is the independently checked strengthening in bgs_seven_adic_independent_review/additional.py.

From the exact last-row equations

[C_0,E_s]=sum_(d=1)^s E_(s−d) C_d,

apply the s-th dual row of the u-basis. The right side vanishes, giving v_s^T C_0=lambda_s v_s^T. The s=0 equation also gives C_0u_0=lambda_0u_0. Hence in the V basis, C_0 becomes Lambda=diag(lambda_0,...,lambda_6), and h=Vu_0 is an eigenvector of Lambda for lambda_0.

Let Z=diag(w^j), R=Z^(−2), and

Q=diag((1+wq^(−1)w^j)^(−2)).

The actual last bond has form b_(L−1,j)=constant*w^(−j)(1+wq^(−1)w^j)^2. The raw penultimate-row column0 has its left Fourier frequency shifted by−1 and its right frequency shifted by−2 relative to E_0. Therefore its simultaneously gauged block is

F_0=alpha Q u_0 v_0^T R,

with alpha≠0. This uses the actual last-bond relation and is not true for independently chosen penultimate and final gauges.

The penultimate-row column0 equation is

[C_0,F_0]+C_1 E_0=0.

In the V basis put x=VQ u_0 and y=v_0^T R V^(-1)=f_1^T V^(-1). For every column j≠0, the C_1E_0 term vanishes. Consequently

(lambda_i−lambda_j)x_i y_j=0, for every i and j=1,...,6.  (A)

It is sufficient that

(B1) y_j≠0 for j=1,...,6;
(B2) (V Q V^(-1))_(0,0)≠0.

Indeed x≠0. Choose any i with x_i≠0. By(B1), all lambda_1,...,lambda_6 equal lambda_i. If lambda_0 were different, the relation Lambda h=lambda_0h would force h to be a nonzero multiple of e_0. Then x_0 would be the same nonzero multiple of (VQV^(-1))_(0,0), which is nonzero by(B2). Equation(A) with i=0 would contradict lambda_0 being different. Thus all seven eigenvalues agree and C_0 is scalar.

This argument never discards C_1. It uses exactly the column where that term is supported, and ignores that column when deriving(A).

## 3. Bounded polynomial certificates for(B1) and(B2)

Let z be a formal variable and define the7-by-7 polynomial coefficient matrix C(q) by the remainders modulo z^7−1 of

p_t(z)=z^(2t) product_(u=t+1)^6(1+q^u z)^2, t=0,...,6.

Its determinant is the Casoratian polynomial P. Clearing the nonzero column factors in V and using the seven-point Fourier evaluation map shows:

- y=r(q) C(q)^(-1), where r(q) is the coefficient row modulo z^7−1 of z^5 product_(u=1)^6(1+q^u z)^2.
- The diagonal quantity in(B2) is r_Q(q,w) C(q)^(-1)e_0, where r_Q is the coefficient row modulo z^7−1 of
  product_(u=1)^6(1+q^u z)^2/(1+wq^(−1)z)^2.

All coefficient arithmetic is explicit. In the ring z^7=1,

(1+wq^(−1)z)^(-2)
 =q²[sum_(k=0)^6 (−w)^k q^(6−k)z^k]^2/(q^7+1)^2.

The denominator is nonzero at an odd-order q. Thus(B2) has numerator K(q,w) polynomial in q,w, modulo Phi_7(w), and denominator a nonzero scalar multiple of P(q)(q^7+1)^2.

The builders bounded_boundary_polynomials.py and bounded_boundary_norm.py compute these expressions and check the polynomial inverse identity C Adj=den I. Their denominators are associates of P modulo5.

For(B1), the numerator degrees and irreducible factor degrees over F5 are:

- j1: degree126; factors of degrees1,1,1,6,23,27,64, with multiplicities recorded in the certificate;
- j2: degree134; degrees1,1,3,4,32,85;
- j3: degree143; degrees1,8,134;
- j4: degree153; degrees1,1,3,3,60,83;
- j5: degree164; degrees1,8,149;
- j6: degree176; degrees1,1,2,2,5,6,6,6,6,6,6,6,8,73.

None is divisible by42. The complete coefficient arrays, multiplicities, multiplication checks and irreducibility identities are in bounded_factor_certificates.json.

For(B2), take the norm/resultant

N(q)=Res_w(K(q,w),Phi_7(w)) over F5.

It has degree828. Its irreducible factor degrees, with multiplicities, are

1^24, 6^6, 36, 54, 66, 246, 366.

Again no factor degree is divisible by42. Thus N(q) cannot vanish at a root whose multiplicative order is divisible by49. Therefore K(q,w) is nonzero for every primitive seventh root w paired with such q. This proves(B2), including the actual w=q^L.

**Why the finite certificates imply the uniform claim.** If a nonzero alpha over F5 has multiplicative order divisible by49, its field degree d satisfies49|5^d−1, hence42|d. Its minimal polynomial must be an irreducible factor of any polynomial vanishing at alpha. The certified factor lists have no such degree, so no such alpha is a zero. This excludes arbitrarily large N uniformly; it is not extrapolation from tested dimensions.

**Irreducibility verification.** verify_bounded_factors.py independently checks every factor list by multiplication and checks each monic degree-d factor by the exact Rabin identities: q^(5^d)=q modulo the factor, and gcd(f,q^(5^(d/p))−q)=1 for every prime p|d. The first says each irreducible constituent has degree dividing d; the gcd conditions exclude every proper divisor, forcing irreducibility. Exponents are evaluated by repeated fifth powers modulo f. The scripts fail when verification assertions are disabled.

## 4. Higher tails and the finite base

For L>=21, scalar C_0 forces every higher C_d to vanish by the independently checked minimal-tail argument. For the smallest d with C_d nonzero:

- If d<=L−7, the last-row equations at columns d,...,d+6 isolate seven independent weighted right rows, so C_d=0.
- If d>=7, the bottom d rows at column d isolate Gtilde_(r,0)C_d=0; seven consecutive right Fourier rows are independent, so C_d=0.

Every positive d falls in one of these cases. The independence assertions hold over K by the Casoratian-unit proof and the nonzero seven-point Fourier determinant.

For N49, L7 is separately verified in the actual residue field F5[q]/Phi49. actual_residue_base49.py constructs the reduced B,G directly, and for T=B+G obtains cyclic rank49 and rank48 of [0,[T,B]e_0,...,[T^48,B]e_0]. The elementary cyclic-commutant certificate proves the residue common commutant scalar. Its field arithmetic and primitive-root order are exact. This finite base handles the short-chain tail exception without an unproved extension of the long-chain dichotomy.

It follows that the residue common commutant is scalar for every N in the theorem. The full commutator-rank minor lifts to characteristic zero, completing the actual-family proof.

## 5. Unresolved branches and review status

The proof relies on direct reduction at5 with all internal bonds units and the Fourier kernel retaining rank. It does not apply when5|N. Nor does its rank-one endpoint formula apply when7|N but49∤N. These remain separate algebraic branches.

This candidate adds an actual-model theorem if its bounded polynomial builders, the two-row implication and the residue lift pass independent review. The characteristic-zero weighted-surrogate theorem was already separately reviewed, but it is not the justification for the residue argument here. No canonical theorem, ledger, manuscript or evidence file has been modified by this worker.
