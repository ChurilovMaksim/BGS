# Current mathematical core

This file is the concise active theory. Historical proof attempts are provenance only and live under `archive/`.

## 1. Finite-field setup

Let `N` be an odd prime and let `H=<a> <= F_N^*` have order `K`. Put

`S=H^perp`, `m=|S|=(N-1)/K`.

For multiplicative characters `chi,psi in S` and additive frequency `q`, use

`J(chi,psi;q)=sum_(x!=0,1) conjugate(chi(x)) psi(x-1) e_N(qx)`.

If `g` is a primitive root, `S={chi_(Kj):j mod m}`. The generator `chi_K` has order `m`, not `K`.

## 2. Exact pair-key geometry

For `x,y in F_N\{0,1}` define

`u=x/y`, `v=(x-1)/(y-1)`, `d=x-y`.

The diagonal `x=y` collapses to `(u,v)=(1,1)` with multiplicity `N-2` and `d=0`. Off the diagonal the map is a bijection onto

`D_off={(u,v):u,v in F_N^*\{1}, u!=v}`,

with inverse

`y=(1-v)/(u-v)`, `x=u(1-v)/(u-v)`

and

`d(u,v)=(u-1)(v-1)/(v-u)`.

The collapsed key table therefore has `(N-2)(N-3)+1` records.

## 3. Exact k=2 reduction

The `k=2` constraint requires the off-diagonal key itself to lie in `H x H`, so its mass is exactly

`(K-1)(K-2)`.

Define

`C_H(t)=#{(u,v) in (H\{1})^2:u!=v, d(u,v)=t}`.

This distribution will also control the reducible bad fibers of the `k=4` geometry.

## 4. Exact k=4 distribution and total variety

For weighted key records `r=(u_r,v_r,d_r,n_r)`, define

`B(t)=sum_(r,s) n_r n_s 1_H(u_r u_s)1_H(v_r v_s)1_(d_r+d_s=t)`.

Then

`V4=sum_t B(t)`, `Z0=B(0)`, `E_B=sum_t B(t)^2`.

The four ordered coupling classes give the exact closed form

`V4=(K^2+1)N^2-(6K^2+3K)N+13K^2-3K`.

This identity is combinatorial and finite, not asymptotic.

## 5. Character collapse and fourth moment

Define

`A_(chi,psi)(d)=sum_(r:d_r=d) n_r chi(u_r)psi(v_r)`.

Double character orthogonality yields for every `t`

`sum_(chi,psi in S)(A_(chi,psi)*A_(chi,psi))(t)=m^2 B(t)`.

For the unnormalized finite Fourier transform this is equivalent to

`sum_(chi,psi) Ahat_(chi,psi)(xi)^2=m^2 Bhat(xi)`.

Expanding `J^2 conjugate(J)^2` gives

`sum_(chi,psi in S)|J(chi,psi;q)|^4=m^2 Sigma4(q)`

with

`Sigma4(q)=sum_t B(t)e_N(qt)`.

The same orthogonality mechanism gives the exact even-moment reduction for every fixed even moment; estimating the resulting varieties remains a separate problem.

## 6. Exact mean/variance duality

Let `V=sum B`, `Z=B(0)`. Then

`mean_(q!=0)Sigma(q)=(NZ-V)/(N-1)`

and

`Var_(q!=0)Sigma(q)=N Var_(t!=0)B(t)`.

Thus the target `std Sigma4=O(NK)` is exactly equivalent to

`Var_(t!=0)B(t)=O(K^2N)`.

## 7. Structural decomposition

Exactly,

`B(t)=O(t)+2(N-2)C_H(t)+(N-2)^2 1_(t=0)`,

where `O(t)` is the pure off/off layer and `C_H(0)=0`.

This splits M1 into a mixed `k=2` energy, a pure off/off elliptic-family variance, and a deterministic diagonal spike.

## 8. Cayley transform and exact mixed-layer energy

Set

`c(h)=(h+1)/(h-1)`.

Then

`d(u,v)=2/(c(u)-c(v))`.

Hence `C_H` is the nonzero additive-difference representation function of `A=c(H\{1})`, up to a bijective relabeling. Also

