# From band-limited to Schwartz factorial correlations

**Status: proved deterministic extension lemma.** This corrects the separate
high-frequency-tail requirement in §6 of `trace_to_local_statistics_bridge.md`.
It supplies no arithmetic or dynamical trace estimates, and makes no claim
of priority or of a solution of BGS.

Fix `k >= 2`, and put `d=k-1`. Take `N` labelled points `x_j` on the circle
of length `N`, allowing coincident positions. Define the positive measure

```text
mu_N = (1/N) sum_(j_1,...,j_k distinct) sum_(ell in Z^d)
       delta_(x_(j_1)-x_(j_k)+N ell_1,...,
              x_(j_d)-x_(j_k)+N ell_d).
```

Its action is exactly the anchored factorial statistic of the bridge note.
The conclusions also hold for **positive normalized averages** of these
measures. Discard finitely many initial dimensions and assume `N>2`.

## 1. Occupation bounds

Let `n(t)` count periodic points, with multiplicity, in `[t,t+2)`. A window
contains at most one lift of each labelled point because `2<N`. For
`Q_a=a+[0,1)^d`, with `a_k=0`,

```text
mu_N(Q_a) <= (1/N) integral_0^N product_(i=1)^k n(t+a_i) dt
          <= (1/N) integral_0^N n(t)^k dt.                     (1)
```

For each tuple counted by the cube, choose anchor lift `y_k` and integrate
`t` over `[y_k-1,y_k]`, of length one. Every other lift belongs to
`[t+a_i,t+a_i+2]`, and the anchor to `[t,t+2]`. Endpoint choices affect only
a null set of `t`. For fixed `t`, these tuples inject into those counted by
the occupancy product: each shifted window admits only one lift per label.
Integration over a period counts each original anchored atom with weight
one. Dropping distinctness only enlarges the product. Hölder and periodic
translation invariance prove the second inequality.

Writing `(r)_k=r(r-1)...(r-k+1)`, the exact identities are

```text
(1/N) integral_0^N n(t) dt = 2,
(1/N) integral_0^N (n(t))_k dt
  = integral (2-span(0,z_1,...,z_d))_+ d mu_N(z).               (2)
```

Here `span` means maximum minus minimum. Each ordered distinct-label tuple,
with fixed relative lifts, fits in a length-two interval for a set of
starting points of length exactly `(2-span)_+`. Summing these overlap
lengths proves (2), including coincident positions. Its integrand is at
most two and supported in `[-2,2]^d`.

For every nonnegative integer `r`,

```text
r^k <= k^k ((r)_k+r).
```

For `r<k`, use `r^k<=k^(k-1)r`; for `r>=k`, every factor of `(r)_k` is at
least `r/k`. Therefore

```text
sup_a mu_N(Q_a) <= 2 k^k (1+mu_N([-2,2]^d)).                  (3)
```

Positivity and normalization allow averaging these inequalities with the
same constant term. Constants are deliberately not optimized.

## 2. A positive band-limited majorant

Choose nonzero nonnegative `eta in C_c^infinity(R^d)` and let
`h=inverse_Fourier(eta)` with the bridge note's `2 pi` convention. Then
`h` is Schwartz and `h(0)>0`. Choose `epsilon>0` sufficiently small that
`|h(epsilon z)|>=h(0)/2` throughout `[-2,2]^d`. Thus

```text
B(z)=4 |h(epsilon z)|^2 / h(0)^2
```

is nonnegative, Schwartz, at least one on that cube, and has compact
Fourier support (the difference of two scaled copies of `supp(eta)`).
Boundedness of the single statistic `mu_N(B)` implies, by (3),

```text
mu_N(a+[0,1)^d) <= M  uniformly in a,N.                       (4)
```

Convergence on all band-limited Schwartz tests bounds this one test. No
absolute high-frequency trace-sum estimate is inferred or required.

## 3. Extension theorem

**Theorem.** Let `mu_N,nu_N` be positive normalized averages of the above
spectral measures, at fixed `k`. Suppose `nu_N(B)` is bounded and
`mu_N(f)-nu_N(f)->0` for every Schwartz `f` with compact Fourier support,
with **no fixed upper bound on that support**. Then this comparison holds
for every Schwartz function. If the reference sequence has a Schwartz
local-statistics limit, the other sequence has the same limit.

**Proof.** Comparison on `B` bounds both sequences on that test. Hence (4)
holds for both with a common `M`. For `p>d`,

```text
|mu_N(g)| <= M sum_(q in Z^d) sup_(z in q+[0,1)^d) |g(z)|
          <= C_(d,p) M sup_z (1+|z|)^p |g(z)|.                (5)
```

The same holds for `nu_N`. Choose smooth compactly supported `chi`, equal
to one near zero, and set

```text
f_R=inverse_Fourier(chi(xi/R) Fourier(f)(xi)).
```

Then `f_R->f` in Schwartz topology, with each `f_R` band-limited. Bound
(5) makes approximation errors uniform in `N`. First let `N` tend to
infinity at fixed `R`, then let `R` tend to infinity. □

A target-free version also holds: finite limits on every band-limited
Schwartz test imply limits on all Schwartz tests. The same bounds and
approximation prove the Cauchy property directly. The limit is a positive
continuous functional on Schwartz space, hence a tempered positive measure.

## 4. Limits of the statement

A fixed Fourier cap is insufficient in general. For even `N`, compare the
unit clock with the period-two configuration with basis `{0,a}`, where
`0<a<2`, `a!=1`. Their pair measures are exactly

```text
mu_N^clock = sum_(r in Z) delta_r - sum_(r in Z) delta_(Nr),
mu_N^a = sum_(r in Z) delta_(2r)
       + (1/2) sum_(r in Z) [delta_(2r+a)+delta_(2r-a)]
       - sum_(r in Z) delta_(Nr).
```

For Fourier support in `(-1/2,1/2)`, Poisson summation gives the same action
`integral f - sum_r f(Nr)` on both. Their full limits differ, for example
at `a=1/2`. This counterexample uses a fixed small cap; no assertion about
every possible cap is needed.

Signed averages break the proof. At `N=12`, `k=2`, take the normalized
signed combination `2 mu_clock-mu_cluster`, with all cluster positions
coincident. Its mass on `[-2,2]` is `2*4-11=-3`, while its mass on `[6,7)`
is `2`. Thus (3) would incorrectly assert `2<=-16`. Signed normalization
alone does not suffice.

The corrected bridge target is Heisenberg trace comparison at every fixed
`k` and every compact Fourier support, under positive normalized averages
and a reference limit (or the majorant bound stated above). A separate tail
assumption is unnecessary in this setting. The arithmetic or dynamical
trace-comparison problem itself remains unresolved.

## 5. Regression evidence

`computations/verification/correlation_extension.py` independently checks
cube counts and piecewise occupation integrals with exact rational
arithmetic, for clocks, clusters, repeated points and seeded configurations.
These finite checks supplement, and do not replace, the proof above.
