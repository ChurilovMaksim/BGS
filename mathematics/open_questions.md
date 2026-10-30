# Open mathematical obligations

## Phase average, revival, and the signed sum

Line H (BGS-TRACE-207 to BGS-TRACE-209) refutes Conjecture R (BGS-TRACE-179) as stated, at η = 2, and leaves the following open. (i) The odd m with 3 ∤ m in {17, 19, 23, 25, 29, 31, 35, 37, 41, 43}, where the Weyl term dominates the certified bound (m = 11, 13 are BGS-TRACE-195). (ii) Every m with 3 | m (BGS-TRACE-190). (iii) η ≠ 2 for the Line B kick: certifying η-intervals would decide R restricted to compact ranges avoiding 2, which is not registered separately. (iv) The sign s = +1. (v) R_NSW (BGS-TRACE-210, open; split from BGS-TRACE-179): it fails if and only if h_m is prime for infinitely many m, which is unknown. (vi) H∞,7 as stated in BGS-TRACE-196 (single-disc space) is not proved; only its conclusion for s = −1 is established, on the lifted space. None of this bears on BGS-BGS-001 or BGS-TRACE-148.

Lines F and G (BGS-TRACE-197 to BGS-TRACE-206) settle the k1-kick analogue of Conjecture R at η = 2 for all odd m ≥ 15 (computer-assisted) and leave the following open. (i) Run the lifted certificate for the Line B kick f_B (about 24 000 dimensions per operator); with an alphabet-tail bound this would discharge H∞,7 of BGS-TRACE-196 and decide Conjecture R (BGS-TRACE-179) at η = 2 along 3 ∤ m. (Done for s = −1 in Line H: BGS-TRACE-208, 209.) (ii) Certify the η-window (BGS-TRACE-202) on intervals rather than grid points. (iii) Prove the dilution identity (BGS-TRACE-204). (iv) Test Conjecture R′ (BGS-TRACE-206) against its pre-registered m = 17 prediction, then at larger m.

Line E (BGS-TRACE-183 to BGS-TRACE-196) bears on BGS-TRACE-179. The natural next steps are the following. (i) Discharge H∞,7 (BGS-TRACE-196): certify the truncated 49-state spectrum for the Line B kick, and prove a uniform alphabet-tail bound, e.g. on stadium domains. That would disprove Conjecture R at η = 2 along 3 ∤ m. (Done on the lifted space instead, Line H: BGS-TRACE-209.) (ii) Do the same for the k1 analogue (H∞, BGS-TRACE-188). (iii) Decide the subsequence 3 | m (BGS-TRACE-190), where 7 | h_m and the ∓196 resonance is diluted. (iv) Certify on η-intervals (BGS-TRACE-191). (v) Formalise the general-m identity γ = −s·ι(c) of BGS-TRACE-194 in Lean, and extend the Line B kick certificate of BGS-TRACE-195 beyond m = 13.

BGS-TRACE-179 (Conjecture R; refuted as stated at η = 2 by BGS-TRACE-209) and BGS-TRACE-210 (R_NSW, split from 179; open) ask for \(\max_{\eta\in[\eta_0,\eta_1]}|\tilde W^{\mathrm{rest}}_m(\eta)|=o(m)\) on compact \(\eta\)-ranges, through odd \(m\) (179), and along NSW-prime \(m\) (210). It is not reduced to a known conjecture or a large-sieve inequality. BGS-TRACE-180, the fixed-\(\eta\) central limit law, is open; the numerics stop at \(m\le 11\) and the KS yardstick is heuristic. BGS-TRACE-181, non-degeneracy \(\mathrm{ND}_m\) for composite \(h_m\) and for even \(m\), is open, so BGS-TRACE-164 stays conditional on \(\mathrm{ND}_m\) for these \(m\). BGS-TRACE-182, the \((m,\eta)=(11,2)\) outlier, is unexplained; the torsion attribution is withdrawn. BGS-TRACE-177 records numerical observations only and is filed as open. BGS-TRACE-174 stays conditional on (I1)–(I3). Nothing is proved at \(\tau=m/N=O(1)\). This is not progress on BGS-BGS-001 or BGS-TRACE-148. "\(B_m\to 2m\)" is not claimed.

BGS-TRACE-149 through BGS-TRACE-151 give the exact bridge $E|\mathrm{Tr}\,U^m|^2=\Psi_m(t_N)$ for a fixed finite set of random cosine modes, at every odd $N$ with $\gcd(N,D_m)=1$, the $1/N$ expansion with residue period $g'_m$ (not uniform in $\eta$ or $K$), and the orbit-pair form. These are Line B's Theorem 1 applied for each kick realisation and the Boasman–Keating mechanism, not new. BGS-TRACE-152 proves the strong-kick limit $B_m^{\mathrm{sym}}$ at every residue under dihedral-class separation. BGS-TRACE-154 proves $B_m^{\mathrm{sym}}<2m$ for every odd $m$. BGS-TRACE-153, the instances $m\le 7$, stays verification-pending. BGS-TRACE-155, $B_m^{\mathrm{sym}}<2m$ for even $m$ beyond the computed range, remains open. BGS-TRACE-156 is multiset separation and the half-turn collisions. BGS-TRACE-157 shows that the $1/N$ coefficient is odd in the residue, so it is not $-2m^2$ uniformly in $N$. BGS-TRACE-158, the decay $c_1\to 0$, is conditional and Gaussian-only. BGS-TRACE-159 remains open: for uniform phases $c_1$ is not shown to vanish and numerically grows with $\eta$. BGS-TRACE-160 transfers Line C (BGS-TRACE-146) to the full band up to $p^me^{-cp}$. BGS-TRACE-161, the intermediate band $K=\kappa N$, is an open sketch. BGS-TRACE-162, the crossover conjecture, remains open. This does not prove BGS-TRACE-005 or BGS-BGS-001, and it says nothing about eigenvalue statistics beyond the second moment of $\mathrm{Tr}\,U^m$ at fixed $m$.

BGS-TRACE-143 through BGS-TRACE-146 give, for every prime $p>4^m$, the fixed-$m$, exact-in-$p$ expansion through order $1/p$ of the maximal Haar diagonal-phase form factor, including the coefficient $-2m^2$ for $m\ge 5$. Gnutzmann–Seif 2004 derived $2\tau-2\tau^2$ diagrammatically for this ensemble, Gnutzmann–Altland 2005 and Pluhař–Weidenmüller 2014 predict the full COE form factor non-rigorously, and Berkolaiko–Keating 1999 did exact all-pairs combinatorics for random-phase star graphs; new here is only the rigorous fixed-$m$ exact-in-$p$ result, the complete classification including swaps, and the $m\le 12$ expansions. BGS-TRACE-147 stays verification-pending: the expansions through $m=12$ are computer-assisted, an independent referee replay at $171$ primes is deposited, and promotion is a separate status decision, as for BGS-RES-022. The fixed-$m$ coefficient of $p^{-2}$ differs from $2m^3$ at $m=5,6,8,9,12$. BGS-TRACE-148, the scaling-limit conjecture, remains open. None of this is a fixed-$\tau$ theorem, none of it covers the fixed kick, and BGS-TRACE-005 stays open.

BGS-TRACE-133 gives the twisted closure formula for the position-diagonal kick; BGS-TRACE-134 proves a pointwise bound and the \(\exp(-\eta^2 t\sigma_d/2)\) limit on the minimal-period sequence, with an explicit bound that is non-informative at computable \(N\) (first below \(1\) near \(N\approx10^{191}\) at \(\lambda=1/4\)); BGS-TRACE-135 gives the half-period parity reduction when \(S^{t/2}\equiv -I\). BGS-TRACE-136 (even order) and BGS-TRACE-137 (odd order) remain open conjectures; Monte Carlo in the note is diagnostic only. Nothing is claimed for the full kick, the fixed kick, or returns \(kt\) with \(k\ge 2\). BGS-TRACE-140 proves that Haar position phases and Haar momentum phases give the short-time unitary value \(m\) on odd primes with \(\delta\not\equiv -1\), with an explicit error. The reflection contribution is \(o(1)\), and position conjugation reverses the momentum factor only on a Haar-null set. BGS-TRACE-141 extends the count to the moment \(k!\,m^k\). BGS-TRACE-142 identifies the Gaussian main term \(m(1+e^{-vm})\); the non-injective remainder is not bounded, so the limit is verification-pending. The odd part of the maintained symbol has energy \(9/125000\). The choice \(v=\sigma_{\mathrm{odd}}\eta^2\) is a convention, and partner-variance matching gives twice that. The windows of Theorems 1 and 2 stop at a multiple of \(\log p/\log\log p\). Times of order \(p\), the fixed kick, and BGS-TRACE-005 remain open.

