# BGS — quantum chaos and spectral universality

[Русский](README.ru.md) · [Research overview](RESEARCH.md) · [Corpus atlas](docs/corpus_atlas.md) · [Mathematical introduction](docs/reader_guide.en.md) · [Theorem index](mathematics/results.md) · [Complete manuscript](manuscript/README.md)

The **Bohigas–Giannoni–Schmit conjecture** is a central question in quantum chaos: under appropriate dynamical and symmetry conditions, why should the microscopic energy-level statistics of deterministic chaotic systems agree with random-matrix theory? This repository develops exact mathematics, counterexamples, and reproducible verification around this question, especially for one explicitly specified quantum torus map.

**Scientific status (22 October 2026):** The microscopic BGS limit for the fixed deterministic map below is **open**. Several related theorems have project proofs in their precisely stated regimes; none is a proof of universality for all chaotic systems. The [22 October repository review](record/audits/repository_recheck_20261022/report.md) records its exact verification scope. [Registered status](record/claims.json) · [Open proof obligations](mathematics/open_questions.md).

**Kick-blind spikes (28 October 2026).** On the pure cat map, every odd return $n\ge5$ at dimension $N=u_n$ keeps the Abel pair statistic a distance greater than $1/2$ from the CUE value. The fixed kick $\tau=10^{-80}$ preserves that gap at each of the 99 odd indices $5\le n\le201$, including the 77-digit dimension $u_{201}$. This is [BGS-TRACE-117](mathematics/fixed-map/kick_blind_arithmetic_spike.md). The next odd index $n=203$ is settled by a second-order expansion: the cat-map orbit of the symbol is trace-orthogonal up to one explicit overlap, and [BGS-TRACE-118](mathematics/fixed-map/orbit_orthogonal_kick_spike.md) gives the same gap at the 78-digit dimension $u_{203}$. The next odd index $n=205$ is settled by a positive-time expansion that keeps trace orthogonality: [BGS-TRACE-119](mathematics/fixed-map/positive_time_spike.md) gives the same gap at the 79-digit dimension $u_{205}$. At $n=207$ the pure second-order center still satisfies $(1-\varepsilon_2)^2<3/4$, so that disk cannot prove the gap. The order of $C$ modulo $N$ splits the same statistic: [BGS-TRACE-120](mathematics/fixed-map/order_ladder_abel.md) puts every odd dimension with $12t(N)\le5N$ strictly above $3/4$, and puts every odd prime whose order is at least half the dimension within distance $1/2$ of the CUE value. The fixed kick preserves the short side through $10^{39}$ and the long side through $10^{26}$. The dimension $N=35$, of order $6$, is not a Pell number, and one return there lies below $3/4$. [BGS-TRACE-121](mathematics/fixed-map/order_trichotomy_abel.md) closes the remaining prime orders: every order divides $p-\varepsilon$ and is short, long, or split-half, the prime $p=7$ lies above $3/4$, and every larger split-half prime lies below $5/7$. The same depth decides every prime power. The pure map at $u_{207}$ is already above $3/4$, because its order divides $207$. None of these results proves the limit or the kicked gap at $u_{207}$. [BGS-TRACE-122](mathematics/fixed-map/crt_composite_abel.md) multiplies the trace square over the prime-power factors of every odd modulus and decides every product of two odd primes: short composite orders and the seven-family lie above $3/4$, and every remaining semiprime lies below $5/7$. The fixed kick preserves that upper gap through $10^{26}$ on $N=21$. A split full-order window and a non-short product of $3$ with a short prime do not occur. [BGS-TRACE-123](mathematics/fixed-map/squarefree_product_abel.md) places every square-free odd modulus with at least three distinct prime factors strictly above $3/4$. The fixed kick preserves that gap through $10^{39}$ when there are at least four prime factors or the modulus is a product of three primes not divisible by $15$, and through $10^{26}$ on $N=15r$. A prime square such as $315=3^2\cdot5\cdot7$ is outside that statement. [BGS-TRACE-124](mathematics/fixed-map/odd_modulus_abel.md) places every odd modulus strictly above $3/4$ or strictly below $5/7$; $315$ is short because its radical $105$ is short. The fixed kick preserves the upper gap when $8t(N)\le3N$ and $N\le10^{39}$, through $10^{26}$ on the ratio-preserving families whose pure margin exceeds $13/420$, and through $2\cdot10^{26}$ on $N=15r$. The kick is not claimed for a ceiling tower, for an inert partner $q\ge40$ at exponent one, for $15r>2\cdot10^{26}$, or at $u_{207}$. [BGS-TRACE-125](mathematics/fixed-map/uniform_orbit_overlap.md) gives the quadratic trace coefficient of the transported product at every odd Pell return $n\ge5$: $Tr(S^2)/N=n\cdot1650797/4000000$. The dimensions $u_n$ form an exponential sequence. This coefficient is the second derivative at zero coupling, not a bound on $f(1)$, and it does not decide the eigenvalues of $U_N$. The [strategy note](mathematics/fixed-map/offdiagonal_strategy.md) is not a theorem. The density of the order classes and the signed off-diagonal sum stay open. BGS-TRACE-005 and BGS-BGS-001 remain open.

