# Prime resonant blocks: exact sector criterion and spectral comb

**Claim ID:** `BGS-TRACE-009`. **Status:** elementary project proof,
author self-review and separately labelled finite regression. The actual
frozen-map cancellation hypothesis in Section 3 remains **OPEN**.
The order-divisibility input, ordered iteration and scalar-return exclusion
are prior corpus results; their reconstruction here is not a priority claim.
The [submission audit](../record/prime_resonant_review_20260930.md)
records the rejected stronger assertions.

## 1. Orientation and exact block algebra

Use the unchanged model $U_p=B_pM_p$, $B_p=e^{it_pA_p}$,
$t_p=\tau p$, $\tau=10^{-80}$, and raw Weyl operators
$$
T_p(a,b)\psi(x)=e_p\bigl(b(x+2^{-1}a)\bigr)\psi(x+a).
$$
Then $M_pT_p(v)M_p^{-1}=T_p(Sv)$, with
$$
S=\begin{pmatrix}3&4\\2&3\end{pmatrix},\qquad
Q(a,b)=a^2-2b^2,\qquad \lambda=3+2\sqrt2.
$$
The submitted inverse-conjugation formula has the inverse matrix $S^{-1}$;
that covariance is valid but cannot reverse the product orientation for
$U_p=B_pM_p$. Induction gives
$$
U_p^m=\left(\prod_{j=0}^{m-1}M_p^jB_pM_p^{-j}\right)M_p^m,       \tag{1}
$$
where increasing $j$ runs **from left to right**. This agrees with the
prior [ordered-iteration proof](frozen_spectral_flow_controls.md).
The same convention gives $\omega(v,Sv)=2Q(v)$,
$\omega(v,S^{-1}v)=-2Q(v)$ and $\det(I+S)=8$. The submitted negative
transversality sign belongs to inverse conjugation; it cannot be carried
over silently after changing orientation.

For an odd prime put $\chi_p=(2/p)$ and $d=d_p=\operatorname{ord}_p(S)$.
Over $\mathbb F_p$ or $\mathbb F_{p^2}$, the eigenvalues are
$\lambda^{\pm1}$, interpreted modulo $p$. They are distinct since
$\operatorname{disc}(S)=32\ne0$ modulo $p$. Frobenius gives
$\lambda^{p-\chi_p}=1$, so $d\mid p-\chi_p$. More precisely:

- If $\chi_p=1$, $\lambda=(1+\sqrt2)^2$ in $\mathbb F_p^*$, hence
  $d\mid(p-1)/2$ and $q_p=(p-1)/d$ is even. It need not equal 2.
- If $\chi_p=-1$, $(1+\sqrt2)^{p+1}=-1$, hence
  $\lambda^{(p+1)/2}=-1$. Thus $d$ has the full 2-adic valuation of
  $p+1$, and $q_p=(p+1)/d$ is odd.

Since $M_p^d$ commutes with every raw Weyl matrix and these span the full
matrix algebra, $M_p^d=\zeta_pI$ with $|\zeta_p|=1$. Therefore
$$
C_{p,d}=\prod_{j=0}^{d-1}\exp(it_pM_p^jA_pM_p^{-j}),\qquad
U_p^{rd}=\zeta_p^r C_{p,d}^{\,r}                              \tag{2}
$$
for every integer $r$, including negative $r$ by inversion. No commutativity
of different kicks is used. Merely replacing $M^jAM^{-j}$ by
$M^{-j}AM^j$ produces the block for $B_pM_p^{-1}$ instead.

The block does not inherit a new cat symmetry. Writing $B=B_p$, periodic
conjugation and a cyclic move of the first factor give exactly
$$
M_pC_{p,d}M_p^{-1}=B^{-1}C_{p,d}B,\qquad [U_p,C_{p,d}]=0.     \tag{3}
$$
The last identity is also immediate from $C_{p,d}=\zeta_p^{-1}U_p^d$.
It supplies no new independent spectral information.

There is an unconditional quantitative lower bound on $d$. The nonzero
integer determinant of $S^d-I$ is divisible by $p^2$, so
$$
p^2\le |\det(S^d-I)|=\lambda^d+\lambda^{-d}-2<\lambda^d,
\qquad d>\frac{2\log p}{\log\lambda}.                         \tag{4}
$$
In particular $d\to\infty$ along **all** primes. No conjecture about
multiplicative-order density is needed.

## 2. What the CUE reference actually means

