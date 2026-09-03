# M1 off/off layer — elliptic pencil and correlation theorem route

This note isolates the genuinely hard part of the fourth-moment variance after the exact `k=2` mixed term has been separated.

## 1. Cayley coordinates

For an off-diagonal key write

`a=c(u)=(u+1)/(u-1)`,
`b=c(v)=(v+1)/(v-1)`.

For a subgroup parameter `h`, put `alpha=c(h)`. Then

`T_alpha(a)=c(h/u)=(alpha*a-1)/(a-alpha)`.

The key difference is

`d(u,v)=2/(a-b)`.

For a fixed parameter pair `(h1,h2)`, with `alpha=c(h1)` and `beta=c(h2)`, the off/off fiber over `t` is

`2/(a-b)+2/(T_alpha(a)-T_beta(b))=t`.

After clearing denominators this is a plane cubic. Solving quadratically in one variable gives a double cover of the `a`-line branched over a binary quartic.

## 2. Binary-quartic discriminant

Set

`p=alpha+beta`,
`d=alpha-beta`.

For the branch quartic let `I,J` denote the classical binary-quartic invariants. Up to a nonzero convention-dependent scalar, its discriminant factors as

`Delta=d^2(dt-2)^4`
`      (p-d-2)^2(p-d+2)^2(p+d-2)^2(p+d+2)^2`
`      R_(p,d)(t)`,

where

`R_(p,d)(t)`
`=d^2t^4`
` +2d(p^2-d^2-4)t^3`
` +4(5d^2-p^2+4)t^2`
` -64dt+64`.

The omitted scalar is nonzero away from characteristics `2,3`.

The residual-quartic discriminant is, again up to a nonzero scalar,

`disc_t R=d^2p^2`
`         (p-d-2)^2(p-d+2)^2`
`         (p+d-2)^2(p+d+2)^2`.

For genuine Cayley parameters neither `alpha` nor `beta` equals `+1` or `-1`, so the last four factors never vanish. The only parameter strata where the residual quartic is not squarefree are

`d=0 <=> h1=h2`,

and

`p=0 <=> h1h2=1`.

Each contains only `O(K)` of the `K^2` parameter pairs.

The factorization has been reproduced independently in SymPy and Wolfram.

## 3. Exact degree and non-isotriviality of j

On the generic locus `d!=0`, the discriminant has the factor `(dt-2)^4`. At

`t0=2/d`

the quartic invariant satisfies exactly

`I(t0)=256`.

Thus the order-four discriminant zero is not cancelled in the elliptic `j`-invariant.

A direct polynomial gcd computation gives, on the generic `(p,d)` locus,

`gcd_t(I(t),Delta(t))=1`

up to a nonzero scalar. Moreover

`deg_t I=4`,
`deg_t Delta=8`.

Therefore

`j(t) ~ I(t)^3/Delta(t)`

has rational-map degree exactly `12`. Its pole divisor has type

`(4,4,1,1,1,1)`:

- order four at `t=infinity`;
- order four at `t=2/d`;
- four simple poles at the roots of `R_(p,d)`.

In particular every generic parameter pair defines a non-isotrivial one-parameter elliptic family.

The gcd, degree, pole value and factorization have been reproduced independently in SymPy and Wolfram.

## 4. Exact parameter symmetry

The key involution

`(u,v)->(v^-1,u^-1)`

preserves `d(u,v)` and sends

`(h1,h2)->(h2^-1,h1^-1)`.

Hence

`O_(h1,h2)(t)=O_(h2^-1,h1^-1)(t)`.

In Cayley parameters this is

`(alpha,beta)->(-beta,-alpha)`,

which preserves `d` and changes `p` to `-p`.

The swap `(u,v)->(v,u)` gives the separate relation

`O_(h1,h2)(t)=O_(h2,h1)(-t)`.

