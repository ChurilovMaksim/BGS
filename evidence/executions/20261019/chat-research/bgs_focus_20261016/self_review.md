# Author self-review: deep feedback Gaussian law

16 October 2026. Review of deep_feedback_gaussian.md. This is a self-review,
not an independent review. No subagents were used for this pass.

**Primary verdict: conditional on a named input.** The downstream argument
closes relative to the exact stopped identities and coefficient inequalities
of internal TRACE-077/080 and the reversal identities of TRACE-073 section 7.
Those source texts were inspected, but their complete upstream dependency
closure was not freshly reconstructed during this pass. No downstream gap
was found in this self-review. This is not an unconditional external
certification or a BGS solution.

## Normalized claims

1. Deterministic initial unitaries with max P<=C0/N and ||P-J||<=1/100:
   at log(2N)^(4+kappa)<=u=o(N), uniformly sampled disjoint directed entries
   multiplied by sqrt(u) converge jointly to independent standard circular
   complex Gaussians, with all fixed moments and empirical intensity laws.
2. In addition ||B_N||<=rho_*<1 uniformly, B_ij=S_ij conjugate(S_ji):
   an entire fixed randomly sampled principal block has the same independent
   Gaussian limit, including its diagonal and both pair directions.
3. For an additional independent uniform retained diagonal phase D_u,
   every fixed collection of Tr[(D_u S_u)^m] has the standard fixed-power
   CUE joint Gaussian moments. The powers and moment degrees are fixed.

Every probability includes fresh independent phase feedback and uniform
coordinate deletion. No fixed-u, growing-degree, deterministic initial
spectral or physical BGS claim is made.

## Dependency graph

- TRACE-080 old-state inequalities and full first-crossing rule, plus
  TRACE-077 embedded Green telescoping identity;
- Tropp 2011 matrix Freedman, Theorem 1.2/Corollary 1.3, p.264;
- exact protected-label combinatorics and rank-v covariance projector;
- Gaussian comparison by third-order Taylor expansion, with deterministic
  target covariances and no invocation of an unchecked CLT;
- for full blocks: TRACE-073 reversal expansion, uncentered block Green
  identity, four three-label Frobenius identities, then diagonal bootstrap;
- for traces: exact retained-coordinate phase integration and finite
  directed-cycle matching. No Heisenberg expansion is imported.

## Obligation matrix

| Obligation | Status | Decisive check |
|---|---|---|
| Exact underlying process and preserved unitarity | passed downstream | The feedback formula, original labels, chosen port and fresh phase are explicit; finite rational controls supplement the algebra. |
| Protective marks do not bias the unmarked trajectory | passed | Exact prefix weight (v)_L/[(N)_L (N-L)_(N-v)]=1/(N)_(N-v); conditioning is never imposed on future flatness. |
| Matrix Freedman applicability | passed | Fixed N-dimensional embeddings; predictable old-state stop; conditional phase mean zero; variance bounded in both dilation products; dimension prefactor 2N. |
| Arbitrary polynomial failure exponent | passed relative to TRACE-080 | Increase fixed D/log(2N), preserve all deterministic margins; original row/two-step exceptions are already superpolynomial. |
| Complex variance and pseudo-variance | passed | E q^2=0 and E|q|^2=1/(1-P_ee); all conjugate index orders are fixed in equation (6). |
| Rank and normalization of covariance kernel | passed | Orthogonal vectors a_e(i,j)=S_ie S_ej; projector rank v, Frobenius square v, diagonal P^2. |
| Averaged diagonal variance of disjoint entries | passed | ||(P-J)^2||F<=rho sqrt(L-1); no false uniform o(1/v) bound. |
| Stopping and Gaussian replacement | passed | Keep the full crossing, then freeze; total missing covariance bounded on the failure event; deterministic Gaussian suffix in Taylor replacement. |
| Uniform integrability | passed | Stopped entry Freedman tails for ANY fixed equality pattern; actual normalized entries <=sqrt(N); choose failure exponent larger than the prescribed degree. |
| Reversal Green coordinate | passed relative to TRACE-073 | M=(I-B)^(-1)-I compresses without Perron centering; explicit fixed-rho<1 constants; no use at a singular boundary. |
| Full off-diagonal block | passed | Four endpoint-pattern Frobenius sums, and reverse covariance B^2 with shrinking operator norm. |
| Diagonal bootstrap noncircularity | passed | First off-diagonal mixed moments, then v(P^2)_II variance and diagonal/cross covariance; only moment bounds are used for unknown diagonal entries. |
| Initial diagonal term in the final CLT | passed after correction | Use uniform second moments at v0, giving O(u/v0). The initially tempting uD/v0 estimate is insufficient for all u=o(N). |
| Uniformity in the final depth window | passed | A sequence of offending depths would contradict the theorem along that sequence; bounds uniform for all equality patterns of fixed size. |
| Trace corollary | passed | Retained D forces at most K free vertices; d<K patterns vanish; directed edges match uniquely into cycles. |
| Original frozen spectrum and Heisenberg powers | not addressed | No quantitative comparison uniform in degree ~u or ~N; phase removal is not proved. |
| Novelty/world priority | not addressed | Limited primary-source searches are not a novelty verdict. |

