# Independent audit: actual cat-eigenspace first-order splitting

## Claim and verdict

**Primary verdict: proved as written**, in exactly the finite scope N=35 and N=175, with the explicitly inherited registered Lindemann–Weierstrass input for the algebraic-time conclusion.

For each of these two dimensions, every nonzero eigenspace of the actual prescribed M_N has simple Hermitian compression of A_N. Therefore the actual exp(it A_N)M_N has simple spectrum at every nonzero real algebraic t, including t=10^(-80)N. At N=7 the first-order condition fails exactly. This is an exact computer-assisted finite theorem, not a uniform-family theorem, quantitative gap estimate, simple-power theorem, or BGS result.

The reviewed candidate is `frozen/first_order_cat_split.md`, SHA-256 `afdb9f47bc1d5823b922d8caaa1fc45d71d0b951c4adb6da7b07ca83bd1b2e17`. The complete supplied bundle is frozen locally and verified against its supplied manifest. `source_manifest.json` pins the canonical revision and source snapshots; canonical BGS and the author's files were not changed. This is a fresh independent internal review, not an external referee assessment or a Lean formalization. The independent computation imports none of the candidate code.

## Dependency graph

Prescribed raw Fourier symbol and kernel -> exact Hermitian A and unitary M -> exact raw Weyl covariance and finite symplectic order -> G^R=cI -> integral spectral idempotents and direct-summand lattices -> complete finite-field compression certificates -> simple characteristic-zero compressions -> distinct first-order eigenvalue slopes -> non-identically-zero discriminant -> algebraic-coefficient exponential polynomial -> registered Lindemann–Weierstrass -> simple actual U at every nonzero algebraic time.

No arrow uses prior A_175 simplicity, pair-commutant scalarity, total Fourier minors in an A basis, or numerical eigensolver separation.

## Obligation matrix

| Obligation | Result | Evidence / boundary |
|---|---|---|
| Actual raw A, including centering and upper/lower phases | Passed | Rebuilt from 32 raw Fourier modes and raw T_N(a,b); exact involution check |
| Actual G and avoidance of square-root phase | Passed | Independent chirp-Fourier-chirp factorization; raw unitarity and generator covariance |
| Primitive q, i, primes and S orders | Passed | Own trial division, primitive-root enumeration, full order iteration |
| Characteristic-zero G^R=cI | Passed | Exact kernel covariance plus Weyl irreducibility; c is a local unit by inverse integrality |
| Complete spectral projectors | Passed | All R roots, including three zero projectors at N175; sum I, eigenrelations, idempotency and pairwise orthogonality |
| Projector specialization and rank equality | Passed | Integral direct summands over a DVR; no generic singular-matrix rank lift |
| Compressed matrices | Passed | Independent projector-column bases and selected-row left inverse |
| Characteristic polynomials and squarefreeness | Passed | Newton trace identities, Cayley–Hamilton, own Euclidean gcd; exact agreement with candidate |
| N7 failure control | Passed | A7=(9/10)I; block dimensions 2,2,3 and gcd degrees 1,1,2 |
| First-order splitting -> nonzero discriminant | Passed | Schur complement and scaled root discs, reconstructed below |
| Exponential-polynomial algebraicity | Passed | Distinct-eigenvalue projectors of A are algebraic even without simple A |
| External LW theorem | Inherited named input | EXT-POPESCU-2023, arXiv:2306.14352v2, Theorem 3.2; application checked, external proof not re-audited |
| Uniform N=7*5^e, all odd N, quantitative gaps, BGS | Out of scope | No inference from these finite certificates |

## 1. Actual model and phases

Canonical `fixed_model_symmetry_theorem.md` specifies raw T(a,b) with entries q^(b(x+h a)) at y=x+a, h=2^(-1) mod N. The raw symbol is cos(14pi q)+r(q)/10+r(q)sin(2pi q)/100+r(q)cos(2pi p-alpha)/100-1/10, with cos(alpha)=-3/5, sin(alpha)=4/5. Expanding in Fourier modes gives exactly the author's diagonal and upper coefficient (-3-4i)r((x+h)/N)/1000; the lower entry is the conjugate. The independent script instead multiplies sparse Laurent polynomials and assembles all 32 raw modes as Weyl matrices, so it does not assume the supplied Jacobi implementation.

