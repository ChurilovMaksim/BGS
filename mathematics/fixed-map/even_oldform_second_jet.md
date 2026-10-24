# Fixed-residue second-order splitting of the three oldform blocks

Status: independently accepted project proof within the stated component scope. The claim concerns only the three actual M-eigenspaces of dimensions3,2,2 isolated by even_oldform_first_order_obstruction.md, for N=7*5^(2r), r>=2. Their first-order slopes vanish, while their second-order Hermitian phase matrices are claimed simple. It is not a theorem of full U-simplicity at any fixed coupling.

## 1. Exact resolvent as a finite rotated-Weyl sum

Put h=5^r, n=h², R=6*5^(2r-1). In CRT coordinates the normalized cat is M7 tensor Mn, with induced primitive roots w of order7 and q of ordern. The oldform unit vector psi has Mn psi=psi and stabilizer expectation

    <psi,T_n(v)psi>=1_(v in h Z²).

Write A=4000^(-1)sum_v d_v T7(v) tensor Tn(v), with the unchanged32 Gaussian-integer coefficients. Let P be one of the full oldform eigenspaces with eigenvalue lambda, and Q=I-P. Its second-order Hermitian phase matrix is

    H2=(i/2) P A Q (lambda+M_Q)(lambda-M_Q)^(-1) Q A P.

For Z=M/lambda one has Z^R=I, and the following polynomial equals (1+Z)/(1-Z) on the complement of the eigenvalue1 and equals zero at1:

    (1/R)sum_(k=1)^(R-1)(R-2k) Z^k.                (1)

To see this, differentiate the finite geometric sum at a nontrivial Rth root; at1 the coefficients sum to zero. Thus no omitted projector or singular denominator is hidden in(1).

Move M^k through the right Weyl operator and then onto the oldform vector and the seven-factor eigenspace. The lambda^k cancels. It follows that H2 is the P7-compression of the COMMON seven-dimensional matrix

    F_r = i/(2R*4000²) sum_(v,u) d_v d_u
          sum_(k=1)^(R-1) (R-2k)
          1_(v+S^k u in h Z²)
          q^(omega(v,S^k u)/2)
          T7(v) T7(S^k u),                          (2)

where S=[[3,4],[2,3]], omega((a,b),(c,d))=ad-bc, and all Weyl phases use modular halves at their own odd modulus. The seven-factor product in(2) includes its exact Weyl cocycle. Its dependence on k is only through k modulo3.

## 2. Actual two-step return classes

Let Q0(a,b)=2b²-a². The matrices [[u,2v],[v,u]] of norm u²-2v²=1 modulo5^s form a group of order6*5^(s-1): there are six solutions modulo5, and each lifts five ways per level by the nonzero norm gradient. The exact order calculation for S shows it generates this group.

A primitive vector has Q0 a unit modulo5 because2 is not a square. Two primitive vectors are related by a unique group element if and only if their Q0 values agree. This follows by solving the two linear equations for u,v; their determinant is a unit. Therefore, for primitive v,u, the return condition in(2) holds exactly when

    Q0(v)=Q0(u) modulo h,

and then the return times form one class k=a modulo L, L=6*5^(r-1), inside0<=k<R. There are h such times. For the only nonprimitive modes, (0,±5), divide both vectors by5 and use modulus5^(r-1), hence period L'=6*5^(r-2). Primitive and nonprimitive modes cannot mix.

Let J=[[0,2],[1,0]]. Modulo h²,

    S^L=I+h beta_r J,   beta_r is a unit, beta_r≡2 modulo5.  (3)

The diagonal part is one modulo h² by the norm equation; the off-diagonal quotient is a unit by the order calculation. The value beta_r≡2 follows from (S^6)_(2,1)/5=2772≡2 and binomial induction.

For a primitive returning pair and k=a+Lj, (3) gives

    q^(omega(v,S^k u)/2) = theta z^j,
    theta in mu_h, z=zeta^C, zeta=q^h,
    C=beta_r Q0(v)/2 modulo h.                       (4)

In particular C is a unit. Indeed S^a u=-v modulo h and
omega(v,Jv)=-Q0(v). All higher binomial terms are zero modulo h². Also L is divisible by3, so the seven-factor operator in(2) is constant along this return class.

The weighted sum is exact:

    sum_(j=0)^(h-1)(R-2a-2Lj)theta z^j
       =2R theta/(1-z).                             (5)

