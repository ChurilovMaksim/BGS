# Frobenius amplification for Cayley collisions over minimal finite extensions

**Status.** The structural theorems below are **EXACT** for odd prime subgroup
order `K`, conditional only on the maintained characteristic-zero Cayley
collision classification and square-resultant theorem.  The density theorem is
**EXACT + EXTERNAL-THEOREM**, using only the prime number theorem,
Brun--Titchmarsh, and the standard divisor bound `tau(n)=n^(o(1))`.
The finite examples are **FINITE-REGRESSION**.

This note deliberately changes one aspect of the maintained split-prime model.
Instead of requiring `p==1 (mod K)` and working in `F_p`, for every rational
prime `p!=2,K` we work in the **minimal extension**

```text
F_(p^f),     f=ord_K(p),
```

which contains the `K`-th roots of unity.  This exposes a Frobenius
multiplicity that is invisible in the completely split case `f=1`.

The result is not microscopic BGS.  Its value for the BGS programme is
structural: the existing `O(K^4)` collision-resultant mass budget combines with
Frobenius orbit size to give an almost-all **exact** quadratic Cayley-energy
theorem throughout every dyadic regime `K=X^theta`, `theta<1/3`, for this
minimal-extension family.  The exponent `1/3` matches the existing
double-averaged split-prime *mean-excess* threshold, while the split-prime exact
baseline theorem itself currently stops at `theta<1/5`.

## 1. Minimal-extension Cayley set

Let `K` be an odd prime and let `p!=2,K` be rational prime.  Put

```text
f=f_K(p):=ord_K(p),
q=p^f.
```

Then `K | q-1`, so `F_q^*` has a unique subgroup

```text
H=mu_K(F_q)
```

of order `K`.  Put

```text
c(h)=(h+1)/(h-1),
A_(K,p)=c(H\{1}) subset F_q.
```

The Mobius map `c` is injective away from `1`, so `|A_(K,p)|=K-1`.  Moreover

```text
c(h^-1)=-c(h).
```

For `d in F_q`, let

```text
r(d)=#{(x,y) in A_(K,p)^2:x-y=d}.
```

The characteristic-zero identity and central inversion-swap relations force,
for nonzero differences, the same combinatorial baseline as in the split
model:

```text
B_K=(K-1)(2K-5).
```

Define the minimal-extension non-forced excess

```text
Delta_K^ext(p)
 :=sum_(d!=0) r(d)^2-B_K.                                (1)
```

Exactly as in the split case, this is the number of ordered equal-difference
collision quadruples outside the two forced relations, hence

```text
Delta_K^ext(p) in Z_(>=0).                               (2)
```

If `Delta_K^ext(p)=0`, then the zero-difference bin contributes `(K-1)^2`, so

```text
E_+(A_(K,p))=3(K-1)(K-2).                               (3)
```

## 2. Frobenius orbit theorem

Choose a generator `h` of `H` and index the Cayley points by
`i in F_K^*`:

```text
a_i=c(h^i).
```

A non-forced ordered collision is a quadruple

```text
(i,j,r,s) in (F_K^*)^4,
i!=j, r!=s,
a_i-a_j=a_r-a_s,                                        (4)
```

not belonging to identity or inversion-swap.

### Theorem 1 (exact Frobenius amplification)

For every odd prime `K` and every rational prime `p!=2,K`, with
`f=ord_K(p)`,

```text
f | Delta_K^ext(p).                                      (5)
```

In particular,

```text
Delta_K^ext(p)>0  ==>  Delta_K^ext(p)>=f.                (6)
```

More strongly, the non-forced collision set is a disjoint union of Frobenius
orbits, each of size exactly `f`.

### Proof

The `p`-power Frobenius is an automorphism of `F_q` and

```text
c(x)^p=c(x^p)
```

because `c` is defined over `F_p`.  Therefore (4) is carried to

```text
(pi,pj,pr,ps) mod K,                                    (7)
```

and the forced/non-forced classification is preserved.

Suppose the `d`-th Frobenius power fixes one collision tuple with
`0<d<f`.  Its first coordinate gives

```text
p^d i == i (mod K).
```

Since `i!=0 (mod K)` and `K` is prime,

```text
p^d == 1 (mod K),
```

