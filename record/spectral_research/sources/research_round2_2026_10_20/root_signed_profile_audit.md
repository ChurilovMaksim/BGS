> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round2_2026_10_20/root_signed_profile_audit.md`. Embedded SHA256: `be18850a3d06be8e7b26c3aa1a1b979638923537acbe67bfd8dbf49a2223df41`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/research_record.md).

# Root audit of the complete signed three-cell profile

20 October 2026. Input read in full:

`fermionic_signed_three_cell_profile.md`, SHA-256
`edf6fa35b9f60dc9c19fbb4c588265c1157abe637f4bae94e2e4b2b88db68be5`.

## Verdict

PASS for the stated fixed parameter, all sufficiently large odd dimensions,
and the explicitly selected complete three-cell family. The result is

$$
 E_{m,N}^{\rm full}
 =\frac{c_*}{144}m^4\varepsilon^3e^{-\kappa m\varepsilon}
       \operatorname{Tr}K_{2\pi\chi N\varepsilon}^{3}+o(N),
 \quad N\le m\le3N/2,
$$

with uniform error. This is not a statement about the full sum of all
different orbit pairs. Its complement is the explicitly unproved
estimate (8.2) of the input. Neither `H_diag` nor its negation follows.

## Independent checks

1. **Endpoint slopes and normalization.** With fixed-edge Hessian entries
   `alpha=F_QQ`, `beta=F_Qq>0`, `gamma=F_qq`, the half-chain denominator
   satisfies `d=-alpha-gamma-beta^2/d`. The stated limits
   `s_u=alpha+beta^2/d`, `s_s=-gamma-beta^2/d` are fixed by the actual
   slope map `s -> alpha-beta^2/(gamma+s)`. Their horizontal multipliers
   are `d/beta` and `beta/d`, respectively. Thus
   `chi=s_s-s_u=beta(Lambda-Lambda^(-1))>0`. No equality of alpha and
   gamma is required.

2. **Uniform Hessian limit.** The open-chain inverse has a uniform
   maximum row-sum bound by diagonal dominance. Moving the two endpoints
   by `O(Lambda^(-R))` therefore moves all internal positions by that
   amount. On the first and last `floor(R/2)` edges the actual path
   converges uniformly to the fixed orbit. Continued-fraction contraction
   less than `.04` makes the remaining coefficients irrelevant to the
   endpoint diagonal in the limit. The cross entry decays exponentially
   in the full cell length. This proves the required uniform `o(1)`
   without assuming differentiability of the structural conjugacy.

3. **Exact action difference.** At the homoclinic endpoints the momenta
   give the boundary gradient exactly. Moving to the common fixed cut
   gives `p_*+chi delta S+o(delta)` and
   `-p_*+chi delta U+o(delta)`. The cyclic Hessian is
   `-chi I+o(1)`. Strong concavity first confines the actual critical
   vector to an `O(delta)` neighborhood. Substitution yields the
   critical-value correction `chi delta^2 sum(S_previous+U_next)^2/2`.
   Cell constants and the individual S and U squares cancel between
   permutations. Reversal of the coded order gives the sign in (3.11);
   changing that global sign would in any case leave the real trace
   integral unchanged. The deck phase is the exact one supplied by the
   earlier boundary-action proof.

4. **Scale of the error.** The preceding remainder is uniformly
   `o(delta^2)`, and `N delta^2` stays in a fixed compact interval.
   Therefore the quantum phase error is `o(1)`. The exact scalar-cocycle
   comparison is `O(theta^R)` per fixed collection of cells, with no
   factor m. The modulus comparison has error `O(m/N^2)=O(1/N)`.

5. **Noncommuting renewal.** Writing `A_k=sum_(j<k)(zJ)^j`, the identity
   `(I-zBA_k)(I-zJ)=I-zT+z^(k+1)BJ^k` gives the displayed order of the
   numerator and inverse. On the complementary spectral subspace the
   resolvent is uniformly bounded on `|z|<=1.05`. The scalar Schur
   correction is quadratic in the perturbation. Its unique pole is
   `1+kappa epsilon+O(k epsilon^2+epsilon theta^k)`; its normalized
   residue is `Pi+O(k epsilon)`. Removing it leaves a uniformly bounded
   analytic function on the fixed contour. This justifies the claimed
   coefficient estimate for all allowed long middle blocks.

6. **Endpoint measures and avoidance.** The prefix and suffix cylinder
   probabilities normalize by `nu T=nu` and `T h=h`. Their consistency
   uses the correct reversed prefix-operator order. The extra forbidden
   runs crossing a fixed cylinder boundary have total scalar weight
   `O_K(epsilon)` relative to the normalized weight, since they force
   at least `k-K` consecutive zeros. This is a positive scalar bound;
   it does not claim domination of arbitrary Holder norms by a positive
   transfer operator. Fixed-cylinder approximation followed by
   `N -> infinity`, then `K -> infinity`, proves the stated product
   measure with uniform error at the bounded rescaled frequency.

7. **Trace cube.** The integral is `Tr((V_t V_t^*)^3)`, where V_t has
   Hilbert--Schmidt norm one. It is strictly positive, continuous in t,
   and hence bounded below on the compact frequency interval. The more
   general permutation identity and its factorial normalization were
   separately proved in `root_gram_permutation_identity.md`.

8. **Counting.** The two independent length intervals have widths
   `m/24` and `m/12`, giving `m^2/288+O(m)`. The three different gap
   ranges imply primitive period and distinguish the two cyclic orders.
   The unique marker preceding the shortest gap fixes the initial cut.
   Thus each unordered pair occurs once. Its two pointed cross
   directions supply exactly `2m^2`, yielding the coefficient `1/144`.
   The counting remainder contributes `O(m^3 epsilon^3)=O(1)`; all
   relative errors contribute `o(m^4 epsilon^3)=o(N)`.

## Exact scope of the endpoint kernel

The input theorem defines the actual measures by consistent cylinder
probabilities and does not assume that they are uniform interval laws.
The possible identification with an explicitly normalized sine-kernel
compression is a separate geometric statement under investigation.
No such identification is needed for the audited theorem above.

The proof as written has `R_0>=0`. Its estimates also suggest an
extension to any fixed integer `R_0`, because the only requirement is a
fixed compact interval for `N epsilon` and `R -> infinity`. This audit
does not silently alter the frozen theorem's stated range.
