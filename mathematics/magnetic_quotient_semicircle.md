---

**Stable claim IDs:** BGS-CAYLEY-009.
title: "Magnetic quotients and a restricted global semicircle law"
author: "BGS research programme"
date: "5 September 2026"
---

# Status and scope

This is a complete project derivation, not a claim of priority or an externally
refereed theorem. It concerns the **global empirical spectral measure of a
compressed observable**, not microscopic BGS statistics of a quantum
propagator. The arithmetic restriction is strong: prime subgroup orders
$K=o(\log p)$. Section 9 proves that this regime is incompatible with the
orders of any one fixed hyperbolic integral cat map. The exact operator
identities and computational representation do not require that restriction.

The argument uses an explicit finite Heisenberg-group product, not the
historical unverified word-rewrite claims. Independent implementations check
its finite algebra; they are not substitutes for the limiting proof.

# 1. The exact matrix being studied

Let $p$ be an odd prime, let $H\leq\mathbb F_p^*$ have odd order $K$, and
let $q\in\mathbb F_p^*$. All exponents and fractions inside
$e_p(t)=\exp(2\pi i t/p)$ are interpreted in $\mathbb F_p$. On
$\mathbb C^{\mathbb F_p}$, with the counting-measure inner product, define
$$
 W(a,b)f(x)=e_p(a(x-b/2))f(x-b),\qquad W_q=W(q,1),
$$
$$
 S_hf(x)=f(h^{-1}x),\quad Q=\frac1K\sum_{h\in H}S_h,\quad
 R=S_{-1},\quad P_-=(I-R)/2.
$$
The projections $Q,P_-$ commute. Set
$$
 \mathcal E=\operatorname{ran}(QP_-),\quad n=\dim\mathcal E=\frac{p-1}{2K},
 \qquad B_q=W_q+W_q^*,
$$
$$
 A_q=(QB_qQ)|_{\mathcal E},\qquad X_q=\sqrt{K/2}\,A_q,
 \qquad \mu_m(q)=\frac1n\operatorname{Tr}_{\mathcal E}X_q^m. \tag{1}
$$
The dimension follows by using signed indicators of the nonzero orbits of
$H\cup(-H)$; odd functions vanish at zero. The identity $RW_qR=W_q^*$ shows
that $B_q$ preserves parity. Thus $A_q$ is Hermitian and $\|A_q\|\leq2$.
The notation $A_q$ here is an operator, not the Cayley set in other notes.

For each odd multiplicative character $\chi$ trivial on $H$, extend
$f_\chi(x)=\chi(x)/\sqrt{p-1}$ by zero at $x=0$. These form an orthonormal
basis of $\mathcal E$. Direct substitution gives
$$
 M_{\chi,\psi}=\frac{e_p(-q/2)}{p-1}
   \sum_{x\ne0,1}\overline{\chi(x)}\psi(x-1)e_p(qx),
 \qquad [A_q]=M+M^*. \tag{2}
$$
This is precisely the centered full-complex matrix in the maintained
`spectral_diagnostics.py`, not a surrogate ensemble. Compression of
$RW_qR=W_q^*$ to one parity sector also gives $M=M^*$; it does not make
$M$ entrywise real.

# 2. An explicit antiunitary and an isospectral real gauge

Define
$$
 (F_qf)(x)=p^{-1/2}\sum_y e_p(qxy)f(y),\qquad
 (Cf)(x)=\overline{f(x)},\qquad \Theta_q=F_qC.
$$
**Proposition 1.** The map $\Theta_q$ is an antiunitary involution preserving
$\mathcal E$ and commuting with $A_q$. For a nontrivial character,
$$
 \Theta_q f_\chi=a_\chi(q)f_\chi,\qquad
 a_\chi(q)=\frac{\chi(q)\tau(\overline\chi)}{\sqrt p},\qquad
 \tau(\overline\chi)=\sum_{y\ne0}\overline{\chi(y)}e_p(y),
 \quad |a_\chi(q)|=1. \tag{3}
