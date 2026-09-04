# Full proof of the Fibonacci/Lucas ratio energy theorem

**Status: EXACT, conditional only on the cited classical primitive-divisor theorem; FINITE-CERTIFICATE for the bounded residue.**

This file supplies the load-bearing details behind Theorem 3 of
[`cayley_resultant_structure.md`](cayley_resultant_structure.md).  It is kept
separate so that the proof can be audited without the surrounding BGS
narrative.

Let

```text
F_0=0, F_1=1, F_{n+1}=F_n+F_{n-1},
L_0=2, L_1=1, L_{n+1}=L_n+L_{n-1},
x_n=L_n/F_n                    (n>=1),
S_N={+-x_1,...,+-x_N}.
```

For `d != 0` put

```text
r_N(d)=#{(u,v) in S_N^2 : u!=v and u-v=d},
E*(S_N)=sum_{d!=0} r_N(d)^2.
```

## The theorem

For every integer `N>=3`,

```text
E*(S_N)=2N(4N-3)+32=8N^2-6N+32.
```

Equivalently, relative to the universal centrally-symmetric forced baseline,
the excess is exactly `32` for every `N>=3`.

## 1. Exact Fibonacci/Lucas identities

For `m,n>=1`, standard addition identities give

```text
L_m F_n + L_n F_m = 2 F_(m+n),
L_m F_n - L_n F_m = 2 (-1)^m F_(n-m),
```

where the second identity is interpreted with the usual signed extension
`F_(-j)=(-1)^(j+1) F_j`.  Consequently

```text
x_m+x_n = 2 F_(m+n)/(F_m F_n),
|x_m-x_n| = 2 F_|m-n|/(F_m F_n).
```

We also use

```text
L_n=F_n+2F_(n-1).
```

Hence

```text
1 <= x_n <= 3,
```

with equality `x_n=1` only for `n=1` and equality `x_n=3` only for `n=2`.
Indeed `0<=F_(n-1)<=F_n`; the first equality requires `F_(n-1)=0`, and the
second requires `F_(n-1)=F_n`, which occurs only at `n=2`.

The difference formula also shows that the positive numbers `x_n` are all
distinct.

## 2. The only external theorem

We use the following classical fact.

> For every `j>12`, the Fibonacci number `F_j` has a prime divisor that divides
> no earlier positive Fibonacci number.

Yabuta, *A Simple Proof of Carmichael's Theorem on Primitive Divisors*,
Fibonacci Quarterly 39 (2001), Theorem 3, proves the stronger exact statement
that the `n`-th Fibonacci term has a primitive divisor for
`n notin {1,2,6,12}`.  This is the publication-grade source used here.

Nothing below needs a quantitative bound on that primitive prime.

## 3. Equal absolute differences

Take `a>b>=1` and `c>d>=1`.  Suppose

```text
F_(a-b)/(F_a F_b) = F_(c-d)/(F_c F_d).          (D)
```

Assume first that `a>c` and `a>12`.  Let `ell` be a primitive prime divisor of
`F_a`.  Cross-multiplying (D) gives

```text
F_(a-b) F_c F_d = F_(c-d) F_a F_b.
```

Thus `ell` divides the left-hand side.  But each Fibonacci index on that side
is strictly smaller than `a`:

```text
a-b<a,  c<a,  d<c<a.
```

This contradicts primitivity.  Interchanging the two pairs rules out `c>a`
when `c>12`.  Therefore, whenever `max(a,c)>12`, one must have `a=c`.

With `a=c`, equation (D) reduces to

```text
F_(a-b)/F_b = F_(a-d)/F_d.                      (D_a)
```

For fixed `a>3`, the sequence

```text
R_b=F_(a-b)/F_b,   1<=b<a,
```

is strictly decreasing.  Indeed, from `b` to `b+1` the numerator weakly
decreases and the denominator weakly increases.  Equality in both changes
could occur only simultaneously at

```text
F_(a-b)=F_(a-b-1)  and  F_(b+1)=F_b,
```

which forces `a-b=2` and `b=1`, hence `a=3`.  For `a>3` at least one change is
strict.  Thus (D_a) gives `b=d`.

So every nontrivial equality of absolute differences is confined to upper
indices at most `12`.

## 4. Equal sums

Suppose

```text
F_(m+n)/(F_m F_n) = F_(r+s)/(F_r F_s).          (S)
```

Let `A=m+n` and `B=r+s`.  If `A>B` and `A>12`, choose a primitive divisor
`ell` of `F_A`.  Cross-multiplication gives