**Random-phase encounter pairs (29 October 2026).** For $U=D\cdot M_p$ with Haar diagonal $D$ and $S=\begin{pmatrix}3&4\\2&3\end{pmatrix}$, [BGS-TRACE-143](mathematics/fixed-map/random_phase_encounter_pairs.md)–[146](mathematics/fixed-map/random_phase_encounter_pairs.md) give, for each fixed $m$ and every prime $p>4^m$, an exact identity $E|\mathrm{Tr}\,U^m|^2=\sum_k a_{m,k}(p)p^{-k/2}$ with $a_{m,0}=2m$, $a_{m,1}=0$, $a_{m,2}=-2m^2$ ($m\ge5$). The coefficient of $1/p$ is $-2m^2$ for every $m\ge 5$. Gnutzmann–Seif 2004 derived $2\tau-2\tau^2$ diagrammatically for this ensemble, Gnutzmann–Altland 2005 and Pluhař–Weidenmüller 2014 predict the full COE form factor non-rigorously, and Berkolaiko–Keating 1999 did exact all-pairs combinatorics for random-phase star graphs; new here is only the rigorous fixed-$m$ exact-in-$p$ result, the complete classification including swaps, and the $m\le 12$ expansions. [BGS-TRACE-147](mathematics/fixed-map/random_phase_encounter_pairs.md) records the computer-assisted expansions through $m=12$, including the fixed-$m$ deviation from the COE $\tau^3$ value at $m=5,6,8,9,12$. An independent referee engine reproduces every coefficient at $171$ primes; the claim stays verification-pending, and promotion is a separate status decision, as for BGS-RES-022. [BGS-TRACE-148](mathematics/fixed-map/random_phase_encounter_pairs.md) is the open scaling-limit conjecture. The values at $m=1,2,3$ are BGS-TRACE-127 and are not re-claimed. This does not prove BGS-TRACE-005 or BGS-BGS-001, and it does not cover the fixed kick.

**Band-limited random kicks (29 October 2026).** For $U=e^{i\eta V_\theta}M_N$ with a fixed finite set of random cosine modes, [BGS-TRACE-149](mathematics/fixed-map/band_limited_kick_bridge.md)–[151](mathematics/fixed-map/band_limited_kick_bridge.md) prove the exact bridge $E|\mathrm{Tr}\,U^m|^2=\Psi_m(t_N)$ for every odd $N$ with $\gcd(N,D_m)=1$, its $1/N$ expansion with residue period $g'_m$ (not uniform in $\eta$ or $K$), and the orbit-pair form over period-$m$ solutions of $q_{j+1}+q_{j-1}=6q_j$; these are Line B's Theorem 1 applied for each kick realisation and the Boasman–Keating mechanism, not new. [BGS-TRACE-152](mathematics/fixed-map/band_limited_kick_bridge.md) proves that under separation of dihedral classes the strong-kick limit is $B_m^{\mathrm{sym}}$ at every residue, and [BGS-TRACE-154](mathematics/fixed-map/band_limited_kick_bridge.md) that $B_m^{\mathrm{sym}}<2m$ for every odd $m$; the instances $m\le7$ are verification-pending ([BGS-TRACE-153](mathematics/fixed-map/band_limited_kick_bridge.md)) and even $m$ is open ([BGS-TRACE-155](mathematics/fixed-map/band_limited_kick_bridge.md)). [BGS-TRACE-157](mathematics/fixed-map/band_limited_kick_bridge.md) shows the $1/N$ coefficient is odd in the residue, so it is not $-2m^2$ uniformly in $N$; its decay is conditional and Gaussian-only ([BGS-TRACE-158](mathematics/fixed-map/band_limited_kick_bridge.md)), and open for uniform phases ([BGS-TRACE-159](mathematics/fixed-map/band_limited_kick_bridge.md)). [BGS-TRACE-160](mathematics/fixed-map/band_limited_kick_bridge.md) transfers Line C (BGS-TRACE-146) to the full band up to $p^me^{-cp}$; the intermediate band and the crossover scaling are open ([BGS-TRACE-161](mathematics/fixed-map/band_limited_kick_bridge.md), [162](mathematics/fixed-map/band_limited_kick_bridge.md)). On main at d6fa6e2a the next free TRACE identifier was 149, so this block is registered as BGS-TRACE-149 through BGS-TRACE-162; the Line B packet had not merged. This does not prove BGS-TRACE-005 or BGS-BGS-001, and it says nothing about eigenvalue statistics beyond the second moment of $\mathrm{Tr}\,U^m$ at fixed $m$.

