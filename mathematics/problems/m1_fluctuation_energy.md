# M1 — concentration of the exact k=4 key-table energy

## Goal

Prove concentration of the exact fourth-moment object strongly enough to support the next local-spectral-law step. The historical Möbius-fiber assembly is no longer the theorem object; it is retained only as a falsifier in `archive/` and `experiments/m1/cross_term_energy.py`.

## Exact object

For collapsed pair-key records `r=(u_r,v_r,d_r,n_r)`, define

`B(t)=sum_{r,s} n_r n_s 1_H(u_r u_s)1_H(v_r v_s)1_{d_r+d_s=t}`.

Then

`Sigma_4(q)=sum_t B(t)e_N(qt)`

and exactly

`sum_{chi,psi in H^perp}|J(chi,psi;q)|^4=m^2 Sigma_4(q)`.

The full twist assembly also collapses:

`sum_tau(A_tau*A_tau)(t)=m^2 B(t)`.

Thus there is no separate missing cross-twist term once the correct key-table object is used; all cross information is encoded in `B`.

## Exact finite identities already available

- collapsed key count: `(N-2)(N-3)+1`;
- diagonal weight: `N-2`;
- each ordered diagonal/off class: `(N-2)(K-1)(K-2)`;
- off/off total:
  `K^2(N-2)(N-3)-3K(K-1)(N-3)+2(K-1)(K-2)`;
- total variety:
  `V4=(K^2+1)N^2-(6K^2+3K)N+13K^2-3K`;
- mean:
  `mean_(q!=0)Sigma_4=(N B(0)-V4)/(N-1)`;
- variance duality:
  `Var_(q!=0)Sigma_4=N Var_(t!=0)B(t)`.

The active Python/C++ verifiers cross-check these structures at multiple finite designs.

## Load-bearing theorem target

The target is

`Var_(t!=0)B(t)=O(K^2 N)`.

Equivalently,

`std_(q!=0)Sigma_4(q)=O(NK)`.

With a mean of order `N^2`, this gives relative fluctuation `O(K/N)` and concentration whenever the chosen asymptotic regime makes `K/N -> 0`.

A first theorem may legitimately have a narrower range than the ultimate conjectural one. The current realistic route leads first to `K=o(N^(1/4))`; improving the range is a later problem.

## Exact decomposition

Write

`B(t)=O(t)+M(t)+(N-2)^2 1_{t=0}`,

where

`M(t)=2(N-2)C_H(t)`

and `O(t)` is the pure off-diagonal/off-diagonal layer.

For `t!=0` the deterministic diagonal spike disappears, so

`Var B = Var(O+M)`.

Once both component variances are `O(K^2N)`, covariance is automatic:

`|Cov(O,M)| <= sqrt(Var O * Var M)=O(K^2N)`.

Therefore no independent covariance theorem is needed. The variance programme now has only two components, one of which is already controlled in a broad explicit arithmetic regime.

## Component A — mixed k=2 layer: controlled outside explicit exceptions

Let

`c(h)=(h+1)/(h-1)`,
`A=c(H\{1})`.

Then exactly

`d(u,v)=2/(c(u)-c(v))`,

so `C_H` is the nonzero additive-difference representation function of `A`, up to the bijection `Delta -> 2/Delta`.

For odd prime `K`, the exact cyclotomic matching audit proves that over characteristic zero the only difference collisions are:

- identity: `(r,s)=(i,j)`;
- inversion-swap: `(r,s)=(-j,-i)`.

Reduction modulo `N` can create extra collisions only at an explicit finite set

`E_K={N prime : N == 1 (mod K), N | D_K}`,

where `D_K` is the product/radical of the nonzero cyclotomic collision norms. Conversely every prime in that set produces a non-forced collision.

The default verified sets are

`E_11={23,67,89}`,
`E_13={53,79,131,157,313}`.

For odd prime `K` and `N notin E_K`,

`sum_t C_H(t)^2=(K-1)(2K-5)`

and

`Var_(t!=0) C_H(t)`
`=(K-1)(2K-5)/(N-1)`
` -(K-1)^2(K-2)^2/(N-1)^2`.

Hence

`Var_(t!=0)M(t)=O(K^2N)`

with an explicit exact formula. This component is no longer the main obstruction.

Detailed derivation: `research/notes/k2_cayley_energy.md`.

## Component B — generic off/off elliptic family: the remaining hard part

For fixed `(h1,h2)` define

`C_(h1,h2,t): d(u,v)+d(h1/u,h2/v)=t`.

In Cayley coordinates

`a=c(u)`, `b=c(v)`, `alpha=c(h1)`, `beta=c(h2)`,

and

`T_alpha(a)=(alpha*a-1)/(a-alpha)`,

the fiber becomes

`2/(a-b)+2/(T_alpha(a)-T_beta(b))=t`.

After clearing denominators this is a plane cubic / genus-one double cover.

### Generic parameter geometry already established

Put

`p=alpha+beta`, `d=alpha-beta`.

The branch-quartic discriminant has a residual quartic whose discriminant is, up to a nonzero scalar,

`d^2 p^2`
`(p-d-2)^2(p-d+2)^2(p+d-2)^2(p+d+2)^2`.

For valid Cayley parameters the last four factors never vanish. Thus the only parameter strata on which the residual branch quartic ceases to be squarefree are

`d=0  <=> h1=h2`,

and

`p=0  <=> h1 h2=1`.

Each contains only `O(K)` parameter pairs and can be treated separately.

