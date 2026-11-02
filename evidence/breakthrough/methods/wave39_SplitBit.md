# Wave 39, task 3: Split Bit Lemma — proved modulo exactly one statement

## Statement

Level $j\ge3$: $Q=2^{2j+3}$, $N=2^j$. $y$ a kernel sequence mod $Q$
($N$-periodic, $y_{i+1}=6y_i-y_{i-1}$) with minimal period $p$,
$8\le p\mid N$. Half-period defect: $y_{i+p/2}-y_i=(Q/2)\nu_{i\bmod2}$
for $\nu=(\nu_0,\nu_1)\in(\mathbf Z/2)^2$ (Lemma 1 below).
**Split Bit Lemma:** split fiber $\implies \nu=(1,1)$; i.e. if
$\nu\ne(1,1)$ then the fiber of $y$ is a single $\Gamma$-orbit.
Result: proved modulo exactly one named statement (Gap G, §6).
All other ingredients are proved below; the base case is a finite check.

## Lemma 1 (ν)

$M=\bigl(\begin{smallmatrix}6&-1\\1&0\end{smallmatrix}\bigr)$ acts on
$M$-seeds $(y_1,y_0)$ by $M^i(y_1,y_0)=(y_{i+1},y_i)$.
$M^4\equiv I\pmod4$, so for $p\ge8$, $M^{p/2}\equiv I\pmod4$ and
$M^{p/2}+I=2L$, $L\equiv I\pmod2$, $\det L$ odd. From
$(M^{p/2}-I)(M^{p/2}+I)s=(M^p-I)s=0$ mod $Q$ get
$(M^{p/2}-I)s=(Q/2)\nu$, unique $\nu$. $\nu\ne(0,0)$: else
$M^{p/2}s=s$, period divides $p/2$. Shift swaps $\nu_0\leftrightarrow
\nu_1$; reversal preserves $\nu$ ($-i\equiv i\pmod2$).
Hence $\nu=(1,1)$ is $\Gamma$-invariant; $(1,0)\leftrightarrow(0,1)$
under shift. For $\nu=(1,0)$: even positions pair via half-shift,
so the even sub-multiset $E$ is $Q/2$-symmetric; for $\nu=(0,1)$,
the odd sub-multiset $O$ is symmetric.

## Lemma 2 (quarter defect; reduction halves period exactly)

Let $\bar y=y\bmod(Q/2)$, $p\ge8$. Then $\bar y$ has minimal period
exactly $p/2$, and $\bar\nu=\nu$ ($p\ge16$) or $\bar\nu=\mathrm{swap}(\nu)$
($p=8$), where $\bar\nu$ is $\bar y$'s invariant w.r.t. $Q/2$.
Proof. $w=(M^{p/4}-I)s$ satisfies $(M^{p/4}+I)w=(Q/2)\nu$.
For $p\ge16$, $4\mid p/4$, so $M^{p/4}\equiv I\pmod4$,
$M^{p/4}+I=2L'$, $L'\equiv I\pmod2$, giving
$y_{i+p/4}\equiv y_i+(Q/4)\nu_{i\bmod2}\pmod{Q/2}$.
For $p=8$, $M^2+I=2L'$, $L'\equiv\mathrm{swap}\pmod2$, giving the same
formula with $\nu$ swapped. Since $\nu\ne(0,0)$, $\bar y$ cannot have
period dividing $p/4$, so its period is exactly $p/2$; reading the
formula at $i=0,1$ gives $\bar\nu$.
Verified exactly at $m=32$: 8064 points, 0 bad
(`wave39_splitbit_nubar.py`: 7680 with $\bar\nu=\nu$, 384 with swap).

## Lemma 3 (lifts are exactly the 4 flips)

Let $z\equiv y\pmod{Q/2}$ be kernel mod $Q$. Write $z_i=y_i+(Q/2)b_i$.
The recurrence mod $Q$ gives $b_{i+1}-6b_i+b_{i-1}\equiv0\pmod2$,
i.e. $b_{i+1}\equiv b_{i-1}\pmod2$: $b$ is 2-periodic. So the lifts of
$\bar y$ are exactly $y$, $\Psi y$ (even-flip, $+Q/2$ on even $i$),
$\Phi y$ (odd-flip), $\Psi\Phi y$ (both-flip).
Verified at $m=32$: lift-set $=4$ flips for all $p\ge8$ points.

## Lemma 4 (flip analysis)

