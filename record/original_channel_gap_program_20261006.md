# Original two-pair microscopic-mass checkpoint, 6 October 2026

Base main: `fa007c498fe116a814a90aa3215cfd65b1f2a154`.
Parent: [collective diffusion](collective_diffusion_program_20261006.md).
The actual deterministic fixed-map BGS target and original m=1 common-noise law are unchanged.

[FM-020](../mathematics/original_channel_gap.md) closes the parent’s explicit low-spectral-projection continuation. Each total-label pair generator has at most 4 N sqrt(lambda)(1+log N) positive eigenvalues below lambda. The mutually unbiased partial-Fourier bases turn that count and the existing exact kernel angle into a low-spectral angle below 4/5 at lambda=(1024(1+log N))^-2. The two-contraction loss argument then proves an explicit singular gap at least (1-exp(-2u lambda))/50. At u=N^-alpha, 0<alpha<1, this lower bound dominates N^-1 for the original ordered law, without subdivision.

The [independent audit](original_channel_gap_review_20261006.md) reconstructed all parity sectors, the axis count, projection reduction and ordered-product loss. It corrected one sentence that had identified the lower-bound asymptotic with the actual gap; no actual-gap asymptotic or upper bound is claimed. The canonical proof retains that correction. Float64 spectra and exact rational lattice counts are separately identified by the [contract](../evidence/20261006/original_channel_gap_contract.json); they support finite identities and do not prove the asymptotic theorem.

The prior summed-generator theorem and refined-law result FM-019 remain valid. This result strengthens its original m=1 rate only. No external gap theorem, world priority, external referee or analytic Lean certification is claimed. The existing D19 kernel angle and Gaussian moment framework are credited. The [primary-source comparison](../literature/original_channel_gap_sources_20261006.md) distinguishes prior full diagonal twirls, including composite dimensions, from this finite two-Gaussian sinusoidal law; global priority remains unverified.

## Continuing frontier

The new bound holds for every U and therefore has no model-specific spectral information by itself. Quantitative higher-copy permutation-complement control and the full nonlinear quenched determinant functional remain open; the actual signed stable-band sum and noise-removal estimate also remain open. FM-020 does not transfer a noisy one-step channel to quenched spectral powers. TRACE-005 and BGS-BGS-001 are unchanged.

## Integration checks

The [pre-publication receipt](../evidence/executions/20261006/original-channel-gap/integration.json) records 156/156 maintained Python/C++ checks, all 21 C++ builds, the pinned Lean 20-job build, the scoped supplement replay, all manuscript synchronization checks and the 256-page three-pass manuscript build. The receipt separates container setup from source changes and local validation from remote publication/CI.
