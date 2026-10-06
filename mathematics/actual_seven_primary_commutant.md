# Actual scalar joint commutant in every odd dimension except seven

Claim ID: BGS-FM-024. Original higher-seven publication base: 300d99270d11c87d0aa84e9d8f624491788629ba; first-seven integration base: 66724291b2ec77c22823f52ecc5ee56278fed096.
Status: exact project proof with independent internal review and computer-assisted finite polynomial inputs. This is the sole current theorem owner for this family; historical raw/weighted surrogate and failed-endpoint routes are provenance only. The literal-U corollary additionally uses the already registered external Lindemann–Weierstrass theorem. No external-referee acceptance or global-priority claim.

## Current combined scope

The actual pair (A_N,M_N) has scalar complex joint commutant for every odd
N>=3 except N=7. This is an explicit combination of separately scoped proofs:

- For 7∤N, prior [FM-008](frozen_algebraic_spectral_simplicity.md) gives simple
  A_N and nonzero entries of M_N in its eigenbasis. A joint commuter is
  diagonal there, and every diagonal value agrees. This r=1 leaf now has a [fresh independent audit](../record/fm008_fresh_independent_review.md)
  and uses no Lindemann–Weierstrass input. The separate literal-U
  algebraic-entry corollary below still requires that external theorem.
- For 49|N,5∤N, the higher-seven proof below applies.
- For 7|N,49∤N,N>7, the [chain-trace proof](ramified_first_seven_commutant.md)
  includes arbitrary five-adic ramification.
- For 245|N, the [corrected v2 normalized-lattice proof](ramified_higher_seven_commutant.md)
  closes the last family. Its finite-base gauge correction and independent
  effective/unit-upper witnesses are preserved explicitly.

The [unramified first-seven proof](actual_first_seven_commutant.md) remains
an independent alternative on its smaller range; its determinant checks
are not repurposed as proof of the ramified cases. At N=7, A_7=(9/10)I
and its complex joint commutant has dimension 17 by the separately reviewed
characteristic-zero argument below; no residue nullity is lifted. There is no remaining unknown odd-dimensional
family for this pair-commutant statement. Neither scalar full complex
commutant of a single U_N, seven-divisible spectral simplicity, quantitative
gaps nor BGS follows.

## Exact exceptional dimension seven

In the prescribed raw convention put zeta=exp(2 pi i/7),
G(x,y)=zeta^(-(3x²-2xy+3y²)), M_7=G/sqrt(7), and T=tr(G).
The independently reviewed integer phase-histogram identities are
T²=-7 and G³=-7 T I=T³ I. In particular T is nonzero.
Thus H=G/T satisfies H³=I and tr(H)=1. Since X³-1 is square-free,
H is diagonalizable with eigenvalues 1,omega,omega². Their multiplicities
(a,b,c) satisfy a+b+c=7 and a+b omega+c omega²=1. The rational
independence of 1 and omega gives a-c=1 and b-c=0, hence (a,b,c)=(3,2,2).
Its complex commutant is the direct sum of three full matrix algebras,
of dimension 3²+2²+2²=17. Nonzero scalar normalization preserves the
commutant. Since A_7=(9/10)I, this is also the pair commutant and,
for every real t, the commutant of U_7(t)=exp(9it/10)M_7.
No choice of Gauss-sum sign and no reduction-mod-prime lifting is used.

The [scoped independent review](../record/exceptional_seven_review.md)
and its frozen originals establish this separate characteristic-zero
consequence. The [exact replay](../computations/verification/exceptional_seven_commutant.py)
checks 49 cube entries, the trace-square identity and all 512 candidate
multiplicity triples. These bounded checks do not claim any other dimension's
spectral simplicity.

## Higher-seven theorem and boundary


For every odd N with 49|N and 5∤N, the actual prescribed pair A_N,M_N has complex common commutant C I.

