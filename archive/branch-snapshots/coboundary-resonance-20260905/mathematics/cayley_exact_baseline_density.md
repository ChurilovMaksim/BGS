# Almost-all exact Cayley baseline below the `theta=1/5` density threshold

**Status: EXACT, conditional only on the same classical Bombieri--Vinogradov theorem and prime number theorem used in `cayley_jacobi_trace_average.md`.**

This note strengthens the existing double-averaged quadratic theorem from

```text
Delta_K(p)=o(K^2) in density
```

to the integer-valued statement

```text
Delta_K(p)=0 exactly in density,
```

at the smaller but still polynomial scale `K=X^theta`, `0<theta<1/5`.
The point is elementary but useful: `Delta_K(p)` literally counts ordered
non-forced collision quadruples and is therefore a nonnegative integer.  Once
the global resultant mass budget is combined with a lower bound on the weight
of one bad prime, it bounds the **number of bad designs**, not merely their
average excess.

The theorem is not a microscopic BGS theorem.  It is an exact additive-energy
rigidity statement for asymptotically almost every split pair in the stated
double average.

## 1. Setup

Let `K` be an odd prime and let `p==1 (mod K)` be prime.  Let `H<=F_p^*` be
the unique subgroup of order `K`, and put

```text
A=c(H\{1}),
c(h)=(h+1)/(h-1).
```

Write

```text
E_K^nz(p)=sum_{d!=0} r_{A-A}(d)^2
```

for the nonzero-difference energy.  Identity and central inversion force the
exact baseline

```text
B_K=(K-1)(2K-5),
```

and the maintained resultant note proves

```text
Delta_K(p):=E_K^nz(p)-B_K in Z_{>=0}.                    (1)
```

Moreover, with

```text
N_K=K^3-5K^2+6K+1,
C_K=(K-1)log 12-3log K,
```

the exact global weighted-prime budget is

```text
sum_{p==1 mod K} Delta_K(p) log p <= N_K C_K.            (2)
```

For `K>=3`, the rough bounds

```text
N_K<K^3,
C_K<K log 12                                             (3)
```

will suffice.

Fix `0<theta<1/2`, let `Q=X^theta`, and use the same dyadic design family as
in `cayley_jacobi_trace_average.md`:

```text
D_theta(X)
 = {(K,p):
      K,p prime,
      Q/2<K<=Q,
      X/2<p<=X,
      p==1 (mod K)}.                                    (4)
```

Bombieri--Vinogradov plus the prime number theorem gives, for fixed
`theta<1/2`,

```text
|D_theta(X)|
 ~ [log 2/(2 theta)] X/(log X)^2.                        (5)
```

Define the bad subfamily

```text
B_theta(X)={(K,p) in D_theta(X): Delta_K(p)>0}.          (6)
```

## 2. Bad-design counting theorem

### Theorem 1
For every fixed `0<theta<1/2`,

```text
|B_theta(X)| <<_theta X^(5 theta)/(log X)^2,             (7)
```

and consequently

```text
|B_theta(X)|/|D_theta(X)| <<_theta X^(5 theta-1).        (8)
```

In particular, for every fixed

```text
0<theta<1/5,                                             (9)
```

one has

```text
|B_theta(X)|/|D_theta(X)| -> 0.                          (10)
```

Thus asymptotically almost every pair in `D_theta(X)` has

```text
Delta_K(p)=0                                             (11)
```

**exactly**.

### Proof
Fix a prime `K in (Q/2,Q]`.  If `(K,p)` is bad and `X/2<p<=X`, then the
integrality in (1) gives

```text
Delta_K(p)>=1,
```

hence its contribution to the left side of (2) is at least `log(X/2)`.
Therefore

```text
#{p in (X/2,X]: p prime, p==1 mod K, Delta_K(p)>0}
 <= N_K C_K/log(X/2)
 <  (log 12) K^4/log(X/2).                              (12)
```

Summing over prime `K in (Q/2,Q]` gives

```text
|B_theta(X)|
 <= (log 12)/log(X/2)
    sum_{Q/2<K<=Q, K prime} K^4.                         (13)
```

By the prime number theorem and partial summation,

