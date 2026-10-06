# Independent audit: actual-model finite spectral-pivot certificates

Date: 2026-10-06. Review scope: the frozen external candidate package `bgs_spectral_pivot_tests`, with canonical BGS read-only at `41a2788ef21e787e983e88a8b58470d104013740`.

## Normalized claim and verdict

**Primary verdict: computationally verified only in the stated range.** More specifically, **implementation and finite assertion independently verified for N = 21, 35, 49, 63**.

For each of these four dimensions, the actual unchanged Hermitian generator A_N has N distinct eigenvalues. In decreasing eigenvalue order, all N leading principal minors of the actual cat matrix M_N in an orthonormal A_N eigenbasis are nonzero. The author certificate replays exactly, and a separately written checker independently validates all **168 root intervals and 168 nonzero leading pivots**. This is a finite computer-assisted result, not a uniform statement.

For N = 7, the actual generator is exactly (9/10)I. The exact identities G^3 = -7 tr(G) I and tr(G)^2 = -7, where G = sqrt(7) M_7, were independently verified by integer phase histograms. Consequently U_7(t) is never simple, for any real t. The separate characteristic-zero multiplicity argument below gives multiplicities (3,2,2) and exact complex commutant dimension 17 for G, M_7, and every U_7(t).

**Spectral consequence and named dependency:** the four finite certificates, combined with the maintained Section 4 large-imaginary-time argument and the registered Lindemann–Weierstrass theorem `EXT-POPESCU-2023` (Popescu, arXiv:2306.14352v2, Theorem 3.2), imply that U_N(t) has simple spectrum for every nonzero real algebraic t in these four dimensions, including t = 10^-80 N. The finite arithmetic does not prove the external transcendence theorem. Its registered exact-source review is inherited rather than redone here. The elementary implication from the certified leading minors to a non-identically-zero discriminant was checked below.

There is no claim about other seven-divisible dimensions, all minors, uniform gaps, a scalar full U commutant, BGS, or TRACE-005. The p-adic total-minor proof in Sections 1–3 of FM-008 is not imported to these seven-divisible dimensions; the finite certificate supplies the required hypotheses directly.

## Frozen sources

The following candidate hashes were required before execution and verified unchanged after execution:

- certify.py: `b62ff3aafe2cdaf7baf852a7cb86453f918abc848f7c3012c2629bc58a24125d`
- PROOF_CONTRACT.md: `9a20545833e38b914922cdb545697fc3b1999e47dcb4adddb15ef03eacc6b5cd`
- manifest.json: `edb2b256600f59e4a8b6dc5595c605ce373122aa2ad5d1477712a99eaddea760`
- n7_exact.py: `15f274ad1ac38dc2abb841c51da2109d273bad7009914fe30d29327a61f36059`

The full before/after source hashes are in `run_receipt.json`. Canonical mathematical definitions were checked in:

1. `mathematics/frozen_kick_rank_boundary.md`, Section 1: diagonal, off-diagonal bonds, cuts, path decomposition.
2. `mathematics/fixed_model_symmetry_theorem.md`, Section 1: raw modular Weyl convention and cat kernel.
3. `mathematics/frozen_algebraic_spectral_simplicity.md`, Sections 3–4: the boundary of the non-seven-divisible total-minor proof, and the general sufficient spectral argument.
4. `literature/external_dependencies.json`, entry `EXT-POPESCU-2023`: the inherited external input and its exact intended use.
5. `supplement/fixed_map/algebraic-return/exact_coefficients.py`: independent canonical Fourier-symbol assembly used in the exact model-binding control.

Canonical HEAD and the empty Git status were checked before and after the bounded final run. No canonical source or claim status was edited.

## Dependency graph

Actual raw-Weyl model → exact seven-path decomposition → Hermitian Jacobi blocks → rigorous trigonometric coefficient enclosures → certified ordered roots → actual eigenvector enclosures → interval spectral-basis G matrix → nonzero no-permutation pivots → nonzero leading principal M minors.

For the stated spectral consequence only:

simple real algebraic A spectrum + nonzero leading M minors → separated large-imaginary-time eigenvalue scales → discriminant not identically zero → algebraic-coefficient exponential polynomial with distinct collected algebraic frequencies → registered Lindemann–Weierstrass input → simple U_N(t) at nonzero algebraic t.

The exact N7 phase-histogram computation is a separate branch, independent of any transcendence input.

## Obligation matrix

