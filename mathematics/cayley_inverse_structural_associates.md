# Universal structural associates in the inverse row

**Status: EXACT for the four residue-class cyclotomic-unit identities and their split-support implication; FINITE-REGRESSION for the displayed norm and finite-field anchors; OPEN for any uniform bound on the total same-embedding inverse multiplicity.**

This note changes the emphasis of the inverse-row programme.  The previous
support notes ask when a split prime creates two zero pair sums.  Here we show
that characteristic-zero arithmetic already supplies a pair of **associate
reduced edge elements** for every sufficiently large prime conductor.  Thus
order-three support is not an accidental exceptional phenomenon to be removed
completely: there are universal structural pairs whose simultaneous reduction
is forced at every prime ideal dividing one common principal ideal.

The useful pointwise target is therefore multiplicity control, not literal
elimination of all `I_-1>=4` primes.

## 1. Setup

Let `K` be an odd prime, `zeta` a primitive `K`-th root, and put

```text
tau=zeta+zeta^(-1),
L^+=Q(tau),
O^+=Z[tau].
```

As in `cayley_inverse_quartic_localization.md`, define

```text
v_0=0,
v_n=(t_n-2)/(tau-2),
w_(a,b)=2-v_a-v_b.                                      (1)
```

Choose the primitive `2K`-th root

```text
y=-zeta^((K+1)/2),
y^2=zeta,
y^K=-1, y^(2K)=1,                                      (2)
```

and put

```text
eta_n=(y^n-y^(-n))/(y-y^(-1)).                           (3)
```

Then `eta_n` is a real cyclotomic unit whenever `n` is nonzero modulo `K`, and

```text
v_n=eta_n^2.                                             (4)
```

Indeed `eta_n` differs from `(1-zeta^n)/(1-zeta)` by a root-of-unity factor
chosen so that the quotient is real.

For a valid inverse edge `(a,b)`, reduction of `w_(a,b)` to zero at a split
embedding prime is equivalent to the zero pair-sum condition for the centred
trace roots.  Two disjoint zero edges therefore give `I_-1>=4`.

## 2. Four universal associate identities

Write

```text
K=5r+s,    s in {1,2,3,4}.                              (5)
```

For each residue class define two edges `e_s,f_s` and a unit `eps_s` by the
following table.

```text
s=1:
 e_1=(r-2, 2r+3),   f_1=(r+2, 2r+1),
 eps_1=eta_(r-1) eta_(2r+2) / (eta_(r+1) eta_(2r)).

s=2:
 e_2=(r+1, 2r-1),   f_2=(r+3, 2r+3),
 eps_2=eta_r eta_(2r) / (eta_(r+2) eta_(2r+2)).

s=3:
 e_3=(r-2, 2r-1),   f_3=(r,   2r+3),
 eps_3=eta_(r-1) eta_(2r) / (eta_(r+1) eta_(2r+2)).

s=4:
 e_4=(r-1, 2r+1),   f_4=(r+3, 2r-1),
 eps_4=eta_r eta_(2r+2) / (eta_(r+2) eta_(2r)).          (6)
```

### Theorem 1 (structural associate theorem)

Whenever the displayed indices are nonzero modulo `K`, one has in `L^+`

```text
w_(e_s)=eps_s w_(f_s).                                   (7)
```

Every `eps_s` is a unit of `O^+`.  Hence

```text
(w_(e_s))=(w_(f_s))                                      (8)
```

as principal ideals.

For prime `K>=37`, the two displayed edges are distinct, disjoint, valid real
trace-class edges in the maintained inverse row.  The smaller prime cases may
be handled separately; the asymptotic statement needs no exception after
`K>=37`.

### Proof

Put

```text
S_n=y^n-y^(-n),    D=S_1.                                (9)
```

Then

```text
eta_n=S_n/D,
D^2 w_(a,b)=2D^2-S_a^2-S_b^2.                           (10)
```

For one row of (6), write

```text
e_s=(a,b), f_s=(c,d),
eps_s=eta_A eta_B/(eta_C eta_D).                         (11)
```

After cross-multiplication and clearing `D^4`, equation (7) is equivalent to
vanishing of the Laurent polynomial

```text
N_s=(2D^2-S_a^2-S_b^2) S_C S_D
    -(2D^2-S_c^2-S_d^2) S_A S_B.                        (12)
```

A direct expansion has exactly twelve nonzero monomials.  More precisely,

```text
N_s=(y^(2K)-1) Q_s(y),                                   (13)
```

where the six-term Laurent quotients are

```text
Q_1=
  y^(-7r-7)-y^(-7r-3)-y^(-5r-5)+y^(3-5r)
 +y^(1-3r)-y^(5-3r),

Q_2=
 -y^(-7r-6)+y^(-7r-2)+y^(-5r-6)-y^(2-5r)
 -y^(-3r-2)+y^(2-3r),

Q_3=
 -y^(-7r-5)+y^(-7r-1)+y^(-5r-7)-y^(1-5r)
 -y^(-3r-5)+y^(-3r-1),

Q_4=
  y^(-7r-4)-y^(-7r)-y^(-5r-8)+y^(-5r)
 +y^(-3r-8)-y^(-3r-4).                                  (14)
```

