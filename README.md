# BGS — quantum chaos and spectral universality

[Русский](README.ru.md) · [Research overview](RESEARCH.md) · [Corpus atlas](docs/corpus_atlas.md) · [Mathematical introduction](docs/reader_guide.en.md) · [Theorem index](mathematics/results.md) · [Complete manuscript](manuscript/README.md)

The **Bohigas–Giannoni–Schmit conjecture** is a central question in quantum chaos: under appropriate dynamical and symmetry conditions, why should the microscopic energy-level statistics of deterministic chaotic systems agree with random-matrix theory? This repository develops exact mathematics, counterexamples, and reproducible verification around this question, especially for one explicitly specified quantum torus map.

**Scientific status (12 October 2026):** The microscopic BGS limit for the fixed deterministic map below is **open**. Several related theorems have project proofs in their precisely stated regimes; none is a proof of universality for all chaotic systems. [Scientific status](record/claim_ledger.md) · [Open proof obligations](mathematics/open_questions.md).

![BGS research logic: exact model, proved reductions, and outstanding signed spectral comparison](assets/figures/bgs_frontier.svg)

*Research map, not a chain of proved implications: the final arrow is the missing mathematical step.*

## Checked continuation, 11 October

[The 12 October unitary obstruction](mathematics/unitary_two_step_obstruction_20261012.md)
shows that logarithmic entry flatness and a vanishing intensity singular
norm can coexist with a logarithmic two-step peak, even for genuine
unitary matrices. Three-step mixing does not supply the two-step Schur
variance estimate. The [fresh-phase drift theorem](mathematics/two_step_restoring_drift_20261012.md)
proves a restoring one-step mean for the constructed peaks; concentration
and all-time flatness probability remain open.


[The new checkpoint](record/chat_integration_20261011.md) proves maximal
full local-process transport for the maintained deterministic map on an
observable-flow interval $o(\sqrt{\log N})$, physical-source comparison in $L^2$,
and every fixed mixed product of normally absorbed sources. Separate theorems
give frozen compatible-phase Sine-beta laws for Haar circular backgrounds
and an all-order critical CSE Gaussian limit. Their hypotheses are explicit;
the initial deterministic spectral law and signed TRACE-005 remain open.


The [Schur continuation](record/cavity_continuation_20261011.md) additionally
proves conditional concentration of incoming/outgoing delays and all fixed
killed clock upper moments down to $\lceil\log(2N)^{1+\kappa}\rceil$,
with [uniform equality laws at every fixed order](mathematics/conditional_clock_universality_20261011.md)
and an [explicit clock measure at every retained fraction](mathematics/full_depth_clock_measure_20261011.md),
including the atom forced by a finite rank bound. A separate harmonic-lift theorem
contracts every classical centered singular value and controls the quantum
position-chain and [reversal gaps](record/reversal_channel_continuation_20261011.md) down to $\lceil\log(2N)^{3+\kappa}\rceil$. Both stochastic
conclusions still assume all-time entry flatness; its probability and the
initial microscopic spectral law remain open.

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

Here $M_N$ is the specified quantization of the hyperbolic cat map, and $A_N$ the specified Weyl-quantized nonlinear kick. [The canonical model source](mathematics/fixed_map_resolvent_frontier.md) fixes conventions, exceptional dimensions, and symmetry questions. **The coupling remains fixed as $N\to\infty$**; replacing it with vanishing coupling, independent random phases, or noise changes the problem.

Even a necessary two-point reference remains unproved for this family:

```math
L_N(s)=\frac{1}{N^2}\sum_{m\ge1}e^{-2sm/N}
\left|\mathrm{Tr}\,U_N^m\right|^2
\;\longrightarrow\;
\frac{1-e^{-2s}}{4s^2},
\qquad s>0.
```

