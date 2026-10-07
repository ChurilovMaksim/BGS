# Independent audit: complete convex pinch resummation

7 October 2026. Fresh reconstruction of the two author manuscripts from their definitions. This review writes only this separate review directory; it makes no canonical-repository or proof-source change. Canonical BGS HEAD inspected: `129c676b8e6457e7e5f1bd6f786b3939cbd84653`.

## Verdict and decisive consequence

**Primary verdict: proved as written under the explicitly stated hypotheses.** The conditional finite-N resummation, every `d_N -> 0` undeconvolved consequence, bounded-u deconvolution, noneffective slow divergent schedule, and annealed compactness/Abel companion all pass. The actual fixed-positive-lag RIGHT-frame compression is a named input whose stationary-phase proof is outside this review. Its separately assigned extension review must supply the actual-family application; the accepted LEFT-frame theorem alone is not silently substituted.

There is also a sharp **actual-family unsigned obstruction**. Accepted whole-traceless one-step contraction implies, for `u=A0 log N`, `A0>2/(kappa a)`, uniformly on the positive band, `F_m=1+o(1)`. Hence

    N^-2 sum_(m=ceil(aN))^floor(bN) z^-m F_m
      = (1+o(1)) N^(b A0-1)/(A0 log N) -> infinity.

This is a mathematical impossibility for the proposed full positive deconvolution target in that window, rather than merely a missing quantitative rate. The common identity sector cancels exactly in occupation subtraction and is excluded by the relevant high-Hamming projection. This result does not refute T16, signed microscopic comparison, or BGS. A signed route must preserve that cancellation before taking absolute bounds.

## 1. Normalized claim cards and exact scope

### Conditional unmasked resummation

Objects: any unitary `U_N` on `C^N`; `H_N=End(C^N)` with ordinary Hilbert--Schmidt norm; ordinary matrix and superoperator traces; `T=Ad(U)`, `D=N^-1 sum_b Ad(Z_b U Z_b*)`; `T_z=zT+(1-z)D`; literal row-minus-column slices `A_c`; `C e_c=A_c*`; RIGHT multiplication `R X=XU`. The convention reindexes the accepted column-minus-row charge by `c -> -c` in the full sum.

Hypotheses: uniform `||C||^2<=C0`, `C0>=1`; real `0<=z<=1`; and, only for the asymptotic conclusion, `||C*R^r C|| -> 0` for every fixed positive integer r. No rate or growing-r uniformity is required. The at-least-one-pinch correction is

    F_m(z)=Tr_H T_z^m-z^m |Tr U^m|^2 >= 0.

Conclusions: manuscript equations (1) and (2) for every integer interval `1<=A<=M` and every `L>=1`; vanishing normalized fixed positive bands for every `d_N->0`, including all `u_N=Nd_N=o(N)`; bounded-u deconvolution; the sufficient quantitative condition (5); and the expressly noneffective schedule (13).

### Annealed companion

Additional objects: normalized torus Haar measure on the N independent coordinate phases; `V_theta=Ad(Z_theta)`, `T_theta=V_theta T`, `D_theta=V_theta D`, `M_theta=zT_theta+dD_theta`. The complete positive annealed correction is `F_theta,m=Tr M_theta^m-z^m|Tr(Z_theta U)^m|^2`.

Additional hypothesis: D admits uniformly bounded-rank approximants at every fixed ordinary operator-norm accuracy. Accepted FM-028 C4 supplies this at theta=0 for the actual sequence; unitary left multiplication and contraction right multiplication transport rank/error without requiring theta-uniform compact convergence. Accepted TRACE-023 (A) supplies the universal annealed Abel estimate.

Conclusions: companion equation (3), its optimized (4), both bounded-u conclusions (2) for arbitrary bounded compact-band weights, and exact complete signed bounded-u stability (12) when combined with the conditional RIGHT-frame theorem. No Hamming/path mask or high-switch extraction is included.

### Actual unsigned logarithmic obstruction

Additional accepted input: whole `H0=I^perp` gap `||D|H0||<=rho<1`, not just nonzero-charge contraction. Fixed actual-map constants and existential startup; `kappa=1-rho` is in `(0,1]`. Main equation (15) applies on every nondegenerate fixed band `0<a<b` at the prescribed large logarithmic damping.

## 2. Dependency graph and source check

