# Independent audit of the repaired uniform cluster candidate, version 2

Date: 2026-10-06.

**Normalized claim.** For every integer e≥1, the actual frozen raw-Weyl generator A_(7·5^e) has simple complex spectrum.

**Primary verdict: proved as written**, using the explicitly inherited, independently reviewed finite input of 35 distinct residue eigenvalues with nonzero offset derivatives. This is an independent internal mathematical audit of the repaired source, not an external referee certificate, a formal proof-assistant result, or a new independent reconstruction of that finite input.

The scope is exactly this family of actual A matrices. It does not establish simplicity of U, other seven-divisible dimensions, quantitative complex gaps, or BGS.

Reviewed source: `source_snapshot/pure_five_uniform_cluster_candidate_v2.md`, SHA-256 `b3177dc35cf63a0ee49fd462a2a85c80333ea9c313c93084d7b23840c4631199`.

Version 1 remains frozen with hash `b4eaac5b517cda99f259709eb38f2eedc51b7c7b82181363aba51112d2cece3e`. Its separate audit remains **incomplete**: the present verdict does not retrospectively promote those earlier bytes. Version 2 adds the load-bearing coefficientwise two-index invariant and the analytic-domain argument identified in that audit.

## 1. Inputs and dependency graph

Inherited actual-model input:

- `first_ramified_cluster_split.md`, hash `811dd1b7ef91ecddf46d203e81860c813e4aca020a22697a337e5a96071b9fc7`;
- its independent bounded audit, hash `7d9853493c291e92ea9d2e4e058593523ef9d2f957d93c6f2b0d8e55c97db1c9`.

The inherited input fixes the actual raw-Weyl convention, algebraic real-Jacobi similarity, normalization, seven residue blocks, squarefreeness and pairwise coprimality, and nonzero offset derivative for each residue eigenvalue. In this audit, their use is checked but their finite-field computation is not rerun.

The repaired proof has the following closed dependency chain:

1. Actual coefficient formulas and local cyclotomic valuations → integral translated coefficient family with explicit cut factors.
2. Fixed finite residue input → analytic block eigenvalues and integral invertible eigenbases.
3. Unit-gap species elimination → coefficientwise first Schur matrix and a common isometric scalar diagonal function.
4. Coefficientwise cyclic-arc invariant, indexed simultaneously by elimination depth s and cap depth R → weighted bounds on all dense Schur entries.
5. Centered analytic inverse and contraction → new diagonal roots, analytic unit normalization, and exact higher-digit separation.
6. Broad-domain covariance → identification of the new scalar functions at surviving sites.
7. Nested disjoint spectral discs and scalar Schur roots → N distinct eigenvalues.
8. Nonzero algebraic discriminant at one local embedding → simple complex spectrum of A.

No new external theorem is used without proof here. The analytic ingredients are reconstructed below inside complete coefficient algebras.

## 2. Model and base analytic input

Let q have order N=7·5^e, let Q=q^7 have order 5^e, and put pi=Q−1. After adjoining a finite unramified extension splitting the fixed residue polynomials, work over its complete valuation ring O. The base cyclotomic ramification gives v_pi(5)=4·5^(e−1).

For u not divisible by 5^e, v_pi([u]_Q)=5^v5(u)−1. At a cut u=5l this gives 2d_v5(l) for the squared normalized bond factor, where d_s=5^(s+1)−1. At an actual zero boundary, the translated factor is Q^u y, and hence obeys every capped lower bound used in the proof.

On y=pi^d_R u, the factor [5l]_Q+Q^(5l)y is coefficientwise divisible by pi^min(d_v5(l),d_R). Squaring it gives b_R(l)=2min(d_v5(l),d_R). This is a direct coefficient factorization, not a conclusion from evaluating at a set of points. The other bond factors and their inverses are integral analytic units. The seventh-root series has integral coefficients because 1/7 is a 5-adic integer and the branch is evaluated on 1+pi y.

