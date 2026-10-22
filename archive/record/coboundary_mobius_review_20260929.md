# Continuation: fourth-order coboundary dynamics and Möbius reduction

Checkpoint: `coboundary-mobius-20260929`, based on remote main
`c11f45165c9dc2fdb720ec783aa94eba348a148e`, whose tree equals the local
research base `1918512d6121b4d7b95a22012654feb7cc70014a`.
No subagents were used. Verdicts below are author self-review only.

## Exact outcome

**BGS-FLOW-008: proved as written.** The finite Gaussian coboundary step
has a nonzero expected fourth-degree logarithm in general. Even explicit
frozen subtraction of its second-degree mean leaves an additional drift.
The raw quadratic covariance alone does not identify its diffusion limit.
See [the algebraic proof](../mathematics/coboundary_fourth_order_drift.md).

**BGS-FLOW-009: proved as written, in its stated iterated-limit scope.**
For independent normalized GUE kicks, starting from odd clock matrices,
the uncentered coboundary chain has the phase-averaged Sine_2 weak limit
when the step first tends to zero at each fixed dimension, followed by
dimension tending to infinity at t_N -> 0, N t_N -> infinity, with
approximately 2 t_N / epsilon^4 steps. The proof passes through a
Möbius-centered spectral diffusion; it does not claim convergence of
the original matrix paths or an explicit simultaneous epsilon_N regime.
See [the full proof](../mathematics/coboundary_mobius_diffusion.md).

The original deterministic BGS goal was **not reached**. This closes a
specified fourth-order spectral mechanism for actual repeated random
coboundary kicks; it does not remove the added randomness.

## Mechanism and dependency closure

The faster second-degree mean is repulsive first-harmonic phase motion.
It is tangent to common disk-Möbius orbits. Local conformal centering sets
the first trace to zero, changes averaged local Laplace functionals by
O(|m_1|), and makes the expected fourth logarithm vanish. The remaining
projected covariance has a controlled two-direction correction and an
explicit Itô drift bounded by 80/N². Coupling and the existing Dyson
clock theorem then yield the local limit.

The dependency chain is FLOW-003 -> FLOW-008, and
FLOW-003/FLOW-004/FLOW-007/FLOW-008 -> FLOW-009. Only the existing
FLOW-007 Dyson clock input uses the pinned Forrester source. No claim
depends on the conditional fixed-model source application FM-013.

The Möbius/Kuramoto connection is prior work, not a novelty claim:
B. Chen, J. R. Engelbrecht, R. Mirollo,
[*Hyperbolic Geometry of Kuramoto Oscillator Networks*, arXiv:1707.00713v1](https://arxiv.org/abs/1707.00713v1).
Its abstract and metadata were inspected. The local contraction,
infinitesimal action and uniqueness argument needed here are proved
directly; no uninspected global barycenter theorem is imported.

## Adversarial self-audit

| Obligation | Verdict | Decisive check |
|---|---|---|
| Actual versus compensated steps | Passed | Both are defined explicitly; the compensated step has the extra B_4 drift. |
| BCH sign and time normalization | Passed | Exact rational free-word expansion; independent Wick contraction; h=epsilon^4/2. |
| Möbius centering domain | Passed | Explicit contraction for |m_2|<=3/4, |m_1|<=1/1024; small center unique. |
| Common rotation and conjugation | Passed | Quotient observables are invariant under both; eigenvectors are not asserted to converge. |
| Fast-coordinate control | Passed | Killed 2p-th moments O(epsilon^(2p)); p=3 bounds exits over epsilon^(-4) steps. |
| Small-step spectral limit | Passed | Generator error summed over time is O_N(epsilon); tightness, smooth projected SDE uniqueness and regular-level localization are specified. |
| Projection Itô drift | Passed | Explicit expansion plus independent nonlinear finite-difference Hessian; not replaced by a Stratonovich equation. |
| Dimension-uniform comparison | Passed | Bounds on residual covariance, projected second trace and drift; discarded exit probability O(t/N²). |
| Order of limits | Passed | Fixed N precedes epsilon -> 0; no finite computation or dimension-dependent remainder is promoted to a uniform joint limit. |
| Deterministic noise removal | Not established | The clock changes its local law under the very chain studied; centering removes only the fast collective mode. |
| Independent review / formalization | Not addressed | No independent reviewer or Lean compilation for these analytic arguments. |

Sard regular values are chosen for the smooth phase quotient of the
trace-zero matrix manifold, not for an assumed smooth space of unordered
eigenvalues. Positivity is used only on the nonconstant normal direction.
Smooth localization and invariant backward semigroups supply uniqueness
of the spectral martingale problem through eigenvalue collisions.

## Finite evidence

[The maintained verifier](../computations/verification/coboundary_mobius_diffusion.py)
checks the free algebra and mean coefficients with exact fractions;
full Wick sums at N=2,3,4,5 agree with the explicit formula within
4.8e-16. A finite sequence of step sizes checks the predicted fifth-order
matrix-log remainder without asserting an asymptotic certificate.

At N=4,5,7,9, in non-diagonal coordinates, independent nonlinear
centering and finite-difference Hessians agree with the projected drift
within 5.6e-8 at step 2e-4. The same controls check the trace constraint,
Hermiticity, relative commutator cancellation, Möbius orbit centering,
and the stated coarse drift/bracket bounds. These are finite controls,
not a simulation or proof of the stochastic limit.

```bash
python3 computations/verification/coboundary_mobius_diffusion.py --output build/coboundary-mobius/check.json
```

Fresh evidence and a source-hash manifest are under `evidence/20260929/`.
Earlier dated evidence remains unchanged.

## Routes and next executable boundary

1. **Direct identification from covariance:** refuted in that form by the
   exact B_4 term and faster mean. The Möbius quotient repairs the
   specified repeated-step mechanism; arbitrary compensation is not equivalent.
2. **Generic deterministic noise removal:** the attempted removal of the
   collective drift succeeds by (4)--(5) of FLOW-009, but does not remove
   the residual diffusion. The clock example prevents extending this
   argument to the whole stochastic evolution without a new model-specific input.
3. **Classical correspondence alone:** spectral-rounding obstructions
   already exist in the repository. Reusing weak Egorov information
   without strengthening it does not resolve the missing implication;
   that duplicate route was not promoted to a new result.

The remaining direct target is still BGS-TRACE-005: a model-specific
Heisenberg-scale signed joint-trace estimate, or a comparably strong
approximate stationarity argument for microscopic observables of the
deterministic family. An independent follow-up within the new stochastic
route is to quantify epsilon_N uniformly or prove relaxation from the
actual centered starting spectra. Neither is silently assumed here.
