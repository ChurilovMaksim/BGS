---
title: "Smooth observables, Fourier cohomology, and two arithmetic resonance scales"
author: "WoW research programme"
date: "5 September 2026"
---

# Status and main statements

This is a project derivation, with proofs and separately scoped finite checks.
It is not a claim of priority, a complete Lean formalization, or a solution of
fixed-system BGS. The new scope relative to the one- and two-frequency notes
is the entire class of real, even, smooth observables of one fixed cat map.
Classical Green--Kubo variance, coboundaries, and the second-order residual
perturbation mechanism are prior mathematics and physics, not inventions
claimed here. The proposed contribution is their deterministic, quantitatively
controlled combination at arithmetic quantum recurrences, including a proof
that passes from finite Fourier support to smooth functions.

Put
$$
 T=\begin{pmatrix}3&2\\4&3\end{pmatrix},\qquad
 \alpha=1+\sqrt2,\quad\lambda=3+2\sqrt2,\qquad
 N+F\sqrt2=\alpha^K,
$$
where K tends to infinity through odd primes. Thus $N^2-2F^2=-1$ and
$N\asymp\lambda^{K/2}$. All statements allow composite N. Fix the cat
quantization $U_0$ described in Section 1, with $U_0^K=I$, and work on its
whole odd space of dimension $d_N=(N-1)/2$. Let $\tau_-$ be normalized trace.
The Fourier convention is $e_v(x)=e^{2\pi i v\cdot x}$ and
$\mathcal C e_v=e_{Tv}$, equivalently $\mathcal C f=f\circ T^{\mathsf T}$.
This explicitly specifies the covector convention; it does not substitute
an unrelated map when passing between observables and propagators.

Let $\mathscr E$ be the real even $C^\infty(\mathbb T^2)$ functions of
mean zero. Write $b_v=e_v+e_{-v}$. Choose one representative r for each
orbit of nonzero integer vectors under $v\mapsto\pm T^jv$, and write
$$
 f=\sum_{\mathcal O}\sum_{j\in\mathbb Z}a_{\mathcal O,j}(f)b_{T^jr},
 \quad A_{\mathcal O}(f)=\sum_j a_{\mathcal O,j}(f),\quad
 \Sigma(f,g)=2\sum_{\mathcal O}A_{\mathcal O}(f)A_{\mathcal O}(g).
 \tag{1}
$$
All these sums converge absolutely. Define $\sigma^2(f)=\Sigma(f,f)$.

**Theorem A (smooth first-order resonance).** For every fixed $f\in\mathscr E$,
put
$$
 F_N=\operatorname{Op}_N(f),\quad
 \overline F_N=\frac1K\sum_{j=0}^{K-1}U_0^jF_NU_0^{-j},\quad
 X_N(f)=\sqrt K\,\overline F_N.
$$
For any fixed ordered word in such X's, the normalized odd trace converges
to the corresponding moment of a *commuting* centered Gaussian family with
covariance $\Sigma$. In particular the empirical spectrum of $X_N(f)$
converges weakly to $N(0,\sigma^2(f))$, allowing the point mass at zero.
If $\varepsilon_K\sqrt K\to t\in\mathbb R$, then for every fixed integer m,
$$
 \tau_-\!\left[(e^{i\varepsilon_KF_N}U_0)^{mK}\right]
       \longrightarrow e^{-m^2t^2\sigma^2(f)/2}.                \tag{2}
$$
There is no random parameter or replacement by a random matrix in (2).
For arbitrary smooth f no uniform numerical convergence rate is claimed.

**Theorem B (exact first-order degeneracy criterion).**
$$
 \begin{split}
 \Sigma(f,g)&=\sum_{n\in\mathbb Z}\int_{\mathbb T^2}
                               f\,\mathcal C^n g\,dx,\\
 \sigma^2(f)=0
 &\quad\Longleftrightarrow\quad
 f=g-\mathcal Cg\text{ for some }g\in\mathscr E.                \tag{3}
 \end{split}
$$
In the latter case $X_N(f)=0$ **exactly for every Pell modulus**, not merely
in the limit. Thus the scalar variance classifies which smooth kicks are
invisible to the first-order recurrence average.

