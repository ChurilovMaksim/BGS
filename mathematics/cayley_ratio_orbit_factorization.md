# Ratio-orbit factorization and fourth-power structure of the Cayley difference discriminant

**Status: EXACT for odd prime `K`, using the maintained characteristic-zero Cayley collision classification and the classical prime-modulus equality criterion for Dedekind sums.  FINITE-REGRESSION through `K=47`.**

This note refines `cayley_difference_discriminant.md`.  The squarefree nonzero
difference polynomial does not behave as a generic polynomial of degree
`(K-1)^2/2`: it factors into `(K-1)/2` Galois-orbit factors, and its full
discriminant has an exact universal `2`/`K` part times a **fourth power**.

This structure explains the repeated prime exponents seen in every maintained
exceptional-prime computation. The finite cross-resultant data below suggest
`K^4`-scale total mass on the tested orders. They motivate deprioritizing a
naive archimedean improvement, but do not establish an asymptotic obstruction
to improving the `O(K^4)` global resultant budget.

## 1. Ratio classes

Let `K` be an odd prime and put

```text
n=K-1,
m=(K-1)/2.
```

Let `zeta` be a primitive `K`-th root of unity and

```text
c(z)=(z+1)/(z-1).
```

For `r in F_K^*\{1}` and `a in F_K^*`, define

```text
d_(r,a)=c(zeta^a)-c(zeta^(r a)).                         (1)
```

The inversion-swap relation sends

```text
(a,r a) -> (-r a,-a),
```

so it sends the ratio `r` to `r^(-1)`.  Hence introduce

```text
R_K=(F_K^*\{1})/(r~r^(-1)).                              (2)
```

There is one fixed class `r=-1`; all other classes have two members.  Thus

```text
|R_K|=m.                                                 (3)
```

## 2. An integral polynomial for one ratio orbit

For an integer representative `2<=r<=K-1`, set

```text
D_r(X)=(X-1)(X^r-1),
N_r(X)=2(X^r-X),                                         (4)
```

and

```text
A_r(T)=Res_X(Phi_K(X), T D_r(X)-N_r(X)).                 (5)
```

At `X=zeta^a`,

```text
N_r(zeta^a)/D_r(zeta^a)=d_(r,a),                         (6)
```

while

```text
product_a D_r(zeta^a)=K^2.                              (7)
```

Consequently

```text
A_r(T)=K^2 product_{a in F_K^*}(T-d_(r,a)).              (8)
```

Since `Phi_K(X)==(X-1)^n (mod K)` and the second polynomial in (5)
vanishes at `X=1`, every coefficient of `A_r` is divisible by `K`.  Define

```text
F_r(T)=A_r(T)/K in Z[T].                                 (9)
```

Then

```text
deg F_r=n,
LC(F_r)=K,
F_r(0)=2^n.                                              (10)
```

The last identity follows from

```text
product_a (zeta^(r a)-zeta^a)=K.                         (11)
```

The Galois action `zeta -> zeta^u` is transitive on the roots `d_(r,a)`.
The maintained characteristic-zero rigidity theorem shows that no nontrivial
Galois element fixes one such difference.  Therefore `F_r/K` is the monic
minimal polynomial over `Q` of `d_(r,1)` and has degree `n`.

Moreover

```text
F_r=F_(r^(-1)).                                          (12)
```

Indeed inversion-swap identifies their complete root sets.  Conversely, two
ratio factors have a common root only when their ratios are equal or inverse,
again by characteristic-zero rigidity.

It follows that the squarefree nonzero difference polynomial from
`cayley_difference_discriminant.md` factors exactly as

```text
S_K(T)=product_[r] in R_K F_r(T).                        (13)
```

In particular

```text
deg S_K=m n=(K-1)^2/2,
LC(S_K)=K^m.                                             (14)
```

## 3. Even scaling and the congruence `H_r == 1 (mod K)`

