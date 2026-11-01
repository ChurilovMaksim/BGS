# Review of the nonlinear bracket pressure result (23 September 2026)

**Claim:** `BGS-FM-006`. **Scope:** internal derivation and exact algebra; no
independent referee report, novelty assessment, or quantum universality claim.
The status authority is [`claim_ledger.md`](claim_ledger.md); the full
argument is [`nonlinear_bracket_pressure.md`](../mathematics/fixed-map/nonlinear_bracket_pressure.md).

## Proof audit

1. The map is the *ordinary-midpoint* map of `BGS-FM-001`: the factor
   `r(q+1/2)` in its momentum harmonic is essential. Its smallness,
   hyperbolicity, four fixed points, and fixed-point Hessians are imported
   from that internal theorem. The inverse Egorov convention is checked in
   Section 1 of the proof; symplectic invariance equates forward and inverse
   bracket norms exactly.
2. For smooth invariant area, Pesin's formula gives equality in Ruelle's
   entropy bound. Therefore area is the equilibrium measure of `-phi` and
   `P(-phi)=0`. Mixing Markov coding, the Gibbs bounds for `phi` and `-phi`,
   and bounded distortion yield the **two-sided** weighted estimate
   `integral(exp(2 S_r phi)) asymp exp(r P(phi))`. Fixing admissible cylinders
   at both ends and mixing the `phi` equilibrium state gives the endpoint
   lower bound. The open sets on which the stable derivative of the first
   observable and unstable derivative of the second are nonzero exist
   because stable/unstable leaves of the conjugate cat map are dense.
   Contracting contributions cannot cancel the growing contribution for
   sufficiently large `r` on these endpoint sets.
3. The four fixed-point unstable multipliers differ for each nonzero
   allowed kick. A constant-cohomology unstable potential would give the
   same multiplier at every fixed point. Strict convexity of pressure
   therefore gives `P(phi)>2 log lambda` from `P(-phi)=0` and
   `P(0)=log lambda`. This strict conclusion does not depend on an
   effective third-order perturbation error.
4. The conjugacy is constructed in a Hölder space using the split Green
   inverse of `u o S - S u`. The unstable graph transform on a smaller
   Hölder space gives the derivative of the pulled-back unstable potential
   `b=(g_pp-2 g_qq)/(2 sqrt(2))`. Pressure symmetry through `P(-phi)=0`
   cancels the unknown second-order correction to the potential. The
   Hessian at the cat map is the asymptotic variance of `b` under Haar.
5. The independent code assembles all 32 ordinary-symbol Fourier modes
   from the trigonometric expression over exact Gaussian rationals. Its
   invariant quadratic form, support-cone argument and exact two remaining
   correlations yield `V=(pi^4/2)*7834656061/500000`.

## Primary external inputs checked

| ID | Direct source and locator | Use |
|---|---|---|
| `EXT-PESIN-1977` | [Pesin, Theorem 5.1](https://www.mathnet.ru/php/getFT.phtml?jrnid=rm&paperid=3219&what=fullteng), printed p. 81 | Smooth invariant-volume entropy formula. |
| `EXT-RUELLE-1978` | [Ruelle, Theorem 2](https://www.ihes.fr/~ruelle/PUBLICATIONS/%5B51%5D.pdf), printed pp. 84–85 | Entropy bound for each invariant probability. |
| `EXT-PP-1990` | [Parry–Pollicott](https://smf.emath.fr/system/files/filepdf/AST_1990__187-188__1_0.pdf), Appendix III; Theorem 2.2, Proposition 3.2, Theorem 3.5, Propositions 4.7, 4.11, 4.12 | Markov coding, Gibbs estimates, variational principle, pressure derivatives and strict convexity. The endpoint bound is derived in the project. |

The source list and exact locators are indexed in
[`external_dependencies.json`](../literature/external_dependencies.json).

## Reproduction and limits

Run `python3 computations/verification/nonlinear_pressure_variance.py --output
build/nonlinear_pressure_variance.json` from the repository root. Compare the
output byte for byte with
[`evidence/20260923/nonlinear_pressure_variance.json`](../archive/evidence/20260923/nonlinear_pressure_variance.json).
The checker certifies finite exact Fourier arithmetic and its algebraic
all-future-lags support argument; it does not compute topological pressure,
verify the analytic proof mechanically, or establish quantum statistics.

SHA-256 of the checked proof: `311ec9ba6d0fc8dc942103971d191db4364d7b21b9d616911312320fdc8ba3c1`;
of the exact checker: `cba8fb106e372d9758b555be5f7ec05c779ce47eac78a83238016cee06b40e48`;
of the saved JSON certificate: `b2919acd61907be20674aa54788f4526e9331fe512e0c3588bcc0bb3e1f2c80c`.
The focused workspace runner returned exit code zero and wrote its source and
log hashes to the ignored `build/nonlinear-check/manifest.json`; the manuscript
builder reported PASS and 233 pages. These checks do not replace the proof.

In particular the full-lag *linear* normalization in `BGS-RES-005` cannot be
extended unchanged to the actual nonlinear map. No conclusion about an
adapted nonlinear weight follows. The required model-specific
Heisenberg-time joint-trace estimate `BGS-TRACE-005`, the fixed-strength
microscopic CUE question `BGS-BGS-001`, and a theorem covering all chaotic
systems are still open. At the actual `tau=10^-80`, pressure-gap positivity
uses the fixed-point argument: no explicit error bound justifies plugging
this number into the second-order asymptotic formula.
