# Independent audit: uniform oldform second-order splitting

Date: 6 October 2026. Review workspace: `/workspace/shared/bgs_uniform_second_jet_review`. Canonical BGS was read-only. Its observed HEAD was `a4d59bf91b1aeff88719e3b1eaa0ba3b8dafe8d8`; concurrent unrelated work is present, so no clean-tree or whole-tree immutability claim is made. The reviewed sources are individually frozen and hash-bound.

## Claim and verdict

**Primary verdict: proved as written.** For every integer r≥2, N=7·5^(2r), the three complete actual M_N eigenspaces singled out by the accepted first-order obstruction have dimensions 3,2,2, zero first-order phase matrices, and simple second-order Hermitian phase matrices. The jet order needed to separate each of these three groups is exactly two.

The target is `inputs/uniform_oldform_second_jet.md`, SHA-256 `c504620ef3111c7cf40af636eb7d00a1b4103463986c3ff3f7d8e3f01fee0e3a`. Its frozen candidate manifest matches all five named source hashes. No mathematical correction is required. The proof is uniform in r, with a separately reconstructed finite exact certificate; it is not extrapolation from r=2,3.

This conclusion covers only these three groups. It does not establish splitting of any size-seven group, full U_N simplicity at any coupling, a quantitative interval in coupling uniform in r, the full commutant, or BGS universality. The normalized residue matrix itself need not be Hermitian over the residue field; Hermiticity belongs to the characteristic-zero H_2 before the complex scalar normalization.

## Dependency graph

1. Actual raw kernel and symbol + exact CRT + accepted oldform obstruction → three full λ-eigenprojections, dimensions 3,2,2, with PAP=0.
2. Second-order block elimination + scalar cat return → exact reduced-resolvent polynomial → actual rotated two-Weyl sum, with cancellation of λ^k.
3. Elementary norm-one torus and exact order of S → exhaustive primitive/nonprimitive return classes at every r.
4. Linearized cat return + exact weighted geometric sum → cancellation of R and explicit cyclotomic denominator.
5. Actual Gaussian coefficient valuations + cyclotomic valuations → only the 17 upper/upper pairs remain after multiplication by 4000²(1−q^h).
6. Independently reconstructed fixed residue matrix and all three projector compressions → squarefree characteristic polynomials.
7. Integral split projector lattices + reduction of characteristic polynomials → simple characteristic-zero second-order matrices.

The accepted uniform cat multiplicity theorem and first-order obstruction are dependencies, rather than reclassified here as new results. The latter review also independently verifies the CRT roots, full eigenspaces, raw symbol and H_2 sign. This audit rederives the new return, normalization, finite residue and lifting steps. No external literature theorem is needed for those steps, and no author computation is imported into either independent checker.

## Obligation matrix

| Obligation | Verdict | Decisive evidence |
|---|---|---|
| H_2 sign and coefficient of t² | Passed | Schur expansion gives +(i/2) PAQ(λ+B)(λ−B)^−1QAP |
| Reduced-resolvent polynomial including eigenvalue 1 | Passed | Exact polynomial identity below; f_R(1)=0 |
| Scalar return and λ cancellation | Passed | M^R scalar from Weyl covariance; λ^R is that scalar; M^kP=λ^kP |
| CRT primitive roots | Passed | w=e_7(n^−1), q=e_n(7^−1), same raw halves and labels |
| Raw Weyl cocycle and order | Passed | Direct products of independent 7×7 Weyl matrices match the cocycle formula |
| Primitive torus orbit classification | Passed uniformly | Norm fiber is a free transitive norm-one torus orbit |
| S order, diagonal return and β_r≡2 | Passed uniformly | Binomial induction from S^6, then the norm equation |
| Mixed contents | Passed | Invertibility modulo 5 preserves primitivity |
| Nonprimitive actual modes | Passed uniformly | Exactly (0,±5); period 6·5^(r−2), root order 5^(r−1) |
| Weighted sum and k=0 deletion | Passed uniformly | Finite geometric identity; deletion cancels R before reduction |
| Actual Gaussian valuations | Passed | Independent raw-symbol assembly and exact Gaussian division |
| Exhaustiveness of 17 surviving pairs | Passed uniformly | Norm residues are distinct modulo 25; all omitted pairs have positive normalized valuation |
| r=2 boundary | Passed | All 1,024 mode pairs and all 750 times checked, including every nonprimitive return |
| Finite matrix and characteristic polynomials | Passed independently | Different field representation, direct arithmetic, matrix-product Weyl construction, permutation determinants |
| Integral reduction and lift | Passed | Denominators 3 and τ are units; residue discriminants are nonzero |
| Other size-seven blocks or full U spectrum | Out of scope | No conclusion supplied by this certificate |

