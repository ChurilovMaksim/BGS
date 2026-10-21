> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round9_2026_10_21/r9_sector_continuous_symbol_stability.md`. Embedded SHA256: `0145256f03ad92f70a5852ecb11280dc3b1bccfa54b74af8b70e459b2e6577df`.
> [Thematic guide](../../topics/arithmetic.md).

# Continuous-symbol microscopic stability by analytic diagonal approximation

21 October 2026. Branch `/root/r9_sector_coherence`.

## 0. Result and exact scope

The Round 3 file `subprincipal_stability_theorem.md` already proves
microscopic stability and full all-order $H_{\rm diag}$ equivalence
for $N^{-1}$-sized generators in a fixed compact smooth-symbol family.
Repeating its uniform QE or moment-transfer argument is not new work.

This note proves a strictly broader approximation theorem. **Every fixed
real continuous function on the torus admits a slowly varying sequence
of real trigonometric-polynomial generators whose exact unitary
perturbations of the prescribed family have the same limiting local
laws and the same validity or failure of full $H_{\rm diag}$.** The
polynomial degrees and their smooth seminorms may tend to infinity.
One may impose any countable list of additional fixed-polynomial
semiclassical accuracy requirements by increasing the dimension
thresholds. All odd dimensions are retained.

This supplies the spectral-stability part of an actual unitary
realization of the continuous first scalar cocycle correction.
The separate analytic construction and its independent audit are
identified in Section 8.
It does not prove the full weighted pair sum, and does not justify
summing a pointwise relative orbit error through an exponentially
large oscillatory orbit sum.

No anti-Wick calculus or unproved boundedness of Weyl quantization on
all continuous symbols is assumed. The construction uses the actual
ordinary torus Weyl quantization on polynomial symbols and an
elementary fixed-symbol norm bound.

## 1. Exact quantization and the inputs actually needed

For odd $N$, put

$$
 Q_N(a)=\sum_{\kappa=(k,l)\in\mathbb Z^2}
 \widehat a(\kappa)W_N(\kappa),\qquad
 W_N(k,l)=(-1)^{kl}T_N(l,k).
 \tag{1.1}
$$

For smooth $a$, the sum converges absolutely in operator norm.
For real $a$, $Q_N(a)$ is self-adjoint. Integer frequencies are
retained before reduction modulo $N$, including the indicated signs.
Direct multiplication gives

$$
 W_N(\kappa)W_N(\eta)
 =\exp\!\left(\frac{\pi i\omega(\kappa,\eta)}N\right)
 W_N(\kappa+\eta),\qquad
 \omega((k,l),(k',l'))=lk'-kl'.
 \tag{1.2}
$$

Two previously derived properties of the exact initial $U_N$ are
used below:

$$
 U_N^{-r}Q_N(a)U_N^r=Q_N(a\circ\Psi^r)+o_{a,r}(1)
 \quad\text{in operator norm for every fixed }a,r,
 \tag{1.3}
$$

and

$$
 \frac1N\operatorname{Tr}(Q_N(a)^*Q_N(c))
 \longrightarrow\int_{\mathbb T^2}\overline a c.
 \tag{1.4}
$$

Here $\Psi$ is the actual principal map, which preserves normalized
area and is ergodic. The fixed-time proof and normalization in Round 3,
Sections 1--3, were read in full for this use. Its proof of (1.3) uses
the exact finite Weyl commutator, Duhamel along the actual Schrödinger
kick, and exact covariance for $M_N$; its proof of (1.4) estimates the
nonzero alias frequencies by rapid Fourier decay. Neither uses
Heisenberg-time trace estimates or quantum universality.

For an independent way to obtain the required classical ergodicity,
the actual Fourier operator calculation in the classical source,
Section 3, was also read. It constructs

$$
 R_{nk}=\frac{w_n}{w_k}\langle e_n,e_k\circ\Psi\rangle,
 \qquad R=1\oplus R_\perp,\quad \|R_\perp\|<1,
 \tag{1.5}
$$

as a trace-class operator. For fixed $n,k,r$, finite Fourier
truncations telescope their weights; passage to the limit uses
operator-norm convergence of the truncations of $R$, and strong
convergence of the corresponding truncated unitary Koopman operators.
Therefore

$$
 (R^r)_{nk}=\frac{w_n}{w_k}
 \langle e_n,e_k\circ\Psi^r\rangle.
 \tag{1.6}
$$

For mean-zero trigonometric polynomials $a,c$, their finite Fourier
supports and (1.5)--(1.6) give
$|\langle c,a\circ\Psi^r\rangle|\le C_{a,c}\|R_\perp\|^r$.
Approximation by trigonometric polynomials and the $L^2$ isometry of
composition by $\Psi$ extend mixing to $L^2$, hence imply
ergodicity. This route requires no new invocation of a general
Anosov-ergodicity theorem. The explicit operator-norm bound in (1.5)
is the already computed classical bound, not an estimate for
$\operatorname{Ad}U_N$.

## 2. A fixed-symbol norm estimate with an elementary proof

### Lemma 2.1

For every fixed real smooth $a$,

$$
 \limsup_{N\to\infty,\;N\text{ odd}}\|Q_N(a)\|_{\rm op}
 \le\|a\|_\infty.
 \tag{2.1}
$$

**Proof.** Equation (1.2) and $|e^{iu}-1|\le|u|$ imply, for fixed
smooth $a,c$,

$$
 \|Q_N(a)Q_N(c)-Q_N(ac)\|
 \le\frac\pi N\sum_{\kappa,\eta}
 |\widehat a(\kappa)\widehat c(\eta)|
 |\omega(\kappa,\eta)|=O_{a,c}(N^{-1}).
 \tag{2.2}
$$

Fix $M>\|a\|_\infty$. The function

$$
 c=(M^2-a^2)^{1/2}
$$

is real and smooth, because its radicand is bounded below by a
positive constant. Both $Q_N(a)^2$ and $Q_N(c)^2$ are positive
semidefinite. Equation (2.2) gives

$$
 Q_N(a)^2+Q_N(c)^2=M^2I+O_{a,M}(N^{-1}).
 \tag{2.3}
$$

Hence $\|Q_N(a)\|^2\le M^2+O_{a,M}(N^{-1})$. Take the limit
superior and then $M\downarrow\|a\|_\infty$. This proves (2.1).

This argument does **not** say that $\|Q_N(a)\|\le\|a\|_\infty$
for every $N$, or that $Q_N$ is bounded on the entire space
$C^0$ uniformly in $N$. Only fixed smooth symbols enter (2.1).

## 3. The diagonal construction

Fix an arbitrary real $v\in C(\mathbb T^2)$. Let $v_j$ be its
rectangular two-dimensional Fejér approximants. Equivalently,

$$
 \widehat v_j(k,l)=
 \left(1-\frac{|k|}{j+1}\right)_+
 \left(1-\frac{|l|}{j+1}\right)_+
 \widehat v(k,l).
 \tag{3.1}
$$

They are real trigonometric polynomials and satisfy

$$
 \|v_j-v\|_\infty\longrightarrow0,
 \qquad \|v_j\|_\infty\le\|v\|_\infty,
 \qquad \int v_j=\int v=:\bar v.
 \tag{3.2}
$$

For completeness, the one-dimensional Fejér kernel is

$$
 F_j(t)=\frac1{j+1}\left|\sum_{r=0}^je^{2\pi irt}\right|^2.
$$

It is nonnegative, has integral one and, for fixed distance
$\delta>0$ from the integers, is bounded by
$(j+1)^{-1}\sin^{-2}(\pi\delta)$. Its product in two coordinates
therefore forms an approximate identity. Splitting convolution into
a small neighborhood, where uniform continuity controls the error,
and its complement proves all assertions in (3.2).

Use Lemma 2.1 to choose increasing finite thresholds $n_j$, with
$n_j\ge2j+3$, such that every odd $N\ge n_j$ obeys

$$
 \|Q_N(v_j)\|\le\|v\|_\infty+\frac1j,
 \tag{3.3}
$$

and, simultaneously for every $1\le l\le j$,

$$
 \|Q_N(v_j-v_l)\|
 \le\|v_j-v_l\|_\infty+\frac1j.
 \tag{3.4}
$$

Only finitely many fixed symbols are involved at each stage, so the
threshold exists. It may be increased arbitrarily. Require also
$n_j>n_{j-1}$, and set

$$
 j(N)=\max\{j:n_j\le N\},\qquad B_N=Q_N(v_{j(N)}),
 \tag{3.5}
$$

once the set is nonempty. Define the finitely many earlier $B_N$
arbitrarily. All odd dimensions occur, and $j(N)\to\infty$.

The operators $B_N$ are self-adjoint and uniformly bounded.
Furthermore, for every fixed $l$,

$$
 \limsup_{N\to\infty}\|B_N-Q_N(v_l)\|
 \le\|v-v_l\|_\infty\longrightarrow0\quad(l\to\infty).
 \tag{3.6}
$$

Because $N>2j(N)$, no nonconstant frequency of $v_{j(N)}$
aliases to zero. Consequently the mean is exact:

$$
 \frac1N\operatorname{Tr}B_N=\bar v.
 \tag{3.7}
$$

### Incorporating arbitrary additional fixed-stage requirements

Suppose for each stage $j$ an independently proved estimate holds
for all sufficiently large odd $N$, with error $E_j(N)\to0$.
Increasing $n_j$ so that $|E_j(N)|\le1/j$ for every odd
$N\ge n_j$ preserves (3.3)--(3.7). The same applies to any
finite initial list of a countable collection of such requirements
at stage $j$. This is a single sequence through all odd $N$,
not a selected subsequence of dimensions.

For example, if a fixed-stage graph expansion has remainder
$C_jh^2$, impose $C_j/N\le1/j$, along with its fixed-stage
small-$h$ threshold. This makes that remainder $o(h)$ along
the diagonal. No common bound on $C_j$ or common analytic strip
is asserted before this choice.

## 4. Uniform QE for the varying continuous-symbol approximation

Set

$$
 V_N(s)=e^{isB_N/N}U_N,\qquad 0\le s\le1.
 \tag{4.1}
$$

Then $V_N(s)$ is exactly unitary and

$$
 \sup_s\|V_N(s)-U_N\|\le\|B_N\|/N=O(N^{-1}).
 \tag{4.2}
$$

For every fixed smooth $a$ and fixed $r$, a finite telescoping
of $r$-th powers combines (4.2) and (1.3) to give

$$
 \sup_s\|V_N(s)^{-r}Q_N(a)V_N(s)^r
              -Q_N(a\circ\Psi^r)\|\longrightarrow0.
 \tag{4.3}
$$

For any eigenbasis $\{\psi_j\}$ of $V_N(s)$, time averaging
preserves diagonal expectations. If $a$ is fixed and mean zero,
let

$$
 A_{N,s,T}=\frac1T\sum_{r=0}^{T-1}
 V_N(s)^{-r}Q_N(a)V_N(s)^r,
 \qquad a_T=\frac1T\sum_{r=0}^{T-1}a\circ\Psi^r.
$$

The elementary diagonal Hilbert--Schmidt bound yields

$$
 \frac1N\sum_j|\langle\psi_j,Q_N(a)\psi_j\rangle|^2
 \le\frac1N\operatorname{Tr}(A_{N,s,T}^*A_{N,s,T}).
 \tag{4.4}
$$

For fixed $T$, equations (4.3) and (1.4) imply that the right
side tends to $\|a_T\|_2^2$, uniformly in $s$. Ergodicity
gives $\|a_T\|_2\to0$. Thus

$$
 \sup_{s,\,\mathcal E}\frac1N\sum_{\psi_j\in\mathcal E}
 |\langle\psi_j,Q_N(a)\psi_j\rangle|^2\longrightarrow0,
 \tag{4.5}
$$

where the supremum includes every orthonormal eigenbasis, including
all choices inside degenerate eigenspaces.

Now center $B_N$ by its exact scalar $\bar v$. For fixed $l$,
the triangle inequality in normalized $\ell^2$ gives

$$
 \begin{split}
 &\left(\frac1N\sum_j
 |\langle\psi_j,(B_N-\bar v I)\psi_j\rangle|^2\right)^{1/2}
 \\
 &\quad\le
 \left(\frac1N\sum_j
 |\langle\psi_j,Q_N(v_l-\bar v)\psi_j\rangle|^2\right)^{1/2}
 +\|B_N-Q_N(v_l)\|.
 \end{split}
 \tag{4.6}
$$

Take the supremum over $s$ and eigenbases, then the limit superior
as $N\to\infty$, and use (4.5) and (3.6). Finally let
$l\to\infty$. We have proved

$$
 q_N:=\sup_{s,\,\mathcal E}\frac1N\sum_{\psi_j\in\mathcal E}
 |\langle\psi_j,(B_N-\bar v I)\psi_j\rangle|^2
 \longrightarrow0.
 \tag{4.7}
$$

No derivatives of $v$, $v_{j(N)}$, or their classical iterates
appear in this final passage. Fixed-time semiclassical correspondence
is used only for one fixed polynomial $v_l$ at a time.

## 5. Eigenangle motion, including crossings

Choose absolutely continuous real lifts $\theta_j(s)$ of the
eigenangles of $V_N(s)$, in turns. Such branches can be obtained
locally by choosing a spectral cut, taking a Hermitian logarithm,
and using its ordered Lipschitz eigenvalues. On overlap intervals
the branches are matched by permutations and integer shifts.

At almost every $s$, their slopes are the eigenvalues of the
compression of $B_N/(2\pi N)$ to each degenerate eigenspace.
Choosing an orthonormal basis diagonalizing these compressions gives

$$
 \theta_j'(s)=\frac1{2\pi N}
 \langle\psi_j(s),B_N\psi_j(s)\rangle.
 \tag{5.1}
$$

This follows at a simple eigenvalue by differentiating its eigenvalue
equation. Restriction of that differentiated equation to a repeated
eigenspace gives the compression statement. Global differentiable
eigenvectors and lower bounds on gaps are unnecessary.

The generator norm gives

$$
 \max_j N|\theta_j(s)-\theta_j(0)|\le C_0.
 \tag{5.2}
$$

Set $\phi_N(s)=s\bar v/(2\pi N)$. Equations (5.1) and (4.7),
followed by Cauchy--Schwarz in the eigenstate index, yield

$$
 \begin{split}
 \eta_N&:=\sup_{0\le s\le1}\sum_j
 |\theta_j(s)-\theta_j(0)-\phi_N(s)|
 \\
 &\le\frac1{2\pi}\sqrt{q_N}\longrightarrow0.
 \end{split}
 \tag{5.3}
$$

The centered microscopic displacements remain bounded by a fixed
constant, by (5.2). The scalar rotation $\phi_N(s)$ is exact and
is invisible to the uniform random origin.

## 6. Transfer of weak local laws and all factorial moments

This section records explicitly why no uniform-integrability
assumption is hidden in the $H_{\rm diag}$ conclusion.

After removing the scalar rotation, let the matched endpoints have
angle differences $\varepsilon_j$, with

$$
 \sum_j|\varepsilon_j|\le\eta_N\to0,
 \qquad \max_jN|\varepsilon_j|\le C.
 \tag{6.1}
$$

Couple their point processes with the same uniform origin. For
$f\in W^{1,1}(\mathbb R)$, the exact change of variables over the
origin and periodized copies gives

$$
 \begin{split}
 \mathbb E\sum_{j,\ell}
 |f(N(\theta_j+\varepsilon_j-\alpha+\ell))
       -f(N(\theta_j-\alpha+\ell))|
 &=\frac1N\sum_j\|f(\cdot+N\varepsilon_j)-f\|_1\\
 &\le\|f'\|_1\eta_N.
 \end{split}
 \tag{6.2}
$$

Consequently, for every nonnegative $f\in C_c^\infty$,

$$
 |\mathbb E e^{-\langle f,\Xi_N^1\rangle}
  -\mathbb E e^{-\langle f,\Xi_N^0\rangle}|
 \le\|f'\|_1\eta_N\to0.
 \tag{6.3}
$$

The same coupling on a countable family of test functions generating
the vague topology gives convergence to zero in a bounded metric
between the laws. Thus the endpoints have exactly the same weak
local limits, whenever such limits exist.

Suppose now that one endpoint satisfies the full requested
$H_{\rm diag}$. For any fixed compact interval $I$, choose an
admissible nonnegative bandlimited Schwartz test $\beta$ bounded
below by a positive constant on $I$. This is possible by taking
the squared modulus of the inverse Fourier transform of a smooth
compact bump with nonzero integral, dilating, translating, and
rescaling. For all sufficiently large $N$, its periodized label
weights lie in $[0,1]$. If their sum is $Z$, expansion by
distinct labels gives

$$
 Z^p\le\sum_{r=1}^p r!\,S(p,r)e_r(w_1,\ldots,w_N),
 \tag{6.4}
$$

where $S(p,r)$ is a Stirling number. Source $H_{\rm diag}$
and the finite CUE bound $M_{r,N}^{\rm CUE}(\beta)
\le(\int\beta)^r/r!$ therefore imply bounded moments of all
orders for the source count in $I$.

Bounded microscopic matching gives pointwise

$$
 \Xi_N^{\rm target}(I)
 \le\Xi_N^{\rm source}(I+[-C,C]).
 \tag{6.5}
$$

It supplies all target count moments as well. The random-origin laws
are stationary on the real line, so these bounds are uniform over
translates of a fixed interval. For any Schwartz $b$, put
$c_n=\sup_{x\in[n,n+1]}|b(x)|$. Since $\sum_n c_n<\infty$,
Minkowski's inequality gives

$$
 \sup_N\mathbb E\langle|b|,\Xi_N^0+\Xi_N^1\rangle^p<\infty
 \quad\text{for every fixed }p.
 \tag{6.6}
$$

Now write $w_j^i=b_N(\theta_j^i-\alpha)$,
$D_N=\sum_j|w_j^1-w_j^0|$, and
$S_N=\sum_j(w_j^0+w_j^1)$. Telescoping each distinct-label
product yields

$$
 |e_k(w^1)-e_k(w^0)|\le\frac{D_NS_N^{k-1}}{(k-1)!}.
 \tag{6.7}
$$

Equation (6.2) gives $\mathbb ED_N\le\|b'\|_1\eta_N$.
On $S_N\le R$, use this bound; on $S_N>R$, use
$D_N\le S_N$ and (6.6) at order $k+1$. Then

$$
 |M_{k,N}^1(b)-M_{k,N}^0(b)|
 \le\frac{R^{k-1}\|b'\|_1\eta_N+C_{k+1,b}/R}{(k-1)!}.
 \tag{6.8}
$$

First let $N\to\infty$, then $R\to\infty$. Reversing the
matching proves the converse implication. Therefore

$$
 \boxed{H_{\rm diag}(U_N)\quad\Longleftrightarrow\quad
 H_{\rm diag}(e^{iQ_N(v_{j(N)})/N}U_N).}
 \tag{6.9}
$$

This equivalence is proved for the constructed diagonal family,
not merely for each fixed polynomial separately.

## 7. A canonical continuous-symbol endpoint and an actual norm error

There is also a simple positive quantization of the continuous target
itself. Its construction makes the comparison with the diagonal
analytic endpoint an actual $o(N^{-1})$ operator-norm statement.

Represent residues $x$ by centered integers. Set

$$
 L_N=\lfloor\sqrt N\rfloor,\qquad
 \varphi_N(x)=\frac{\mathbf1_{|x|\le L_N}}{\sqrt{2L_N+1}},
 \qquad \rho_N=|\varphi_N\rangle\langle\varphi_N|,
 \tag{7.1}
$$

for sufficiently large odd $N$. The finitely many earlier choices
can be any unit vector. For $a\in C(\mathbb T^2)$, define

$$
 Q_N^+(a)=\frac1N\sum_{u,v\in\mathbb Z/N\mathbb Z}
 a(-u/N,v/N)\,T_N(u,v)\rho_NT_N(u,v)^*.
 \tag{7.2}
$$

Finite Weyl orthogonality gives the exact twirling identity

$$
 \sum_{u,v}T_N(u,v)\rho_NT_N(u,v)^*=NI.
 \tag{7.3}
$$

One direct proof expands $\rho_N$ in the orthogonal Weyl basis.
Conjugation multiplies each nonidentity Weyl term by a nonconstant
character of $(u,v)$; summing kills all of them. The identity
coefficient is $\operatorname{Tr}\rho_N/N=1/N$, producing $NI$.

Consequently $Q_N^+$ is positive, unital, and, for real $a,c$,

$$
 \|Q_N^+(a)-Q_N^+(c)\|\le\|a-c\|_\infty.
 \tag{7.4}
$$

The sampling coordinates in (7.2) are essential: a Weyl translate
$T_N(u,v)\varphi_N$ is centered at position $-u/N$ and
momentum $v/N$, with the conventions of this problem.

For $e_\kappa(q,p)=e^{2\pi i(kq+lp)}$, the same character
orthogonality gives exactly

$$
 Q_N^+(e_\kappa)=\chi_N(\kappa)W_N(\kappa),\qquad
 \chi_N(\kappa)=\langle\varphi_N,W_N(\kappa)^*\varphi_N\rangle.
 \tag{7.5}
$$

For each fixed $\kappa=(k,l)$, $\chi_N(\kappa)\to1$.
Indeed, on the overlap of the two indicator packets there is no
wraparound for large $N$, and the ordinary Weyl phase is
$e^{2\pi ik(x+l/2)/N}$. The overlap loses at most $|l|$
sites, and the midpoint has absolute value at most $L_N$. Thus

$$
 |1-\chi_N(k,l)|
 \le\frac{|l|}{2L_N+1}+\frac{2\pi |k|L_N}{N}
 \longrightarrow0.
 \tag{7.6}
$$

It follows by a finite Fourier sum that, for every fixed polynomial
$a$,

$$
 \|Q_N^+(a)-Q_N(a)\|\longrightarrow0.
 \tag{7.7}
$$

The statement also holds for fixed smooth $a$, by absolute Fourier
summation, but polynomial approximation suffices below.

For the continuous target $v$ and the actual diagonal generator
$B_N$ of Section 3, use a fixed $v_l$ as an intermediate
observable. Equations (3.6), (7.4), and (7.7) give

$$
 \begin{split}
 \limsup_N\|B_N-Q_N^+(v)\|
 &\le\limsup_N\|B_N-Q_N(v_l)\|
    +\|v_l-v\|_\infty\\
 &\le2\|v_l-v\|_\infty.
 \end{split}
$$

Letting $l\to\infty$ proves

$$
 \boxed{\|B_N-Q_N^+(v)\|=o(1).}
 \tag{7.8}
$$

Both operators are self-adjoint. The exact Duhamel identity for their
unitary exponentials therefore gives

$$
 \boxed{\left\|e^{iB_N/N}U_N-e^{iQ_N^+(v)/N}U_N\right\|
 \le\frac{\|B_N-Q_N^+(v)\|}{N}=o(N^{-1}).}
 \tag{7.9}
$$

This is an operator-norm bound on the actual $N$-dimensional
Hilbert space. Its comparison endpoint is an exactly unitary
continuous-symbol perturbation, not a formal edited trace sum.

The canonical endpoint itself has the same local-law and
$H_{\rm diag}$ conclusions. To see this without importing any
general perturbation principle, note that

$$
 \limsup_N\|Q_N^+(v)-Q_N(v_l)\|
 \le\|v-v_l\|_\infty.
 \tag{7.10}
$$

The uniform QE proof in Section 4 applies verbatim with
$B_N=Q_N^+(v)$. Center by $\bar v=\int v$; the continuous
Riemann-sum formula
$N^{-1}\operatorname{Tr}Q_N^+(v)=N^{-2}\sum_{u,w}v(-u/N,w/N)\to\bar v$
is consistent with this centering, and the QE estimate itself
already controls the difference. Sections 5--6 then apply. Therefore

$$
 H_{\rm diag}(U_N)
 \Longleftrightarrow H_{\rm diag}(e^{iB_N/N}U_N)
 \Longleftrightarrow H_{\rm diag}(e^{iQ_N^+(v)/N}U_N).
 \tag{7.11}
$$

No claim is made that $Q_N^+(v)$ has an analytic oscillatory kernel
when $v$ is merely continuous. The analytic diagonal endpoint is
the one used for the separate scalar-cocycle construction.

## 8. What this does and does not remove in the scalar-cocycle route

The old scalar-cocycle construction gives a fixed continuous real
$\sigma$ through

$$
 \gamma_h(x)=\gamma_0(x)
 (1+ih\sigma(x)+O(h^2)),\qquad h=(2\pi N)^{-1}.
 \tag{8.1}
$$

Its graph is constructed by a uniform contraction in continuous
sections. Smoothness of $\sigma$ was not proved and is not assumed
here. The relevant continuous target for phase removal is

$$
 v=-\frac{\sigma\circ\Psi^{-1}}{2\pi}.
 \tag{8.2}
$$

The theorem above applies to this target without any smoothness
assumption. It constructs actual exactly unitary analytic-polynomial
endpoints $e^{iQ_N(v_{j(N)})/N}U_N$ and proves their complete
spectral-statistics equivalence with the original family.

**Separate analytic input for the phase statement.** For each fixed
polynomial $v_j$, the exact kernel/graph construction for the actual
exponential multiplier gives

$$
 \frac{\gamma_h^{(j)}(x)}{\gamma_0(x)}
 =1+ih\bigl(\sigma(x)+2\pi v_j(\Psi x)\bigr)+O_j(h^2),
 \tag{8.3}
$$

uniformly in the real base point. This statement, including the
actual analytic kernel, the fixed-polynomial remainder, and the
exact all-time sector construction, is proved in the separate
Round 9 root_diagonal_cocycle_normalization.md, Sections 2--4.
Its raw analytic proof was independently checked in
r9_sector_analytic_normalization_independent_audit.md.
Those are the inputs used here; the older first-jet transformation
law by itself would not have established the exact kernel assertion.

Combining (8.3) with its fixed-stage threshold, the diagonal
construction enforces $C_j/N\le1/j$ for its remainder constant.
Because $v_j\to v$ uniformly, it follows rigorously that

$$
 \sup_x\left|\frac{\gamma_{h_N}^{(j(N))}(x)}{\gamma_0(x)}-1\right|
 =o(N^{-1}).
 \tag{8.4}
$$

For every fixed $B>0$, a product estimate then gives

$$
 \sup_{1\le m\le BN}\sup_x
 \left|\prod_{r=0}^{m-1}
 \frac{\gamma_{h_N}^{(j(N))}(\Psi^rx)}{\gamma_0(\Psi^rx)}-1\right|
 \longrightarrow0.
 \tag{8.5}
$$

This last implication is elementary: if the uniform one-step error
is $a_N=o(N^{-1})$, the left side is at most
$(1+a_N)^{BN}-1\le e^{BN a_N}-1\to0$.

Neither (8.4) nor (8.5) implies a small error after taking an absolute
sum over exponentially many periodic points. The remaining principal
action phases still require their full coherent cancellation. In
particular, there is no proof here of

$$
 \frac1{N^2}\sum_{1\le m<2N}|\widehat b_*(m/N)|^2
 \left(|\operatorname{Tr}U_N^m|^2-\min(m,N)\right)\to0.
 \tag{8.6}
$$

## 9. Provenance and avoided duplicates

All hashes below were computed on the actual files read in this
branch. No historical source or master document was changed.

| Source | SHA-256 |
|---|---|
| research_round9_2026_10_21/root_diagonal_cocycle_normalization.md | afeaa52cea23836c5b4fa58d1040daa6df792d0b9adea83f8eb1de8690211921 |
| research_round9_2026_10_21/r9_sector_analytic_normalization_independent_audit.md | 0fc9a15bcccab691e2912e64c4d018aba8c822494d00ad848d468fbb5933cd51 |
| `research_round3_2026_10_21/subprincipal_stability_theorem.md` | `63597dea1e627925280e79644ccc54ed68b9327c9ab757f6eea9ad69962e2381` |
| `research_continuation_2026_10_20/classical_trace_and_pair_diagonal.md` | `355f2c6deb1549c32ab7b7313774b8c27b1310d019013838fc5e3679721af55c` |
| `research_continuation_2026_10_20/gaussian_cocycle_and_modulus.md` | `c1a863e613a327acb5fe43ff1093c4a8fe51b37ebd5dcee9fddf0ae0a91986f1` |
| `research_round8_2026_10_21/r8_weyl_all_odd_endpoint_fiber_identity.md` | `ec36b997ef3a38dd464d468833f78a3934b45bdc57dbc36f54987aa42a649b70` |
| `research_round8_2026_10_21/r8_weyl_full_weight_relative_path_cancellation.md` | `038d6c03710c38829fba3d96367d271f5c33cdeacf94889d32cc3d7a22070109` |
| `research_round5_2026_10_21/root_physical_cycle_classes.md` | `de9d6a510aa9c6e36f30a1d42d7c5e3760e71e594cbf0335a4c1a1653ac7708d` |

The all-odd endpoint identities, complete cyclic physical-path ramp,
long-arc reconnection cancellation, occupation-sector resummation,
and fixed smooth-generator stability were inspected before this
construction. They were already established in earlier rounds and
are not relabeled as new Round 9 results.
