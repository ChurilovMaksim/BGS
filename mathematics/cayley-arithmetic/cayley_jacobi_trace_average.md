# Cayley energy as a twisted-Jacobi trace and a double-averaged quadratic theorem

**Status: EXACT, conditional only on the classical Bombieri--Vinogradov theorem and the prime number theorem in the explicitly cited standard forms.  FINITE-REGRESSION for the maintained trace identity checks.**

This note connects the centered Cayley-energy problem to the **ordinary trace of the full annihilator twisted-Jacobi matrix** and then combines the global resultant collision-mass budget with Bombieri--Vinogradov to obtain a genuine almost-everywhere quadratic theorem in a two-parameter average.

The result is an averaged fourth-moment statement.  It is **not** a central-limit theorem, is not a statement about a parity/desymmetrized spectral block, and does not prove microscopic BGS/GOE statistics.

**September 9 continuation:** [`cayley_trace_gaussian_limit.md`](cayley_trace_gaussian_limit.md)
supplies a separate all-order proof of a full-trace Gaussian limit, pointwise
for `K=o(log p)` and in dyadic density for subpolynomial `K`.
Its smaller size regimes and its new higher-moment argument are essential;
the fourth-moment theorem in this note alone does not imply it.

## 1. Twisted-Jacobi normalization

Let `p` be an odd prime, let `H<=F_p^*` have order `K`, and let

```text
S=H^perp,
m=|S|=(p-1)/K.
```

For `chi,psi in S`, define the full annihilator twisted-Jacobi matrix

```text
J_S(q)_(chi,psi)
 = sum_{x in F_p\{0,1}}
     chi^(-1)(x) psi(x-1) e_p(qx).                       (1)
```

This is the same convention implemented in `computations/python/bgs/jacobi.py`.  Define the normalized matrix

```text
M_S(q)=e_p(-q/2) J_S(q)/(p-1),                           (2)
```

where `q/2` means multiplication by the inverse of `2` in `F_p`.  This is the full `S`-matrix; no parity-sector restriction is imposed in this note.

Let

```text
A=c(H\{1}),
c(h)=(h+1)/(h-1),
```

and use the unnormalized additive Fourier transform

```text
1_Ahat(r)=sum_{a in A} e_p(ra).                          (3)
```

## 2. Exact Cayley--Jacobi trace identity

### Theorem 1 (trace identity)
For every `r in F_p`,

```text
1_Ahat(r)=K Tr M_S(2r).                                  (4)
```

In particular `Tr M_S(q)` is real for every `q`, because `A=-A`.

### Proof
Put `y=(h-1)^(-1)`. Then

```text
h=(y+1)/y,
c(h)=1+2y,
```

and character orthogonality gives

```text
1_Ahat(r)
 = e_p(r)/m * sum_{chi in S} T_chi(r),                  (5)
```

where

```text
T_chi(r)=sum_{y!=0,-1} chi((y+1)/y)e_p(2ry).             (6)
```

Set `x=y+1`.  Then

```text
T_chi(r)
 = e_p(-2r)
   sum_{x in F_p\{0,1}}
     chi(x) conjugate(chi(x-1)) e_p(2rx)
 = e_p(-2r) J_S(2r)_(conjugate(chi),conjugate(chi)).     (7)
```

Because `S` is closed under inversion/conjugation,

```text
sum_{chi in S}T_chi(r)=e_p(-2r)Tr J_S(2r).              (8)
```

Substitution into (5), followed by `(p-1)/m=K`, gives

```text
1_Ahat(r)
 = e_p(-r)Tr J_S(2r)/m
 = K Tr M_S(2r),                                        (9)
```

which proves (4).  Finally `A=-A`, so `1_Ahat(r)` is a real cosine sum.

This is an ordinary diagonal trace identity.  It does not use any cyclic rewrite of noncommutative matrix words and is unrelated to the retracted historical noncommutative trace shortcut recorded in `record/retractions.md`.

## 3. Exact trace moments

Since multiplication by `2` permutes `F_p`, Parseval and the additive-energy identity give

