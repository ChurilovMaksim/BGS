# Independent audit: uniform cat multiplicities on 7·5^e

Date: 2026-10-06. Canonical BGS was read-only at commit `6f3874e5fb1d5b31b5825e2ff273e8c643e0046a`; its Git status was clean before and after the controls.

## Normalized claim and verdict

**Primary verdict: proved as written.** This verdict concerns the stated spectral conclusion, for every integer **e≥1**, in the unchanged raw quadratic-kernel convention:

- M_(5^e) has simple complex spectrum.
- Writing n=5^e, every M_(7n) eigenspace has dimension at most 7.
- For odd e, its eigenspace dimensions are n−2 copies of 7 and one each of 4,5,5.
- For even e, they are n−1 copies of 7 and one each of 3,2,2.

There is one local wording correction required before promoting the proof: the phrase “v5(S^(6j)−I)=1+v5(j) entrywise” at target line 12 must not assert equality for every individual entry. Already j=1 has entry valuations (2,1,1,2). The exact sufficient statement is

    S^(6j)−I = 5^(1+v5(j)) B_j, with B_j integral and invertible modulo 5.

Equivalently, use the minimum valuation of the matrix entries, together with invertibility of its leading matrix. This correction changes neither the theorem nor its hypotheses; the explicit binomial argument below supplies the stated sufficient property.

No compressed kick is shown simple. No simplicity of the kicked U_N, quantitative gap, BGS, or full complex U_N-commutant conclusion is asserted.

## Frozen source binding

The reviewed target is `/workspace/shared/bgs_seven_adic_resume/cat_splitting/uniform_cat_multiplicity.md`, SHA-256:

`f9d4ead9e1916f62bafd8e8db660957b5c315bb6f1eecf7dcbd2b9626d002a9c`.

The source-bound dependencies are:

1. Canonical `mathematics/fixed_model_symmetry_theorem.md`, Section 1, raw kernel and S. SHA-256 `32b2302c2567eebb75ff2231345e3336495ba8719517be6b5ce8734b416920c2`.
2. Canonical `mathematics/frozen_arithmetic_trace_rigidity.md`, “Arithmetic of the unperturbed cat map,” especially equation (2), exact raw-Weyl covariance and fixed-point trace identity. SHA-256 `e23c99caec20d8e5ed8477b5689801296d011fa0daba466c42b20707452a94b8`.
3. `/workspace/shared/bgs_spectral_pivot_independent_review/REPORT.md`, “Separate N7 characteristic-zero multiplicity certificate,” for the raw identities T²=−7 and G³=−7TI and their (3,2,2) consequence. SHA-256 `74e1d3f9c39232e474d66dc58503b13b03e61c3aadeaf43786f541ac34ce20dd`.

Only the cat-arithmetic portion of item 2 and the N7 branch of item 3 are dependencies. Their other kicked-map assertions and any Lindemann–Weierstrass input are not used. No external Weil/torus multiplicity theorem, literature leaf, finite-field-to-characteristic-zero transfer, or unverified large-dimension spectral computation is used. There is no `.mathbox` ledger in the canonical root.

All four bound hashes were unchanged before and after the exact controls. Canonical AGENTS, source-of-truth/convention files, and the relevant current claim/status entries were inspected. Existing pair-commutant and N7 results were attributed rather than treated as new conclusions of this audit.

## Dependency graph

Raw kernel → unitary primitive-root kernels and exact Weyl covariance → fixed-point trace identity and scalar return ⇢ two branches:

- S modulo 5 and invertible binomial leading matrix → exact order 6·5^(e−1) and prime-power fixed-point counts → cyclic Parseval → simple M_(5^e).
- Order 3 modulo 7 + prime-power counts → full cyclic multiplicity-square sum 49n−32.

Separately, reviewed N7 identities → primitive-root N7 multiplicities (3,2,2).

Exact raw-kernel CRT factorization + prime-power simplicity + N7 multiplicities → maximum multiplicity 7 → three-cycle occupancy table. The full square sum makes exactly one occupancy cycle partial → parity-dependent exact distribution.

Every arrow is established below using internal definitions, elementary matrix/binomial/Fourier arithmetic, or the named source-bound input. There is no circular spectral input.

## Obligation matrix