The exact translation law is y⊕z=y+z+pi yz. Shifts by 35 preserve the block partition and species labels, and the actual coefficients transform by the corresponding cyclic permutation. One can choose the block eigenbases compatibly: normalize the first eigenvector coordinate to one and use the tridiagonal recurrence. The internal bonds are units and the residue eigenvalues are simple, so this produces analytic integral eigenvectors and an invertible integral eigenbasis. Consequently there is no hidden basis-choice obstruction to the covariance used later.

The full local branch derivative modulo pi is precisely the certified offset derivative: the q-phase derivative contributes a factor pi, while [x]_Q has translation derivative Q^x≡1. The fixed normalization does not vary. Thus the actual analytic branches have unit divided differences on pi^4 O.

For the first Schur reduction, all complementary species have unit diagonal denominators with constant nonzero residue. Every original cut has coefficientwise valuation at least 8. Therefore the complementary Neumann series converges in the coefficient algebra. A nontrivial diagonal return uses at least two cuts, so its self-energy has valuation at least 16. On the pi^4 parameter ball, its y-divided differences are divisible by pi^12. Centering the spectral variable at the original local root gives a strict analytic contraction, and the resulting diagonal factor can be divided by an analytic unit. These operations preserve all raw cut lower bounds.

This establishes the level-zero common root function and the coefficientwise weighted off-diagonal base, simultaneously on every smaller parameter ball.

## 3. The interval-weight induction is valid

For a fixed branch S_s={k:k≡c mod 5^s}, define the earlier denominator toll

D_s=Σ_(j<s)4·5^(s−j−1)d_j=(4s−1)5^s+1.

For each interval I between adjacent S_s sites, set

E_s^(R)(I)=Σ_(original cuts in I)b_R(l)−D_s, for R≥s.

There are exactly 7·5^s original cuts in I. The divisibility count for j≤s is independent of the interval origin. Thus

E_s^(R)(I)≥E_s^(s)(I)≥56(s+1)5^s−D_s=H_s,

where H_s=(52s+57)5^s−1>d_s. Intervals may have different additional weights; the proof correctly retains those differences.

The invariant bounds each dense off-diagonal entry by the minimum of the two weighted cyclic-arc sums between its endpoints. At level zero, unit-gap species elimination proves it directly from the convergent original-edge walk expansion, followed by removal of positive-cost loops.

For the induction, work with the representation indexed by R≥s+1. Newly removed current vertices have denominator cost d_s; the complementary inverse converges because H_s>d_s. For each Neumann term, replace every dense edge by an arc attaining its invariant lower bound. Concatenate the arcs, then additionally charge d_s at every encountered newly removed current vertex that did not originally supply a denominator. This only lowers the bound.

Every closed subwalk now has positive cost: each traversed elementary interval costs at least H_s, while its vertex charge is at most d_s. Erasing such a loop lowers the adjusted cost. A remaining simple path is one of the two cyclic arcs. Each group of five adjacent old intervals has exactly four newly removed intermediate vertices, giving

Σ_(five old intervals)E_s^(R)−4d_s
 =Σ_(raw cuts in the new interval)b_R(l)−5D_s−4d_s
 =Σ_(raw cuts in the new interval)b_R(l)−D_(s+1).

This proves the invariant at s+1. Passing a surviving S_(s+1) vertex inside an expanded dense edge adds no denominator, as required. Repeated vertices, backtracking, long dense edges, and wraparound are all covered by the same loop-erasure argument. The direct retained entry is covered as a term with no newly introduced denominator.

The coefficientwise Gauss bound of a convergent sum cannot be smaller than the uniform lower bound of its summands. No noncancellation claim is needed.

Crucially, this argument uses the R=s+1 representation to obtain H_(s+1). It never attempts to infer the extra high-cut divisibility from H_s alone, and never flattens previously resummed diagonal returns through high-cost denominators. The two diagnostic counterexamples in the version-1 audit therefore do not apply to this repaired invariant.

## 4. Centered coefficient algebras and denominator units

The source distinguishes the broad translation domain at level s from its smaller weighted charts. This distinction is sufficient.