| Obligation | Status | Decisive check |
|---|---|---|
| Actual model, raw convention, centering | Passed | Exact group-ring Fourier/chain equality for all matrix entries at N=7,21,35,49,63 |
| Exact cut count and complete chain coverage | Passed | Exact modular criterion, seven disjoint paths, independent full vertex-list matching |
| Outward real arithmetic, including negative division | Passed | Static endpoint analysis and 4,356 exhaustive small-grid interval pairs |
| Machin pi and parity of alternating remainder | Passed | Exact rational parity analysis; independently computed tighter pi bracket lies inside it |
| Taylor tail and rounding | Passed | K=69, degree 138/139, absolute argument <4, one-unit tail expansion; independent Horner enclosures inside all 336 author trig intervals |
| Sturm count orientation and root association | Passed | All author endpoint counts independently checked via LDL congruence/inertia |
| Strict global root order and no missing roots | Passed | 168 complete chain/root labels, integer or exact-rational strict separation |
| Gauge orientation | Passed | Exact rational identities conj(eta^j) conj(eta) eta^(j+1)=1 |
| Eigenvector recurrence | Passed | Recurrence proof and independently reversed endpoint normalization |
| Raw G replacing M | Passed | G=sqrt(N)M; every order-k minor differs by nonzero scalar N^(k/2) |
| Unnormalised vectors | Passed | Diagonal congruence relation, detailed below |
| Complex pivots and elimination | Passed | Rectangle exclusion, strictly positive square-sum lower bound, no permutations; all 168 independently recomputed pivots exclude zero |
| Disabled assertions | Passed | Both author certificate programs reject Python -O |
| Reproducibility and source binding | Passed | All mathematical JSON fields identical in replay; all tracked inputs unchanged |
| N7 genuine exception | Passed | 49 cubic-entry identities plus trace-square identity by independent phase histograms |
| N7 characteristic-zero multiplicities and commutant | Passed | Square-free cubic plus exact trace forces (3,2,2), hence dimension 17 |
| Large-imaginary-time sufficient implication | Passed | Adjacent dominant characteristic coefficients and disjoint scaled Rouché discs |
| External Lindemann–Weierstrass theorem | Conditional / inherited | Exact registered dependency, not newly source-reviewed by this audit |
| All seven-divisible N, quantitative gaps, BGS | Out of scope | No such inference supported |

## Static mathematical and implementation audit

### Real intervals, pi, and trigonometry

An interval endpoint pair represents its full closed real interval. Addition and negation are exact. Products take all four endpoint products and round lower down and upper up. On a denominator interval not containing zero, a real quotient attains its extrema among endpoint quotients; Python floor division and ceil(a/b) = -floor(-a/b) work for negative denominators as well. Squaring uses zero as lower endpoint when the interval crosses zero. Every source run uses integer endpoints and rational coefficients; no floating acceptance path was found.

In atan_recip, after k terms the next term has sign (-1)^k. The returned lower/upper pairing has this parity exactly. Machin's identity then gives a rigorous pi interval. Reduction of grid arguments to (-pi,pi] bounds their absolute value by pi < 4. The cosine truncation has Lagrange error at most 4^(2K+1)/(2K+1)!, and the sine error is smaller because its ratio to that bound is 4/(2K+2) < 1 at the actual K=69. The final one-dyadic-unit expansion covers these errors. Intermediate interval evaluation also covers pi and all rounding uncertainty.

### Sturm roots

At a real q with all leading characteristic determinants nonzero, the sign variations in p_0=1, p_j=det(J_j-qI) equal the negative inertia of J-qI and hence the number of eigenvalues below q. The source counts this orientation correctly. An uncertain intermediate determinant is rejected rather than assigned a sign. Endpoint counts k and k+1 isolate precisely one root. The bisection updates preserve the relevant bracket; the final counts are explicitly rechecked. The independent verifier uses LDL pivots instead of the determinant recurrence and validates the author's candidate brackets without trusting the stored success flags.

The norm bound 79/50 < 2 supplies the initial source bracket. Additionally the actual source verifies counts at -2 and 2. Completeness is not inferred from separated intervals alone: every chain has all its root indices represented, and the seven vertex lists partition all coordinates. Strict separation orders these true roots globally and excludes common eigenvalues between different chains.

### Gauge, recurrence, and minors

For a chain ordered by +1, its upper bond is conj(eta)b_j with eta=(-3+4i)/5 and b_j>0. With D_j=eta^j, D* A D has upper bond b_j, because conj(eta^j) conj(eta) eta^(j+1)=1. Thus a real J eigenvector maps to an actual A eigenvector by multiplying by D, exactly as the source does. Chain wraparound causes no extra phase condition because the closing bonds are exactly zero.

