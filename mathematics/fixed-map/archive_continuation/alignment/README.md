# Once-counted path pairs above half alignment

**Registry:** BGS-TRACE-356.

**Status:** supplementary analytic result from the 22 November packet, with the
fixed-time inputs and their verification boundary stated
[separately](../contacts/README.md). It does not change the status of
BGS-TRACE-005 or BGS-BGS-001. The [packet's full chapter](BGS_Alignment.tex)
also contains the reflection folding, boundary calculation, and finite tests.

## Statement and comparison

Use the canonical [fixed map](../../fixed_map_resolvent_frontier.md),
with `tau = 10^-80`, and put
`a(x)=product_t (U_N)_{x_(t+1),x_t}` for a cyclic word of length `m`.
An alignment is either `f(t)=t+s` or `f(t)=s-t` modulo `m`.
For fixed `1/2 < d <= 1`, write `H_{m,N}(d)` for the sum
of `a(x) conj(a(y))` over all ordered pairs with
`# {t : x_t=y_{f(t)}} >= ceil(dm)` for **some** alignment. Count a
pair only once, even when several alignments qualify. Then the proof
gives, for sufficiently large odd `N` and all `m >= ceil(log N)`,

```math
H_{m,N}(d)=m+O_d(e^{-c_d m}),\qquad c_d>0.
```

The exact once-counted cyclic-orbit contribution also equals
`m+O_d(exp(-c_d m))`, so the noncyclic part of this high-overlap
family is exponentially small. No uniformity in `d` down to
`1/2` or effective startup is asserted.

The cyclic contribution and exact reverse-cyclic family were already
controlled by [FM-021](../../position_chain_mixing.md) and
[FM-022](../../reversed_path_decay.md). Once-counted
[three-cut](../../three_block_unmarking.md) and
[four-cut](../../four_block_unmarking.md) classes are different, defined
by reconnections rather than time-aligned agreement. The previous
[Contacts](../contacts/README.md) argument for the once-counted
alignment union used `d>2/3`; the extension above handles every
fixed `d>1/2`, including even and composite times.

## Proof structure

1. **One alignment.** Mark equality in the tensor propagators
   `U⊗conj(U)` and `U⊗U*` using the diagonal-equality projection `P`.
   In the first case the constant vector on the diagonal yields
   the term `z^m`; remove its line. Compress the return series
   `sum_(j>=1) lambda^(-j) V^j` to the remaining marked space.
   The [fixed-time contact bounds](../contacts/README.md) and the
   geometric tail imply invertibility of the compressed resolvent
   for `|z|=100` and `|lambda|>=exp(1/20)` for all large `N`.
   Thus extracting degrees at least `ceil(dm)` costs at most
   `N^2 exp(m/20) 100^(-dm)/(1-1/100)` after the main term.
   Summing over the `2m` alignments preserves exponential decay when
   `m>=ceil(log N)`.

2. **Large relative rotation order.** If two same-direction
   alignments differ by a rotation of order `r`, their full
   bipartite equality graph is a union of cycles of length `2r`.
   Selecting `k=ceil(dm)` edges from each alignment leaves at most
   `k/r` cycles, so the number of free letters is at most
   `2m-2k+k/r`. With `max |U_xy|^2<=K/N`, the total absolute
   path weight is at most
   `binom(m,k)^2 K^m N^(m-2k+k/r)`. Choose fixed `r_0` such
   that `2d-1-d/(r_0+1)>0`. All intersections containing
   such a pair with `r>r_0`, even summed over the at most
   `2^(2m)` choices in inclusion–exclusion, are exponentially small
   at any prescribed fixed rate for large enough `N`.

3. **Bounded relative order.** The remaining intersections contain at
   most `2 L_0` alignments, `L_0=lcm(1,...,r_0)`. Let
   `r=gcd(L_0,m)`. Fold the time circle into `r` strands per
   word for rotations alone and at most `2r` for rotations and
   reflections; only at most two residue classes are left at the
   reflection boundary. The folded transfer is a tensor product
   `W` of copies of `U`, its conjugate or their transposes.
   Each regular section meets each alignment in a perfect matching.
   Two different such matchings have disjoint edge sets on regular
   sections. If together they exceed the number of positions in
   one word of the section, they force three strands to share a
   letter. A positive fraction of sections must do this when
   the two alignments both pass the `d>1/2` threshold.

4. **Folded marked resolvent.** Let `R` project onto overloaded
   sections and `D(z)` mark all alignment degrees, with each
   `|z_f|=1`. Write `V=D(z)W`. Expand `R` by the Boolean
   threshold inclusion–exclusion; every term contains a
   three-strand equality. After a fixed number of visits to `R`,
   at least two selected triples touch a common strand. Start
   with the earlier triple and stop at the next equality that
   touches it. A third strand not involved in the stopping
   equality preserves orthogonality of the input letters. On
   each such input the stopping equality has probability
   `O_j(1/N)`, by the entrywise bound on the relevant fixed
   powers of `U`. Interim marks act only on the outside
   strands. Consequently a fixed power of
   `sum_(j>=1) lambda^(-j) R V^j R` is `o(1)`, uniformly
   for `|lambda|>=2`. Here one first truncates the geometric
   tail, then sends `N` to infinity. Mark `R` by an extra
   variable `u`; the resolvent of
   `[I+(u-1)R]V` is bounded on `|lambda|=2` for any fixed
   `|u|<=M`. If the folded chain has length `n`, the
   boundary matrix has polynomial trace norm in `N`, and
   Cauchy extraction of at least `eta n` visits costs
   `2^n M^(-eta n)` up to polynomial factors. Fix a sufficiently
   large `M`, then send `N` to infinity. This controls
   each multiple intersection, not just its two-mark marginal.

5. **Remove multiplicities.** Full inclusion–exclusion combines the
   previous bounds. There are only polynomially many bounded-order
   subsets in step 3. To subtract cyclic copies exactly, note that
   their weight is `sum_x d(x)|a(x)|^2`, with `d(x)` the
   minimal period. Replacing `d(x)` by `m` costs at most
   `m^2 K^m N^(-m/2)`, and the intensity-chain estimate gives
   `|Tr(P_intensity^m)-1| <= N(1/100)^m` for large `N`.

## What this removes from the pair problem

Let `R_{m,N}(d)` denote the signed sum over pairs with **fewer**
than `ceil(dm)` matches in **every** alignment. For the weight
`w=|bhat_*|^2` of the [standalone problem](../../../../record/remaining_breakthrough_task_20261021.md),

```math
\Delta_{2,N}(b_*)=\int_1^2(t-1)w(t)\,dt
+N^{-2}\sum_{\lceil\log N\rceil\le m<2N}
w(m/N)R_{m,N}(d)+o(1).
```

The short band contributes `o(1)` already by the repository's
[uniform trace bound](../../fixed_kick_uniform_trace_bound.md):
`|Tr U^m|<=Ca^m`, `1<a<sqrt(3+2 sqrt(2))<e`. This replaces
the stronger log-band pressure input used in the packet for this
particular deduction. The high-overlap sum then gives the complete
linear ramp in the displayed normalization. The **whole weighted
residual** must supply its negative correction; no pointwise limit
or support restriction on that residual follows. A diagonal choice
can take `d=d_N` to `1/2` from above, with no quantified rate.

At the exact boundary the packet additionally treats a pair of
forward alignments separated by `m/2` and no three-letter
coincidence anywhere. Each section has one of two complete
pairings, each used equally often. The two-pattern transfer has
a constant-vector switch coefficient `-1/N+O(N^-2)`, and
a complementary block of norm `<1/4`. A closed sequence using both
patterns has at least two switches; the fixed-degree coefficient
and the replacement by the two-dimensional compression both cost
`O(m/N^2)`. Thus at `m≍N` this contribution is `O(1/N)`
per such intersection. Summing this bound over the at most `m`
choices per time still gives a vanishing contribution to the
weighted microscopic pair sum on each compact Heisenberg band.
This is **not** a bound on the full union
at `d=1/2`, on general switching classes, or on the remaining
factorial hierarchy.

## Verification boundary

The [finite check](../../../../computations/verification/bgs_f_november/alignment/check.py)
tests the folding layout, exact root-of-unity polynomial identities
for small tensors, and the finite switching identities. It does not
test fixed-strength asymptotics or certify the contact inputs.