1. Finite character orthogonality and `Tr_H Ad(K)=|Tr K|^2` establish D's slice/twirl dictionary, every CP-word trace positivity, and the distinguished-pinch formula.
2. A unitary RIGHT orbit and the block Gram estimate establish the uniform fixed-B moving-time block law. Only the named RIGHT overlap hypothesis enters its asymptotic version.
3. Prefix division and monotone summation by parts give exact short-run remainders.
4. Noncommutative telescoping at a fixed linear cut gives the first-pinch factorization. Holding the tail length p fixed makes the tail-word distribution independent of the averaged coherent time n.
5. Finite triangular reindexing gives the total scalar masses and equations (1),(2), without insertion-count entropy. Marking pinches independently gives the cyclic multiplicity identity.
6. Fixed-L then large-N then large-L limits establish all `d_N->0` unmasked bands. Minimizing over `L<=sqrt N` supplies the slow schedule.
7. Accepted compact D limit gives fixed-rank approximants; a smooth long-run cutoff, two finite differences, and the universal Abel estimate control the companion's expected time-kernel trace norm. Trace duality closes its rank/tail argument.
8. Accepted whole-centered one-step gap yields uniform `F_m=1+o(1)` and the exact unsigned divergent geometric sum. The identity subtraction remains separate.

I inspected the actual current proof statements in:

- `BGS/mathematics/global_switch_transfer.md`, T2--T6;
- `BGS/mathematics/onestep_charge_gap.md`, G1 and G4;
- `BGS/mathematics/actual_charge_radial_shell.md`, C2 equation C4;
- `BGS/mathematics/uniform_phase_pair_abel_bound.md`, theorem (A), its Poisson normalization and proof;
- the current `phase_trace_checkpoint.md`, claim ledger, and core registry;
- the accepted left-frame packet, for frame conventions and normalization only.

The checkpoint/ledger's current acceptance scope overrides historical candidate headings. The independently reviewed one-pinch averaged lemma is prior work credited by the companion's compact/Poisson mechanism. No Egorov, quasimode, radial spectral, source-CFT, or microscopic-law conclusion is needed for the new compactness/Abel step. All author source-bindings hashes checked against the inspected local sources. There is no `.mathbox` ledger in canonical BGS; no ledger was initialized or changed.

## 3. Obligation matrix

| Obligation | Status | Decisive reason |
|---|---|---|
| Ordinary HS and trace normalization | Passed | Orbit vector has squared norm N; final normalization is N^-2. |
| Every binary-word trace nonnegative | Passed | Expand D as a probability mixture of unitary Ad maps; every word is another such mixture. |
| RIGHT-frame orbit orientation | Passed | `C*(BU^n)` has coordinates `Tr(A_c BU^n)=Tr(U^n A_c B)`. |
| Actual RIGHT fixed-lag stationary phase | Out of scope / named input | Separately assigned extension audit, never inferred from LEFT multiplication. |
| Fixed p law independent of n | Passed | Tail expansion of `T_z^p` depends on p,z,U alone. |
| Prefix/remainder and decreasing weights | Passed | Remainder r<L costs exactly `(C0-delta)r`; Abel summation costs R times initial weight. |
| First-pinch word multiplicity | Passed | Unique first D after the rooted cut. |
| Cyclic multiplicity and zero runs | Passed | Mark each of k pinches; periodic words retain all marks, yielding m/k with weak compositions. |
| Finite-N scalar sums and endpoints | Passed | Direct triangular sums; z=0 uses 0^0=1, z=1 gives correction zero. |
| Varying B_n fixed-time obstruction | Passed | `B_n=U^(-n-1)` gives `sum_c ||A_c||_HS^4>=N`. |
| Every u_N=o(N), undeconvolved | Passed | Fixed L limsup <=bC0/L; the R d term vanishes. |
| Noneffective deconvolution schedule | Passed | E_N->0 but E_N>=C0/floor(sqrt N); exponential cost leaves E_N^(1/2+o(1)). |
| Compact approximation rank/input uniformity | Passed | Compress a fixed finite-rank approximation to the accepted common compact limit. |
| Annealed V_theta D orientation | Passed | First-pinch product is `T_theta^n V_theta D M_theta^p`; factors within the coherent orbit remain theta-dependent. |
| Short n and cutoff endpoints | Passed | n=0 retained; chi_eta vanishes near all nonpositive n, and g has smooth compact upper support. |
| Poisson trace-norm normalization | Passed | Trace equals N^2+2 sum r^j E|Tr W^j|^2, at most 4N^2. |
| No hidden log or p-dependent loss | Passed | Two differences and L1 second derivative give displayed 1+eta^-1 only; p is a translation of g. |
| Whole-centered gap used for obstruction | Passed from accepted source | G4 explicitly combines nonzero charges with zero-charge `||P-J||<=1/2`. |
| Occupation/Hamming scope | Passed | Main frame input is untwisted; companion covers complete occupation subtraction only; neither infers mask positivity. |
| Required logarithmic unsigned vanishing | Refuted, as explicitly stated | Identity sector gives main (15); it cancels from T16's signed projection. |

## 4. Independent reconstruction of the conditional inequalities

