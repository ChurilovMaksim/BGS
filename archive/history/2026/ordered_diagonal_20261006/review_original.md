# Independent audit of the ordered-diagonal cyclic trace

6 October 2026. This is a fresh-context internal mathematical audit, read-only with respect to canonical BGS and the author route. It is not an external referee certificate or a formal proof.

## Verdict and exact claim

**Primary verdict: proved as written.** The claim is the specified ordered-diagonal sector, for every integer N >= 2 and m >= 1, with ordinary unnormalized Hilbert–Schmidt structure on the full ordered End((C^N)^tensor m). The cycle acts on both sides by conjugation. The exact formulas O1–O4 and O7 hold for every unitary U. With the inherited FM-021 singular bound for the unchanged fixed-tau family, O5–O6 yield, for each fixed a > 0 and all sufficiently large odd N,

    sup_(integer m >= aN) |s_ord(m,U_N)| <= 12 N^3 exp(-c_a N),
    c_a = min(a log 2, -a log sqrt(159/160), 1/160) > 0.

There is no upper restriction on m in this statement. It is exponential in N, uniformly in the displayed range, and is not an exponential-in-m theorem at fixed N. The explicit N=2 even-degree example confirms the latter boundary.

The actual-family application imports only FM-021's eventual ||P_N-J|| <= 1/2. It does not need that theorem's separate entrywise flatness estimate. I checked the pinned theorem, model, dependency interface and inherited review. I did not conduct a new complete independent certification of the old parametrix/oscillatory-kernel analytic proof. The new Haar conditioning and probability estimates are reconstructed below rather than accepted on the strength of an earlier verdict.

No estimate of the full balanced range, permutation-decorated enlargement, complete residual, higher factorial hierarchy, or BGS follows. The separate decorated notes are outside this audit.

## 1. Frozen source and dependency graph

The authoritative target is `bgs_ordered_diagonal_route/ordered_diagonal.md`, SHA-256

    ce254d3b6d937ec7232d7c10a3a9ab8a7e9909f18a7e8cae59acfc6cadd80307.

All seven entries of the author's `manifest.json` matched the supplied bytes. Its own SHA-256 is `f5cefa976406b5f248c760666e34552a578c25d2f729ed692dbbb0ed5cb5d3d4`. The review's `input_manifest.json` freezes 23 files, including instructions, current status authorities, the target, supplied evidence and the inherited analytic boundary. File hashes, not historical base labels, bind this review. At the final source check, 23:22:47 UTC, all 23 live source files still matched their frozen copies. Canonical HEAD was `801de3ab760cab4349e68b9843dcd67955314e62`; the pre-existing sole worktree modification was `.github/workflows/ci.yml`. These are time-stamped observations, not continuing assertions about that worktree. This audit made no canonical or author-route edits.

Load-bearing sources:

- `collective_hierarchy_v2.md`, SHA `cb09192dac743bd78fd21b76f6bd9d32c79050e4f616c7a04644e3f8c4c9c037`: Section 2, C4–C5, provides the full ordered tensor two-leg estimate before its restriction to symmetric tensors; Section 4, C9, provides the conditional-row Haar tail. Its C6 rank formula and C11 finite-degree sum are not used by the present theorem.
- Its prior independent review, SHA `3801a9aaa707704337ee63d2b45ec384150736e27d533d61152075805d800636`, and v2 confirmation, SHA `79a9379b8f91807d4ba8c34984dc1d10e1bc109ad2e0ba1111556bdb1f43306d`, are provenance, not substitutes for the reconstruction below.
- Canonical `position_chain_mixing.md`, SHA `3a589f988defb569d12f075add16dda669c9409dabd4a81f59c4d0b5d5e44b09`: Sections 1–2 state and prove limsup_(odd N -> infinity) ||P_N-J|| <= 10^-64 and hence the eventual 1/2 singular bound. The threshold is not effective.
- Its exact actual-model source `fixed_map_path_model.md`, SHA `d5365063f0967dabcac741a93c6f411d6402c913074944e1f9e383b2b5149b08`, and `four_branch_parametrix.md`, SHA `c696ebd39a52ca83205800a41fc30a9d570ebd3ed5dc96069f212948275600d7`, preserve U_N = exp(i tau N A_N) M_N at tau = 10^-80, through odd dimensions including composite ones. The inherited exact-model review and execution receipt are also pinned.
- The exact Haar-cycle identity is the same finite-dimensional Schur–Weyl/hook identity reconstructed in the prior residual review and in the pinned `balanced_kernel_plateau.md`, P4. No stable-degree Haar Gaussian moment matching is used. The derivation below includes the length cutoff at m > N.

