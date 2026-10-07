# Source-bound accepted review: residual25_affine_dictionary.md

This is the historical independent internal review, with its original scope
and verdict. Its frozen SHA256 is `ae99eba98e71959d8c35367ea70fd1380f6d2294c22f5234c1993d2bb9d22e10`.
The [maintained proof](../mathematics/residual25_affine_dictionary.md) makes only the status, navigation,
and disclosed nonblocking exposition changes recorded in the promotion map.
Original outside paths and commands in the report identify historical
artifacts; their exact bytes are recoverable through the
[archive map](../evidence/intermediate_old_layers_20261007/input_map.json).
The [portable replay](../computations/verification/intermediate_old_layers_certificates.py)
replaces historical execution paths and retains all arithmetic checks under
Python optimization. This is independent internal review, not external peer
review or formal certification.

# Independent audit: residual-25 affine second-order splitting

## Claim and verdict

**Primary verdict: proved as written, relative to the explicitly inherited accepted cat/oldform inputs and the separately audited general return formula. No correction found.**

For every integer j ≥ 2, set h = 5^j, n = 5^(2j+2), N = 7n. In the complete oldform spectral subspace H7 ⊗ J_j H25, each of the 24 seven-dimensional intermediate product-cat eigenspaces has zero first-order compression and a simple second-order Hermitian phase matrix. The three deepest blocks of dimensions 3,2,2 are outside this continuation and retain their prior separate theorem. This is local eigenjet splitting, not a conclusion about simplicity of the full propagator at its fixed coupling, gap size, or BGS universality.

Audited source: `frozen/residual25_affine_dictionary.md`, SHA256 `afc110371271dcb24a52c5059184ee5ebdd9db8b5a127bb10f13d414819bf421`. Its executable/manifest and the general-return source were frozen without editing. No canonical project file or previously accepted packet was changed.

The audit independently establishes the residual-25 bridge, rather than inferring a uniform theorem from the author's two finite-characteristic controls. The general-return auditor has separately reported acceptance of the frozen source `intermediate_return_operator.md`, SHA256 `3f42c4f41f448c221e4dc92495a11caa3b2cd661168f8cd888abd35971ed1932`; that source's scope ends before residual cat-character compression.

## Dependency closure and obligation matrix

| Obligation | Disposition | Evidence |
|---|---|---|
| Actual 32-mode coefficients and raw CRT Weyl convention | Passed, inherited coefficients independently reduced | Frozen coefficient source plus derivation below |
| Complete oldform eigenspaces and exact first-order vanishing | Accepted inherited input | Oldform embedding/compression and simple cat spectrum |
| General rotated-return formula, conjugated initial factors, weighted inverse | Separately audited input | Frozen general-return source, equations (6), (7), (14) |
| Primitive scalar regime j ≥ 2 | Passed uniformly | Residual order 30 divides L = 6·5^(j−1) |
| Entrywise normalization and orbit-line residue | Passed uniformly | Five-cycle holonomy and exact inverse numerator |
| Initial translation on the same line | Passed uniformly | Exact norm identity and polar kernel |
| Actual upper/upper filter, including nonprimitive j = 2 | Passed uniformly | Gaussian valuations and shorter-period five-cycle bound |
| Residual circle/tame labels and integral eigenbasis | Passed uniformly | Exact coherent phases and circlewise unit Fourier inverse |
| Fixed finite matrices and squarefreeness | Independently verified | Different field and direct 42-position projectors, all six roots |
| Lift to the 24 characteristic-zero second-order blocks | Passed uniformly | Integral matrix with squarefree residue |

No literature theorem is introduced by this continuation. Previously accepted cat, oldform and CRT inputs are retained as dependencies, not silently re-proved by finite checks here.

## 1. Raw normalization and return dictionary

Write A = 4000^(-1) Σ_v d_v T7(v) ⊗ T_n(v), with the unchanged Gaussian coefficients. For a primitive returning pair, the general-return formula gives the common second-order contribution

    i d_v d_u / (4000²) · Pλ [C7,a ⊗ D_a (I − X_(u,a))^(-1)] Pλ,

