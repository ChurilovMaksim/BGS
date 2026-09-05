# Current results and exact scope

This is the concise theorem index. The repository-wide status authority is
[`../record/claim_ledger.md`](../record/claim_ledger.md); historical commits or
notes do not override it.

## 1. Pair-key / fourth-moment reduction — EXACT

For odd prime `p`, the off-diagonal key

```text
u=x/y, v=(x-1)/(y-1), d=x-y
```

is bijective with the maintained inverse formulas; the diagonal has
multiplicity `p-2`. Under subgroup constraints there are exactly
`(K-1)(K-2)` off-diagonal pairs and

```text
|V4|=(K^2+1)p^2-(6K^2+3K)p+13K^2-3K.
```

The corrected distribution is

```text
B(t)=O(t)+2(p-2)C_H(t)+(p-2)^2 1_{t=0}.
```

See [`fourth_moment_reduction.md`](fourth_moment_reduction.md).

## 2. Cayley additive-energy reduction — EXACT

For

```text
c(h)=(h+1)/(h-1),
A=c(H\{1}),
```

one has `d(u,v)=2/(c(u)-c(v))` and `c(h^-1)=-c(h)`. Thus the mixed layer is
controlled by `E_+(A)`. Prime-order characteristic-zero additive collisions
are only the forced identity/inversion-swap relations.

## 3. Best uniform pointwise theorem — EXACT + EXTERNAL-THEOREM

For

```text
100<K<p^(3/4)/3,
```

Vyugin--Makarychev gives

```text
E_+(A)<34K^(8/3).
```

The sharp target remains

```text
E_+(A)=(K-1)^4/p+O(K^(2+o(1))).
```

## 4. Fixed-product rows — EXACT

For one valid pair put `u=xy`, `s=x+y`. Then

```text
c(x)+c(y)=2(u-1)/(u-s+1).
```

At fixed product and nonzero parameter there is at most one unordered subgroup
pair. If `I_K(p)` is the maximal intersection size of two distinct product
rows, then

```text
Delta_K(p)<=4 I_K(p)(K-1)(K-2).
```

The normalized row ratio `r` has affine trace map

```text
Y=alpha_r X+beta_r,
alpha_r=U_(r-1)(tau/2),
beta_r=-2U_(r-2)(tau/2),
tau=zeta+zeta^-1.
```

## 5. Exact maximal-real order-three support — EXACT + EXTERNAL-THEOREM

Let `C_K(T)` be the minimal polynomial of `tau` and

```text
H_K(T)=(T-2)C_K(T).
```

After removing the unique invalid characteristic-zero trace, the source/target
cofactors have fixed degree `m=(K-1)/2`. For every split embedding prime,

```text
deg gcd(P_(K,r),Q_(K,r) mod q)=row intersection count.
```

The first three fixed-degree subresultants define an ideal contracting to
`Lambda_(K,r)^(3) Z`, and

```text
p|Lambda_(K,r)^(3)
iff
some row pair in ratio class [r] has I>=3.
```

Outside the product support `Lambda'_K^(3)`,

```text
I_K(p)<=2,
Delta_K(p)<=8(K-1)(K-2),
E_+(A)<=11(K-1)(K-2).
```

Exact anchors include

```text
Lambda'_(13,12)=5^2,
Lambda'_(17,10)=103,
Lambda'_(23,18)=47^3*139.
```

The older dehomogenized `D'/G'` invariants remain one-way obstructions only;
their converse failed a degree-drop audit at projective infinity.

See [`cayley_product_row_real_trace_ideal.md`](cayley_product_row_real_trace_ideal.md).

## 6. Characteristic-zero trace-intercept rigidity — EXACT + EXTERNAL-THEOREM

For trace classes define

```text
gamma_r(a,b)=t_b-alpha_r t_a.
```

Bass's prime-conductor cyclotomic-unit theorem implies multiplicative
independence of

```text
|1-zeta|,...,|1-zeta^m|.
```

Using

```text
|s_n|=E_[2n],
|t_x-t_y|=E_[x-y]E_[x+y],
```

one gets a complete fibre classification: every characteristic-zero fibre has
size at most `2`. For `r=-1` doubletons are swaps; for `r!=+-1` every doubleton
is, up to signs/exchange,

```text
([a],   [a+1-r]),
([a+2], [a+1+r]).
```

