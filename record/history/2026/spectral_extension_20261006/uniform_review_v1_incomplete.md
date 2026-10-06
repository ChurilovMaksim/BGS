# Independent audit of the uniform 7·5^e spectral candidate, version 1

Date: 2026-10-06.

**Normalized claim.** For every integer e≥1, the actual frozen generator A_(7·5^e) has simple complex spectrum. The operator is the raw-Weyl A of the canonical BGS model, transported by the already reviewed algebraic real-Jacobi similarity and the nonzero scalar normalization T=(200A_real−180I)/eta. No statement about U, other dimensions, the commutant, complex quantitative gaps, or BGS is under review.

**Primary verdict: incomplete, with the smallest missing implication identified below.** This verdict concerns the frozen version 1, not a subsequently repaired argument. No counterexample to actual A-simplicity was found. The exponent identities and a suitable *stronger* combinatorial invariant are sound. Version 1 does not establish the simultaneous, coefficientwise analytic invariant that is needed to apply those identities at the next depth. Its stated scalar bounds alone do not imply that invariant.

Frozen candidate: `source_snapshot/pure_five_uniform_cluster_candidate.md`, SHA-256 `b4eaac5b517cda99f259709eb38f2eedc51b7c7b82181363aba51112d2cece3e`.

Inherited bounded input: the independently reviewed A_175 argument, source hash `811dd1b7ef91ecddf46d203e81860c813e4aca020a22697a337e5a96071b9fc7`; prior audit hash `7d9853493c291e92ea9d2e4e058593523ef9d2f957d93c6f2b0d8e55c97db1c9`. Copies are in `source_snapshot/`. The finite-field certificates are inherited within that prior review's explicit boundary; this audit does not relabel their reuse as a new independent finite-field computation.

## 1. Dependency graph and precise scope

1. Actual A and algebraic real-Jacobi gauge → the normalized integral coefficient formulas. **Inherited reviewed input**, checked for consistency with this use.
2. Seven degree-five residue blocks → 35 distinct residue species with nonzero offset derivative. **Inherited exact finite input**.
3. Integral translation family and cyclic translation covariance → common analytic local branches. **Internal argument**, locally sound, but later restrictions require explicit charts.
4. Unit-gap species elimination → first scalar diagonal roots and weighted off-diagonal entries. **Internal Schur argument**, valid with coefficientwise Neumann expansion.
5. Simultaneous weighted cyclic-arc invariant at every narrower parameter depth → bounds H_r after digit elimination. **Missing formal induction in version 1**.
6. Coefficientwise self-energy bounds on centered two-variable domains → strictly contracting translation correction and nonvanishing spectral derivative. **Conditional on a correctly specified analytic induction**.
7. Equivariance on domains stable under the relevant shifts → exact higher-digit gaps. **Conditional on broad-domain/translated-chart compatibility**.
8. Nested disjoint spectral discs, Schur determinant identities and contractions → all N roots simple. **Valid consequence of 5–7**, not an independent substitute for them.
9. Nonzero local discriminant → nonzero algebraic and complex discriminant. **Valid elementary algebraic transfer**.

No external theorem is a new load-bearing leaf. The required facts can be proved by the stated integral power-series and Neumann/contraction arguments. No browser or external literature assertion was used to fill a gap.

## 2. What checks out

Write d_s=5^(s+1)−1. For Q of order 5^e and pi=Q−1,

- v_pi(5)=4·5^(e−1);
- v_pi([u]_Q)=5^v5(u)−1 for 5^e not dividing u;
- at u=5l, the normalized cut bond has valuation 2d_v5(l), with zero when appropriate;
- on y=pi^d_R u, the translated factor [5l]_Q+Q^(5l)y is coefficientwise divisible by pi^min(d_v5(l),d_R), including the zero-boundary case.

The remaining bond factors are units: the residue of q has odd order seven, so q^x+1 never reduces to zero; the fixed normalization factors are units. The seventh-root translation is integral and is the unique branch reducing to one. The composition law y⊕z=y+z+pi yz is exact. A shift by 35 preserves the length-five partition and its residue labels.

