# Independent internal audit of FLOW-016 and FLOW-017

Date: 5 October 2026. Opening repository revision:
be2e7a9c236df20a0e026a714c8c97327bde973a.

**Primary verdict: proved as written**, for the final source revisions pinned
below and under their stated reference, time and step-size hypotheses.

This was one independent internal subagent proof audit, using
mathbox:proof-audit, with an initial pass and a correction pass. They are not
two independent reviewers. The candidate proofs and the load-bearing raw
estimates were read directly; their status labels were not treated as proof.
The author made the proof corrections reported below. This audit wrote only
this review record, did not run full-workspace verification, and did not
commit. It is not external refereeing, a complete re-audit of the inherited
corpus, a formal analytic certificate, or a priority determination.

## 1. Normalized claims and precise scope

**FLOW-016, point fields.** For random or deterministic period-N counting
measures with N labels per period, including multiplicities, a measurable
circle matching has average pth unfolded displacement cost c(p,N). Reference
unit-window moments are uniformly bounded at every fixed order q>1.
Bounded expected cost gives uniformly bounded target count moments of order
1<s<p+1. Vanishing expected cost transfers the weak local law and factorial
expectations at each integer k<p+1. All fixed vanishing transport orders
therefore transfer all fixed factorial orders, including Schwartz tests.
The factorial convention is distinct atom labels, with multiplicities
retained.

**FLOW-016, diffusion application.** Start the globally localized projected
diffusion at exactly Pi(A_N), with the bounded first two unnormalized starting
traces stated in the proof, and couple it to traceless unitary Brownian motion
from that same matrix. At t_N tending to zero with t_N^2 log N tending to zero,
every fixed even transport moment vanishes. When FLOW-014's stated reference
hypotheses hold at these times, this gives Sine_2 at every fixed factorial
order and uniform bounded-window count moments.

**FLOW-017.** Keep the original uncentered normalized-GUE coboundary chain
(C1), not a centered or whitened algorithm. Assume bounded first two starting
traces, t_N at least 1/N, t_N tending to zero, t_N^2 log N tending to zero,
and N^b epsilon_N tending to zero for every fixed b>0. Also assume that
FLOW-014 applies from exactly Pi(A_N) at t_N. The output has the Sine_2 local
law, all fixed compact-continuous and Schwartz factorial expectations, and
all fixed bounded-window count moments. For each fixed test, its conditional
uniform-origin expectation converges to the sine expectation in L2 over
the chain randomness. Formula (C15) gives the complete signed, finite-Fourier-
support partition trace comparison to finite CUE in that same L2 sense.

The reference hypothesis is essential. Low starting traces and the time/step
inequalities alone do not assert arbitrary-start Dyson relaxation. All orders
are fixed before taking N to infinity. There is no growing-order uniformity,
full-sequence almost-sure assertion, maximum-displacement conclusion, or
deterministic noise removal.

## 2. Reviewed revisions

These are the exact final revisions read after the mathematical corrections
and subsequent status-only header changes.

| Artifact | SHA-256 |
|---|---|
| mathematics/local_moment_transport.md | dcbf7ecdf146186188c03e4076d6aec8fe8bcf71397016a32c70049e9801757a |
| mathematics/coboundary_all_order_limit.md | ac59bc85917aa5414cf1d3b6498a08af9bd65464213042e6d8379e4a86b3176f |
| computations/verification/local_moment_transport.py | 6ede9eec4d85dfe2fbc96952805fea44361287acecfff81a2cf91a4d7e6e203d |
| mathematics/quadratic_noise_coupling.md | 82811249be42c9c44eb2e59c72037e469681853d8e01f8bab8b7f1b9ba3b71fa |
| mathematics/coboundary_mobius_diffusion.md | 699f97454edee866fdcebe9f69b92d4ce28334cd177e17ed7952118d4a4df4ee |
| mathematics/coboundary_joint_limit.md | b3a831c9d9855031924bbb81f4bb9421f500d1a9dc724d7764f43bcee7f9d53f |
| mathematics/coboundary_polynomial_limit.md | 80e4ecb86aca0cf8d3c4f6e5115ced3ed9665e1800e8e771afd67dde2134785e |
| mathematics/coboundary_general_start.md | a1827a51b718032cfa79b9664ef02dfe546c499974a89d8e69728c088e8eebfc |
| mathematics/circular_dyson_actual_start.md | 148d2daf09c8d77f4580a0f6d17b304ed76dcdcb3f7475c7cf81442568d959f3 |

