# Even-multiplicity localization in the inverse row

**Status: EXACT for the general opposite-pair criterion, the parity-gcd multiplicity identity, and the translated-resultant coefficient detector; FINITE-REGRESSION for the displayed split controls; OPEN for arithmetic bounds excluding large multiplicity in the intended large-prime regime.**

This note continues

```text
cayley_inverse_pair_sum_factorization.md
cayley_inverse_resultant_transversality.md
cayley_inverse_quartic_localization.md
cayley_inverse_associate_quotient.md
```

and changes the natural inverse threshold once more.  Universal characteristic-zero associate pairs show that multiplicity four is structurally unavoidable.  The next useful obstruction is therefore multiplicity six: three disjoint opposite pairs at one split embedding.

The point of this note is that the quartic `e_1=e_3=0` certificate is the first case of an exact all-multiplicity theorem.  It produces a canonical `d`-scalar detector for `d` simultaneous inverse zero edges.

## 1. Setup

Let `K=2m+1` be an odd prime and let `p!=2,K` be a rational split prime,

```text
p==1 mod K.
```

Fix one real split embedding prime `q|p`.  As in the maintained inverse-row notes, let

```text
F(X)=prod_a (X-x_a),
x_a=t_a-tau,
```

where the product runs over the valid real trace classes `[a]!=[1]`.  On the split locus used here,

```text
F is split and squarefree,
F(0)!=0.                                                  (1)
```

Let

```text
S_F(Z)=prod_(a<b)(Z-x_a-x_b).                            (2)
```

The pair-sum theorem gives

```text
I_-1(q)=2 ord_(Z=0) S_F(Z).                              (3)
```

Because the `x_a` are distinct and nonzero, two distinct zero pair sums cannot share a root.  Hence the zero edges form a matching.

Write

```text
d(q)=#{ {a,b}: x_a+x_b=0 mod q }.                        (4)
```

Every zero factor in (2) is linear and occurs once, so

```text
I_-1(q)=2 d(q).                                          (5)
```

In particular the inverse intersection multiplicity is always even.

## 2. General opposite-pair criterion

Let `k` be a field of characteristic different from `2`, and let

```text
u_1,...,u_(2d)
```

be distinct nonzero elements of an algebraic closure of `k`.  Denote their elementary symmetric functions by `e_j`.

### Theorem 1 (all even localizations)

The following are equivalent:

```text
1. {u_1,...,u_(2d)} is a disjoint union of d opposite pairs;
2. prod_i (X-u_i) is an even polynomial;
3. e_1=e_3=...=e_(2d-1)=0.                               (6)
```

### Proof

If the set is

```text
{z_1,-z_1,...,z_d,-z_d},
```

then

```text
prod_i (X-u_i)=prod_(j=1)^d (X^2-z_j^2),
```

which is even.

Conversely, if the monic polynomial is even, its root multiset is invariant under `X -> -X`.  Since the roots are distinct, nonzero, and the characteristic is not `2`, the involution has no fixed root and partitions the set into `d` opposite pairs.

Finally,

```text
prod_i (X-u_i)
 =X^(2d)-e_1 X^(2d-1)+e_2 X^(2d-2)-...+e_(2d),
```

so evenness is exactly the vanishing of all odd elementary symmetric functions. `□`

### Corollary 2 (canonical inverse `2d`-root certificate)

For every `1<=d<=floor(m/2)`,

```text
I_-1(q)>=2d
iff
there exists a 2d-subset A of valid centred roots with
    e_1(A)=e_3(A)=...=e_(2d-1)(A)=0 mod q.               (7)
```

### Proof

If `I_-1(q)>=2d`, choose any `d` zero edges.  They are disjoint, so their `2d` endpoints satisfy Theorem 1.

Conversely, Theorem 1 turns a `2d`-subset satisfying the odd-symmetric equations into `d` zero edges.  Equation (5) gives `I_-1(q)>=2d`. `□`

The quartic certificate in `cayley_inverse_quartic_localization.md` is exactly `d=2`.

## 3. Exact parity-gcd identity

Write the centred polynomial uniquely as

```text
F(X)=E(X^2)+X O(X^2).                                    (8)
```

### Theorem 3 (multiplicity equals parity gcd degree)

Over the split residue field,

```text
d(q)=deg gcd(E,O),
I_-1(q)=2 deg gcd(E,O).                                  (9)
```

### Proof

Let `y` be a common root of `E` and `O`.  Because `F(0)!=0`, one has `y!=0`.  Choose `z` with `z^2=y`.  Then

```text
F(z)=E(y)+zO(y)=0,
F(-z)=E(y)-zO(y)=0,
```

so `{z,-z}` is one opposite root pair of `F`.

Conversely, if `z` and `-z` are roots of `F`, adding and subtracting the two equations gives

```text
E(z^2)=O(z^2)=0.
```

Distinct opposite pairs give distinct squares: if `z^2=w^2`, then `w=+-z` and the pairs coincide.  Since `F` is squarefree, no extra multiplicity is present.  Thus common roots of `E,O` are in bijection with zero pair sums, proving the first identity.  Equation (5) proves the second. `□`

This is the exact algebraic form of the inverse matching multiplicity.

## 4. Translated resultant gives a `d`-scalar detector

Translate by `Z/2` and write

```text
F(X+Z/2)=E_Z(X^2)+X O_Z(X^2),
rho(Z)=Res_Y(E_Z,O_Z).                                   (10)
```

The multi-root transversality theorem in
`cayley_inverse_resultant_transversality.md` proves, under the squarefree and nonzero hypotheses (1),

```text
ord_(Z=0) rho(Z)=deg gcd(E,O).                           (11)
```

