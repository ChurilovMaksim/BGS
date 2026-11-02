# Wave 37: the three lemmas behind the 2-part pattern

## Setup

Level $j$: $m=2^j$, modulus $Q=2^{2j+3}$. Kernel points are $m$-periodic
sequences mod $Q$ with $y_{i+1}=6y_i-y_{i-1}$; $\Gamma$ = dihedral (shift +
reversal). A fiber = points with equal sorted multiset; split = $\ge2$
$\Gamma$-orbits. On-support = all 16 torsion conditions $y\cdot z\equiv
2Q(z)\pmod Q$ hold. $\rho:\mathrm{Ker}(j+1)\to\mathrm{Ker}(j)$ is reduction
mod $Q$; it is 16-to-1 onto an image of index 4. A level-$(j+1)$ split fiber
is NEW if all its orbits reduce to one level-$j$ orbit, else OLD.
Wave 36 proved $T_k=5(k-4)$ modulo the three lemmas below; this note proves
each of them modulo exactly one named gap. No counterexample was found.

## Common tool: lifts and drift (proved)

Let $N=2^j$, $M=\bigl(\begin{smallmatrix}6&-1\\1&0\end{smallmatrix}\bigr)$.
$M^4\equiv I\pmod 4$, so $M^N\equiv I\pmod 4$ for $j\ge2$. For a level-$j$
seed $s$ with $(M^N-I)s=Q\,u$, a lift $s'=s+Qt$, $t\in(\mathbf Z/4)^2$, is a
level-$(j+1)$ kernel point iff $(M^N+I)u+(M^{2N}-I)t\equiv0\pmod4$, i.e.
iff $2u\equiv0\pmod4$, independent of $t$. So a point has 16 lifts or none.

For a point $y$ of period $p$ with $4\mid p$, write a lift as
$y'_i=\bar y_i+Q\delta_i$. Then $L\delta=-e\pmod4$ where
$L=S-6+S^{-1}$ and $e_i=(\bar y_{i+1}-6\bar y_i+\bar y_{i-1})/Q\pmod4$.
The drift $D_r=\delta_{r+p}-\delta_r$ satisfies $LD=0$, so
$D_r=C+D\,r\pmod4$, and is lift-independent since $4\mid p$.
Proved identity (verified on 3456 points, 0 bad):
$D_r\equiv\sum_{j=1}^{p-1}j\,e_{r+j}\pmod4$, hence $D_r$ odd
$\iff\sum_{j\ \mathrm{odd}}e_{r+j}\equiv1\pmod2$.

**Drift-multiset theorem (proved).** If $D_r$ is odd for all $r$ and
$p\le N/2$, the lift multiset is $\bigsqcup_v\{v+Qd:d\in\mathbf Z/4\}$
with multiplicity $m_v/2$ per digit, $m_v$ = multiplicity of $v$ in $y$.
Proof: along each $p$-orbit $\{r+kp\}$, $\delta$ is an arithmetic
progression with odd difference over $2N/p$ terms ($4\mid 2N/p$), hence
covers $\mathbf Z/4$ uniformly; $m_v$ is even since $p\le N/2$. So the lift
multiset depends only on the base multiset.

## Lemma P: preimage of a fiber is a fiber

**Status: proved modulo the Drift Lemma.** Let $F$ be a split fiber and
$y\in F$. Its points have $4\mid p\le N/2$ (verified: periods at $m\le256$
are $8,16,32,64$, all $\le N/2$). If the drift of $y$ is odd, the
drift-multiset theorem gives every lift of $y$ the same multiset, and that
multiset depends only on $F$'s multiset, so $\rho^{-1}(F)$ is one fiber.
Type transformation $(o,s)\mapsto(4o,16s)$ follows (an orbit lifts to
exactly 4 orbits when its points have $4\mid p$).

**Drift Lemma (remaining gap for P).** Every point of every on-support
split fiber has $C$ odd, $D$ even (i.e. $D_r$ odd for all $r$).
Verified exhaustively: all points of all on-support split fibers at
$m=32,64,128,256$ — 14,336 points, 0 bad (periods $8$ / $16,8$ / $32,16,8$ /
$64,32,16,8$); plus the full $m=32$ census, where every split point with
lifts has $(C,D)\equiv(1,0)\pmod2$. What is missing is a proof of oddness
from splitness + support, e.g. via the mod-2 form above.

