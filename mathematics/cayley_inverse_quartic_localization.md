# Inverse-row quartic localization and reduced cyclotomic edge ideals

**Status: EXACT for the quartic localization, the pair-sum discriminant factorization, the universal `K`-factor removal, and the split-support ideal criterion; FINITE-CERTIFICATE for the displayed split witnesses; OPEN for an asymptotic largest-supported-prime bound.**

This note continues the inverse-row chain

```text
reflection -> pair-sum square -> translated half-degree resultant
```

from `cayley_product_row_reflection.md`,
`cayley_inverse_pair_sum_factorization.md`, and
`cayley_inverse_resultant_transversality.md`.

The main point is local.  An inverse order-three exception is not merely a
double zero of one large pair-sum polynomial: it is exactly a four-root
configuration with two elementary-symmetric equations.  In cyclotomic trace
coordinates the unavoidable ramified factor at `K` can then be removed
explicitly, leaving two very small algebraic integers of the form

```text
2 - (cyclotomic unit)^2 - (cyclotomic unit)^2.
```

A new finite certificate at `K=89` shows that an inverse exceptional split
prime can already exceed `K^4`.  This kills the strict finite inequality
`p<=K^4`; it does **not** disprove the maintained asymptotic target
`K^(4+o(1))`.

## 1. Inverse centred roots and pair sums

Let

```text
K=2m+1>=7
```

be prime, let `zeta` be a primitive `K`-th root of unity, and write

```text
t_a=zeta^a+zeta^(-a),
tau=t_1,
H_K(T)=(T-2)C_K(T),
P(T)=H_K(T)/(T-tau).
```

For the normalized inverse ratio `r=-1`, put

```text
F(X)=P(tau+X).                                            (1)
```

The roots of `F` are the centred valid trace roots

```text
x_a=t_a-tau,   [a]!=[1].                                 (2)
```

They are nonzero in characteristic zero.  At every split prime
`p==1 mod K`, `p!=K`, the reduction of `F` is split and squarefree and
`F(0)` is a unit.

Let

```text
S_F(Z)=prod_(i<j)(Z-x_i-x_j).                            (3)
```

The maintained pair-sum theorem gives, for each split embedding prime `q|p`,

```text
I_-1(q)=2 ord_(Z=0)(S_F(Z) mod q).                       (4)
```

In particular `I_-1(q)` is even.

## 2. Two zero pair sums must be disjoint

Suppose two distinct factors of `S_F` vanish at `Z=0` modulo a split embedding
prime:

```text
x_i+x_j=0,
x_k+x_l=0.                                               (5)
```

If the two unordered edges shared a vertex, say `i=k`, then (5) would give
`x_j=x_l`.  Squarefreeness of `F` would force `j=l`, contradicting that the two
pair-sum factors are distinct.  Therefore any two distinct zero pair sums use
four distinct roots.

This elementary observation is load-bearing: an inverse order-three event is
already a four-point event, not a three-point collision.

## 3. Canonical quartic certificate

For four distinct centred roots `x_1,x_2,x_3,x_4`, let

```text
e_j=e_j(x_1,x_2,x_3,x_4)                                (6)
```

be their elementary symmetric functions.

### Theorem 1 (quartic localization)

Over any field of odd characteristic on which the four roots are distinct and
nonzero,

```text
{x_1,x_2,x_3,x_4} is the disjoint union of two opposite pairs
iff
e_1=0 and e_3=0.                                         (7)
```

Consequently, on the maintained split locus,

```text
I_-1(q)>=3
iff I_-1(q)>=4
iff there exists a four-subset of valid centred roots
       with e_1=e_3=0 mod q.                             (8)
```

### Proof

If the roots are `{u,-u,v,-v}`, then both odd elementary symmetric functions
vanish.

Conversely, the monic quartic with these roots is

```text
X^4-e_1 X^3+e_2 X^2-e_3 X+e_4.
```

When `e_1=e_3=0`, this polynomial is even.  Hence its root set is invariant
under `X -> -X`.  Since the roots are distinct and nonzero in odd
characteristic, the four roots split into exactly two opposite pairs.

Equation (8) follows from (4), the disjointness observation of Section 2, and
the theorem. `□`

The certificate is pairing-free: it depends only on the four-root set.

## 4. Pair-sum discriminant factorization

The quartic localization has a useful universal companion identity.

Let `F(X)=prod_(i=1)^m(X-x_i)` be any monic polynomial over a domain, and let
`S_F` be (3).  For each four-subset

```text
A={i,j,k,l}
```

define

```text
q_A=e_1(A)^3-4 e_1(A)e_2(A)+8 e_3(A).                   (9)
```

The expression is symmetric in the four roots.  With any labeling of `A`,

```text
q_A
 =(x_i+x_j-x_k-x_l)
  (x_i+x_k-x_j-x_l)
  (x_i+x_l-x_j-x_k).                                    (10)
```