The original local eigenvalue branches have integral power series in y and unit derivative, using the accepted finite residue input. On y∈pi^4 O their pairwise translated values satisfy the exact isometry property. The first complementary inverse has only unit residue denominators; its walk expansion is coefficientwise convergent. A nontrivial first return requires two cut edges, giving valuation at least 16; on the pi^4 parameter ball the corresponding translation Lipschitz gain is at least 12. These margins are sufficient for the first diagonal normalization.

The arithmetic identities in version 1 are correct:

D_r=Σ_(s<r)4·5^(r−s−1)d_s=(4r−1)5^r+1,

56(r+1)5^r−D_r=H_r=(52r+57)5^r−1,

D_(r+1)=5D_r+4d_r,

2H_r−d_r−d_(r+1)=(104r+84)5^r>0.

Counting original cut edges in a *specified monotone interval* also gives the claimed cost. The problem is transporting that interval estimate through all dense, normalized Schur entries on the requisite smaller analytic ball.

## 3. The exact version-1 gap

The candidate's lines 71–85 assert the weighted estimate, derive its value for a straight original path, and then invoke the scalar lower bound H_s on current dense edges to erase detours. Lines 95–104 use those estimates to preserve the analytic diagonal and announce the next induction step.

Two stronger statements are needed there and are not stated or proved:

1. **Simultaneous smaller-ball control.** After s digit eliminations, the effective entries must retain their *individual original-cut weights on every ball pi^d_R O with R≥s*. The R=s+1 version is needed to recover the next high-cut contribution. Restricting an analytic entry already known only to be divisible by pi^H_s does not increase its divisibility. In fact,

   H_(s+1)−(5H_s−4d_s)=56·5^(s+1).

   This entire extra amount comes from a stronger invariant, not from H_s>d_s or positivity of coarse detours.

2. **Coefficientwise analytic control.** The weighted bounds, inverse-unit statements, and self-energy bounds must hold in one specified centered power-series/Gauss algebra, not merely at the arithmetic translation points or pointwise over the ground valuation ring. Otherwise the claimed Cauchy/Lipschitz inference is not justified.

These are linked: the first demands a two-index invariant; the second demands that it be proved in the analytic matrix algebra in which the contractions and root normalizations occur.

## 4. Exact diagnostic counterexamples to weaker implications

These examples are deliberately **not** actual A_N matrices and do not refute the normalized claim. They distinguish the invalid weaker implications from the stronger invariant that might repair them.

### 4.1 Scalar edge and denominator bounds do not recover H_1

Over F_5((pi)), take a six-site tridiagonal chain with every nearest-neighbor edge pi^56. Eliminate the four intermediate sites whose diagonal denominators are pi^4, 2pi^4, 3pi^4, 4pi^4. Thus the initial edge bound is H_0=56 and every eliminated denominator has valuation d_0=4.

The four-site complementary determinant is exactly

4pi^16+2pi^120+pi^224.

The off-diagonal Schur numerator between the endpoints is, up to sign, pi^280. Therefore the resulting entry has valuation 280−16=264=5H_0−4d_0, strictly below H_1=544.

This is an exact counterexample to deriving H_1 from the scalar hypotheses alone. It omits the high-cut information, exactly as the version-1 induction statement does. It is not a counterexample to an induction that explicitly retains those high-cut factors.

### 4.2 An unrestricted flattened raw-walk invariant is false

A proposed repair must keep returns resummed at their actual elimination level. One cannot expand the final inverse as unrestricted original walks and charge each visited removed site its eventual denominator d_v5(j−c).

For example, choose reference c=1, a high-level removed site j=126, and its neighbor 127. Their eventual denominator costs are d_3=624 and d_0=4. Choose the intervening seven cut indices to be 883,…,889, a legitimate seven-edge interval for this abstract weighted graph. Their total one-way cut cost is 96. The flattened two-way loop then has adjusted cost

2·96−624−4=−436.

Such a raw-walk geometric expansion does not converge. In the genuine stagewise elimination, the lower-level return has already been absorbed into the scalar diagonal before the 624-cost denominator is introduced. This is why levelwise resummation is essential. Version 1's warning against a global inverse is correct; a repaired invariant must not reintroduce that inverse implicitly.

### 4.3 Pointwise smallness is not a Gauss-norm estimate