contradicting the definition `f=ord_K(p)`.  Hence every Frobenius orbit has
exactly `f` elements.  Counting the non-forced tuples proves (5)--(6).  `□`

The split case `p==1 (mod K)` is the extremal case `f=1`, so Theorem 1 gives no
extra multiplicity there.  This is precisely why the mechanism below improves
an all-prime minimal-extension average without silently improving the original
split-prime theorem.

## 3. The collision-resultant budget extends to every rational prime

Retain the normalized non-forced exponent-scaling orbits from
`cayley_resultant_mass_budget.md`.  Their number is

```text
N_K=K^3-5K^2+6K+1.                                      (8)
```

For a normalized representative `Q=(i,j,r,s)`, let `P_Q(X)` be the maintained
cleared collision polynomial and

```text
R_Q=Res(Phi_K,P_Q)=K^3 M_Q^2,    M_Q in Z\{0}.           (9)
```

Also

```text
|R_Q|<=12^(K-1).                                        (10)
```

For `p!=K`, choose a prime ideal `P` of `Z[zeta_K]` above `p`.  Its residue
degree is

```text
f=ord_K(p),
```

and reduction sends `zeta_K` to a primitive `K`-th root
`h in F_(p^f)`.

Let

```text
s_Q(p)
 =#{a in F_K^*: P_Q(h^a)=0}.                            (11)
```

This is exactly the number of non-forced collisions from the full
`F_K^*`-scaling orbit of `Q` in the minimal extension.

### Lemma 2 (valuation controls the whole non-split root orbit)

For every `p!=K`,

```text
s_Q(p)<=v_p(R_Q)=2v_p(M_Q).                              (12)
```

### Proof

The norm/product formula in the cyclotomic field is

```text
R_Q=product_(a in F_K^*) P_Q(zeta_K^a).                 (13)
```

Every `a` counted by (11) puts the corresponding factor in the prime ideal
`P`, so the right side lies in `P^(s_Q(p))`.  The prime `p` is unramified in
`Q(zeta_K)` because `p!=K`; with valuations normalized by `v_P(p)=1`, a
rational integer satisfies

```text
v_P(R_Q)=v_p(R_Q).
```

Thus `s_Q(p)<=v_p(R_Q)`.  Equation (9), with `p!=K`, gives the last equality
in (12).  `□`

Every non-forced collision belongs to one normalized scaling orbit, so

```text
Delta_K^ext(p)=sum_Q s_Q(p).                             (14)
```

The proof of the maintained split-prime mass budget therefore gives, without
the splitting hypothesis:

### Theorem 3 (all-prime weighted collision budget)

For every odd prime `K`,

```text
sum_(p prime, p!=2,K) Delta_K^ext(p) log p
 <= N_K ((K-1)log 12-3log K).                           (15)
```

In particular the right side is `<(log 12)K^4`.

### Proof

Using (12), then prime factorization of each `M_Q`,

```text
sum_(p!=2,K) Delta_K^ext(p)log p
 <=sum_Q sum_(p!=2,K) 2v_p(M_Q)log p
 <=sum_Q 2log|M_Q|.
```

By (9)--(10),

```text
2log|M_Q|
 =log(|R_Q|/K^3)
 <=(K-1)log12-3logK.
```

There are `N_K` normalized non-forced orbits.  `□`

Thus the old `O(K^4)` archimedean budget is unchanged, but a bad prime now
costs at least its residue degree `f`, not merely one collision.

## 4. The canonical discriminant criterion also extends beyond split primes

Let `S_K(T)` be the maintained primitive squarefree polynomial whose roots are
the distinct nonzero characteristic-zero Cayley differences, with weights
`w(alpha) in {1,2}`.  Its leading coefficient has no prime support away from
`K`.

### Theorem 4 (all-prime discriminant classification)

For every odd prime `K` and every rational prime `p!=2,K`,

```text
Delta_K^ext(p)>0  iff  p | Disc(S_K),                   (16)
Delta_K^ext(p)<=4v_p(Disc(S_K)).                         (17)
```

### Proof

