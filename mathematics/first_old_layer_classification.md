# Exact classification of even first-old-layer two-mode blocks

Claim family: BGS-FM-026. Source-bound [independent review](../archive/record/first_old_layer_review.md).
The frozen original SHA256 is `3711869ecb05efda76066216ce29b84263ec12edca9c379e2ede9d16c5f21b41`;
its exact bytes, original status and execution records remain in the
[provenance map](../evidence/intermediate_old_layers_20261007/input_map.json).
Inherited [oldform](oldform_tower_compression.md),
[newest-sector](even_new_sector_first_jet.md), and
[rank-transfer](algebraic_time_rank_transfer.md) proofs retain their own scopes.
The [literal-time theorem owner](literal_time_multiplicity_bounds.md) is the
only maintained owner of the resulting fixed-time simple-eigenvalue counts.

The portable maintained command is
`python3 computations/verification/intermediate_old_layers_certificates.py`
(or the same command with `python3 -O`). Original bare script names below
identify archived historical implementations; the portable entry replays the
independent reviewers' algorithms in scratch storage and verifies their
outputs against the frozen reviewed results.

Status: independently reviewed project proof, accepted within the inherited cat/oldform inputs.
The fixed finite-field discriminator has been rebuilt without importing the
author's field, matrix, coefficient, polynomial, or diagnostic code. The exact
cyclotomic cancellation computation is also new and import-independent.

## Claim and dependency boundary

Let N=7*5^(2l+2), l>=1, h=5^l, m=h², L=6*5^(l-1). Work on the
first-old-layer quotient W1 orthogonal to W2. The accepted oldform theorem
identifies this with H7 tensor the primitive coherent sector of H_m; these
are COMPLETE product-cat eigenspaces, all of dimension seven. Its compressed
actual generator is exactly

    Aold = (1/800)[-i T7(0,5) tensor Tm(0,1)
                        +i T7(0,-5) tensor Tm(0,-1)].

The prime-power root q is the actual induced primitive m-th root. The
seven-factor root is likewise the actual induced seventh root. No coefficient
or phase is discarded. H7 below denotes the normalized seven-dimensional cat
G7/Tr(G7), with eigenvalues z=1,omega,omega² and multiplicities 3,2,2.

Dependencies: the accepted complete-eigenspace isolation and exact two-mode
compression in oldform_tower_compression.md; the accepted cat simplicity,
coherent norm-circle model, and common-denominator argument used in
even_new_sector_first_jet.md. This note rederives the relevant Weyl cocycles
and the new singular-block conclusion. It does not infer simplicity of U,
prove literal-coupling noncollision, or establish any BGS conclusion.

## Main classification

Each primitive norm circle

    O_c={(a,b) mod h: 2b²-a²=c}, c a unit modulo h,

has L points and supplies L complete seven-dimensional product-cat blocks.
Put D=1/2-c modulo h. Then:

1. If c=1 modulo 5, every block on O_c is EXACTLY ZERO.
2. If c=2 or 4 modulo 5, every block on O_c is SIMPLE, with rank six and
   eigenvalue zero of multiplicity one. This is uniform in l and all wild
   character labels; the certificate retains all six tame labels.
   The c=2,4 classes account for exactly 12*5^(2l-2) simple size-seven
   blocks, exactly half of the first-old quotient dimension.
3. If c=3 modulo 5 and l=1, all six blocks are simple of rank six.
4. If c=3 modulo 5 at any depth, every block is either exactly zero or
   simple of rank six. There are no intermediate positive ranks and no
   nonzero repeated slopes. A completely explicit cyclotomic coefficient
   test below decides which alternative for every (l,c,character label).

In particular, singular zero residue is not identified with zero in
characteristic zero. The uniform theorem here is the exact scalar reduction
and zero criterion. A simpler closed digit rule at arbitrary l is not claimed.

## 1. Exact intersections and the dependence on higher digits

For u=(0,1), simultaneous membership of y=(a,b) and y+u in O_c is equivalent to

    b=-1/2 modulo h,       a²=D=1/2-c modulo h.                     (1)

