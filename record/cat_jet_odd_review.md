# Independent audit: second-order splitting of the deepest odd oldform core

Date: 6 October 2026. Review workspace: `bgs_odd_core_second_jet_review`. Canonical BGS was read-only. The observed canonical HEAD was `801de3ab760cab4349e68b9843dcd67955314e62`; the observed status was clean. These observations are not a claim that a concurrently maintained repository remained immutable. The reviewed sources are individually frozen and hash-bound.

## Normalized claim and verdict

**Primary verdict: proved as written.** For every integer r >= 2 and N = 7·5^(2r+1), the six complete actual cat eigenspaces contained in the deepest oldform subspace H_7 tensor J_r H_5 have dimensions 7,7,7,4,5,5, zero first-order phase matrices, and simple second-order Hermitian phase matrices. Each of these six groups consequently splits at exactly second order near zero coupling.

The audited source is `inputs/odd_core_second_jet_extension.md`, SHA-256 `38b1e1b442f942a81a3ea7f89c9bd6a91f4a6ed39f12beb644d0c44064d0b46e`. All eight source files match the supplied candidate manifest. No mathematical correction or scope restriction is needed.

The result concerns only this 35-dimensional deepest core. It does not establish simplicity of the other oldform layers, new blocks, the full kicked propagator at any fixed coupling, the literal fixed-coupling U, a uniform interval in coupling, its full commutant, or BGS universality. The normalized residue need not be Hermitian in characteristic five; Hermiticity belongs to the actual characteristic-zero second-order phase matrix before complex scalar normalization.

### Accepted dependencies

- Even-depth second-order theorem and its fixed residue: `inputs/accepted_even_REPORT.md`, SHA-256 `c3a98ad153737e4cdac381bf6318eff2d3c44e073a81a7387dbee785ab6a172c`. Its accepted proof source is `uniform_oldform_second_jet.md`, SHA-256 `c504620ef3111c7cf40af636eb7d00a1b4103463986c3ff3f7d8e3f01fee0e3a`. This supplies the correct reduced-resolvent convention, actual coefficients, fixed 17-pair K_7 dictionary, and individually squarefree compressed polynomials.
- Complete oldform tower and zero first order: `inputs/accepted_tower_REPORT.md`, SHA-256 `f3d142204ed6d10015e70595633c714acaf097fa1b0e6f19fdf6a51d4e663be5`. Its source is `oldform_tower_compression.md`, SHA-256 `d359482763667a6707ed9a060a3874e951f95336561a4ac645df453022b085ae`. This supplies complete-eigenspace isolation, the exact intertwining and Weyl compression, and the uniform cat simplicity input.
- The unchanged raw kernel and centered symbol are in `inputs/fixed_model_symmetry_theorem.md`, Section 1.

Those previously accepted reviews are inherited evidence, not falsely represented as fresh executions of their entire dependency closures. The odd-depth lattice, matrix geometric sum, valuations, product-sector compression and new pairwise arithmetic are audited here. None of these steps needs an external literature theorem.

## Dependency graph

1. Accepted full oldform tower -> six complete actual eigenspaces in H_7 tensor J_r H_5, and PAP = 0.
2. Raw Weyl covariance, a small-translation polynomial lattice, and the exact sixth-power cat phase -> a cat-stable H_5 lattice with every T_5(v) congruent to I modulo rho.
3. Accepted norm-torus return classification plus exact translated-oldspace covariance -> operator returns D_0 B_a^j, including the internal five-dimensional Weyl cocycle.
4. Exact matrix geometric identity -> cancellation of R and a single scalar-dominant cyclotomic denominator for each return class.
5. Strict valuation comparison and actual Gaussian coefficient classes -> normalized common operator reducing to K_7 tensor I_5, uniformly in r.
6. Integral product-cat projectors -> each normalized compression reduces to a direct sum of distinct members of the three accepted K_7 compression blocks.
7. Fresh pairwise gcd/resultant certificate, together with the accepted individual squarefreeness -> every such direct sum has nonzero discriminant.
8. Integral projector lattices and discriminant reduction -> actual characteristic-zero second-order simplicity.

There is no circular dependency on the odd-depth conclusion and no extrapolation from a finite list of r.

## Obligation matrix

