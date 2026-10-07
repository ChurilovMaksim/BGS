# Independent audit: fixed-order factorial removal of the ordered-diagonal sector

6 October 2026. Fresh-context internal mathematical audit. The author route and canonical BGS repository were read-only throughout. This is not an external referee certificate or a formal proof.

## Normalized claim and primary verdict

**Primary verdict: proved as written.** For every integer N >= 2, every unitary U with N max|U_ab|^2 <= C, and every canonical positive/negative consecutive-cycle presentation with positive lengths and equal total M >= 1, the specified Haar-removed ordered-diagonal trace obeys

    |Tr_E(R P_ord C_U)| <= C_(h,C) (1+log N)^(2h),

where h is the number of distinct positive/negative interval endpoints. The constant is independent of M and every individual cycle length. For every fixed k >= 2 and bounded compactly supported Fourier weight, the complete sum of these specified ordered-diagonal terms in the exact partition/Möbius expansion is O_(k,weight,C)((1+log N)^(2k)/N).

The statement under entrywise flatness is proved here without a position-chain spectral-gap assumption. The application to the actual fixed-tau quantization retains the accepted actual entrywise-flatness input, through odd N >= 3 as N tends to infinity. This audit does not independently re-prove that inherited analytic parametrix. No implication to the remaining signed factorial complement or BGS is supplied.

The final target is `general_fixed_order_v2.md`, SHA-256 `5995e81f5a89f6f1ec28cfaa5eaa341c3f6fc9493d02a6b7aa0787da5872defb`. The initial target is preserved as `general_fixed_order.md`, SHA-256 `df94ed1b369895820b2200ccb04b04a82c320eccaa1d01098c2eda7e94efa9a7`. The exact delta, SHA-256 `32c74a691c9e04ad93df63a433d13a49f929747738f7013fe11e13cb8c8302da`, inserts only an explicit explanation that the cut set meets every common closed cycle. It changes no object, formula, assumption, bound, or conclusion. Both versions are mathematically valid; v2 makes an important implicit point explicit.

## 1. Authority, pins, and dependency graph

The source repository was at `157277eeca8d8318976ea26bdbb1d3b1aa0d438a`, with no reported local changes when checked. `AGENTS.md`, `SOURCE_OF_TRUTH.md`, conventions, RESEARCH, the relevant claim ledger/registry and results/open-question entries were inspected. TRACE-005 and fixed-map BGS remain open. There is no local `.mathbox` ledger in the source repository. This review does not edit canonical claim status.

Every file in `general_v2_manifest.json` was read and its hash verified before copying it to `frozen/`. Both manifests, the original target and the exact delta are preserved. Additional actual-model pins are:

- `fixed_map_path_model.md`: `d5365063f0967dabcac741a93c6f411d6402c913074944e1f9e383b2b5149b08`.
- `four_branch_parametrix.md`: `c696ebd39a52ca83205800a41fc30a9d570ebd3ed5dc96069f212948275600d7`.

The load-bearing chain is:

1. Full ordered traceless-support decomposition and elementary Haar fourth-entry moments -> all-degree Gram conditioning.
2. True range projector and non-conjugating two-sided permutation compression -> exact centered Neumann identity.
3. Canonical interval cycles and complete cut set -> finite open-string network, including zero strings.
4. Entrywise flatness -> O(C^(2h)) network bound; exact scalar cancellation plus an M-independent continuity estimate -> a tail controlled by products of Haar stochastic compressions.
5. Exact independent-product second moments -> a fixed cutoff; an elementary maximum-entry Haar tail -> O(log^(2h) N) beginning.
6. Exact Möbius/Fourier normalization and independent zero-power hyperplanes -> O(log^(2k) N/N) full fixed-k sector aggregate.
7. Accepted actual entrywise flatness -> actual fixed-tau application.

Steps 1–6 are reconstructed below. The Haar facts are proved by normalized Gaussian vectors and elementary conditional expectations. No additional external estimate, spectral-universality theorem, representation-uniform gap, or mixing hypothesis is imported.

## 2. Exact non-conjugating compression

Let W=(C^N)^tensor M, E=End(W), and D be the full ordered diagonal algebra with ordinary unnormalized Hilbert–Schmidt metric. The normalized global identity e has norm one. Decompose each local operator space into the identity and traceless summands, and tensor this decomposition over all ordered slots. Conjugation by V in every slot preserves every exact support S. On the diagonal support of size q, Haar compression is E T_V^tensor q, where T_V=P_V-J on the traceless diagonal space. Identity factors have norm one and introduce no extra N.