For -u, b=+1/2 and the same a equation applies. Consequently an empty square
root set makes both prime-power matrix elements identically zero, before any
residue reduction. For c=1, D=2 modulo 5 is a nonsquare. For c=2,4, D=1,4
modulo 5 respectively and exactly two roots lift uniquely at every depth.

For singular c=3, choose D in [0,h). If D is nonzero and v=v5(D)<l,
roots exist precisely when v=2s is even and D/5^(2s) is a nonzero square
modulo 5. There are then 2*5^s roots. If D=0, there are
5^floor(l/2) roots, precisely a divisible by 5^ceil(l/2). These are exact
5-adic square-root facts, not residue heuristics.

There are h/5 singular norm classes. Exactly

    1 + 2 sum_{s=1}^{floor((l-1)/2)} 5^(l-2s-1)

have nonempty intersections (with an empty sum interpreted as zero).
The others have every seven-dimensional block exactly zero.
Nonempty intersections alone do NOT imply a nonzero compression.

## 2. The common denominator and independent 48-matrix certificate

With the unit coherent state psi supported on hZ/mZ, put phi_v=T_m(v)psi.
On O_c the cat is a monomial L-cycle with phases of 5-power order. Every
normalized eigenvector has coefficients of modulus L^(-1/2). Multiplying
each matrix element by L therefore gives a sum of algebraic integers.
Thus 800L, not a projector-denominator shortcut, is the common scalar used
in the residue certificate.

Choose i -> 2 at a prime over 5 and let xi be a primitive sixth root. For a
full product eigenvalue whose normalized residue is xi^t, the associated
prime-power eigenvalue in the z_i seven-cat sector has residue

    gamma_i=xi^t/z_i,       t=0,1,2,3,4,5.

On the six-point circle modulo 5, each directed intersection y->x=y+u
contributes gamma_i^(k_x) gamma_j^(-k_y). Its seven-factor matrix is
V7^(-1)T7(0,5)V7 for u=(0,1), and V7^(-1)T7(0,-5)V7 for u=(0,-1).
The actual coefficients are -i and +i. They remain separate. At c=2,4
the two intersections lift and their residues are unchanged. At singular
c=3 and l>=2, any nonempty root set has size divisible by 5 and every
root has the same orbit indices modulo 6, so its residue is zero.
At l=1 its single intersection is retained.

independent_residue.py uses F5[w]/(1+w+...+w^6), where w=5 in base-5
coefficient encoding. This polynomial is irreducible because the order of
5 modulo 7 is six. It uses xi=1314 and omega=1313. Characteristic
polynomials are computed by subset expansion of det(XI-C), rather than
interpolation, Faddeev division, or imported author code. Gaussian
elimination independently computes each matrix rank. All 48 records,
including the six tame labels, are in independent_residue.json.

For c=2,4, in either depth regime, the polynomials are

    t=0,3: X^7 + 13351 X^5 + 11700 X^3 + 14103 X;
    t=1,4: X^7 + 14103 X^5 +  3004 X^3 +  7054 X;
    t=2,5: X^7 +  7804 X^5 + 14854 X^3 +     4 X.

All three are squarefree. The l=1,c=3 polynomial for every t is

    X^7 + 3X^5 + 4X^3 + 3X,

also squarefree. The other 18 residue matrices are zero, with polynomial
X^7. The finite assertion is 30 squarefree/rank-six matrices and 18 zero
matrices. It is the root-lifting argument above that makes the residue
list uniform in l; finite checks alone do not do so. All primitive choices
of the seventh root are covered because Frobenius acts transitively on
them. A local lift of the seven-factor eigenbasis can be chosen with unit
determinant since its three eigenvalues remain distinct modulo 5.
Squarefree residue therefore proves nonzero characteristic-zero
discriminant of the actual scaled compression.

For the rank assertion, simultaneous parity P7 tensor Pm commutes with
the product cat and anticommutes with the two-mode generator. It preserves
the complete block, so its spectrum is symmetric about zero. Simplicity
in odd dimension seven consequently gives precisely one zero eigenvalue.

## 3. Singular blocks are scalar copies of a fixed seven-point sine matrix