If the class includes k=0, subtract its R contribution because(2) starts at1. This extra finite term vanishes after the normalization below. For nonprimitive pairs the same calculation has a root of order5^(r-1) in place of zeta; the longer list of returning times causes no additional denominator, since its length times L' is still R.

## 3. Leading Gaussian-prime normalization

Use the prime over5 with i reducing to2 and put delta=1-zeta. Its valuation is a_r=1/(4*5^(r-1)). Multiply (2) by4000² delta before reducing.

For primitive returns, (5) and delta/(1-zeta^C) give the residue coefficient

    i d_v d_u / C = 2 d_v d_u / Q0(v) modulo5,       (6)

because theta reduces to1 and beta_r/2 reduces to1. Terms subtracted at k=0 have an extra delta and disappear.

The actual coefficient valuations are crucial. Upper modes a=1 have unit d_v; lower modes a=-1 have valuation2; diagonal modes have valuation at least1. Thus every primitive pair except upper/upper disappears in this normalized residue. For nonprimitive pairs both d_v have valuation1, while the denominator root has valuation5a_r; their total normalized valuation is at least2-4a_r>0. Mixed contents have no returns. Consequently no exceptional coefficient class is omitted.

The upper-mode b values are0,±1,±6,±7,±8. Their distinct norm values are

    -1, 1, 71, 97, 127,

which are pairwise distinct already modulo25. Since r>=2, a surviving upper/upper return therefore has the SAME integer norm, not merely a congruent norm. There are exactly17 ordered pairs: one with b=0 and four choices within each of the other four equal-|b| classes.

For each pair, k modulo3 is determined uniquely by S^k u=-v modulo5, using the six powers of S modulo5. Therefore the leading residue is the single fixed matrix over F_(5^6)

    K = sum_(17 pairs) [2 d_v d_u / Q0(v)]
        w^(omega(v,S^k u)/2) T7(v+S^k u).            (7)

This formula retains both the cocycle and the correct actual upper coefficients. The possible large p-adic return logarithm affects theta but theta reduces to1. No claim that the entire return sum is independent of r is made.

## 4. Bounded residue certificate and lift

oldform_second_jet_residue.py constructs(7) in the pinned field
F5[t]/(t^6+t^4+3t^3+t²+1), with w=t^9. It uses the actual raw Gaussian coefficients reduced at i=2. Let G7 be the raw seven-dimensional cat and tau=Tr(G7). Then H=G7/tau has order3. The code forms all three projectors

    P_gamma=(I+gamma^(-1)H+gamma^(-2)H²)/3,

constructs bases of their images, and computes the characteristic polynomials of their K compressions. The dimensions are3,2,2, and every derivative gcd has degree zero. The complete17-pair dictionary, matrix, compression matrices and characteristic coefficients are in oldform_second_jet_residue.json. These are finite exact calculations, not a test in r.

All primitive seventh roots are Frobenius conjugates over F5; all three cubic eigenvalues are explicitly checked. The characteristic-zero projectors are integral at5 because their denominators are3 and their scalar normalizations are units. Thus the squarefree residue characteristic polynomials lift to simple characteristic-zero compressions of4000² delta F_r. Scaling back proves each actual H2 compression simple, for every r>=2.

The first-order blocks vanish exactly by the separate oldform obstruction. Consequently these three eigenvalue groups split at order t² near zero. The required jet order for THESE groups is exactly two and does not grow with r. Other eigenvalue groups, including possible zero size-seven first-order blocks, are not covered by this theorem. No full or fixed-coupling U-simplicity conclusion is asserted.

## 5. Direct-power support and its limitation

For9j<h, an unrotated word in j actual Fourier modes has |a|<=j and |b|<=9j. A surviving oldform matrix element must have both coordinates divisible by h, hence both are zero as integers. Therefore P_W A^j P_W is scalar on W in that range. The resolvent formula(2) contains S^k u instead, so this growing direct-power threshold does not obstruct second-order effective splitting. Equations(3)–(7) exhibit the non-scalar rotated returns that bypass it.

## Publication and dependency scope

This exact source has its separately pinned independent review in the
cat/jet promotion map. The final accepted combined FM-026 statement is in
[the theorem owner](literal_time_multiplicity_bounds.md). Conditional sector
premises retain their historical proof structure and are used only where
the separately accepted premise is explicitly bound. No unpublished CRT or
first-old-layer diagnostic is a new theorem input or extra U dimension.
