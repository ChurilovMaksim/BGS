# Wave 12, task 1 — G1: odd prime-power lift for the exact per-class lemma

## Verdict (honest)

**No counterexample found. G1 is reduced to two named lemmas (L6, L7 below);
it is not yet a complete proof.** The reduction itself — scaling, LTE,
G0/H0 identity, Frobenius, and the p-group orbit being a coset — is proved
below. The linear case $2k\ge f$ (in particular every $f=2$, i.e.
$v_p(D_m)=4$) is complete modulo L6. The general case needs L7 as well.
Nothing here is a Lean formalisation; the repository was not touched.

## 0. Statement

Let $p$ be odd, $p\mid D_m$, $t=\gcd(m,4)$, $R=\mathbf Z[\sqrt2]$,
$\alpha=3+2\sqrt2$, $\beta=\alpha^{-1}$, $\operatorname{Tr}(x)=x+\bar x$.
A recurrence sequence mod $P$ is $y_i=\operatorname{Tr}(A\alpha^i)$,
$A\in R/P$. Its per-class multisets are
$\{y_i : i\equiv r\pmod t\}$, $r\bmod t$.

**G1.** For $q=p^{2f}\parallel D_m$ ($f=v_p(D_m)/2$), if
$y,y'\in\mathrm{Fix}_m\bmod q$ have the same sorted multiset mod $q$,
then their per-class multisets are $D_t$-related mod $q$.

By Lemma 1 below this is equivalent to:

**G1'.** For every odd $p\mid D_m$, with $f=v_p(D_m)/2$, if
$y,y'$ are *arbitrary* recurrence sequences mod $p^f$ (all $A\in R/p^f$)
with the same sorted multiset mod $p^f$, then their per-class
multisets are $D_t$-related mod $p^f$.

Note the quantifier: G1' is about all sequences mod $p^f$, not only
$\mathrm{Fix}$ sequences mod $p^f$ (they coincide here, since
$\alpha^m\equiv1\pmod{p^f}$, see Lemma 1). The mod-$p$ case $f=1$ is
wave 11, task 2. The new content is $f\ge2$.

## 1. Scaling — proved

**Lemma 1.** Let $e_0=v_p(D_m)$. Then $e_0$ is even, $e_0=2f$ with
$f\ge1$, and $\delta:=\alpha^m-1$ satisfies
$v_{\mathfrak p}(\delta)=f$ for every ${\mathfrak p}\mid p$ (with
$v_{\mathfrak p}$ normalised by $v_{\mathfrak p}(p)=1$ in the split case
per component, and $v_{\mathfrak p}$ the DVR valuation in the inert case).
Consequently, for every $e\ge1$,
$$\mathrm{Fix}_m\bmod p^e
  =\{\,p^{\max(0,e-f)}\cdot z : z\text{ recurrence mod }p^{\min(e,f)}\,\},$$
in particular $\mathrm{Fix}_m\bmod p^{2f}=p^f\cdot\{\text{all sequences
mod }p^f\}$.

*Proof.* $\bar\delta=\beta^m-1=-\beta^m\delta$, so
$N(\delta)=\delta\bar\delta=-\beta^m\delta^2$, while
$N(\delta)=2-(\alpha^m+\beta^m)=-D_m$. Hence $\delta^2=\beta^m D_m$,
so $(\delta)^2=(D_m)$ as ideals of $R$ ( $\beta^m$ is a unit). Taking
${\mathfrak p}$-valuations, $v_{\mathfrak p}(D_m)=2v_{\mathfrak p}(\delta)$
for every ${\mathfrak p}\mid p$. Since $D_m\in\mathbf Z$ and $p$ is
unramified, $v_{\mathfrak p}(D_m)=v_p(D_m)=e_0$, so $e_0$ is even and
$v_{\mathfrak p}(\delta)=e_0/2=:f$. Localising at $p$, $(\delta)=(p^f)$,
so $(\alpha^m-1)A\equiv0\pmod{p^e}$ iff $p^{e-f}\mid A$ (for $e>f$),
and is automatic for $e\le f$. The periodicity criterion
$(\alpha^m-1)A=0$ (wave 11, Lemma 2, valid mod $p^e$ since
$\alpha-\beta$ has norm $-32$, a unit mod $p^e$) gives the formula. ∎

Henceforth fix $f$, $P=p^f$, and work with all sequences mod $P$.

## 2. Orders and LTE — proved up to standard DVR LTE