At `N=53,K=13` and `N=199,K=11`, exact same-`t` class arrays have no coincidences beyond the first involution: there are `(K^2+K)/2` distinct arrays, with `K` fixed parameters `h1h2=1` and every other orbit of size two. A separate finite check finds no additional centered arrays related by a global sign.

## 5. Generic same-base j-classification

On the open locus

`d!=0`, `p!=0`,

the residual quartic is squarefree. Thus `j(t)` has a unique finite pole of order four, at `t=2/d`.

If two generic parameter pairs have the same rational `j(t)`, equality of that pole recovers the same `d`.

Next take the polynomial part of `I^3/Delta` at infinity. If `L4,L3` are its `t^4,t^3` coefficients, then

`L3/L4=4(p^2-d^2-2)/d`.

Since `d` is already known, this recovers `p^2`. Therefore same-base equality of generic `j`-functions leaves only

`p'=p`

or

`p'=-p`,

that is

`(alpha',beta')=(alpha,beta)`

or

`(alpha',beta')=(-beta,-alpha)`.

So the exact key involution accounts for every generic same-base `j` coincidence.

## 6. No nontrivial generic isogenies

Different `j`-functions are not by themselves enough to distinguish `R^1` local systems: isogenous elliptic curves have isomorphic rational Tate modules. The missing step can nevertheless be closed using the degree and cusp structure above.

Assume two generic members are geometrically isogenous over the function field. Remove any common multiplication factor from an isogeny. A primitive separable isogeny has cyclic kernel of degree `n` prime to the characteristic, so the pair of `j`-maps lifts to the modular curve `X_0(n)`.

Let

`psi(n)=[SL_2(Z):Gamma_0(n)]=n product_(q|n)(1+1/q)`.

Both degeneracy maps `X_0(n)->X(1)` have degree `psi(n)`. Since both of our generic `j`-maps have degree `12`, a nonconstant lift `f:P^1_t->X_0(n)` must have

`deg f=12/psi(n)`.

Hence `psi(n)` divides `12`. Since `psi(n)>=n`, the only possibilities are

| n | psi(n) | deg f |
|---:|---:|---:|
| 2 | 3 | 4 |
| 3 | 4 | 3 |
| 4 | 6 | 2 |
| 5 | 6 | 2 |
| 6 | 12 | 1 |
| 8 | 12 | 1 |
| 9 | 12 | 1 |
| 11 | 12 | 1 |

For a cusp of denominator `c|n`, the first degeneracy map has cusp width

`w(c)=n/gcd(c^2,n)`.

The Fricke involution interchanges the two degeneracy maps and sends cusp denominator `c` to `n/c` up to cusp equivalence. Thus, at a point of ramification index `e` above such a cusp, the two `j`-pole orders are

`e w(c)`

and

`e w(n/c)`.

At `t=infinity` **both** of our family members have pole order exactly `4`. Therefore one needs

`e w(c)=e w(n/c)=4`.

Exact enumeration of the eight candidate levels gives:

- `n=2,3,5,6,8,11`: no Fricke-paired cusp has equal widths;
- `n=4`: equality occurs only at the middle cusp `c=2`, with `w=1`; this would require `e=4`, but `deg f=2`;
- `n=9`: equality occurs only at `c=3`, with `w=1`; this would require `e=4`, but `deg f=1`.

Every nontrivial separable cyclic isogeny is therefore impossible.

An inseparable isogeny has a nontrivial Frobenius factor. After a Frobenius factor of degree `N^r`, the source `j`-map has degree `12N^r`; a subsequent prime-to-`N` cyclic isogeny factors through two equal-degree degeneracy maps on `X_0(n)`, so the target `j`-map would have the same degree. Since every member of the present family has degree `12`, this forces `r=0`. Thus inseparable nontrivial isogenies are excluded as well.

Conclusion: two generic family members are geometrically isogenous **only** inside the exact involution orbit, where the finite key arrays are already identical.

This modular argument uses only standard formulas for the degree and cusp widths of `X_0(n)` plus the exact degree/pole data proved above.