Applicable AGENTS.md, SOURCE_OF_TRUTH.md and repository conventions were
read, along with the relevant ledger, registry, results and frontier entries.
Additional raw algebra checked was FLOW-003's covariance operator,
FLOW-008's fourth-order expansion, TRACE-001's partition identity, and
FM-017's phase/potential estimates.

## 3. Dependency graph and leaf roles

| Edge | Role and exact input |
|---|---|
| Reference unit-window moments → maximal density → packing → target moments | Internal proof, FLOW-016 (T3)–(T7). Periodic HL constants do not depend on N. |
| Vanishing transport → local Laplace law → factorial expectations | Internal proof, FLOW-016 (T8), counting-measure continuity and uniform integrability. |
| Matrix Schatten moments → circle matching | Internal unitary-path argument, FLOW-016 (T9), including collisions and multiplicities. |
| FLOW-003 covariance → FLOW-004/009 common-noise comparison | Raw internal covariance, cancellation, both brackets and projected drift estimates; checked at the precise region used. |
| Scalar p2 tail + fixed high matrix moment → all fixed transport costs | Internal stopping argument, FLOW-016 (T10)–(T14). |
| Prior finite circular kernel + strip/potential assumptions → reference moments/law | FLOW-014 (U6)–(U24), using the already source-checked KLZF finite kernel; confluence handled at fixed N. |
| Fast contraction + chart + initial boundary layer → high exit estimates | FLOW-010 (5), (8); FLOW-012 (G3)–(G6); FLOW-017 (C3)–(C7). |
| Normalized coefficient derivatives → dimension-uniform semigroup → polynomial-test comparison | FLOW-011 (P7)–(P14), then FLOW-017 (C8)–(C10). |
| Exact partition identity + lattice decay → collision-safe factorial test norms | TRACE-001, then FLOW-017 (C11)–(C12). |
| Weak law + count moments + translation ergodicity → one-chain L2 averages | FLOW-017 (C13)–(C14); prior spatial Soshnikov Theorem 7. |
| One-chain L2 + finite CUE law + Schwartz copy tail → signed Fourier comparison | FLOW-017 (C15), with all partitions and p0=N retained. |
| Finite Markov telescoping + vanishing noisy variance → deterministic equivalences | FLOW-017 (C16)–(C17); the vanishing actual defect remains unproved. |

There is no cycle: weak comparison is established before chain moment
majorants, and those moment bounds are established before the unbounded
L2 averaging argument. FLOW-016 obtains its moments from the reference,
not from an assumed moment conclusion for the original chain.

## 4. Obligation matrix

Status words refer to the mathematical obligation in this audit, not to a
software run.

