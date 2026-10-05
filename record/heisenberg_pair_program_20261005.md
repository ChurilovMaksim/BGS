# Heisenberg pair determinant continuation, 5 October 2026

Checkpoint: `20261005-pair-heat`. Opening main:
`1e25c415239c283652c9155d03b0924b8aa61674`, clean at opening.
Parent: [growing-degree programme](growing_degree_program_20261005.md).
The original full deterministic BGS objective remains open. The unchanged
odd-dimensional frozen operator is one prescribed target, not every
chaotic system.

## Unchanged target and ancestry

Keep $U_N=e^{i10^{-80}NA_N}M_N$, the physical finite Fourier symbol,
modular Weyl convention, symmetry reduction and unfolding. The forward
map is $G=S\circ\Phi_g^\kappa$, packet centers use $G^{-1}$ and
$\kappa=10^{-80}/(2\pi)$. The terminal criterion remains the complete
signed factorial/CUE comparison at every fixed order and compact Fourier
weight, equivalently the actual-chain defect in FLOW-017 C16--C17.

The opening commit passed both remote workflows:
[independent manuscript 37334972106](https://github.com/ChurilovMaksim/BGS/actions/runs/37334972106)
and [scientific verification 37334971932](https://github.com/ChurilovMaksim/BGS/actions/runs/37334971932).
The latter passed on attempt 2 after retrying its canceled TeX-install
job, with no source change. All six final jobs refer to exactly the
opening commit. Existing Lean jobs compiled finite kernels, not the
analytic BGS argument.

## Executed routes and mathematical decision

| Route | Central move and executed discriminator | Result and boundary |
|---|---|---|
| Explicit top-degree pair modes | Derive signed hook modes directly from a determinant ratio and diagonalize the full stable Wick generator. | H1--H21 give exact pointwise heat evolution, every contraction, the Haar spectral measure and the microscopic time profile. No pointwise L2 inference is made. |
| Actual determinant contour estimate | Reflect the numerator outside the unit disk, choose an interior coefficient circle and use the actual logarithmic trace window on both radii. | H26--H31 give a superpolynomially accurate **smoothed** stable-band form factor for the unchanged U_N. The finite-dimension exponential correction is retained as the prefactor exp(b). This is not deterministic noise removal. |
| Falsify input-only recovery | Construct simple globally uniform spectra with identical first Q_N=o(N) traces, all satisfying one global exponential trace bound. | H22--H25 separate their unperturbed pair values. H27 additionally makes both smoothed values vanish at the same schedule, separating their full signed heat defects. No inference from these short-trace data alone can estimate the actual missing defect. |
| Exact Riemann--Siegel resummation | Read the primary determinant identity and the actual diagonal/off-diagonal argument, then write its source-to-U_N dictionary. | The algebraic half-Heisenberg identity transfers. The uniform quantum trace remainder and complete signed off-diagonal estimate do not follow from it. The model-specific resummation route remains OPEN. |

These are distinct mechanisms: exact mode resolution, a quantitative
pointwise contour estimate, an information discriminator and an external
resummation check. The dependency chain of FLOW-021 is not counted as
four purported solutions of BGS.

## Strongest surviving result

Let $Q_m=|p_m|^2-m$, $2m\le N$, and define

$$
H_m(A;y)=\frac{[x^m]}{1-y}
 \frac{\det(I-yxA)}{\det(I-xA)},\qquad
K_m=|H_m|^2-my^{m-1}
 -(1-y)^2\sum_{k=1}^{m-1}(m-k)y^{m-k-1}|H_k|^2.
$$

The quotient at y=1 is a polynomial removable limit. Then
$P_tQ_m(A)=e^{-t[m+m(m-1)/N]}K_m(A;e^{mt/N})$.
The formula is valid at repeated eigenvalues; individual-residue
expressions are used only for simple spectra. It supplies the full
compensation vector, rather than a finite initial heat jet.

For fixed $0<a<b<1/2$, the actual exponential trace estimate supplies
$J_N=\lfloor\log N/[2(\alpha+1)]\rfloor$ and normalized short-trace
bound $d_N=C_0N^{-1/2}$. At
$t_N=\max(32,8/a)\log J_N/J_N$, every integer $aN\le m\le bN$
satisfies, for all sufficiently large odd N,

$$
\left|\mathbb E|p_m(B_{t_N}U_N)|^2-m\right|
\le\left[e^b(at_N)^{-2}+N^2/2+N\right]
 e^{-a(1-b)Nt_N/4}=o(N^{-H})
$$

for every fixed H>0. No effective starting dimension is claimed.
The time constant depends on the fixed lower band endpoint a and is
not silently equated with FLOW-014's time constant 32.

The same first Q_N traces can nevertheless belong to two simple spectra
with $J_{N,w}$ tending to a negative clock constant or growing as
$L\int w>0$. This input limitation applies to arbitrary nonlinear
functions of the specified short traces, beyond linear projections.
It is not a counterexample to the actual quantum map.

## Exact remaining implication and next executable work

For $J_{N,w}=N^{-2}\sum_mw(m/N)Q_m$, the estimate just proved gives
$P_{t_N}J_{N,w}(U_N)=o(N^{-H})$. Thus its actual defect is
$-J_{N,w}(U_N)+o(N^{-H})$, and still needs a new signed estimate.
The deterministic model-specific obligation remains

$$
N^{-2}\sum_mw(m/N)(|p_m(U_N)|^2-m)\longrightarrow0.
$$

This fixed stable band is necessary, not sufficient for every Fourier
band and factorial order. The full signed hierarchy remains the terminal
target. Noise smoothing and determinant self-inversiveness cannot replace
the actual missing estimate.

The direct route remains OPEN at the signed sum of actual determinant
coefficients/ordered propagators at Heisenberg degree. The next attempted
input must use the fixed quantization beyond short traces: for example a
uniform weighted pseudo-orbit remainder or a signed estimate of the
principal-minor sum. An absolute residue bound needs microscopic gaps,
as H20 shows. A scalar classical CLT, auxiliary transition expansion or
another finite heat-jet computation would repeat an existing obstruction.
No known quantitative model-specific arrow of that kind is asserted here;
this route is unresolved, not exhausted or disproved. Normalized local
loop and justified limit-level variational routes remain separate open
alternatives from the earlier programme.

## Evidence and review boundary

The canonical [proof](../mathematics/heisenberg_pair_heat_formula.md),
[source audit](../literature/heisenberg_pair_heat_sources_20261005.md)
and maintained
[exact verifier](../computations/verification/heisenberg_pair_heat_formula.py)
distinguish mathematical implications from finite arithmetic.
The source audit credits prior hook/cut-and-join and determinant
resummation mechanisms. World novelty and external refereeing are
not asserted.

The [independent internal review](heisenberg_pair_review_20261005.md)
accepted H1--H31 in three analytic passes by one fresh reviewer and a
closing wording check. The promoted mathematical body differs from the
accepted body only in its status header. The review records inherited
inputs and resolved corrections; it is not external refereeing.

The final [bounded execution](../evidence/executions/20261005/pair-heat/manifest.json)
completed successfully in 1.572494 seconds under a 55-second wall limit,
50-second per-process CPU limit, 2 GiB address-space limit and one-core /
one-thread caps. Its nine listed input hashes were unchanged, and the
manifest validator accepted the packet. Python 3.12.14 exact Fraction
arithmetic checked 36 holomorphic modes, 204 Gram entries, 110 mixed
trace-generator eigenvectors, 15 independent radial eigenvectors, 108
genuine-unitary determinant values and 108 complete contractions.
It also checked 72 finite multiplicity cases and 1,052 / 10,911
uncontracted / contracted contour exponents. These are finite controls,
not an execution of the large-N analytic proof.

A separate
[Wolfram source](../computations/verification/heisenberg_pair_heat_checks.wl)
was executed through the evaluator; its
[receipt](../evidence/20261005/heisenberg_pair_heat_wolfram.json)
records the returned result, requested time constraint and unreported
kernel version/effective limits. Its returned contraction, generating,
cut-and-join and exponent checks were all true; an effective kernel cap
and kernel version were not reported. Neither run is an analytic certificate.

For a direct finite replay and evidence validation, from the repository root:

```sh
python3 computations/verification/heisenberg_pair_heat_formula.py
python3 computations/maintenance/sync_fixed_map_section.py --check
python3 computations/maintenance/render_claim_registry.py --check
python3 /root/.codex/plugins/cache/openai-curated-remote/mathbox/3.2.0/skills/computation-audit/scripts/validate_manifest.py --root . evidence/executions/20261005/pair-heat/manifest.json
```

The installed Mathbox runner command, exact limits, input pins and output
hashes are recorded in the bounded manifest. Its existing output directory
is immutable; a bounded replay uses a fresh directory. The maintained
checker itself needs only the recorded Python/NumPy environment and
repository helper closure, not the Mathbox plugin.

The [integration record](../evidence/executions/20261005-pair-heat-integration.json)
pins the proof, review, exact packet, separate symbolic receipt and
synchronized manuscript sources. Four selected maintained verifiers
passed with an unchanged recorded source snapshot. The complete
manuscript passed three LaTeX runs in 253 pages with no forbidden
warnings; the added formulas on pages 241--242 were visually inspected.
These validation results do not strengthen the mathematical scope.
Publication and the subsequent CI observations are kept separately so
the tracked evidence does not claim a future self-referential commit.

**Full deterministic BGS and TRACE-005 remain OPEN.**
