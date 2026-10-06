# Independent audit: even-depth actual first-order obstruction

Date: 6 October 2026. Review workspace: `bgs_oldform_obstruction_review`. Canonical `BGS` was read-only throughout this audit. Its HEAD was `6f3874e5fb1d5b31b5825e2ff273e8c643e0046a`; it already contained unrelated modified and untracked files, and concurrent unrelated file additions were observed. No clean-working-tree or whole-tree-unchanged claim is made. This audit wrote only to its separate review directory; the load-bearing sources were individually hash-bound.

## Normalized claim and verdict

**Primary verdict: proved as written.** For every integer r≥2, put q=5^r, n=q² and N=7n. In the unchanged raw-kernel model, there are three complete eigenspaces of M_N, of dimensions 3,2,2, on each of which the actual Hermitian kick compression is zero. Consequently the criterion that every first-order cat compression is simple fails at every even depth e=2r≥4. This is a theorem about the actual kick and cat, not a modified-model example.

The target's second-order formula, including its sign and factor 1/2, is correct when H_2 denotes the coefficient of t² in the eigenphase expansion of exp(itA)M and P is the full λ-eigenprojection with PAP=0. The supplementary claim that P_W A^j P_W is scalar for integers j≥0 with 9j<5^r is also correct. It gives no bound on effective eigenjet order. No statement about actual H_2 simplicity, eigenjet growth, nonzero-coupling collisions, uniform kicked-U simplicity, the full U-commutant, or BGS is proved here.

## Frozen source and dependencies

The exact target is `inputs/even_depth_first_order_obstruction.md`, copied without changes from `bgs_seven_adic_resume/cat_splitting/even_depth_first_order_obstruction.md`.

SHA-256: `37482d57477777ac40bc6a6375bcbf53667f16070e1bcf7e33db04fb9737f654`.

The source-bound inputs are:

1. `inputs/uniform_cat_multiplicity_v2.md`, SHA-256 `b6e219832f094136f0ca80201ae61f80a9d2435bebc59dd2f18163e3444c8e1e`. This accepted theorem supplies simple M_(5^e), primitive-root applicability, the N7 spectrum with multiplicities (3,2,2), and exactly one partial cubic orbit, of occupancy one when e is even.
2. Its independent review binding, `inputs/cat_multiplicity_V2_BINDING.md`, SHA-256 `dbe6d39858060fa0540dc551cb2ecf227bf476821ddff306dcb673a86f6ec2be`; the associated full review, `inputs/cat_multiplicity_REPORT.md`, SHA-256 `c9ea460328b7e5aca3bd12378bc46e93edd0b9e5fc379ae114900409779ece5a`. The accepted v2 theorem's proof, primitive-root argument and occupancy deficit calculation were inspected. Its entire prior computation was not rerun and is not reported as new evidence.
3. Canonical `mathematics/fixed_model_symmetry_theorem.md`, Section 1, copied to `inputs/`, SHA-256 `32b2302c2567eebb75ff2231345e3336495ba8719517be6b5ce8734b416920c2`. This gives the actual raw kernel, raw Weyl convention and actual centered symbol.
4. The cat-arithmetic portion of `mathematics/frozen_arithmetic_trace_rigidity.md`, already included in the accepted multiplicity dependency closure. The HEAD version copied to `inputs/frozen_arithmetic_trace_rigidity_at_HEAD.md` has the prior reviewed SHA-256 `e23c99caec20d8e5ed8477b5689801296d011fa0daba466c42b20707452a94b8`. The current working copy's hash is `0b12ac9254845c2ac2bc95dc149dcd4a19116f447d2bce1a2c530c3f204ca1b2`; its diff consists only of an appended, unrelated one-step companion paragraph. The cat-arithmetic input is unchanged.

This audit uses no external literature theorem, no unverified phase convention, and no finite-field-to-characteristic-zero inference. The N4375 compression diagnostics in the target are not dependencies and were not independently audited here. All scientific scope statements remain restricted accordingly. No `.mathbox` ledger was found in the canonical root.

## Dependency graph

Actual raw kernel and Weyl convention → exact CRT tensor factorization with primitive powers → normalized q-supported vector ψ and its stabilizer expectations → P_W A_N P_W=0 for the actual Fourier support.

