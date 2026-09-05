# Same-embedding inverse support versus congruence modulo a rational prime

**Status: EXACT for the split ideal decomposition and the impossibility of rational-modulus vanishing for one valid inverse edge; EXTERNAL-SOURCE-SCOPE for the interpretation of Dvornicich--Zannier as working in `Z[mu]/(ell)`; FINITE-REGRESSION for displayed split witnesses.**

This note records a load-bearing scope distinction for attempts to use the
literature on roots-of-unity relations modulo a prime.

The inverse row needs a congruence modulo **one chosen prime ideal**

```text
q | p
```

of a split cyclotomic field.  This is not the same problem as a congruence
modulo the rational ideal

```text
p O.
```

The distinction is decisive: for a valid inverse edge at a split prime
`p!=K`, rational-ideal vanishing is impossible, even though one-prime-ideal
vanishing occurs in many exact witnesses.

## 1. Split residue embeddings

Let `K=2m+1` be an odd prime, let `zeta` be a primitive `K`-th root, and let

```text
O=Z[zeta].
```

If

```text
p==1 mod K,
p!=K,                                                       (1)
```

then `p` splits completely in `Q(zeta)`:

```text
p O = product_(j=1)^(K-1) P_j.                              (2)
```

Choosing a primitive `K`-th root `h in F_p^*`, the residue maps may be indexed
so that

```text
zeta mod P_j = h^j,     1<=j<=K-1.                          (3)
```

The prime ideals are pairwise comaximal.  Hence, for every `alpha in O`,

```text
alpha in pO
iff
alpha in P_j for every j.                                  (4)
```

For a Laurent polynomial `L in Z[X^+-1]`, this says

```text
L(zeta)==0 mod pO
iff
L(h^j)==0 mod p for every 1<=j<=K-1.                       (5)
```

By contrast, a same-embedding inverse event imposes (5) for only one `j`
(up to the real conjugation identification after passing to `O^+`).

## 2. The inverse edge Laurent polynomial

For a valid inverse edge

```text
e={a,b},
0<=a<b<=m,
a,b!=1,                                                    (6)
```

put

```text
L_e(X)
 =X^a+X^-a+X^b+X^-b-2X-2X^-1.                             (7)
```

This is the direct trace relation from
`cayley_inverse_cyclotomic_unit_normalization.md`:

```text
L_e(zeta)=t_a+t_b-2tau=-(tau-2)w_e.                        (8)
```

Multiplying by the Laurent unit `X^b`, define

```text
H_e(X)=X^b L_e(X)
       =X^(a+b)+X^(b-a)+X^(2b)+1
        -2X^(b+1)-2X^(b-1).                               (9)
```

After collecting coincident exponents, `H_e` is a nonzero polynomial and

```text
deg H_e<=2b<=2m=K-1.                                      (10)
```

Non-vanishing is immediate from the top term: because `b>=2` and `a<b`, the
term `X^(2b)` is not cancelled by any of the other displayed exponents.

Also

```text
H_e(1)=0.                                                  (11)
```

## 3. Rational-modulus vanishing is impossible on the split locus

### Theorem 1

Under (1) and (6),

```text
L_e(zeta) notin pO.                                       (12)
```

Equivalently, no valid inverse edge relation vanishes modulo the rational ideal
`pO`.

### Proof

Assume the contrary.  By (5), `H_e(h^j)=0` for every
`j=1,...,K-1`.  These are exactly all roots of

```text
Phi_K(X)=1+X+...+X^(K-1)                                  (13)
```

in `F_p`, since `p==1 mod K`.  Therefore

```text
Phi_K | H_e   in F_p[X].                                  (14)
```

By (10), either `H_e=0` or

```text
H_e=c Phi_K                                                     (15)
```

for some `c in F_p`.  The first alternative is excluded above.  Evaluating
(15) at `X=1` gives

```text
0=H_e(1)=c Phi_K(1)=cK.                                   (16)
```

Since `p!=K`, `K` is nonzero modulo `p`; hence `c=0`, again contradicting
`H_e!=0`. `□`

### Corollary 2

Every actual split inverse zero edge is intrinsically a **one-prime-ideal**
event:

```text
P | L_e(zeta)
```

for at least one but never all `P|p`.

Thus no theorem whose hypothesis is vanishing in the quotient

```text
Z[mu]/(p)
```

can be applied directly to a single same-embedding inverse edge.

## 4. Why this matters for Dvornicich--Zannier

Dvornicich--Zannier, *Sums of roots of unity vanishing modulo a prime*, studies
congruences modulo a rational prime in the cyclotomic integer ring.  The same
scope is explicit in the later use by Kedlaya--Kolpakov--Poonen--Rubinstein:
they work in

```text
Z[mu]/(2)
```

and cite Dvornicich--Zannier as the direct modulo-prime analogue of the
Conway--Jones classification.

That theory is therefore a useful comparison and classification framework for
**rational-ideal** congruences.  Theorem 1 shows that the maintained split
inverse event lies outside its direct hypothesis.

This resolves the apparent paradox created by the exact witness

```text
K=229,
p=966684838398077,
weight(L_e)=8.                                            (17)
```

The supporting weight-eight relation is indecomposable modulo one split prime
ideal, yet has level `K=229`.  There is no contradiction with a
Conway--Jones/Dvornicich--Zannier type bound because the relation does not
vanish modulo `pO`; it vanishes only at one residue embedding.

Any future use of that literature for this project therefore requires a new
**local / one-prime-ideal strengthening**, not a direct invocation of the
rational-modulus theorem.

## 5. Finite controls

`computations/verification/cayley_inverse_prime_ideal_vs_rational_modulus.py`
checks the distinction on exact split anchors.

For each displayed edge it enumerates all real split embeddings and verifies:

```text
K=59,  p=21713,            cross-class edge support;
K=89,  p=143207231,        structural support;
K=229, p=966684838398077,  large structural support.
```

In every case the edge relation vanishes at the recorded supporting embedding
but not at all embeddings.  The finite checks are regression only; Theorem 1
is the proof of the universal split statement.

## 6. Consequence for the active route

The sparse weight-eight normal form remains useful, but the correct arithmetic
question is now sharply stated:

```text
two or three nonassociate weight-eight Laurent relations
share one primitive K-th root in one residue embedding modulo p.           (18)
```

This is a local sparse common-root problem, not a rational-modulus vanishing-sum
problem.  The active routes remain the associate quotient, reduced ordinary
resultants, and characteristic-zero sparse unlikely intersections; none is
replaced by a direct Dvornicich--Zannier shortcut.
