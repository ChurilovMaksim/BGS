# Frontier continuation — inverse multiplicity, unit normalization, and reduced resultants

Date: 2026-09-05
Branch: `frontier/inverse-quartic-20260905`
PR: `#13`

This record continues `frontier_pass_20260905.md`. It is a research-state
snapshot, not a substitute for the repository-wide authority
`claim_ledger.md`. GitHub Actions status is head-specific and must be checked
separately; this file does not imply that a later head is green.

## Objective

The original inverse-row route tried to eliminate all split order-three support
and thereby force `I_-1<=2`. Exact characteristic-zero associate identities now
show that this target is structurally overstrong: multiplicity four occurs in
universal associate families. The continuation therefore asks for a bounded or
subpolynomial **same-embedding multiplicity** theorem, with the first genuinely
new inverse threshold at `I_-1>=6`.

The full project closure remains much further downstream:

```text
inverse/general row multiplicity
    -> pointwise centred Cayley energy
    -> complete fourth moment
    -> Heisenberg-scale desymmetrized trace comparison
    -> microscopic RMT/BGS.
```

No microscopic BGS theorem is claimed.

## Exact results added in this continuation

### 1. All inverse multiplicities form one exact even filtration

On the split squarefree inverse locus, with

```text
F(X)=E(X^2)+X O(X^2),
F(X+Z/2)=E_Z(X^2)+X O_Z(X^2),
rho(Z)=Res_Y(E_Z,O_Z),
```

one has exactly

```text
I_-1(q)=2 deg gcd(E,O)=2 ord_(Z=0) rho(Z).
```

For every `d>=1`,

```text
I_-1(q)>=2d
```

if and only if some `2d` distinct valid centred roots form `d` opposite pairs,
which is equivalent to

```text
e_1=e_3=...=e_(2d-1)=0.
```

Thus

```text
I_-1>=6
iff three disjoint zero edges
iff six roots satisfy e_1=e_3=e_5=0
iff deg gcd(E,O)>=3
iff rho_0=rho_1=rho_2=0.
```

This is proved in
`mathematics/cayley_inverse_even_multiplicity_localization.md`.

### 2. Every valid centred inverse root is a ramified scalar times a unit

Put

```text
lambda_a=v_a-1.
```

Using

```text
eta_a^2-eta_(a-1)eta_(a+1)=1,
```

one obtains

```text
lambda_a=eta_(a-1)eta_(a+1) in O^(+x),
x_a=t_a-tau=(tau-2)lambda_a.
```

Consequently

```text
w_(a,b)=-(lambda_a+lambda_b).
```

For an oriented edge, `R_(a,b)=lambda_a/lambda_b` is a cyclotomic unit and

```text
q|w_(a,b) iff R_(a,b)=-1 mod q.
```

For several edges, their ideal can be row-reduced to one sign equation and
unit-ratio equality equations.

### 3. Simultaneous inverse support has a weight-eight trace normal form

The more economical sparse form is

```text
P_(a,b)=t_a+t_b-2tau=-(tau-2)w_(a,b).
```

At a primitive `K`-th root `zeta`,

```text
P_(a,b)(zeta)
 =zeta^a+zeta^-a+zeta^b+zeta^-b-2zeta-2zeta^-1.
```

Its coefficient `l1`-weight is exactly `8`. For simultaneous edges, subtract
one edge equation from the others; every new generator still has coefficient
`l1`-weight at most `8`.

Hence `I_-1>=6` gives three simultaneous weight-eight Laurent relations at the
**same** primitive `K`-th root and the **same** split prime ideal.

The large structural control

```text
K=229,
p=966684838398077
```

shows why one must use simultaneity: each individual structural weight-eight
relation is indecomposable modulo `p` under exhaustive proper-submultiset
checking. Therefore the naive inference

```text
small relation weight => small conductor K
```

is false in this split positive-characteristic setting.

### 4. Same-embedding cross-class support has an ordinary scalar filter

For two inverse edge polynomials before specializing `T=tau`, let

```text
G=gcd(w_e,w_f) in Z[T],
w_e=G A,
w_f=G B,
gcd(A,B)=1.
```

If one prime ideal `q|p` contains both specialized edge generators, then

```text
p | Res_T(C_K,G) Res_T(A,B).
```

Thus the radical of the exact cross-class contraction integer is contained in
the radical of a rational ordinary-resultant filter. This is a **necessary
condition only**; extra resultant primes can be false positives for the
distinguished real cyclotomic embedding.

The reciprocal lift does not create new prime information. For

```text
A~(z)=z^deg(A) A(z+z^-1),
B~(z)=z^deg(B) B(z+z^-1),
```

the root-product formula proves exactly

```text
Res_z(A~,B~)=Res_T(A,B)^2.
```

