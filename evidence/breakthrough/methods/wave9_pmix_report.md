# Wave 9, task 2 — Lemma Y gap Pmix: CRT mixing and carries

## 1. Problem and reduction

Lemma Y (for $t=\gcd(m,4)$, classes $O_r=\{i:i\equiv r\pmod t\}$,
$Y_r(y)=\sum_{i\in O_r}y_i$): if $y,y'\in\mathrm{Fix}_m$ have the same
multiset of entries, then $Y(y')=\pi(Y(y))$ for some $\pi\in D_t$.

Fix $m$ with $t=4$ (the only non-trivial case with mixing risk).
Write $D=D_m$, $q_2=2^{v_2(D)}$, $q_3=3^{v_3(D)}$.
Component Lemma Y (Wave 8, verified by enumeration at $m\le 20$,
and in the searches below at $m\le 28$) gives, for a global pair
$y'=\sigma(y)$, per-prime-power permutations $\pi_q\in D_4$ with
$Y'\equiv\pi_q(Y)\pmod q$. The vanishing lemma (proved in Wave 8
via $\mathbb Z[\sqrt2]$, $\alpha-\beta$ a unit at $p\neq2,3$)
gives $Y\equiv0\pmod q$ for every odd prime power $q\parallel D$,
$q\neq3$, so those components constrain nothing. Hence only
$q_2$ and $q_3$ matter, and the question is whether
$\Pi_2\cap\Pi_3\neq\emptyset$ for a component pair that admits a
common $\sigma$.

Definitions used in the searches: component pairs are ordered
pairs $(z,z')$ of Fix vectors mod $q$ with the same multiset;
$\Pi_q(z,z')=\{\pi\in D_4 : Y(z')=\pi(Y(z))\pmod q\}$.
A pair is *incompatible* if $\Pi_2\cap\Pi_3=\emptyset$.
A global fiber pair $y'=\sigma(y)$ restricts to component pairs
with the same $\sigma$ (Kuhn matching on the joint values
$(z_2[i],z_3[i])$). Therefore:

**Reduction theorem (mod-$D$ level).** If no incompatible
component pair admits a common $\sigma$, then $Y'\equiv\pi(Y)
\pmod D$ for some $\pi\in D_4$ for every global fiber pair.

## 2. Ker-level mixing is real (component lemmas alone do not suffice)

Abstract ker vectors can mix. Example at $m=12$ ($q_2=128$, $q_3=9$):

- $v_2=(0,32,64,96)\pmod{128}$, $v_2'=v_2$: $\Pi_2=\{\mathrm{id}\}$
  (rotation by 2 gives $(64,96,0,32)$, reflection
  $(0,3,2,1)$ gives $(0,96,64,32)$, both $\neq v_2$).
- $v_3=(0,3,0,6)\pmod 9$, $v_3'=(0,6,0,3)$:
  $\Pi_3\supset\{(0,3,2,1),(2,3,0,1)\}$ (reflection fixing 0,2,
  and rotation by 2), and $\mathrm{id}\notin\Pi_3$.

