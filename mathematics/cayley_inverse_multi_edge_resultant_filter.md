# A multi-edge reduced-resultant filter for inverse multiplicity six

**Status: EXACT for the multi-edge necessary condition and radical support inclusion; FINITE-REGRESSION for the displayed high-multiplicity anchors; OPEN for a uniform bound on the resulting triple filters.**

The preferred inverse threshold is now `I_-1>=6`, not `I_-1>=4`: universal
characteristic-zero associate pairs make multiplicity four structurally
unavoidable.  This note adapts the ordinary reduced-resultant filter to the
first genuinely new threshold.

The key point is elementary but useful.  A one-embedding three-edge event forces
one rational prime to divide **three different pair filters simultaneously**.
Taking their gcd can remove false-positive factors that occur in only one pair.

## 1. Pair filter recalled

For two valid inverse edges `e,f`, write their real-trace edge polynomials as

```text
w_e(T)=G_(e,f)(T) A_(e,f)(T),
w_f(T)=G_(e,f)(T) B_(e,f)(T),
gcd(A_(e,f),B_(e,f))=1,                                  (1)
```

where `G_(e,f)` is the monic polynomial gcd.  Let `C_K(T)` be the real
prime-conductor cyclotomic polynomial.  Define

```text
Rred_(K;e,f)
 = |Res_T(C_K,G_(e,f)) Res_T(A_(e,f),B_(e,f))|.           (2)
```

The theorem in `cayley_inverse_reduced_resultant_filter.md` gives

```text
q|w_e(tau), w_f(tau),   q|p
    ==> p | Rred_(K;e,f).                                (3)
```

This implication is one-way.

## 2. Multi-edge gcd filter

Let

```text
E={e_1,...,e_d},   d>=2,                                  (4)
```

be distinct valid edges and define the rational integer

```text
M_(K;E)
 = gcd_(1<=i<j<=d) Rred_(K;e_i,e_j).                     (5)
```

### Theorem 1 (same-embedding multi-edge filter)

If one prime ideal `q|p` satisfies

```text
w_(e_i)(tau)==0 mod q   for every i=1,...,d,              (6)
```

then

```text
p | M_(K;E).                                              (7)
```

### Proof

Condition (6) implies the two-edge condition for every pair `(e_i,e_j)`.
Applying (3) to each pair shows that `p` divides every integer in the gcd (5),
hence divides `M_(K;E)`. `□`

The theorem does not assert a converse: the pair resultants may vanish modulo
`p` at different polynomial roots or for different specialization mechanisms.

## 3. Exact ideal contraction and radical inclusion

Let

```text
J_E=(w_(e_1)(tau),...,w_(e_d)(tau)) subset O^+            (8)
```

and write its contraction as

```text
J_E cap Z = D_(K;E) Z,   D_(K;E)>=0.                      (9)
```

### Corollary 2

For every nonzero contraction,

```text
rad D_(K;E) | rad M_(K;E).                               (10)
```

### Proof

Let `p|D_(K;E)`.  Since `J_E cap Z` is contained in `(p)`, the ideal

```text
J_E+p O^+                                                 (11)
```

is proper; otherwise an integer congruent to `1 mod p` would lie in
`J_E cap Z`.  Choose a prime ideal `q` containing (11).  Then `q|p` and every
edge generator lies in `q`.  Theorem 1 gives `p|M_(K;E)`. `□`

Valuation divisibility is not claimed.

## 4. The multiplicity-six specialization

For three pairwise disjoint edges put

```text
M_(K;e,f,g)
 =gcd(Rred_(K;e,f),Rred_(K;e,g),Rred_(K;f,g)).            (12)
```

The exact even-multiplicity theorem says

```text
I_-1(q)>=6
iff
there exist three disjoint zero edges e,f,g at q.         (13)
```

### Corollary 3 (rational filter for `I_-1>=6`)

Every split rational prime supporting inverse multiplicity at least six divides
at least one integer (12) attached to a triple of pairwise disjoint valid
edges.

Thus a global one-way support integer is

```text
M_K^(6)=product_(e,f,g pairwise disjoint) M_(K;e,f,g),    (14)
```

with

```text
I_-1(q)>=6, q|p  ==>  p | M_K^(6).                       (15)
```

No claim is made that the prime support of (14) is exact.

## 5. Why the triple gcd can be substantially sharper

An ordinary pair resultant often has rational prime factors that are false
positives for the distinguished real cyclotomic embedding.  A true three-edge
event, however, forces the **same** rational prime into all three pair filters.
False-positive factors need not persist across all pairs.

This is visible already in exact small anchors.

### `K=29, p=59`

The maximal embedding has exactly three zero edges

```text
(3,11), (4,8), (6,12).                                   (16)
```

The three pair filters are

```text
2*59,
23*59,
59,                                                       (17)
```

so

```text
M_(29;e,f,g)=59.                                         (18)
```

### `K=43, p=173`

The maximal embedding has four zero edges

```text
(3,13), (6,17), (8,14), (12,20).                         (19)
```

The six pair filters contain various extra factors

```text
5, 19, 101, 211, 929, 1559, 7193,                       (20)
```

but the gcd of all six is exactly

```text
173.                                                      (21)
```

More strongly, **every** three-edge subcollection already has triple filter
exactly `173`.

## 6. High-multiplicity finite regression

`computations/verification/cayley_inverse_multi_edge_resultant_filter.py`
checks every triple of zero edges at the maximal embedding for

```text
(K,p)=(29,59):   1 triple,
(K,p)=(43,173):  4 triples,
(K,p)=(83,167): 35 triples,
(K,p)=(89,179): 56 triples.                              (22)
```

For all `96` triples, exactly

```text
M_(K;e,f,g)=p.                                            (23)
```

It also checks that the gcd of **all** pair filters from the complete zero-edge
set equals `p` in each of the four anchors.

This is finite regression only.  It does not prove that (23) holds for arbitrary
`K,p`, nor that the triple filter has no large false-positive prime divisors.

## 7. Revised arithmetic target

The triple filter is aligned with the actual inverse closure threshold:

```text
structural associate pairs may create I_-1=4,
I_-1>=6 requires one additional disjoint edge,
that additional event forces a common prime divisor across three pair filters.
```

A high-value next theorem would bound the largest split prime divisor of
`M_(K;e,f,g)` for disjoint triples, preferably at a scale that excludes such
primes in the intended regime

```text
K=o(p^(1/4)).                                              (24)
```

This is potentially weaker and more natural than bounding every pair resultant,
because structural size-two associate classes are harmless unless a third edge
joins them.

The filter concerns only the inverse ratio.  General product-row ratios and the
Heisenberg-scale spectral closure remain open.