The first coordinate of a nonzero eigenvector of an irreducible Jacobi matrix cannot vanish. Fixing it to 1 therefore defines the recurrence used in the source. The final row holds because the enclosed true lambda is a root of the full characteristic polynomial. Interval reuse of lambda can widen the enclosure but cannot omit its actual vector. The independent checker instead fixes the last coordinate to 1 and runs the recurrence backwards.

Let V=QR where Q is an orthonormal eigenbasis in certified order and R is an invertible diagonal matrix. Then H=V*GV=R*(Q*GQ)R, and for every leading index set I,

det(H_I)=conj(det R_I) det R_I det((Q*GQ)_I).

The factor is nonzero. Since G=sqrt(N)M, these tests are exactly the required nonvanishing tests for M. If one interprets an unnormalised eigenbasis using V^-1GV instead, its leading minors differ from H's by the nonzero diagonal Gram factors as well. There is no conflation of a general congruence with a similarity here.

For each complex pivot rectangle, excluding zero in either its real or imaginary interval is sufficient to exclude the complex origin. Complex division also checks a strictly positive lower endpoint for Re(p)^2+Im(p)^2. If this lower bound rounds to zero the code refuses the division, even when the rectangle itself excludes zero. Hence no uncertain pivot is accepted. No row or column permutation occurs. Exact elimination therefore makes the leading order-k determinant equal the product of the first k exact pivots. Every interval update encloses that exact elimination; dependency overestimation cannot create a false zero exclusion.

### Large imaginary time and fixed algebraic time

For a_1>...>a_N, the largest r-subset sum is uniquely a_1+...+a_r, whether or not other subset sums coincide. Thus the leading term of the rth characteristic coefficient is b_r exp(s sum_{j<=r} a_j). On the scale z=exp(sa_j)w, exactly the adjacent coefficient terms r=j-1,j have maximal exponential order. After scaling, their nonzero root is w=b_j/b_{j-1}; all other terms are exponentially smaller on a small circle around that nonzero root. Rouché counts one root, including multiplicity, in each corresponding disc for sufficiently large s. Distinct a_j make these N discs disjoint. The discriminant is consequently not identically zero.

A_N and M_N have algebraic entries. Simple A spectral projectors are algebraic, so the discriminant is a finite exponential polynomial with algebraic coefficients and real algebraic frequencies. Equal frequencies must first be collected. At nonzero algebraic t, the remaining exponents it omega are distinct algebraic numbers. The registered Lindemann–Weierstrass theorem then prevents a nonzero collected polynomial from vanishing. This mapping uses no special assumption 7 does not divide N beyond the hypotheses already certified for these four cases.

## Independent execution and controls

The checker `independent_check.py` imports no author certificate code. Its differences are substantive:

- Decimal intervals with denominator 10^260, rather than denominator 2^512.
- pi/4 = atan(1/2)+atan(1/3), with exact rational alternating bounds, rather than Machin's formula.
- Horner evaluation of degree-204 cosine and degree-205 sine, rather than Taylor-term recurrence.
- LDL inertia at supplied root endpoints, rather than Sturm determinant recurrence or the author's bisection decisions.
- Last-coordinate-normalized, backwards eigenvectors, rather than first-coordinate-normalized forward eigenvectors.
- Chirp–Fourier–chirp construction of G, rather than direct use of the quadratic-kernel residue.
- Direct Schur updates (H_ik H_kj)/H_kk rather than precomputing H_ik/H_kk.

The source root intervals are candidate witnesses; their association and count are independently verified. Source pivots are never used by this checker. Mathematical independence is not claimed for the underlying standard facts (Jacobi recurrences, inertia, and Gaussian elimination), and this remains an internal computational review rather than peer review or a formal proof.

An exploratory version at 180 decimal digits refused an uncertain LDL sign because high-degree Horner coefficient rounding produced too wide an enclosure. No success was claimed from that run. The final 260-digit version passes all endpoints and pivots. The author's 512-bit recurrence evaluation does not share that particular width issue.

Reviewer controls cover 4,356 exhaustive real interval pairs at only four bits, including 1,980 nonzero denominator pairs; 600 deterministic complex boxes (351 accepted and checked on 81 corner/center combinations, 249 safely refused); all 336 production trigonometric component intervals against tighter independently computed bounds; eight exact Sturm counts; nine exact rational gauge identities; and two assertion-disabling refusals. These supplement, rather than replace, the mathematical enclosure audit.

