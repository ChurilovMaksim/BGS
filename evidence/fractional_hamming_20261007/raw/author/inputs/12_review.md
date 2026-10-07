# Independent audit: balanced coordinate-Hamming cyclic hierarchy

7 October 2026. Fresh-context internal mathematical audit. Canonical BGS and the author directory were read-only. This is neither an external referee certificate nor a formal analytic proof.

## Normalized claim and primary verdict

**Primary verdict: proved as written.** This verdict covers the frozen candidate and, separately, the frozen growth/dimension addendum. The universal finite-dimensional inequality is valid with exactly its stated sufficient hypotheses. Its actual-family application inherits the accepted eventual position-chain singular bound and explicit Haar tail; this audit does not newly certify the earlier parametrix analysis.

For integers N>=2, m>=1 and 0<=r<=m, use ordinary unnormalized Hilbert–Schmidt structure on E=End((C^N)^tensor m), the two-sided full slot cycle R=Ad(C_m), the conjugation C_U=Ad(U^tensor m), and the full Haar-invariant projector P_H. Let B_r be the literal span of balanced matrix units whose coordinate Hamming distance is at most r, and let P_r project orthogonally onto (I-P_H)B_r. With D=N^2-1, n=m-2r, t=||P_U-J|| on the traceless diagonal, a_n=E_Haar||P_V-J||^n, and the exact marker count L from the candidate, the audited bound is

    |Tr_E(R P_r C_U)| <= D L (t^n+a_n)/(1-L a_n),
    provided n>=1 and L a_n<1.

The separately audited balanced counting refinement gives L<=(r+1)(mN)^r. Thus, for the unchanged fixed-tau odd-dimensional U_N and every fixed 0<a<=b<infinity, set gamma_a=min{a log(1/rho),1/160}, rho=sqrt(159/160). For any fixed 0<kappa<gamma_a/2 and 0<c<gamma_a-2kappa, both P_r and the genuine residual projector Q_r=P_r-P_0 have cyclic trace at most exp(-cN), uniformly for aN<=m<=bN and 0<=r<=kappa N/log N, once N is sufficiently large. The original candidate's weaker constants with 3kappa are consequently also valid.

No conclusion about the complete balanced complement, off-charge sector, plateau, or signed higher factorial comparison follows. No asymptotic theorem is inferred from the finite computations below.

## Frozen evidence and independence

Target candidate: `inputs/candidate_v1.md`, SHA-256 `2ce67b8d33b574e5b245affd49f6592a9636b6075e4c288af8e718cc27c9404f`.

Separate addendum: `inputs/author/growth_addendum.md`, SHA-256 `966c31db09a3f50134d52ab63bba37b0d6d4e57a7fef521de5ab6d0deb111ae5`.

`input_manifest.json` freezes the candidate, repository instructions/status authorities and load-bearing accepted sources. `author_artifact_pin.json` freezes the author's scripts, outputs, logs and execution manifests; every one of the six file hashes declared by each author execution manifest was checked. Canonical HEAD at the initial observation was `157277eeca8d8318976ea26bdbb1d3b1aa0d438a`; the worktree was already dirty with concurrent integration. No canonical or author files were modified by this review. Artifact hashes, rather than that base label or the author's earlier clean-state observation, define the audited version. The final source check found all targets, author controls, and load-bearing proofs unchanged; five broad status/index files had changed during concurrent integration. Their initial snapshots remain preserved, and no newly integrated theorem or status is used in this audit.

The critical proof was derived before reading the author's implementations. The independent controls construct Haar invariants as exact common kernels of infinitesimal conjugation generators, whereas the author constructs an invariant frame from slot permutations. The independent top Gram test uses an equal-norm Pauli basis and invariant pairings, checked against the entire infinitesimal-rotation kernel. The author's implementations were subsequently inspected and reproduced separately. This is meaningful implementation independence, not a claim that two related model reviews supply a formal certificate.

## Dependency graph and scope

1. Literal balanced matrix units -> orthogonal marker-projector expansion -> exact traceless-support grading.
2. Support grading + a single transitive slot cycle + Haar removal -> only full traceless support contributes.
3. Haar average + local contraction bounds -> positive compression H with ||H||<=L a_n -> injective centered inclusion and the genuine Gram inverse.
4. Equivariance and C_U P_H=P_H -> exact range-projector trace formula.
5. Independent Haar stages + full-cycle tensor trace + shifted seam + duplicated projections -> D-dimensional product bound with j+1 marker choices.
6. Scalar geometric-series summation -> the finite inequality.
7. Accepted Haar tail + accepted actual singular gap + balanced list count -> growing-radius exponential conclusion and original N^-2 band normalization.
8. Nested centered ranges + torus balance -> the true orthogonal residual decomposition and difference estimate.