Combining (9) and (11) gives the exact identity

```text
I_-1(q)=2 ord_(Z=0) rho(Z).                              (12)
```

Write

```text
rho(Z)=rho_0+rho_1 Z+rho_2 Z^2+... .                    (13)
```

### Corollary 4 (coefficient detector)

For every `d>=1`,

```text
I_-1(q)>=2d
iff
rho_0=rho_1=...=rho_(d-1)=0 mod q.                       (14)
```

Using coefficients rather than derivatives avoids any factorial convention in positive characteristic.

Thus the hierarchy is

```text
I_-1>=2  <=> rho_0=0,
I_-1>=4  <=> rho_0=rho_1=0,
I_-1>=6  <=> rho_0=rho_1=rho_2=0,
...                                                        (15)
```

The two-scalar theorem was not the end of the inverse structure; it was the `d=2` layer of this exact filtration.

## 5. The new closure threshold: multiplicity six

Set `d=3`.  The preceding theorems give four equivalent local descriptions:

### Corollary 5 (six-root / three-edge localization)

On the maintained split locus,

```text
I_-1(q)>=6
```

if and only if any of the following equivalent events occurs:

```text
1. three disjoint valid zero edges occur at q;
2. some six valid centred roots satisfy e_1=e_3=e_5=0 mod q;
3. deg gcd(E,O)>=3;
4. rho_0=rho_1=rho_2=0 mod q.                            (16)
```

This is the first inverse threshold not forced by the universal size-two associate families in `cayley_inverse_structural_associates.md`.

## 6. Three-generator arithmetic localization

For three pairwise disjoint valid edges `e,f,g`, put

```text
j_(e,f,g)=(w_e,w_f,w_g) subset O^+,                      (17)
```

where

```text
w_(a,b)=2-v_a-v_b.
```

For a six-subset `A` of valid centred roots, put

```text
j_A^(6)=(e_1(A),e_3(A),e_5(A)) subset O^+.               (18)
```

At a split prime ideal `q` away from `K`, the universal factor `tau-2` is a unit.  Therefore

```text
I_-1(q)>=6
iff
q contains j_(e,f,g) for some disjoint triple of edges
iff
q contains j_A^(6) for some six-subset A.                (19)
```

Taking products over all local triples or six-subsets gives exact global ideal supports for the rational primes admitting `I_-1>=6`.  Equality of the resulting ideals or valuations is not claimed.

The arithmetic gain is conceptual: multiplicity six is a **three-generator** local condition, whereas multiplicity four is only two-generator and can be forced by characteristic-zero association.

## 7. Interaction with the associate quotient

Let `B_K` be the largest nonunit characteristic-zero edge-associate class from `cayley_inverse_associate_quotient.md`.

If

```text
B_K<=2,                                                    (20)
```

then an event `I_-1(q)>=6` cannot be supported entirely inside one associate class: three zero edges are present, so at least two of them are nonassociate.  Hence the rational prime below `q` divides a cross-class contraction integer

```text
D_(K;e,f),    e !~ f.                                    (21)
```

This makes precise why the quotient architecture is aligned with the new threshold.  Universal size-two classes may produce arbitrarily large split prime factors while remaining harmless for a bounded-energy goal: they stop at `I_-1=4` unless another class joins them.

More generally, the exact quotient theorem already gives

```text
I_-1(q)<=2 B_K
```

whenever the rational prime avoids every nonassociate cross-class contraction.

## 8. Finite exact controls

`computations/verification/cayley_inverse_even_multiplicity.py` checks independent finite consequences of the exact theorems.

1. `K=29, p=59`: the maximal embedding has exactly `d=3` zero edges, `I_-1=6`.  The six endpoints satisfy `e_1=e_3=e_5=0`; `deg gcd(E,O)=3`; and direct translated-resultant computation gives `ord_0 rho=3`.
2. `K=43, p=173`: exactly `d=4` zero edges in the maximal embedding, with all odd elementary symmetric functions on the eight endpoints zero; `deg gcd(E,O)=4`; and `ord_0 rho=4`.
3. `K=83, p=167=2K+1`: `d=7`, hence `I_-1=14`; the fourteen endpoints pass the full odd-symmetric test and the parity gcd has degree `7`.
4. `K=89, p=179=2K+1`: `d=8`, hence `I_-1=16`; the sixteen endpoints pass the full odd-symmetric test and the parity gcd has degree `8`.
5. For `K=29,p=59`, all `3003` six-subsets of the fourteen valid roots are exhaustively checked: `e_1=e_3=e_5=0` occurs exactly for the unique six-subset made from the three zero edges.

These are regression controls only.  They do not imply a growing-`K` multiplicity theorem.

The high-multiplicity controls at `p=2K+1` are deliberately retained because they falsify any range-free bounded-multiplicity claim.  They lie far outside the intended `K=o(p^(1/4))` large-prime regime.

## 9. Revised arithmetic target

The inverse route no longer needs to eliminate all multiplicity-four support.  A sharper sufficient target is to control the three-edge layer in the intended large-prime regime, for example by proving either

```text
I_-1(q)=K^o(1),                                           (22)
```

or, more concretely, a combination of

```text
B_K=K^o(1)
```

and a polynomial bound/exclusion theorem for split prime divisors of cross-class contractions.

For the especially attractive conjectural bound `B_K<=2`, excluding large-prime cross-class support would immediately yield

```text
I_-1(q)<=4.                                               (23)
```

This concerns only the inverse product-row ratio.  The full Cayley-energy closure still needs the other ratio classes, and microscopic BGS/RMT still additionally requires the separate Heisenberg-scale trace-comparison theorem.
