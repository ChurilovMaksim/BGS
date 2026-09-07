# Dense-regime Cayley centered energy from mixed Weil cancellation

**Status: EXACT + EXTERNAL-WEIL.** The character decomposition, Parseval step, and hybrid comparison are exact. The only external input is the classical mixed Weil/Deligne bound for a rank-one multiplicative-additive character sum with three singular points. This result is new to the project; external priority for this particular Cayley specialization has not been established.

Let `p` be an odd prime, let `H <= F_p^*` have order `K>=2`, let

```text
m=(p-1)/K,
c(h)=(h+1)/(h-1),
A=c(H\{1}),
n=|A|=K-1.
```

Use the unnormalized additive Fourier transform

```text
Ahat(q)=sum_(a in A) exp(2*pi*i*q*a/p).
```

The theorem below complements `cayley_curve_uniform.md`. It does not improve the sparse `K^(8/3)` exponent, but it gives a strictly stronger centered bound once `K` is denser than the crossover `p^(3/5)`.

## 1. Character decomposition

Let `S=H^perp` be the group of multiplicative characters of `F_p^*` that are trivial on `H`; thus `|S|=m`. For `h!=0`,

```text
1_H(h)=m^(-1) sum_(chi in S) chi(h).
```

Therefore, for every `q!=0`,

```text
Ahat(q)=m^(-1) sum_(chi in S) T_chi(q),
T_chi(q)=sum_(h in F_p^*, h!=1) chi(h) exp(2*pi*i*q*c(h)/p).       (1)
```

The Mobius map `z=c(h)` bijects `F_p^*\{1}` with `F_p\{-1,1}`. Hence the trivial character contributes exactly

```text
T_1(q)=-e_p(q)-e_p(-q),
|T_1(q)|<=2.                                                       (2)
```

For a nontrivial `chi`, after the same change of variables,

```text
T_chi(q)=sum_(z in F_p\{+-1}) chi((z+1)/(z-1)) e_p(qz).          (3)
```

The Kummer factor has a simple zero at `-1` and a simple pole at `1`, so it is not a power of order `ord(chi)`. The additive factor has a simple pole at infinity. The classical mixed Weil theorem applies. In sheaf language the rank-one sheaf is lisse on `P^1\{-1,1,infinity}`, is tamely ramified at the two finite points, has Swan conductor one at infinity, and has no `H_c^0` or `H_c^2`. Grothendieck--Ogg--Shafarev therefore gives `dim H_c^1=2`, and the Riemann hypothesis over finite fields gives

```text
|T_chi(q)| <= 2 sqrt(p).                                          (4)
```

Combining (1)--(4),

```text
|Ahat(q)| <= M_m(p),
M_m(p)=2*((m-1)*sqrt(p)+1)/m <= 2 sqrt(p).                        (5)
```

## 2. Centered fourth moment

Parseval gives

```text
sum_q |Ahat(q)|^2 = p n,
Ahat(0)=n,
sum_(q!=0)|Ahat(q)|^2 = n(p-n).                                  (6)
```

The additive-energy identity is

```text
E_+(A)=p^(-1) sum_q |Ahat(q)|^4.                                 (7)
```

Using one factor in the fourth moment pointwise and (6),

```text
E_+(A)-n^4/p
 <= M_m(p)^2 * n(p-n)/p                                          (8)
 = 4*((m-1)*sqrt(p)+1)^2/(m^2*p) * n(p-n)
 <= 4 n(p-n).                                                     (9)
```

Thus, uniformly for every subgroup size,

```text
E_+(A)=(K-1)^4/p + O(pK),                                        (10)
```

with the explicit one-sided error (9).

## 3. Hybrid with the global genus-one curve theorem

`cayley_curve_uniform.md` independently gives

```text
E_+(A) << K^(8/3)+K^4/p.                                         (11)
```

Together,

```text
E_+(A)-(K-1)^4/p << min(pK, K^(8/3)+K^4/p).                      (12)
```

If `K=p^(alpha+o(1))` with `alpha>3/5`, then the `pK` branch is strictly smaller than the previous worst-curve scale. In terms of `K`, its centered exponent is

```text
1+1/alpha < 8/3.                                                  (13)
```

At `alpha=2/3` this is `K^(5/2)`; as `alpha->1` it approaches the desired quadratic exponent. This is a genuine dense-regime improvement but it does **not** solve the sparse arithmetic frontier relevant to the present BGS route.

## 4. Why the sparse regime remains open

The Fourier coefficient in (1) is an inversive rational exponential sum over a subgroup. The complete-field character expansion proves square-root cancellation only at the `sqrt(p)` scale. Current small-subgroup Weil-sum methods do not cover this rational inverse shift in the range below `sqrt(p)`; Ostafe--Shparlinski--Voloch explicitly identify complete sums of `(a g+b)^(-1)` over subgroups below the square-root barrier as an open direction. Therefore (12) should not be read as evidence that the centered `K^(2+o(1))` theorem is close in the sparse regime.

## 5. Verification

`computations/verification/cayley_fourier_hybrid.py` enumerates every subgroup of every odd prime through a requested limit and checks exactly

```text
p*E_+(A)-n^4 <= 4*p*n*(p-n),                                     (14)
```

together with Cayley injectivity, central symmetry and equality of sum and difference energy. `computations/cpp/cayley_fourier_hybrid.cpp` is an independent C++20 implementation. The extended local audit through `p<=509` checks 807 subgroup designs, of which 364 lie on the strict dense side `K^5>p^3`; both implementations agree and pass.

Finite regression does not prove the mixed Weil theorem. Equation (4) is the external theorem input; equations (1)--(3) and (5)--(14) are project-internal algebra.
