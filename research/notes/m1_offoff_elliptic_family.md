# M1 off/off layer — elliptic pencil and correlation target

This note isolates the genuinely hard part of the fourth-moment variance after the exact `k=2` mixed term has been separated.

## 1. Cayley coordinates

For an off-diagonal key write

`a=c(u)=(u+1)/(u-1)`,
`b=c(v)=(v+1)/(v-1)`.

For a subgroup parameter `h`, put `alpha=c(h)`. Then inversion/multiplication becomes the involution

`T_alpha(a)=c(h/u)=(alpha*a-1)/(a-alpha)`.

The key difference is

`d(u,v)=2/(a-b)`.

For a fixed parameter pair `(h1,h2)`, with `alpha=c(h1)` and `beta=c(h2)`, the off/off fiber over `t` is therefore

`2/(a-b) + 2/(T_alpha(a)-T_beta(b)) = t`.

After clearing denominators this is a plane cubic. Equivalently, solving quadratically in one variable produces a double cover of the `a`-line branched over a quartic.

## 2. Binary-quartic discriminant

Set

`p=alpha+beta`,
`d=alpha-beta`.

For the branch quartic `q(a)`, let `I,J` denote the classical binary-quartic invariants. Up to a nonzero convention-dependent scalar, its discriminant factors as

`Delta = d^2 (d t-2)^4`
`        (p-d-2)^2(p-d+2)^2(p+d-2)^2(p+d+2)^2`
`        R_(p,d)(t)`,

where

`R_(p,d)(t)`
`= d^2 t^4`
`  + 2d(p^2-d^2-4)t^3`
`  + 4(5d^2-p^2+4)t^2`
`  - 64dt + 64`.

The omitted scalar is nonzero away from characteristics `2,3`.

The residual-quartic discriminant is, again up to a nonzero scalar,

`disc_t R = d^2 p^2`
`             (p-d-2)^2(p-d+2)^2`
`             (p+d-2)^2(p+d+2)^2`.

For genuine Cayley parameters `alpha=c(h1)`, `beta=c(h2)`, neither `alpha` nor `beta` can equal `+1` or `-1`. Thus the last four factors never vanish. The only parameter strata on which the residual quartic is not squarefree are

`d=0  <=> h1=h2`,

and

`p=0  <=> h1 h2=1`.

Each is only an `O(K)` subset of the `K^2` parameter pairs.

The factorization has been reproduced independently in SymPy and Wolfram.

## 3. Non-isotriviality

On the generic locus `d!=0`, the discriminant has the boundary factor `(dt-2)^4`. At

`t0=2/d`

the binary-quartic invariant satisfies exactly

`I(t0)=256`,

so the order-four zero of the discriminant is not cancelled in the `j`-invariant. Therefore the elliptic `j`-function has a genuine pole and is nonconstant.

Hence every generic parameter pair defines a non-isotrivial one-parameter elliptic family.

This is the key geometric input needed before invoking any monodromy/trace-sheaf theorem.

## 4. Exact parameter symmetry

The key involution

`(u,v) -> (v^-1,u^-1)`

preserves the difference `d(u,v)` and changes the coupling parameter by

`(h1,h2) -> (h2^-1,h1^-1)`.

Therefore the class arrays satisfy exactly

`O_(h1,h2)(t)=O_(h2^-1,h1^-1)(t)`.

In Cayley parameters this is

`(alpha,beta) -> (-beta,-alpha)`,

which preserves `d=alpha-beta` and changes `p` to `-p`.

The swap `(u,v)->(v,u)` gives the separate relation

`O_(h1,h2)(t)=O_(h2,h1)(-t)`.

At the audited designs `N=53,K=13` and `N=199,K=11`, the exact same-`t` class arrays have no coincidences beyond the first involution: there are `(K^2+K)/2` distinct arrays, with `K` fixed parameters satisfying `h1 h2=1` and all remaining orbits of size two.

## 5. Generic same-base j-classification

On the open locus

`d!=0`, `p!=0`,

the residual quartic is squarefree. Thus the `j`-function has a unique finite pole of order four at `t=2/d`.

If two generic parameter pairs have the same rational `j(t)`, equality of that pole recovers the same `d`.

Next consider the polynomial part of `I^3/Delta` at infinity. If `L4` and `L3` are the coefficients of `t^4` and `t^3`, their ratio is

`L3/L4 = 4(p^2-d^2-2)/d`.

Since `d` is already known, this recovers `p^2`.

Therefore equality of the generic same-base `j`-functions leaves only

`p' = p`

or

`p' = -p`.

Equivalently,

`(alpha',beta')=(alpha,beta)`

or