This is an infinite actual-model family, not a theorem merely about an upper-bond surrogate. This higher-seven component does not cover 5|N or 7|N with 49∤N. The separate chain-trace first-seven component above now covers the latter for every N>7, including 5|N. FM-008 separately covers 7∤N. N=7 remains genuinely exceptional. The combined pair-commutant theorem above closes the odd-dimensional classification except N=7. Seven-divisible spectral simplicity, quantitative gaps, signed Heisenberg comparison and microscopic BGS are not asserted.

## 1. Actual model, coordinates, and direct reduction

Write e_N(t)=exp(2 pi i t/N), h=2^(-1) modulo N, and
r(theta)=(1-cos(14 pi theta))(1+cos(2 pi theta)). The prescribed Hermitian
matrix A has

A(x,x)=cos(14 pi x/N)+r(x/N)/10+r(x/N)sin(2 pi x/N)/100-1/10,
1000 A(x,x+1)=(-3-4i)r((x+h)/N),
1000 A(x+1,x)=(-3+4i)r((x+h)/N),

and all other off-diagonal entries vanish (indices modulo N). The raw
metaplectic kernel is
G(x,y)=e_N(-8^(-1)(3x²-2xy+3y²)); M=G/sqrt(N).
This is the modular Weyl convention of FM-001, without an ordinary-symbol
substitution. Put a=1-h modulo N and order positions x_(t,j)=a+t+jL,
0<=t<L, 0<=j<7. The seven removed bonds occur at t=L-1.
The internal upper bond between t=u-1 and u is b_(u,j)=(-3-4i)r((u+jL)/N).
With z=e_N(u+jL), the exact Laurent identity is
r=-(z^7-1)^2(z+1)^2/(4z^8).

Use the field K=F_(5^f), f=ord_N(5), with q a primitive Nth root and w=q^(N/7) primitive seventh root. Reduce i to2 at the Gaussian prime over5. Since5∤N, the order of q is exactly N. The actual integral matrix 1000A reduces to its weighted upper-bond part B: diagonal coefficients vanish, -3+4i vanishes, and -3-4i becomes4. Every internal bond is nonzero because q^(7u)≠1 for 1<=u<L=N/7 and an odd-order root cannot equal-1. The raw kernel G=sqrt(N)M remains invertible and integral.

Normalize the seven upper chains by the unit diagonal D, obtaining J=J_L tensor I_7 and simultaneously Gtilde=D^(-1)GD. A scalar common commutant over K produces a nonzero (N²−1)-minor of the actual commutator map, which lifts to characteristic zero. Thus it is enough to prove scalar common commutant of J,Gtilde over K.

## 2. Two bounded endpoint conditions force scalar C_0

A commuter with J has upper block-Toeplitz coefficients C_0,...,C_(L−1). The last row, column depths 0,...,6, consists of nonzero rank-one blocks

E_s=gamma_s u_s v_s^T,
u_s=D_(L−1)^(-1) f_(4+2s),
v_s^T=f_(s+3)^T D_s,
f_b(j)=w^(bj).

The columns u_s are independent. Up to nonzero row scalars, the right-row matrix is

V_(s,j)=w^(j(2s+3))/product_(u=1)^s(1+q^u w^j)^2.

To justify the row formula, the Laurent identity gives
D_(s,j)=c_s w^(sj)/product_(u=1)^s(1+q^u w^j)^2 with c_s nonzero and
independent of j. Direct expansion of the quadratic kernel gives
E_(r,s)(j,k)=gamma_(r,s) w^((2s+6r+4)j+(s+5r+3)k)
for row depth L-1-r. The quadratic chain-index terms vanish because 7|L;
gamma_(r,s) is a nonzero root of unity. These identities establish all
rank-one and frequency assertions used below.

The exact Casoratian certificate proves V invertible over K: its integer coefficient determinant P has degree 113 and gcd_F5(P,q^(5^84)−q)=q²+1. A root with order divisible by 49 would have degree divisible by 42=ord_49(5), impossible for those factors. Denominators are units. Indeed an irreducible factor of P having such a root must have degree
42 or 84 (degree P=113). Both divide 84, so that factor divides
q^(5^84)-q and hence q²+1, a contradiction. The portable
actual_casoratian_check.py checks the gcd and binds P to the dictionary denominator.

