# Growing-degree and particular-local-test continuation, 5 October 2026

Checkpoint: `20261005-degree-growth`. Opening main:
`9555cd19dbf7cac335320dc231f2a7b7bb71954f`, clean at opening.
Parent: [critical-noise programme](critical_noise_program_20261005.md).
The objective remains the full deterministic BGS problem. The unchanged
odd-dimensional frozen operator is one prescribed target, not every
chaotic system.

## Target contract and ancestry

Keep $U_N=e^{i10^{-80}NA_N}M_N$, all odd $N\ge3$, the physical
finite Fourier symbol, modular Weyl convention, symmetry reduction and
unfolding. Forward conjugation uses $G=S\circ\Phi_g^\kappa$ and packet
centers use $F=G^{-1}$, with $\kappa=10^{-80}/(2\pi)$.
The terminal success criterion remains the complete signed factorial/CUE
comparison for every fixed order and compact Fourier test, or the
equivalent actual-chain defect in FLOW-017 C16--C17. Agreement of a
trace projection, a clock, or an externally randomized chain is partial.

The opening commit completed both remote workflows: independent
[manuscript run 37304049450](https://github.com/ChurilovMaksim/BGS/actions/runs/37304049450)
and [scientific run 37304049435](https://github.com/ChurilovMaksim/BGS/actions/runs/37304049435).
All six jobs passed at exactly `9555cd19dbf7cac335320dc231f2a7b7bb71954f`.
The computation log has 152 maintained success rows and 28 supplement
PASS rows; these counts are log observations, not a number of distinct
theorems. Lean compiled existing finite kernels, not the analytic BGS
argument. The prior immutable integration evidence is not rewritten.

## Executed mechanisms and decisive outcomes

| Mechanism | Discriminating calculation or proof | Outcome and boundary |
|---|---|---|
| Growing projection from the actual traces | Replace the old raw Gram-matrix norm by its exact Wick reproducing kernel; derive exponential packet seminorm bounds uniformly in logarithmic time. | G1--G11 give exact evaluation cost, a Mehler upper bound, actual $|p_j(U_N)|\le C_0e^{\alpha|j|}$ and projected compact-test error $O(N^{-1/4})$ for $Q_N=\lfloor\gamma\log N\rfloor$, uniformly at every heat time. The complementary statistic is not estimated. |
| Falsify norm-only recovery and sublinear completeness | Restrict the Wick kernel to three diagonal Laguerre choices per trace; choose one fixed pair test with frequency support in $(a,b)\subset(0,1/2)$. | G13 forces whole-span evaluation norm at least $e^{c\sqrt Q}$, and G14 makes every $Q_N=o(N)$ projection exactly blind to the fixed pair test. A clock has its nonzero limiting defect. This is an obstruction to these recovery methods, not a chaotic counterexample or a BGS disproof. |
| Invert the particular microscopic observable rather than a global character | Derive the full top-degree Casimir interval by actual permutation cut-and-join and the stable Wick quotient. | G15 has exact, attained endpoints $q\pm q(q-1)/N$. G16 gives a heat gap $a(1-b)N$ for the same fixed local pair test, hence Haar-$L^2$ inverse norm at least $e^{a(1-b)Nt}$. This closes the preceding programme's global-versus-particular-test limitation in this norm; it supplies no actual point evaluation. |

These mechanisms have distinct roles: a quantitative actual-map partial
estimate, a static missed-observable discriminator and a dynamical
inverse estimate. Their jointly needed implications are recorded as
dependencies of FLOW-020, not as three purported solutions of BGS.

## Mathematical information added

The neutral Wick basis is exact when $2Q\le N$. Its point cost
$\mathcal K_Q(A)$ is explicit and its centered norm is
$\sqrt{\mathcal K_Q(A)-1}$. The prior complex Mehler formula bounds it by

$$
\log\mathcal K_Q(A)\le2sQ+\frac{\pi^2}{12s}
+2\sum_{m\le Q}\frac{e^{-sm}}{1+e^{-sm}}\frac{|p_m(A)|^2}{m}.
$$

The growing-time input is proved anew: after removing accumulated
quadratic evolution, an order-$\ell$ packet word has at most $\ell$
insertions and degree at most $3\ell$. Fixed-order Schwartz seminorms,
sampling residuals and torus lattice overlaps grow only exponentially
in the number of map steps. Uniform return-volume integration gives
$Ce^{\alpha j}$ through a small logarithmic window; unitarity extends
this coarse bound to every integer $j$. It is not a useful bound at
$j\asymp N$.

At $s=2\alpha+1$, $\gamma=1/(4s)$, the centered cost is at most
$CN^{1/4}$. FLOW-019's compact local Haar variance $C_F/N$ then
gives the actual $N^{-1/4}$ projected rate. A separate stronger
hypothesis $|p_m(A_N)|\le K$ through all $m\le Q_N$ gives
convergence up to $Q_N\le c(\log N)^2$, $c<3/(2\pi^2)$.
That stronger hypothesis is not established for the actual operator.
No quantitative Schwartz rate is inferred from a qualitative variance.

For nonzero $0\le w\in C_c^\infty((a,b))$, $0<a<b<1/2$, the
concrete missed statistic is

$$
J_{N,w}(A)=N^{-2}\sum_m w(m/N)(|p_m(A)|^2-m).
$$

It is exactly a fixed real even Schwartz pair comparison, with
$\widehat\varphi(\xi)=w(|\xi|)/2$. Stable moments give both
$\mathsf P_QJ_{N,w}=0$ at $Q<aN$ and
$\|J_{N,w}\|_2^2=N^{-4}\sum m^2|w(m/N)|^2=O(N^{-1})$.
Its clock limit is $-\int_a^b\xi w(\xi)d\xi$, strictly negative.
The top-degree permutation spectrum gives
$\|P_tJ_{N,w}\|_2\le e^{-a(1-b)Nt}\|J_{N,w}\|_2$.
Neither its small norm nor its exponential noisy damping identifies
$J_{N,w}(U_N)$.

## Direct signed-vector continuation and unresolved implications

Applying the new exponential trace bound to the actual missed band is
a decisive failure of that input as a tail estimate: its indices are
$aN<m<bN$, while the useful window of G8 is logarithmic. Capping
G8 by $|p_m|\le N$ gives only $|J_{N,w}(U_N)|=O_w(N)$, not $o(1)$.
The projection and inverse mechanisms therefore cannot be iterated
unchanged to close this band.

The inherited D5 hierarchy retains the exact next candidate estimate:

$$
P_tJ_{N,w}(U_N)-J_{N,w}(U_N)
=N^{-2}\sum_m w(m/N)\int_0^t
P_s\left[m^2-m|p_m|^2-\frac mN
\Re\left(\bar p_m\sum_{r=1}^{m-1}p_rp_{m-r}\right)\right](U_N)\,ds.
$$

No cancellation estimate for this complete signed integral was obtained.
Replacing its cubic vector by absolute terms does not repair the lost
Heisenberg information. The original deterministic pair target already
requires $J_{N,w}(U_N)\to0$ for each such fixed $w$; all factorial
orders require their full additional counterterms.

The next open route is a **model-specific** signed ordered-propagator or
mixed-trace estimate in this fixed band. G15 permits resolving its
coefficient vector by top-degree permutation modes, but the actual
values of those modes remain unestimated. That continuation is untried
at Heisenberg degree in this checkpoint, not ruled out by the norm
obstructions. A different microscopic loop or justified limiting
variational input also remains open. Effective packet thresholds,
faster noisy relaxation and growing factorial order are separate
questions, not substitutes for the requested deterministic theorem.
The research goal is open; these are a reproducible checkpoint and an
exact remaining obligation, not an exhausted-program claim.

The [late primary-source discriminator](../literature/periodic_orbit_clt_scope_20261005.md)
checks a periodic-orbit alternative and proves a separate elementary
rounding example: all fixed Gaussian moments can converge while the
growing-frequency characteristic function equals one. The fixed-strength
oscillatory adaptation therefore needs more than a weak CLT. This small
example received author self-review, not the FLOW-020 independent review.
It does not change FLOW-020's frozen proof or bounded execution inputs.

## Review, sources and reproduction

The canonical [proof](../mathematics/growing_degree_trace_projection.md),
[independent internal review](growing_degree_review_20261005.md) and
[source check](../literature/growing_degree_sources_20261005.md) separate
new implications from inherited inputs. Complex Hermite/Mehler,
Ehrenfest packets and permutation cut-and-join are prior or standard
mechanisms. World novelty and external referee approval are not claimed.

The [contract](../evidence/20261005/growing_degree_contract.json) states
exact rational arithmetic and the finite surrogate scopes. The
[bounded manifest](../evidence/executions/20261005/degree-growth/manifest.json)
records an exit-zero run with all 11 input hashes unchanged, under
55-second wall, 50-second CPU, 2-GiB address-space, one-core and
one-thread caps. The
[result](../evidence/executions/20261005/degree-growth/checks.json)
passes 9,787 Wick Gram entries, 15 raw-versus-Wick evaluation cases,
156 Mehler coefficients, four full tensor Casimirs, 612 blind Gram
entries, 225 band covariances, 66 permutation cycle cases and 77
top-Wick generator images. It also checks 1,445 Casimir Gram entries
and 14 semidefinite interval matrices, plus clock/unitary-design,
Laguerre and 255 integer composition controls. These are declared
case families, not a count of independent proofs.

Four selected maintained verifiers passed on an immutable staged source
snapshot: the new growing-degree verifier, clock structure/projection,
microscopic removal and expansion/wavepacket audit. The replay used the
previous dependency overlay for SymPy/mpmath; the integration record
retains its actual environment. It is a focused local replay, not the
complete Python/C++/Lean surface.

The canonical manuscript built in three LaTeX passes to 252 pages,
with immutable inputs, no horizontal overflow or unresolved references.
Pages 240--241 were rendered and visually inspected, including the new
estimate, the fixed local inverse bound and the adjacent open actual
obligation. Nine static metadata, source synchronization, syntax and
diff checks passed. The
[integration record](../evidence/executions/20261005-degree-growth-integration.json)
pins the proof/review, bounded execution, focused replay and manuscript
outputs. Publication and exact-commit remote CI are recorded afterward,
without a self-referential tracked commit record.

Finite composition counts do not propagate packets; finite Casimir
matrices do not prove the all-degree spectrum or the asymptotic inverse
bound. No new analytic Lean certificate or large-N actual-spectrum
simulation is claimed. Full deterministic BGS and TRACE-005 remain **OPEN**.
