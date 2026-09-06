# Frontier pass — 2026-09-05

## Objective

The closure target remains a rigorous microscopic BGS/RMT theorem for a
specified deterministic chaotic quantum system after all genuine symmetries are
resolved.  Finite moments, eigenfunction statements, numerical resemblance and
fixed-power trace information are not substitutes for a mean-spacing local law.

This date produced several exact arithmetic and deterministic spectral
advances.  It did **not** solve microscopic BGS.

## A. Frobenius amplification over minimal finite extensions

Authoritative note:

- `mathematics/cayley_frobenius_amplification.md`

For odd prime `K` and rational prime `p!=2,K`, put

```text
f=ord_K(p), q=p^f,
H=mu_K(F_q), A=c(H\{1}).
```

Every non-forced collision has a Frobenius orbit of size exactly `f`, so

```text
f | Delta_K^ext(p).
```

The normalized collision-resultant budget and canonical difference
discriminant extend to all rational `p!=2,K` in the minimal extension.  PNT,
Brun--Titchmarsh and scarcity of small multiplicative orders then give a
density-one **exact** Cayley baseline for unrestricted prime pairs
`K~X^theta,p~X` for every fixed `theta<1/3`.  This does not improve the split
slice, where `f=1`.

Independent exact controls include

```text
(K,p,f,Delta)
=(7,13,2,32),
 (11,43,2,128),
 (13,3,3,432),
 (13,5,4,496).
```

## B. Exact trace-to-local-statistics bridge

Authoritative note:

- `mathematics/trace_to_local_statistics_bridge.md`

Partition-lattice Mobius inversion gives, for a zero-sum integer tuple,

```text
D_U(m_1,...,m_k)
 =sum_(pi in Pi_k) mu(pi)
   product_(B in pi) Tr(U^(sum_(a in B)m_a)).
```

Poisson summation then gives

```text
C_(k,N)(U;phi)
 =N^(-k) sum_(m in Z^(k-1)) phihat(m/N) D_U(m).
```

Compact Fourier support therefore probes powers `Theta(N)`, the Heisenberg
scale.  The deterministic Fourier conversion is closed.  The open spectral
input is a weighted Heisenberg-scale joint-trace comparison for the correct
desymmetrized block, plus a high-frequency tail theorem beyond band-limited
tests.

## C. Exact real-trace order-three support

The earlier dehomogenized `D'/G'` constructions were adversarially re-audited.
Leading degree can drop at the projective point `mu=infinity`, so their
converses are retracted; they remain one-way obstructions only.

The active exact split support is the fixed-degree maximal-real trace ideal
from

- `mathematics/cayley_product_row_real_trace_ideal.md`,
- `computations/verification/cayley_product_row_real_trace_ideal.py`.

For split primes,

```text
p|Lambda_(K,r)^(3)
iff
some row pair in ratio class [r] has I>=3.
```

Outside the product support,

```text
I_K(p)<=2,
Delta_K(p)<=8(K-1)(K-2),
E_+(A)<=11(K-1)(K-2).
```

Exact realized support anchors include

```text
Lambda'_(17,10)=103,
Lambda'_(23,18)=47^3*139.
```

## D. Inverse-row reflection reduction

For `r=-1`,

```text
alpha=-1,
beta=2tau,
Q(T)=-P(2tau-T).
```

Writing

```text
F(X)=P(tau+X)=E(X^2)+X O(X^2)
```

gives exactly

```text
I_-1(q)=2 deg gcd(E,O mod q).
```

Thus inverse-row intersections are automatically even and the order-three
event is a corank-two half-degree problem.  The associated exact support
integer is `Xi_K`.  At `(K,p)=(31,1303)` the direct inverse intersection has
size `4`.

Authoritative files:

- `mathematics/cayley_product_row_reflection.md`,
- `computations/verification/cayley_product_row_reflection.py`.

## E. Cyclotomic trace-intercept rigidity

Authoritative note:

- `mathematics/cayley_trace_intercept_rigidity.md`

Let

```text
t_a=zeta^a+zeta^(-a),
s_a=zeta^a-zeta^(-a),
gamma_r(a,b)=t_b-(s_r/s_1)t_a.
```

