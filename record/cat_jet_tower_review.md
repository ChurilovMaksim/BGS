# Independent audit: complete oldform tower and first-order compression

Date: 6 October 2026. Review workspace: `bgs_oldform_tower_review`.

## Normalized claim and verdict

**Primary verdict: proved as written.** For every integer e≥4, the actual raw cat M_(7·5^e) has a spectral subspace W_2 of dimension 7·5^(e−4), consisting of complete eigenspaces, on which the actual centered Hermitian generator has zero compression. Each complete cat eigenspace contained in W_2 therefore has a zero first-order slope matrix. The stated parity-dependent block counts, all oldform intertwinings, the j=1 coefficients −i/800 and +i/800, and the strict direct-power scalar threshold 9k<5^j are correct.

This is an extension to every depth e≥4 and a growing oldspace, rather than only the three even-depth blocks in the previously accepted obstruction. The result makes no assertion of degeneracy or simplicity for kicked U, no claim about the full U-commutant, and no BGS conclusion. Direct-power scalarity does not bound effective eigenjet order.

## Source binding, scope, and provenance

The reviewed source is the unchanged local copy `inputs/oldform_tower_compression.md`, copied from `bgs_seven_adic_resume/cat_splitting/oldform_tower_compression.md`.

SHA-256: `d359482763667a6707ed9a060a3874e951f95336561a4ac645df453022b085ae`.

Dependencies were inspected and copied into `inputs/`:

- `uniform_cat_multiplicity_v2.md`, SHA-256 `b6e219832f094136f0ca80201ae61f80a9d2435bebc59dd2f18163e3444c8e1e`. This is the accepted uniform prime-power simplicity, primitive-root applicability, N7 multiplicity, and unique partial cubic orbit input.
- Its acceptance binding `V2_BINDING.md`, SHA-256 `dbe6d39858060fa0540dc551cb2ecf227bf476821ddff306dcb673a86f6ec2be`, and full prior `REPORT.md`, SHA-256 `c9ea460328b7e5aca3bd12378bc46e93edd0b9e5fc379ae114900409779ece5a`. Their prior arithmetic runs are inherited evidence, not reported as new runs here.
- Canonical `mathematics/fixed_model_symmetry_theorem.md`, Section 1, SHA-256 `32b2302c2567eebb75ff2231345e3336495ba8719517be6b5ce8734b416920c2`, for the unchanged raw kernel, raw Weyl convention, and actual centered symbol.

The earlier `bgs_oldform_obstruction_review/REPORT.md` was read for scope and conventions. It proves only its own even-depth endpoint obstruction; the full tower and odd-depth assertion are derived below rather than inferred from that report.

Canonical `BGS` was read-only throughout. Its observed HEAD was `a4d59bf91b1aeff88719e3b1eaa0ba3b8dafe8d8`; its status before and after this audit showed an existing modification to `RESEARCH.md`. This review wrote no canonical files. Its scientific artifacts are confined to its separate review workspace; the supplied manifest validator was staged temporarily in `/tmp`. No whole-tree cleanliness or absence of other actors' changes is asserted. Relevant source/status/convention material was inspected. No canonical `.mathbox` ledger was found. No external literature leaf is needed for this audit.

## Claim card

Let e and j be nonnegative integers with 2j≤e, n=5^e, q=5^j, and m=n/q². Every Hilbert space has its standard counting-measure inner product. For a unit c modulo an odd modulus d, use

    M_(d,c)(x,y)=d^(−1/2) e_d(c Q_d(x,y)),
    Q_d(x,y)=−8^(−1)(3x²−2xy+3y²),
    (T_(d,c)(a,b)f)(x)=e_d(c b(x+2^(−1)a)) f(x+a).

All inverses here are modular; all square roots in normalization are positive real. At d=1 set M_1=T_1=1. The lower primitive root has coefficient c modulo m. Define

    (J_j f)(x)=q^(−1/2) f(x/q mod m) when q divides x,
               0 otherwise.

The uniform assertions being audited are:

1. J_j is isometric and M_(n,c)J_j=J_jM_(m,c mod m).
2. J_j* T_(n,c)(a,b) J_j vanishes unless q divides a and b, and otherwise equals T_(m,c mod m)(a/q,b/q).
3. In exact CRT coordinates, W_j=H_7⊗J_jH_m is a sum of complete eigenspaces of the actual M_(7n).
4. The actual A has the stated two surviving modes at j=1 and zero W_j-compression for j≥2.
5. For nonnegative integers k, P_(W_j) A^k P_(W_j)=c_k P_(W_j) whenever 9k<q. This concerns unrotated powers only.

## Dependency graph and obligation matrix

Raw model → exact CRT phase factorization → compatible primitive-root kernels and Weyl operators.

Oldform definition → isometry + exact cat intertwining + exact Weyl compression.