For a Haar row, Gaussian normalization gives E|V_ia|^4=2/[N(N+1)] and E|V_ia|^2|V_ib|^2=1/[N(N+1)] for a != b. Thus E(T* T)=E(T T*)=I/(N+1) on the mean-zero space. Every bistochastic P is an l2 contraction and has reducing constant subspace, hence ||T|| <= 1.

For q >= 2, in a quadratic form of T^tensor q move the factor on the first leg to the first vector and retain the second-leg factor on the second vector; the remaining legs are contractions. Cauchy–Schwarz over Haar measure bounds the absolute expected quadratic form by ||v||^2/(N+1). Positivity follows from compression of the orthogonal Haar projector. The q=1 compression vanishes. Therefore 0 <= H_c <= I/(N+1) on the entire centered ordered space, uniformly in M. The inverse is the genuine range Gram inverse, not an unweighted YY* substitute.

R(X)=C_sigma X C_pi* is unitary on E. It commutes with every simultaneous conjugation, so with C_U and P_H; it generally does not preserve D or P_ord. With Y=(I-P_H)i restricted to e-perp,

    Y*Y=I-H,
    Y*C_U RY=i*(C_U R-P_H R)i.

Cyclic trace, with its order preserved, gives exactly

    Tr_E(R YG^-1Y* C_U)=Tr_(e-perp)(G^-1(B_R-H_R)).

Both the e column and e row of D_R=B_R-H_R vanish: R(I) and R*(I) are slot permutation matrices and are fixed by every simultaneous conjugation. The expression therefore extends to all D using (I-H_c)^-1. This verifies G1 without assuming R-invariance of P_ord.

The convergent series is the H_c series. H=P_0+H_c, with P_0 H_c=0, and P_0D_R=D_RP_0=0. Consequently H_c^j may be replaced by H^j inside these traces, including j=0. Since H=E P_V^tensor M, independence gives H^j=E(Q_j^tensor M), in the stated product order. Also H_R=E B_R(V). The last V is independent. This proves G2. The two full-H series are not independently summed, and the invariant scalar is canceled inside each summand.

## 3. Canonical network and boundary cases

The positive and negative cycle lengths are strictly positive, each family has total M, and their interval endpoints include M. At every noncut position i, both permutations send i to i+1. Deleting the union of endpoint edges leaves exactly the intervals [e_(j-1)+1,e_j] as directed open strings. Every positive cycle has its endpoint deleted, so no common closed cycle survives. In particular, a completely matched cycle is still cut at its endpoint and contributes one string and one cut, not an unlisted loop factor.

Every cut image is one of the listed starts. Since sigma and pi are bijections and the internal noncut edges already account for every nonstart destination, their cut images each visit all starts once. Hence alpha and beta are genuine permutations, including adjacent endpoints and singleton cycles.

A literal diagonal-basis calculation gives

    B_R(U)_(y,x)=product_i U_(y_sigma(i),x_i) conjugate(U_(y_pi(i),x_i)).

The trace against Q^tensor M supplies product_i Q_(x_i,y_i). Summing each x_i gives W_Q. Internal common edges give K_(y_(i+1),y_i); summing their intermediate y values gives (K^L)_(b,a), with exactly the orientation in G3. This works for complex U and nonnormal Q without rearranging matrix products.

For L=0 there are no common edges and no interior sum. Start and end are the same vertex, represented by delta_(b,a). This is an identity matrix, never J. All values of the ports are retained, including repeated values. A delta for string j identifies its own b_j with a_j and removes one independent b variable, even when other a values happen to coincide. Thus z zero strings leave exactly 2h-z free summation indices.

Flatness gives K_ab <= C/N by the column sums of Q. Positive powers retain that entry bound because they multiply nonnegative bistochastic matrices. Weighted Cauchy–Schwarz gives |W_Q(a,c;b)| <= sqrt(K_ab K_cb) <= C/N. There are h cut factors and h-z nonzero-length links. The sum therefore has at most N^(2h-z) terms, each bounded by (C/N)^(2h-z), proving G4. No independent label-distinctness condition or residual closed-loop factor is missing.