Let $L_0$ = order of $\alpha$ mod $p$ (so $L_0\mid m$, $L_0\mid p-1$ split,
$L_0\mid p+1$ inert, $\gcd(L_0,p)=1$). Let
$k=v_{\mathfrak p}(\alpha^{L_0}-1)\ge1$ (the same for all
${\mathfrak p}\mid p$, since $\overline{\alpha^{L_0}-1}
=-\beta^{L_0}(\alpha^{L_0}-1)$). Let $s=v_p(m/L_0)$.

**Lemma 2.** $f=k+s$. The order of $\alpha$ mod $P$ is $L=L_0p^s$,
$m/L$ is coprime to $p$, and $\gamma:=\alpha^{L_0}=1+\varepsilon$ with
$\varepsilon=p^ku$, $u$ a unit mod $p$ (i.e. $u\notin{\mathfrak p}$
for all ${\mathfrak p}\mid p$).

*Proof.* DVR LTE for odd $p$: if $x\equiv1\pmod{\mathfrak p}$ then
$v_{\mathfrak p}(x^n-1)=v_{\mathfrak p}(x-1)+v_p(n)$. Apply with
$x=\alpha^{L_0}$, $n=m/L_0$: $v_{\mathfrak p}(\alpha^m-1)=k+s$,
but this equals $f$ by Lemma 1. The order claim follows:
$\alpha^{L_0}$ has order $p^{f-k}=p^s$ mod $P$ (again by LTE:
$(\alpha^{L_0})^{p^{s-1}}\not\equiv1\pmod{p^f}$,
$(\alpha^{L_0})^{p^s}\equiv1$), and $\alpha$ has order $L_0p^s$
since its mod-$p$ order is $L_0$ and $L_0$ is coprime to $p$.
$m/L=(m/L_0)/p^s$ is coprime to $p$ by definition of $s$. ∎

Write $G=\langle\alpha\rangle\bmod P$ ($|G|=L$),
$G_0=\langle\alpha^{p^s}\rangle$ ($|G_0|=L_0$),
$G_p=\langle\gamma\rangle$ ($|G_p|=p^s$), so $G\cong G_0\times G_p$.
Let $g=\gcd(L,t)=\gcd(L_0,t)$ (since $\gcd(t,p)=1$),
$H=\langle\alpha^t\rangle$ ($|H|=L/g$),
$H_0=\langle\alpha^{tp^s}\rangle$ ($|H_0|=L_0/g$),
so $H\cong H_0\times G_p$ (the $p$-part of $H$ is all of $G_p$,
since $t$ is coprime to $p$). Classes $r\bmod t$ depend only on
$r\bmod g$ for the value multisets (wave 11, §7 / §2 above):
$\alpha^rH$ depends only on $r\bmod g$, and the $t$-tuple of
per-class multisets is the $g$-tuple repeated $t/g$ times, so it
suffices to prove the $g$-tuple is $D_g$-related.

## 3. The coprime-to-$p$ part — proved

**Lemma 3.** Let $G_0$ be as above. Then
$\prod_{z\in G_0}(T-z)=T^{L_0}-1$ in $(R/P)[T]$,
$\sum_{z\in G_0}z=0$, and differences $z_1-z_2$ ($z_1\ne z_2$) are
units mod $P$. The same holds for $H_0$ with $T^{|H_0|}-1$.

*Proof.* Each $z\in G_0$ satisfies $z^{L_0}=1$, so $(T-z)\mid T^{L_0}-1$
in any commutative ring. Distinct $z$'s are distinct mod $p$ (order
$L_0$ is preserved mod $p$), so $z_1-z_2\not\equiv0\pmod{\mathfrak p}$
for all ${\mathfrak p}\mid p$, i.e. it is a unit mod $P$; hence the
linear factors are comaximal and their product, monic of degree $L_0$,
equals $T^{L_0}-1$. The sum vanishes since multiplication by a
generator permutes $G_0$ and the generator minus $1$ is a unit mod $p$
(same argument as $\alpha^{p^s}-1$ being a unit: it is $\ne0$ mod $p$). ∎

Consequence used below: for $|H_0|$ (coprime to $p$), the polynomial
identity of wave 11, Step 1,
$$\prod_{z\in H_0}(X-\operatorname{Tr}(Cz))
  = V_{|H_0|}(X,N(C))-\operatorname{Tr}(C^{|H_0|})\quad(\text{up to sign }-1),$$
holds over $R/P$ (same resultant proof as mod $p$, using Lemma 3
in place of the field factorisation). The point where the full-$G$
identity *fails* is precisely the $p$-part: for $G_p$,
$\prod_{z\in G_p}(T-z)\ne T^{p^s}-1$ mod $P$ (e.g. $p=3$, $H$ of order 3
mod 9: the three elements are $1,1+3\sqrt2,1+6\sqrt2$, whose product
polynomial is $(T-1)^3\ne T^3-1$). All of §4–§5 is the replacement
for that failed identity.