## 7. From local-system isomorphism to isogeny

For a non-isotrivial elliptic curve over a geometric function field, the geometric endomorphism ring is `Z`; equivalently, extra endomorphisms force isotriviality. Zarhin's geometric-field Tate theorem then gives, for `ell` different from the characteristic,

`Hom(E1,E2) tensor Z_ell`
` = Hom_Gal(T_ell(E1),T_ell(E2))`.

Therefore an isomorphism of the generic rank-two `ell`-adic local systems would produce a nonzero homomorphism of elliptic curves, hence an isogeny.

Combined with Section 6, this proves that generic geometric `R^1` local systems are non-isomorphic outside the exact parameter involution orbit.

This closes the logical gap left by the earlier same-`j` classification.

## 8. Reducible bad fiber and the Cayley spike

The order-four bad fiber is not merely nodal. At

`t0=2/(alpha-beta)=d(h1,h2)`

the cleared cubic factors exactly into two lines:

`[(beta-1)a+(1-alpha)b+(alpha-beta)]`

and

`[(beta+1)a-(alpha+1)b+(beta-alpha)]`.

Thus this fiber can contribute an additional `N`-scale point-count term relative to the generic elliptic main term.

Crucially, the bad-fiber location is exactly the `k=2` difference

`t0=d(h1,h2)`.

Hence the number `R(t)` of parameter pairs whose reducible fiber occurs at a fixed `t` satisfies

`R(t)<=C_H(t)`

(up to the parameter strata that were already removed from the generic family).

The aggregate reducible-fiber spike is therefore bounded in `L^2` by the already solved Cayley energy:

`(1/N) sum_t |N R(t)|^2`
` <= N sum_t C_H(t)^2`.

Outside the explicit cyclotomic exception set for odd prime `K`,

`sum_t C_H(t)^2=(K-1)(2K-5)=O(K^2)`,

so the entire reducible-fiber contribution is

`O(K^2 N)`,

exactly the global M1 target scale.

The four roots of the squarefree residual quartic are simple discriminant zeros. Their double-cover fibers have one double branch point and are irreducible nodal/rational fibers, so they contribute only bounded point-count corrections after subtracting the `N` main term. They do not create another `N`-scale spike family.

This is why solving the `k=2` Cayley energy first was structurally useful rather than merely a side result.

## 9. Special diagonal parameter stratum

When `h1=h2=h`, the cleared cubic factors by `(u-v)`. On the valid off-diagonal domain the residual curve is

`(h-1)uv+h t(u-v)+h(1-h)=0`.

For `h=1`,

`O_(1,1)(0)=(N-2)(N-3)`

and `O_(1,1)(t)=0` for `t!=0`.

For `h!=1`, the bilinear curve degenerates only when

`t^2=(h-1)^2/h`.

For odd `K`, write uniquely `h=s^2` in `H`; the two special values are

`t=+-(s-s^-1)`.

The map `s->s-s^-1` is injective on `H\{1}` because equality forces either `s=r` or `sr=-1`, and `-1 notin H` for odd `K`.

Thus the whole diagonal parameter stratum has only `O(K)` exceptional nonzero fibers. Its direct `L^2` contribution is `O(KN)` and is smaller than the target `O(K^2N)`.

## 10. The inverse-pair stratum

The second special locus is

`h1h2=1`, equivalently `p=0`.

It is the fixed locus of `(h1,h2)->(h2^-1,h1^-1)` and contains `K` parameter pairs. These classes can be removed from the generic pair-correlation sum.

Each individual family still has fixed-degree geometry and nonconstant `j`; its centered trace has `L^2` norm `O(N^2)` by the same one-family elliptic/sheaf theory. Cauchy-Schwarz over only `K` classes gives aggregate variance `O(K^2N)`. No cross-family quasi-orthogonality is needed on this special stratum.

## 11. Trace-sheaf input

For a generic parameter pair `lambda=(h1,h2)`, let