For $m\ne0$, the exact pair identity and Haar reference are
$$
D_{U_p}(m,-m)=|\operatorname{Tr}U_p^m|^2-p,\qquad
\mathbb E_{\rm CUE}D_V(m,-m)=\min(|m|,p)-p.                  \tag{5}
$$
The [trace bridge](trace_to_local_statistics_bridge.md) uses a weighted
sum of these differences. An ensemble expectation is not a required
pointwise value for one deterministic trace. Its weighted absolute
comparison is a sufficient criterion, not a necessity theorem for BGS.
In particular, at $m=p-\chi_p$ the number
$p-(1+\chi_p)/2$ is the reference expectation only.

Nor should $C_{p,d}$ itself be compared with Haar CUE($p$). For Haar $V$,
$\operatorname{Tr}(V^d)^r=\operatorname{Tr}V^{dr}$, whose squared mean is
$\min(dr,p)$. Rains' prior power-map theorem gives the stronger distributional
statement: $V^d$ has the union of $d$ independent Haar spectra of sizes
$\lceil(p-i)/d\rceil$, $0\le i<d$ (zero-size components omitted).
The sum of their power-trace variances is $\min(dr,p)$.
See [the pinned source](../literature/prime_resonant_sources.md).
This is a reference ensemble statement, not an independence assertion
about the actual deterministic block.

## 3. Exact criterion for the whole sector

Let $K\subset[a,b]\subset(0,\infty)$ be compact, and set
$$
\mathcal R_p(K)=\{r\ge1:rd/p\in K\},\quad n_p=|\mathcal R_p(K)|,
$$
$$
E_p(K)=p^{-2}\sum_{r\in\mathcal R_p(K)}|\operatorname{Tr}C_{p,d}^r|^2,
\quad
S_p(K)=p^{-2}\sum_{r\in\mathcal R_p(K)}
\left||\operatorname{Tr}C_{p,d}^r|^2-\min(rd,p)\right|.
$$
For nonnegative numbers $x,y$, $\bigl||x-y|-x\bigr|\le y$. Consequently
$$
\boxed{|S_p(K)-E_p(K)|\le\frac{n_p}{p}
\le\frac{b-a}{d}+\frac1p.}                                  \tag{6}
$$
The same proof works with any nonnegative bounded weights $w(rd/p)$,
with the right side multiplied by $\|w\|_\infty$. Negative times duplicate
the positive-time absolute contribution for an even weight.

**Sector theorem.** Along the odd primes,
$S_p(K)\to0$ if and only if $E_p(K)\to0$. Thus the CUE reference carried
by this sparse sector already vanishes by (4); what remains to prove is
vanishing of its **actual total normalized trace mass**.

If $n_p=0$, both sides are zero. Otherwise, defining the sector mean
$H_p=n_p^{-1}\sum_{r\in\mathcal R_p(K)}|\operatorname{Tr}C^r|^2$,
the exact requirement is $n_pH_p=o(p^2)$. For a fixed interval $[a,b]$
with $a<b$ and $p/d\to\infty$, $n_p\sim(b-a)p/d$, so this is
$$
H_p=o(pd).                                                   \tag{7}
$$
Uniform $O(\sqrt p)$ traces throughout the sector would be sufficient:
$S_p(K)=O_K(d^{-1}+p^{-1})$. It is substantially stronger than (7).
For one selected time alone, $|\operatorname{Tr}C^r|=o(p)$ suffices.
Uniform $o(p)$ across an increasing number of times, without a rate,
does not by itself give (7).
If instead $d_p/p$ is bounded below by a positive constant, there are
only $O_K(1)$ times; uniform $o(p)$ on this finite sector is sufficient.

**Open model input:** prove $E_p(K)=o(1)$ for the specified frozen
$C_{p,d}$ on every compact $K$. Neither (6), scalar exclusion, nor
the source reference theorem proves this input. Its completion would
dispose of this prime-resonant contribution to `BGS-TRACE-005` only;
nonresonant times, composite dimensions and higher joint traces remain.

## 4. Block-spectrum Fejer energy and an exact microscopic comb

Write $e^{2\pi i\varphi_j}$ for the block eigenvalues and
$$
F_L(x)=L^{-1}\left|\sum_{s=0}^{L-1}e^{2\pi isx}\right|^2
=\sum_{|r|<L}(1-|r|/L)e^{2\pi irx},\qquad
G_L(C)=p^{-2}\sum_{j,l}F_L(\varphi_j-\varphi_l).
$$
Expansion gives the exact positive identity
$$
G_L(C)-1=\frac2{p^2}\sum_{r=1}^{L-1}(1-r/L)|\operatorname{Tr}C^r|^2.
                                                               \tag{8}
