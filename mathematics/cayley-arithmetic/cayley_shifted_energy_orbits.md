# Cayley fibers as diagonal product bins of shifted subgroups

**Status: EXACT for the algebraic reduction and the global shift-energy identity; EXACT + EXTERNAL-THEOREM for the local `O(K^2 log K)` orbit bound; FINITE-REGRESSION for the promoted generic/exceptional designs.**

This note records a useful but deliberately limited reformulation of the
pointwise Cayley additive-energy problem.  A multiplicative `H`-orbit of Cayley
sum parameters is controlled by the multiplicative energy of one additive shift
`H+lambda`.  Shkredov's near-quadratic shifted-energy theorem therefore gives a
near-quadratic `L^2` bound **inside each parameter orbit**.

The same calculation also exposes the limitation of this route: summing the
orbit bounds by themselves gives only `O(K^3)` globally, which is weaker than
the maintained `O(K^(8/3))` pointwise theorem.  No pointwise quadratic Cayley
energy, CLT, or microscopic BGS statement is claimed here.

Throughout, `p` is an odd prime, `H<=F_p^*` is a multiplicative subgroup of
order `K`,

```text
c(h)=(h+1)/(h-1),
A=c(H\{1}),
```

and

```text
r(t)=#{(a,b) in A^2:a+b=t}.
```

## 1. Shifted product bins

Fix `lambda!=0`.  For `g in H`, define

```text
R_lambda(g)
 =#{(x,y) in H^2:(x+lambda)(y+lambda)=(g+lambda)^2}.      (1)
```

Scaling both variables by `g` gives the exact identity

```text
R_lambda(g)=R_(lambda/g)(1).                              (2)
```

For `mu!=-1`, put

```text
t(mu)=2mu/(1+mu).                                         (3)
```

The bilinear Cayley sum fiber is

```text
P_t(x,y)=(2-t)xy+t(x+y)-(2+t)=0.
```

With `mu=t/(2-t)`, the elementary identity

```text
((2-t)x+t)((2-t)y+t)=(2-t)P_t(x,y)+4
```

shows that on `P_t=0`,

```text
(x+mu)(y+mu)=(1+mu)^2.                                    (4)
```

Conversely (4) implies `P_t=0`.  In the enlarged domain `H^2`, the point
`(1,1)` always satisfies (4).  If `mu!=-1`, it is the only solution of (4)
with `x=1` or `y=1`: setting one variable equal to one forces the other to one.
Therefore

```text
R_mu(1)=r(t(mu))+1.                                       (5)
```

Combining (2) and (5), for every `g in H` with `g!=-lambda`,

```text
R_lambda(g)-1=r(t(lambda/g)).                              (6)
```

where the right-hand parameter is understood through (3).

## 2. Exact orbit-energy inequality

Let

```text
S_lambda=H+lambda
```

and let `rho_lambda(u)` be its ordered product representation function.  Write

```text
E_x(S_lambda)=sum_u rho_lambda(u)^2.                       (7)
```

For a product bin `u`, let

```text
d_lambda(u)=#{z in S_lambda:z^2=u}.                       (8)
```

The identity and swap relations contribute exactly

```text
2 rho_lambda(u)-d_lambda(u)
```

ordered collision quadruples in that bin.  Hence the non-forced contribution
of the bin is

```text
rho_lambda(u)^2-2rho_lambda(u)+d_lambda(u)
 =(rho_lambda(u)-1)^2+d_lambda(u)-1 >=0.                  (9)
```

Summing the identity/swap union over all bins gives the universal baseline for
any `K`-element set,

```text
D_K=2K^2-K.                                                (10)
```

The selected diagonal bins are

```text
u_g=(g+lambda)^2,   g in H, g!=-lambda.                   (11)
```

A nonzero selected bin has one or two diagonal preimages, and these are exactly
the corresponding `g`'s in (11).  Thus, bin by bin,

```text
sum_{g:u_g=u}(rho_lambda(u)-1)^2
 <=2[(rho_lambda(u)-1)^2+d_lambda(u)-1].                  (12)
```

Using (6), we obtain the main exact reduction.

### Theorem 1 (shifted-energy orbit bound)

For every `lambda in F_p^*`, define

```text
T_(lambda H)
 ={2mu/(1+mu):mu in lambda H, mu!=-1}.                   (13)
```

Then

```text
sum_{t in T_(lambda H)} r(t)^2
 <=2(E_x(H+lambda)-D_K).                                  (14)
```

The left side depends only on the multiplicative coset `lambda H`; the right
side does as well, since scaling `H+lambda` by an element of `H` preserves
multiplicative energy.

The sets `T_C`, as `C` ranges over the nonzero multiplicative cosets of `H`,
partition

```text
F_p\{0,2}.                                                (15)
```

Indeed `mu -> 2mu/(1+mu)` is a bijection from
`F_p\{-1}` to `F_p\{2}`, and nonzero `mu` correspond exactly to nonzero `t`.

## 3. Near-quadratic control of every orbit

A source-exact theorem of I. D. Shkredov, *On tripling constant of
multiplicative subgroups*, arXiv:1504.04522v1, Theorem 6, states that if
`Gamma,Pi<=F_p^*` and `|Gamma||Pi|<p`, then for nonzero shifts `x,y`,