apart from the k = 0 finite subtraction when that class contains zero. Here C7,a = T7(v)T7(S^a u), D_a = θ_a T25(c_a), c_a = (v + S^a u)/h modulo 25, and X_(u,a) is the residual-cat conjugate of the normalized return. The factor i follows from i/(2R) times the exact weighted geometric numerator 2R. No factor R, 5, or residual orbit length may be discarded or inserted.

For primitive u, L = 6·5^(j−1) is divisible by 30. Since M25^30 = I and every occupied residual μ has μ^30 = 1, M25^L = I and μ^(−L) = 1. Thus X_u = z_u T25(b_u), with b_u = (S^L − I)u/h. Modulo 5, b_u = 2Ju, where J = [[0,2],[1,0]]. It is nonzero. On the coherent labels F5², X_u permutes each affine line parallel to Ju in a five-cycle.

Put δ* = 1 − q^(5h), with valuation a* = 1/(4·5^j). The monomial holonomy η on such a cycle is z_u^5 times a fifth-root phase. Since z_u has exact order 5^(j+2), η has exact order 5^(j+1). More precisely, for the corresponding global coherent label x = u + hy,

    η = q^(−ω(x,S^(5L)x)/2).

The off-diagonal coefficient of S^(5L), divided by 5h, is 2 modulo 5. Hence the exponent divided by 5h reduces to Q(u), and

    δ* / (1 − η) → Q(u)^(-1).

The inverse on a five-cycle is exactly (1 − η)^(-1)(I + X + X² + X³ + X⁴). Its five permutation supports are disjoint, so each numerator entry is a unit and the residue is the unnormalized line sum. This explains both the scale and the absence of a 1/5 factor.

After conjugation by M25^a, the line direction becomes S^a Ju = J S^a u, which is −Jv modulo 5. Thus the line indicator is exactly R_v(x,y) = 1 if x − y lies in span(Jv), zero otherwise.

### Initial-factor cancellation

For each surviving pair, the INTEGER norms are equal. Since S preserves Q and S^a u = −v + h c_a,

    Q(v) = Q(−v + h c_a) = Q(v) − h B(v,c_a) + h² Q(c_a),

where B(v,c) = −2v_1 c_1 + 4v_2 c_2. Therefore B(v,c_a) = h Q(c_a), so B(v,c_a) = 0 modulo 5. Its one-dimensional kernel is span(Jv), because v is primitive and Q(v) is a unit. Consequently c_a lies in the same line; multiplication by its reduced translation preserves the complete line sum. The phase θ_a has 5-power order and reduces to one.

The seven-dimensional operator remains the entire raw product T7(v)T7(S^a u). S has order 3 modulo 7, while the unique mod-5 return specifies a modulo 6. Consequently no higher lift of a changes C7,a. The independent code builds this raw product from the Weyl phase ω(v,S^a u)/2, not by deleting the cocycle.

## 2. Actual coefficient filter and all 17 pairs

Let r4(b) be 4,2,−1,−2,−1 at |b| = 0,1,6,7,8. The upper coefficients are r4(b)(−3−4i), units at i → 2. The lower coefficients are r4(b)(−3+4i), of valuation 2 because −3+4i = (1+2i)² and its conjugate is a unit. Every diagonal coefficient has positive valuation; specifically all have valuation 1 except the b = ±7 coefficients, which have valuation 2. Thus every primitive pair other than upper/upper has positive residual coefficient valuation after the common entrywise normalization.

The five possible upper norms are −1, 1, 71, 97, 127, with distinct residues 24,1,21,22,2 modulo 25. For h ≥ 25, congruent upper norms therefore mean equal integer norms. Exactly 17 ordered pairs survive. The following complete table uses v = (1,b), u = (1,d), and coefficient 2 d_v d_u / Q(v) modulo 5.

