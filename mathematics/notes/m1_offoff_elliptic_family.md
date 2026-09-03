# M1 off/off layer — elliptic pencil and restricted variance theorem draft

This note isolates the pure off/off term `O(t)` in the exact fourth-moment distribution. The mixed `k=2` term is treated separately in `k2_cayley_energy.md`.

## 1. Cayley model

For an off-diagonal key put

`a=c(u)=(u+1)/(u-1)`, `b=c(v)=(v+1)/(v-1)`.

For a subgroup parameter `h!=1`, write `alpha=c(h)`. Then

`T_alpha(a)=c(h/u)=(alpha*a-1)/(a-alpha)`

and

`d(u,v)=2/(a-b)`.

For `lambda=(h1,h2)` with `alpha=c(h1)`, `beta=c(h2)`, the fiber over `t` is

`2/(a-b)+2/(T_alpha(a)-T_beta(b))=t`.

After clearing denominators this is a plane cubic. Viewed as a quadratic in one variable it is a double cover of `P^1` branched over a binary quartic.

The generic parameter set used below excludes the `O(K)` strata

- `h1=1` or `h2=1`;
- `h1=h2`;
- `h1 h2=1`.

These are handled separately in Section 8.

## 2. Discriminant and generic elliptic geometry

Set

`p=alpha+beta`, `d=alpha-beta`.

Up to a nonzero scalar away from characteristics `2,3`, the binary-quartic discriminant is

`Delta=d^2(dt-2)^4`
`      (p-d-2)^2(p-d+2)^2(p+d-2)^2(p+d+2)^2`
`      R_(p,d)(t)`,

where

`R_(p,d)(t)`
`=d^2t^4+2d(p^2-d^2-4)t^3`
` +4(5d^2-p^2+4)t^2-64dt+64`.

The residual-quartic discriminant is proportional to

`d^2 p^2`
`(p-d-2)^2(p-d+2)^2(p+d-2)^2(p+d+2)^2`.

For genuine Cayley parameters the last four factors never vanish. Thus the residual quartic is squarefree precisely off the two parameter strata

`d=0 <=> h1=h2`,

`p=0 <=> h1 h2=1`.

At

`t0=2/d`

the quartic invariant satisfies exactly

`I(t0)=256`.

Moreover, on the generic locus,

`gcd_t(I,Delta)=1`, `deg_t I=4`, `deg_t Delta=8`.

Hence the generic elliptic `j`-map has degree exactly `12` and pole divisor

`(4,4,1,1,1,1)`:

- order `4` at `t=infinity`;
- order `4` at `t=2/d`;
- four simple poles at the roots of `R_(p,d)`.

In particular the generic family is non-isotrivial.

These identities have been reproduced independently in SymPy and Wolfram.

## 3. Exact parameter symmetries

The key involution

`(u,v)->(v^-1,u^-1)`

preserves `d(u,v)` and sends

`(h1,h2)->(h2^-1,h1^-1)`.

Therefore

`O_(h1,h2)(t)=O_(h2^-1,h1^-1)(t)`.

In Cayley variables this is

`(alpha,beta)->(-beta,-alpha)`,

which preserves `d` and sends `p` to `-p`.

The swap `(u,v)->(v,u)` gives the separate reflection

`O_(h1,h2)(t)=O_(h2,h1)(-t)`.

Finite exact arrays at `N=53,K=13` and `N=199,K=11` show no same-`t` coincidences, even up to a global sign after centering, beyond the first involution.

## 4. Generic same-base j classification

On the generic locus the unique finite pole of order `4` occurs at `t=2/d`. Thus equality of two rational `j(t)` functions first recovers the same `d`.

If `L4,L3` are the `t^4,t^3` coefficients of the polynomial part of `I^3/Delta` at infinity, then

`L3/L4=4(p^2-d^2-2)/d`.

So the same `d` and the same `j(t)` recover `p^2`. Consequently the only generic same-base `j` coincidences are

`(alpha',beta')=(alpha,beta)`

and

`(alpha',beta')=(-beta,-alpha)`.

Thus the exact key involution accounts for every generic same-`j` pair.

## 5. No nontrivial generic isogenies

Different `j`-functions can still come from isogenous elliptic curves, so same-`j` classification alone is not enough for the `R^1` local systems.

Assume two generic family members are geometrically isogenous over the function field. After removing a common multiplication factor, a primitive separable isogeny has cyclic kernel of degree `n` prime to the characteristic and yields a lift

`P^1_t -> X_0(n)`.

Let

`psi(n)=[SL_2(Z):Gamma_0(n)]`.

