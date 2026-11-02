# Wave 8, task 1 — Lemma Y: proof attempt, not a proof in general

**Verdict: Lemma Y is NOT proved in general by this attempt, and NO
counterexample was found.** What is proved below is the odd-primary part
(up to the mod-3 base case, which is proved by a period-4 classification),
plus a complete componentwise computational verification for all prime
powers dividing $D_m$, $m\le 20$. The exact points where the argument
breaks are §6 (2-primary component) and §7 (CRT mixing / exact-integer
carries). Repository untouched; Lean not built; enumerations are exact
integer arithmetic, i.e. verifier artefacts, not theorems.

## 0. Statement, reconciled

$H_m = 6I-C-C^T$, $(Hy)_i = 6y_i-y_{i-1}-y_{i+1}$ (indices mod $m$),
$D_m = \det H_m = s_m-2$, $s_0=2$, $s_1=6$, $s_{n+1}=6s_n-s_{n-1}$
($s_m = \alpha^m+\beta^m$, $\alpha=3+2\sqrt2$, $\beta=3-2\sqrt2$).
$\mathrm{Fix}_m = \ker(H_m \bmod D_m)$, $y$ lifted to $0\le y_i<D_m$.
$t=\gcd(m,4)$, $O_r=\{i: i\equiv r \pmod t\}$, $Y_r(y)=\sum_{i\in O_r} y_i$
(exact integer sum of lifts). $D_t$ = dihedral permutations of
$\mathbb Z/t$ ($r\mapsto r+b$, $r\mapsto -r+b$).