From the exact last-row equations

[C_0,E_s]=sum_(d=1)^s E_(s−d) C_d,

apply the s-th dual row of the u-basis. The right side vanishes, giving v_s^T C_0=lambda_s v_s^T. The s=0 equation also gives C_0u_0=lambda_0u_0. Hence in the V basis, C_0 becomes Lambda=diag(lambda_0,...,lambda_6), and h=Vu_0 is an eigenvector of Lambda for lambda_0.

Let Z=diag(w^j), R=Z^(−2), and

Q=diag((1+wq^(−1)w^j)^(−2)).

The actual last bond has form b_(L−1,j)=constant*w^(−j)(1+wq^(−1)w^j)^2. The raw penultimate-row column 0 has its left Fourier frequency shifted by−1 and its right frequency shifted by−2 relative to E_0. Therefore its simultaneously gauged block is

F_0=alpha Q u_0 v_0^T R,

with alpha≠0. This uses the actual last-bond relation and is not true for independently chosen penultimate and final gauges.

The penultimate-row column 0 equation is

[C_0,F_0]+C_1 E_0=0.

In the V basis put x=VQ u_0 and y=v_0^T R V^(-1)=f_1^T V^(-1). For every column j≠0, the C_1E_0 term vanishes. Consequently

(lambda_i−lambda_j)x_i y_j=0, for every i and j=1,...,6.  (A)

It is sufficient that

(B1) y_j≠0 for j=1,...,6;
(B2) (V Q V^(-1))_(0,0)≠0.

Indeed x≠0. Choose any i with x_i≠0. By(B1), all lambda_1,...,lambda_6 equal lambda_i. If lambda_0 were different, the relation Lambda h=lambda_0h would force h to be a nonzero multiple of e_0. Then x_0 would be the same nonzero multiple of (VQV^(-1))_(0,0), which is nonzero by (B2). Equation(A) with i=0 would contradict lambda_0 being different. Thus all seven eigenvalues agree and C_0 is scalar.

This argument never discards C_1. It uses exactly the column where that term is supported, and ignores that column when deriving(A).

## 3. Bounded polynomial certificates for (B1) and (B2)

Let z be a formal variable and define the 7-by-7 polynomial coefficient matrix C(q) by the remainders modulo z^7−1 of

p_t(z)=z^(2t) product_(u=t+1)^6(1+q^u z)^2, t=0,...,6.

Its determinant is the Casoratian polynomial P. Clearing the nonzero column factors in V and using the seven-point Fourier evaluation map shows:

- y=r(q) C(q)^(-1), where r(q) is the coefficient row modulo z^7−1 of z^5 product_(u=1)^6(1+q^u z)^2.
- The diagonal quantity in(B2) is r_Q(q,w) C(q)^(-1)e_0, where r_Q is the coefficient row modulo z^7−1 of
  product_(u=1)^6(1+q^u z)^2/(1+wq^(−1)z)^2.

All coefficient arithmetic is explicit. In the ring z^7=1,

(1+wq^(−1)z)^(-2)
 =q²[sum_(k=0)^6 (−w)^k q^(6−k)z^k]^2/(q^7+1)^2.

The denominator is nonzero at an odd-order q. Thus (B2) has numerator K(q,w) polynomial in q,w, modulo Phi_7(w), and denominator a nonzero scalar multiple of P(q)(q^7+1)^2.

For clarity let F_(k,j)=w^(kj), H_j=product_(u=1)^6(1+q^u w^j)^2,
and T=diag(w^(3j)/H_j). Then V=CFT. Hence
f_1^T T^(-1) has evaluation data (w^j)^5 H_j, proving y=r C^(-1).
Likewise f_3^T Q T^(-1) has evaluation data H_j/(1+wq^(-1)w^j)^2,
proving the K00 dictionary. The seven-term inverse formula follows by
multiplying its unsquared geometric sum by 1+wq^(-1)z; the product is
1+q^(-7). Thus no independence assumption on the actual w=q^L is hidden.