```text
sum_q |Tr M_S(q)|^2 = p(K-1)/K^2,                       (10)

sum_q |Tr M_S(q)|^4 = p E_+(A)/K^4.                    (11)
```

At `q=0`, (4) gives

```text
Tr M_S(0)=(K-1)/K.                                      (12)
```

Therefore, with averages over `q!=0`,

```text
mu_2(K,p)
 :=1/(p-1) sum_{q!=0}|Tr M_S(q)|^2
 =(K-1)(p-K+1)/(K^2(p-1)),                              (13)
```

and

```text
mu_4(K,p)
 :=1/(p-1) sum_{q!=0}|Tr M_S(q)|^4
 =[p E_+(A)-(K-1)^4]/[K^4(p-1)].                        (14)
```

Now assume `K` is an odd prime and `p==1 (mod K)`.  Let `Delta_K(p)` be the non-forced **nonzero-difference** excess from `cayley_resultant_mass_budget.md`.  The zero-difference class contributes `(K-1)^2`, while the forced nonzero baseline is `(K-1)(2K-5)`. Hence exactly

```text
E_+(A)=3(K-1)(K-2)+Delta_K(p).                          (15)
```

Consequently all departure of the fourth trace moment from the forced centrally symmetric model is carried by `Delta_K(p)`:

```text
mu_4(K,p)-mu_4^forced(K,p)
 = p Delta_K(p)/[K^4(p-1)].                             (16)
```

## 4. Dyadic split-design family

Fix a real number

```text
0<theta<1/3.                                             (17)
```

For `X>1`, put

```text
Q=X^theta                                                (18)
```

and define the dyadic design family

```text
D_theta(X)
 = {(K,p):
      K and p prime,
      Q/2<K<=Q,
      X/2<p<=X,
      p==1 (mod K)}.                                    (19)
```

For every pair in this family,

```text
K asymp X^theta,
p asymp X.                                               (20)
```

In particular when `theta<1/4` this lies uniformly in the pointwise BGS-moment subregime `K=o(p^(1/4))`; the averaged theorem below actually holds throughout the larger range `theta<1/3`.

## 5. Counting the dyadic designs

We use the standard Bombieri--Vinogradov theorem in the form of Iwaniec--Kowalski, *Analytic Number Theory*, Theorem 17.1: for every fixed `A>0`, uniformly for moduli up to `x^(1/2)` with a sufficiently large logarithmic saving,

```text
sum_{q<=R} max_{(a,q)=1}
  |pi(x;q,a)-pi(x)/phi(q)|
 <<_A x/(log x)^(A+1).                                  (21)
```

For fixed `theta<1/2`, `Q=X^theta` is eventually inside that modulus range both at `X` and at `X/2`.  Restricting the sum in (21) to prime moduli `K in (Q/2,Q]` and residue class `1`, then subtracting the endpoints, gives

```text
|D_theta(X)|
 = [pi(X)-pi(X/2)]
   sum_{Q/2<K<=Q, K prime} 1/(K-1)
   + O_A(X/(log X)^(A+1)).                              (22)
```

The prime number theorem and partial summation give

```text
pi(X)-pi(X/2) ~ X/(2 log X),                            (23)

sum_{Q/2<K<=Q, K prime}1/(K-1)
 ~ log(2)/log Q.                                        (24)
```

Thus

```text
|D_theta(X)|
 ~ [log(2)/(2 theta)] X/(log X)^2.                      (25)
```

In particular the denominator in the average below has the expected order `X/(log X)^2`; no individual prime-number theorem for a varying modulus `K` is being assumed.

## 6. Double-averaged quadratic excess theorem

### Theorem 2 (almost-all quadratic mixed energy in a two-parameter average)
For every fixed `0<theta<1/3`,

```text
1/|D_theta(X)|
 sum_{(K,p) in D_theta(X)} Delta_K(p)/K^2
 <<_theta X^(3theta-1).                                 (26)
```

Hence

```text
1/|D_theta(X)|
 sum_{(K,p) in D_theta(X)} Delta_K(p)/K^2 -> 0.          (27)
```

Equivalently, for every fixed `eta>0`,