Dependency chain:

    full ordered traceless-support grading + Haar orthogonal projection
      -> true centered Gram and exact dimension
      -> two-sided cyclic trace -> only the full support survives
    Haar fourth moments + two-leg Cauchy–Schwarz
      -> invertibility for every m, without a stable-degree cutoff
    independent Haar factors + tensor multiplication + cyclic trace
      -> exact matrix-product Neumann identity
    strict positive stochastic contraction + conditional Haar-row tail
      -> scalar absolute convergence -> O4/O5
    inherited actual FM-021 singular gap
      -> O6 uniformly over all m >= aN -> original N^-2 band aggregate
    torus balance + Haar hook trace
      -> exact orthogonal remainder O7, without any estimate of that remainder

There is no circular appeal to the desired deterministic spectral limit.

## 2. Full ordered space and support grading

The complex local operator space splits orthogonally as C I/sqrt(N) plus the traceless matrices. Tensoring this decomposition gives an orthogonal decomposition of the entire End((C^N)^tensor m) by exact support subsets S. The ordered diagonal space inherits the same splitting, with traceless diagonal factors in S.

For every V, conjugation by V in each slot fixes I/sqrt(N) and preserves tracelessness. Therefore every support subspace is reducing for Ad(V^tensor m); its Haar average also preserves each support. Compression to the diagonal has blocks

    B_S = T_U^tensor |S|,     H_S = E T_V^tensor |S|,

after ordering the occupied slots increasingly. The omitted identity slots have norm one, so there is no extra power of N. With unnormalized identities, the corresponding metric factor appears on both sides and cancels. This is an ordered tensor space, not End(Sym^m C^N), and not merely Sym^m(D_0).

The global scalar occupies S empty and is removed. All other S remain in D_c; their total dimension is N^m - 1.

## 3. Conditioning, genuine range projector, and trace order

H is positive and self-adjoint because it is a compression of the Haar orthogonal projection. Individual T_V need not be self-adjoint, positive, or normal.

For a Haar row, normalized independent complex Gaussian coordinates give

    E |V_ia|^4 = 2/[N(N+1)],
    E |V_ia|^2 |V_ib|^2 = 1/[N(N+1)]  (a != b).

Summing rows and removing J proves E(T* T) = I/(N+1) on D_0. Column symmetry gives E(T T*) = I/(N+1). A bistochastic matrix is an l2 contraction and constants reduce it, hence ||T|| <= 1.

For q >= 2 and a vector v in the full ordered D_0^tensor q, move the factor on one leg to the left in the quadratic form and retain a different leg on the right. All remaining legs are contractions. Cauchy–Schwarz in Haar measure then yields

    |E <v,T^tensor q v>| <= ||v||^2/(N+1).

Positivity of H_q upgrades this to 0 <= H_q <= I/(N+1). Also H_1 = 0, since E P_V = J. Thus every centered Gram block is bounded below by N/(N+1), establishing injectivity of Y and its claimed dimension in every degree.

Haar-invariant vectors are fixed by every C_U, so C_U P_H = P_H C_U = P_H. Expanding the two centered factors gives exactly

    Y*Y = I-H,      Y*C_U Y = B-H.

The true orthogonal range projector is Y(I-H)^(-1)Y*, not YY*. Since the slot conjugation R commutes with C_U and P_H, RY = Yr. Cyclicity of the finite-dimensional trace therefore gives

    Tr_E(R P_ord C_U)
      = Tr_Dc[(I-H)^(-1)Y*C_U RY]
      = Tr_Dc[r(I-H)^(-1)(B-H)].

No commutation of P_ord with C_U has been assumed.

The two factors after r preserve every S. The cycle sends S to c(S). A diagonal trace block can survive only when c(S)=S. For a single m-cycle, an invariant occupancy indicator must be constant around the entire cycle, so only the empty and full subsets qualify. The empty subset was removed. A proper subset may have a shorter orbit, such as {0,2} at m=4, but orbit length greater than one still has zero diagonal trace. This proves O2. A one-sided physical cycle would not implement this action on operator supports and cannot replace R.

## 4. Exact Neumann identity and all interchanges

For fixed finite N,m, ||H_m|| < 1, so its Neumann series converges in operator norm. Finite-dimensional trace is continuous. Each term may be written using independent Haar V_1,...,V_k:

    H_m^k = E[(T_1 ... T_k)^tensor m].

This uses multiplication of tensor products and independence entry by entry, not commutativity of the random matrices. For every matrix A on the d=N-1 dimensional D_0, direct index contraction gives

    Tr_(D_0^tensor m)(r A^tensor m) = Tr_(D_0)(A^m).

