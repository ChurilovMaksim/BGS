# BGS: quantum chaos and microscopic spectral statistics

[Русская версия](README.ru.md) · [Research brief](RESEARCH.md) ·
[Theorem index](mathematics/results.md) · [Claim ledger](record/claim_ledger.md)

**The deterministic microscopic BGS problem remains open.** This repository
contains maintained proofs, exact finite controls and a consolidated research
manuscript. It studies how classical chaos can produce random-matrix spectral
statistics, with an explicit nonlinear quantum map as the principal test case.

## What the conjecture asks

The [Bohigas–Giannoni–Schmit paper of 1984](https://doi.org/10.1103/PhysRevLett.52.1)
identified random-matrix level fluctuations in a chaotic billiard. The general
problem is to prove the appropriate local law for a specified semiclassical
family, after resolving symmetries and normalizing the mean level spacing.
Classical chaos alone is not a complete set of hypotheses: arithmetic
structure and the choice of quantization matter.

For the unitary symmetry class, the density-one reference is the Sine$_2$
process. Its kernel and pair correlation are

$$K(x,y)=\frac{\sin\pi(x-y)}{\pi(x-y)},\qquad
\rho_2(x,y)=1-|K(x,y)|^2.$$

![Analytic Sine2 pair correlation and Poisson reference](assets/figures/microscopic_pair_reference.svg)

*Analytic reference curves, not measured spectra of the maintained map.
The horizontal coordinate is separation in units of the mean spacing;
the pair correlation is not the nearest-neighbour spacing density.*

A complete local law requires every fixed correlation order. A few trace
moments or a spacing plot do not determine that law.

## The exact model and target

The principal family uses odd $N\ge3$, the ordinary Weyl convention, and

$$S=\begin{pmatrix}3&4\\2&3\end{pmatrix},\qquad
U_N=e^{i\tau N A_N}M_N,\qquad \tau=10^{-80}.$$

The [canonical model statement](mathematics/fixed_map_resolvent_frontier.md)
specifies the symbol, metaplectic kernel and exceptional dimensions. The
coupling stays fixed as $N\to\infty$. A necessary pair reference is

$$L_N(s)=\frac1{N^2}\sum_{n\ge1}e^{-2sn/N}
|\operatorname{Tr}U_N^n|^2
\longrightarrow\frac{1-e^{-2s}}{4s^2},\qquad s>0.$$

The full target, [BGS-TRACE-005](mathematics/open_questions.md#b-prove-heisenberg-scale-desymmetrized-joint-trace-estimates),
is the correctly desymmetrized, density-unfolded **signed factorial joint-trace
comparison at Heisenberg powers** for every fixed order and compact smooth
Fourier test. The modulus is outside the complete sum. The
[trace-to-local-statistics bridge](mathematics/trace_to_local_statistics_bridge.md)
states the exact hypotheses converting these trace estimates to local laws.

## Three reconstructed analytic results

**Phase memory with reused coordinate phases — [BGS-TRACE-053](mathematics/max_entry_phase_channel.md).**
For $S\in U(m)$, set $P_{ij}=|S_{ij}|^2$, $\delta=\max P_{ij}$,
$A=\Pi\operatorname{Ad}(S)$, and
$T_n=\mathbb E_D\operatorname{Ad}((DS)^n)$. Here $\Pi$ is diagonal pinching
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

$$\int\operatorname{Tr}(\dot T T^{-1}\dot T)\,d\mu
\le\frac13\int\operatorname{Tr}(T^3-T)\,d\mu,$$

$$\int\|F''T^{-1/2}\|_F^2\,d\mu
\le\frac43\int\operatorname{Tr}T^3\,d\mu
-2\int\operatorname{Tr}T^2\,d\mu
+\frac23\int\operatorname{Tr}T\,d\mu.$$

The leading coefficient $4/3$ is optimal in every matrix dimension; the
submission had $13/3$. Smooth localization has an explicit derivative penalty.
The proof does not supply a random-cavity cubic-delay moment.

**Normally absorbed scalar transport — [BGS-TRACE-056](mathematics/phase_channel_real_flow.md).**
For deterministic phase-independent Hermitian $H$ with
$\operatorname{Tr}H=m$ and $\operatorname{Tr}H^2\le C_Hm$, eigenphase matching
along $DS e^{ixH/m}$ gives a locally uniform $L^1$ comparison with
$e^{ix/m}DS$ for the normalized normally absorbed scalar resolvent, including
each fixed source derivative. Repeated eigenvalues are included. The
anisotropic physical source and mixed source products require further inputs.

These are self-contained project proofs with independent internal
reconstruction. External priority is not established. The
[submission review](literature/phase_channel_jet_sources_20261008.md) maps the
attached article to maintained results and explicitly pending candidates.
In particular, BGS-TRACE-055's polylogarithmic deep-source hierarchy remains
**verification-pending**.

## What else is established, and what is missing

| Family | Maintained conclusion | Remaining boundary |
|---|---|---|
| Fixed-map structure | Actual intensity mixing, cyclic ramp and reverse-cyclic suppression; common pair commutant classified for odd $N\ne7$ | Common commutant is not simplicity of $U_N$ or microscopic universality |
| Signed trace sectors | Selected weighted WKB, fixed-order ordered-diagonal and specified low-switch families | Complete balanced law, high-switch interference and plateau |
| Unmasked insertion calculus | Complete separated/convex hierarchy; bounded-parameter signed weak-noise stability | Masks, undamped endpoint and signed noise removal |
| Noisy local laws | Actual-start weak local law; all fixed factorial orders on a separately stated schedule | Transfer back to the unchanged deterministic propagator |
| Arithmetic and return laws | Cayley, Pell, Floquet, resonance, locality and information-theory theorems in their own regimes | Their hypotheses do not by themselves identify the frozen-map local law |

Exact statements and dependencies are in the [research brief](RESEARCH.md)
and [thematic reading paths](mathematics/topics/README.md). The central
unresolved estimates are the absorbed Ward overlap defect, the complete
balanced microscopic law, and the signed deterministic all-order comparison.
The [obligation board](mathematics/open_questions.md) states them precisely.

## Read, reproduce, and cite

Start with the [reader background](docs/reader_guide.en.md), then the theorem
source appropriate to your question. The [claim ledger](record/claim_ledger.md)
controls scientific status; [SOURCE_OF_TRUTH.md](SOURCE_OF_TRUTH.md) resolves
conflicting surfaces. The single publication root is
[manuscript/BGS_unified.tex](manuscript/BGS_unified.tex).

The [computation guide](computations/README.md),
[formalization scope](formalization/README.md), and
[reproduction guide](REPRODUCE_unified.md) give commands and coverage.
The [8 October execution packet](evidence/executions/20261008/phase-channel-jet/README.md)
records Python quadrature, exact independent C++ occupation counts, Wolfram
identities, a 20-module Lean 4.33.1 build and the 280-page manuscript build.
Lean certifies stated finite/algebraic kernels; the analytic theorems and BGS
are not formalized by that build.

Historical records retain their original provenance. A scoped review does
not certify every earlier proof. [Citation metadata](CITATION.cff),
[review policy](REVIEWING.md), and [publication scopes](papers/README.md)
complete the research-facing entry points.