Accepted simple prime-power spectrum and unique partial cubic orbit + new trace recurrence + intertwining → common partial occupied subset → oldspace is a sum of complete product-cat eigenspaces.

Actual centered 32-mode symbol + Weyl compression → j=1 two-mode formula and j≥2 zero compression → zero first-order slope matrices on complete blocks. Accepted multiplicities, including the separately handled m=1 endpoint, give the stated counts.

Raw Weyl multiplication + integer support bounds → strict direct-power scalarity; no implication to resolvent-containing effective jets is used.

| Obligation | Status | Decisive point |
|---|---|---|
| Raw rather than ordinary midpoint convention | Passed | Modular inverses of 2 and 8 are retained throughout |
| CRT root powers and normalization | Passed | c7=n^−1 mod7, cn=7^−1 modn; no extra phase |
| J normalization and adjoint | Passed | q disjoint repeated coordinates per lower basis vector |
| Cat intertwining | Passed | Exact q-term geometric sum; lower coefficient reduces modulo m |
| Weyl compression and midpoint phase | Passed | Support kills q∤a; repeated-coordinate sum kills q∤b |
| m=1 endpoint | Passed | M_1=T_1=1, trace 1, simple singleton spectrum |
| Gauss trace invariance | Passed | G_e=5G_(e−2), positive square-root normalization |
| Full product eigenspaces rather than pieces | Passed | The entire occupied subset of the sole partial cubic orbit agrees |
| Seven-factor root under lowering | Passed | Lower-root ratio q² is a coordinate-rescaling conjugacy |
| Actual j=1 coefficients | Passed | Independently assembled exact Gaussian-rational symbol |
| j≥2 vanishing | Passed | 32 modes, |a|≤1, |b|≤9, no zero mode |
| Even and odd block counts | Passed | Smaller exact cat distribution with explicit m=1 endpoint |
| Direct-power strict threshold | Passed | Only total integer frequency (0,0) survives when 9k<q |
| Effective eigenjet order | Out of scope | Cat rotations occur inside reduced resolvents |
| Kicked-U/full-U/BGS conclusion | Out of scope | No such implication is made |

## Independent derivation

### 1. Isometry and exact cat intertwining

For each t modulo m, its oldform basis vector is supported on the q coordinates

    x=q(t+m l),  0≤l<q,

with value q^(−1/2). Distinct t give disjoint supports. Its norm is one, proving J_j*J_j=I. Explicitly,

    (J_j* g)(t)=q^(−1/2) Σ_(l=0)^(q−1) g(q(t+m l)).

In M_(n,c)J_j, sum the raw kernel over y=q(t+m l). The l-dependent y² terms disappear modulo n=q²m. The remaining l-dependent phase is

    e_q(c·4^(−1) x l).

Its coefficient is a unit times x, so the sum is zero unless q divides x, when it equals q. Put x=qu on that support. The remaining phase is

    e_m((c mod m) Q_m(u mod m,t)).

The normalization equals

    n^(−1/2) q^(−1/2) q = q^(−1/2)m^(−1/2),

which is exactly J_jM_(m,c mod m). This includes m=1: the lower phase is 1 and the lower kernel is the stipulated scalar 1. No metaplectic rephasing occurs.

### 2. Exact Weyl compression

In the adjoint sum write x=q(u+m h). The shifted oldform is nonzero only if q divides a. If a=qA, its lower argument is u+A mod m. The remaining average of phases is

    q^(−1) Σ_(h=0)^(q−1)
      e_n(c b q(u+m h+2_n^(−1)A)).

The h-dependent factor is e_q(c b h). It vanishes unless q divides b. If b=qB, the phase left after summation is

    e_m((c mod m) B(u+2_m^(−1)A)).

The reduction of the modular inverse is exact. Therefore the compression is precisely T_(m,c mod m)(A,B), with no residual sign, scalar, or seven-factor change. At m=1 it is 1 whenever both divisibilities hold.

### 3. CRT, including the root change under lowering

For N=7n set c7=n^−1 mod7 and cn=7^−1 modn. The CRT permutation gives

    M_N = M_(7,c7) ⊗ M_(n,cn),
    T_N(a,b)=T_(7,c7)(a,b) ⊗ T_(n,cn)(a,b).

The phase identity follows from e_N(z)=e_7(c7 z mod7)e_n(cn z modn); the modular inverse factors reduce in each modulus, and sqrt(N)=sqrt(7)sqrt(n). These are exact identities of the raw normalized matrices.

The lower five-primary coefficient is cn mod m=7^−1 modm. The seven-primary coefficient for the actual smaller cat M_(7m) is m^−1 mod7, which need not literally equal n^−1 mod7. This does not undermine the statement about smaller-cat block dimensions. In fact it admits an exact conjugacy: m^−1=q² n^−1 mod7. If V_q sends the standard basis vector at x to that at qx modulo7, then

    V_q* M_(7,n^−1) V_q = M_(7,m^−1),