**Theorem C (smooth second-order resonance).** For $g\in\mathscr E$, set
$$
 f=g-\mathcal Cg,\qquad
 h_g=\frac{\{g,\mathcal Cg\}}{4\pi},\qquad
 \Gamma(g)=\sigma^2(h_g),                                     \tag{4}
$$
where $\{g,d\}=\partial_1g\,\partial_2d-\partial_2g\,\partial_1d$.
If $\varepsilon_K^2\sqrt K/N\to t\in[0,\infty)$, then
$$
 \tau_-\!\left[(e^{i\varepsilon_K\operatorname{Op}_N(f)}U_0)^{mK}\right]
       \longrightarrow e^{-m^2t^2\Gamma(g)/2}.                 \tag{5}
$$
The functional $\Gamma$ is a continuous nonnegative homogeneous quartic on
$\mathscr E$. Its positive set is open and dense. In any finite real cosine
coefficient space containing a nonzero mode, its zero set is a proper real
algebraic set of Lebesgue measure zero. This is generic nondegeneracy, not
an assertion that every nonzero generator has positive $\Gamma$.

The quantum critical scales in the two nondegenerate cases are respectively
$K^{-1/2}$ and $\sqrt N K^{-1/4}$. The corresponding classical action
amplitudes are proportional to $\varepsilon/N$ and both tend to zero.
Neither theorem covers a fixed nonzero classical perturbation.

# 1. Quantization, parity, and the phase that cannot be omitted

On $\mathbb C^{\mathbb Z/N\mathbb Z}$ use
$$
 W_N(a,b)u(x)=e_N(a(x-b/2))u(x-b),\quad S_hu(x)=u(h^{-1}x).
$$
Here division by two is modular. For the *fixed classical Fourier modes*
use instead
$$
 Q_N(v)=(-1)^{v_1v_2}W_N(v),\qquad
 \operatorname{Op}_N(f)=\sum_v\widehat f(v)Q_N(v).              \tag{6}
$$
The series is norm convergent for smooth f. Direct multiplication gives,
for integer vectors before reduction,
$$
 Q_N(v)Q_N(w)=e^{i\pi\omega(v,w)/N}Q_N(v+w),\quad
 Q_N(v)^*=Q_N(-v),\quad\omega(v,w)=v_1w_2-v_2w_1.              \tag{7}
$$
The sign in (6) is necessary when both coordinates are odd; omitting it
would quantize a different classical Fourier symbol. Since $T=I$ modulo 2,
this sign is invariant along every T-orbit. Consequently an exact Egorov
operator for W also obeys $U_0Q_N(v)U_0^*=Q_N(Tv)$. Real even f gives a
Hermitian parity-preserving operator. Individual Weyl translations do not
in general preserve parity.

Here is an explicit construction. Put $s=F^{-1}\pmod N$, so $s^2=2$, and
$h=3+2s$. Let $C_tu(x)=e_N(tx^2/2)u(x)$ and let $\mathcal F_N$ have kernel
$e_N(xy)/\sqrt N$. The unitary
$$
 V=C_{s^{-1}}S_{1/2}\mathcal F_NC_{2s},\qquad U_0=VS_h^{-1}V^*
$$
has covariance T, because V has covariance
$$
 M=\begin{pmatrix}-1/(2s)&1\\-1/2&-s\end{pmatrix},\quad
 \det M=1,\quad T=M\operatorname{diag}(h,h^{-1})M^{-1}.
$$
All factors preserve parity. The Pell identity gives $(1+s)^K=1$, hence
$h^K=1$ and $U_0^K=I$. In fact $T^K=I\pmod{2N}$, by
$Q_{2K}=2N^2+1$ and $P_{2K}=2NF$, so (6) is consistent with that period.
No prime-modulus Weil representation is being silently used.

Full-space Weyl orthogonality and the parity trace are
$$
 N^{-1}\operatorname{Tr}(W_N(v)^*W_N(w))=\mathbf1_{v=w\bmod N},
 \qquad\operatorname{Tr}(RW_N(v))=1.
$$
Thus a noncentral Weyl word has normalized odd trace of modulus
$1/(N-1)$; a central word has modulus at most $N/(N-1)+1/(N-1)$.
We use full-space orthogonality only, and restrict by the valid inequality
$$
 \|A\|_{2,-}\leq\sqrt{\frac{2N}{N-1}}\|A\|_{2,N}               \tag{8}