Both degeneracy maps `X_0(n)->X(1)` have degree `psi(n)`. Since both present `j`-maps have degree `12`, the lift has degree `12/psi(n)`. Hence `psi(n)|12`, leaving only

`n in {2,3,4,5,6,8,9,11}`.

For a cusp of denominator `c|n`, one degeneracy map has cusp width

`w(c)=n/gcd(c^2,n)`,

while the Fricke-related map has width `w(n/c)`.

At `t=infinity` both of our `j`-maps have pole order exactly `4`, so a lift of ramification index `e` would require

`e w(c)=e w(n/c)=4`.

For `n=2,3,5,6,8,11` there is no Fricke-paired cusp with equal widths. For `n=4` equality occurs only at `c=2`, with width `1`, which would require `e=4` although the lift degree is `2`. For `n=9` the middle cusp likewise requires `e=4` although the lift degree is `1`. Thus every nontrivial separable cyclic isogeny is excluded.

An inseparable Frobenius factor would multiply the degree of the source `j`-map by a positive power of the characteristic, while every member of this family still has degree `12`; hence no nontrivial inseparable factor is possible either.

Therefore two generic family members are geometrically isogenous only inside the exact parameter involution orbit.

## 6. Local-system non-isomorphism

For a non-isotrivial elliptic curve over a geometric function field the geometric endomorphism ring is `Z`. Zarhin's geometric-field Tate theorem identifies `ell`-adic Galois-equivariant homomorphisms of Tate modules with geometric homomorphisms of the elliptic curves.

Thus an isomorphism of two generic rank-two `R^1` local systems would force a nonzero geometric homomorphism, hence an isogeny. Section 5 then shows that generic local systems are geometrically non-isomorphic outside the exact involution orbit.

This closes the gap between the elementary `j` calculation and the sheaf quasi-orthogonality theorem.

## 7. Trace-to-affine bookkeeping lemma

Let `F_lambda` be the middle extension to the finite `t`-line of the rank-two `R^1` local system of a generic parameter `lambda`, and let `a_lambda(t)` denote its unnormalized Frobenius trace.

The exact affine key count differs from the projective elliptic count only by a uniformly bounded boundary, except at finitely many singular fibers.

### 7.1 Boundary degree

In projective `(a:b:z)` coordinates, the complement of the valid key-domain is contained in the union of

- the line at infinity `z=0`;
- `a=+z`, `a=-z`, `a=alpha z`;
- `b=+z`, `b=-z`, `b=beta z`;
- the diagonal `a=b`;
- the homogenized second-denominator conic `T_alpha(a)=T_beta(b)`.

The sum of their degrees is `10`. On an irreducible cubic none is a component, so Bezout gives at most `30` geometric boundary intersection points, counted with multiplicity.

Consequently, at every smooth finite fiber,

`O_lambda(t)=N-a_lambda(t)+e_lambda(t)`

with an absolute bound on `e_lambda(t)`.

### 7.2 Four simple residual bad fibers

The four simple roots of `R_(p,d)` have one double branch point and give irreducible nodal/rational fibers. Their affine point counts are `N+O(1)`. The middle-extension trace is bounded by the fixed sheaf complexity, so after the unnormalized weight-one scaling any mismatch can be absorbed into

`e_lambda(t)=O(sqrt(N))`

at at most four `t`-values per generic parameter.

### 7.3 Reducible fiber

At

`t_lambda=2/(alpha-beta)=d(h1,h2)`

the cleared cubic factors, up to a nonzero scalar, as

`[(beta-1)a+(1-alpha)b+(alpha-beta)]`

`*[(beta+1)a-(alpha+1)b+(beta-alpha)]`.

The affine fiber is therefore two lines up to the same finite boundary deletion and has

`O_lambda(t_lambda)=2N+O(1)`.

Hence the uniform bookkeeping identity may be written

`O_lambda(t)`
`=N-a_lambda(t)`
` +N 1_{t=t_lambda}`
` +e_lambda(t)`,

where `e_lambda(t)=O(1)` away from the five singular fibers and `O(sqrt(N))` at those fibers.

### 7.4 Aggregate error

Let `Lambda_gen` be the generic parameter set, of size `O(K^2)`, and set

`E(t)=sum_(lambda in Lambda_gen)e_lambda(t)`.

The ubiquitous bounded boundary part contributes `O(K^4)` to the population variance. The sparse singular part is supported on only `O(K^2)` parameter/fiber incidences and has size `O(sqrt(N))` per incidence; even the worst collision pattern gives another `O(K^4)` after division by `N`.

Thus

`Var_t E(t)=O(K^4)`.

This is below the target `O(K^2N)` whenever `K^2<=N`, in particular throughout the first regime `K=o(N^(1/4))`.

## 8. Reducible spikes are controlled by the solved Cayley energy

