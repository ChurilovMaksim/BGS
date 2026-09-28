# Research checkpoint: quadratic coboundary noise, 28 September 2026

## Original target and outcome

The target remains deterministic microscopic CUE statistics for the maintained
fixed-strength quantum map, including the mixed Heisenberg-time information
in BGS-TRACE-005. General BGS and the fixed-map target are **not solved**.
No subagents were used. The work prioritized a mechanism absent from the
previous second-order calculation rather than another audit of the uploaded
CUE archive.

The result is [BGS-FLOW-003](../mathematics/quadratic_coboundary_noise.md):
an exact finite-$N$ covariance theorem for a centered quadratic commutator,
its complete ellipticity criterion, explicit covariance correction to the
traceless Dyson generator, an uncorrected Haar stationarity defect, and
rank restrictions on smooth finite-direction realizations. These are project
derivations, not an external review or a worldwide-priority determination.

## Route tree and discriminating outcomes

| Route | Precise success criterion | Executed discriminator | Outcome |
|---|---|---|---|
| Dense quadratic Gaussian curvature | Obtain nondegenerate phase noise beyond the vanishing first derivative | Wick contraction, full Hermitian-basis covariance, scalar and antipodal spectra | Exact covariance depends on $m_2$; elliptic on all traceless directions iff $|m_2|<1$. Explicit whitening gives the infinitesimal Dyson generator. Subsidiary theorem closed. |
| Smooth finite-direction realization | Realize enough radial directions from a small smooth input family and its time translates | Dimension of centered quadratic span; frozen-frame conjugation identity | Rank at most $d(d+1)/2$; unmixed translates preserve diagonal range. With mixed translates of finitely many inputs through logarithmic time, instantaneous radial rank is only $O(\log^2N)$. This construction fails; evolving-frame bracket generation remains deferred. |
| Noise removal / deterministic transfer | Preserve local statistics while reaching a regime where noise proves universality | Fourth-order centered displacement; local clock observable; exact Haar integration | Original curvature suggests $Nt^4$ scale only as a fixed-$N$ derivative. A clock pair statistic has a Dyson derivative of order $N$. Raw quadratic noise is not Haar stationary. No uniform relaxation-scale transfer established. |

The first theorem does not close the third route. The second route is a scoped
rank obstruction, not a general impossibility theorem. No claim that all
possible BGS approaches have been exhausted is made.

## Exact accepted statements

For normalized GUE $G$ and any fixed $U\in U(N)$, let
$X=i[G,UGU^*]/\sqrt2-\mathbb E(i[G,UGU^*]/\sqrt2)$.
For traceless Hermitian $T$,

$$
\frac{1-|\operatorname{Tr}U^2/N|}{N}\operatorname{Tr}T^2
\le\mathbb E(\operatorname{Tr}XT)^2
\le\frac{2+|\operatorname{Tr}U^2/N|}{N}\operatorname{Tr}T^2.
$$

The exact tensor and invariant operator are proved in the linked note.
Their use includes these qualifications:

- Ellipticity is a statement about externally sampled noise, and is also
  true at clock spectra. It does not characterize chaotic spectra.
- Covariance whitening yields an exact *infinitesimal* generator at fixed
  $N$; no uniform diffusion approximation is claimed.
- At $m_2=0$, the uncorrected generator differs from circular Dyson by
  common-phase removal and a rank-two Hessian. The local pair error is
  at most $2(N-1)N^{-2}\sup|x^2\phi''|$, pointwise at that spectrum.
- For nonzero $m_2$, at most $M$ phases per mean-spacing arc implies the
  microscopic-time pair-generator error
  $C_{R,\phi}|m_2|M^2(1+\log N)+2N^{-2}\sup|x^2\phi''|$.
  Symmetrized phase derivatives cancel the cotangent pole without a
  smallest-gap bound. The project trace estimate would suffice if
  $M=o(N^{1/80}/\sqrt{\log N})$, but this occupancy has not been proved.
- The raw noise has Haar stationarity defect
  $\int\mathcal L_X|\operatorname{Tr}U^2|^2\,d\mathrm{Haar}=4+2/N^2$
  for $N\ge4$. The set $m_2=0$ cannot be treated as an invariant manifold.
