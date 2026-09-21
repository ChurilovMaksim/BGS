# All-time classical stability sum and exact periodic counts

Date: 21 September 2026.

Status: project proof for the corrected frozen classical map, using the
real-analytic Anosov trace formula of Jézéquel as an external theorem. Exact
periodic-point counts use only the already-proved topological conjugacy. This
is a classical all-time result, not a quantum trace formula and not BGS.

## 1. Corrected physical map

Let \(F_\tau\) be the classical map attached to the actual raw-modular frozen
operator. The maintained symmetry theorem proves that for the actual
\(\tau=10^{-80}\), \(F_\tau\) is a real-analytic area-preserving Anosov
diffeomorphism and is topologically conjugate to

\[
S=\begin{pmatrix}3&4\\2&3\end{pmatrix}.
\]

Since \(S\) is topologically mixing, so is \(F_\tau\).

Nothing in the argument below uses the obsolete pre-gauge symbol from the
14 September dossier.

## 2. Analytic Ruelle trace formula

For a real-analytic Anosov diffeomorphism and analytic weight, Jézéquel
constructs an anisotropic Hilbert space on which the transfer operator is
trace class. Proposition 4.3 of
[M. Jézéquel, arXiv:2212.09881](https://arxiv.org/abs/2212.09881)
gives, for the weight \(1\),

\[
\operatorname{tr}\mathcal L^m
=
\sum_{F_\tau^m x=x}
{1\over|\det(I-D_xF_\tau^m)|}.
\tag{1}
\]

The nonzero eigenvalues of this trace-class realization are the Ruelle
resonances. For a mixing volume-preserving Anosov diffeomorphism, \(1\) is
the simple peripheral resonance and there is no other unit-modulus
resonance. Since a trace-class spectrum can accumulate only at zero, there is
some \(0<\rho_{\rm cl}<1\) such that every other resonance has modulus at
most \(\rho_{\rm cl}\).

Writing the eigenvalues as \(1,\lambda_2,\lambda_3,\ldots\), trace class gives
\(\sum_{j\ge2}|\lambda_j|<\infty\). Therefore

\[
\left|\sum_{j\ge2}\lambda_j^m\right|
\le \rho_{\rm cl}^{m-1}\sum_{j\ge2}|\lambda_j|.
\]

Combining with (1),

\[
\boxed{
\sum_{F_\tau^m x=x}
{1\over|\det(I-D_xF_\tau^m)|}
=
1+O(C_{\rm cl}\rho_{\rm cl}^m)}
\tag{2}
\]

for every \(m\ge1\), with constants depending only on the frozen map. In
particular the error is exponentially small at \(m=\Theta(N)\).

## 3. Exact periodic-point counts

Topological conjugacy gives a bijection

\[
\operatorname{Fix}(F_\tau^m)\longleftrightarrow
\operatorname{Fix}(S^m)
\]

for every \(m\), preserving exact periods. Thus

\[
\boxed{
\#\operatorname{Fix}(F_\tau^m)
=
|\det(S^m-I)|
=
(3+2\sqrt2)^m+(3-2\sqrt2)^m-2.}
\tag{3}
\]

If \(\mathcal P_m\) denotes primitive period-\(m\) orbits, Möbius inversion
gives

\[
\boxed{
\#\mathcal P_m
=
{1\over m}\sum_{d\mid m}\mu(m/d)|\det(S^d-I)|.}
\tag{4}
\]

Thus the nonlinear frozen map changes actions and derivative/stability data,
but not the exact periodic-orbit counts.

## 4. Boundary

Equation (2) controls a positive classical stability-weighted sum. It does
not evaluate the signed quantum double-path expansion, identify unitary
encounter coefficients, or prove the CUE form factor. Classical periodic
mixing cannot replace the quantum post-cyclic cancellation theorem.

The elementary integer part of (3)--(4) is regression-tested in
[fixed_map_classical_sum_rule_audit.py](../computations/verification/fixed_map_classical_sum_rule_audit.py).