Let

`R(t)=#{lambda in Lambda_gen : t_lambda=t}`.

Since `t_lambda=d(h1,h2)`, every such parameter pair is counted by the `k=2` distribution `C_H(t)`. Therefore

`R(t)<=C_H(t)`.

The aggregate `N`-scale spike has population `L^2` contribution

`(1/N)sum_t |N R(t)|^2`
`<=N sum_t C_H(t)^2`.

For odd prime `K` outside the exact cyclotomic exception set `E_K`,

`sum_t C_H(t)^2=(K-1)(2K-5)`.

Hence all reducible generic fibers together contribute only

`O(K^2N)`

to `Var_t O(t)`.

## 9. The generic trace correlation sum

The standard sheaf inputs are now explicit.

- **Purity.** Smooth proper base change plus Deligne gives a rank-two weight-one local system on the good locus; rescaling numerical traces by `N^-1/2` gives weight-zero trace functions.
- **Geometric irreducibility.** Nonconstant `j` plus Igusa/open-image monodromy gives irreducible geometric rank-two monodromy.
- **Uniform complexity.** The equations, compactification and bad-fiber degrees are absolutely bounded. Quantitative sheaf theory therefore gives a uniform complexity bound for the middle extensions.
- **Geometric non-isomorphism.** Sections 5–6 leave only the exact involution orbit.
- **Quasi-orthogonality.** Sawin–Forey–Fresan–Kowalski then gives square-root complete cross-correlation for pure geometrically irreducible bounded-complexity sheaves that are not geometrically isomorphic.

Thus for generic non-equivalent parameters

`sum_t a_lambda(t)a_mu(t)=O(N^(3/2))`,

while self/involution correlations are `O(N^2)`.

There are `O(K^2)` self/involution ordered pairs and `O(K^4)` non-equivalent ordered pairs. Therefore

`Var_t sum_lambda a_lambda(t)`
`=O(K^2N+K^4sqrt(N))`.

## 10. Special parameter strata

The complement of `Lambda_gen` has only `O(K)` parameter pairs:

- one coordinate equal to the identity;
- `h1=h2`;
- `h1h2=1`.

For each fixed special parameter, the cleared equation still has bounded degree. Away from `O(1)` values of `t`, the geometric component pattern is constant and every component has genus at most one. Weil bounds give `O(sqrt(N))` fluctuations around the appropriate component-count main term; the `O(1)` exceptional fibers contribute only `O(N)` to the per-family population second moment.

Thus each special family has population variance `O(N)`. Cauchy-Schwarz over only `O(K)` families gives total special-stratum variance

`O(K^2N)`.

For `h1=h2` this can be seen directly from the explicit bilinear factor

`(h-1)uv+h t(u-v)+h(1-h)=0`.

## 11. Restricted off/off variance theorem draft

Combining Sections 7–10 gives, for primes `N>3`, odd prime `K|N-1`, and `N` outside the explicit Cayley collision set `E_K`,

`Var_(t!=0) O(t)`
`=O(K^2N+K^4sqrt(N)+K^4)`.

The implied constant is absolute once the standard sheaf complexity/quasi-orthogonality constants are fixed.

In particular, if

`K=o(N^(1/4))`,

then

`Var_(t!=0)O(t)=O(K^2N)`.

Together with the exact mixed-layer estimate in `k2_cayley_energy.md` and Cauchy-Schwarz for covariance, this yields the full M1 variance scale

`Var_(t!=0)B(t)=O(K^2N)`

in the same regime.

By the exact Fourier duality,

`Var_(q!=0)Sigma_4(q)=N Var_(t!=0)B(t)`,

so

`std Sigma_4=O(NK)`.

The mean estimate already gives `mean Sigma_4~2N^2` in this smaller regime. Hence the relative fourth-moment fluctuation is `O(K/N)`.

## 12. Promotion status

The mathematical chain for the restricted M1 variance theorem is now assembled from:

1. exact key-table combinatorics;
2. exact Cayley collision energy outside `E_K`;
3. explicit elliptic discriminant and `j` geometry;
4. modular no-isogeny plus Zarhin's Tate theorem;
5. published elliptic monodromy/purity and quantitative sheaf quasi-orthogonality;
6. the explicit trace-to-affine bookkeeping lemma above.

It is **not yet promoted as a final theorem in the paper layer**. Before promotion the project should do a line-by-line proof audit of the modular-curve cusp argument, replace the CAS discriminant/gcd identities by a hand or formal algebraic certificate, and pin exact theorem numbers/hypotheses for Igusa/Zarhin/Sawin in the manuscript.

This is now a proof-verification/formalization task rather than an unidentified analytic gap.