$$
for parity-preserving A. Restricted Weyl matrices are not assumed orthogonal.

# 2. Canonical orbits and an effective finite cohomology decomposition

Identify $v=(a,b)$ with $\psi(v)=b+\sqrt2a$. Then
$$
 \psi(Tv)=\lambda\psi(v),\qquad
 q(v)=\operatorname{Norm}\psi(v)=b^2-2a^2\ne0\quad(v\ne0).
$$
Choose the sign and the unique translate r satisfying
$$
 \psi(r)>0,\qquad |q(r)|\leq\psi(r)^2<\lambda^2|q(r)|.         \tag{9}
$$
Multiplication by $\lambda^2$ on the squared positive embedding makes the
interval half-open and yields existence and uniqueness. This is also an
exact algorithm using signs of integers of the form $p+q\sqrt2$.

For an input vector with $\|v\|_\infty\leq R$, its representative satisfies
$\|r\|_\infty\leq C R$ and the translating exponent has magnitude at most
$C\log(2+R)$, for universal C. Indeed $1\leq|q(v)|\leq2R^2$, both real
embeddings of $\psi(v)$ are at most $3R$ in modulus, and their product has
modulus at least one. After balancing, the two embeddings of r are between
constant multiples of $\sqrt{|q|}$. This proves the radius and logarithmic
translation bounds. All intermediate translates between v and r stay in a
constant multiple of the same box, since one embedding increases and the
other decreases monotonically in modulus.

For a finite Fourier polynomial of radius R, replace every orbit chain
$\sum_j a_j b_{T^jr}$ by $(\sum_j a_j)b_r$. This gives a polynomial $h_R$
with pairwise inequivalent representative frequencies and a polynomial $g_R$
such that
$$
 f_R=h_R+g_R-\mathcal Cg_R.                                   \tag{10}
$$
Explicitly set $d_j=a_j-(\sum_l a_l)\mathbf1_{j=0}$ and
$b_j=\sum_{l\leq j}d_l$; these b's have finite support and
$d_j=b_j-b_{j-1}$. This proves (10) coefficient by coefficient.
If the sum of absolute cosine coefficients of $f_R$ is at most M, then
$$
 \|h_R\|_{\ell^1}\leq M,\quad
 \|g_R\|_{\ell^1}\leq C M\log(2+R),                           \tag{11}
$$
and all three polynomial supports have radius at most CR. There are at
most $CR^2$ representative frequencies. Period averaging kills the last
two terms of (10) exactly, in the classical or quantum cyclic sum.

The Fourier proof of (3) is elementary but its principle is classical.
Orthogonality of the $e_v$ gives the Green--Kubo identity; absolute
rearrangement is justified by
$$
 \sum_n\sum_v|\widehat f(v)\widehat g(-T^nv)|
 \leq\Big(\sum_v|\widehat f(v)|\Big)
       \Big(\sum_w|\widehat g(w)|\Big).
$$
There is at most one n relating a given nonzero pair, since T is hyperbolic.
Hence $\sigma^2(f)=0$ is equivalent to zero sum on every signed orbit.

To obtain a *smooth* g, apply the cumulative-sum construction on each
infinite orbit. With r balanced as in (9), $\|T^jr\|$ is comparable to
$\sqrt{|q(r)|}\lambda^{|j|}$, uniformly in r and j, up to fixed constants.
For $j\geq0$ use $b_j=-\sum_{l>j}a_l$; for $j<0$ use
$b_j=\sum_{l\leq j}a_l$. The zero total makes the two definitions agree.
Rapid Fourier decay and the outward geometric growth imply
$|b_j|\leq C_s(1+\|T^jr\|)^{-s}$ for every s. Thus g is smooth, real, even,
and can be chosen mean zero. Conversely, a smooth difference has zero
orbit sum by telescoping its rapidly decaying coefficients. This proves B.

# 3. Short-relation lifting with quantitative dependence on Fourier radius

Take representatives $r_1,\ldots,r_J$ satisfying (9), in a box of radius R,
and inequivalent under $\pm T^j$. A signed m-atom modular relation is
$$
 \sum_{\nu=1}^m\epsilon_\nu T^{j_\nu}r_{a_\nu}=0\pmod N.
 \tag{12}