The broad domain is y∈pi^d_s O. It is stable under shifts whose parameter has valuation at least d_s. On that domain the scalar root functions are obtained from a base integral unit-derivative function by corrections whose divided differences have positive valuation.

A slightly stronger fact, supplied by the actual construction, makes the unit assertions precise: after rescaling to the broad ball, each correction is pi^B times a restricted series with B>d_s. Its difference quotient in the unscaled variable is therefore coefficientwise divisible by pi^(B−d_s). Translating its argument inside the closed ball is an integral substitution of restricted series. The base function's quotient has a fixed nonzero constant residue, while every correction has zero residue in its quotient. Thus the needed normalized differences are *Gauss-analytic units*, not merely functions nonzero at O-valued points.

For the weighted estimates choose a reference surviving site and use

y=pi^d_R u,

z=rho_(s,c)(y)+pi^(d_s+1)w,

in O⟨u,w⟩. The source allows the physical origin to be shifted to that reference; this simply shifts the raw cut indices and does not change the uniform interval count.

For an earlier eliminated level j<s, both the parameter movement and the spectral chart displacement are strictly smaller than its gap pi^d_j. After division by pi^d_j the denominator has a nonzero constant residue and positive-valuation nonconstant part, so it is an invertible element of O⟨u,w⟩. For newly removed next-digit classes, their gap from the reference is exactly d_s; with R≥s+1 the same argument applies after division by pi^d_s.

All row-normalizing factors are analytic units. Their inverses remain integral on restriction and centered substitution. Matrix Neumann inverses consequently exist in the complete Gauss algebra itself. This verifies the coefficientwise interpretation of the interval induction.

No finite-residue pointwise-to-Gauss inference is used. The t^q−t warning from the version-1 audit is resolved by these direct coefficient factorizations and unit-residue statements.

## 5. Analytic scalar roots and new normalization

The new diagonal self-energy has coefficientwise valuation at least

B_s=2H_s−d_s.

Terms with additional complementary edges gain at least H_s−d_s per additional step, so this bound applies to the entire inverse expansion.

In the selected centered chart, write the self-energy as pi^B_s F(u,w), with F restricted and integral. The scalar equation for the reference root becomes, up to a harmless sign,

w=pi^(B_s−d_s−1)F(u,w).

Since B_s−d_s−1=2H_s−2d_s−1>0, this is a strict contraction in the complete algebra O⟨u⟩. Starting at zero, successive substitutions converge coefficientwise to a restricted series w(u), and in fact w lies in pi^(B_s−d_s−1)O⟨u⟩. Therefore the actual spectral correction is

rho_(s+1,c)(y)−rho_(s,c)(y)∈pi^B_s O⟨y/pi^d_(s+1)⟩.

Its y-divided differences gain at least

B_s−d_(s+1)=(104s+84)5^s>0.

This establishes the next exact isometry property on the broad new ball. It is an analytic construction, not independent pointwise fixed points being asserted to glue afterward.

The same construction is made for each retained site. Their old roots differ within the selected child class by valuation at least d_(s+1)>d_s+1, so their centers belong to the same old spectral chart. The difference quotient of the self-energy in z has valuation at least B_s−d_s−1>0. Consequently each new diagonal equation factors as

(rho_(s+1,k)(y)−z) × an analytic unit.

Normalizing by the inverse of this unit preserves every off-diagonal lower bound. The new center differs from the old one by valuation B_s>d_s+1, and the new spectral radius is smaller. Thus substituting the next centered chart is integral in the Gauss algebra, as claimed in source lines 107–111.

This completes the analytic half of the simultaneous induction. The sharper derivative margin used in version 1 is not needed and is not silently imported.

## 6. Covariance and exact higher-digit gaps

The matrix family has exact covariance under the cyclic translations preserving the current retained class. Schur complement is compatible with the corresponding permutation, and the integral block eigenbasis can be chosen covariantly as above. Scalar root uniqueness and analytic unit factorization preserve that identity.