**Resonant residues of the fixed kick (30 October 2026).** At the residues N ≡ −4 (mod h_m), the Pell phase of Line B collapses exactly ([BGS-TRACE-183](mathematics/fixed-map/resonant_residue_lineE.md)). Z_m is then the trace of m-independent IFS transfer operators ([184](mathematics/fixed-map/resonant_residue_lineE.md)). For the single-cosine kick 0.9 cos 2πq, the leading eigenvalue is certified (185–186), and |W̃rest_m| > m is proved for odd m ∈ [17,39] at η = 2 ([187](mathematics/fixed-map/resonant_residue_lineE.md), computer-assisted). This is the k1-kick analogue of Conjecture R, not R itself. Not yet refereed: the a²-resonance law, which gives a 49-state law for the Line B kick at N ≡ ∓196 when 3 ∤ m ([194](mathematics/fixed-map/resonant_residue_lineE.md)); rigorous bounds for the Line B kick at m = 11 and 13 (m = 17 certificate pending) ([195](mathematics/fixed-map/resonant_residue_lineE.md)); and a conditional asymptotic failure of R along 3 ∤ m ([196](mathematics/fixed-map/resonant_residue_lineE.md)). TRACE-179 (Conjecture R), 180 and 182 stay open.

**Fixed diagonal kick (29 October 2026).** Line B is the fixed-$m$, fixed-kick derandomized analogue of the random-phase short-time results, for $U=K_\eta M_N$ with the diagonal part of the repository kick. Proved: [BGS-TRACE-163](mathematics/fixed-map/derandomized_fixed_kick.md), [BGS-TRACE-165](mathematics/fixed-map/derandomized_fixed_kick.md), [BGS-TRACE-166](mathematics/fixed-map/derandomized_fixed_kick.md), [BGS-TRACE-167](mathematics/fixed-map/derandomized_fixed_kick.md), [BGS-TRACE-168](mathematics/fixed-map/derandomized_fixed_kick.md), [BGS-TRACE-169](mathematics/fixed-map/derandomized_fixed_kick.md), [BGS-TRACE-170](mathematics/fixed-map/derandomized_fixed_kick.md), [BGS-TRACE-171](mathematics/fixed-map/derandomized_fixed_kick.md), [BGS-TRACE-172](mathematics/fixed-map/derandomized_fixed_kick.md), [BGS-TRACE-173](mathematics/fixed-map/derandomized_fixed_kick.md), [BGS-TRACE-175](mathematics/fixed-map/derandomized_fixed_kick.md), [BGS-TRACE-178](mathematics/fixed-map/derandomized_fixed_kick.md). Conditional: [BGS-TRACE-164](mathematics/fixed-map/derandomized_fixed_kick.md), [BGS-TRACE-174](mathematics/fixed-map/derandomized_fixed_kick.md), [BGS-TRACE-176](mathematics/fixed-map/derandomized_fixed_kick.md). Open: [BGS-TRACE-177](mathematics/fixed-map/derandomized_fixed_kick.md) (numerical-only), [BGS-TRACE-179](mathematics/fixed-map/derandomized_fixed_kick.md), [BGS-TRACE-180](mathematics/fixed-map/derandomized_fixed_kick.md), [BGS-TRACE-181](mathematics/fixed-map/derandomized_fixed_kick.md), [BGS-TRACE-182](mathematics/fixed-map/derandomized_fixed_kick.md). BGS-TRACE-173 is proved only with the directed-rounding constants; the authors' float constants are excluded. Nothing is proved at τ = m/N = O(1). All results are fixed-m (diagonal / below Ehrenfest). This is not progress on BGS-BGS-001 or BGS-TRACE-148. "B_m → 2m" is not claimed. Theorem N covers a finite list of certified NSW primes, and the infinitude of NSW primes is open. The Theorem D_cert arithmetic is IEEE float with an a-priori error bound (plus arb coefficients), not full interval arithmetic, until the full directed-rounding rerun. (Second-reader annotation, not part of the referee's verbatim text: that rerun has now been done, 93/93; non-claim 8 still applies to the authors' float grid, and BGS-TRACE-173 is proved with the directed-rounding constants only.) On main at 502af245 the highest registered TRACE id was BGS-TRACE-162, so BGS-TRACE-163 was the next free id and the block was not renumbered.