Accepted uniform prime-power simplicity and unique partial cubic orbit + independently derived raw trace one → the partial singleton is {1}, with ω,ω² absent → W is the sum of three complete eigenspaces → three zero first-order blocks of sizes 3,2,2.

Separately: full eigenprojection + PAP=0 + second-order block elimination → the stated Hermitian H_2. Weyl product support → direct-power scalar compression; inserting cat resolvents invalidates that unrotated support bound.

## Obligation matrix

| Obligation | Status | Reason |
|---|---|---|
| Actual model and centered support | Passed | Independently assembled exact 32 modes; |a|≤1, |b|≤9, no constant |
| CRT primitive-root powers | Passed | Explicit t7=n^−1 mod7, tn=7^−1 modn; raw kernel and Weyl phases factor identically |
| Normalization of ψ and M | Passed | ψ=q^−1/2 on q points; positive sqrt(n)=q |
| ψ is an exact eigenvector for every primitive power | Passed | Primitive geometric sum kills x not divisible by q |
| Stabilizer expectation including phase | Passed | Exactly 1 for q dividing both labels, otherwise 0 |
| Full eigenspace isolation | Passed | Trace locates the unique partial singleton at 1; simplicity and absence of ω,ω² exclude other tensor contributions |
| First-order phase slopes | Passed | They are the eigenvalues of the full Hermitian compression |
| H_2 sign, normalization and Hermiticity | Passed | Direct Schur derivation and cotangent weights below |
| Direct powers P_W A^j P_W | Passed | Only zero total integer frequency survives when 9j<q |
| Deduction of growing effective eigenjet order | Not justified | Resolvents insert cat rotations, outside the direct-power support argument |
| N4375 zero size-seven diagnostic blocks | Out of scope | Not used to prove the reviewed theorem |
| Uniform kicked-U simplicity or BGS | Out of scope | Neither is a consequence of this obstruction |

## Independent derivation

### 1. Exact CRT and conventions

For an odd modulus m and unit c mod m write

    M_(m,c)(x,y)=m^(-1/2) e_m(c Q_m(x,y)),
    Q_m(x,y)=−8^(-1)(3x²−2xy+3y²),
    (T_(m,c)(a,b)u)(x)=e_m(c b(x+2^(-1)a)) u(x+a).

These are the raw modular matrices, without the midpoint sign replacement. The canonical actual kick quantizes e^(2πi(kq+ℓp)) as T_N(ℓ,k); thus a is the shift label and b is the position-frequency label.

Set t7=n^−1 mod7 and tn=7^−1 modn. In CRT coordinates x=n t7 x7+7 tn xn modN, and similarly y, every scalar residue z obeys

    e_N(z)=e_7(t7 z7)e_n(tn zn).

The modular inverses of 8 and 2 reduce to the corresponding inverses in each factor. Hence, under the same coordinate permutation,

    M_N = M_(7,t7) ⊗ M_(n,tn),
    T_N(a,b) = T_(7,t7)(a,b) ⊗ T_(n,tn)(a,b).

Both t7 and tn are units. Positive square roots satisfy sqrt(N)=sqrt(7)sqrt(n), so no unexplained scalar or metaplectic phase appears. Labels reduce modulo the factor; primitive powers enter the phases. In particular they do not change divisibility by q.

### 2. Exact oldform and stabilizer

Let ψ(x)=q^−1/2 for x=qk, 0≤k<q, and zero otherwise. There are q support points, so ||ψ||²=q·q^−1=1. For every unit c modulo n,

    (M_(n,c)ψ)(x)
      =q^(-3/2) e_n(−3c·8^(-1)x²)
         Σ_(k=0)^(q−1) e_q(2c·8^(-1)xk).

The coefficient 2c·8^−1 is a unit modulo q. The sum is zero unless q|x, and equals q otherwise. When q|x the remaining chirp is 1 because n=q² divides x². This proves M_(n,c)ψ=ψ with exactly the stated normalization.

In the expectation of T_(n,c)(a,b), both support indicators can be nonzero only if q|a. In that case

    <ψ,T_(n,c)(a,b)ψ>
      =q^−1 e_n(c b·2^(-1)a) Σ_(k=0)^(q−1)e_q(c b k).

The sum vanishes unless q|b. If q divides a and b, n divides ab and the prefactor is also 1. Therefore the stated expectation is exactly 1 or 0, with no residual sign or root-of-unity factor.