## 4. Exact common scalar, continuity, and fixed tail

J^tensor M is precisely |e><e| on D. Hence

    F_J(U)=<e,B_R(U)e>=N^-M Tr_W(C_sigma C_pi*),

which is N^(cycles(sigma pi^-1)-M), independent of U. This proves scalar cancellation regardless of short or zero-length strings. At the network level W_J(a,c;b)=delta_(a,c)/N. Compressing all common strings preserves cycles minus vertices and gives the equivalent exponent cycles(alpha beta^-1)-h. No claim that a uniform link kills every repeated-port term is used.

For Delta=Q-J, both Delta and T_U=P_U-J are contractions and annihilate constants. For L>=1,

    K^L-J=(T_U Delta)^L,
    ||K^L-J|| <= ||Delta||^L <= ||Delta||.

The last inequality uses ||Delta||<=1. For a cut factor, Cauchy–Schwarz pairs a column of Delta with the vector (U_ax conjugate(U_cx))_x. Its l2 norm is at most one, so each cut difference is bounded by ||Delta||. All unchanged factors have absolute value at most one. Telescoping only the h cut factors and h-z positive-length link factors, leaving the z identity deltas untouched, gives G6 with the looser count 2h N^(2h). Its independence of M is genuine. Taking the difference between U and an independent Haar V costs 4h N^(2h)||Delta||.

For j>=1, Q_j-J=T_1...T_j. Conditional expectation of the first factor in

    Tr(T_j* ... T_1* T_1 ... T_j)

gives (N+1)^-1 times the same expression with that factor removed. Repetition yields E||Q_j-J||_HS^2=(N-1)/(N+1)^j exactly. Operator norm is at most HS norm and Jensen gives G7. At j=0, ||I-J||=1 <=sqrt(N-1), valid even at N=2.

With L=4h+4, the absolute tail is at most

    [4h/(1-1/sqrt(3))] N^-3/2.

Indeed sqrt(N-1)<=sqrt(N), (N+1)^(-L/2)<=N^(-2h-2), and the geometric denominator is uniformly bounded below for N>=2. There is no M cost or hidden replica dimension in this tail.

For the beginning, Y_N=N max|V_ab|^2 has tail bounded by N^2 exp(-t/2), since the exact one-entry tail is (1-t/N)^(N-1) when 0<=t<=N and zero thereafter. Thus Z=(Y_N-4log N)_+ has tail at most exp(-u/2), giving E Z^p <=2^p p!. Minkowski proves G10. Apply G4 to each Haar V with its random flatness constant Y_N, regardless of the independent Q_j. There are only 4h+4 beginning terms. This establishes G11 and G12, uniformly for all positive lengths, including M=1 and all singleton cycles.

Haar variables here implement the exact invariant projector and Gram inverse. They neither replace U by a random matrix nor replace its dynamics by a stochastic process.

## 5. Complete fixed-k factorial aggregation

The normalization N^-k is the exact product of the 1/N anchor normalization and the N^-(k-1) Fourier periodization factor. The partition coefficient is product_B (-1)^(|B|-1)(|B|-1)!. The identity holds before any estimates, with m_k=-sum_(a<k)m_a.

For a partition with b blocks, T_U(0)=N is extracted exactly once for each of the z zero block powers. If any nonzero powers remain, zero total forces at least two of them, one positive and one negative. Their lengths define M>=1 and the canonical mixed presentation. The full trace identity is the trace of left multiplication by C_sigma U^tensor M and right multiplication by (C_pi U^tensor M)*, hence the indicated product of positive traces and conjugate negative traces.

For a selected proper subset of z zero blocks, the block indicators are disjoint. A linear combination of them equal to a multiple of the total indicator must have that multiple zero, by evaluating on an omitted block, and then every coefficient zero by evaluating on its own block. Thus the z forms are independent on the zero-total frequency space. Here at least two blocks are omitted. In the original k-1 integer coordinates, the matrix has rank z. Choose a nonsingular z-column minor. Each assignment to the remaining k-1-z coordinates determines at most one value of the selected pivot coordinates. All coordinates lie in a fixed O(N) box by compact Fourier support, so the lattice count is O(N^(k-1-z)). Nonzero restrictions on the other blocks only remove points.