The only analytic inputs imported into this route are:

- `inputs/mathematics/position_chain_mixing.md`, Sections 1–2, SHA `3a589f988defb569d12f075add16dda669c9409dabd4a81f59c4d0b5d5e44b09`: eventual ||P_U_N-J||<=1/2 for the exact fixed-tau odd-N family. The model interface and inherited review were checked; its full parametrix/TT* proof is not independently re-proved here. No entrywise flatness estimate is used.
- `inputs/mathematics/collective_occupation_hierarchy.md`, Section 4, C9, SHA `e1a7590ac0f572e3effd68ce0d783ced38f33e2c0c8bbc5939a2d40914fc373f`: for N>=20, Pr(||T_V||>rho)<=4N^2 exp(-N/160). Since 0<=||T_V||<=1, splitting the expectation at rho gives a_n<=rho^n+4N^2 exp(-N/160) for every n>=1. No upper-degree restriction is required for this immediate moment consequence. The collective theorem's separate upper-degree summation restriction is not imported or removed.

`inputs/mathematics/ordered_diagonal_cyclic_trace.md` identifies P_0 with the accepted ordered-diagonal projector. Its inherited bound is consistent with the r=0 specialization; the candidate does not need to import its sharper dimension factor N-1.

There is no new external-source leaf, stable-degree Schur–Weyl assumption, or circular appeal to the desired spectral limit.

## Obligation matrix

| Obligation | Verdict | Reason |
|---|---|---|
| Literal once-counted balanced span and marker decomposition | Passed | Offdiagonal positions/ordered labels determine the marker uniquely; zero total charge is exactly occupation balance. |
| Repeated labels and arbitrary marker placement | Passed | Retained by the definition and the charge test; no distinctness or separation condition. |
| Exact support grading of the centered range | Passed | Local identity/traceless spaces reduce every conjugation and the raw projector; orthogonal centered ranges inherit the grading even on singular blocks. |
| Removal of every proper support | Passed | A transitive m-cycle fixes only the empty and full subsets; the empty centered range is zero. |
| Positivity, block bound and Gram injection | Passed | H compresses an orthogonal projection; L-block norm estimate gives ||H||<=L a_n<1. |
| Genuine range projector and noncommuting trace order | Passed | Y*(C_U)Y=B-H; Y*Y=I-H; no commutation of P_r with C_U is asserted. |
| Exactly j+1 projector-color factors | Passed | The repeated endpoint K is removed inside the cyclic trace using K^2=K and [R,K]=0. |
| Cycle orientation and shifted seam | Passed | Either orientation produces a single local trace; the last stage joins the next slot in that orientation. |
| Projection insertion and product-norm estimate | Passed | Duplicate every intervening projection and close the first one by trace cyclicity; all factors become compressed transitions. |
| Haar independence | Passed | Independent draws occur between stages only; the same draw is retained across all m slots in its stage. |
| No hidden replica dimension or normalization | Passed | The final ordinary trace is on V of dimension D, giving D rather than D^m. |
| Nested centered ranges and residual projector | Passed | Linear centering preserves inclusions; P_0<=P_r<=Pi-P_H. |
| Growing radius and improved counting constant | Passed | Original entropy is 3kappa N+o(N); balance improves it to 2kappa N+o(N). |
| Exact top new-sector dimension | Passed | Orthogonal tensor ranks add; Gram injectivity preserves this dimension on full support. |
| Original pair normalization | Passed | O(N) band terms under N^-2 weighting add at most a polynomial factor. |
| Actual parametrix input independently re-certified | Not addressed | Accepted input is pinned and its interface checked; its historical analytic proof remains inherited. |
| Full balanced/off-charge remainder, plateau, higher factorial/BGS | Out of scope | No bound for these is proved or used. |

## Decisive independent reconstruction

### 1. The subspace and its exact grading