**Unitary short-time value for momentum phases (29 October 2026).** [BGS-TRACE-140](mathematics/fixed-map/momentum_phase_cue.md) proves that Haar phases in position and in momentum give $E|\mathrm{Tr}\, U^m|^2\to m$ for each fixed $m\ge 3$, on odd primes with $\delta\not\equiv -1$, with an explicit error of order $(m!)^2/p$. The same window reaches $m\le c\log p/\log\log p$ for $c<1/2$. [BGS-TRACE-141](mathematics/fixed-map/momentum_phase_cue.md) gives the moment limit $k!\,m^k$. [BGS-TRACE-142](mathematics/fixed-map/momentum_phase_cue.md) identifies the Gaussian main term $m(1+e^{-vm})$; the non-injective remainder is not bounded, so the limit is verification-pending. The odd part of the maintained symbol has energy $9/125000$. This is not the fixed kick and not the sixteen-phase ensemble. BGS-TRACE-005 and BGS-BGS-001 remain open.

**Fixed-time limits (29 October 2026).** [BGS-TRACE-132](mathematics/fixed-map/hyperbolic_short_time_limit.md) gives the fixed-time limits for every hyperbolic matrix. Haar diagonal phases tend to $2m$ for each $m\ge 3$, with an explicit error. The antiunitary $\Theta'=DEK_0$ reverses $DM_N$ for every such matrix. A finite cosine with $\eta=o(N^{-2/3})$ tends to $1$ along odd $N$ coprime to $\beta(2-u_m)$, along $N$ divisible by $7$ (e.g. $35,77,91,707$) the time-$3$ kernel has order at least $49$, so the limit $1$ fails when $\gcd(N,\beta(2-u_m))>1$. Sending $\eta\to\infty$ first, with frequencies $1$ through $m$ present, recovers $2m$. Row inversion tends to $m$. A momentum sine is not identified, and the orthogonal-class name remains a heuristic for $\Theta'$. BGS-TRACE-005 and BGS-BGS-001 remain open.

**Revival closure law (29 October 2026).** [BGS-TRACE-133](mathematics/fixed-map/revival_closure_law.md)–[135](mathematics/fixed-map/revival_closure_law.md) prove, for the position-diagonal kick ($\sigma_d=13203/32000$), the twisted closure formula, a pointwise bound at the scalar return with its limit along the Bonechi–De Bièvre minimal-period sequence, and the half-period parity reduction. The explicit bound of BGS-TRACE-134 gives no information at any computable $N$: at $\lambda=1/4$ it first drops below $1$ near $N\approx 10^{191}$, so only the limit is proved. [BGS-TRACE-136](mathematics/fixed-map/revival_closure_law.md) and [BGS-TRACE-137](mathematics/fixed-map/revival_closure_law.md) are open conjectures for even and odd order; Monte Carlo rows are diagnostics only. BGS-TRACE-005 and BGS-BGS-001 remain open.

**Hyperbolic diagonal form factor (29 October 2026).** [BGS-TRACE-131](mathematics/fixed-map/hyperbolic_diagonal_form_factor.md) extends the phase average from one cat map to every hyperbolic matrix in $\mathrm{SL}(2,\mathbb Z)$. For odd $N$ coprime to the upper-right entry, the quantization is unitary and flat, and symmetric exactly when the diagonal entries agree modulo $N$. The antiunitary $\Theta'=DEK_0$ reverses the kicked propagator for every such matrix. A finite cosine kick has phase average $|\ker|+\eta^2 D_2+\rho$, with an explicit remainder. The prime kernel is read from the trace when the prime does not divide that entry. At an identity revival the second-order coefficient is $-m(\sigma-\sigma_0)p^2$. This is not the all-order revival law and not a fixed-time limit. BGS-TRACE-005 and BGS-BGS-001 remain open.

**Local antiunitary for a position-diagonal kick (29 October 2026).** [BGS-TRACE-130](mathematics/fixed-map/sixteen_phase_symmetry.md) proves that for every real diagonal kick, including every position-diagonal realization, the antiunitary $\Theta=DK_0$ satisfies $\Theta^2=1$ and $\Theta U\Theta^{-1}=U^\dagger$. The orthogonal-class name is the heuristic for that antiunitary. It is not a COE form factor, and it does not exclude a CUE form factor. Each of the rows $\ell=\pm 1$ has energy $9/160000$, with $4000 c_{1,k}=(-3-4i)r(k)$. The full symbol fails to be real for almost every phase. The momentum sine has symbol energy $1/2$ and leaves the antiunitary argument. BGS-TRACE-005 and BGS-BGS-001 remain open.

