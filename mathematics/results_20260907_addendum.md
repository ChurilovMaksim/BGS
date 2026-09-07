# Current-results addendum — 2026-09-07

This file extends `results.md`. The status authority is `../record/claim_ledger.md` together with `../record/claim_ledger_addendum_20260907.md`; the dated addendum wins for the scopes it covers.

## 1. Unrestricted finite-Fourier temporal nondegeneracy — EXACT

For every hyperbolic `A in SL(2,Z)` and every nonconstant real trigonometric polynomial `g`, the second Poisson-bracket resonance has strictly positive orbit variance. More generally all finite lags are independent modulo `L2` coboundaries. The support proof constructs an exposed frequency with a unique decomposition, nonzero symplectic determinant, forward escape in the expanding eigencoordinate and backward escape in the contracting eigencoordinate.

The fixed-box consequence is

```text
c_R(A)=inf Gamma_A(g)/||g||_2^4 > 0
```

on every finite real mean-zero Fourier box. There is no claimed bandwidth-uniform lower bound.

See `extremal_resonance_nondegeneracy.md` and `../manuscript/unified_sections/temporal_resonance.tex`.

## 2. Global Cayley curve theorem — EXACT + EXTERNAL-THEOREM

For every odd prime `p` and every subgroup `H<=F_p^*` of order `K>=2`, the off-diagonal ratio collision curve is a smooth geometrically irreducible genus-one `(2,2)` curve with four boundary points. Corvaja--Zannier gives

```text
N(rho,sigma)
 <= max(3*cuberoot(32)K^(2/3),48K^2/p),
N(rho,sigma)<=2K.
```

Exact restoration and diagonal bookkeeping imply

```text
E_+(c(H\{1})) << K^(8/3)+K^4/p
```

for every subgroup size, with no odd-order or lower/upper subgroup-size restriction. The exponent remains `8/3`; the centered quadratic target is still open.

See `cayley_curve_uniform.md` and `../evidence/certificates/cayley_curve_uniform_20260907.json`.

## 3. Temporal hierarchy and spectral modules — EXACT / FINITE-REGRESSION

The maintained September 6–7 temporal branch proves, in addition to the finite-lag nondegeneracy theorem:

- exact classification of finite quadratic temporal cancellations by lag-diagonal sums;
- reciprocal-filter cancellation and autocorrelation classification;
- all-frequency classical spectral positivity and finite-window Riesz bounds for fixed finite Fourier symbols;
- high-lag pair-orbit Gram/Toeplitz comparison and polynomial soft-mode classification by common orbit-filter divisors;
- explicit one-harmonic and complementary-filter repairs;
- finite quantum cyclic-module variance identities, including the balanced even-order phase case and phase-rank transition.

These are covariance/observable results, not local eigenphase universality.

See `temporal_resonance_hierarchy.md`, `weighted_wiener_resonance.md`, `resonance_riesz_regularization.md`, and `../manuscript/unified_sections/spectral_modules.tex`.

## 4. Holomorphic shell and Husimi identifiability — EXACT / FINITE-REGRESSION

The later identifiability branch includes:

- finite-rank holomorphic product-curve contact bounds;
- sharp `2d` complete shell/normal-jet identification for maps to `C^d`;
- `2d-1` counterexamples, including nonpolynomial entire examples;
- no degree-uniform Holder recovery from two circles and a sub-Holder lower modulus;
- bosonic Husimi-shell rank completeness without a photon cutoff;
- impossibility of finite coherent-projector identification for all pure states without a cutoff;
- fixed-energy compactness/continuity statements and explicit instability lower bounds.

These are tomography/phase-retrieval statements, not BGS statements.

## 5. Aperture-dependent tomography — EXACT

For fixed `s,beta,E,R0>0`, with moment constraint but no hard Fock cutoff, the coherent-ball and censored-heterodyne minimax scale is governed by