Either cycle orientation has the same value because every leg carries the same A. Consequently the actual part of the kth term is E Tr[(T_1 ... T_k T_U)^m]. The Haar subtraction starts at k=1 after the Neumann index is shifted. This proves O3 with exactly the displayed product order and no normalization by d or by d^m. One does not take an infinite random-matrix product.

Both scalar series are absolutely convergent. A Haar P_V has strictly positive entries almost surely. Strict Jensen contraction on the nonconstant subspace, followed by compactness of its unit sphere, implies ||T_V|| < 1 for every such matrix. Therefore a_m = E ||T_V||^m < 1. Independence gives

    E |Tr[(T_1 ... T_k T_U)^m]| <= d a_m^k ||T_U||^m,
    E |Tr[(T_1 ... T_k)^m]| <= d a_m^k.

Tonelli/dominated summation is thus legitimate even for the absolute values inside the expectations. Summing proves O4. The analytic identity itself also follows from the finite-dimensional operator-norm series before these improved scalar bounds are introduced.

At m=1, H_1=0. Each k>=1 expectation in the scalar expression is zero by independence and E T_j=0. This handles the minimum degree without inserting a spurious constant term.

## 5. Haar-tail constants and the unbounded upper range in m

The supplied tail proof can be made explicit using elementary exponential Markov bounds, with no independent-row assumption.

A Haar row is u=z/||z||, where X_j=|z_j|^2 are independent mean-one exponentials. The probability p=P(1<=X<=2)=e^-1-e^-2 exceeds 1/5. A half-mean Bernoulli bound puts at least N/10 such coordinates outside an event of probability e^(-N/40). The sum of the X_j is at most 2N outside probability e^(-N/4). For example the Markov parameter 1/2 gives exponent 1-log 2 > 1/4. On the good event there is I, |I|>=N/10, with |u_j|^2>=1/(2N) for j in I.

Conditional on u, a second Haar row is uniform on the complex sphere in u^perp, of dimension N-1. The subspace C^I intersect u^perp has complex dimension k >= |I|-1 >= N/20 for N>=20. In its Gaussian representation the squared norm in this subspace is Gamma(k,1), regardless of its orientation. Its lower tail below N/40 is bounded by the half-mean lower tail e^(-k/8) <= e^(-N/160). Here exponential Markov at parameter -1 gives exponent log 2 - 1/2 > 1/8. The total Gaussian norm is Gamma(N-1,1); its upper tail above 2N is bounded by e^(-N/8), even with a stronger exponent available. Numerator and denominator need not be independent for this union bound.

Thus, except on a conditional event of the stated probabilities,

    sum_(j in I) |v_j|^2 >= 1/80,
    sum_j |u_j|^2 |v_j|^2 >= 1/(160N).

Each distinct row pair has failure probability at most 4e^(-N/160). Union bounding over at most N^2 pairs gives the advertised factor 4N^2. Diagonal overlaps are always at least 1/N. On the resulting event,

    P P* = J/160 + (159/160) R_0,

where R_0 is symmetric nonnegative and doubly stochastic. Its l2 norm is at most one. Restriction to D_0 proves ||T|| <= rho = sqrt(159/160). The tail bound is valid even when its right side exceeds one at startup dimensions.

Since always ||T||<=1, splitting its mth moment by this event yields

    a_m <= rho^m + 4N^2 e^(-N/160)

for every integer m>=1. There is no sum over all degrees and no rank/dimension cost attached to the bad event. The finite upper cutoff needed in the different collective hierarchy's C11 argument is therefore unnecessary here.

## 6. Actual FM-021 input and large-N conclusion

The pinned actual family has fixed tau=10^-80 and odd N. FM-021 gives limsup ||P_N-J|| <= 10^-64, hence one eventual threshold with ||T_U_N|| <= 1/2. Its proof obtains an asymptotic operator bound; no threshold effective in tau or finite-N numerical certification is asserted. The normalized coordinate l2 convention of the model has the same induced matrix operator norm as ordinary l2, so no additional N factor enters this interface.

For a fixed a>0, every m>=aN satisfies

    ||T_U_N||^m <= e^(-a N log 2),
    rho^m <= e^(a N log rho).

The upper bound for a_m tends to zero uniformly over this entire half-line, so eventually 1/(1-a_m)<=2. Taking c_a as in the claim and d<=N gives

    |s_ord| <= 2N (2+4N^2)e^(-c_a N)
            <= 12N^3 e^(-c_a N).