For $\nu=(1,0)$: $\Psi y=S^{p/2}y\in\Gamma y$ (even-flip $=$ half-shift,
since $\nu_{i\bmod2}=[i\text{ even}]$). $\Phi y\in F(y)\iff O$ is
$Q/2$-symmetric: indeed
$\mathrm{mult}_{E\cup(O+Q/2)}(v)-\mathrm{mult}_{E\cup O}(v)
=\mathrm{mult}_O(v-Q/2)-\mathrm{mult}_O(v)$, so equality for all $v$
$\iff O$ invariant under $+Q/2$. $\Psi\Phi y\in F(y)\iff S$ is
$Q/2$-symmetric; but $S$ has asymmetry $a=a_O$ (as $E$ is symmetric),
so this follows from $O$ symmetric. Symmetric statements for
$\nu=(0,1)$ (roles of $E,O$ and $\Phi,\Psi$ exchanged; shift by 1
reduces $(0,1)$ to $(1,0)$).

## Lemma 5 (base case, period 4: finite check, no $\nu$ condition needed)

Period-dividing-4 kernel sequences mod $2^K$: $(M^4-I)(y_1,y_0)=0$
gives, dividing by 4, $297y_1-51y_0\equiv0$,
$51y_1-9y_0\equiv0\pmod{2^{K-2}}$, hence $y_0=2^{K-5}U$,
$U\in\mathbf Z/32$, $y_1=2^{K-5}(a+8t)$, $a=(3U)\bmod8$, $t\in\mathbf Z/4$,
and reduced tuple
$(U,\ a+8t,\ 6a+16t-U,\ 3a+24t-6U)\bmod32$.
The reduction is $K$-independent and preserves multisets and
$\Gamma$-orbits. Exhaustive check over all 128 $(U,t)$:
39 reduced fibers, **all single orbits, 0 violations**
(`wave39_splitbit_basecase.py`; period breakdown 96/28/4 matches
the $m=32$ census). So period-4 fibers are never split, for any $\nu$.

## Theorem (induction on $p$, modulo Gap G)

Induction on $p$ (base $p=4$ by Lemma 5). Let $p\ge8$, $\nu_y\ne(1,1)$,
$z\in F(y)$. Reduce mod $Q/2$: $\bar y,\bar z$ have the same multiset
and $\bar\nu\ne(1,1)$ (Lemma 2, $(1,1)$ swap-invariant), so by the
induction hypothesis $\bar z\in\Gamma\bar y$. Replacing $z$ by a
$\Gamma$-translate, $\bar z=\bar y$; by Lemma 3,
$z\in\{y,\Phi y,\Psi y,\Psi\Phi y\}$. For $\nu=(1,0)$: $\Psi y\in\Gamma y$
and, by Gap G, $\Phi y,\Psi\Phi y\notin F(y)$ (Lemma 4). For
$\nu=(0,1)$: symmetric. Hence $z\in\Gamma y$: the fiber is one orbit.
∎ (modulo G)

## §6. The single remaining gap (G)

**G:** for $\nu=(1,0)$, $O$ is never $Q/2$-symmetric
(equivalently $\Phi y\notin F(y)$); for $\nu=(0,1)$, $E$ never is.
Verified exactly: $m=32$, $0/2688$ per type ($\Phi y$ in neither fiber
nor orbit, `wave39_splitbit_phi.py`); $m=64$, $0/10880$ per type.
Why G is hard (two no-go facts, both checked): (i) power sums cannot
see it — symmetry forces only $m\cdot P_{m-1}\equiv0\pmod2$, automatic
since all odd positions share one parity and $p/2$ is even; (ii) dyadic
defects cannot see it — $\Phi$ preserves every dyadic defect, since
every shift by $p/2^r$ ($2^r\le p/2$) is even. A proof of G must use
the $M^2$-theory of the odd subsequence (top-bit balance of $w$),
not statistics or defects.

## Computational verification

- $m=32$ (8192 pts): split $\implies\nu=(1,1)$, 0 violations;
  nonsplit $p\ge8\implies\nu\in\{(1,0),(0,1)\}$, 0 violations.
- $m=64$ (32768 pts, 539 fibers, 20 split): same, 0 violations;
  split orbit counts $2/4/8/16=p/4$ by period.
- Lemma 2, Lemma 3, Lemma 5: verified as stated above.
Scripts: `wave39_splitbit_census.py`, `wave39_splitbit_census64.py`,
`wave39_splitbit_explore.py`, `wave39_splitbit_val.py`,
`wave39_splitbit_orbits.py`, `wave39_splitbit_support.py`,
`wave39_splitbit_phi.py`, `wave39_splitbit_nubar.py`,
`wave39_splitbit_basecase.py`. Repository untouched; no Lean built.

## Status

Split Bit Lemma: **proved modulo Gap G alone**. Together with wave 38,
$T_k=5(k-4)$ now rests on exactly three named statements: reversal
exclusion, Gap G (Split Bit), and the U-lemma. (Note: wave 38's
"odd-flip provably leaves the fiber" is equivalent to G by Lemma 4,
so it was not in fact proved there — G is the precise gap.)