### 3. Actual symbol and zero compression

The canonical raw symbol, writing s for the position coordinate and ρ for its auxiliary trigonometric polynomial, is

    cos(14πs)+ρ(s)/10+ρ(s)sin(2πs)/100
      +ρ(s)cos(2πp−α)/100−1/10,
    ρ(s)=(1−cos(14πs))(1+cos(2πs)),
    cos α=−3/5, sin α=4/5.

Exact Laurent assembly gives 32 nonzero Gaussian-rational coefficients, supported in |a|≤1 and |b|≤9, and zero coefficient at (0,0). The independent checker records every coefficient in `checks.json`; it also verifies conjugate symmetry. This is the actual raw symbol, not the ordinary-midpoint symbol used for a different classical dictionary.

For r≥2, q≥25. Among those 32 integer labels, none is divisible by q in both coordinates. The Weyl tensor identity and stabilizer expectation therefore give

    P_W A_N P_W=0,    W=H_7⊗span(ψ).

This is an exact complex matrix identity. There is no aliasing issue: all labels lie strictly inside the relevant q-bound and N≥4375.

### 4. Why these are complete eigenspaces

The accepted prime-power theorem is simple-spectrum and applies to the actual CRT primitive power. For even e its eigenvalue set E has exactly one partial orbit under multiplication by ω, and that partial orbit contains one eigenvalue β. Every other occupied orbit has all three elements. This full/partial occupancy is invariant under a common scalar spectral normalization, so the conclusion applies to the actual raw eigenvalues before the trace calculation locates β.

Here the phase location is obtained directly in the unchanged kernel. On the diagonal Q_n(x,x)=−2^−1 x². Write x=u+qv, with 0≤u,v<q. Then

    Tr M_(n,c)
      =q^−1 Σ_u e_n(−c·2^−1 u²) Σ_v e_q(−cuv)
      =1.

Only u=0 survives because c is a unit, and its inner sum equals q. Every full cubic orbit has eigenvalue sum zero, so the unique singleton β equals this trace: β=1. Thus E contains 1 and contains neither ω nor ω². The eigenvector ψ found above spans the entire 1-eigenspace by simplicity.

Write the seven-factor eigenvalues α,αω,αω², with multiplicities 3,2,2. If a tensor eigenvector has eigenvalue αω^j, its n-factor eigenvalue must equal ω^(j−k) for one of the three seven-factor indices k. The only present possibility is 1 and therefore k=j. This is an exhaustive classification of the product eigenspace. Consequently

    E_(αω^j)(M_N) = E_(αω^j)(M_(7,t7))⊗span(ψ),

with the indicated respective dimensions. It proves that W is the direct sum of complete eigenspaces, rather than merely an invariant seven-dimensional subspace. Applying the zero W-compression to their subprojections proves that all their first-order eigenphase slopes equal zero.

### 5. Second-order Schur calculation

Fix one complete λ-eigenspace, with projection P; let Q=I−P and B=M_Q. Since the eigenspace is complete, λ−B is invertible on QH. Assume PAP=0. In the decomposition PH⊕QH, for U(t)=exp(itA)M,

    U_PP=λP−(t²λ/2) PAQAP+O(t³),
    U_PQ=it PAQB+O(t²),
    U_QP=itλ QAP+O(t²),
    U_QQ=B+O(t).

The block eigenvalue equation is

    [U_PP+U_PQ(z−U_QQ)^−1 U_QP]v=zv.

Near λ, the first-order coefficient is zero, so z=λ+O(t²). Substituting the expansions yields

    effective z-matrix
      =λ[P−(t²/2) PAQ(λ+B)(λ−B)^−1 QAP]+O(t³).

Writing z=λ exp(i t²h+O(t³)) identifies

    H_2=(i/2) PAQ(λ+B)(λ−B)^−1 QAP.

For λ=e^(iθ), μ=e^(iφ) in the complementary spectrum,

    (i/2)(λ+μ)/(λ−μ)=(1/2)cot((θ−φ)/2),

which is real. Spectral calculus therefore proves H_2 is Hermitian. Its eigenvalues are the t² phase coefficients, not the second derivatives themselves; those derivatives are twice the coefficients. A simple H_2 separates this block for sufficiently small nonzero real t. The target does not assert that simplicity.

