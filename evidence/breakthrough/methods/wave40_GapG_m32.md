# Wave 40, task 1 — Gap G at m=32: PROVED
**Theorem.** Let $y$ be a kernel sequence mod $Q=8192$, 32-periodic, $y_{i+1}=6y_i-y_{i-1}$,
minimal period $p\ge8$, $\nu=(1,0)$ ($y_{i+p/2}-y_i=4096\,\nu_{i\bmod2}$). Then the odd
sub-multiset $O=\{y_i:i\text{ odd},\,0\le i<p\}$ is never $4096$-symmetric ($\Phi y\notin F(y)$);
$\nu=(0,1)$ follows by shift. Uses wave 39, Lemmas 1–2: $\nu\ne(0,0)$; quarter-defect
$y_{i+p/4}\equiv y_i+2048\,\nu_{i\bmod2}\pmod{4096}$ ($p\ge16$, $\nu$ swapped for $p=8$).
## Setup
$w_k=y_{2k+1}$ satisfies $w_{k+1}=34w_k-w_{k-1}\pmod{8192}$ and has period $p/4$ in $k$
($\nu_1=0$). $O$ is the $w$-cycle repeated $(p/2)/L$ times ($L$ = minimal $w$-period), so
$O$ symmetric $\iff$ $w$-cycle symmetric (once $L=p/4$, Lemma L).
## Lemma L: $L=p/4$
$L\mid p/4$. If $L<p/4$: $\tilde y_i=y_{i+2L}-y_i$ is a kernel sequence, $0$ at odd $i$;
recurrence at even $i$ gives $6\tilde y_i\equiv0$, so $\tilde y_i\in\{0,4096\}$; dividing by
4096 mod 2, $\tilde y/4096$ is 2-periodic, hence $\tilde y_i=4096c\,[i\text{ even}]$ for one $c$.
Then $y_{i+4L}=y_i$, so $p\mid4L$, but $4L\mid p$; hence $4L=p$. ∎
## Lemma Balance ($p\in\{16,32\}$)
$S=p/4$, $d_i=y_{i+S}-y_i$; quarter-defect gives $d_i\in\{0,4096\}$ for odd $i$. Put
$\varepsilon_k=d_{2k+1}/4096\in\{0,1\}$, $k<L/2$: $w_{k+L/2}$ is $v_k$ with top bit flipped iff
$\varepsilon_k=1$. For a mod-4096 class $c$, $K_c=\{k<L/2:v_k\equiv c\}$, the lower-lift count
in class $c$ is $\sum_{K_c}\varepsilon_k+2\sum_{K_c,\varepsilon_k=0}(1-t_k)$ ($t_k$ = top bit of $v_k$);
symmetry needs it $=|K_c|$, i.e. $\sum_{k\in K_c}(1-\varepsilon_k)$ even for every $c$. ∎
## Lemma ε-alternation ($p\in\{16,32\}$)
$d$ satisfies the recurrence; $d_i\equiv0\pmod{4096}$ (odd $i$), $d_i\equiv2048\pmod{4096}$
(even $i$), so $e_i=d_i/2048\bmod4$ is defined and $e_{i+1}+e_{i-1}\equiv2e_i\pmod4$. At even
$i=2k$: $e_{2k+1}+e_{2k-1}\equiv2\pmod4$ with $e_{2k\pm1}=2\varepsilon_k,2\varepsilon_{k-1}$
($\varepsilon_{-1}=\varepsilon_{L/2-1}$ by periodicity, $L/2$ even), so $\varepsilon_k+\varepsilon_{k-1}$ is
odd: $\varepsilon$ alternates. ∎
## Case $p=8$
$O=\{w_0,w_1\}$ doubled; symmetry needs $w_1=w_0+4096$. But the swapped quarter-defect
($p=8$, $\mathrm{swap}(\nu)=(0,1)$) gives $y_3\equiv y_1+2048\pmod{4096}$, i.e.
$w_1-w_0\in\{2048,6144\}\ne4096$. ∎
## Case $p=16$
$L=4$, $\varepsilon=(\varepsilon_0,\varepsilon_1)$, $\varepsilon_0\ne\varepsilon_1$. Let $j$ be the index with
$\varepsilon_j=0$; for $c=v_j\bmod4096$, $\sum_{K_c}(1-\varepsilon_k)=1$ (the other index
contributes $0$), odd — balance fails. ∎
## Case $p=32$: parametrisation
$M^{32}\equiv\bigl(\begin{smallmatrix}2849&416\\7776&5345\end{smallmatrix}\bigr)\pmod{8192}$.
The kernel conditions $2848y_1+416y_0\equiv0$, $7776y_1+5344y_0\equiv0\pmod{8192}$,
divided by 32, give $89y_1+13y_0\equiv0$, $243y_1+167y_0\equiv0\pmod{256}$, whence
$y_0\equiv0\pmod{32}$ and $y_1\equiv43y_0\pmod{256}$; i.e. $y_0=32t$, $y_1=96t+256s$
($t\in\mathbf Z/256$, $s\in\mathbf Z/32$), and every such pair is a kernel point
(direct substitution).
$M^{16}\equiv\bigl(\begin{smallmatrix}401&208\\7984&1649\end{smallmatrix}\bigr)$:
$y_{17}-y_1\equiv4096(t+s)$, $y_{16}-y_0\equiv4096s\pmod{8192}$. Since $(h_0,h_1)=(4096,0)$
generates $h_i=4096[i\text{ even}]$, $\nu=(1,0)$ at $p=32\iff s,t$ odd (2048 points).
In particular $u_0:=y_1\bmod4096\equiv32\pmod{64}$.
## Case $p=32$: the bad case is impossible
$L=8$, $\varepsilon=(\varepsilon_0,1-\varepsilon_0,\varepsilon_0,1-\varepsilon_0)$. Balance holds iff the bad
case: $(\varepsilon_0=0\land u_2=u_0)$ or $(\varepsilon_0=1\land u_3=u_1)$, where $u_k=w_k\bmod4096$,
$u$ of period 4. Put $\delta_k=(u_{k+2}-u_k)/2048\bmod2$ ($u_{k+2}\equiv u_k\pmod{2048}$ by
Lemma 2 at level 4096).
(A) $\delta_0+\delta_1=1$: from $u_{k+1}=34u_k-u_{k-1}\pmod{4096}$ at $k=1,2$ with
$u_2=u_0+2048\delta_0$, $u_3=u_1+2048\delta_1$: $u_0+1024\delta_0\equiv17u_1$,
$u_1+1024\delta_1\equiv17u_0\pmod{2048}$, hence $1024(\delta_0+\delta_1)\equiv288u_0\pmod{2048}$,
$9u_0\equiv32(\delta_0+\delta_1)\pmod{64}$; with $u_0\equiv32\pmod{64}$ this forces
$\delta_0+\delta_1$ odd, i.e. $1$.
(B) $\varepsilon_0=\delta_1$: let $e_i=y_{i+4}-y_i$; Lemma 2 at level 4096 gives
$e_{\text{odd}}\equiv0$, $e_{\text{even}}\equiv1024\pmod{2048}$. Recurrence mod 4096 at $i=2$:
$e_3\equiv2048-e_1$, so $\delta_1=1\iff e_1\equiv0\pmod{4096}$. Mod 8192, writing
$e_2=1024+2048a+4096a'$, $e_4=1024+2048b+4096b'$: $e_5=e_1+4096(b-a)$; since
$d_1=y_9-y_1=e_5+e_1$, $\varepsilon_0=\delta_1\iff a\ne b$. Finally $f_i=(e_i/1024)\bmod8$
satisfies $f_{i+1}\equiv-f_{i-1}\pmod4$ at odd $i$, so $f_4\equiv-f_2\pmod4$ with $f_2,f_4$
odd, i.e. $f_2\not\equiv f_4\pmod4$, which is exactly $a\ne b$ ($a=0\iff f_2\equiv1\pmod4$).
By (A),(B): $\varepsilon_0=0\Rightarrow\delta_1=0\Rightarrow\delta_0=1$, and
$\varepsilon_0=1\Rightarrow\delta_1=1$ — both bad disjuncts fail. ∎
## Conclusion
Gap G holds at $m=32$ for all three periods, hence the Split Bit Lemma is unconditional
at $m=32$; $T_k=5(k-4)$ now rests on reversal exclusion and the U-lemma only (at the
2-part). No Lean, repo untouched.
Checks: `wave40_GapG_m32_check.py` (matrix values, parametrisation, $\nu\iff s,t$ odd,
direct Gap G on all 2688 points, 0 symmetric).
