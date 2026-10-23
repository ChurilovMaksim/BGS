# Adversarial author self-review, 17 October 2026

This is self-review in the same session. No fresh reviewer, subagent, external
referee, Lean kernel or independent certification was used. Finite experiments
are evidence for their stated identities, not substitutes for proofs.

## Primary verdict

**Conditional on named project inputs:** the dimension-uniform feedback
theorem follows from the local Green, row-energy and two-step identities in
TRACE-077, TRACE-080 and TRACE-079, and the covariance identities of the
16 October external checkpoint. The new proof supplies the missing current-
rank moment estimate and first-exit marked union bounds. Those changes remove
the previous log(N) cutoff. The upstream local algebra is not freshly
independently re-audited here; its exact files are pinned in proof_inputs.json.

The finite-dimensional spectral-averaging/Abel reduction and the auxiliary
iid counterexample are separately reconstructed below. No obligation toward
full BGS is marked closed by these results.

## Normalized claim cards

DU: deterministic S_N in U(N), fixed max P_N<=C0/N and ||P_N-J||<=1/100;
fresh uniform port and phase elimination. For every A, constants independent
of N give failure C_A m^(-A) down to every m>=m_A. For any u->infinity,
u=o(N), distinct sampled endpoints have Gaussian limits in all fixed moments.
The entire principal block additionally requires a fixed initial reversal
gap rho_*<1. Independent retained row phases are REQUIRED for the fixed
trace-power corollary.

SA: any finite deterministic U in U(N), full iid uniform coordinate phases,
source-weighted eigenvector sampling. Open ratios satisfy exact identities,
and transmission law tends to Uniform iff the bounded ratio tends to
Beta(1,2). Typical-eigenvector empirical Exp(1) convergence is a sufficient
input, not a conclusion from startup flatness.

HP: positive rooted-word Wick law or iid circular entries. Fixed positive
collision tilts condense when m/log(Nm)->infinity. For any fixed matching
order K and alpha>0 a fixed bounded circular law can match Gaussian moments
through order 2K yet have exponentially larger trace second moment at
m/N->alpha. These matrices need not be unitary.

## Dependency graph

DU: local project coefficient bounds -> stopped Green expansion ->
rank-sensitive high moments; protected prefix identity -> depth-u union;
both -> unconditional dimension-uniform corridor -> shrinking deep gap ->
covariance projector + Taylor comparison -> Gaussian entries/moments.
Optional reversal Green compression -> entire sampled principal block ->
extra row phases + exact vertex balance -> fixed-power trace moments.

SA: rank-one phase derivative -> weighted spectral change of variables ->
open/closed ratio identity; scalar circle kernel -> bounded Abel transform ->
injectivity; typical empirical intensity W1 input -> source/target averaging
-> Beta ratio -> uniform transmission. The intensity input remains open.

HP: exact rooted-word expansion + Gaussian finite kernel benchmark ->
collision deficit bounds -> positive-tilt condensation. Rooted BEST clique
count + moment-preserving positive density construction -> exponential
failure of every prescribed finite-order iid moment comparison.

## Obligation matrix