```text
#{(K,p) in D_theta(X): Delta_K(p)>=eta K^2}
 / |D_theta(X)|
 <<_theta X^(3theta-1)/eta -> 0.                        (28)
```

Thus asymptotically almost every dyadic split design has

```text
sum_t C_H(t)^2
 =(K-1)(2K-5)+o(K^2)                                    (29)
```

in pair-density.

### Proof
For one prime `K`, the exact resultant-mass theorem gives

```text
sum_{p==1 mod K} Delta_K(p) log p <= N_K C_K,           (30)
```

where

```text
N_K=K^3-5K^2+6K+1 < K^3,
C_K=(K-1)log12-3logK < K log12.                         (31)
```

Every `p in (X/2,X]` has `log p>=log(X/2)`. Therefore

```text
sum_{X/2<p<=X, p==1 mod K} Delta_K(p)/K^2
 <= log(12) K^2/log(X/2).                               (32)
```

Summing over prime `K in (Q/2,Q]` and using the prime number theorem (or the standard Chebyshev upper bound plus partial summation) gives

```text
sum_{(K,p) in D_theta(X)} Delta_K(p)/K^2
 << Q^3/(log Q log X).                                  (33)
```

By (25), division by `|D_theta(X)|` yields

```text
<< Q^3/X = X^(3theta-1),                                (34)
```

proving (26).  Equation (28) is Markov's inequality, using `Delta_K(p)>=0`.

The threshold `theta=1/3` here comes from the exact `O(K^4)` global collision-mass budget divided by the natural `K^2` energy scale and then summed over `K`.  It is not a claim that the pointwise centered-energy theorem holds to this range.

## 7. Double-averaged Gaussian fourth-moment ratio for the full trace

Define the nonzero-frequency trace kurtosis

```text
kappa(K,p)=mu_4(K,p)/mu_2(K,p)^2.                       (35)
```

Because the trace is real, the Gaussian fourth-moment benchmark is `3`.

From (13)--(15), uniformly for `(K,p) in D_theta(X)`,

```text
|kappa(K,p)-3|
 << Delta_K(p)/K^2 + 1/K + K^2/p.                       (36)
```

Averaging (36), using Theorem 2 and `K asymp Q`, `p asymp X`, gives

```text
1/|D_theta(X)|
 sum_{(K,p) in D_theta(X)} |kappa(K,p)-3|
 <<_theta
   X^(3theta-1)+X^(-theta)+X^(2theta-1) -> 0.            (37)
```

Therefore the **second/fourth moment ratio of the full normalized Jacobi trace is asymptotically real-Gaussian for almost all dyadic split designs in this double average**.

This is deliberately weaker than a Gaussian distribution theorem.  Equality of a fourth-moment ratio with `3` does not imply a CLT, and an ordinary full trace is not a local eigenvalue statistic.  The theorem therefore does not close the microscopic BGS problem.

## 8. Evidence boundary and relation to historical retractions

- The trace identity (4) is a direct diagonal calculation from the currently maintained twisted-Jacobi definition.
- The energy-to-fourth-trace identity (11) is finite Fourier Parseval.
- The averaged theorem uses the already proved resultant collision-mass budget plus the classical Bombieri--Vinogradov theorem and the prime number theorem.
- The finite regression `computations/verification/cayley_jacobi_trace_regression.py` compares the maintained Jacobi implementation with an independent direct Cayley Fourier calculation on finite designs.  It is not used to prove Theorems 1 or 2.
- No cyclic reordering of a noncommutative matrix word is used anywhere.  The historical R86/R87 trace shortcut remains retracted.

## 9. What remains open

The pointwise target

```text
E_+(A)=(K-1)^4/p+O(K^(2+o(1)))                          (38)
```

is still open.  Theorem 2 proves that its natural quadratic **excess scale** is attained for almost every split pair in a double average for `theta<1/3`, but does not supply a uniform bound for a prescribed `(K,p)`.

For the BGS programme, the most relevant subrange is `theta<1/4`, where the double-average theorem lies strictly inside `K=o(p^(1/4))`.  The off/off elliptic correlation and the microscopic local-statistics bridge remain separate open obligations.