$$
For $R\ge1$ and $E_{\le R}=p^{-2}\sum_{r=1}^R|\operatorname{Tr}C^r|^2$,
$$
\tfrac12\bigl(G_{R+1}(C)-1\bigr)\le E_{\le R}
\le G_{2R+1}(C)-1.                                           \tag{9}
$$
If $R=0$, the trace sum is zero and no large-$R$ inference is needed.
Thus a sufficient quantitative hypothesis for Section 3 is
$G_{2\lfloor bp/d\rfloor+1}(C)=1+\varepsilon_p$, $\varepsilon_p\to0$;
then $S_p(K)\le\varepsilon_p+(b-a)/d+1/p$.

Let $e^{2\pi i\theta_j}$ be the eigenvalues of $U_p$. By (2),
$\varphi_j=d\theta_j-\arg\zeta_p/(2\pi)$ modulo 1. The scalar phase
cancels from differences. Fourier expansion proves
$$
F_L(dx)=\frac1d\sum_{h=0}^{d-1}F_{dL}(x-h/d),                 \tag{10}
$$
and hence
$$
\boxed{G_L(C)=\frac1{dp^2}\sum_{h=0}^{d-1}\sum_{j,l}
F_{dL}(\theta_j-\theta_l-h/d).}                               \tag{11}
$$
When $L\asymp p/d$, these kernels have width $O(1/p)$, centered at
**all** rational shifts $h/d$. The block route asks for control of an
average of shifted microscopic pair energies, not solely pairs near zero.
Ordinary short-time smooth-observable equidistribution is not the needed
estimate. Mere $O(1)$ occupancy control also gives at most an $O(1)$
energy bound; (8) needs the sharper baseline $1+o(1)$.

These are exact reductions and diagnostics, not proved cancellation for
the actual block. A non-scalar simple-spectrum counterexample is
$C_p=\operatorname{diag}(e^{2\pi ij/p^3})_{j=0}^{p-1}$:
its normalized traces tend uniformly to 1 for $r\le bp/d$, despite
non-scalarity. It is an abstract control, not the prescribed map.

## 5. A genuine asymptotic obstruction would require less than a fraction

Suppose along infinitely many primes there are $r_p$ with
$r_pd_p/p\in[a,b]$ and $|\operatorname{Tr}C^{r_p}|\ge cp$, $c>0$.
Then the sector absolute comparison has a term at least $c^2-1/p$.
More strongly, pass to a subsequence with $r_pd_p/p\to t_0>0$.
The positive measures
$$
\mu_p=p^{-2}\sum_{m\ge1}|\operatorname{Tr}U_p^m|^2\delta_{m/p},\qquad
\nu_p=p^{-2}\sum_{m\ge1}\min(m,p)\delta_{m/p}
$$
have a mass at least $c^2$ approaching $t_0$, while
$\nu_p\Rightarrow\min(t,1)\,dt$ on compact intervals. Choose a
nonnegative smooth bump equal to 1 near $t_0$, with compact support
so narrow that its reference integral is less than $c^2/2$.
Then $\mu_p(w)\ge c^2$ eventually, whereas $\nu_p(w)<c^2/2+o(1)$.
Other frequencies cannot repair this difference, since $\mu_p$ is positive.
The even extension of $w$ is the Fourier transform of a band-limited
Schwartz pair test; (5) and the exact trace bridge give a failure of its
CUE pair comparison. Thus **one recurrent coherent Heisenberg mode**
already suffices. No such infinite-prime assertion is proved here.

## 6. Reproducing -98 and the alleged collision primes

In $g(q,p)=\sum\widehat g(n,m)e^{2\pi i(nq+mp)}$, the correct raw
coefficient is $a_{(m,n)}=(-1)^{mn}\widehat g(n,m)$.
At $v_0=(0,7)$ it is $9/20$ and $Q(v_0)=-98$.
The complete other invariant values and their differences from $-98$ are

| $Q(v)$ | $Q(v)+98$ |
|---:|---:|
| -162 | -64 |
| -128 | -30 |
| -127 | -29 |
| -97 | 1 |
| -72 | 26 |
| -71 | 27 |
| -50 | 48 |
| -8 | 90 |
| -2 | 96 |
| -1 | 97 |
| 1 | 99 |

