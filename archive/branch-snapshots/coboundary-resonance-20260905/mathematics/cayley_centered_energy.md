# Centered additive energy of the Cayley image

**Status: EXACT for the identities and reductions below; OPEN for the near-quadratic centered-energy bound.**

This note isolates the correct quantitative target left after
[`cayley_direct_energy.md`](cayley_direct_energy.md).  The raw energy cannot be
uniformly `O(K^2)` in every density regime because every subset of `F_p` has a
forced Fourier zero-mode contribution.  What the fourth-moment argument really
needs is control of the **centered** energy.

Let `p` be an odd prime, let `H <= F_p^*` have order `K`, and put

```text
c(h)=(h+1)/(h-1),
A=c(H\{1}),
n=|A|=K-1.
```

Throughout, use the unnormalized additive Fourier transform

```text
fhat(q)=sum_x f(x) e_p(qx).
```

## 1. Exact centered-energy identity

For every `A subset F_p`, Parseval applied to `1_A * 1_A` gives

```text
E_+(A)=1/p * sum_q |1_Ahat(q)|^4
      = |A|^4/p + 1/p * sum_{q!=0} |1_Ahat(q)|^4.        (1)
```

Thus the density term `|A|^4/p` is unavoidable.  The sharp target for the
Cayley image is therefore not a global statement `E_+(A)=O(K^2)`, but rather

```text
E_+(A)=(K-1)^4/p + O(K^(2+o(1))),                       (2)
```

or equivalently

```text
sum_{q!=0} |1_Ahat(q)|^4 << p K^(2+o(1)).               (3)
```

In the intended cat-map regime `K=o(p^(1/4))`, the zero-mode term
`K^4/p=o(1)` relative to the natural quadratic collision scale, so (2)--(3)
would give essentially the desired mixed-term size.

This is an **OPEN target**, not a theorem of the repository.

## 2. Exact Fourier/character decomposition

Let

```text
S=H^perp,
m=|S|=(p-1)/K.
```

For `h!=1`, put `y=(h-1)^(-1)`.  Then

```text
h=(y+1)/y,
c(h)=1+2y,
```

and `h in H\{1}` corresponds exactly to `y in F_p\{0,-1}` satisfying
`(y+1)/y in H`.  Character orthogonality on `F_p^*` therefore gives

```text
1_Ahat(q)
 = e_p(q)/m * sum_{chi in S} T_chi(q),                  (4)

T_chi(q)
 = sum_{y in F_p\{0,-1}}
     chi((y+1)/y) e_p(2 q y)
 = sum_{y in F_p\{0,-1}}
     chi(y+1) conjugate(chi(y)) e_p(2 q y).              (5)
```

Here multiplicative characters are evaluated only on nonzero arguments, so no
extension-at-zero convention is hidden in (5).

The inner sums are concrete Kummer/Artin--Schreier trace-function Fourier
transforms.  Formula (4) shows exactly what a trace-function approach would
have to exploit: cancellation **jointly across the annihilator family `S`**,
not merely a pointwise Weil bound for each `T_chi`.

## 3. Exact Gram matrix of the character family

For `chi,eta in S`, additive orthogonality gives

```text
sum_q T_chi(q) conjugate(T_eta(q))
 = p * sum_{y in F_p\{0,-1}}
       (chi conjugate(eta))((y+1)/y).                    (6)
```

The map

```text
y -> (y+1)/y
```

is a bijection from `F_p\{0,-1}` onto `F_p^*\{1}`.  Hence

```text
sum_q T_chi(q) conjugate(T_eta(q))
 = p(p-2),   chi=eta,
 = -p,       chi!=eta.                                  (7)
```

Substituting (7) into (4) recovers the exact second moment

```text
sum_q |1_Ahat(q)|^2 = p(K-1),                            (8)
```

and therefore

```text
sum_{q!=0} |1_Ahat(q)|^2
 = (K-1)(p-K+1).                                         (9)
```

The Gram identity is much stronger than treating the `T_chi` independently,
but by itself it controls only an `L^2` norm.  The open target (3) is an `L^4`
problem.