The identity comes from `t_(x+r)-t_(x-r)=s_r s_x`. A third point would create
a triangle in the step-two quotient of an odd cycle, which is impossible.

An independent C++20 group-ring verifier checks every normalized ratio through
the quick range `K<=199`; the recorded extended run reaches prime `K=809`.

See [`cayley_trace_intercept_rigidity.md`](cayley_trace_intercept_rigidity.md).

## 7. Cyclotomic-unit matching and general scalar support — EXACT

With `u_n=s_n/s_1`, valid row intersections satisfy exactly

```text
W_r(b)=V_r(a) mod q,
W_r(b)=u_((b+r)/2)u_((b-r)/2),
V_r(a)=u_r u_((a+1)/2)u_((a-1)/2).
```

Define the scalar shift resultant

```text
R_(K,r)(Z)
 =Res_T(P_1(T),R_r(alpha_r T+beta_r+Z))
 =c_0+c_1Z+c_2Z^2+....
```

Then

```text
ord_0 R_(K,r)=I_(1,r),
I>=3 iff c_0=c_1=c_2=0 mod q.
```

The three-generator contraction `Omega_(K,r)^(3)` has the same split
rational-prime support as `Lambda_(K,r)^(3)`. For each fixed ratio,

```text
sum_(p==1 mod K, I_r(p)>=3) log p=O(K^3).
```

This is not a polynomial largest-prime theorem; summing over `O(K)` ratios
returns the existing `O(K^4)` scale.

## 8. Inverse-row reflection — EXACT

For `r=-1`,

```text
alpha=-1,
beta=2tau,
Q(T)=-P(2tau-T).
```

Writing

```text
F(X)=P(tau+X)=E(X^2)+X O(X^2),
```

one has for every split embedding prime

```text
I_-1(q)=2 deg gcd(E,O mod q).
```

Thus inverse intersections are automatically even. A fixed-degree half-size
support ideal defines `Xi_K`. At `(K,p)=(31,1303)`, the direct intersection
size is `4`.

See [`cayley_product_row_reflection.md`](cayley_product_row_reflection.md).

## 9. Inverse pair-sum perfect square — EXACT

Let the roots of `F` be `x_1,...,x_m` and define

```text
R_-(Z)=Res_X(F(X),F(Z-X)).
```

Then universally

```text
R_-(Z)=2^m F(Z/2) S(Z)^2,
S(Z)=prod_(i<j)(Z-x_i-x_j).
```

For split primes, `2^mF(0)` is a unit, so

```text
I_-1(q)=2 ord_0 S(Z),
I_-1(q)>=3 iff S(0)=S'(0)=0 mod q.
```

The two-scalar ideal `(S(0),S'(0))` contracts to `Theta_K`; `Theta_K` has the
same split order-three support as `Xi_K` and the inverse factor of `Lambda`.
Full integer equality is not claimed.

See [`cayley_inverse_pair_sum_factorization.md`](cayley_inverse_pair_sum_factorization.md).

## 10. Inverse pair sums are a translated half-degree resultant — EXACT

The square root itself has a much cheaper description. Translate

```text
F_Z(X)=F(X+Z/2)=E_Z(X^2)+X O_Z(X^2).
```

Then, up to a convention-dependent sign,

```text
S(Z)=+-Res_Y(E_Z,O_Z).
```

In particular

```text
S(0)=+-Res(E,O),
S'(0)=+-d/dZ Res(E_Z,O_Z)|_(Z=0).
```

The first-order deformation is

```text
dE_Z/dZ|_0=(O+2Y O')/2,
dO_Z/dZ|_0=E'.
```

Hence inverse order-three support is simultaneous vanishing of a half-degree
resultant and its translation derivative. Both scalars can be computed with
one Sylvester determinant over dual numbers `eps^2=0`, avoiding the degree-`m^2`
shift resultant.

Exact two-scalar anchors are

```text
Theta'_7=1,
Theta'_11=1,
Theta'_13=5,
Theta'_17=1,
Theta'_19=37,
Theta'_23=47^2*137.
```

For comparison `Xi'_23=47*137`: split prime support agrees, valuations differ.
The translated route is orders of magnitude faster than the full shift
resultant in the maintained SymPy reference computation; Smith normal form is
the next finite-algebra bottleneck.