Let local End(C^N)=Ce orthogonal-sum V, e=I/sqrt(N), and write the diagonal algebra as Ce orthogonal-sum D_0. Each offdiagonal E_ab is traceless and has torus charge e_a-e_b. In a matrix unit |x><y|, the changed coordinates determine the offdiagonal markers uniquely; all unchanged coordinates are diagonal. Occupation balance is exactly cancellation of the marker charges. Therefore the raw orthogonal projector is the sum over balanced marker choices, with rank-one E_ab factors at markers and full diagonal factors elsewhere. Different choices have orthogonal ranges because a differing marker position or color is locally orthogonal.

Expanding only the unmarked diagonal factors into Ce and D_0 exhibits the exact support decomposition. Every conjugation preserves Ce and V, so every support projector commutes with both C_U and P_H. It also commutes with the raw balanced-Hamming projector. Consequently each support component of (I-P_H)B_r is independent and orthogonal to the others, and its true range projector is support-diagonal. This reasoning requires no injectivity on proper-support components.

R sends support S to C_m S. The diagonal trace block on S can be nonzero only when C_m S=S. Transitivity of a full m-cycle leaves exactly empty/full support, regardless of shorter orbits of subsets under powers of R. Empty support is the scalar and is killed by I-P_H. Thus the full trace equals its full-traceless-support trace.

On that support each unmarked factor is the whole P_D0, not a rank-one surrogate. The marker expansion is exactly K=sum_alpha K_alpha with L choices, and is preserved by every slot permutation, in particular R.

### 2. Positive Haar compression and the exact trace formula

Let A_V=Ad(V)|_V. It is a unitary on the local Hilbert–Schmidt space. The compression P_D0 A_V P_D0 is P_V-J on D_0; each remaining projector-to-projector compression is a contraction. For fixed alpha,beta, at most 2r slots meet a marker on either side. Tensor operator-norm multiplicativity then gives

    ||K_alpha A_V^tensor m K_beta|| <= ||T_V||^(m-2r).

This uses ||T_V||<=1 to weaken the actual number of good slots to n. It is valid even with collisions between marker sets. Averaging yields block norms <=a_n. For the L-block orthogonal decomposition, Cauchy–Schwarz in the finite block index gives ||H||<=L a_n for H=K P_H K|ran K. H is positive and self-adjoint because P_H is an orthogonal projection; the individual A_V or T_V need not be positive, self-adjoint, or normal.

Under L a_n<1, Y=(I-P_H)|ran K has Y*Y=I-H>0. Its orthogonal range projector is Y(I-H)^-1Y*, with no scalar or frame normalization. Since RY=Yr on ran K, [r,H]=0 and C_U P_H=P_H C_U=P_H, cyclicity gives

    Tr(R P_r C_U) = Tr_ran K[r (I-H)^-1(B-H)],
    B=K A_U^tensor m K|ran K.

This justifies the ordered formula even though the centered projector need not commute with C_U. Only the top-support part is expressed using this inverse. Neumann expansion is legal in finite-dimensional operator norm and gives the two series in the candidate.

### 3. Endpoint count, cyclic orientation, and compressed transitions

For example, an H^j B term embedded in V^tensor m initially contains K A_1 K A_2 ... K A_j K A_U K. Its last K is removed within the trace: cycle it past R, use [R,K]=0 and K^2=K. Thus there are exactly j+1 independently expanded color choices. The H^(j+1) term has the same number. No deleted endpoint introduces a missing factor of L.

Choose an orientation in which the full-cycle identity reads Tr(R tensor_i X_i)=Tr(X_1...X_m); the opposite orientation reverses the slot-block order. Inside each X_i, the stage order remains unchanged. The final A_U in slot i is followed by p_(1,next(i)), not by p_(1,i).

Here is an explicit justification of the projection-insertion step. For any cyclic sequence of projections Q_1,...,Q_h and operators A_1,...,A_h,

    Tr(Q_1 A_1 Q_2 A_2 ... Q_h A_h)
      = Tr[(Q_1 A_1 Q_2)(Q_2 A_2 Q_3)...(Q_h A_h Q_1)].

Multiply out using Q_i^2=Q_i and then use trace cyclicity and Q_1^2=Q_1 to close the end. Therefore its absolute value is at most D times the product of all compressed-transition norms. This is an equality of traces, not an unjustified equality of open matrix products.

