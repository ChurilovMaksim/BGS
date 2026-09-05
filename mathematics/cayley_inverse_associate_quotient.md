# Inverse edge-associate quotient and the multiplicity closure target

**Status: EXACT for the associate-class decomposition, canonical unit-edge skeleton, cross-class contraction criterion, and multiplicity reduction; FINITE-REGRESSION for the displayed small-conductor and split-prime anchors; OPEN for uniform bounds on nonunit associate-class size and on split divisors of cross-class contractions in the intended `K=o(p^(1/4))` regime.**

This note refines the structural-associate theorem.  Universal inverse edge
associations show that eliminating every order-three prime is too strong.  The
right object is the quotient of reduced edges by characteristic-zero unit
association.

## 1. Reduced inverse edges

Let `K=2m+1` be an odd prime, `tau=zeta+zeta^-1`, and

```text
v_0=0,
v_n=(t_n-2)/(tau-2),
w_(a,b)=2-v_a-v_b.                                      (1)
```

Valid inverse edges are unordered pairs of real trace classes excluding the
invalid class `[1]`.  At a split embedding prime `q`,

```text
q | w_(a,b)
```

is exactly the zero pair-sum condition for the two centred trace roots.
Because the valid trace polynomial is squarefree, distinct zero edges are
disjoint, and

```text
I_-1(q)=2 * #{valid zero edges at q}.                    (2)
```

## 2. A canonical skeleton of unit edges

Some reduced edge generators are already units in characteristic zero and can
never contribute finite support.

The trace recurrence is

```text
t_n+t_(n+2)=tau t_(n+1).                                (3)
```

Hence, whenever the displayed trace classes are valid,

```text
w_(a,a+2)
 =(2tau-t_a-t_(a+2))/(tau-2)
 =tau(2-t_(a+1))/(tau-2)
 =-tau v_(a+1).                                          (4)
```

For prime `K`, both factors on the right are units: `v_(a+1)` is a square of a
real cyclotomic unit, while

```text
tau=zeta^-1(1+zeta^2)
```

is a unit because `1+zeta^2=(1-zeta^4)/(1-zeta^2)` is a quotient of associated
prime-conductor cyclotomic differences.

There is one further universal boundary edge.  Since `K=2m+1`,

```text
t_(m+1)=t_m,
t_(m-1)=(tau-1)t_m,                                     (5)
```

and therefore

```text
w_(0,m-1)=-(tau-1)v_m.                                   (6)
```

Here `tau-1=zeta^-1(zeta^2-zeta+1)` is a unit: write

```text
zeta^2-zeta+1=(1+zeta^3)/(1+zeta),                      (7)
```

and each `1+zeta^j=(1-zeta^(2j))/(1-zeta^j)` is a
prime-conductor cyclotomic unit.

Thus the step-two trace skeleton and the boundary edge (6) are support-free.
There can be additional unit edges at special small conductors; no completeness
claim for unit edges is made here.

## 3. Quotient by characteristic-zero association

Let `E_K` be the set of valid inverse edges with nonzero reduced generators.
Define

```text
e ~ f
iff
w_e / w_f is a unit of O^+=Z[tau].                      (8)
```

Equivalently,

```text
(w_e)=(w_f)                                               (9)
```

as principal ideals.  Let `C_K` be the set of equivalence classes after unit
edges are discarded, and put

```text
B_K=max_(C in C_K) |C|.                                  (10)
```

The four `K mod 5` families in
`cayley_inverse_structural_associates.md` give explicit nonunit classes of
size at least two whenever their common norm is not `1`.  They are not asserted
to be the complete list of classes.

## 4. Cross-class contraction integers

For two nonassociate edges `e !~ f`, define the integral ideal

```text
J_(e,f)=(w_e,w_f) subset O^+,                            (11)
```

and its contraction

```text
J_(e,f) intersect Z = D_(K;e,f) Z,
D_(K;e,f)>0.                                              (12)
```

### Proposition 1 (exact same-embedding support)

For every rational prime `p`,

```text
p | D_(K;e,f)
```

if and only if some prime ideal `q|p` contains both `w_e` and `w_f`.
For split `p==1 mod K`, this is exactly the statement that the two distinct
edge classes vanish in one real residue embedding.

### Proof

A rational prime divides the positive generator of `J_(e,f) cap Z` exactly
when `J_(e,f)` is contained in a maximal ideal above that rational prime.  This
is the standard contraction criterion.  On the split locus the residue
embedding identifies `q|w_e,w_f` with the two edge congruences. `□`

This is stronger than `p|gcd(N(w_e),N(w_f))`: rational norms may acquire the
same prime at different embeddings.