## 11. Inverse quartic localization and reduced edge ideals — EXACT

Two distinct zero pair sums of the split squarefree polynomial `F` cannot share
a root. Therefore inverse order-three support is already a four-root event. For
four distinct nonzero centred roots,

```text
I_-1>=3
iff I_-1>=4
iff e_1(x_1,x_2,x_3,x_4)=e_3(x_1,x_2,x_3,x_4)=0.
```

The converse is exact because the quartic

```text
X^4+e_2 X^2+e_4
```

is even, hence its four distinct nonzero roots form two opposite pairs.

For a general monic `F` of degree `m`, the pair-sum polynomial also has the
universal discriminant factorization

```text
Disc(S_F)=Disc(F)^(m-2) Q_F^2,
Q_F=prod_(|A|=4)(e_1(A)^3-4e_1(A)e_2(A)+8e_3(A)).
```

The first factor comes from pairs of pair-sum edges sharing one vertex; the
second comes from the three disjoint-edge pairings of each four-subset.

In the prime real cyclotomic field define

```text
v_n=(t_n-2)/(tau-2),
w_(a,b)=2-v_a-v_b.
```

Then `v_n` is a square of a real cyclotomic unit and

```text
2tau-t_a-t_b=(tau-2)w_(a,b),
|N(tau-2)|=K.
```

Away from `K`, inverse zero pair sums are therefore exactly `w_(a,b)=0 mod q`.
The inverse order-three support is equivalently the union of prime-ideal
supports of the two-generator ideals `(w_e,w_f)` for disjoint edges, or of the
quartic ideals `(e_1,e_3)`.

A rational `gcd(N(w_e),N(w_f))` is only a candidate filter: the two rational
norms can be divisible by the same `p` at different prime ideals. The maintained
negative control `K=41,p=2908049` exhibits precisely this failure, so a
same-embedding check is load-bearing.

An independent exact finite witness is

```text
K=89,
p=143207231,
p/K^4=2.282469174...,
I_-1=4,
zero edges=(16,35),(20,33).
```

Moreover

```text
|N(w_(16,35))|=|N(w_(20,33))|=143207231.
```

Thus a strict finite inverse-support ceiling `p<=K^4` is false. This does **not**
disprove the maintained asymptotic target `K^(4+o(1))`.

See [`cayley_inverse_quartic_localization.md`](cayley_inverse_quartic_localization.md).

## 11a. Full inverse even-multiplicity filtration — EXACT

The quartic statement is the first nontrivial case of a general theorem. On the
split squarefree locus,

```text
I_-1(q)=2 deg gcd(E,O)=2 ord_(Z=0) rho(Z),
rho(Z)=Res_Y(E_Z,O_Z).
```

For every `d>=1`,

```text
I_-1(q)>=2d
iff some 2d valid centred roots satisfy
e_1=e_3=...=e_(2d-1)=0.
```

Thus the first threshold not already manufactured by a universal size-two
associate class is

```text
I_-1>=6
iff three disjoint zero edges
iff six roots satisfy e_1=e_3=e_5=0
iff deg gcd(E,O)>=3
iff rho_0=rho_1=rho_2=0.
```

The finite regression checks direct translated-resultant order at `K=29,43`
and exhausts all `3003` six-subsets at `K=29,p=59`.

See [`cayley_inverse_even_multiplicity_localization.md`](cayley_inverse_even_multiplicity_localization.md).

## 11b. Cyclotomic-unit and weight-eight normalization — EXACT

Each valid centred inverse root has the stronger factorization

```text
x_a=(tau-2)lambda_a,
lambda_a=v_a-1=eta_(a-1)eta_(a+1) in O^(+x).
```

Hence

```text
w_(a,b)=-(lambda_a+lambda_b).
```

For sparse arithmetic it is even cheaper to use

```text
P_(a,b)=t_a+t_b-2tau=-(tau-2)w_(a,b).
```

At a primitive `K`-th root this is a Laurent relation of coefficient `l1`
weight exactly `8`. For a simultaneous `d`-edge event, subtract the first edge
equation from the other `d-1`; every generator still has weight at most `8`.
Thus `I_-1>=6` is a same-embedding three-generator weight-eight system.

The `K=229,p=966684838398077` structural edge relations are an adversarial
control: each individual weight-eight relation is indecomposable modulo `p`, so
small relation weight alone does not force small conductor in this split
positive-characteristic setting.