| Obligation | Status | Decisive check |
|---|---|---|
| Periodic maximal operator uniformly in period | passed | For radii at least N, the average is at most 3/2 of the period mean. High-threshold witnesses fit in three periods. Weak (1,1), truncation at lambda/2 and distribution integration give (T4) with an N-independent constant. |
| Packing with shortest lifted displacements | passed | n≤N and M≥1 give r=n/(8M)≤N/8. In the active case r>2R, at most n/4 reference labels lie within r, and at least 3n/4 moves cost at least n/(16M). |
| Mixed-density Hölder estimate | passed | The required density exponent is ps/(p+1-s)>1 precisely when s>1; no independence of M and transport is used. |
| Weak transfer and intensity/tightness | passed | Origin integration gives the exact displacement average; positive smooth Laplace tests determine local laws. First count moments are bounded, also directly by the fixed unit intensity. |
| Factorial continuity at coincident positions | passed | Partition inclusion-exclusion is a finite sum of integrals against product counting measures with compact continuous diagonally restricted tests. Integer multiplicity is retained; no simplicity is silently imposed. |
| Uniform integrability at fixed factorial order | passed | Choose k<s<p+1. Higher target count moments dominate the factorial observable. |
| Schwartz and L2 tails | passed | Stationarity and Hölder bound each tiled count product by a fixed common moment. Summable Schwartz box suprema control expectation tails and, at order 2k, L2 tails. |
| Claimed range and excluded endpoint | passed | The collapsed clock gives cost tending to zero but factorial defect tending to one at every k>p+1. The proof makes no critical-endpoint assertion. |
| Schatten-to-angle coefficient, including collisions | passed | Eigenangle speeds are diagonal expectations/compressed eigenvalues of H. Convexity, Minkowski and the chord inequality give exactly N^(p-1)/4^p in (T9). |
| Both stopped matrix brackets | passed | Noise coefficients V* R_a Y have left and right bracket contractions bounded by vI, by unitarity. Stopping only truncates these coefficients. |
| Matrix even moments without a log dimension factor | passed | Hermitian dilation has dimension 2N; its trace moment is twice the original matrix moment. The trace-Itô recursion starts at 2N and leaves exactly N(2r−1)!!(vt)^r. |
| Projected trace estimates and commutator cancellation | passed | FLOW-009 (9)–(14) were reconstructed from the covariance and centering expansion, not accepted from its status. T, T* and the square-root commuting subspace give the stated cancellation. |
| Broad time window and exit tail | passed | K(N,r)^2=C(K,r)(1+t log N) gives an exit tail at most C N^(-4r-4). Multiplication by the full circle cost (N/2)^(2r) still vanishes. The retained cost scale is (t+t^2 log N)^r. |
| Reference fixed factorial moments for distinct starts | passed | FLOW-014's local uniform kernel bound and Hadamard bound dominate each fixed determinant integral. Stirling identities give ordinary moments. |
| Repeated initial reference levels | passed after clarification | Gap-independent determinant bounds pass at each fixed N through continuous bounded origin-averaged factorial majorants; no pointwise confluent-kernel gauge is assumed. |
| Fast first-trace contraction and its N-uniform forcing | passed | The canceled Gaussian gradient has size epsilon^2/sqrt N. Centered increment moments are epsilon^2/N. The exact fourth Wick coefficient is proportional to x; the absolute sixth remainder produces equilibrium epsilon^4. |
| Frozen high stopped first-trace moments | passed | Dropping negative drift in the stopped one-step inequality gives (C4); no union bound on the decaying starting value and no epsilon^(-2) starting-value loss occurs. |
| High p2 Lyapunov test and smooth extension | passed after region clarification | C5 is used only before the 2/5 stop, within the imported 1/2 region. The extension agrees through good overshoots up to 9/20. Its sixth norm is at most C_r N^(2r). |
| Radial Itô factors in C5 | passed | The leading drift is −r(1−|q|^2)|p2|^(2r); the Hessian maximum is at most 4r^2|p2|^(2r−2). Half its contraction with bracket at most 64 gives 128r^2. |
| Arbitrarily high exit suppression | passed | Division of (C6) by the exit value N^(2r)(2/5)^(2r), together with (C4), gives N^(-L)+N^4 epsilon for arbitrary fixed L. The Gaussian large-jump event has every fixed epsilon-power bound. |
| Dimension-uniform semigroup and time rounding | passed | Positive-order noise/drift derivatives retain normalized O(1) bounds in FLOW-011. Variation moments give exp(Cs), not exp(CNs). Semigroup splitting bounds the local time defect using L^2g and derivatives through order six. |
| Weak comparison for signed polynomially bounded tests | passed | Sup norms bound discarded paths, derivative norms bound weak remainders; positivity is unnecessary for C8. One fixes b and chooses L>b. |
| Fast terminal centering | passed | C3 gives the decaying first moment plus rho. Since epsilon^2 n≥1/(N epsilon^2), the transient beats every fixed power of N under C2. |
| Fourier lattice norm and zero-index factors | passed | Charge zero leaves k−1 lattice dimensions. The prefactor N^(−k) cancels the coarse partition product N^k; the sixth sum is O(N^(k+5)). p0=N is retained and k=1 is constant. No gap denominator appears. |
| A single epsilon sequence for all fixed orders | passed | N^(−log log N) satisfies C2 for every fixed b. Order-dependent moment constants/stops are only analytical estimates of the same process, not different algorithms. |
| Chain count moments before unbounded extensions | passed | Nonnegative smooth tensor bumps majorize each factorial count; the Stirling identity yields all ordinary moments, then compact-continuous/Schwartz extension. |
| Quenched spatial L2 | passed | Conditional origin laws are exactly translation invariant for every S. Jensen, fixed-S weak convergence with moments above 2k, then spatial mean ergodicity in S give C14. |
| Signed finite-CUE Fourier comparison | passed after copy-tail clarification | Full-line and distinct-circle-label Schwartz statistics differ only on tuples of diameter at least N. Their L2 tail vanishes. CUE determinants are bounded by one and converge locally, yielding b_N→c and C15. |
| C16–C17, including complex tests | passed | Finite Markov telescoping is exact. Var(X_N)→0 and E|X_N−a_N|^2=Var(X_N)+|E X_N−a_N|^2 give both equivalences without a new moment premise. |
| Actual-time and actual-centering substitution | passed | G3 bounds p2(Pi A_N) from bounded p1,p2. At t=8g, g=4 log J/J and J=floor(c log N), t^2 log N→0 while t log N does not tend to zero. |
| Full FM-007/FM-013 model-specific derivations | out of scope | Their recorded inputs are used in the actual-map corollary; this audit did not re-prove the full seven-cut or packet/frame constructions. |
| Deterministic vanishing of the actual defect | not addressed | C17 identifies this precise remaining input; none of the reviewed estimates supplies it. |