For unitary B, `f_B(n)=||C*(BU^n)||^2<=NC0`. Assemble `S=[C,R^-1 C,...,R^-(L-1)C]`. Its block Gram has diagonal norm at most C0 and off-diagonal norm at most epsilon, with negative-lag blocks adjoint to positive-lag blocks. The block row/column bound and trivial C0 bound give

    ||SS*/L||<=delta=min(C0,C0/L+(1-1/L)epsilon).

Pair against `BU^n` to obtain every moving block sum `<=NLdelta`, uniformly in its start and in a single fixed B. Mixtures inherit the same bound. For `K=qL+r`, the exact prefix estimate is `N(delta K+(C0-delta)r)<=N(delta K+R)`. For nonincreasing nonnegative weights, writing a weighted sum as the nonnegative combination of prefix sums gives `Ndelta sum w+NR w_start`. There is no z^-L loss.

Set `A=zT`, `B=dD`. The telescoping expansion of `(A+B)^m-A^m` is `sum_{n+p=m-1} A^n B(A+B)^p`; a first distinguished pinch uniquely factors every rooted word. The tail's unitary word distribution depends only on fixed p, not n. This proves the fixed-p applicability of the block/prefix law.

For `p=0,...,M-1`, `s_p=max(0,A-1-p)`, `t_p=M-1-p`. Directly,

    d sum_p sum_(n=s_p)^t_p z^n=sum_(m=A)^M (1-z^m),
    sum_p z^s_p=M-A+1+sum_(r=1)^(A-1)z^r.

These give (1). Deconvolution cancels n exactly: `z^-m z^n=z^(-p-1)`. Now apply the unweighted prefix estimate and use

    d sum_p z^(-p-1)(t_p-s_p+1)=sum_(m=A)^M(z^-m-1),
    d sum_p z^(-p-1)=z^-M-1.

This proves (2) without stripping a convex mixture after the fact. Summing fixed insertion counts is legitimate because their normalized tail masses add to one; all-D and adjacent-D words remain included. The m/k cyclic formula follows from marking all k pinches, including periodic words, rather than quotienting necklaces.

At fixed total m, p changes with n, so the fixed-B block law cannot be applied. The displayed counterexample is exact by cyclicity and `Tr A_c U*=||A_c||_HS^2`; Cauchy--Schwarz over N slices gives its lower bound N. The manuscript correctly makes this distinction.

Finally, (1) on M<=bN gives `bdelta+bC0(L-1)d`; for fixed L the second term vanishes for every d->0. The subsequent L->infinity limit requires only fixed-lag o(1). The slow schedule also passes: delta>=C0/L implies `E_N>=C0/floor(sqrt N)`, hence u=O(log N), u/N->0; its exponential exponent is `1/[2(1-u/N)]`, leaving `E_N^(1/2+o(1))`. Its coefficient is at most `1/(4b)` on log N and cannot meet `2/(kappa a)` with kappa<=1 and a<=b.

## 5. Independent reconstruction of the annealed companion

The distinguished charge Parseval identity is

    sum_c |Tr(W_theta^n Z_theta A_c B)|^2
      =||C*(B W_theta^n Z_theta)||^2<=NC0.

This is a pointwise bound on a unitary vector and requires no twisted fixed-lag theorem. After deconvolution, its tail-length weight is `d z^(-p-1)`. The short-cutoff contribution has at most `2eta N+1` values of n per p, including n=0, and gives exactly the first term of companion (3).

For the long part, `a_p(t)=g(t+(p+1)/N)chi_eta(t)` has support of uniformly bounded length, `sum |a_p(n/N)|<=K_g N`, and `||a_p''||_L1<=K_g(1+eta^-1)`. The first-derivative cutoff term has bounded L1 norm; the second-derivative cutoff term costs eta^-1. All bounds are uniform in p. Extending samples to all integers introduces neither endpoint jump: chi_eta vanishes for t<=eta and g vanishes smoothly near the upper endpoint.

With h=1/N, the exact second-difference representation is a double integral of a_p''. Summing the triangular convolution weights over h-lattice translates gives constant total weight h; thus

    sum_n |Delta^2 a_p(nh)|<=h integral |a_p''|.

Together with the trivial coefficient sum this proves the scalar kernel bound by `K_g(1+eta^-1)P_(e^-1/N)`. For the unitary `T_theta=Ad(W_theta)`, normal functional calculus preserves the bound on all N^2 eigenoperators, with all multiplicities. Its Poisson trace is exactly

    N^2+2 sum_(j>=1) r^j |Tr W_theta^j|^2.

Accepted Abel (A) bounds its expectation by `N^2+N(1+r)/(1-r)<=4N^2` at r=e^-1/N. The factor 2 and the ordinary superoperator trace are correct. There is no unaveraged pair-density assertion.

