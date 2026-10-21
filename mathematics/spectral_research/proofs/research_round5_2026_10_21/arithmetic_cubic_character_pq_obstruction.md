> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round5_2026_10_21/arithmetic_cubic_character_pq_obstruction.md`. Embedded SHA256: `0b67c9c8d2f698046af49d0527eaf81169cd76d84112ffeebd6bfdeb79ac1625`.
> [Thematic guide](../../topics/arithmetic.md).

# Cubic-character circulants: strong P and Q estimates coexist with microscopic spectral clusters

Date: 2026-10-21.  
Status: proved auxiliary obstruction, including the published character-sum input and all its hypotheses.  
Scope: the matrices in this note are auxiliary matrices $V_p,\widetilde V_p$. Neither is the original $U_N=e^{i\tau N A_N}M_N$. No change of the original fixed $\tau$ is made or authorized by this construction.

## 1. Main statement

There are infinitely many primes $p>5$, $p\equiv1\pmod3$, and explicit deterministic unitary matrices $V_p\in U(p)$ such that, with
$$
 P(V)_{xy}=|V_{xy}|^2,\qquad
 Q(V)_{xy}=V_{xy}\overline{V_{yx}},\qquad
 \Pi_p=p^{-1}{\bf1}{\bf1}^{*},
$$
one has
$$
 V_p^3=I,\qquad
 \max_{x,y}|(V_p)_{xy}|\le4p^{-1/2},
 \tag{1.1}
$$
and
$$
 \|P(V_p)-\Pi_p\|_{\rm op},
 \ \|Q(V_p)\|_{\rm op}
 \le B_p:=\min\{1,4p^{-1/2}+7p^{-1}\}.
 \tag{1.2}
$$
In particular, the unistochastic matrix has a gap tending to one, and the reversal matrix tends to zero in operator norm.

Nevertheless, their randomly translated local eigenangle processes converge weakly to the empty point measure. For every nonzero admissible $b$ from $H_{\rm diag}$, putting
$$
 H=\int_{\mathbb R}b,\qquad \beta=\int_{\mathbb R}b^2>0,
$$
the exact local factorial moment satisfies
$$
 M^{V_p}_{2,p}(b)\ge
 \left(\frac p6-\frac12\right)\beta ,
 \qquad
 \Delta^{V_p}_{2,p}(b)\longrightarrow+\infty.
 \tag{1.3}
$$

A second explicit deterministic family $\widetilde V_p$ satisfies
$$
 \max_{x,y}|(\widetilde V_p)_{xy}|\le5p^{-1/2},\qquad
 \|P(\widetilde V_p)-\Pi_p\|_{\rm op},
 \ \|Q(\widetilde V_p)\|_{\rm op}=O(p^{-1/2}),
 \tag{1.4}
$$
has simple spectrum, has simple spectrum in every positive integer power, and has no nontrivial scalar power. It still has the same empty local weak limit and divergent second local factorial moment. Its near returns obey the explicit estimate
$$
 \|\widetilde V_p^{\,3m}-I\|_{\rm op}
 \le6\pi\sqrt2\,m\,p^{-3}\qquad(m\ge0).
 \tag{1.5}
$$
Thus the estimates (1.1)–(1.2), even supplemented by spectral simplicity and absence of exact scalar returns, cannot alone establish local CUE statistics.

All constants here are independent of $p$. The prime restriction belongs only to this auxiliary obstruction.

## 2. Exact construction and infinitude of the dimensions

For a prime $p\equiv1\pmod3$, choose a multiplicative character
$\chi:\mathbb F_p^\times\to\{1,\omega,\omega^2\}$ of order three, where
$\omega=e^{2\pi i/3}$, and set $\chi(0)=0$.
For definiteness one may choose the least positive primitive root of $\mathbb F_p^\times$ and assign it the value $\omega$. The usual cyclicity of $\mathbb F_p^\times$ also follows directly from the fact that a degree-$d$ polynomial over a field has at most $d$ roots: the maximal element order in a finite abelian subgroup is its exponent (combine maximal prime-power components), and the exponent therefore cannot be less than the subgroup's cardinality.

Set
$$
 R=\{0,1,3\}\subset\mathbb F_p,\qquad
 P_0(X)=X(X-1)(X-3),
$$
and define
$$
 \lambda_j=
 \begin{cases}
   \chi(P_0(j)),&j\notin R,\\
   1,&j\in R.
 \end{cases}
 \tag{2.1}
$$
Each $\lambda_j$ is a third root of unity. Define
$$
 (F_p)_{jx}=p^{-1/2}e_p(jx),\qquad
 V_p=F_p^*\operatorname{diag}(\lambda_j)F_p.
 \tag{2.2}
$$
Fourier orthogonality proves $F_p$ unitary. Hence (2.2) is unitary and $V_p^3=I$ exactly.

For completeness, infinitely many primes $1\pmod3$ follow without a prime-distribution theorem. If there were only finitely many, let $a$ be three times their product. A prime divisor $q$ of $a^2+a+1>1$ is not three and divides neither $a$ nor $a-1$: a common divisor with $a-1$ would divide three. Thus $a$ has multiplicative order exactly three modulo $q$, giving $q\equiv1\pmod3$. But $a^2+a+1\equiv1\pmod q$ for every prime in the alleged finite list, a contradiction. Removing finitely many small primes leaves infinitely many $p>5$.

## 3. Published character-sum input and checked specializations

The external input is Todd Cochrane and Christopher Pinner, *Using Stepanov's method for exponential sums involving rational functions*, **Journal of Number Theory 116** (2006), no. 2, 270–292, Theorems 1.1 and 1.2. The author-hosted version is
https://www.math.ksu.edu/~cochrane/research/stepmix.pdf
(Theorems 1.1–1.2 on its pages 3–4). The author's publication list explicitly identifies this PDF with the published article:
https://www.math.ksu.edu/~cochrane/research/research09.html
The publisher record is
https://www.sciencedirect.com/science/article/pii/S0022314X05000983 .
The hypotheses and theorem statements were directly read from the author-hosted PDF.

In the notation of that paper, a polynomial $g$ has $L$ distinct geometric zeros and $U$ zeros whose multiplicities give a trivial power of $\chi$. Their condition (1.11) excludes $g=c h^t$ for every $t>1$ dividing $p-1$. A zero of multiplicity one verifies this condition.

For $g=P_0$, Theorem 1.1 with $f(X)=uX$, $u\ne0$, has $M=1,L=3,U=0$, no finite poles, and $p\nmid M$. Thus
$$
 \left|\sum_{j\in\mathbb F_p}\chi(P_0(j))e_p(uj)\right|
 \le3\sqrt p\quad(u\ne0).
 \tag{3.1}
$$
Theorem 1.2 with $g=P_0$ has $L=3,U=0,\deg g=3$, so
$$
 \left|\sum_{j\in\mathbb F_p}\chi(P_0(j))\right|
 \le\sqrt p+1.
 \tag{3.2}
$$

We will also use Theorem 1.2 on
$$
 g_\varphi(X)=P_0(X)P_0(\varphi(X))^2,
 \tag{3.3}
$$
where $\varphi(X)=X+r$ with $r\ne0$, or $\varphi(X)=r-X$ with any $r$. Its hypotheses and parameters are checked next.

### Root-set check

A nonzero translation cannot preserve $R$: its orbits on the prime field have cardinality $p>3=|R|$.

No reflection $x\mapsto r-x$ preserves $R$ when $p>5$. A permutation of a three-element set induced by an involution has a fixed element. If the fixed element is $0$, then $r=0$, while the other pair would require $r=1+3=4$, impossible for $p>5$. If it is $1$, then $r=2$, while the other pair would require $r=0+3=3$, impossible. If it is $3$, then $r=6$, while the other pair would require $r=0+1=1$, requiring $p=5$.

Thus the two three-element root sets of the factors in (3.3) are different. Write $m\in\{0,1,2\}$ for the size of their intersection. The union has $L=6-m$ elements. At the $m$ shared roots, $g_\varphi$ has multiplicity three, and at the remaining roots it has multiplicity one or two. In particular, a root of multiplicity one exists. This verifies the full perfect-power exclusion (1.11), not merely exclusion of cubes.

Here $U=m$, $L>U$, $\deg g_\varphi=9$, and $\chi^9$ is trivial. Theorem 1.2 therefore gives
$$
 \left|\sum_j\chi(g_\varphi(j))\right|
 \le (L-2-U)\sqrt p+(U+1)
 =(4-2m)\sqrt p+m+1.
 \tag{3.4}
$$
There are no finite poles, so the sum is exactly over the full prime field, with $\chi(0)=0$.

Away from the union of the two root sets, the summand in (3.4) equals
$\lambda_j\overline{\lambda_{\varphi(j)}}$, since $\overline\chi=\chi^2$. At a root in the union, the former summand is zero and the latter has modulus one. There are $6-m$ such roots. Consequently
$$
 \left|\sum_j\lambda_j\overline{\lambda_{\varphi(j)}}\right|
 \le (4-2m)\sqrt p+7\le4\sqrt p+7.
 \tag{3.5}
$$
This verifies both the nondegeneracy and the modification-at-zeros error.

## 4. Entries and the exact P/Q Fourier diagonalizations

Equation (2.2) gives
$$
 (V_p)_{xy}=a_{y-x},\qquad
 a_t=\frac1p\sum_j\lambda_j e_p(jt).
 \tag{4.1}
$$
The replacement of $\chi(P_0(j))$ by $\lambda_j$ alters any Fourier sum by at most three. Equations (3.1)–(3.2) imply
$$
 |a_t|\le\frac{3\sqrt p+3}{p}\quad(t\ne0),\qquad
 |a_0|\le\frac{\sqrt p+4}{p}.
 \tag{4.2}
$$
For $p\ge13$ these imply $\max_t|a_t|\le4/\sqrt p$. The only remaining prime $p>5,\ p\equiv1\pmod3$ is seven, for which the trivial unitary-entry bound $|a_t|\le1<4/\sqrt7$ suffices. This proves the exact constant in (1.1).

Both $P$ and $Q$ are circulant. On the character $x\mapsto e_p(rx)$, $P$ has eigenvalue
$$
 \gamma_r
 =\sum_t|a_t|^2e_p(rt)
 =\frac1p\sum_j\lambda_j\overline{\lambda_{j+r}}.
 \tag{4.3}
$$
Indeed, after inserting (4.1), summing over $t$ enforces
$j-k+r=0$. Thus $\gamma_0=1$, and (3.5) controls every nonconstant mode. Fourier diagonalization is unitary even though $P$ need not be symmetric. Therefore
$$
 \|P-\Pi_p\|_{\rm op}
 =\max_{r\ne0}|\gamma_r|
 \le4p^{-1/2}+7p^{-1}.
 \tag{4.4}
$$

For $Q$, its circulant kernel is $a_t\overline{a_{-t}}$. Its eigenvalue on the same character is
$$
 \eta_r
 =\sum_ta_t\overline{a_{-t}}e_p(rt)
 =\frac1p\sum_j\lambda_j\overline{\lambda_{-r-j}}.
 \tag{4.5}
$$
Here Fourier orthogonality enforces $j+k+r=0$. Equation (3.5), applied to the reflection $j\mapsto-r-j$, controls all $r$, including $r=0$:
$$
 \|Q\|_{\rm op}=\max_r|\eta_r|
 \le4p^{-1/2}+7p^{-1}.
 \tag{4.6}
$$
The matrix $Q$ is Hermitian because $Q_{yx}=\overline{Q_{xy}}$; equivalently the sums (4.5) are real after replacing $j$ by $-r-j$.

Each normalized sum in (4.3) or (4.5) is an average of $p$ unit-modulus numbers, hence also has absolute value at most one. This proves (1.2), including its minimum with one.

## 5. Local weak limit and failure of the second factorial moment

The eigenangles of $V_p$ lie in the three-point set
$\{0,1/3,2/3\}$. Let their multiplicities be $n_0,n_1,n_2$, so
$$
 n_0+n_1+n_2=p,\qquad
 \sum_{a=0}^2n_a(n_a-1)\ge p^2/3-p.
 \tag{5.1}
$$
The inequality is Cauchy–Schwarz.

Let $\alpha$ be uniform on the circle, exactly as in the original local-process definition. For any fixed $R_0>0$, the event that the scaled process places a point in $[-R_0,R_0]$ requires $\alpha$ to be within circular distance $R_0/p$ of one of three locations. Its probability is at most $6R_0/p$, hence tends to zero. Every vague neighborhood of the zero measure contains a neighborhood specified by finitely many compactly supported test functions. Enclosing their supports in one such interval proves convergence in probability, and therefore in law, to the empty point measure.

This is incompatible with the sine process: for any nonzero nonnegative compactly supported test function $f$, the sine process has
$\mathbb E\langle f,\mathrm{Sine}_2\rangle=\int f>0$, so its Laplace functional is strictly less than one. The auxiliary process's Laplace functional tends to one. Its exact unit intensity is consistent with this weak limit because the local counts are not uniformly integrable.

For the moment statement, $b_p(t)=\sum_{\ell\in\mathbb Z}b(p(t+\ell))$ is nonnegative. Keeping only distinct eigenvalue indices from the same cluster gives
$$
 M^{V_p}_{2,p}(b)
 \ge\frac12\sum_an_a(n_a-1)\int_0^1b_p(t)^2\,dt.
 \tag{5.2}
$$
All summands are nonnegative, and
$$
 \int_0^1b_p(t)^2\,dt
 \ge\int_0^1\sum_{\ell}b(p(t+\ell))^2\,dt
 =\frac{\beta}{p}.
 \tag{5.3}
$$
Combining (5.1)–(5.3) proves (1.3). The CUE benchmark is bounded by $H^2/2$, so
$$
 \Delta^{V_p}_{2,p}(b)
 \ge \left(\frac p6-\frac12\right)\beta-\frac{H^2}{2}
 \longrightarrow+\infty.
 \tag{5.4}
$$
For example, any fixed $\epsilon>0$ is exceeded along all sufficiently large primes in this sequence.

Nonzero admissible $b$'s exist explicitly: choose nonzero
$\phi\in C_c^\infty(\mathbb R)$, let $g=\mathcal F^{-1}\phi$, and put
$b=|g|^2/(2\|g\|_\infty^2)$. Then $b\ge0$, $\sup b=1/2$, $b$ is Schwartz, and its Fourier transform is a smooth compactly supported convolution. This is a fixed function independent of $p$.

## 6. Removing every exact return and every spectral multiplicity

Use the integer representatives $j=0,\ldots,p-1$, set
$$
 \varepsilon_p=\frac{\sqrt2}{p^4},\qquad
 \widetilde\lambda_j=\lambda_j e^{2\pi i\varepsilon_p j},\qquad
 \widetilde V_p=F_p^*\operatorname{diag}(\widetilde\lambda_j)F_p.
 \tag{6.1}
$$
This modification is only part of the auxiliary construction. It is not a replacement $\tau\mapsto\tau_N$ in the original problem.

Define
$$
 d_p=2\pi\varepsilon_p(p-1)\le2\pi\sqrt2\,p^{-3}.
 \tag{6.2}
$$
Then
$$
 |\widetilde\lambda_j-\lambda_j|\le d_p,\qquad
 \max_t|\widetilde a_t-a_t|\le d_p.
 \tag{6.3}
$$
For $p\ge7$, $d_p\le p^{-1/2}$, so the entry bound in (1.4) follows.

Each product
$\widetilde\lambda_j\overline{\widetilde\lambda_k}$ differs from
$\lambda_j\overline{\lambda_k}$ by at most $2d_p$. Applying the exact Fourier formulas (4.3) and (4.5) to the modified sequence therefore yields
$$
 \|P(\widetilde V_p)-\Pi_p\|_{\rm op},
 \ \|Q(\widetilde V_p)\|_{\rm op}
 \le B_p+2d_p=O(p^{-1/2}).
 \tag{6.4}
$$
This bound uses the normal circulant diagonalization, so there is no missing factor $p$.

For distinct indices $j,k$, the eigenangle difference is congruent modulo one to
$$
 \frac{a}{3}+\frac{\sqrt2(j-k)}{p^4}
 \quad\text{for some integer }a.
 \tag{6.5}
$$
It is irrational. No positive integer multiple is an integer. Hence distinct eigenvalues remain distinct in every positive integer power. In particular, no positive power of $\widetilde V_p$ is scalar. Only the elementary irrationality of $\sqrt2$ is used here.

On the other hand,
$$
 \widetilde V_p^{\,3m}
 =F_p^*\operatorname{diag}
     \left(e^{2\pi i\,3m\varepsilon_p j}\right)F_p,
$$
because $\lambda_j^3=1$. The inequality $|e^{it}-1|\le|t|$ proves (1.5) for every $m\ge0$.

The eigenangles in (6.1) lie in three intervals of length
$$
 w_p=\varepsilon_p(p-1)\le\sqrt2\,p^{-3}
 \tag{6.6}
$$
starting at the three cube-root locations. Consequently
$$
 \mathbb P_\alpha\bigl(\Xi^{\widetilde V_p}_{p,\alpha}
       ([-R_0,R_0])>0\bigr)
 \le3w_p+\frac{6R_0}{p}\longrightarrow0.
 \tag{6.7}
$$
The local weak limit is again the empty process.

To check the factorial moment without assuming exactly coincident angles, let
$$
 C_b(t)=\int_{\mathbb R}b(x)b(x+t)\,dx .
$$
It is nonnegative and continuous, with $C_b(0)=\beta$. Periodization and a change of variable give the exact identity
$$
 \int_0^1b_p(\theta-\alpha)b_p(\theta'-\alpha)\,d\alpha
 =\frac1p\sum_{\ell\in\mathbb Z}
      C_b\bigl(p(\theta-\theta'+\ell)\bigr).
 \tag{6.8}
$$
Absolute convergence follows from Schwartz decay; all terms are nonnegative. For indices from the same original cube-root cluster,
$|\theta-\theta'|\le w_p$, and $pw_p\to0$.
Let
$$
 e_p=\sup_{|t|\le pw_p}|C_b(t)-\beta|\longrightarrow0.
$$
Keeping the $\ell=0$ term in (6.8), and then only within-cluster distinct index pairs, proves
$$
 M^{\widetilde V_p}_{2,p}(b)
 \ge\left(\frac p6-\frac12\right)(\beta-e_p).
 \tag{6.9}
$$
Thus $\Delta^{\widetilde V_p}_{2,p}(b)\to+\infty$, as claimed. The label $e_p$ in this paragraph denotes a real error, not the finite-field additive character.

## 7. What this obstruction establishes at Heisenberg times

For fixed $t>0$, let $n_p=3\lfloor tp/3\rfloor$. Then $n_p/p\to t$, and (1.5) implies
$$
 \|\widetilde V_p^{\,n_p}-I\|_{\rm op}=O_t(p^{-2}),\qquad
 \frac{|\operatorname{Tr}\widetilde V_p^{\,n_p}|^2}{p^2}
 \longrightarrow1.
 \tag{7.1}
$$
In contrast, from (6.4) and the exact diagonalizations,
$$
 |\operatorname{Tr}P(\widetilde V_p)^{n_p}-1|
 \le(p-1)(B_p+2d_p)^{n_p}\longrightarrow0,
$$
and
$$
 |\operatorname{Tr}Q(\widetilde V_p)^{n_p}|
 \le p(B_p+2d_p)^{n_p}\longrightarrow0.
 \tag{7.2}
$$
The same statements for $V_p$ have exact return in (7.1).

Thus rapid mixing of the squared-entry operator and decay of the reversal operator coexist with almost maximal quantum trace at times proportional to dimension. Their spectra do not encode all coherent contributions to the quantum trace. The example prohibits a deduction of the missing dense-history cancellation solely from these two operator estimates, entry flatness, simplicity, or qualitative absence of exact scalar powers.

It does not prove or disprove $H_{\rm diag}$ for the original fixed family. Its purpose is to distinguish a valid bound on selected coherent classes from a false general closure principle. The original first missing estimate remains the fully weighted signed trace-product cancellation, with its original $\tau$, all required $k,b$, and all odd dimensions.