Since $Q(Sv)=Q(v)$, an additional support point can enter the
$v_0$-orbit only at a prime divisor of one of these differences.
The **candidate** set is $\{2,3,5,11,13,29,97\}$; 1 is not a prime.
For $p>17$ away from 29 and 97, the orbit sum is $9/20$ or $9/10$
according as $-v_0$ is absent from or present in the oriented orbit.

At $p=29$, the orbit of $(0,7)$ is
$$
(0,7),(28,21),(23,3),(23,26),(28,8),
(0,22),(1,8),(6,26),(6,3),(1,21).
$$
Its supported integral representatives are $(0,\pm7)$ and
$(\pm1,\pm8)$. Each of the latter has real coefficient $3/4000$;
the imaginary coefficients cancel in pairs. Its sum is exactly
$$
9/10+4(3/4000)=903/1000.                                    \tag{12}
$$
At $p=97$, take $\sqrt2=14$. The coordinate $\xi=a+14b$ evolves by
$\xi\mapsto31\xi$, and 31 has order 48, generating the squares.
For $v_0$, $\xi=1$; for the candidate extra points $(\pm1,\pm1)$,
$\xi\in\{\pm13,\pm15\}$, all nonsquares since
$13^{48}=15^{48}=-1$ and $(-1/97)=1$. They are in the other orbit.
Here $-v_0=S^{24}v_0$ and the sum is $9/10$.
The order certificate can be reproduced by repeated squaring:
$31^{48}=1$, $31^{24}=-1$, and $31^{16}\ne1$ modulo 97.
Thus neither 29 nor 97 needs exclusion for this scalar test.

In fact the earlier [FM-010 proof](frozen_arithmetic_trace_rigidity.md)
already proves a stronger all-odd-dimensional statement. For every
$p\ge19$, the negative real-coefficient mass of the full raw symbol is
$14/125$, so the $v_0$-orbit sum has real part at least
$9/20-14/125=169/500$. If
$H_d=\sum_{j=0}^{d-1}M_p^jA_pM_p^{-j}$, every nonzero Weyl orbit has
length $d$, and Weyl orthogonality gives
$$
p^{-1}\operatorname{Tr}H_d^2
=d\sum_{\mathcal O\ne\{0\}}\left|\sum_{v\in\mathcal O}a_v\right|^2
\ge d(169/500)^2>0.                                         \tag{13}
$$
Here $\operatorname{Tr}A_p=0$ and the 32 modes do not alias.
This proves that the **linearized orbit sum** is not scalar; FM-010
separately rules out every scalar power of the actual $U_p$.
The exceptional dimension 7 has $A_7=(9/10)I$ and $d_7=3$.
No trace upper bound follows from either exclusion.

## 7. Fixed-coupling finite-size coherence is not an asymptotic obstruction

The exact coefficient mass is $L_g=19/20+\sqrt{101}/50$, so
$\|A_p\|\le L_g$ for $p\ge19$. Telescoping unitary factors yields
$\|C^r-I\|\le m|\tau|pL_g$, $m=rd$. For a unitary $V$,
$\operatorname{Re}\operatorname{Tr}V=p-\|V-I\|_{HS}^2/2$.
Consequently, if $x=m|\tau|pL_g\le\sqrt2$,
$$
|\operatorname{Tr}C^r|^2\ge p^2(1-x^2/2)^2.                 \tag{14}
$$
This is a rigorous coherent regime when $m\le bp$ and
$bL_g|\tau|p^2\ll1$, at dimensions far below $10^{40}$.
It covers only finitely many primes for fixed nonzero $\tau$.
It cannot establish the infinite-prime premise of Section 5.
Ordinary floating-point diagonalization at tiny fixed $\tau$ cannot
resolve the transition and must not be used as evidence of that premise.

## 8. Verification boundary

The maintained [checker](../computations/verification/prime_resonant_audit.py)
reconstructs the symbol through the prior audited Laurent expansion,
uses exact Gaussian rationals and integer modular orbits, and separately
checks matrix orientation and Fejer energies in complex128 at declared
control couplings. The promoted output and source hashes are in
`evidence/20260930/prime_resonant_checks.json` and
`evidence/20260930/prime_resonant_manifest.json`.
No Lean compilation, external referee report, new priority claim,
frozen-map sector cancellation or BGS solution is certified by these tests.