Because

```text
d_(r,-a)=-d_(r,a),                                      (15)
```

each `F_r` is even.  Define

```text
G_r(U)=F_r(2U)/2^n.                                      (16)
```

This polynomial is integral.  Indeed, if

```text
A'_r(U)
 =Res_X(Phi_K(X), U D_r(X)-(X^r-X)),                    (17)
```

then

```text
A_r(2U)=2^n A'_r(U),
G_r(U)=A'_r(U)/K,                                        (18)
```

and the same reduction modulo `K` used above shows that `K` divides every
coefficient of `A'_r`.

Since `G_r` is even, write

```text
G_r(U)=H_r(U^2),
H_r(Y) in Z[Y].                                          (19)
```

Then

```text
deg H_r=m,
LC(H_r)=K,
H_r(0)=1.                                                (20)
```

There is a stronger congruence:

```text
H_r(Y)==1 (mod K).                                       (21)
```

To prove it, work in `L=Q(zeta)` and let `lambda=zeta-1`, the unique prime
above `K`.  The norm expression (17) factors as

```text
A'_r(U)
 =N_{L/Q}(lambda)
  N_{L/Q}( U(zeta^r-1)-(zeta^r-zeta)/(zeta-1)).          (22)
```

Here `N(lambda)=K`.  The second factor inside the norm is congruent modulo
`lambda` to the constant `-(r-1)`.  Every conjugate has the same reduction,
so

```text
G_r(U)==(r-1)^n==1 (mod lambda).                         (23)
```

The coefficients of `G_r` are rational integers and
`(lambda) intersect Z=(K)`, hence (21).

Therefore there is a monic polynomial `P_r in Z[Y]` of degree `m`, with
`P_r(0)=0`, such that

```text
H_r(Y)=1+K P_r(Y).                                       (24)
```

## 4. Dedekind sums distinguish the ratio factors

In this section assume `K>=5`, so `m>=2`.  The constant term of `H_r`
then does not contribute to the coefficient of `Y^(m-1)`.

Write

```text
P_r(Y)=Y^m+b_r Y^(m-1)+... .                             (25)
```

The next coefficient is explicit:

```text
b_r=(K-1)(K-2)/12-K s(r,K),                              (26)
```

where `s(r,K)` is the classical Dedekind sum.

### Proof
The roots of `H_r` are

```text
y_(r,a)=(d_(r,a)/2)^2,
```

with `a` taken modulo `a~-a`.  Hence

```text
b_r
 =-sum_{a mod +-1} y_(r,a)
 =-(1/8) sum_{a=1}^{K-1} d_(r,a)^2.                     (27)
```

Using

```text
c(zeta^a)=-i cot(pi a/K),                               (28)
```

together with the classical identities

```text
sum_{a=1}^{K-1} cot^2(pi a/K)=(K-1)(K-2)/3,             (29)

sum_{a=1}^{K-1}
 cot(pi a/K)cot(pi r a/K)=4K s(r,K),                    (30)
```

gives (26).

The prime-modulus equality criterion for Dedekind sums says

```text
s(r,K)=s(s,K)
 iff r==s (mod K) or r s==1 (mod K).                    (31)
```

The nontrivial implication follows, for example, from the standard congruence
behind the Dedekind reciprocity law; it is also Corollary 1.2 of
Jabuka--Robins--Wang, *When are two Dedekind sums equal?*, International
Journal of Number Theory 7 (2011), arXiv:1103.0370.

Therefore

```text
b_r=b_s iff [r]=[s] in R_K.                              (32)
```

In particular, for two distinct ratio classes,

```text
deg(P_s-P_r)=m-1.                                       (33)
```

This one-degree drop is the source of the exact extra factor of `K` in the
cross-resultants below.

For `K=3` there is just one ratio class, represented by `r=2`, and directly

```text
H_2(Y)=1+3Y,  P_2(Y)=Y,  F_2(T)=S_3(T)=3T^2+4.
```

