# Independent audit of the mixed and several-cycle ordered-diagonal interfaces

6 October 2026. Fresh-context mathematical audit, read-only with respect to canonical BGS and the author route. This is an independent internal review, not an external referee certificate or a formal proof.

## Normalized claim and verdict

**Primary verdict: proved as written.** For every finite N >= 2, ordinary unnormalized Hilbert–Schmidt space E = End((C^N)^tensor M), and the specified Haar-removed ordered-diagonal projection P_ord, formulas M1–M10 hold at their stated scope. The general two-sided interface has independent slot permutations on the ket and bra. The matched several-cycle interface uses common Haar draws across all selected cycles. The first mixed pattern has positive cycles of lengths l,r >= 2 and one negative cycle of length l+r.

Relative to the explicitly inherited FM-021 actual-family singular gap and the pinned accepted Haar tail, for each fixed a>0 and all sufficiently large odd N,

    sup_(integers l,r >= aN) |Tr_E(R_(sigma,pi) P_ord C_U_N)|
      <= 36 N^6 exp(-c_a N),
    c_a = min(a log 2, -a log sqrt(159/160), 1/160).

The threshold may depend on a and the unchanged fixed-tau model. There is no upper-length restriction. This is exponential in N, not a fixed-N exponential-in-length statement. Fixed-many matched cycles have the corresponding O_r(N^(r+2) exp(-c_a N)) bound when every cycle length is at least aN.

The conclusion removes one specified replica subspace only. The full factorial observable, short-cycle boundaries, the unestimated signed residual and BGS remain open.

Two supplied-evidence limitations do not invalidate the theorem: the separately supplied matched controls were omitted from the author's manifest, and the matrix Q=(I+2S)/3 in the author port checker is normal, contrary to its “nonnormal” comment. This review freezes the matched files independently and adds genuinely nonnormal Q controls.

## 1. Frozen sources and dependency boundary

The exact audited target is `bgs_mixed_ordered_interface/higher_cycle_interface.md`, SHA-256

    f9c7d5ace01782ff37f360e4e9d76afc117e2dca9f24fbe0e0b5f32276740304.

The author manifest itself has SHA-256 `9eba1cd3e3eac9e0ee5e2eae093163c79874c0509cc9a43805a1d62501d32846`; all seven entries matched their live sources at capture. The separate matched script and result were also frozen:

- `check_matched.py`: `da3df32a70a8f8b2f34db88d30cc165a21d2d2643f2ad32bd1476205920bf319`.
- `matched_checks.json`: `89f738b601037f63e34b0022fedc7a0276821b6e92bb3783cc2d401d27133cab`.

`input_manifest.json` pins 18 files, including the exact target, supplied computations and outputs, accepted dependencies and current repository instructions/status authorities. Copies are under `frozen/`. This review does not change any canonical or author source. The captured canonical HEAD was `157277eeca8d8318976ea26bdbb1d3b1aa0d438a`, with a clean worktree; these are capture-time observations. All 18 source files still matched their captured hashes at the final source check.

Only the following previously accepted mathematical inputs are inherited:

1. O1–O7 ordered-diagonal construction, SHA `ce254d3b6d937ec7232d7c10a3a9ab8a7e9909f18a7e8cae59acfc6cadd80307`, with its source-bound review SHA `2d781da069b408f505da78d9cdd60048fa14e20a13617dc6a1066aa3a089261f`. In particular, the full ordered support decomposition and the two-leg Haar fourth-moment bound imply centered Gram conditioning uniformly in replica degree.
2. The accepted Haar row-pair tail in `collective_hierarchy_v2.md`, SHA `cb09192dac743bd78fd21b76f6bd9d32c79050e4f616c7a04644e3f8c4c9c037`: a_q <= rho^q + 4N^2 exp(-N/160), N>=20, rho=sqrt(159/160).
3. Actual FM-021, `BGS/mathematics/position_chain_mixing.md`, SHA `3a589f988defb569d12f075add16dda669c9409dabd4a81f59c4d0b5d5e44b09`, Sections 1–2: the literal fixed tau=10^-80 odd-dimensional family has ||P_U_N-J|| <= 1/2 eventually. No new audit of its heavy analytic parametrix proof is claimed. Its separate entrywise flatness estimate and three-link marked-path estimate are not needed here.