$$
Cancel equal opposite atoms, cut the cyclic time support at its largest
gap, and rotate. There are at most m occupied times, so the associated
polynomial
$$
 P(\lambda)=\sum_\nu\epsilon_\nu\psi(r_{a_\nu})\lambda^{j_\nu}
$$
has nonnegative exponents at most $L=K-\lceil K/m\rceil$.
The modular relation says $P(\lambda)\in N\mathbb Z[\sqrt2]$.
A nonzero algebraic norm would therefore have modulus at least $N^2$, but
$$
 |\operatorname{Norm}P(\lambda)|\leq9m^2R^2\lambda^L.           \tag{13}
$$
Whenever the latter is less than $N^2$, the relation lifts to zero in the
quadratic field. For each fixed m this condition holds if R is any fixed
power of K and K is sufficiently large. Thus the lifting is uniform in
precisely the slowly growing supports needed below.

There is a uniform cluster bound as well. Split a lifted relation at a gap
b with $\lambda^b>9m^2R^2$. If the higher part is nonzero, its conjugate
embedding has modulus at most $3mR$ and its nonzero integer norm forces
its positive embedding to have modulus at least $1/(3mR)$. Its shifted
value then dominates the lower part, whose modulus is at most
$3mR\lambda^a$ if its degree is a. This contradicts cancellation. Both
parts therefore vanish separately.

Iteration gives components with cyclic spans at most
$$
 D_m=(m-1)\left(\left\lceil\log_\lambda(9m^2R^2)\right\rceil+1\right).
 \tag{14}
$$
Two-atom zero components can only be identical opposite representative-time
atoms. This is exactly the reason for first carrying out (10). After those
pairs are removed, every remaining component has at least three atoms.
An unpaired even $2r$-word has at most $r-1$ components; an odd m-word has
at most $\lfloor m/2\rfloor$ components. Each component has K translations,
and only finitely many partitions, signs, species choices and offsets of
size at most $D_m$. There is **no extra K for choosing the cut**: the cut
proves bounded cyclic width, while the count is of translated components.

One convenient coarse upper bound for this count, after normalization by
$K^{m/2}$, is
$$
 C_{m,M}(1+R)^{4m}(1+\log(2+R))^m K^{-\nu_m},\quad
 \nu_m=\begin{cases}1,&m\text{ even},\\1/2,&m\text{ odd}.
 \end{cases}                                                   \tag{15}
$$
Indeed there are at most $CR^2$ species; choosing one for every position,
one bounded offset for every position, a partition, and signs already
suffices, and is overbounded by (15). The bound is intentionally loose.

For four-atom relations this also gives a useful replacement for a
no-collision assertion. Form signed pairs with two distinct time labels.
A collision of their sum keys either cancels into the same unordered pair,
or all four atoms lie in one cyclic interval of length $D_4$. Fixing one
input atom, each output time is then at circular distance at most $D_4$.
Thus the nonzero pair-key multiplicity is bounded by
$$
 \mathcal M_R\leq1+4J^2(2D_4+1)^2
             \leq C R^4(1+\log(2+R))^2.                       \tag{16}
$$
No zero pair key is possible after the two-atom lifting condition. A
three-plus-one split cannot occur because a single nonzero atom cannot
vanish. This argument includes structural four-relations; it does not
assume a nonexistent Sidon property for a general observable.

# 4. Summable phases, Gaussian moments, and the finite normal form

For representative frequencies v,w of radius R, put
$$
 a_j=\max_{v,w}|e_N(\omega(v,T^jw))-1|,\qquad
 c_j=\frac{K-1-2j}{2K}.
$$
The maximum can be over their finite union. Symplectic invariance gives
$a_{K-j}=a_j$. For a centered time delta,
$|\omega(v,T^\delta w)|\leq C R^2\lambda^{|\delta|}$.
Since $N\asymp\lambda^{K/2}$, summing the geometric tails away from the
half-period proves
$$
 \sum_{j=0}^{K-1}a_j\leq C R^2,\qquad
 \sum_{j=0}^{K-1}|c_j|a_j\leq C R^2/K.                         \tag{17}