For each interior Haar stage, the bad slots lie in the union of its two adjacent marker sets and number at most 2r. At the last-stage seam, the second marker set is cyclically shifted; its size remains at most r, so the same bound applies. The product contains at least n good occurrences of each stage. All other compressions cost at most one. A single summand is consequently bounded by

    D t^n product_(ell=1)^j ||T_(V_ell)||^n.

The stage Haar variables are independent, while the m occurrences within a stage use the same variable. Integrating exactly gives a_n^j, not a factor obtained by pretending the slots independent. Summing L^(j+1) colors proves

    |Tr(r H^j B)| <= D L^(j+1) t^n a_n^j,
    |Tr(r H^(j+1))| <= D L^(j+1) a_n^(j+1).

The trace is now on local V, with dimension D=N^2-1; no N^m, D^m, or tensor multiplicity is omitted. Both scalar series converge absolutely because L a_n<1. Their geometric sum is exactly the candidate's bound.

### 4. Nesting and the authentic remainder

Raw inclusions B_0 subset B_r persist under the same linear map I-P_H. Hence the corresponding orthogonal projections satisfy P_0<=P_r and Q_r=P_r-P_0 is an orthogonal projector. Haar invariants are fixed by diagonal unitary conjugations and therefore lie in ran Pi; raw B_r is also balanced. Thus (I-P_H)B_r lies in ran(Pi-P_H), so P_r<=Pi-P_H.

It follows that Pi-P_H-P_r is an orthogonal projector orthogonal to Q_r, and

    Pi-P_H-P_0 = Q_r + (Pi-P_H-P_r).

These statements are true even where the sufficient top Gram bound fails. They do not identify Q_r with a raw path mask, K-P_H, or a sum of independently centered decorations. The exact controls below explicitly distinguish the true centered trace from the invalid raw-minus-Haar shortcut.

### 5. Uniform exponent, addendum, and top-sector dimension

For the original candidate, log L<=log(r+1)+r log(mN^2) <=(3kappa+o(1))N uniformly on the fixed band. Also n>=aN-o(N). The accepted tail gives a_n<=exp[-(gamma_a-o(1))N], including its polynomial bad-event factor; actual mixing gives t^n<=exp[-(a log 2-o(1))N]. Since gamma_a<=a log 2, the numerator, denominator and polynomial D yield the stated strict-slack exponent. There is no effective threshold assertion.

For the addendum, map a balanced length-s list to its source list (a_1,...,a_s) and a permutation matching the equal multisets of source/target labels. There are at most N^s source lists and s! permutations. Repeated labels create duplicate descriptions, which can only overcount, and dropping a_i!=b_i only enlarges the count. Therefore b_N(s)<=s! N^s, including s=0. Multiplying by binom(m,s) gives (m)_s N^s<=(mN)^s and hence L<=(r+1)(mN)^r. Uniformly on the same band this replaces 3kappa by 2kappa, with no change in the Gram or cyclic proof. For r_N=o(N/log N), every fixed c<gamma_a follows similarly.

For Q_r choose an intermediate exponent c' with c<c'<gamma_a-2kappa, apply the P_r and P_0 bounds with c', and absorb the fixed factor two. This avoids asserting that adding two exp(-cN) bounds preserves the identical threshold and exponent without slack.

Orthogonality of the raw marker summands gives exactly

    dim ran K = sum_(s<=r) binom(m,s)b_N(s)(N-1)^(m-s).

Whenever L a_n<1, the full-support centered map is injective, preserving that dimension. The nested ordered top-support range has dimension (N-1)^m, so subtraction gives the addendum's top Q_r dimension. At r=2 the new dimension is binom(m,2)N(N-1)^(m-1). No dimension formula for all proper supports is needed or claimed. The hierarchy is strictly enlarged at r=2 under this condition; r=0 and r=1 coincide with the ordered diagonal because b_N(1)=0.

Finally, for fixed bounded weight w supported in [a,b], there are O(N) contributing integer m. Hence N^-2 sum_m w(m/N)s_r(m) is bounded by a fixed polynomial multiple of the uniform exponential bound. The same holds for Q_r. The two-sided cyclic trace and ordinary unnormalized operator trace are the ones required by the original pair normalization; neither the origin average nor the fixed symbol/tau/basis is changed.

## Exact computation checks and commands