| Obligation | Status | Reconstruction / limit |
|---|---|---|
| Noncommutative martingale expansion | Passed, author proof | One-Y trace terms have zero conditional mean; every remaining word is bounded by trace Holder. The induction uses p>=4 even, r^j<=r^2+r^p and sum binom(p,j)p^-j<1. It does not assume commuting increments. |
| Current rank versus ambient N | Passed | Each embedded Green increment is zero outside the v retained coordinates; dilation rank <=2v. Summing v^(2/p-2)log(2v)^2 gives m^(-1+2/p), with no N prefactor. Future retained projections occur only after chronological summation. |
| Matrix maximal probability | Passed | ||dilation(Z)||_p^p is a nonnegative submartingale. Stop at its first crossing and use conditional Jensen up to the finite terminal step. No strong Doob constant is needed. |
| Protected prefix law | Passed | Exact falling-factorial identity holds for each deletion prefix including all its phase values. It does not need a random or permutation-invariant initial matrix. |
| First crossing, no future survival bias | Passed | At a fixed first-exit depth u, conditional uniform retained marks convert the expected number of bad rows/pairs to u or (u)_2 times a protected-mark probability. Sum over u afterwards. No event of future success is conditioned upon. |
| Row drift rescaling | Passed | Protected source: conditional raw moments multiply by v/(v-1); after Y=(v-1)R' the factor cancels to -R+v E DeltaR. This gives (13), rather than an uncontrolled omitted-endpoint error. |
| Pair and diagonal drift rescaling | Passed | The exact factor is v/(v-d), d=1 or 2. The coefficient alpha=(v-1)/(v-d) lies in [1,2] and yields (16). Diagonals use d=1. |
| Summable depth tails | Passed | Row/pair tails are exp[-c sqrt(u)/log(2u)] times u or u^2. Entry tails are a chosen inverse power of u. Their sums are uniform in N. Constants K and the sufficient m_A depend on A. |
| Green inverse at full crossing | Conditional on named input | Old-state Neumann bound from TRACE-077/080 gives new inverse norm <3 before or at crossing. The full crossing is never clipped. |
| Local coefficient inequalities | Conditional on project proofs | Precisely (4),(5) and Green expansion are imported. Current finite tests are not claimed to independently establish their continuous-Haar phase integrals. |
| Shrinking-gap use in covariance | Passed | Use prefix-adapted events {rho_v<=epsilon} and the old stop mask before averaging marks at v. Bounds on their complements cost their probabilities since the full active covariance sum is O(1). This avoids claiming marks stay uniform after conditioning on the entire future good trajectory. |
| Terminal-dimension moment transfer | Passed | The actual terminal normalized entry is bounded by sqrt(u), not sqrt(N); failure C_Au^-A permits any fixed prescribed moment. A need not be uniform over all moment orders. |
| Reversal extension | Conditional on named prior identities | Jointly stop its Green process with the old intensity stop; use rank estimate with 8H^2 and remainder 128H^3. Combine probabilities unconditionally. Constants may depend on fixed rho_*<1. |
| Smooth-test rate | Passed, author proof | Initial term O((u/N)^(1/4)); covariance gap O(sqrt(u/N)+u^-1/8); jumps O(log(2u)/sqrt(u)); target variance O(sqrt(u/N)+1/u). These imply (25) for bounded C3 tests. |
| Scalar spectral averaging normalization | Passed | At a simple branch dtheta/dalpha=w_i. For a fixed non-pole theta there is one closing alpha and one eigenvector with nonzero source. Integrating theta then the remaining uniform phases yields the open law without an extra N. Diagonal U is a dark-state control: Q=1, not N. |
| Simple spectrum and dark states | Passed | Coordinate compressions span each repeated eigenspace, so some diagonal perturbation splits it; generic phase points are simple. Dark states have zero source weight and are excluded only through that zero factor. |
| Scalar angular derivative sign | Passed | In z=exp(i beta), -i conjugate(zH) d(zH)/d beta=1+||X||^2. Replacing beta by the eigenangle theta changes sign; this is why beta is explicitly used in the note. |
| Kernel endpoints / injectivity | Passed | T=0 maps to Y=0; T=1 maps to Y=1/2. Weighted half-integer moments determine sqrt(t)mu, and total mass fixes mu({0}). No lost endpoint mass. |
| Abel inversion atoms | Passed with stated restriction | The density inversion is asserted at continuity points t in (0,1), with right limits for interior atoms. Endpoint atoms are read from Y's atoms separately. |
| Quantitative W1 source weighting | Passed | K_f(x,y)=x f(y/(x+y)) is separately 1-Lipschitz when f(0)=0. Its product-coupling error is <=2W1; removing the diagonal costs <=1/[4(N-1)]. |
| Empirical weak-to-W1 upgrade | Passed | Exact mean 1 and limiting mean 1 imply tail control via integral(x-R)_+=1-integral min(x,R). Uniform bound W1<=2 permits expectation. Pooled intensity convergence alone does not control a typical eigenvector's squared empirical measure. |
| Two-ratio abstract counterexample | Passed, scope limited | Exp and inverse-Gamma(2) yield the same source-weighted one-ratio law. Neither is asserted to arise in the physical phase ensemble solely by this construction. |
| Collision condensation count | Passed | A non-loop edge is <=m/2 by balance. For a dominant loop m-r, non-a positions <=r-1, deficit >=r(m-r). Far tables lose >=m^2/4. Exact finite integer tests include the explicit remainder. |
| Gaussian rate normalization | Passed with standard external input | The finite kernel derivation has the 1/(m+1) factor and applies to m>=N; m=1 gives h=N. Version/source mapping is recorded below. |
| Clique root multiplicity | Passed with standard BEST input | m t product(degree-1)! / product edge! gives [(Lq)!]^q/(L!)^(q^2), including loops and periodic roots. Six exact clique enumerations match. |
| Arbitrary finite matching order | Passed | Corrections to a truncated exponential density are made on disjoint intervals through an invertible Vandermonde limit. The added far atom has bounded low-order corrections and arbitrarily large next moment while positivity is retained. |
| BGS / fixed two-channel law | Not addressed by DU; open in SA | Neither large-u Gaussian scattering entries nor an iid high-power counterexample proves phase-ensemble eigenvector statistics or the frozen all-order spectral hierarchy. |