Let e_i denote the prime-power cat eigenvector paired with the seven-cat
sector z_i. Its eigenvalue is lambda_i=lambda/z_i for one full block.
For singular c=3 all intersections in (1) reduce to the same y mod 5,
and x=y+u=-y mod 5. Hence their orbit indices satisfy

    k_y=r modulo 3,       k_x=r modulo 3

for one r, independent of the square root a. Factoring the cubic
characters out of the exact matrix-element sum, not just its residue,
gives

    L <e_i,Tm(0,1)e_j> = z_i^(-r) z_j^r G(lambda),                 (2)

where G is a scalar root-of-unity sum retaining the complete 5-power
phases and the full, possibly wildly ramified, lambda.

The prime-power eigenvectors in this block have the same parity. Indeed,
S modulo m has order R=6*5^(2l-1) and S^(R/2)=-I. Exact covariance and
irreducibility of the Weyl representation imply M_m^(R/2)=kappa Pm.
Since 3 divides R/2, replacing lambda by lambda/z_i leaves its
R/2-th power unchanged. Thus Pm has the same sign on every e_i.
As Pm T(u) Pm=T(-u), the matrices of T(u) and T(-u) between these
three eigenspaces are equal. Their being adjoints shows G is real.

Let D7 be the diagonal matrix with entries z_i^r, repeated with the
actual 3,2,2 multiplicities. If B7(+)=V7^(-1)T7(0,5)V7 and B7(-)
is its inverse, the full compression is exactly

    C=(G/(800L)) D7^(-1) [-i B7(+)+i B7(-)] D7.                 (3)

The bracket is similar to the position-diagonal matrix with seven
entries 2 sin(2 pi k*5/7), with k permuted by the actual seventh-root
choice. They are all distinct: equality of two such sine values would
force either equal angles modulo 2pi or their sum to be pi modulo 2pi;
the latter cannot occur with denominator seven. Only k=0 is zero.
Thus G=0 gives the zero block, while G!=0 gives simple rank six.
This proves the uniform dichotomy without any conjectural Gauss-sum
nonvanishing statement.

## 4. An explicit all-depth exact zero test, including wild characters

The following integer recipe is a necessary and sufficient test, not a
finite-field proxy. It also specifies every phase in (2).
For canonical v=(a,b) with 0<=a,b<h, a lift v+h(r,s) obeys

    phi_(v+h(r,s)) = q^[h(br-as)/2] phi_v.                     (4)

All exponents are modulo m; 1/2 is the modular inverse. This follows by
evaluating both coherent functions at x=-a, using
T(a,b)f(x)=q^[b(x+a/2)] f(x+a). The exact Weyl product is
T(u)T(v)=q^[(u_a v_b-v_a u_b)/2]T(u+v).

Choose v0 in O_c and enumerate v_k=S^k v0 modulo h. Write
S v_k=v_(k+1)+h(r_k,s_k) and put

    e_k=h[(v_(k+1))_b r_k-(v_(k+1))_a s_k]/2 modulo m,
    E_0=0, E_k=sum_(a<k) e_a modulo m.

Then M phi_(v_k)=q^(e_k)phi_(v_(k+1)) and every eigenvector has
coefficients L^(-1/2) lambda^(-k)q^(E_k), with lambda^L=q^(E_L).
E_L is divisible by h. Let zeta be primitive of order 6m with
q=zeta^6 and set

    alpha_j=5 E_L/h + 5h j modulo 6m,
    lambda_j=zeta^(alpha_j),             0<=j<L.             (5)

These are all L eigenvalues in the circle and all L normalized full
product labels. No wild label is omitted.

For each root a²=D, let y=(a,-1/2), x=y+(0,1), and let k_y,k_x
be their canonical orbit indices. If y+u=x+h(r,s), its Weyl carry is
h(x_b r-x_a s)/2. Define

    f_a=-a/2 + h(x_b r-x_a s)/2 + E_(k_y)-E_(k_x) modulo m,
    d_a=k_x-k_y.

Then the exact scalar numerator is

    G_j=sum_(a²=D) zeta^[6f_a+alpha_j d_a].                   (6)