See [`cayley_inverse_cyclotomic_unit_normalization.md`](cayley_inverse_cyclotomic_unit_normalization.md).

## 11c. Reduced ordinary-resultant filter — EXACT

Before specializing `T=tau`, let `G` be the polynomial gcd of two inverse edge
polynomials and write

```text
w_e=G A,
w_f=G B,
gcd(A,B)=1.
```

If one prime ideal `q|p` contains both specialized edge generators, then
necessarily

```text
p | Res_T(C_K,G) Res_T(A,B).
```

Consequently the radical of the exact cross-class contraction integer divides
the radical of this rational scalar filter. The implication is one-way: extra
resultant primes need not correspond to the distinguished `K`-cyclotomic
embedding.

The reciprocal lift preserves the same prime information exactly. For

```text
A~(z)=z^deg(A) A(z+z^-1),
B~(z)=z^deg(B) B(z+z^-1),
```

one has

```text
Res_z(A~,B~)=Res_T(A,B)^2.
```

Exhaustive CI audits at `K=31,37,41,43` show that every nonconstant polynomial
gcd encountered evaluates as a unit at the real `K`-cyclotomic root. A separate
max-index-50 exact development audit found no shared irreducible non-cyclotomic
factor. The universal torsion-factor classification remains **OPEN**.

See [`cayley_inverse_reduced_resultant_filter.md`](cayley_inverse_reduced_resultant_filter.md).

## 12. Square collision resultants and canonical discriminants — EXACT

Every maintained prime-order cleared collision polynomial satisfies

```text
Res(Phi_K,P)=K^3M^2.
```

The Fibonacci slice

```text
Res(Phi_K,X^2+3X+1)=F_K^2
```

shows individual resultants may be exponentially large. The canonical
difference polynomial gives for split primes

```text
Delta_K(p)>0 iff p|Disc(S_K),
Delta_K(p)<=4v_p(Disc(S_K)),
```

with exact ratio-orbit fourth-power structure

```text
|Disc(S_K)|
 =2^((K-1)^4/4)K^((K-1)(K^2-7)/4)J_K^4.
```

## 13. Global split-prime mass and averaged theorems — EXACT / EXTERNAL-THEOREM

For odd prime `K`,

```text
sum_(p==1 mod K) Delta_K(p)log p
 <=(K^3-5K^2+6K+1)((K-1)log12-3logK).
```

For prime `K~X^theta`, split prime `p~X`, Bombieri--Vinogradov and PNT imply

```text
average Delta_K(p)/K^2 <<_theta X^(3theta-1)
```

for fixed `theta<1/3`. For fixed `theta<1/5`, asymptotically almost every split
pair has the exact baseline

```text
Delta_K(p)=0,
E_+(A)=3(K-1)(K-2).
```

## 14. Frobenius amplification in minimal finite extensions — EXACT

For arbitrary prime `p!=2,K`, put

```text
f=ord_K(p), q=p^f, H=mu_K(F_q).
```

Every non-forced collision Frobenius orbit has size exactly `f`, hence

```text
f | Delta_K^ext(p).
```

The weighted resultant budget and canonical discriminant classification extend
to all such rational primes. For unrestricted prime pairs `K~X^theta,p~X`,
PNT + Brun--Titchmarsh + the Frobenius multiplicity give a density-one exact
baseline for every fixed `theta<1/3` in the minimal extension. This does not
improve the split slice, where `f=1`.

See [`cayley_frobenius_amplification.md`](cayley_frobenius_amplification.md).

## 15. Full Cayley/Jacobi trace identity — EXACT

For the normalized full annihilator twisted-Jacobi matrix,

```text
1_Ahat(r)=K Tr M_S(2r),
sum_q|Tr M_S(q)|^2=p(K-1)/K^2,
sum_q|Tr M_S(q)|^4=pE_+(A)/K^4.
```

The normalized fourth/second moment ratio tends to `3` in the maintained split
double average below `theta<1/3`. This is not a CLT and not a local spectral
law.

## 16. Corrected off/off elliptic theorem — EXACT + EXTERNAL-THEOREM

Every generic class has a coherent reducible fibre of exact size `2p-8`.
After extraction, Igusa monodromy and Deligne/Fouvry--Kowalski--Michel
quasi-orthogonality give