because Q_7(qx,qy)=q² Q_7(x,y). Thus the restriction to W_j is unitarily equivalent to the actual smaller raw cat M_(7m), not merely an unrelated root variant with the same counts.

### 4. Trace recurrence identifies the whole partial occupied subset

For r≥2 write d=5^r and define the raw trace numerator

    G_(r,c)=Σ_(x mod d) e_d(−c·2^(−1)x²).

Write x=y+5^(r−1)z with y modulo5^(r−1) and z modulo5. The z² term disappears modulo d. The z-sum is zero unless 5 divides y. Substituting y=5u gives

    G_(r,c)=5 G_(r−2,c mod 5^(r−2)).

Divide by sqrt(5^r)=5sqrt(5^(r−2)) and iterate. Thus the actual raw traces at n and m agree, with the compatible lower primitive root. At m=1 the trace is 1.

Let E_d be the actual, unrephased eigenvalue set. Accepted simplicity and J intertwining give E_m⊂E_n. For d>1 the accepted theorem gives exactly one partial orbit under multiplication by ω, with occupancy one for even r and two for odd r. At d=1 the singleton {1} has the same even-parity property directly.

Each full cubic orbit sums to zero. Hence, for even parity, the sole occupied point of the partial orbit equals Tr M_d. For odd parity, the sole missing point equals −Tr M_d, and the two occupied points are its ω and ω² multiples. Equal traces therefore determine the same partial orbit AND the same occupied subset at n and m. Mere equality of occupancy counts would not have sufficed; this trace step supplies the necessary phase location.

Now inspect each cubic orbit. If E_m occupies it fully, spectral inclusion makes E_n occupy it fully. On the common partial orbit, both sets have exactly the same points. On every remaining orbit, E_m is empty and E_n is either empty or full. Therefore E_n\E_m is a union of full cubic orbits disjoint from all occupied E_m orbits.

Write the seven-factor eigenvalues as γ, γω, γω² with multiplicities 3,2,2. A product collision γω^a λ=γω^b μ implies λ/μ is a power of ω. Consequently a lower eigenvalue λ∈E_m cannot collide in the product cat with μ∈E_n\E_m. Because the prime-power factor is simple, J_jH_m contains each of its selected eigenspaces in full. It follows that W_j contains complete product-cat eigenspaces, with no contributions to those eigenvalues from its orthogonal complement. This is the central spectral-completeness implication.

### 5. The actual centered symbol and block counts

Independently assemble the raw Fourier polynomial from the fixed model:

    r(q)=(1−cos(14πq))(1+cos(2πq)),
    a(q,p)=cos(14πq)+r(q)/10+r(q)sin(2πq)/100
           +r(q)cos(2πp−α)/100−1/10,
    cos α=−3/5, sin α=4/5.

Quantization sends e^(2πi(bq+ap)) to T_N(a,b). Exact Gaussian-rational expansion yields 32 nonzero coefficients, |a|≤1, |b|≤9, conjugate symmetry, and zero constant coefficient. Among those labels, only (0,5) and (0,−5) are divisible by 5 in both coordinates. Their coefficients are respectively −i/800 and +i/800. Applying the Weyl compression gives precisely

    (I⊗J_1*) A_N (I⊗J_1)
      =−i/800 T_(7,c7)(0,5)⊗T_(m,cn mod m)(0,1)
       +i/800 T_(7,c7)(0,−5)⊗T_(m,cn mod m)(0,−1).

For j≥2, q≥25. No nonzero label in the 32-mode dictionary has both coordinates divisible by q; the zero label has zero coefficient. Thus P_(W_j)A_NP_(W_j)=0 exactly over the complex numbers. This is not a residue-field inference.

For every e≥4, j=2 is available and dim W_2=7m with m=5^(e−4). The preceding complete-eigenspace identification and smaller-cat conjugacy give:

- even e: m−1 blocks of dimension 7, plus dimensions 3,2,2;
- odd e: m−2 blocks of dimension 7, plus dimensions 4,5,5.

At e=4, m=1 and the first number is zero, leaving exactly 3,2,2. At e=5, m=5 and the first number is three, leaving 4,5,5. Each list has total dimension 7m. For every contained full eigenprojection P, PAP=0 follows by compressing the zero W_2-compression. Its first-order phase slope matrix for exp(itA_N)M_N is therefore identically zero.

### 6. Direct powers and the perturbation boundary

The raw Weyl product law is

    T_N(a,b)T_N(c,d)=e_N(2^(−1)(ad−bc))T_N(a+c,b+d).