Every d_a has the same residue modulo 6. Fix one term with exponent
b0, subtract it from all exponents modulo 6m and divide by six. This
writes G_j=zeta^(b0) sum q^e. Let n_r be the multiplicity of exponent
r modulo m in that latter sum. Since

    Phi_m(X)=1+X^(m/5)+X^(2m/5)+X^(3m/5)+X^(4m/5),

we have the exact equivalence

    G_j=0 iff for every 0<=r<m/5 the five numbers
    n_r,n_(r+m/5),n_(r+2m/5),n_(r+3m/5),n_(r+4m/5)
    are equal.                                             (7)

This is an explicit finite-integer classification for every l,c,j.
It involves only modular matrix orbits, modular square roots, integer
multiplicities and a cyclotomic identity. It is stronger than leaving
an unevaluated 'possibly zero Gauss sum' as a premise. We do not claim
a shorter closed digit formula for arbitrary l.

The zero-test period in j can also be reduced exactly. Fix d0 and put
b_a=5h(d_a-d0)/6, an integer. The test depends only on

    j modulo lcm_a [m/gcd(m,b_a)],

a power of five dividing L. The implementation uses this proved period
at larger depths; it does not sample or extrapolate omitted labels.

## 5. First failed blocks, and the first higher-digit cancellation

At l=1, N=4375, the first-old quotient has 24 size-seven blocks.
The six blocks on c=1 are zero, rank zero, zero multiplicity seven;
the other 18 are simple rank six. The separate deeper old core W2
has the inherited sizes 3,2,2 and zero first-order compression.

At l=2, h=25, N=109375, the singular classes are c=3,8,13,18,23.
Only c=13 has intersections, with a=0,5,10,15,20. Take v0=(0,12).
Then E_L=450, and lambda_j=zeta^(90+125j) for 0<=j<30.
The pairs (f_a,d_a), in increasing a order, are exactly

    (400,15), (10,-9), (45,-3), (580,3), (615,9).

Put beta=q^125, a primitive fifth root. Formula (6) gives

    j=0:  3+beta+beta^4;
    j=1: -(3+beta²+beta³);
    j=2:  1+2beta+2beta^4;
    j=3: -(1+beta+beta²+beta³+beta^4)=0;
    j=4:  1+2beta²+2beta³;
    G_(j+5)=-G_j.

The four displayed nonzero expressions are nonzero by the degree-four
minimal polynomial of beta. Therefore exactly j=3 modulo 5 vanish.
Equivalently, with eta=zeta^5 and lambda=eta^t, the zero condition is
t=93 modulo 125. These are six genuinely zero seven-dimensional blocks;
the other 24 c=13 blocks have rank six and simple spectrum.

Across the complete first-old quotient at l=2: c=1 contributes 150 zero
blocks, the four empty singular classes contribute 120 zero blocks,
and the surviving singular circle contributes six zero plus 24 simple.
The c=2,4 classes contribute 300 simple blocks. Thus there are exactly
276 zero blocks and 324 simple rank-six blocks, all of dimension seven.
Again W2 is separate and has dimension 175 with zero compression.

## 6. Executed scope, obligations, and non-claims

exact_singular_sums.py uses only integer cocycles and explicit reduction by
Phi_m. It checks every singular circle and every wild label at l=1,...,5,
using the proved period for l>=3. In order of l, the nonempty singular
circles number 1,1,3,11,53; exact zero-block counts on those circles are
0,6,120,300,3150; their simple rank-six counts are 6,24,330,7950,195600.
Empty-root circles are separately counted in the output. Through this
range all phase-cancellation zeros are on D=0; extending THAT pattern
to all depths is an unproved possible simplification, not needed for
(3), (6), or the exact criterion (7).

The current result is a uniform exact algebraic reduction and
necessary-and-sufficient integer classifier, with closed residue-class
answers for c=1,2,4 and an explicit first singular cancellation. If a
closed 5-adic digit formula is demanded in place of (7), the remaining
obligation is precisely to evaluate the coefficient-balancing condition
for singular square-root families at arbitrary l. No failure of a
first-order criterion is turned into a propagator collision claim.

Reproduction:

    python3 independent_residue.py
    python3 exact_singular_sums.py 1 2 3 4 5

The supplied manifest pins sources, implementations, outputs and actual
commands. Canonical repository files were read only.