| Obligation | Status | Decisive check |
|---|---|---|
| Complete actual eigenspaces and zero first order | Passed, accepted input | Exact tower theorem at j=r, e=2r+1 |
| Shift wraparound on L_0 | Passed | Integral Lagrange correction has valuation at least 5/8 |
| Multiplication by eta^x and raw Weyl midpoint | Passed | Binomial expansion and scaled-degree bound; midpoint root is even closer to 1 |
| Raw M_5 scalar phase | Passed | Gauss trace squared is 1; simple spectrum and scalar sixth power give M_5^6=I |
| Cat-stable lattice and eigenbasis | Passed | Finite sum of six lattice images, exact covariance, integral order-six projectors |
| Exact translated-oldspace operator | Passed | Explicit B_u=z_u T_5(b_u), with the stated sign |
| Conjugation at the first return time | Passed | B_a=M_5^a B_u M_5^(-a), with no unexplained scalar phase |
| Matrix weighted geometric sum | Passed | Right multiplication by I-B_a yields 2R D_0 exactly |
| Primitive scalar denominator | Passed uniformly | Order 5^(r+1), leading quotient Q_0(u) |
| Nonprimitive and mixed-content classes | Passed uniformly | Only (0,+/-5); scalar order 5^r; mixed classes impossible |
| r=2 strict valuation margin | Passed | v(delta)=1/100, nonprimitive denominator valuation 1/20 < 1/8 |
| Internal five-factor cocycle | Passed | Explicit exponent progression, exhaustively checked at r=2,3 |
| Exact 17-pair residue and seven-factor cocycle | Passed | Same norm classes and time modulo 3; accepted fixed K_7 retained |
| Product-sector compression | Passed | Orthogonal five-factor projectors kill all cross terms |
| New pairwise finite input | Passed independently | Three gcds 1, three nonzero Sylvester resultants, product degree seven squarefree |
| Discriminant lift | Passed | Integral direct summands with unchanged residue ranks |
| Other layers or full/literal U simplicity | Out of scope | No implication supplied |

## Reconstruction of the new uniform implications

### 1. The lattice survives wraparound and raw phases

Work over a finite extension of Q_5 containing the relevant roots and cat entries, with valuation normalized by v(5)=1. Let eta be primitive of order five, rho^2=eta-1, and v(rho)=1/8. The five functions rho^k x^k, k=0,...,4, are a basis of the function space: the unscaled evaluation determinant is the Vandermonde product of differences among 0,...,4, hence a 5-adic unit.

For Xf(x)=f(x+1 mod 5), the ordinary polynomial difference of rho^k x^k lowers degree by at least one, hence gains at least one rho. At x=4, the difference between polynomial evaluation at 5 and cyclic evaluation at 0 is -rho^k 5^k for k>=1. Interpolation of this point mass has coefficients integral at five, because all Lagrange denominators are products of nonzero differences among 0,...,4. Its output degree d<=4 therefore has valuation at least

    k + (k-d)/8 >= k + (k-4)/8 >= 5/8.

For k=0 this correction is zero. Thus wraparound does not break the claimed 1/8 bound.

For Zf(x)=eta^x f(x), the exact finite expansion is

    eta^x = sum_(j=0)^4 binom(x,j) rho^(2j),  x=0,...,4.

The denominator j! is a 5-adic unit. Multiplication of rho^k x^k by the jth term, j>=1, followed by reduction modulo the monic integral polynomial product_(a=0)^4(x-a), has output degree d<=k+j. The scaled coefficient valuation is at least j/4+(k-d)/8 >= j/8. Hence Z-I also sends L_0 into rho L_0.

Every raw Weyl is a product of powers of X and Z and a fifth-root midpoint scalar. The scalar minus one has valuation at least 1/4. Therefore every T_5(v)-I sends L_0 into rho L_0, with the raw modular-half convention intact.

### 2. The raw cat really has sixth power one

Covariance and the order-six label action imply M_5^6 is scalar by irreducibility of the Weyl representation. The accepted simplicity theorem makes its five eigenvalues five distinct members of a scalar multiple of the sixth roots. If m is the missing sixth root in that coset, the sum of the whole coset is zero, so m=-Tr(M_5).

