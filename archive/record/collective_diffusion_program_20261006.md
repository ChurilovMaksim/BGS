# Quantitative collective-noise continuation, 6 October 2026

Checkpoint `20261006-collective-diffusion`, starting from clean main
`a3d73edf6fd26485325405d4d24197730c76e9f7`. Parent programme:
[actual operator transfer](frozen_operator_transfer_program_20261006.md).
The full deterministic BGS target and prescribed actual U_N are unchanged.

## Contract and executed route portfolio

The initial named subsidiary target is a reduced common-noise two-copy
singular mass exceeding N^-1 at a vanishing noise scale. Retain common
variables, odd composite dimensions and identity/swap contractions.
A quantitative regulator theorem remains partial progress toward the
original signed noise defect. No finite spectrum certifies a large-N gap.

| Mechanism | Discriminator | Current outcome |
|---|---|---|
| Collective diffusion | Exact total-Weyl blocks; bounded floating spectra; shifted lattice Poincare estimate with all parity cases | D2 PROVED: a universal gap for the summed generator; independently internally audited |
| Original two-pair channel | Kernel-angle calculation and smallest positive pair eigenvalue | D3 PROVED: fully explicit rate for m=1, insufficient to prove Heisenberg dominance at vanishing noise; no impossibility claim |
| Refined common regulator | Retain the shared variables but subdivide their kicks; exact one-copy equality and contraction Trotter comparison | D23 PROVED: Heisenberg-dominating two-copy mass at u=N^-alpha, m=N^3, 0<alpha<1; this changes the higher-copy regulator explicitly |
| Original-spectrum transfer | Compare the strongest regulator conclusion with the signed fixed-matrix target and microscopic closeness boundary | The smooth-observable classical limit supplies no signed spectral comparison; original noise removal remains open |

The canonical proof is
[collective_diffusion_gap.md](../mathematics/collective_diffusion_gap.md).
The [independent review](collective_diffusion_review_20261006.md) records
two passes by one fresh read-only reviewer, and the accepted body pins.
No new external theorem is imported; the [attribution check](../literature/collective_diffusion_sources_20261006.md) preserves the prior
Brownian/design and alternating-shear framework and unestablished priority.

## Executions and continued frontier

The exact [contract](../evidence/20261006/collective_diffusion_contract_v2.json)
and [bounded manifest](../evidence/executions/20261006/collective-diffusion-exact-v2/manifest.json)
pin the proof, Weyl conventions, checker, imported cyclotomic implementation,
its transitive frequency-map import and source check. No floating arithmetic
or sampling enters that run. Replay with
`python3 computations/verification/collective_diffusion_gap.py`.

This is the corrected v2 replay. The initial gauge checker used Python
float signs from negative powers of -1, contrary to its declared exact
domain. Integer parity and type guards correct that implementation;
the [dated correction](history/2026/collective_diffusion_arithmetic_correction_20261006.md)
preserves the original source and unmodified v1 execution. The analytic
proof and its acceptance pins are unchanged.

The separate [floating contract](../evidence/20261006/collective_diffusion_spectrum_contract.json)
and [diagnostic manifest](../evidence/executions/20261006/collective-diffusion-spectrum/manifest.json)
cover all N^2 total-label blocks at N=3,5,7,9,11,13 and six selected blocks
at N=17,21,33,65. The sparse start is explicitly deterministic. These are
unverified float64 eigenvalues, not certified lower bounds or all-block
coverage at the larger dimensions. An initial ignored probe omitted the
implicit sparse start from its contract; the maintained replay corrects
that reproducibility issue. No preliminary artifact is relabelled.

D2 closes the uniform two-copy **summed-generator** question. D3 gives a
rate for the original ordered two-pair law, but not its Heisenberg dominance.
D20--D23 close that quantitative obligation for the explicitly refined law,
with u=N^-alpha, m=N^3, 0<alpha<1 and the same complete Gaussian sequence
in both copies. Its one-copy channel is exactly unchanged. D25 proves
retention of the actual map on each fixed smooth observable in normalized
HS mean square; no microscopic operator-norm or spectral continuity follows.

The direct m=1 improvement is OPEN, rather than disproved by the weak D3
bound. A plausible continuation is a low-spectral-projection uncertainty
estimate for the two weighted blocks, stronger than their exact kernel
angle. The generic sum-gap/Trotter estimate at m=1 does not suffice.
This continuation is preserved, not declared exhausted.

For the refined law, the next input is control of the full nonlinear
quenched determinant functional at the microscopic source, with all
permutation sectors and higher-copy moments retained. The unchanged
actual signed noise defect must still be estimated separately. No value
of the original stable-band J_(N,w)(U_N) is supplied by the universal
regulator gap, which holds for every unitary U. TRACE-005, all higher
factorial counterterms and full deterministic BGS remain OPEN.

The integration receipt records completed local validation, source
synchronization and manuscript build separately from remote publication/CI.
The parent checkpoint and its evidence remain unchanged. No analytic Lean
source was added and no world-priority or external referee claim is made.
