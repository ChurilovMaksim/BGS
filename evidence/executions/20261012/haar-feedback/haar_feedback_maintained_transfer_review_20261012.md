# Maintained-transfer review of the Haar feedback clock law

Date: 12 October 2026. Scope: read-only fidelity review of the maintained
mathematical transcription after independent reconstruction of the original
candidate. This is a separate internal review artifact, not external peer
review or a new upstream proof audit.

## Input identities

Maintained source:
`/workspace/scratch/06745ba532e4/BGS/mathematics/haar_feedback_clock_law_20261012.md`.

Reviewed maintained SHA256:
`41015612e954913ea1fcc8b2a44962b9143bbcf0ae990da503e9d42baa1e8857`.

Original candidate and preserved evidence input both have SHA256:
`7a717c01207e12cf8c7ac6c2cc2f0ac95b625d36a0b3e5bdfd30ae72554b8c22`.

Original independent reconstruction:
`/workspace/scratch/06745ba532e4/research_session/haar_feedback_independent_review_20261012.md`,
SHA256 `5e2e6eb96019c68233c60690a5476261520a3e506227861407656032235dbfb1`.

Base repository HEAD:
`6bd6c3129b0b69eeb4ec5243a7e6e2eba75865f7`.

## Verdict

**PASS for mathematical fidelity.** Sections 1-6 preserve the independently
reconstructed result, including its hypotheses, singular dimension regime,
atom, moment threshold, deterministic-uniformity argument, and order of
entropy-transfer limits. No substantive loss, unproved strengthening, new
circular dependency, or incorrect noncommuting manipulation was found.

One minor editorial point remains in Section 6: specify a **nonzero**
nonnegative continuous test function compactly supported inside the forbidden
interval. The current wording omits “nonzero”, while the following positive
expected integral uses that choice. Such a function exists and the gap proof
is valid; this is not an extra hypothesis or a mathematical gap.

For standalone clarity, Section 4's finite-moment criterion may explicitly
quantify over probability measures on `[0,infinity)`. This is already the
relevant class because `T>=I` and all clock empirical laws are positive.
Bounded first moments then imply tightness as stated. No correction to the
application is required.

## Preservation checks

| Component | Fidelity finding |
| --- | --- |
| Phase absorption and sequential elimination | `U-hat=diag(I,W_E)U` acts on eliminated rows; the same linear system in the disk gives sequential/block agreement, followed by analytic continuation at the regular boundary point. Fixed phases, predetermined retained sets, and independence from initial Haar are retained. |
| Delay derivative | `T=S^*F_u'(1)=I+X^*X`; the angular derivative factor is correct. At full size `T=I`. |
| Cayley/graph order | `S=(A-i)(A+i)^(-1)` and `X=B(A+i)^(-1)` retain the correct right inverse. No commuting assumption about the rectangular block or `G,D` has entered. |
| Complete Jacobian | Real powers `det(I+A^2)^q det(G)^q`, block triangular square-root argument, Schur determinant, and transformed exponent `-(N+u)` are retained. |
| Independence | `S` is Haar and independent of `T`; `Q` has the same law and is independent of `S`. No independence of `(T,Q)` from `S` or across depths is claimed. |
| Gaussian ratio and spectrum | Wishart degrees remain `2u,q`; (10) is an equality of spectra, not an incorrect equality of noncommuting matrices. |
| Rectangular SVD addition | Powers `sigma_l^(2|q-u|+1)` and squared Vandermonde are correct. Transposition exchanges the two rectangular regimes as a real isometry with the same singular values. The direct reconstruction supplies the two-complex-direction determinant explicitly. |
| Atom and moment threshold | Exact rank gives `max(0,2-N/u)` at `u/N`, only for this Haar ensemble. For `q>0`, finite trace moment iff `k<u+1`, with both necessity and sufficiency stated. The full-size exception remains explicit. |
| First moment | Projected Gaussian shape `u+1`, `E W^(-1)=I/u`, and `E T=(N/u)I` are preserved. |
| Whole-trajectory flatness | The bound `b_N(K)=N^3(2N)^(-K(1-1/m))` uses only marginals and a union bound; no independent-depth assumption or future-event conditioning is introduced. |
| Deterministic uniformity | (15) follows from the canonical theorem for every deterministic unitary sequence, with common tolerance depending only on fixed `L,K,kappa`. This is exactly the diagonal-choice argument required for integration over initial laws. |
| Weak-law addition | Compact reference support and continuous polynomial moments, tightness, higher fixed moments for uniform integrability, and compact moment determinacy prove a uniform finite-`L` criterion. No growing moment order enters the probabilistic theorem. |
| Entropy transfer | The initial law is independent of fresh phase/order randomness. Binary entropy applies to product laws with the same relative entropy `D_N`; `q_N=0` is handled by absolute continuity. The `O(log N)` proof lets fixed `K` tend to infinity only after `limsup_N`. |
| Microscopic obstruction | Haar conditioned on a prescribed microscopic gap has entropy `O(1)` and cannot converge locally to intensity-one Sine_2 at that origin. The test-function argument avoids exceptional-event moment transfer. It makes no origin-averaged claim. |

The additions are explanatory proofs of already stated implications. The
maintained text does not assert growing-order control, a finite-N compact edge,
unrestricted exceptional-event delay moments, or high-probability all-time
flatness for one prescribed finite `K` throughout the `O(log N)` class.

## Exact dependency boundary

Sections 1-3 are independently reconstructed finite-dimensional algebra and
probability identities. They require neither TRACE-060 nor an intensity-gap
premise. Standard Gaussian Gram densities can be derived by QR/Cholesky as in
the original independent review.

The convergence claims of Sections 4-5 use **only the published conditional
all-fixed-order TRACE-060 theorem and its published full-depth reference
measure as asymptotic inputs**. Their precise source identities are:

* `mathematics/conditional_clock_universality_20261011.md`:
  `8517456f3c4b7b5e6243d6f644b705ea80e4267e92b6e0ab157db0bc7c1d08dc`.
* `mathematics/full_depth_clock_measure_20261011.md`:
  `d7d13458f1c5a7a31ed3632bb6e54668dca3b85610ea0f48b28e84dbd5f0e3e2`.

Those statements are used with their fresh independent original phases,
uniform independent coordinate order, `F_N=zU_N`, and `T_N=Q_N=I` conventions.
Their arbitrary-deterministic-initial-sequence scope was checked in the
original review. This transfer audit does not re-prove their upstream moment
or finite-word arguments. The newly proved Haar flatness probability
discharges their explicit intersection premise for Haar initial data;
entropy and deterministic uniformity then extend the clock conclusions to
independent initial laws with relative entropy `O(log N)`.

No physical TRACE-055 hierarchy, signed TRACE-005 theorem, deterministic-map
flatness input, microscopic eigenphase law, new literature priority claim,
manuscript audit, or global BGS argument is part of this verdict. The
prescribed-origin obstruction is an explicit limitation of the entropy class,
not a deterministic BGS counterexample.

Section 7 records separate finite controls. Their execution and verifier
implementation were not re-audited here, and none is used in the mathematical
acceptance above. The maintained section correctly states that those finite
checks prove none of the probability-limit or entropy claims.

No repository file, frozen candidate, or preserved evidence input was edited
by this reviewer. No additional agents or numerical regression were run.
