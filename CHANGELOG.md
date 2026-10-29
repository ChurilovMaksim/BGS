# Scientific changelog

## 2026-10-29 — Strategy note records an unverified reconnaissance

Section 6 of `mathematics/fixed-map/offdiagonal_strategy.md` records an external reconnaissance as a lead list. No constant from that report is adopted. The half-order divisibility in the report is the lemma already proved in BGS-TRACE-121 and corrected by ERR-061; no maintained note on this branch still uses \(t=(p+1)/2\) as a nonempty class. The hypothesis \(2t\ge p+1\) in BGS-TRACE-120 remains a lower bound and, on an odd prime, is exactly the inert full order. The next route named in the note is a symmetry-breaking reformulation of the kicked model. No new claim ID is opened. BGS-TRACE-005 and BGS-BGS-001 remain open.

## 2026-10-29 — Uniform Pell-orbit overlap

Register BGS-TRACE-125. For every odd integer \(n\ge5\), at \(N=u_n\), the fixed symbol overlaps only at lags \(1\) and \(n-1\), both with value \(-7/2000000\). The quadratic trace coefficient of the transported product is exactly \(n\cdot1650797/4000000\). The sequence \(u_n\) is exponential, not an arithmetic progression. The index \(n=5\) is a finite scan; every larger odd index is a size, archimedean, and quadratic-form argument. This is \(f''(0)\), not a bound on \(f(1)\). The claim does not assert that Kurlberg–Rudnick degeneracies fail to be eigenvalues of the kicked propagator: that sentence does not follow from BGS-FM-032. A separation of \(L_N(U_N;1)\) from the CUE value is a bound on the Abel sum, not a lower bound on one normalized trace. Prime squares, including \(315\), are placed by BGS-TRACE-124; \(315\) is short because its radical \(105\) is short. The ledger phrase says that Lean certifies integer comparisons only. Python, C++ and that Lean witness certify the integers. No new kick window is claimed. The third-order remainder, the signed off-diagonal sum, and the limit stay open. BGS-TRACE-005 and BGS-BGS-001 remain open. No new external dependency.

## 2026-10-29 — Half-order errata and the odd-modulus assembly

ERR-061, ERR-062 and ERR-063 correct three statements already registered on this branch. The order \(t=(p+1)/2\) does not occur: a split order divides \((p-1)/2\), and an inert cofactor \((p+1)/t\) is odd. The long class is the inert full order. A split full-order tower and a non-short product of \(3\) with a short prime are empty, so they are not kick windows. The square-free window \(N=15r\) requires an odd prime \(r\ge7\); \(N=45\) is strongly short and is covered by \(8t\le3N\). Theorem 1 of BGS-TRACE-124 is assembled from BGS-TRACE-121 Theorems 1 and 2, BGS-TRACE-122 Theorem 3, BGS-TRACE-123 Theorem 1, and Sections 2--7 for a non-square-free modulus that is not a prime power. The ledger phrase for BGS-TRACE-117 through BGS-TRACE-124 now says that Lean certifies integer comparisons only. The inert-domain check compares \(\gamma<5\), not \(\gamma/q<5\). No claim state changes. BGS-TRACE-005 and BGS-BGS-001 remain open.

## 2026-10-29 — Every odd modulus lies above 3/4 or below 5/7

Register BGS-TRACE-124. Every odd modulus \(N\ge3\) satisfies \(L_N(M_N;1)>3/4\) or \(L_N(M_N;1)<5/7\). The modulus \(315=3^2\cdot5\cdot7\) is short because its radical \(105\) is short; no separate expansion at \(315\) is required. The fixed kick \(\tau=10^{-80}\) preserves the gap above \(3/4\) when \(8t(N)\le3N\) and \(N\le10^{39}\), through \(10^{26}\) on the ratio-preserving families whose pure margin exceeds \(13/420\), and through \(2\cdot10^{26}\) for \(N=15r\). The kick is not claimed for a ceiling tower: at \(3\cdot23\) the gap \(575/22594\) is smaller than \(13/420\). It is not claimed for an inert exponent-one partner \(q\ge40\), for \(15r>2\cdot10^{26}\), or at \(u_{207}\). Python, C++ and a Lean rational witness certify the integers. Lean certifies the closed comparisons, including the fraction at inert partner \(13\); the other twenty-six inert rows are recomputed only by the two integer programs. No density is proved. The signed off-diagonal sum stays open. BGS-TRACE-005 and BGS-BGS-001 remain open. No new external dependency.