The prescribed raw cat kernel factors as G=D F D, D_x=q^(-3*8^(-1)x^2), F_xy=(q^(4^(-1)))^(xy). This independent construction gives the actual G, not an arbitrarily phase-normalized Weil representation. Algebraically, G G^*=NI. The script checks its residue version and A^*=A using the field involution q -> q^(-1), i -> -i.

Direct kernel substitution gives G T(1,0)=T(3,2)G and G T(0,1)=T(4,3)G. These identities have no extra scalar phase in the raw convention. Their Weyl multiplication law gives covariance under S=[[3,4],[2,3]]. Hence S^R=I implies G^R commutes with the two generators. A matrix commuting with the diagonal clock is diagonal, and then commuting with the shift makes it scalar. Thus G^R=cI exactly in characteristic zero. This is not inferred by lifting the observed finite-field scalar identity.

The independent script checks covariance on the two generators and two additional labels, iterates S until its first identity, and finds R=3,6,30 at N=7,35,175. It directly checks the corresponding residue G power. The prime choices are independently verified as primes and split primes for Q(q,i); gcd(4,N)=1 makes the separately selected primitive q and i a consistent cyclotomic specialization.

## 2. Integral projectors and lifting the certificate

Work over a finite number field containing q, i and all roots of X^R-c, localized and completed at the selected place. Since p does not divide 1000N, both A and G are integral and G inverse is integral: G^(-1)=G^*/N. Thus c is a unit. The polynomial X^R-c is monic with unit derivative at every root, because p does not divide R and every root is a unit. All R distinct residue roots lift, and the resulting roots have pairwise unit differences. Passing to a finite extension if necessary does not change this argument.

For each root lambda, P_lambda=(1/R)sum_j lambda^(-j)G^j is integral. The identities P_lambda^2=P_lambda, sum P_lambda=I and P_lambda P_nu=0 for lambda!=nu hold exactly. In characteristic zero G is diagonalizable since X^R-c is squarefree. Therefore these are precisely its spectral projectors, with the same eigenspaces as M=G/sqrt(N).

For an integral idempotent P on O^N, O^N=im(P) direct sum ker(P). Both summands are free over the DVR, and reduction is exact on this split decomposition. Consequently the dimension of the characteristic-zero image equals the dimension of its residue image. In particular the three zero residue projectors at N175 are genuinely absent characteristic-zero eigenspaces; no eigenvalue is omitted.

Let V be any residue basis of im(Pbar). Lift its vectors arbitrarily and apply P. These lifted vectors have independent reduction and form a basis of im(P) by Nakayama and the equal rank. A selected-row minor that is invertible modulo p remains a unit. The induced endomorphism P A on im(P) has integral coordinates in this lifted basis, and its characteristic polynomial reduces to that of the independently constructed finite compression. A squarefree residue polynomial has nonzero residue discriminant, so its characteristic-zero discriminant is a unit, in particular nonzero.

At the physical complex embedding these polynomial projectors are the orthogonal projectors of the normal M. Because A is Hermitian, the restrictions are exactly the claimed Hermitian compressions. The proof certifies every algebraic eigenspace before choosing the physical embedding.

## 3. Independent exact finite reconstruction

The alternative script `independent_projector_audit.py` uses no SymPy or author functions. It constructs complete full-matrix projectors from powers of independently assembled G, takes pivot columns of each P as an image basis B, chooses invertible rows of B, and computes C=(B_rows)^(-1)(PAB)_rows. It checks BC=PAB. This differs from the supplied nullspace/free-coordinate route.

Characteristic coefficients are computed from trace(C^j) by Newton identities, with all denominators j units since block size <=7<p. Cayley–Hamilton is verified. Squarefreeness is checked by a separate Python-integer Euclidean polynomial gcd. All reported characteristic polynomials agree exactly, root by root, with the frozen author certificate despite the different bases and characteristic-polynomial implementation.

| N | p | R | cbar | Nonzero block dimensions | Gcd degrees |
|---|---:|---:|---:|---|---|
| 7 | 337 | 3 | 279 | 2,2,3 | 1,1,2 |
| 35 | 2521 | 6 | 2503 | 4,5,5,7,7,7 | six zeros |
| 175 | 4201 | 30 | 1347 | 2,2,3 and twenty-four 7s | twenty-seven zeros |

At N175, the three zero-projector residue roots are 1857,2973,3572. Every one of the 30 projectors was checked. All pairwise products, all idempotencies, their sum I, eigenrelations and trace/rank identities passed. Every nonzero image basis and action identity passed. The exact N7 control also directly checks A=(9/10)I.

