# Full-symbol Gaussian crossover on odd Pell periods

**Claim ID:** `BGS-FM-002`

Date: 21 September 2026.

Status: project theorem with author check and exact/finite checks. It is an incremental fixed-symbol extension of earlier return-law mechanisms, not a fixed-\(\tau\) BGS theorem, independent referee acceptance, or a priority claim.

## 1. Model

For positive odd \(K\), define

\[
N_K+F_K\sqrt2=(1+\sqrt2)^K,
\qquad
S=\begin{pmatrix}3&4\\2&3\end{pmatrix}.
\]

Then \(N_K\) is odd and \(S^K=I\pmod{N_K}\). Use the frozen generator \(A_N\) and cat propagator \(M_N\) from the fixed-model frontier, and write

\[
U_{\epsilon,N}=\exp(i\epsilon A_N)M_N.
\]

The original frozen problem has \(\epsilon=\tau N\), \(\tau=10^{-80}\). The theorem below instead assumes \(\epsilon_K\sqrt K\) has a finite limit, hence its classical coupling \(\epsilon_K/N_K\) tends to zero.

## 2. Exact variance and Gaussian theorem

Let

\[
\overline A_K=\frac1K\sum_{j=0}^{K-1}M_N^jA_NM_N^{-j},
\qquad
X_K=\sqrt K\,\overline A_K.
\]

Exact rational Fourier-orbit assembly gives

\[
\boxed{\sigma^2=\frac{1650797}{4000000}=0.41269925.}
\tag{1}
\]

As \(K\to\infty\) through odd integers, the empirical eigenvalue measure of \(X_K\) tends to the centered real Gaussian of variance \(\sigma^2\). For every fixed \(r\ge1\),

\[
N_K^{-1}\operatorname{Tr}X_K^{2r}
=(2r-1)!!\,\sigma^{2r}+O_r(K^{-1}),
\]

\[
N_K^{-1}\operatorname{Tr}X_K^{2r+1}=O_r(K^{-1/2}).
\tag{2}
\]

No uniform-in-\(r\) characteristic-function rate is asserted.

Because \(M_N^K=\eta_KI\) for a scalar \(|\eta_K|=1\), if

\[
\epsilon_K\sqrt K\longrightarrow t\in\mathbb R,
\]

then for every fixed integer \(m\),

\[
\boxed{
\eta_K^{-m}N_K^{-1}\operatorname{Tr}
U_{(\epsilon_K,N_K)}^{mK}
\longrightarrow
\exp(-m^2t^2\sigma^2/2).}
\tag{3}
\]

Equivalently, the empirical eigenvalue measures of \(\eta_K^{-1}U^K\) tend to a wrapped centered Gaussian with the displayed Fourier transform.

## 3. Pair-statistic obstruction in the bounded crossover window

For

\[
L_{N_K}(s)=N_K^{-2}\sum_{n\ge1}
e^{-2sn/N_K}|\operatorname{Tr}U_{(\epsilon_K,N_K)}^n|^2,
\]

the subsequence \(n=mK\), together with (3), yields for every \(s>0\)

\[
\liminf_{K\to\infty}L_{N_K}(s)
\ge
\sum_{m=1}^{\infty}e^{-m^2t^2\sigma^2}.
\tag{4}
\]

For \(t=0\) the right-hand side diverges; for finite nonzero \(t\) it is a positive constant independent of \(s\). Hence the CUE pair transform cannot hold in this bounded crossover regime. A necessary condition for CUE pair universality along these Pell dimensions is therefore

\[
\boxed{|\epsilon_K|\sqrt K\to\infty.}
\tag{5}
\]

At the frozen coupling \(\epsilon_K=\tau N_K\), condition (5) eventually holds. Thus this theorem deliberately stops before the actual fixed-\(\tau\) regime.

## 4. Proof architecture

For a general fixed finite **mean-zero** Hermitian Weyl symbol

\[
A_N=\sum_{v\in\Lambda}a_vT_N(v),\qquad
a_{-v}=\overline{a_v},\qquad a_0=0,
\]

the zero-mode hypothesis is essential. If $a_0\ne0$, apply the centered statement to $A_N-a_0I$ and retain the scalar factor $\exp(i mK\epsilon_K a_0)$ in the return trace; $\sqrt K\,\overline A_K$ itself is not centered Gaussian (the example $A_N=I$ already excludes that reading). The maintained frozen generator is centered.

Group the nonzero finite support into oriented \(S\)-orbits and replace each orbit by its summed representative coefficient. The variance is exactly

\[
\sigma_A^2
=
\sum_{\text{oriented orbits }O}
\left|\sum_{v\in O}a_v\right|^2.
\tag{6}
\]

For each fixed moment length, a modular zero word can be cyclically rotated across its largest time gap so that its integer representative has norm below \(N_K\); the congruence therefore lifts to an integer zero relation. Hyperbolic separation then decomposes every zero word into bounded-diameter time components. Pair components give Wick contractions; components of size at least three cost one free time variable and produce the errors in (2). Weyl phases across separated components are controlled before summation rather than discarded.

The detailed moment lifting, bounded-cluster counting and crossing-phase estimates are in [smooth recurrence, Section 1.1](../returns/smooth_recurrence_and_compensation.md). The passage from the averaged exponential to the actual $K$-step product uses the [finite-symbol normal form](../../supplement/fixed_map/design-return/finite_symbol_normal_form.md) and its [all-odd sparse-orbit input](../../supplement/fixed_map/design-return/sparse_orbit_theorem.md). For the present frequency support, the sparse-orbit condition holds for all odd $K\ge39$; the normal-form error at $\epsilon_K\sqrt K=O(1)$ is $O(K^{-1/2})$. These are proof dependencies, not deductions from a finite numerical scan.

For the frozen finite symbol, independent sparse and dense assemblies reproduce (1). A zero-variance coboundary control collapses exactly, which guards against treating the Gaussian law as automatic.

## 5. Boundary

The theorem concerns the full Hilbert space and every sufficiently large odd Pell index, with no primality assumption. It proves a genuine necessary escape condition from the weak-kick obstruction. It neither identifies the transition after (5) nor estimates the frozen \(\epsilon_K=\tau N_K\) dynamics at Heisenberg scale.