The threshold can depend on a and on the inherited actual-model threshold, but not on m. This establishes the stated uniform quantifier. For a fixed bounded weight supported in [a,b] subset (0,infinity), the original N^-2 sum has O(N) terms and is at most a fixed polynomial in N times e^(-c_a N), hence exponentially small. A common spectral-origin phase cancels in C_U and leaves P_U unchanged, so the probability convention is preserved exactly.

At N=2, T_V=2X-1 is uniform on [-1,1]. Therefore H_m is zero for odd m and 1/(m+1) for even m. On the one-dimensional full support r=1, giving

    s_ord=t^m                 (m odd),
    s_ord=((m+1)t^m-1)/m     (m even).

For every fixed |t|<1 the even sequence is asymptotic to -1/m. For the exact Hadamard choice t=0 it equals -1/m identically at every even m. This is a genuine obstruction to a stronger fixed-N exponential claim; it does not contradict O6.

## 7. Exact residual and its scope

Every raw ordered diagonal operator is balanced under the diagonal torus. Every Haar-invariant operator is also torus-invariant. Hence the Haar-subtracted ordered sector lies in ran Pi and is orthogonal to ran P_H. Therefore

    P_H P_ord=0,      P_H+P_ord<=Pi,
    Q_ord=(Pi-P_H-P_ord)+(I-Pi)

is an orthogonal decomposition into the remaining balanced and off-charge ranges. All these projectors commute with the two-sided slot cycle. They need not commute with C_U.

Schur–Weyl decomposes the invariant operator space as the direct sum of End(Specht_lambda) over partitions lambda of m with length(lambda)<=N. Slot conjugation has trace |chi_lambda(c_m)|^2 on each summand. The m-cycle character is zero except on hooks (m-r,1^r), where it is (-1)^r. The allowed hooks number min(m,N), including the finite-N exclusion when m>N. Since C_U is the identity on the invariant space,

    |Tr U^m|^2 = min(m,N)+s_ord(m,U)+Tr(R Q_ord C_U).

This recovers O7 without replacing the actual U by a Haar matrix. Haar measure is used only to define its invariant projector. At m=1, the off-diagonal matrices lie in Q_ord while the cycle is the identity, so cycle-fixed residual vectors certainly remain.

The collective centered space is a subspace of this ordered centered space, since its symmetrized diagonal insertions were already in D_c. Its cycle-fixed trace can be canceled by the complementary cycle representation inside P_ord. Thus an O(1) collective contribution is compatible with the present exponentially small total ordered-sector trace.

No identification of these projectors with stationary-path masks has been established. The exact remaining target is still the signed, unnormalized trace on Q_ord, followed by the specified original weighted sum. Smallness of the removed sector alone gives no estimate of this target.

## 8. Obligation matrix

| Obligation | Status | Decisive reason |
| --- | --- | --- |
| Exact ordered operator space and ordinary HS normalization | Passed | Full tensor support reconstruction |
| Haar subtraction and true range Gram inverse | Passed | Y*Y=I-H and Y*C_UY=B-H |
| All-degree conditioning and injectivity | Passed | Two-leg fourth-moment argument on the unsymmetrized tensor space |
| Two-sided cyclic support cancellation | Passed | Only the full nonempty support is fixed |
| Independent product law and tensor trace reduction | Passed | Entrywise independence and exact finite index contraction |
| Neumann/expectation/sum interchanges | Passed | Operator-norm convergence plus d a_m^k absolute majorants |
| Strict a_m<1 and rare-Haar constants | Passed | Positive stochastic contraction and conditional row proof |
| Every m>=aN, without an upper band | Passed | Moment bound is pointwise in degree, denominator uniform |
| Actual unchanged fixed-tau application | Passed relative to named FM-021 input | Eventual 1/2 singular bound, odd N; no flatness input needed |
| New full certification of inherited FM-021 analytic proof | Not addressed | Pinned accepted theorem and inherited review, not re-proved here |
| N=2 even-m non-exponential control | Passed | Exact uniform[-1,1] moment calculation |
| Exact Haar term and orthogonal remainder | Passed | Hook cutoff and balanced subprojection algebra |
| Full balanced/decorated sectors and BGS | Out of scope | No bound on the complete residual |

## 9. Computation checks and provenance

The independent checker `checks/exact_ordered_check.py` starts from literal ordered-word slot-permutation matrices, selects an exact independent basis of their full finite-N span, and builds the Haar projector using its physical operator Gram. It then constructs the entire ordered diagonal space in a rational orthogonal but non-unit-normalized basis, removes Haar components, and retains the exact metric. It does not import the author's implementation or restrict the physical space to a symmetric power.

