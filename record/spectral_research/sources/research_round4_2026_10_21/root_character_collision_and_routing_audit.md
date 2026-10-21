> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round4_2026_10_21/root_character_collision_and_routing_audit.md`. Embedded SHA256: `05bc62f64f2e7b51106c04f1f6b458dd77aa11bbff7c8fda8bb64fb868bc6bb4`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/arithmetic.md).

# Relative-character collision mass and audit of prescribed routing

21 October 2026. Root-owned argument. The exact family, including the fixed
`tau=10^(-80)`, is unchanged. This is an auxiliary theorem about the actual kick,
not a spectral-universality statement.

## 1. Frozen analytic inputs and their scope

The exact finite-dimensional translation formula is proved in
`counter_one_step_pinching_hs.md`, SHA-256
`a8babde8cfa7cdf0ef794775ac73672431bd9f9d36491f50e3bf19515543c629`.
Its independent audit is `audit_one_step_pinching_hs.md`, SHA-256
`7c59bc69854347e4615db94691d7d15bd86e0e776ce4bc639c07878bc611acce`.
The explicit finite-type argument is in
`audit_explicit_symbol_finite_type16.md`, SHA-256
`1da0fbd15dec74a90a742804f69165f478673ce07aaf7eb38760de7f60cb7ffb`.
It has an independent audit in `dual_audit_explicit_finite_type16.md`, SHA-256
`34ecf87576cb73990458a656200d9b6e41016f0082796beacea247106c4ed90e`.

The root has read the raw exact-shift calculation, center action and transport,
normalized-HS residual, alias trace formula, and both coefficient extractors.
In particular, the proof uses the exact action, rather than replacing its
oscillatory exponential by that of its first-order Taylor term.

These arguments give fixed constants `C,N_0` such that, for every odd `N>=N_0`
and every Weyl translation corresponding to `z` on the torus,

$$
 |\mathcal E_N(z)|
 :=\left|N^{-1}\operatorname{Tr}(E_N^*T_zE_NT_z^*)\right|
 \le C(1+N\operatorname{dist}(z,0))^{-1/16}+C/N.
 \tag{1.1}
$$

The notation in (1.1) does not require an operator for arbitrary real `z`:
only the Weyl grids appearing below are used. The analytic integral estimate is
uniform over real translations and therefore supplies the bound on these grids.

## 2. An exact probability distribution and its squared discrepancy

Let `N=d^2m`, `G=(Z/dZ)^2`, and `D=|G|=d^2`. Use the original modular Weyl
operators

$$
 H_g=T_N(sN/d,uN/d),\quad g=(s,u),\qquad
 P_\chi=D^{-1}\sum_{g\in G}\overline{\chi(g)}H_g.
$$

The cocycle vanishes on this subgroup: every symplectic product of its labels
is a multiple of `N`. Thus `g -> H_g` is an ordinary unitary representation.
The projections are orthogonal, sum to the identity, and have rank `m`.
The rank assertion follows from the Weyl trace: only the identity element has
nonzero trace, equal to `N`, so `Tr P_chi=N/D=m`.

For each relative character define

$$
 \mathcal Q_\nu(X)=\sum_\chi P_{\nu\chi}XP_\chi,
 \qquad p_\nu=N^{-1}\|\mathcal Q_\nu(E_N)\|_{\rm HS}^2.
$$

These maps are mutually orthogonal projections on the Hilbert space of
matrices, and their sum is the identity on that space. Hence

$$
 p_\nu\ge0,\qquad \sum_\nu p_\nu=1.
 \tag{2.1}
$$

Their exact character formula is

$$
 p_\nu=D^{-1}\sum_{g\in G}\overline{\nu(g)}\mathcal E_N(z_g),
 \qquad z_g=(s/d,-u/d).
 \tag{2.2}
$$

Indeed the group average defining `Q_nu` selects exactly the blocks with
output character `nu chi`. Taking its inner product with `E_N` proves (2.2).
The identity term in (2.2) is `D^{-1}`. Orthogonality of characters now gives
the exact Plancherel identity

$$
 \boxed{\sum_\nu|p_\nu-D^{-1}|^2
       =D^{-1}\sum_{g\ne0}|\mathcal E_N(z_g)|^2.}
 \tag{2.3}
$$

There is no lost factor of `D`: the Fourier transform in (2.2) has the
normalization `D^{-1}`, and the sum on the left is unnormalized.

Square (1.1), using `(a+b)^2<=2a^2+2b^2`. For nonzero `z` this is at most

$$
 C N^{-1/8}\operatorname{dist}(z,0)^{-1/8}+C N^{-2}.
$$

Centered lattice shells of radius `j` have at most `Cj` points and torus
distance at least `j/d`. Consequently

$$
 d^{-2}\sum_{z\ne0}\operatorname{dist}(z,0)^{-1/8}
 \le C d^{-15/8}\sum_{j\le d/2+1}j^{7/8}\le C'.
$$

The case `d=1` is an empty sum. Substitution in (2.3) proves, uniformly in all
square divisors,

$$
 \boxed{0\le\sum_\nu p_\nu^2-d^{-2}\le C N^{-1/8}.}
 \tag{2.4}
$$

The nonnegative sign is exact, since the left side equals the sum of squares
in (2.3). This is a collective estimate on all the relative-character masses;
it is stronger than obtaining their squared sum from the individual
`O(N^{-1/16})` discrepancy bound.

## 3. Consequences and their precise meaning

Cauchy--Schwarz in the finite character set gives the total-variation bound

$$
 \frac12\sum_\nu|p_\nu-d^{-2}|\le C d N^{-1/16}.
 \tag{3.1}
$$

Thus these exact masses become uniform in total variation for every allowed
sequence with `d=o(N^(1/16))`. This statement concerns an internal orthogonal
decomposition of the fixed deterministic operator; it is not an additional
randomization of the kick or of the spectrum.

The reciprocal collision mass satisfies

$$
 \left(\sum_\nu p_\nu^2\right)^{-1}
 \ge(d^{-2}+C N^{-1/8})^{-1}
 \ge c\min(d^2,N^{1/8}).
 \tag{3.2}
$$

For completeness, the Shannon entropy obeys

$$
 -\sum_{p_\nu>0}p_\nu\log p_\nu
 \ge-\log\sum_\nu p_\nu^2.
$$

This follows directly from Jensen's inequality for the convex function
`-log`, applied with weights `p_nu` to the numbers `p_nu`; zero weights are
omitted. Hence (3.2) is also a lower bound on the exponential of that entropy.
No independence at subsequent times follows from either (3.1) or (3.2).

## 4. Independent finite-dimensional audit of relative routing

The audited file is `counter_relative_character_routes.md`, SHA-256
`1b27d09f2dc4a8e8d87ccdf31c7b3c7230065e0c5ee35492c7149880a75ecae3`.
The root checked its entire argument. The conclusions below are conditional
only on the separately proved all-pairs compression bound in the stated
divisor range, not on any statistical hypothesis.

First, the character average has coefficient `overline(nu)`, because the
conjugation eigenvalue of `P_psi X P_chi` is `psi overline(chi)`. The resulting
map is an orthogonal projection in HS inner product even when it is not a
positive map on Hermitian matrices. Positivity of that map is nowhere needed.

Second, exact multiplication of the displayed kernel for `M_N` yields

$$
 M_N T_N(a,b)M_N^*=T_N(3a+4b,2a+3b).
$$

It follows that `M_N P_chi=P_(mathsf S chi)M_N`, with
`mathsf S chi=chi circ L` and `L=[[3,-4],[-2,3]]`. Thus
`Q_(nu_j)(E_N) M_N` sends input character `chi` only to the output character
`nu_j mathsf S chi`. This is a permutation for each `j`. Its input and output
blocks are both orthogonal. If every `P_psi E_N P_chi` has norm at most
`rho=1-g`, then each selected operator `K_j` has norm at most `rho`; its
normalized HS norm is at most `sigma_bar=d^{-1}+C N^{-1/32}`. The complementary
operator `R_j=U_N-K_j` has norm at most `2-g`.

For a word of length `n` with `j<n` complementary factors, the HS ideal
inequality, with one selected factor placed in HS norm, gives

$$
 |\operatorname{Tr}(\mathrm{word})|/N
 \le\overline\sigma\,\rho^{n-j-1}(2-g)^j.
$$

This is valid for time-dependent factors. Summing all placements with
`j<=floor(delta(g)n)` uses only the binomial count, where

$$
 \delta(g)=\frac{-\log(1-g/2)}{2\log(2(2-g)/g)},
 \quad z_g=\frac{g}{2(2-g)},\quad\eta=\sqrt{1-g/2}.
$$

Indeed `rho+z_g(2-g)=1-g/2` and `z_g^(-delta(g))=(1-g/2)^(-1/2)`.
The resulting trace bound is `(sigma_bar/rho) eta^n`, and the corresponding
operator bound is `eta^n`. The latter ensures the normalized removed trace
has magnitude at most one, at every dimension and time.

For `p=Tr U_N^n` and the removed trace `s`,
`||p|^2-|p-s|^2|<=2|p||s|+|s|^2<=3N|s|`.
The geometric sum, `rho>=1/2`, and `1-eta>=g/4` therefore prove the exact
all-time bound `24 W sigma_bar/g`, including the full cross-term. The same
estimate remains valid for a separately chosen route at each `n`, since
every per-time bound is uniform in the chosen route.

**Audit verdict:** the finite routing extension is proved as stated, with the
explicit exponent supplied by the independent analytic proofs above. Summing
over all `d^(2n)` routes is not licensed by this estimate. Nor is a new unitary
matrix constructed whose traces equal the retained partial sums.

