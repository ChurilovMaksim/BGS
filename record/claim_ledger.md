# Claim ledger

## Every odd modulus, 29 October 2026

BGS-TRACE-124 is a project proof with an exact integer certificate and a Lean rational witness. Let \(N\ge3\) be odd. Then \(L_N(M_N;1)>3/4\) or \(L_N(M_N;1)<5/7\), and the two alternatives are exclusive because \(5/7<3/4\). The distance to \((1-e^{-2})/4\) is greater than \(1/2\) in the first case and less than \(1/2\) in the second. Raising an exponent cannot increase the ratio \(t(N)/N\). Every odd \(N\) whose radical is short is short, so \(315=3^2\cdot5\cdot7\) is short because its radical \(105\) has order \(12\). A non-preserving power of a non-short semiprime, or of \(195\), is short. A ratio-preserving tower over a ceiling semiprime satisfies \(L_N(M_N;1)<5/7\). The ratio-preserving towers on the other side, and \(3\cdot5^b\cdot13\) for \(b\ge2\), satisfy \(L_N(M_N;1)>3/4\). The fixed kick \(\tau=10^{-80}\) preserves the gap above \(3/4\) when \(8t(N)\le3N\) and \(N\le10^{39}\), through \(10^{26}\) on those ratio-preserving families whose pure margin exceeds \(13/420\), and through \(2\cdot10^{26}\) for \(N=15r\). The kick is not claimed for a ceiling tower: at \(3\cdot23\) the gap \(575/22594\) is smaller than \(13/420\). It is not claimed for an inert exponent-one partner \(q\ge40\), where the comparison that proves \(L>3/4\) lies below \(82/105\). It is not claimed for \(15r>2\cdot10^{26}\). The defect majorant exceeds \(1\) at every integer of \(79\) digits, and the second-order center of BGS-TRACE-119 already lies below \(3/4\) at index \(207\), so the kick at \(u_{207}\) is not proved. No density of orders is asserted. The signed off-diagonal sum remains open. [Proof](../mathematics/fixed-map/odd_modulus_abel.md), [certificate](../evidence/executions/20261029/odd-modulus-abel/README.md). BGS-TRACE-005 and BGS-BGS-001 remain OPEN.

## Square-free products of at least three primes, 29 October 2026

BGS-TRACE-123 is a project proof with an exact integer certificate and a Lean rational witness. Let \(N\) be square-free and divisible by at least three distinct odd primes. Then \(L_N(M_N;1)>3/4\), and the distance to \((1-e^{-2})/4\) is greater than \(1/2\). The argument bounds the order by \(\prod(p_i+1)/2^{r-1}\). Four or more prime factors are short, and strongly short. A product of three primes is short except \(N=195=3\cdot5\cdot13\), where the eight-term subset expansion lies above \(82/105\). The fixed kick \(\tau=10^{-80}\) preserves the gap through \(10^{39}\) when there are at least four prime factors and when \(15\) does not divide a product of three primes. On \(N=15r\) the kick uses the return series plus the defect of BGS-TRACE-122, and it stops at \(10^{26}\). Above that window the pure sum remains above \(3/4\) and the kick is not claimed. The modulus \(315=3^2\cdot5\cdot7\) is not square-free, and no bound is claimed for a prime square. Semiprimes remain the dichotomy of BGS-TRACE-122. No density of orders is asserted. The signed off-diagonal sum and the kick at \(u_{207}\) remain open. [Proof](../mathematics/fixed-map/squarefree_product_abel.md), [certificate](../evidence/executions/20261029/squarefree-product/README.md). BGS-TRACE-005 and BGS-BGS-001 remain OPEN.

## Chinese product for the cat-map trace square, 29 October 2026

BGS-TRACE-122 is a project proof with an exact integer certificate and a Lean rational witness. For every odd modulus, the pure trace square is the product of the trace squares at the prime-power factors, and the order of \(C\) is the least common multiple of the prime-power orders. On a square-free modulus the Abel sum is a finite combination of geometric series, one for each subset of the prime factors. Every product of two odd primes is then on a definite side of the thresholds. A short composite order, a non-short multiple of \(7\), and a non-short product of \(3\) with a short prime satisfy \(L_N(M_N;1)>3/4\). Every remaining semiprime satisfies \(L_N(M_N;1)<5/7\). The fixed kick \(\tau=10^{-80}\) preserves the gap above \(3/4\) for every such \(N\le10^{26}\) in three sub-families: \(N=21\), a split full-order multiple of \(7\), and a non-short product of \(3\) with a short prime of odd order. No such short prime is asserted to exist. The kick is not transferred to the side below \(5/7\) or to the inert full-order multiples of \(7\). The modulus \(N=195=3\cdot5\cdot13\) has order \(84\) and is not short; no bound is claimed for three or more distinct prime factors. No density of orders is asserted. The signed off-diagonal sum and the kick at \(u_{207}\) remain open. [Proof](../mathematics/fixed-map/crt_composite_abel.md), [certificate](../evidence/executions/20261029/crt-composite/README.md). BGS-TRACE-005 and BGS-BGS-001 remain OPEN.

## Cat-map order trichotomy, 29 October 2026

BGS-TRACE-121 is a project proof with an exact integer certificate and a Lean rational witness. The order of \(C\) modulo an odd prime divides \(p-\varepsilon\), where \(\varepsilon=1\) exactly when \(p\equiv\pm1\pmod8\). Every such order is short, long, or split-half. A short order with \(p\ge5\) gives \(L_p(M_p;1)>3/4\). A long order gives \(L_p(M_p;1)<5/7\). The only split-half prime below \(17\) is \(p=7\), where the full Abel sum is above \(3/4\); the return subsum alone is still below \(3/4\), and the unit-trace terms cross the threshold. Every larger split-half prime has \(L_p(M_p;1)<41/60\). For a prime power the same alternatives are read off the lifting depth of the first return. Every power of \(7\) stays above \(3/4\). Every depth-one power of a split-half prime \(p\ge17\) stays below \(5/7\). Depth at least two makes the higher powers short, so they lie above \(3/4\) even when the prime itself lies below \(5/7\): this happens at \(p=13\) and at \(p=31\). The fixed kick preserves the prime comparisons through \(10^{26}\) and the large split-half powers through \(10^{25}\). For every odd \(n\ge5\), \(t(u_n)\) divides \(n\), so the pure map at \(u_n\), including the \(79\)-digit dimension \(u_{207}\), is already above \(3/4\). The kick at \(u_{207}\) remains outside every proved window. No density of orders is asserted, and a modulus with two distinct prime factors is not classified. [Proof](../mathematics/fixed-map/order_trichotomy_abel.md), [certificate](../evidence/executions/20261029/order-trichotomy/README.md). BGS-TRACE-005 and BGS-BGS-001 remain OPEN.

## Cat-map order and the Abel statistic, 28 October 2026

BGS-TRACE-120 is a project proof with an exact integer certificate and a Lean rational witness. Let \(t(N)\) be the multiplicative order of the frequency matrix \(C\) modulo an odd dimension \(N\ge3\). If \(12t(N)\le5N\), the pure cat map satisfies \(L_N(M_N;1)>3/4\). If \(p\) is an odd prime and \(2t(p)\ge p+1\) (with the direct evaluation \(t(3)=4\)), then \(L_p(M_p;1)<5/7\), so the distance to \((1-e^{-2})/4\) is less than \(1/2\). The fixed kick \(\tau=10^{-80}\) preserves the short-order gap for every such \(N\le10^{39}\) and the long-order ceiling for every such prime \(p\le10^{26}\). The proof sums the geometric return ladder. At \(N=35\), which is not a Pell number, the order is \(6\) and the first return alone lies below \(3/4\). The prime \(p=7\) meets neither hypothesis, and its return subsum is below \(3/4\); the full sum at that prime is not decided. The kicked dimension \(u_{207}\) lies outside both digit windows. [Proof](../mathematics/fixed-map/order_ladder_abel.md), [certificate](../evidence/executions/20261028/order-ladder-abel/README.md). BGS-TRACE-005 and BGS-BGS-001 remain OPEN.

## Positive-time trace expansion, 28 October 2026

BGS-TRACE-119 is a project proof with an exact integer certificate and a Lean rational witness. At the single dimension \(N=u_{205}\), the fixed kick satisfies \(L_N(U_N;1)>3/4\). The proof expands the kicked trace in diagrams. Every resonant diagram of degree at most 11 is an exact zero in \(\mathbb Z[\sqrt2]\), indecomposable successive gaps are at most 4, and the pinned activity plus the degree-\(\ge12\) tail leaves the Abel term above \(3/4\). The integer \(u_{205}\) has 79 decimal digits, so any effective statement that the Abel gap is less than \(1/2\) for all odd \(N\ge N_0\) needs \(N_0>u_{205}\). The third-order operator-norm remainder and the Hilbert--Schmidt triangle remain silent at this index; they are not used. At \(n=207\) the pure second-order center still satisfies \((1-\varepsilon_2)^2<3/4\), so no disk \(N(1-\varepsilon_2-E)\) with \(E\ge0\) proves the gap. That ceiling is a failure of the disk, not a proof that \(L_N\) drops. [Proof](../mathematics/fixed-map/positive_time_spike.md), [certificate](../evidence/executions/20261028/positive-time-spike/README.md). BGS-TRACE-005 and BGS-BGS-001 remain OPEN.

## Kick-blind arithmetic spikes, 28 October 2026

BGS-TRACE-118 is a project proof with an exact integer certificate and a Lean rational witness. At the single dimension \(N=u_{203}\), the fixed kick satisfies \(L_N(U_N;1)>3/4\). The proof expands the kicked trace to second order. Cross terms vanish except for the explicit overlap \(\gamma(1)=\gamma(202)=-7/2000000\), and the third-order remainder still leaves the Abel term above \(3/4\). The integer \(u_{203}\) has 78 decimal digits, so any effective statement that the Abel gap is less than \(1/2\) for all odd \(N\ge N_0\) needs \(N_0>u_{203}\). The same remainder majorant is at least \(1\) at \(n=205\), the Hilbert--Schmidt triangle is silent there, and at \(n=207\) the pure second-order center satisfies \((1-\varepsilon_2)^2<3/4\). That ceiling is a failure of the disk, not a proof that \(L_N\) drops. [Proof](../mathematics/fixed-map/orbit_orthogonal_kick_spike.md), [certificate](../evidence/executions/20261028/orbit-orthogonal-spike/README.md). BGS-TRACE-005 and BGS-BGS-001 remain OPEN.

BGS-TRACE-117 is a project proof with an exact integer certificate and a Lean rational witness. For every odd \(n\ge5\), the pure cat map at dimension \(N=u_n\) has \(L_N(M_N;1)>3/4\). For every odd \(n\) with \(5\le n\le201\), the fixed kick \(\tau=10^{-80}\) preserves the same gap for \(U_N\). The largest such dimension, \(u_{201}\), has 77 decimal digits, so any effective statement that the Abel gap is less than \(1/2\) for all odd \(N\ge N_0\) needs \(N_0>u_{201}\). The one-term lower bound stops beating \(3/4\) at \(n=203\). The argument is self-contained and overlaps the classical cat-map trace arithmetic of BGS-FM-010 without using that note as a lemma. [Proof](../mathematics/fixed-map/kick_blind_arithmetic_spike.md), [certificate](../evidence/executions/20261028/kick-blind-spike/README.md). BGS-TRACE-005 and BGS-BGS-001 remain OPEN.

## Aristotle formalization integration, 28 October 2026

Adapted all 39 substantive modules from the older Aristotle snapshot into the existing Lean 4.33.1 graph. The [coverage map](../formalization/MATHLIB_LAYER_RU.md) and [receipt](../evidence/formalization/aristotle_20261027/receipt.json) record exact theorem scope, 589 axiom-audited declarations and the successful aggregate build. ERR-060 corrects the pure-loss scalar identity in the proof and manuscript. Current claim states, TRACE-114–116 and pinned dependencies are retained; no BGS closure is asserted.

## Adopted operator continuation, 27 October 2026

TRACE-114, TRACE-115 and TRACE-116: analytic proofs reconstructed with author self-review; [full disposition and dependencies](trace005_continuation_review.md). They cover balanced short-trace rounding, bounded microscopic/positive pair stability and original-family pair transfer through O(N^-2) approximants. No CUE limit is supplied; BGS-TRACE-005 and BGS-BGS-001 remain OPEN. Earlier provisional nonregistration statements below are superseded for these three precise claims only.

## Provisional research checkpoint, 27 October 2026 (superseded above)

[Bounded microscopic test stability](../mathematics/trace-bridge/microscopic_unitary_stability_20261027.md) is an author argument pending verification; the stronger pair-transfer claims in the archive have not been registered.

[Balanced spectral rounding](../mathematics/fixed-map/balanced_rounding_research_20261027.md) is an author argument pending verification; no new proved registry claim is asserted. It builds on the barrier context of TRACE-025 and conditionally applies TRACE-113. TRACE-005 and BGS-BGS-001 remain open. The earlier chat reconstructions of FM-001, RES-006, TRACE-007 and TRACE-092 are credited to the existing repository results.

## Trace dependency closure, 22 October 2026

| Claim | Current status | Exact scope |
|---|---|---|
| BGS-TRACE-109 | ANALYTIC PROOF + SELF-REVIEW | [Inserted trace](../mathematics/fixed-map/inserted_trace_coboundary.md); the new [finite-grid proof](../mathematics/fixed-map/finite_grid_one_step_trace.md) supplies the $O(N^{-1})$ remainder without an all-time sector input |
| BGS-TRACE-110 | ANALYTIC PROOF + SELF-REVIEW | [Global spectral distance](../mathematics/fixed-map/spectral_orbit_distance.md); all-odd-$N$ upper bound $O(1/\log N)$ and matching Pell lower order, using TRACE-112/113 |
| BGS-TRACE-112 | ANALYTIC PROOF + SELF-REVIEW | [Displacement density and short logarithmic trace window](../mathematics/fixed-map/displacement_density_trace_bound.md); independent pressure-free upper spectral comparison |
| BGS-TRACE-113 | ANALYTIC PROOF + SELF-REVIEW | [Uniform power-trace bound](../mathematics/fixed-map/fixed_kick_uniform_trace_bound.md); one $N_0$ for all $m\ge1$, $|\operatorname{Tr}U_N^m|\le Ca^m$, $1<a<\sqrt{3+2\sqrt2}$; published pressure input separately checked |

[Proof/dependency review](spectral_research/trace_closure.md) and
[bounded execution evidence](../evidence/executions/20261022/trace-closure/README.md).
These results close the two qualifications recorded below on 21 October.
No external refereeing or formal proof is asserted. The bound $Ca^m$ becomes
uninformative at times proportional to $N$; the full signed pair plateau and
all higher factorial tests remain open. **BGS-TRACE-005 and BGS-BGS-001: OPEN.**

## Historical integration verdict, 21 October 2026 (TRACE-109/110 superseded above)