Fix a prime ideal `P|p` in the cyclotomic field.  All roots of `S_K` are
`P`-integral and reduce to the nonzero differences of the minimal-extension
Cayley set.  (A nonzero characteristic-zero difference cannot reduce to zero:
that would give `c(h^a)=c(h^b)` with `a!=b`, contradicting injectivity of the
Mobius map.)

Partition the roots into clusters with equal reduction modulo `P`.  Exactly as
in the split proof,

```text
Delta_K^ext(p)
 =2 sum_clusters sum_(alpha<beta) w(alpha)w(beta).       (18)
```

Since the leading coefficient is a `p`-adic unit, the root formula gives

```text
v_P(Disc(S_K))
 =2 sum_(alpha<beta) v_P(alpha-beta).                    (19)
```

The discriminant is a rational integer and `p` is unramified, so

```text
v_P(Disc(S_K))=v_p(Disc(S_K)).
```

Hence `p` divides the discriminant exactly when at least one pair of distinct
roots coalesces modulo `P`, proving (16).  If `N_p` is the number of such
unordered pairs, (19) gives `v_p(Disc)>=2N_p`; since
`w(alpha)w(beta)<=4`, equation (18) gives

```text
Delta_K^ext(p)<=8N_p<=4v_p(Disc(S_K)).
```

This proves (17).  `□`

For `K=7`, the maintained exact factorization

```text
Disc(S_7)=2^348 7^63 13^12
```

therefore predicts the unique odd non-`K` exceptional rational prime `13`.
The finite regression below confirms

```text
ord_7(13)=2,
Delta_7^ext(13)=32.
```

## 5. Density-one exact baseline up to `theta<1/3`

The Frobenius factor becomes quantitatively useful when we average over
**unrestricted** rational primes rather than forcing the residue degree to be
one.

Fix

```text
0<theta<1/3,
Q=X^theta,
```

and define the dyadic minimal-extension design family

```text
D_theta^ext(X)
 ={(K,p):
     K,p prime,
     Q/2<K<=Q,
     X/2<p<=X}.                                         (20)
```

For large `X`, `p>K`, so `p!=K` automatically.  The prime number theorem gives

```text
|D_theta^ext(X)|
 ~(Q/(2log Q))(X/(2log X))
 =QX/(4log Q log X).                                    (21)
```

Let

```text
B_theta^ext(X)
 ={(K,p) in D_theta^ext(X):Delta_K^ext(p)>0}.            (22)
```

### Theorem 5 (almost-all exact baseline in minimal extensions)

For every fixed `0<theta<1/3`,

```text
|B_theta^ext(X)|/|D_theta^ext(X)| -> 0.                 (23)
```

Consequently, for asymptotically almost every pair in (20),

```text
Delta_K^ext(p)=0,
E_+(A_(K,p))=3(K-1)(K-2)                                (24)
```

**exactly**.

More quantitatively, choose any fixed `beta` satisfying

```text
max(0,4-1/theta)<beta<1.                                (25)
```

Then

```text
|B_theta^ext(X)|/|D_theta^ext(X)|
 <<_(theta,beta)
    Q^(beta-1+o(1)) + Q^(4-beta)/X.                     (26)
```

Both terms tend to zero under (25).

### Proof

Split pairs according to

```text
f=ord_K(p)<=K^beta                                      (27)
```

or `f>K^beta`.

**Small Frobenius order.**
Because `F_K^*` is cyclic, the number of nonzero residue classes modulo `K`
whose order is at most `K^beta` is

```text
sum_(d|K-1, d<=K^beta) phi(d)
 <=K^beta tau(K-1)
 =K^(beta+o(1)).                                        (28)
```

For each such residue class, Brun--Titchmarsh gives, uniformly for
`K<=X^theta`,

```text
#{p<=X:p==a (mod K)}
 <<_theta X/(K log X).                                  (29)
```

Therefore, for one prime `K~Q`, the number of primes in `(X/2,X]` with
`ord_K(p)<=K^beta` is

```text
<< X K^(beta-1+o(1))/log X.                             (30)
```

Summing over prime `K~Q` and dividing by (21) gives the first term in (26):

```text
<<Q^(beta-1+o(1)).                                      (31)
```

This tends to zero because `beta<1`.

**Large Frobenius order and bad reduction.**
If `f>K^beta` and the pair is bad, Theorem 1 gives