Every term of A_N^k has total INTEGER label satisfying |a|≤k, |b|≤9k. If 9k<q, divisibility by q of both coordinates forces (a,b)=(0,0). The coefficient accumulated from Weyl phases is scalar, and the remaining zero-label operator is identity in both CRT factors. Thus

    P_(W_j) A_N^k P_(W_j)=c_k P_(W_j),  9k<5^j.

The inequality is strict and k is a nonnegative integer. It asserts neither vanishing of c_k nor any converse once the threshold fails. For k=0 the scalar is 1; for k=1 it is 0 in the applicable range; for k=2 it is 66033/160000 whenever the threshold applies. These distinguish scalarity from zero compression.

Reduced cat resolvents contain powers of the cat, hence rotated Weyl labels such as v+C^s w, where C is the raw label action (conjugate to the stated S by coordinate swap). The rotation exponent is not bounded by the number of kicks. Their possible orbit lengths grow with e even at fixed perturbation order. The integer support box used for unrotated A^k is therefore unavailable for effective eigenjets. No growing lower bound, nor any bounded upper bound, for the actual splitting order follows here.

## Independent exact finite controls

Command, from the review workspace:

    python3 check_tower.py

The checker imports no author code. Its arithmetic is Python integers, exact Fraction Gaussian rationals, and reduction modulo

    Φ_(5^e)(z)=1+z^(5^(e−1))+z^(2·5^(e−1))
                +z^(3·5^(e−1))+z^(4·5^(e−1)).

It uses explicit runtime checks rather than removable Python assertions, no floating spectral computation, and no tolerance. The successful run took approximately 6.78 seconds and checked:

- 289,342 raw kernel-sum entry identities, with e=0,...,6 and every allowed j. For j≥1, all matrix entries are tested at n≤625 and at (e,j)=(5,2). Larger levels and j=0 use the exact representative lists recorded in `checks.json`. All primitive powers are tested at n≤125; the larger explicit root lists include the actual CRT root.
- Exact oldform norm and disjoint-support identities at every e=0,...,6 and allowed j, including m=1.
- 183 full Gauss-sum lowering identities across e=2,...,8 and every positive allowed j. Every summand is enumerated for each stated root. At e=7,8 the roots are 1 and the actual CRT root; lower root scopes are explicitly listed.
- 43,878 exact Weyl-compression row identities, including the actual 32 modes, stabilizer/boundary labels, negative labels, the m=1 endpoint, and representative odd/even nonterminal tower levels.
- 68,684 CRT quadratic-kernel phase identities and 175,104 CRT Weyl phase identities. The two smallest kernel controls are exhaustive; all scope lists are in the output.
- The exact seven-factor coordinate-rescaling phase identity at every e=0,...,9, every allowed j, and every x,y modulo7; the compatible lower five-primary root is also checked.
- Independent exact assembly of the 32-mode symbol, its zero coefficient, Hermiticity, j=1 coefficients, j≥2 empty retained support, and the k=2 constant coefficient.
- All six nonempty proper subsets of a cubic orbit and their trace rule in Q[ω]. The universal comparison of different dimensional spectra is proved above, not inferred from this finite subset control.
- Reachable integer support boxes through k=13, checking each applicable strict threshold for j=0,1,2,3. Reachable labels overapproximate support when cancellations occur, which is safe for the exclusion test.
- Both parity formulas and total dimensions for e=4,...,20, complementing the uniform counting proof.

`checks.json` records every finite scope, software version, source hash and exact coefficient. `computation_manifest.json` records the execution contract and output hashes; `audit_manifest.json` binds this report and deliverables. The supplied computation-audit validator accepted the manifest with `--root` as a valid legacy v1 evidence record; it explicitly noted that v1 lacks machine-checkable resource-limit and declared-result provenance. Those legacy limits are retained in the manifest. These bounded controls supplement the proof and are not extrapolated to establish its universal quantifiers.

## Remaining gap and strongest safe conclusion

There is no remaining implication gap in the audited oldform-tower theorem. Its only substantial inherited theorem input is the explicitly accepted uniform cat multiplicity result, with m=1 handled directly. The trace argument supplies the previously unaudited bridge from an invariant oldspace to complete repeated product-cat eigenspaces.

The strongest safe conclusion is exactly the all-depth first-order obstruction on a 7·5^(e−4)-dimensional spectral subspace, plus the stated more general tower compression identities. A next-order calculation must retain reduced cat resolvents and actual coefficients. Neither a first-order degeneracy nor scalar unrotated moments decides actual nonzero-coupling spectral multiplicity.

## Publication mapping

Exact original proof/review bytes and dependency maps are preserved in
record/cat_jet_promotion_mapping.json. Portable replays retain all exact
mathematical outputs; execution path/timing hashes are reported separately.
Each component keeps its independently reviewed scope; diagnostics in the
author handoff are not promoted as further literal-U cases.