## 4. Frobenius — proved

**Lemma 4.** Let $X\in R/P$. Then $X^{p^s}\bmod P$ depends only on
$X\bmod p^k$. Conversely, $X^{p^s}\bmod P$ determines $X\bmod p^k$
at every prime ${\mathfrak p}\mid p$ where $X$ is a unit; where
$X\in{\mathfrak p}$, one has $X^{p^s}\equiv0\pmod{{\mathfrak p}^f}$
and no information about $X\bmod{\mathfrak p}^k$ is retained.

*Proof.* If $X'=X+p^kE$, then
$(X')^{p^s}-X^{p^s}=\sum_{j\ge1}\binom{p^s}{j}X^{p^s-j}(p^kE)^j$.
$v_p\binom{p^s}{j}\ge s-v_p(j)$, so the $j$-th term has valuation
$\ge s-v_p(j)+jk$. For $j=1$ this is $s+k=f$. For $j\ge2$,
$(j-1)k\ge v_p(j)$ (as $p^{v_p(j)}\le j\le 1+(j-1)\le1+(j-1)k$ for
$p\ge3$, $k\ge1$), so the valuation is $\ge s+k=f$. Hence the
difference is $0\bmod P$. For determination at a unit prime: if
$X'\equiv X\pmod{{\mathfrak p}^t}$ with $t<k$ and $X$ a unit at
${\mathfrak p}$, the $j=1$ term has valuation exactly $s+t<f$ at
${\mathfrak p}$, so the powers differ. If $X\in{\mathfrak p}$,
then $v_{\mathfrak p}(X^{p^s})=p^s\cdot v_{\mathfrak p}(X)\ge p^s\ge
s+k=f$ (since $p^s\ge s+k$ for $p\ge3$), so $X^{p^s}\equiv0$ and
$X\bmod{\mathfrak p}^k$ is lost — e.g. $p=3$, $k=2$, $s=1$:
$3^3\equiv6^3\equiv0\pmod{27}$ while $3\not\equiv6\pmod9$.
That loss is exactly the divisible case handled by induction in L6. ∎

Applied with $D=A^{|H_0|}$: $B:=A^{|H|}=D^{p^s}$ (since
$|H|=|H_0|p^s$). So $B\bmod P$ is determined by $D\bmod p^k$,
and $D\bmod p^k$ is determined by $B$ at unit primes (divisible
primes are the induction case). In particular the global
$B$-invariant below lives at modulus $p^k$, not $p^f$ — this is why
$N(A)$ itself is *not* determined mod $P$ (numerically: $m=12$,
$P=9$, one fibre has $N=2,5,8\bmod9$, all $\equiv2\bmod3$; $m=36$,
$P=27$, one fibre has $N\equiv2\bmod3$ arbitrary mod $27$), while
$N(B)$ and $\operatorname{Tr}(B^g)$ *are* constant on fibres
(verified in §7).

## 5. The $p$-group orbit is a coset — proved (sketch of the key step)

Fix $C\in R/P$ and consider the $G_p$-orbit
$F(C)=\{\operatorname{Tr}(C\gamma^j):j\in\mathbf Z/p^s\}$.

**Lemma 5.** $F(C)$ is a coset: there are $v\in[0,s]$ and
$a\in\mathbf Z/P$ with
$$F(C)=\{\,a+p^{k+v}t : t\in\mathbf Z/p^{s-v}\,\},$$
each value occurring exactly $p^v$ times, where
$v=v_p(\operatorname{Tr}(Cu))$ (with $v=s$ meaning $F(C)$ is a singleton,
$\operatorname{Tr}(Cu)\equiv0\pmod{p^s}$).

*Proof sketch.* Write $\gamma^j-1=\varepsilon\cdot\phi(j)$ with
$\phi(j)=((1+\varepsilon)^j-1)/\varepsilon
=\sum_{t\ge1}\binom{j}{t}\varepsilon^{t-1}$.
Then $\operatorname{Tr}(C\gamma^j)=\operatorname{Tr}(C)
+p^k\operatorname{Tr}(Cu\,\phi(j))$.
Claim: $\phi:\mathbf Z/p^s\to R/p^s$ (more precisely its trace
against $Cu$) is bijective onto residues in the following sense:
$\phi(j)\equiv j\pmod p$ (since $\varepsilon\equiv0\pmod p$ kills
$t\ge2$ terms mod $p$), and $\phi$ is a $p$-adic analytic function
with unit derivative mod $p$; by induction on $s$ (if
$\phi(j_1)\equiv\phi(j_2)\pmod{p^{s}}$, first $j_1\equiv j_2\pmod p$,
then write $j_2=j_1+pt$ and use that $\phi(j+pt)-\phi(j)$ is
divisible by $pt$ — true for Mahler basis functions $\binom{j}{t}$),
$\phi$ induces a bijection $\mathbf Z/p^s\to\mathbf Z/p^s$ after
tracing against a unit. Hence as $j$ varies,
$\operatorname{Tr}(Cu\,\phi(j))$ runs over all multiples of
$p^v$ mod $p^s$, each $p^v$ times, where $v=v_p(\operatorname{Tr}(Cu))$.
Multiplying by $p^k$ and adding $\operatorname{Tr}(C)$ gives the
coset. ∎

*Remark.* Lemma 5 does not need $2k\ge f$ (linearity); the quadratic
and higher Taylor terms are absorbed into $\phi$. The linear case
$2k\ge f$ is the special case $\phi(j)\equiv j\pmod{p^s}$.

Corollary for per-class multisets: with $C_{r,z}=A\alpha^r z$
($r\bmod g$, $z\in H_0$), the per-class multiset for $g$-class $r$ is
(up to the common repetition factor $(m/t)/|H|$)
$$\bigcup_{z\in H_0} F(C_{r,z}),$$
each $F(C_{r,z})$ a coset as in Lemma 5, lying in the residue class
$\operatorname{Tr}(C_{r,z})\bmod p^k$.

## 6. The two remaining lemmas

**Lemma 6 (H0-orbit rigidity — SKETCHED, not fully proved).**
Let $C,C'\in R/P$ with $C\not\equiv0\pmod p$ (i.e. $C$ not divisible
by $p$ in $R$). If $C,C'$ have the same $H_0$-orbit multiset
$\{\operatorname{Tr}(Cz):z\in H_0\}$ mod $P$, then
$C'\equiv Cz$ or $\bar Cz\pmod P$ for some $z\in H_0$.
*Sketch.* Induction on $f$. Mod $p$ this is wave 11, Step 1–2 for
$H_0$ (order coprime to $p$; norm-1 $|H_0|$-th roots of unity in
$R/p$ form the unique subgroup $H_0$ of the cyclic norm-1 group).
For the step $f-1\to f$: by induction $C'\equiv Cz_0$ or
$\bar Cz_0\pmod{p^{f-1}}$; normalise to $C'=C+p^{f-1}E$.
Power sums over the orbit give, for $r=2$ (using Lemma 3 orthogonality
and $|H_0|\nmid2$ unless $|H_0|\le2$, handled separately),
$\operatorname{Tr}(C\bar E)\equiv0\pmod p$, i.e. $E/C$ is purely
imaginary mod $p$, $E\equiv b\sqrt2\,C$. Then for a conjugate pair
$w,\bar w$ in the orbit ($w=Cz$, $\bar w=Cz'$ with $z'\ne z$),
the two orbit values are both $2\Re w$ mod $p^{f-1}$, and after the
digit shift they become $2\Re w\pm p^{f-1}\cdot4by$ ($w=x+y\sqrt2$);
equality of multisets forces $by\equiv0\pmod p$, and some pair has
$y\not\equiv0\pmod p$ unless every $w$ is real mod $p$ (impossible
for $|H_0|>2$ with $C$ a unit; the $|H_0|\le2$ and real cases are
checked directly). If instead the orbit values are distinct mod $p$,
fibres mod $p^{f-1}$ are singletons and the digit shift must vanish
for each $z$ individually. **Gap in this sketch:** the case where
$C z$ is real mod $p$ for some $z$ (discriminant divisible by $p$)
makes trace fibres larger than pairs; that subcase is not written
out here, though no counterexample occurs in §7.
*Divisible case:* if $p\mid C$ in $R$, write $C=pC_1$; the orbit is
$p$ times the orbit of $C_1$ mod $p^{f-1}$, and induction on $f$
applies. This is exactly why $(N,C^{|H|})$ fails to determine the
$H$-orbit only for $p\mid C$ (see §7): those are the induction cases,
not counterexamples to G1.