The coefficient of `Y^0` in `P_2` is `0`, whereas the right-hand side of
(26) is `1/3`; hence (26) is not asserted at `K=3`.  There are no distinct
ratio classes to separate or cross-resultants to consider.  The one-factor
and global discriminant formulas below still hold, with `I_2=J_3=1` and
`|Disc(S_3)|=48`.

## 5. Exact cross-resultant square theorem

For distinct `[r],[s] in R_K`, define

```text
M_(r,s)=Res_Y(H_r(Y),P_s(Y)-P_r(Y)) in Z\{0}.            (34)
```

### Theorem 1
For distinct ratio classes,

```text
|Res_T(F_r,F_s)|
 =2^(n^2) K^(K+1) M_(r,s)^2.                             (35)
```

### Proof
At a root `alpha` of `H_r`, equation (24) gives

```text
H_s(alpha)=K(P_s-P_r)(alpha).                            (36)
```

Since both `H_r,H_s` have degree `m` and leading coefficient `K`, while
`P_s-P_r` has degree exactly `m-1`, the Poisson formula gives

```text
|Res_Y(H_r,H_s)|
 =K^(m+1) |M_(r,s)|.                                     (37)
```

Next, composition with `U^2` gives

```text
|Res_U(H_r(U^2),H_s(U^2))|
 =|Res_Y(H_r,H_s)|^2.                                   (38)
```

Finally `F_r(2U)=2^n H_r(U^2)`.  Rescaling the variable and the two
polynomials yields

```text
|Res_T(F_r,F_s)|
 =2^(n^2)|Res_U(H_r(U^2),H_s(U^2))|.                    (39)
```

Since `2(m+1)=K+1`, equations (37)--(39) prove (35).

Thus every cross-resultant has, after the universal `2`- and `K`-parts, an
exact square.

## 6. One-factor discriminants and the maximal real cyclotomic field

Let

```text
J_r(Z)=Z^m H_r(1/Z).                                     (40)
```

Because `H_r(0)=1`, this is a monic polynomial in `Z[Z]`.  Its roots are

```text
z_(r,a)=1/y_(r,a)=4/d_(r,a)^2.                           (41)
```

The stabilizer of `y_(r,1)` in `Gal(Q(zeta)/Q)` is exactly `{+-1}` by the
characteristic-zero collision classification.  Hence `z_(r,1)` generates the
maximal real cyclotomic field

```text
L^+=Q(zeta+zeta^(-1)),
[L^+:Q]=m.                                               (42)
```

Let

```text
I_r=[O_(L^+):Z[z_(r,1)]] in Z_{>0}.                     (43)
```

For prime `K`,

```text
Disc(L^+)=K^(m-1).                                       (44)
```

The usual index-discriminant identity therefore gives

```text
|Disc(J_r)|=K^(m-1) I_r^2.                               (45)
```

Reciprocal polynomials `H_r` and `J_r` have the same discriminant because
`H_r(0)=1`, so

```text
|Disc(H_r)|=K^(m-1) I_r^2.                               (46)
```

Now use `F_r(2U)=2^n H_r(U^2)`.  A direct derivative/resultant calculation
(or the root formula) gives

```text
|Disc(H_r(U^2))|=2^n K |Disc(H_r)|^2,                   (47)
```

and rescaling roots by `2` contributes `2^(n(n-1))`.  Hence

### Theorem 2
For every ratio class,

```text
|Disc(F_r)|
 =2^(n^2) K^(K-2) I_r^4.                                 (48)
```

Thus the non-universal part of every one-orbit discriminant is an exact fourth
power.

## 7. Global fourth-power discriminant theorem

Define the positive integer

```text
J_K
 = product_[r] I_r
   product_[r]<[s] |M_(r,s)|.                            (49)
```

### Theorem 3
For every odd prime `K`,