- The original coboundary flow has phase covariance $t^4\Sigma/2+o(t^4)$
  at fixed $N$, not a complete fourth-order generator equal to the corrected
  process. The earlier second-order normal form is credited to prior project work.
- The earlier fixed-time trace bound would make the constructed covariance
  uniformly elliptic for the actual map. That earlier estimate was not
  re-proved here and does not supply deterministic noise removal.

## Finite verification and its coverage

Command from the repository root:

```bash
python3 computations/verification/quadratic_coboundary_noise.py --output evidence/20260928/quadratic_coboundary_noise.json
```

The executed suite contains twelve covariance cases with $N\in\{2,3,4,5,7\}$:
clock, irregular, scalar and repeated antipodal spectra. It contracts the
centered Gaussian quadratic polynomial in a complete Hermitian basis,
independently compares the invariant covariance operator, checks its full
traceless spectrum and whitening, and verifies the determinant constraint.
Maximum tensor discrepancy was below $8\cdot10^{-16}$ in complex128.

Four irregular spectra through $N=13$ check the $p_2$ generator, its
quadratic variation and the real Hessian of $|p_2|^2$. Five clock spectra
through $N=65$ check the pair-generator identity; for the selected bump,
$\mathcal L_DF/N\simeq0.1275583706$. Exact Fraction Laurent integration
of the $U(4)$ Vandermonde density gives the stationarity defect $33/8$.
Three smoothly deformed clocks through $N=65$ have nonzero $m_2$ and
occupancy two; they check the symmetrized nonzero-$m_2$ generator identity.
Three decreasing step sizes check the second-order normal form; a
three-direction example checks the rank bound and three exact time
translates check unchanged radial output.

Finite floating-point checks do not prove the all-$N$ assertions. Their
proofs are the Wick, Hilbert--Schmidt, Taylor, character-orthogonality and
dimension arguments in the maintained note. No Monte Carlo, proxy coupling,
large-$N$ experiment, formal Lean check, or external referee review is claimed.
Source hashes and commands are in the dated evidence manifest.

## Literature and priority boundary

Searches included `random matrix commutator unitary conjugation Dyson
Brownian motion covariance`, `quadratic coboundary Dyson`, `random commutator
unitary covariance Gaussian`, and `coboundary spectral Brownian`.
Both available search systems were used; absence of a matching result is
not evidence of priority.

- Palheta, Barbosa and Novaes, *Commutators of random matrices from the
  unitary and orthogonal groups*, [arXiv:2004.09266](https://arxiv.org/abs/2004.09266),
  studies a multiplicative commutator of independent Haar matrices, a different
  object from the additive commutator with a correlated conjugate here.
- Landon, Sosoe and Yau, *Fixed energy universality for Dyson Brownian motion*,
  [arXiv:1609.09011](https://arxiv.org/abs/1609.09011), provides context for
  microscopic noise relaxation with assumptions on initial density. Its
  Hermitian result has **not** been imported as a theorem about the present
  circular, state-dependent construction. Only abstract-level scope was
  checked in this pass; no exact source theorem is load-bearing here.

Standard Wick and finite character orthogonality are used explicitly in the
proof. The three-exponential normal form and second-order sine curvature
were already project results. No novelty claim is attached to covariance
whitening as a general linear-algebra technique.

## Remaining proof obligation

A viable next step must control a quantitative evolving-frame realization
or a deterministic comparison of microscopic observables with the corrected
noise process. It must simultaneously track noise time, dimension, spectral
regularity and all-order statistics. Mere low-trace decay, full covariance
rank, qualitative controllability, or a Dyson theorem for another ensemble
does not meet that obligation. Those stronger implications are deferred,
not proved and not broadly disproved by the scoped obstructions above.

Starting local main: `36e4dc2c0a428012bd45dcdb21023d10a34f019a`.
Starting remote main: `2bcc4b7a90d2c8e47e3018bbe86fc1ef585e3abc`.
Their matching content tree was `2ca0ba8adf7eadf54c5c5469bb90f2e4b4042841`;
the pre-existing history difference is preserved without force-pushing.