Integer arithmetic is exact. Matrix multiplication operands are reduced to [0,p-1] and each product is guarded by N(p-1)^2<2^63-1. The largest bound is 3,087,000,000. Scalar-array updates use factors below p and additions/differences at most the corresponding small multiples of p^2; none approaches int64 overflow. Python integers handle primality, powers and polynomial arithmetic. There are no floating-point acceptance decisions, random samples, or truncations.

The original author script was copied before execution because it writes its JSON beside itself. Its output reproduced the frozen evidence exactly after dropping only timing fields. Its disabled-assertion guard is separately tested. The independent implementation uses explicit runtime checks that remain active under python -O; its optimized run gives the same mathematical output.

## 4. First-order perturbation argument

Fix an eigenvalue mu of M and its eigenspace E of dimension m. In the orthogonal decomposition E plus E-perp, write U(t)=M+itAM+O(t^2). For z=mu(1+it x), the upper-left block of zI-U(t) is it mu(xI-A_E)+O(t^2), while the off-diagonal blocks are O(t). The lower-right block is invertible for sufficiently small t and bounded x, because mu is absent from the complementary spectrum. Its Schur correction to the upper-left block is O(t^2).

After division by (it mu)^m the Schur determinant converges locally uniformly in x to det(xI-A_E). Every limiting root is simple. Choose disjoint small circles around these m roots. Rouché's theorem gives exactly one root, counted with multiplicity, inside each circle for every sufficiently small nonzero t. Thus each corresponding eigenvalue of U(t) is simple. Distinct mu have disjoint fixed neighborhoods, which cover all N roots for sufficiently small t. The characteristic discriminant is therefore not identically zero.

This is a qualitative witness only. It does not claim that a numerically resolved tiny-time eigenvalue gap equals the literal physical gap, or provide an explicit radius uniform in N.

## 5. LW boundary and algebraic time

For any Hermitian algebraic A, the distinct eigenvalues a_j are real algebraic and the projectors Q_j=product_(k!=j)(A-a_k I)/(a_j-a_k) have algebraic entries. Repeated eigenvalues create no obstacle: this formula ranges over distinct eigenvalues. Hence exp(itA)M=sum_j exp(it a_j)Q_j M has algebraic coefficients. Its characteristic coefficients and discriminant are finite exponential polynomials with algebraic coefficients and real algebraic frequencies.

Collect equal frequencies. If the discriminant is not identically zero, at least one collected coefficient is nonzero. At nonzero algebraic t all exponents it beta are distinct algebraic numbers. EXT-POPESCU-2023, Popescu arXiv:2306.14352v2, Theorem 3.2, gives their exponentials' linear independence over algebraic coefficients. Thus the discriminant cannot vanish at this t. This is exactly the registered qualitative implication used in `frozen_arithmetic_trace_rigidity.md` and `frozen_algebraic_spectral_simplicity.md`.

The present audit rechecks the algebraic hypotheses and implication against the durable exact-source registry and historical review. It inherits the existing source verification; it does not newly verify Popescu's external proof. No stronger transcendence or simple-power conclusion follows merely from first-order splitting, and none is accepted here.

## 6. Commands, remaining gap, and next useful check

The bound evidence is in `independent_results.json`, `replay/exact_projector_certificate.json`, and `verification_controls.json`. `computation_manifest.json` records the actual rerun, software versions, hashes before/after, finite range and non-claims. It is checked by the copied upstream `validate_manifest.py`; metadata validation is not itself a mathematical proof.

Reproduce with `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 independent_projector_audit.py` in this audit directory. Run the original only from `replay/exact_projector_certificate.py`. Full control and manifest regeneration use `python3 run_audit.py`.

There is no missing internal implication for the two claimed dimensions. The named external LW input remains separately attributed. For a uniform N=7*5^e theorem, the smallest outstanding input is an actual uniform compression/multiplicity formula and proof that every nonzero block has nonvanishing discriminant; observing size <=7 twice is not such a formula. The cheapest next research step is to derive the CRT/character formula for these blocks, rather than simply increase the finite screen. Canonical statuses have not been promoted by this audit.

## Publication mapping

Exact original proof/review bytes and dependency maps are preserved in
record/cat_jet_promotion_mapping.json. Portable replays retain all exact
mathematical outputs; execution path/timing hashes are reported separately.
Each component keeps its independently reviewed scope; diagnostics in the
author handoff are not promoted as further literal-U cases.