The maintained verifier actual_algebra_check.py reconstructs C and its
inverse denominator, verifies all seven identities y_num C=den r over Z[q],
checks every K coefficient identity modulo 5, and proves both saved
denominators are associates of det C. It independently constructs the
six-by-six multiplication-by-K matrix modulo Phi_7(w) and checks its
complete determinant against all 829 saved norm coefficients.

For (B1), the numerator degrees and irreducible factor degrees over F_5 are:

- j1: degree 126; factors of degrees 1,1,1,6,23,27,64, with multiplicities recorded in the certificate;
- j2: degree 134; degrees 1,1,3,4,32,85;
- j3: degree 143; degrees 1,8,134;
- j4: degree 153; degrees 1,1,3,3,60,83;
- j5: degree 164; degrees 1,8,149;
- j6: degree 176; degrees 1,1,2,2,5,6,6,6,6,6,6,6,8,73.

None is divisible by 42. The complete coefficient arrays and multiplicities are in computations/verification/actual_commutant_data/bounded_factor_certificates_fast.json; actual_factor_check.py checks them against the defining polynomials by exact multiplication and Rabin identities.

For (B2), take the norm/resultant

N(q)=Res_w(K(q,w),Phi_7(w)) over F_5.

It has degree 828. Its irreducible factor degrees, with multiplicities, are

1^24, 6^6, 36, 54, 66, 246, 366.

Again no factor degree is divisible by 42. Thus N(q) cannot vanish at a root whose multiplicative order is divisible by 49. Therefore K(q,w) is nonzero for every primitive seventh root w paired with such q. This proves(B2), including the actual w=q^L.

**Why the finite certificates imply the uniform claim.** If a nonzero alpha over F_5 has multiplicative order divisible by 49, its field degree d satisfies49|5^d−1, hence42|d. Its minimal polynomial must be an irreducible factor of any polynomial vanishing at alpha. The certified factor lists have no such degree, so no such alpha is a zero. This excludes arbitrarily large N uniformly; it is not extrapolation from tested dimensions.

**Irreducibility verification.** actual_factor_check.py independently checks every factor list by multiplication and checks each monic degree-d factor by the exact Rabin identities: q^(5^d)=q modulo the factor, and gcd(f,q^(5^(d/p))−q)=1 for every prime p|d. The first says each irreducible constituent has degree dividing d; the gcd conditions exclude every proper divisor, forcing irreducibility. Exponents are evaluated by repeated fifth powers modulo f. Every maintained check raises an explicit RuntimeError on failure; correctness checks remain active under python -O. Source-data SHA-256 identities are checked before calculation; imports are silent and inert.

## 4. Higher tails and the finite base

For completeness, the entire block commutation equation is
sum_(e=0)^(L-1-r) C_e Gtilde_(r+e,s)=sum_(e=0)^s Gtilde_(r,s-e) C_e.
The commutant of the upper block shift J consists exactly of these upper
block-Toeplitz matrices: comparing XJ and JX makes each upper block
diagonal constant and each lower block zero.

For L>=21, scalar C_0 forces every higher C_d to vanish by the following minimal-tail argument. Subtract the scalar matrix first. For the smallest d with C_d nonzero:

- If d<=L−7, use last-row column s=d+t for 0<=t<=6. All coefficients below d are zero. The remaining outputs have column factors u_t,u_(t−1),...,u_0; apply the dual row selecting u_t. It leaves v_t^T C_d=0. The Casoratian independence of these seven rows forces C_d=0.
- If d>=7, use r=L−d,...,L−1 and s=d. Every left coefficient has index at most L−1−r<d and vanishes; only Gtilde_(r,0)C_d remains on the right. Each block is nonzero rank one. Its right Fourier frequency increments by 4^(-1)=2 modulo 7 when r increments by one. D_0=I, and the left gauges are invertible, so any seven consecutive right rows are independent and force C_d=0.