## 2026-10-29 — Square-free products of at least three primes

Register BGS-TRACE-123. Every square-free odd modulus with at least three distinct prime factors satisfies \(L_N(M_N;1)>3/4\), at distance greater than \(1/2\) from the CUE value. The fixed kick \(\tau=10^{-80}\) preserves that gap through \(10^{39}\) when there are at least four prime factors, and when the modulus is a product of three primes not divisible by \(15\). On \(N=15r\) the kick is preserved only through \(10^{26}\); above that window the pure sum remains above \(3/4\) and the kick is not claimed. The modulus \(N=195\) is not short, and the bound there is the eight-term subset expansion. A prime square is outside this note. The later note BGS-TRACE-124 places \(315=3^2\cdot5\cdot7\), which is short because its radical \(105\) is short. ERR-063 corrects the wording \(r\) other than \(5\). Semiprimes remain the dichotomy of BGS-TRACE-122. Python, C++ and a Lean rational witness certify the integers. No density is proved. The kick at \(u_{207}\) remains unresolved. BGS-TRACE-005 and BGS-BGS-001 remain open. No new external dependency.

## 2026-10-29 — Chinese product for the cat-map trace square

Register BGS-TRACE-122. For every odd modulus the pure trace square is the product of the trace squares at the prime-power factors, and the order is the least common multiple of the prime-power orders. The square-free Abel sum is a finite combination of geometric series. Every product of two odd primes is decided: short composite orders, non-short multiples of \(7\), and non-short products of \(3\) with a short prime lie above \(3/4\), and every remaining semiprime lies below \(5/7\). The fixed kick preserves the gap above \(3/4\) through \(10^{26}\) on \(N=21\). ERR-062 records that a split full-order multiple of \(7\) and a non-short product of \(3\) with a short prime do not occur. It is not transferred on the side below \(5/7\). A modulus with three distinct prime factors is not classified in this note; \(N=195\) is settled later by BGS-TRACE-123. Python, C++ and a Lean rational witness certify the integers. No density is proved. The kick at \(u_{207}\) remains unresolved. BGS-TRACE-005 and BGS-BGS-001 remain open. No new external dependency.

## 2026-10-29 — cat-map order trichotomy

Register BGS-TRACE-121. The order of \(C\) modulo an odd prime divides \(p-\varepsilon\) and is short, long, or split-half. Short primes lie above \(3/4\), long primes lie below \(5/7\), and the only undecided prime of TRACE-120, \(p=7\), lies above \(3/4\). Every larger split-half prime lies below \(41/60\). The lifting depth decides every odd prime power: powers of \(7\) stay above \(3/4\), depth-one powers of a larger split-half prime stay below \(5/7\), and depth at least two puts the higher powers above \(3/4\). The fixed kick preserves these comparisons through \(10^{26}\), except the large split-half powers, which stop at \(10^{25}\). The pure map at every odd Pell dimension \(n\ge5\), including \(u_{207}\), is already above \(3/4\); the kick at \(u_{207}\) is not. Python, C++ and a Lean rational witness certify the integers. No density is proved. BGS-TRACE-005 and BGS-BGS-001 remain open. No new external dependency.

## 2026-10-28 — cat-map order ladder

Register BGS-TRACE-120. The multiplicative order \(t(N)\) of the frequency matrix \(C\) decides the Abel statistic. If \(12t(N)\le5N\), the pure cat map satisfies \(L_N(M_N;1)>3/4\). If \(p\) is an odd prime and \(2t(p)\ge p+1\), the distance from \(L_p(M_p;1)\) to the CUE value is less than \(1/2\). The fixed kick preserves the short side for every such odd \(N\le10^{39}\) and the long side for every such prime \(p\le10^{26}\). At \(N=35\), not a Pell number, one return lies below \(3/4\) and the geometric ladder crosses it. Python, C++ and a Lean rational witness certify the integers. The kicked map at \(u_{207}\) is not decided. BGS-TRACE-005 and BGS-BGS-001 remain open. No new external dependency.

## 2026-10-28 — kick-blind arithmetic spikes