$$
Choose any square roots $d_\chi^2=a_\chi(q)$ and put $D=\operatorname{diag}(d_\chi)$.
Then $D^*[A_q]D$ is real symmetric and has exactly the spectrum of $A_q$.

**Proof.** Fourier orthogonality gives $F_q\overline{F_q}=I$. Substitution
$y=z+1$ in $\Theta_qW_q$ gives
$$
 e_p(qxy-q(y-1/2))=e_p(q(x-1/2))e_p(q(x-1)z),
$$
which proves $\Theta_qW_q=W_q\Theta_q$. Changing variables in the Fourier
sum yields $\Theta_qS_h=S_{h^{-1}}\Theta_q$, hence invariance of $Q,R$.
For $x\ne0$, substitution $u=qxy$ proves (3); at zero the character sum
vanishes. Expanding the square of the Gauss sum and using orthogonality gives
$|\tau(\chi)|^2=p$. Finally
$\Theta_q(d_\chi f_\chi)=d_\chi f_\chi$. A commuting operator has real
entries in this fixed basis, and Hermiticity makes them symmetric. $\square$

This is a geometric conjugation, not conjugation chosen after diagonalizing
an arbitrary Hermitian matrix. Nonetheless an antiunitary symmetry alone is
not a GOE universality theorem. In particular, the old operation of taking
$[A_q].\mathrm{real}$ is not reinstated: it is generally not isospectral.

# 3. Orbit assembly with only p minus two contributions

Choose representatives $r_i$ of $\mathbb F_p^*/(H\cup-H)$. Let $i(x)$ be
the orbit index, and let $s(x)$ be $+1$ on $Hr_i$ and $-1$ on $-Hr_i$.
The orbit basis is $v_i(x)=s(x)/\sqrt{2K}$ on its orbit. Consequently
$$
 [M]^{\rm orb}_{ij}=\frac1{2K}
 \sum_{\substack{x\ne0,1\\i(x)=i,\ i(x-1)=j}}
 s(x)s(x-1)e_p(q(x-1/2)),\qquad
 [A_q]^{\rm orb}=M^{\rm orb}+(M^{\rm orb})^*. \tag{4}
$$
There are $p-2$ contributions, so sparse arithmetic assembly costs $O(p)$
and there are at most $O(p)$ nonzero locations before coalescing. This avoids
a naive $O(n^2p)$ character-sum construction. The reference implementation
returns a **dense** $n\times n$ matrix, so its storage is $O(n^2)$; sparse
assembly does not remove eigensolution costs. The overlap of the two
orthonormal bases proves exact unitary equivalence.

# 4. All-order trace identity with every word case included

The Weyl and dilation rules are
$$
 W(a,b)W(c,d)=e_p((ad-bc)/2)W(a+c,b+d),\qquad
 S_gW(a,b)S_g^{-1}=W(a/g,gb). \tag{5}
$$
Expand $(B_qQ)^m$ into words with $\epsilon_j\in\{-1,1\}$ and $h_j\in H$.
Starting with $(g,a,b,c)=(1,0,0,0)$, update at each letter by
$$
 a'=a+\epsilon/g,\quad b'=b+\epsilon g,\quad
 c'=c+\epsilon(ag-b/g)/2,\quad g'=gh. \tag{6}
$$
The product is $e_p(qc)W(qa,b)S_g$. Define
$$
 T_g(a,b)=
 \begin{cases}
 p\,\mathbf1_{a=b=0},&g=1,\\
 e_p\!\left(\dfrac{qab(1+g)}{2(1-g)}\right),&g\ne1.
 \end{cases} \tag{7}
$$
**Proposition 2.** For every integer $m\geq1$,
$$
 \operatorname{Tr}_{\mathcal E}A_q^m
 =\frac1{2K^m}\sum_{\epsilon_1,\ldots,\epsilon_m;\ h_1,\ldots,h_m}
   e_p(qc)\bigl(T_g(a,b)-T_{-g}(a,b)\bigr). \tag{8}