$$
For clarity, write $|\delta|=(K-1)/2-l>0$. Its contribution is at most
$C R^2\lambda^{-l}$, and the two coefficient magnitudes are $l/K$ and
$(l+1)/K$. The zero-time contribution is at most $CR^2/N$ and is absorbed
because $N>K$. Constants here and below are universal unless indexed.

Let H be a polynomial in orbit representatives with cosine coefficient
l1 norm at most M. Expand $X_N(H)^m=K^{-m/2}(\sum_j H_j)^m$.
The noncentral odd-trace contribution is bounded by
$(2M)^mK^{m/2}/(N-1)$. Nonpairable central words obey (15).
For a paired word, opposite identical atoms cancel in pairs, the signs
from (6) occur twice, and its Weyl phase is the product of the full
symplectic crossing phases. The product bound
$|\prod u_i-1|\leq\sum|u_i-1|$, together with (17), gives an average
phase error at most $C_mR^2/K$. Independence of crossing phases is not
required. Their individual time differences are uniform.

Summing species coefficients on each pair gives the covariance in (1).
Repeated atom labels in a pairing produce only a lower-order overcount.
The same argument applies to an ordered product of different H's. Thus its
Wick formula has error bounded by a constant times (15), plus
$$
 C_{m,M}R^2/K+C_{m,M}K^{m/2}/(N-1).                            \tag{18}
$$
Unlike the single-frequency special case, odd central words need not be
absent. The three frequencies $(1,0),(0,1),(1,1)$ are an explicit control:
they have structural three-atom relations and a nonzero third moment of
order $K^{-1/2}$. Such a word is small in the limit, not identically zero.

Here is the operator estimate required for actual propagators. Write
$\bar H=K^{-1}\sum H_j$ and $G_H=\sum c_jH_j$. Coefficient subtraction
shows $G_H-U_0G_HU_0^*=H-\bar H$. Four signed terms per species pair,
(17), and the triangle inequality imply
$$
 \|[G_H,H]\|_{\rm op}+\|[H,\bar H]\|_{\rm op}\leq C M^2R^2/K.
$$
For $[G_H,\bar H]$, apply Cauchy--Schwarz inside each Fourier key class,
use the multiplicity (16), and use full Weyl orthogonality. This yields
$$
 \begin{split}
 \|[G_H,\bar H]\|_{2,N}^2
 &\leq\frac{4\mathcal M_R M^4}{K^4}
                   \sum_{j=1}^{K-1}(K-j)j^2a_j^2\\
 &\leq\frac{\mathcal M_R M^4}{K}\sum_j a_j
 \leq\frac{C M^4R^6(1+\log(2+R))^2}{K}.                     \tag{19}
 \end{split}
$$
The second inequality uses symmetry, $j(K-j)\leq K^2/4$, and
$a_j^2\leq2a_j$. Estimate (8) transfers this to the odd space.

The standard two-factor Duhamel estimate
$$
 \|e^{i\varepsilon A}e^{i\varepsilon D}-e^{i\varepsilon(A+D)}\|
       \leq\varepsilon^2\|[A,D]\|/2                          \tag{20}
$$
holds for any unitarily invariant norm. It follows by differentiating a
product of unitaries and integrating over a triangle. Applying it twice
with the cohomological identity above gives
$$
 \left\|e^{-i\varepsilon G_H}(e^{i\varepsilon H}U_0)e^{i\varepsilon G_H}
                  -e^{i\varepsilon\bar H}U_0\right\|_{2,-}
 \leq C M^2\varepsilon^2
       \left(\frac{R^2}{K}+\frac{R^3(1+\log(2+R))}{\sqrt K}\right).
 \tag{21}
$$
This requires no smallness assumption on $\varepsilon\|G_H\|$.

To pass from $f_R$ to its representative part H use the finite g of (10).
For fixed integer frequencies, (7) gives
$\|[Q_N(v),Q_N(w)]\|\leq2\pi|\omega(v,w)|/N$. Its Fourier l1 version,
(11), and two more applications of (20) show
$$
 \left\|e^{-i\varepsilon\operatorname{Op}_N(g_R)}
       (e^{i\varepsilon\operatorname{Op}_N(f_R)}U_0)
             e^{i\varepsilon\operatorname{Op}_N(g_R)}
                    -e^{i\varepsilon H}U_0\right\|_{\rm op}
 \leq C M^2\varepsilon^2 R^2(1+\log(2+R))^2/N.                \tag{22}