Dependency graph:

    accepted ordered support grading and Gram conditioning
      -> general mixed compression M1 -> paired full-H series M2/M3
    matched slot action + tensor permutation trace identity
      -> shared-draw product M4 -> summed-degree bound M5
    literal two-cut contraction + unitary row orthogonality
      -> M6/M7 -> exact repeated-port scalar M8 -> remainder M9
    M3 with scalar cancellation before summation + independent draws
      -> M10 with three geometric denominators
    accepted Haar tail + actual FM-021 eventual singular gap
      -> uniform M11 and polynomially weighted long-long aggregates
    orthogonal projection algebra alone
      -> exact unestimated residual, without commutation with mixed R.

There is no appeal to a full factorial estimate or a desired spectral limit.

## 2. Normalizations and the general two-sided compression

The physical space W has dimension D=N^M. In E=End(W), the matrix units |x><y| are orthonormal for the ordinary unnormalized Hilbert–Schmidt inner product. The diagonal basis |x><x| is therefore orthonormal as well. The global unit identity is e=I/sqrt(D). Locally the identity is I/sqrt(N), so the exact support grading contributes no extra dimension factors on unoccupied slots.

Let C_U(X)=U^tensor M X (U*)^tensor M and R(X)=C_sigma X C_pi*. This R is a unitary superoperator, but is generally not conjugation and need not preserve either the diagonal algebra or its centered image. The slot matrices commute with every V^tensor M, hence R commutes with C_V and with the Haar orthogonal projector P_H. Also C_U P_H=P_H C_U=P_H.

On D_c=e^perp, Y=(I-P_H)i has Gram G=I-H, H=i*P_H i. The accepted supportwise bound gives ||H|D_c|| <=1/(N+1), including H_1=0, so Y is injective and the true range projector is Y G^(-1)Y*. Its dimension is N^M-1. It is essential to retain the Gram inverse.

Cyclic finite-dimensional trace, with no assumption about R preserving the range, gives

    Tr_E(R P_ord C_U)
       = Tr_Dc(G^(-1) Y* C_U R Y),
    Y* C_U R Y = i*(C_U R-P_H R)i = B_R-H_R.

This is M1. The full trace of R C_U is exactly the product of positive power traces indexed by sigma times conjugate power traces indexed by pi: Tr_End(L_A R_B)=Tr(A)Tr(B), followed by the ordinary tensor permutation contraction. There is no division by N, N^M or an invariant-space dimension.

Although R need not preserve D_c, the compressed difference Delta=B_R-H_R has zero scalar row and column. Indeed R(I)=C_sigma C_pi* lies in the Haar-invariant space, so C_U R(I)=R(I), proving Delta e=0. Applying the same argument to R* and C_U* proves e* Delta=0. Thus Delta=P_c Delta P_c.

Write H=P_0+H_c, with H_c zero on the scalar line. The convergent Neumann series is initially the one in H_c. For k>=1, H^k=P_0+H_c^k; its P_0 term annihilates Delta. The k=0 term is identical as well. This proves M2. Separating the two full-H series would wrongly retain an eigenvalue-one scalar contribution in each series and is not legitimate.

The identity H=E(P_V^tensor M) and independence give H^k=E(Q_k^tensor M), Q_k=P_V1 ... P_Vk. Separately H_R=E_V B_R(V), with the final Haar V independent of Q_k. This proves M3 term by term. For the cases under audit, the estimates below additionally justify absolute scalar summation after subtraction. At k=0, Q_0=I, and ||Q_0-J||=1 because N>=2.

## 3. Matched fixed-many cycles and shared draws

