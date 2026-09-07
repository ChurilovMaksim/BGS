# Pure-loss discrimination review — 2026-09-07

## Claim card

For `|psi_n^±>=sqrt(1-u)|0> ± sqrt(u)|n>`, `n>=1`, `0<u<=1/16`, let `sigma_±` be the outputs of pure loss with `0<eta<=1`. For `B>=1` set `t=B u eta^n`. The proved finite inequality is

`|D(sigma_+^{⊗B},sigma_-^{⊗B})-sqrt(1-exp(-4t))| <= 5ut+sqrt(u(43t+8sqrt(t)))`.

**Primary verdict: proved as written in the project proof.** Independent finite Python/C++ checks audit the load-bearing scalar inequalities; they are not used as a continuum proof.

## Dependency audit

- exact pure-loss action on the `|0>`, `|n>` coherences: standard channel identity;
- exact two-dimensional active block and determinant identity: internal algebra, passed;
- dominant-eigenvector replacement and tensor-product trace-distance perturbation: internal spectral/metric argument, passed;
- exact squared overlap of the two dominant eigenvectors and binomial block occupancy: internal spectral/product argument, passed;
- uniform `delta`/`L=-log gamma` bounds for `u<=1/16`: internal inequalities, passed and independently finite-stress-tested;
- binomial absolute-deviation bound plus 1/2-Hölder control of `sqrt(1-exp(-x))`: elementary inequalities, passed.

No asymptotic interchange is needed for the displayed finite theorem. The critical law and copy-threshold equivalents follow by sending the explicit right-hand side to zero as `u->0` at fixed `t` scale.

## Independent finite controls

- Python high precision: 440 scalar-grid points plus 300 finite-`B` binomial replacement cases: PASS.
- independent Boost.Multiprecision C++: 168 scalar points: PASS.
- both implementations include endpoints close to zero/one transmissivity and multiple `n`/`u` scales.

## Boundary

This result is for a known explicit binary pair. It does not close the full varying-noise moment-class tomography minimax problem and has no implication by itself for microscopic BGS/GOE/COE universality. External priority and independent human-referee acceptance are not established.