Put

```text
Q_F=prod_(|A|=4) q_A.                                    (11)
```

### Theorem 2 (discriminant of the pair-sum polynomial)

```text
Disc(S_F)=Disc(F)^(m-2) Q_F^2.                           (12)
```

### Proof

The roots of `S_F` are indexed by the edges of the complete graph on the roots
of `F`.  In the discriminant of `S_F`, compare two edges.

If two edges share one vertex, say `{i,j}` and `{i,k}`, their pair-sum
difference is `x_j-x_k`.  For each unordered root pair `{j,k}` there are
exactly `m-2` choices of the shared vertex `i`.  The total contribution from
all intersecting edge pairs is therefore

```text
Disc(F)^(m-2).                                            (13)
```

If the two edges are disjoint, their four vertices determine a unique
four-subset `A`.  The three partitions of `A` into two unordered edges give
exactly the three factors in (10).  Since discriminants square every root
difference, the disjoint-edge contribution is `Q_F^2`.  Multiplying the two
classes proves (12). `□`

On the maintained split locus `Disc(F)` is a unit.  Hence a repeated pair sum
is equivalent to `Q_F=0`.  This is **not** by itself the inverse exceptional
event: the repeated pair sum may be nonzero.  The order-three event requires
the repeated value to be specifically zero, equivalently Theorem 1.

## 5. Removing the universal ramified `K` factor

For `0<=n<=m` define

```text
v_0=0,
v_n=(t_n-2)/(tau-2),   n!=0.                            (14)
```

These are algebraic integers in `O^+=Z[tau]`.  Indeed, with division of
indices by `2` taken modulo `K`,

```text
t_n-2=s_(n/2)^2,
tau-2=s_(1/2)^2,
```

so

```text
v_n=(s_(n/2)/s_(1/2))^2.                                 (15)
```

For prime conductor the quotient in (15) is a real cyclotomic unit.  Thus
`v_n` is the square of a cyclotomic unit.

For an unordered valid edge `e={a,b}` set

```text
w_e=w_(a,b)=2-v_a-v_b.                                   (16)
```

Then the inverse zero-pair equation factors exactly as

```text
2tau-t_a-t_b=(tau-2) w_(a,b).                            (17)
```

Moreover

```text
|N_(L^+/Q)(tau-2)|=K.                                    (18)
```

For every split prime `p!=K`, the factor `tau-2` is therefore a unit at every
prime ideal `q|p`, and

```text
x_a+x_b=0 mod q
iff
w_(a,b)=0 mod q.                                         (19)
```

The factor `K` visible in many unreduced Smith contractions is thus universal
ramification, not part of the prime-to-`K` geometric obstruction.

## 6. Exact local ideal decomposition of inverse support

Let `E_K` be the set of unordered edges between distinct valid trace classes.
For two disjoint edges `e,f in E_K`, define the two-generator ideal

```text
j_(e,f)=(w_e,w_f) subset O^+.                            (20)
```

and the global pair-local product ideal

```text
J_K^pair=product_(e,f disjoint) j_(e,f).                 (21)
```

Equivalently, for every four-subset `A` of valid centred roots define

```text
j_A^(4)=(e_1(A),e_3(A))                                  (22)
```

and

```text
J_K^(4)=product_(|A|=4) j_A^(4).                         (23)
```

### Theorem 3 (exact split support by local two-generator ideals)

For every split rational prime `p==1 mod K`, `p!=K`, the following are
equivalent:

```text
1. some inverse-ratio row pair has I_-1>=3;
2. some embedding prime q|p contains j_(e,f) for two disjoint edges;
3. some embedding prime q|p contains j_A^(4) for a four-subset A;
4. some embedding prime q|p contains J_K^pair;
5. some embedding prime q|p contains J_K^(4).             (24)
```

Hence the rational contractions of `J_K^pair` and `J_K^(4)` have the same
**split rational-prime support** as the maintained inverse support integers
`Theta_K`, `Xi_K`, and the inverse factor of `Lambda_K^(3)`.

Equality of the ideals, contractions, or valuations is not claimed.

### Proof

The equivalence of 1 and 2 is (4), Section 2, and (19).  The equivalence of 1
and 3 is Theorem 1.  Since a prime ideal contains a finite product of ideals if
and only if it contains at least one factor ideal, 2 and 4 are equivalent, as
are 3 and 5.  Rational contraction then gives the stated split-prime support. `□`

This localization is useful computationally and arithmetically: the global
inverse support is a union of explicitly indexed two-generator local ideal
conditions.

## 7. Why gcds of rational norms are only a candidate filter

If a split rational prime `p` divides both

```text
N(w_e), N(w_f),                                           (25)
```

then there exist prime ideals above `p` dividing `w_e` and `w_f`, but they need
not be the **same** prime ideal.  Therefore

```text
p | gcd(N(w_e),N(w_f))                                   (26)
```