## 5. Exact multiplicity reduction

For a split embedding prime `q`, let

```text
Z(q)={e in E_K : q|w_e}.                                 (13)
```

### Theorem 2 (associate quotient reduction)

Assume `q` lies above a rational split prime `p` and that

```text
p does not divide D_(K;e,f)
```

for any pair of nonassociate nonunit edges `e !~ f`.  Then `Z(q)` is contained
in one associate class.  Consequently

```text
I_-1(q)=2|Z(q)| <= 2 B_K.                                (14)
```

### Proof

If `Z(q)` met two distinct associate classes, choose `e,f` from those classes.
Then `q` contains `(w_e,w_f)`, so Proposition 1 gives `p|D_(K;e,f)`, contrary
to the hypothesis.  Unit edges never occur in `Z(q)`.  Equation (2) now gives
(14). `□`

This isolates two independent closure obligations:

```text
(A) bound B_K, the largest characteristic-zero nonunit associate class;
(B) bound split prime divisors of D_(K;e,f) for e !~ f.  (15)
```

If, in the intended large-prime regime `K=o(p^(1/4))`, one proves

```text
B_K=K^o(1)                                                (16)
```

and excludes such `p` from all cross-class contractions, then

```text
I_-1(q)=K^o(1).                                          (17)
```

A uniform `B_K=O(1)` gives a uniform bounded inverse multiplicity in that
regime.  This is enough for the inverse contribution to the quadratic/near-
quadratic row-energy target.  No claim is made that analogous bounds already
hold for the other ratio classes.

## 6. Finite exact controls

### Nonunit associate classes

An exact small-conductor audit groups edges by exact absolute norm and then,
within equal-norm groups, computes `w_e/w_f` in `Q(tau)`, checks that the
quotient lies in `Z[tau]`, and verifies unit norm `+-1`.

For

```text
K=19,23,29,31,37,41,43,47,53,                            (18)
```

every observed **nonunit** associate class has size exactly two.  The large
norm-one class is support-free and is not counted in `B_K`.

The four structural families are not complete.  For example, at `K=31` there
is an additional exact class

```text
(2,11) ~ (5,12),
|N(w_(2,11))|=|N(w_(5,12))|=1303.                        (19)
```

This is finite evidence only; it is not a proof that `B_K<=2` in general.

### One cross-class contraction anchor

At

```text
K=59,
e=(8,26),
f=(9,10),                                                (20)
```

the two edge generators are not associates (their absolute norms are unequal),
but one split embedding at

```text
p=21713                                                   (21)
```

contains both.  Exact Hermite-normal-form contraction of the two-generated
ideal gives

```text
(w_e,w_f) intersect Z = 21713 Z.                         (22)
```

This is a calibrated nonassociate cross-class support event.

### Why the prime range must be explicit

A global bounded-multiplicity conjecture is already false as a useful target.
For example direct complete split enumeration gives

```text
K=83, p=167=2K+1:  7 zero edges, I_-1=14,
K=89, p=179=2K+1:  8 zero edges, I_-1=16.                (23)
```

These lie far outside the intended `K=o(p^(1/4))` regime.

By contrast, available structural large-prime controls include

```text
K=139, p=3596704231 > K^4: I_-1=4,
K=229, p=966684838398077 >> K^4: I_-1=4.                 (24)
```

Finite data therefore support the quotient strategy but do not prove either
(A) or (B).

## 7. New arithmetic target

The previous largest-prime target for the full inverse support asked, in effect,
to eliminate even the universal structural associate classes.  The quotient
formulation removes those deterministic classes first.

A sharper sufficient theorem would be a polynomial cross-class bound such as

```text
P_split^+( product_(e !~ f) D_(K;e,f) ) <= K^(4+o(1)),   (25)
```

combined with

```text
B_K=K^o(1).                                               (26)
```

Because the intended pointwise regime is `K=o(p^(1/4))`, (25)--(26) would force
`I_-1=K^o(1)` there even though individual structural edge norms can possess
split prime factors vastly larger than `K^4`.

The finite observations suggest the cross-class factors may be much smaller
than `K^4` (often on an `O(K^2)` scale), but **no such exponent-two theorem is
claimed**.

## 8. Downstream scope

This note concerns only the inverse product-row ratio.  Completing the Cayley
energy theorem still requires corresponding control of all ratio classes or an
argument showing that the inverse mechanism dominates the worst multiplicity.
Even a sharp Cayley energy theorem remains upstream of the separate
Heisenberg-scale desymmetrized trace problem required for microscopic BGS/RMT.
