# Source comparison for the unistochastic two-step obstruction

Checked against the primary source on 12 October 2026:
Karol Życzkowski, Marek Kuś, Wojciech Słomczyński and Hans-Jürgen Sommers,
*Random unistochastic matrices*, Journal of Physics A 36 (2003), 3425–3450.
The checked preprint is [arXiv:nlin/0112036v3](https://arxiv.org/html/nlin/0112036v3),
dated 28 August 2002.

## Exact locators and applicability

- Introduction and §IV.2 define the Haar-induced unistochastic ensemble.
  The object \(P_Z=|Z|^2\) is established prior work.
- §IV.3, including Figure 7, studies spectra and singular-value statistics.
  Its numerical singular-value observations are not imported as a rigorous
  operator-norm theorem.
- Appendix E, especially equations (82)–(85), develops Haar-entry moment
  computations for average traces. Those formulas concern the source's
  observables; we do not attribute our centered fourth-Schatten identity
  to them.

## What the maintained proof supplies

[TRACE-074](../mathematics/trace-bridge/unitary_two_step_obstruction.md)
derives its exact centered fourth moment from Dirichlet row moments and
the conditional complex-sphere second moment. Its residual completion law
is proved by compact-group invariance. Its existence bound then uses only
Markov's inequality and union bounds. No singular-gap theorem from the
paper is load-bearing, and no new external-dependency registry leaf is
added for this comparison.

The two-correction construction and the two-step obstruction are project
results with independent internal reconstruction. This limited source
check does not establish world priority for the construction, its moment
identity or the elementary higher-step bound. It does not identify a
chaotic quantizer or a random Schur trajectory.
