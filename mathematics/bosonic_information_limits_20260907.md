# Bosonic information proof summary — 2026-09-07

## Fixed-moment rare-phase family

For `u=E/n^beta` and `|psi_n^±>=sqrt(1-u)|0>±sqrt(u)|n>`, the heterodyne balance squared radius is `x_n=[n!(1-u)/u]^(1/n)=n/e+O(log n)`. Exact angular averaging gives a scalar factor `F(t)` with `F(t)=tF(1/t)` and `min(1,t)<=F(t)<=4min(1,t)`. After the shift `x=x_n+y`, dominated convergence gives the universal radial Hellinger profile. The full-aperture constant is represented by a convergent scalar series and interval-certified as `2.9086102383180<C_*<2.9086102383183`. The exact aperture discrimination exponent is `alpha-1-log(alpha)` for `alpha<=1/e` and `1/e` thereafter. The critical heterodyne likelihood experiment is obtained from a compensated integral; it is distinct from adaptive critical optimality for every coherent binary protocol.

## Fixed strictly noisy Gaussian channel

For a fixed finite-mode physical phase-insensitive Gaussian product channel with positive gains and at least one strictly noisy mode, inaccessible environment and no pre-channel encoding, the sole total-number beta-moment class has input trace-distance minimax risk `Theta((log B)^(-beta/2))` even against arbitrary collective output POVMs. The deterministic inverse modulus is `Theta((log(1/delta))^(-beta/2))`.

The upper bound uses low-Fock Weyl inversion: the discarded integral is controlled by exponential decay of the known Weyl kernel rather than by an assumed cutoff of the unknown characteristic function. Randomized product homodyne gives unit-modulus unbiased characteristic-function samples; choosing the Fock cutoff proportional to `log B` balances inverse-noise amplification and moment projection bias.

The lower bound is measurement-independent. The hard vacuum/high-Fock pair loses its coherence exponentially under pure loss; tensor fidelity bounds every collective POVM. Quantum-limited amplification is handled by an exponentially decaying trace-norm bound for the image of `|0><n|`; additional Gaussian noise is contractive. Hence collective measurements cannot beat the logarithmic input-reconstruction order for a fixed nonzero channel.

For the `n=128` mean-energy-one pair, 10 unrestricted input copies first reach 75% known-pair success. Full heterodyne needs more than `3e18`, unit-aperture censored heterodyne more than `3e218`, and after 50% pure loss arbitrary collective output measurement has threshold `3e39<B_75<=4e39`.

## Boundary

These results are not microscopic BGS universality. The full varying-noise moment-class minimax transition also remains open: the uniform pure-loss theorem controls the explicit hard pair but does not supply a matching arbitrary-state upper law when noise vanishes with sample size.