| Obligation | Status | Decisive evidence |
|---|---|---|
| Actual matrix and raw phase | Passed | Unchanged −8^−1(3x²−2xy+3y²) kernel |
| C versus S label order | Passed | C=J S J with J swapping two coordinates |
| Primitive-root variants | Passed | Raw covariance over Q(zeta); unit roots give a full Weyl basis |
| Unitarity and scalar normalization | Passed | Chirp–Fourier–chirp factorization; scalar phase has unit modulus |
| Order and invertible 5-adic leading matrix | Passed | Binomial lifting below |
| Literal equality of every entry valuation | Failed as wording | At j=1 the valuations are (2,1,1,2); replacement given above |
| Nonreturn kernel count | Passed | Determinants modulo 5 are 1,3,4,3,1 |
| Prime trace sum and cyclic Parseval | Passed | Exact sum Rn; nonnegative integer multiplicities force simplicity |
| e=1 endpoint | Passed | Empty valuation sum, R=6, trace-square sum 30 |
| CRT phases and normalization | Passed | Explicit primitive powers n^−1 mod 7 and 7^−1 mod n |
| N7 multiplicities for every primitive root | Passed | Galois extension; six independent exact quotient-ring checks |
| Full trace sum | Passed | Exact R(49n−32) calculation |
| Partial occupancy deficit | Passed | Exactly 32 for either partial type, 0 otherwise |
| Exact parity counts | Passed | n mod 3 fixes unique partial occupancy |
| Compression/U/BGS conclusions | Out of scope | No such consequence follows here |

## Reconstructed uniform proof

### 1. Primitive roots, covariance, and phase normalization

For odd m and any unit a modulo m define

    M_(m,a)(x,y)=m^(−1/2) exp(2πi a Q_m(x,y)/m),
    Q_m(x,y)=−8^−1(3x²−2xy+3y²) modulo m.

The xy coefficient is 4^−1, a unit. Thus this is a unitary diagonal chirp times a Fourier matrix with a unit frequency permutation times a unitary diagonal chirp. It is unitary for every such a.

Use Weyl matrices with the same primitive root power a. The canonical intertwining relation can first be written for the unnormalized G=sqrt(m)M, whose entries and Weyl entries lie in Q(zeta_m). The automorphism zeta_m↦zeta_m^a preserves the intertwining relation. Scalar normalization does not affect conjugation. These Weyl matrices still form a full matrix-algebra basis, since a is a unit. Hence the exact covariance and its fixed-point trace identity apply unchanged to M_(m,a).

The canonical trace proof uses C=[[3,2],[4,3]], whereas the target uses S=[[3,4],[2,3]]. For J=[[0,1],[1,0]], C=JSJ, so their fixed-point counts and orders agree over every modulus.

If S^R=I modulo m, conjugation by M_(m,a)^R fixes the full Weyl basis. It therefore fixes every matrix, so M_(m,a)^R=cI. Unitarity gives |c|=1. Choose a scalar phase b with b^R=c^−1. Then (bM_(m,a))^R=I, and every eigenvalue lies in the Rth roots of unity. This changes no eigenspace or absolute trace. Conversely a scalar power forces S^k=I by the faithful Weyl label action. Thus the scalar-return order is exactly the classical order, and choosing the phase never assumes an unproved metaplectic normalization.

### 2. Order and counts modulo 5^e

Direct arithmetic gives S order 6 modulo 5, and det(S^r−I) modulo 5 for r=1,...,5 equal to 1,3,4,3,1. Thus every nonmultiple of 6 has an invertible difference matrix modulo 5^e.

Put H=(S^6−I)/5. Its reduction is [[0,4],[2,0]], with determinant 2 modulo 5. If r≥1 and B is an integral matrix, then

    (I+5^r B)^5 = I+5^(r+1)(B+5D)

for an integral D: every nonleading binomial term has at least one additional factor of 5 after division by 5^(r+1). Repeating this shows

    S^(6·5^s) = I+5^(s+1) H_s,  H_s≡H modulo 5.

For j=5^s u with 5∤u, a further binomial expansion gives

    S^(6j)−I = 5^(s+1) B_j,  B_j≡uH modulo 5.

Thus B_j is invertible modulo 5 and modulo every power of 5. For 0<j<5^(e−1), the kernel of S^(6j)−I modulo 5^e has size 5^(2(s+1)). Together with the nonmultiple case this proves exact order R=6·5^(e−1). At k=0 the kernel size is n², n=5^e.

Write P=5^(e−1). There are 5P exponents not divisible by 6. Among 1≤j<P, precisely 4·5^(e−2−s) have valuation s for 0≤s≤e−2. Hence the target trace sum is correct. For e≥2 its last sum is n(P−1); therefore

    5P+n²+n(P−1)=Rn.

For e=1 the valuation sum is empty and the equality reads 5+25=30=6·5, so no negative-exponent counting term is used.

After the scalar normalization from Section 1, cyclic Fourier orthogonality gives sum(multiplicity²)=n. Since the multiplicities are nonnegative integers summing to n, sum m(m−1)=0, so every occupied eigenvalue has multiplicity 1. This proves prime-power simplicity uniformly, for every primitive-root version.

### 3. Exact CRT factorization and N7 root variants

Let t7=n^−1 modulo 7 and tn=7^−1 modulo n. The CRT coordinate map uses

    x=n t7 x7+7 tn xn modulo 7n,

and similarly for y. Under this coordinate permutation the raw phase satisfies

    exp(2πi Q_(7n)(x,y)/(7n))
      =exp(2πi t7 Q_7(x7,y7)/7)
       exp(2πi tn Q_n(xn,yn)/n).