$$
**Proof.** A diagonal entry of $W(qa,b)S_g$ requires
$x=g^{-1}(x-b)$. For $g\ne1$, its unique solution is $x=b/(1-g)$, giving
(7). For $g=1$, one needs $b=0$; orthogonality of the remaining additive
character gives the first line, since $q\ne0$. Inserting $R$ changes $g$ to
$-g$ and $a,b$ to their negatives, preserving $ab$. The trace of the
compressed power equals $\operatorname{Tr}(P_-(B_qQ)^m)$ by cyclicity and
idempotence of $Q$. Expansion proves (8). Since $H$ has odd order, $-g$ is
never 1. No other cases are omitted. $\square$

In particular there is an integer, possibly signed, histogram $C_m(t)$ such
that
$$
 \operatorname{Tr} A_q^m=\frac1{2K^m}\sum_tC_m(t)e_p(qt),\qquad
 \mathbb E_{q\ne0}\operatorname{Tr} A_q^m
 =\frac{pC_m(0)-\sum_tC_m(t)}{2K^m(p-1)}. \tag{9}
$$
Histograms differing by a constant vector are equal at every nontrivial
$p$th root. Negative coefficients cannot be discarded.

# 5. Reciprocal short-relation rigidity

**Lemma 3.** Suppose $K$ is prime, $1\leq m<K$, and
$$
 p^2>m^{K-1}. \tag{10}
$$
If $t_j\in H$ and $\epsilon_j\in\{-1,1\}$ satisfy
$$
 \sum_j\epsilon_jt_j=\sum_j\epsilon_j/t_j=0\quad\text{in }\mathbb F_p,
 \tag{11}
$$
each label $t$ occurs equally often with positive and negative sign. In
particular $m$ is even.

**Proof.** Write $t_j=h^{e_j}$, $0\leq e_j<K$, and collect coefficients in
$P(Z)=\sum_j\epsilon_jZ^{e_j}$. Its coefficient $\ell^1$ norm is at most
$m$. If $P(\zeta_K)\ne0$, its norm $N$ is a nonzero integer with
$$
 |N|=\prod_{a=1}^{K-1}|P(\zeta_K^a)|\leq m^{K-1}. \tag{12}
$$
Multiplication by $P$ in $\mathbb Z[Z]/\Phi_K$ has determinant $N$. Modulo
$p$, $\Phi_K$ splits into distinct roots $h^a$, and (11) makes two distinct
eigenvalues zero, at $h,h^{-1}$. Its nullity is at least two; Smith normal
form then gives $p^2\mid N$, contradicting (10)--(12).
Thus $P(\zeta_K)=0$. Irreducibility of $\Phi_K$ follows from Eisenstein
applied after $Z\mapsto Z+1$. Since $\deg P\leq K-1$, we have
$P=c\Phi_K$ for an integer $c$. A nonzero $c$ would give coefficient
$\ell^1$ norm at least $K>m$. Hence $P=0$ coefficientwise, proving balance.
$\square$

Both reciprocal equations and the strict cutoff are used. This sufficient
cutoff is not an exact characterization of exceptional primes.

# 6. Main term and an explicit remainder

For words ending with $g=1$, put $t_1=1$ and
$t_j=h_1\cdots h_{j-1}$ for $j\geq2$. The labels $t_2,\ldots,t_m$ are
arbitrary in $H$, and the final $h_m$ is determined. The state becomes
$$
 a=\sum_j\epsilon_j/t_j,\quad b=\sum_j\epsilon_jt_j,\quad
 c=\frac12\sum_{i<j}\epsilon_i\epsilon_j(t_j/t_i-t_i/t_j).
$$
Equations (1) and (8) give
$$
 \mu_m(q)=\frac{p}{p-1}\frac{1}{2^{m/2}K^{m/2-1}}
 \sum_{\substack{t_1=1,\ t_2,\ldots,t_m\in H;\ \epsilon\\a=b=0}}
 e_p(qc)+\mathcal R_m(q), \tag{13}