For the normalized raw kernel, its diagonal trace is a fifth-root quadratic Gauss sum divided by sqrt(5). Its square is one. For example, g=1+2eta+2eta^4 has g^2=5, while the trace numerator uses the nonsquare exponent 2 and equals -g. Either sign chosen by the primitive-root embedding and positive complex normalization still gives (Tr M_5)^2=1. The scalar sixth power is m^6=1.

Thus L=sum_(j=0)^5 M_5^j L_0 is a finite full lattice stable under M_5. Exact covariance gives

    (T_5(v)-I) M_5^j = M_5^j (T_5(S^(-j)v)-I),

which sends each summand into rho times that summand. Every T_5(v)-I therefore sends L into rho L.

Order-six spectral projectors have denominator 6, a unit at five, and preserve L. Their five nonzero images have rank one and split L as a direct sum. After adjoining the sixth roots if needed, this is an integral eigenbasis. Distinct sixth roots remain distinct in characteristic five. No assertion that the standard Fourier matrix is integral or a unit was used.

### 3. Exact operator-valued returns, with order and cocycle

Put h=5^r, n=5h^2, R=6·5^(2r), J=J_r, and L_h=6·5^(r-1). The accepted intertwining gives M_n J=J M_5. Since M_5^(L_h)=I and S^(L_h)u-u is divisible by h, covariance and the raw Weyl product imply

    M_n^(L_h) T_n(u)J = T_n(u)J B_u,
    B_u = z_u T_5(b_u),
    b_u = (S^(L_h)u-u)/h mod 5,
    z_u = q^(-omega(u,S^(L_h)u)/2).

The sign follows from T(u)T(w)=q^(omega(u,w)/2)T(u+w), applied to w=S^(L_h)u-u. The compression formula also proves the needed intertwining T_n(hb)J=J T_5(b): alternatively it follows from the same explicit oldform support formula. This is equality of operators, not equality only after taking a trace.

Write S^(L_h)=aI+h beta J_0, with J_0=[[0,2],[1,0]]. The exact cat order calculation gives beta congruent to 2 modulo 5, and the norm equation gives a-1 divisible by h^2. Because omega(u,J_0u)=-Q_0(u), the exact scalar is

    z_u=(q^h)^(beta Q_0(u)/2).

For primitive u its order is 5h=5^(r+1). Since the eigenvalues of T_5(b_u) are fifth roots, 1 is not an eigenvalue of B_u. Also B_u^(R/L_h)=I.

Let a be the first return time for the ordered pair (v,u), and write k=a+L_h j. The precise conjugation omitted from the source's short prose is

    T_n(S^k u)J = T_n(S^a u)J B_a^j,
    B_a = M_5^a B_u M_5^(-a)
        = z_u T_5(S^a b_u).

There is no additional phase in this exact covariance. On the returning class,

    J* T_n(v) T_n(S^k u)J = D_0 B_a^j,
    D_0 = q^(omega(v,S^a u)/2) T_5((v+S^a u)/h).

This formula retains the internal five-dimensional Weyl cocycle. If c_0=(v+S^a u)/h and b_a=S^a b_u, its explicit scalar exponent at the jth return is

    E_j = E_0 + j Z_u + h^2 j omega(c_0,b_a)/2  (mod n),

where z_u=q^(Z_u). The last term must not be dropped. The five-dimensional label is c_0+j b_a modulo five. These are exactly the independently checked finite progression identities.

Since L_h is divisible by three, the seven-dimensional factor is fixed along this return class. The accepted reduced-resolvent polynomial cancels the cat eigenvalue lambda^k against lambda^(-k), so the same common 35-dimensional rotated-Weyl sum compresses to all six complete eigenspaces.

For the only nonprimitive modes u=(0,+/-5), write u=5u_0 and use L_h'=6·5^(r-2). The same argument works since M_5^(L_h')=I, including r=2. Now

    z_u=(q^(5h))^(beta Q_0(u_0)/2),

which has order h=5^r. The returning class has R/L_h'=25h terms; its length is a multiple of both the scalar order and five, so B_a to that length is I. Primitive and nonprimitive modes cannot return together because the label action is invertible modulo five.

### 4. Matrix geometric cancellation really removes R

For B^m=I and I-B invertible, the polynomial identities give

    sum_(j=0)^(m-1) B^j=0,
    sum_(j=0)^(m-1) j B^j=-m(I-B)^(-1).

