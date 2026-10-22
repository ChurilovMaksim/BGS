# Critical-noise and fixed-degree continuation, 5 October 2026

Checkpoint: `20261005-critical-noise`. Opening local and remote main:
`0f3ac906f804a69006edd95194ea32fc6c5f601f`, clean at opening.
Parent: [all-order continuation](all_order_program_20261005.md).
The objective remains the full deterministic BGS problem; the unchanged
odd-N frozen operator is one concrete target, not every chaotic system.

## Exact contract and executed routes

Keep the original $U_N=e^{i10^{-80}NA_N}M_N$, all odd dimensions, its
raw Weyl convention, existing symmetry reduction and unfolding. Success
for the terminal claim requires the actual complete signed factorial
comparison, equivalently the actual chain defect C16--C17, for every
fixed order and compact Fourier weight. A clock or a stochastic chain
does not replace that target.

| Route | Executed discriminator | Result and first remaining implication |
|---|---|---|
| Fixed neutral heat degree | Use the stable Haar Gram matrix and invariant cut-and-join span, instead of just five explicit characters. | FLOW-019 bounds the entire fixed-degree projected heat defect by $C_{Q,K}t$, including the actual operator. Finite CUE covariance decay gives $O(N^{-1/2})$ agreement of each fixed projected compact local statistic with CUE, uniformly at all heat times. The complementary terms in P3/P7 remain unestimated; no growing-Q bound follows. |
| Critical noise scale | Integrate the exact clock kernel's angular Fourier constraints and retain the conditional-density Bragg contribution. | FLOW-018 gives the finite second moment, full critical local law with all moments, transport robustness and an explicit nonzero low-band noise defect. Clock preservation requires $Nt\to0$, while its Sine relaxation requires $Nt\to\infty$. The actual operator is not proved close to a clock. |
| Signed pair/resolvent compensation | Compare the exact covariance measures before taking variation; test the Abel weight. | Every Bragg mass has an exactly equal negative mesh mass. The signed pair comparison is uniformly $O((Nt)^{-2})$ and has a sharp three-atom leading defect. The noisy clock Abel statistic is strictly below finite CUE and has the exact negative leading coefficient. The clock selection rule has no established analogue for the actual spectrum. |

These are three executed mechanisms, not three formulations of an
unproved estimate. The first yields an actual-map partial estimate;
the other two isolate a control mechanism and a sharp boundary. **The
actual noise-removal estimate and full BGS remain open.**

## Mathematical information added

For each fixed neutral degree $Q$, both weighted degrees in the Haar
Gram product are at most $2Q$. Diaconis--Evans therefore gives one
positive definite, dimension-independent matrix at $N\ge2Q$. D5
preserves the span; its coefficients are $a+b/N$. Uniform coefficient
and starting-trace evaluation bounds prove P2. Finite CUE cross-window
determinant decay proves $\operatorname{Var}_{\rm CUE}F_N\le C_F/N$
for compact tests. The same finite-span evaluation bound proves P6:
each fixed projected actual statistic is within $O(N^{-1/2})$ of the
CUE expectation, uniformly at every heat time. Schwartz tests have
qualitative $o(1)$ only. These statements eliminate every fixed degree
from the actual heat defect but supply no estimate for
the growing-degree complement. In particular, a diagonal choice of
more and more fixed degrees is not a justified bound on that complement.

For the clock, exact Fourier integration gives
$\mathbb E|p_m|^2=m(1-e^{-tm})$ when $0<m<N$, and a coherent squared
mean when $N\mid m$. The covariance includes both continuous/mesh
terms and Bragg atoms. Dropping the latter would misidentify the critical
law. Each signed difference has zero mass, yielding a factor-of-$Nt$
improvement over the prior absolute alias-kernel bound.

The joint signed measure limit is
$\tau^2(\mathcal S_{N,t}-\mathcal S_N^{\rm CUE})
\to\delta_1+\delta_{-1}-2\delta_0$ when
$\tau=Nt\to\infty$ and $t\to0$. A fixed smooth Fourier weight near
1 proves optimality. The clock Abel difference has leading coefficient
$e^{-2s}-1$, so no monotonicity in time is inferred merely from its
upper/lower sandwich. The all-fixed-order critical original-chain
corollary uses the existing weak comparison C10 and moment transport;
it adds neither a quenched result nor a chain statement below $1/N$.

## Source and review boundary

The [source check](../literature/critical_noise_sources_20261005.md)
reads the prior kernels with exact time dictionaries. Katori--Tanemura's
equal-time kernel matches after transposition. Forrester's visible v1
(5.10) prints a plus which is incompatible with the adopted finite-clock
initial data; that formula is not imported. The journal version was not
checked in this pass. No world-priority assertion follows from this
bounded source survey.

The [independent internal review](critical_noise_review_20261005.md)
records three passes by one fresh reviewer, with the original alias
correction and the added compact covariance/complement arguments. Inherited analytic inputs keep their existing
grades; successful finite software checks certify only their declared
finite assertions.

## Continuing the actual objective

P3 is a genuine partial estimate for the prescribed map, but the
complement still contains the growing Heisenberg degrees. An unchanged
fixed-degree expansion would repeat this bottleneck. The next direct
continuation is a bound on the actual projected-complement defect with
an explicit degree/time regime, or actual ordered-propagator mixed
trace cancellation. P8 additionally proves that a particular positive local test has a
Haar-small complement with a nonzero clock evaluation. The analogous
actual-map point evaluation is still unestimated. S6's equal positive
and negative masses suggest
testing a comparable signed compensation before taking absolute values;
that mechanism must be proved for the actual initial data.

The critical clock comparison is closed in its stated scope. Extending
its exact selection rule to arbitrary starts is not claimed; a different
input would be needed. The fixed-degree route remains open at the
complement, and the full direct TRACE-005 route remains open. Polynomial
all-order chain schedules and effective startup thresholds are separate
subsidiary questions and are not substituted for the main objective.

## Reproduction and integration

The [bounded execution contract](../evidence/20261005/critical_noise_contract.json)
pins 17 mathematical, source and verifier inputs. Its
[manifest](../evidence/executions/20261005/critical-noise/manifest.json)
records an exit-zero run with unchanged inputs under a 55-second wall,
50-second CPU, 2-GiB address-space, one-core and one-thread cap.
The [result](../evidence/executions/20261005/critical-noise/checks.json)
passes 443 exact rational cases and 31 numerical diagnostics. The 30
cross-block Taylor cases are generic rational surrogates, not CUE samples;
the floating-point diagnostics have no interval certificate.

Nine selected maintained Python verifiers then passed on an unchanged
staged source snapshot. This focused local replay covers the new verifier,
the clock, microscopic removal, local moment transport and the inherited
chain controls; it is not the complete C++/Lean surface. The integration
record retains each executable/log hash and the exact selection.

The full consolidated manuscript built in three LaTeX passes to 251 pages,
with immutable inputs, no horizontal overflow and no unresolved references
or citations. Pages 239--241 were rendered and visually inspected, including
both new implications and their adjacent open deterministic obligation.
All scientific metadata, canonical structure, active links, generated
registry/source synchronization, Python syntax and diff checks passed.
The [integration record](../evidence/executions/20261005-critical-noise-integration.json)
pins these outputs. Exact-commit remote CI is recorded separately after
publication, avoiding a self-referential tracked publication record.

No newly written analytic Lean certificate or external referee report is
claimed. The mathematical proofs, finite controls and typesetting checks
have distinct scopes. The final scientific status remains: FLOW-018 and
FLOW-019 closed within their printed hypotheses; actual complementary
evaluation, deterministic noise removal and full BGS open.