The completed suite `checks/bounded_suite.py` verifies:

- Literal full-End centered vectors, true Gram, direct actual two-sided cyclic trace, O1/O2 agreement, exact zero contribution of every proper support, and the Haar cycle trace for N=2 with m=1,...,4; N=3 with m=1,...,3; and N=4,m=2.
- Exact Gram conditioning in those cases, correct centered dimension N^m-1, balanced/off-charge ranks and nonnegative remaining balanced dimension. Every N=3 and N=4 fixture has nonnormal P. The N=3,m=2,3 and N=4,m=2 fixtures also have H_m B_m != B_m H_m, so no accidental commutativity is built into the finite controls.
- Two genuinely complex Q(i) full-End cases, N=2,m=3 and N=3,m=2, with adjoints rather than transposes in actual conjugation. The latter P is nonnormal.
- A separate exact physical-permutation Gram contraction for the unsymmetrized full-support N=3,m=4 block. It has dimension 16, rank 3 and spectrum 1/10 once, 1/20 twice, and zero thirteen times. The symmetric restriction has rank 1. Thus this test genuinely detects ordered, non-symmetric coefficient content beyond the previous collective hierarchy. This extra case checks the Haar block and its conditioning, not a new literal full-End actual-U trace at m=4.
- Finite Neumann partial sums through k=3 with their exact algebraic tail retained; noncommuting small matrix-product trace identities for m=1,...,4; and exact five-node rational cubature of the N=2 Haar scalar law through degree 5, with independently multiplied factors through k=3. No random sampling occurs.
- The N=2 even/odd trace formulas in the literal cases and the exact t=0 even-m value -1/m at m=2,4,6,8,10. Their all-degree validity rests on the uniform[-1,1] integral in Section 6.

The author's `check_ordered.py` and saved `checks.json` were separately replayed in all eight supplied cases. That code uses SVD, QR and floating linear algebra at tolerance 2e-10. Its data reproduce within that tolerance. This is replayed floating evidence, clearly distinct from the independent rational and Q(i) controls.

The completed bounded run took approximately 13.2 seconds for the suite. `checks/completed_run/manifest.json` records actual command, software versions, before/after input hashes, result hashes and enforced caps: 300 seconds wall time, 280 seconds per-process CPU, 2 GiB per-process virtual memory, one CPU affinity core, one cooperative numerical-library thread and 1 MiB combined logs. Both scientific result files were produced. The installed computation-audit validator passed with `--root` hash checks.

An initial attempt retained a substantially more expensive complete N=3,m=4 physical-space calculation and hit its 280-second CPU cap after printing completion of the eight smaller cases. Its status is **resource-limit**, not success; it produced no final scientific result file. That first script and receipt remain unchanged under `checks/provenance_run/`. The successful rerun uses the smaller exact permutation-trace contraction for the specifically stated m=4 Haar-block assertion. Both receipts validate as provenance records; only the second records successful completion.

Reproduction from this review directory:

    python3 <installed computation-audit>/scripts/run_experiment.py \
      --root . --contract checks/bounded_contract.json \
      --input checks/exact_ordered_check.py --input checks/bounded_suite.py \
      --input frozen/bgs_ordered_diagonal_route/check_ordered.py \
      --input frozen/bgs_ordered_diagonal_route/checks.json \
      --input frozen/bgs_ordered_diagonal_route/ordered_diagonal.md \
      --output checks/completed_run \
      --result checks/completed_run/results.json \
      --result checks/completed_run/author_floating_replay.json \
      --timeout 300 --max-output-bytes 1048576 \
      --max-memory-bytes 2147483648 --max-cpu-seconds 280 \
      --max-cores 1 --max-threads 1 -- python3 checks/bounded_suite.py

The output directory must be new: run this in a fresh copy without the existing completed_run output, preserving the original evidence. The actual installed runner location and argv are recorded in the receipt. No finite case or successful tool execution proves the universal or large-N statement; that conclusion comes from Sections 2–7 above.

## 10. Remaining gap and safe next use

No missing implication was identified inside the target O1–O7 at its stated scope. Its strongest safe use is removing precisely P_ord from the actual pair trace at an exponentially small cost in the original compact Heisenberg-band aggregate, with the inherited FM-021 dependency retained.

The unresolved part is exactly Tr(R Q_ord C_U), including both remaining balanced and off-charge contributions. Any enlargement must supply the correct overlapping-space projector or an equivalent trace identity and then estimate its own signed trace. The present result and finite controls do not justify summing separate sectors as though their ranges were orthogonal. More samples of the present ordered sector cannot close that missing implication.