When sigma=pi, R is conjugation and does intertwine Y with the slot permutation on D_c. Both the actual diagonal compression and the Haar Gram preserve exact traceless support. A diagonal trace block can survive only if its occupied set is fixed by sigma, hence only if it is a union of complete cycles. Shorter nontrivial subset orbits do not contribute.

For a nonempty selected set I of cycles, write q_I=sum_(j in I) l_j. On the corresponding ordered D_0^tensor q_I space, direct tensor index contraction gives

    Tr(r_I A^tensor q_I) = product_(j in I) Tr(A^l_j).

The same matrix A appears on every leg. Substituting A=T_1 ... T_k T_U and A=T_1 ... T_k proves M4. There is one independent Haar draw per product index k, not one draw per cycle. This distinction remains essential even at N=2: for two one-cycles, the correct Haar scalar moment is E(z^2)=1/3, while using independent cycle draws would give (Ez)^2=0. For two two-cycles, E(z^4)=1/5 differs from (E z^2)^2=1/9.

For d=N-1 and any A, each |Tr(A^l)| <=d ||A||^l, without normality. Therefore the product is bounded by d^|I| times the q_I-th power of the common matrix-product norm. Independence across draws gives a_(q_I)^k, rather than a product of a_(l_j)'s. The two series are separately absolutely summable in this matched case, yielding exactly

    d^|I| (t^q_I+a_(q_I))/(1-a_(q_I)).

For fixed r, there are 2^r-1 nonempty choices of I. If every l_j>=aN, then q_I>=aN; the inherited moment tail gives a uniform denominator eventually >=1/2. Since |I|<=r, summing gives for example

    |s_R(U_N)| <= 12(2^r-1) N^(r+2) exp(-c_a N).

This explicitly supplies the constant implicit in the author's fixed-r statement. No upper bound on the lengths is used. If the positive and negative cycle types agree, a matched representative gives the same full trace product. Independently relabeling ket and bra also transports P_ord; it does not identify the untransported standard-diagonal contributions for two arbitrary differently labeled permutations.

## 4. Literal cut-port contraction and repeated labels

For sigma=(1 ... l)(l+1 ... M), pi=(1 ... M), M=l+r, a literal diagonal-basis expansion is

    F_Q(U)=sum_(x,y in [N]^M) product_i
       Q_(x_i,y_i) U_(y_sigma(i),x_i) conjugate(U_(y_pi(i),x_i)).

This follows from the stated C_sigma convention, not from replacing R by conjugation. At ordinary positions the two unitary row labels agree, producing K=P_U Q. At the two cut positions they differ, producing

    W_Q(a,c;b)=sum_x Q_(x,b) U_(a,x) conjugate(U_(c,x)).

Following the two resulting chains gives M6, including the indices (K^(l-1))_(b,a) and (K^(r-1))_(d,c). The order P_U Q is important; neither factor need commute or be normal.

Every a,c,b,d is summed freely, including repeated labels. Bistochasticity and unitarity give

    sum_b W_Q(a,c;b)=delta_(a,c),
    W_Q(a,a;b)=K_(a,b),
    |W_Q(a,c;b)| <= sqrt(K_(a,b)K_(c,b)) <=1.

The first identity uses row sums sum_b Q_(x,b)=1. The third is weighted Cauchy–Schwarz at fixed b and nonnegativity of Q.

Since K is bistochastic, T_K=K-J kills constants on both sides and K^L=J+T_K^L for L>=1. Also

    T_K=(P_U-J)(Q-J),
    ||T_K|| <= t ||Q-J||.

The lengths l,r>=2 are exactly what ensures both link exponents l-1,r-1 are positive. With both links replaced by J, summing b,d first gives

    N^-2 sum_(a,c) delta_(a,c) delta_(c,a)=1/N.

This is the repeated-port contribution. With the first link uniform and the second T_K^(r-1), the b sum forces a=c, giving

    (1/N) sum_(a,d) (T_K^(r-1))_(d,a) K_(a,d)
       =Tr(T_K^r)/N.