## 4. Difference fibers are a one-parameter unipotent PGL2 family

Because `A=-A`, its sum and difference energies coincide.  Solving

```text
c(h)-c(k)=t
```

for `k` gives

```text
k = u_t(h)
  = ((2-t)h+t)/(2+t-t h).                                (10)
```

The matrices

```text
U_t = [[2-t, t],[-t,2+t]]
```

have determinant `4` and trace `4`; after division by `2` they are unipotent
in `SL_2(F_p)`.  Moreover `u_t=c o (z -> z-t) o c`, so `{u_t}` is exactly a
one-parameter unipotent subgroup conjugate to additive translations.
Consequently

```text
r_{A-A}(t)
 = #{h in H\{1}: u_t(h) in H\{1}}.                      (11)
```

Thus the centered-energy problem can equivalently be viewed as an `L^2`
intersection problem between the multiplicative torus `H` and a conjugated
unipotent one-parameter family.  Generic PGL2 incidence theorems do not
currently recover the near-quadratic target from (11); the special subgroup
and one-parameter structure is the feature a sharper argument must use.

## 5. Shifted-product factorization and why shifted energy alone is insufficient

For the sum fiber from `cayley_direct_energy.md`,

```text
P_t(x,y)=(2-t)xy+t(x+y)-(2+t).
```

If `t!=2` and

```text
lambda=t/(2-t),
```

then the exact factorization

```text
((2-t)x+t)((2-t)y+t)=(2-t)P_t(x,y)+4
```

shows that `P_t(x,y)=0` is equivalent to

```text
(x+lambda)(y+lambda)=(1+lambda)^2.                       (12)
```

For `x,y in H`, the enlarged subgroup fiber contains exactly one pair involving
the Cayley singularity, namely `(x,y)=(1,1)`.  Therefore its multiplicity is

```text
R_lambda=r_{A+A}(t)+1.                                   (13)
```

This connects each Cayley sum fiber to one distinguished product class of the
shifted subgroup `H+lambda`.

There is also an exact global identity.  Let `E_x(H+lambda)` denote
multiplicative energy and put

```text
D=2K^2-K,
```

the number of identity/swap quadruples.  Expanding

```text
(a+lambda)(b+lambda)=(c+lambda)(d+lambda)
```

gives

```text
ab-cd + lambda(a+b-c-d)=0.
```

If `a+b!=c+d`, there is exactly one `lambda`; if the sums agree, equality of
products is equivalent to equality of the unordered pairs.  Summing over all
`lambda in F_p` yields

```text
sum_lambda E_x(H+lambda)
 = K^4 - E_+(H) + p(2K^2-K),                              (14)
```

or

```text
sum_lambda (E_x(H+lambda)-D)=K^4-E_+(H).                 (15)
```

Known near-quadratic pointwise estimates for `E_x(H+lambda)` are therefore
relevant context, but (12)--(15) also expose the obstruction to a direct
shortcut: Cayley energy sums the squares of **one moving distinguished product
class** across essentially all shifts.  A bound for total multiplicative
energy at each fixed shift, or the global identity (15), does not by itself
supply the required `O(K^(2+o(1)))` sum over those distinguished classes.

## 6. Current closure condition

The direct Stepanov theorem already proves

```text
E_+(A) < 34 K^(8/3)
```

for `100<K<p^(3/4)/3`.  To reach the strongest intended mixed scale, the first
unresolved implication is now precisely one of the equivalent statements
(2)--(3).

A viable improvement must use information beyond a worst-fiber
`r(t)<<K^(2/3)` estimate.  The two most structured formulations currently
available are:

1. the fourth moment of the explicitly orthogonal character family
   `T_chi(q)` in (4)--(7);
2. the torus-versus-unipotent intersection family (10)--(11), equivalently the
   distinguished shifted-product classes (12)--(13).

No existing theorem has been verified in the current audit that turns either
formulation into (2)--(3) without an additional exponent loss.  This is the
active mixed-term research gap.