There are h<=b-z<=k cuts. The sector estimate is uniform in each lattice point, so absolute values may now be taken for this sector:

    N^-k * N^z * O(N^(k-1-z)) * O((1+log N)^(2k))
      = O((1+log N)^(2k)/N).

The number of partitions and zero/nonzero strata and their Möbius coefficients are bounded in terms of fixed k. Boundedness of the Fourier weight handles its magnitude. Summation proves G14. This sectorwise absolute bound does not introduce the prohibited all-order absolute comparison of the full deterministic observable.

If all b block powers vanish, the product is exactly N^b, and there is no nonzero replica degree: M=0. Assigning its ordered-diagonal contribution zero is consistent, since in degree zero the entire operator space is already Haar-invariant. These constant terms are retained in the exact factorial expression; they are not asserted negligible. Their all-zero equations have rank b-1, not b, but that rank is never used as z=b in G14. This distinction is essential and is handled correctly.

## 6. Actual model, exact remainder, and non-claims

The general argument has source domain N>=2. The actual model has fixed literal tau=10^-80 and odd dimensions; its nontrivial domain is odd N>=3. The cited position-chain source obtains an entrywise O(N^-1/2) four-branch kernel uniformly in grid indices, hence N max|U_ab|^2<=C at sufficiently large odd N. A finite startup set can be absorbed into a larger fixed C; no effective threshold is claimed. Its separate eventual singular gap is unused here.

Since P_H and P_ord are orthogonal projections with orthogonal ranges, Q_res=I-P_H-P_ord is an orthogonal projector. Inserting their sum before C_U gives G13 exactly. The first term is Tr(RP_H) because P_H C_U=P_H. Neither P_ord nor Q_res must commute with mixed R. No such commutation is invoked. Different independent ket/bra relabelings transport the chosen ordered sector; they do not prove invariance of the untransported sector.

The complement Tr[R Q_res C_U], the remaining balanced coherence and off-charge contribution, and their signed fixed-k aggregation are unestimated. The argument has not changed the actual quantization, literal coupling, symmetry convention, coordinate basis, or common spectral-origin averaging. It supplies no full factorial comparison and no BGS theorem.

## 7. Obligation matrix

| Obligation | Status | Evidence |
| --- | --- | --- |
| Full ordered space, unnormalized HS, all-degree Gram | Passed | Support decomposition and two-leg moment bound |
| Genuine mixed R, exact trace order, e annihilation | Passed | Range-projector reconstruction |
| Exact centered Neumann identity | Passed | H_c convergence and within-term scalar subtraction |
| Arbitrary canonical patterns and complete cut graph | Passed | All endpoint edges deleted; every vertex lies in an open string |
| Zero strings and unrestricted/repeated ports | Passed | Identity deltas remove exactly their own b variables |
| Flatness-only O(C^(2h)) bound | Passed | Entrywise cut/link bounds and exact count |
| U-independent all-uniform term | Passed | Rank-one trace and permutation trace |
| M-independent N^(2h) Lipschitz bound | Passed | Power contraction, telescoping only cut-network factors |
| Exact Haar product HS contraction and fixed cutoff | Passed | Conditional second moment, explicit N^-3/2 tail |
| Finite Haar maximum-entry moment bound | Passed | Exact beta tail, union bound, exponential excess moment |
| Möbius normalization and all zero-power strata | Passed | Exact partition identity and independent linear constraints |
| M=0 / all-zero powers | Passed | Exact constants retained; no sector to remove |
| Actual fixed-tau application | Passed relative to named accepted flatness input | Odd N>=3; same model and tau |
| Fresh full re-proof of inherited actual parametrix | Not addressed | Outside this interface audit |
| Residual factorial complement, BGS | Out of scope | No signed complement estimate |

## 8. Independent exact computation and provenance

The independent `checks.py` imports no author implementation. It builds physical slot-permutation matrices from their action on ordered words, tensor powers of rational or Gaussian-rational unitaries, and diagonal compressions. A separate implementation contracts the cut network. Its Q at N=3 is a rational convex combination of the identity, a three-cycle and a transposition; QQ* != Q*Q is checked exactly. It is genuinely nonnormal. Complex fixtures test conjugation rather than merely real transpose arithmetic.

The finite scope is:

- All ordered positive/negative compositions at N=2 and M=1,...,4; all at N=3 and M=1,...,3; one additional genuinely complex N=3 mixed pattern.
- Literal full-End range-projector controls at N=2,M=1,2,3 and N=3,M=2,3, including non-conjugating R, exact Gram metrics, annihilation of the identity row/column, H versus H_c trace agreement, and a four-term Neumann partial sum with its exact algebraic remainder.
- All set partitions for k=2,...,7 and every zero-block subset omitting at least two blocks, checking the exact integer ranks; all-zero rank b-1 separately. Literal Möbius identities include zero powers and k>N.
- Exact Haar covariance matrices in dimensions 2,...,8; the arbitrary-product conditional recursion is proved in Section 4 rather than inferred from those checks.

Finite controls cannot certify universal quantifiers, the actual flatness theorem, or BGS. They test the specific algebraic failure modes above. The exact execution outcome and bounded-run receipt are recorded in the accompanying execution summary after completion.

## 9. Remaining gap and strongest safe use

No missing implication was found inside G1–G14 at their stated scope. The strongest safe use is to remove this specified canonical ordered-diagonal sector from every fixed-order compact-weight factorial Fourier expression at cost O_(k,weight,C)(log^(2k) N/N), with the accepted actual flatness dependency retained. Since N>=2, replacing 1+log N by log N only changes the constant.

The exact open quantity is the complete signed aggregation of Tr[R(I-P_H-P_ord)C_U]. A new estimate must concern that genuine remainder or an exact, correctly normalized decomposition of it. Further success on the already-controlled ordered sector cannot establish the missing signed comparison.

## 10. Completed execution and reproducibility

The bounded independent run completed successfully in 56.98 seconds (55.12 seconds reported inside the checker), with 107 exact network cases, five literal full-End Gram cases, 11,928 proper zero-block rank strata and 1,154 all-zero rank cases. All five literal projector cases passed. In each of the four genuinely mixed cases, R failed to preserve the ordered sector, checked exactly, while the claimed compression remained correct. Thus these cases do not accidentally reduce the mixed interface to conjugation or invariant-subspace trace algebra.

The enforced caps were 300 seconds wall time, 280 seconds per-process CPU, 2 GiB address space, one CPU-affinity core, conventional one-thread library settings, and 1 MiB combined logs. Arithmetic was exact Q/Q(i) with Python 3.12.14 and SymPy 1.14.0. No random samples or numerical tolerances were used. `run/manifest.json` records the actual command, unchanged input hashes, software, result hashes, output completeness and effective caps. Its computation-audit validation passed with `--root` hash checks. This isolated review directory is not a Git checkout; the runner correctly reports its local repository revision unavailable, while the source base and all source bytes are pinned separately.

The author's five `check_general.py` cases were also replayed from frozen inputs. Their output matches `general_checks.json` byte-for-byte (SHA-256 `4a09a58fd8385f8c7c6c39bf2650ad5adcfeada1f24d3bc79655223348b8e9d8`). `author_replay.json` records that separate reproduction. The imported older `check_mixed.py` contains a misleading comment calling its identity/one-cycle convex combination “nonnormal”; that older circulant matrix is normal. This is a finite-fixture label error, not a theorem defect. The new author's general controls and this independent checker each verify a genuinely nonnormal N=3 Q exactly, so the present review does not inherit the older label as evidence.

Reproduction of the independent suite requires a fresh copy with no existing `run/` output:

    python3 <installed computation-audit>/scripts/run_experiment.py \
      --root . --contract contract.json \
      --input checks.py \
      --input frozen/bgs_mixed_ordered_interface/general_fixed_order_v2.md \
      --output run --result run/results.json \
      --timeout 300 --max-output-bytes 1048576 \
      --max-memory-bytes 2147483648 --max-cpu-seconds 280 \
      --max-cores 1 --max-threads 1 -- python3 checks.py

Then validate `run/manifest.json` with the installed computation-audit validator and `--root .`. The exact installed runner location and argv are preserved in the execution environment/receipt; none is a mathematical theorem certificate. All original author manifest hashes were rechecked after the runs and remained unchanged.

## Portable replay boundary

The maintained entry replays the successful exact finite controls only.
Historical480s/360s mixed-suite timeouts remain explicitly failed receipts;
their partial logs do not certify N3 full-End cases. The original normal
circulant fixture label is preserved historically; genuinely nonnormal Q
fixtures are independently checked exactly in the promoted controls.
