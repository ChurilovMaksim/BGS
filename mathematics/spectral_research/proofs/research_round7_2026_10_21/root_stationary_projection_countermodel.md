> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round7_2026_10_21/root_stationary_projection_countermodel.md`. Embedded SHA256: `fd3e82d27c0bb78adff8093e7255a32a3d23d71c95e57b6e3132482cf5b9884d`.
> [Thematic guide](../../topics/dephasing.md).

# The auxiliary countermodel also has a vanishing nonconstant stationary compression

21 October 2026. This note strengthens the verified properties of the
auxiliary prime-square construction. It is not a claim about a
counterexample for the original fixed-kick family.

The distinction is relevant to the new original-family estimate for
the coordinate compression of the stationary projection. The estimate
is a substantive property of the original matrices, but the proof
below shows that this property, even with an explicit rate, does not
by itself supply the missing spectral statistic.

## 1. Exact statement

Let $N=p^2$, with $p>3$ prime, and let $C_p$ be the exact
finite-field unitary in the included source
root_unipotent_flat_clock.md. The verified properties used here are
only
$$
C_p^p=I,\qquad
|C_p^n|^{\circ2}=J_N\quad(1\le n<p),
\quad J_N=N^{-1}{\bf1}{\bf1}^T.
\tag{1.1}
$$

Let $V$ be the algebraic orthonormal eigenbasis of $C_p$
chosen in the included source r7_return_generic_microperturbation.md.
That source chooses a deterministic algebraic unitary $G$ with
$\|G-I\|_{\rm HS}<\eta_N=N^{-12}$, sets $H=GV$, and splits
the eigenvalues by the specified algebraic binary shifts. The
resulting $\widetilde U_N$ has simple spectrum, eigenbasis $H$,
and an invertible intensity matrix
$$
\mathsf A_H=(|H_{xj}|^2)_{x,j}.
$$
It also has the pair defect and empty local limit proved there.

Then
$$
\boxed{\quad
0\le \mathsf A_H\mathsf A_H^*-J_N,\qquad
\|\mathsf A_H\mathsf A_H^*-J_N\|_{\rm op}
\le N^{-1/2}+4N^{-12}\longrightarrow0.
\quad}
\tag{1.2}
$$
Because the perturbed spectrum is simple, its stationary
compression is exactly $\mathsf A_H\mathsf A_H^*$.

Its signed first-return function also satisfies
$$
F_{\widetilde U_N}'(1)
=(\mathsf A_H\mathsf A_H^*)^{-1},
$$
and therefore
$$
\left.F_{\widetilde U_N}'(1)\right|_{{\bf1}^{\perp}}
\ \ge\
\frac{1}{N^{-1/2}+4N^{-12}}\,
I_{{\bf1}^{\perp}} .
\tag{1.3}
$$
Thus even this growing lower bound for the signed derivative
coexists with
$$
\frac{\Delta_{2,N}^{\widetilde U}(b)}{\sqrt N}
\longrightarrow\int_0^\infty|\widehat b(u)|^2\,du>0
\tag{1.4}
$$
for every fixed nonzero admissible $b$.

## 2. The exact compression before splitting

On the Hilbert space of $N$-by-$N$ matrices with its
unnormalized Hilbert--Schmidt norm, write
$$
W_0(X)=C_pXC_p^*,\qquad
\iota v=\operatorname{diag}(v).
$$
The map $\iota:\mathbb C^N\to M_N(\mathbb C)$ is an isometry.
Since $W_0^p=I$, the orthogonal projection onto
$\ker(W_0-I)$ is exactly
$$
E_0=\frac1p\sum_{n=0}^{p-1}W_0^n.
\tag{2.1}
$$
Indeed, on each eigenspace with eigenvalue a $p$-th root of
unity, the geometric average is one precisely at eigenvalue one
and zero elsewhere.

For every unitary $U$,
$$
(\iota^*\operatorname{Ad}(U)\iota)_{xy}=|U_{xy}|^2.
$$
Combining this identity with (1.1) gives
$$
\iota^*E_0\iota
=\frac1p I_N+\frac{p-1}{p}J_N
=J_N+\frac1p(I_N-J_N).
\tag{2.2}
$$

Let $E_V$ be the orthogonal projection onto the span of the
$N$ orthonormal eigenvector projectors
$|V_j\rangle\langle V_j|$. This subspace lies in
$\ker(W_0-I)$, regardless of the repeated eigenvalues of
$C_p$. Consequently $0\le E_V\le E_0$. Its coordinate
compression is
$$
\iota^*E_V\iota=\mathsf A_V\mathsf A_V^*,
\qquad \mathsf A_V=(|V_{xj}|^2)_{x,j}.
$$
Both projections contain the normalized identity matrix, so
their compressions fix the constant vector. Subtracting $J_N$
and restricting to ${\bf1}^{\perp}$, (2.2) proves
$$
0\le\mathsf A_V\mathsf A_V^*-J_N
\le \frac1p(I_N-J_N).
\tag{2.3}
$$
The lower bound also follows directly because the intensity
matrix is bistochastic and hence maps the constant vector to
itself, with a positive Gram matrix on its orthogonal complement.

## 3. Stability under the prescribed eigenbasis perturbation

For complex numbers of modulus at most one,
$$
\bigl||h|^2-|v|^2\bigr|
\le (|h|+|v|)|h-v|\le2|h-v|.
$$
Since $H=GV$ and $V$ is unitary,
$$
\|\mathsf A_H-\mathsf A_V\|_{\rm HS}
\le2\|H-V\|_{\rm HS}
=2\|G-I\|_{\rm HS}<2\eta_N.
\tag{3.1}
$$

Every bistochastic matrix has operator norm at most one:
Jensen's inequality for each row gives
$\|Av\|_2^2\le\sum_{x,j}A_{xj}|v_j|^2=\|v\|_2^2$.
It follows that
$$
\|\mathsf A_H\mathsf A_H^*
 -\mathsf A_V\mathsf A_V^*\|_{\rm op}
\le2\|\mathsf A_H-\mathsf A_V\|_{\rm op}
<4\eta_N.
\tag{3.2}
$$
Equations (2.3) and (3.2) prove (1.2). No auxiliary
randomization or unproved generic conditioning bound is used.

## 4. The signed derivative and its scope

The general finite-dimensional return calculation is proved in
full in r7_original_intensity_jacobian_audit.md, Section 6:
whenever a unitary has simple spectrum and an invertible
eigenvector intensity matrix $\mathsf A$, its diagonal-pair
return series and derivative converge absolutely at one, and
$$
\sum_{r\ge1}F_r=I,\qquad
\sum_{r\ge1}rF_r=(\mathsf A\mathsf A^*)^{-1}.
$$
Those precise finite-dimensional hypotheses hold here by the
companion construction. The identity needs no bound on the
inverse uniform in dimension.

The Gram matrix is $J_N+Q_N$, where $Q_N>0$ on
${\bf1}^{\perp}$ because $\mathsf A_H$ is invertible.
Equation (1.2) bounds every eigenvalue of $Q_N$ above by
$N^{-1/2}+4N^{-12}$. Inverting on this subspace gives
(1.3). The pair defect (1.4) is the previously proved
fixed-test defect of this same auxiliary sequence, unchanged by
the additional observation.

This calculation isolates a limitation of the new projection
estimate: convergence of the compressed stationary projection
and divergence of the signed derivative do not specify the
spectral behavior on scale $1/N$. It leaves open whether
additional quantitative phase information from the particular
nonlinear original map can supply the required cancellation.