$$
$$
 |\mathcal R_m(q)|\leq\frac{2^{m/2+1}K^{m/2+1}}{p-1}. \tag{14}
$$
Indeed every trace outside the $g=1,a=b=0$ contribution has modulus at most
one; bounding the two traces of each of $(2K)^m$ words by two gives (14).
Under Lemma 3 odd moments have no main term.

# 7. Pairings, overcounting, and crossing cancellation

Let $m=2r$. Every balanced tuple admits a matching of the $2r$ positions,
with equal labels and opposite signs on matched positions. Write
$$
 P_r=(2r-1)!!,\qquad C_r=\frac1{r+1}\binom{2r}{r}.
$$
These are the numbers of all and of noncrossing matchings. Order pairs by
their first endpoints, so pair 1 contains position 1. Assign labels
$x_1=1,x_2,\ldots,x_r\in H$ and orientations $\sigma_i\in\{-1,1\}$.
With distinct labels the matching is unique. Overcounting is possible only
when two labels coincide. A union bound bounds the number of bad matching
assignments by
$$
 P_r2^r\binom r2 K^{r-2}, \tag{15}
$$
interpreted as zero for $r=1$. Each balanced tuple has at least one matching;
therefore (15) also bounds the excess multiplicity of the replacement sum.

Summing the four interactions between two matched pairs gives the exact
Laurent polynomial
$$
 F_{\pi,\sigma}(x)=\sum_{\substack{i<j\\\text{pairs }i,j\text{ cross}}}
 \sigma_i\sigma_j(x_j/x_i-x_i/x_j). \tag{16}
$$
Disjoint or nested pairs give zero; interlaced pairs give the indicated term.
Noncrossing matchings have $F=0$. Any crossing matching has nonconstant $F$:
each crossing contributes two unique directed-ratio monomials with opposite
unit coefficients. After $x_1=1$, the monomials involving pair 1 become
$x_j,x_j^{-1}$ and remain distinct from every other term. Thus they cannot
cancel in odd characteristic.

For a crossing let $d=r-1$ and
$$
 S_F(q)=K^{-d}\sum_{x\in H^d}e_p(qF(x)).