## Lemma S: the support rule

**Statement.** The preimage of an on-support split fiber $F$ at level $j$
is on-support at level $j+1$ iff $o(F)<2^{j-4}$, the max orbit count over
**on-support** split fibers. The qualifier is necessary: preimages of
$m=32$ fibers at $m=64$ are off-support split fibers with $o=8>4$.

**Proved.** (i) Defect lift-independence: the support defect
$d_z(y')=2Q(z)-y'\cdot z$ is the same for all lifts $y'$ of $y$. Correction
of wave 36: torsion rows are not affine in $i\bmod4$ — they are
4-periodic (periods 1, 2, 4; mod 4 each row is constant or a permutation
of $\mathbf Z/4$), and 4-periodicity suffices, since
$\sum_{i<2N}(A+Bi)z_i\equiv0\pmod4$ ($N/2\equiv0\pmod4$, and the $4k$ term
vanishes). (ii) Defect fiber-constancy follows from Lemma P + support
constancy on fibers, so one lift decides. (iii) Defect dichotomy: the
defect vector is either $0$ or $(q_{hi}/2)\cdot\mathrm{pat}$ with the
universal pattern $\mathrm{pat}=(0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0)$,
and $\mathrm{pat}_z=1\iff z$ is non-constant mod 4. Verified for every
fiber at $32\to64$, $64\to128$, $128\to256$, defect constant across lifts.

**Remaining gap for S.** The identification defect $\ne0\iff o(F)$ is max.
Mechanism: since $z$ is 4-periodic, $y'\cdot z=(N/2p)\cdot T$ for a
one-period sum $T$; $N/2p=2$ for max period vs divisible by 4 otherwise
($p=4o$ for on-support split fibers, verified). What remains is the exact
computation $T\equiv Q\pmod{2Q}$ for max-period fibers (and defect 0
otherwise). Verified 45/45 fibers, not yet proved.

## Lemma B: the birth rule

**Statement.** At each level $k\ge6$, exactly 10 NEW on-support split
fibers are born, with profile: 4-orbit $(128\times3,\ 64\times2)$ and
2-orbit $(32\times3,\ 16\times2)$.

**Mechanism (proved).** NEW fibers at level $j+1$ are in bijection with
non-split on-support orbits at level $j$ whose lifts fully collide (all
lifts share one multiset). By the drift-multiset theorem, full collision
$\iff$ drift odd ($4\mid p$) or the degenerate $p=1$ case; the lifted
orbits (4, or 2 for source size $\le2$) then form one fiber. Correction
of wave 36 §5: it is full collision, not "two of four collide" — no
pair-collision orbit occurs (distinct-multiset counts observed are
1, 4, 6, 7, 8, 10, never 2).

**Exact accounting (verified).** At $32\to64$ (all 71 non-split on-support
orbits) and at $128\to256$ (all 263), exactly 10 orbits fully collide,
with sizes $8,8,8,4,4,2,2,2,1,1$, periods $4,4,4,4,4,2,2,2,1,1$, and
lifted-orbit counts $4,4,4,4,4,2,2,2,2,2$. These give exactly the NEW
profile: $8\to4\times32$ (size 128), $4\to4\times16$ (64), $2\to2\times16$
(32), $1\to2\times8$ (16). The NEW profile itself matches at $m=64,128,256$.

**Remaining gap for B.** Stability: source orbits have period $\le4$ at
every level (from the NEW profile + lift period rule), so the claim is a
classification over the 128 period-$\le4$ points per level. Why exactly
these 10 orbits at every level — i.e. level-independence of the
full-collision condition — is verified at 3 steps but not proved.

## Status

| Lemma | Proved | Remaining gap |
|---|---|---|
| P (preimage is a fiber) | modulo Drift Lemma | prove drift odd from splitness + support |
| S (support rule) | modulo defect identification | prove $T\equiv Q\pmod{2Q}$ for max-period fibers |
| B (birth, 10 per level) | mechanism + accounting at 2 steps | prove stability of the period-$\le4$ classification |

Together with wave 36, $T_k=5(k-4)$ now rests only on these three named
gaps. Repository untouched; no Lean built. All computations are exact
integer checks (Python), not proofs, where so labeled.