## Computations, actual scope

The exact rational checks are supplementary checks of finite identities,
not substitutes for the proofs or upstream assumptions.

- feedback_exact_run: four prescribed rational unitary matrices at sizes
  2..5, 84 complete feedback transitions, covariance projection and index
  identities. Protected marks: 65 parameter cases, 10,081 full deletion
  prefixes and 57,611 compatible ordered mark tuples, N=3..7.
- feedback_extension_run: 16 three-label Frobenius identities, four diagonal
  projector identities, 42 reversal feedback expansions, 12 Green
  compressions and 27 ordered inverse expansions in their inverse domain.
  All nine transitions from dimension 3 to 2 are explicitly outside that
  inverse domain, as expected. The initial reversal Green inverse at size
  2 is also absent; it is not silently counted as a passed inverse case.
- Leading trace combinatorics: all 209 pairs of integer partitions of
  common total K=1..6; all 93,663 advanced-label permutations; 29 nonzero
  matching cases, with exact factor product p_m! m^(p_m).

Both exact execution manifests passed the computation-audit validator.
Executed source, contracts and results are hashed in those manifests.
No Lean compiler, formal proof or C++ result is asserted.

Separately, two_channel_run is exploratory floating-point evidence, not a
check of (24). It executed 1,350 trajectories (150 per case) at N=49,121,225,
with NumPy 2.3.5, PCG64 seed 2026101602, one core/thread, in 8.85 seconds.
For the symplectic involution the three sample means were 0.517, 0.508,
0.489; for frozen row-permuted Fourier starts they were 0.479, 0.493, 0.503.
The excluded symmetric-Fourier control gave 0.337, 0.306, 0.320. The
nonreversal samples' uniform KS statistics ranged 0.054..0.078; the
symmetric control's ranged 0.266..0.311. These small samples discriminate
the symmetry control; they do not establish the open uniform limit.
Finite startup/cutoff effectiveness is not claimed. This execution
manifest also passed the validator; raw samples are retained.

## Exact frontier and failed shortcut

The first small-channel target is the law |(S_2)12|^2, whose Haar reference
is Uniform[0,1]. It remains OPEN, as does its clock coupling. For every
2-by-2 unitary the reversal channel has eigenvalue 1, so the small reversal
Green estimate cannot be continued to that state. A separate boundary law
is necessary.

The extra retained phase in the trace corollary also cannot be deleted:
E Tr S_u=(u/N)Tr S_N exactly. The existing project symplectic involution
has Tr S_N=sqrt(N), P=J and reversal norm N^(-1/2); its unphased trace
moments therefore need not be CUE even though the Gaussian block theorem
applies. This is a new application of the existing construction, not a new
construction or a counterexample to the prescribed frozen physical map.

The strongest safe result is the conditional theorem package above.
The cheapest next analytic check is the first two-channel transmission
moment under the exact deterministic-start hypotheses, retaining the full
random denominator. Matching fixed-degree entries, scalar uniformity and
mean clock alone do not close that implication.