$$
The combined unitary gauges and the exact equality of the period averages
are all that is needed. The size of a gauge itself is never used as a
small perturbation bound.

# 5. The smooth limit: the cutoff must grow and its error must be controlled

A fixed-cutoff argument alone is insufficient: the trivial estimate for
the omitted averaged observable has a factor $\sqrt K$. We give the
uniform argument explicitly.

Let $f_R$ be the Fourier cutoff in the box of radius R. For smooth f and
any s,
$$
 E_R:=\sum_{\|v\|_\infty>R}|\widehat f(v)|\leq C_{f,s}R^{-s}.
 \tag{23}
$$
The same estimate can be used for a finite family. Its l1 norms are
uniformly bounded. For a fixed word length m choose
$R=\lfloor K^{1/(32m)}\rfloor$. Apply (10), (15), and (18) to the
cutoffs. All lifted-relation conditions hold eventually by (13), and the
polynomial-logarithmic error in (15) tends to zero. The canonical radii
are only a constant multiple of R. The orbit covariances of the cutoffs
converge to (1) by absolute l1 convergence.

Meanwhile $\|X_N(f)-X_N(f_R)\|\leq\sqrt K E_R$. Telescoping an ordered
word gives a trace error at most $C_{m,f}K^{m/2}E_R$. Choose s greater than
$16m^2$ in (23); this tends to zero. It is legitimate to choose a different
cutoff for each fixed moment, because the matrix being approximated is
always the same $X_N(f)$. No uniform growing-order assertion follows.
This proves the moment part of A. Tightness, higher-moment uniform
integrability and Gaussian moment determinacy give its spectral weak limit.

For the actual propagator use instead $R=\lfloor K^{1/32}\rfloor$.
The telescoped difference of the full and truncated kicked powers is at
most $|m|K|\varepsilon|E_R$, which tends to zero for bounded
$|\varepsilon|\sqrt K$. Equations (21)--(22), telescoped for |m|K steps,
give errors at most
$$
 C_{m,f}(\varepsilon^2K)
 \left(\frac{R^2}{K}+
       \frac{R^3(1+\log(2+R))}{\sqrt K}+
       \frac{R^2(1+\log(2+R))^2}{N}\right)=o(1).              \tag{24}
$$
Since $\bar H$ commutes with $U_0$ and $U_0^K=I$, the comparison power is
$e^{im\varepsilon K\bar H}$. The averaged cutoff can be replaced by f
using (23), and its characteristic function converges by the already proved
Gaussian law. Negative m follows by taking adjoints. This proves (2).

# 6. Smooth coboundaries and their generated second-order symbol

For finite Hermitian A,D and real epsilon, a useful uniform loop estimate is
$$
 \left\|e^{-i\varepsilon A}e^{i\varepsilon(A-D)}e^{i\varepsilon D}
                       -e^{-\varepsilon^2[A,D]/2}\right\|_{\rm op}
 \leq|\varepsilon|^3\left(\tfrac12\|[A,[A,D]]\|
                              +\tfrac16\|[D,[A,D]]\|\right).  \tag{25}
$$
For completeness, set $Q=[A,D]$ and call the product on the left L(u).
Differentiation gives
$$
 L'(u)L(u)^*=-\int_0^u
       \operatorname{Ad}_{e^{-iuA}e^{iv(A-D)}}Q\,dv.
$$
The comparator $e^{-u^2Q/2}$ has logarithmic derivative -uQ. Differentiating
unitary conjugations bounds the difference of the two generators by
$u^2\|[A,Q]\|+u^2\|[A-D,Q]\|/2$. Integrating u and using the triangle
inequality gives (25). Negative epsilon is obtained by replacing A,D by
-A,-D. This is not a formal small-generator BCH truncation.

Take $A=\operatorname{Op}_N(g)$ and $D=\operatorname{Op}_N(\mathcal Cg)$.
Define
$$
 \Omega(g,d)=\sum_{v,w}\omega(v,w)\widehat g(v)\widehat d(w)e_{v+w}
            =-\{g,d\}/(4\pi^2).