The J term vanishes because T_K^(r-1)J=0. The other single-uniform term gives Tr(T_K^l)/N. The double-centered term is exactly E_Q(U). These are all four terms of M8, with no omitted coincidences or normalization factors.

Every matrix entry of T_K^L is bounded in modulus by ||T_K||^L, whether or not T_K is normal. There are N^4 port choices and each W factor has modulus <=1. This proves M9 with exponent (l-1)+(r-1)=M-2 and prefactor N^4.

As a negative control, Q=J gives K=J and W_Q(a,c;b)=delta_(a,c)/N. Thus F_J(U)=1/N for every U and every l,r>=2. A distinct-port-only sum vanishes in this control and therefore cannot represent F_Q. The exact scalar cannot be discarded by a distinct-port orthogonality assertion.

## 5. Cancellation, exponents and constants

Because J reduces every stochastic factor,

    Q_k-J=T_1 ... T_k,
    ||Q_k-J|| <= product_j ||T_j||.

There is also an invariant-space explanation of the scalar: sigma pi^(-1) is a transposition, so <e,R e>=Tr(C_sigma C_pi*)/N^M=N^(M-1)/N^M=1/N. Consequently each of the two unsubtracted full-H kth traces tends to 1/N as k grows. Separate summation really would diverge.

The universal 1/N in M8 has no dependence on Q_k or U. It cancels inside F_Qk(U)-E_V F_Qk(V) for every k, including k=0, before either infinite series is separated. This is the necessary extra step beyond the marked distinct-port lemma.

For a centered trace term of exponent l, use |Tr(T_K^l)|<=d(t||Q_k-J||)^l. The coefficient is d/N, not N^M or d^M. The final independent Haar V replaces t^l by a_l. Averaging Q_k contributes a_l^k, so summing k yields (t^l+a_l)/(1-a_l). The r term is identical with r in place of l.

For the error term, the exact exponent is M-2. Its kth averaged majorant is

    N^4 (t^(M-2)+a_(M-2)) a_(M-2)^k.

This proves M10 with precisely its three denominators. A Haar unistochastic matrix has positive entries almost surely; strict Jensen contraction on nonconstant vectors and compactness imply ||T_V||<1 almost surely. Hence every a_q<1 for q>0, so all displayed denominators are positive. The resulting geometric majorants prove absolute convergence of the scalar difference series. None of these estimates requires the residual projector to commute with R.

For l,r>=aN and aN>=2, all three exponents l,r,M-2 are at least aN. With c_a as stated,

    t^q+a_q <= (2+4N^2) exp(-c_a N)

uniformly for these exponents. For sufficiently large N, each a_q<=1/2. Since d/N<=1, M10 is bounded by

    [4(2+4N^2)+2N^4(2+4N^2)] exp(-c_a N)
      =(8+16N^2+4N^4+8N^6) exp(-c_a N)
      <=36N^6 exp(-c_a N).

The constant 36 is therefore valid, albeit deliberately loose. The uniform range is unbounded above in l,r. A fixed compact Fourier support contains only polynomially many lattice pairs; multiplying by any fixed polynomial normalization and uniformly bounded weights retains exponential negligibility, provided the restriction l,r>=aN remains. A neighborhood of the axes, or one o(N) cycle, is not covered.

## 6. Exact residual and scope

The range of Y is orthogonal to the Haar-invariant range. Therefore P_H P_ord=0 and Q_res=I-P_H-P_ord is an orthogonal projector. Inserting this orthogonal decomposition into the full ordinary trace gives

    Tr_E(R C_U)=Tr_E(R P_H)+s_R(U)+Tr_E(R Q_res C_U).

C_U P_H=P_H is the only simplification used in the Haar term. This identity does not require any of the three projections to commute with C_U, and does not require P_ord or Q_res to commute with mixed R. In the mixed case, calling the remainder an invariant sector or a restriction of R to that range would generally be unjustified; the displayed cyclic trace is the precise valid object.

