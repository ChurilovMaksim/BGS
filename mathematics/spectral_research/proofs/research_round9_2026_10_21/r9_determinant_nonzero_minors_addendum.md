> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round9_2026_10_21/r9_determinant_nonzero_minors_addendum.md`. Embedded SHA256: `69233cc4b5d5772bafbf7d95aceb792f7e4a2f5f579500120984c4bf1693cc79`.
> [Thematic guide](../../topics/algebra.md).

# The determinant obstruction survives nonvanishing of every physical minor of every power

21 October 2026. Addendum to
`r9_determinant_exact_cue_detdet_counterexample.md`.

This is an **auxiliary countermodel for a proof mechanism**, not the
original prescribed family. Its purpose is to show that eliminating
exact scalar returns and all zero physical minors does not repair the
determinant-to-statistics inference.

## 1. An explicit perturbation

Let $F_N$ be the unitary Fourier matrix with rows $x=0,\ldots,N-1$
and columns $j=1,\ldots,N$,
$$
 (F_N)_{xj}=N^{-1/2}e^{2\pi ix(j-1)/N}.
$$
Put
$$
 \delta_N=2^{-N^3},\qquad \xi_j=e^{2\pi ij/(N+1)},\qquad
 W_N=F_N\operatorname{diag}(\xi_j e^{i\delta_Nj})_{j=1}^NF_N^*.
 \tag{1.1}
$$
The matrices $W_N$ are exactly unitary. Every exponent perturbation
$\delta_Nj$ is a specified nonzero rational number.

## 2. Every physical minor of every nonzero power is nonzero

Fix $r\in\mathbb Z\setminus\{0\}$ and row and column sets
$I,J$ of equal size $k\ge1$. Set $T=e^{ir\delta_N}$.
Cauchy--Binet gives
$$
 \det(W_N^r[I,J])
 =\sum_{|E|=k}
 \det F_N[I,E]\,\overline{\det F_N[J,E]}
 \left(\prod_{j\in E}\xi_j^r\right)
 T^{\sum_{j\in E}j}.
 \tag{2.1}
$$
This is a polynomial in $T$ with algebraic coefficients. Its largest
degree occurs uniquely at
$E_{\max}=\{N-k+1,\ldots,N\}$. For any physical set $I$, the
minor $F_N[I,E_{\max}]$ is a nonzero monomial in its nodes times
their Vandermonde determinant: its exponents are the consecutive
integers $N-k,\ldots,N-1$. The nodes $e^{2\pi ix/N}$, $x\in I$,
are distinct. This argument works for composite as well as prime $N$.
Thus the coefficient of the largest power in (2.1) is nonzero, and
the polynomial is not identically zero.

After equal powers have been collected and zero coefficients removed,
(2.1) is an algebraic linear combination of exponentials with distinct
algebraic exponents $ir\delta_Ns$, where $s$ runs over distinct
integers. The Lindemann--Weierstrass theorem therefore proves
$$
 \boxed{\det(W_N^r[I,J])\ne0
 \quad\text{for every }r\ne0\text{ and every }I,J,\ |I|=|J|.}
 \tag{2.2}
$$
The precise external theorem is Cheng-Chao Huang, *Explicit Bounds for
Linear Forms in the Exponentials of Algebraic Numbers*, ISSAC 2022,
Theorem 1.1, DOI
[10.1145/3476446.3536170](https://doi.org/10.1145/3476446.3536170).
Its original theorem statement and publication metadata were independently
read in the author's [version 2, page 1](https://arxiv.org/abs/2112.05004v2)
through the raw PDF tool on 21 October 2026. Its hypotheses are exactly
the distinct algebraic exponents and retained nonzero algebraic
coefficients checked above. No quantitative transcendence bound is used.

The same theorem applied to a two-term exponential sum shows that all
eigenvalues of $W_N^r$ are distinct for every $r\ne0$.
Applied to $\sum_{j=1}^N\xi_j^rT^j$, it also gives
$\operatorname{Tr}W_N^r\ne0$. In particular there is no nonzero
scalar return.

## 3. The complete determinant autocorrelation is still CUE up to an error smaller than every inverse power

Write
$\det(I-zW_N)=\sum_{k=0}^Nd_k(W_N)z^k$.
For the unperturbed deleted clock, $d_k(V_N)=1$. Expanding the
elementary symmetric functions and using $|e^{it}-1|\le|t|$ gives
$$
 |d_k(W_N)-1|
 \le\delta_N kN\binom Nk
 \le\delta_N N^2\binom Nk.
 \tag{3.1}
$$
For any fixed $C\ge0$, the autocorrelation definition and
$|z|,|w|\le e^{C/N}$ imply
$$
 \begin{split}
 \left|\mathcal C_{W_N}(z,w)-\sum_{k=0}^N(z\overline w)^k\right|
 &\le e^{2C}\sum_{k=0}^N
 \left(2|d_k(W_N)-1|+|d_k(W_N)-1|^2\right)\\
 &\le e^{2C}\left(2\delta_NN^22^N+
                  \delta_N^2N^44^N\right).
 \end{split}
 \tag{3.2}
$$
We used $\sum_k\binom Nk=2^N$ and
$\sum_k\binom Nk^2=\binom{2N}N\le4^N$.
Because $\delta_N=2^{-N^3}$, the right side is $o(N^{-A})$
for every fixed $A>0$. Any fixed number of derivatives in $z$
and $\overline w$ multiplies the bound by at most a fixed power
of $N$, so the same conclusion holds for all such derivatives.

## 4. The fixed pair defect and the clock limit persist

For $m\ge1$,
$$
 |\operatorname{Tr}W_N^m-\operatorname{Tr}V_N^m|
 \le m\delta_N\sum_{j=1}^Nj
 \le m\delta_NN^2.
$$
Both traces have modulus at most $N$. In the fixed compact Fourier
band of the test from (3.3) of the main note, (3.2) there therefore gives
$$
 |\Delta_{2,N}^{W}(b)-\Delta_{2,N}^{V}(b)|
 \le C_b\delta_NN^3\longrightarrow0.
 \tag{4.1}
$$
Consequently the same fixed test satisfies
$\Delta_{2,N}^{W}(b)\to-c_b<0$.

For local convergence, each eigenangle has moved by
$\delta_Nj/(2\pi)$. Its unfolded displacement is at most
$\delta_NN^2/(2\pi)\to0$. More explicitly, for a smooth compactly
supported $f$, stationarity and translation in the center phase give
$$
 \mathbb E_\alpha
 \bigl|\langle f,\Xi^W_{N,\alpha}\rangle-
         \langle f,\Xi^V_{N,\alpha}\rangle\bigr|
 \le\frac{\delta_NN(N+1)}{4\pi}\,\|f'\|_1.
 \tag{4.2}
$$
Indeed the contribution of eigenvalue $j$ is at most
$\delta_Nj\|f'\|_1/(2\pi)$. Thus the bounded Laplace observables
have the same limits as in the main note, and the limit remains the
uniformly shifted unit lattice.

## 5. The inverse-determinant obstruction also persists

Let $r_N=e^{-s/N}$, fixed $s>0$. Uniformly in $\alpha$,
$$
 \frac{D_{W_N}(r_Ne^{i\alpha})}{D_{V_N}(r_Ne^{i\alpha})}
 =\prod_{j=1}^N(1+u_j),\qquad
 |u_j|\le\frac{r_N\delta_Nj}{1-r_N}.
$$
Hence $\sum_j|u_j|=O_s(\delta_NN^3)$.
For sufficiently large $N$, each $|u_j|\le1/2$; using
$|\log|1+u||\le2|u|$ shows that the squared moduli of this
ratio and its reciprocal are $1+O_s(\delta_NN^3)$, uniformly.
Equation (5.1) of the main note therefore implies
$$
 \int_0^{2\pi}|D_{W_N}(r_Ne^{i\alpha})|^{-2}
 \frac{d\alpha}{2\pi}
 \longrightarrow\frac2{1-e^{-2s}}.
 \tag{5.1}
$$
The CUE value still grows as $N/(2s)$.

## 6. Logical boundary

One explicit auxiliary sequence simultaneously has all the following
properties: all physical minors of all nonzero powers are nonzero;
all those powers have simple spectra and nonzero traces; the full
determinant autocorrelation, including every fixed derivative at
microscopic arguments, approaches CUE faster than any inverse power;
the fixed pair statistic has a nonzero defect; and a bounded Laplace
observable has a non-Sine limit.

This construction does **not** retain the prescribed fixed perturbation
or its classical dynamics. It is not an alternative answer to the
original question. It closes the narrower logical loophole that the
deleted clock's finite order or vanishing minors could explain the
failure of the determinant comparison mechanism.