$$
By (7) and the global scalar bound $|\sin u-u|\leq|u|^3/6$,
$$
 [A,D]=\frac{2\pi i}{N}\operatorname{Op}_N\Omega(g,\mathcal Cg)
          +O_g(N^{-3})\quad\hbox{in operator norm}.            \tag{26}
$$
For example the remainder is at most
$\pi^3(3N^3)^{-1}\sum_{v,w}|\widehat g(v)\widehat d(w)||\omega(v,w)|^3$.
Similarly the two double commutators in (25) have norms $O_g(N^{-2})$:
expand three Fourier series, apply twice
$|2\sin(\pi\omega/N)|\leq2\pi|\omega|/N$, and sum the resulting finite
weighted l1 norm. Smoothness makes both bounds uniform in N, without
excluding high-frequency aliases.

Since $h_g=-\pi\Omega(g,\mathcal Cg)$, (25)--(26) and the Lipschitz
bound for exponentials of anti-Hermitian matrices give the finite estimate
$$
 \left\|e^{-i\varepsilon A}
      (e^{i\varepsilon\operatorname{Op}_N(g-\mathcal Cg)}U_0)
                 e^{i\varepsilon A}
          -e^{i(\varepsilon^2/N)\operatorname{Op}_N(h_g)}U_0\right\|_{\rm op}
 \leq C_g\left(\frac{|\varepsilon|^3}{N^2}
                         +\frac{\varepsilon^2}{N^3}\right).   \tag{27}
$$
The symbol $h_g$ is real, even, smooth and has zero mean. Its definition is
independent of the constant ambiguity of the solution g in (3); there is
no other smooth invariant ambiguity, as is seen along the Fourier orbits.

When $\varepsilon^2\sqrt K/N$ is bounded, the error after |m|K steps in
(27) is
$$
 O_{g,m}(K^{1/4}/\sqrt N+\sqrt K/N^2)=o(1).                    \tag{28}
$$
Apply Theorem A to the fixed symbol $h_g$ with effective exponent
$\varepsilon^2/N$. This proves (5), including either sign of epsilon.
The remainder control, rather than a claim that epsilon is small, is what
permits the growing quantum exponent of Theorem C.

# 7. Generic second-order nondegeneracy and computable tests

The map $g\mapsto h_g$ is a continuous homogeneous quadratic map on
$\mathscr E$, and $\Sigma$ is continuous in Fourier l1. Therefore $\Gamma$
is a continuous nonnegative homogeneous quartic. To prove it is not
identically zero, take $g=c\,b_v$, $v=(a,b)\ne0$. Then
$$
 h_g=\pi c^2\omega(v,Tv)(b_{v-Tv}-b_{v+Tv}),\qquad
 \omega(v,Tv)=4a^2-2b^2=-2q(v).
$$
The two signed T-orbits are different, since
$$
 q(v+Tv)=8q(v),\qquad q(v-Tv)=-4q(v).
$$
Both are nonzero. Consequently
$$
 \boxed{\ \Gamma(c\,b_v)=16\pi^2 c^4(b^2-2a^2)^2>0\quad(c\ne0).\ }
 \tag{29}
$$
For every g and a fixed such mode $b_v$, $\Gamma(g+t b_v)$ is a real
polynomial of degree four with positive leading coefficient. It has only
finitely many zeros. This proves density of the positive set in the smooth
topology; continuity proves openness. On a finite coefficient space that
contains a mode, (29) proves that its quartic polynomial is nonzero, giving
the stated full-measure conclusion. We do not claim an infinite-dimensional
Lebesgue measure or universal positivity for every nonconstant generator.

For rational finite Fourier data all orbit reductions and
$\Gamma(g)/\pi^2$ are exactly rational, so degeneracy can be decided by
finite computation. Some controls, with $v=(1,0)$ and $w=(0,1)$, are
$$
 \sigma^2(b_v)=2,\quad \sigma^2(b_v+b_{Tv})=8,\quad
 \sigma^2(b_v-b_{Tv})=0,\quad \sigma^2(b_v+b_w)=4.
