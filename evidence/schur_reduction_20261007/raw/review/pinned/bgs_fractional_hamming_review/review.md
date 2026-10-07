# Independent audit: fixed-fraction Hamming cancellation

7 October 2026. Fresh-context internal mathematical audit. The canonical BGS repository and the author directory were read-only. This is an independent reconstruction with finite algebraic controls, not an external referee certificate or formal certification of the inherited analysis.

## Normalized claim and primary verdict

**Primary verdict: proved as written.** The frozen candidate's finite inequalities (1)–(3), exact orthogonal identities (4) and (16), and the actual-family consequences with their stated strict exponent margins are valid. This verdict inherits the accepted FM-021 position-chain estimate and explicit Haar tail, within their existing review boundaries. It does not independently re-prove the parametrix, TT* argument, or earlier probabilistic estimates.

The target is the exact candidate `inputs/candidate_v1.md`, SHA-256
`8feb1a9a402c679299fe060c3903f6d783a6e9939ad175bbf6a79dc0f9dde041`.
The author supplied that hash before this verdict. `input_manifest.json` preserves the candidate, earlier sparse theorem and review, repository instructions/status authorities, and analytic source snapshots.

For N≥2, m≥1, and 0≤r≤m, let E=End((C^N)^⊗m) carry ordinary unnormalized Hilbert–Schmidt structure. R is conjugation by a single full slot cycle; C_U is conjugation by U^⊗m. F_r is the literal coordinate-Hamming-at-most-r projector, Π is the occupation-balanced projector, and P_H is the full Haar invariant projector. Define

    P_r = Proj((I−P_H) ran(ΠF_r)),
    P̃_r = Proj((I−P_H) ran F_r),
    O_r = (I−Π)F_r,
    D = N²−1,  n=m−2r,  M=Σ_{s=0}^r binom(m,s),
    t=||P_U−J|| on traceless diagonals,
    a_n=E_Haar ||P_V−J||^n.

For n≥1 and M a_n<1, both P_r and P̃_r satisfy

    |Tr_E(R P C_U)| ≤ D M (t^n+a_n)/(1−M a_n).

For every n≥0, with 0^0 interpreted as 1 in this bound,

    |Tr_E(R O_r C_U)| ≤ 2 D M t^n.

The exact identity P̃_r=P_r+O_r holds for every radius, without any smallness assumption. The bound for P̃_r is proved directly using the unbalanced position blocks. It is not inferred by combining its split with the balanced estimate, which would give a weaker constant.

The actual balanced/all-centered fixed-fraction result requires BOTH

    h(δ)<(1−2δ)λ,   b h(δ)<1/160,
    λ=½ log(160/159),

on a fixed positive band aN≤m≤bN. Every positive δ satisfying these constraints works, with every strict c below

    γ=min{a[(1−2δ)λ−h(δ)], 1/160−b h(δ)}.

The off-charge estimate separately allows δ=1/6 from eventual t≤1/2, and δ=0.49 from eventual t≤10^−63. The latter conclusion applies only to O_r, not to the entire centered or balanced ball at that radius.

One non-load-bearing historical comparison should be corrected in maintained exposition: Section 6 says the advance is from “o(N/log N)” markers. The accepted sparse result already covers r≤κN/log N with an explicit positive κ. The accurate comparison is from that O(N/log N) range to a fixed positive fraction of m. This does not alter a hypothesis, conclusion, or proof in the frozen candidate.

## Evidence pinning and independence

Canonical HEAD when the inputs were frozen was `157277eeca8d8318976ea26bdbb1d3b1aa0d438a`; the repository already contained concurrent integration changes. The exact hashes, not that base commit or a claim of a clean worktree, define the audited sources. No canonical or author artifact was edited.

The critical proof was reconstructed before inspecting any new author implementation. The independent full-End controls construct Haar invariants as the simultaneous kernel of infinitesimal conjugation by all matrix units. This is different from the author's permutation-frame construction. The independent torus test uses a provably exact finite roots-of-unity average in its stated small range; the author uses Laurent coefficient extraction. Local p/q network tests retain the whole offdiagonal space and nontrivial N=3 traceless-diagonal space.

The actual source leaves are:

- `inputs/08_position_chain_mixing.md`, Sections 1–2, SHA-256 `3a589f988defb569d12f075add16dda669c9409dabd4a81f59c4d0b5d5e44b09`: limsup over odd N of ||P_N−J_N||≤10^−64 for the unchanged fixed-tau map. This implies every fixed eventual upper bound strictly larger than 10^−64, including 10^−63 and 1/2. It does not, by itself, imply eventual t≤10^−64.
- `inputs/09_ordered_diagonal_cyclic_trace.md`, O5, SHA-256 `54d6e6873b620a34523b96767e8229721800486a687016a48af08c06f2e16faf`: a_n≤ρ^n+4N²e^(−N/160), N≥20, ρ=√(159/160).
- The explicit tail source is also independently pinned as `inputs/collective_occupation_hierarchy.md`, Section 4, C9, SHA-256 `e1a7590ac0f572e3effd68ce0d783ced38f33e2c0c8bbc5939a2d40914fc373f`. Splitting the expectation using 0≤||T_V||≤1 gives the moment bound for every n≥1. No degree restriction from that source's different collective sum is imported into this elementary moment consequence.
- The accepted sparse-marker construction and its independent review are credited as prior work. Their color enumeration is not used as a surrogate for the new position-count argument.

There is no new external theorem leaf, stable-degree Schur–Weyl assumption, spectral universality assumption, or circular appeal to a desired trace limit.

## Dependency graph

1. Literal matrix units and torus characters → exact Π and raw Hamming projectors.
2. Identity/traceless local decomposition → support grading of F_r, Π, P_H, C_U, and both true centered range projectors.
3. One transitive slot cycle plus centering/off-charge removal → only full traceless support contributes.
4. Position-block orthogonality and p-to-p contractions → positive Haar compression norm ≤M a_n.
5. Exact centered inclusion and its genuine Gram → range-projector trace formula with B−H.
6. Normalized torus integrals, full-cycle trace contraction, shifted stage seam, and duplicated projections → a local D-dimensional trace bound with exactly M^k choices.
7. Independent Haar stages and the convergent Gram series → the two centered finite inequalities.
8. Difference of the two exact raw traces → off-charge finite inequality without a Haar denominator.
9. Orthogonal balance splitting before centering → P̃_r=P_r+O_r and the exact residual projectors.
10. Binomial entropy, accepted analytic inputs, and strict exponent slack → fixed-fraction conclusions and the original N^−2 compact-band aggregate.

## Obligation matrix

| Obligation | Verdict | Decisive point |
|---|---|---|
| Literal Hamming and occupation constraints | Passed | Both are diagonal masks on matrix units; repeated labels remain counted once. |
| Exact normalized torus projection | Passed | One common z per projector occurrence kills precisely nonzero total charge. |
| Different torus variables at successive occurrences | Passed | Each integral is a separate exact projector; no independence of slots is introduced. |
| Support grading of the true centered range | Passed | Centering preserves every exact support; orthogonal images on different supports remain orthogonal. |
| Proper-support and empty-support trace removal | Passed | Full-cycle fixed subsets are only empty/full; the empty support is killed by centering or I−Π. |
| Orthogonal position-block count | Passed | Π commutes with every J_S; ΠJ_S are orthogonal projections, some possibly zero. |
| Full-rank O and D0, rather than rank-one substitutes | Passed | Only operator norms and block counts are used; all local ranks are retained. |
| Haar Gram compression and positivity | Passed | K_S A K_T=Π(J_S A J_T)Π; block norms ≤a_n and positivity is inherited from P_H. |
| Genuine range inverse and noncommuting trace order | Passed | Y*Y=I−H and Y*C_UY=B−H; no [P_r,C_U]=0 assumption. |
| Exactly j+1 raw projectors in a series term | Passed | The duplicate endpoint is removed by trace cyclicity, K²=K, and [R,K]=0. |
| Shifted cyclic seam | Passed | Final stage joins the next slot's first projection; shift preserves marker cardinality. |
| Arbitrary torus phases at the seam | Passed | pD_z=D_zp=p; every other phase factor remains unitary. |
| Projection insertion | Passed | Equality of cyclic traces follows after duplicating and closing all projection endpoints. |
| Haar-stage versus slot independence | Passed | Independent draws only between stages; the same draw acts on every slot in its stage. |
| Dimension and normalization | Passed | Final ordinary trace is on V, so factor D, not D^m or N^m. |
| Direct all-centered bound | Passed | Repeat the proof with F and omit torus variables. |
| Off-charge raw identity and trace bound | Passed | O=F−ΠF after top reduction; each raw trace is bounded separately. |
| Full centered range split and residual | Passed | P_H annihilates off-charge vectors; balanced/off-charge images remain orthogonal. |
| Entropy, radius rounding and strict exponents | Passed | M≤e^(m h(δ)); r≤δm implies n≥m(1−2δ). |
| Actual 0.49 fraction | Passed | Uses eventual 10^−63, correctly deduced from the pinned limsup. |
| Original pair normalization | Passed | O(N) compact-band terms and N^−2 add only polynomial factors. |
| Earlier analytic proofs independently re-certified | Not addressed | Accepted source statements and interfaces checked; underlying parametrix/tail analysis inherited. |
| Entire high-Hamming complement, plateau and BGS | Out of scope | No conclusion for these follows. |

