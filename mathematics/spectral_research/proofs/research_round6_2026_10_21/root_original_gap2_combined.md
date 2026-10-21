> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round6_2026_10_21/root_original_gap2_combined.md`. Embedded SHA256: `f764a95fddaccebfe5a84c231279e0c6036b9495cea9c0d752aa7e6fe1cf9ed2`.
> [Thematic guide](../../topics/arithmetic.md).

# A complete unequal-occupation class with a linear number of substitutions

21 October 2026. This note combines two separately proved estimates for
the exact prescribed $U_N$. The kick remains $10^{-80}$, and all
limits are over every odd dimension. The class is defined by actual
rooted word pairs and includes up to $\lfloor n/2\rfloor$ changed
positions, without choosing marks or dividing by a presumed multiplicity.

## 1. Exact class

For a rooted word $x=(x_0,\ldots,x_{n-1})$, set
$$
a_N(x)=\prod_{j\pmod n}(U_N)_{x_jx_{j+1}},\qquad
d_v(x)=\#\{j:x_j=v\}.
$$
Let
$$
I(x,y)=\{j\pmod n:x_j\ne y_j\}.
$$
Define $\Omega_n^{(2)}(U_N)$ as the sum of
$a_N(x)\overline{a_N(y)}$ over exactly those pairs satisfying:

1. $I(x,y)\ne\varnothing$;
2. no two elements of $I(x,y)$ are adjacent on the cycle;
3. $d(x)\ne d(y)$.

For $n=1$ the allowed class is empty. For $n=2$ the two singleton
mismatch sets are allowed. Repeated vertices, repeated words, both
orientations, and all changed labels are included with their original
ordered-pair multiplicities.

## 2. The estimate

Put
$$
B_0=\frac{10^{76}}{331776}.
$$
For every sufficiently large odd $N$, every $0<B\le B_0$, and
every weights with $|w_{n,N}|\le W$,
$$
\boxed{
\frac1{N^2}\left|
\sum_{1\le n\le BN}w_{n,N}\Omega_n^{(2)}(U_N)
\right|
\le\frac{776W}{N^2}
+6BNW\exp[-N/331776].
}
\tag{2.1}
$$
In fact the same right side bounds
$N^{-2}W\sum_{n\le BN}|\Omega_n^{(2)}(U_N)|$.
The threshold dimension is not given effectively because the physical
oscillatory-matrix limits used in the inputs have no claimed effective
rate. It is independent of the weights and of $B$ in the displayed
range.

## 3. Proof with disjoint subtraction

Let $F_n^{(2)}$ be the same sum without condition 3, and let
$H_n^{\rm iso}$ be its equal-occupation part. These are disjoint
parts of precisely the same literal class. Therefore
$$
\Omega_n^{(2)}=F_n^{(2)}-H_n^{\rm iso}
\tag{3.1}
$$
exactly. This is subtraction of one specified subset from one specified
set; it is not a union estimate for overlapping signed classes.

The original two-step physical-kernel theorem proves
$$
\max |(U_N^2)_{ab}|\le6/\sqrt N,\qquad
\bigl\||U_N^2|^{\circ2}-J\bigr\|\le8\cdot10^6t+o(1),
\quad t=10^{-80}/(2\pi).
$$
Together with the previously proved one-step estimates, it gives
$$
\max |(U_N)_{ab}|\le3/\sqrt N,\quad
\|E\|\le1/4,\quad\|D\|\le1/4,
$$
where $E=P-J$, $D=|U_N^2|^{\circ2}-P^2$, and
$P=|U_N|^{\circ2}$. All these matrices are the original physical
matrices; $P^2$ is not substituted for $|U_N^2|^{\circ2}$.

For a literal mismatch pattern with $r$ changes and cyclic gaps
$g_i\ge2$, summing all labels first gives
$$
\operatorname{Tr}(D P^{g_1-2}\cdots D P^{g_r-2}).
$$
Since $DJ=JD=0$, positive-length common arcs can be replaced by
$E$; zero-length arcs stay the identity. The entry bounds imply
$$
\|E\|_{\rm HS}\le\sqrt8,\qquad
\|D\|_{\rm HS}\le\sqrt{35}+\sqrt8/4<7.
$$
For $n\ge3$, the resulting word has at least two factors. Two
Hilbert--Schmidt factors and $n-r-2$ operator factors give the bound
$49(1/4)^{n-r-2}$. The exact cyclic independent-set sum is the
scalar companion partition function $Z_n(1/4,1/4)$, whose sum for
$n\ge3$ is $2/3$. At $n=2$,
$|F_2^{(2)}|=|2\operatorname{Tr}D|\le72$. Hence
$$
\sum_{n\ge1}|F_n^{(2)}|
\le72+784(2/3)=1784/3.
\tag{3.2}
$$

For $H_n^{\rm iso}$, the exact coefficient extraction by independent
coordinate phases and the proved matrix bounded-differences estimate
give
$$
\frac1{N^2}\sum_{n\le BN}|H_n^{\rm iso}|
\le\frac{544}{3N^2}
+6BN e^{-N/331776},
\tag{3.3}
$$
provided $Bq_N\le1/331776$. The original theorem permits
$q_N\le10^{-76}$ eventually, so every $B\le B_0$ meets this
condition. Equation (3.3) is a bound on an exact subset of original
word pairs; no target spectrum is replaced by a random-phase ensemble.

Take moduli in (3.1), after the complete contractions and exact
coefficient extraction already performed. Equations (3.2)--(3.3), and
$(1784+544)/3=776$, prove (2.1).

## 4. Relation to the first open pair test

Let $b_*$ be the fixed nonnegative band-limited function defined in
the current report, with $\operatorname{supp}\widehat b_*=[-2,2]$,
and put $w=|\widehat b_*|^2$. Since $2<B_0$, this theorem removes
the entire class $\Omega_n^{(2)}$ from that pair test at error
$$
\frac{776\|w\|_\infty}{N^2}
+12N\|w\|_\infty e^{-N/331776}=o(1).
$$
The remaining estimate is still
$$
\frac1{N^2}\sum_{1\le n<2N}w(n/N)
\left\{\mathcal O_n(U_N)-\min(n,N)
+\Omega_n(U_N)-\Omega_n^{(2)}(U_N)\right\}\longrightarrow0.
\tag{4.1}
$$
Equation (4.1) is **not proved**. It involves all adjacent mismatches
and longer changed runs, among other configurations. The new bound
does not identify the limit of $\mathcal O_n$, and no nonnegativity
or domination of the remaining signed sum is asserted. The all-order,
all-band criterion $H_{\rm diag}$ remains stronger still.

## 5. Complete proof sources

- `r6_original_twostep_physical_mixing.md`, SHA256
  `7d502a881f133743cd3d28afd6ac373351fd4a12f23e8292c59895358f1e747b`:
  exact all-odd kernel, propagated physical estimates, and (3.2).
- `r6_dense_phasechaos_isolated_all_orders.md`, SHA256
  `88bc04559c4961bb0441984b1f9df5fc1d0ab2f99349d603e171a67bac7bebbe`:
  finite-dimensional concentration theorem with verified published input,
  exact class extraction, and (3.3).
- `r6_original_isolated_cross_occupation.md`, SHA256
  `20585b313f25044ae8cab78bdd70edeb3922356788d912666d3f690e5676e68f`:
  direct label-contraction and cyclic-count proofs.

All three full sources, their audits, and the earlier physical input
are included in the cumulative Markdown. The present note adds the
disjoint subtraction and its explicit constant; it does not treat an
unproved hypothesis as an available theorem.