**Lemma 7 (coset inversion — SKETCHED).** Let $S_c$ be the global
multiset restricted to values $\equiv c\pmod{p^k}$. Then $S_c$
determines, up to permutation of $(r,z)$, the cosets $F(C_{r,z})$
with $\operatorname{Tr}(C_{r,z})\equiv c\pmod{p^k}$.
*Sketch.* By Lemma 5 each $F$ is a coset of $p^{k+v}\mathbf Z$ with
repetition $p^v$. In the discriminant-unit case, $H_0$-orbit trace
fibres mod $p^k$ have size $\le2$ (conjugate pairs), so the numbers
$n_{v,a}$ of cosets of each step and residue satisfy
$n_{v,a}<p$ for the relevant $v$, and Möbius inversion over the
coset lattice (processing $v$ from $s$ downwards, using that a
coset of step $p^{k+v}$ contributes $p^v$ to each of its values)
recovers them. The real/discriminant-divisible case is the same gap
as in Lemma 6. **This lemma is the precise point where the global
multiset is converted into per-class data; it is stated, not proved,
here.**

## 7. Theorem (conditional) and numerical verification

**Theorem (conditional on L6, L7).** G1' holds, hence G1 holds.

*Proof sketch.* Let $y,y'$ have the same global multiset mod $P$.
Reducing mod $p^k$, their values are the $G_0$-orbit of $A\bmod p^k$
($\gamma\equiv1\pmod{p^k}$), so by L6 applied to $G_0$ (L6 is stated
for $H_0$ but its proof uses only that the group order is coprime
to $p$, so it applies verbatim to $G_0$),
$A'\equiv A\cdot(\text{$G_0$-element})$ or its conjugate
mod $p^k$; $G_0$-action shifts indices by multiples of $p^s$, which
permute classes mod $t$ by shifts ( $p^s$ is a unit mod $t$), and
conjugation gives reflection, so per-class multisets mod $p^k$ are
$D_t$-related. For the full modulus: by L7, the global multiset
determines the cosets $F(C_{r,z})$ up to permutation of $(r,z)$;
each $F(C_{r,z})$ is the $p$-part of the per-class multiset for
$g$-class $r$, and permuting $(r,z)$ by the $G_0$-action found mod
$p^k$ permutes $g$-classes by $D_g$, hence $t$-classes by $D_t$
(§2). The divisible-$p$ case ($p\mid A$) follows by induction on
$f$ (divide by $p$), as in L6. ∎