## Independent reconstruction of the load-bearing argument

### 1. Literal objects and full-support reduction

A matrix unit |x⟩⟨y| is a tensor product of E_(x_i,y_i). Its Hamming distance counts exactly the offdiagonal local factors. Under conjugation by diag(z_1,…,z_N)^⊗m it receives character ∏_i z_(x_i) conjugate(z_(y_i)). Its normalized torus integral equals one exactly when every label has the same total count in x and y, and zero otherwise. Thus Π is the genuine occupation-balanced projector, including all repeated labels.

The local identity/traceless decomposition End(C^N)=Ce⊕V gives orthogonal exact support spaces E_T. The diagonal algebra is Ce⊕D0, while O is already traceless. Expanding unmarked diagonal factors shows F_r preserves every E_T. Torus and unitary conjugation preserve identity and traceless spaces, so Π, C_U and P_H preserve them as well. Both centered range maps therefore send each raw support subspace into the same E_T. The corresponding true range projectors are support-diagonal even when a proper-support Gram is singular.

R moves E_T to E_(cycle(T)). The diagonal trace block on T vanishes unless T is a fixed subset of the full cycle. Such subsets are only empty and full; being on a shorter orbit under a power of R does not make a subset fixed under R. Empty support is the scalar and is removed by I−P_H or I−Π. Hence all three target traces equal their top-support traces on V^⊗m. No uniform invertibility on proper supports is needed.

### 2. Position blocks and the genuine Gram

On top support set J_S=⊗_i q_i at S and p_i elsewhere. The J_S are orthogonal projections with pairwise orthogonal ranges, because p and q are orthogonal. They need not have rank one. Their sum over |S|≤r is the exact top raw projector F. Each J_S commutes with diagonal conjugation and hence with Π, so K_S=ΠJ_S is itself a projection. Different K_S remain orthogonal; their sum is K=ΠF. Empty K_S may be retained in the index count M without harming a bound.

For any unitary V,

    ||J_S A_V^⊗m J_T||
      = ∏_i ||p_(S,i) A_V p_(T,i)||
      ≤ ||T_V||^(m−|S∪T|) ≤ ||T_V||^n.

There are at least n slots outside both marker sets; every other compression has norm at most one. Since Π commutes with J_S and J_T,

    K_S A_V^⊗m K_T = Π (J_S A_V^⊗m J_T) Π,

which costs no factor. Haar integration gives norm at most a_n for every block of H=K P_H K on ran K. For v=⊕_T v_T, blockwise triangle inequality and Cauchy–Schwarz give ||Hv||²≤M² a_n²||v||². Thus ||H||≤M a_n. Positivity/self-adjointness follow from the orthogonal projector P_H, not from individual stochastic matrices or tensor integrands. The same proof without Π applies to F P_H F.

When M a_n<1, Y=(I−P_H)|ran K has Y*Y=I−H>0. Its range projection is exactly Y(I−H)^−1Y*. Using RY=Yr, cyclicity, and C_U P_H=P_H C_U=P_H gives

    Tr_E(R P_r C_U)=Tr_ran K[r(I−H)^−1(B−H)],
    B=K A_U^⊗m K|ran K.

These identities remain valid without any commutation of the centered projection with C_U. The inverse is on the actual raw top range, not a redundant color/frame space.

### 3. Torus insertion and the local shifted seam

Write each K as a sum of position projections and a normalized torus integral. For k raw factors the same torus variable z_l occurs at all m slots of stage l; different stages have separate variables. A chosen integrand is the full-cycle trace of tensor factors

    X_i = p_(S1,i) D_(z1) A_1 … p_(Sk,i) D_(zk) A_k.

For the orientation taking a tensor tuple (v_1,…,v_m) to (v_2,…,v_m,v_1), Tr(R⊗_i X_i)=Tr(X_1…X_m). Reversing the cycle reverses the slot-block order, without reversing the order of stages within a block.

The exact trace-level insertion identity is

    Tr(Q_1 B_1 … Q_h B_h)
     =Tr[(Q_1 B_1 Q_2)(Q_2 B_2 Q_3)…(Q_h B_h Q_1)].

It follows by multiplying out Q_i²=Q_i and closing the last projection by cyclicity. This is the required statement; an equality of corresponding open matrix products would generally be false.

