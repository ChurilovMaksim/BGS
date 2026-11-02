# Wave 41, task 1 — Gap G at m=64: PROVED
**Theorem.** Let $y$ be a kernel sequence mod $Q=32768$, 64-periodic,
$y_{i+1}=6y_i-y_{i-1}$, minimal period $p\in\{8,16,32,64\}$, $\nu=(1,0)$
($y_{i+p/2}-y_i=(Q/2)\nu_{i\bmod2}$). Then the odd sub-multiset
$O=\{y_i:i\text{ odd}\}$ is never $(Q/2)$-symmetric ($\Phi y\notin F(y)$).
$\nu=(0,1)$ follows by shift. Hence the Split Bit Lemma is unconditional at $m=64$.
## Setup (all periods)
$w_k=y_{2k+1}$ satisfies $w_{k+1}=34w_k-w_{k-1}\pmod Q$, period $p/4$ ($\nu_1=0$);
$O$ is the $w$-cycle repeated, so $O$ symmetric $\iff$ $w$-cycle symmetric.
Write $w_{k+p/8}=w_k+(Q/2)\varepsilon_k$ (quarter defect; $\varepsilon_k\in\{0,1\}$,
$k<p/8$), $v_k=w_k\bmod(Q/2)$, $t_k$ the top bit of $w_k$.
**Lemma Balance (refined).** For a class $c\bmod(Q/2)$,
$K_c=\{k<p/8:v_k=c\}$, $A_c=\#\{k\in K_c:\varepsilon_k=0\}$,
$B_c=\sum_{k\in K_c,\varepsilon_k=0}(1-t_k)$: $w$-cycle symmetric $\iff$
$2B_c=A_c$ for all $c$. (Count difference $=2\sum_{\varepsilon_k=0}(2t_k-1)$.)
**Lemma $\varepsilon$-alternation.** $d_i=y_{i+p/4}-y_i$,
$g_i=d_i/(Q/4)\bmod4$: $g_{\text{odd}}=2\varepsilon$, $g_{\text{even}}$ odd;
recurrence mod 4 at even $i$ gives $\varepsilon_k+\varepsilon_{k-1}$ odd
(cyclic, $p/8$ even), so $\varepsilon_k=\varepsilon_0\oplus(k\bmod2)$.
## Cases $p=8,16$
$p=8$: $O=\{w_0,w_1\}$ doubled; swapped quarter defect (wave 39, Lemma 2)
gives $w_1-w_0\in\{Q/4,3Q/4\}\ne Q/2$. ∎
$p=16$: $p/8=2$, $\varepsilon=(\varepsilon_0,1-\varepsilon_0)$; any class
containing an $\varepsilon=0$ index has $A_c=1$ (singleton, or both indices
with $(1-\varepsilon_0)+(1-\varepsilon_1)=1$), so $2B_c\ne A_c$. ∎
## Case $p=32$: parametrisation, (A), (B)
$M^{32}\equiv\bigl(\begin{smallmatrix}19233&16800\\15968&21729\end{smallmatrix}\bigr)$.
$(M^{32}-I)/32\bmod1024$: $601y_1+525y_0\equiv0$, $499y_1+679y_0\equiv0$,
so $y_1\equiv299y_0\pmod{1024}$ ($601\cdot299\equiv-525$) and
$376y_0\equiv0\pmod{1024}$, i.e. $y_0=128t$, $y_1=5504t+1024s$
($t\in\mathbf Z/256$, $s\in\mathbf Z/32$; substitution confirms kernel).
Via $M^{16}$: $y_{16}-y_0\equiv16384(t+s)$, $y_{17}-y_1\equiv16384s\pmod Q$,
so $\nu=(1,0)\iff t$ odd, $s$ even (2048 points).
$u_k=w_k\bmod(Q/2)$ ($k<4$); $u_0\equiv128\pmod{256}$ ($5504=21\cdot256+128$).
(A) $u_{k+2}\equiv u_k\pmod{Q/4}$ (Lemma 2 at level $Q/2$);
$\delta_k=(u_{k+2}-u_k)/(Q/4)\bmod2$. The $u$-recurrence mod $Q/2$ gives
$(Q/8)(\delta_0+\delta_1)\equiv288u_0\pmod{Q/4}$; with $u_0\equiv128\pmod{256}$,
RHS $\equiv4096\pmod{8192}$, so $\delta_0+\delta_1=1$.
(B) $e_i=y_{i+4}-y_i$; Lemma 2 at level $Q/2$ gives $e_{\text{odd}}\equiv0$,
$e_{\text{even}}\equiv Q/8\pmod{Q/4}$; the recurrence + $f$-argument of wave 40
(level-independent) gives $\varepsilon_0=\delta_1$.
Finish: if $\delta_1=0$ then $\varepsilon_0=0$, $\delta_0=1$; class $c=u_0$
contains $0$ ($\varepsilon_0=0$) but not $2$ ($u_2=u_0+Q/4$), and any other
member has $\varepsilon=1$, so $A_c=1$, $2B_c\ne1$. If $\delta_1=1$ then
$\varepsilon_0=1$, $\delta_0=0$; class $c=u_1$ contains $1$ ($\varepsilon_1=0$)
but not $3$ ($u_3=u_1+Q/4$), other members have $\varepsilon=1$, so $A_c=1$. ∎
## Case $p=64$: parametrisation
$M^{64}\equiv\bigl(\begin{smallmatrix}13889&832\\31936&18881\end{smallmatrix}\bigr)$.
$(M^{64}-I)/64\bmod512$: $217y_1+13y_0\equiv0$, $499y_1+295y_0\equiv0$,
so $y_1\equiv427y_0\pmod{512}$ ($217\cdot427\equiv-13$) and
$376y_0\equiv0\pmod{512}$, i.e. $y_0=64t$, $y_1=27328t+512s$
($t\in\mathbf Z/512$, $s\in\mathbf Z/64$; substitution confirms kernel).
Via $M^{32}$: $y_{32}-y_0\equiv16384(t+s)$, $y_{33}-y_1\equiv16384s\pmod Q$,
so $\nu=(1,0)\iff t$ odd, $s$ even (8192 points).
## Case $p=64$: the $\varphi$-machinery
$f_i=y_{i+8}-y_i$; Lemma 2 at level $Q/2$ gives $f_i\equiv0\pmod{Q/4}$ for odd $i$.
Put $\varphi_k=f_{2k+1}/(Q/4)\bmod4$. Then:
(i) $\varphi_{k+1}\equiv2\varphi_k-\varphi_{k-1}\pmod4$ ($f$ is kernel, its odd
subsequence has the 34-recurrence; divide by $Q/4$).
(ii) Parity lemma $\varphi_k\equiv\varepsilon_k\pmod2$: by (i) mod 2,
$\varphi$-parity is 2-periodic, as is $\varepsilon$; suffices $k=0,1$, from the
parametrisation: $f_1\equiv4096s\pmod{Q/2}$, $d_1\equiv8192s\pmod Q$, so
$\varphi_0\equiv\varepsilon_0\equiv(s/2)\bmod2$; $f_3\equiv8192t+4096s\pmod{Q/2}$,
$d_3\equiv16384t+8192s\pmod Q$, so $\varphi_1\equiv\varepsilon_1\equiv1+(s/2)\bmod2$
($t$ odd, $s$ even).
(iii) $\varphi_k+\varphi_{k+4}\equiv2\varepsilon_k\pmod4$
($d_{2k+1}=f_{2k+1}+f_{2k+9}=(Q/4)(\varphi_k+\varphi_{k+4})=(Q/2)\varepsilon_k$).
Also $\delta_k:=(u_{k+4}-u_k)/(Q/4)\bmod2=\varphi_k\bmod2=\varepsilon_k$ ($k<4$),
since $u_{k+4}-u_k\equiv f_{2k+1}\pmod{Q/2}$.
$t$-rule: writing $w_k=8192\alpha_k+\rho_k+16384t_k$ ($\alpha_k\in\{0,1\}$),
$w_{k+4}=w_k+8192\varphi_k$ gives $t_{k+4}=t_k\oplus(q_k\bmod2)$,
$q_k=(\alpha_k+\varphi_k)//2$; for $\varphi_k$ even: $\varphi_k=0\Rightarrow t$
same, $\varphi_k=2\Rightarrow t$ flips.
Unique $\varphi=0$: the $\varepsilon=0$ pairs among $k<4$ are $(0,2)$ or $(1,3)$;
$\varphi\in\{0,2\}$ there by (ii). If both equal, (i) at the middle index
($\varepsilon=1$, so $\varphi$ odd) gives a contradiction, e.g. $\varepsilon_0=0$:
$\varphi_0=\varphi_2\Rightarrow\varphi_2\equiv2\varphi_1-\varphi_0\Rightarrow
\varphi_1\equiv\varphi_0\pmod2$, impossible. Hence exactly one $j^*<4$ has $\varphi=0$.
Pair analysis: for a class $c$, $\delta=1$ pairs contribute $0$ to $(A_c,B_c)$
($\varepsilon=1$); a $\delta=0$ pair $(j,j+4)$ with $v_j=c$ contributes
$2B-A=2(1-2t_j)$ if $\varphi_j=0$, $0$ if $\varphi_j=2$. So
$2B_c-A_c=\sum_{j<4:\,\delta_j=\varepsilon_j=0,\,v_j=c,\,\varphi_j=0}2(1-2t_j)$.
Only $j^*$ has $\varphi=0$, so class $c^*=v_{j^*}$ has $2B-A=\pm2\ne0$:
balance fails, $w$-cycle and hence $O$ not symmetric. ∎
## Conclusion
Gap G holds at $m=64$ for all periods; the Split Bit Lemma is unconditional
at $m=64$. Checks: `wave41_GapG_m64_check.py` (matrices, parametrisations,
$\nu$-formulas, parity lemma, $\varphi$-recurrence, direct Gap G:
$p=8$: 128 pts, $p=16$: 512, $p=32$: 2048, $p=64$: 8192, all 0 symmetric).
No Lean, repo untouched.
