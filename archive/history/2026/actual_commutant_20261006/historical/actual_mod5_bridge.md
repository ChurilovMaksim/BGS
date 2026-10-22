# Actual-model characteristic-five bridge and exact remaining system

Same BGS base d4132ccee82849b644520d88c953cb9b33382a59. This file is a further extension; the two earlier proof files remain frozen. It isolates the actual, not merely truncated, implication. The universal rank-six assertion below is **open**.

## Scope and residue field

Assume N is odd, 49 divides N, and 5 does not divide N. Put L=N/7, f=ord_N(5), and take K=F_(5^f) with a primitive Nth root q. Then w=q^L has exact order7. Work at the Gaussian prime over5 with i mapping to2. This defines a reduction of Z[i,zeta_N,1/2] into K; the cyclotomic root retains exact order N because N is prime to5.

Let A be the actual generator and G=sqrt(N)M the actual scalar-normalized metaplectic matrix. The entries of 1000A are integral at this prime. Its diagonal terms have factors1000,100,10 or100, hence vanish. Its lower bonds have coefficient -3+4i mapping to0; its upper bonds have coefficient -3-4i mapping to4. Therefore

reduction(1000A)=B, with B_(x,x+1)=4 r((x+h)/N),

and all other entries zero. Every internal bond is nonzero: writing its coordinate as q^u w^j with 1<=u<L, q^(7u) is not1 and q^u w^j is not -1 (the latter has odd order). Thus B consists of the same seven nonzero weighted nilpotent chains. G remains the exact quadratic kernel over K. It is invertible, since its Fourier determinant has nonzero squared norm proportional to a power of N, and N is nonzero in K.

Normalize the internal bonds by the diagonal D with D_0=I and D_(t+1,j)=D_(t,j)/b_(t+1,j). All entries of D and D^(-1) are units in this unramified setting. Then D^(-1)BD=J_L tensor I_7, and G must simultaneously become D^(-1)GD.

**Actual lifting implication.** If the common commutator map of (B,G) has kernel dimension1 over K, a nonzero (N²−1)-minor lifts to characteristic zero. Hence the actual pair (1000A,G), equivalently (A,M), has scalar complex common commutant. This uses rank semicontinuity via one nonzero minor, not lifting a selected idempotent. No extra sigma-dependent filtration is required in this coprime-to5 case.

## The exact leading compatibility system

For a block-Toeplitz commuter with J, use the matrices C_0,...,C_(L-1). The last row and the first seven columns give

[C_0,Etilde_s]=sum_(d=1)^s Etilde_(s-d) C_d, 0<=s<=6,

where Etilde_s is a nonzero scalar multiple of u_s v_s^T,

u_s=D_(L-1)^(-1) f_(4+2s),
v_s^T=f_(s+3)^T D_s,
f_b(j)=w^(bj).

The independent review proved that these seven v_s form an invertible matrix over K. Its exact certificate is in bgs_seven_adic_independent_review/additional.py: for the integer Casoratian polynomial P of degree113,

gcd_(F5[q])(P,q^(5^84)-q)=q²+1, and ord_49(5)=42.

Consequently no root of P in characteristic5 has multiplicative order divisible by49. All other normalized Casoratian denominators are units.

Let U have columns u_0,...,u_6, V have rows v_0^T,...,v_6^T, and H=VU. The same support argument as in characteristic zero shows that any leading C_0 from the boundary system obeys

VC_0=diag(lambda_0,...,lambda_6)V,
U^(-1)C_0U is upper triangular.

Thus it suffices to prove that the following 21-by-7 matrix over K has rank6:

T_((r,s),t)=(H^(-1))_(r,t) H_(t,s), 0<=s<r<=6, 0<=t<=6.

The all-ones vector always lies in its kernel, since H^(-1)H=I. Rank6 forces every lambda_t equal and hence C_0 scalar. This is a concrete finite-size compatibility test with no suppressed higher C_d terms.

To express H without gauge denominators, row scalars may be removed: left multiplication H -> R H by an invertible diagonal R leaves H^(-1)diag(lambda)H unchanged. The resulting entries are

H_(t,s)=sum_(j=0)^6 w^(j(2t+2s+1)) product_(u=t+1)^(L-1)(1+q^u w^j)^2.

Here L=0 modulo7 has been used. Equivalently H_(t,s) is7 times the sum of coefficients at powers divisible by7 in

z^(2t+2s+1) product_(u=t+1)^(L-1)(1+q^u z)^2,

with coefficients reduced in K. This formula retains the actual long endpoint product; it cannot be replaced by an arbitrary endpoint diagonal gauge.

**Uniform residue implication.** At every L>=21, rank(T)=6 implies scalar C_0, and the now-unit Casoratian plus the minimal-tail proof kills all higher C_d over K. Therefore the rank-six assertion implies the actual scalar commutant for this N. The unproved family is precisely rank(T)=6 for every odd49|N, 5∤N, N>=147. Archimedean positivity does not establish this rank in K.

## Smallest exceptional residue base

At N49, the three first-column overlaps at t=4,5,6 vanish even in characteristic zero, so their vanishing cannot be ignored in a residue proof. Two independent-purpose exact checks distinguish this base:

1. residue_boundary_49.py works in K=F5[q]/Phi49(q). Phi49 is irreducible of degree42. It constructs the displayed H, computes H^(-1), and finds rank(T)=6. Thus the last-row leading compatibility does hold despite the three zero overlaps.
2. actual_residue_base49.py works in the same field and constructs the actual reduced upper generator B and raw G directly in position order. With C=B+G and e=e_0, the Krylov matrix [e,Ce,...,C^48e] has rank49, and [0,[C,B]e,...,[C^48,B]e] has rank48. The cyclic-commutant lemma therefore certifies scalar common commutant of the residue pair itself. This also kills all tails at L7, where the long-chain dichotomy does not apply.

The second certificate uses exact polynomial arithmetic, reducing products first by q^49=1 and then by Phi49=1+q^7+...+q^42. Integer convolution coefficients before reduction are bounded by42*16=672. Field inversions and irreducibility are checked with exact polynomial arithmetic. This is a route-specific finite base in the actual residue characteristic, rather than another split-prime certificate of the previously known N49 conclusion.

For additional discrimination, residue_overlap_discriminator.py computes the first-column root-filter polynomials modulo5. At N147 and343 every overlap has gcd1 with Phi_N modulo5; at N49 it reproduces the three exact zeros. These checks support neither a universal nonvanishing theorem nor a universal rank-six claim. The safer rank-six system can succeed even when some overlaps vanish.

## Separate ramified and remaining families

If 5 divides N, q reduces to order N/5^(v5(N)), internal bonds can acquire positive valuation, and the unscaled Fourier matrix may lose rank. The direct unramified reduction argument does not cover this case. A valuation-sensitive lattice/filtration argument is still required there.

If 7 divides N but49 does not, the raw endpoint blocks are full rank rather than the rank-one blocks used in this reduction. This note does not silently extend its boundary system to that family. FM-008 covers 7 not dividing N; it does not fill either of these remaining families.

The all-odd-N actual common-commutant theorem is open. The new explicit rank-six residue family is the first unresolved implication for the unramified higher-seven-primary branch. It is a subsidiary algebraic problem; neither its solution nor the characteristic-zero upper-truncation theorem would prove BGS.