The integral polynomial t^5−t maps Z_5 into 5Z_5, but its derivative 5t^4−1 is a unit everywhere and its Gauss norm is one. For a finite residue extension, replace 5 by its residue cardinality q. Thus pointwise divisibility on the valuation ring plus integral coefficients does not itself yield the claimed coefficient divisibility or Lipschitz gain.

In this problem the stronger coefficient divisibility looks obtainable directly from numerator factors, normalized denominators and Neumann series. It must actually be retained through the centered substitutions and diagonal root normalization.

The small exact script `check_induction_obstructions.py` verifies the displayed four-by-four determinant, valuations, loop arithmetic, the residue polynomial diagnostic, and twelve elementary exponent rows. It imports no candidate code and uses integer arithmetic modulo five. It does not construct or test any actual A_N, and the twelve rows are not offered as a uniform proof.

## 5. A precise combinatorial repair

The following is a sufficient replacement for the unqualified detour paragraph. It addresses the graph argument; it is not by itself the missing analytic theorem.

Fix a target cap R. Let S_s={k:k≡c mod 5^s}, with s≤R. For each interval I between adjacent S_s sites, define

E_s^(R)(I)=Σ_(original cuts in I) 2min(d_v5(l),d_R)−D_s.

Every such interval contains the same multiplicities of earlier removed digit classes, so its toll is exactly D_s. The raw edge count gives E_s^(R)(I)≥H_s. Let C_s^(R)(i,j) be the smaller of the sums of E_s^(R) along the two cyclic arcs joining distinct S_s sites i,j.

**Required invariant:** every off-diagonal effective entry, including after scalar row normalization, has coefficientwise valuation at least C_s^(R)(i,j).

At s=0, the first species-elimination expansion proves this: every complementary walk crosses one of the relevant original arcs, all residue-denominator costs are zero, and all original-edge loops have positive cost.

Assume the invariant at s and eliminate S_s\S_(s+1), whose denominators all have valuation d_s. In a Neumann term:

1. Replace each dense edge by an arc attaining its lower-bound cost C_s^(R).
2. Concatenate these arcs into a walk in the adjacent-S_s cycle.
3. Charge d_s also at every previously uncharged visit to an eliminated S_s site. This only decreases the cost. Charge nothing at S_(s+1) sites, even if an expanded dense edge passes through them.
4. Erase closed subwalks. Every such loop has positive adjusted cost because each elementary interval costs at least H_s>d_s, while each vertex visit is charged at most d_s.
5. The remaining simple path is one of the two cyclic arcs. Five old intervals combine into one new interval, with exactly four newly removed vertices. Since D_(s+1)=5D_s+4d_s, its cost is exactly E_(s+1)^(R).

This proves preservation of the invariant, provided it is applied to genuine convergent coefficientwise Schur expansions. In particular choose R=s+1, rather than merely restricting the naked R=s bound, to obtain H_(s+1). It avoids an unrestricted raw-walk inverse and handles dense edges, long arcs, backtracking and wraparound.

The argument remains valid with exact zero physical edges: treating them by finite lower weights only weakens a bound. At the last one-site cycle there is no off-diagonal estimate to establish.

## 6. Analytic obligations for the repair

A complete revised proof should construct the following objects and verify their compatibility.

### 6.1 Broad domains and covariance

At level s, construct the diagonal root functions for all sites in S_s on the broad translation ball pi^d_s O. A shift by 35·5^s m has translation parameter of valuation d_s in general; it preserves this broad ball but need not preserve pi^d_R O for R>s.

Prove covariance there using the permutation identity for the original analytic family, the chosen eliminated set, uniqueness of each scalar root, and normalization by the analytic diagonal unit. Then use restricted or translated charts for the finer weighted estimates. Do not apply covariance on a narrower ball that the shift leaves.

### 6.2 Centered two-variable domains

For each selected reference site and each R≥s, state an explicit coefficient algebra, for example the valuation ring's restricted algebra O⟨u,w⟩ with

y=pi^d_R u,

z=rho_(s,c)(y)+pi^(d_s+1)w.