| b | d | a mod 6 | coefficient |
|---:|---:|---:|---:|
| 0 | 0 | 3 | 3 |
| 1 | 1 | 3 | 3 |
| 1 | −1 | 1 | 3 |
| −1 | 1 | 5 | 3 |
| −1 | −1 | 3 | 3 |
| 6 | 6 | 3 | 2 |
| 6 | −6 | 1 | 2 |
| −6 | 6 | 5 | 2 |
| −6 | −6 | 3 | 2 |
| 7 | 7 | 3 | 4 |
| 7 | −7 | 2 | 4 |
| −7 | 7 | 4 | 4 |
| −7 | −7 | 3 | 4 |
| 8 | 8 | 3 | 1 |
| 8 | −8 | 4 | 1 |
| −8 | 8 | 2 | 1 |
| −8 | −8 | 3 | 1 |

### Nonprimitive terms, explicitly including j = 2

The only nonprimitive modes are u = (0,±5) = 5u0, and their coefficients both have valuation 1. Their correct period is L′ = 6·5^(j−2). At j = 2 one MUST retain both M25^6 and μ^(−6) in X′; setting them to one would be incorrect. This does not invalidate the proposed bound.

Modulo 5, S^L′ = I and b′ = (S^L′ − I)u/h = 2Ju0. Therefore the coherent permutation of X′ still consists of five-cycles, including j = 2. After five steps μ^(−5L′) = 1, because 30 divides 5L′. For x = u + hy = 5(u0 + 5^(j−1)y), the cycle holonomy is

    η′ = q^(−ω(x,S^(5L′)x)/2).

The off-diagonal coefficient of S^(5L′) has valuation j, and x has content exactly 5. Its exponent has valuation j+2, so η′ has exact order 5^j. Every nonzero inverse entry therefore has valuation −1/(4·5^(j−1)) = −5a*. The full normalized term has valuation at least

    1 + 1 + a* − 5a* = 2 − 4a* = 2 − 5^(−j) > 0.

At j = 2 this is 49/25, so the exceptional non-scalar residual cat case is harmless after the actual coefficient filter. Mixed primitive/nonprimitive contents cannot return modulo h. The k = 0 subtraction has no remaining 1/R denominator, is integral after multiplying by 4000², and vanishes after the additional δ* factor.

## 3. Residual-25 labels and the integral circlewise eigenbasis

Use unnormalized coherent vectors φ_y = T25(y)ψ, with ψ the indicator of 5Z/25Z. This differs from the orthonormal coherent basis by one common scalar only. The coherent coordinate lattice, not the standard position lattice with its 1/5 Fourier inverse, is the lattice used in the reduction.

Exact raw arithmetic in Z[q25]/Φ25 verifies M25 φ_y = θ_y φ_(Sy mod 5), φ_y*φ_z = 5·1_(y=z), and the Weyl phase formula. Every θ_y has 5-power order. The origin vector is fixed. The other 24 labels split into four six-cycles O_c indexed by Q(y) = c in F5×.

For representatives in {0,…,4}², writing r = Sy mod 5 gives θ_y = q25^(−ω(r,Sy)/2). The exact cycle holonomy is q25^(5c) = ζ5^c. Accordingly its six eigenvalues are precisely

    μ_(c,t) = ζ5^c ξ^t,  t = 0,…,5,

where ξ is any primitive sixth root. This proves that the four circle labels stay distinct in characteristic zero, even though their wild factors all reduce to one.

On one cycle, set p_0 = 1 and p_k = θ_0⋯θ_(k−1). An eigenvector with eigenvalue μ has kth coordinate p_k μ^(−k). Its dual has kth coordinate (1/6) p_k^(-1) μ^k. All p_k and μ are units, and 6 is a unit at 5. Equivalently, the determinant is a unit diagonal factor times a tame six-point Fourier determinant whose pairwise root differences are units. Thus this circlewise eigenbasis and its inverse are integral with unit determinant. The direct sum of the four such bases and the origin vector remains integral, regardless of eigenvalue coalescence BETWEEN circles.