Bass's prime-conductor theorem implies multiplicative independence of

```text
|1-zeta|,...,|1-zeta^((K-1)/2)|.
```

Together with

```text
|s_n|=E_[2n],
|t_x-t_y|=E_[x-y]E_[x+y],
```

this closes the characteristic-zero affine-intercept problem.

### Exact theorem

For every odd prime `K>=7` and normalized ratio `r!=1`, every fibre of

```text
([a],[b]) -> gamma_r(a,b)
```

has cardinality at most two.

- For `r=-1`, a double fibre is only a swap.
- For `r!=+-1`, every double fibre is, up to signs/exchange,

```text
([a],   [a+1-r]),
([a+2], [a+1+r]).
```

The identity follows from `t_(x+r)-t_(x-r)=s_r s_x`.  A third source point
would create a triangle in the step-two quotient of the odd `K`-cycle by
`a~-a`; that quotient is a path.  Hence finite order-three support is genuinely
created by reduction.

The independent C++20 sparse group-ring verifier checks every normalized ratio
through the maintained quick range `K<=199`; the recorded extended run reaches
prime `K=809`, always with maximum fibre size `2` and the predicted double-fibre
form.

Evidence:

- `evidence/cayley_trace_intercept_rigidity_20260905.txt`.

## F. Cyclotomic-unit matching and general scalar support

Put

```text
u_n=s_n/s_1,
W_r(b)=u_((b+r)/2)u_((b-r)/2),
V_r(a)=u_r u_((a+1)/2)u_((a-1)/2).
```

Every split row intersection is exactly

```text
W_r(b)=V_r(a) mod q.
```

Define

```text
R_(K,r)(Z)
 =Res_T(P_1(T),R_r(alpha_r T+beta_r+Z))
 =c_0+c_1 Z+c_2 Z^2+....
```

The product formula gives

```text
ord_(Z=0)(R_(K,r) mod q)=I_(1,r)(q),
I>=3 iff c_0=c_1=c_2=0 mod q.
```

The three-generator contraction `Omega_(K,r)^(3)` has the same split
rational-prime support as the exact real-trace `Lambda_(K,r)^(3)`.  For each
fixed ratio,

```text
sum_(p==1 mod K, I_r(p)>=3) log p=O(K^3).
```

This is a localization gain, not pointwise closure: there are `O(K)` ratios, so
summing returns the existing `O(K^4)` scale.

Exact small Smith anchors are

```text
(K,r)=(7,2):   Omega'=1,
(K,r)=(11,7):  Omega'=1,
(K,r)=(13,3):  Omega'=1,
(K,r)=(13,12): Omega'=5^2.
```

## G. Inverse pair-sum perfect square

New authoritative note:

- `mathematics/cayley_inverse_pair_sum_factorization.md`

New exact verifier/evidence:

- `computations/verification/cayley_inverse_pair_sum_factorization.py`,
- `evidence/cayley_inverse_pair_sum_factorization_20260905.txt`.

Let the roots of the inverse centred cofactor `F` be `x_1,...,x_m`.  The
inverse shift resultant satisfies the universal identity

```text
Res_X(F(X),F(Z-X))
 =2^m F(Z/2) S(Z)^2,
S(Z)=product_(i<j)(Z-x_i-x_j).
```

For split `p!=K`, the diagonal factor is a unit at zero.  Hence

```text
I_-1(q)=2 ord_0 S,
I_-1(q)>=3 iff S(0)=S'(0)=0 mod q.
```

The two-scalar ideal `(S(0),S'(0))` contracts to `Theta_K`, which has the same
split rational-prime order-three support as `Xi_K` and the inverse factor of
`Lambda`; full valuations may differ.

The old reflection resultant is exactly the constant pair-sum coefficient up
to sign:

```text
S(0)=+-Res_Y(E,O).
```

Also

```text
|N(R_-(0))|
 =2^(m^2) K^m |N(Res(E,O))|^2.
```

Thus prime-to-`2K` valuations in this particular norm are automatically even.
This explains part of the finite square pattern but does not imply equality of
support integers.