Let $v,v'$ be the coordinatewise CRT lifts of
$(v_2,v_3,0,0,0)$ and $(v_2',v_3',0,0,0)$ mod $D_{12}$.
Then $v'$ is in the $D_4$-orbit of $v$ mod 128 and mod 9,
but no single $\pi$ works for both. So Pmix is a genuine gap:
component Lemma Y does **not** by itself imply global Lemma Y.
The question is whether such a ker pair can be realised as
$Y(y),Y(y')$ for a global fiber pair with a common $\sigma$ —
the searches below say no, at every $t=4$ case tested.

## 3. Common-$\sigma$ searches: 0 mixing at all tested $t=4$ cases

Method: enumerate Fix mod $q_2$ and mod $q_3$ (numpy, exact),
group by sorted multiset, compute $\Pi_q$ for every component
pair, then for every incompatible pair test whether a common
$\sigma$ exists (Kuhn matching on joint component values).
Scripts: `methods/pmix_search_general.py`
(and `methods/pmix_search_m12.py`, `methods/pmix_ker_test.py`).

| $m$ | $q_2$ | $q_3$ | incompatible pairs checked | mixing found |
|-----|-------|-------|---------------------------|--------------|
| 4   | 128   | 9     | 5,584                     | 0 |
| 8   | 512   | 9     | 84,448                    | 0 |
| 12  | 128   | 81    | 401,616                   | 0 |
| 16  | 2048  | 9     | 1,216,192                 | 0 |
| 20  | 128   | 9     | 5,584                     | 0 |
| 24  | 512   | 81    | 5,798,880                 | 0 |
| 28  | 128   | 9     | 5,584                     | 0 |

At $m=16$ (new in this wave): Fix mod 2048 has 2048 vectors,
77,852 ordered component pairs, $\Pi$-size distribution
$\{1:48768,\ 2:23424,\ 4:5088,\ 8:572\}$ (no empty $\Pi$);
Fix mod 9 has 9 vectors, 24 ordered pairs, all with
$|\Pi|=2$. Hence, by the reduction theorem, mod-$D$ Lemma Y
holds at each of these $m$ (given the component lemmas, which
the same enumerations verify: $\Pi_q\neq\emptyset$ for every
same-multiset component pair).

For $t=2$ ($m\equiv2\pmod4$) mixing is vacuous: $3\nmid D_m$,
so only the 2-primary component matters. For $t=1$ (odd $m$)
Lemma Y is trivial (single class, $Y$ = total sum).

## 4. Exact level (carries): no counterexample found, gap remains open in general

Mod-$D$ Lemma Y does not by itself imply exact Lemma Y.
Writing $Y'-\pi(Y)=D\cdot d$ with $d_r\in\{-(k-1),\dots,k-1\}$,
$k=m/t$, $\sum d_r=0$, the carry vector $d$ is a priori free.
Tested exact classes (script `methods/pmix_exact_general.py`):

- $m=12$, other components zero (CRT coefficients
  $c_2=588305025$, $c_3=1347068800$ for moduli 128, 81):
  284,960 common-$\sigma$ pairs, **0 exact failures**.
- $m=8$, other components zero: 47,888 common-$\sigma$ pairs,
  **0 exact failures** (global $m=8$ exact Lemma Y is already
  known by full enumeration).
- $m=12$, glued-fiber permutation
  $\tau=(10,4,11,6,1,8,3,9,5,0,7,2)$ (script
  `methods/pmix_glued_tau_exhaust.py`): the $\tau$-stable
  component sets have sizes $8,3,5,7,1$ for
  $q=128,81,25,49,121$; all $840$ CRT combinations checked,
  **0 exact failures**.

Other component pair counts at $m=12$ (for reference):
$q=25$: 120 ordered pairs; $q=49$: 186; $q=121$: 1320.
No exact counterexample was found anywhere. The exact carry
step (proving $d=0$ in general, e.g. via the $W$-formulation
$H_t d=\Delta W$ with $W$ bounded) is **not** proved here;
it is the remaining subgap Pcarry.

## 5. A general mechanism: 2-component $P$-periodicity

Let $P=2^{v_2(m)}$ (largest power of 2 dividing $m$).
Claim: every $z\in\mathrm{Fix}_m$ reduced mod $2^a$
($a=v_2(D_m)$) is $P$-periodic.

*Proof sketch.* $v_2(D_m)$ depends only on $v_2(m)$
(data: $a=2v_2(m)+3$ for $4\mid m$; $a=5$ for $v_2=1$;
$a=2$ for odd $m$), hence $v_2(D_P)=a$ as well.
$\ker(M^P-I\bmod 2^a)$ has size $2^a$ by the SNF argument
($d_1d_2=D_P$, $v_2(d_1)+v_2(d_2)=a$, both $\le a$), which
equals $|\mathrm{Fix}\bmod 2^a|$. Since $P\mid m$,
$\ker(M^P-I)\subseteq\ker(M^m-I)$, so equality holds:
$\mathrm{Fix}\bmod 2^a$ = $P$-periodic recurrence sequences
mod $2^a$. The $v_2(D_m)$-depends-only-on-$v_2(m)$ step is
the usual LTE phenomenon in $\mathbb Z[\sqrt2]$ and is the
one analytic input still to be written out in full.

Period data confirms it (periods are minimal cyclic periods):

- $m=16$, $q=2048$, 2048 vectors: $\{16:1536,\ 8:384,\ 4:96,\ 2:28,\ 1:4\}$;
- $m=24$, $q=512$, 512 vectors: $\{8:384,\ 4:96,\ 2:28,\ 1:4\}$;
- $m=12$, $q=128$, 128 vectors: $\{4:96,\ 2:28,\ 1:4\}$;
- $m=8$, $q=512$, 512 vectors: $\{8:384,\ 4:96,\ 2:28,\ 1:4\}$.

In particular $Y_r\bmod 2^a = (m/P)\cdot(\text{pattern class sum})$,
and $m/P$ is odd, hence a unit mod $2^a$ — so $Y\bmod 2^a$
determines the pattern class sums and vice versa.

*Intended dihedral argument (not yet complete).* If $z_2$ is
$P$-periodic with pattern $p$ and $\sigma(z_2)=z_2'$ is also
$P$-periodic, then in the generic case (pattern values
distinct) $\sigma$ induces a well-defined $\tau$ on
$\mathbb Z/P$ with $p'=p\circ\tau$; recurrence plus
distinctness forces $\tau(j+1)=\tau(j)\pm1$, i.e. $\tau$ is
dihedral on $\mathbb Z/P$, and since $4\mid P$ its reduction
mod 4 is a dihedral $\pi$ on classes. Then
$\sigma(O_r)=O_{\pi(r)}$ as sets, hence $Y'=\pi(Y)$ exactly,
for *all* components at once. Remaining substeps for a
general proof:

1. **Repeats / stabiliser:** when pattern values repeat,
   $\tau$ is not unique; one must adjust $\sigma$ by the
   stabiliser of $y$ (permuting positions with equal $y$-values)
   to a class-permuting $\sigma$ without changing $y'$.
2. **$P=m$ case** ( $m$ a power of 2): the period lemma is
   vacuous, yet the search at $m=16$ still finds 0 mixing, so
   a different argument is needed there.
3. **Pcarry:** the exact carry step of §4.

## 6. Conclusion

- Pmix is **closed at the mod-$D$ level** for every $t=4$
  case tested ($m=4,8,12,16,20,24,28$) by the reduction
  theorem plus the common-$\sigma$ searches (0 mixing in
  1.2M–5.8M incompatible pairs at the largest cases).
- **No counterexample** (mixed-permutation or exact-carry)
  was found: exact checks pass at $m=8$ and $m=12$ in the
  tested classes, and the glued-$\tau$ exhaustive check
  passes (840/840).
- **Not proved in general:** the dihedral-$\tau$ argument
  (§5) is a promising route with three named subgaps
  (repeats/stabiliser, $P=m$, Pcarry). A single exact
  failure in a future search (e.g. with nonzero other
  components at $m\ge 32$, or at $m=36$ where $q_3=81$ and
  $q_2=128$ combine with a new odd part) would be a
  Lemma Y counterexample and would falsify the route.