Thus, with mL_h=R (or mL_h'=R),

    sum_j (R-2a-2L_h j) D_0 B^j = 2R D_0(I-B)^(-1).

D_0 is always on the left; no commutation with B is assumed. Equivalently, multiplying the weighted sum on the right by I-B yields 2R D_0. This cancels the factor R in the actual reduced resolvent exactly before any valuation estimate. The k=0 term, when present, contributes only a finite unweighted correction after this cancellation, and multiplication by delta makes it vanish in the residue.

### 5. Scalar-dominant denominator, coefficient classes and K_7

Let zeta=q^h and delta=1-zeta. Then v(delta)=1/(4h)<1/8. For a primitive return, B=z T_5(b), z=zeta^C with C congruent to Q_0(u) modulo five. On the lattice L,

    (I-B)/delta = ((1-z)/delta)I - z(T_5(b)-I)/delta.

The second term has positive valuation, and the first reduces to C I=Q_0(u)I. The reduced matrix is invertible. Consequently its inverse is integral and

    delta D_0(I-B)^(-1) reduces to Q_0(u)^(-1)I_5.

Here D_0 reduces to I_5 because its Weyl part is small on L and every five-power scalar root reduces to one.

For nonprimitive returns let delta'=1-z. Its valuation is 5v(delta), still strictly less than 1/8. The identical argument with delta' proves an inverse-denominator bound, while the two actual coefficients each have valuation one. Their normalized contribution has valuation at least

    2 + v(delta) - v(delta') = 2 - 4v(delta) > 0.

At r=2 this is 49/25 and the denominator valuation is 1/20, safely below 1/8. This addresses the boundary without assuming a scalar translation operator.

The actual upper coefficients have Gaussian valuation zero at i congruent to 2, lower coefficients valuation two, and all diagonal coefficients valuation at least one. Thus among primitive pairs only upper/upper survives the normalization 4000^2 delta. All k=0 subtractions and all nonprimitive terms disappear. The upper norm values -1,1,71,97,127 are distinct already modulo 25, so all surviving pairs have equal integer norms. There are exactly 17 ordered pairs, as in the accepted even-depth residue.

Their return time modulo three is fixed by the action modulo five, so the seven-factor cocycle is identical to the accepted K_7 formula. The prefactor i reduces to 2; the leading denominator quotient is Q_0. Therefore the normalized common odd-core operator reduces to exactly K_7 tensor I_5. There is no hidden dependence on r in this leading matrix. All primitive seventh roots are Frobenius conjugate over F_5, and the accepted certificate handles all three seven-factor cat eigenvalues.

### 6. Why the product-sector compression is a direct sum

Let P_gamma be a seven-factor cat projector and E_mu a five-factor cat projector. At a fixed product eigenvalue lambda,

    P_lambda = sum_(gamma mu=lambda) P_gamma tensor E_mu.

For each gamma there is at most one mu, and different gamma give different mu. All these projectors are integral on the chosen lattices. In the normalized reduction,

    (P_gamma tensor E_mu)(K_7 tensor I)(P_gamma' tensor E_mu')
      = (P_gamma K_7 P_gamma') tensor (E_mu E_mu').

If gamma differs from gamma', then mu differs from mu', so the second factor is zero. Therefore the compression is a direct sum of a subset of the three K_7 compressed blocks, with no off-diagonal mixing. The dimensions are exactly the accepted six core dimensions 7,7,7,4,5,5.

The accepted certificate gives individually squarefree polynomials. The fresh calculation below gives pairwise coprimality. Hence every subset direct sum is squarefree. Integral idempotents split a free lattice into free direct summands over the valuation ring, and a residue-image basis lifts to a basis of each summand. Thus the characteristic-zero characteristic polynomial reduces to the checked squarefree polynomial. Its discriminant is nonzero. Removing the nonzero common normalization preserves simplicity of the actual H_2.

Finally PAP=0 exactly, while each H_2 is simple. The local analytic Hermitian phase matrix, with its scalar constant and zero linear term removed and divided by t^2, tends to H_2. Distinct second-order eigenvalues separate for sufficiently small nonzero t for each fixed r. This proves the claimed jet order, with no claim of a neighborhood uniform in r.

## Fresh exact finite evidence

The three checkers use only Python 3.12.14 standard-library exact arithmetic and explicit runtime checks. They import no candidate code. Commands from the review directory are:

    python3 check_pairwise.py
    python3 check_lattice.py
    python3 check_operator_returns.py

### Pairwise certificate

`check_pairwise.py` reconstructs the three accepted characteristic polynomials in F_5[W]/Phi_7(W). It maps the pinned author generator to t=1+3W+2W^2+W^4, verifies t^9=W and its defining polynomial, and checks every source characteristic coefficient. Euclidean gcd and an independent permutation-determinant Sylvester resultant are computed for each pair. The resultants, in ascending W coefficients, are:

- blocks 0,1: (3,0,1,3,3,1);
- blocks 0,2: (4,0,4,0,0,4);
- blocks 1,2: (3,0,3,2,2,3).

All are nonzero; all three gcds are one. The entire degree-seven product also has derivative gcd one. These computations rebuild the new finite input; they do not merely rerun the candidate's imported field implementation.

### Five-dimensional lattice and phase

`check_lattice.py` works exactly in

    Q[rho]/(rho^8+5rho^6+10rho^4+10rho^2+5).

The polynomial is Eisenstein, so the valuation of its degree-below-eight representation is the minimum coefficient valuation plus degree/8; different terms cannot have equal valuation because their degrees differ modulo eight. It constructs every raw T_5(a,b) in the rho^k x^k basis using exact Lagrange interpolation. All 24 nonidentity Weyl differences have minimum valuation exactly 1/8. It also checks the Gauss square, normalized trace -1, the cat sixth-power identity and all 25 exact covariance identities. Changing the complex square-root normalization by a sign leaves the sixth-power identity and lattice sum unchanged.

### Whole-support odd-depth return checks

`check_operator_returns.py` independently assembles all 32 actual Gaussian coefficients from the displayed trigonometric symbol. At both r=2 and r=3 it enumerates all 1,024 ordered pairs and every k in [0,R), then checks exact operator-valued phase/label progressions and weighted geometric sums by cyclotomic reduction separately in all 25 Weyl basis components.

- r=2: N=21875, n=3125, R=3750; 120,000 mode-time steps; 124 primitive returning pairs and four nonprimitive returning pairs; 18,000 returning terms including k=0; 128 exact operator geometric checks; 32 k=0 classes; exactly 17 surviving upper/upper pairs.
- r=3: N=546875, n=78125, R=93750; 3,000,000 mode-time steps; 108 primitive and four nonprimitive returning pairs; 80,000 returning terms including k=0; 112 exact operator geometric checks; 32 k=0 classes; exactly 17 survivors.
- At r=2 the nonprimitive period is six, there are 625 returns in each such class, the scalar root order is 25, and the normalized valuation is 49/25. At r=3 these values are respectively 30,3125,125,249/125.

These are exhaustive at the two stated depths, not exhaustive over all r. The all-r implication comes from the separately reconstructed lattice and exact matrix geometric proof above. The author's separate F_525001 35-dimensional control was inspected and frozen, but was not rerun and is not a proof dependency of this verdict. Its 17,968 nonzero-time return count agrees with our independent 18,000 minus 32 k=0 terms.

## Source integrity, remaining gap and safest conclusion

There is no remaining implication gap in the stated deepest-odd-core theorem. The current review is independent of the proof author and new finite implementation, but remains an internal mathematical audit rather than a formal proof-assistant certification or external referee decision.

The candidate manifest binds the eight listed files but does not itself bind the transitive imports used by its short pairwise script or its direct control. Our fresh checkers do not import those programs. The review separately freezes and hashes their directly relevant transitive source files for provenance; this omission is a reproducibility-hardening issue, not a mathematical defect in the theorem.

The strongest safe conclusion is exactly the six-core-block second-order theorem for all r>=2. The cheapest next action is to retain the scoped proof, accepted input bindings and this report together. No extension to a larger oldform layer follows automatically: it would need its own small-translation/projector analysis and a correspondingly larger finite residue certificate.

## Publication mapping

Exact original proof/review bytes and dependency maps are preserved in
record/cat_jet_promotion_mapping.json. Portable replays retain all exact
mathematical outputs; execution path/timing hashes are reported separately.
Each component keeps its independently reviewed scope; diagnostics in the
author handoff are not promoted as further literal-U cases.
