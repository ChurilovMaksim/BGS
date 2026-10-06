# Collective checker arithmetic correction, 6 October 2026

Before publishing FM-019, the author found a mismatch between the initial
gauge check and its declared coefficient domain. In Python,
`(-1)**negative_integer` produces a float. Those sign values are exactly
+1.0 or -1.0, but multiplying Fraction coefficients by them changes their
type and therefore violates the strict rational-arithmetic contract.
The initial passing output is not accepted as Fraction-only evidence.

The maintained [checker](../../../computations/verification/collective_diffusion_gap.py)
now obtains both signs by integer parity. Every polynomial scale operation
also asserts an integer/Fraction scalar and Fraction coefficients.
The [new contract](../../../evidence/20261006/collective_diffusion_contract_v2.json)
and [new bounded replay](../../../evidence/executions/20261006/collective-diffusion-exact-v2/manifest.json)
repeat the same declared finite cases without floating arithmetic.

The [initial contract](../../../evidence/20261006/collective_diffusion_contract.json),
[initial manifest](../../../evidence/executions/20261006/collective-diffusion-exact/manifest.json)
and their results are unchanged. They describe what was actually executed
and are superseded for the strict coefficient-domain assertion. Their
current-source freshness is intentionally not asserted: the active input
path has since been corrected. The byte-for-byte
[archived initial checker](collective_diffusion_initial_checker.py) has
SHA256 `386d6082f39bce9244748bb779740667431da9eab851634529cb5db0999f743a`,
matching the source pin in that initial manifest. It is a historical input,
not a second maintained implementation or a CI target. Its imported helpers
are pinned by the initial manifest and base Git commit.

The independently reviewed [analytic proof](../../../mathematics/collective_diffusion_gap.md)
and its accepted mathematical body are unchanged. No universal gap was
inferred from either finite run. The correction strengthens the finite
implementation's arithmetic provenance and changes no theorem statement.