| Claim | Status at that checkpoint | Scope |
|---|---|---|
| BGS-TRACE-108 | ANALYTIC AUTHOR PROOF + SELF-REVIEW | [Quartic coordinate return](../mathematics/fixed-map/coordinate_return_quartic.md), one step at fixed coupling with explicit remainder; no microscopic pair limit |
| BGS-TRACE-109 | EXACT LEMMAS + CONDITIONAL ASYMPTOTIC APPLICATION | [Inserted trace and coboundary projection](../mathematics/fixed-map/inserted_trace_coboundary.md); arbitrary multiplicities handled, numerical asymptotic bound retains the older amplitude/sector construction |
| BGS-TRACE-110 | EXACT LEMMAS + CONDITIONAL ASYMPTOTIC APPLICATION | [Spectral orbit distance](../mathematics/fixed-map/spectral_orbit_distance.md); uniform original-family trace input (T) not fully independently closed here |
| BGS-TRACE-111 | ANALYTIC AUTHOR PROOF + SELF-REVIEW | [Full weighted Pell gradient/Hessian and forced inflection](../mathematics/fixed-map/pell_weighted_curvature.md); initial point and shrinking times, not the fixed positive parameter |

[Complete integration and review](spectral_research/spectral_final_integration.md)
accounts for all 535 source units, six historical version qualifications,
56 bounded research checks and distinct original/fresh evidence. Source
preservation and internal author audits are not blanket mathematical
certification. Previously integrated TRACE-106/107 and TRACE-086 remain at
their stated scopes. **BGS-TRACE-005 and BGS-BGS-001 remain OPEN.**

## Physical-kick review, 21 October 2026

**BGS-TRACE-106:** [Uniform physical-kick decay](../mathematics/fixed-map/physical_kick_trace_decay.md)
strengthens the imported exponent 1/25 to 1/9 on the same explicit small-time
interval; bounded-time decay and maximal scalar-distance limits concern the
single kick. **BGS-TRACE-107:** [All-order polynomial error control](../mathematics/fixed-map/physical_trace_polynomial_approximation.md)
extends the pair replacement bound to every fixed factorial order and records
the exact Pell two-copy alias threshold. Both are analytic author proofs with
self-review; finite checks certify only their stated finite inputs.

[Exact source review and coverage](spectral_research/spectral_master_audit.md) explicitly
leave most historical blocks unreviewed. BGS-TRACE-005 and BGS-BGS-001 remain
OPEN; no original signed Heisenberg sum has been evaluated by these results.

## Signed circular-phase continuation, 19 October 2026

**BGS-TRACE-005 and BGS-BGS-001 remain OPEN.** All following proofs are author
proofs with self-review; exact finite computations are used only at their stated
scope. No independent review, compiled Lean certificate or priority is asserted.
[Full adopted statements and proof revisions](../mathematics/trace-bridge/phase_ensemble_continuation.md).

| Stable ID | Disposition | Exact boundary |
|---|---|---|
| BGS-TRACE-095 | CONDITIONAL author proof | Dimension-uniform feedback under pinned trajectory/moment and reversal inputs; no fixed two-channel substitution. |
| BGS-TRACE-096 | Exact identities and criterion | Transmission versus bounded eigenvector ratio law; the required limiting law is not identified. |
| BGS-TRACE-097 | CONDITIONAL author proof | Complete normalized positive Heisenberg path current under TC, not a signed trace law. |
| BGS-TRACE-098 | Author proof | All fixed traces and secular hierarchy of the symplectic phase model; t2=t1 squared exactly. |
| BGS-TRACE-099 | Author proof | Polynomial trace windows and fixed interior disk; no microscopic absorption limit. |
| BGS-TRACE-100 | Author computer-assisted proof | Exact signed formula and first two stable cancellations for fixed m>=17, all odd primes. |
| BGS-TRACE-101 | Author proof | Connected j<=delta+1; finite primitive schemes at each fixed defect, not all-defect summability. |
| BGS-TRACE-102 | Author computer-assisted proof | Full four-port kernel and complete total defect two for tau<1; stable degree bound, not vanishing. |
| BGS-TRACE-103 | Author computer-assisted proof | All individual defects <=2 in arbitrary counts for tau<1/9; normalization V_m/m; residual begins -3 tau^3. |
| BGS-TRACE-104 | Author proof with classical averaging | Local iid-phase/Cauchy comparison for a Hermitian involution; universality remains a separate hypothesis. |
| BGS-TRACE-105 | Author proof, classical mechanism | Exact positive Cauchy source law and genuine matrix-law counterexample; no BGS counterexample or novelty claim. |

[Complete import and correction map](../archive/record/chat_integration_20261019.md) records the
other adopted auxiliary results and preserves conditional G/TC/R assumptions.
ERR-031 marks the stale original failed transmission run. The current invalid
first prefix implementation and failed missing-dependency checker are retained
and excluded from mathematical evidence. Finite run completion is not a theorem
status. Historical unknown-four-port sentences are superseded only by TRACE-102.

## Complete flat collision law, 16 October 2026

**BGS-TRACE-094 — PROJECT PROOF + INDEPENDENT INTERNAL CORE RECONSTRUCTION.**
[The full high-derivative proof](../mathematics/trace-bridge/wick_collision_poisson.md)
proves C_edge => Poisson(2alpha^2) and B/G -> exp(-alpha^2) at m/N->alpha>0
under the exact flat positive Wick measure. The previously missing bound for
every fixed coordinate derivative and all partial contractions is proved.
Collision locations have a uniform Poisson limit; fixed distinct vertex
occupations have independent geometric mean-alpha limits. The iid radial
corollary requires all even moments <=j!.

[Review and current route checkpoint](../archive/record/wick_poisson_continuation_20261016.md)
distinguish the independently reconstructed core, author-derived corollaries
and exact finite evidence. The earlier open-law sentences for TRACE-093 are
superseded ONLY for this flat auxiliary measure. The non-flat physical profile,
full signed cancellation, TRACE-005 and BGS-BGS-001 remain OPEN.

## Abel rigidity and flat equal-edge continuation, 16 October 2026

**BGS-TRACE-092 — PROJECT PROOF + INDEPENDENT INTERNAL RECONSTRUCTION.**
[Exact decomposition and optimal rigidity](../mathematics/trace-bridge/abel_clock_rigidity.md)
split the Abel excess into a nonnegative low-mode term and a geometric pair
energy. Stationary intensity-one processes obey a square-root local transport
bound to the uniform clock; alternating gap spectra prove the exponent optimal.
The fixed physical Abel excess remains unestimated.

**BGS-TRACE-093 — PROJECT PROOF + CHECKED CLASSICAL INPUT + INTERNAL REVIEW.**
[Gaussian comparison](../mathematics/trace-bridge/gaussian_equal_edge.md) proves
B/G->1 for every m=o(N) in the exactly flat equal-edge sector. At m/N->alpha>0,
log(B)/N tends to (1+alpha)log(1+alpha)-alpha and its Wick collision mean tends
to 2alpha^2, with triple edges negligible. The limiting collision law and
limiting ratio are subsequently evaluated by TRACE-094 for this same flat measure. The Gaussian finite product and sinh crossover
are prior 2002 results. The physical non-flat profile and full signed trace
are separate unresolved steps.

[Research checkpoint](../archive/record/research_continuation_20261016.md) records the route tree,
proof reviews, finite checks and exact next obligations. Neither result closes
BGS-TRACE-005 or BGS-BGS-001. No award-level or world-priority assessment follows
from an internal proof or the finite execution receipts.

## Imported research record, 16 October 2026

**Scope:** author self-review and fresh finite replay. The source inventory has
90 entries; this is not a fresh independent certification of all 90 statements.
The untouched historical text cannot override the dispositions below.
[Review and correction map](../archive/record/chat_integration_20261016.md).

| Stable ID | Status | Canonical source | Exact boundary |
|---|---|---|---|
| BGS-FM-032 | PROVED as scoped | [proof](../mathematics/fixed-map/quantum_cyclic_cohomology.md) | Additive normalized-HS cohomology and initial eigenphase response only; fixed physical strength grows as tau*p. No multiplicative holonomy or microscopic limit. |
| BGS-TRACE-084 | PROVED as scoped | [proof](../mathematics/trace-bridge/resonant_mesoscopic_criterion.md) | Sufficient selected-sector deletion criterion only; the sector need not vanish for a valid full signed local law. |
| BGS-TRACE-085 | PROVED as scoped | [proof](../mathematics/trace-bridge/root_lifting_sector_boundary.md) | Abstract spectra, including deterministic existence via CUE local-average variance. Does not identify root labels or traces of the maintained propagator. |
| BGS-TRACE-086 | PROVED as scoped | [proof](../mathematics/trace-bridge/all_order_process_closure.md) | The implication is proved; H_diag and TRACE-005 for the frozen matrix remain open. Every fixed order and every compact bandwidth are required. |
| BGS-FM-033 | CONDITIONAL as scoped | [proof](../mathematics/fixed-map/scaled_weyl_overlap.md) | Conditional on the exact quantitative G1-G3 analytic inputs pinned in the source. Finite algebra checks do not recertify those analytic inputs. No cyclic Heisenberg trace bound. |
| BGS-CUE-002 | PROVED as scoped | [proof](../mathematics/trace-bridge/full_pair_cue_covariance.md) | Exact deterministic derivative and CUE reference covariance. Proxy computations are diagnostics, not a physical limit or a p-value. |
| BGS-TRACE-087 | PROVED as scoped | [proof](../mathematics/trace-bridge/parameter_deaveraging.md) | Only the reduction is proved. The required physical parameter q-moment o(N^-2), or sixth moment O(N^-3), is unproved; Haar sixth moments cannot supply it. |
| BGS-TRACE-088 | PROVED as scoped | [proof](../mathematics/trace-bridge/equal_edge_occupation.md) | Dense-mixing intensities with a fixed C and rho<1; cancellation is established only to an O(N^2) remainder. Equal-edge is smaller than the vertex-balanced sector. |
| BGS-TRACE-089 | PROVED as scoped | [proof](../mathematics/trace-bridge/collision_crossover.md) | m tends to infinity with m/sqrt(N) tending to a fixed finite c; not m of order N. Harer-Zagier is a classical external input. |
| BGS-TRACE-090 | PROVED as scoped | [proof](../mathematics/trace-bridge/bounded_radial_ratios.md) | Any unitary spectrum. The mixed-moment convergence premise for the frozen model is open; weak convergence alone supplies no unbounded count UI. Discrete Toeplitz contraction requires grid M>=N. |
| BGS-TRACE-091 | PROVED as scoped | [proof](../mathematics/trace-bridge/hardy_spectral_remainder.md) | p is the characteristic polynomial of a unitary, with all roots on the unit circle. Self-inversiveness alone is insufficient. Required CUE excesses are positive and unproved for the physical family. |

**BGS-TRACE-005 and BGS-BGS-001 remain OPEN.** The conditional implication
H_diag => Sine2 supplies local UI at every fixed moment order. Pair-only or
bounded-ratio convergence does not. The late-chat Gaussian comparison was unverified at import time. The subsequent
BGS-TRACE-093 reconstruction proves it and strengthens its range to every
m=o(N); it does not certify the unavailable original derivation.


## Observed pulse and cyclic memory, 14 October 2026

**BGS-TRACE-083 — PROJECT PROOF + INDEPENDENT INTERNAL RECONSTRUCTION.**
[The first-return theorem](../mathematics/spectral-obstructions/coherent_first_return_pulse.md)
strengthens TRACE-082's full-return example to a specified individual
coefficient L E^(2p-2) C. For the TRACE-081 abstract family this map is
almost an isometry on (4^k-1)(p-1) centered diagonal directions.
Exact finite-support amplitudes, uniform perturbation bounds and a
total observed energy tail at most 16 N^-6 are proved.
Despite that tail bound, low unconjugated pulse traces can vanish while
cubic cyclic compositions survive. These powers are not later
first-return coefficients and are not conjugated covariance moments.
The example excludes source-uniform norm shortcuts; it estimates
neither the actual physical cavity source nor TRACE-005.

[Independent proof and actual execution scope](../archive/evidence/executions/20261014/first-return/README.md).
The new claim is analytically proved in the project; no full operator
Lean certification is asserted. Main 57150ac's CI did not provide
code-step receipts and skipped the new formalization job. Its earlier
236 local tests and 5 focused checks precede this continuation;
they are not a certificate of this later source revision.

## Spectral and coherence obstructions, 14 October 2026

**BGS-TRACE-081 — PROJECT PROOF + INDEPENDENT INTERNAL RECONSTRUCTION.**
[Perfect intensity mixing does not identify microscopic statistics](../mathematics/spectral-obstructions/flat_spectrum_obstruction.md).
For any odd-prime sequence p_k->infinity, the abstract dimensions N_k=4^k p_k
support deterministic simple-spectrum unitaries with P=J, reversal norm2^-k
and a uniform macroscopic eigenphase measure. Origin-averaged microscopic
point processes converge vaguely in probability to the empty measure;
unfolded spacing distributions converge weakly to delta0, with non-UI
counts. Normalized form factors diverge at times asymptotic to N_k.
A self-contained generic-column phase lemma applies to every invertible
complex matrix. No unchanged fixed-map, smooth chaotic quantization,
full phase-ensemble contradiction, BGS, priority or analytic formal claim.

**BGS-TRACE-082 — PROJECT PROOF + INDEPENDENT INTERNAL RECONSTRUCTION.**
[Exact return memory and singular-norm plateau](../mathematics/spectral-obstructions/coherence_memory_plateau.md).
Every unitary in dimension N>=2 has ||(Q Ad_U Q)^r||=1 in Hilbert--Schmidt
operator norm for integers0<=r<N. Exact resolvent/return recurrence is
self-contained; TRACE-081 separately gives order-one observed return
memory near Heisenberg time. Equality of norms is not a spectral-radius
assertion or a nondecay assertion for every source. A precise prose error
in the frozen draft was corrected: dephased and unmeasured operators need
not agree, but can agree for special unitaries. Lean source covers only the
arithmetic positivity budget. Compilation of the new CoherenceBudget module
is currently unconfirmed; the new main 57150ac formalization job was skipped.
[Independent reconstruction and actual finite scope](../archive/evidence/executions/20261014/spectrum-coherence/README.md).

This is the current scientific-status authority. A project proof is not an external referee certificate. The [core registry](claims.json) deliberately covers fewer statements than the full corpus; the theorem-family tables below retain the broader claims.

## Unconditional feedback trajectory, 13 October 2026

**BGS-TRACE-080 — PROJECT PROOF + INDEPENDENT INTERNAL RECONSTRUCTION.**
[The global feedback theorem](../mathematics/trace-bridge/unconditional_feedback_flatness.md)
starts from any deterministic unitary family with intensity bound C0/N and
centered singular norm at most 1/100. Fresh independent uniform phases and
uniform ports give simultaneous entry flatness, intensity gap, row/column
fourth-power energies and two-step control at every retained depth
u>=ceil(log(2N)^(4+kappa)), with failure O(log(2N)^(-1-kappa)). One common
first-exit rule retains every full and simultaneous crossing; no future
flatness event is conditioned upon. Row/column energy supplies the early
three-step forcing that the maximum-entry estimate could not provide.
TRACE-060 at exactly this cutoff then gives unconditional every-fixed-order
clocks and the uniform empirical weak law. The reference atom and pathwise
rank lower bound keep their original scope. TRACE-073 C9 additionally gives
uniform reversal-norm convergence when its separate initial norm tends to
zero; FM-021/FM-022 supply named eventual actual-map inputs only.
No effective startup, smaller general cutoff, growing-order or edge law,
physical microscopic reference, TRACE-005 or BGS is proved.
[Review and actual finite scope](../archive/evidence/executions/20261013/global-feedback-flatness/README.md).