Register BGS-TRACE-119. At the single dimension \(N=u_{205}\) the fixed kick satisfies \(L_N(U_N;1)>3/4\). The argument is a positive-time diagram expansion: resonant diagrams of degree at most 11 are archimedean zeros, and indecomposable gaps are at most 4, so the activity remainder stays below the Abel budget. Python, C++ and a Lean rational witness certify the integers. The third-order operator-norm remainder and the Hilbert--Schmidt triangle remain silent at this index. At \(n=207\) the pure second-order center still lies below \(3/4\). BGS-TRACE-005 and BGS-BGS-001 remain open. No new external dependency.

Register BGS-TRACE-118. At \(N=u_{203}\) the fixed kick still satisfies \(L_N(U_N;1)>3/4\), by a second-order trace expansion. The cat-map orbit of the symbol is trace-orthogonal except for one overlap of size \(7/10^6\). Python, C++ and a Lean rational witness certify the integers. The same third-order majorant is vacuous at \(n=205\). The Hilbert--Schmidt triangle is silent at that index as well, and at \(n=207\) the pure second-order center lies below \(3/4\). BGS-TRACE-005 and BGS-BGS-001 remain open. No new external dependency.

Register BGS-TRACE-117. The pure cat map stays a fixed distance from the CUE Abel value on \(N=u_n\) for every odd \(n\ge5\). The fixed kick \(\tau=10^{-80}\) preserves that gap on the 99 odd indices \(5\le n\le201\), through the 77-digit dimension \(u_{201}\). Python, C++ and a Lean rational witness certify the integers. The one-term estimate stops beating \(3/4\) at \(n=203\). BGS-TRACE-005 and BGS-BGS-001 remain open. No new external dependency.

## Aristotle formalization integration, 28 October 2026

Adapted all 39 substantive modules from the older Aristotle snapshot into the existing Lean 4.33.1 graph. The [coverage map](formalization/MATHLIB_LAYER_RU.md) and [receipt](evidence/formalization/aristotle_20261027/receipt.json) record exact theorem scope, 589 axiom-audited declarations and the successful aggregate build. ERR-060 corrects the pure-loss scalar identity in the proof and manuscript. Current claim states, TRACE-114–116 and pinned dependencies are retained; no BGS closure is asserted.

## 2026-10-27 — operator-resolution continuation

Adopt TRACE-114/115/116 at their exact author-reviewed scopes; connect the uniform trace bound to compact pair-test transfer, and distinguish the short-trace barrier from the exact kicked family. Synchronize the registry, theorem index, dependency graph, topic views, bilingual introductions and unified manuscript. Consolidate the historical chat source into one immutable archived Markdown; avoid duplicate proofs and programs. Unreviewed candidate estimates remain explicitly unadopted.

## research-2026.10.1 — phase-5 release preparation

Layered licensing applied (decision R3): source code under MIT
(`LICENSE`), scholarly texts and data under CC BY 4.0
(`LICENSE-CC-BY-4.0.txt`); per-path map in `LICENSE_POLICY.md`.
License sections added to `README.md` / `README.ru.md`;
`CITATION.cff` and `.zenodo.json` license fields set (single-license
fields, D4 confirmed). No registry state, claim
status, or manuscript content changed by this package. Release tag research-2026.10.1; registry at freeze: 199 claims =
173 proved / 12 verification-pending / 9 conditional / 5 open
(BGS-BGS-001, BGS-CAYLEY-005, BGS-INFO-001, BGS-RES-003,
BGS-TRACE-005). The freeze receipt
(record/audits/freeze_receipt_research-2026.10.1.md) carries the
release commit.

## 2026-10-22 — full repository recheck

Restored and authenticated all 6,563 files of main at 7fb99b4 before editing.
Repaired five missing external dependencies for CAYLEY-006/007, 30 missing
source anchors and 19 malformed errata authority paths. Corrected a registry
audit false positive and added regression checks. Aligned the arithmetic
density main term with the checked source; synchronized generated views and
current English/Russian navigation. No claim state was changed by this recheck.
[Findings and actual checks](record/audits/repository_recheck_20261022/report.md).

## 2026-10-21/22 — trace closure and complete spectral edition

Integrated the 535-unit final spectral source edition and TRACE-106 through
TRACE-113. Analytic project proofs close the earlier TRACE-109/110 input
qualifications; TRACE-112 supplies an independent displacement-density route,
and TRACE-113 supplies the uniform power-trace input. Global matching has
order $1/\log N$, including a Pell lower order. Microscopic BGS remains open.
[Trace closure review](record/spectral_research/trace_closure.md) and
[source integration](record/spectral_research/spectral_final_integration.md).