## 5. Critical reconstructions

For (T9), with unfolded coordinate N theta/(2pi), the unitary path gives
sum |delta theta_j|^p at most Tr|H|^p. The principal spectral argument
can be chosen at −1 with absolute value pi, so that endpoint causes no
exception to the chord bound. Thus

$$
c_{p,N}\le {1\over N}\left({N\over2\pi}\right)^p
\operatorname{Tr}|H|^p
\le {N^{p-1}\over4^p}\operatorname{Tr}|V-W|^p.
$$

For the matrix martingale, the dilation trace f_r satisfies

$$
f_r'\le r(2r-1)v f_{r-1},\qquad f_0=2N.
$$

Integration yields the displayed double-factorial bound. The drift adds
at most a Schatten cost of order [((K^2+1)t)/N]^(2r). This is absorbed
when (K^2+1)t tends to zero. The exit multiplication leaves N^(-2r-4),
so the stopped comparison really proves a full-process transport estimate.

The frozen first-trace estimate is also a full stopped-variable estimate:
before each stop its conditional 2p-moment increment is at most
C_p epsilon^2 rho^(2p). Summation costs n epsilon^2 rho^(2p), not a sum of
the initial transient over n separate exit tests.

The fast quartic coefficient was recomputed from all 16 words in
(G−UGU*)^4 and the three exact Gaussian Wick pairings. The nonplanar
term cancels. The five remaining normalized-trace monomials are

$$
{x\over8}-{q\bar x\over6}
 +{q\bar q x-x^2\bar x+\bar x^2 r\over24},
$$

exactly FLOW-010 (4). This is why the fourth mean term does not create
an additional order-one forcing on the fast coordinate.

For a compact local factorial test, the averaged translate in C13 is
itself a factorial test with kernel
S^(-1) integral from 0 to S of psi(x_1−u,...,x_k−u) du. It is compact
continuous and has a fixed enlarged support for each fixed S. This
provides the continuity and domination needed before the ergodic limit;
there is no interchange of N and S limits.