## Uniform proof reconstruction

### 1. Exact reduced resolvent and cancellation

For a complete λ-eigenprojection P, Q=I−P, B=M restricted to Q, and PAP=0, block elimination for exp(itA)M gives

    effective eigenvalue matrix
      = λ[I − (t²/2) PAQ(λ+B)(λ−B)^−1QAP] + O(t³).

Thus the coefficient of t² in the eigenphase is

    H_2 = (i/2) PAQ(λ+B)(λ−B)^−1QAP.

For a complementary eigenvalue μ=e^(iφ), λ=e^(iθ), its scalar weight is (1/2)cot((θ−φ)/2), hence real. This fixes both sign and factor.

Weyl covariance and S^R=I show that M^R is scalar. Since λ is an eigenvalue, Z=M/λ satisfies Z^R=I, regardless of the raw cat’s scalar phase. Define

    f_R(z) = (1/R) Σ_(k=1)^(R−1) (R−2k) z^k.

In Q[z]/(z^R−1), direct coefficient subtraction gives

    (1−z)f_R(z) = 1+z − (2/R)Σ_(k=0)^(R−1)z^k.

Consequently f_R(z)=(1+z)/(1−z) at every nontrivial R-th root, and f_R(1)=0 by summing the coefficients. This is exactly the reduced resolvent with its singular eigenspace removed.

For every right Weyl factor, M^k T(u)P=T(S^k u)M^kP=λ^kT(S^k u)P. The λ^(−k) in Z^k therefore cancels completely. The tensor-product oldform expectation is the indicator that v+S^k u is divisible by h in both coordinates. The remaining n-factor product contributes q^(ω(v,S^k u)/2), and the seven-factor product is literally T_7(v)T_7(S^k u), with its raw cocycle. This proves target equation (2), including operator order.

CRT uses w=e_7(n^−1 mod7), q=e_n(7^−1 modn). Both are primitive. Modular halves and inverse eights reduce correctly in each factor, so no additional midpoint sign or phase is introduced. Modulo 7, S has order 3.

### 2. All primitive return classes

Let O_s=Z/5^s and G_s be the pairs (x,y) with x²−2y²=1, acting by [[x,2y],[y,x]]. There are six pairs modulo 5. At every lift step the derivative (2x,−4y) is not identically zero modulo 5, so every solution has exactly five lifts. Hence |G_s|=6·5^(s−1).

The exact sixth power is

    S^6 = [[19601,27720],[13860,19601]],
    (S^6−I)/5 ≡ [[0,4],[2,0]] = 2J (mod5),
    J = [[0,2],[1,0]].

Binomial induction shows S^(6·5^(s−1))=I+5^s B_s with B_s≡2J modulo 5. As S has order six modulo 5, its exact order modulo 5^s is 6·5^(s−1). It therefore generates all of G_s.

For a primitive vector u=(a,b), D=a²−2b² is a unit, since 2 is nonsquare modulo 5. To send u to v=(c,d), solve

    [[a,2b],[b,a]] [x,y]^T = [c,d]^T.

The determinant is D, a unit, so the solution is unique. The identity Q_0(gu)=(x²−2y²)Q_0(u) implies this solution lies in G_s exactly when Q_0(v)=Q_0(u). This proves, without a counting surrogate, the free transitive action on every primitive norm fiber.

Taking target −v gives the exact return criterion modulo h. Every primitive return class has period L=6·5^(r−1) and exactly R/L=h representatives in [0,R). Mixed primitive/nonprimitive pairs cannot return, since S is invertible modulo 5.

The only nonprimitive actual modes are (0,±5). Dividing both vectors by 5 gives a primitive problem modulo h/5, with period L/5 and exactly 5h representatives in [0,R). This covers all actual mode classes.

### 3. Phase progression and weighted sum

Write S^L=xI+yJ. The preceding order calculation gives 5-adic valuation v_5(y)=r and x≡1 modulo 5. The norm equation (x−1)(x+1)=2y² then gives x≡1 modulo h². Thus

    S^L = I+hβ_r J (mod h²),  β_r≡2 (mod5).