**Lemma Y.** If $y,y'\in\mathrm{Fix}_m$ and $\mathrm{sorted}(y')=
\mathrm{sorted}(y)$, then $Y(y')\in D_t\cdot Y(y)$.

Equivalently, with $w=Hy/D_m\in\{-1,\dots,5\}^m$ and
$W_r=\sum_{i\in O_r} w_i$: $H_t Y = D_m W$, where $H_t$ is the $t\times t$
matrix $6I-\mathrm{shift}-\mathrm{shift}^{-1}$ ($t=2$: off-diagonal $-2$;
$t=1$: $[4]$), so $Y\leftrightarrow W$ is a $D_t$-equivariant bijection
over $\mathbb Q$ (eigenvalues $D_m/4, D_m/6, D_m/8, D_m/6$ for $t=4$). Lemma Y
for $Y$ is equivalent to Lemma Y for $W$.

## 1. The suggested CRT route, corrected: Fix mod q is NOT cyclic

Let $M=\begin{pmatrix}6&-1\\1&0\end{pmatrix}$, so a recurrence sequence
is determined by $(y_0,y_1)$ and $y\in\mathrm{Fix}_m\bmod q$ iff
$(M^m-I)(y_0,y_1)^T\equiv 0 \pmod q$. Smith form of $M^m-I$ is
$\mathrm{diag}(d_1,d_2)$, $d_1d_2=D_m$ (e.g. $m=6$: $(70,560)$;
$m=8$: $(408,3264)$; $m=12$: $(13860,110880)$). For $q=p^e\parallel D_m$,
with $a=v_p(d_1)$ (so $v_p(d_2)=e-a$), $\ker(M^m-I\bmod q)$ has size $q$
but structure $\mathbb Z/p^{e-a}\times\mathbb Z/p^a$, NOT cyclic in
general: max scalar-orbit sizes observed are $q/p^{\min(a,e-a)}$
(e.g. $m=8,q=512$: $64$; $m=6,q=25$: $5$; $m=4,q=128$: $32$).
Hence "Fix mod q is cyclic", as suggested in the wave-7 note, is FALSE
as stated; the correct parametrisation is the SNF one:
$(y_0,y_1)=V(p^{e-a}X',p^aY')$, $X'\in\mathbb Z/p^a$,
$Y'\in\mathbb Z/p^{e-a}$, $V$ unimodular. In particular every
$\mathrm{Fix}\bmod q$ point has all entries divisible by
$p^{\min(a,e-a)}$. This SNF parametrisation is what makes the large-$q$
component tests below feasible (no $q^2$ scan).

## 2. Odd prime powers: the vanishing lemma (PROVED)

Work in $R=\mathbb Z[\sqrt2]$, $R/qR$, $q$ odd. Then $\alpha-\beta=4\sqrt2$
has norm $-32$, a unit mod $q$, hence is a unit in $R/qR$. So every
recurrence sequence mod $q$ has a unique representation
$y_i = A\alpha^i + \bar A\beta^i$, $A\in R/qR$ (conjugate
$\bar A$ because $y_i\in\mathbb Z/q$), and periodicity
$y_{i+m}=y_i$ gives $(\alpha^m-1)A=0$, $(\beta^m-1)\bar A=0$ in $R/qR$
(determinant $\alpha-\beta$ is a unit, so $i=0,1$ suffice).

Class sums: $Y_r = A\alpha^r S_\alpha + \bar A\beta^r S_\beta$ with
$S_\alpha=\sum_{k<m/t}(\alpha^4)^k$ (for $t=2$ the sum has $m/2$ terms,
for $t=1$ it has $m$ terms; in all cases $(\alpha^4-1)S_\alpha$ is a
multiple of $\alpha^m-1$, resp. $(\beta^4-1)S_\beta$ a multiple of
$\beta^m-1$). Hence

$$(\alpha^4-1)Y_r = 0 \quad\text{in } R/qR.$$

Now $\alpha^4-1 = 576+408\sqrt2$, and $1,\sqrt2$ are a free basis of
$R/qR$ over $\mathbb Z/q$, so this gives $576Y_r\equiv 0$ and
$408Y_r\equiv 0 \pmod q$. Since $\gcd(576,408)=24$:

- **$p\nmid 24$ (i.e. $p\ne 2,3$): $Y_r\equiv 0 \pmod q$ for every
  $\mathrm{Fix}\bmod q$ point.** Component Lemma Y mod $q$ is then
  trivial (both sides are the zero vector).
- **$p=3$: $Y_r\equiv 0 \pmod{q/3}$.** Moreover $3\mid D_m$ iff $4\mid m$
  (from $s_m\bmod 3$: $s_m\equiv 0$ iff $m$ odd, $s_m\equiv 2$ iff
  $4\mid m$, $s_m\equiv 1$ iff $m\equiv 2\pmod 4$; $D_m=s_m-2$), so the
  $p=3$ case occurs only for $t=4$.

This explains the component data: for odd $q\ne 3^e$, the only class-sum
vector mod $q$ is $0$ (e.g. $q=25,49,289,841,361$: exactly 1 distinct $Y$);
for $q=3^e$, $Y$ is a multiple of $3^{e-1}$ (e.g. $q=81$: $Y\in 27\cdot
(\mathbb Z/3)^4$, 9 distinct values).

## 3. The mod-3 base case (PROVED by period-4 classification)

For $3\mid D_m$ (hence $4\mid m$), $\mathrm{Fix}\bmod 3$ is all recurrence
sequences mod $3$ (since $M^m\equiv I\pmod 3$): $9$ points. Mod $3$,
$6\equiv 0$, so $y_{i+1}\equiv -y_{i-1}\pmod 3$, i.e. every sequence is
4-periodic: $(y_0,y_1,-y_0,-y_1)$ repeated. Class sums mod $3$ are
$(m/4)\cdot(y_0,y_1,-y_0,-y_1)\pmod 3$ (for $m\equiv 0\pmod{12}$,
$m/4\equiv 0\pmod 3$ and $Y\equiv 0$). Multisets fall into exactly three
types: all zero; one of $(y_0,y_1)$ zero, the other $\ne 0$ (counts
$m/2$ zeros, $m/4$ of each of $\pm a$); both nonzero (counts $m/2$ of
each of $\pm a$). In each type the $Y$ vectors over all $(y_0,y_1)$
form a single $D_4$-orbit (e.g. type "both nonzero":
$(1,1,2,2)$ rotates to $(1,2,2,1),(2,2,1,1),(2,1,1,2)$).
Hence component Lemma Y mod $3$ holds, by classification, not just by
enumeration (the enumeration for $m=4,8,12,16,20,24$ confirms it:
$3$ multisets, $0$ bad, in every case).

## 4. Component verification for all prime powers, $m\le 20$ (NO counterexample)

For every prime power $q\parallel D_m$, $m=4,6,8,10,12,14,16,18,20$,
all $\mathrm{Fix}\bmod q$ points were grouped by multiset, and the
class-sum vector mod $q$ was checked to lie in a single $D_t$-orbit
per multiset. Small $q$ by vectorised kernel enumeration; large $q$
($28561,57121,38809,39601,332929$) by the SNF parametrisation of §1.
Result in every case: **bad multisets $=0$**. Examples: $m=10$,
$q=1681$: $189$ multisets, $0$ bad; $m=16$, $q=332929$: $10693$
multisets, $0$ bad; $m=14$, $q=57121$: $4200$ multisets, $0$ bad.
Scripts: `wave8_lemmaY_explore.py` (+log), `wave8_lemmaY_snf.py` (+log).

Note what this does and does not show: it shows component Lemma Y
mod $q$ (per prime power separately). It does NOT by itself show
global Lemma Y, for the reasons in §§6–7.

## 5. The 2-primary component: structure, but no proof

Here $\alpha-\beta$ has norm $-32\equiv 0\pmod{2^e}$, so §2 fails at
the first step (no $A,\bar A$ representation in $R/2^eR$). What is
known structurally: $Y\bmod 2^a$ ($a=v_2(D_m)$, $q=2^a$) lies in
$\ker(H_t\bmod 2^a)$, whose size is independent of $a$ once $a$ is
large: $H_4$ has SNF $\mathrm{diag}(1,1,12,96)$, so
$|\ker(H_4\bmod 2^a)|=1\cdot1\cdot\gcd(12,2^a)\cdot\gcd(96,2^a)=128$
for $a\ge 7$ (matches: $128$ distinct $Y$ mod $512$ at $m=8$, mod $128$
at $m=12$); $H_2$ has SNF $\mathrm{diag}(2,16)$, so $|\ker|=32$ for
$a\ge 4$ (matches: $32$ distinct $Y$ mod $32$ at $m=6,10$). Thus
$Y\bmod 2^a$ is parametrised by $(x',y')\in\mathbb Z/4\times\mathbb Z/32$
($t=4$) or $\mathbb Z/2\times\mathbb Z/16$ ($t=2$). The unproved step
is: **multiset of a $\mathrm{Fix}\bmod 2^a$ point determines
$(x',y')$ up to $D_t$.** No argument for this was found; it is the
first precise subproblem (P2) left open.

## 6. Exact-integer / CRT-mixing obstruction (the second gap)

Even if component Lemma Y mod $q$ held for every $q$ with a proof,
global Lemma Y (exact integers, not mod $D$) would not follow
automatically, for two distinct reasons:

1. **Per-component permutations can in principle differ.** A global
   fiber mate $y'=\sigma(y)$ ($\sigma\in S_m$, the same $\sigma$ for
   all components, since reduction mod $q$ commutes with permuting
   coordinates) gives, per component, some $\pi_q\in D_t$ with
   $Y'\equiv\pi_q(Y)\pmod q$. Nothing in the component argument forces
   $\pi_q$ to be independent of $q$. For odd $q\ne 3$, $\pi_q$ is
   unconstrained (both sides are $0$); for $q=3^e$ it is constrained
   only mod $3$; the only components that can pin $\pi$ are the
   2-primary one (and, weakly, the 3-primary one). A proof of
   non-mixing must use that $\sigma$ is common to all components —
   i.e. that the subset sums $\sum_{j\in\sigma(O_r)} y_j$ are
   simultaneously $D_t$-related in the 2- and 3-components — and no
   such argument was found. Global exhaustive data ($m\le 8$) show no
   mixing occurs there, but that is evidence, not a proof.