```text
sum_{Q/2<K<=Q, K prime} K^4 << Q^5/log Q.               (14)
```

Since `Q=X^theta`, equations (13)--(14) yield

```text
|B_theta(X)| <<_theta Q^5/(log X)^2
              = X^(5 theta)/(log X)^2,                  (15)
```

which proves (7).  Dividing by (5) proves (8), and (10) follows when
`5 theta-1<0`.

No pointwise prime-number theorem for a varying modulus is used.  The only
place Bombieri--Vinogradov enters is the denominator count (5), exactly as in
the previously maintained double-average theorem.

## 3. Exact energy consequence

The zero-difference class contributes exactly `(K-1)^2`, while the forced
nonzero baseline is `(K-1)(2K-5)`.  Hence whenever `Delta_K(p)=0`,

```text
E_+(A)
 =(K-1)^2+(K-1)(2K-5)
 =3(K-1)(K-2).                                          (16)
```

Combining (10) and (16) gives:

### Corollary 2 (almost-all exact quadratic energy)
For every fixed `0<theta<1/5`, asymptotically almost every
`(K,p) in D_theta(X)` satisfies the exact identity

```text
E_+(c(H\{1}))=3(K-1)(K-2).                              (17)
```

Equivalently, all additive collision quadruples are accounted for by the
zero-difference class together with the identity and central-inversion
relations.

This is stronger than an `O(K^2)` bound on this density-one subfamily: the
entire non-forced collision excess vanishes.

## 4. Exact Jacobi-trace fourth moment on the good subfamily

The maintained trace identity gives, for `q!=0`,

```text
mu_2(K,p)
 =(K-1)(p-K+1)/(K^2(p-1)),                              (18)

mu_4(K,p)
 =[p E_+(A)-(K-1)^4]/[K^4(p-1)].                        (19)
```

On the exact-baseline subfamily (17), therefore

```text
mu_4(K,p)
 =[3p(K-1)(K-2)-(K-1)^4]/[K^4(p-1)].                    (20)
```

The standardized nonzero-frequency fourth-moment ratio is exactly

```text
kappa(K,p)=mu_4/mu_2^2
 =(p-1)[3p(K-2)-(K-1)^3]
   /[(K-1)(p-K+1)^2].                                   (21)
```

Consequently

```text
kappa(K,p)=3+O(1/K+K^2/p)                               (22)
```

uniformly on the good dyadic subfamily.  For fixed `0<theta<1/5`, both error
terms tend to zero because `K asymp X^theta` and `p asymp X`.

Again, (21)--(22) are fourth-moment statements for the ordinary full Jacobi
trace.  They do not imply a central-limit theorem and do not constitute local
eigenphase universality.

## 5. Why the exponent is `1/5`

The threshold here is transparent.  The exact resultant theorem supplies a
per-`K` total logarithmic collision budget `O(K^4)`.  Detecting merely whether
a design is bad costs one unit of the integer excess, rather than the `K^2`
normalization used in the previous averaged theorem.  Summing `K^4` over the
prime `K`-window costs `Q^5`, while the number of dyadic designs is of order
`X/(log X)^2`.  The resulting bad fraction is therefore

```text
O_theta(Q^5/X)=O_theta(X^(5 theta-1)).                  (23)
```

A constant-size symmetry orbit of every non-forced collision could improve the
constant in (23) but **not** the exponent `1/5`.  Raising the exponent by this
route requires a genuine improvement of the `O(K^4)` global resultant budget,
a growing lower multiplicity for every bad reduction, or a stronger structural
restriction on the prime divisors of the orbit resultants.

## 6. Evidence boundary

- Equations (1)--(3) are inherited from the exact resultant mass-budget proof.
- Equation (5) is the previously maintained Bombieri--Vinogradov/PNT design
  count.
- The new step is the integer bad-design count (12)--(15).
- No finite computation is used in the proof.
- No statement here proves microscopic BGS/GOE statistics.

The next high-value questions are therefore structural: can the total
resultant budget be reduced below `K^(4+o(1))`, or can one prove that every
non-forced split reduction consumes a growing amount of that budget?  Either
would move the exact-baseline density threshold beyond `theta=1/5`.