For a primitive return with representative a, S^a u≡−v modulo h. As J²=2I and h²=0 in the relevant quotient, for k=a+Lj:

    ω(v,S^k u)/2
      = ω(v,S^a u)/2 + jhβ_r Q_0(v)/2 (mod h²).

Here ω(v,Jv)=−Q_0(v), including the sign from S^a u≡−v. The constant exponent is divisible by h. Thus the phase is θ z^j, θ∈μ_h, z=ζ^C, ζ=q^h, C=β_rQ_0(v)/2 a unit modulo 5. Since L is divisible by 3, the seven-factor operator is constant on this return class.

For any z≠1 with z^m=1, the exact identities Σz^j=0 and Σjz^j=−m/(1−z) give

    Σ_(j=0)^(m−1)(R−2a−2Lj) θ z^j = 2R θ/(1−z)

when mL=R. For primitive returns m=h. For nonprimitive returns, apply the same calculation after division by 5: m=5h, L is replaced by L/5, and z has order h/5. The fact that m is 25 times the root order changes neither identity nor denominator. It is important that this identity cancels R exactly; a bound on individual summands would not justify the normalization.

If a=0, the k=0 summand omitted in the reduced-resolvent polynomial is R, with phase 1. After the prefactor 1/(2R), its contribution is a finite coefficient, not a residual 5-adic denominator. Multiplication by δ therefore makes it vanish in the residue.

### 4. Valuations and the exhaustive residue

Take the Gaussian prime at which i≡2 and normalize v(5)=1. Its uniformizer can be taken as 2−i. The actual upper coefficients are unit multiples of −3−4i, whose reduction is −11≠0. The lower coefficients are unit multiples of −3+4i=−(2−i)² and have valuation two. Every diagonal coefficient has valuation at least one; for (0,±5) it is exactly one. These statements were also checked by exact Gaussian division after independently assembling the raw centered symbol.

For ζ of order h, put δ=1−ζ. Since Φ_h(1)=5 and every primitive conjugate of δ has the same valuation,

    v(δ)=a_r=1/(4·5^(r−1)).

For unit C, δ/(1−ζ^C) reduces to 1/C. The primitive-return contribution to 4000²δF_r therefore reduces to i d_vd_u/C=2d_vd_u/Q_0(v). Every primitive pair other than upper/upper has positive coefficient valuation and disappears.

For nonprimitive pairs, the denominator uses a primitive root of order h/5 and has valuation 5a_r. Both coefficients have valuation one. The normalized total valuation is therefore exactly

    2+a_r−5a_r = 2−4a_r > 0.

In particular at r=2 this is 9/5, not zero or negative. This addresses the lower-order-root issue without discarding those terms prematurely. Mixed contents have no returns. The k=0 deletion terms also have positive valuation. Sums of these integral positive-valuation terms cannot create a negative-valuation contribution.

The upper b labels are 0,±1,±6,±7,±8. Their norm values and residues modulo 25 are

    −1→24, 1→1, 71→21, 97→22, 127→2.

These residues are distinct. Therefore, for every r≥2, an upper/upper return is possible exactly within equal integer-norm classes. There is one ordered pair from b=0 and four ordered pairs from each nonzero absolute-b class, yielding exactly 17. Their k modulo 6 is already determined modulo 5; thus their k modulo 3, seven-factor product and limiting coefficient are fixed independently of r.

### 5. Independent finite certificate

`check_residue.py` uses F_5[W]/Φ_7(W), with Φ_7=1+W+...+W^6. This field is different from the author’s polynomial representation; irreducibility follows because 5 has order 6 modulo 7. Arithmetic is direct polynomial multiplication/reduction, without exponent/log tables, NumPy or author imports.

The raw 32 coefficients are assembled from the trigonometric symbol using rational arithmetic. The 17-pair matrix is built from products T_7(v)T_7(S^k u), and each product is separately checked against the raw cocycle. Raw cat covariance G T(v)=T(Sv)G is checked on all 32 modes. The three eigenspaces and projectors are constructed by exact elimination. Characteristic polynomials use permutation determinants, independently of the author’s Newton identities. Euclidean polynomial gcd with each derivative is one.

An explicit isomorphism is found by requiring the author’s generator t to satisfy its pinned polynomial and t^9=W. Its image is

    t = 1+3W+2W²+W⁴.

Under this isomorphism, every author pair coefficient, the entire K matrix, all three compression matrices and all characteristic coefficients agree exactly. This comparison is a check after independent construction, not an input defining K.