```text
|Disc(S_K)|
 =2^((K-1)^4/4)
  K^((K-1)(K^2-7)/4)
  J_K^4.                                                 (50)
```

### Proof
For a product of pairwise coprime polynomials,

```text
Disc(product F_r)
 =product Disc(F_r)
  product_{r<s} Res(F_r,F_s)^2                           (51)
```

up to the irrelevant sign.  There are `m` factors and `m(m-1)/2` unordered
pairs.  Substituting (35) and (48), the exponent of `2` is

```text
m n^2 + m(m-1)n^2
 =m^2 n^2
 =(K-1)^4/4,                                             (52)
```

while the exponent of `K` is

```text
m(K-2)+m(m-1)(K+1)
 =(K-1)(K^2-7)/4.                                        (53)
```

All remaining factors combine to the fourth power in (49).

### Corollary 4 (split-prime valuations)
For every prime `p==1 (mod K)`, one has `p!=2,K`, and therefore

```text
v_p(Disc(S_K))=4 v_p(J_K).                               (54)
```

Combining this with the single-discriminant collision theorem gives

```text
Delta_K(p)>0 iff p divides J_K,                          (55)

Delta_K(p)<=16 v_p(J_K).                                 (56)
```

In particular, the previously observed divisibility by four of all split
prime discriminant exponents is structural, not accidental.

## 8. Adversarial scaling test: why this does not yet beat `O(K^4)`

The fourth-power theorem initially suggested that the prime-to-`2K` part of
the discriminant might have only `O(K^3 log K)` logarithmic size. The larger
finite computations below weaken the motivation for that heuristic, but
cannot refute an asymptotic `O(K^3 log K)` bound.

Using the direct ratio resultants (5), without constructing the enormous full
difference discriminant, exact computations give the following average
prime-to-`K` logarithmic size of the residual cross-resultant `M_(r,s)`:

```text
K     average log|M_(r,s)| / K^2
29            0.208402...
31            0.205677...
37            0.228878...
41            0.237168...
43            0.238877...
47            0.247175...
```

The corresponding full prime-to-`2K` fourth-power contribution satisfies

```text
4 log J_K^(2K) / K^4
 =0.08368...  (K=23),
  0.09662...  (K=29),
  0.09616...  (K=31),
  0.10805...  (K=37),
  0.11265...  (K=41),
  0.11376...  (K=43),
  0.11818...  (K=47),                                  (57)
```

where `J_K^(2K)` denotes removal of the `2`- and `K`-parts before taking the
logarithm.

These exact integer data, whose logarithms are displayed numerically, suggest
`K^4`-scale total cross-resultant mass on the tested orders. The earlier
small-`K` heuristic is therefore deprioritized and is not used in any theorem.
Finite data do not prove `Theta(K^4)` growth or disprove `O(K^3 log K)`.

The discriminant compression is a structural simplification. Cancellation or
sparsity **among the split prime divisors of the cross-resultants** remains
a promising target; these data do not prove that an improvement through total
archimedean size is impossible.

## 9. Evidence boundary and next closure target

- Sections 1--7 are exact algebraic consequences of the maintained
  characteristic-zero collision classification, classical cyclotomic field
  discriminants, and the prime-modulus Dedekind-sum equality criterion.
- The numerical values in Section 8 come from exact integer resultant/discriminant
  computations and are used only to reassess a heuristic, not to settle an
  asymptotic growth bound.
- No `O(K^3 log K)` discriminant bound is claimed.
- No theorem here proves local BGS/GOE universality.

The new high-value target is arithmetic rather than archimedean:

```text
control only prime divisors p==1 (mod K)
inside the integers I_r and M_(r,s),                     (58)
```

or prove that their split-prime valuations are sparse on average.  The exact
factorizations (35), (48), and (50) isolate that problem without the redundant
forced `2`/`K` mass that obscured it in the full difference discriminant.
