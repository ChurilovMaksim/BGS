# Cayley collision resultants: square structure and the Fibonacci slice

**Status: EXACT for the algebraic theorems below; FINITE-CERTIFICATE for the explicit `(K,p)=(131,F_131)` witness.**

This note strengthens the prime-order mixed-term analysis in
[`cayley_additive_energy.md`](cayley_additive_energy.md).  It also records a
mechanism-level obstruction: a uniform polynomial upper bound for the entire
cyclotomic collision norm is impossible, because one explicit collision family
has Fibonacci-sized norm.

Throughout, `K` is an odd prime, `zeta` is a primitive `K`-th root of unity,
and

```text
c(z)=(z+1)/(z-1).
```

For nonzero residues `i,j,r,s mod K`, with `i!=j` and `r!=s`, choose integer
lifts in `{1,...,K-1}` and define

```text
P(X)
 = X^(r+s+i) - X^(r+s+j) - X^(r+i+j) + 2 X^(r+j) - X^r
   + X^(s+i+j) - 2 X^(s+i) + X^s + X^i - X^j.
```

The exact cleared collision identity is

```text
2 P(X)
 = (c(X^r)-c(X^s)-c(X^i)+c(X^j))
   (X^r-1)(X^s-1)(X^i-1)(X^j-1).
```

The coefficient `L1` norm of `P` is at most `12`.

## 1. A universal square-factor theorem for the resultants

### Lemma 1: a forced cubic zero at `X=1`

`(X-1)^3` divides `P(X)` in `Z[X]`.

Indeed, after expanding the cleared Cayley identity term-by-term, each Cayley
fraction cancels one of the four factors `X^a-1`; every remaining summand
contains the other three factors, each divisible by `X-1`.

Write

```text
P(X)=(X-1)^3 Q(X),   Q in Z[X].
```

### Lemma 2: reciprocity

If `T=i+j+r+s`, then

```text
P(X^-1) = -X^(-T) P(X),
Q(X^-1) =  X^(3-T) Q(X).
```

This is immediate from

```text
c(X^-a)=-c(X^a)
```

and

```text
X^-a-1 = -(X^a-1)/X^a.
```

The four denominator factors contribute no sign, whereas the Cayley-difference
factor contributes one minus sign.

### Theorem 1: `K^3` times a perfect square

For every odd prime `K` and every admissible quadruple,

```text
Res(Phi_K,P) = K^3 M^2
```

for some integer `M` (possibly `M=0` for a forced characteristic-zero
collision).

**Proof.**  Put `L=Q(zeta_K)` and let `L+` be its maximal real subfield.  Since
`K` is odd, choose an integer `m` modulo `K` satisfying

```text
2m = 3-T (mod K).
```

Set

```text
beta = zeta^m Q(zeta).
```

Using Lemma 2,

```text
conj(beta)
 = zeta^(-m) Q(zeta^-1)
 = zeta^(-m+3-T) Q(zeta)
 = beta.
```

Thus `beta` is an algebraic integer in `L+`.  Multiplication by the root of
unity `zeta^m` does not change the absolute norm, so

```text
N_{L/Q}(Q(zeta))
 = N_{L/Q}(beta)
 = N_{L+/Q}(beta)^2
 = M^2
```

with `M in Z`.  Finally

```text
N_{L/Q}(zeta-1)=Phi_K(1)=K,
```

and therefore

```text
Res(Phi_K,P)
 = N_{L/Q}(P(zeta))
 = K^3 M^2.
```

This explains the previously empirical factor shapes `K^3 q^2`, `K^5 q^2`,
etc.; outside the distinguished factor `K`, every prime valuation of a nonzero
collision resultant is even.

## 2. Improved uniform exceptional-prime cutoff

The Chowla cotangent-independence argument in
[`cayley_additive_energy.md`](cayley_additive_energy.md) proves that a
non-forced characteristic-zero collision has `P(zeta)!=0`, hence `M!=0`.

Suppose a rational prime `p` satisfies `K | (p-1)` and supports a non-forced
finite-field collision.  Then `p` divides `Res(Phi_K,P)`.  Since `p!=K`,
Theorem 1 forces `p | M`, and therefore

```text
K^3 p^2 <= |Res(Phi_K,P)|.
```

On the other hand every conjugate satisfies `|P(zeta^a)|<=12`, so

```text
|Res(Phi_K,P)| <= 12^(K-1).
```

Hence every non-forced collision prime obeys the stronger bound

```text
p <= 12^((K-1)/2) / K^(3/2).
```

Equivalently, if

```text
p > 12^((K-1)/2) / K^(3/2),
```