For `D=K+E`, rank K<=R, ||K||<=2, ||E||<=epsilon, the factor `V_theta K M_theta^p` has rank<=R and norm<=2, while `V_theta E M_theta^p` has norm<=epsilon. The time-kernel pairing costs at most `2RK_g N` plus expected `4epsilon K_g(1+eta^-1)N^2`. No statistical independence between kernel and tail factor is needed because the factor norm is controlled pointwise. Sum the exact p weights to `z^-M-1`; this proves (3), with constants enlarged once.

A common compact-limit embedding gives K by compressing a fixed finite-rank F: `K_N=I_N* F I_N`. Its error is bounded by the accepted limit error plus `||K_limit-F||`; no occupation-uniform embedding or trace-norm convergence is used. The scalar normalized/ordinary HS convention can be absorbed in the isometry and changes no operator norm or rank.

At bounded u, `z^-M` stays bounded. Fix epsilon and eta first, let N tend to infinity with the corresponding fixed rank/threshold, then use eta=sqrt epsilon and let epsilon tend to zero. Alternatively take epsilon then eta after N, in that order. This proves the result even for bounded nonsmooth/complex w because a fixed smooth nonnegative g dominates its whole support, and positivity bounds the absolute weighted aggregate. The full signed stability identity (12) is exact. It gives no masked or logarithmic conclusion.

## 6. Independent check of the unsigned logarithmic obstruction

The accepted source is unambiguous: onestep_charge_gap G1 states whole-traceless contraction, and G4 explicitly covers zero charge by `||P_N-J_N||<=1/2`; the nonzero-charge blocks are an orthogonal direct sum. Global_switch_transfer T2--T6 uses this full gap. Hence e0 is reducing and fixed, and

    |Tr T_z^m-1| <= (N^2-1)(1-kappa d)^m <=N^2 e^(-kappa dm).

For m>=aN and d=A0 log N/N, A0>2/(kappa a), this is o(1). Also `z^m |Tr U^m|^2<=N^2e^(-dm)=o(1)` because kappa<=1. Thus F_m=1+o(1) uniformly.

Uniform relative error permits multiplication by positive z^-m and summation. The exact geometric sum is `z^-M(1-z^(M-A+1))/d`. Since `z^-M=N^(bA0)(1+o(1))` and `z^(M-A+1)->0`, equation (15) follows with its stated constant. The undeconvolved aggregate is `(b-a+o(1))/N`. Arbitrary occupation twists preserve e0 and the same centered contraction; their coherent trace has the same trivial N bound, so their positive deconvolved corrections have the same leading identity divergence uniformly. The signed subtraction cancels that identity before a norm estimate. No contradiction with bounded-u stability or the much slower noneffective schedule arises.

## 7. Computation checks, evidence labels and remaining gap

The author's exact SymPy script was copied and run in the review directory, leaving the author's original output untouched. All **1486** checks reproduced with identical result JSON: dimensions 2,3; every binary word through degree 6; explicit charge-Kraus words for N=2 through degree 4; weak-composition/cyclic and fixed-count first-pinch identities; triangular endpoint identities; scalar original and refined weighted-prefix controls; and the two scope warnings. These are finite auxiliary controls only.

A separately implemented NumPy script tested complex QR unitaries in N=2,3,4,5 with fixed seed 742198. All **8708** assertions passed: literal slice/twirl equality, RIGHT frame identity for arbitrary B, changing-B counterexample, every full binary word through length 5, first-pinch identities through m=9, block Gram bounds through L=5, and both finite-N band inequalities for z=0,.2,.5,.99,1 (deconvolution only for z>0). Largest identity residual: `4.884981308350689e-15`. Floating control evidence is not an asymptotic proof and does not certify actual U_N.

Reproduction commands:

    python3 author_snapshot/exact_controls.py
    python3 independent_bounded_controls.py

Appendix A also passes. A nonnegative remainder of length r is bounded by both NC0r and NLdelta, by extending it to a full L-block. Subtracting Ndelta r yields exactly the minimum defining R_opt. The continuous crossing at r=Ldelta/C0 has maximum Ldelta(1-delta/C0)<=C0L/4, and the finite integer maximum tends to C0(1-1/L) at fixed L, including L=1. The replacement does not change any scope or the original valid equations.

No missing implication remains inside either stated abstract theorem. For the actual unmasked conditional consequence, the exact named external-to-this-audit input is the RIGHT fixed-lag compression. For T16, the remaining implication is a signed masked centered-remainder estimate at the large-logarithmic deconvolution boundary; bounding the two complete positive corrections separately is now proved impossible. The strongest safe new consequence is complete unmasked bounded-u signed stability, plus all d->0 undeconvolved unmasked stability and the explicit unsigned logarithmic obstruction. No microscopic balanced law, factorial hierarchy, or BGS conclusion follows.