$$
Multiplication of $F(x)-F(y)$ by all $2d$ variables clears denominators and
gives a nonzero polynomial of total degree at most $2d+1=2r-1$. The grid
zero bound therefore gives at most $(2r-1)K^{2d-1}$ equal-value pairs.
For completeness, that bound follows by induction on the number of variables:
separate the leading coefficient in the last variable, use the univariate
root bound off its zero set, and induct on that coefficient on the remaining
fibres. Additive orthogonality now yields
$$
 \mathbb E_{q\ne0}|S_F(q)|^2
 =\frac{pK^{-2d}\#\{(x,y):F(x)=F(y)\}-1}{p-1}
 \leq\frac{p(2r-1)}{(p-1)K}. \tag{17}
$$
This uses no independence assumption for matrix entries, words, or crossings.

# 8. Quantitative theorem and limiting law

**Theorem 4.** Let $K$ be an odd prime and let $p$ be prime with $K\mid p-1$.
For $2r<K$ and $p^2>(2r)^{K-1}$, uniform nonzero $q$ satisfies
$$
\begin{aligned}
 \|\mu_{2r}-C_r\|_{L^2(q\ne0)}\leq{}&\frac{C_r}{p-1}\\
 &+\frac p{p-1}(P_r-C_r)
       \sqrt{\frac{p(2r-1)}{(p-1)K}}\\
 &+\frac p{p-1}\frac{P_r\binom r2}{K}
       +\frac{2^{r+1}K^{r+1}}{p-1}.
\end{aligned} \tag{18}
$$
For odd $m<K$ under $p^2>m^{K-1}$,
$$
 \sup_{q\ne0}|\mu_m(q)|\leq
       \frac{2^{m/2+1}K^{m/2+1}}{p-1}. \tag{19}
$$
**Proof.** Replace the balanced tuples of (13) by matching assignments.
After division by $2^rK^{r-1}$, (15) gives the third term of (18).
Each noncrossing matching contributes exactly one; together they give
$pC_r/(p-1)$, whose difference from $C_r$ is the first term. For each
crossing average over its $2^r$ orientations, apply (17), and apply the
$L^2$ triangle inequality over the $P_r-C_r$ matchings. This is the second
term. The last term is (14). Lemma 3 and (14) give (19). $\square$

**Corollary 5 (global law only).** Suppose $K\to\infty$ through odd primes,
$p\equiv1\pmod K$ is prime, and $K=o(\log p)$. Every fixed moment of the
empirical spectral measure of $X_q$ converges in $L^2$ over nonzero $q$ to
the standard semicircle moment. The empirical measures converge weakly in
probability to
$$
 \rho_{\rm sc}(x)\,dx=\frac{\sqrt{4-x^2}}{2\pi}
       \mathbf1_{[-2,2]}(x)\,dx. \tag{20}
$$
The averaged empirical measures converge weakly as well.

**Proof.** For every fixed $m$, eventually $m<K$ and (10) holds, while every
fixed power of $K$ divided by $p$ tends to zero. Equations (18)--(19) give
the moment limits. From any subsequence, select a further subsequence on
which all integer moments converge almost surely, by diagonal extraction.
Bounded second moments give tightness; bounded higher even moments give
uniform integrability for each lower moment. Every weak subsequential limit
therefore has the semicircle moments. Since $C_r\leq4^r$, any measure with
these moments is supported on $[-2,2]$; polynomial approximation on that
compact interval proves uniqueness. The subsequence criterion gives weak
convergence in probability. Bounded continuous tests then also converge in
expectation, proving the averaged assertion. $\square$

This does not assert eigenvalue rigidity, an edge law, microscopic spacing
statistics, or estimates uniform for $m$ growing with $n$.

# 9. Obstruction for one fixed cat map and remaining work

Let $T\in\mathrm{SL}_2(\mathbb Z)$ be one fixed hyperbolic matrix with
order $K$ modulo $p$. Then $T^K-I$ vanishes modulo $p$. At least one of its
integer entries is nonzero, and its absolute value is at most
$C_T\Lambda_T^K$, for constants depending only on $T$. Hence
$$
 p\leq C_T\Lambda_T^K,\qquad
 \log p\leq K\log\Lambda_T+\log C_T. \tag{21}
$$
Thus $K=o(\log p)$ is impossible along such an order sequence. On the split
semisimple locus the eigenvalue order equals the matrix order, so that
interpretation does not avoid the obstruction.

The new global law is a theorem about an arithmetic matrix-design regime,
not a fixed-cat-map BGS theorem. The exact trace formula, antiunitary, and
orbit assembly remain valid outside the cutoff. The next substantive step
is to control non-balanced reciprocal words in polynomial regimes rather
than eliminate them with an exponential norm bound. Microscopic BGS then
still requires a specified desymmetrized propagator and Heisenberg-scale
joint-trace estimates. Neither assertion is proved here.

# 10. Verification and related work

The maintained regression checks 14 integer histograms against a separate
C++ affine-fixed-point implementation, 32,054 oriented pairings through
$r=5$, three matrix representations, Gauss rephasing, and finite reciprocal
cutoffs. Floating matrix agreement and exact finite certificates are labeled
separately. The Lean module records small finite trace certificates only;
it is not a formalization of Theorem 4 or Corollary 5.

Semicircle laws in finite harmonic analysis are not new in general. Gurevich
and Hadani study normalized Gram fluctuations of incoherent dictionaries
(arXiv:0812.2602). Forey, Fresan, Kowalski, and Wigderson construct arithmetic
graph families with global semicircle spectra (arXiv:2511.21351) and introduce
Jacobian graphs (arXiv:2603.13198). Rosenzweig studies fluctuations of cat-map
matrix elements (arXiv:0909.1410). These are relevant comparison objects, not
unverified inputs to the proof above. The source audit does not establish
priority for this particular compressed-observable theorem.
