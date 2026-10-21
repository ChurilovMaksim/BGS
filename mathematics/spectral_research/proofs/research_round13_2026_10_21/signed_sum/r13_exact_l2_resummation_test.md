> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round13_2026_10_21/signed_sum/r13_exact_l2_resummation_test.md`. Embedded SHA256: `c92306e56c2559c052c0669cc6ee97a72049fb27bf4a91c0accef5dace7eb24f`.
> [Thematic guide](../../../topics/closure.md).

# Round 13: exact test of a coefficient-square-sum resummation

Date: 21 October 2026. Branch: `/root/r13_original_signed_sum`.

## 0. Status and target

No new estimate of the original pair functional was obtained in this branch.
Neither $H_{\rm diag}$ nor its negation is established. The calculation below
is a test of an attempted summation principle, **not** a counterexample for the
specified kick $e^{i10^{-80}NA_N}$.

The unchanged first target is, with the fixed admissible $b_*$ from the
Round 12 checkpoint and $w=|\widehat b_*|^2$,

$$
 F_N=N^{-2}\sum_{1\le m<2N}w(m/N)
 \left(|\operatorname{Tr}[(e^{i10^{-80}NA_N}M_N)^m]|^2-
 \min(m,N)\right)\stackrel?\longrightarrow0.
\tag{0.1}
$$

The intended central move was to replace the unusable product of coefficient
$\ell^1$ budgets in the exact growing-degree expansion by a contraction using
coefficient $\ell^2$ norm and exact twisted-convolution unitarity. This test
rules out that principle if it uses only those conditions, even supplemented
by maximal pointwise coefficient spreading and global single-kick spectral
uniformity. It does **not** rule out an argument exploiting additional exact
features of the prescribed $A_N$.

## 1. Inputs and provenance

The declared base master was hashed, not reread in its entirety:

- `Spectral_research_master.md`, 7,941,879 bytes, SHA-256
  `10b90c7d12668cd7327bcc08bda292f4c7d6cf82218ee95d5d4f7603fac86cef`.

The following two files were read completely:

- `research_round12_2026_10_21/r12_full_product_nonperturbative_attempt.md`,
  SHA-256 `d1418d95d9a5482251a66241e99e555f48519b437a7a2ed3a29a00eaa91d4225`.
- `research_round12_2026_10_21/round12_continuation_ledger.md`,
  SHA-256 `8b0ac292a355e6bf529e2f1f108ae55b72ebb6d3c01ed965dffdbe1c05200b88`.

Targeted `rg` searches over prior route files identified earlier Parseval,
Markov, physical-diagonal resolvent, and Krylov obstacles, in particular the
Round 4 `counter_growing_routing_families.md` coherent-character evaluation
obstruction. Only search excerpts of those older files were read; their proofs
are not imported below. Generic Fourier/Parseval reformulation is not counted
as new original-family progress.

The following finite calculation is proved directly from the given kernel.
There is no external theorem leaf and no numerical experiment on spectra.

## 2. Exact coefficient constraints

Use native modular Weyl conventions

$$
 W_v=T_N(l,k),\quad v=(k,l)\in G_N=(\mathbb Z/N\mathbb Z)^2,
 \qquad \sigma(v,w)=lk'-kl'.
$$

Direct multiplication gives

$$
 W_vW_w=e_N(\overline2\sigma(v,w))W_{v+w},\quad W_v^*=W_{-v},
 \quad \operatorname{tr}_N(W_v^*W_w)=\mathbf1_{v=w}.
\tag{2.1}
$$

Here $\operatorname{tr}_N=N^{-1}\operatorname{Tr}$ and $\overline2$ is the
modular inverse. Every matrix $E$ therefore has unique coefficients

$$
 E=\sum_{v\in G_N}e(v)W_v,\qquad e(v)=\operatorname{tr}_N(W_v^*E).
$$

If $E$ is unitary, orthogonality and $EE^*=I$ imply

$$
 \sum_v|e(v)|^2=1,
\tag{2.2}
$$

and, for every $u\in G_N$,

$$
 \sum_v e(v)\overline{e(v-u)}
 e_N(\overline2\sigma(v,u))=\mathbf1_{u=0}.
\tag{2.3}
$$

Indeed the coefficient of $W_u$ in $EE^*$ is the left side: writing the two
labels as $v$ and $v-u$ gives phase
$\sigma(v,-(v-u))=\sigma(v,u)$. Equation (2.2) is its $u=0$ case.

These identities apply exactly to the original exponential, with no scalar
polynomial tail and no omission of Fourier aliases. The attempted next step
was to use (2.2)--(2.3) to control the complete squared trace of $(EM_N)^m$.

## 3. A maximally spread kick for which every full trace is coherent

Define solely for testing that implication

$$
 K_N=M_N^*.
\tag{3.1}
$$

This is an auxiliary kick. It is not asserted to equal the prescribed
$e^{i10^{-80}NA_N}$ or to be its approximation.

Let

$$
 G_N^{(2)}=\sum_{x\bmod N}e_N(\overline2 x^2),\qquad
 \gamma_N=G_N^{(2)}/\sqrt N.
$$

For all odd $N$, $|\gamma_N|=1$. To prove it without evaluating the sign of a
Gauss sum, use invertibility of 2 and the bijection
$u=x-y$, $v=x+y$:

$$
 |G_N^{(2)}|^2
 =\sum_{u,v\bmod N}e_N(\overline2 uv)=N.
\tag{3.2}
$$

The last equality follows by summing in $v$: only $u=0$ survives.

The given kernel yields

$$
\begin{aligned}
 \operatorname{Tr}(W_{(k,l)}M_N^*)
 &=N^{-1/2}\sum_x e_N\left(
   \overline8[3(x+l)^2-2(x+l)x+3x^2]
   +k(x+\overline2l)\right)\\
 &=N^{-1/2}e_N(\overline4l^2-\overline2k^2)
   \sum_x e_N(\overline2 x^2)\\
 &=\gamma_N e_N(\overline4l^2-\overline2k^2).
\end{aligned}
\tag{3.3}
$$

For the middle line, the quadratic expression before completing the square is

$$
 \overline2x^2+(\overline2l+k)x+
 \overline8\,3l^2+\overline2kl.
$$

Translate $x$ by $\overline2l+k$. The residual constant is
$\overline4l^2-\overline2k^2$. All operations take place modulo odd $N$.

Replacing $(k,l)$ by $(-k,-l)$ leaves the quadratic constant unchanged, so the
native Weyl coefficient of $K_N$ is exactly

$$
 \boxed{\quad
 \kappa_N(k,l)=\operatorname{tr}_N(W_{(k,l)}^*K_N)
 =\frac{\gamma_N}{N}
 e_N(\overline4l^2-\overline2k^2).
 \quad}
\tag{3.4}
$$

Consequently

$$
 |\kappa_N(v)|=N^{-1}\quad(v\in G_N),\qquad
 \sum_v|\kappa_N(v)|^2=1.
\tag{3.5}
$$

This is maximal possible spreading in coefficient $\ell^\infty$: a unit
vector with $N^2$ components must have maximum modulus at least $1/N$.
Moreover $K_N$ is unitary, so all the twisted identities (2.3) hold exactly.
Nevertheless

$$
 (K_NM_N)^m=I,\qquad
 |\operatorname{Tr}(K_NM_N)^m|^2=N^2
 \quad\text{for every }m\ge1.
\tag{3.6}
$$

Thus neither exact coefficient-square norm nor maximal pointwise spreading
prevents complete constructive interference in the full closed trace.

## 4. Even global single-kick spectral uniformity does not repair that step

For completeness the same auxiliary kicks also have globally uniform
spectral measures as $N\to\infty$ through all odd integers. This property
is proved here solely to make the scope of the countertest precise.

Direct covariance from the kernel is

$$
 M_NW_vM_N^*=W_{Cv},\qquad
 C=\begin{pmatrix}3&2\\4&3\end{pmatrix}.
\tag{4.1}
$$

One verification compares coefficients of $x,y$ in $M_NT_N(a,b)$ and
$T_N(a',b')M_N$, giving $a'=3a+4b$, $b'=2a+3b$. The constant terms agree
by the rational identity

$$
 \tfrac12a'b'-\tfrac38(a')^2=-\tfrac38a^2-\tfrac12ab,
$$

which remains valid modulo every odd $N$.

The trace of the conjugation operator $X\mapsto M_N^jXM_N^{-j}$ on the
$N^2$ dimensional matrix space equals $|\operatorname{Tr}M_N^j|^2$.
Indeed in an orthonormal eigenbasis of $M_N^j$ its eigenvalues are
$\lambda_a\overline{\lambda_b}$, whose sum is that square. In the Weyl
basis, (4.1) makes this same operator a permutation, giving exactly

$$
 |\operatorname{Tr}M_N^j|^2
 =\#\ker(C^j-I:G_N\to G_N).
\tag{4.2}
$$

Fix $j\ge1$ and put $D_j=\det(C^j-I)\ne0$. Nonvanishing follows because
the eigenvalues of $C$ are $3+2\sqrt2>1$ and its reciprocal, neither of
whose positive powers is 1. If $(C^j-I)v=0$ modulo $N$, multiplication
by the adjugate gives $D_jv=0$ modulo $N$. There are at most
$\gcd(N,|D_j|)^2\le D_j^2$ such pairs $v$. Therefore

$$
 |\operatorname{tr}_N K_N^j|
 =|\operatorname{tr}_N M_N^j|
 \le |D_j|/N\longrightarrow0
 \quad(j\text{ fixed},\ j\ne0).
\tag{4.3}
$$

Negative powers follow by conjugation. Trigonometric polynomials are
uniformly dense in continuous functions on the circle: for example
convolution with the nonnegative Fejer kernels gives polynomial
approximations converging uniformly, by uniform continuity and concentration
of those kernels near zero. Applying (4.3) first to each polynomial and then
using this uniform approximation proves convergence of the normalized
single-kick spectral measures to Haar measure.

This does not contradict any result about the original kick: it shows that
a global single-kick spectral law by itself has no implication for the
correlated product with the fixed $M_N$.

## 5. Divergence of the tested functional for the auxiliary kick

Let $w=|\widehat b_*|^2$. It is nonnegative, continuous, supported in
$[-2,2]$, and $w(0)>0$, since $\int b_*>0$. Write $F_N^{\rm aux}$ for
the left side of (0.1) with $e^{i10^{-80}NA_N}$ replaced by $K_N$.
Using (3.6),

$$
 F_N^{\rm aux}=
 \sum_{1\le m<2N}w(m/N)
 -\frac1{N^2}\sum_{1\le m<2N}w(m/N)\min(m,N).
$$

The second sum is $O(1)$, because it has at most $2N$ terms of size
at most $N\|w\|_\infty$, and the first is a Riemann sum. Hence

$$
 \frac{F_N^{\rm aux}}N\longrightarrow
 \int_0^2w(t)\,dt>0.
\tag{5.1}
$$

This calculation refutes only an implication whose hypotheses are (2.2),
(2.3), maximal coefficient spreading, covariance of the fixed $M_N$, and
global spectral uniformity of the kick. It does not satisfy the exact
prescribed-generator hypothesis of the task and is therefore **not** an
admissible negative answer to $H_{\rm diag}$.

## 6. Exact remaining obligation and continuation condition

The Round 12 physical polynomial approximation remains valid, with uniform
trace approximation through $m<2N$ and aggregate error $O(N^{2-K})$ for
$K>2$. Its exact signed sum includes every congruence class and every Weyl
phase. The attempted next contraction cannot follow merely from the
coefficient constraints in Section 2; Sections 3--5 provide an explicit
finite-dimensional countertest to that claimed implication.

No estimate of the original $F_N$ in (0.1) follows from this branch. In
particular, no original $o(1)$ error, no nonzero fixed original lower bound,
and no original countersequence was obtained.

A continuation of this particular coefficient route must use an additional
proved quantitative correlation property of the coefficients of
$e^{i10^{-80}NA_N}$ with their $C$-transforms and with the complete closure
phases, at word length proportional to $N$. Merely deriving a new notation
for the same trace sum or proving another isolated coefficient norm cannot
supply that missing information. The route is unresolved; the explicit test
closes only the attempted norm/flatness-only contraction.

Review status: directly derived and self-checked in this branch. No independent
review has yet been imported. The universal original assertion remains open
in this record.