**BGS-TRACE-079 — PROJECT PROOF + INDEPENDENT INTERNAL RECONSTRUCTION.**
[All-pair stopped concentration](../mathematics/trace-bridge/two_step_stopped_concentration.md)
includes diagonal pairs, endpoint freezing, deterministic scalar continuation,
and the full first entry/three-step crossing. Its quantitative scalar tail
and shrinking-Green corollary give 9/u on reached deep-range states. That
stopped theorem alone makes no early-survival estimate; the separate
TRACE-080 argument supplies the unconditional global trajectory result
under stronger startup hypotheses.
[Review and exact controls](../archive/evidence/executions/20261013/stopped-concentration/README.md).

## Two-step fluctuation control, 13 October 2026

**BGS-TRACE-078 — PROJECT PROOF + INDEPENDENT INTERNAL RECONSTRUCTION.**
[The complete second moment](../mathematics/trace-bridge/two_step_increment_variance.md)
is at most `2600 delta²[(P²)ij+(P³)ij]/u` for a conditionally uniform
port among all labels, with frozen endpoint increments zero and
`delta<=1/4`. The stronger deterministic sum over ports holds for any
circle phases; phase independence is unnecessary for this bound.
Complete row/column Parseval controls the linear coefficient before
absolute values; all higher coherent feedback terms remain included.
This is a raw second moment, not a concentration theorem or survival
estimate. Together with TRACE-075 and TRACE-077 it supplies complementary
one-step fluctuation, mean and deep-range forcing inputs. These one-step inputs are completed by the separate TRACE-079/080
concentration and trajectory results on their stated cutoff. TRACE-005
and BGS remain open.
[Independent review and finite scope](../archive/evidence/executions/20261013/two-step-variance/README.md).

## Shrinking stopped gaps, 13 October 2026

**BGS-TRACE-077 — PROJECT PROOF + INDEPENDENT INTERNAL RECONSTRUCTION.**
[Green-coordinate compression](../mathematics/trace-bridge/green_compression_gap.md)
turns classical stochastic complementation into orthogonal compression of
`M=(I-P+J)^(-1)-I`. With deterministic unitary initial flatness `C0/N`
and singular norm at most `1/5`, fresh independent feedback phases and
port choices made before their phase, the original term is bounded by
`min(1/4,Bu/N)`. An adapted matrix martingale and quadratic remainder give
an unconditional quantitative bound through the first entry exit,
including simultaneous exits. At reached, entry-admissible depths
`log(2N)^(7+kappa) <= u <= N/log(2N)^2`, the singular norm is
`O(log(2N)^(-2))` except with probability `O(log(2N)^(-kappa))`.
The three-step kernel is then `(1+O(1/log(2N)))/u` before entry exit.
TRACE-077 alone does not estimate the probability of reaching that range;
TRACE-079/080 supply the separate concentration and probability results
for their stated initial class and cutoff. TRACE-005 and BGS remain open. Actual-map startup uses only named FM-021
initial inputs. No new formal certificate or priority claim is asserted.
[Review and finite scope](../archive/evidence/executions/20261013/green-compression/README.md).

## An unconditional clock class, 12 October 2026

**BGS-TRACE-076 — PROJECT PROOF + INDEPENDENT INTERNAL RECONSTRUCTION.**
[The exact Haar feedback law](../mathematics/trace-bridge/haar_feedback_clock_law.md)
couples a Haar effective scattering matrix, independent of its incoming
delay, to \(T=I+X^*X\) with density
\(\det(I+X^*X)^{-(N+u)}\). It gives the inverse-Jacobi spectrum,
the exact rectangular atom, threshold \(k<u+1\) for trace moments when
\(N>u\), and \(\mathbb ET=(N/u)I\).
Haar marginals yield a simultaneous flatness failure bound
\(N^3(2N)^{-K(1-1/m)}\), \(m=\lceil\log(2N)^{1+\kappa}\rceil\).
TRACE-060 then supplies unconditional full-depth laws at every fixed clock
order and the empirical weak law. These extend to independent initial
distributions with relative entropy \(O(\log N)\) by taking \(K\) after
\(\limsup_N\). Only the \(o(\log N)\) class receives high-probability
flatness for each specified \(K>3\).
A bounded-entropy microscopic-gap ensemble disproves the corresponding
prescribed-origin Sine₂ implication, without an origin-averaged claim.
The maintained deterministic initial matrix is outside this entropy class;
TRACE-080 now supplies its feedback probability on the larger stated
cutoff. Physical microscopic TRACE-055, signed TRACE-005 and BGS remain open. Prior Cauchy/Haar projection/beta objects are credited.
[Exact review and execution scope](../archive/evidence/executions/20261012/haar-feedback/README.md).

## Unitary two-step obstruction, 12 October 2026

**BGS-TRACE-075 — PROJECT PROOF + INDEPENDENT INTERNAL RECONSTRUCTION.**
[The exact fresh-phase drift](../mathematics/trace-bridge/two_step_restoring_drift.md)
bounds the complete two-step coherence by a three-step path-swap pairing.
For max intensity \(\delta\le1/16\), it gives
\(\mathbb E\Delta K_{ij}\le[-K_{ij}/2+5(P^3)_{ij}+2\delta P_{ij}]/u\),
with endpoint freezing and uniform selection among all \(u\) labels.
At the TRACE-074 constructed peaks,
\(\mathbb E\Delta K_{ij}=-(1+o(1))K_{ij}/u\).
The core theorem is self-contained; TRACE-074 supports only its comparison
and witness corollary. TRACE-078/079/080 now provide the separate fluctuation, concentration and
trajectory companions at their explicit scopes. Microscopic identification
and BGS remain unproved.
The original averaging sentence was corrected before promotion.
[Review and exact finite scope](../archive/evidence/executions/20261012/two-step-drift/README.md).

**BGS-TRACE-074 — PROJECT PROOF + INDEPENDENT INTERNAL RECONSTRUCTION.**
[Two rank-one unitary corrections](../mathematics/trace-bridge/unitary_two_step_obstruction.md)
give genuine unistochastic matrices with max-entry bound
\(8\log(2n)/n\), vanishing centered intensity singular norm and an exact
two-step peak \(1/\lfloor n/\log(2n)\rfloor\). A universal extra
singular-norm factor in the two-step estimate is false. The correct
higher-step factor is \(\rho^{h-2}\); this sequence is uniformly mixed
at the third step and has a one-step Schur variance
\(\sim\log(2n)/n^2\) at the exceptional pair. The constructed states are
not asserted to occur along the maintained trajectory. This is neither
a BGS counterexample nor a flatness-probability theorem. Priority and
analytic Lean certification are not claimed.
[Exact review and execution scope](../archive/evidence/executions/20261012/unitary-two-step/README.md).

## Checked research integration, 11 October 2026

This checkpoint integrates the complete retained 8--11 October chat research
against main 9e3c90fb18fbdca8b0fd7d192aab0b76dd2d757d. It distinguishes
internal proof reconstruction, finite execution and external law inputs.
Priority and a solution of global BGS are not claimed.

| Claim | State | Canonical source | Exact boundary |
|---|---|---|---|
| BGS-TRACE-057 | PROVED | [Arbitrary-source phase covariance](../mathematics/trace-bridge/source_covariance.md) | The arbitrary complex source bound is an exact contraction theorem; it does not identify a microscopic reference law. |
| BGS-TRACE-058 | PROVED | [Integrable all-order phase absorption](../mathematics/trace-bridge/integrable_phase_absorption.md) | Every fixed Lp absorption bound and Abel continuity; no uniformity as p grows and no local-law identification. |
| BGS-TRACE-059 | PROVED | [Anisotropic physical-source transport](../mathematics/trace-bridge/physical_source_transport.md) | Phase-independent positive clock, trace m, bounded normalized second moment, endpoint flatness and gap. L2 scalar comparison and fixed derivatives only; no higher physical-source mixed moments or actual-cavity hypotheses. |
| BGS-TRACE-060 | CONDITIONAL | [Joint incoming and outgoing delay bootstrap](../mathematics/trace-bridge/delay_bootstrap.md) | Strengthened [conditional proof](../mathematics/trace-bridge/all_moment_delay_bootstrap.md): joint first-delay concentration, all fixed killed upper moments and [uniform equality laws at every fixed order](../mathematics/trace-bridge/conditional_clock_universality.md), with the [full-depth measure and exact rank atom](../mathematics/trace-bridge/full_depth_clock_measure.md) down to ceil(log(2N)^(1+kappa)). For arbitrary startups the premise remains conditional; TRACE-080 closes it for the explicit entry-flat small-gap class at log^(4+kappa). Smaller cutoffs, growing-order/edge bounds, physical microscopic identification and unrestricted exceptional-event moments remain open. |
| BGS-TRACE-061 | PROVED | [Finite frame identities, Stiefel threshold and clock-basis obstruction](../mathematics/trace-bridge/fresh_phase_average.md) | Exact finite controls and the specified Haar-frame comparison model. A constructed clock/basis obstruction at one phase point is not a typical phase-ensemble or literal-map counterexample. |
| BGS-TRACE-062 | PROVED | [Flat completion with arbitrary clock law](../mathematics/trace-bridge/flat_completion.md) | Constructed flat unitary completions and a prescribed mean-one clock law; no independently sampled phase-ensemble violation and no change-free counterexample to the maintained quantization. |
| BGS-TRACE-063 | PROVED | [Global noncommuting ordinary-body coercivity](../mathematics/trace-bridge/nonlinear_coercivity.md) | Strict matrix balls, intensity singular gap, exact determinant defect and source derivatives. Ordinary-body coercivity alone does not control the entire graded integral. |
| BGS-TRACE-064 | PROVED | [Sharp maximal-torus contraction for compact simple groups](../mathematics/trace-bridge/torus_contraction.md) | Central L2 functions under Haar sampling, sharp 1/(h+1) variance factor. A chosen deterministic scattering matrix and circular symmetric spaces require separate statements. |
| BGS-TRACE-065 | PROVED | [Signed finite-field cycle and collision calculus](../mathematics/trace-bridge/coherence_form_factor.md) | Explicit finite-field Fourier scattering with reused independent phases. Leading ramp n=o(N^(1/8)); symmetric first correction n=o(N^(1/9)), not N^(1/7), not Heisenberg times. Dihedral occupation sector alone does not provide the plateau. |
| BGS-TRACE-066 | PROVED | [Birthday rank law and thinned collision limit](../mathematics/trace-bridge/previous_rank_results.md) | Recovered proof of the rank/collision coupling, specified Poisson TV bound and stated CLT window. An unsaved proposed N^(1/7) correction is explicitly unconfirmed; no variance asymptotic inferred from L1 coupling. |
| BGS-TRACE-067 | PROVED | [Sharp balanced Laurent Jack coefficient bound](../mathematics/trace-bridge/jack_coefficient_theorem.md) | All alpha>0, nonzero balanced signatures and K>=1: ratio at most 1/(N+alpha K); unique sharp highest-root mode. External priority is not established. |
| BGS-TRACE-068 | PROVED | [Frozen circular phase laws in the three symmetry classes](../mathematics/trace-bridge/phase_contraction.md) | Haar circular background frozen once, randomness then only in compatible phases; spectral L2 functions, paired CSE phases and half trace. Full conditional weak Sine-beta limit in probability over the background. No prescribed deterministic-background theorem or Sine-limit rate. |
| BGS-TRACE-069 | PROVED | [All-order critical CSE trace limit](../mathematics/trace-bridge/exact_cumulants.md) | Growing n/N->1, d=o(N), logarithmic critical variance, every fixed cumulant and mixed moment, conditional Gaussian law. Second/fourth cumulants are prior HSW formulas; no independent-block interpretation or external novelty certificate. |
| BGS-TRACE-070 | PROVED | [Complete CUE and CSE form-factor curves](../mathematics/trace-bridge/form_factor_curve.md) | Mean L2(0,T) convergence of the ceil(N*tau) interpolation and all-time individual CSE MSE control. No expected temporal supremum; floor interpolation with n=0 is excluded. The limiting curves are prior work. |
| BGS-TRACE-071 | PROVED | [Maximal phase point-process paths and all fixed normal-source products](../mathematics/trace-bridge/laplace_path_transport.md) | Full centered point-process path comparison on R^2 loglog(1/delta)/log(1/delta)->0; all fixed normal-source Lp products and derivatives. Random clock is conditioned on the phase-independent past. No initial law, no Lp norm of a continuous supremum, no higher physical-source product assertion. |
| BGS-TRACE-072 | PROVED | [Deterministic maximal microscopic observable flow](../mathematics/trace-bridge/deterministic_path_transport.md) | Finite-N maximal path bound under one common observation origin. Actual-map growing interval o(sqrt(log N)) uses FM-018 mixing/Egorov and a fixed smooth exactly centered symbol. The time-average endpoint mechanism is prior corpus work; the initial law and BGS remain open. |

The [integration disposition](../archive/record/chat_integration_20261011.md) records every
research branch, prior overlap, corrected guesses and unclosed candidates.
TRACE-055 remains verification-pending after its covariance, physical-source
and conditional barrier components were reconstructed. TRACE-080 now supplies
the maintained startup's probability and matching clock/channel applications
at log^(4+kappa). The scalar microscopic law remains unresolved.
**BGS-BGS-001 and the every-fixed-order signed TRACE-005 remain OPEN.**

## Reviewed 8 October continuation

| Claim | Current status | Exact authority |
|---|---|---|
| BGS-TRACE-053 | PROJECT PROOF + independent internal reconstruction | [Max-entry phase memory](../mathematics/trace-bridge/max_entry_phase_channel.md): complete collision corrections, degree-two norm, explicit averaged-pinching rate; no microscopic spectral law |
| BGS-TRACE-054 | STRENGTHENED PROJECT PROOF + independent internal reconstruction | [Sharp matrix inner jets](../mathematics/trace-bridge/sharp_inner_jet.md): optimal leading 4/3 for general noncommuting rational inner F=zG; localization penalty retained |
| BGS-TRACE-055 | VERIFICATION-PENDING SUBMISSION | [Audit disposition](../archive/record/research_checkpoint_20261008.md): the complete submitted hierarchy remains pending; covariance and physical L2 transport are reconstructed, while delay and gap results retain all-time-flatness hypotheses |
| BGS-TRACE-056 | PROJECT PROOF + independent internal reconstruction | [Direct real-flow scalar transport](../mathematics/trace-bridge/phase_channel_real_flow.md): normally absorbed unweighted scalar L1 source comparison and fixed derivatives; no mixed products or anisotropic source |

[Proof review and bounded executions](../archive/evidence/executions/20261008/phase-channel-jet/README.md)
are separate evidence tiers. The 4/3 matrix theorem improves the submitted
13/3 inequality; no world-priority verdict is made. TRACE-053 operator norm
cannot be promoted to a microscopic superoperator-trace law. TRACE-055 is a
submitted claim, not a proved dependency for another accepted result.
**BGS-BGS-001, TRACE-005, actual balanced law and signed deterministic transfer
remain OPEN.** Earlier dated checkpoints retain their historical scope.

## Current decision and scope