Show that each previously removed diagonal factor is pi^d_j times a Gauss-analytic unit with constant nonzero residue, and that the old normalizing factors remain analytic units after this substitution. This is stronger than saying that its values have valuation d_j.

The estimates for different reference-site charts must refer to the same algebraic Schur complement. Either retain a broad parent spectral domain or explicitly identify translated charts; otherwise root covariance has no common object on which to act.

### 6.3 Contraction and factorization in the coefficient algebra

Use H_s>d_s for a matrix Neumann series in that algebra. The new diagonal self-energy has coefficientwise valuation at least B_s=2H_s−d_s. Its correction on y=pi^d_(s+1)u then has Lipschitz gain at least B_s−d_(s+1)>0.

A generic Gauss estimate on the displayed spectral chart gives the sufficient spectral derivative gain

B_s−d_s−1=2H_s−2d_s−1>0.

Version 1 states the slightly sharper 2H_s−2d_s. That can be proved by a direct derivative/resolvent calculation, but it is unnecessary: using the weaker chart bound avoids an extra hypothesis and still gives a strict contraction with ample margin.

The fixed-point construction must produce the root as a restricted analytic function in u, not only pointwise. Factor the diagonal equation as an analytic unit times rho_(s+1,c)(y)−z by the difference quotient, and verify that its inverse preserves every coefficientwise off-diagonal weight.

Finally verify that the correction is strictly Lipschitz on the broad next ball, including at translated boundary points. Comparing an original integral unit-derivative function plus a strict Lipschitz correction then gives the exact valuation of every deeper diagonal difference. A merely small absolute correction does not.

### 6.4 Termination

With these invariants, the final count is routine but should be explicit: each child spectral disc lies in the parent chart, distinct next-digit centers differ by valuation d_s, scalar corrections have greater valuation, every complementary determinant is nonzero, and each final Schur root has nonzero spectral derivative. Exactly 35·5^(e−1) distinct final roots exhaust the characteristic degree. The final parameter ball is used only for the scalar root; no fictitious further digit split is needed.

## 7. Obligation matrix

- Scope, actual operator and gauge: **passed within the inherited review boundary**.
- Cyclotomic cut valuations and analytic translation: **passed**.
- Fixed 35 residue species and offset derivative: **accepted bounded input**, not recomputed here.
- First unit-gap Schur estimate: **passed with coefficientwise expansion**.
- Exponent arithmetic and monotone original-edge count: **passed**.
- Version-1 implication from scalar H_s to weighted H_(s+1): **not established; scalar-only version refuted by the toy chain**.
- Levelwise cyclic-arc combinatorial repair: **proved above, conditional on the analytic matrix invariant**.
- Simultaneous coefficientwise (s,R) invariant for the actual matrix: **not addressed sufficiently in version 1**.
- Centered denominators, root factorization and Gauss norms: **conditional on the explicit domain induction**.
- Iterated covariance on appropriate broad domains: **conditional**, no contradiction found.
- Final root count: **conditional on those invariants**.
- Uniform actual A-simplicity: **incomplete in this frozen source**.
- A_175 reviewed theorem: **unaffected**.
- U-simplicity, other dimensions and BGS: **out of scope**.

## 8. Sources, reproduction and strongest safe conclusion

Applicable `BGS/AGENTS.md` and the source-of-truth hierarchy were followed. The canonical checkout was read-only throughout; it already had modifications and untracked work, which this audit did not change. Its HEAD at audit time was `41a2788ef21e787e983e88a8b58470d104013740`. No integration, commit, push, full build or formal proof verification was performed.

Reproduction from this audit directory:

    python3 check_induction_obstructions.py

`computation_manifest.json` records the exact finite diagnostic scope. `source_manifest.json` binds the reviewed source hashes and repository context. The authoritative candidate hash was checked before and after the audit.

The strongest safe conclusion is that the proposed mechanism survives the elementary exponent and weighted-graph tests, and the graph part has a clean levelwise repair. The frozen candidate does not yet prove the all-e theorem. The prior A_35/A_175 scope remains the accepted spectral result inherited here. The cheapest next step is a revised source containing the simultaneous coefficientwise domain-and-matrix induction above, followed by a fresh audit of that exact revision. More isolated N certificates would not decide this missing implication.
