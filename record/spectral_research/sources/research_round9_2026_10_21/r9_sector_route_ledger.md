> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round9_2026_10_21/r9_sector_route_ledger.md`. Embedded SHA256: `ad07baa0fae652ea65f15e41dc931840a7d6046ebf30abac9a62d819e80b41e2`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/arithmetic.md).

# Round 9 sector/coherence route: completed work and exact remaining gap

21 October 2026. Branch /root/r9_sector_coherence.

## Starting point and unchanged target

The parent supplied the Round 8 master checkpoint
SHA-256 b1dc28374e62fb77c59d7da04f638916e43e0ac5809c68ea02c501fb92436a20.
The assignment was to attack the fully weighted pair sum using the
actual adjoint/sector structure, without converting quantum amplitudes
into a Markov model.

Let

$$
 \phi(\xi)=e^{-1/(1-\xi^2)}\mathbf1_{|\xi|<1},\qquad
 I=\int\phi,\qquad
 b_*(x)=\frac{|\mathcal F^{-1}\phi(x)|^2}{2I^2},\quad
 w=|\widehat b_*|^2.
$$

The first original-family estimate is still

$$
 \frac1{N^2}\sum_{1\le m<2N}w(m/N)
 \left(|\operatorname{Tr}U_N^m|^2-\min(m,N)\right)
 \longrightarrow0
 \quad(N\to\infty,\ N\ {\rm odd}).
 \tag{0.1}
$$

This branch did not prove (0.1), disprove it, or construct an original
fixed-test countersequence. The exact original parameter and family
remain unchanged.

## 1. Previously completed routes were identified before reuse

The all-odd Weyl endpoint-fiber proof was read. Its central projection
and sector autocorrelation bounds are exact, but their sum retains
the full quantum coherence. In particular, the pointwise sector bound
by the central sector is not an estimate of the weighted total at
$m\asymp N$.

The next proposal was to use cyclic rotations of physical closed
paths to obtain the factor $m$ missing from simple identity-sector
returns. A history search found that this route had already been
fully completed in Round 5. Its complete physical-cycle proof was
then read. It already obtains the full linear ramp from genuine
distinct cyclic rotations, and controls the reversed-path class.
No new theorem was claimed from that rediscovery.

Likewise, the existing long-directed-arc reconnection proof already
handles growing reconnection counts of order $\sqrt N$ after literal
path identification. Extending the marking count by absolute
estimates loses control of exceptional repeated words and their
large coherent multiplicities. The small signed three-arc estimate
and its two opposite large components were already recorded.

The occupation-sector determinant identity was also already known:
literal arc reorderings preserve occupation. Their complete
resummation does not determine phases between different occupation
sectors. Another same-occupation rearrangement would not change the
stuck step in (0.1).

Finally, the apparently promising smooth Planck-size perturbation
argument was found in its complete Round 3 form. It already includes
uniform QE along the path, eigenangle crossings, exact global mean
rotation, and full $H_{\rm diag}$ transfer with the needed moment
bounds. This was communicated immediately to prevent duplication.

## 2. Actual new construction in this branch

The useful change was to remove the fixed smooth-symbol-family
requirement rather than repeat the existing QE argument.

The completed continuous-symbol note proves:

1. For each fixed real smooth $a$,
   $\limsup\|Q_N(a)\|\le\|a\|_\infty$, by quantizing
   $a^2+(M^2-a^2)=M^2$ and using positivity of squares.
2. Any fixed real continuous torus function $v$ has Fejér polynomials
   $v_j$ and a slow all-odd diagonal $j(N)$ such that
   $B_N=Q_N(v_{j(N)})$ is uniformly bounded and uniformly
   approximable in operator norm by each sufficiently accurate
   fixed polynomial quantization.
3. The actual paths $e^{isB_N/N}U_N$ obey uniform QE for their
   varying generators, in all eigenbases and at degeneracies.
   After the exact scalar rotation, the summed angle displacement
   tends to zero and the maximum microscopic displacement stays
   bounded.
4. The endpoint local laws approach each other. If one endpoint
   has full $H_{\rm diag}$, its higher local-count moments transfer
   and prove the full factorial-moment comparison. Thus full
   $H_{\rm diag}$ holds at one endpoint exactly when it holds
   at the other.
5. An explicit positive coherent-state quantization $Q_N^+(v)$
   of the continuous target provides a canonical rough endpoint.
   The actual analytic diagonal endpoint differs from
   $e^{iQ_N^+(v)/N}U_N$ by $o(N^{-1})$ in operator norm.

The theorem permits every fixed-stage analytic accuracy condition
to be added to the same threshold sequence. It does not need a
quantitative QE rate and does not silently transport a varying
rough symbol through an Ehrenfest estimate.

## 3. Joint advance with the root analytic branch

The continuous target

$$
 v=-\frac1{2\pi}\sigma\circ\Psi^{-1}
$$

comes from the first scalar coefficient of the old continuous
dominated graph. The root branch constructed the exact analytic
amplitude for each actual polynomial multiplier. This branch
independently audited that construction, including:

- the exact horizontal weighted Weyl shift and its signs;
- flattening a Weyl word before taking real-$h$ derivatives,
  avoiding an accumulated spatial strip loss;
- exact integer covariance and the original coherent/Abel
  sector construction for the new exponential;
- the scalar transformation law
  $\sigma\mapsto\sigma+2\pi v_j\circ\Psi$;
- one all-odd choice of thresholds giving uniform
  $\widetilde\gamma_N/\gamma_0=1+o(N^{-1})$ and scalar products
  $1+o(1)$ for every $m\le BN$.

This closes the particular continuous-cocycle regularity and
actual-unitary-realization issue left open in Round 3, at that
precision. It still leaves the coherent principal action sums.

## 4. Precise restrictions on what may be inferred

Uniform relative error on each orbit is insufficient after an
absolute sum over exponentially many orbits. A global signed
error estimate has not been obtained.

The new spectral equivalence is unconditional for bounded local
Laplace observables, and conditional on one complete
$H_{\rm diag}$ side for the all-order moment comparison.
It is **not** an unconditional assertion that the second factorial
moments at the two endpoints differ by $o(1)$.
Proving only one pair estimate for the normalized endpoint would
still require a separate uniform-integrability argument to transfer
that moment alone. The proof does not hide this distinction.

The deleted-clock determinant obstruction was independently accepted
in its auxiliary scope. It shows that complete direct determinant
autocorrelation, even exactly equal to CUE for every complex
argument, does not force microscopic pair statistics or inverse
determinant behavior. It is not a counterexample for the prescribed
Fourier--Jacobi family.

## 5. Artifacts produced by this branch

- r9_sector_continuous_symbol_stability.md: full new theorem,
  exact positive quantization, complete proofs, and source hashes.
- r9_sector_analytic_normalization_independent_audit.md:
  independent raw-proof audit of the root analytic construction.
- r9_sector_deleted_clock_independent_audit.md:
  independent audit of the auxiliary determinant obstruction.
- r9_sector_route_ledger.md: this route history and remaining gap.
- r9_sector_positive_quantization_check.py: independent finite
  modular-midpoint checks of the positive-frame Fourier identity
  at $N=3,5,9,15$, including aliased frequencies. Maximum matrix-entry
  discrepancy was below $1.45\cdot10^{-15}$ in double precision.
  This verifies conventions only; it is not asymptotic evidence.

No master document or historical source was edited.

## 6. Additional actual input hashes

Hashes for the primary norm/QE and graph sources appear in the
proof and analytic audit. Additional old routes inspected here:

| Source | SHA-256 |
|---|---|
| research_round8_2026_10_21/round8_continuation_ledger.md | 84469e7eb461cd3c18929424cf3bcdce8e1e6b525d8d077bf61a01adc7d652e7 |
| research_round5_2026_10_21/dual_directed_encounter_growing_order_cancellation.md | f0ffa2acc3e4b66b75620ee116a20cf8793c4d7efc40d5db67ded4259436c4e4 |
| research_round5_2026_10_21/dual_directed_encounter_marked_unitarity_resummation.md | f3e6a9e37739a557c0a065ef685b9e341804f630ddff30a3618e24e1e65876c9 |
| research_round5_2026_10_21/arithmetic_occupation_resummation_obstruction.md | 1aeefa2931e83e4368ecdc4b5b0aa3b31c81beef8eb6fbb69ea825e08e5b0556 |

No historical-priority claim is attached to the new construction.