- **BGS-BGS-001 and TRACE-005 remain OPEN:** signed Heisenberg-scale joint traces of the unchanged deterministic map.
- **FLOW-014:** actual-start noisy weak local convergence on its specified logarithmic-time, polynomial-step schedule.
- **FLOW-017:** all fixed factorial orders and one-chain L2 averages on a different, superpolynomial schedule; this supersedes a blanket statement that every unbounded-correlation transfer remains open.
- **FM-020:** the original m=1 two-copy microscopic-rate obligation is closed by the reviewed project proof. FM-018/019 historical statements that this rate is open describe their earlier checkpoints.
- **Higher-copy rates, nonlinear quenched determinants and deterministic noise removal remain OPEN.**
- The scoped corpus revision and its known standalone-verifier repair passed remote acceptance at `0ffb20cc152d0ddd2620887e46d21d1120b95fd8`. Research has resumed; [review coverage](../archive/record/corpus_revision_20261006.md) records its limits.
- **TRACE-014:** all-copy induced-HS channel proximity can coexist with an exact clock spectrum in the same ensemble. This is a negative control on unqualified universality criteria, not a counterexample to the frozen map.

Exact statements: [FLOW-014](../mathematics/fixed-map/circular_dyson_actual_start.md), [FLOW-017](../mathematics/fixed-map/coboundary_all_order_limit.md), [FM-020](../mathematics/fixed-map/original_channel_gap.md), and [the obligation board](../mathematics/open_questions.md). The [registered dependency view](claim_registry.md) does not replace canonical proofs.

- **FM-021/FM-022:** actual position-chain mixing, the cyclic ramp, a specified marked three-link estimate, and reverse-cyclic suppression are established in their project proofs. General once-counted noncyclic sums and the spectral plateau correction remain open.

## Reviewed bounded proof batch, 6 October 2026

- **BGS-TRACE-015 — project analytic proof, independent internal review, exact finite controls.** [Once-counted three-block cancellation](../mathematics/fixed-map/three_block_unmarking.md), with distinct ports and all nonempty link lengths, has signed compact positive Heisenberg-band ambiguity error O_w((log N)^5/N), plus superpolynomial and exponential terms. FM-021 supplies actual fixed-coupling inputs. Repeated ports, general reconnections and the full signed remainder remain open.
- **BGS-FM-023 — project analytic proof, independent internal review, portable exact finite controls.** [Arithmetic translation exclusion](../mathematics/spectral-obstructions/arithmetic_translation_exclusion.md): for odd d>=3 dividing N, compression is at most min(1,C_tau(d^262/N)^(1/129)). C_tau is independent of N,d and labels; every fixed delta<1/262 gives uniform residual sqrt(2)+o(1) for d<=N^delta. All fixed d follow. The projector corollary requires a nonzero centered part in this algebra. No arbitrary-projector exclusion, endpoint decay or optimality claim.
- **BGS-TRACE-016 — project analytic proof, independent internal review, computer-assisted classification input.** [Once-counted reduced four-block cancellation](../mathematics/fixed-map/four_block_unmarking.md), with distinct ports and all nonempty link lengths, has signed compact positive Heisenberg-band error O_w((log N)^10/N), plus superpolynomial and exponential terms. The [universal rank-two classification](../mathematics/fixed-map/four_cut_rank_two_classification.md) has a separately reviewed mathematical compression/lifting proof and bounded kernel. Repeated ports, growing/general reconnections, inter-family overlaps and full signed statistics remain open.
- **BGS-FORMAL-002 — FINITE-CERTIFICATE.** The bounded executable predicate checks pairs 5..12 (3858 configurations, 560 directed local matches) and oriented triples 5..10 (650 configurations, zero matches) with native-evaluation trust; m=4 exclusions use ordinary decide. Compilation is separate from mathematical compression/lifting, abstract-word correspondence, and the analytic TRACE-016 chain: those are not formalized.

All analytic claims retain odd N and literal fixed tau=10^-80 where applied to the actual model. No practical startup, external-referee acceptance or global-priority claim is made. **TRACE-005 and BGS-BGS-001 remain OPEN.** Original preparation receipts and accepted-source provenance retain their execution identities; destination checks are recorded separately.

## Reviewed extension of the conditional loop owner, 6 October 2026

**BGS-LOOP-001 — EXACT + EXTERNAL-THEOREM; conditional.** The
[single-anchor/dense-test reduction and logarithmic deletion](../supplement/fixed_map/resolvent-flow/loop_test_reductions.md)
extend the existing owner, without a new claim ID. Every fixed anchor order
and pointwise countably dense mixed tests imply the whole-space compact-uniform
hypothesis. FM-007 supplies only the actual short-leg excision input, yielding
O(N^(-1/40) log N) relative error on fixed compact positive height intervals
with the original denominator. The unnormalized tensor partial trace gives an
exact long-long signed target. Actual anchors, that target, and the full mixed
hierarchy remain unproved; TRACE-005 and BGS-BGS-001 remain OPEN. The named
external characterization is inherited, not reproved. See the
[scoped review](../archive/record/loop_test_reductions_review_20261006.md).

## Status vocabulary

- **EXACT** — current project derivation with explicit hypotheses.
- **EXACT + EXTERNAL-THEOREM** — exact reduction with a verified named theorem as input.
- **FINITE-CERTIFICATE** — exact statement at explicit finite parameters.
- **FINITE-REGRESSION** — implementation/reference agreement; not a growing-parameter proof.
- **NUMERICAL** — descriptive floating-point evidence only.
- **DRAFT** — route with named unresolved obligations.
- **OPEN** — closure condition not achieved.
- **RETRACTED** — false or superseded.

## Critical row-support correction

The dehomogenized projective-row integers `G'_(K,r)^(3)` and
`D'_(K,r)^(3)` are safe **one-way** obstructions only:

```text
I>=3 ==> p|D' ==> p|G'.
```

Their converses are not active because specialization may drop leading degree
at the projective point `mu=infinity`.

The active exact split support is the fixed-degree maximal-real construction
`Lambda_(K,r)^(3)`.  Two specialization-safe scalar reformulations are also
active:

```text
Omega_(K,r)^(3)  from the first three coefficients of the row shift resultant,
Theta_K          from two coefficients of the inverse-ratio pair-sum polynomial.
```

`Lambda`, `Omega`, `Xi` and `Theta` are asserted to have the same relevant
**split rational-prime support** only in the scopes proved below. Equality of
full integers or valuations is not silently assumed.

## Active claim table

| Claim | Status | Current support |
|---|---|---|
| all-order moment-channel proximity with a rigid clock spectrum (TRACE-014) | **EXACT + EXACT FINITE CONTROLS** | [Canonical proof](../mathematics/spectral-obstructions/isospectral_clock_moment_control.md); every N>=3 and k>=1, error≤1/N, exact two-copy error1/(N²−1); no frozen-map or diamond-norm claim |
| actual kicked Pell propagator at $\epsilon=\tau/\sqrt{2K}$: all fixed return traces converge in $L^2$ over harmonic windows to the cycle-pair diagram series | **EXACT** | `mathematics/pell_harmonic_returns.md`, Theorem 1; fixed $m,\tau$, full odd space, global law |
| return-law endpoints are wrapped normal and free unitary Brownian; second-return closed formula for $\beta\ge1/6$ | **EXACT + EXTERNAL-THEOREM** | same note (R4)--(R5); moments derived internally, conventional free Brownian identification uses Demni (1) |
| full nonzero lifted-aggregate Bessel weight is $O_{m,\tau}(K^{-1})$ | **EXACT** | same note Lemma 2, cyclic integer image and $\ell^1$ dominance; no growing-$m$ phase theorem |
| finite return-diagram, cyclic-lattice, circle-clique and independent matrix controls | **FINITE-CERTIFICATE + FINITE-REGRESSION** | `evidence/certificates/pell_harmonic_returns_20260910/`; exact checks separated from floating approximation |
| fixed Pell cat map, unit harmonics up to $L=N^{\beta+o(1)}\le\sqrt N$: all fixed compressed-observable moments converge in $L^2$ to circle-graphon moments, uniformly over odd eigenspaces | **EXACT** | `mathematics/pell_harmonic_transition.md`, Theorem 1; sampled harmonics, global observable law only |
| harmonic law has fourth moment $3-2\beta$, explicit sixth moment, weak continuity, and unbounded support for $\beta<1/2$ with semicircle endpoint | **EXACT** | same note, (H6), (H18)--(H19), Corollary 4; no finite-size edge rigidity |
| harmonic weighted ordered quantum moments have graphon limits; complementary normalized half-window commutator squared norm tends to $8\beta(1-\beta)$ | **EXACT** | same note, (H20)--(H21); tracial convergence, no measurement path or BGS claim |
| physical harmonic $a$ produces magnetic parameter $a^2q_0$; 192324 finite oriented word checks and 36 numerical independent spectral comparisons | **FINITE-CERTIFICATE + FINITE-REGRESSION** | `evidence/certificates/pell_harmonic_transition_20260909/`; exact algebra and floating matrix results separated |
| scalar Cayley trace `d_Kol<=C((K-1)^(-1/2)+sqrt((K-1)/log p))`; dyadic rate `O(Q^(-1/2)+sqrt(log Q/log X))` outside fraction `O((log X)X^(-1/4))` for large `Q<=X^(1/4)` | **EXACT + EXTERNAL-THEOREM** | `mathematics/cayley_trace_gaussian_limit.md`, Section 7; Esseen smoothing; constants unoptimized |
| all-order weighted Cayley collision budget `sum_p Delta_w(p) log p = O_w(K^r)` for prime `K`, split primes `p`, and a fixed positive integer word of length `r>=1` | **EXACT + EXTERNAL-THEOREM** | `mathematics/cayley_trace_gaussian_limit.md`, Proposition 3; Chowla input |
| normalized full Cayley--Jacobi trace: joint independent Gaussian limit at fixed distinct positive parameter multipliers for `K->infinity`, `K=o(log p)` | **EXACT + EXTERNAL-THEOREM** | same note, Theorem 1; not traces of matrix powers |
| same joint empirical laws converge weakly in probability over dyadic split designs with `Q->infinity`, `log Q=o(log X)` | **EXACT + EXTERNAL-THEOREM** | same note, Theorem 2; Bombieri--Vinogradov/PNT; does not cover fixed `Q=X^theta` |
| `(K,p)=(11,199)` has `Z4=B4=270` but `Z3=6`, `Z6-B6=1350` | **FINITE-CERTIFICATE** | exact integer convolution in `computations/verification/cayley_higher_moments.py` |
| pair-key bijection; diagonal multiplicity `p-2`; exact constrained count `(K-1)(K-2)` | **EXACT + FINITE-CERTIFICATE** | `mathematics/fourth_moment_reduction.md`; Python/C++/Lean |
| exact `card(V4)=(K^2+1)p^2-(6K^2+3K)p+13K^2-3K` | **EXACT + FINITE-CERTIFICATE** | fourth-moment note + independent checks |
| corrected `B(t)=O(t)+2(p-2)C_H(t)+(p-2)^2 1_{t=0}` and Fourier mean/variance | **EXACT + FINITE-REGRESSION** | `fourth_moment_reduction.md` |
| Cayley identity and additive-energy reduction for `A=c(H\{1})` | **EXACT** | `cayley_additive_energy.md` |
| prime-order characteristic-zero additive collision rigidity | **EXACT** | Chowla cotangent independence + cross-polytope argument |
| `Res(Phi_K,P)=K^3 M^2`; Fibonacci slice; `(K,p)=(131,F_131)` excess `32` | **EXACT + FINITE-CERTIFICATE** | resultant/Fibonacci notes + Lucas/Python/C++ certificates |
| for `100<K<p^(3/4)/3`, `E_+(A)<34K^(8/3)` | **EXACT + EXTERNAL-THEOREM** | `cayley_direct_energy.md`; Vyugin--Makarychev |
| centered Fourier identity and shifted-energy orbit reductions | **EXACT / EXTERNAL-THEOREM** | centered/shifted Cayley notes; Shkredov input where stated |
| summing shifted-energy orbits alone gives only `O(K^3)` | **EXACT** | exact global identity |
| one unordered pair per fixed-product row/nonzero parameter and exact cross-row excess identity | **EXACT + FINITE-REGRESSION** | `cayley_product_row_intersections.md` |
| `Delta_K(p)<=4 I_K(p)(K-1)(K-2)` | **EXACT** | fixed-product-row identity |
| affine trace equation with `alpha_r=U_(r-1)(tau/2)`, `beta_r=-2U_(r-2)(tau/2)` | **EXACT** | `cayley_product_row_real_trace_ideal.md` |
| dehomogenized `G'` and `D'` order-three invariants | **EXACT, one-way only** | subresultant/coefficient-ideal notes; degree-drop correction |
| fixed-degree real-trace cofactors have gcd degree exactly equal to row-intersection count | **EXACT** | real-trace note |
| split `p divides Lambda_(K,r)^(3)` iff some row pair in ratio class `[r]` has `I>=3` | **EXACT + EXTERNAL-THEOREM + FINITE-REGRESSION** | fixed-degree subresultants + Brown--Traub + Smith gate |
| outside product support `Lambda'_K^(3)`: `I_K<=2`, `Delta<=8(K-1)(K-2)`, `E_+(A)<=11(K-1)(K-2)` | **EXACT + EXTERNAL-THEOREM** | exact support + row-energy identity |
| inverse ratio reflection `Q(T)=-P(2tau-T)` and `I_-1(q)=2 deg gcd(E,O mod q)` | **EXACT + FINITE-REGRESSION** | `cayley_product_row_reflection.md` |
| inverse exact support integer `Xi_K` from the half-degree reflection problem | **EXACT + FINITE-REGRESSION** | reflection note/verifier |
| every characteristic-zero affine intercept fibre has size at most `2`; all double fibres classified | **EXACT + EXTERNAL-THEOREM + FINITE-REGRESSION** | `cayley_trace_intercept_rigidity.md`; Bass 1966; C++20 regression |
| valid finite row intersections are explicit cyclotomic-unit congruences `W_r(b)=V_r(a) mod q` | **EXACT** | trace-intercept note |
| general row shift-resultant zero order equals row-intersection count | **EXACT + FINITE-REGRESSION** | scalar shift-resultant theorem |
| three-generator `Omega_(K,r)^(3)` has the same split order-three support as `Lambda_(K,r)^(3)` | **EXACT + FINITE-REGRESSION** | shift-resultant/Smith anchors |
| for each fixed ratio, split order-three primes satisfy `sum log p=O(K^3)` | **EXACT** | norm bound for nonzero shift-resultant constant |
| inverse shift resultant factors `R_-(Z)=2^m F(Z/2) S(Z)^2` with `S(Z)=prod_{i<j}(Z-x_i-x_j)` | **EXACT + FINITE-REGRESSION** | `cayley_inverse_pair_sum_factorization.md` |
| inverse `I_-1(q)=2 ord_0 S`; hence `I_-1>=3 iff S(0)=S'(0)=0 mod q` | **EXACT + FINITE-REGRESSION** | pair-sum factorization note/verifier |
| inverse two-scalar contraction `Theta_K=(S(0),S'(0)) cap Z` has the same split order-three support as `Xi_K` / inverse `Lambda` | **EXACT + FINITE-REGRESSION** | pair-sum note + Smith anchors |
| writing `F(X)=E(X^2)+X O(X^2)`, one has `S(0)=+-Res(E,O)` | **EXACT** | pair-sum/reflection resultant identity |
| for `F_Z(X)=F(X+Z/2)=E_Z(X^2)+X O_Z(X^2)`, `S(Z)=+-Res(E_Z,O_Z)` | **EXACT + FINITE-REGRESSION** | translated half-degree resultant theorem |
| inverse order-three support is equivalently simultaneous vanishing of `Res(E,O)` and its translation derivative | **EXACT + FINITE-REGRESSION** | translated resultant theorem + exact anchors |
| polynomial largest-split-divisor bound such as `P_split^+(Lambda'_K^(3))<=K^(4+o(1))` | **OPEN** | sufficient pointwise arithmetic closure target |
| weighted split-prime excess budget is explicit `O(K^4)` | **EXACT + FINITE-REGRESSION** | `cayley_resultant_mass_budget.md` |
| canonical difference discriminant classification and ratio-orbit fourth-power structure | **EXACT + FINITE-REGRESSION** | difference-discriminant / ratio-orbit notes |
| characteristic-zero multiplicative Cayley rigidity and product discriminant classification | **EXACT + FINITE-REGRESSION** | multiplicative notes/verifiers |
| minimal-extension Frobenius amplification: `f=ord_K(p)` divides `Delta_K^ext(p)` and every non-forced orbit has size exactly `f` | **EXACT + FINITE-REGRESSION** | `cayley_frobenius_amplification.md` |
| all-prime minimal-extension weighted budget and discriminant classification | **EXACT + FINITE-REGRESSION** | one-prime-ideal resultant argument |
| unrestricted prime pairs have density-one exact minimal-extension baseline for fixed `theta<1/3` | **EXACT + EXTERNAL-THEOREM** | Frobenius amplification + PNT + Brun--Titchmarsh + divisor bound |
| full ordinary Cayley/Jacobi trace identity and exact second/fourth trace moments | **EXACT + FINITE-REGRESSION** | `cayley_jacobi_trace_average.md` |
| split double-average `Delta/K^2 <<_theta X^(3theta-1)` for `theta<1/3`; full trace kurtosis tends to `3` | **EXACT + EXTERNAL-THEOREM** | mass budget + Bombieri--Vinogradov + PNT |
| density-one exact split baseline for fixed `theta<1/5` | **EXACT + EXTERNAL-THEOREM** | `cayley_exact_baseline_density.md` |
| corrected off/off spike and `Var O << pE_+(A)+K^2p+K^4sqrt(p)+K^4` | **EXACT + EXTERNAL-THEOREM + FINITE-REGRESSION** | `offoff_elliptic_spike_theorem.md` |
| partition-Mobius formula for distinct-index spectral sums | **EXACT** | `trace_to_local_statistics_bridge.md` |
| exact Poisson/Fourier trace-to-microscopic-statistics identity | **EXACT** | trace-to-local note |
| weighted Heisenberg-scale joint-trace comparison is sufficient for band-limited microscopic RMT correlations | **EXACT** | deterministic comparison theorem |
| all-bandwidth comparison extends to every Schwartz correlation test under positive normalized spectral averages and a reference Schwartz limit | **EXACT** | `bandlimited_correlation_extension.md`; corrected 2026-09-08; no separate tail hypothesis |
| sharp centered pointwise Cayley target for every intended split design | **OPEN** | closed outside exact order-three support only |
| Heisenberg-scale trace estimates for required desymmetrized spectral blocks | **OPEN** | deterministic bridge closed; arithmetic/spectral estimate not proved |
| microscopic BGS/GOE/COE local eigenphase law | **OPEN** | no current theorem |