No estimate of Tr_E(R Q_res C_U) was supplied or deduced. No complete factorial partition transform, short-cycle boundary, stationary-path mask identification or BGS consequence follows. The accepted two-point ordered theorem and this mixed interface do not resolve the complete signed hierarchy.

## 7. Obligation matrix

| Obligation | Status | Evidence |
|---|---|---|
| Exact ordinary HS trace and normalized identities | Passed | Section 2 reconstruction |
| General mixed R, not conjugation | Passed | Literal two-sided definition and Section 4 contraction |
| True Gram projector without mixed range invariance | Passed | YG^-1Y* and cyclic trace |
| Scalar row and column cancellation | Passed | R(I), R*(I) Haar invariant |
| Full-H Neumann replacement and paired subtraction | Passed | Delta annihilates P_0 |
| Matched unions of whole cycles | Passed | Exact support permutation |
| Shared Haar draw across selected cycles | Passed | Tensor power expectation and summed-degree moments |
| All repeated cut ports retained | Passed | Exact 1/N and Q=J control |
| Nonnormal Q/P_U and multiplication order | Passed | K=P_U Q; no spectral-radius substitution |
| Exponents l,r,M-2 and their own denominators | Passed | Section 5 geometric majorants |
| 36 N^6 exponential constant, no upper cutoff | Passed relative to accepted inputs | Explicit polynomial domination |
| Uncommuting residual projection | Passed | Trace decomposition only |
| New full analytic certification of FM-021/Haar tail | Not addressed | Source-bound inherited inputs |
| Full factorial, short-cycle and BGS conclusions | Out of scope | Residual remains unestimated |

## 8. Exact finite controls and provenance

The independent implementation `checks/exact_mixed_fast.py` imports no author code. It starts from literal ordered words and their physical slot-permutation matrices. An exact independent basis of the finite-N permutation span is selected using its rational physical Gram; its inverse gives the Haar projection without a stable-degree assumption. The diagonal vectors E_x-E_last are deliberately not orthonormal, so their actual Gram is retained. Actual mixed action is applied as C_sigma U^tensor M X (U*)^tensor M C_pi*, with adjoints in genuinely complex fixtures.

Successful exact literal full-End controls include the following seven cases. The first four are recorded in `checks/small_physical_run/results.json`:

- N=2, positive cycles (1,1), negative cycle (2), Q(i) unitary: direct centered trace -414/625; the mixed range-noninvariance residual has entry 1/2.
- N=2, positive cycles (1,2), negative cycle (3), Q(i) unitary: direct centered trace -6661/31250; the range-noninvariance residual has entry -1/12.
- N=2, matched cycles (1,1): trace -589/625, agreeing with the exact shared-Haar scalar law.
- N=2, matched cycles (1,2): trace -10693/15625; all four non-fixed support blocks have exactly zero trace, and the union-support total agrees with the complete centered trace.

A separate successful matrix-free run, `checks/n2_m4_run/results.json`, reaches the actual long-long specialization and an additional fixed-many-cycle case:

- N=2, M=4, positive cycles (2,2), negative cycle (4), Q(i) unitary: trace -436297/937500. The physical invariant rank is 14, the centered Gram rank is 15, and an exact range-noninvariance residual entry is -5/144.
- N=2, matched cycles (2,2): trace -78681/78125, with all 12 non-fixed support blocks exactly zero.
- N=2, matched cycles (1,1,2): trace -125861/78125, with all eight non-fixed support blocks exactly zero.

All seven verify the true physical Gram compression and both scalar annihilation directions exactly. The complex fixtures lie in Q(i), not a floating approximation. The mixed cases of M=2,3 test the general M1 interface. The M=4 mixed case directly tests the l=r=2 specialization, which also has the independent literal rational port controls below.