As a sign control, take M=diag(1,i), A=[[0,1],[1,0]], and the λ=1 projection. The formula gives H_2=−1/2. The exact characteristic equation z²−(1+i)cos(t)z+i=0 has the branch z(t)=1−it²/2+O(t⁴), agreeing with that sign and factor.

### 6. Supplementary direct powers and their exact limit

The raw Weyl multiplication rule is

    T_N(a,b) T_N(c,d)=e_N(2^−1(ad−bc)) T_N(a+c,b+d).

Thus every term in A_N^j has total integer label (a,b) satisfying |a|≤j and |b|≤9j. If 9j<q, the only such total label divisible by q in both coordinates is (0,0). Every other term vanishes on W by the same stabilizer compression. Every zero-label term is a scalar multiple of the identity on both CRT factors. Therefore

    P_W A_N^j P_W=c_j P_W  whenever 9j<q.

Here j is a nonnegative integer, c_j is the raw Weyl constant coefficient, and c_j=Tr(A_N^j)/N in this no-aliasing range. For j=0 the scalar is 1, for j=1 it is 0, and for j=2 it is 66033/160000. These checks distinguish scalarity from vanishing.

This controls direct powers only. A reduced resolvent is a function of M, and, in finite dimension, can be represented by a polynomial in M with the eigenspace projection included. Its insertion produces terms involving cat-rotated labels, such as v+S^k w, not merely v+w. Their integer sizes need not satisfy the direct-power box bound. In particular the explicit H_2 already contains such a resolvent between two kicks. No claim that the effective matrices remain scalar through the direct-power range follows. Neither a growing splitting order nor a bounded splitting order is established by this observation.

## Independent finite controls and reproducibility

Run from the review directory:

    python3 check_oldform.py

The implementation imports no author code. It uses exact Python integers and fractions; primitive-root sums are checked by exact reduction modulo Φ_(5^e)(z)=1+z^(n/5)+...+z^(4n/5). No numerical diagonalization, eigengap threshold, or root-of-unity tolerance is used.

The successful run checked:

- Independent exact assembly of all 32 actual raw-symbol coefficients, their conjugate symmetry, support bound, absent constant, and the exact square constant 66033/160000.
- 5,588 entries of the unnormalized kernel-vector equality: all x and all 20 primitive powers at n=25; all x and the eight listed primitive powers at n=625; eleven boundary/interior x values and eight listed powers at n=15625. The n=25 control is deliberately below the theorem's support threshold and checks the kernel identity only.
- 36 complete quadratic trace sums at those same primitive powers and dimensions.
- 4,164 direct stabilizer expectations: labels −6≤a,b≤6 at n=25; all actual support labels and a stabilizer/boundary grid at n=625 and n=15625.
- 70,000 CRT kernel-phase identities: all x,y at N=175 and all x with nine specified y values at N=4375.
- 145,600 CRT Weyl-phase identities: all x and all 32 actual modes at N=175 and N=4375.
- Reachable integer Fourier-support bounds for powers j=1,...,13; the stabilizer intersection is only zero for j=1,2 at r=2 and j=1,...,13 at r=3. These are support controls, not effective-eigenjet calculations.
- The exact Gaussian-rational second-order sign benchmark described above.

`checks.json` gives complete finite scopes and results. `computation_manifest.json` records provenance, source hashes, command, versions and boundaries; `audit_manifest.json` hashes the deliverable and controls. The finite checks supplement the uniform proof; no finite range is extrapolated. The original target and named v2 source are checked again against their frozen hashes at closeout.

## Remaining gap and strongest safe conclusion

There is no remaining gap in the reviewed first-order obstruction, the full-eigenspace identification, the stated H_2 formula, or the bounded direct-power scalar implication. The uniform multiplicity result remains an explicitly attributed accepted dependency; this review does not relabel it as newly proved.

The obstruction invalidates an all-depth first-order-simple-compression strategy for the actual family. The next required mathematical input for these three blocks is coefficient control of the effective second-order matrix or a later effective jet, with the cat resolvents retained. The direct-power support calculation is not a substitute. Actual nonzero-coupling simplicity and the BGS problem remain outside this verdict.

## Execution boundary

This inherited accepted argument supplies the deepest even-core isolation
and effective-second-order formula. Its original finite controls are not
newly rerun here; the stronger tower and second-jet replays are recorded
separately. The original source/review hashes are preserved in the map.
