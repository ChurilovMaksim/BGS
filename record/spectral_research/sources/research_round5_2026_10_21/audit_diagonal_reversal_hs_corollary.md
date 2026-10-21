> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round5_2026_10_21/audit_diagonal_reversal_hs_corollary.md`. Embedded SHA256: `ddfefc8e1e72d6ff599e41c023cd3e5a1d212f2ce6248f5b86d02d743d5d2c54`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/symmetry.md).

# Exact Hilbert--Schmidt identity for diagonal gauge reversal

Round 5, 21 October 2026. Author: /root/audit_uniform_word_r4.

## 1. Inputs and statement

The physical reverse-path matrix is
$$
Q_N(x,y)=U_N(x,y)\overline{U_N(y,x)}.
$$
The source root_oscillatory_matrix_cancellation.md, SHA-256

ff98c2a2ee7dcd55b046c2039a86b2c206c3fcc170df3433c76f49281eff968d,

together with the physical kernel source, SHA-256

0b8e8a685c619ba95fab9f9eac65f5328ee81123780ae94515e17f4e8e70235c,

proves $\|Q_N\|_{\rm op}\to0$ for the original matrices along all odd
dimensions. Both sources were independently checked in the audits
audit_sampled_oscillatory_matrix.md and audit_four_branch_physical_kernel.md.
This note records a further exact finite-dimensional consequence; its
orientation is proved below.

For any diagonal unitary $D=\operatorname{diag}(d_0,\ldots,d_{N-1})$ and
any scalar $|\eta|=1$, define
$$
\mathcal E_N(D,\eta)=N^{-1/2}
\|D\overline{U_N}D^*-\eta U_N^*\|_{\rm HS}.
$$
Then the exact identity is
$$
\boxed{\quad
\mathcal E_N(D,\eta)^2
=2-\frac2N\operatorname{Re}\!\left(\eta\,d^*Q_Nd\right).
\quad}
\tag{1}
$$
Consequently
$$
\boxed{\quad
\sup_{D,\ |\eta|=1}\left|\mathcal E_N(D,\eta)^2-2\right|
\le2\|Q_N\|_{\rm op}\longrightarrow0.
\quad}
\tag{2}
$$
In particular every diagonal gauge and every scalar phase, even when chosen
arbitrarily as a function of $N$, have normalized Hilbert--Schmidt reversal
defect tending uniformly to $\sqrt2$.

## 2. Direct proof and transpose convention

Both matrices in the difference defining $\mathcal E_N$ have squared
Hilbert--Schmidt norm $N$. Their Hilbert--Schmidt inner product is
$$
\begin{split}
&\sum_{x,y}
\overline{d_x\overline{U_{xy}}\overline{d_y}}\,
\eta\,\overline{U_{yx}}\\
&\qquad=\eta\sum_{x,y}\overline{d_x}d_y
U_{xy}\overline{U_{yx}}
=\eta\,d^*Q_Nd .
\end{split}
$$
Expanding the squared norm proves (1), including the unconjugated $\eta$
in that formula. Since $Q_N(y,x)=\overline{Q_N(x,y)}$, the matrix $Q_N$
is Hermitian and $d^*Q_Nd$ is real. This reality is not needed for the bound
$$
|d^*Q_Nd|\le\|Q_N\|_{\rm op}\|d\|_2^2=N\|Q_N\|_{\rm op},
$$
which proves (2). Also,
$$
|\mathcal E_N(D,\eta)-\sqrt2|
\le\sqrt2\,\|Q_N\|_{\rm op}
$$
follows by dividing the squared difference by
$\mathcal E_N(D,\eta)+\sqrt2$.

Entrywise conjugation of the original defect, followed by multiplication
on the left by $D$ and on the right by $D^*$, gives the equivalent norm
$$
\|U_N-\overline\eta\,D U_N^T D^*\|_{\rm HS}.
$$
Thus the same statement can be read as uniform failure of diagonal
symmetrization of the physical matrix kernel. It is not a statement about
arbitrary conjugations chosen in a spectral basis.

The antiunitary corresponding to a diagonal gauge is $\Theta=DK$, where
$K$ is entrywise conjugation. Its action on $U_N$ is exactly
$\Theta U_N\Theta^{-1}=D\overline{U_N}D^*$; moreover $\Theta^2=I$.
Hence no additional gauge or half-phase convention is implicit.

## 3. Quantitative and structural scope

The inequality $\|F\|_{\rm op}\ge\|F\|_{\rm HS}/\sqrt N$ also gives,
uniformly in $D,\eta$,
$$
\|D\overline{U_N}D^*-\eta U_N^*\|_{\rm op}
\ge\sqrt{\,2-2\|Q_N\|_{\rm op}\,}
$$
whenever $\|Q_N\|_{\rm op}\le1$. In particular a defect of order $1/N$,
or even $o(1)$, is impossible along any sequence of such gauges.

The earlier finite-dimensional discriminator
audit_quantitative_gauge_reversal_obstruction.md, SHA-256

7cb30d1ef2cba42132c5aff08d06fd931be1175c87fd2bdc26a8b4de3a8c2c29,

gives a different effective statement: a lower bound $10^{-328}$ already
for every odd $N\ge10^7$. That explicit threshold does not follow from the
qualitative oscillatory lemma used here. The two conclusions should retain
their separate quantifiers.

Permutations of physical coordinates are not included in this corollary.
Neither are general antiunitaries unconnected to the chosen physical
coordinates. The statement removes one approximate-symmetry mechanism; it
does not prove any local spectral-statistics limit.