BGS-TRACE-132 gives the fixed-time limits. Haar diagonal phases tend to \(2m\) for each \(m\ge 3\). The antiunitary \(\Theta'=DEK_0\) reverses \(DM_N\) for every hyperbolic \(S\). A finite cosine with \(\eta=o(N^{-2/3})\) tends to \(1\) along odd \(N\) coprime to \(\beta(2-u_m)\). Along \(N\) divisible by \(7\) (e.g. \(35,77,91,707\)) the time-\(3\) kernel has order at least \(49\), so the limit \(1\) fails when \(\gcd(N,\beta(2-u_m))>1\). Sending \(\eta\to\infty\) first, with frequencies \(1\) through \(m\) present, recovers \(2m\). A fixed nonzero \(\eta\) and a frequency set that does not contain \(\{1,\ldots,m\}\) are not identified. Row inversion tends to \(m\). A momentum sine leaves the class \(DM_N\), and its form factor is not identified. BGS-TRACE-131 gives the phase average for every hyperbolic \(S\in\mathrm{SL}(2,\mathbb Z)\) and every finite cosine kick, through order \(\eta^2\). The identity revival is identified only through order \(\eta^2\). The all-order law at \(m=\mathrm{ord}(S\bmod N)\) is proved only as a limit along the Bonechi–De Bièvre minimal-period sequence (BGS-TRACE-134, explicit bound non-informative below \(N\approx10^{191}\)); for generic \(N\) it is the open BGS-TRACE-136 (even order) and BGS-TRACE-137 (odd order). BGS-TRACE-005 stays open.


BGS-TRACE-130 proves the local antiunitary \(\Theta=DK_0\) for every real diagonal kick, with \(\Theta^2=1\) and \(\Theta U\Theta^{-1}=U^\dagger\). The orthogonal-class name is a heuristic for that antiunitary. It is not a COE form factor, and it does not exclude a CUE form factor. The modes with displacement \(\ell=\pm 1\) each have energy \(9/160000\). The full symbol is \(K_0\)-even for some phases and not for almost every phase. The momentum sine \(B_N=(T_N(1,0)-T_N(-1,0))/(2i)\) is odd under position conjugation and has symbol energy \(1/2\); a nonzero multiple is not a function of position, and its form factor is not identified. The scale \(\eta^2 N\cdot 9/160000\) is not derived. BGS-TRACE-129 gives the Bessel average of the classical orbit sum for a position-diagonal kick at a scalar return. That identity is not the quantum sixteen-phase average: a referee Monte Carlo differs from it by ≈1.7 at \(N=11\), \(m=12\), and by up to ≈6 at \(N=29\), \(m=10\) (\(\eta=2\)). It also gives the vanishing of the sixteen-phase coefficient at time one, so the average there equals \(1+\rho_1\). The exponential \(\exp(-m\sigma\eta^2)\) is the degree-two jet of that average. It is not an identity at \(\eta^2\sigma m\) of order one: the quadruple excess of the position orbit is positive at \(p=11\). A uniform bound of the quantum trace by that exponential, a COE limit of the sixteen-phase form factor, and the crossover to CUE driven by the momentum modes of energy \(9/160000\), remain unresolved. BGS-TRACE-128 gives the fixed-time limits of the diagonal-phase ensemble: \(2m\) for the symmetric cat map at each \(m\ge 3\), and \(m\) after row inversion on an odd prime. Both of those windows stop at a multiple of \(\log N/\log\log N\). The sixteen-phase ensemble at times of order \(N\) remains unresolved.

BGS-TRACE-126 evaluates an auxiliary average of \(|\operatorname{Tr} U^m|^2\) over independent phases on the 16 mode pairs, through order \(\eta^2\), and identifies the second-order coefficient at a prime revival. That average is not the fixed-kick statistic. The linear term of the fixed kick is nonzero at \(N=11\), \(m=3\). Replacing the time-ordered product at a full period by the exponential of the averaged kick is not proved, so the Kurlberg–Rudnick matrix-element law does not evaluate \(N^{-1}|\operatorname{Tr} U^P|\). Inside the truncation \(m B|\eta|\le 1\) with \(m\le N\) and \(\eta=\tau N\), the parameter \(\tau^2 N^3\) is \(O(1/N)\) along \(m\sim N\). A positive limiting value of that parameter remains open.

Parity and position-basis conjugation hold for every real coupling at dimension \(7\), where the kick is \((9/10)I\), and they fail for every other odd dimension when \(0<\lvert\eta\rvert<\pi/B\). That dichotomy does not decide a COE or CUE limit. The signed off-diagonal sum in BGS-TRACE-005 remains the open fixed-family obligation.

## Remaining fixed-family task after the final spectral edition

The [self-contained task](../record/remaining_breakthrough_task_20261021.md)
supplies all definitions and the complete all-order criterion without file
access. Even its first fixed band-two pair defect remains unestimated.
After rotational-path removal the signed remainder must produce a nonzero
negative plateau correction. TRACE-108's one-step quartic term and TRACE-111's
initial curvature/early inflection do not evaluate that remainder.
The TRACE-109/110 input qualifications are closed by the
[22 October review](../record/spectral_research/trace_closure.md). TRACE-112/113 control
short logarithmic windows or global spectral distance, not this signed
Heisenberg-scale remainder.

The [21 October physical-kick results](fixed-map/physical_kick_trace_decay.md) do not close
the original signed Heisenberg hierarchy. [All-order polynomial replacement](fixed-map/physical_trace_polynomial_approximation.md) controls its approximation error,
while the complete remaining signed polynomial sum is still unestimated.

## Current open obligations (20 October 2026)

The five claims with `state: open` in
[claims.json](../record/claims.json) on this date are:

| Claim | Obligation |
|---|---|
| BGS-BGS-001 | Fixed-strength microscopic BGS universality for the maintained frozen map |
| BGS-TRACE-005 | Model-specific signed Heisenberg-scale desymmetrized joint-trace estimate |
| BGS-CAYLEY-005 | Sharp centered pointwise Cayley energy target |
| BGS-INFO-001 | Full vanishing-noise tomography transition |
| BGS-RES-003 | All-members analytic resonance nondegeneracy |

The dated sections below are historical snapshots in chronological
layers; the table above is the current summary.

## After the 19 October signed-cluster continuation

The complete second defect and full four-port open zero are now established
for the special symplectic circular-phase ensemble. Arbitrary counts of all
individual defects one or two are controlled for tau<1/9. The missing connected
(3,3,3) source is known only through size nine; no full value is assigned.
The next saturated type is (4,3,5). A general graph Ward cancellation, a uniform
sum of all remaining types, all mixed Heisenberg traces and frozen-model transfer
are still required. [Exact current account](trace-bridge/phase_ensemble_continuation.md).
Positive Cauchy projections do not determine the needed joint matrix law.
The fixed-channel route retains its separate G/TC/R hypotheses.

## After the 16 October Abel/Gaussian continuation

The [Abel theorem](trace-bridge/abel_clock_rigidity.md) closes quantitative stability
of the clock floor, with optimal exponent 1/2; it does not estimate the physical
excess. The [flat equal-edge theorem](trace-bridge/gaussian_equal_edge.md) closes
Gaussian relative comparison for every m=o(N), exact exponential growth at
m/N->alpha, the first collision moment and negligible triples.

The subsequent [TRACE-094 theorem](trace-bridge/wick_collision_poisson.md) proves the
full flat Wick collision law Poisson(2alpha^2), the exact ratio exp(-alpha^2),
and the formerly missing all-fixed-order derivative bound. These are analytic
conclusions beyond the earlier first moment and C++ samples. Still open are
transfer to the actual non-flat profile, the full physical signed polynomial
remainder and every-order hierarchy TRACE-005. The radial iid corollary does
not cover fourth moment greater than two without an additional exponential-UI
argument. [Current checkpoint](../archive/record/wick_poisson_continuation_20261016.md).


## Research-record integration, 16 October 2026

[Exact review and 90-entry inventory](../archive/record/chat_integration_20261016.md).
The all-order process implication no longer requires an independent UI premise.
The actual signed hierarchy, physical parameter moment and positive Hardy
excess limits remain unproved. Resonance deletion is sufficient only.


TRACE-083 closes the abstract-family question left by TRACE-082's
full-return comparison: an individual observed memory coefficient
can remain almost an isometry on nearly all centered diagonal
directions, even with a negligible monitored energy tail.
The exact cubic-composition resonance prevents replacing the
full signed hierarchy by low unconjugated trace cancellations.
It does not supply an estimate for the actual fixed-map source.
[Exact scope](spectral-obstructions/coherent_first_return_pulse.md).

[TRACE-081](spectral-obstructions/flat_spectrum_obstruction.md) rules out inferring an
initial microscopic law from flat intensities, small reversal norm, simple
spectrum and a uniform macroscopic measure alone. Its origin average can
still converge to the empty process. [TRACE-082](spectral-obstructions/coherence_memory_plateau.md)
rules out a general singular-norm decay for the full unaveraged coherence
block before time N. Cancellation of specified observed/signed returns is
a different obligation and remains open for the unchanged fixed map.
These obstructions change neither the TRACE-005 target nor the BGS status.

## Frontier after unconditional feedback control, 13 October 2026

[TRACE-080](trace-bridge/unconditional_feedback_flatness.md) closes the
entry-flatness probability for deterministic entry-flat, small-gap starts
on u>=ceil(log(2N)^(4+kappa)). It also closes the corresponding fixed-order
clock and weak-law applications; the extra reversal corollary retains its
separate initial condition. Named eventual FM-021/FM-022 inputs place the
maintained odd-N fixed-coupling family in this auxiliary trajectory regime.
[TRACE-079](trace-bridge/two_step_stopped_concentration.md) supplies the complete
stopped two-step concentration, including the diagonal. Earlier frontier
sentences below concern those older theorems alone and are superseded for
this explicit startup/cutoff class.

The unresolved target is now the microscopic scattering/physical-source
reference law, its signed Ward/balanced identification and deterministic
TRACE-005 comparison/noise removal. The probability theorem and clock law
do not identify the initial deterministic local process. Smaller logarithmic
cutoffs, growing orders, edge laws and BGS remain open.

## Frontier after the checked 11 October integration

Maximal microscopic path stability does not evaluate the initial process.
The balanced phase law still needs the signed overlap defect to vanish;
the deterministic problem still needs complete signed TRACE-005 comparison
and noise removal at the local-relaxation scale. The scalar cavity law is not
supplied by the covariance, clock moment or source-continuation theorems.
The repaired induction now proves every fixed clock order conditional on
all-time entry flatness. [TRACE-076](trace-bridge/haar_feedback_clock_law.md)
now closes that probability premise for a Haar start and gives
unconditional clock laws for independent initial distributions with
relative entropy O(log N) relative to Haar. TRACE-080 now supplies the probability and fixed-order applications for
the maintained initial family on its stated larger cutoff. Smaller cutoffs,
growing-order and edge laws remain unproved. A bounded-entropy gap example rules out a
prescribed-origin microscopic implication from these clock laws alone.
[Exact new boundaries](../archive/record/haar_feedback_continuation_20261012.md).

The [unitary two-step obstruction](trace-bridge/unitary_two_step_obstruction.md)
rules out deriving the required two-step kernel from unitarity, logarithmic
entry flatness and a vanishing intensity singular norm alone. Three-step
mixing can coexist with a logarithmic two-step peak. A dynamic estimate
of the row--column correlation or its accumulated effect is still needed.

The [exact two-step drift](trace-bridge/two_step_restoring_drift.md) now provides
a restoring conditional mean bounded by the three-step kernel. It does
not provide the higher moments or stopped concentration needed for all
entries and times. The additional term
\(\rho(\delta-1/u)/u\) is not \(O(u^{-2})\) from logarithmic flatness alone;
TRACE-077 now controls this forcing on reached entry-admissible depths
`log(2N)^(7+kappa) <= u <= N/log(2N)^2`, by a shrinking Green-coordinate
gap. That stopped theorem alone leaves early entry survival and accumulated
concentration open; TRACE-079/080 supply separate proofs on their
explicit startup/cutoff class. The reached range may be empty;
this stopped theorem does not prove all-time flatness.
[Exact boundary](trace-bridge/green_compression_gap.md).


[TRACE-078](trace-bridge/two_step_increment_variance.md) now supplies the raw
one-step fluctuation estimate `2600 delta²[(P²)ij+(P³)ij]/u` under the
uniform-port frozen-endpoint convention. Earlier descriptions of the
one-step second moment as entirely missing are superseded at this scope.
TRACE-079/080 now close these accumulated and first-exit obligations for
the stated startup/cutoff class. Physical microscopic identification and
BGS remain open.


## Priorities snapshot (11 October 2026)

The table distinguishes the **terminal fixed-model problem**, possible
intermediate proof routes, and mathematically independent directions.
It does **not** assert that completing one auxiliary estimate would
automatically prove BGS. Full mathematical statements and later
qualifications follow below.

| Role | Precise task | Status / caution |
|---|---|---|
| **Main mathematical target** | [BGS-TRACE-005](#b-prove-heisenberg-scale-desymmetrized-joint-trace-estimates): signed, desymmetrized all-fixed-order Heisenberg joint traces at every compact Fourier bandwidth | **Open** for the unchanged frozen propagator; [BGS-BGS-001](#d-positive-microscopic-bgs-universality-for-a-natural-fixed-map) is the terminal local-law claim |
| Balanced pair frontier | Evaluate the actual absorbed [phase Ward overlap](trace-bridge/phase_ward_identity.md) or the corresponding microscopic [Schur-energy radial limit](trace-bridge/balanced_pair_schur_reduction.md) | Exact identities and reductions are available; the necessary limits are **unproved** |
| Signed paths and removal of auxiliary noise | Close the [high-switch/masked residual](trace-bridge/global_switch_transfer.md) and the [deterministic noise-removal defect](fixed-map/microscopic_noise_removal.md) | Partial sector bounds and noisy laws are proved in their regimes; neither gives deterministic all-order universality |
| Pending physical source hierarchy | Complete the submitted [BGS-TRACE-055](../archive/record/research_checkpoint_20261008.md) hierarchy after the [11 October reconstruction](../archive/record/chat_integration_20261011.md) | Covariance and physical L2 transport are proved. Conditional clock and gap theorems require all-time flatness. TRACE-076 gives unconditional clocks for Haar and the entropy class; TRACE-080 closes the maintained startup's probability and corresponding clocks at log^(4+kappa); physical microscopic cavity identification remains open |
| Independent theorem frontiers | Centered [Cayley energy](#a-improve-pointwise-cayley-energy-to-the-centered-quadratic-scale), all-analytic [resonance](#e-all-members-analytic-resonance-nondegeneracy) and [information limits](#f-full-vanishing-noise-tomography-transition) | Their status and hypotheses are independent of the fixed-map BGS conclusion |

The [claim ledger](../record/claim_ledger.md) determines status.
The [full manuscript](../manuscript/README.md) is a developing research
account, while older dated observations below remain accessible for
scientific provenance. The current Lean scope is **23 active modules /
26 Lake jobs** at the [11 October execution](../archive/evidence/executions/20261011/chat-research/fresh/lean_execution.json);
older receipts retain the smaller scope of their original builds.
No analytic BGS conclusion is formalized.

## Frontier after the 8 October continuation

TRACE-053 closes the stated max-entry phase-channel/pinching theorem and
TRACE-054 closes the sharp noncommuting 4/3 inner-jet inequality, including its
smooth localization correction. TRACE-056 closes direct normally absorbed
scalar L1 transport along bounded real unitary flows. These three subsidiary
obligations are no longer open.

The submitted TRACE-055 m=ceil(log(2N)^20) physical hierarchy remains
verification-pending. The 11 October results reconstruct source covariance,
physical-source L2 continuation. The [cavity continuation](../archive/record/cavity_continuation_20261011.md)
adds conditional all-fixed killed upper bounds and gap propagation. The
[repaired fixed-order induction](trace-bridge/conditional_clock_universality.md)
identifies every fixed clock power and its full-depth measure. TRACE-080
now supplies the probability on its matching larger cutoff. Establish
the remaining physical cavity hypotheses, identify the retained scalar
cavity law, control source products and the signed undamped/high-switch
comparison, and close every-fixed-order TRACE-005 for the unchanged frozen
map. Channel-norm decay cannot replace spectral trace extraction.
[Exact disposition](../archive/record/research_checkpoint_20261008.md).


## Current phase/signed frontier

The [current checkpoint](../record/checked_research_checkpoint_20261007.md)
separates the phase Ward v2 signed overlap estimate (13), literal
occupation/Hamming/high-switch marked endpoint T16, completed compact source
signed growing-degree hook covariance, possible literal infinite-subsequence
obstructions and full boundary/gauge/body synthesis. The higher factorial
and bandwidth hierarchy remains an additional obligation after pair closure. The actual q=1,
theta=0 radial theorem has no occupation-uniform or trace conclusion; body
coercivity and complex source bounds do not identify a limit. The original
BGS-TRACE-005 complete signed comparison remains OPEN.

[FM-021](fixed-map/position_chain_mixing.md) supplies the actual cyclic-path ramp and specified marked three-link cancellation, while [FM-022](fixed-map/reversed_path_decay.md) suppresses reverse-cyclic pairs. The remaining once-counted signed OTHER-path contribution must supply the full target, including the negative plateau correction above m/N=1. The once-counted distinct-port three-block and reduced four-block families are now controlled by [TRACE-015](fixed-map/three_block_unmarking.md) and [TRACE-016](fixed-map/four_block_unmarking.md). Variable representations and endpoint-dependent masks still prevent unrestricted automatic unmarking; repeated ports, inter-family overlaps and growing reconnection complexity remain open. Higher factorial orders remain open.


[FM-019](fixed-map/collective_diffusion_gap.md) closes a universal two-copy
summed-generator gap on the full identity/swap complement for every odd
N>=3. Its refined shared-noise law at m=N^3, u=N^-alpha, 0<alpha<1 has
singular mass at least c_0u/4, dominating N^-1. Its one-copy channel is
exactly that of FM-018; its higher-copy law is explicitly changed.

[FM-020](fixed-map/original_channel_gap.md) now closes the original m=1 microscopic-rate obligation: its explicit lower bound is asymptotic to u/[25*1024^2*(1+log N)^2] when u=N^-alpha, 0<alpha<1, and dominates N^-1. The noise law is unchanged. This follows from a uniform low-eigenvalue count and a low-spectral projection angle, not from identifying the ordered product with the summed exponential.

For the refined law, the next obligation is the full nonlinear quenched
determinant functional at a microscopic source, retaining permutation
sectors and quantitative higher-copy moments. Its fixed-smooth-observable
HS mean-square classical limit supplies no microscopic spectral comparison.
The original signed noise defect and J_(N,w)(U_N) are still unestimated.
All deterministic bands/orders and full BGS remain unchanged and OPEN.

The [exact pair heat formula](fixed-map/heisenberg_pair_heat_formula.md) now gives
every signed contraction and a superpolynomial **smoothed** stable-band
form factor for the actual map at a vanishing logarithmic time.
For $J_{N,w}=N^{-2}\sum_mw(m/N)(|p_m|^2-m)$, its actual heat defect is
$-J_{N,w}(U_N)+o(N^{-H})$ for every fixed H>0. The unknown original
value remains the required estimate. The matching simple-spectrum
construction excludes estimating this defect from the specified
sublinear short traces alone. A model-specific signed determinant or
propagator estimate is still needed; this one fixed band is necessary
but does not cover the full signed factorial hierarchy.

The [growing-degree proof](fixed-map/growing_degree_trace_projection.md) now controls
actual compact local projections through $Q=\gamma\log N$ at rate
$N^{-1/4}$. Every $Q_N=o(N)$ still misses the fixed pair vector
$J_{N,w}(U_N)=N^{-2}\sum_mw(m/N)(|p_m(U_N)|^2-m)$, with
$0<a<m/N<b<1/2$, exactly. Its actual vanishing remains open.
G13 obstructs whole-filtration norm control at Heisenberg degree;
G15--G16 obstruct stable Haar-$L^2$ heat inversion even for this
particular fixed local test. Neither excludes a model-specific signed
comparison. The stronger logarithm-squared projection range requires
a uniform growing-index trace bound not proved for the actual operator.

The [fixed-degree projection](fixed-map/fixed_degree_heat_projection.md) now
estimates every fixed neutral projected local test on the actual map.
The exact remaining unperturbed term is $(I-\mathsf P_{Q,N})F_N(U_N)$
for each fixed Q; P7 does not bound it. Small Haar norm is insufficient.
The [clock compensation](fixed-map/clock_structure_and_noise_scale.md) is an exact
control mechanism, not an identity for the actual initial spectrum.

[FLOW-017](fixed-map/coboundary_all_order_limit.md) closes all fixed unbounded
factorial orders and the complete signed Fourier target for the original
**noisy** chain at one superpolynomial step schedule, including one-chain
origin averages in $L^2$. C16--C17 reduce the deterministic signed target
to vanishing of the exact signed sum of one-step defects, equivalently
$L^2$ noise removal for each fixed test. That estimate remains open for
the actual $U_N$. Do not replace the signed sum by absolute step errors.
A single polynomial schedule for all orders, growing-order bounds, an
effective startup threshold and almost-sure full-sequence convergence
also remain open.

[FLOW-015](fixed-map/microscopic_noise_removal.md) states the next weak local
obligation exactly: prove $\int_0^{t_N}P_sG_N\Phi_{N,f}(U_N)ds\to0$
for every positive compact smooth test at the proved logarithmic time.
The modulus must remain outside the entire signed integral. Initial heat
jets cannot establish this in general, even if every derivative vanishes.
Unscaled full-class stationarity is too strong for the actual bounded-trace
start; normalized microscopic loops remain possible. A variational route
must establish a genuine limiting minimizer or justify regularization,
since every raw finite deterministic field has infinite Poisson entropy.
The [six-route review](../record/noise_removal_program_20261005.md)
records the exact alternatives and boundaries. Neither the actual
defect nor the stronger signed factorial hierarchy is estimated yet.

The [general-start comparison](fixed-map/coboundary_general_start.md) now retains
the actual frozen initial matrix and compares its original random chain
to the exact centered-start Dyson law. [FM-017](fixed-map/frozen_mesoscopic_regularity.md) supplies initial Poisson
regularity at $g_N\asymp\log\log N/\log N$ and controlled local stationary
points and unweighted vertical phase-tail suppression at $t_N=\sqrt{g_N}$.
[FLOW-014](fixed-map/circular_dyson_actual_start.md) closes the gap-independent
global contour estimate, crossing residues, all windings, confluence and
Fredholm convergence. At $t_N=8g_N$, the original chain from the actual
map has the Sine$_2$ weak local limit. The next deterministic obligation
is to compare this noisy law with the initial spectrum using actual-map
information; it does not follow by continuity on the microscopic scale.
The [kernel route](../record/circular_kernel_route_20261004.md)
pins the prior finite formula and actual normalization. The
[prescribed-time falsifier](fixed-map/dyson_relaxation_obstruction.md) excludes
choosing $N^{-2/3}$ using only the listed trace inputs, even the whole
logarithmic window. Deterministic noise removal remains a separate task.

The direct FM-013 Gaussian refinement closes K=20 for the first two
initial traces at all sufficiently large odd dimensions. An effective
dimension threshold, the sharper historical action-phase formula,
all-N initial-trace convergence and Heisenberg-time cancellation remain
open; they are different obligations from fixed-time boundedness.

[TRACE-012](fixed-map/folded_quadratic_resonance_control.md) refines the actual-map
input to $E_pG_{d_p,p}=o(1)$ with factorial counterterm control, where
$G_{d,p}=\|P_d(\rho_p^2)\|_2^2$. For prime orders, $G_{d_p,p}=o(d_p^2)$
is sufficient for the latter. Estimate the positive shifted four-point
energy, retaining root allocation, or derive signed cancellation bypassing
this sufficient condition. A crowding obstruction needs an infinite
prime subsequence; finite small-tau*p^2 coherence is not one. Actual
asymptotic inputs and nonresonant signed cancellation remain open.

[TRACE-011](trace-bridge/resonant_cubic_density_control.md) supplies a conditional
resonant cubic deletion: prove the actual block mass $E_p\to0$ and a
bounded averaged local occupancy moment of any order s>3, or critical
cubic density uniform integrability. A quantitative alternative is
$E_p=O(1/d_p)$ and $M_4(p)=o(d_p)$. These inputs remain open. The new
pair-compatible rare-cluster counterexample rules out deriving the needed
cubic tails from pair tests and spectral positivity alone.

The [absolute-norm obstruction](trace-bridge/signed_heisenberg_comparison.md)
(`BGS-TRACE-010`) excludes simultaneous unaveraged absolute pair and
all-order comparison. TRACE-005 means the **signed** weighted discrepancy,
with a modulus outside the entire sum. The first mixed attack is the
factorial cubic, splitting all three resonant strips and retaining the
exact finite CUE counterterms. The reference variance and formal phase
control in that note are not actual-map estimates.

The [prime-resonant audit](fixed-map/prime_resonant_sector.md) identifies the exact
remaining sector input: for every compact positive Heisenberg window,
prove $p^{-2}\sum_{rd_p/p\in K}|\operatorname{Tr}C_{p,d_p}^r|^2=o(1)$.
An equivalent absolute sector comparison has only an $O_K(1/d_p+1/p)$
reference correction. A sufficient spectral condition is Fejer comb energy
$1+o(1)$ across shifted microscopic pairs. Scalar exclusion and a bound
for one selected mode do not establish it. Nonresonant times, composite
dimensions and higher joint traces remain separate TRACE-005 obligations.

The [Heisenberg-note audit](../record/heisenberg_note_review_20260930.md)
closes the classical commutator action and ideal-alphabet FUP obligations.
It leaves the actual quantum torus FIO, normalized matrix-element bounds,
boundary/adjacent-strip channels, a controlled open-compression normal
form, and the pair/all-order renewal identities unresolved. Neither a
scalar finite-type estimate nor an ideal Fourier FUP derives the CUE
plateau or BGS-TRACE-005. A natural-quantization route additionally needs
one common all-order identification with controlled norms/holonomy.

The [quadratic-noise continuation](fixed-map/quadratic_noise_coupling.md)
removes microscopic occupancy from comparison of the two evolved noisy
laws. It does not close BGS-TRACE-005. FLOW-014 supplies actual-start
Dyson relaxation at a logarithmic time. FLOW-016--017 now supply all-order
uniform integrability and limits for the original noisy chain at a different
superpolynomial step schedule; deterministic noise removal remains open. The
[clock theorem](fixed-map/quadratic_noise_clock_limit.md) proves that low traces
and bounded occupancy alone cannot remove the noise. The [direct fixed-time packet proof](fixed-map/fixed_time_wavepacket_trace_bound.md)
now closes bounded starting traces; its constants are not uniform at
Heisenberg times. The historical Faure action-phase application remains
conditional on regularized trace matching. [TRACE-013](spectral-obstructions/arithmetic_word_expansion_obstruction.md)
shows that even bounded fixed traces and a full-space auxiliary two-copy
channel gap cannot replace coherent-word estimates.
The [Möbius reduction](fixed-map/coboundary_mobius_diffusion.md) now proves a
fixed-dimension stopped spectral quotient limit for repeated Gaussian
coboundary steps and an iterated clock-to-Sine theorem. An explicit
simultaneous regime is now established by
[FLOW-010](fixed-map/coboundary_joint_limit.md) at epsilon_N=exp(-N), and the
[polynomial continuation](fixed-map/coboundary_polynomial_limit.md) closes that
clock regime with epsilon_N=N^(-26/3) and exactly 2N^34 steps.
Optimizing the step exponent, actual-start relaxation at faster than the
proved logarithmic time, and deterministic noise removal remain open. No convergence
of the rapidly changing original matrix paths is asserted.

This board primarily tracks unresolved mathematical obligations, but also
identifies a continuing **formalization-depth** task whose earlier finite
build is already established. Stable IDs are assigned in
`../record/claims.json`; the current status authority remains
`../record/claim_ledger.md`. Closed routes and finite controls are indexed in
`results.md`; false or superseded statements belong in
`../record/retractions.md`.

## Frontier board

The [27 September upload audit](../archive/record/cue_upload_review_20260927.md)
does not close any quantum frontier below. The retained classical
periodic-point average (BGS-FM-012) has no oscillatory weight. Pair-only
TG-mean estimates, even if proved, still require a separate higher-order
joint-trace argument to reach the all-order target.

| Claim ID | Priority / role | Closure condition |
|---|---|---|
| `BGS-TRACE-005` | **central fixed-map bottleneck** | Prove the correctly desymmetrized signed weighted Heisenberg-scale joint-trace comparison, with the modulus outside the whole sum, or an equivalent mixed-resolvent hierarchy, on every compact Fourier support. |
| `BGS-BGS-001` | **terminal microscopic target** | Combine `BGS-TRACE-005` with the exact trace bridge, every-bandwidth extension, fixed unfolding, and correct symmetry-class hypotheses to prove the positive microscopic law for the maintained frozen map. |
| `BGS-CAYLEY-005` | arithmetic fourth-moment frontier | Prove centered Cayley energy `(K-1)^4/p + O(K^(2+o(1)))`, or a genuinely equivalent support/divisor theorem in the intended pointwise regime. |
| `BGS-RES-003` | analytic resonance frontier | Resolve the nonlinear analytic coboundary equation for arbitrary nonconstant real-analytic observables. |
| `BGS-INFO-001` | information-theory application frontier | Determine matching minimax upper/lower transitions for the full moment class when physical Gaussian-channel noise vanishes with copy budget. |
| `BGS-FORMAL-001` | continuing formalization-depth work, distinct from open BGS theorems | The earlier receipts are historical; the 11 October **23-module / 26-job** build verifies only its stated finite/algebraic kernels. Expand formal coverage selectively; do not relabel analytic results as formally checked. |

The principal BGS route is therefore not “prove everything above first”.
`BGS-TRACE-005` is the direct model-specific obligation. The Cayley,
resonance, and information-theory frontiers are valuable independent
programmes and possible sources of techniques, but they are not silently
treated as prerequisites for `BGS-BGS-001`.

The pair part of this frontier now has an exact adjoint-resolvent form
(`BGS-RES-006`) and a universal regular-polygon lower floor
(`BGS-TRACE-007`). These sharpen the finite-dimensional description but do
not estimate the model's resolvent or its Heisenberg-scale joint traces. The
closure condition of `BGS-TRACE-005` is unchanged.

The [smooth seven-cut transfer](fixed-map/fixed_map_resolvent_frontier.md)
(`BGS-RES-007`) identifies all compact positive-$s$ scalar-resolvent
limits and their derivatives between the original and cut **full**
propagators, without supplying a value for either. The
[`BGS-TRACE-008` two-clock example](trace-bridge/two_clock_gram_falsifier.md)
shows that the $4/3$ Gram milestone, even alongside simple phases and
nonzero traces of every positive power, is insufficient as a universal
criterion for CUE pairs. The milestone is still necessary and open for
the actual frozen model.

The 23 September exact kick-rank result `BGS-FM-005` does not estimate joint
traces at Heisenberg times. The all-lag classical gap `BGS-RES-005` uses
linear transport of one physical symbol. The subsequent
[`BGS-FM-006`](fixed-map/nonlinear_bracket_pressure.md) proves that **the same**
linear normalization has no uniform nonlinear full-lag upper bound for the
actual kicked map. This classical pressure obstruction does not supply the
`BGS-TRACE-005` quantum joint-trace estimate. The separate arbitrary-analytic
resonance question remains `BGS-RES-003`.

After the 24 September seven-cut reduction (`BGS-FM-007`), the same
compact-frequency signed joint-trace obligation may be proved for either
the original $U_N$ or the **full** approximant
$V_N=e^{i\tau N A_N^{\rm cut}}M_N$. Their full fixed-order local-law
statements are equivalent, and their pair/Abel tests differ by
$O(\tau/\log N)$. The seven path projectors of $A_N^{\rm cut}$ do not
commute with $V_N$; assume no independent spectra. Algebraic
simple-spectrum (`BGS-FM-008`, only $7\nmid N$) and common antiunitary
obstruction (`BGS-FM-009`, except $N=7$) exclude exact degeneracy
mechanisms within their scopes but give no quantitative mixed-trace
cancellation. A concrete pair-moment milestone in the prescribed hierarchy is
$N^{-1}\operatorname{Tr}\Gamma_{N,N}^2\to4/3$, where
$\Gamma_{N,N}=[N^{-1}\operatorname{Tr}U_N^{b-a}]_{0\le a,b<N}$;
this has not been proved for the model.

The later exact [arithmetic trace theorem](fixed-map/frozen_arithmetic_trace_rigidity.md)
(`BGS-FM-010`) proves *nonvanishing* of every positive-power trace,
including at \(7\mid N\), but gives no **upper** estimate in the Abel
sum. The [effective gap floor](fixed-map/frozen_effective_gap_floor.md)
(`BGS-FM-011`) for \(7\nmid N\) is vastly smaller than the mean gap;
it gives no local occupation control. Neither result changes the
closure condition of `BGS-TRACE-005`.

The [singular Haar-CUE benchmark](spectral-obstructions/cue_singular_energy.md)
(BGS-CUE-001) identifies the reference law when the
adjoint inverse-gap regularization is removed, but
weak local process limits alone do not control this
singular boundary. The [coboundary spectral-flow bound](fixed-map/coboundary_spectral_flow_bound.md)
(BGS-FLOW-001) would transfer weak local limits under
specified Birkhoff and commutator estimates, neither
of which is available for the maintained fixed family.
Its associated sine-curvature calculation (BGS-FLOW-002)
blocks a proposed Gaussian-coboundary Dyson-noise shortcut.
None changes the exact closure condition above.

## A. Improve pointwise Cayley energy to the centered quadratic scale

The off/off elliptic correlation layer is no longer an independent open problem: after extraction of the coherent reducible fibre, `offoff_elliptic_spike_theorem.md` proves

```text
Var O << p E_+(A)+K^2p+K^4 sqrt(p)+K^4.
```

The mixed/off-off bottleneck is therefore the same Cayley additive energy.

Three complementary pointwise bounds are now closed:

1. the older Vyugin--Makarychev route gives `E_+(A)<34K^(8/3)` in its explicit range;
2. `cayley_curve_uniform.md`, using Corvaja--Zannier, gives globally for every subgroup order `K>=2`

```text
E_+(A) << K^(8/3)+K^4/p;
```

3. `cayley_fourier_hybrid.md`, using the classical mixed Weil bound after the exact annihilator-character expansion, gives the centered estimate

```text
0 <= E_+(A)-(K-1)^4/p <= 4(K-1)(p-K+1),
```

and therefore

```text
E_+(A)-(K-1)^4/p
 << min(pK, K^(8/3)+K^4/p).
```

The Fourier branch is strictly stronger than the previous worst-curve scale when `K>p^(3/5)`; for `K=p^(alpha+o(1))`, `alpha>3/5`, it has centered exponent `1+1/alpha<8/3` in `K`. It approaches the quadratic scale as `alpha->1`, but it does not improve the sparse arithmetic regime.

The sharp pointwise target remains

```text
E_+(A)=(K-1)^4/p+O(K^(2+o(1))),
```

or equivalently

```text
sum_(q!=0)|1_Ahat(q)|^4 << p K^(2+o(1)).
```

The remaining material intermediate target is now specifically the sparse/intermediate range: obtain any explicit centered `K^(2+delta)` bound with `delta<2/3` where the complete mixed-Weil `pK` branch is not already stronger. The exact split-prime support machinery, scalar resultants, Frobenius amplification and dyadic averaged theorems remain available inputs. None currently gives that sparse pointwise cancellation.

## B. Prove Heisenberg-scale desymmetrized joint-trace estimates

The [clustered Abel calculation](trace-bridge/clustered_abel_window_boundary.md) gives a
quantitative corollary in the existing compensated pinning range, and a
simple-spectrum counterexample to inferring a positive-time Heisenberg-window
form-factor bound from cluster containment, spacing collapse, or Abel
divergence alone. The example does not model the prescribed frozen map; it
clarifies why its mixed-resolvent estimate must still be proved separately.

The 21 September continuation narrows the loop-equation route without closing
it.  Exact moment inequalities strengthen the first two mixed levels, and a
second orientation ((w,w,v)) yields a strictly stronger conditional
differential barrier.  Conversely, repeated-clock spectra show that
arbitrarily many one-upper tests ((w,v,\ldots,v)) at one selected height can
all vanish while the pair statistic remains non-CUE.  Hence any successful
route must control the relevant orientations and varying off-real arguments,
not merely one residual row.


The short-return necessary condition is now explicit in
`returns/return_trace_obstruction.md`: an ergodic intensity-one local limit requires
all normalized sublinear-time traces to vanish, and mesoscopic empirical
densities to become uniform in spatial L1. For the current positive-variance
Gevrey return regime this requires $K\epsilon_K^2\to\infty$.
The converse fails for clock spectra, and density-dependent unfolding changes
the critical obstruction. No positive trace comparison is supplied by this
necessary condition.

The intensity-loss extension now gives the sharp abstract bound
$\alpha\le\operatorname*{ess\,inf}\rho$ for an ergodic local limit and
return density $\rho$. At the free Brownian endpoint with $0<t<4$, such a
limit must be empty. Identifying the actual nonergodic local limit, or its
conditional law after unfolding by $\rho$, remains open for the kicked map.
The inverse-density construction produces the same complete return law
with different unfolded local laws among abstract spectra. Thus return-law
identification alone cannot close this conditional-law obligation.


The September 10 harmonic return theorem now does concern powers of the
actual kicked propagator: `pell/pell_harmonic_returns.md` proves its global
return law, including a free unitary Brownian endpoint. Its multiplicity
$m$ is fixed and its times $mK$ are logarithmic in dimension.
Extending the diagram phase estimates and summability uniformly to
$m\asymp D/K$, and obtaining the required joint-trace comparison, are
unresolved. A marginal free probability law supplies neither estimate.

The September 9 all-order budget now proves a Gaussian distribution theorem
for the full Cayley--Jacobi trace in logarithmic pointwise and subpolynomial
dyadic density regimes; see `cayley_trace_gaussian_limit.md`.
This concerns `Tr M_S(mq)` as an additive parameter varies. The following
obligation concerns `Tr U^m` for a single correctly desymmetrized propagator.
No identity transferring the new theorem to that obligation has been proved.

For the arithmetic trace itself, extending the CLT to fixed polynomial
subgroup size is also open. At order `r`, the current averaged error contains
`Q^(r/2+1)/X`; no fixed positive exponent `Q=X^theta` makes it small for every
order. A stronger all-order estimate or a different distributional argument
is needed to cross this boundary.

For the correct `N x N` spectral block, the deterministic bridge is exact:

```text
C_(2,N)(U;phi)
 = N^(-2) sum_m phihat(m/N)(|Tr U^m|^2-N),
```

and the higher factorial correlations are partition-Mobius sums of joint traces. Compact Fourier support probes powers `|m|=Theta(N)`.

**Closure condition:** prove the weighted joint-trace comparison with the appropriate GOE/COE/GUE target on the Heisenberg scale for a clearly specified natural deterministic family, with all symmetry reduction and unfolding conventions fixed before the estimate.

Classical Green--Kubo positivity, global moment laws, recurrence-time normal forms and finite cyclic-module identities do not substitute for this estimate.

## C. Scope of Fourier-support control

The former separate tail obligation is **closed as a deterministic implication**
for positive normalized averages of finite-circle spectral measures. By
`bandlimited_correlation_extension.md`, comparison on every compact Fourier
support with a reference Schwartz limit extends to every Schwartz correlation
test. The proof supplies uniform translated-cube bounds from one nonnegative
band-limited majorant. It does not bound the absolute Fourier trace tail.

**Remaining scope requirement:** the trace comparison in B must hold for every
compact Fourier support, not merely a common fixed cap. The clock/period-two
counterexample proves that the latter is insufficient. Signed averages,
Hamiltonian window boundaries, and conversion from correlation functions to a
full point-process or spacing law require separately stated hypotheses.

## D. Positive microscopic BGS universality for a natural fixed map

For the prescribed frozen model, the ordinary midpoint symbol is now derived
exactly from the raw Weyl convention.  Its classical map is analytic Anosov,
has only power (C^1) commuters, has no (C^1) reversor, and is not
(C^1)-conjugate to the relevant affine model in the proved small-coupling
range containing the actual (\tau/(2\pi)).  Thus smooth inherited classical
symmetry is no longer a plausible missing explanation.  This does not rule
out (N)-dependent quantum arithmetic structure.

The full-symbol odd-Pell crossover also proves that bounded
(|\epsilon_K|\sqrt K) is incompatible with the CUE pair transform.  The
actual frozen strength eventually escapes that obstruction, so the theorem
locates rather than closes the hard regime.


The harmonic-transition theorem realizes circle-graphon global laws,
including a free semicircular endpoint, in the same fixed Pell cat map.
It varies and samples the observable frequency up to $\sqrt N$. It does not
change the unperturbed propagator's arithmetic spectrum.
The harmonic return theorem subsequently perturbs the propagator and
identifies its global recurrence law, but the quantum kick vanishes,
harmonics are sampled, and microscopic universality remains unproved.
The registry boundary of `BGS-RET-001` records the same limits, together with
the control scope (exact diagram/lattice checks; complex128 matrix controls
at $K=3,5$ with the single value $\epsilon=0.23$) and the external
free-unitary-Brownian identification via Demni (`EXT-DEMNI-2016`).

The project contains several strong negative and structural lessons:

- arithmetic cat maps retain exceptional symmetries;
- some kicked families remain smoothly or all-orders conjugate to the arithmetic model;
- bounded clustering in the Pell critical regime is incompatible with GOE/COE under global unfolding;
- weak Egorov information alone allows spectral rounding counterexamples.

**Closure condition:** identify a natural fixed chaotic map/quantization family not protected by the known conjugacies, determine the correct desymmetrized ensemble, and prove B on every compact Fourier support with the hypotheses in C. Only then can a positive BGS/GOE/COE/GUE microscopic theorem be asserted.

## E. All-members analytic resonance nondegeneracy

The generic infinite-support part is now closed substantially beyond analytic strips. `resonance-cohomology/resonance_wiener_stability.md` gives an explicit weighted-Wiener stability ball around every nonconstant real trigonometric polynomial. `resonance-cohomology/generic_wiener_resonance.md` proves that `{Gamma_A>0}` is open and dense in the natural weighted-Wiener Banach space, every fixed analytic Wiener strip, every `H^s(T^2)` with `s>2`, and `C^infinity(T^2)` with its Frechet topology. Exact zero-variance cancellations are therefore closed and nowhere dense in all of those spaces.

Two further analytic mechanisms are also closed:

1. `foundations/analytic_bracket_rigidity.md` proves

```text
{g,C_A g}=0 identically and g real analytic  =>  g constant.
```

So the separated-support pointwise-zero mechanism cannot occur for a nonconstant analytic observable.

2. `resonance-cohomology/analytic_coboundary_regularization.md` proves that an analytic zero-orbit-sum observable has an analytic cohomological transfer, with no loss of the exponent in its adapted frequency norm (and a positive strip width in ordinary coordinates). Hence any hypothetical nonconstant analytic `g` with `Gamma_A(g)=0` must satisfy

```text
{g,C_A g}/(4*pi)=u-C_A u,
{g,C_A g} != 0,
u real analytic.                                                (*)
```

A complete infinite-dimensional subfamily is now closed: for every
Fourier-line observable (g(x)=G(v\cdot x)) in the stated (H^{1+\beta})
coercive range, the 21 September theorem gives a sharp positive orbit-sum
bound and excludes an (L^2) coboundary.  In particular (H^{3/2}) positivity
holds for every such line when (|\operatorname{tr}A|\ge6).  An exact local
polynomial example simultaneously shows that fixed-point Taylor jets alone
cannot settle the global periodic equation.

The remaining question is therefore sharply reduced:

**Open question:** can the nonlinear analytic cohomological equation (*) have a nonconstant real-analytic solution `g`, or can one prove it impossible? Equivalently, is `Gamma_A(g)>0` for every nonconstant real-analytic observable?

**22 September partial closure.** The project proof in
`resonance-cohomology/finite_orbit_resonance_rigidity.md` excludes zero variance, and proves all
finite-lag independence, for every nonconstant real smooth observable whose
support is contained in finitely many signed A-orbits. Equivalently, it
covers support with bounded `abs(det(k,Ak))`. Any remaining analytic
counterexample must have infinitely many such orbits and unbounded invariant
values. The large-gap separation threshold is not uniform in the family;
no passage to arbitrary analytic support is justified by truncation alone.

The known compactly supported Gevrey counterexample is not analytic; the project's nontrivial entire temporal all-pass gauges of one harmonic are proved to lie in no finite Gevrey class. Neither resolves (*).

This question may inform perturbation theory but is not itself the missing BGS theorem.

## F. Full vanishing-noise tomography transition

For every fixed strictly noisy phase-insensitive Gaussian product channel, moment-class input tomography has logarithmic minimax risk, and the explicit pure-loss binary pair has a uniform varying-loss transition with penalty `eta^{-n}`.

**Open question:** determine the matching minimax transition for the full moment class when the physical channel noise vanishes with the copy budget. The binary-pair theorem supplies a lower-bound mechanism but is not a complete minimax characterization.

## G. Formalization depth

The active Lean tree contains finite certificates and algebraic lemmas, not formalizations of the full analytic asymptotic theorems. Native certificates have the trust boundary described in `../formalization/README.md`. The current 11 October Lean 4.33.1 receipt covers 23 active modules / 26 Lake jobs; printed axiom lists and earlier receipts remain preserved. The cavity continuation adds no analytic formalization.

**Open engineering/mathematical task:** formalize load-bearing algebraic pieces when doing so reduces proof risk, especially exact finite-support/cohomological identities and finite Cayley bookkeeping. Do not label source presence as compilation or analytic formalization.

## Engineering boundary

Julia migration is complete and is not an open mathematical task. The current computational roles are Python/SymPy for transparent exact/CAS orchestration, C++20 for independent exact/exhaustive kernels, Lean for kernel-checked finite residues, and TeX for the publication-facing proof record. GitHub-hosted workflow attempts that terminate with `steps=[]` provide no execution evidence. The pinned Lean 4.33.1 build now covers 23 active modules / 26 Lake jobs, as recorded in `formalization/README.md`; earlier smaller builds retain their own historical scope. This changes execution status, not the scope of the
formalized mathematics. Full analytic formalization remains open.

### Equivalent WKB target

[TRACE-017](fixed-map/factorial_wkb_reduction.md) permits replacing the actual complete fixed-order partition transform with either named fixed-J WKB table, J>=k. The full signed WKB comparison is an equivalent remaining target, not a weaker or solved condition. The separate [global rotated-box theorem](fixed-map/global_rotated_box_trace.md) closes the saturated-contour and summed-tail step in its explicit finite band, conservatively m<=2N. Signed evaluation of exact box sums, entropy-compatible local remainders, unrestricted bands and TRACE-005 remain open.

### Closed actual pair-commutant classification

[FM-024](fixed-map/actual_seven_primary_commutant.md), including the corrected [higher-ramified proof](fixed-map/ramified_higher_seven_commutant.md), now covers every odd N>=3 except the genuine N=7 exception by explicit combination with prior FM-008. No unknown odd-dimensional pair-commutant family remains. General seven-divisible U simplicity beyond the four certified cases, quantitative gaps, the complete literal-U complex commutant and deterministic BGS are separate questions; scalarity is asserted for the pair and only algebraic-entry commuters of literal U.

### Remaining signed complement

[TRACE-019](fixed-map/selected_weighted_coefficient.md) now controls the selected full-weight
fixed-J family. Its [exact stationary residual](fixed-map/stationary_cyclic_residual.md)
removes disjoint cyclic and homoclinic ordered pairs once; only unremoved
torsion portions remain. The complete signed residual and plateau correction,
other displacements and higher factorial orders are open. The phase-only
TRACE-018 averaged Fourier-square bound is not fixed-N time averaging.

### Exact operator residual after collective removal

[TRACE-020](fixed-map/collective_projector_residual.md) leaves
Q=(Pi-P_H-P_coll)+(I-Pi), including some cycle-fixed vectors. Its complete
signed cyclic trace is unestimated. This is distinct from the stationary-label
WKB residual. [FM-026](fixed-map/literal_time_multiplicity_bounds.md) leaves intermediate
old-layer U simplicity and quantitative gaps open.

### Remaining fixed-order mixed projector trace

The [general TRACE-020 theorem](fixed-map/factorial_ordered_diagonal.md) handles the
ordered sector for all canonical cycle lengths, zero powers and compact
fixed-order Fourier weights under flatness alone. The complete signed
Tr[R(I-P_H-P_ord)C_U] aggregation remains open. Mixed R need not commute
with the projector; no conclusion for the full balanced sector or BGS follows.

### Intermediate arithmetic layers after residual 25

[FM-026](fixed-map/literal_time_multiplicity_bounds.md) now includes the exact
[first-old classifier](fixed-map/first_old_layer_classification.md) and uniform
[residual-25 splitting](fixed-map/residual25_affine_dictionary.md). Larger even residuals
(at least 625) and odd intermediate residuals beyond 125 still require compatible bases
and their actual wild-character affine sums. The
[return obstruction](fixed-map/intermediate_return_operator.md) defeats one scalar
normalization, not every possible lattice or later cancellation. Full U
simplicity, quantitative gaps and BGS remain open.

### The current single pair residual

[TRACE-021](fixed-map/hamming_low_switch_residual.md) supplies one exact orthogonal Q
after disjoint Hamming and low-switch removal, with exponentially small pair-band
error. The task is to estimate its complete signed trace; no bound is known here.
Its centered balanced part is not a path mask, and safe translations cannot be
added again to the low-switch family. All higher fixed-order comparison remains
open. The odd arithmetic owner now includes the newest and residual-125 bridges;
the first-old odd follow-on, full simplicity and quantitative gaps remain open.


## Wave2: exact remaining signed targets

The actual unmasked q=1 one-pinch aggregate is closed at [TRACE-024](fixed-map/actual_one_pinch_disappearance.md). Complete unmasked separated and growing convex insertions are now closed at TRACE-028's exact normalizations. Masked/source-weighted insertions, occupation/Hamming/high-switch extraction and signed boundary deconvolution remain unestimated. The annealed consecutive-block leaf does not close the positive block hierarchy. [Fixed-N centering](fixed-map/ordinary_compact_stratum_centering.md) leaves N-uniform source-differentiated signed cancellation, including circle-boundary strata at ab=exp(-2s/N), open. [The corrected hook/current reduction](fixed-map/hook_tree_phase_current_reduction.md) requires N^-2 sum_m exp(-2sm/N) H_m(U_N) -> -exp(-2s)/(4s^2) for each s>0, including Heisenberg degrees, repeated occupations and the Abel tail. The required negative plateau correction is not a small-error target. Literal signed marked T16, completed-source growing-degree covariance, actual Ward overlap (13), full balanced microscopic law, higher factorial comparison, TRACE-005 and BGS remain OPEN.


## Weighted coherence boundary

[TRACE-027](fixed-map/weighted_phase_coherence_covariance.md) leaves the absorbed infinite Poisson contractions at degrees Theta(N) and above, including all mixed terms, unestimated. Its factorial bound cannot be summed termwise over that solution. Upper-half slow-window Ward convergence is not convergence at every fixed m or on the full prefix. The precise degree-two mixed-moment exception is removed for the actual operator; all fixed-degree CUE moment identification remains open.


## Wave3 current insertion frontier

The complete UNMASKED separated and convex insertion hierarchy is now closed by [TRACE-028](fixed-map/right_frame_unmasked_pinch_hierarchy.md), superseding older open wording for that complete normalized sum. Every z_N in [0,1] is included; j>=3 centered words have a uniform o(N) bound. Still open: Hamming/high-switch coefficient extraction, source weights/derivatives/rates, masked sums and marked-switch T16, signed centered deconvolution and the undamped zero-insertion spectral difference. [TRACE-029](fixed-map/convex_pinch_weak_noise_and_deconvolution.md) proves complete signed bounded-u stability only. Its actual unsigned large-log divergence comes from the retained identity contribution and does not refute T16; cancellation must be maintained before absolute estimates. Balanced law, Ward(13), TRACE005, higher factorial comparison and BGS remain OPEN.


### Operator approximation route and its boundary

[TRACE-116](trace-bridge/microscopic_unitary_stability_20261027.md) reduces the compact pair test to any explicitly controlled matrix approximant with $O(N^{-2})$ norm error. The missing step is a tractable approximant with a proved CUE pair limit; the theorem does not supply it. Higher factorial orders require their own estimates.

[TRACE-114](fixed-map/balanced_rounding_research_20261027.md) shows that absolute short-trace agreement through $N^\gamma$, $\gamma<1/2$, and the same eigenvectors do not identify a weak local law for a general quantizer. It does not preserve the exact kicked-family identity. The [disposition review](../record/trace005_continuation_review.md) tracks the remaining intensity, dispersion, arithmetic and gauge candidates without treating them as current theorem inputs.

[TRACE-117](fixed-map/kick_blind_arithmetic_spike.md) shows that the fixed kick preserves the cat-map Abel spike on \(N=u_n\) for every odd \(n\) with \(5\le n\le201\). No threshold \(N_0\le u_{201}\) can start an effective statement that the Abel gap is less than \(1/2\) for every larger odd dimension. The one-term estimate stops being conclusive at \(n=203\).

[TRACE-118](fixed-map/orbit_orthogonal_kick_spike.md) passes that index by a different estimate. At \(N=u_{203}\) the orbit of the \(32\) Fourier modes is trace-orthogonal except for one overlap of size \(7/10^6\), and \(L_N(U_N;1)>3/4\). The threshold for an effective gap below \(1/2\) on every larger odd dimension is now \(N_0>u_{203}\). The third-order operator-norm remainder and the Hilbert--Schmidt triangle are already silent at \(n=205\). At \(n=207\) the pure second-order center lies below \(3/4\). Signed cancellation on the remaining dimensions, and the limit, stay open.

[TRACE-119](fixed-map/positive_time_spike.md) passes \(n=205\) by another estimate. A positive-time expansion, using the same trace orthogonality, gives \(L_N(U_N;1)>3/4\) at the single dimension \(N=u_{205}\). The effective threshold is now \(N_0>u_{205}\). The \(n=207\) obstruction is unchanged: \((1-\varepsilon_2)^2<3/4\), so no nonnegative remainder about that center proves the gap. The limit, a generic odd dimension, and BGS-TRACE-005 stay open.

[TRACE-120](fixed-map/order_ladder_abel.md) does not cross that disk. It proves a different statement: the order \(t(N)\) of \(C\) modulo \(N\) places the pure cat map above \(3/4\) when \(12t(N)\le5N\), and places every odd prime with \(2t(p)\ge p+1\) within distance \(1/2\) of the CUE value. The fixed kick preserves those two sides through \(N\le10^{39}\) and \(p\le10^{26}\) respectively. Orders strictly between \(5N/12\) and \((N+1)/2\), the kicked dimension \(u_{207}\), the limit, and BGS-TRACE-005 stay open.

[TRACE-121](fixed-map/order_trichotomy_abel.md) closes that interval for primes and prime powers. Every odd prime order divides \(p-\varepsilon\) and is short, long, or split-half; \(p=7\) is above \(3/4\) and every larger split-half prime is below \(5/7\). The lifting depth decides every \(p^k\). The pure map at every odd Pell dimension \(n\ge5\), including \(u_{207}\), is already above \(3/4\) because the order divides \(n\). [TRACE-122](fixed-map/crt_composite_abel.md) multiplies the trace square over prime-power factors and decides every product of two odd primes. Short composite orders and non-short multiples of \(7\) lie above \(3/4\). Every product of \(3\) with a short prime is short, and every remaining semiprime lies below \(5/7\). The fixed kick preserves the gap above \(3/4\) through \(10^{26}\) on \(N=21\). A split full-order multiple of \(7\) does not occur. [TRACE-123](fixed-map/squarefree_product_abel.md) places every square-free product of at least three distinct odd primes above \(3/4\). The fixed kick preserves that gap through \(10^{39}\) when \(N\) has at least four prime factors or is a product of three primes not divisible by \(15\), and through \(10^{26}\) when \(N=15r\). [TRACE-124](fixed-map/odd_modulus_abel.md) places every odd modulus above \(3/4\) or below \(5/7\). The modulus \(315\) is short because its radical \(105\) is short. The fixed kick preserves the upper gap when \(8t(N)\le3N\) and \(N\le10^{39}\), through \(10^{26}\) on the ratio-preserving families whose pure margin exceeds \(13/420\), and through \(2\cdot10^{26}\) on \(N=15r\). Still open: the kick on a ceiling tower, including the gap \(575/22594<13/420\) at \(3\cdot23\); the kick on an inert exponent-one partner \(q\ge40\); the kick on \(15r>2\cdot10^{26}\); the kick at \(u_{207}\); any density of the three classes; the off-diagonal sum; the limit; and BGS-TRACE-005.

[TRACE-125](fixed-map/uniform_orbit_overlap.md) is the uniform overlap law, not another Abel window. For every odd \(n\ge5\), at \(N=u_n\), the symbol overlap \(\gamma(r)\) vanishes for \(1\le r\le n-1\) except at \(r=1\) and \(r=n-1\), where it equals \(-7/2000000\). The quadratic coefficient of the transported product is exactly \(n\cdot1650797/4000000\). The sequence \(u_n\) is exponential. The index \(n=5\) is a finite scan of the middle lags; every larger odd index is the size, archimedean, and quadratic-form argument. This fixes \(f''(0)\), not \(f(1)\). The [strategy note](fixed-map/offdiagonal_strategy.md) records methods that stop at the linear cat map. BGS-FM-032 is an additive, linearized distance for odd primes \(p>99\); it does not identify the eigenvalues of \(U_N\). A separation of \(L_N(U_N;1)\) from the CUE value is a bound on the whole Abel sum. The third-order remainder, the Heisenberg-time signed sum, the limit, and BGS-TRACE-005 stay open. Section 7 of the strategy note ranks the concrete \(U_N\) problem first and the generalizations second. The signed sum at times of order \(N\) is not within reach of the methods now proved. A finite symmetry test of this symbol is the realistic concrete step. A sharper pure-map gap is not that step.