```text
Var O << pE_+(A)+K^2p+K^4sqrt(p)+K^4.
```

Thus the elliptic layer is governed by the same Cayley-energy bottleneck.

## 17. Exact trace-to-local-statistics bridge — EXACT

For an `N x N` unitary matrix, partition-lattice Mobius inversion expresses
distinct-index exponential sums through products of traces. Poisson summation
then gives microscopic factorial statistics as weighted sums of those trace
products. In particular,

```text
C_(2,N)(U;phi)
 =N^(-2) sum_m phihat(m/N)(|Tr U^m|^2-N).
```

Band-limited microscopic tests require trace powers `|m|=Theta(N)`.
A weighted Heisenberg-scale joint-trace comparison with the target RMT ensemble
is sufficient for the corresponding band-limited microscopic theorem. The
required arithmetic/spectral trace estimates and the high-frequency tail for
arbitrary Schwartz tests are **OPEN**.

See [`trace_to_local_statistics_bridge.md`](trace_to_local_statistics_bridge.md).

## 18. Verification and adversarial controls

Promoted finite controls include:

- `(K,p)=(29,728017)` and `(31,1042903)` with `p>K^4` but positive excess;
- `(K,p)=(41,2908049)` with a row pair sharing two parameters, and separately
  as a reduced-edge norm-gcd false positive for inverse support;
- `(K,p)=(31,1303)` with inverse intersection size `4`;
- `(K,p)=(29,59)` with inverse multiplicity `6` and a unique six-root
  `e_1=e_3=e_5=0` certificate among all `3003` six-subsets;
- `(K,p)=(89,143207231)` with inverse intersection size `4`,
  `p=2.282469...K^4`, and exact four-root `e_1=e_3=0` certificate;
- `(K,p)=(229,966684838398077)` with exactly two structural inverse zero edges,
  `I_-1=4`, and indecomposable individual weight-eight relations;
- exact reduced-resultant cross-class anchors at `K=59,73,97` and structural
  anchors at `K=89,229`;
- max-index-50 exact shared-factor audit: `1225` edge polynomials, `24`
  repeated irreducible factor types, no non-cyclotomic reciprocal lift found;
- `(K,p)=(131,F_131)` with exact excess `32`;
- C++20 characteristic-zero intercept regression through an extended prime
  anchor `K=809`;
- independent C++20 verification of the `K=89` inverse witness;
- inverse translated-resultant/Smith anchors through `K=23`;
- exact reduced-edge split-support sweeps through the explicitly recorded
  prime `K=101`; no interrupted larger-batch output is promoted;
- minimal-extension controls
  `(K,p,f,Delta)=(7,13,2,32),(11,43,2,128),(13,3,3,432),(13,5,4,496)`.

Finite computation proves only its explicit finite statements.

## 19. Current frontier — OPEN

The active inverse arithmetic chain is now

```text
characteristic-zero edge associate classes
        + cross-class same-embedding support
        -> inverse multiplicity I_-1
        -> pointwise centered Cayley energy.
```

Literal elimination of every inverse `I>=4` event is structurally overstrong:
explicit associate pairs exist for every prime residue class modulo `5` in the
proved range. The more appropriate sufficient target is range-explicit
multiplicity, for example

```text
K=o(p^(1/4)),
B_K=K^o(1),
large split primes excluded from nonassociate cross-class contractions,
```

which would imply `I_-1=K^o(1)`. A stronger old target such as

```text
P_split^+(Lambda'_K^(3))<=K^(4+o(1))
```

remains logically sufficient to force `I<=2`, but is no longer the preferred
inverse mechanism. The new weight-eight and reduced-resultant formulations
identify concrete subproblems; they do not yet provide the required
largest-prime theorem. The torsion classification of shared edge-polynomial
factors is also open.

Even complete inverse control would not settle the other normalized row ratios.
For the full arithmetic problem the target remains

```text
I_K(p)=K^o(1), ideally O(1),
```

in the intended large-prime regime, which feeds the exact row-energy bound.

The microscopic chain is independently

```text
Heisenberg-scale desymmetrized joint traces
        -> band-limited microscopic RMT correlations
        -> high-frequency tail control
        -> full microscopic BGS/GOE/COE.
```

Full microscopic universality remains **OPEN**.