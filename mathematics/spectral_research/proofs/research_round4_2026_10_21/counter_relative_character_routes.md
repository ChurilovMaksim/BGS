> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round4_2026_10_21/counter_relative_character_routes.md`. Embedded SHA256: `1b27d09f2dc4a8e8d87ccdf31c7b3c7230065e0c5ee35492c7149880a75ecae3`.
> [Thematic guide](../../topics/arithmetic.md).

# Relative-character projections and arbitrary prescribed routing

21 October 2026. Addendum to the one-step HS theorem.

This extends `counter_one_step_pinching_hs.md`, frozen SHA-256 `a8babde8cfa7cdf0ef794775ac73672431bd9f9d36491f50e3bf19515543c629`. Its analytic representation and error, and the all-pairs growing-order compression gap cited there, retain their separate audit gates. The finite-dimensional extension below introduces no additional analytic hypothesis.

## 1. Every relative-character component has the same HS bound

Let `G=(Z/dZ)^2` and let `H_g` and `P_chi` be the exact commuting Weyl representation and its character projections. For any character `nu` of `G`, define

$$
\mathcal Q_\nu(X)=\sum_{\chi\in\widehat G}P_{\nu\chi}XP_\chi.
\tag{1.1}
$$

Here multiplication of characters is pointwise. Character orthogonality gives the exact formula

$$
\mathcal Q_\nu(X)
=\frac1{d^2}\sum_{g\in G}\overline{\nu(g)}H_gXH_g^*.
\tag{1.2}
$$

Indeed the `P_psi X P_chi` block is multiplied by the average of `overline(nu) psi overline(chi)`, which equals one exactly when `psi=nu chi`.

The block spaces in (1.1) are orthogonal for the Hilbert--Schmidt inner product, so `mathcal Q_nu` is an orthogonal projection on the vector space of matrices. For `nu` nontrivial this need not be a positive map on Hermitian matrices, and no positivity of that map is used. Its HS projection identity is

$$
\begin{aligned}
\sigma_\nu^2
:=\frac1N\|\mathcal Q_\nu(E_N)\|_{\rm HS}^2
&=\frac1N\langle E_N,\mathcal Q_\nu(E_N)\rangle_{\rm HS}\\
&=\frac1{d^2}\sum_{g\in G}\overline{\nu(g)}
\frac1N\operatorname{Tr}(E_N^*H_gE_NH_g^*).
\end{aligned}
\tag{1.3}
$$

The identity group element contributes exactly `d^(-2)`. The uniform echo bound and its grid sum in Sections 5--6 of the source apply unchanged, because the additional character weights have absolute value one. Therefore, with precisely the same constants and exponent as that source,

$$
\boxed{
\sup_{\nu\in\widehat G}|\sigma_\nu^2-d^{-2}|\le C N^{-\epsilon},
\qquad
\sup_\nu\sigma_\nu\le\overline\sigma_{N,d}
:=d^{-1}+C N^{-\epsilon/2}.
}
\tag{1.4}
$$

The case `nu=1` is the usual character pinching. Formula (1.4) treats all relative-character sectors, not only that case.

## 2. Prescribed routes may vary at every time

The exact metaplectic factor permutes the character projections by
`M_N P_chi=P_(S chi)M_N`, where

$$
\mathsf S\chi=\chi\circ L,\qquad
L=\begin{pmatrix}3&-4\\-2&3\end{pmatrix}.
$$

Choose any deterministic sequence of characters `nu_(j,N)`, allowed to depend on `N` and to change at every step. Put

$$
K_j=\mathcal Q_{\nu_{j,N}}(E_N)M_N,\qquad R_j=U_N-K_j.
\tag{2.1}
$$

The permitted transition for the `j`th factor is

$$
\chi\longmapsto\nu_{j,N}(\mathsf S\chi).
\tag{2.2}
$$

This is a permutation of the complete set of characters. Every complementary transition belongs to `R_j`; inserting the character resolutions gives an exact disjoint partition of histories.

Suppose that the all-pairs compression bound has been proved with `rho=1-g`, `0<g<=1/2`:

$$
\sup_{\chi,\psi}\|P_\psi E_NP_\chi\|\le\rho.
\tag{2.3}
$$

The orthogonal input and output blocks of (2.1) give

$$
\|K_j\|\le\rho,\quad
N^{-1/2}\|K_j\|_{\rm HS}\le\overline\sigma_{N,d},\quad
\|R_j\|\le2-g,
\tag{2.4}
$$

uniformly in the entire selected route.

Expand

$$
U_N^n=(K_n+R_n)\cdots(K_1+R_1).
\tag{2.5}
$$

Let `S_(n,route)` be the sum of the terms having at most `floor(delta(g)n)` occurrences of `R_j`, where

$$
\delta(g)=\frac{-\log(1-g/2)}{2\log(2(2-g)/g)},
\qquad \eta=\sqrt{1-g/2}.
\tag{2.6}
$$

Every retained term contains at least one `K_j`, since `delta(g)<1`. Place one such factor in HS norm, use (2.4) on all the remaining factors, and then use `|Tr X|<=sqrt N ||X||_HS`. Summing over placements of the `R` factors by the same binomial identity as in the source gives

$$
\boxed{
\frac{|\operatorname{Tr}S_{n,\mathrm{route}}|}{N}
\le\frac{\overline\sigma_{N,d}}\rho\eta^n,
\qquad \|S_{n,\mathrm{route}}\|\le\eta^n.
}
\tag{2.7}
$$

The calculation uses the number of placements and the norms in (2.4), not equality of the `K_j` or `R_j`. This is why no time-independence of the route is needed.

## 3. Complete signed estimate and scope

Let `p_n=Tr U_N^n` and `s_(n,route)=Tr S_(n,route)`. For every array of complex weights with supremum at most `W`,

$$
\boxed{
\frac1{N^2}\sum_{n\ge1}|w_{n,N}|
\left||p_n|^2-|p_n-s_{n,\mathrm{route}}|^2\right|
\le24W\,\frac{\overline\sigma_{N,d}}g.
}
\tag{3.1}
$$

Proof: the square identity is bounded by three times the normalized removed trace because that trace is at most one. Apply (2.7), sum `eta^n`, and use `rho>=1/2`, `1-eta>=g/4`. The difference series is absolutely convergent. This includes the full cross-term with the retained part.

The estimate is uniform over every prescribed route. One may even choose a different route separately at each `n`, because (2.7) is a uniform estimate on each term of the summed bound. This remains an estimate for one chosen route at each time, not the union or coherent sum of the removed histories over all possible routes.

Under `log d>=C_2(log N)^(2/3)`, the audited all-pairs escape estimate supplies the explicit

$$
g_N=\tfrac12\exp[-2C_3(\log N)^{1/3}\log\log N]
$$

used in Section 9 of the source. Then `overline(sigma)_(N,d)/g_N -> 0`, so (3.1) is `o(1)` uniformly over all such selected routes, with the original matrices unchanged. The allowed number of deviations at `n` comparable to `N` is `N^(1-o(1))`, and their fraction tends to zero.

There are `d^(2n)` possible length-`n` relative-character routes. Summing (3.1) over all of them would introduce this uncontrolled factor and would not prove a bound on the full trace. The union also covers arbitrary character histories and has extensive overlaps once deviations are permitted. No estimate on that union, no random-route averaging, and no `H_diag` conclusion is claimed.