Every positive d falls in one of these cases. The independence assertions hold over K by the Casoratian-unit proof and the nonzero seven-point Fourier determinant.

For N=49, L7 is separately verified in the actual residue field F5[q]/Phi49. actual_field_check.py constructs the reduced B,G directly, and for T=B+G obtains cyclic rank 49 and rank 48 of [0,[T,B]e_0,...,[T^48,B]e_0]. Here Phi49 has degree 42 and is irreducible over F_5 because ord49(5)=42.
All field products use exact integer coefficients with polynomial reduction.
The cyclic rank 49 means e_0,T e_0,...,T^48 e_0 is a basis. Any X commuting
with T is uniquely p(T), degree p<=48: choose p with p(T)e_0=Xe_0 and
commute through this basis. The additional equation [X,B]e_0=0 has rank 48
in these 49 coefficients; its constant column is zero, so only constants
survive. Thus any common commuter of B and G is scalar. This proves the
finite actual-residue base; it does not borrow a characteristic-zero
surrogate certificate. Its field arithmetic and primitive-root order are exact. This finite base handles the short-chain tail exception without an unproved extension of the long-chain dichotomy.

It follows that the residue common commutant is scalar for every N in the theorem. For the integral map X -> ([X,1000A],[X,G]), the scalar identity is in
the kernel. Its reduction has rank N²−1, so at least one (N²−1)-minor
reduces to a nonzero field element. That same minor is nonzero in the
cyclotomic characteristic-zero field and over C. Rank is therefore exactly
N²−1 over C, proving the theorem. Division of A and G by their nonzero
scalars does not affect common commutants.

## 5. Unresolved branches and review status

The proof relies on direct reduction at 5 with all internal bonds units and the Fourier kernel retaining rank. It does not apply when 5|N. Its rank-one endpoint formula does not apply when 7|N but 49∤N; that branch is now covered by the separate chain-trace proof for every N>7. The endpoint-free unramified proof remains an alternative when 5∤N. The separate corrected normalized-lattice proof now covers odd multiples of 245; this higher-seven component retains its own unramified hypotheses.

The accepted source was independently reviewed at SHA-256
47b2692f034a23888d4223e73120a685609a6ca58c2a983293310bc735e42d4f.
Its locator-only promotion revision is
cc90a3e0fc2354692e93aac2f8f5948d5d62fec58b563ae96292f418a182b725.
The preserved review and manifest state exactly which finite certificates
completed. The slower development log is not a proof dependency.

## 6. Algebraic-entry commuters of the literal propagator

Corollary (additional external input EXT-POPESCU-2023, Theorem 3.2).
For every odd N>=3 with N≠7, and every nonzero algebraic real t, the only
matrices X with algebraic entries commuting with exp(itA)M are scalar
matrices with algebraic scalar. In particular this holds for t=10^(-80)N
and the literal prescribed U_N.

Proof. Let a_1,...,a_m be the distinct spectral values of the Hermitian
algebraic matrix A. They are real algebraic numbers; no assertion that m=N
is made. Its spectral projectors
P_j=product_(k!=j)(A-a_k I)/(a_j-a_k) have algebraic entries, sum to I,
and A=sum a_j P_j. If X has algebraic entries, then

0=[X,exp(itA)M]=sum_j exp(it a_j)(X P_j M-P_j M X).

The exponents it a_j are distinct algebraic numbers. The cited
Lindemann–Weierstrass linear-independence theorem over the algebraic
numbers, applied entry by entry, forces X P_j M=P_j M X for every j.
Summing gives XM=MX. Right multiplication by M^(-1), using this equality,
then gives XP_j=P_jX, hence XA=AX. The main theorem makes X scalar.
The converse is immediate.

This is only an algebraic-entry restriction. It neither makes the full
complex commutant of U scalar nor proves its spectral simplicity. The
latter does not follow from common irreducibility of A and M.