$$
The instantaneous L2 variances of the middle two examples are both 4.
Using that variance instead of the orbit-sum variance would therefore
predict the wrong recurrence law in both directions.

For the rational generator
$$
 g=b_{(1,0)}+\tfrac12b_{(0,1)}-\tfrac13b_{(1,1)},
$$
exact orbit computation gives
$$
 \sigma^2(g)=49/18,\qquad \Gamma(g)/\pi^2=10150/81.             \tag{30}
$$
The implementation reconstructs (10) coefficientwise and compares two
independent orbit algorithms. Dense matrices additionally test the physical
Fourier sign in (6), the covariance convention, and the sign and remainder
in (26). These are finite falsifiers, not proofs by sampling of (2) or (5).

# 8. What the resonance limits obstruct, and what they do not prove

A short proof connects either recurrence limit to pair statistics without
requiring Heisenberg-time comparison. Suppose a family of d-dimensional
unitaries satisfies K/d tending to zero and
$\tau(U^{mK})\to e^{-m^2v/2}$ for every integer m, for finite v>=0.
For the compact tent test $\phi_L(s)=L^{-1}(1-|s|/L)_+$, periodization and
Poisson summation give, at d>L,
$$
 C_d(\phi_L)\geq1-\frac1L+
    2\sum_{m=1}^{M}\operatorname{sinc}^2(LmK/d)|\tau(U^{mK})|^2.
 \tag{31}
$$
Here $C_d$ is the normalized ordered distinct-pair count tested against
$\phi_L$ at the global mean spacing. The zero Fourier mode contributes 1,
the removed diagonal contributes $1/L$, and all omitted Fourier terms are
nonnegative. Thus for v>0,
$$
 \liminf C_d(\phi_L)\geq\sum_{m\in\mathbb Z}e^{-m^2v}-1/L>1-1/L.
 \tag{32}
$$
For v=0 the lower bound is infinite. A bounded limiting pair density R(s)
with $R(s)\to1$ at large separation would give
$\int\phi_LR\to1$ as L tends to infinity, contradicting (32). The order
is first d to infinity at each fixed L,M, then M, then L; no unproved
exchange of a growing test support with the quantum limit is involved.

Apply this with $v=t^2\sigma^2(f)$ in A or $v=t^2\Gamma(g)$ in C.
It gives a negative microscopic obstruction throughout any bounded
critical-parameter subsequence. It is not a positive universality theorem
once that parameter diverges. Global unfolding, preservation of
multiplicities, and the specified odd space are all part of the statement.
Additional local unfolding or additional symmetry restrictions are different
questions. Since the classical kick goes to zero and $K=O(\log N)$ while
$d_N\asymp N$, this does not settle conventional fixed-system BGS.

The unresolved next alternatives are now more specific: control the
Heisenberg-scale remainder at a nonvanishing classical perturbation; or
classify the next generated symbol when both (1) and (4) vanish. This paper
does not claim an all-orders normal form merely because the first two
stages have been established.

# 9. Verification and prior-work boundary

The companion `pell_smooth_cohomology.py` implements exact rational Fourier
cohomology, the generated quadratic symbol, and finite numerical spectral
checks. `pell_fourier_orbits.cpp` checks 624 canonical representatives by
bounded multiprecision enumeration rather than the Python reduction loop.
The C++ bound is a finite test, not the proof of the universal reduction.
The Lean module proves a telescoping identity and arithmetic anchors; it
does not formalize the smooth limit, genericity, Duhamel estimates or BGS.
All source hashes and executed commands belong in the verification record.

Relevant primary precedents include Kuperberg's *A tracial quantum central
limit theorem* (arXiv:math-ph/0202035), whose stated input is i.i.d. tracial
samples; Conze, Le Borgne and Roger's work on CLTs for products of toral
automorphisms (arXiv:1006.4051); and Prosen and Znidaric's residual quantum
fidelity freeze (arXiv:quant-ph/0401142, PRL 94, 044101). The standard
commutator-sensitive product estimates also have an extensive literature,
including Childs et al., PRX 11, 011020. None is being relabelled as a new
mechanism. The proof above uses direct arithmetic counts and norm estimates
rather than importing an i.i.d. theorem into a deterministic array. A
complete priority comparison and independent referee validation remain
necessary before a novelty claim.