## Executed finite evidence

transmission_run_v2: 50 exact residue/mixture checks, including an independent
closed 2x2 eigenvector calculation; 9 source closures and scalar derivative
checks in U(2..4); 20 ordered-pair Schur closures; 9 sampling normalizations.
The first run failed in SymPy's integer polynomial domain when shifting by
a rational pole. It was an implementation domain error, fixed by explicitly
using QQ; its failed manifest and stderr are retained. Both mechanisms and
their input hashes are visible in the run records. The original failed
script is preserved at history/verify_transmission_bridge_v1.py and its
SHA256 was checked against the failed manifest. That historical manifest's
old root script path is intentionally superseded by the corrected script;
only transmission_run_v2 is current successful evidence.

high_power_run: 11,886 exhaustive words, 782 edge tables; 6 complete-clique
counts; dynamic exact N=2 word counts at m=18,24,32; the explicit tilt upper
bound is nonvacuous and checked at m=24,32; rational R=4096 moment matching.
The decimal delta=0.290563... is only an illustration: positivity follows
exactly from e<3 and 3*4098>256*27. Log-factorial rate samples are labeled
floating evidence and are not used as rigorous certificates.

dimension_uniform_run: 16 adapted noncommuting paths with decreasing support,
trace moments p=4,6,8,10,12 and 120 exact maximal-threshold controls;
186 scalar induction controls; 4,244 deletion prefixes, 26,183 compatible
ordered marks and 133 first-exit prefixes; 64 rational feedback states of
Walsh U(16). Four prescribed phases check port normalization only, not
continuous-Haar phase moment identities.

All current scripts passed. Their manifests are validated against the final
script and contract bytes before packaging. A stale failed manifest is
retained only as a failed historical run and is not promoted as current
evidence.

## Source checks and attribution

The new rank estimate is proved here; standard Schatten Holder and elementary
scalar Bernstein mechanisms are not claimed as discoveries. The project
local one-step proofs are pinned by path and SHA256, rather than treated as
fresh external certification.

The classical Ginibre formula is credited to hep-th/0205033v2 equation (2.4)
and the finite Ginibre kernel to arXiv:2211.16223v3, propositions 2.1--2.2.
The project's exact source comparison was read; unversioned primary PDFs
were also fetched successfully after version-suffixed fetches failed.
The latter fetch failures are not evidence against any source theorem.
The all-m kernel argument, rather than extending the source's N>m display,
is used in the new note.

The scalar reciprocal delay/intensity relation is PRIOR Ossipov--Fyodorov
(2005), cond-mat/0411576v2, equations (10)--(11). Gnutzmann--Keating--Piotet,
arXiv:1005.1026, section 7.1 and conclusion, explicitly call the full
universality criterion conjectural and discuss Gaussian massive-mode
approximations. That source cannot close the missing eigenvector input.
The new finite-phase-model argument is given in full instead of importing
an unstated exact scattering hypothesis. No world-priority conclusion follows.

## Open continuation after this checkpoint

The actual breakthrough obligation remains a fixed-dimensional entrance law
with its scalar/radial clock, or an equivalent microscopic signed hierarchy.
The dimension-uniform theorem now permits a controlled N->infinity limit at
every sufficiently large fixed m, with an explicit error tending to zero as
m->infinity. Identifying the resulting coherent finite-channel laws still
requires more than their large-m finite-block Gaussian asymptotics.

The bounded source-weighted ratio criterion is an executable alternative:
prove the averaged typical-eigenvector W1 intensity input, or directly prove
the Beta(1,2) bounded ratio law. No attempt here derives it from the current
large-u entry CLT. Closing u=2 by simply setting m=2 in a large-m probability
bound is invalid; the reversal Green singularity already occurs for Haar.
Unitarity or exact phase-stationary information is necessary for any future
Heisenberg comparison; any finite-order iid moment substitution is excluded
by the explicit counterexample.