then the mixed Cayley collision energy is exactly the forced baseline

```text
(K-1)(2K-5).
```

This improves the earlier exponent by a factor two.  It is still logarithmic
in the useful `K`-range and therefore does not close the intended
`K=o(p^(1/4))` moment regime.

## 3. Fibonacci collision slice

There is an explicit non-forced family showing that the square factor `M`
cannot be polynomially bounded in `K`.

Take the ordered pairs of exponents

```text
(i,j)=(1,-1),
(r,s)=(2,1)
```

modulo `K`.  The collision is

```text
c(h^2)-c(h) = c(h)-c(h^-1).
```

Since `c(h^-1)=-c(h)`, this is equivalent to

```text
c(h^2)=3c(h).
```

For `h!=+-1`, direct simplification gives

```text
c(h^2)-3c(h)
 = -2 (h^2+3h+1) / ((h-1)(h+1)).
```

Thus this non-forced collision is exactly the quadratic condition

```text
q(h)=h^2+3h+1=0.
```

### Theorem 2: Fibonacci resultant identity

For every odd prime `K`,

```text
Res(Phi_K(X), X^2+3X+1) = F_K^2,
```

where `F_K` is the `K`-th Fibonacci number (`F_0=0,F_1=1`).  Consequently the
full cleared collision resultant for this slice is

```text
K^3 F_K^2.
```

**Proof.**  Let `alpha,beta` be the roots of `X^2+3X+1`; then
`alpha*beta=1`, `alpha+beta=-3`, and for prime `K`,

```text
Phi_K(X)=(X^K-1)/(X-1).
```

Therefore

```text
Res(Phi_K,q)
 = Phi_K(alpha) Phi_K(beta)
 = ((alpha^K-1)(beta^K-1))/((alpha-1)(beta-1))
 = (2-(alpha^K+beta^K))/5.
```

Writing `phi=(1+sqrt(5))/2`, the two roots are `-phi^2` and `-phi^-2`.
Because `K` is odd,

```text
alpha^K+beta^K = -L_(2K),
```

where `L_n` is the Lucas sequence.  The standard identity

```text
L_(2K)=5 F_K^2-2        (K odd)
```

gives the result.

Since `F_K ~ phi^K/sqrt(5)`, Theorem 2 proves:

> **No uniform polynomial bound `|M| <= K^C` can hold for all collision
> resultants.**

Therefore a polynomial exceptional-prime theorem, if true, must use arithmetic
information about the *eligible prime divisors* of the resultants (or avoid a
worst-case resultant argument), not merely a polynomial bound on their total
size.

### Exact finite-field characterization of the Fibonacci slice

Let `p` be a prime with `K | (p-1)`.  For this particular collision family,

```text
non-forced collision over F_p
<=> p | F_K.
```

Indeed the collision is equivalent to a common root of `Phi_K` and `q`; because
`K | p-1`, all `K`-th roots of unity already lie in `F_p`.  The resultant
identity then gives the equivalence (and `p!=K`).

Thus one explicit part of the BGS mixed-term exceptional set is controlled by
prime divisors of Fibonacci numbers.  Classical rank-of-apparition theory says
primitive Fibonacci divisors lie in congruence classes `+-1 mod K`; the
`+1 mod K` divisors are exactly the ones eligible for this split finite-field
slice.

## 4. Cayley values become Fibonacci/Lucas ratios

Assume `q(h)=0` and put `t=c(h)`.  Substituting

```text
h=(t+1)/(t-1)
```

into `h^2+3h+1` gives

```text
5t^2=1.
```

For every `n>=1`, the polynomial identity modulo `q(h)` is

```text
F_n c(h^n) = L_n c(h).
```

It follows either from Binet formulas or by induction from the Fibonacci/Lucas
recurrences.  If `p | F_K`, `K` is prime and `1<=n<K`, then
`p` does not divide `F_n` (use `gcd(F_m,F_n)=F_gcd(m,n)`).  Hence for
`N=(K-1)/2`, the finite Cayley set is a scalar multiple of

```text
S_N = { +- L_n/F_n : 1<=n<=N }
```

reduced modulo `p`.

This gives a second, independent description of the Fibonacci exceptional
slice.

## 5. An almost-Sidon theorem for Fibonacci/Lucas ratios

Define over `Q`

```text
x_n=L_n/F_n,
S_N={+-x_1,...,+-x_N}.
```

For `N>=3`, let

```text
E*(S_N)=sum_{d!=0} r_{S_N-S_N}(d)^2.
```

### Theorem 3: exact rational difference energy

For every `N>=3`,

```text
E*(S_N) = 2N(4N-3) + 32
        = 8N^2 - 6N + 32.
```