## Current split arithmetic obstruction architecture

The fourth-moment bottleneck is the pointwise Cayley energy.  Fixed-product rows
reduce all non-forced excess to row intersections.  The exact split event
`I>=3` now has several compatible specialization-safe descriptions:

```text
fixed-degree real-trace subresultants             -> Lambda,
general scalar shift coefficients c_0,c_1,c_2   -> Omega,
explicit cyclotomic-unit matching W_r/V_r,
inverse reflection gcd(E,O)                      -> Xi,
inverse pair-sum coefficients S(0),S'(0)         -> Theta.
```

For a general ratio,

```text
R_(K,r)(Z)=Res_T(P_1(T),R_r(alpha_r T+beta_r+Z)),
ord_0 R_(K,r)=I_(1,r).
```

For `r=-1`, writing `F(X)=P(tau+X)` gives the stronger exact factorization

```text
R_-(Z)=2^m F(Z/2) S(Z)^2,
S(Z)=prod_(i<j)(Z-x_i-x_j).
```

For split primes `2^mF(0)` is a unit, hence

```text
I_-1=2 ord_0 S,
I_-1>=3 iff S(0)=S'(0)=0.
```

Moreover, with

```text
F_Z(X)=F(X+Z/2)=E_Z(X^2)+X O_Z(X^2),
```

one has

```text
S(Z)=+-Res(E_Z,O_Z).
```

Thus inverse order-three support is the common-divisor problem for a
half-degree resultant and its translation derivative.  Computationally this
reduces the required determinant dimension to `O(K)` and eliminates the
full degree-`m^2` shift resultant.

The next arithmetic closure target is not another individual height bound. It
is a uniform theorem controlling the **common split prime divisors** of these
small scalar systems strongly enough to imply, for example,

```text
P_split^+(Lambda'_K^(3))<=K^(4+o(1)).
```

The existing per-ratio logarithmic mass `O(K^3)` and global `O(K^4)` mass are
not polynomial largest-prime bounds.

## Minimal-extension / Frobenius extension

For every rational prime `p!=2,K`, put

```text
f=ord_K(p), q=p^f, H=mu_K(F_q), A_(K,p)=c(H\{1}).
```

Every non-forced collision Frobenius orbit has size exactly `f`, hence
`f|Delta_K^ext(p)`.  The normalized resultant and canonical discriminant
arguments extend to all such primes.  This yields density-one exact baseline
for unrestricted prime pairs with `K~X^theta`, `p~X` and fixed `theta<1/3`.
It does not improve the split slice, where `f=1`.

## Heisenberg-scale spectral closure

For an `N x N` unitary matrix, partition-lattice Mobius inversion and Poisson
summation give exact formulas expressing microscopic factorial correlations in
terms of joint traces.  In particular,

```text
C_(2,N)(U;phi)
 =N^(-2) sum_m phihat(m/N)(|Tr U^m|^2-N).
```

Compact Fourier support probes `|m|=Theta(N)`.  The Fourier conversion is exact;
the open spectral problem is a weighted Heisenberg-scale joint-trace comparison
for the **correct desymmetrized block** at every compact Fourier support.
For positive normalized averages with a reference Schwartz limit, extension to
arbitrary Schwartz correlation tests follows from the translated-cube bound
in `bandlimited_correlation_extension.md` (correction, 2026-09-08).

## Adversarial finite controls

- `(K,p)=(29,728017)` and `(31,1042903)` have `p>K^4` but positive excess: bare `p>K^4 => exact baseline` is false.
- `(K,p)=(41,2908049)` has a row pair with two common parameters: `I_K<=1` is false.
- `(K,p)=(31,1303)` has inverse-row intersection size `4`.
- real-trace anchors include `Lambda'_(13,12)=5^2`, `Lambda'_(17,10)=103`, `Lambda'_(23,18)=47^3*139`.
- inverse reflection anchors include `Xi'_13=5`, `Xi'_19=37`, `Xi'_23=47*137`.
- two-scalar inverse anchors are

```text
Theta'_7=1,
Theta'_11=1,
Theta'_13=5,
Theta'_17=1,
Theta'_19=37,
Theta'_23=47^2*137.
```

These agree with `Xi` on split rational-prime support but not necessarily on
valuations.
- independent C++20 characteristic-zero intercept regression reaches prime
  `K=809` in the recorded extended run with maximum fibre size `2` throughout.
- minimal-extension controls remain
  `(K,p,f,Delta)=(7,13,2,32),(11,43,2,128),(13,3,3,432),(13,5,4,496)`.

Finite computation proves only the displayed finite statements.

## Evidence boundaries

- finite regression is not a growing-parameter proof;
- equal split support does not imply equality of `Lambda`, `Omega`, `Xi`, or `Theta` as integers;
- the inverse perfect-square factorization does not by itself bound the largest supported split prime;
- Dvornicich--Zannier remains an unmatched literature lead until its exact congruence hypotheses are verified for the one-prime-ideal setting;
- fourth moments/kurtosis are not a CLT or local eigenvalue law;
- the ordinary full Jacobi trace is not a parity/desymmetrized spectral block;
- the exact trace-to-local-statistics identity does not prove the required Heisenberg-scale trace estimates.

## Retractions and superseded routes

See [`retractions.md`](retractions.md). Historical all-orders Catalan/arcsine
promotion, ESY-to-BGS shortcut, noncommutative trace shortcut, unsupported
higher-rank extrapolations, the former spike-free off/off theorem, the residual
`O(K^3 log K)` height heuristic, and the two-sided geometric interpretation of
dehomogenized `D/G` row ideals are not active.

Microscopic BGS/GOE/COE universality remains open.

## Magnetic-quotient claims (2026-09-05)

| Claim | Status | Boundary |
|---|---|---|
| Explicit antiunitary and Gauss real gauge | Exact project proof, finite numerical cross-checks | Does not establish GOE universality |
| Signed orbit assembly and all-order Weyl trace identity | Exact project proof; independent Python/C++ histograms | Reference enumeration remains exponential in moment order |
| Reciprocal short-relation rigidity | Proved for prime K, m<K, p^2>m^(K-1) | No polynomial-regime extension asserted |
| Quantitative moment bound and global semicircle law | Complete project derivation, not externally refereed; prime K=o(log p) | Not microscopic BGS; priority not established |
| Fixed-map scope obstruction | Exact growth argument | This regime cannot occur for orders of one fixed hyperbolic integral map |
| Lean magnetic trace checks | Four finite native_decide certificates; compiler execution recorded separately by CI | Not an analytic formalization |
| Triple-resultant filters of draft PR #13 | Necessary divisibility survives; exactness of every triple gcd is false | K=43,p=173 gives 865=5p |

Proof authority for these additions is `mathematics/magnetic_quotient_semicircle.md`.
The earlier ledger remains in force outside these explicitly delimited additions.

## Pell Floquet continuation, 2026-09-05

Proof authority: `mathematics/pell_floquet_normal_form.md`. The argument is
self-contained and does not assume completion of the earlier arithmetic
programme. Status: project theorem with proof, awaiting independent review;
no priority or complete analytic Lean formalization is claimed.

- Exact cyclic cohomological inverse and weighted phase bound
  sum |c_j| a_j <= 2 pi/[K(1-lambda^(-K))].
- Exact four-letter pair-support dissociation for odd prime K>=11 and
  composite Pell N; exact full-HS commutator formula, bounded by 9/K.
- Actual kicked-propagator normal form with odd normalized HS error
  <=12 epsilon^2/sqrt(K), valid for all real epsilon.
- Critical wrapped Gaussian law for U_epsilon^K at epsilon=tau/sqrt(2K).
  The comparison error is 6|m|tau^2/sqrt(K); the additional Gaussian
  characteristic-function error is only asserted to be o(1).
- Subcritical folded-phase W2 limit under epsilon sqrt(K)->0; no statement
  that the old clusters remain separate or keep identifiable ranks.
- Independent C++/Python finite checks and finite/general-algebraic Lean
  kernels are recorded at their own scope, not promoted to the full limit.
- Gamma decimal corrected to 5.614220692151198071627965... and now enclosed
  by a pure-integer interval certificate. Three legacy K=7,p=29 anchors
  corrected with negative controls and explicit positive embeddings.

Not established: Heisenberg-scale joint traces, microscopic local statistics,
fixed nonzero classical-kick universality, or full BGS. K is logarithmic in N
and the critical classical kick is of order 1/(N sqrt(K)).

## Compact-test microscopic obstruction in the Pell family

Section 7 of `mathematics/pell_floquet_normal_form.md` proves a negative
microscopic consequence under global mean-density unfolding of the complete
odd space. For every fixed L and finite nonzero tau=lim epsilon sqrt(2K),
liminf C_d(phi_L)>=Theta(tau)-1/L and liminf Var N_L>=L^2(Theta(tau)-1),
where Theta(tau)=sum_m exp(-m^2 tau^2)>1. Subcritical tau->0 gives divergence
of every such fixed-L pair statistic. Therefore a bounded clustering pair
limit requires |epsilon|sqrt(K)->infinity. Compact tests avoid any hidden
Schwartz-tail assumption. No sufficient condition for positive universality,
no density-adapted unfolding result, and no further-sector result is claimed.
The forty finite configurations are checked independently by pair sums and
moving-window integration; they are evidence about implementation, not the
proof. Priority and analytic Lean formalization are not established.

## Temporal hierarchy and spectral modules (2026-09-06)

Proof authority: `manuscript/unified_sections/temporal_resonance.tex`,
`manuscript/unified_sections/spectral_modules.tex`, and `cayley_scaling.tex`.
These are complete project derivations with the displayed hypotheses, not
independent referee acceptance, established priority, or full Lean proofs.
They supersede the old finite-band nondegeneracy open status only.

| Claim | Status | Boundary |
|---|---|---|
| All finite-lag h_r={g,C^r g}/(4 pi) independent modulo L2 coboundaries for every real nonconstant Fourier polynomial | EXACT + FINITE-REGRESSION | Both trace signs, arbitrary finite phases/support |
| Full quadratic temporal cancellation iff all lag-diagonal sums vanish; explicit transfer | EXACT + FINITE-REGRESSION | Finite combinations |
| Reciprocal-filter cancellation and autocorrelation classification | EXACT + FINITE-REGRESSION | Second-order classes, not quantum spectra |
| Positive fixed-band coercivity and Gevrey stretched-exponential upper bound | EXACT | Not arbitrary infinite analytic support |
| All h_r free over C[z,z^-1]; all-frequency spectral positivity; Riesz bounds uniform in time window | EXACT + FINITE-REGRESSION | Constants depend on the largest lag and fixed symbol |
| Every finite Fourier symbol has an exact high-lag pair-orbit Gram formula and Toeplitz comparison | EXACT + FINITE-REGRESSION | Sufficiently large fixed starting lag; classical covariance |
| High-lag smallest eigenvalue Theta(n^(-2M)) classified by common orbit-filter divisor on hyperbolic circles | EXACT + FINITE-REGRESSION | General Toeplitz zero-order mechanism is prior theory |
| One-harmonic repair of the q-filter family has uniform crossover (n^(-2q)+epsilon^2)^2 | EXACT | Fixed A,q,v and sufficiently large starting lag; not kicked BGS |
| Complementary separate filters remove common soft zeros | EXACT + FINITE-REGRESSION | Sum of separate covariance matrices, not covariance of their sum |
| No-alias physical-Weyl HS variance lower bound | EXACT + NUMERICAL | Sufficient window logarithmic |
| Regular semisimple finite quantum cyclic module with exact all-time variance | EXACT + FINITE-REGRESSION + NUMERICAL | Odd order with arbitrary nonzero c; observable commutators, not eigenphase correlations |
| Balanced phase extends exact orthogonality/all-time formula to even order | EXACT + FINITE-REGRESSION + NUMERICAL | c=a+ib, a^2=b^2>0; correct modular-centred Weyl convention |
| Even-order phase-rank transition: K(K-2)/2 for ab!=0, K(K-2)/8 for nonzero pure real/imaginary c | EXACT + FINITE-REGRESSION | Finite commutator-observable module, not spectral universality |
| Cayley scaling classes are inversion pairs; unimodular toric classes have at most four members | EXACT + FINITE-REGRESSION | No energy-exponent improvement |