Finally, let X_N=F(N,psi)(U_n), a_N=F(N,psi)(A_N), and b_N the finite-CUE
expectation. C15 says E|X_N−b_N|^2→0. Hence E X_N−b_N→0 and
Var(X_N)→0. C16 is D_N=E X_N−a_N, so

$$
a_N-b_N\to0\ \Longleftrightarrow\ D_N\to0,\qquad
\mathbb E|X_N-a_N|^2=\operatorname{Var}(X_N)+|D_N|^2.
$$

This proves C17 even for complex signed tests, while leaving the actual
vanishing of D_N untouched.

## 6. Corrections identified during the audit

All mathematical comments were first sent to the author. The reviewed final
revision incorporates the following corrections or clarifications:

1. The actual first-two-trace source in FLOW-017 Section 6 is FM-013,
   not FLOW-013, which is the prescribed-time obstruction.
2. Reference factorial bounds for repeated starting levels are passed
   by a fixed-N dominated-convergence argument with smooth factorial
   majorants. FLOW-014's Laplace confluence alone was not silently promoted
   to a pointwise confluent kernel assertion.
3. C5 is stated in the imported region |q|≤1/2; its extension agrees
   through good overshoots to 9/20. The coefficient 16/25 is explicitly
   a safe weakening of 3/4. It is not used as a generator estimate along
   the entire globally localized process.
4. The full-line/distinct-circle-label distinction for Schwartz tests
   is explicitly removed in L2 before C15.

No counterexample or unresolved implication was found in the final auxiliary
claims. The collapsed clock is a counterexample only to a stronger transport
range that the proof expressly excludes.

## 7. Source and computational boundaries

The exact external kernel leaf is KLZF, arXiv:2012.11993v2,
Proposition 12/(2.4.10), Theorem 7(3), and Proposition 21/(3.2.2)–(3.2.3),
with project heat time divided by 2N. Its source mapping is recorded in
literature/actual_start_dyson_sources_20261004.md and EXT-KLZF-2022.
The raw FLOW-014 contour crossing, winding, two-dimensional pole bound,
kernel normalization and Hadamard/Fredholm steps were read in this audit.
Repeated levels do not require the source's distinct-spectrum formula
outside its stated domain.

The spatial ergodicity leaf is Soshnikov, arXiv:math/0002099v4,
Theorem 7, printed pp.38–42. Its exact source was already checked in
literature/return_local_limits_sources.md and in the dated all-order source
record. The sine Fourier projection onto [−1/2,1/2] is Hermitian, a positive
contraction and locally trace class. Its spatial translation conclusion
is the required one. Temporal Dyson ergodicity is not substituted.
The exact public PDFs were not fetched again by this reviewer.

The new finite verifier was inspected read-only. Its contract is appropriately
limited: Fraction arithmetic for periodic window integrals and packing
witnesses, exact Laurent character differentiation at N=4,5,6, collapsed-clock
controls, and floating unitary matching at N=3,5,9. It uses upper reference
density bounds, which impose a stronger active packing condition and do not
invalidate the witnesses. The matching diagnostic uses seed 20261005 and
tolerance 2e−10 times max(1,right), plus nine endpoint identities.
The stated packet contains 234 exact window-integral cases, 96 active packing
segments, 12 collapse cases, 15 radial-character cases and 54 sampled matching
cases. Those are finite source-coverage counts, not certification of the
universal transport, diffusion, chain or BGS conclusions. Radial Lyapunov
controls cover fixed orders 1–8, not all orders by computation.
The author's execution evidence is separate; this reviewer did not re-run
that packet.

Read-only commands in this pass included targeted cat/sed/rg reads,
git status, git rev-parse HEAD, and sha256sum. A standalone Python
Fraction calculation independently enumerated the exact four-letter Wick
coefficient and matched the five monomials above. An initial SymPy version
could not run because SymPy was absent in the default Python; it was replaced
by the successful dependency-free Fraction calculation. No failed command
is counted as verification.