In particular the centrally symmetric forced baseline is exceeded by the
**constant amount `32`, independent of `N`**.

The only non-forced rational difference relations are generated by

```text
x_1=1,  x_2=3,  x_3=2,

|x_3-x_1|=|x_2-x_3|=1,
x_1+x_1=x_2-x_1=2,
x_1+x_2=x_3+x_3=4,
```

and their sign/ordering symmetries.

**Proof architecture.**  Two standard identities are

```text
x_m+x_n = 2 F_(m+n)/(F_m F_n),
|x_m-x_n| = 2 F_|m-n|/(F_m F_n).
```

For Fibonacci numbers, Carmichael's primitive-divisor theorem implies that
`F_j` has a prime divisor dividing no earlier Fibonacci number for every
`j>12`.

1. If two absolute differences are equal and the larger upper index exceeds
   `12`, cross-multiplication and a primitive divisor of the largest Fibonacci
   denominator force the two upper indices to agree; elementary monotonicity
   then forces the lower indices to agree.
2. If two sums are equal and the larger index-sum exceeds `12`, a primitive
   divisor of the largest `F_(m+n)` forces the two index-sums to agree.  With
   the sum fixed, the product identity

   ```text
   5 F_m F_n = L_(m+n) - (-1)^n L_(m-n)
   ```

   forces the unordered index pairs to agree.
3. A sum can equal an absolute difference only at the endpoint value `2`,
   because `1<=x_n<=3`; equality gives exactly `x_1+x_1=x_2-x_1`.
4. The remaining bounded cases (indices / index-sums at most `12`) have only
   the two displayed extra same-type relations.  This finite residual check is
   independently encoded in Python and Lean in the maintained tree.

For a centrally symmetric set of `2N` points, forced inversion pairing gives
baseline `2N(4N-3)`.  The two oriented bins `+-1` have multiplicity `4` rather
than two separate multiplicity-`2` bins, contributing excess `8` each.  The
four bins `+-2,+-4` have multiplicity `3` rather than one multiplicity-`1` and
one multiplicity-`2` bin, contributing excess `4` each.  Total excess is
`2*8+4*4=32`.

The external number-theory input is only the classical primitive-divisor
statement; the low-index residual classification is finite exact arithmetic.

## 6. A 28-digit exceptional-prime certificate at K=131

The Fibonacci number

```text
F_131 = 1066340417491710595814572169
```

is prime.  The repository does not rely on a probable-prime label: the
verification producer checks the complete factorization

```text
F_131 - 1
 = 2^3 * 11 * 89 * 131 * 199 * 521 * 2081 * 9901 * 19801 * 24571
```

and a Lucas primality certificate with base `3`:

```text
3^(p-1) = 1 (mod p),
gcd(3^((p-1)/q)-1,p)=1
```

for every prime `q` in the factorization of `p-1`.

Moreover

```text
p = F_131 = 1066340417491710595814572169,
K = 131,
h = 188706367382658195937453923
```

satisfy

```text
h^2+3h+1 = 0 (mod p),
h^131 = 1 (mod p),
h != 1.
```

Since `K=131` is prime, `h` has exact order `131`.  The explicit non-forced
collision is

```text
c(h^2)-c(h)=c(h)-c(h^-1).
```

An exact dictionary-based `O(K^2)` computation (which never allocates an array
of length `p`) gives

```text
nonzero Cayley collision energy = 33442,
forced baseline                 = 33410,
excess                          = 32,
maximum nonzero multiplicity    = 4.
```

Thus the older `(461,23)` negative control is not an isolated small-field
phenomenon: an explicit 28-digit prime supports the structurally predicted
Fibonacci excess.

The same witness is checked independently by Python arbitrary-precision
integers and a C++20 `boost::multiprecision::cpp_int` implementation.

## 7. Consequence for the BGS programme

The mixed-term problem is now split more sharply:

1. **Characteristic-zero collision classification:** closed for prime `K` by
   Chowla/cross-polytope rigidity.
2. **Resultant shape:** closed at the general level `K^3 M^2`.
3. **Worst-case norm-size route:** proved incapable of yielding a polynomial
   cutoff, because `M=F_K` on an explicit subfamily.
4. **Eligible bad-prime problem:** still open at the polynomial/average scale;
   it is now visibly connected to arithmetic of prime divisors of Lucas-type
   sequences, not just generic sparse-polynomial height.

This does not prove the off/off elliptic estimate and does not provide the
microscopic BGS bridge.  It does eliminate one plausible but impossible route
to a growing-`K` theorem and replaces it with a more structured arithmetic
problem.
