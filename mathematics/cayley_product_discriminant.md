# The Cayley product discriminant

**Status: EXACT for odd prime `K`, conditional only on the multiplicative rigidity theorem in `cayley_multiplicative_rigidity.md`.  FINITE-REGRESSION for `K=5,7,11,13`.**

This is the multiplicative analogue of `cayley_difference_discriminant.md`.
It packages every non-forced finite-field product collision of the Cayley image
into the discriminant of one canonical squarefree product polynomial.

## 1. Product resultant

Let

```text
Q_K(X)=((X+1)^K-(X-1)^K)/2,
n=K-1.                                                     (1)
```

The roots of `Q_K` are the characteristic-zero Cayley set

```text
A_K={c(zeta^a):a in F_K^*}.                              (2)
```

and `Q_K(0)=1`, so no root is zero.  Define

```text
R_K^x(T)
 =Res_X(Q_K(X), X^n Q_K(T/X)) in Z[T].                   (3)
```

The root-product formula shows that a complex number `t` occurs as a root of
`R_K^x` with multiplicity exactly

```text
#{(a,b) in A_K^2: ab=t}.                                 (4)
```

Let

```text
S_K^x(T)=primitive squarefree part over Q[T] of R_K^x(T). (5)
```

By multiplicative Cayley rigidity, each root of `S_K^x` has characteristic-zero
weight

```text
w(alpha) in {2,4}.                                       (6)
```

The weight-two classes are exactly the fixed loci `x=y` and `x=-y`; all other
classes have weight four.  Burnside's lemma therefore gives

```text
deg S_K^x
 =[(K-1)^2+2(K-1)]/4
 =(K^2-1)/4.                                             (7)
```

As in the additive case, all roots are integral away from the cyclotomic prime
above `K`; hence the leading coefficient of the primitive integral polynomial
`S_K^x` has no prime support away from `K`.

## 2. Reduction at a split prime

Let `p==1 (mod K)` be prime and let `H<=F_p^*` be the unique subgroup of order
`K`.  Put

```text
A=c(H\{1}).                                               (8)
```

Choose a Teichmuller primitive `K`-th root in `Q_p` reducing to a generator of
`H`.  Every characteristic-zero product root of `S_K^x` is `p`-integral and
reduces to the corresponding finite-field Cayley product.

Partition the roots of `S_K^x` into reduction clusters `C_t`.  Then exactly

```text
r_x(t)=#{(a,b) in A^2:ab=t}
      =sum_{alpha in C_t} w(alpha).                      (9)
```

The forced characteristic-zero product-energy baseline is

```text
B_K^x
 =sum_alpha w(alpha)^2
 =4(K-1)(K-2).                                          (10)
```

Define the non-forced multiplicative excess

```text
Delta_K^x(p)=E_x(A)-B_K^x >=0.                           (11)
```

Then the cluster expansion is

```text
Delta_K^x(p)
 =2 sum_t sum_{alpha<beta in C_t} w(alpha)w(beta).       (12)
```

## 3. Single-discriminant theorem

Write

```text
Disc_K^x=Disc(S_K^x) in Z\{0}.                           (13)
```

### Theorem 1
For every odd prime `K` and every split prime `p==1 (mod K)`,

```text
Delta_K^x(p)>0
 iff
p divides Disc_K^x.                                     (14)
```

Moreover,

```text
Delta_K^x(p) <= 16 v_p(Disc_K^x).                       (15)
```

### Proof
The leading coefficient is a `p`-adic unit and all roots lie in `Q_p`, so

```text
v_p(Disc_K^x)
 =2 sum_{alpha<beta}v_p(alpha-beta).                     (16)
```

Let `N_p` be the number of unordered pairs of distinct roots that coalesce
modulo `p`.  Then

```text
v_p(Disc_K^x)>=2N_p.                                     (17)
```

A positive discriminant valuation is therefore equivalent to at least one
nontrivial merger, proving (14).  Since every weight is at most four,

```text
Delta_K^x(p)
 <=2*16*N_p
 <=16 v_p(Disc_K^x),                                    (18)
```

which proves (15).

Consequently

```text
sum_{p==1 mod K} Delta_K^x(p) log p
 <=16 log |Disc_K^x|_(split).                            (19)
```

This is an exact compression statement; no improved asymptotic bound for the
right side is asserted here.

## 4. Exact small cases

For `K=5`, direct elimination gives

```text
R_5^x(T)
 =(5T^2-1)^4
  (5T^2-10T+1)^2
  (5T^2+10T+1)^2.                                       (20)
```

For `K=7`,

```text
R_7^x(T)
 =(7T^3-35T^2+21T-1)^2
  (7T^3-7T^2-7T-1)^4
  (7T^3+7T^2-7T+1)^4
  (7T^3+35T^2+21T+1)^2.                                 (21)
```

The exponents `2` and `4` are exactly the forced multiplicities from the two
weight classes.

For the promoted finite designs:

```text
K=11:
split prime divisors of Disc(S_11^x)={23,89},

K=13:
split prime divisors of Disc(S_13^x)={53,79,313}.       (22)
```

Thus multiplicative exceptional primes form a strict subset of the maintained
additive exceptional sets in these cases.  Exact energies are

```text
K=11:
Delta_x(23)=192,
Delta_x(67)=0,
Delta_x(89)=16,

K=13:
Delta_x(53)=128,
Delta_x(79)=96,
Delta_x(131)=0,
Delta_x(157)=0,
Delta_x(313)=16.                                        (23)
```

The corresponding split discriminant valuations include

```text
K=11: v_23=20, v_89=4,
K=13: v_53=12, v_79=12, v_313=4,                        (24)
```

and obey (15).

## 5. Why this matters for the additive BGS route

The trace/unipotent reformulation of Cayley additive energy introduces the
hyperbolic parameter points

```text
q_v=(beta_v,2 alpha_v),
alpha_v=1/(v-v^(-1)),
beta_v=(v+v^(-1))/(v-v^(-1)),                            (25)
```

with

```text
beta_v^2-(2alpha_v)^2=1,
beta_v+2alpha_v=c(v),
beta_v-2alpha_v=c(v)^(-1).                               (26)
```

Hence their Minkowski distance satisfies

```text
D_m(q_v,q_w)
 =(c(v)-c(w))(c(v)^(-1)-c(w)^(-1)
 =2-c(v)/c(w)-c(w)/c(v).                                 (27)
```

Equality of two such distances is therefore equivalent to equality of Cayley
ratios up to inversion.  The rectangular-quadruple/Minkowski energy of this
one-dimensional hyperbola is controlled exactly by the multiplicative energy
of the same Cayley image.  Theorems 1 and the characteristic-zero rigidity
result isolate the arithmetic obstruction to making that auxiliary energy
near-quadratic in every reduction.

This still does **not** prove the additive centered target

```text
E_+(A)=(K-1)^4/p+O(K^(2+o(1))).                          (28)
```

A remaining high-value route is to combine near-quadratic control of the
Minkowski parameter energy with a specialized rich-incidence theorem for this
single unipotent/conic family.

## Evidence boundary

- Theorem 1 is exact once `cayley_multiplicative_rigidity.md` is established.
- Equations (20)--(24) are finite exact regressions.
- No universal near-quadratic finite-field multiplicative-energy theorem is
  claimed.
- No microscopic BGS/GOE statement is inferred from this discriminant theorem.