Python and independent C++ witness sources are now supplied, and the previously
dangling Fourier-tail reference points to a maintained proof. The Lean draft
is outside active imports until compiler execution is verified. Exact integer
checks, floating-point diagnostics, analytic proofs, and remote CI are separate
evidence categories. The all-time finite-field statement does not furnish
joint traces of a perturbed quantum propagator. Positive microscopic BGS /
GOE / COE / GUE universality remains OPEN.


## Holomorphic shell rigidity and spectral resolution

The intervening Wiener, control, and polynomial-shell results and their
corrections are recorded in `continuation_review_20260906.md`. The following
entries extend the polynomial-shell branch, not the BGS universality claim.
Proofs are included in the single canonical manuscript.

| Claim | Status | Boundary |
|---|---|---|
| Rank-r holomorphic kernels have positive product-curve contacts of total multiplicity at most r-1 | EXACT + FINITE-REGRESSION | Centred bidisk, finite separated rank, positive product constants |
| Two holomorphic maps to C^d are identified up to one unitary by 2d total shell/normal-jet conditions | EXACT + FINITE-REGRESSION | Whole interior spheres, centre included; no rationality or degree assumption |
| 2d-1 prescribed conditions do not suffice, including mixed repeated-shell allocations | EXACT + FINITE-REGRESSION | Sharp in one complex dimension; nonpolynomial entire examples included |
| Scalar two-circle uniqueness | PRIOR THEOREM | Perez, arXiv:2009.02061v2, Theorem 2.2; not claimed as new |
| Punctured-domain scalar functions agree in intensity on infinitely many shells without a constant phase | EXACT + NUMERICAL | Analytic theta construction; numerical checks are diagnostics only |
| Bounded disk-holomorphic pairs have no degree-uniform Holder intensity-recovery estimate from two circles | EXACT + FINITE-REGRESSION | Explicit polynomial sequence; norms bounded above and below; no measurement lower bound assumed |
| Any uniform modulus is at least c exp(-C sqrt(log(1/delta))) | EXACT | Lower bound only; a matching upper rate is OPEN |
| Simple clock spectra agree on all traces below N/2 but have different microscopic spacing laws | EXACT + FINITE-REGRESSION | Abstract unitary negative control, not chaotic dynamics |
| Spectral rounding preserves O(1/N) Egorov while producing collapsed spacings, including a simple-spectrum variant | EXACT | Weak quantization axioms only; no fixed microlocal symbol-class assertion |
| Unbiased rounding preserves simultaneous unnormalized low traces for each specified K_N=o(N^(1/3)), simple spectrum, O(N^-1) norm distance and coarse P/Q/Egorov control, while a fixed stable-band pair test has liminf>1/2 | EXACT; independently internally reviewed | [Canonical refinement](../mathematics/spectral-obstructions/microscopic_rounding_control.md); extends prior project spectral rounding. Changed operator; no exact-quantization, subprincipal-data or all-order microlocal preservation, and no counterexample to actual BGS |

Fresh execution coverage, exact source hashes, literature attribution and the
limited PDF build scope are in `holomorphic_shell_review.md` and
`../evidence/certificates/holomorphic_shell_review.json`. These entries do not
assert external priority, full-repository referee acceptance, Lean compilation,
or successful cloud CI. Positive microscopic BGS universality remains OPEN.


## Bosonic Husimi-shell application

Proof authority: `manuscript/unified_sections/husimi_shell_tomography.tex`,
using the finite-rank holomorphic contact theorem above. The Hilbert space is
not truncated. Each sphere carries ideal complete angular data.

| Claim | Status | Boundary |
|---|---|---|
| Ranks a and b are distinguished by a+b total complete shell/normal-jet conditions in any finite number of bosonic modes | EXACT | No photon cutoff; ideal continuum data, not finite-copy sample complexity |
| Any 2r circles give rank-r completeness; normalized Laguerre mixtures show 2r-1 can fail at trace distance one | EXACT + FINITE-REGRESSION | Sharp universal guarantee over radius choices; not failure at every prescribed design |
| Rank-r strict completeness does not follow: ranks r and r+1 can agree on 2r circles | EXACT + FINITE-REGRESSION | Unknown competitor rank is a different tomography problem |
| No finite set of coherent-state projectors identifies every pure state without a cutoff | EXACT + FINITE-REGRESSION | Infinite-dimensional orthogonal-complement construction |
| Without an energy bound, bounded-region Husimi data have no uniform trace-distance inverse modulus | EXACT | Orthogonal number-state sequence |
| Fixed mean energy restores uniform continuity on rank-bounded states, but not a Holder modulus even with a measured intensity floor | EXACT + FINITE-REGRESSION | Explicit pure-state pairs; modulus at least c sqrt(loglog(1/delta)/log(1/delta)); no matching upper rate |

The pure scalar two-circle case and the definitions of rank-r versus strict
completeness are prior work, explicitly cited. This application is not a BGS
result. Execution, source hashes, and the combined-excerpt build scope are
recorded in `husimi_shell_review.md` and its evidence certificate.


## Aperture-dependent statistical tomography (2026-09-06)

Proofs: `manuscript/unified_sections/coherent_aperture_minimax.tex` and
`heterodyne_aperture_minimax.tex`. Status: EXACT project derivations, with
FINITE-REGRESSION for scalar identities and NUMERICAL high-precision
reconstruction tests; not independently refereed or fully Lean formalized.

For fixed s,beta,E,R0>0, states obey Tr(rho N_total^beta)<=E, without a
rank or hard Fock cutoff. Define K_R(T)=T/(1+log_+(T/R^2)). Uniformly over
R>=R0, including infinity and R varying with the budget:

- Complete-ball coherent-probability modulus is Theta(K_R(log(1/delta))^(-beta/2)).
- Adaptive fresh-copy binary coherent tests have minimax expected trace
  distance Theta(K_R(log B)^(-beta/2)); a nonadaptive finite design suffices.
- Heterodyne censored outside the ball, with an outside flag and every copy
  counted, has the same minimax order. Infinity is ordinary heterodyne.
- Pure-state vacuum/high-Fock pairs already imply all three lower bounds.
- At beta=1 fixed radius requires exp(Theta(epsilon^-2 log(1/epsilon)))
  copies; unrestricted amplitudes/full heterodyne require exp(Theta(epsilon^-2)).

The estimator cutoff has a proved uniform bias; it is not a state truncation
hypothesis. Constants are not uniform in s,beta,E. The proof does not cover
homodyne, arbitrary squeezed Gaussian or collective measurements. It does
not provide the still-missing upper rate for finitely many fixed shells.
The one-mode numerical implementation has narrower dimensional scope than
the analytic theorem. No established world priority or BGS universality is
claimed. The source-level comparison with published heterodyne bounds is
recorded narrowly in `literature/coherent_minimax_context.md`.


## Arithmetic returns: smooth symbols and periodic points (2026-09-11)

Working-proof base: 9ed93cd1bc5e3362c1dbf520f0f391478dfb6969.
The sources below are working mathematical notes; this entry does not
claim their incorporation into the canonical manuscript or PDF.
EXACT retains its project-derivation meaning. Independent review,
priority verification, and Lean formalization of these results are open.

| Claim | Status | Proof and boundary |
|---|---|---|
| Fixed-harmonic return suppression, uniformly in every replica count with r abs(epsilon) below a fixed radius; explicit quartic replica correction | EXACT + FINITE-REGRESSION + NUMERICAL | mathematics/fixed_harmonic_return_gas.md; one arithmetic sequence, fixed harmonic, vanishing classical kick |
| Entire-lattice weighted resonance bound; Gaussian return estimate for analytic position symbols | EXACT + FINITE-REGRESSION | mathematics/analytic_kick_return_gas.md, Sections 1–4; all Fourier modes and 32 classes included |
| First Edgeworth correction is the classical third-cumulant rate, uniformly in replicas at epsilon=t/(r sqrt(K)) | EXACT + FINITE-REGRESSION | Same note, Section 6; O(1/K) error for analytic symbols, bounded t |
| Smooth position symbols with finite order-32 Fourier moment have the same first correction with O(K^(-7/12)) error | EXACT | Same note, Section 7; controlled moving truncation, not the whole large-variance regime |
| General real smooth symbols on T² admit a one-return comparison with an explicit classical periodic-point average, with O(K^(-q)) error for every q at epsilon=t/sqrt(K) | EXACT + FINITE-REGRESSION + NUMERICAL | mathematics/periodic_point_trace_comparison.md; balanced Weyl quantization; accuracy is in K, not N |
| Centered-cell coupling to Haar measure; one-return Gaussian law with the full Green–Kubo variance for finite fourth Fourier moment | EXACT + EXTERNAL-THEOREM + FINITE-REGRESSION | Same note, Section 7; Cohen–Conze Theorem 2.18 checked at source; no imported Gaussian convergence rate |
| Uniform comparison of all integer replicas with error O(K^(-1/2)) for finite fourth Fourier moment | EXACT + LIMITED INTERNAL AUDIT + FINITE-REGRESSION + NUMERICAL | Same note, Sections 8–9; epsilon=t/(r sqrt(K)); normalized Hilbert–Schmidt normal form, not operator-norm normal form |
| Smooth zero variance iff smooth coboundary; first-scale operator return error O(1/N); uniform second-order Gaussian return law | EXACT + LIMITED INTERNAL AUDIT + FINITE-REGRESSION + NUMERICAL | Same note, Section 10; second-scale epsilon=±sqrt(t N/(r sqrt(K))); generated variance may vanish |
| Joint characteristic trace law for any fixed finite family of physical critical return operators | EXACT + NUMERICAL | Same note, Section 11; self-reviewed deduction from normal-form commutator estimates; not Heisenberg-scale joint traces |
| General analytic phase-space kicks: exponential return suppression and absolute Gaussian approximation O(K^(-1/2)), uniformly when r abs(epsilon) is below a fixed radius | EXACT + LIMITED INTERNAL AUDIT + FINITE-REGRESSION + NUMERICAL | mathematics/phase_space_return_gas.md, Sections 1–6; full orbit variance, vector Weyl phases and all 32 classes; vanishing classical strength |
| Joint Gaussian characteristic traces of period-averaged observables under sum abs(f_hat(v)) sqrt(log(2+norm(v))) < infinity | EXACT + LIMITED INTERNAL AUDIT + FINITE-REGRESSION | Same note, Section 7; averaged observables only, including zero variance; full space and even symbols on the odd block |
| The logarithmic exponent one half is sharp as a class guarantee, including after quantum centering | EXACT + LIMITED INTERNAL AUDIT + FINITE-REGRESSION + NUMERICAL | Same note, Sections 8–9; fixed continuous examples for all smaller exponents; centered example has at least 1/25-o(1) escaping mass |
| Replacing the classical period by rK fails at quadratic order; keeping period K and scaling the kick fails at order 1/K | EXACT + FINITE-REGRESSION | Same note, (P15)–(P16); failures of proposed comparisons, not counterexamples to BGS |
| Required Heisenberg-scale joint traces and microscopic BGS universality | OPEN | Neither comparison supplies the missing long-time estimate or a fixed nonzero classical perturbation |

The analytic-symbol verifier exhausts 612,864 ordered cubic atom words,
2,532,760 independently organized unordered multisets, and 5,152,304
multisets classified by exact rational preimages. The finite sets overlap
between methods; these are not counts of distinct systems.
The computation found additional winding aliases and corrected the
initial cubic prediction. The logarithmic coefficient is explicitly
per period length in (A14).

The two-dimensional verifier checks 960 rational-preimage cases and
1,206 integer-word phases, including 603 odd local areas, and compares
an N=35 physical matrix with all 39,200 classical periodic points.
Exact algebra and floating diagnostics are reported separately.
Reproduction commands are in the notes; generated outputs are
build/analytic-kick-return-gas-precheck.json and
build/periodic-point-trace-comparison-precheck.json.
Continuation on the same date closes the formerly missing classical step.
A direct centered-time coupling transfers the checked Haar CLT; no
periodic-point theorem is silently imported. Source version and hashes
are in literature/periodic_return_clt_sources.md.
The updated verifier additionally exhausts 1,122,112 ordered pair
representations, including a K=262 case in the theorem's range; checks
seven exact distance bounds; and separately tests the unitary normal
form, joint products, and second-order loops on physical N=35 matrices.
The limited internal analytic review covers the pair multiplicity,
weighted fourth-moment estimate, and second-order proof. The coupling
and joint-law extension remain self-reviewed, and none of this is
external referee acceptance or a completed Lean proof.
Uniformity in the replica count is at the explicitly scaled amplitude;
it does not give Heisenberg-time control at a fixed classical strength.

The analytic phase-space continuation removes the position-only
restriction on the small-amplitude, all-variance return theorem.
Orbit-representative cohomology removes quadratic finite-component
resonances; a positive Fourier-atom majorant then starts at degree three.
The proof keeps the onsite phase and the nontrivial antipodal phase.
The logarithmic regularity theorem uses an early-return estimate.
Its centered counterexample retains spectral escape after the actual
quantum mean is removed. This is a regularity boundary for period
averages, not a closure of microscopic BGS.

The new verifier passes 320 exact phase identities, 3,000 rational
endpoint inequalities, 120 finite runs, 1,224 finite atomic exclusions,
25 early-return cases, both counterexample arithmetic constructions,
and separately labeled small-matrix diagnostics. Reproduction and
precise internal review scope are in the phase-space note, Section 10.
Growing-parameter proofs are not inferred from finite checks.

## General hyperbolic toral automorphisms (2026-09-12)

| Claim | Status | Proof and boundary |
|---|---|---|
| For every fixed hyperbolic A in SL(2,Z), an explicit odd-dimensional arithmetic subsequence carries the same analytic return suppression and O(K^(-1/2)) Gaussian approximation | EXACT + LIMITED INTERNAL AUDIT + FINITE-REGRESSION + NUMERICAL | mathematics/general_cat_return_laws.md, Theorem 1; constants depend on A,f; all replicas with r abs(epsilon) below the stated fixed radius |
| The return suppression and approximation extend to every fixed finite Gevrey order, with Fourier weight exp(rho norm(v)^alpha), 0<alpha<=1 | EXACT + LIMITED INTERNAL AUDIT + FINITE-REGRESSION | Same note, Section 6; capped Weyl phases give logarithmic particle weights and conditional-field penalties; no uniform alpha-to-zero limit or all-smooth theorem |
| The weighted logarithmic averaged-observable joint CLT holds for every such A, and exponent one half is sharp even after quantum centering | EXACT + LIMITED INTERNAL AUDIT + FINITE-REGRESSION | Same note, Theorems 2–3; counterexample is a fixed continuous symbol for each A; subsequence depends on A |
| Universal quadratic refinement, composite odd moduli, negative traces, and exact arithmetic class count Delta q_A² | EXACT + LIMITED INTERNAL AUDIT + FINITE-REGRESSION + NUMERICAL | Same note, Sections 2–3; excludes N=1; central character at (N,0) is minus the identity in this convention |
| Generic microscopic BGS for fixed nonlinear chaotic systems | OPEN | Generality over linear hyperbolic maps and global return laws does not establish Heisenberg-scale joint spectral correlations |

