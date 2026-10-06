# Actual scalar commutant at the first unramified seven-primary level

Supporting extension of BGS-FM-024, accepted after fresh independent internal
review on 6 October 2026. Exact computation is load-bearing; this is not Lean
formalization or external peer review. Original base/status records and hashes
are retained in the source map. The previously accepted higher-seven-primary
proof is unchanged. This is the maintained first-seven component of the integrated FM-024 theorem.

## Theorem and resulting remaining branch

For every odd N with 7|N,49∤N,5∤N and N>7, the actual pair (A_N,M_N) has complex common commutant C I.

Together with the separately reviewed 49|N,5∤N theorem and existing FM-008 for 7∤N, this establishes scalar common commutant at every odd N>=3 with 35∤N, except the genuine exception N=7. The separate [chain-trace theorem](ramified_first_seven_commutant.md) now covers the ramified first-seven branch. Together with the higher-seven component, the remaining uniform family is odd multiples of 245. No seven-divisible spectral-simplicity, quantitative gap, Heisenberg comparison or BGS theorem follows.

## 1. Actual reduction and four small boundary blocks

Put L=N/7, so L>=3 and 7∤L. Reduce the actual 1000A at the Gaussian prime i=2 modulo 5, in a field containing a primitive Nth root q. Because5∤N, q retains order N. Its diagonal and lower entries vanish, and every internal upper bond remains a unit. The actual entry dictionary is recorded in [the maintained higher-seven-primary proof](actual_seven_primary_commutant.md), Section 1, and is reconstructed in the independent review. Normalize the seven upper chains by D to J_L tensor I_7, while simultaneously replacing G=sqrt(N)M by D^(-1)GD.

Let a=1−2^(-1) modulo N, w=q^L, and z_j=w^j. Define the raw 7-by-7 blocks

A(j,k)=G(a+L−1+jL,a+kL),
B(j,k)=G(a+L−1+jL,a+1+kL),
C(j,k)=G(a+L−2+jL,a+kL),
D_raw(j,k)=G(a+L−2+jL,a+1+kL).

Let R=D_(L−1)^(-1), D1=diag(b_(1,j)^(-1)), and Dl=diag(b_(L−1,j)^(-1)), using the actual reduced internal bonds. The gauged blocks are

E0=RA, E1=RBD1, F0=R Dl C, F1=R Dl D_raw D1.

A is invertible. After nonzero diagonal factors it is the seven-point Fourier matrix with mixed coefficient2L modulo 7. A common commuter with J has upper block-Toeplitz coefficients C0,C1,..., and the four displayed blocks impose

[C0,E0]=0,
[C0,E1]=E0C1,
[C0,F0]=−C1E0,
[C0,F1]=F0C1−C1E1.                                      (1)

All conventions, including the raw modular midpoint, are unchanged.

## 2. Central cross-ratio and removal of the long endpoint product

Direct expansion of the quadratic kernel gives

D_raw=theta C A^(-1)B,
F1=theta F0 E0^(-1)E1,

theta=q^(−4^(-1) mod N) / w^(−2L^(-1) mod7).

Here theta≠1: raising equality of numerator and denominator to the fourth power would force q to have order dividing7, contrary to N>7.

Define two matrices independent of the long endpoint factor R:

J=A^(-1) Dl C=E0^(-1)F0,
K=A^(-1) B D1=E0^(-1)E1.

Equations(1) imply

C1=[C0,K],
[C0,J]=−E0^(-1)C1E0.

Using the cross-ratio in the last equation of(1) gives F0C1=C1E1 because theta−1≠0. Consequently

[C0,JK]=E0^(-1)(F0C1−C1E1)=0.                         (2)

The first equation of(1) gives R^(-1)C0R=A C0A^(-1). A diagonal conjugation preserves diagonal entries, hence

diag(C0−A C0A^(-1))=0.                                (3)

Similarly,

A[C0,J]A^(-1)=−R^(-1)C1R.

Taking diagonal entries and substituting C1=[C0,K] yields

diag([C0,K]+A[C0,J]A^(-1))=0.                          (4)

Thus the actual C0 obeys the bounded linear system(2)–(4), which contains **no endpoint-product variables**. Only the first and last actual bond factors remain. No assumption that the boundary matrices scalar-q-commute has been made; that proposed shortcut is not used by this proof.

## 3. Polynomial normalization of the bounded system

Put l=L modulo 7, so l=1,...,6, and Z=diag(w^j), U=Z². Up to one nonzero scalar the raw A is the constant matrix

A_l(j,k)=w^[−3l(j²+k²)+2l jk+(l+4)j+(2l+3)k].           (5)

The actual bond identity r(z)=−(z^7−1)²(z+1)²/(4z^8), together with the raw kernel ratios, gives a common nonzero scalar lambda such that

J=lambda Jbar_l(q), K=lambda w² Kbar_l(q),              (6)

where Jbar,Kbar are the following polynomial matrices of degree at most12. For z_j=w^j define

S_c(q,z)=sum_(k=0)^6 (−wz)^k q^(6−k),
S_q(q,z)=sum_(k=0)^6 (−qz)^k,

Jbar=A_l^(-1) diag(S_c(q,z_j)²) A_l U^(-1),
Kbar=A_l^(-1) U A_l U diag(S_q(q,z_j)²).                 (7)

To check the scalars, before clearing denominators write

J=nu A_l^(-1)(1+wq^(-1)Z)^(-2) A_l U^(-1),
K=nu w²q² A_l^(-1) U A_l U(1+qZ)^(-2).

