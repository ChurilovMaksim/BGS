# Independent internal review: critical noise and fixed-degree projection

Base: `0f3ac906f804a69006edd95194ea32fc6c5f601f`.
One fresh read-only reviewer reconstructed the candidate arguments without
being supplied an author verdict. Three successive passes by that same
reviewer covered the initial implications, P5--P7, and final P8. They are
not three independent reviewers or external refereeing. The author
performed a separate self-review and source normalization check.

**Primary verdict: proved as written**, under the exact inherited inputs,
for the final mathematical bodies of FLOW-018 and FLOW-019. The only
initial proof defect was a negative-alias majorant. The corrected
bound is $e^{-\tau|r|(|r|-1)/2}$; for $r=-1,s=1/2$ the old bound would
incorrectly bound a weight of one by $e^{-\tau}$. It was repaired before
acceptance, without changing the theorem domain.

## Obligations and dependencies

| Obligation | Inputs | Review result |
|---|---|---|
| S1 covariance normalization | Periodization and uniform origin | Passed; coefficient is N^-2 and conditional means are retained. |
| S3 exact second moment | Prior clock kernel and two angular constraints | Passed; no independent-trace approximation. |
| S5--S7 compensation and pair rate | Finite geometric square | Passed; every negative mesh mass equals its Bragg mass. |
| S8 leading joint measure | q=±1 concentration and higher-q tails | Passed; t→0 is retained with Nt→∞. |
| S9--S10 critical law and all moments | Corrected alias bound and Fredholm/Hadamard controls | Passed; the unconditional law is a phase mixture. |
| S11 stopped moment induction | Noncolliding ordered lifts and drift monotonicity | Passed; localization preserves the nonnegative recursion. |
| S12 synchronous contraction | Particle noises and paired cotangent differences | Passed; not identical matrix noise. |
| Original-chain critical corollary | FLOW-017 C10--C12 and FLOW-016 costs | Passed; C10 does not require the separate Sine reference assumption. |
| S14 Abel sign and coefficient | Positive-frequency S6 and TRACE-007 floor | Passed; no time monotonicity inferred. |
| P1--P4 fixed-degree estimate | Diaconis--Evans 2.1(a), D5, FM-013 | Passed; 2Q≤N and fixed Q are essential. |
| P5 compact CUE covariance rate | Cross-block determinant expansion | Passed; initially N>8R, finite smaller dimensions absorbed. |
| P6--P7 actual projected statistic | Bounded finite-span evaluation and Haar contractivity | Passed uniformly for all t≥0; Schwartz rate not asserted. |
| P8 local complement obstruction | P5/P6 and prior strict clock Laplace defect | Passed; point evaluation, not heat inversion. |
| Complete actual complementary/noise defect | Unproved model-specific estimate | Not addressed; OPEN. |
| Full inherited-claim referee audit, world novelty, analytic Lean | Outside this audit | Out of scope. |

## Independently reconstructed critical steps

For the cross-kernel Fourier integral, the constraints are $s=-r$ and
$l-k=m-rN$. Their weight product is $e^{-trm}$ and the number of
ordered pairs is $(N-|m-rN|)_+$. The squared mean survives precisely
when $N\mid m$. In particular $0<m<N$ gives $m(1-e^{-tm})$.
This independently fixes the sign and normalization.

Writing $d=m-qN$ turns the negative mesh mass into
$N^{-2}e^{-\tau q^2}(\sum_{l=-M}^M e^{tql})^2=a_{q,N}^2$.
For q=±1, $\tau a_{1,N}=(1-e^{-\tau})t/(2\sinh(t/2))\to1$;
the negative profiles concentrate at zero. Higher-q rescaled variation
vanishes. These prove the three-atom leading measure and sharp rate.
For the Abel weight, the mesh square replaces $tq$ by $tq+2s/N$;
$H_N'(x)=2N^{-1}\sum_{l=1}^M l\sinh(lx)>0$ proves the sign.

For stopped $H_r=N^{-1}\sum_j\Delta_j^{2r}$, paired cotangent
monotonicity makes the drift nonpositive. Ito gives
$\mathbb EH_r(t\wedge\sigma)\le r(2r-1)N^{-1}
\int_0^t\mathbb EH_{r-1}(s\wedge\sigma)ds$.
Nonnegativity permits the stopped-integrand bound; induction and Fatou
prove S11. The same pair sign gives the martingale-free contraction
for two starts using common particle noises. Convex interpolation stays
inside the ordered chamber.

For P5, a non-block permutation crosses in both directions. For Laplace
tests, $D(z)=\det\left(\begin{smallmatrix}A&zB\\zC&D_0\end{smallmatrix}\right)$
has $D'(0)=0$, and its second derivative has at most $n^4$ terms,
each with two small cross entries and an $(n-2)$-minor bounded by
Hadamard. The double Fredholm weights sum to $(2H)^n/n!$, making
the printed majorant summable. Periodic covariance integration then
gives $C_F/N$, without distant-window independence or an ergodic rate.

