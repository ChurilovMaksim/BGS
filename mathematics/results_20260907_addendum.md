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

## 2a. Dense Cayley Fourier hybrid — EXACT + EXTERNAL-WEIL + FINITE-REGRESSION

Let `m=(p-1)/K`, `A=c(H\{1})`, and `n=K-1`. Expanding `1_H` in multiplicative characters trivial on `H` gives, for every nonzero additive frequency `q`,

```text
Ahat(q)=m^(-1) sum_(chi in H^perp) T_chi(q).
```

The trivial character contributes exactly `-e_p(q)-e_p(-q)`. For every nontrivial annihilator character, the classical mixed multiplicative-additive Weil/Deligne bound applied to

```text
chi((z+1)/(z-1)) e_p(qz)
```

gives `|T_chi(q)|<=2sqrt(p)`. Therefore

```text
|Ahat(q)| <= 2*((m-1)*sqrt(p)+1)/m <= 2sqrt(p).
```

Parseval and the additive-energy identity then imply the explicit centered bound

```text
0 <= E_+(A)-(K-1)^4/p
   <= 4*((m-1)*sqrt(p)+1)^2/(m^2*p) * (K-1)(p-K+1)
   <= 4(K-1)(p-K+1).
```

Combined with the global genus-one theorem,

```text
E_+(A)-(K-1)^4/p
 << min(pK, K^(8/3)+K^4/p).
```

Hence for `K=p^(alpha+o(1))` with `alpha>3/5`, the centered exponent in `K` is `1+1/alpha<8/3`; at `alpha=2/3` this is `K^(5/2+o(1))`, and it approaches the quadratic scale as `alpha->1`. This is a genuine dense-regime improvement, but it does not improve the sparse arithmetic regime relevant to the present BGS route.

The Python exact verifier and an independent C++20 implementation both pass every subgroup design for odd primes through `p<=509`: 807 designs total, 364 on the strict dense side `K^5>p^3`, maximum order 508. The dated certificate was re-read and refreshed after detecting stale source hashes; the theorem values did not change. See `cayley_fourier_hybrid.md`, `../computations/verification/cayley_fourier_hybrid.py`, `../computations/cpp/cayley_fourier_hybrid.cpp`, and `../evidence/certificates/cayley_fourier_hybrid_20260907.json`.

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

Thus every nonconstant finite polynomial has an explicit infinite-support weighted-Wiener stability ball. More globally, on the real Banach space with norm `|fhat(0)|+M_0(f)+M_A(f)`, the set `{Gamma_A>0}` is open and dense; its exact-cancellation complement is closed and nowhere dense.

The same open-dense conclusion holds in each of the following spaces:

```text
fixed analytic Wiener strip: sum_v exp(rho ||v||_1)|fhat(v)|<infinity,
H^s(T^2;R) for every s>2,
C^infinity(T^2;R) with its Frechet topology.
```

The Sobolev statement follows from the continuous embedding `H^s -> X_A` for `s>2`, and the smooth statement follows through any such Sobolev norm plus density of Fourier truncations. Smooth exact-cancellation examples therefore remain valid but form a closed nowhere-dense exceptional set in these topologies.

See `resonance_wiener_stability.md`, `generic_wiener_resonance.md`, and the exact regression `../computations/verification/resonance_wiener_stability.py`.

## 9. Analytic rigidity of the remaining zero-variance mechanism — EXACT

For every hyperbolic toral automorphism `S` and every real-analytic observable `g`,

```text
{g,g o S}=0 identically  =>  g is constant.             (A)
```

The proof uses the analytic level-set line field `L=ker dg`, its equivariance `L(Sx)=S L(x)`, Poincare recurrence, projective hyperbolicity and irrationality of the stable/unstable eigenlines. Thus the compactly supported separated-support mechanism cannot occur for a nonconstant analytic observable.

There is also an analytic cohomological regularity theorem. In an adapted hyperbolic frequency norm

```text
N_A(k)=|xi(k)|+|eta(k)|,
```

if a zero-mean analytic `h` obeys `|hhat(k)|<=M exp(-rho N_A(k))` and has zero sum on every oriented frequency orbit, then

```text
h=u-C_A u,
|uhat(k)|<=M' exp(-rho N_A(k)).                       (B)
```

Hence if a nonconstant real-analytic `g` nevertheless has `Gamma_A(g)=0`, its bracket is necessarily **nonzero** and solves a genuinely analytic nonlinear cohomological equation

```text
{g,C_A g}/(4*pi)=u-C_A u,
u analytic.                                                        (C)
```

This sharply reduces but does not close the all-members analytic question. See `analytic_bracket_rigidity.md`, `analytic_coboundary_regularization.md`, and `../manuscript/unified_sections/analytic_resonance_rigidity.tex`.

## 10. Current principal open frontiers

The remaining BGS chain is still

```text
Heisenberg-scale desymmetrized joint traces
 -> correlations at every compact Fourier support
 -> Schwartz correlations by positivity (extension proved 2026-09-08).
```

The arithmetic pointwise frontier remains the centered Cayley energy scale `K^(2+o(1))`. The dense Fourier branch closes a stronger pointwise regime for `K>p^(3/5)` but leaves the sparse/intermediate regime open; the global curve theorem and the mixed-Weil hybrid do not close that remaining range. The all-members analytic resonance question is now reduced to the nonzero analytic coboundary equation (C). The full vanishing-noise tomography transition is also open but logically separate from BGS.