Here B is D_z A_l. Internal stage l joins p_(Sl,i) to p_(S(l+1),i). Stage k joins p_(Sk,i) to p_(S1,next(i)), which is a shifted marker set. For every stage the union of its two endpoint marker sets has at most 2r positions, including this last seam. At the at-least-n unmarked transitions,

    p D_z A_l p=p A_l p,

whose norm is ||T_(U_l)||. All other transitions have norm at most one because D_z and A_l are unitary. Therefore the absolute integrand is at most D∏_l ||T_(U_l)||^n, uniformly for arbitrary torus phases. Integrating normalized Haar measure costs no volume or dimension, and summing the M^k position choices proves the candidate's (14). With F instead of K the same argument omits the phases entirely.

### 4. The series, off-charge subtraction, and exact split

After expanding the genuine inverse, Tr(rH^jB) has j+1 copies of K. The formal embedding initially appears to have an extra endpoint K, but trace cyclicity, [R,K]=0 and K²=K remove that duplicate. Independent Haar variables occur between stages only. Applying the preceding bound then integrating gives

    |Tr(rH^jB)| ≤ D M^(j+1) a_n^j t^n,
    |Tr(rH^(j+1))| ≤ D M^(j+1) a_n^(j+1).

The two scalar series converge because M a_n<1. Their sum gives the exact stated fraction. The proof for P̃_r uses F directly and has the same constants.

For O_r, full-support reduction gives the projector F−K. Apply the one-stage bound to Tr(R F C_U) and Tr(R K C_U), then use the triangle inequality for their difference. This gives 2DMt^n for n≥0 without a Haar tail or denominator. It is a bound on these exact signed traces; no monotonicity of Tr(RPC_U) under projector inclusion is asserted.

Finally, before any support restriction, ran F_r is the orthogonal sum of its balanced and off-charge parts. Since ran P_H⊆ran Π, P_H vanishes on the latter. Thus I−P_H maps the two parts into orthogonal balanced and off-charge spaces and acts as identity on the second. Orthogonal range projections add, proving P̃_r=P_r+O_r. Likewise

    I−P_H−P̃_r=(Π−P_H−P_r)+[(I−Π)−O_r]

is an equality of orthogonal projectors with orthogonal summands. Nested raw balls stay nested after the same linear centering, so Q_r=P_r−P_0 is a genuine projector. These algebraic identities do not require the sufficient Gram estimate to hold.

### 5. Entropy, constants, and normalized aggregation

For 0<δ<1/2, let x=δ/(1−δ)<1. Since s≤r≤δm,

    M≤x^(−r)(1+x)^m≤x^(−δm)(1+x)^m=e^(m h(δ)).

Together with n≥m(1−2δ), the Haar input gives

    M a_n≤e^(−m[(1−2δ)λ−h(δ)])
            +4N²e^(m h(δ)−N/160).

The two strict constraints in the claim bound these terms uniformly by polynomial factors times e^(−γN). The t≤1/2 term is at least as good because log 2>λ. D is polynomial and the denominator tends to one. Every c<γ follows after absorbing these factors. Applying the bounds with an intermediate exponent between c and γ also absorbs the fixed factor two in the trace difference defining Q_r.

For the off-charge result only M t^n is needed. At δ=1/6,

    (1−2δ)log 2−h(δ)=log(3125/2916)/6>0.

For δ=49/100, eventual t≤10^−63 gives

    (1−2δ)63 log 10−h(δ)
       = (63/50)log 10−h(49/100)>0,

since h(49/100)<log 2<(63/50)log 10. These two estimates do not require an upper band or Haar conditioning. The stronger fixed-tau threshold remains non-effective; its mere existence is what the candidate claims.

On a fixed positive compact band, there are O(N) integer m. Multiplying by a bounded weight and N^−2 changes the bounds by only polynomial factors. With strict exponential slack the normalized complete contribution of each controlled sector remains exponentially small. The map, fixed coupling, basis, raw symbol, and origin convention are unchanged.

## Independent finite controls and reproduction

The authoritative execution record is `execution_manifest.json`; the detailed results are under `results/verified/`. Regenerate and validate from this directory with

    python run_review.py
    python validate_manifest.py execution_manifest.json --root .

The completed capped run took 149.86 seconds and passed all assertions. The run uses exact QQ(i) arithmetic, no tolerance or random sampling, Python 3.12.14 and SymPy 1.14.0. Its subprocess is capped at one CPU core, 3 GiB address space, 300 CPU seconds and 320 wall seconds; numerical thread environment caps are cooperative. Input before/after hashes and scientific output hashes are recorded.