Thus the twelve terms pair into six opposite-coefficient monomials whose
exponents differ by

```text
2K=10r+2s.                                               (15)
```

Since `y^(2K)=1`, (13) gives `N_s=0`, proving (7).  Each factor `eta_n` in (6)
is a cyclotomic unit, so `eps_s` is a unit and (8) follows. `□`

The proof uses only the order relation `y^(2K)=1`; no finite-field theorem and
no numerical pattern recognition enters the identity.

## 3. Deterministic split-support factory

Let

```text
M_(K,s)=|N_(L^+/Q)(w_(e_s))|
       =|N_(L^+/Q)(w_(f_s))|.                            (16)
```

### Corollary 2 (split divisor gives inverse multiplicity four)

Let `p!=K` be a rational prime with

```text
p==1 mod K,
p | M_(K,s).                                             (17)
```

Then for some split prime ideal `q|p`, both structural edges vanish modulo the
**same** `q`.  Consequently

```text
I_-1(q)>=4.                                              (18)
```

### Proof

Since `p|N(w_(e_s))`, some prime ideal `q|p` divides `(w_(e_s))`.  By (8) the
same ideal divides `(w_(f_s))`.  For `p==1 mod K`, the residue field is `F_p`;
the two edge congruences are exactly two disjoint inverse zero pair sums.  The
pair-sum formula gives two units of zero order and hence `I_-1>=4`. `□`

This is a one-way factory.  It does **not** say that every inverse exceptional
prime comes from the structural pair, nor that `M_(K,s)` always has a split
prime divisor.

## 4. Exact norm anchors

One resultant per conductor is enough to evaluate the structural norm.  Exact
integer computations give, among others,

```text
K= 19: M=37,
K= 29: M=59,
K= 31: M=929,
K= 41: M=3361,
K= 59: M=50033,
K= 71: M=3148423=853*3691,
K= 79: M=10969151=317*34603,
K= 89: M=143207231,
K=139: M=2003364256667=557*3596704231,
K=229: M=32763849227826023761
                =33893*966684838398077.                 (19)
```

The congruence signs of the displayed factors matter.  For example:

```text
3596704231 == 1 mod 139,
33893       == 1 mod 229,
966684838398077 == 1 mod 229.                            (20)
```

whereas some other structural norm factors are `-1 mod K` and therefore do
not give split `F_p` witnesses for the original split row problem.

The norm data suggest exponential rather than polynomial raw norm growth; this
is finite evidence only, not an asymptotic theorem.

## 5. A stronger finite adversarial witness at K=229

For

```text
K=229,
r=45,
s=4,
e=(44,91),
f=(48,89),
p=966684838398077,                                      (21)
```

exact arithmetic verifies

```text
p is prime,
p==1 mod 229,
p/229^4 = 351514.2841786269... .                         (22)
```

Using a primitive `229`-th root in `F_p` and real embedding exponent `j=91`,
the complete zero-edge enumeration is exactly

```text
(44,91), (48,89).                                        (23)
```

Thus

```text
I_-1=4.                                                  (24)
```

The structural norm itself is

```text
|N(w_(44,91))|=|N(w_(48,89))|
 =33893*966684838398077.                                 (25)
```

This is a finite certificate.  It strengthens the earlier `K=89` observation
that a strict universal ceiling `p<=K^4` is false.  It still does **not** by
itself disprove an asymptotic statement of the form `K^(4+o(1))`.

## 6. Strategic consequence for the energy route

The product-row theorem gives

```text
Delta_K(p)<=4 I_K(p)(K-1)(K-2).                         (26)
```

Therefore quadratic or near-quadratic Cayley energy does not require
`I_K<=2`.  A uniform bound

```text
I_K(p)=O(1)                                              (27)
```

would already give `Delta=O(K^2)`, and even

```text
I_K(p)=K^o(1)                                            (28)
```

would give the near-quadratic form `K^(2+o(1))`.

Theorem 1 shows that trying to eliminate every `I_-1>=4` prime is structurally
misaligned: universal associate pairs exist before reduction.  The higher-value
pointwise question is now:

```text
How many distinct reduced edge elements can vanish at one split embedding
prime q?                                                  (29)
```

Equivalently, control the maximum same-embedding multiplicity of the zero root
of the inverse pair-sum polynomial, rather than the mere support of that zero.

## 7. Open problems exposed by the structural families

1. **Multiplicity bound.** Prove `I_-1(q)=K^o(1)` or ideally `O(1)` uniformly
   on the intended split range.
2. **Associate-class classification.** Determine all characteristic-zero unit
   associations among the reduced edge elements `w_(a,b)`.  The four families
   above are explicit universal classes, not yet a completeness theorem.
3. **Structural norm arithmetic.** Understand `M_(K,s)`, including its size,
   factorization, and the occurrence of residue-degree-one factors `p==+-1 mod K`.
4. **General ratios.** Decide whether analogous unit-associate families exist
   for `r!=-1` product rows.
5. **BGS scope.** None of these arithmetic identities proves microscopic RMT;
   the separate Heisenberg-scale trace-comparison problem remains open.