## 8. Remaining gap and strongest safe statement

There is no remaining gap in the reviewed auxiliary implication under its
stated inputs. One superpolynomial epsilon schedule gives the original noisy
chain all fixed factorial correlations, their conditional spatial L2 limits,
and the complete signed finite-CUE Fourier comparison.

For the unchanged deterministic actual spectrum, the exact remaining edge
is the vanishing of D(chain,N,psi) in C16 for every fixed signed test/order,
equivalently either other condition in C17. Neither initial low traces,
reference Sine relaxation, rare-exit control nor noisy self-averaging proves
that edge. The cheapest focused next mathematical check is an estimate of
that actual signed telescoped defect for one specified test; an absolute
sum of step errors or another finite simulation would not establish the
required all-order cancellation. Full deterministic BGS and TRACE-005
remain open. No world novelty, external referee agreement or analytic Lean
certification is asserted.

## 9. Wick execution scope and canonical replay addendum

This addendum records the executed check more precisely. It belongs to the
same audit and does not add a second independent review, a new alternative
algorithm, or a stronger mathematical status.

The initial standalone Fraction script was executed from a shell heredoc and
was not retained as a source file. It enumerated the 16 actual-step words and
their two planar contractions, giving 32 programmed contributions and the
five monomials in Section 5. The third, nonplanar contraction was checked
directly by algebra, not programmed in that initial script. The initial run
must therefore not be described as a programmed verification of all 48
word/pairing contributions.

For the exact third pairing, write
A1=U^(b1−b0), A2=U^(b2−b1), A3=U^(b3−b2).
The crossing term in the four-GUE Wick identity is A3 A2 A1/N^2.
Including the outer U powers and the terminal U in the normalized trace
leaves m1/N^2 for every word. Its signed coefficient sum is
(1−1)^4/24=0. This direct derivation is the justification of the third
pairing in the analytic review; it is distinct from the initial execution
scope.

On the follow-up source search, the same normalized-trace exponent dictionary
representation was found already in
computations/verification/coboundary_joint_limit.py, function
exact_fourth_mean. To avoid duplicating a maintained implementation, no
new coboundary_fast_wick.py source was created. The existing function was
replayed narrowly; its NumPy/SciPy module imports were available, but the
matrix/gradient controls and module main were not run. The replay sums
32 planar monomials and 16 coefficients of the common nonplanar term, and
asserts both the exact polynomial and zero nonplanar coefficient. It is
a canonical-method replay, not an independent alternative representation.

Replay source SHA-256:
682cac6863baee3c68bffb50fe4c03086bd3fd434eb9406065dd68f478aec355.
The earlier proof/source pins in Section 2 are unchanged.

Exact executed command, from /workspace/scratch/00a8504af897/BGS:

    PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY'
    import hashlib
    import json
    from pathlib import Path
    import sys
    sys.path.insert(0, 'computations/verification')
    from coboundary_joint_limit import exact_fourth_mean
    source = Path('computations/verification/coboundary_joint_limit.py')
    print(json.dumps({
        'status': 'PASS',
        'scope': 'Canonical exact_fourth_mean replay only; no alternate algorithm or new review',
        'arithmetic': 'fractions.Fraction; normalized-trace exponent monomials',
        'words': 16,
        'planar_contributions': 32,
        'nonplanar_coefficient_contributions': 16,
        'coefficient': exact_fourth_mean(),
        'source': str(source),
        'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
    }, indent=2))
    PY

Exit code was zero. The returned coefficients were 1/8 for (1,),
−1/6 for (−1,2), and 1/24, −1/24, 1/24 for
(−2,1,2), (−1,1,1), (−1,−1,3), respectively. No numerical tolerance,
random input, large chain simulation, full-workspace verification or commit
was used in this replay. This invocation printed JSON to stdout; it did not
create an execution JSON file. The module's broader main supports --output,
but invoking that main would exceed this deliberately narrow replay.