*Numerical verification (exact arithmetic, all 0 failures):*

| case | modulus | $t$ | split/inert | groups | bad |
|---|---|---|---|---|---|
| $m=12$ | $9$ ($f=2$) | 4 | inert ($p=3$) | 7 | 0 |
| $m=36$ | $27$ ($f=3$) | 4 | inert ($p=3$) | 17 | 0 |
| $m=30$ | $25$ ($f=2$) | 2 | inert ($p=5$) | 17 | 0 |
| $m=42$ | $49$ ($f=2$) | 2 | split ($p=7$) | 59 | 0 |
| $m=14$ | $169$ ($f=2$) | 2 | inert ($p=13$) | 1105 | 0 |

Scripts: `wave12_G1_explore.py` (per-class check),
`wave12_G1_Bcheck.py` / `wave12_G1_Ball.py` (the $B$-invariant:
$B=A^{|H|}$ is $D$-related within every global fibre in all cases
above, including $P=81$ ($m=12$, $2995$ groups) and $P=169$;
$N(B)$ and $\operatorname{Tr}(B^g)$ are constant on fibres).
The only failure of "$(N,C^{|H|})$ determines the $H$-orbit" occurs
for $p\mid C$ (e.g. $m=12$, $P=9$: key $(N,C^{|H|})=(0,0)$ with orbits
$(0,0,0)$, $(6,6,6)$, $(3,3,3)$ for $C$ divisible by $3$), which is
the induction case of L6, not a counterexample to G1.

## 8. What remains, precisely

1. **L6, discriminant-divisible subcase:** $Cz$ real mod $p$ for some
   $z\in H_0$ (trace fibres larger than pairs). Prove the digit
   argument there, or find the (numerically absent) counterexample.
2. **L7 in full:** coset inversion when $H_0$-orbit trace fibres
   collide beyond pairs; same subcase as (1) in practice.
3. After (1)–(2), G1 is proved (as a mathematical argument, not yet
   Lean). The remaining gaps for the full exact per-class lemma are
   then only G2 (2-primary) and G3 (common $\pi$ across components);
   note wave 11 task 3 already gives $\pi_2=\pi_3$ compatibility at
   mod-$D$ level modulo Lemma S, and wave 11 task 1 gives the
   2-primary pattern lemma, so G2/G3 are now the bottleneck, not G1.
4. Suggested next step: attack L6/L7 subcase (1) directly — enumerate
   the real-$Cz$ configurations at $f=2,3$ (they occur, e.g. $C$ real
   mod $p$) and check whether the digit argument closes there by the
   same pair reasoning applied to the $p$-group cosets of §5.