In the W representation, put

    γ = 1+3W+3W²+3W⁴,  γ² = 3+2W+2W²+2W⁴.

The exact characteristic polynomials are:

    dimension 3, eigenvalue 1:
      X³ + (2+W³+W⁴)X²
         + (4+4W²+W³+W⁴+4W⁵)X + (2+W³+W⁴);

    dimension 2, eigenvalue γ:
      X² + 4X + (W²+4W³+4W⁴+W⁵);

    dimension 2, eigenvalue γ²:
      X² + (3+4W³+4W⁴)X + (4+2W²+W³+W⁴+2W⁵).

Every derivative gcd equals 1. `residue_checks.json` includes all data and the full independent coefficient/valuation table. The Frobenius orbit of W contains all six primitive seventh roots, and all three cube roots are checked. Consequently changing the actual CRT primitive power does not create an unchecked block.

### 6. Lifting the certificate

Let O be the valuation ring of a number field containing the roots, cat scalars and entries, at the chosen prime above 5. The normalized F_r has integral entries by the preceding uniform calculation, and its reduction is K. For the raw seven-dimensional cat G, τ=Tr(G) is a 5-adic unit, as its nonzero residue is explicitly checked (also τ²=−7 in characteristic zero). Set H=G/τ. Its three projectors have denominators only 3 and powers of τ, hence lie in Mat_7(O).

Each projector splits O^7 as a direct summand. Over the local valuation ring its image is free, and a basis can be chosen lifting a residue-image basis. The characteristic polynomial of its normalized compression reduces to the computed characteristic polynomial of P_γ K on the image. The nonzero residue discriminant implies the characteristic-zero discriminant is nonzero. Scaling back by the nonzero scalar 4000²δ preserves simplicity.

Finally PAP=0 exactly, whereas each H_2 is simple. The analytic local spectral block can be represented by a Hermitian analytic phase matrix, divided by t² after its zero constant and linear terms are removed. Its limit is H_2; distinct eigenvalues remain separated for sufficiently small nonzero t, for each fixed r. This gives exactly the claimed second-order group splitting, with no uniform interval or statement about other groups.

## Boundary controls and execution

Commands, from the review directory:

    python3 check_residue.py
    python3 check_returns.py

The programs use only Python 3.12.14 standard-library exact arithmetic, deterministic inputs and assertions, with optimized assertion-free execution explicitly rejected.

`check_returns.py` checks all 1,024 ordered actual-mode pairs and every time k in [0,R) at r=2 and r=3. It verifies their exact return periods, phase progression, denominator order, seven-factor period, normalized coefficient valuation, and the weighted-sum identity by reduction modulo Φ_(h²), including k=0 subtraction classes. These finite controls complement the uniform proof, rather than replacing it.

- r=2: h=25, n=625, R=750, β_r=22 modulo 25. There are 124 primitive returning pairs and four nonprimitive pairs. Exactly 17 have nonzero normalized residue. The four nonprimitive pairs each have 125 returns of period 6, root order 5, and normalized valuation 9/5. All 128 exact weighted-sum identities pass.
- r=3: h=125, n=15625, R=18750, β_r=122 modulo 125. There are 108 primitive returning pairs and four nonprimitive pairs. Exactly 17 survive. Nonprimitive pairs each have 625 returns of period 30, root order 25, and normalized valuation 49/25. All 112 exact weighted-sum identities pass.
- The larger number of primitive congruence returns at r=2 is real. Every extra pair is killed by coefficient valuation; the proof does not mistakenly equate integer norms for all primitive modes.
- Complete norm-one torus/orbit controls pass modulo 5 and 25. Exact polynomial controls for the reduced resolvent pass at R=3,6,30,150,750,18750.

## Source integrity and remaining gap

There is no remaining implication in the stated three-block theorem. The finite implementation and assertion are independently verified, with the uniform reduction proved separately above.

The original candidate manifest binds its finite script and JSON but omits three transitive imports: `field15625.py`, canonical `frozen_antireversor.py`, and `spectral_extension/reduced_chain_charpolys.py`. This is a provenance-hardening suggestion, not a mathematical failure; this review freezes and hashes all three, and its independent checker does not import them. Full hashes, generated outputs, execution scope and canonical-source boundaries are recorded in the review manifests.

The cheapest next action is to preserve this exact scoped proof and the independent certificate together. The next scientific obstruction beyond this result remains splitting the other actual eigenspace groups; it is not resolved by this audit.