Indeed Q_(7n) reduces to Q_7 and Q_n, including its modular inverse of 8, and the two cross terms of CRT idempotents vanish. Both t7 and tn are units. The positive normalization sqrt(7n)=sqrt(7)sqrt(n) then yields the exact tensor identity

    M_(7n) ≅ M_(7,t7) tensor M_(n,tn).

There is no extra scalar phase in this coordinate factorization.

For the seven-dimensional raw matrix G, the bound source gives T²=−7 and G³=−7TI, T=tr G. Apply any automorphism zeta_7↦zeta_7^t to obtain the same identities for G_t,T_t. This argument is made before introducing sqrt(7), so no extension of a Galois automorphism to a square-root convention is assumed. H_t=G_t/T_t has H_t³=I and trace 1; the square-free cubic and rational independence of 1,omega give multiplicities (3,2,2), as in the reviewed source. Consequently M_(7,t) has eigenvalues gamma_t times 1,omega,omega², with those multiplicities. The unknown common phase gamma_t is harmless.

For any proposed product eigenvalue, each of these three distinct seven-factor eigenvalues selects at most one eigenvalue of the simple n-factor. The combined dimension is therefore at most 3+2+2=7.

### 4. Full trace sum and exactly one partial orbit

S has exact order 3 modulo 7; its first two difference determinants are nonzero modulo 7. Thus the seven-primary fixed-point count is 49 for 3|k and 1 otherwise. Since 3|R, the full cat has scalar-return order R.

Let Tn denote the prime trace-square sum Rn. The exponents divisible by 6 contribute Tn−5P; those congruent to 3 modulo 6 contribute P; the other four classes contribute 4P. The full sum is

    49(Tn−5P)+49P+4P = 49Rn−192P = R(49n−32).

Scalar-normalized cyclic Parseval therefore gives the stated full multiplicity-square sum 49n−32.

Let E be the simple n-factor eigenvalue set in its Rth-root coset. Multiplication by omega partitions this ambient coset into disjoint cycles of size 3, and all possible tensor products from one cycle stay within its gamma_t-scaled copy. Distinct cycles cannot merge under this common nonzero scalar multiplication.

An occupied singleton contributes weights 3,2,2. Two occupied vertices contribute 4,5,5, with cyclic permutation depending on the omitted vertex. Three contribute 7,7,7. Each partial cycle has deficit

    7·7−(9+4+4)=32,
    7·14−(16+25+25)=32,

respectively; empty and full cycles have deficit 0. Total tensor dimension is 7n, and the full deficit is 49n−(49n−32)=32. Therefore exactly one cycle is partial, without cancellation or an unproved sign assertion.

If e is odd, n≡2 modulo 3, so that partial cycle has occupancy 2 and the full cycles account for n−2 prime eigenvalues. They yield n−2 eigenspaces of dimension 7. If e is even, the partial occupancy is 1 and the full cycles yield n−1 such eigenspaces. This gives precisely the claimed distributions.

The stated quantifier is e≥1. The separate e=0 case would be N=7 and is already covered by the reviewed N7 multiplicities, but the formula R=6·5^(e−1) is not to be used at e=0.

## Independent exact controls

Run in this review directory:

    python check_arithmetic.py

The checker imports no author implementation. It uses exact integer matrix arithmetic, integer Smith invariants for kernel sizes, direct vector enumeration for small controls, and explicit arithmetic in Q[zeta_7] for all six primitive-root versions. All checks use explicit runtime failures rather than removable Python assertions. Its successful run took approximately 1.45 seconds on this host and recorded:

- All modular powers and fixed-point trace counts through one full return for each e=1,...,7, in dimensions n=5,...,78125 and N=35,...,546875. This covers 117,186 exponents in total for each of the two modulus families.
- 72 independent brute-vector versus Smith-kernel comparisons at n=5,25 and N=35,175.
- 797,475 exact quadratic CRT phase comparisons, every matrix entry at N=35,175,875.
- 294 N7 cube-entry equalities and six trace-square identities, covering all six primitive-root powers.
- All eight subsets of an omega-cycle, including every rotation of the partial configurations.
- 96,348 raw generator-covariance phase equalities at N=5,7,25,35,125,175.
- Both first parity endpoints: N=35 gives three 7-blocks plus 4,5,5 and square sum 213; N=175 gives twenty-four 7-blocks plus 3,2,2 and square sum 1193.

The bounded controls supplement the uniform argument above; no tested range is being extrapolated. `arithmetic_checks.json` records commands' mathematical results, environment version, source hashes, canonical status, complete depth summaries, and exact scope. `manifest.json` hashes this report, the checker, and its output.

## Remaining gap and strongest safe statement

There is no remaining implication gap in this uniform cat-multiplicity theorem. Replace the misleading “entrywise” valuation wording, retain the precise primitive-root/phase explanations and source boundary, and the candidate is suitable for source-bound integration.

The first-order kick-compression matrices have size at most 7, but their actual coefficients and spectra still require a separate proof. This audit does not turn bounded compression size into a simple compressed spectrum or a simple kicked spectrum.