```text
K_R(T)=T/(1+log_+(T/R^2)).
```

Uniformly over `R>=R0`, including `R=infinity`, the complete-ball inverse modulus is `Theta(K_R(log(1/delta))^(-beta/2))`, and the finite-copy minimax expected trace-distance risk is `Theta(K_R(log B)^(-beta/2))`. The cutoff used by the estimator is an analytic bias-control device, not a state-space truncation.

## 6. Rare-phase and fixed-noisy-Gaussian information limits — EXACT / FINITE-CERTIFICATE

For the explicit vacuum/high-Fock pair, the balance radius is `x_n~n/e`, with an exact radial transition and certified fixed-test constant

```text
2.9086102383180 < C_* < 2.9086102383183.
```

At `n=128`, mean photon number one, unrestricted known-pair discrimination reaches 75% at exactly 10 copies while ordinary heterodyne requires more than `3e18` and unit-aperture censored heterodyne more than `3e218`.

For a fixed finite-mode phase-insensitive Gaussian product channel with at least one strictly noisy mode, inaccessible environment, positive gains and no pre-channel encoding, full input-state moment-class tomography has minimax expected input trace-distance risk

```text
Theta((log B)^(-beta/2)),
```

even against collective output POVMs; randomized product homodyne attains the upper order. The deterministic inverse modulus is `Theta((log(1/delta))^(-beta/2))` for fixed channel parameters.

## 7. Uniform pure-loss binary transition — EXACT

For

```text
|psi_n^±> = sqrt(1-u)|0> ± sqrt(u)|n>,
0<u<=1/16,
t=B u eta^n,
```

the pure-loss outputs satisfy

```text
|D(sigma_+^B,sigma_-^B)-sqrt(1-exp(-4t))|
 <= 5ut+sqrt(u(43t+8sqrt(t))).
```

Thus the known-pair copy penalty is asymptotically `eta^{-n}`. At 50% loss and `n=128`, the certified 75% threshold obeys `3e39<B_75<=4e39`. This does not determine the full varying-noise tomography minimax transition.

## 8. Infinite-support resonance stability and genericity — EXACT / FINITE-REGRESSION

Let

```text
M_0(f)=sum_v ||v||_1 |fhat(v)|,
M_A(f)=sum_v ||A v||_1 |fhat(v)|.
```

For a nonconstant finite polynomial `p`, the isolated witness `u,v` gives

```text
D=|det(u,Av)| |phat(u) phat(v)|>0.
```

If `g=p+r` and

```text
E=M_0(p)M_A(r)+M_0(r)M_A(p)+M_0(r)M_A(r)<D,
```

then

```text
Gamma_A(g)>=2 pi^2 (D-E)^2>0.
```

Thus every nonconstant finite polynomial has an explicit infinite-support weighted-Wiener stability ball. More globally, on the real Banach space with norm `|fhat(0)|+M_0(f)+M_A(f)`, the set `{Gamma_A>0}` is open and dense; its exact-cancellation complement is closed and nowhere dense. The same open-dense theorem holds in every fixed analytic Wiener strip

```text
sum_v exp(rho ||v||_1)|fhat(v)|<infinity.
```

This is a generic analytic nondegeneracy theorem, not an all-members theorem: whether every nonconstant analytic observable has positive variance remains open.

See `resonance_wiener_stability.md`, `generic_wiener_resonance.md`, and the exact regression `../computations/verification/resonance_wiener_stability.py`.

## 9. Current principal open frontiers

The remaining BGS chain is still

```text
Heisenberg-scale desymmetrized joint traces
 -> band-limited microscopic RMT correlations
 -> uniform high-frequency tail
 -> full microscopic BGS/GOE/COE.
```

The arithmetic pointwise frontier remains the centered Cayley energy scale `K^(2+o(1))`; the global curve theorem above does not close it. The all-members analytic resonance question and the full vanishing-noise tomography transition are also open but logically separate from BGS.