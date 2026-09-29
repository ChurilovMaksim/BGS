# Quadratic-noise continuation: proof review and integration

Date: 29 September 2026. Author derivation and self-review only.
No subagents, independent referee report, analytic Lean certificate,
priority claim, or solution of deterministic BGS.

## Outcome and provenance

The previously unintegrated research packet has been consolidated into
five maintained notes rather than copied as overlapping scratch files.
Its four accepted auxiliary claims are FLOW-004--007. The source-to-model
fixed-time application is recorded as conditional FM-013. The integration
also completes two extensions beyond the earlier packet: full raw/reversible
path-law total variation at vanishing time, and the corrected process's
fixed-trace functional CLT with uniform moment bounds.

| Maintained source | Retained result | Boundary |
|---|---|---|
| [Coupling](../mathematics/quadratic_noise_coupling.md) | Hilbert--Schmidt estimate, local Laplace/count comparison, every-even matrix moment, operator coupling at t log N -> 0 | Two noisy processes; no initial-spectrum recovery |
| [Reversibility](../mathematics/quadratic_noise_reversibility.md) | Full divergence-form drift, gradient potential, stopped entropy and unstopped path-TV estimate | Same covariance in Girsanov; scalar points can be absorbing |
| [Trace fluctuations](../mathematics/quadratic_noise_trace_fluctuations.md) | Raw and corrected fixed-trace OU limits, variance anomaly, fixed-time coupling obstruction | Fixed number of traces and fixed time horizon |
| [Clock limit](../mathematics/quadratic_noise_clock_limit.md) | Exact odd-N kernel normalization, local error bound and Sine_2 limit for both quadratic diffusions | Special clock start; Dyson clock mechanism credited to Forrester |
| [Fixed-time input](../mathematics/quadratic_noise_fixed_time_input.md) | Exact parity repair and conditional quantitative trace input | Full regularized trace and quantization/remainder matching not completed |

The earlier fourth-moment coupling window t=o(N^(-1/2)) is retained as
the p=2 consequence of the stronger all-even-moment proof. The earlier
small-normalized-trace stopped entropy estimate is subsumed by the
explicit bounded-unnormalized-trace estimate in FLOW-005. Neither is
silently upgraded to fixed positive time.

## Adversarial proof audit

1. **State-dependent coefficients:** the coupling is written in Itô
   form with the frozen generator. Symmetry of the covariance square root
   cancels the mixed commutator. Smooth quadratic factorization and
   Brownian extension establish weak coupling even at singular covariance;
   no false global Lipschitz square-root hypothesis is used.
2. **Matrix moments:** both row and column quadratic variations are bounded.
   Hermitian dilation and weighted Young give the general trace inequality;
   the finite seeded tests are only controls of individual algebraic terms.
3. **Local observables:** phase averaging and bounded Laplace tests avoid
   an occupancy hypothesis. Count-vector TV does not mean full configuration
   TV. No unbounded pair/correlation moment transfer is inferred.
4. **Reversibility:** the radial divergence identity is lifted to the
   full matrix field by conjugation equivariance and the stabilizer torus.
   Common-phase invariance handles the determinant constraint. Independent
   matrix-coordinate finite differences check the full divergence.
5. **Girsanov:** the two compared processes have identical covariance;
   a stopped uniform inverse bound controls the density. The exit event
   is measurable from the stopped path, allowing an explicit unstopping
   estimate. This argument is not applied to raw versus Dyson path laws.
6. **Trace CLT:** zero-index terms m_0=1 are preserved. Uniform maximal
   trace moments are proved before taking limits, including the corrected
   drift's higher-index terms. Tightness, bracket identification and
   moment uniform integrability are stated explicitly. The anomalous
   second trace survives despite the small covariance rank.
7. **Clock limit:** odd-N periodic heat normalization and full versus
   traceless Brownian phase are distinguished. Non-Hermitian kernel
   convergence uses Hadamard/Fredholm domination, not an inapplicable
   positive-kernel inequality. The hole argument gives a strict obstruction
   to generic noise removal, not a chaotic-system counterexample.
8. **External input:** Forrester's kernel is prior work. Faure's full
   torus theorem is even-dimensional. The earlier scratch conclusion
   applying it to the maintained odd-N map is not promoted on the strength
   of a parity check alone; FM-013 explicitly retains the missing matching.

## Fresh computation scope

The [dynamics verifier](../computations/verification/quadratic_noise_dynamics.py)
uses deterministic complex128 Hermitian-basis contractions, centered finite
differences, seeded finite matrix examples, and exact Python integers:

- 25 coupling cases at N=2,3,4,5,7, including scalar, antipodal, clustered,
  irregular and clock spectra with non-diagonal matrix coordinates;
- 72 trace-drift cases at N=3,4,5,7, orders 1--6, and the corresponding
  holomorphic/mixed brackets; corrected drift included;
- radial and full matrix divergence, potential gradient and second-trace
  corrections; maximum finite-difference discrepancy below 3.6e-11;
- 252 matrix-moment terms, p=2--8, and 1,875 exact integer parity cases.

The [clock verifier](../computations/verification/quadratic_noise_clock.py)
compares 12 Fourier-alias and independent heat/Gram kernels (maximum
discrepancy below 3.4e-15), records local kernels through N=1001 and
three hole quadratures. The latter approximate 0.170217421379185 and
are illustrations, not an exact proof of positivity. No simulation of
the maintained fixed-strength map or numerical certification of a limit
has been performed.

Reproduce from the repository root:

```bash
python3 computations/verification/quadratic_noise_dynamics.py --output build/quadratic-noise/dynamics.json
python3 computations/verification/quadratic_noise_clock.py --output build/quadratic-noise/clock.json
python3 computations/verification/scientific_registry_audit.py
python3 computations/verification/repository_audit.py
python3 computations/maintenance/render_claim_registry.py --check
python3 computations/maintenance/sync_fixed_map_section.py --check
python3 computations/maintenance/sync_finite_orbit_section.py --check
```

Fresh immutable numerical outputs and source hashes are under
`evidence/20260929/`. The integration-check record there states what
structural checks and manuscript build actually ran; those checks are
not mathematical certificates. Historical evidence was not rewritten.

## Remaining scientific task

The clock result closes a genuine auxiliary local-limit problem, but
does not identify the deterministic map's local law. The next useful
claim must supply additional dynamical information sufficient for
deterministic noise removal, or directly control the model's signed
joint traces at Heisenberg times. Small fixed traces, bounded local
occupancy and the auxiliary Sine limit alone provably do not supply
that implication. BGS-TRACE-005 and BGS-BGS-001 remain **OPEN**.
