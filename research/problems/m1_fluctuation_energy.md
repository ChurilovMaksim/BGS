# M1 — concentration of the exact k=4 key-table energy

## Goal

Prove concentration of the exact fourth-moment object strongly enough to support the next local-spectral-law step. The historical Möbius-fiber assembly is no longer the theorem object; it is retained only as a falsifier in `archive/` and `experiments/m1/cross_term_energy.py`.

## Exact object

For the collapsed pair-key records `r=(u_r,v_r,d_r,n_r)`, define

`B(t)=sum_{r,s} n_r n_s 1_H(u_r u_s)1_H(v_r v_s)1_{d_r+d_s=t}`.

The exact fourth-moment fluctuation is

`Sigma_4(q)=sum_t B(t)e_N(qt)`

and

`sum_{chi,psi in H^perp}|J(chi,psi;q)|^4=m^2 Sigma_4(q)`.

The complete twist assembly also collapses exactly:

`sum_tau (A_tau*A_tau)(t)=m^2 B(t)`.

There is therefore no missing “cross-twist term” once the correct key-table object is used; all cross information is already encoded in `B`.

## Exact finite identities already available

- collapsed key count: `(N-2)(N-3)+1`;
- diagonal weight: `N-2`;
- each ordered diagonal/off class: `(N-2)(K-1)(K-2)`;
- off/off total:
  `K^2(N-2)(N-3)-3K(K-1)(N-3)+2(K-1)(K-2)`;
- total variety:
  `V4=(K^2+1)N^2-(6K^2+3K)N+13K^2-3K`;
- mean:
  `mean_(q!=0) Sigma_4=(N B(0)-V4)/(N-1)`;
- variance duality:
  `Var_(q!=0) Sigma_4=N Var_(t!=0)B(t)`.

The active Python/C++ verifiers cross-check these finite structures at multiple designs.

## New theorem target

The load-bearing variance statement is

`Var_(t!=0) B(t)=O(K^2 N)`.

It is exactly equivalent to

`std_(q!=0) Sigma_4(q)=O(NK)`.

Combined with a mean of order `N^2`, this gives relative fluctuation `O(K/N)` and concentration whenever `K=o(N)`.

A first realistic rigorous theorem may have a narrower range (for example a small-power condition on `K`) if it is obtained from pairwise trace-function correlations. That would still be meaningful progress; the range should be stated honestly and improved later.

## Decomposition

Write

`B(t)=O(t)+2(N-2)C_H(t)+(N-2)^2 1_{t=0}`,

where `C_H` is the `k=2` difference distribution and `O` is the pure off/off layer.

Thus it is enough to control:

1. `L^2` collisions of `C_H`;
2. `L^2` fluctuations of `O`;
3. their covariance.

Fresh corrected data show that each of the first two standard deviations is naturally on the `K sqrt(N)` scale and that their covariance is positive but of the same order. This is evidence only.

## Mean work package

The mean can be attacked separately and is structurally easier.

At `t=0`:

- the diagonal key self-coupling contributes `(N-2)^2`;
- `(h1,h2)=(1,1)` in the off/off layer contributes all `(N-2)(N-3)` off keys because inversion flips the sign of `d`;
- `h1=1,h2!=1` and the reverse contribute no valid zero-difference off/off points;
- `h1=h2=h!=1` reduces to the explicit equation `uv=h`;
- `h1,h2!=1`, `h1!=h2` gives a smooth genus-one curve at `t=0` after projective completion, apart from finitely many boundary points.

The generic `t=0` singularity resultant has now been factored independently in SymPy and Wolfram; away from `h1=1`, `h2=1`, and `h1=h2` it is nonzero. A conservative boundary count plus Hasse-Weil therefore gives

`B(0)=B0_det+R0`,
`B0_det=2N^2+K^2N-2KN-8N-4K+14-S_eta`,
`|R0| <= (K-1)(K-2)(2 sqrt(N)+28)`,

where `S_eta=sum_{h in H\{1}}eta(h)` is `K-1` for even `m` and `-1` for odd `m`. Hence

`mean Sigma_4 = 2N^2 + O(KN+N+K^2 sqrt(N))`.

This already gives the mean asymptotic for `K=o(N^(3/4))`, modulo turning the CAS-resultant identity into a publication-quality algebraic lemma. The variance, not the mean, is now the genuinely load-bearing obstruction.

## Variance work package: off/off trace family

For fixed `(h1,h2)`, define the cubic family

`C_(h1,h2,t): d(u,v)+d(h1/u,h2/v)=t`.

The branch-quartic discriminant factors as

`h1^2 h2^2 (h1-h2)^2 ((h1-1)(h2-1)+t(h1-h2))^4 Q(h1,h2,t)`

up to a nonzero scalar, with `Q` quartic in `t`.

Tasks:

1. prove the projective smoothness statement on the complement of the explicit bad strata;
2. define the normalized Frobenius-trace function of the smooth family;
3. bound its conductor uniformly in `(h1,h2)`;
4. classify when two parameter pairs give geometrically isomorphic/dual trace sheaves;
5. apply a correlation theorem only after those checks;
6. count the exceptional parameter tuples separately.

Fouvry–Kowalski–Michel-type sums-of-products results are candidate tools, not yet an applied theorem: their monodromy/independence hypotheses still need to be verified for this family.

## Variance work package: k=2 collision energy

`C_H(t)` has total mass `(K-1)(K-2)`. The desired scale is equivalent to an additive-energy estimate of the form

`sum_t C_H(t)^2 = O(K^2 + K^4/N)`

(up to harmless lower-order terms).

This should be attacked directly from collisions of

`d(u,v)=(u-1)(v-1)/(v-u)`

on `(H\{1})^2`, rather than by a pointwise Weil bound for each `t`.

## Fresh falsifiers

Use exact/corrected designs, not archived producer outputs. Current anchors include

| N | K | m | mean(Sigma4)/N^2 | std(Sigma4)/(NK) | relative std /(K/N) |
|---:|---:|---:|---:|---:|---:|
| 29 | 7 | 4 | 1.3236 | 2.2038 | 1.6650 |
| 89 | 22 | 4 | 1.4512 | 3.2990 | 2.2733 |
| 139 | 23 | 6 | 1.6683 | 3.8515 | 2.3086 |
| 199 | 11 | 18 | 1.8556 | 3.7996 | 2.0476 |
| 211 | 21 | 10 | 1.7752 | 3.8238 | 2.1540 |
| 281 | 28 | 10 | 1.7814 | 4.0190 | 2.2561 |
| 461 | 23 | 20 | 1.8895 | 3.8797 | 2.0532 |
| 521 | 13 | 40 | 1.9357 | 3.8408 | 1.9842 |

The larger-`m` rows strongly suggest, but do not prove,

`mean Sigma4 ~ 2N^2`,
`std Sigma4 ~ 4NK`,
`relative std ~ 2K/N`.

## Status

OPEN, but substantially sharper than the historical M1 statement. The exact combinatorial object, its Fourier collapse, its mean/variance duality, and the first generic curve stratification are now explicit. The remaining obstacle is a genuine family-correlation theorem, not a missing normalization or an unspecified perfect-power exception.