On the generic locus the elliptic `j`-function has a genuine order-four pole at

`t=2/d`,

because the quartic invariant satisfies `I(2/d)=256`. Hence the family is non-isotrivial.

Moreover, same-base equality of generic `j`-functions is completely classified:

1. the unique order-four finite pole recovers `d`;
2. the ratio of the `t^3` and `t^4` Laurent coefficients at infinity is
   `4(p^2-d^2-2)/d`, so it recovers `p^2`;
3. therefore the only generic same-base `j` coincidences are
   `(alpha,beta)` and `(-beta,-alpha)`,
   i.e. `(h1,h2)` and `(h2^-1,h1^-1)`.

This is exactly the involution already seen in the finite key arrays.

Detailed derivation: `research/notes/m1_offoff_elliptic_family.md`.

## Special off/off strata

### h1=h2

The cubic factors by `(u-v)`; on the valid off-diagonal domain the residual equation is bilinear:

`(h-1)uv+h t(u-v)+h(1-h)=0`.

For odd `K`, its only exceptional nonzero fibers occur at

`t=+-(s-s^-1)`,  `h=s^2`,

and the map `s -> s-s^-1` is injective on `H\{1}`. Thus this entire stratum contributes only `O(K)` exceptional fibers and can be bounded directly.

### h1 h2=1

This is the fixed locus of the exact parameter involution `(h1,h2)->(h2^-1,h1^-1)`, again only `K` pairs. It should be removed from the generic sheaf family and handled directly.

A crude Hasse/point-count `L^2` bound for `O(K)` such parameter classes is already compatible with the global `O(K^2N)` target.

## The remaining sheaf proposition

For a generic parameter `lambda=(h1,h2)`, let `F_lambda` denote the normalized rank-two middle-extension trace sheaf arising from `R^1` of the smooth elliptic family over the good `t`-locus.

The remaining load-bearing proposition is to prove:

1. **Purity.** `F_lambda` is pointwise pure of weight zero after the standard `1/2` normalization.
2. **Geometric irreducibility / monodromy.** The generic non-isotrivial elliptic family has the expected irreducible rank-two geometric monodromy.
3. **Uniform complexity.** Complexity/conductor is bounded by an absolute constant because the defining equations and number of bad fibers have bounded degree.
4. **Non-isomorphism.** For generic `lambda,mu`, the sheaves are geometrically isomorphic only when `mu=lambda` or the exact involution partner of `lambda` (with any required dual/twist ambiguity classified explicitly).
5. **Quasi-orthogonality.** Apply a published quantitative sheaf theorem only after items 1–4 are verified.

Sawin–Forey–Fresán–Kowalski quantitative sheaf theory is a strong candidate for item 5; Igusa/Michel-type elliptic monodromy results are candidates for item 2. These inputs are identified, not yet silently assumed.

## First honest asymptotic regime if the sheaf proposition is proved

For generic parameter pairs let `a_lambda(t)=O(sqrt(N))` be the unnormalized centered elliptic trace.

- self/involution correlations: `O(N^2)` each, with only `O(K^2)` such ordered parameter pairs;
- non-equivalent correlations: square-root quasi-orthogonality gives `O(N^(3/2))`, with `O(K^4)` ordered pairs.

Therefore

`Var_t O(t)=O(K^2N+K^4 sqrt(N))`.

Consequently, if

`K=o(N^(1/4))`,

then

`Var_t O(t)=O(K^2N)`.

Together with Component A and Cauchy–Schwarz for covariance, this proves the full M1 variance bound in the same regime.

This is a **conditional theorem target**, not a completed theorem. The remaining mathematics is now narrowly localized to the trace-sheaf proposition above.

## Mean work package

The mean is structurally easier and can be treated independently.

At `t=0`:

- the diagonal key self-coupling contributes `(N-2)^2`;
- `(h1,h2)=(1,1)` in the off/off layer contributes all `(N-2)(N-3)` off keys because inversion flips the sign of `d`;
- one-sided identity strata contribute no valid zero-difference off/off points;
- `h1=h2=h!=1` reduces to `uv=h`;
- generic `h1,h2!=1`, `h1!=h2` gives a smooth genus-one curve.

The generic `t=0` singularity resultant has been independently factored in SymPy and Wolfram. Hasse-Weil gives

`B(0)=B0_det+R0`,
`B0_det=2N^2+K^2N-2KN-8N-4K+14-S_eta`,
`|R0| <= (K-1)(K-2)(2 sqrt(N)+28)`.

Hence

`mean Sigma_4 = 2N^2 + O(KN+N+K^2 sqrt(N))`.

The mean is therefore asymptotic to `2N^2` at least in the provisional range `K=o(N^(3/4))`, modulo rewriting the CAS-resultant identity as a publication-quality algebraic lemma.

## Fresh falsifiers

Use corrected key-table outputs, not archived Run-93 producers.

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

The larger-`m` rows suggest, but do not prove,

`mean Sigma4 ~ 2N^2`,
`std Sigma4 ~ 4NK`,
`relative std ~ 2K/N`.

## Status

OPEN, but the uncertainty is now sharply localized. Exact pair-key combinatorics, the full twist collapse, mean/variance Fourier duality, the mixed Cayley component, generic non-isotriviality, and generic parameter-symmetry classification are explicit. The principal unresolved step is the rigorous trace-sheaf construction and quasi-orthogonality theorem for the generic off/off elliptic family.