Normalize the seven-factor cat as H7 = G7/Tr(G7), with cubic labels z_i and multiplicities 3,2,2. Its projectors are integral at 5 (denominator 3 and a unit trace normalization). The characteristic-zero eigenbasis can be chosen to reduce to an integral finite-field eigenbasis.

For a fixed c and tame product label t, the full eigenvalue, after dividing by the seven-factor scalar trace normalization, is ζ5^c ξ^t. Its seven coordinates use residual eigenvalues ζ5^c ξ^t/z_i from this SAME circle. Their reductions are exactly γ_i = ξ^t/z_i. Hence the reduced residual matrix element is

    (1/6) Σ_(kx,ky=0)^5 γ_i^kx γ_j^(−ky) R_v(y_kx,y_ky).

This is the proposed dictionary including its dual denominator, norm label, tame label and initial translation. It never uses a global denominator-30 projector. Tangent intersections are counted once by the indicator; no identity-plus-reflection shortcut is used.

## 4. Independent finite certificate and replay

`independent_residue.py` imports neither the author's field code nor its residue implementation. It constructs the distinct field F5[x]/(x^6+x+2), verifies irreducibility and a complete primitive-element multiplicative cycle, and uses:

1. the raw seven-position quadratic cat kernel and Weyl cocycle;
2. the 42-dimensional product of seven position coordinates and the six-point residual circle;
3. the full order-six projector E_t = (1/6) Σ_(k=0)^5 (ξ^(−t) H7⊗P)^k;
4. a rank-seven image basis and an independently computed left coordinate inverse;
5. characteristic polynomials by division-free subset determinant expansion, rather than interpolation or Newton division in characteristic five;
6. an exact polynomial derivative gcd.

It verifies projector idempotence and rank seven, then reconstructs all 144 matrices: six primitive seventh roots × four norms × six tame labels. Every characteristic polynomial is squarefree. For the initial seventh root, all 24 characteristic polynomials equal the author's polynomials under an explicit field embedding. In the independent field, the author's degree-six generator maps to 1770, w maps to 1144, and ξ maps to 8843. The independent field's primitive element is encoded as 5.

Coverage of seventh roots is both explicit and structural: ord_7(5) = 6, so the six primitive seventh roots form one Frobenius orbit. The tame labels are all checked, so their Frobenius permutation causes no omission.

`raw_coherent_check.py` separately verifies the exact residual-25 raw kernel/coherent dictionary over Q(ζ25), not a non-5 prime-field surrogate. It checks all 625 raw-kernel/coherent entries, the full coherent Gram matrix, Weyl generators, origin and all four circle holonomies. It also checks the primitive/nonprimitive holonomy coefficients and the 17 initial translations for j = 2,…,6. Those last checks are bounded controls; the all-j arguments are sections 1–3 above.

The author's original script was replayed in an owned replay directory. Every JSON field other than elapsed time matches its frozen output. Every source and output hash listed by its manifest matches the inspected file.

Reproduction commands, with assertions enabled:

    python /workspace/shared/bgs_residual25_affine_review/independent_residue.py
    python /workspace/shared/bgs_residual25_affine_review/raw_coherent_check.py
    python /workspace/shared/bgs_residual25_affine_review/replay/residual25_affine_residue.py

All arithmetic is exact. No randomized sample, numerical eigenvalue tolerance, heuristic extrapolation, or external computation library for characteristic polynomials is used.

## 5. Lift and exact stopping boundary

After the actual coefficient filter and the circlewise integral basis change, each matrix 4000²δ* H2 is integral and reduces to one of the 24 squarefree finite matrices. Its discriminant reduces to a nonzero field element, so the characteristic-zero discriminant is nonzero. Removing the nonzero scalar normalization preserves eigenvalue multiplicities. This proves the stated second-order simplicity for every j ≥ 2.

No unresolved identity remains in this continuation. Its inherited dependencies remain explicit. The new theorem covers exactly residual dimension 25, even depth e = 2j+2 ≥ 6, and the 24 intermediate size-seven blocks. Larger residual powers, full U simplicity at a prescribed nonzero coupling, and BGS statistics are not asserted.
