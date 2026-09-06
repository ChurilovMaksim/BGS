# Direct additive-energy bound for the Cayley image of a subgroup

**Status: EXACT, conditional only on the cited Vyugin--Makarychev Stepanov theorem; FINITE-REGRESSION anchors are maintained independently.**

This note gives a growing-`K` bound for the mixed Cayley term that does not
classify cyclotomic exceptional primes.  It applies uniformly to generic and
exceptional reductions in its stated size range.

## Setup

Let `p` be an odd prime, let `H <= F_p^*` be a multiplicative subgroup of
order `K`, and put

```text
c(h)=(h+1)/(h-1),
A=c(H\{1}).
```

The Cayley map is injective on `F_p\{1}` and `c(h^-1)=-c(h)`, so

```text
|A|=K-1,   A=-A,   0 in A iff K is even.
```

Write

```text
r(t)=#{(a,b) in A^2 : a+b=t},
E_+(A)=sum_t r(t)^2.
```

Because `A=-A`, this is also the difference energy used by
`cayley_additive_energy.md`.

## Bilinear fibers

For `x,y != 1`,

```text
c(x)+c(y)=2(xy-1)/((x-1)(y-1)).
```

Hence the equation `c(x)+c(y)=t` is equivalent to

```text
P_t(x,y)=(2-t)xy+t x+t y-(2+t)=0.             (1)
```

This family is much simpler than the off/off elliptic pencil: every fiber is a
bidegree `(1,1)` curve.

For a bilinear polynomial `a xy+b x+c y+d`, reducibility over the algebraic
closure is equivalent to `ad-bc=0`.  For (1),

```text
(2-t)(-(2+t))-t^2=-4.
```

Thus for every `t` and every odd characteristic, `P_t` is absolutely
irreducible.

## External input: Vyugin--Makarychev

Theorem 2 of I. Vyugin and S. Makarychev,
*Solutions of polynomial equation over F_p and new bounds of additive energy*,
arXiv:1504.01354v2 (2015), states the following in the specialization needed
here.

If `P(x,y)` is absolutely irreducible of bidegree `(m,n)`,
`P(0,0)!=0`, `deg P(x,0)>=1`, `G<=F_p^*`,

```text
100(mn)^(3/2) < |G| < p^(3/4)/3,
```

then for any two multiplicative cosets `g_1 G`, `g_2 G`,

```text
#{(x,y) in g_1 G x g_2 G : P(x,y)=0}
 <= 16 m n^2 (m+n) |G|^(2/3).
```

The source is recorded exactly in `literature/bibliography.md`; its hypotheses
are not being replaced by an unnamed "Stepanov-style" assertion.

For `P_t`, `m=n=1`.  The source hypotheses `P_t(0,0)!=0` and
`deg P_t(x,0)>=1` fail only at

```text
t=-2  and  t=0,
```

respectively.  Therefore, if

```text
100 < K < p^(3/4)/3,                            (2)
```

then for every `t notin {0,-2}`,

```text
r(t) <= #{(x,y) in H^2 : P_t(x,y)=0}
     <= 32 K^(2/3).                              (3)
```

The enlargement from `A^2` to `H^2` is harmless and only makes the count
larger.

## Exceptional fibers

At `t=0`, central symmetry gives exactly

```text
r(0)=|A|=K-1.
```

At `t=-2` we only need the trivial bound

```text
r(-2)<=|A|=K-1,
```

because for each first coordinate the sum determines the second coordinate
uniquely.  No unproved subgroup-intersection estimate is used here.

## Theorem: uniform direct Cayley-energy bound

Assume (2).  Then

```text
E_+(A)
 = r(0)^2+r(-2)^2+sum_{t notin {0,-2}} r(t)^2
 <= 2(K-1)^2
    + (max_{t notin {0,-2}} r(t))
      sum_{t notin {0,-2}} r(t).
```

Since `sum_t r(t)=|A|^2=(K-1)^2`, (3) gives

```text
E_+(A) <= 2(K-1)^2 + 32 K^(2/3)(K-1)^2
        < 34 K^(8/3).                            (4)
```

Consequently the mixed collision distribution from
`cayley_additive_energy.md` satisfies

```text
sum_t C_H(t)^2 = E_+(A)-|A|^2 < 34 K^(8/3).     (5)
```

This holds for **every** prime `p` and subgroup `H` satisfying (2), including
all cyclotomic/Fibonacci exceptional reductions.  No resultant cutoff enters
the proof.

## Propagation to the fourth-moment mixed term

For nonzero `t`, the mixed contribution to the corrected pair-key distribution
is

```text
M(t)=2(p-2) C_H(t).
```

Let the variance over `F_p^*` use the repository convention
`Var_{t!=0}` with normalization `1/(p-1)`.  Dropping the nonnegative square of
the mean,

```text
Var_{t!=0} M(t)
 <= 4(p-2)^2/(p-1) * sum_{t!=0} C_H(t)^2
 < 136 p K^(8/3)                               (6)
```

for odd `p`.  Thus the direct theorem gives a genuine polynomial-scale mixed
variance bound `O(p K^(8/3))`.

The intended sharp scale from forced central symmetry is `O(p K^2)`.  The
current direct theorem therefore leaves an explicit exponent gap of `K^(2/3)`.
It is useful because it replaces an exponential exceptional-prime condition by
a uniform polynomial-range theorem, but it does **not** yet attain the mixed
scale required by the strongest draft moment target.

## Finite regression and non-claims

`computations/cpp/cayley_direct_energy_verifier.cpp` independently checks the
fiber identity, Cayley-set energy and maximum generic fiber multiplicity for
several prime-order subgroups with `K>100` in the range (2).  These finite
checks are regression evidence only; the universal theorem comes from the
algebra above plus the cited Stepanov theorem.

This result does not close the off/off elliptic correlation theorem and does
not imply microscopic BGS statistics.  The next quantitative target is to
replace `K^(8/3)` in (4) by `K^(2+o(1))` (or another bound that propagates to
`p K^(2+o(1))`) using the special one-parameter Möbius family rather than a
worst-fiber estimate.