`c(h^-1)=-c(h)`.

For odd prime `K`, clearing denominators in an additive collision gives a six-term cyclotomic matching problem. The active exact verifier classifies all `6!=720` matchings; ranks over `Q` are 30/240/450, rank can drop only in characteristic 2, and all admissible characteristic-zero collisions are identity or inversion-swap.

For each fixed odd prime `K`, non-forced finite-field collisions occur exactly at a finite set of rational primes dividing explicit resultants. Outside this set,

`sum_t C_H(t)^2=(K-1)(2K-5)`

and

`E^+(A)=3(K-1)(K-2)`.

Default exact exception sets are

`E_11={23,67,89}`, `E_13={53,79,131,157,313}`.

Therefore the mixed layer has standard deviation `O(K sqrt(N))` in the nonexceptional odd-prime-`K` regime.

## 9. Mean geometry

At `t=0`, two deterministic `N^2` spikes appear:

1. the weighted diagonal self-coupling `(N-2)^2`;
2. the off/off `(h1,h2)=(1,1)` inversion class `(N-2)(N-3)` because `d(u^-1,v^-1)=-d(u,v)`.

For `h1=h2=h!=1`, the zero-difference condition is `uv=h`. One-sided `h1=1` or `h2=1` classes have no valid zero-difference off/off solutions. Generic distinct nontrivial parameters give a smooth plane cubic. Hasse-Weil plus the finite boundary yields

`mean Sigma4=2N^2+O(KN+N+K^2 sqrt(N))`.

Thus the mean is asymptotic to `2N^2` when `K=o(N^(3/4))`, subject to publication-quality certification of the resultant/boundary lemma.

## 10. Why the historical Mobius assembly is wrong

Elimination produces the historical graph

`v_d(u)=((d-1)u+1)/(d+1-u)`,

but unsaturated elimination adds `(u,v)=(1,1)` for every `d` although the inverse pair map is undefined there. Finite comparison gives

- `d!=0`: `A_hist=A_key+1` for every twist pair;
- `d=0`, first twist trivial: `A_hist=A_key=N-2`;
- `d=0`, first twist nontrivial: `A_hist=-1` while `A_key=N-2`.

The historical perfect-power/cross-term argument therefore analyzes the wrong object and is not a theorem route.

## 11. Generic off/off elliptic pencil

Put `a=c(u)`, `b=c(v)`, `alpha=c(h1)`, `beta=c(h2)` and

`T_alpha(a)=(alpha*a-1)/(a-alpha)`.

Then a fixed parameter pair is governed by

`2/(a-b)+2/(T_alpha(a)-T_beta(b))=t`.

After clearing denominators this is a plane cubic; solving quadratically gives a binary-quartic double-cover model. For

`p=alpha+beta`, `d=alpha-beta`,

the residual quartic is squarefree except on

`d=0 <=> h1=h2`, `p=0 <=> h1h2=1`.

The generic `j`-map has degree 12 and pole type `(4,4,1,1,1,1)`. Hence the family is non-isotrivial.

The unique finite order-four pole recovers `d`; the first Laurent-coefficient ratio at infinity recovers `p^2`. Therefore equal generic same-base `j`-functions occur only for the identical parameter and

`(alpha,beta)->(-beta,-alpha)`,

which is exactly

`(h1,h2)->(h2^-1,h1^-1)`.

## 12. No generic isogenies outside the exact involution

If two generic family members were connected by a primitive separable cyclic `n`-isogeny, the two degree-12 `j`-maps would lift through `X_0(n)`. Since `psi(n)=[SL_2(Z):Gamma_0(n)]` must divide 12, only

`n=2,3,4,5,6,8,9,11`

are possible. Comparing Fricke-paired cusp widths with the fact that both `j`-maps have pole order 4 at infinity excludes every candidate; the only equal-width middle cusps (`n=4,9`) require ramification index 4 although the lift degree is only 2 or 1.

An inseparable Frobenius factor would multiply the degree of the `j`-map, contradicting degree 12. Thus no nontrivial generic isogeny exists outside the exact involution orbit.