The generalization changes both the arithmetic subsequence and the
Weyl convention. The invariant refinement v1*v2+v1+v2 modulo two
works for all SL(2,Z); its negative central sign is retained in the
counterexample. The latter uses an odd prime other than five dividing
b5=t^4-3t²+1, followed by prime-square lifting. A fixed positive
fraction of the centered empirical spectrum then escapes.
The arithmetic, phase, estimate-transfer, and prime-lifting arguments
received limited independent internal review. External priority and
formal verification remain open.

The Gevrey extension uses a further analytic estimate: the bounded
Weyl phase gives a logarithmic, rather than linear, charge cost.
A size Ds²L in the tree criterion retains the connected O(Ks⁴)
remainder. The subadditive alpha quasi-norm of the cyclic Green
operator supplies the stretched-exponential lattice estimate.
The general verifier covers 72 matrices, 200 admissible dimension
cases, 800 exact cyclic preimages, 3,200 exact phase identities,
28 prime-lifting cases, eight counterexample cases, and 72 exact
capped-kernel envelope sums. Physical quantization tests at four
small dimensions are explicitly floating diagnostics.

## Publication integration (2026-09-12)

The five fixed-harmonic, position-kick, periodic-point, phase-space, and
general return-law proof modules are now included in the canonical TeX
manuscript. `sync_return_sections.py --check` verifies source synchronization.
This is publication integration, not a new mathematical scope promotion.

The general modulo-two refinement already had a Lean invariance certificate.
Its polarization identity and nontrivial central parity are now also
kernel-checked without axioms. The full 16-module build passed; the general
analytic return and regularity theorems remain unformalized. Eight focused
return-law Python checks passed. The complete historical Python/C++ suite
was not rerun in this revision. See `publication_review_20260912.md`.


## Short-return obstruction (2026-09-12)

| Claim | Status | Exact boundary |
|---|---|---|
| Ergodic intensity-one local-process convergence forces uniformly vanishing normalized sublinear-frequency traces | PROJECT PROOF + SELF-REVIEW | return_trace_obstruction.md, Theorem 1; first-moment uniform integrability, no second-moment hypothesis |
| The same convergence forces spatial L1 self-averaging on every window with a diverging number of mean spacings | PROJECT PROOF + SELF-REVIEW | Same note, bounded-Lipschitz strengthening; no mixing-rate assumption |
| Critical Gevrey/harmonic returns preclude those local limits and standard globally unfolded pair limits | DERIVED FROM PROJECT RETURN THEOREMS + SELF-REVIEW | Existing return-law proofs remain inputs; shrinking quantum kicks, stated spectral sectors, global unfolding |
| Positive microscopic BGS at fixed classical strength | OPEN | The new criterion is necessary only; a density-dependent unfolding can remove the return obstruction |

Finite exact Fourier/marked-convolution checks and separate floating Gaussian
controls are in the companion verifier. No new full analytic Lean formalization
or external referee validation is claimed. Review: return_obstruction_review_20260912.md.


## Return intensity and local unfolding (2026-09-13)

Theorem 3 of mathematics/return_trace_obstruction.md proves conditional-intensity domination by the absolutely continuous return density, with an essential-infimum cap for ergodic local limits and explicit sharp abstract-spectrum constructions. Formula (S22) quantifies possible first-moment loss. Formula (S25) supplies the origin-weighted density transport; (S26) realizes the same return law with different locally unfolded statistics.

Status: PROJECT PROOF + SELF-REVIEW. The free Brownian support-gap consequence (S24), for 0<t<4, additionally uses the existing project harmonic return theorem and the checked Demni--Hmidi source. It does not identify the full cat-map local limit. Finite rational, symbolic, and floating controls have distinct scopes. External priority and full analytic formalization remain unverified. See record/return_local_limits_review_20260913.md.


## Dated acceptance history

Earlier acceptance narratives are preserved with their original scientific scope. Follow current supersession statements above before interpreting an older OPEN label.

## 6 October 2026 — original ordered two-pair microscopic mass