Covariance is established on the broad level-s ball, which these translations preserve. Narrower R>s charts are used only after restriction or the explicitly shifted origin. Version 2 no longer uses a shift of valuation d_s as though it preserved a ball of depth d_R>d_s.

For k,l in the same new retained class, covariance identifies their scalar diagonal values with evaluations of one new root function at translated parameters. Translation itself has unit slope 1+pi y_delta. The base unit divided difference plus the strictly contracting correction therefore gives

v_pi(rho_(s+1,k)(0)−rho_(s+1,l)(0))
 =v_pi(y_k−y_l)
 =d_v5(k−l).

Thus arbitrarily deep gaps are preserved by a common analytic function. The proof does not substitute an absolute small-norm diagonal perturbation for this exact statement.

## 7. Final roots and degree count

For a fixed residue species there are P=5^(e−1) copy labels. At level s, choose representatives of the five next-digit classes. Their scalar centers have pairwise gap valuation d_s, so the discs of depth d_s+1 are disjoint. The complementary block is invertible throughout each selected disc.

Inside a child class, all relevant old centers differ by valuation at least d_(s+1). The next diagonal corrections have valuation B_s>d_(s+1). Consequently every subsequent descendant chart and root remains in the selected ancestor disc. This verifies the nesting needed to compare roots obtained through different branches.

After all e−1 copy digits are fixed, only one fixed-species site remains. Its scalar Schur root is an eigenvalue of the original matrix because every previously removed complementary determinant is nonzero on its chart. Its scalar derivative is a unit. Roots from different copy labels separate at their first differing digit; roots from different residue species already differ modulo pi.

There are exactly 35P=7·5^e distinct roots. These exhaust the characteristic degree. Equivalently, the Schur determinant factorization and unit scalar derivatives give their simplicity directly. No unproved claim about intermediate root multiplicities, no Rouché theorem, and no cancellation assumption is required for this final count.

For e=1, there are no copy digits to split and the 35 distinct residue species already supply the conclusion. At the last one-site level for e>1, the off-diagonal invariant is vacuous; the final scalar domain is used only for its root. Exact zero boundaries remove possible contributions and cannot worsen any lower bound.

Finally all matrix coefficients, the similarity, and the scalar normalization are algebraic, with eta nonzero for this family. The characteristic discriminant is nonzero at the chosen local embedding, hence is a nonzero algebraic number and remains nonzero under the complex embedding. Undoing normalization and similarity proves the stated simplicity of the actual complex A_N.

## 8. Obligation matrix and boundary

- Actual operator, gauge, normalization: **passed within the stated inherited review boundary**.
- Seven residue blocks and both required derivative properties: **inherited exact finite input**, not rerun in this audit.
- Integral translation and cut coefficient factors: **passed**.
- First species reduction and isometric diagonal base: **passed**.
- Two-index coefficientwise interval invariant: **passed**.
- Dense cyclic edges, loops, denominator tolls, wraparound: **passed** by levelwise arc expansion and positive loop erasure.
- Gauss-analytic inverse units and centered chart transitions: **passed**.
- Analytic fixed points, strict divided differences, row normalization: **passed**.
- Broad-domain covariance and narrower chart restrictions: **passed**.
- Final simple-root construction, distinctness and degree exhaustion: **passed**.
- All-e actual A-simplicity in this family: **proved as written in the reviewed version 2**.
- U-simplicity, other families, complex quantitative gaps, BGS: **out of scope**.
- External independent refereeing or full proof-assistant formalization: **not claimed**.

## 9. Evidence and provenance

This audit read the exact frozen candidate and reconstructed the critical induction, rather than accepting a numerical list of exponent checks. The diagnostic script in the version-1 audit is useful only to identify invalid weaker implications; it is not evidence of the all-e theorem. The author's bounded tropical controls were not used as a proof input here.

The version-1 report and its computations remain unchanged. `source_manifest_v2.json` records the new source hash, inherited sources, audit hash, and report boundary. Applicable canonical instructions and source-of-truth records were respected. Canonical BGS files were not edited. No commit, push, integration, full build, or new formal theorem was performed by this audit.
