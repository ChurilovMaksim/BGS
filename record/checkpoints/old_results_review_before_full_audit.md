# Old workspace archaeology — promotion queue

Source: the original `BGS(1).zip`, read independently of the cleaned repository. The raw source remains under `archive/legacy-workspace/`.

## Promoted after fresh checks

### Even-moment / k=4 factorization

Old sources include `data/proof/h3_k4_factorization.json`, `data/proof/h3_even_k_template.json`, `data/proof/sigma4_second_moment.json`, and `formal/Bgs/K4Variety.lean` in the archived workspace.

Fresh result: the `k=4` identity has been rebuilt from the original pair variables and independently reproduced in Python and C++. The active verifier now goes beyond the old producer: it reconstructs the complete difference distribution `B(t)`, the ordered coupling classes, and the twist-sum collapse. Exact anchors currently include `N=23,53,199,461`.

The general even-moment character-orthogonality reduction is promoted as an exact algebraic identity. The high-dimensional asymptotic estimate is still open.

## Important old signal reproduced by a corrected producer

### Layer-uniform fourth-moment fluctuation law

The archive reported a pattern resembling `relative fluctuation ~ c K/N`. One of the late large-design producers used to support that narrative (`code/large_m/third_calibration.py`, Run 93.2) contains a real ordered-count bug: it adds diagonal→off coupling but omits the reverse off→diagonal class.

That old output is therefore not accepted as evidence by itself.

However, a fresh corrected key-table implementation, independent of that file, reproduces the qualitative scaling on new and old designs. For larger `m`, the current exact data are consistent with

`mean Sigma4 ~ 2N^2`,
`std Sigma4 ~ 4NK`,
`relative std ~ 2K/N`.

This is now an **active conjectural target backed by corrected computations**, not a theorem and not a restored Run-93 claim.

## High-priority rechecks

### Stieltjes/resolvent convergence

Old file: `data/spectral/stieltjes_convergence.json` in the archive.

Archive signal: bulk Stieltjes deviation decreased strongly with matrix size before a sparse-sampling plateau. Two comparison bugs had already been fixed in the old run. Required before promotion: rebuild the producer against the current exact kernel, use dense/controlled q sampling, and state the convergence norm needed by the eventual local law.

### Rank-2 / Sp4 programme

Old files: `data/rank2_sp4/*`, especially `product_kernel_negative.json`, `rank2_diagonal_identity.json`, `rank2_coset_flatness.json`, `rank2_coset_sector.json`, and `rank2_hyperbolic_period4.json`.

The negative product-kernel observation is structurally plausible and easy to isolate. Later projector/coset claims need a complete rebuild because the old code mixes basis-orientation conventions and some prose called sampled statements exact. Do not use them as theorem inputs until the representation, projector normalization and basis transforms are independently certified.

## Quarantined contradictions and broken producers

### Historical Möbius M1 assembly

The eliminated Möbius graph is not the exact pair-key image. It contains a phantom `(1,1)` point for every `d!=0` and mishandles the multiplicity-`N-2` diagonal at `d=0`. The exact correction formula is recorded in `research/notes/m1_mobius_fibers.md`. Historical cross-term calculations remain useful only as falsifiers of the old proof.

### Old M1 killer test

The archive reported no violations of a universal `4 sqrt(N)` fiber bound. A complete scan of the same historical graph finds the exact semi-trivial `d=0` values `N-2`. The old killer test did not cover the twist class required by its prose claim.

### Run 93.2 third calibration

The source comments recognize two ordered mixed directions but the implementation adds only one. At the `N=53,K=13` analogue the missing class has size `6732`, changing `417147` to the independently verified `423879`. Any downstream old number that depends on this producer remains archaeology-only.

### Historical M4D proof

Retained only as provenance. Beyond the now-known assembly mismatch, it also omitted cross terms, mishandled the asymptotic regime and used an invalid uniform fiber bound.

## Lower-priority archive material

The old workspace also contains spectral-radius fits, edge-mass experiments, shape automata, Kloosterman probes, theorem-named scripts and extensive review logs. They are not deleted. They stay in the immutable archive until a concrete active problem requires a clean reconstruction.
