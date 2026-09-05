# Shared-endpoint inverse gcd factors are torsion and support-free

**Status: EXACT for the torsion classification and support-free real-cyclotomic resultant of every shared-endpoint polynomial gcd; FINITE-REGRESSION for the maintained symbolic controls.**

This note removes an entire sector from the open shared-factor problem in
`cayley_inverse_reduced_resultant_filter.md`.

Two distinct inverse edges that share one endpoint can have nonconstant
characteristic-zero polynomial gcds, but every such gcd is a torsion factor and
evaluates to a unit at the prime-conductor real cyclotomic root.  Hence the
open non-torsion gcd problem is supported only on **disjoint** edge pairs —
exactly the sector relevant to simultaneous inverse zero edges.

## 1. Setup

Let `K=2m+1` be an odd prime and let

```text
0<=a,b,c<=m,
a,b,c != 1,
b!=c.                                                       (1)
```

Consider the two distinct valid edges

```text
e={a,b},
f={a,c}.                                                    (2)
```

As in the inverse normalization notes, put

```text
t_n(T)=2 T_n(T/2),
v_0(T)=0,
v_n(T)=(t_n(T)-2)/(T-2),
w_(r,s)(T)=2-v_r(T)-v_s(T).                                (3)
```

Let

```text
C_K(T)
```

be the minimal polynomial of

```text
tau=zeta_K+zeta_K^-1,
deg C_K=m.                                                   (4)
```

## 2. Subtracting two edges kills the shared endpoint

The identity

```text
-(T-2) w_(r,s)(T)=t_r(T)+t_s(T)-2T                         (5)
```

implies

```text
-(T-2)(w_(a,b)-w_(a,c))=t_b-t_c.                           (6)
```

Let

```text
G=gcd_Z[T](w_(a,b),w_(a,c))                                (7)
```

be the monic primitive gcd.

### Lemma 1

```text
G | (t_b-t_c) in Z[T].                                     (8)
```

### Proof

The gcd divides the difference `w_(a,b)-w_(a,c)`.  Equation (6) gives

```text
G | (t_b-t_c)/(T-2)                                       (9)
```

whenever the quotient is interpreted in `Q[T]`; in particular `G|(t_b-t_c)`.
Gauss's lemma returns divisibility in `Z[T]`. `□`

For the torsion conclusion, only the weaker displayed divisibility (8) is
needed.

## 3. Every reciprocal common root is torsion

Let `alpha!=0` and set

```text
T_0=alpha+alpha^-1.                                        (10)
```

The Chebyshev trace identity gives

```text
t_n(T_0)=alpha^n+alpha^-n.                                 (11)
```

Hence a root of `t_b-t_c` satisfies

```text
alpha^b+alpha^-b=alpha^c+alpha^-c.                         (12)
```

Multiplying by `alpha^b` factors the relation exactly:

```text
(alpha^(b-c)-1)(alpha^(b+c)-1)=0.                          (13)
```

### Theorem 2 (shared-endpoint torsion theorem)

Every root of the reciprocal lift

```text
G~(z)=z^deg(G) G(z+z^-1)                                  (14)
```

is a root of unity.  More precisely, its order divides either

```text
|b-c|  or  b+c.                                           (15)
```

Consequently every irreducible factor of `G~` over `Q` is cyclotomic.

### Proof

Lemma 1 and (11)--(13) give (15) for every reciprocal root of `G`. `□`

Since

```text
1<=|b-c|<=m,
2<=b+c<=2m=K-1                                             (16)
```

except for the harmless possibility of order `1`, every nontrivial reciprocal
order is strictly smaller than `K`.

The order-one possibility corresponds to `alpha=1`, hence `T_0=2`.  It cannot
occur in `G`: the removable-value identity

```text
v_n(2)=n^2                                                 (17)
```

gives

```text
w_(r,s)(2)=2-r^2-s^2.                                     (18)
```

For a valid edge neither endpoint equals `1`; the smallest possible square sum
is `0^2+2^2=4`.  Thus every valid edge has

```text
w_(r,s)(2)!=0.                                             (19)
```

Therefore every reciprocal order occurring in `G~` satisfies

```text
1<n<K.                                                     (20)
```

## 4. Prime-conductor evaluation is a unit

The reciprocal lift of the real prime-conductor polynomial is exactly

```text
z^m C_K(z+z^-1)=Phi_K(z).                                  (21)
```

We need only the following elementary cyclotomic resultant identity.

### Lemma 3

If `K` is prime and `1<n<K`, then

```text
|Res(Phi_n,Phi_K)|=1.                                     (22)
```

### Proof

Let `omega` range over the primitive `n`-th roots.  Since `gcd(K,n)=1`, the
map

```text
omega -> omega^K                                          (23)
```

permutes that set.  Using

```text
Phi_K(X)=(X^K-1)/(X-1),                                   (24)
```

we get

```text
Res(Phi_n,Phi_K)
 =product_(omega primitive n) Phi_K(omega)
 =product_omega (omega^K-1)/(omega-1)
 =1.                                                       (25)
```

Up to the irrelevant resultant orientation sign this proves (22). `□`

### Theorem 4 (shared-endpoint gcds are support-free)

For every pair (2),

```text
|Res_T(C_K,G)|=1.                                         (26)
```

### Proof

By Theorem 2 and (20), `G~` is a product of cyclotomic polynomials `Phi_n` with
`1<n<K`, with multiplicities allowed.  Lemma 3 gives

```text
|Res_z(Phi_K,G~)|=1.                                      (27)
```

The reciprocal-square identity from
`cayley_inverse_reduced_resultant_filter.md` gives

```text
Res_z(Phi_K,G~)=Res_T(C_K,G)^2.                           (28)
```

Thus (26) follows. `□`

## 5. Consequence for the open torsion classification

The universal open statement

```text
all shared inverse edge-polynomial gcd factors are torsion                 (29)
```

is now already proved whenever the two edges share an endpoint.

Therefore any non-torsion counterexample to (29) must use four distinct
endpoints:

```text
e={a,b},
f={c,d},
|{a,b,c,d}|=4.                                             (30)
```

This is exactly the disjoint-edge sector relevant to finite-field inverse
multiplicity.  The sparse unlikely-intersection / Filaseta--Granville--Schinzel
reduction should therefore be focused only on (30); the shared-endpoint sector
needs no external theorem and no finite search.

For the reduced-resultant filter, Theorem 4 is stronger still: every
characteristic-zero polynomial gcd from a shared endpoint can be removed with
no finite rational-prime support at the prime conductor `K`.

## 6. Finite regression

`computations/verification/cayley_inverse_shared_endpoint_torsion.py` checks:

1. the reciprocal factorization

```text
z^b (t_b-t_c)(z+z^-1)
 =(z^(b-c)-1)(z^(b+c)-1)                                  (31)
```

for a grid of integer pairs;
2. `v_n(2)=n^2` and the absence of `T=2` roots for valid edges;
3. every shared-endpoint gcd at `K=31` has

```text
|Res(C_K,G)|=1.                                           (32)
```

The finite checks are regression only; Theorems 2 and 4 are exact proofs.