is only a necessary rational candidate test for `j_(e,f) subset q`.

A load-bearing finite verifier must perform a same-embedding check: choose a
primitive `K`-th root `h in F_p`, scan the real embeddings
`h -> h^j` modulo inversion, and require both reduced edge equations to vanish
for one and the same `j`.

The maintained adversarial prime

```text
K=41, p=2908049                                           (27)
```

is a useful negative control for this distinction: it can survive a
rational-norm gcd candidate filter for inverse edge pairs while failing the
same-embedding inverse `I>=4` test.  Rational norm gcds must therefore never be
promoted to exact support without the prime-ideal/embedding check.

## 8. A split inverse witness above `K^4`

There is an exact finite certificate

```text
K=89,
p=143207231,
p==1 mod K,
p/K^4 = 2.282469174... .                                 (28)
```

The prime `p` is prime, and

```text
h=28905841 mod p                                         (29)
```

has exact order `89`.  In the corresponding split embedding the valid centred
trace roots have exactly two zero unordered pair sums:

```text
(16,35): 49215600 + 93991631 == 0 mod p,
(20,33): 74755068 + 68452163 == 0 mod p.                 (30)
```

Therefore

```text
ord_0 S_F=2,
I_-1=4.                                                   (31)
```

For the four indices `{16,35,20,33}`, direct finite arithmetic gives the
pairing-free certificate

```text
e_1=e_3=0 mod p.                                         (32)
```

The two reduced cyclotomic edge elements are even sharper:

```text
|N(w_(16,35))|=143207231,
|N(w_(20,33))|=143207231.                                (33)
```

Thus the same split prime is not merely a small divisor of two huge unrelated
norms in this witness: each relevant reduced norm equals `p` exactly.

`computations/cpp/cayley_inverse_k89_witness.cpp` independently checks the
finite-field certificate.  `computations/verification/cayley_inverse_edge_norm_support.py`
checks the reduced cyclotomic norms and supplies the exact norm-candidate to
same-embedding workflow.

### Consequence

The strict finite statement

```text
all inverse order-three split primes satisfy p<=K^4
```

is false.

This witness does **not** disprove the asymptotic sufficient target

```text
P_split^+(Theta'_K)<=K^(4+o(1)),                         (34)
```

because a fixed factor `2.282...` at `K=89` is compatible with a `K^o(1)`
factor.  It does show that exponent `4` is already genuinely approached and
cannot be treated as a visibly loose artefact of the earlier height budget.

## 9. Finite support sweep and performance boundary

An exact prototype using reduced edge norms as a rational candidate filter and
a same-embedding finite-field check found the following inverse split supports
in completed runs:

```text
K=29:  59
K=31:  311, 1303
K=37:  149, 223, 593
K=41:  83, 739
K=43:  173, 431, 1721
K=47:  283, 659, 1129, 6863
K=53:  107, 1061
K=59:  709, 827, 1063, 21713, 50033
K=61:  367, 733, 977, 1831
K=67:  269, 1609, 680453
K=71:  569, 853, 1279, 1847, 2131, 2273, 2557
K=73:  293, 439, 877, 1607, 1753, 6571
K=79:  317, 1423, 2213, 34603
K=83:  167, 499, 997, 1163, 1993, 2657, 4483, 4649, 17702407
K=89:  179, 1069, 2137, 2671, 3739, 3917, 6053, 36313, 143207231
K=97:  389, 971, 1553, 1747, 3299, 3881, 4463, 4657, 5821, 8731, 11447, 69259
K=101: 607, 809, 1213, 3637, 4243, 5051, 6263, 6869, 8081, 10303.  (35)
```

These are finite exact statements only for the displayed completed sweeps.
A later SymPy batch beyond this range was interrupted and contributes **no**
recorded data.

Repeated exact symbolic resultants become the dominant cost around this scale.
The correct performance direction is therefore not a larger brute-force
SymPy sweep: use modular/fraction-free norm computation or a compiled
specialized resultant kernel, while retaining the same-embedding check as the
load-bearing support gate.

## 10. Current arithmetic target

The inverse obstruction is now simultaneously visible as

```text
rho(0)=rho'(0)=0,
S_F(0)=S_F'(0)=0,
deg gcd(E,O)>=2,
there is a four-root set with e_1=e_3=0,
there are disjoint edges e,f with q|(w_e,w_f).            (36)
```

The new local form suggests a sharper question than another global determinant
height estimate:

> For two distinct reduced edge elements
> `w_e=2-u_a^2-u_b^2` and `w_f=2-u_c^2-u_d^2` attached to
> disjoint trace edges in the varying prime cyclotomic field, how large can a
> rational split prime be if one prime ideal above it divides both?

The `K=89` witness warns that any useful theorem must genuinely tolerate
`K^4`-scale primes.  A proof of the maintained `K^(4+o(1))` target, or an
infinite family violating it, remains open.