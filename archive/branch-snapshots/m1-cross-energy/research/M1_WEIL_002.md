# M1 cycle 002 — regular single-twist Weil bound

Status: **ANALYTIC LEMMA ESTABLISHED FROM A STANDARD WEIL THEOREM; M1 ASSEMBLY STILL OPEN**.

This cycle closes the old perfect-power / individual regular-fiber issue. It does **not** close the cross-twist energy estimate.

Reference used: R. Lidl and H. Niederreiter, *Finite Fields*, 2nd ed., Theorem 5.41: if a multiplicative character has order `t>1` and a polynomial is not a `t`-th power, then its complete character sum is bounded by `(e-1) sqrt(q)`, where `e` is the number of distinct roots in the splitting field.

Executable hypothesis audit: `code/research/m1/regular_weil_classifier.py` plus independent `regular_weil_classifier.cpp`.
Result: `results/research/m1/regular_weil_classifier.json`.

## 1. Setup

Let `N` be an odd prime, let `H < F_N^*` have order `K`, and let

`m=(N-1)/K > 1`.

Choose a primitive multiplicative character `omega` of exact order `m`, extended to `F_N` by `omega(0)=0`. Every character trivial on `H` is `omega^r`, `r in Z/mZ`.

For a regular difference `d != 0` and a twist pair `(r,s)`, the cycle-001 regular fiber sum is

`A_{r,s}(d) = sum_{y admissible} omega(((y+d)/y)^r ((y+d-1)/(y-1))^s)`,

where admissibility removes the points at which any of

`y`, `y-1`, `y+d`, `y+d-1`

vanishes.

The historical proof treated this as a rational-function sum and then referred to a `K`-th-power obstruction. The relevant character order is `m`, not `K`.

## 2. Polynomial domain mask

Let

`Q_d(Y)=Y(Y-1)(Y+d)(Y+d-1)`.

For `r in {0,...,m-1}`, write

`r^- = (-r) mod m`,

and similarly `s^-`.

Define the monic polynomial

`P_{r,s,d}(Y) = Q_d(Y)^m (Y+d)^r Y^{r^-} (Y+d-1)^s (Y-1)^{s^-}`.

The factor `Q_d^m` is the key device.

On an admissible `y`, all four linear factors are nonzero, so

`omega(Q_d(y)^m)=1`,

and, because `omega` has order `m`,

`omega(y^{r^-})=omega(y)^{-r}`,

with the analogous identity for `(y-1)`. Hence

`omega(P_{r,s,d}(y))`

is exactly the original regular summand.

At every inadmissible `y`, `Q_d(y)=0`, so `P_{r,s,d}(y)=0` and the extended character contributes zero.

Therefore the restricted rational sum is **exactly** the complete polynomial character sum

`A_{r,s}(d) = sum_{y in F_N} omega(P_{r,s,d}(y))`.

No `O(1)` endpoint correction is needed.

## 3. Distinct-root count

Because `d != 0`, the only collisions among

`-d, 0, 1-d, 1`

occur at `d=1` or `d=-1`.

Thus:

- if `d notin {0,1,-1}`, `P_{r,s,d}` has exactly four distinct roots;
- if `d=1` or `d=-1`, it has exactly three distinct roots.

The large multiplicities coming from `Q_d^m` do not matter: Theorem 5.41 uses the number of **distinct** roots.

## 4. Non-`m`-th-power classification

The `Q_d^m` factor changes every root multiplicity by a multiple of `m`, so only the residues from the twist factors matter.

### Generic case: `d notin {0,1,-1}`

The four root multiplicities modulo `m` are

`r, -r, s, -s`.

If all four were divisible by `m`, then `r=s=0` in `Z/mZ`.

Therefore every nontrivial twist pair `(r,s)!=(0,0)` gives a polynomial that is not an `m`-th power.

### Collision `d=1`

The distinct roots are `-1,0,1`, with multiplicities modulo `m`

`r, s-r, -s`.

If all were zero modulo `m`, the first and third give `r=s=0`.

Thus every nontrivial twist is again non-`m`-th-power.

### Collision `d=-1`

The distinct roots are `0,1,2`, with multiplicities modulo `m`

`-r, r-s, s`.

Again, simultaneous divisibility by `m` forces `r=s=0`.

Hence for every `d!=0` and every nontrivial annihilator twist, `P_{r,s,d}` satisfies the non-power hypothesis of the standard multiplicative-character Weil theorem.

## 5. The bound

Apply Lidl--Niederreiter Theorem 5.41 to the complete polynomial sum.

For generic regular differences there are four distinct roots, therefore

`|A_{r,s}(d)| <= 3 sqrt(N)`.

For `d=1` or `d=-1` there are three distinct roots, therefore the sharper bound

`|A_{r,s}(d)| <= 2 sqrt(N)`

holds.

Consequently, uniformly over all regular fibers and all nontrivial quotient twists,

`|A_{r,s}(d)| <= 3 sqrt(N),  d != 0`.

This matches the empirical cycle-001 envelope and improves the historical `4 sqrt(N)` constant while fixing its missing singular-fiber qualification.

## 6. What the executable classifier checks

The proof above is general. The Python/C++ programs are not substitutes for it; they are regression checks for the residue bookkeeping.

Both implementations exhaustively check the three divisor categories for

`m=4,18,20,210`,

including all `m^2-1` nontrivial pairs in each category. They independently find zero non-power failures. `m=210` is included because it is the quotient-character order for the large historical `N=3571,K=17` stress case.

## 7. What this closes and what it does not

Closed by this cycle:

- the correct character-order statement (`m`, not `K`);
- the singular qualification (`d!=0`);
- endpoint/exclusion handling via an exact polynomial domain mask;
- the perfect-power classification for every regular twist;
- the individual regular-fiber estimate `3 sqrt(N)` from a standard theorem.

Still open:

- whether the upstream spectral observable exactly centers away the singular term;
- the full cross-twist Gram/covariance sum;
- an assembled energy remainder that vanishes in the true arithmetic regime;
- the downstream spectral implication.

The next analytic workstream is therefore **M1-003/M1-004: centering plus assembled cross-twist covariance**, not another attempt to improve the individual Weil constant.