[Historical acceptance record](../archive/history/2026/corpus_revision_20261006/acceptance_history.md#6-october-2026--original-ordered-two-pair-microscopic-mass).

## 6 October 2026 — uniform collective diffusion and refined shared-noise mass

[Historical acceptance record](../archive/history/2026/corpus_revision_20261006/acceptance_history.md#6-october-2026--uniform-collective-diffusion-and-refined-shared-noise-mass).

## 6 October 2026 — actual Weyl coercivity, regularized gap and common-noise invariants

[Historical acceptance record](../archive/history/2026/corpus_revision_20261006/acceptance_history.md#6-october-2026--actual-weyl-coercivity-regularized-gap-and-common-noise-invariants).

## 5 October 2026 — exact Heisenberg pair compensation and actual smoothed form factor

[Historical acceptance record](../archive/history/2026/corpus_revision_20261006/acceptance_history.md#5-october-2026--exact-heisenberg-pair-compensation-and-actual-smoothed-form-factor).

## 5 October 2026 — growing degree and a particular microscopic inverse obstruction

[Historical acceptance record](../archive/history/2026/corpus_revision_20261006/acceptance_history.md#5-october-2026--growing-degree-and-a-particular-microscopic-inverse-obstruction).

## 5 October 2026 — critical-noise compensation and actual fixed-degree projections

[Historical acceptance record](../archive/history/2026/corpus_revision_20261006/acceptance_history.md#5-october-2026--critical-noise-compensation-and-actual-fixed-degree-projections).

## 5 October 2026 — all-order original-chain law and exact remaining transfer

[Historical acceptance record](../archive/history/2026/corpus_revision_20261006/acceptance_history.md#5-october-2026--all-order-original-chain-law-and-exact-remaining-transfer).

## 5 October 2026 — exact noise-removal defect and four transfer boundaries

[Historical acceptance record](../archive/history/2026/corpus_revision_20261006/acceptance_history.md#5-october-2026--exact-noise-removal-defect-and-four-transfer-boundaries).

## 4 October 2026 — actual-start comparison and circular relaxation

[Historical acceptance record](../archive/history/2026/corpus_revision_20261006/acceptance_history.md#4-october-2026--actual-start-comparison-and-circular-relaxation).

## 4 October 2026 — polynomial original-coboundary clock limit

[Historical acceptance record](../archive/history/2026/corpus_revision_20261006/acceptance_history.md#4-october-2026--polynomial-original-coboundary-clock-limit).

## 4 October 2026 — bounded fixed traces and auxiliary-expansion obstruction

[Historical acceptance record](../archive/history/2026/corpus_revision_20261006/acceptance_history.md#4-october-2026--bounded-fixed-traces-and-auxiliary-expansion-obstruction).

## 1 October 2026 — projected-square refinement and block crowding

[Historical acceptance record](../archive/history/2026/corpus_revision_20261006/acceptance_history.md#1-october-2026--projected-square-refinement-and-block-crowding).

## 1 October 2026 — resonant cubic density control and critical tails

[Historical acceptance record](../archive/history/2026/corpus_revision_20261006/acceptance_history.md#1-october-2026--resonant-cubic-density-control-and-critical-tails).

## 30 September 2026 — universal absolute obstruction and signed cubic continuation

[Historical acceptance record](../archive/history/2026/corpus_revision_20261006/acceptance_history.md#30-september-2026--universal-absolute-obstruction-and-signed-cubic-continuation).

## 30 September 2026 — independent prime-resonant summary audit

[Historical acceptance record](../archive/history/2026/corpus_revision_20261006/acceptance_history.md#30-september-2026--independent-prime-resonant-summary-audit).

## 30 September 2026 — audit and completion of the Heisenberg note

[Historical acceptance record](../archive/history/2026/corpus_revision_20261006/acceptance_history.md#30-september-2026--audit-and-completion-of-the-heisenberg-note).

## 30 September 2026 — simultaneous coboundary clock limit

[Historical acceptance record](../archive/history/2026/corpus_revision_20261006/acceptance_history.md#30-september-2026--simultaneous-coboundary-clock-limit).

## 29 September 2026 — continued research: the actual coboundary chain

[Historical acceptance record](../archive/history/2026/corpus_revision_20261006/acceptance_history.md#29-september-2026--continued-research-the-actual-coboundary-chain).

## 29 September 2026 — quadratic-noise dynamics and audited integration

[Historical acceptance record](../archive/history/2026/corpus_revision_20261006/acceptance_history.md#29-september-2026--quadratic-noise-dynamics-and-audited-integration).

## 28 September 2026 — quadratic coboundary noise

[Historical acceptance record](../archive/history/2026/corpus_revision_20261006/acceptance_history.md#28-september-2026--quadratic-coboundary-noise).

## 27 September 2026 — audit of the independent CUE upload

[Historical acceptance record](../archive/history/2026/corpus_revision_20261006/acceptance_history.md#27-september-2026--audit-of-the-independent-cue-upload).

## 25 September 2026 — CUE singular energy and coboundary flow

[Historical acceptance record](../archive/history/2026/corpus_revision_20261006/acceptance_history.md#25-september-2026--cue-singular-energy-and-coboundary-flow).

## 25 September 2026 — smooth full-propagator transfer and a Gram falsifier

[Historical acceptance record](../archive/history/2026/corpus_revision_20261006/acceptance_history.md#25-september-2026--smooth-full-propagator-transfer-and-a-gram-falsifier).

## 25 September 2026 — exact pair-resolvent bridge and universal Abel floor

[Historical acceptance record](../archive/history/2026/corpus_revision_20261006/acceptance_history.md#25-september-2026--exact-pair-resolvent-bridge-and-universal-abel-floor).

## 24 September 2026 — audited two further fixed-map continuations

[Historical acceptance record](../archive/history/2026/corpus_revision_20261006/acceptance_history.md#24-september-2026--audited-two-further-fixed-map-continuations).

## 24 September 2026 — audited 87-page outside-agent submission

[Historical acceptance record](../archive/history/2026/corpus_revision_20261006/acceptance_history.md#24-september-2026--audited-87-page-outside-agent-submission).

## 23 September 2026 — nonlinear classical pressure boundary

[Historical acceptance record](../archive/history/2026/corpus_revision_20261006/acceptance_history.md#23-september-2026--nonlinear-classical-pressure-boundary).

## 23 September 2026 — full-lag frozen-symbol gap and exact kick rank

[Historical acceptance record](../archive/history/2026/corpus_revision_20261006/acceptance_history.md#23-september-2026--full-lag-frozen-symbol-gap-and-exact-kick-rank).

## 22 September 2026 — clustered Abel and time-window inference

[Historical acceptance record](../archive/history/2026/corpus_revision_20261006/acceptance_history.md#22-september-2026--clustered-abel-and-time-window-inference).

## 22 September 2026 — smooth finite-orbit extension

[Historical acceptance record](../archive/history/2026/corpus_revision_20261006/acceptance_history.md#22-september-2026--smooth-finite-orbit-extension).

## 21 September 2026 — recovered fixed-map continuation

[Historical acceptance record](../archive/history/2026/corpus_revision_20261006/acceptance_history.md#21-september-2026--recovered-fixed-map-continuation).

## Fixed-map update, 20 September 2026

[Historical acceptance record](../archive/history/2026/corpus_revision_20261006/acceptance_history.md#fixed-map-update-20-september-2026).

## Recovered amendments, 20 September 2026

[Historical acceptance record](../archive/history/2026/corpus_revision_20261006/acceptance_history.md#recovered-amendments-20-september-2026).

## Fixed-order complete WKB reduction (6 October 2026)

**BGS-TRACE-017: PROJECT ANALYTIC PROOF + INDEPENDENT INTERNAL REVIEW; analytic chain unformalized.** For each fixed k and compact smooth Fourier weight, choose fixed J>=k. The complete partition transform of either named WKB trace table differs from the actual unitary transform by O(N^(k-J-1/2)). [The proof](../mathematics/fixed-map/factorial_wkb_reduction.md) distinguishes Laurent and adjoint tables. Exact finite-power reciprocity, formal connected coefficients and the actual conditioned rotated-box first-loop theorem are supporting, separately scoped results. No growing-order claim is made. The separate [global rotated-box theorem](../mathematics/fixed-map/global_rotated_box_trace.md) now supplies a finite-band contour representation and summed tail, conservatively through m<=2N; signed box evaluation and unrestricted bands remain open. The full signed comparison is equivalent and remains OPEN, as do TRACE-005 and BGS-BGS-001. See [review scope](../archive/record/heisenberg_wkb_review_scope.md).

## Actual higher-seven-primary common commutant (6 October 2026)

**BGS-FM-024: EXACT + FINITE-CERTIFICATE; independent internal review of the original theorem.** For every odd N with 49|N and 5∤N, the actual pair (A_N,M_N) has scalar complex common commutant. [The maintained proof](../mathematics/fixed-map/actual_seven_primary_commutant.md) gives exact reduction, two-row equations, full finite-polynomial certificates and rank lifting. With the checked Lindemann–Weierstrass input, the literal U_N has only scalar algebraic-entry commuters; the added coefficient-separation argument has a scoped internal check, distinct from independent review of the entire expanded exposition. The cases 5|N with 49|N and 7∥N remain outside this theorem; N=7 remains exceptional. Neither spectral simplicity nor BGS/TRACE-005 follows. The analytic/algebraic proof is not fully formalized.

## Seven-primary finite formal certificate (6 October 2026)

**BGS-FORMAL-003: COMPILED LEAN NATIVE-EVALUATION CERTIFICATE + INDEPENDENT SEMANTIC REVIEW.** The unchanged isolated source compiled and proves 22 executable GF(5) array predicates: seven product identities, all-factor Rabin computational conditions on 46 factor occurrences, seven degree exclusions and the finite order-49 predicate. An independent semantic audit and 1,896 fresh compiled controls passed. This does not formalize generic polynomial correctness, Rabin's theorem, the finite-field bridges or FM-024's actual commutant proof. The aggregate import rebuild remains a distinct gate. See [exact scope](../formalization/seven_primary_certificate.md).

The independent FM-024 consolidation audit accepted the expanded proof and the algebraic-entry literal-U corollary at overlay SHA-256 `812c3610ef28290c3e5c6e1b702807ab8b01d93eae1c48e87cfe79efccf9c86e`. The integration map records subsequent locator/spacing changes only. [Consolidation review](../archive/record/actual_commutant_consolidation_review.md). No spectral-simplicity conclusion was added.

Prior ownership clarification for TRACE-017: heisenberg_trace_support.md Section 3 already proves the general nonunitary integer-power and full partition perturbation estimate without a microscopic correlation assumption. TRACE-017 supplies the actual arbitrary-fixed-order WKB construction/instantiation and explicit adjoint-table convention, rather than inventing that perturbation lemma. See record/heisenberg_wkb_prior_attribution.json for source-bound hashes.

Supporting quantization equivalence: [principal WKB polar comparison](../mathematics/fixed-map/polar_wkb_quantization_stability.md) gives a fixed smooth order-1/N unitary correction from the actual operator and an O(N^-2) polar defect. The smooth-symbol/polar bridge has independent internal review; the RMS transfer theorem and its inherited external mixing leaf are credited, not newly independently audited. An assumed all-order compact law transfers between the two unitary endpoints. No such law is evaluated; no nonnormal W0 eigenvalue matching or J=0 replacement of TRACE-017 follows.

Aggregate Lean update: all 19 active modules passed in 22 Lake jobs; SevenPrimary was freshly compiled and Bgs rebuilt. The previously separate aggregate-build gate is closed by evidence/formalization/seven_primary_20261006/aggregate-build.json. This does not extend FORMAL-003 beyond its executable-array predicates.

## Finite-band global rotated-box trace representation (6 October 2026)

**Supporting project analytic theorem, fresh independent internal review; TRACE-017 core unchanged.** For the actual fixed-coupling odd-dimensional operator and every fixed finite J>=1, uniformly through 1<=m<=2N, the actual trace equals the exact rotated-box sum with error O_J(N^(3/2-J))+O_J(sqrt(N) exp(-4N/5)). [The global contour proof](../mathematics/fixed-map/global_rotated_box_trace.md) establishes a saturated-contour deformation and sums its tails; additional strictly bounded bandwidth ranges are stated there. It does not evaluate the exact box sum, make first-loop algebraic errors absolutely summable, cover unrestricted bands, or prove CUE/BGS/TRACE-005. This separately accepted result supersedes earlier contour-pending descriptions only within its stated finite band.

## Current actual pair commutant and scoped spectral extensions

**FM-024:** [actual pair commutant](../mathematics/fixed-map/actual_seven_primary_commutant.md)
is scalar for every odd N>=3 except7 by explicit combination of reviewed
families and prior FM-008. At7 its characteristic-zero dimension is17 with
multiplicities(3,2,2). The literal-U corollary is algebraic-entry-only.
Component proofs, finite certificates and prior review boundaries are retained.

**FM-025:** [uniform pure-five kick simplicity](../mathematics/fixed-map/uniform_five_cluster_simplicity.md)
holds for A_(7*5^e), e>=1, by reviewed v2 analytic induction and separately
reviewed finite inputs. V1 remains incomplete. The [finite companion](../mathematics/fixed-map/finite_seven_spectral_pivots.md)
gives simple literal U only at N=21,35,49,63, using prior FM-008 Section4 and
registered LW. FM-008's universal7∤N statement is unchanged.

**FM-010 companion:** [one-step squared-trace transcendence](../mathematics/fixed-map/uniform_trace_square_transcendence.md)
holds for every odd N>=3 except7 at nonzero real algebraic t; at7 it equals1.
Repeated eigenvalues are allowed. Original all-power nonvanishing and its
inherited review status remain unchanged; higher-power squared-trace
transcendence at7|N is not claimed.

## Current paired-phase and selected full-weight frontier

**TRACE-018:** [actual phase locality](../mathematics/fixed-map/winding_defect_locality.md)
and [Frostman averages](../mathematics/fixed-map/phase_map_frostman.md) remain phase-only,
with the exact [paired quotient](../mathematics/fixed-map/paired_character_identity.md)
as support. Averaging dimension does not replace fixed-N time averaging.

**TRACE-019:** [selected full-weight coefficient](../mathematics/fixed-map/selected_weighted_coefficient.md)
and its once-counted cyclic/negative family are O(N^-1/2) in every fixed
positive global band m/N<=2, for fixed finite J>=0 in the V representation.
Aggregate U pair transfer requires fixed J>=2. Separate W/Q/EQ and interface
reviews retain exact probabilities, half-density, norm-uniform tests and
source hypotheses. The [stationary residual](../mathematics/fixed-map/stationary_cyclic_residual.md)
credits FM-021 and removes two disjoint pair families once, retaining only
unremoved torsion portions. The [exact homoclinic structure](../mathematics/fixed-map/exact_homoclinic_potential.md)
uses inherited Fourier methods; its additive/distributional obstruction gives
no multiplicative-gauge conclusion. Mane1981 with mandatory1983errata supplies
the verified entropy formula; the original Pesin locator remains unverified.

The full signed complement, plateau mechanism, remaining torsion, higher
orders, TRACE-005 and BGS remain open. No new Lean theorem is claimed.
[Prior component-status history](../archive/history/2026/cohesive_frontier_20261006/prior_ledger_tail.md)
preserves the superseded arithmetic checkpoints and their references.

## Current collective hierarchy and literal-time spectral bounds

**TRACE-020:** [general factorial ordered-sector removal](../mathematics/fixed-map/factorial_ordered_diagonal.md)
gives O_k(log^(2k)N/N) for every fixed k>=2 and compact Fourier weight under
entrywise flatness alone, including zero-power strata and exact constant
terms. Mixed permutations need not preserve the ordered range. Its
[mixed/matched long-cycle companion](../mathematics/fixed-map/mixed_ordered_diagonal.md)
uses separate singular mixing and shared Haar draws; neither bounds the
complete signed complement. The separately retained
[centered collective hierarchy](../mathematics/fixed-map/collective_occupation_hierarchy.md)
has O(1) actual-U cyclic trace through fixed m<=bN bands and O_w(N^-1) pair
aggregate, with true Gram inverse and inherited FM-021 analytic inputs.
The [exact Q residual](../mathematics/fixed-map/collective_projector_residual.md) includes
remaining balanced, off-charge and cycle-fixed vectors. Supporting quadratic
and slow-source obstructions retain sector/vector scope and diagnostic limits.

**FM-026:** [literal-time bounds](../mathematics/fixed-map/literal_time_multiplicity_bounds.md)
for N=7*5^e,e>=1 give multiplicity<=7 at nonzero real algebraic time. At least
612N/625+7 eigenvalues are simple for even e>=4, and at least 612N/625+175
for even e>=6; exact special lower bounds are 4333 at N=4375 and 107443 at
N=109375. The odd counts are 24N/25 for e>=3, 24N/25+35 for e>=5,
and 24N/25+875 for e>=7. The 875 includes the deepest 35 exactly once;
finite 35/175 simplicity is a bounded companion. Component/rank reviews and
registered LW remain explicit. Full uniform simplicity/gaps/BGS are open.

**FM-008 review update:** [fresh independent audit](fm008_fresh_independent_review.md)
accepts the unchanged7∤N theorem with two mapped exposition corrections and
a fresh primary LW statement/application check. Historical author review is
retained. Its r1 pair-commutant leaf used by FM-024 is independently reviewed
and LW-free; the literal-U algebraic-entry corollary still uses LW.

TRACE-020's independently reviewed [ordered-diagonal companion](../mathematics/fixed-map/ordered_diagonal_cyclic_trace.md)
uses a distinct projector of rank N^m-1. For each fixed a>0 its cyclic trace
is bounded by12N³exp(-c_aN), uniformly for every m>=aN and sufficiently large
odd N. It uses only inherited FM-021 singular mixing. This is exponential
in N, not m at fixed N, and does not imply the collective bound because
cycle cancellations differ. The complete Q_ord residual remains unestimated.

## Current checksum-free pair residual and reviewed phase checkpoint

**TRACE-021:** [the current claim card](../mathematics/trace-bridge/phase_trace_checkpoint.md)
and [exact checksum-free synthesis](../mathematics/trace-bridge/checksum_free_residual.md)
remove all low-switch occupation-mismatched partial fibers, including checksum
zero. The orthogonal Q_new=I-P_H-P_bal-O_low-L_all has balanced complement
Pi-P_H-P_bal and the literal high-Hamming/high-switch offcharge mask. Full
switch transfer makes the damped endpoint negligible under
kappa a N(1-z_N)-2 log N→+infinity. **The signed undamped T16, complete Q_new
trace, balanced law, plateau, higher factorial comparison and BGS remain OPEN.**
The older checksum-restricted proof remains valid at its original scope;
constant translations are not counted twice. FM-027 core uses scoped actual
phase/parametrix A2--A5 and FM-021, without FM-018/Egorov/classical mixing.

The independently accepted current checkpoint adds **FM-027** uniform actual
one-step nonzero-charge contraction; **TRACE-022** positive Schur-energy and
three-radius equivalence; **TRACE-023** completed compact pair source identity,
universal Abel bound and full complex source regularity/uniform integrability;
**FM-028** actual q=1,theta=0 radial shell/resolvent; **FM-029** literal fixed-word
moment laws with the separately reviewed triple-log window and fixed-polynomial
strong-freeness obstruction; and **FM-030** scalar/block ordinary-body coercivity and real
absorption. Exact restrictions and independent source/review pins are in
[the maintained claim card](../mathematics/trace-bridge/phase_trace_checkpoint.md) and
[checkpoint record](checked_research_checkpoint_20261007.md).

Separately reviewed changed-family growing-period offcharge failure and
infinite unregularized one-channel boundary-delay variance constrain proposed
proof steps. Accepted phase Ward v2 leaves its actual signed overlap estimate
(13) OPEN. Qualified fixed-N centering and changed-family simple-spectrum/rounding companions are integrated below; actual Schatten sketches remain unpromoted. The color-one ordinary bulk-only source
correction is [qualified narrowly](../literature/color_one_boundary_qualification_20261007.md):
FM-018 direct matrix results survive and invariant prescriptions/graph
universality are not declared false. All BGS/CUE identification remains OPEN.


## Reviewed Wave2 subsidiary results, 7 October 2026

- **BGS-TRACE-024:** [actual unmasked q=1 one-pinch disappearance](../mathematics/fixed-map/actual_one_pinch_disappearance.md) combines the independently accepted actual fixed-lag displacement-frame estimate with annealed deletion in ONE theorem. The positive aggregate holds for bounded compact-band weights; signed occupation-subtracted disappearance retains smooth weights. Constants are fixed-lag; there is no aggregate rate or practical startup. The annealed leaf separately extends to one consecutive block, without an actual positive block-hierarchy claim.
- **BGS-FM-031:** [ordinary centering](../mathematics/fixed-map/ordinary_compact_stratum_centering.md) is a.e. on labelled stable strata for odd N>=3, preserving the original measures, gauge determinant and distinct coarea factor. Completed signed-source and fixed-derivative cutoff bounds are fixed-N only. No positive signed-source measure, super-Berezinian or normalized dimension-uniform microscopic tail.
- **BGS-TRACE-025:** [rounded/split endpoint barriers](../mathematics/fixed-map/rounding_simple_spectrum_endpoint_barriers.md) are changed-quantizer constructions. A successful endpoint proof needs a property or estimate excluding these witnesses and an identified use of it. The stronger strategy sentence in raw rounding line 34 is superseded by this restriction; no particular raw-Weyl/all-order proof method is required. Actual Schatten preservation is not proved.
- **BGS-TRACE-026:** [corrected hook/tree/current reduction](../mathematics/fixed-map/hook_tree_phase_current_reduction.md) gives exact all-N,m identities only after exterior-character zero extension before marked-cycle selection. Its controlled-sector Abel theorem is conditional on the stated eventual flatness/P/reverse constants. Balanced identification requires the residual limit -exp(-2s)/(4s^2), not a small residual. Original v1/audit and corrected v2 acceptance remain separately traceable.
- [Phase-orbit literature qualification](../literature/wave2_phase_orbit_source_qualification_20261007.md) records exact bounded applicability/priority limits. No new graph universality or external load-bearing leaf is added; author P1-P3 inferences are not promoted to independently reviewed asymptotic claims.

The [integration mapping](wave2_promotion_mapping.json) and [review record](wave2_checked_integration_20261007.md) retain byte-exact source/review evidence. **Literal signed masked T16, masked insertion/source-extraction/deconvolution hierarchy, actual signed Ward overlap (13), complete balanced microscopic law, TRACE-005, higher factorial comparison and deterministic BGS remain OPEN.** No formalization or external referee certification is asserted.


## BGS-TRACE-027: separately reviewed coherence covariance

[Weighted coherence](../mathematics/fixed-map/weighted_phase_coherence_covariance.md) proves exact finite covariance/error bounds and the nontrivial classical Green–Kubo leading term. Complete signed Ward convergence is only on the upper half ceil(T_N/2)<=m<=T_N of the specified slowly growing window, without all-fixed-m/full-prefix convergence. The actual unconjugated transpose-product bound removes the stated degree-two mixed-moment exception only. Original ZIP controls were inaccessible/unreplayed; exact exported proof and NEW independent controls are sealed. Absorbed Ward (13), microscopic balanced law, literal masked T16, TRACE-005 and BGS remain OPEN.


## Reviewed Wave3 complete unmasked hierarchy

**TRACE-028:** [right-frame and complete insertion theorem](../mathematics/fixed-map/right_frame_unmasked_pinch_hierarchy.md) closes complete unmasked fixed-j separated sums (actual and annealed) and every complete convex insertion mixture, uniformly z_N in [0,1]. The NEW centered S3 tail ||D0||S3³=o(N) controls every j>=3 word uniformly in theta/gaps/j. Arbitrary fixed-B averaging keeps B fixed during coherent time summation. Older statements that the complete unmasked separated hierarchy was unestimated are superseded at precisely these normalizations.

**TRACE-029:** [convex weak-noise/deconvolution theorem](../mathematics/fixed-map/convex_pinch_weak_noise_and_deconvolution.md) adds exact finite-N bounds, complete signed bounded-u stability and an actual UNSIGNED large-log obstruction: F_m=1+o(1) and normalized unweighted deconvolved interval sum ~N^(bA0-1)/(A0 log N). The common identity contribution cancels only after signed occupation subtraction (or relevant projection); this does not refute T16.

**Current OPEN frontier:** masked/source-weighted separated sums, Hamming/high-switch extraction, source derivatives and quantitative rates, signed centered boundary deconvolution and undamped zero-insertion comparison, actual absorbed Ward (13), complete balanced microscopic law, TRACE-005, higher factorial comparison and deterministic BGS. No formalization or unavailable author222-suite certification.

## Independently reconstructed Schur continuation, 11 October 2026

| Claim | Status | Scope and unresolved boundary |
|---|---|---|
| BGS-TRACE-060, strengthened | CONDITIONAL + INDEPENDENT INTERNAL RECONSTRUCTION | [All fixed killed upper moments and joint first-delay concentration](../mathematics/trace-bridge/all_moment_delay_bootstrap.md) at ceil(log(2N)^(1+kappa)); uniform equality laws at every fixed order and the full-depth reference measure after two substantive word repairs. Probability of all-time flatness, growing-order/edge laws, the physical microscopic reference and unrestricted exceptional-event moments remain open. |
| BGS-TRACE-073 | CONDITIONAL + INDEPENDENT INTERNAL RECONSTRUCTION | [Every ordered classical centered singular value contracts](../mathematics/trace-bridge/schur_censoring_gap.md); stopped fresh-phase quantum gap propagation at ceil(log(2N)^(3+kappa)). FM-021/022 supply only the actual-map initial intensity/reversal gaps. The [separate reversal reconstruction](../archive/record/reversal_channel_continuation_20261011.md) also proves singular-spectrum contraction for arbitrary complex contractions. Quantum realization contraction and flatness probability are not inferred from the mean. |

[The review and exact input lineage](../archive/record/cavity_continuation_20261011.md) separate
analytic arguments from finite Python/C++/Wolfram controls. No new analytic
Lean formalization or world-priority claim is made. TRACE-055's complete
hierarchy, TRACE-005 and BGS remain open.