`pi_lambda:E_lambda->U_lambda`

be the smooth elliptic family over the good `t`-locus, and let the middle extension of `R^1(pi_lambda)_* Q_ell` be normalized to weight zero.

The required standard inputs now line up as follows.

### Purity

Smooth proper base change gives a lisse rank-two sheaf on `U_lambda`; Deligne purity gives weight one, hence weight zero after the conventional Frobenius normalization.

### Geometric irreducibility

The `j`-function is nonconstant. Igusa's open-image theorem for non-isotrivial elliptic curves over function fields gives open geometric monodromy in `SL_2`, hence geometric irreducibility of the rank-two local system.

### Uniform complexity

The cubic equation, the compactification and the number/degree of bad fibers are bounded independently of `N,K,lambda`. Quantitative sheaf theory controls complexity under the six operations, so the middle-extension sheaves have an absolute uniform complexity bound once characteristics `2,3` are excluded.

### Geometric non-isomorphism

Sections 6–7 prove that two generic local systems can be geometrically isomorphic only inside the exact involution orbit.

### Quasi-orthogonality

Sawin–Forey–Fresan–Kowalski quantitative sheaf theory gives effective quasi-orthogonality for pure geometrically irreducible perverse sheaves of bounded complexity that are not geometrically isomorphic. Applied on the `t`-line, the normalized trace functions therefore have complete cross-correlation `O(sqrt(N))` outside the exact involution orbit.

Equivalently, the unnormalized elliptic traces satisfy

`sum_t a_lambda(t)a_mu(t)=O(N^(3/2))`

for generic non-equivalent parameter pairs, while self/involution pairs contribute `O(N^2)`.

At this point the conceptual sheaf hypotheses are no longer unknown; what remains before promotion to a paper theorem is a fully formal write-up of the projective model/middle extension and the bookkeeping that connects its trace to the exact affine key count at every bad/boundary fiber.

## 12. Variance consequence

There are `O(K^2)` self/involution ordered pairs and `O(K^4)` generic non-equivalent ordered pairs. The sheaf correlations therefore give

`O(K^2N+K^4 sqrt(N))`

for the variance contribution of the centered generic elliptic traces.

Section 8 gives `O(K^2N)` for the reducible bad-fiber spikes. Bounded boundary/nodal corrections contribute `O(K^4)`, which is smaller than `O(K^2N)` whenever `K^2<=N`. Sections 9–10 give `O(K^2N)` for the special parameter strata.

Thus the off/off layer has the bound

`Var_t O(t)`
` = O(K^2N+K^4 sqrt(N)+K^4)`

outside the explicit Cayley exception set, subject only to the formal trace-to-affine bookkeeping described at the end of Section 11.

In particular, in the first honest regime

`K=o(N^(1/4))`,

this becomes

`Var_t O(t)=O(K^2N)`.

Combined with the exact Cayley bound for the mixed `C_H` layer and Cauchy-Schwarz for covariance, this gives the full M1 variance target in the same regime once the remaining bookkeeping lemma is written cleanly.

This is substantially narrower than the ultimate conjectural range `K=o(N)`, but it is a concrete first asymptotic theorem target with the hard geometry reduced to standard published tools plus explicit finite algebra.

## 13. Literature route

The proof architecture now uses four standard tool families:

- Igusa/open-image results for geometric irreducibility of non-isotrivial elliptic families;
- Zarhin's Tate theorem over geometric fields to turn `ell`-adic local-system isomorphism into an elliptic-curve isogeny;
- modular-curve degree/cusp-width formulas to exclude every nontrivial generic isogeny in this degree-12 family;
- Sawin–Forey–Fresan–Kowalski quantitative sheaf theory for uniform complexity and quasi-orthogonality.

These are no longer being cited as vague analogies: the repository records the exact hypotheses supplied by the present family and the one remaining affine/bad-fiber bookkeeping step before a restricted M1 theorem can be promoted.