```text
E_x(Gamma+x,Pi+y)
 << |Gamma||Pi| log(min(|Gamma|,|Pi|))
    +|Gamma|^2+|Pi|^2.                                   (16)
```

Applying (16) with `Gamma=Pi=H` gives, whenever

```text
K^2<p,                                                    (17)
```

```text
E_x(H+lambda)<<K^2 log(2K)                               (18)
```

uniformly in every `lambda!=0`.  For `K>=2`, this is also `O(K^2 log K)`;
for `K=1`, the Cayley set is empty.  Theorem 1 therefore yields:

### Corollary 2 (local near-quadratic Cayley `L^2` mass)

If `K^2<p`, then for every nonzero multiplicative coset `C` of `H`,

```text
sum_{t in T_C} r(t)^2 << K^2 log K.                      (19)
```

In particular this applies throughout the intended BGS moment regime
`K=o(p^(1/4))`.

This is stronger than controlling each Cayley fiber separately: one whole
`H`-orbit of parameters has near-quadratic square mass.  It is nevertheless a
**block estimate**, not yet the desired global bound.

## 4. Exact global shift-energy identity

There is an exact accounting identity which shows what is lost by summing (19)
naively.

### Theorem 3 (sum of shifted multiplicative excesses)

For every finite subgroup `H<=F_p^*` of order `K`,

```text
sum_{lambda in F_p}(E_x(H+lambda)-D_K)
 =K^4-E_+(H).                                             (20)
```

### Proof

Expanding a shifted product collision gives

```text
(a+lambda)(b+lambda)=(c+lambda)(d+lambda)
```

if and only if

```text
ab-cd+lambda(a+b-c-d)=0.                                 (21)
```

If `a+b!=c+d`, equation (21) has exactly one `lambda`.  If
`a+b=c+d` and `ab=cd`, the unordered pairs `{a,b}` and `{c,d}` coincide, so
there are exactly `D_K=2K^2-K` such ordered quadruples and each works for every
`lambda`.  If the sums agree but the products do not, no `lambda` works.

The number of quadruples with `a+b=c+d` is `E_+(H)`.  Hence the number with
unequal sums is `K^4-E_+(H)`, and summing shifted multiplicative energies over
all `lambda` gives

```text
sum_lambda E_x(H+lambda)
 =K^4-E_+(H)+pD_K.
```

Subtracting `pD_K` proves (20).

At `lambda=0`, the subgroup product representation is constant on `H`, so

```text
E_x(H)=K^3.                                               (22)
```

Consequently

```text
sum_{lambda!=0}(E_x(H+lambda)-D_K)
 =K^4-K^3+D_K-E_+(H).                                    (23)
```

The energy `E_x(H+lambda)` is constant on each nonzero coset `lambda H`, and
each such coset has `K` elements.  Summing Theorem 1 over nonzero cosets gives
the exact global consequence

```text
sum_{t notin {0,2}} r(t)^2
 <=(2/K)(K^4-K^3+D_K-E_+(H)).                            (24)
```

Thus this route alone gives only

```text
sum_{t notin {0,2}} r(t)^2=O(K^3),                       (25)
```

which is weaker than the maintained `O(K^(8/3))` pointwise theorem.

Equation (24) is useful precisely because it identifies the missing information:
one must exploit the **distribution** of shifted multiplicative excess across
cosets, or correlations between different product-row blocks, rather than sum
the near-quadratic bound (19) independently over all cosets.

## 5. Adversarial finite regression

`computations/verification/cayley_shifted_energy_orbits.py` checks (2), (5),
(14), and the finite version of (20) on small designs.  It also checks (14) on
two large split-prime exceptional reductions

```text
(K,p)=(29,728017),
(K,p)=(31,1042903),
```

both satisfying `p>K^4` and both having non-forced Cayley excess `48`.
These are useful negative controls against any attempted theorem asserting
pointwise exact baseline merely from a polynomial inequality such as `p>K^4`.

The finite checks are not part of the proof of Theorems 1 and 3.

## 6. Next closure target

The most promising refinement exposed by this reduction is to group ordered
subgroup pairs by their product `u=xy`.  For this final parametrization assume
`K` is odd.  Write `u=w^2` with `w in H`, and parametrize

```text
x=wz,
y=wz^(-1).
```

For two nonzero-sum product rows `u=w^2` and `v=q^2`, assume
`w^2!=1` and `q^2!=1`.  Take the admissible pairs `(wz,wz^(-1))` and
`(qs,qs^(-1))`, with `z notin {w,w^(-1)}` and `s notin {q,q^(-1)}`.
Equality of their nonzero Cayley sums is equivalent to an affine intersection
between cyclotomic trace values

```text
X=z+z^(-1),
Y=s+s^(-1),
Y=alpha X+beta,                                          (26)
```

with

```text
alpha=w(1-q^2)/(q(1-w^2)),
beta =2(q^2-w^2)/(q(1-w^2)).                             (27)
```

A uniform near-constant intersection theorem for these constrained affine
copies, in the polynomial-size split-prime regime, would convert the row
second moment to the desired quadratic scale.  Finite computations motivate
this route but do **not** currently prove such a theorem.
