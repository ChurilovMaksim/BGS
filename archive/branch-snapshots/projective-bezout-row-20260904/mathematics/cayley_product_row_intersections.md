# Cayley excess as intersections of fixed-product rows

**Status: EXACT for the row decomposition, cross-row excess identity and affine trace-set reduction; FINITE-REGRESSION for explicit designs; the uniform `O(1)` row-intersection theorem is OPEN.**

This note sharpens the structural target behind the pointwise Cayley additive-energy
problem.  It does not prove the desired quadratic theorem, but it reduces that theorem
to a concrete two-row intersection question.

Let `p` be an odd prime, let `H<=F_p^*` have odd order `K`, and put

```text
c(x)=(x+1)/(x-1),
A=c(H\{1}).
```

For `t in F_p`, write

```text
r(t)=#{(x,y) in (H\{1})^2:c(x)+c(y)=t}.                 (1)
```

When `K` is an odd prime and `p==1 mod K`, let `Delta_K(p)` denote the
non-forced additive excess used throughout the Cayley notes, so exactly

```text
E_+(A)=3(K-1)(K-2)+Delta_K(p).                           (2)
```

## 1. Fixed-product rows

For one ordered subgroup pair put

```text
u=xy,
s=x+y.
```

A direct calculation gives

```text
c(x)+c(y)=2(u-1)/(u-s+1).                                (3)
```

Fix `u`.  If `t!=0`, equation (3) determines `s` uniquely (with the case
`t=2` simply giving `s=2`).  The unordered pair `{x,y}` is then the root set of

```text
Z^2-sZ+u.                                                (4)
```

Therefore:

### Lemma 1 (one unordered pair per row and parameter)

For fixed `u in H` and fixed `t!=0`, there is at most one unordered valid pair

```text
{x,y} subset H\{1}
```

with `xy=u` and `c(x)+c(y)=t`.

The central row `u=1` contributes only at `t=0`, because
`c(x^-1)=-c(x)`.

For `u!=1`, define `T_u` to be the set of nonzero parameters supported by the
row, and for `t in T_u` define

```text
omega_u(t)=1  if the unique pair is diagonal x=y,
omega_u(t)=2  otherwise.                                 (5)
```

Thus

```text
r(t)=sum_{u!=1} omega_u(t),  t!=0.                       (6)
```

## 2. Exact cross-row formula for the non-forced excess

For one nonzero sum bin, the contribution from a single row is
`omega_u(t)^2`.  These are precisely the identity/swap collision quadruples of
that unordered pair.  Different rows have different products, so every cross
term is non-forced.

The zero bin has exactly `K-1` ordered representations and is already part of
the centrally symmetric forced baseline.  Summing the one-row nonzero terms
gives

```text
(K-1)(2K-5),                                             (7)
```

the maintained forced nonzero energy.

Hence:

### Theorem 2 (exact row-intersection identity)

For odd prime `K` and split prime `p==1 mod K`,

```text
Delta_K(p)
 =2 sum_{u<v, u,v in H\{1}}
      sum_{t in T_u intersect T_v} omega_u(t)omega_v(t). (8)
```

In particular, since `omega_u(t) in {1,2}`,

```text
2 sum_{u<v}|T_u intersect T_v|
 <= Delta_K(p)
 <=8 sum_{u<v}|T_u intersect T_v|.                       (9)
```

Let

```text
I_K(p)=max_{u!=v}|T_u intersect T_v|.                    (10)
```

Then immediately

```text
Delta_K(p)<=4 I_K(p)(K-1)(K-2).                         (11)
```

Thus any uniform theorem of the form

```text
I_K(p)=K^(o(1))                                          (12)
```

in the sparse split-prime regime would close the centered Cayley target up to
the harmless density term; a uniform `O(1)` theorem would give the clean
quadratic bound

```text
Delta_K(p)=O(K^2).                                       (13)
```

This is the first reduction in the project for which a bounded **two-row**
intersection statement would directly remove the entire remaining `K^(2/3)`
loss.

## 3. Cyclotomic trace-set form of one row

Because `K` is odd, squaring is a bijection on `H`.  For `u!=1`, write

```text
u=w^2,  w in H\{1},
x=wz,
y=wz^(-1),  z in H.                                    (14)
```

The invalid points `x=1` or `y=1` correspond to
`z in {w,w^(-1)}`.  Put

```text
X=z+z^(-1).                                              (15)
```

For `t!=2`, set

```text
mu=t/(2-t).                                              (16)
```

The shifted-product identity from `cayley_shifted_energy_orbits.md` gives

```text
mu=(1-w^2)/(wX-2).                                       (17)
```

The value `t=2` is the projective case `mu=infinity`, i.e. `wX-2=0`.

Now take two distinct rows `w^2` and `q^2`.  A common finite parameter is
equivalent to

```text
(1-w^2)/(wX-2)=(1-q^2)/(qY-2),                           (18)
```

where

```text
X=z+z^(-1),
Y=y+y^(-1),
z,y in H.                                                     (19)
```

After clearing denominators,

```text
Y=alpha X+beta,                                          (20)
```

with the exact constrained coefficients

```text
alpha=w(1-q^2)/(q(1-w^2)),
beta =2(q^2-w^2)/(q(1-w^2)).                             (21)
```

Thus `I_K(p)` is an intersection problem between the cyclotomic trace set

```text
Tr(H)={z+z^(-1):z in H}                                  (22)
```

and a very special affine copy of itself, with one row-specific forbidden trace
removed on each side; the possible projective point `t=2` is handled separately.

Equivalently, before quotienting by `z<->z^(-1)`, the curve is

```text
y+y^(-1)=alpha(z+z^(-1))+beta,                           (23)
```

with `z,y in H`.  A generic Stepanov/Mobius incidence estimate for (23) only
recovers a power-scale bound; the open question is to exploit the special
coefficients (21) and the prime-order cyclotomic structure.

## 4. Why the row target is plausible but not proved

Characteristic-zero Cayley rigidity implies that two distinct product rows
have no common nonzero parameter over the complex prime-order root-of-unity
model.  Finite-field intersections are therefore genuine reduction phenomena.

The active finite regression includes:

```text
(p,K)=(199,11)       generic control,
(p,K)=(461,23)       exceptional excess 288,
(p,K)=(728017,29)    p>K^4, excess 48,
(p,K)=(2908049,41)   p>K^4, excess 192 and I_K(p)=2.
```

The last design is a deliberate negative control: it disproves the stronger
exploratory guess `I_K(p)<=1` even above `p>K^4`.

Broader finite sweeps have so far found only very small row intersections above
`p>K^4`, but no growing-parameter statement is promoted from those runs.

## 5. Closure condition

The present highest-value arithmetic subproblem is now precise:

> **Product-row intersection problem.**  For odd prime `K`, split prime
> `p==1 mod K`, and preferably in the regime `K=o(p^(1/4))`, prove
> `I_K(p)=K^(o(1))` (ideally `O(1)`), or construct a counterexample family.

A proof closes the pointwise Cayley-energy bottleneck through (11).  A
counterexample family would decisively rule out this route and indicate that
one must return to Fourier/character cancellation rather than row geometry.

No microscopic BGS/GOE conclusion is claimed here.