```text
Delta_K^ext(p)>=f>K^beta.
```

Restricting Theorem 3 to `X/2<p<=X` therefore gives, for each `K~Q`,

```text
#{bad p in (X/2,X] with f>K^beta}
 << K^(4-beta)/log X.                                   (32)
```

Summing over prime `K~Q` gives

```text
<<Q^(5-beta)/(log Q log X).                             (33)
```

After division by (21), this is the second term in (26):

```text
<<Q^(4-beta)/X.                                         (34)
```

Condition (25) is possible when `theta<1/3`, and it makes
`theta(4-beta)-1<0`, so (34) tends to zero.  This proves (23)--(24).  `□`

No Bombieri--Vinogradov theorem is needed here: the denominator is an
unrestricted product of dyadic prime sets, and Brun--Titchmarsh is used only as
an upper bound for the small-order residue classes.

## 6. Exact finite regression

`computations/verification/cayley_frobenius_extension.py` contains two
mechanistically distinct exact implementations:

1. polynomial-basis arithmetic in `F_(p^f)`, direct Cayley differences, and
   explicit Frobenius orbit decomposition;
2. factorization of `Phi_K` modulo `p`, followed by an independent sparse
   collision-polynomial divisibility test against one irreducible degree-`f`
   factor.

They agree on the non-split controls

```text
(K,p,f,Delta_K^ext(p))
 =(7,13,2,32),
  (11,43,2,128),
  (13,3,3,432),
  (13,5,4,496).                                         (35)
```

The direct implementation verifies that **every** non-forced collision orbit
has size exactly `f` in these examples.

For `K=7`, the square-resultant cutoff from
`cayley_resultant_structure.md` is below `94`.  Exhausting every odd rational
prime `p!=7` below `94` by the independent polynomial-factor method gives

```text
[(p,f,Delta)]=(13,2,32),                                (36)
```

in exact agreement with

```text
Disc(S_7)=2^348 7^63 13^12.
```

These finite checks test the mechanism and the all-prime extension of the
discriminant classification.  They are not the proof of Theorems 1--5.

## 7. What this changes, and what it does not

**Established here.**

- Frobenius turns every non-forced collision at rational prime `p` into an
  exact orbit of size `ord_K(p)`.
- The `O(K^4)` collision-resultant mass budget extends from split primes to all
  odd rational primes when the Cayley set is placed in its minimal finite
  extension.
- The canonical discriminant classifies exceptional reductions for all
  `p!=2,K`, not just split primes.
- Combining these facts with the scarcity of low-order residue classes gives
  density-one **exact** quadratic Cayley energy for every fixed
  `theta<1/3` in the minimal-extension family.

**Not established.**

- The theorem does not improve the original split family, because split primes
  have `ord_K(p)=1`.
- It does not prove the pointwise centered bound for every split prime.
- It does not provide a microscopic eigenphase law, a trace hierarchy, or BGS.
- No external novelty claim is made.  Targeted searches for Frobenius-orbit
  versions of this exact Cayley/resultant statement did not locate a matching
  theorem, but a failed search is not proof of novelty.

## 8. Next highest-information questions

1. **Can the Frobenius amplification be imported back into a symmetry-resolved
   quantum-map family?**  The split model erases the mechanism (`f=1`), so a
   useful physical model would have to retain a nontrivial residue-degree
   parameter rather than merely rephrase the same split quantization.
2. **Can the all-prime discriminant theorem constrain split support
   indirectly?**  The split exceptions are the residue-degree-one slice of the
   same canonical integer `Disc(S_K)`.  Any reciprocity, Chebotarev, or
   cyclotomic-unit restriction coupling its prime divisors to residue degree
   would feed directly into the pointwise programme.
3. **Can the `K^4` budget itself be lowered after weighting by residue degree?**
   Theorem 1 suggests studying `sum_p ord_K(p) 1_(Delta>0) log p` rather than
   unweighted support.  A genuine saving here would push the `theta=1/3`
   boundary.
4. **Microscopic bridge.**  Independently of arithmetic energy, BGS still
   requires a trace/correlation or resolvent criterion at mean-spacing scale.
   This should be formulated as an exact closure theorem rather than inferred
   from fourth moments.