## 2026-10-20 — repository reconciliation

Current navigation and complete dependency views are generated from the authorities.
Reconciled bibliographic coverage and explicit epochs; repaired optimized entry guards.
[Review and actual verification scope](archive/record/repository_reconciliation_20261020.md).

## 2026-10-19

- Integrated eleven missing research packets and the reviewed two-channel
  attachment with a 654-file SHA-256 inventory and preserved execution records.
- Added TRACE-095 through TRACE-105 with explicit conditional and auxiliary
  boundaries; synchronized source statements, ledger, registry/DAG, navigation
  and the manuscript continuation. Fixed-model BGS remains open.
- Completed the four-port and second-defect account, the joint quartic cluster
  theorem, and exact positive Cauchy-source laws with a signed-source obstruction.
- ERR-031 records stale source provenance of one historical failed run. New
  invalid/failed attempts are retained separately from corrected runs.

## 2026-10-16

- Reconciled the 15 October 103-section record, 16 original notes and all 90
  historical inventory entries against main e20825f. Preserved source hashes.
- Integrated 11 scoped theorem/reduction families, corrected resonance
  necessity, Hardy hypotheses and discrete Toeplitz grid requirements.
- Added reproducible source checks and execution receipts; synchronized the
  scientific registry, DAG, thematic navigation, RU/EN reading surfaces and
  manuscript section. Physical TRACE-005 and BGS remain open.

## 2026-10-06 — quantitative collective diffusion continuation

- FM-019: exact N^2 total-Weyl blocks and a universal two-copy diffusion
  gap on the whole identity/swap complement at every odd N>=3.
- All parity cases closed by shifted-grid annuli, geometric Hardy
  summation, cross twists and exact kernel compression; no external
  gap theorem or computed spectrum is imported.
- Exact pair-dephasing angle and explicit original m=1 rate; the stronger
  vanishing-noise Heisenberg estimate for that law stays open.
- Explicit refined shared-noise law at m=N^3 gives mass c_0u/4 for
  u=N^-alpha, 0<alpha<1. One-copy channel is exactly unchanged;
  higher-copy law is explicitly changed. Fixed-observable classical
  retention is mean-square HS, not microscopic spectral continuity.
- Two internal analytic passes by one fresh reviewer; bounded exact
  arithmetic and separate deterministic-start float64 diagnostics.
  Nonlinear functional, original signed comparison and BGS remain OPEN.

## 2026-10-06 — actual Weyl transfer and common-noise invariant classification

- FM-018: whole-growing-band twisted average, complete adjoint-arc
  frequency coercivity and explicit all-noise regularized singular gap
  for the unchanged actual fixed-coupling map; constants noneffective.
- Exact two-pair Gaussian realization and a microscopic massive quadratic
  block; finite nonlinear and fourth-moment discriminators retain the
  distinction between channel data and spectral statistics.
- Exact ordered common-noise higher-copy channel; identity/swap is the
  entire peripheral space in two copies at every finite odd dimension,
  including composite N. Uniform reduced shrinking-noise gap is open.
- Three analytic passes by one fresh reviewer, bounded exact arithmetic
  and six supplementary symbolic identities with preserved diagnostics.
  Full nonlinear control, original signed cancellation and BGS remain OPEN.

## 2026-10-04 — actual-start comparison and circular relaxation

- FLOW-012: original-chain comparison retaining the bounded-trace starting
  matrix and its exact centered Dyson reference; initial transient controlled.
- FLOW-013: schedule-dependent empty noisy limits with global uniformity,
  bounded fixed traces, simple spectra and all positive power traces nonzero.
- FM-017: initial Poisson regularity from FM-007's existing logarithmic
  trace window, two controlled heat-phase stationary points and exponential
  unweighted vertical-tail suppression at a slower vanishing time.
- FLOW-014: gap-independent resummed contour bounds, complete crossing
  residues and windings, confluence and full Fredholm convergence.
  Actual-start original-chain Sine_2 at t=8g, epsilon=N^-9/sqrt(t),
  floor(2t^3N^36) steps, with smooth Laplace error O_f(sqrt(g)).
- Independent internal checks and two bounded finite-control packets.
  Deterministic noise removal, faster actual-start relaxation and BGS OPEN;
  priority is unestablished.

