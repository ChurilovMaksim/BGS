# Actual operator-transfer continuation, 6 October 2026

Checkpoint: `20261006-operator-transfer`. Clean opening main:
`89645900bdbaace5d4956f306f6dccc464163e35`.
Parent: [Heisenberg pair programme](heisenberg_pair_program_20261005.md).
The original deterministic all-order BGS target and actual odd-dimensional
family remain unchanged. The complete prior checkpoint was published and
passed both workflows before this cycle.

## Target and executed routes

Keep the raw physical symbol, $\tau=10^{-80}$ and $U_N=e^{i\tau NA_N}M_N$.
The unresolved obligation is the signed noise defect in FLOW-017 C16--C17,
already necessary at the stable pair level. An auxiliary quantum channel's
gap is not that defect. A subsidiary theorem does not reduce the original
target's complexity or generality.

| Route | Central move and executed discriminator | Outcome |
|---|---|---|
| Coherent Weyl transfer | Exact actual kick, uniform whole-band Egorov and classical mixing; independent reconstruction of the twisted average and dissipation argument | O2--O4 PROVED: growing-band norm control, complete adjoint spectral arcs, commutant frequency coercivity and all-noise regularized singular gap |
| Full-band/microscopic transfer | Actual coefficient isolation and traceless-commutant min--max | O19 gives a linear full-band generator discrepancy; uN^3->0 forbids a large Heisenberg radial mass and o(1/N) ensemble operator distance forbids a large commutant singular mass; signed comparisons are not excluded |
| Color-flavor quadratic approximation | Inspect the primary source, realize the exact channel by two Gaussian Hamiltonian kicks and test whether its Hessian determines the nonlinear functional | O21--O23 give the microscopic massive block; O25 exactly falsifies sufficiency of this block alone. The nonlinear integral and ensemble-to-original comparison remain OPEN |
| Common-noise continuation | Retain the same Gaussian variables in all copies; compute the k=2 commutator and invariant sector; explicit Lie-generation/commutant proof | O26--O29 PROVED: ordered higher-copy channel, noncommuting two-copy generators, precisely identity/swap peripheral sector at every finite odd N. A quantitative gap after removing this sector remains OPEN |

The canonical proof and its noise applications are written in
[`frozen_operator_transfer_coercivity.md`](../mathematics/frozen_operator_transfer_coercivity.md).
Its stable ID is BGS-FM-018. The [review](frozen_operator_transfer_review_20261006.md)
records three passes by one fresh read-only reviewer and the unchanged
accepted mathematical body. The
[source check](../literature/frozen_operator_transfer_sources_20261006.md)
credits prior noisy-relaxation/Egorov methods and pins the exact classical
mixing input. Priority is unestablished.

## Precise next mathematical obligation

Let $\mathcal C_{2,N,u}=\mathbb E\operatorname{Ad}(V_{u,\xi}^{\otimes2})$
with the same four Gaussian parameters in the copies, and let $Q_N$
project orthogonally to $\operatorname{span}\{I,\mathsf S_N\}$.
O29 shows that

$$
\delta_2(N,u)=\inf_{|\zeta|=1}\sigma_{\min}
 [(\mathcal C_{2,N,u}-\zeta I)|_{\operatorname{ran}Q_N}]>0
$$

for each finite odd $N\ge3$, $u>0$. It gives no asymptotic rate.
The first quantitative question is whether, for a vanishing-noise scale
retaining the actual classical limit, $N\delta_2(N,u_N)$ dominates the
microscopic source mass. Any proposed bound must account for the
noncommuting pair generators and the permutation sector; copying O4
or using independent noise changes the question.

Even a positive quantitative answer must be followed by full nonlinear
determinant-functional control at the microscopic source, then a
model-specific signed comparison to the original spectrum. This is an
alternative route, not a theorem that these three conditions alone are
equivalent to the entire all-order BGS claim.

The unchanged necessary deterministic target is
$J_{N,w}(U_N)=N^{-2}\sum_mw(m/N)(|\operatorname{Tr}U_N^m|^2-m)\to0$
for every real even smooth fixed stable band $0<a<m/N<b<1/2$, followed by
all signed factorial counterterms. FLOW-021 determines the smoothed mean;
FM-018 determines a regularized channel gap. Neither bounds the original
$J_{N,w}(U_N)$. TRACE-005 and full deterministic BGS remain OPEN.

## Reproduction and handoff

The [contract](../evidence/20261006/frozen_operator_transfer_contract.json)
and [bounded run](../evidence/executions/20261006/operator-transfer/manifest.json)
pin the proof, inherited conventions, literature record, checker and
imported exact symbol helper. The result uses no sampling or floating
arithmetic. The optional Wolfram source has a separately preserved
[raw response](../evidence/20261006/frozen_operator_transfer_wolfram.json),
including all printed diagnostics.

Replay the focused finite assertion with
`python3 computations/verification/frozen_operator_transfer_coercivity.py`.
Validate the dated manifest with the installed mathbox computation-audit
validator and `--root`; do not overwrite historical evidence. Regenerate
the canonical frontier chapter with
`python3 computations/maintenance/sync_fixed_map_section.py`, then use
its `--check`, the scientific/repository audits and the full manuscript
builder. The workspace runner now captures the new check's JSON output.

The [integration receipt](../evidence/executions/20261006-operator-transfer-integration.json)
records actual completed local validations and manuscript inspection.
Remote CI is a separate software check at the published commit, not an
analytic BGS certificate. No analytic Lean module was added.