`checks/ports_run/results.json` records independent direct ordered-word contractions and equality with both M6 and M8 for N=3, (l,r)=(2,2),(2,3), an N=3 Q=J control, and N=4,(l,r)=(2,2). The non-uniform Q is a rational convex combination of identity, cyclic shift and a transposition; exact matrix multiplication verifies Q is nonnormal. In the N=4 case P_U, Q and K=P_U Q are all nonnormal. Its full direct value is

    72750718667532754546/169340918007406640625,

while a distinct-four-ports-only value is

    -72155076325622/16725028939003125.

Thus retaining repeated ports is materially tested. For Q=J the direct answer is exactly 1/3 and the centered remainder exactly zero; the distinct-port value is zero. The code also checks the W row-orthogonality identity exactly.

The same successful file records N=2 shared-Haar moments for cycle lists (1,1), (2,2), (1,2,3), (2,3), (2,2,2), with one and two independent product draws. It uses the exact uniform[-1,1] scalar law, not Monte Carlo. It additionally verifies the tensor permutation trace identity for three lists with deliberately noncommuting local matrices and the actual matrix-product order.

The bounded small full-End run completed in about 1.34 seconds, the three N=2,M=4 cases in about 6.78 seconds, and the port/shared-draw run in about 4.55 seconds. Their runner manifests preserve actual timings, interpreter/library versions, commands, input hashes before/after, output hashes and effective caps. The runs used a 120-second wall cap, 110-second per-process CPU cap, 1 GiB per-process virtual memory, one affinity core, one cooperative thread and 1 MiB combined logs. All three exact-result manifests passed the installed computation-audit validator with project-root hash checks.

The author's scripts were separately replayed from frozen copies. All three exact port results reproduced verbatim. Three mixed full-End and two matched support outputs reproduced within 1e-10. These controls use SVD, QR and floating complex linear algebra, and are not relabeled as exact evidence. Their manifest is `checks/author_replay/manifest.json`; it also validated with input/output hash checks.

Two broader full-End suites, in `checks/completed_run/` and `checks/fast_run/`, reached their 480-second and 360-second wall caps respectively. Both have status **timeout**, and neither produced its declared final scientific-result file. Each log records completion of the three N=2,M=4 cases before the unfinished N=3,M=3 calculation. Their valid provenance manifests are preserved as failed full-suite receipts, not successful evidence. The first used unnecessarily large intermediate dense projectors; the second changed multiplication association to apply the small permutation Gram without forming those projectors. The separately completed N=2,M=4 run above supplies the accepted exact evidence for those three assertions. No exact full-End N=3 claim is made by this audit.

Reproduction of the successful exact control programs from a fresh copy of this review directory, preserving the original evidence:

    python3 checks/small_physical.py
    python3 checks/ports_shared.py
    python3 checks/n2_m4.py

These commands regenerate the scientific JSON at their declared paths in that fresh copy; to generate fresh provenance receipts, use the corresponding `checks/small_contract.json`, `checks/ports_contract.json` and `checks/n2_m4_contract.json` with the installed `run_experiment.py`, new output directories and matching adjusted result paths. Exact argv and actual installed runner locations are stored in the existing manifests. Never overwrite the existing evidence receipt to represent a new run.

Finite successes establish only their explicitly bounded assertions. The universal and large-N conclusions rest on the reconstructed proof in Sections 2–6 and its source-bound inherited inputs.

## 9. Remaining gap and safe use

No missing implication was found inside the frozen M1–M11 claim. The strongest safe use is deleting the specified ordered-diagonal contribution in the matched fixed-many long-cycle and the two-positive/one-negative long-long presentations, while retaining the exact unestimated complement. The next genuinely different obligation is an estimate of that complement or of the short-cycle boundary; more samples of this same subspace cannot provide either.

## Portable replay boundary

The maintained entry replays the successful exact finite controls only.
Historical480s/360s mixed-suite timeouts remain explicitly failed receipts;
their partial logs do not certify N3 full-End cases. The original normal
circulant fixture label is preserved historically; genuinely nonnormal Q
fixtures are independently checked exactly in the promoted controls.