## 2026-10-04 — polynomial original-coboundary joint limit

- FLOW-011: dimension-uniform coefficient and semigroup derivatives;
  positive microscopic Laplace test norm $C_fN^6$.
- Exactly $2N^{34}$ original random steps retain the $O_f(N^{-1/3})$
  clock-to-Sine rate. Independent internal checking covers the new estimates.
- ERR-026: a slower polynomial regime already follows from FLOW-010's
  previous bound; current scope surfaces corrected, dated evidence retained.
- Forty finite matrix controls, exact derivative partitions and Wolfram
  exponent checks; deterministic BGS and noise removal remain OPEN.

## 2026-10-04 — completion of the fixed-time input

- Explicit leading-Gaussian bound for FM-013: eventual first-two traces
  below 4 and 9, hence numerical K=20 without the historical Faure route.
- Higher-packet localization retained in the quantitative trace integral;
  the dimension threshold and Heisenberg estimates remain unavailable.
- Wolfram replay executes successfully after exact polynomial identity
  reduction; source typo and historical/current scope wording repaired.

## 2026-10-04 — fixed-time packet trace closure and auxiliary-expansion boundary

- FM-013: direct odd-N proof of O_j(1) fixed traces; sharper Faure amplitudes
  remain conditional. Earlier normalized trace vanishing is credited.
- FM-016: fixed-classical-map overlap and affine-quantizer separation.
- TRACE-013: primitive irreversible arithmetic word obstruction, exact tensor
  hierarchy, enlarged two-copy gap and factorial flat spectral exclusions.
- Reproducible finite character, orbit, channel and coherent-frame controls;
  frozen Heisenberg sector and full BGS remain OPEN.

This changelog records changes in scientific state. Ordinary formatting and
implementation-only commits need not appear here.

## 2026-10-01 — folded-square refinement of resonant cubic control

- `BGS-TRACE-012`: sharper signed sector estimate, explicit root
  allocation, strict realizable separation from the global fourth
  moment and exact factorial crowding thresholds;
- finite Fourier, convex-count, Gram and noncommuting controls, with
  recorded independent Wolfram symbolic values;
- actual-map coherence remains finite-dimensional; E/G asymptotics,
  nonresonant cancellation and BGS remain OPEN.

## 2026-09-23 — scoped classical and frozen-kick results

- `BGS-RES-005`: all-lag translated classical Riesz gap for the fixed physical
  symbol under linear cat-map transport, with an explicit weighted-Wiener
  neighborhood; the nonlinear analytic frontier remains open;
- `BGS-FM-005`: the actual frozen generator decomposes into `gcd(N,7)`
  irreducible Jacobi chains, yielding a qualitative exact kick-rank bound
  through a pinned classical transcendence theorem; its approximate-rank
  statement applies only before eigenphase wrapping;
- independent internal derivation review covers the classical estimate; the
  kick-rank review is a self-review. Neither result supplies fixed-strength
  Heisenberg joint-trace estimates or proves BGS.

## 2026-09-22 — finite-orbit and spectral-inference boundaries

- `BGS-RES-004`: finite signed-orbit smooth resonance-lag rigidity, with the
  arbitrary analytic infinite-orbit problem left open;
- `BGS-TRACE-006`: clustered Abel lower bound and an abstract counterexample
  to inferring a positive-time Heisenberg-window form factor from clustering;
  no assertion that this spectrum is the frozen quantum map.

## 2026-09-22 — repository institutionalization

- canonical project identity normalized to BGS;
- scientific README and source-of-truth hierarchy established;
- machine-readable claim and theorem-dependency registries introduced;
- stable claim-ID namespace introduced;
- contribution, referee, release, errata, and publication-candidate protocols
  introduced;
- no mathematical claim promoted by this infrastructure work.

## 2026-09-21 — fixed-map continuation

- fixed-model symmetry theorem promoted in its stated small-coupling scope;
- full-symbol odd-Pell crossover and necessary escape condition promoted;
- exact low-moment/transfer controls and repeated-clock falsifier promoted;
- three-orientation mixed-resolvent barrier promoted conditionally;
- Fourier-line resonance coercivity and local-jet obstruction promoted;
- fixed-strength microscopic BGS remained OPEN.

## Corrections

The permanent correction/retraction record is `record/retractions.md`.
`ERRATA.md` is the reader-facing index; it never replaces the full record.