The two geometric-series inverse identities have the common denominator (1+q^7)². They produce (6) with lambda=nu q²/(1+q^7)². All discarded scalars are nonzero: q≠0, q^7≠1 because N>7, and q^7≠−1 because q has odd order. The individual first/last bonds are units in this unramified case.

Consequently the bounded constraints become

[C0,Jbar Kbar]=0,
diag(C0−A_l C0 A_l^(-1))=0,
diag(w²[C0,Kbar]+A_l[C0,Jbar]A_l^(-1))=0.              (8)

This is 63 homogeneous scalar equations on 49 entries. Every scalar matrix is a solution. Subtract C0(0,0)I and omit the coordinate(0,0); full rank of the resulting63-by-48 matrix implies C0 scalar. Denote this polynomial matrix by M_l(q).

Its row degrees are bounded by0 for the seven equations in(3),12 for the seven last equations in(8), and 24 for the 49 commutator equations. The explicit matrices are reconstructed directly by the independent C++ verifier from the displayed dictionary. The normalization was also checked directly against the actual raw blocks in all six residue classes; those finite checks corroborate the displayed algebra, rather than proving its universal scope.

## 4. Exact uniform polynomial certificate

Work over the fixed field F=F5^6, represented as

F5[t]/(t^6+t^4+3t^3+t²+1).

The modulus is irreducible and divides Phi63. The class t has order63, and w=t^9 has order7. The independent C++ replay validates the full logarithm/multiplication table with primitive generator t+4. Field elements in the records are base-five coefficient codes, not ordinary integers modulo 15625.

For each l=1,...,6, three 48-row minors of M_l(q) were selected. Each uses six degree 0 rows, six degree 12 rows and 36 degree 24 rows, so every determinant has degree at most

6*0+6*12+36*24=936.

Each determinant was evaluated at 937 distinct field elements and interpolated exactly. Agreement at 937 points, together with the degree bound, determines the determinant polynomial identically, including over every extension of F. Ten additional evaluations per minor agreed. These are evaluations of a bounded polynomial, **not samples of dimensions N**.

The resulting degrees are:

l1: minor degrees915,918,918; gcd degree 846.
l2: minor degrees918,919,917; gcd degree 844.
l3: minor degrees914,917,917; gcd degree 848.
l4: minor degrees906,918,914; gcd degree 844.
l5: minor degrees916,916,918; gcd degree 846.
l6: minor degrees918,915,916; gcd degree 840.

In every class, after factors supported at q=0 and q^7=−1 are removed, the gcd has degree 40. Its remaining two coprime components have degrees6 and 34. The exact certificate establishes

B_6 divides q^(5^18)−q,
B_34 divides q^(5^102)−q,

gcd(B_6,q^((5^18−1)/8)−1)=1,
gcd(B_34,q^((5^102−1)/8)−1)=1.                         (9)

For18 and 102, the exact two-adic valuation of5^m−1 is 3. Hence the exponents divided by8 in(9) are the full odd parts of the respective multiplicative group orders. Any odd-order root of B_6 or B_34 would violate the corresponding gcd identity. Thus neither component has an odd-order root.

It follows that the three determinant minors have no common nonzero odd-order root. Therefore M_l(q) has rank48 at **every** nonzero odd-order q in the algebraic closure of F5. This is stronger than needed for the actual primitive Nth roots.

All primitive seventh roots are covered. They are Frobenius conjugates of the chosen w over F5. Applying a Frobenius automorphism to the matrix coefficients and to q preserves matrix rank and preserves odd root order, so the fixed-w certificate transfers to every actual w=q^L.

### Portable certificate and exact replay

The maintained entry point is `computations/verification/first_seven_commutant.py`.
It compiles and runs the independent standard-library C++ replay against one
pinned, compact serialized certificate. The underlying inputs include all 18
minor row sets, 937-node values and polynomial coefficients, the gcd/Bezout
and quotient identities, excluded factors, and the degree-6/34 odd-root
certificates. No large duplicate development JSON datasets are required.

Every one of the 17,046 determinant evaluations is rebuilt independently;
16,866 establish identities using the degree bound and distinct nodes. The
remaining 180 evaluations are additional controls. It also verifies the full
field generator orbit, 156,250 direct field products, six raw-model dictionary
controls, and actual residue commutants at N=7,21,63. The latter are controls,
not the universal theorem.

The original input and review manifests are retained. The promotion mapping
binds their serialized input byte-for-byte to the independent review. Portable
Python imports are silent; explicit failures remain active with normal and
optimized Python and with C++ NDEBUG. Original assertion-dependent scripts
are historical provenance only.

## 5. Return to the actual commutant

By the uniform rank result, C0 is scalar. Equations(1) then give C1=0. Every remaining last-row equation has the form

0=E0 Cd + terms involving earlier C_e.

Induction and invertibility of E0 force every Cd=0. Thus the characteristic-five common commutant of the reduced pair is scalar. A nonzero full commutator-rank minor lifts through the unramified cyclotomic reduction to characteristic zero, proving the theorem for the actual A_N,M_N.

There is no additional L>=21 restriction: L>=3 is sufficient for the four small blocks, and the tail argument here uses invertible E0. N=7 is excluded both because its generator is scalar and because the first/last-bond normalization is unavailable.

## 6. Scope still open

At5|N the primitive root order drops, some internal bonds cease to be units, and the direct Jordan normalization used here cannot simply be reduced. This direct-reduction certificate does not remove that obstacle. The separate [chain-trace theorem](ramified_first_seven_commutant.md) covers 7∥N with arbitrary v5(N); odd multiples of 245 remain outside the combined results. This exact symmetry result supplies no quantitative spectral separation or microscopic universality.