The full [BGS-TRACE-005 obligation](mathematics/open_questions.md#b-prove-heisenberg-scale-desymmetrized-joint-trace-estimates) is stronger: correctly desymmetrized **signed factorial joint-trace comparison** for every fixed order and every compactly supported smooth Fourier test, at powers $m\asymp N$. The absolute value is taken **after the complete Fourier sum**, rather than term by term. The [trace-to-local-statistics bridge](mathematics/trace_to_local_statistics_bridge.md) explains the further tightness/extension conditions.

## What else is established, and what is missing

The programme contains independently distinguishable lines of work:

| Mathematical layer | Established in its stated scope | Not yet established |
|---|---|---|
| Spectral-to-trace bridge | Exact finite-dimensional combinatorics and conditional correlation criteria | Required model-specific signed joint-trace estimates |
| Actual map: intensity and paths | [FM-021](mathematics/position_chain_mixing.md) intensity mixing and cyclic ramp; [FM-022](mathematics/reversed_path_decay.md) reverse-path decay | All remaining coherent interference, including the negative plateau correction |
| Balanced microscopic analysis | [Phase Ward](mathematics/phase_ward_identity.md) and [Schur-energy](mathematics/balanced_pair_schur_reduction.md) exact identities | Their requisite absorbed overlap / microscopic radial limits |
| Traces and insertion calculus | Selected [WKB](mathematics/factorial_wkb_reduction.md), [ordered-diagonal](mathematics/factorial_ordered_diagonal.md), and [unmasked](mathematics/right_frame_unmasked_pinch_hierarchy.md) sectors | Complete high-switch signed remainder, masks and endpoints |
| Stochastic comparison | [FLOW-014](mathematics/circular_dyson_actual_start.md) and [FLOW-017](mathematics/coboundary_all_order_limit.md) noisy local laws on explicitly stated schedules | Removal of the noise for the original deterministic family |
| Other mathematics | [Cayley](mathematics/topics/cayley-arithmetic/README.md), [Pell](mathematics/topics/pell/README.md), [return](mathematics/topics/returns/README.md), resonance, locality and information results | A proved implication from their separate regimes to deterministic BGS |

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

## Three reconstructed analytic results

**Phase memory with reused coordinate phases — [BGS-TRACE-053](mathematics/max_entry_phase_channel.md).**
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

**Optimal matrix inner-function jets — [BGS-TRACE-054](mathematics/sharp_inner_jet.md).**
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

**Normally absorbed scalar transport — [BGS-TRACE-056](mathematics/phase_channel_real_flow.md).**
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
In particular, BGS-TRACE-055's polylogarithmic deep-source hierarchy remains
**verification-pending**.

## Read, reproduce, and cite

For an accessible beginning, read the [mathematical background](docs/reader_guide.en.md). Then use the [theorem index](mathematics/results.md) or [topic map](mathematics/topics/README.md) to reach canonical proofs. The [claim ledger](record/claim_ledger.md) is authoritative for status, and [SOURCE_OF_TRUTH.md](SOURCE_OF_TRUTH.md) defines how to resolve conflicting surfaces.

The [consolidated research manuscript](manuscript/README.md) is a **living, full-length scientific account**, intentionally retained while the research continues; it is neither a completed proof of BGS nor a replacement for proof sources. [Focused paper scopes](papers/README.md) are separate, potential publication units rather than asserted submissions.

[Reproduction guide](REPRODUCE_unified.md) · [Computation and verification](computations/README.md) · [Formalization scope](formalization/README.md) · [Literature and priority](literature/README.md) · [Contributing](CONTRIBUTING.md) · [How to cite](CITATION.cff)

The [11 October 2026 execution packet](evidence/executions/20261011/chat-research/fresh/README.md) records exact Python/C++ controls, 23 active Lean modules and the current manuscript build. **Lean verifies selected finite/algebraic kernels, not the complete analytic corpus or BGS.** Project proof status does not imply independent external refereeing or an established novelty/priority claim.