`(alpha',beta')=(-beta,-alpha)`.

So the exact key involution accounts for all generic same-base `j` coincidences. This is a necessary geometric-isomorphism classification for the eventual sheaf correlation argument.

The pole value `I(2/d)=256`, the residual-quartic discriminant, and the Laurent ratio above have all been reproduced independently by SymPy and Wolfram.

## 6. Special diagonal parameter stratum

When `h1=h2=h`, the cleared cubic factors by `(u-v)`. On the valid off-diagonal domain the remaining curve is the bilinear equation

`(h-1)uv + h t(u-v) + h(1-h)=0`.

For `h=1`, inversion gives

`O_(1,1)(0)=(N-2)(N-3)`

and `O_(1,1)(t)=0` for `t!=0`.

For `h!=1`, the bilinear curve degenerates only when

`t^2=(h-1)^2/h`.

For odd `K`, write uniquely `h=s^2` in `H`; the two special values are

`t=+-(s-s^-1)`.

The map `s -> s-s^-1` is injective on `H\{1}` because equality would force either `s=r` or `sr=-1`, and `-1 notin H` for odd `K`.

Thus this diagonal parameter stratum contributes only `O(K)` exceptional nonzero fibers and is well below the size of the generic `K^2` family. It can be treated directly rather than by the generic sheaf theorem.

## 7. The inverse-pair stratum

The second special locus is

`h1 h2=1`, equivalently `p=0`.

It is exactly the fixed locus of the parameter involution `(h1,h2)->(h2^-1,h1^-1)` and contains `K` parameter pairs. The residual branch quartic is not squarefree there, so these classes should be removed from the generic sheaf family and handled directly.

Even a crude `L^2` treatment of `O(K)` such classes is compatible with the global target `O(K^2 N)`.

## 8. Candidate trace-sheaf formulation

For a generic parameter pair `lambda=(h1,h2)`, let `pi_lambda:E_lambda -> U_lambda` denote the smooth elliptic family over the `t`-line with the finitely many bad fibers removed, and let

`F_lambda = R^1 (pi_lambda)_! Q_l(1/2)`

schematically denote the normalized rank-two trace sheaf whose trace is the centered Frobenius point-count fluctuation.

Because the defining equations have fixed degree and the number of bad fibers is uniformly bounded, modern quantitative sheaf theory is a plausible route to a conductor/complexity bound independent of `N,K,lambda` after excluding characteristics `2,3`.

Non-isotriviality supplies geometric irreducibility/big-monodromy input through standard elliptic-family monodromy results. The same-base `j` classification above shows that generic geometric isomorphism can only occur inside the exact involution orbit, subject to checking the passage from elliptic families to their normalized sheaves.

This last passage is not yet recorded as a proved lemma in the repository.

## 9. First realistic variance theorem target

Suppose the following sheaf-correlation proposition is established on the generic parameter set:

- each normalized `F_lambda` is geometrically irreducible and pure of weight zero with uniformly bounded complexity;
- if `mu` is not `lambda` or its exact involution partner, `F_lambda` and `F_mu` are not geometrically isomorphic;
- consequently complete cross-correlations of their trace functions have square-root size.

Then the unnormalized elliptic traces `a_lambda(t)=O(sqrt(N))` satisfy

`sum_t a_lambda(t)a_mu(t)=O(N^(3/2))`

for generic non-equivalent pairs, while self/involution pairs contribute `O(N^2)`.

There are `O(K^2)` self/involution pairs and `O(K^4)` remaining pairs. After dividing by `N` to convert the total `L^2` norm into variance, this gives

`Var_t O(t) = O(K^2 N + K^4 sqrt(N))`

up to the already separated `O(K)` special parameter strata and bounded boundary corrections.

Therefore a first honest theorem regime would be

`K=o(N^(1/4))`,

in which

`Var_t O(t)=O(K^2 N)`.

Combined with the exact Cayley bound for the mixed `C_H` layer, this would prove the full M1 variance target in that regime.

This section is a **conditional theorem target**, not a proved result. Its remaining load-bearing task is now narrow: construct the precise sheaves and verify irreducibility/purity/geometric non-isomorphism so that a published quantitative quasi-orthogonality theorem applies.

## 10. Literature route

Two tool families are now particularly relevant:

- Michel/Igusa-type results for non-isotrivial elliptic families and their monodromy/second moments;
- Sawin–Forey–Fresan–Kowalski quantitative sheaf theory, which controls complexity under the six operations and gives effective quasi-orthogonality for pure irreducible perverse sheaves that are not geometrically isomorphic.

These sources justify the shape of the next proof obligation. They are not cited as if their hypotheses had already been checked for this family.