For non-isotrivial elliptic curves the geometric endomorphism ring is `Z`; Zarhin's geometric Tate theorem turns an isomorphism of rational Tate/local systems into an isogeny. Hence the generic rank-two local systems are geometrically non-isomorphic outside the exact involution orbit.

## 13. Bad fibers and trace-to-affine bookkeeping

At the order-four bad fiber

`t0=2/(alpha-beta)=d(h1,h2)`

the cubic factors into two lines. Thus it can contribute an `N`-scale spike. The number of such parameter pairs at a fixed `t` is bounded by `C_H(t)`, so outside the cyclotomic exception set the aggregate spike variance is

`N sum_t C_H(t)^2=O(K^2N)`.

The four roots of the residual quartic are simple discriminant zeros and give irreducible nodal/rational fibers.

For the exact affine key count, the open-domain boundary is a divisor of total degree 10. By Bezout an irreducible cubic meets it in at most 30 geometric points. Consequently one may write

`O_lambda(t)=N-a_lambda(t)+N 1_(t=d(h1,h2))+e_lambda(t)`,

where `a_lambda` is the unnormalized elliptic Frobenius trace, `e_lambda=O(1)` on good fibers, and only sparse `O(sqrt(N))` errors occur at the non-reducible bad fibers. Summed over `O(K^2)` generic parameters, these bookkeeping errors contribute `O(K^4)` to variance.

The diagonal parameter stratum `h1=h2` has only `O(K)` exceptional nonzero fibers and contributes `O(KN)`. The inverse-pair stratum `h1h2=1` contains `K` classes and is bounded by one-family `L^2` plus Cauchy-Schwarz, giving `O(K^2N)`.

## 14. Sheaf correlation input and restricted M1 draft

For a generic parameter `lambda`, the smooth elliptic family gives a rank-two `R^1` local system on the good `t`-locus.

- Deligne gives purity.
- Nonconstant `j` plus Igusa open monodromy gives geometric irreducibility.
- Fixed-degree equations and uniformly bounded bad fibers give uniform complexity; quantitative sheaf theory controls this under the six operations.
- Sections 11-12 give geometric non-isomorphism outside the exact involution orbit.
- Quantitative quasi-orthogonality then gives normalized complete cross-correlations `O(sqrt(N))`, or unnormalized elliptic-trace correlations `O(N^(3/2))`.

There are `O(K^2)` self/involution pairs and `O(K^4)` non-equivalent pairs, so

`Var O(t) << K^2N + K^4 sqrt(N) + K^4`.

Combining the generic term, special strata, reducible spikes, the exact mixed-layer energy and Cauchy-Schwarz for covariance gives the restricted draft implication

`K=o(N^(1/4)) => Var_(t!=0)B(t)=O(K^2N)`

for odd prime `K`, split primes `N` outside the explicit cyclotomic exception set, and the fixed small-characteristic exclusions of the elliptic/sheaf model.

Then

`std Sigma4=O(NK)`, `std(Sigma4)/mean(Sigma4)=O(K/N)`.

**Status:** this chain is assembled but still needs line-by-line theorem/citation audit and hand/formal certification of the CAS-supported algebraic lemmas before publication. It is not a proof of general BGS.

## 15. Reproducibility anchors

Current exact `k=4` anchors are

- `(N,K)=(23,11)`: `V4=48621`, `B(0)=2609`, `sum B^2=103156981`;
- `(53,13)`: `423879`, `12063`, `3410502105`;
- `(199,11)`: `4681821`, `96641`, `115589503389`;
- `(461,23)`: `111147915`, `641799`, `26960554630421`.

For `N<=53`, direct ordered pairs, collapsed keys and the corrected `H^2` gather agree exactly. Python and independent C++ agree on the certified invariants; the twist identity is independently checked through `N=199`.

## 16. Current frontier after M1

Even a fully audited restricted M1 theorem is not yet a local BGS spacing theorem. The next load-bearing step must connect the controlled finite-field moment/concentration statement to the required local spectral law, with symmetry class, desymmetrization, limiting regime and quantitative error all stated explicitly.