For each fixed Q the stable Gram product has both degrees at most 2Q;
its Gaussian Gram matrix is positive definite. D5 has coefficients a+b/N,
including the cancellation of a zero merged index's p_0=N. Haar
self-adjointness makes the span reducing. If D_Q bounds its coefficient
matrix and lambda_Q is its Gram minimum eigenvalue, one admissible P2
constant is $\sqrt{d_Q}\max(1,K)^{2Q}D_Qe^{D_Q}\lambda_Q^{-1/2}$.
For P6, apply bounded evaluation to the projection of F-b_N and use
Haar contractivity for every heat time. For P8, orthogonal projection
makes the complement's norm at most C/sqrt(N), while its clock value
approaches -delta_f by the exact narrow-window value and P6.

## Source and finite-execution scope

The reviewer reopened the primary Berkeley Diaconis--Evans PDF and
checked Theorem 2.1(a) and its proof on printed pp.3--4, including the
endpoint 2Q=N. The author additionally read pinned Forrester and
Katori--Tanemura pages and visually inspected Forrester page 16, as
recorded in the source check. The reviewer did not independently reopen
those two PDFs or certify the reported Forrester source inconsistency.
The adopted kernel was reconstructed mathematically from the prior
project definition. Existing analytic dependencies keep their earlier
review grades.

The reviewer inspected and executed the earlier verifier at SHA256
`4a0cf236de852a5bdcad4e0925fccc602bbe3219abdca7a941c8fa4fa5d09768`,
with bytecode writing disabled and an in-memory import/run. It passed
168 exact angular selections, 36 mesh masses, 105 generator jets,
20 radial polynomial controls, 12 stable Gram cases, 18 numerical
kernels, nine band variances and four sharp-rate diagnostics. The source
also checks 72 Abel summand signs; the reviewer returned a full PASS
without separately listing that count. Later P5--P8 passes were analytic,
with no additional execution. The subsequently added 30 exact generic
cross-block Taylor surrogates are part of the author's bounded final run,
not retroactively attributed to the reviewer. These surrogates are
rational matrices with bounded entries, not sampled CUE spectra.

No finite execution certifies P5, all-Q bounds, analytic limits, world
novelty or BGS. There was no huge-chain or Brownian trajectory simulation.

## Accepted revisions and promotion

The initial complete FLOW-018 body, including S14, was accepted at
`33b40388519101320b8a071f1b57c56a7e7906afeb22386d23d1b7a06ac89647`.
FLOW-019 before the P5 addition was accepted at
`27ff48dc3dd463dc6578bd68687d7e42b9133542174fae394dbd9526763cdc11`;
the P5--P7 pass pinned
`1678ad876be08c6a1f81cad8186a782422fd1c1b2187df8cda1e3b7e1a689b45`.
The final P8 and small-N clarification were accepted at
`9d1474ff7432308aa1fad0de738464802f70e2671e091cd133fdda12b52778ed`.
Only the two proof status headers were promoted afterward; mathematical
bodies were unchanged. Final source pins follow.

| Source | Final SHA256 |
|---|---|
| `mathematics/clock_structure_and_noise_scale.md` | `08f2d087da3f471581339bd8a83db12a1f07abf7c877f39a723f36ea0de976fb` |
| `mathematics/fixed_degree_heat_projection.md` | `670bdf1e6815ae8add447706726c556874bc7d0f0f562721cb0a3e2b6655f84e` |
| `mathematics/quadratic_noise_clock_limit.md` | `4d8d4ed8ce94a360152b9d7ffd4c8e004c185da5f512df5a58b5ceaa6acdfdd3` |
| `mathematics/microscopic_noise_removal.md` | `f90d7b5ce1d24a05947f74fb101f19c0f40fc02ce13868f00576a1700eb96dfd` |
| `mathematics/local_moment_transport.md` | `dcbf7ecdf146186188c03e4076d6aec8fe8bcf71397016a32c70049e9801757a` |
| `mathematics/coboundary_all_order_limit.md` | `ac59bc85917aa5414cf1d3b6498a08af9bd65464213042e6d8379e4a86b3176f` |
| `mathematics/fixed_time_wavepacket_trace_bound.md` | `dea4b671554a5726756e4d1871b427469b4a3ff960fed52ac4a425a0f481a4b4` |
| `literature/critical_noise_sources_20261005.md` | `750d61b4b4b110336358a541950416b3f744e861b87dc2105915b9d48ec93453` |
| `computations/verification/clock_structure_and_heat_projection.py` | `9df506c8b3595a19776098fce4e533177c95374839083f15e92a349df20d298f` |
| `computations/verification/microscopic_noise_removal.py` | `fe7aad5ceadcaece8fe9fa2e9cc24b456b26b30615dfd788376542a0703b4158` |
| `computations/verification/quadratic_noise_clock.py` | `eb6879234d5fb396590eb0d390eee08d3cf035c3eba3373cfde83fcd13246d07` |

The strongest safe results are the entire stated clock/matched-family
control and every fixed-Q actual projected estimate. Actual clock matching
and the actual unprojected signed complementary estimate remain open.
Neither additional finite-Q checks nor a small Haar norm close that edge.