```text
F_A F_r F_s = F_B F_m F_n.
```

The right-hand Fibonacci indices `B,m,n` are all strictly smaller than `A`,
contradicting primitivity.  The symmetric argument excludes `B>A` when
`B>12`.  Thus outside the bounded residue one has `A=B`.

It remains to show that a fixed sum determines the unordered pair.  Put
`A=m+n` and assume `m<=n`.  The exact identity

```text
5 F_m F_n = L_A - (-1)^m L_(n-m)
           = L_A - (-1)^m L_(A-2m)              (P)
```

follows from the standard Fibonacci/Lucas product formulas.  Suppose also
`r<=s`, `r+s=A`, and `F_m F_n=F_r F_s`.  Equation (P) implies

```text
(-1)^m L_(A-2m) = (-1)^r L_(A-2r).
```

All Lucas numbers in this display are positive, so `m` and `r` have the same
parity.  Hence

```text
L_(A-2m)=L_(A-2r).
```

The Lucas sequence is injective on nonnegative indices: `L_0=2`, `L_1=1`,
`L_2=3`, and it is strictly increasing from index `1` onward.  Therefore
`A-2m=A-2r`, so `m=r` and `n=s`.

Consequently every nontrivial equality of positive sums is confined to the
case in which both index sums are at most `12`.

## 5. A sum cannot equal a difference except at 2

Because `1<=x_n<=3`,

```text
x_m+x_n >= 2,
|x_r-x_s| <= 2.
```

Equality between a positive sum and an absolute difference therefore forces
both sides to equal `2`.

The sum is `2` only when `m=n=1`, since `x_n=1` only for `n=1`.  An absolute
difference is `2` only between the unique endpoint values `1` and `3`, hence
only for the indices `{1,2}`.  Thus the unique cross-type relation, up to
orientation, is

```text
x_1+x_1 = x_2-x_1 = 2.
```

## 6. Exact bounded residue

Sections 3--5 reduce every remaining non-forced relation to signed pairs whose
indices lie in `1..12`.  The maintained exact check performs rational equality
by integer cross multiplication, not floating point.

The finite residue contains exactly the relations generated by

```text
x_1=1, x_2=3, x_3=2,

|x_3-x_1|=|x_2-x_3|=1,
x_1+x_1=x_2-x_1=2,
x_1+x_2=x_3+x_3=4,
```

and sign/order symmetry.

Two independent maintained certificates cover this residue:

- `computations/verification/cayley_resultant_fibonacci.py` recomputes exact
  rational difference energies and multiplicity histograms;
- `formalization/Bgs/FibonacciRatioSmall.lean` kernel-checks the `N=12`
  residue with `native_decide`, including total energy and localization of all
  multiplicity-`>2` bins to indices `1,2,3`.

These finite checks are not substitutes for the unbounded proof above; they
close only the bounded residue left by the primitive-divisor argument.

## 7. Energy bookkeeping

Let `M=|S_N|=2N`.  For any centrally symmetric set in characteristic zero with
no zero, the involution

```text
(u,v) -> (-v,-u)
```

preserves the difference `u-v`.  It fixes exactly the `M` antipodal ordered
pairs `(u,-u)`.  If no additional equal-difference relations existed, the
remaining `M(M-2)` ordered pairs would form two-element orbits.  The forced
energy would therefore be

```text
M*1^2 + (M(M-2)/2)*2^2
= M(2M-3)
= 2N(4N-3).
```

The bounded classification shows exactly six bins where forced orbits merge:

- `d=+1` and `d=-1` have multiplicity `4`; each merges two forced
  multiplicity-`2` orbits, so each contributes excess
  `4^2-2^2-2^2=8`;
- `d=+2,-2,+4,-4` have multiplicity `3`; each merges one fixed
  multiplicity-`1` orbit and one multiplicity-`2` orbit, so each contributes
  excess `3^2-1^2-2^2=4`.

No other bin has a non-forced merger.  Hence the total excess is

```text
2*8 + 4*4 = 32,
```

which proves

```text
E*(S_N)=2N(4N-3)+32
```

for every `N>=3`.

## Audit boundary

The unbounded argument depends on the exact primitive-divisor theorem quoted
above.  The Lean module formalizes only the finite residue and does not
formalize Yabuta/Carmichael.  No finite computation is being used as evidence
for the universal quantifier outside that explicitly bounded residue.