## H. Pair sums are a translated half-degree resultant

The pair-sum square root itself has the exact half-degree representation

```text
F_Z(X)=F(X+Z/2)=E_Z(X^2)+X O_Z(X^2),
S(Z)=+-Res_Y(E_Z,O_Z).
```

Therefore

```text
S(0)=+-Res(E,O),
S'(0)=+-d/dZ Res(E_Z,O_Z)|_(Z=0),
```

with first-order translation

```text
dE_Z/dZ|_0=(O+2Y O')/2,
dO_Z/dZ|_0=E'.
```

This is the preferred scalable inverse computation: one half-degree Sylvester
determinant over dual numbers rather than a degree-`m^2` shift resultant.

### Exact finite anchors

The translated route gives

```text
Theta'_7=1,
Theta'_11=1,
Theta'_13=5,
Theta'_17=1,
Theta'_19=37,
Theta'_23=47^2*137.
```

Existing reflection values include

```text
Xi'_13=5,
Xi'_19=37,
Xi'_23=47*137.
```

The split prime supports agree while valuations need not.

### Performance audit

In the same exact SymPy environment, representative wall times were
approximately

```text
K=17: full degree-m^2 shift route ~50.9 s,
      translated half-degree route ~0.58 s;
K=23: translated half-degree route ~6.1 s.
```

At larger `K`, integer Smith normal form becomes the next bottleneck; an attempt
to push the same reference path to `K=29/31` was deliberately interrupted.
No mathematical conclusion is drawn from the performance cutoff.  The next
engineering target is modular/fraction-free Smith or determinant arithmetic in
`Z[tau]`.

## I. Literature audit

Primary source audit:

- `literature/cyclotomic_row_support_sources_20260905.md`.

Bass 1966 is the load-bearing external theorem for multiplicative independence.
Hang Fu's projective-equivalence work is nearby characteristic-zero prior art.
Dvornicich--Zannier 2002 remains a **lead only**: its modulo-prime
Conway--Jones analogue has not been matched to the one-prime-ideal hypotheses
required here.  The maintained Fibonacci collision family warns directly that
a naive ``short relation modulo one finite embedding implies bounded K'' claim
is false.

## J. Current frontier

### Established

1. Exact pair-key and corrected fourth-moment reductions.
2. Exact real-trace split order-three support and the quadratic Cayley-energy
   theorem outside it.
3. Complete characteristic-zero affine-intercept classification.
4. Explicit cyclotomic-unit congruence model for finite row intersections.
5. General three-scalar shift support and per-ratio `O(K^3)` logarithmic mass.
6. Inverse half-degree reflection support.
7. Inverse perfect-square pair-sum factorization and two-scalar support.
8. Translated half-degree resultant/derivative formulation, eliminating the
   degree-`m^2` symbolic resultant for inverse order-three support.
9. Frobenius density-one exact minimal-extension theorem for `theta<1/3`.
10. Exact Heisenberg-scale trace-to-local-statistics Fourier bridge.

### Open

1. **Largest split support prime / common-gcd theorem.** Prove, for example,

```text
P_split^+(Lambda'_K^(3))<=K^(4+o(1))
```

or an equivalent theorem for `Omega` / inverse `Theta`.  The most structured
inverse target is now common-divisor control of `Res(E,O)` and its translation
derivative.
2. **Pointwise split Cayley energy.** Close

```text
E_+(A)=(K-1)^4/p+O(K^(2+o(1)))
```

for all intended split designs.
3. **Heisenberg trace problem.** Prove weighted joint-trace comparison for the
correct desymmetrized spectral block at powers `Theta(N)`.
4. **High-frequency tail.** Remove the Fourier band-limit.
5. **Microscopic BGS/RMT.** Still open.

## K. Repository state

The earlier frontier PR has been merged.  The date's promoted proofs,
regressions, C++ verifier, evidence, source audit, CI gates, claim ledger,
theorem index, README and manuscript are maintained directly on `main` under
`record/research_operating_protocol.md`.  The claim ledger remains the final
status authority.