2. **Exact $Y$ vs $Y\bmod D$.** $Y_r$ lies in $[0,\frac mt D)$, so
   $Y\bmod D$ determines $Y$ only up to $\lfloor Y_r/D\rfloor\in
   [0,\frac mt)$. From §2, $Y_r = M k_r$ with
   $M=D_{\mathrm{odd}}/3^\varepsilon$ ($\varepsilon=1$ if $t=4,3\mid D$,
   else $0$) and $k_r < \frac mt\cdot 2^a\cdot 3^\varepsilon$; $k_r$
   mod $2^a3^\varepsilon$ is determined by $Y\bmod D$, but the quotient
   $k_r$ by that modulus (bounded by $\frac mt$) is not. Controlling
   this quotient is the carry problem: CRT lifts $y_i$ involve
   $\lfloor(\alpha u_i+\beta v_i)/D\rfloor$ terms that depend on the
   joint $(u_i,v_i)$ pairs, not on separate component multisets.

## 7. What would close it

- (P2) A 2-adic proof that multiset determines the SNF parameters
  $(x',y')$ of $Y\bmod 2^a$ up to $D_t$ (e.g. via 2-adic digit/Hensel
  analysis of the recurrence, or via the $W$-formulation: $W_r$ are
  small integers, and $Y$ is $D\cdot\mathrm{adj}(H_t)W/\det(H_t)$).
- (P3) A non-mixing argument: for a common $\sigma$, the 2- and
  3-component permutations $\pi_2,\pi_3$ coincide (or $Y$ is fixed by
  their difference), plus carry control for $\lfloor Y_r/D\rfloor$.
- (P3') The $p=3$, $e>1$ digit induction: reduce component Lemma Y
  mod $3^e$ to the mod-$3$ classification of §3 by SNF scaling
  (§1) plus a Hensel digit argument; sketched in §2–§3 but not
  written out in full (the step "multiset mod $3^e$ determines the
  top digit class-sum up to $D_t$" is not proved here).

## 8. Files

- This note: `methods/wave8_lemmaY_proof_attempt.md`
- Component tests: `methods/wave8_lemmaY_explore.py`,
  `methods/wave8_lemmaY_explore.log`,
  `methods/wave8_lemmaY_snf.py`, `methods/wave8_lemmaY_snf.log`
- Prior note (statement, class-sum identity, verification table):
  `methods/pair_sorted_identity_note.md`