`exact_model_binding.py` checks full matrices in Q(i)[z]/(z^N-1) by comparing the maintained Fourier symbol under the raw Weyl convention with a separately assembled diagonal and bonds. It covers 8,085 matrix entries across N=7,21,35,49,63, including the exact A_7=(9/10)I exception. Group-ring equality is stronger than equality after imposing the primitive cyclotomic relation; no numerical tolerance is used.

The N7 independent checker counts the phases of all length-three matrix walks. For each of 49 entries, the polynomial representing G^3+7tr(G)I has all seven coefficients equal, hence is a multiple of Phi_7. The analogous trace-square polynomial has the same property. This avoids the author's quotient-ring multiplication implementation entirely.

### Separate N7 characteristic-zero multiplicity certificate

Put T=tr(G). The independently checked identities give T²=−7, so T is nonzero and T³=−7T. Thus H=G/T satisfies H³=I and tr(H)=1. The polynomial X³−1 has three distinct complex roots, so H is diagonalizable. Fix a primitive cube root omega. If the multiplicities of 1, omega, omega² are m0,m1,m2, then

m0+m1+m2=7, and m0+m1 omega+m2 omega²=1.

Using omega²=−1−omega and the rational linear independence of 1,omega gives m0−m2=1 and m1−m2=0. Therefore the multiplicities are exactly (3,2,2). A diagonalizable matrix with these eigenspace dimensions has complex commutant isomorphic to Mat_3(C) direct sum Mat_2(C) direct sum Mat_2(C), of dimension 9+4+4=17.

Multiplying a matrix by a nonzero scalar does not change its commutant or eigenvalue multiplicities. Hence the same exact dimension and multiplicities hold for M_7=G/sqrt(7) and U_7(t)=exp(9it/10)G/sqrt(7), for every real t. No sign for T/sqrt(7) is chosen or needed. This is a characteristic-zero deduction from the verified raw phase convention, **not** a lifting of a residue-field commutant calculation. The separate `n7_multiplicity_check.py` rechecks the raw identities, enumerates the exact nonnegative integer constraints, and records `n7_multiplicity.json`.

## Reproduction, artifacts, and limits

Run from this review directory:

    python run_review.py

This reruns both frozen author certificates, independent full verification, adversarial controls, and exact model binding, then compares replayed mathematical fields and input hashes. Each subprocess has a 120-second CPU cap, 1 GiB address-space cap, and 180-second wall timeout. Processes run sequentially. The production proof checks use Python 3.12.14 standard-library integer/Fraction arithmetic; there is no package installation, eigensolver, floating trigonometry, random acceptance, or network call.

- `run_receipt.json`: exact commands, runtimes, before/after hashes, resource limits, canonical status.
- `replay_certificates/N*.json`: author replay; all mathematical fields identical to the frozen originals.
- `independent_N*.json`: independent endpoint checks and complete pivot enclosures, with denominator 10^260.
- `independent_n7.json`, `replay_n7.json`: separate exact N7 identity evidence.
- `n7_multiplicity.json`: characteristic-zero multiplicities (3,2,2) and complex commutant dimension 17.
- `adversarial_controls.json`, `exact_model_binding.json`: reviewer controls and exact convention checks.
- `manifest.json`: source-bound finite-audit manifest, including artifact hashes.

Residual trust is ordinary Python integer/Fraction semantics, operating-system execution, the elementary mathematical reductions stated above, and the separately registered external transcendence input for the fixed-algebraic-time consequence. Neither certification program is Lean/formally verified. Tests of other dimensions were not performed or claimed.

## Strongest safe statement and remaining work

The four finite actual-model pivot assertions and the N7 exception are accepted within this computational trust boundary. With the named inherited LW input, the simple-U conclusion is valid in exactly the four certified dimensions. No scientific correction to the frozen implementation or its proof contract is required by this audit.

The cheapest next integration check is to preserve these source hashes and finite scope, attach this review with the computational evidence, and ensure any canonical claim explicitly separates the finite assertion from the external LW consequence. Extending dimensions or proving a uniform seven-divisible theorem is separate research, not a consequence of this review.

## Publication scope

Original bytes and exact source hashes remain bound by
record/spectral_extension_promotion_mapping.json. Execution-machine paths
in this curated copy are source roles, not installed dependencies. Portable
replay packaging does not strengthen the independent mathematical verdict.

N7 was already published under FM-024. This overlay promotes only the four
finite spectral-pivot cases; it does not republish N7 as a new result.
