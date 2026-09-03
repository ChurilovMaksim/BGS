# Old workspace archaeology — promotion queue

Source: the original `BGS(1).zip`, read independently of the cleaned repository.  The raw source remains under `archive/legacy-workspace/`.

## Promoted after fresh checks

### Even-moment / k=4 factorization
Old files: `archive/legacy-workspace/data/proof/h3_k4_factorization.json`, `archive/legacy-workspace/data/proof/h3_even_k_template.json`, `archive/legacy-workspace/data/proof/sigma4_second_moment.json`, plus `formal/Bgs/K4Variety.lean`.

Fresh result: the k=4 identity and variety counts reproduce in clean Python and C++.  The general even-moment factorization also has a direct character-orthogonality derivation; see `research/theory.md`.  What remains open is the asymptotic exponential-sum estimate on the resulting variety.

## High-priority rechecks

### Layer-uniform fluctuation law / M2
Old files: `archive/legacy-workspace/data/spectral/layer_uniform_law.json`, `archive/legacy-workspace/data/proof/m2_killer_test.json`, `archive/legacy-workspace/data/spectral/m2_third_design.json`.

Archive signal: relative fluctuations at `k=2,4,6,8` were reported to scale roughly like `K/N` across `N=199,3571,95419`.  This is scientifically interesting but the old wording overstates the conclusion.  Required: rebuild the producer, document q-sampling and normalization, rerun all three designs, then add designs separating `K` from `N`.

### Stieltjes/resolvent convergence
Old file: `archive/legacy-workspace/data/spectral/stieltjes_convergence.json`.

Archive signal: bulk Stieltjes deviation decreased from `0.3586` (`m=9`) to `0.0868` (`m=105`) and `0.0371` (`m=336`), then plateaued at `0.0379` with sparse sampling at `m=837`.  Two comparison bugs had already been fixed in the old run.  Required: fresh dense-q rerun and a theorem-level statement of what convergence scale would actually be sufficient.

### Rank-2 / Sp4 programme
Old files: `archive/legacy-workspace/data/rank2_sp4/*`, especially `product_kernel_negative.json`, `rank2_diagonal_identity.json`, `rank2_coset_flatness.json`, `rank2_coset_sector.json`, `rank2_hyperbolic_period4.json`.

The negative product-kernel observation is structurally plausible and easy to prove.  The later projector/coset claims require a complete rebuild because the old code mixes basis-orientation commentary and several claims were described as exact despite being sampled.  Do not use them as theorem inputs until the representation, projector normalization and basis transforms are independently certified.

## Quarantined contradictions

### Old M1 killer test
`archive/legacy-workspace/data/proof/m1_killer_test.json` reported max nontrivial fiber values `15` and `29` and no violations of `4 sqrt(N)`.  The complete fresh twist scan finds exact values `N-2=51,197` at `d=0` for semi-trivial twist pairs.  The old killer test therefore did not cover the full twist class needed by its prose claim.

### Historical M4D proof
Retained only as provenance.  It omits cross terms, mishandles the asymptotic regime and misses the degenerate fiber.

## Lower-priority archive material

The old workspace also contains spectral-radius fits, edge-mass experiments, shape automata, Kloosterman probes, theorem-named scripts and extensive review logs.  They are not deleted; they stay in the immutable archive until a concrete active problem needs them.