1. **Literal full-End controls:** (N,m)=(2,1),(2,2),(2,3),(3,2), all radii 0≤r≤m. F and Π are constructed from literal local matrix-unit tuples; P_H is the common infinitesimal-commutant projector. Both centered projectors, the split P̃=P+O, nested differences, and residual projections are checked exactly. Every proper and empty support block has zero trace for P, P̃, and O. The N=2,m=3 Haar rank is 5, retaining the below-stable-degree dependence that a naive six-permutation inverse would miss. At r=2 the balanced/all-centered/off-charge ranks are 15, 51, and 36, and their traces are 2336/3125, 8224/15625, and −3456/15625. These obey the exact trace split.

2. **Nonsingular top Gram:** N=2,m=4,r=2 in the basis E01,E10,E00−E11, with the explicit local HS metric diag(1,1,2). The top Haar rank is 3. Balanced and all-Hamming top ranks are 13 and 33. Both Gram determinants are 8/135. The literal centered traces agree with the true Gram formula, respectively −31891/78125 and 204577/390625. Incorrectly using the raw projector minus P_H gives −314496/390625 and 49536/390625, respectively. This checks a nonvacuous inverse and rejects the raw-subtraction shortcut. Here n=0, so this test is not claimed to satisfy the theorem's sufficient smallness hypothesis.

3. **Exact torus projection and position blocks:** N=2,m=3 and N=3,m=2, all radii. The four roots of unity, with the global scalar phase fixed, exactly integrate the projector because each possible nonzero coordinate charge has magnitude at most m<4. This is a proved exact finite quadrature in that bounded range, not a torus sampling approximation. The literal charge mask, this average, and the sum of ΠJ_S agree. Local q has ranks 2 and 6; p has ranks 1 and 2. For N=3,m=2,r=2, there are M=4 position blocks and two nonzero balanced blocks; their ranks are not replaced by the block count.

4. **Arbitrary-phase, noncommuting-stage seams:** N=2,m=3 and N=3,m=2 with one, two and three stages, rational complex torus phases, and noncommuting conjugation matrices. Literal tensor trace, one-local-space cycle trace, and duplicated-projection contraction agree exactly. All tested incorrect unshifted seams instead give zero. One witness has the correct value 12096/78125. A separate orientation control gives forward trace 27 and backward trace 29, each matching the corresponding local product order.

5. **Nonvacuous off-charge inequalities:** N=2, m=1,…,6, every 0≤r≤floor(m/2), with t=7/25. The trace is summed literally over the selected top matrix-unit/diagonal basis terms and obeys 2DMt^(m−2r) in every tested case, including n=0 boundaries. These finite cases do not establish the universal bound; the proof above does.

The centered range oracle in the capped implementation uses the independent identity Proj((I−H)ran F)=F+Proj((I−F)ran H)−H for an orthogonal raw projector F and invariant projector H. Indeed ran(F)+ran(H)=ran(F)⊕(I−F)ran(H), while its orthogonal complement to ran H equals (I−H)ran F. This avoids inverting a large redundant column Gram. It is checked against direct centered column-space projection in the smallest dimensions. The top Gram test separately uses direct centered columns, so it does not reuse the candidate's inverse as its oracle.

One capped optimization attempt stopped during N=3 full-End checks because a DomainMatrix conversion rejected an unexpanded expression that was mathematically in QQ(i). This was a representation-conversion failure, not an assertion failure or counterexample. Its source, runner, failed manifest and traceback are retained in `failed_domain_conversion/`. The definitive source returns to explicit exact expression expansion between products.

A preliminary uncapped development run of the direct column-space version also passed. Its source was revised while that process was already executing to make the definitive run faster, so its results are retained only as exploratory output and are not the source-stable authoritative record. The subsequent capped run pins its source before and after and checks the same mathematical families. No finite result is used to promote the inherited analytic inputs.

## Remaining gap and strongest safe statement

There is no missing implication in the frozen candidate under its named accepted analytic inputs. The strongest safe conclusions are exactly the balanced/all-centered fixed-fraction estimate under both entropy constraints, the denominator-free off-charge estimate up to 0.49m using the conservative eventual bound 10^−63, the genuine residual Q_r estimate, and the exact orthogonal residual decomposition.

The unestimated balanced high-Hamming range and off-charge high-Hamming range remain. Neither projector inclusion nor a small norm of the classical stochastic matrix estimates their signed trace. The plateau correction, full pair residual, higher factorial hierarchy and deterministic BGS statement remain open. The next research step requires an argument for those remaining ranges, not another bounded replay or an extension of the 0.49 label to the balanced result.
