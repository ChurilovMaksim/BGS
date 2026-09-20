# Review and exact claim status

Primary goal: **OPEN**. The frozen fixed-coupling BGS problem is not solved.
No estimate of its mixed microscopic loop hierarchy has been established.

Reviewed artifacts: `loop_bridge.md`, `entropy_obstruction.md`, `checks.py`.
The internal agent `audit_loop_bridge` separately checked the external
theorem's hypotheses and intensity convention, moment upgrade, deterministic
anchored normalization, same-half-plane vanishing, mixed p=2 identity,
entropy argument, and instantaneous noise-rank calculation. The root
agent derived and self-reviewed the Brownian generator and cat-period
covariance claims. No external peer review or Lean execution occurred.

## Obligation table

| Claim | Evidence | Scope / remaining qualification |
|---|---|---|
| Cotangent resolvent is particle-generated | Direct Herglotz and pole calculation; internal audit | Atom masses positive; ordinary residues negative |
| Full normalized mixed hierarchy implies sine process | Bourgade--Huang v2, Theorem 1.9 | External theorem import; whole-space event used |
| Same hypothesis implies every compact anchored factorial test | Moment bootstrap, count bounds, uniform integrability, exact origin integration; internal audit | Not pointwise densities or every fixed origin |
| Same-half-plane loops vanish | Fourier charge proof and quadrature | True for every spectrum and every beta>0 |
| First mixed defect is 8i(L+C0-1/(4s^2)) | Independent Fourier derivation; direct cotangent quadrature | C0 may be complex |
| Finite CUE reference has curvature correction | Exact cubic trace formula and geometric sums; 767 integer coefficient checks | Expected residual O(N^-2), not finite-N zero |
| Brownian drift differentiates corrected real defect | Matrix completeness derivation; full-basis Richardson checks | Not a removal-of-noise theorem; loses imaginary defect |
| Clock violates mixed condition | Exact traces and bounded resolvent moments | Abstract control, not fixed-map counterexample |
| Cat-transport covariance cannot be isotropic | Exact order bound and finite-rank argument | Only this linear-noise mechanism; nonlinear brackets not excluded |
| Transport by V gives rank-one instantaneous phase covariance | Spectral diagonal invariance; internal audit | Requires simple spectrum for unambiguous phase derivatives |
| Microscopic RMS preservation contradicts global entropy o(N) | Explicit CUE tube estimate and data processing; internal audit | Does not exclude local entropy or local-statistics comparison |
| Frozen map satisfies full mixed hierarchy | No proof | Main load-bearing gap |

## Corrections made before recording conclusions

1. The source uses intensity 1/pi; unfolded intensity-one positions are
   obtained by dividing its coordinates by pi, not by silently identifying
   the two scales.
2. Finite circular CUE is not an exact solution of the limiting straight-line
   hierarchy. Its p=2 mean differs by the explicit sinh(s/N) correction.
3. A high-probability truncated hierarchy alone would not give untruncated
   factorial moments. Here the sufficient condition is on the entire origin
   probability space, allowing the source's moment absorption argument.
4. The trace cubic is complex for a fixed spectrum. Taking only its real
   part is legitimate in the Brownian observable, not in the full loop test.
5. At repeated eigenvalues, sorted eigenphase derivatives need not have
   the rank-one covariance of analytic labels. The rank statement is
   expressly restricted to simple V.
6. Numerical runs use an auxiliary kick exponent. They verify formulas
   but do not resolve tau=10^-80 or any asymptotic limit.

## Reproduction

From the repository root:

```sh
OPENBLAS_NUM_THREADS=1 python3 build/resolvent-flow/checks.py
```

Dependencies: Python, numpy, scipy; exact model input is imported from
`build/secular-route/exact_structure_checks.py` and
`build/algebraic-return/exact_coefficients.py`.
Numerical diagnostics are floating checks, not certified enclosures.
All check assertions passed; no proof uses a fitted numerical trend.

The source PDF retained here has SHA-256
`9ae676c7e1161d100244080dae040c5bbce8b0ddb829c9ab1326ec8c3e3ec223`.
Only the cited theorem, assumptions, and bootstrap were audited for this
application; the complete external theorem proof was not re-proved.

## Next mathematical obligation

Obtain cancellation in mixed microscopic resolvent products for the
original deterministic U_N, uniformly for compact off-real arguments,
at every fixed order. A viable argument must explain why the cubic term
in (9) has the required relationship to L_N and must not replace one
origin average by independent matrix-entry or eigenphase randomness.
Linear orbit-noise covariance and globally entropy-small microscopic
smoothing have been checked and do not provide that argument.

Tracked files remain unchanged. Per the user's publication condition,
there is no commit or push before the main barrier is closed.