This explains the square Laurent resultants seen in finite computations and
shows that the real trace variable `T` is the cheaper representation.

See `mathematics/cayley_inverse_reduced_resultant_filter.md`.

## Finite exact controls

The maintained regressions include:

- `K=29,p=59`: three inverse zero edges, `I_-1=6`, parity gcd degree `3`,
  translated-resultant order `3`, and exactly one of all `3003` six-subsets
  satisfies `e_1=e_3=e_5=0`;
- `K=43,p=173`: four zero edges, `I_-1=8`, parity gcd degree and translated
  resultant order both `4`;
- `K=83,p=167`: `I_-1=14`;
- `K=89,p=179`: `I_-1=16`;
- `K=59,p=21713`: calibrated nonassociate cross-class event;
- `K=89,p=143207231`: structural associate event with `I_-1=4` and
  `p>2 K^4`;
- `K=229,p=966684838398077`: structural associate event with `I_-1=4` and
  `p/K^4=351514.284...`;
- exact ordinary-resultant cross-class anchors at `K=59,73,97`;
- exact ordinary-resultant structural anchors at `K=89,229`.

The reduced-resultant CI verifier also exhausts every edge pair at
`K=31,37,41,43`: every nonconstant polynomial gcd `G` encountered has

```text
|Res(C_K,G)|=1.
```

At `K=31`, all `15` distinct gcd polynomials have reciprocal lifts that factor
only into ordinary cyclotomic polynomials.

## Development-scale torsion-factor falsifier

A separate exact development audit is recorded at
`evidence/cayley_inverse_torsion_gcd_audit_20260905.txt`.

Environment:

```text
Python 3.13.5
SymPy 1.14.0
```

Range:

```text
0<=a<b<=50,
a,b!=1.
```

This gives `1225` edge polynomials. Every edge polynomial was factored exactly
over `Z[T]`; irreducible factors shared by two or more distinct edges were
collected globally. There were `24` repeated irreducible factor types. The
reciprocal lift of every one factored completely into ordinary cyclotomic
polynomials; the largest encountered order was `25`. No non-cyclotomic shared
factor was found.

This is **FINITE-EVIDENCE**, not proof of the universal torsion-factor
classification.

## Literature checks and non-imports

- Dvornicich--Zannier, *Sums of roots of unity vanishing modulo a prime*, is a
  relevant finite-characteristic framework, but no theorem from it is used as
  load-bearing input here because exact applicability to the present split,
  same-prime-ideal, simultaneous-congruence system has not been verified.
- Dilcher--Stolarsky, *Resultants and discriminants of Chebyshev and related
  polynomials*, gives explicit resultant formulas for certain Chebyshev linear
  forms. It is structurally adjacent to the new scalar route, but the formulas
  inspected do not directly cover arbitrary inverse edge pairs, so no direct
  theorem transfer is claimed.
- General sparse-polynomial resultant bounds are too weak by themselves: sparse
  resultants can still be exponentially large. The current route needs the
  special cyclotomic/associate structure.

## Open obligations

### A. Associate-class size

Prove a growing-`K` bound

```text
B_K=K^o(1),
```

ideally `B_K<=2` or another absolute constant, for the nonunit
characteristic-zero inverse edge associate classes.

### B. Torsion classification of shared polynomial factors

Prove or disprove:

```text
every irreducible polynomial factor shared by two distinct valid inverse edge
polynomials has cyclotomic reciprocal lift.
```

If true, these characteristic-zero common factors are support-free for prime
`K` outside the finitely compatible torsion orders and can be removed before
cross-class arithmetic.

### C. Large split primes of nonassociate reduced resultants

After removing shared torsion factors, prove a polynomial largest-split-prime
bound for the coprime ordinary resultants, strong enough for the intended

```text
K=o(p^(1/4))
```

regime. The old `K^(4+o(1))` threshold remains a natural sufficient scale, but
no such theorem is proved.

### D. Other normalized product-row ratios

Even complete inverse control is not full Cayley-energy control. The analogous
same-embedding multiplicity problem remains for the other ratio classes.

### E. Spectral closure

The deterministic trace-to-local-statistics bridge is exact, but the required
Heisenberg-scale desymmetrized joint-trace comparison and high-frequency tail
are open.

## Explicit non-claims / retractions preserved

- strict finite `p<=K^4` inverse support is false;
- rational `gcd(N(w_e),N(w_f))` is not a same-prime-ideal criterion;
- a single small-weight root-of-unity congruence does not force small `K` in the
  split finite-characteristic regime;
- the reduced ordinary resultant is not an exact converse for the distinguished
  embedding;
- finite torsion-factor audits are not a universal classification theorem;
- fourth moments/kurtosis are not a CLT or microscopic RMT law;
- full BGS/GOE/COE universality remains open.