**Scalar-return orbit sum (29 October 2026).** [BGS-TRACE-129](mathematics/fixed-map/scalar_return_bessel.md) gives the phase average of the classical orbit sum for a position-diagonal kick at a return $S^m\equiv I$. That identity is not the quantum sixteen-phase average. The average is a product of Bessel factors $J_0$. Its degree-two jet is $\exp(-m\sigma_{\mathrm{diag}}\eta^2)$. The degree-four gap is an additive count on the position orbit, and the exponential is not an identity at $\eta^2\sigma m$ of order one. Time one equals $1+\rho_1$ inside the perturbative window. Each of the rows $\ell=\pm 1$ has energy $9/160000$. A referee sample differs from the classical average by ≈1.7 at $N=11$ and by up to ≈6 at $N=29$ ($\eta=2$). No COE or CUE limit is proved. BGS-TRACE-005 and BGS-BGS-001 remain open.

**Short-time diagonal-phase limits (29 October 2026).** [BGS-TRACE-128](mathematics/fixed-map/diagonal_phase_short_time.md) gives the fixed-time limit of the cat map times independent uniform phases on the $N$ position sites. For each $m\ge 3$ the averaged squared trace tends to $2m$, with an explicit gap from the dihedral main term. Inverting the rows by $x\mapsto x^{-1}$ on an odd prime changes the limit to $m$. Neither bound reaches a power of $N$. This is not the sixteen-phase ensemble and not the fixed kick. BGS-TRACE-005 and BGS-BGS-001 remain open.

**Diagonal random-phase form factor (29 October 2026).** [BGS-TRACE-127](mathematics/fixed-map/diagonal_phase_form_factor.md) gives the exact averaged squared trace of the cat map times independent uniform phases on the $N$ position sites, at times one, two and three, together with the bound $m!$ at every time. The pure kernel is $1$ at time two and is $49$ or $1$ at time three according as $7$ divides the odd modulus. The time-three limit is $6$, not the CUE value $3$. This is not the sixteen-phase ensemble and not the fixed kick. BGS-TRACE-005 and BGS-BGS-001 remain open.

**Phase-averaged form factor (29 October 2026).** For the auxiliary ensemble in which the 16 mode pairs of the kick carry independent uniform phases, [BGS-TRACE-126](mathematics/fixed-map/interaction_phase_form_factor.md) gives the exact order-two expansion of the averaged squared trace, with an explicit Gauss-sum coefficient and an operator-norm remainder. At an odd prime $p$ the second-order revival coefficient is $-m(\sigma-\sigma_0(p))p^2$, where $\sigma_0(p)$ is the energy of the symbol modes congruent to $0$ modulo $p$: $\sigma_0(3)=81/64000$, $\sigma_0(5)=1/320000$, $\sigma_0(7)=81/200$, and $\sigma_0(p)=0$ for every prime $p\ge 11$. The fixed kick has a linear term, nonzero at $N=11$, $m=3$. Parity and position-basis conjugation fail for the kicked propagator when $0<|\eta|<\pi/B$, except at dimension $7$, where $A_7=(9/10)I$. No revival limit is proved. BGS-TRACE-005 and BGS-BGS-001 remain open.

![BGS research logic: exact model, proved reductions, and outstanding signed spectral comparison](assets/figures/bgs_frontier.svg)

*Research map, not a chain of proved implications: the final arrow is the missing mathematical step.*

*GPT 6 and Muse Spark 1.3 were used for repository work, verification, and code implementation.*

## What the conjecture asks

Bohigas, Giannoni and Schmit's [1984 paper](https://doi.org/10.1103/PhysRevLett.52.1) connected chaotic quantum spectra with universal random-matrix fluctuations. A rigorous theorem needs a specified quantum family, the correct symmetry sector, a justified unfolding, and a local correlation limit. Classical hyperbolicity alone does not automatically guarantee a particular symmetry class or a universal spectrum.

For unitary-class spectra, the reference point process is $\mathrm{Sine}_2$, whose determinantal kernel and distinct-point two-point correlation are

```math
K(x,y)=\frac{\sin\pi(x-y)}{\pi(x-y)},
\qquad
\rho_2(x,y)=1-|K(x,y)|^2.
```

![Analytic Sine2 two-point function and Poisson reference](assets/figures/microscopic_pair_reference.svg)

*Analytic benchmark curves, **not measured data** from the deterministic map. The figure depicts pair correlation, not the nearest-neighbour spacing distribution.*

## The exact model and target

For odd $N\ge3$, the maintained family is

```math
S=\begin{pmatrix}3&4\\2&3\end{pmatrix},
\qquad
U_N=\exp(i\tau N A_N)M_N,
\qquad
\tau=10^{-80}.
```

Here $M_N$ is the specified quantization of the hyperbolic cat map, and $A_N$ the specified Weyl-quantized nonlinear kick. [The canonical model source](mathematics/fixed-map/fixed_map_resolvent_frontier.md) fixes conventions, exceptional dimensions, and symmetry questions. **The coupling remains fixed as $N\to\infty$**; replacing it with vanishing coupling, independent random phases, or noise changes the problem.