The complete successful bounded run is recorded by `execution_manifest.json` (schema 2), with input before/after hashes, declared result files, one-core affinity, 2 GiB address-space and 180-second CPU caps per subprocess, 200-second wall limit per subprocess, and single-thread numerical-library environment variables. Arithmetic was exact QQ or QQ(i), Python 3.12.14, SymPy 1.14.0. Regeneration:

    python run_review.py
    python validate_manifest.py execution_manifest.json --root .

The successful run took approximately 17 seconds in total. It contains:

1. **Independent literal full-End controls.** (N,m)=(2,1),(2,3),(3,2), every integer radius 0<=r<=m. The Haar projector is computed from the common kernel of all local-summed infinitesimal matrix-unit conjugations. Every tested centered range projector is orthogonal, Haar-orthogonal, cycle-equivariant and support-diagonal. Every proper-support cyclic trace vanishes; every nested difference and balanced remainder is a genuine orthogonal projector. For N=2,m=3, raw ranks at r=0/2 are 8/20 and centered ranks 7/15; exact traces are -343/15625 and 2336/3125. For N=3,m=2, raw ranks 9/15 and centered ranks 8/13 give exact traces 26/49 and 309/343.

2. **Independent nonsingular Gram control.** N=2,m=4,r=2 in the 81-dimensional full-traceless space. The raw top rank is 13 and Haar rank is 3. The compressed Haar eigenvalues are 7/15 once, 2/3 twice, and zero ten times, so det(I-H)=8/135. The literal centered trace and Gram formula both give -31891/78125. The incorrect raw K-P_H trace is -314496/390625. This is a nonvacuous Gram check; n=0 means it explicitly does not test inequality (1)'s sufficient hypothesis.

3. **Independent exact cyclic seam and full-color sums.** N=2,m=3,r=2, with 7, 49 and 343 terms for one, two and three noncommuting stages. The full tensor trace, all-color one-space contraction and duplicated-projector contraction agree. Pattern (D_0,E_01,E_10) gives correct trace 2592/15625 while the unshifted-seam shortcut gives zero. A separate nonsymmetric matrix triple gives opposite-orientation traces 43 and 61; the verifier checks each against the matching product order, so orientation is not silently washed out by commutative test data.

4. **Independent exact balanced counts.** For N=2,3,4 and s=0,...,4, the counts are respectively (1,0,2,0,6), (1,0,6,12,90), and (1,0,12,48,540). Each obeys the addendum's s!N^s bound. The general bound rests on the multiset argument, not these counts.

5. **Author replay, distinguished from independent tests.** Both author scripts were inspected and executed from frozen copies in a review-owned output directory. After removing only measured elapsed times, the full JSON results exactly match the pinned author outputs. This includes N=2,m=5,r=2 with nonsingular Gram determinant 64/729 and trace -8064967/9765625, and the exact three-term Neumann sum plus exact tail. Complete two-stage color sums contain 441 terms at N=2,m=5 and 361 terms at N=3,m=3. The N=3 control uses a rank-two D_0 projector, so it checks the distinction between marker count L=19 and raw top dimension 44.

The initial independent script lacked intermediate exact expression expansion in its complex-valued network products, causing avoidable symbolic-expression growth. It reached its explicit 240-second wall limit with exit status 124, after the full-End, top-Gram and counting tests but before producing a completed result. Its separate log/source and `initial_timeout_record.json` are retained; the successful version inserts exact algebraic expansion between 3-by-3 multiplications without changing the tested family or any mathematical assertion. The completed schema-2 run is the scientific execution record. No result from the incomplete initial run is promoted.

These are finite convention, implementation and failure-mode controls. They do not certify the actual large-N singular bound, Haar tail, or universal asymptotic conclusion by computation.

## Exact remaining gap and strongest safe conclusion

No missing implication remains in the audited sparse balanced-Hamming theorem under its named accepted analytic inputs. The strongest audited growth statement is the addendum's kappa<gamma_a/2, not merely the original kappa<gamma_a/3. It removes a precisely defined, genuinely enlarged Haar-centered balanced sector with the stated full-support dimension.

The unestimated projector is still Pi-P_H-P_r, together with the off-charge contribution I-Pi. Radius proportional to N, the complete decorated span, the plateau/torsion mechanism and signed higher factorial comparison remain open. The new argument requires only a mixing unitary and the fixed reference Haar law; it does not establish a universality criterion. The cheapest next scientific step is an explicitly new mechanism for the remaining high-Hamming projector, rather than a larger finite replay or a relabelling of this accepted sparse-sector estimate as a full complement bound.