The following pair-moment reference in the prescribed trace hierarchy remains unproved for this family. Weak convergence to Sine₂ alone does not imply convergence of these unbounded pair moments without additional uniform-integrability control:

```math
L_N(s)=\frac{1}{N^2}\sum_{m\ge1}e^{-2sm/N}
\left|\mathrm{Tr}\,U_N^m\right|^2
\;\longrightarrow\;
\frac{1-e^{-2s}}{4s^2},
\qquad s>0.
```

The full [BGS-TRACE-005 obligation](mathematics/open_questions.md#b-prove-heisenberg-scale-desymmetrized-joint-trace-estimates) is stronger: correctly desymmetrized **signed factorial joint-trace comparison** for every fixed order and every compactly supported smooth Fourier test, at powers $m\asymp N$. The absolute value is taken **after the complete Fourier sum**, rather than term by term. The [trace-to-local-statistics bridge](mathematics/trace-bridge/trace_to_local_statistics_bridge.md) explains the further tightness/extension conditions.

The [operator-resolution continuation](mathematics/trace-bridge/microscopic_unitary_stability_20261027.md) transfers the original-family pair test through $O(N^{-2})$ matrix error using TRACE-113; it does not determine that limit. The complementary [short-trace barrier](mathematics/fixed-map/balanced_rounding_research_20261027.md) shows why polynomially many short traces and coarse quantum data alone are insufficient for a general quantizer. The [review](record/trace005_continuation_review.md) separates these author-checked proofs from prior results and remaining candidates.

## What else is established, and what is missing

The programme contains independently distinguishable lines of work:

| Mathematical layer | Established in its stated scope | Not yet established |
|---|---|---|
| Spectral-to-trace bridge | Exact finite-dimensional combinatorics and conditional correlation criteria | Required model-specific signed joint-trace estimates |
| Actual map: intensity and paths | [FM-021](mathematics/fixed-map/position_chain_mixing.md) intensity mixing and cyclic ramp; [FM-022](mathematics/fixed-map/reversed_path_decay.md) reverse-path decay | All remaining coherent interference, including the negative plateau correction |
| Balanced microscopic analysis | [Phase Ward](mathematics/trace-bridge/phase_ward_identity.md) and [Schur-energy](mathematics/trace-bridge/balanced_pair_schur_reduction.md) exact identities | Their requisite absorbed overlap / microscopic radial limits |
| Traces and insertion calculus | Selected [WKB](mathematics/fixed-map/factorial_wkb_reduction.md), [ordered-diagonal](mathematics/fixed-map/factorial_ordered_diagonal.md), and [unmasked](mathematics/fixed-map/right_frame_unmasked_pinch_hierarchy.md) sectors | Complete high-switch signed remainder, masks and endpoints |
| Stochastic comparison | [FLOW-014](mathematics/fixed-map/circular_dyson_actual_start.md) and [FLOW-017](mathematics/fixed-map/coboundary_all_order_limit.md) noisy local laws on explicitly stated schedules | Removal of the noise for the original deterministic family |
| Other mathematics | [Cayley](mathematics/topics/cayley-arithmetic/README.md), [Pell](mathematics/topics/pell/README.md), [return](mathematics/topics/returns/README.md), resonance, locality and information results | A proved implication from their separate regimes to deterministic BGS |
| Lean formalization | The [Mathlib coverage map](formalization/MATHLIB_LAYER_RU.md) ties 29 existing and 39 adapted modules to precisely scoped finite, algebraic and selected scalar/reference results; a historical receipt records axiom checks of 589 declarations | The full analytic trace hierarchy and deterministic BGS limit |

The decisive obstacle is not a shortage of finite-dimensional identities: it is **controlled cancellation of signed Heisenberg-scale contributions** for the unchanged propagator. Neither a numerical spacing plot nor a result for a randomized auxiliary model closes that gap. Consult the [research brief](RESEARCH.md) for precise scope and [obligation board](mathematics/open_questions.md) for the remaining work.

### Why the signed plateau matters

For a Haar-distributed $V_N$ in the circular unitary ensemble, the exact positive-power reference is

```math
\mathbb E_{\mathrm{CUE}}\left|\mathrm{Tr}\,V_N^m\right|^2
=\min(m,N),\qquad m\ge1.
```

The cyclic linear term has normalized shape $x=m/N$, whereas the CUE reference is $\min(x,1)$. Above $x=1$, their difference is **$1-x<0$**. Thus reproducing a cyclic ramp alone cannot establish the required plateau: the remaining coherent, signed path contributions must supply a negative correction in aggregate. This is a necessary target, **not** a result already proved for the deterministic family.

![Exact CUE reference: ramp, plateau and the negative residual required above Heisenberg time](assets/figures/trace_ramp_plateau.svg)

*Analytic comparison (no simulation). The shaded region is the magnitude of the negative correction required relative to the cyclic linear contribution.*

## Recent results and their boundaries

The latest fixed-map results have project proofs with explicit time and scale limits:

| Result | Established scope | Boundary |
|---|---|---|
| [Inserted trace, TRACE-109](mathematics/fixed-map/finite_grid_one_step_trace.md) | Finite-grid corrected amplitude; inserted trace error $O(N^{-1})$ | Selected insertion, not the full signed hierarchy |
| [Spectral distance, TRACE-110](mathematics/fixed-map/spectral_orbit_distance.md) | Global $O(1/\log N)$ matching; matching lower order along Pell dimensions | Macroscopic matching does not imply microscopic statistics |
| [Displacement density, TRACE-112](mathematics/fixed-map/displacement_density_trace_bound.md) | Uniform classical density control and an independent logarithmic-time trace route | No Heisenberg-time cancellation |
| [Uniform power trace, TRACE-113](mathematics/fixed-map/fixed_kick_uniform_trace_bound.md) | $|\mathrm{Tr}\,U_N^m|\le Ca^m$, $1<a<\sqrt{3+2\sqrt2}$, with one size threshold for all $m$ | The bound is uninformative at $m\asymp N$ |

The [fourteen-round research edition](mathematics/spectral_research/README.md)
preserves 535 supplied source units with thematic reading paths and a
[standalone remaining task](record/remaining_breakthrough_task_20261021.md).

The auxiliary phase ensemble uses a Fourier seed of dimension $N=p^{2d}$,
odd prime $p$, and independent uniform phases. Its scaled trace time
$t=m/N$ is separate from the fixed kick strength in the deterministic model.

| Theorem family | Established scope | Remaining implication |
|---|---|---|
| [Signed phase cluster sums](mathematics/trace-bridge/phase_ensemble_continuation.md) | Author proofs, registered verification pending: total-defect-two sum for $0<t<1$; arbitrary counts of clusters of individual defects at most two for $0<t<1/9$, with uniform $O(N^{-1})$ error | Higher connected types and frozen-model transfer |
| [Positive Cauchy projections](mathematics/trace-bridge/cauchy_positive_source_boundary.md) | Author proofs, registered verification pending: exact scalar laws and explicit separation of full matrix laws | Positive projections alone do not identify the spectral law |
| [Abel clock rigidity](mathematics/trace-bridge/abel_clock_rigidity.md), [flat collision law](mathematics/trace-bridge/wick_collision_poisson.md) | Sharp square-root stability and auxiliary Wick ratio $B/G\to e^{-\alpha^2}$ | Physical non-flat signed comparison |
| [All-order process implication](mathematics/trace-bridge/all_order_process_closure.md) | Complete signed hierarchy implies local Sine2 and local moment control | The physical hierarchy remains open |
| [Full-depth feedback](mathematics/trace-bridge/unconditional_feedback_flatness.md) | Entry/intensity bounds and fixed-order clocks under named startup inputs and cutoff | Initial microscopic law and signed transfer |

The rows distinguish proved project results from deposited author proofs whose
registered verification is pending. Consult the [complete registry](record/claim_registry.md)
for each state and its exact boundary.
The Gaussian benchmark is classical; external priority is not established.
[Detailed research brief](RESEARCH.md) · [Review history](record/README.md) ·
[Repository reconciliation](record/audits/repository_recheck_20261022/report.md).

## Three reconstructed analytic results

**Phase memory with reused coordinate phases — [BGS-TRACE-053](mathematics/trace-bridge/max_entry_phase_channel.md).**
For $S\in U(m)$, set $P_{ij}=|S_{ij}|^2$, $\delta=\max P_{ij}$,
$A=\Pi\mathrm{Ad}(S)$, and
$T_n=\mathbb E_D\mathrm{Ad}((DS)^n)$. Here $\Pi$ is diagonal pinching
and the same independent uniform diagonal phases $D$ are reused in every power.
$J_m$ has every entry $1/m$.
On the full complex Frobenius space, for $n\ge2$,

$$\|T_n-A^n\|_{2\to2}
\le(n!-1)\sqrt\delta+n!n(n-1)\delta.$$

The degree-two norm is exactly $\max_{i\ne j}|S_{ij}S_{ji}|\le\delta$.
If $\|P-J_m\|\le\rho<1$, averaged eigenspace pinching on traceless matrices
has norm $O_\rho(\log\log(1/\delta)/\log(1/\delta))$ as $\delta\to0$.
This operator-norm conclusion does not evaluate a microscopic spectral trace.

**Optimal matrix inner-function jets — [BGS-TRACE-054](mathematics/trace-bridge/sharp_inner_jet.md).**
Let $F=zG$ be a square finite rational inner matrix function and set
$T=F^*zF'\ge I$ on the circle, with $d\mu=d\theta/(2\pi)$. Without a
commutativity assumption, with $\dot T=dT/d\theta$,

$$\int\mathrm{Tr}(\dot T T^{-1}\dot T)\,d\mu
\le\frac13\int\mathrm{Tr}(T^3-T)\,d\mu,$$

$$\int\|F''T^{-1/2}\|_F^2\,d\mu
\le\frac43\int\mathrm{Tr}T^3\,d\mu
-2\int\mathrm{Tr}T^2\,d\mu
+\frac23\int\mathrm{Tr}T\,d\mu.$$

The leading coefficient $4/3$ is optimal in every matrix dimension; the
submission had $13/3$. Smooth localization has an explicit derivative penalty.
The proof does not supply a random-cavity cubic-delay moment.

**Normally absorbed scalar transport — [BGS-TRACE-056](mathematics/trace-bridge/phase_channel_real_flow.md).**
For deterministic unitary matrices $S_m$ with
$\delta_m=\max_{ij}|(S_m)_{ij}|^2\to0$ and
$\||S_m|^2-J_m\|\le\rho<1$, and a deterministic Hermitian $H_m$
independent of the reused random phases with
$\mathrm{Tr}H_m=m$ and $\mathrm{Tr}H_m^2\le C_Hm$, eigenphase
matching along $DS_m e^{ixH_m/m}$ compares the normalized scalar resolvent
in $L^1$ with that of $e^{ix/m}DS_m$. Convergence is locally uniform
for $\mathrm{Re}\,s>0$ and bounded real $x$, including each fixed derivative
in the absorbed scalar parameter $s$. Repeated eigenvalues are included.
The 11 October continuation proves physical-source comparison in $L^2$ and
every fixed normally absorbed source product under its stated hypotheses.
Higher physical-source products and the actual cavity hypotheses remain open;
no deterministic $D=I$ limit is proved.

These are self-contained project proofs with independent internal
reconstruction. External priority is not established. The
[submission review](literature/phase_channel_jet_sources_20261008.md) maps the
attached article to maintained results and explicitly pending candidates.
> **Status distinction — BGS-TRACE-055 is not a proved result.** In
> particular, BGS-TRACE-055's polylogarithmic deep-source hierarchy remains
> **verification-pending**, unlike the reconstructed TRACE-053/054/056
> above. Its registered source is a research checkpoint record
> (`record/research_checkpoint_20261008.md`), not a maintained proof in
> `mathematics/`, and it must not be cited as a project proof.

## Read, reproduce, and cite

For an accessible beginning, read the [mathematical background](docs/reader_guide.en.md). Then use the [theorem index](mathematics/results.md) or [topic map](mathematics/topics/README.md) to reach canonical proofs. The [claim registry](record/claims.json) controls registered status; the [dated ledger](record/claim_ledger.md) explains changes, and [SOURCE_OF_TRUTH.md](SOURCE_OF_TRUTH.md) defines how to resolve conflicting surfaces.

The [consolidated research manuscript](manuscript/README.md) is a **living, full-length scientific account**, intentionally retained while the research continues; it is neither a completed proof of BGS nor a replacement for proof sources. [Focused paper scopes](papers/README.md) are separate, potential publication units rather than asserted submissions.

[Reproduction guide](REPRODUCE_unified.md) · [Computation and verification](computations/README.md) · [Formalization scope](formalization/README.md) · [Literature and priority](literature/README.md) · [Contributing](CONTRIBUTING.md) · [How to cite](CITATION.cff)

The [11 October 2026 execution packet](archive/evidence/executions/20261011/chat-research/fresh/README.md) records exact Python/C++ controls, 23 active Lean modules and the manuscript build for that earlier revision. The [28 October formalization](formalization/README.md) extends the source graph to 68 leaf modules; its [execution receipt](evidence/formalization/aristotle_20261027/receipt.json) distinguishes historical kernel checks from the GitHub merge, which has no fresh CI verification. **Lean verifies selected finite/algebraic and scalar/reference kernels, not the complete analytic corpus or BGS.** Project proof status does not imply independent external refereeing or an established novelty/priority claim.


## License

Source code (`computations/`, `formalization/`) is released under the
MIT License — see `LICENSE`. Scholarly texts, the manuscript,
mathematical exposition, registries and research data are released
under CC BY 4.0 — see `LICENSE-CC-BY-4.0.txt`. The per-path map is in
`LICENSE_POLICY.md`. Until this release, no open license was granted;
see `LICENSE_POLICY.md` for the history of that decision.

