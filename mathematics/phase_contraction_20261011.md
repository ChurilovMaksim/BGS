# Sharp variance contraction under diagonal phases

**Stable claim:** BGS-TRACE-068. **State:** PROVED.
**Boundary:** Haar circular background frozen once, randomness then only in compatible phases; spectral L2 functions, paired CSE phases and half trace. Full conditional weak Sine-beta limit in probability over the background. No prescribed deterministic-background theorem or Sine-limit rate.
**Integration and review:** [11 October disposition](../archive/record/chat_integration_20261011.md).
**Original input:** [dated source](../evidence/executions/20261011/chat-research/original/jack_phase_2026_10_11/phase_contraction.md).


## Models

Let \(\beta\in\{1,2,4\}\), set \(\alpha=2/\beta\), and fix \(N\ge2\).

- CUE: \(Q\) is Haar in \(U(N)\).
- COE: \(Q=gg^T\), with \(g\) Haar in \(U(N)\).
- CSE: \(Q=gg^R\), with \(g\) Haar in \(U(2N)\), where
  \(A^R=J A^T J^{-1}\) and
  \(J=\operatorname{diag}(J_2,\ldots,J_2)\),
  \(J_2=\begin{pmatrix}0&1\\-1&0\end{pmatrix}\).

CSE has \(N\) eigenvalues each with multiplicity two. Throughout, spectral
statistics in CSE count each Kramers pair once. Thus
\(\operatorname{tr}_4 Q=\tfrac12\operatorname{Tr}Q\); in CUE and COE,
\(\operatorname{tr}_\beta Q=\operatorname{Tr}Q\).

For CUE and COE take
\(D=\operatorname{diag}(e^{i\theta_1},\ldots,e^{i\theta_N})\).
For CSE take

\[
D=\operatorname{diag}(e^{i\theta_1}I_2,\ldots,e^{i\theta_N}I_2).
\tag{1}
\]

All \(N\) phases are independent and uniform, and independent of \(Q\).
Replacing (1) by \(2N\) independent phases does not preserve this CSE model.

For any measurable spectral \(f\in L^2(\mu_{\beta,N})\), define

\[
(Af)(Q)=\mathbb E_D f(DQ).
\]

For COE and CSE, \(DQ\) is similar to \(D^{1/2}QD^{1/2}\), which is
symmetric or self-dual respectively, so \(f(DQ)\) is unambiguous as a
function of the spectrum.

## The theorem

With complex variance interpreted as
\(\mathbb E|f-\mathbb Ef|^2\),

\[
\boxed{\operatorname{Var}_{Q\sim\mu_{\beta,N}}(Af)
\le\frac{1}{N+2/\beta}\operatorname{Var}_{\mu_{\beta,N}}f.}
\tag{2}
\]

This estimate is exact in \(N\), requires no restriction on trace order,
and has the optimal constant. The domain is spectral functions.
For an arbitrary non-spectral function on a symmetric space, a nontrivial
torus-invariant function need not contract at all.

## COE and CSE proof

Use the compact Gelfand pairs

\[
(G,K)=
\begin{cases}
(U(N),O(N)),&\beta=1,\\
(U(2N),Sp(N)),&\beta=4.
\end{cases}
\]

Here \(Sp(N)\) means the compact group of quaternionic rank \(N\),
acting on \(\mathbb C^{2N}\). Some references write \(Sp(2N)\) using
the complex matrix dimension. For COE, \(K=O(N)\), not \(SO(N)\).

The lift \(F(g)=f(gg^{T/R})\) is right \(K\)-invariant. Spectrality makes
it left \(K\)-invariant as well. The spherical representation indexed by
an integer signature \(\lambda\) has highest weight \(2\lambda\) for COE,
and \((\lambda_1,\lambda_1,\ldots,\lambda_N,\lambda_N)\) for CSE.
Let \(v_\lambda\) be its unit \(K\)-fixed vector and
\(d_\lambda\) its representation dimension. Its spherical matrix coefficient is

\[
\varphi_\lambda(g)
=\langle v_\lambda,\pi_\lambda(g)v_\lambda\rangle,
\qquad \|\varphi_\lambda\|_{L^2(G)}^2=d_\lambda^{-1}.
\]

The normalized spherical function on the eigenvalues \(z_1,\ldots,z_N\)
of \(gg^{T/R}\) is

\[
\varphi_\lambda(g)=
\frac{P_\lambda^{(\alpha)}(z_1,\ldots,z_N)}
{P_\lambda^{(\alpha)}(1^N)},\qquad
\alpha=2\ \hbox{or}\ 1/2.
\tag{3}
\]

These identifications are the standard compact symmetric-space theorem;
the parameter convention is checked against the primary sources.

Let \(T\) be the diagonal torus in COE and the paired torus in CSE.
For \(t\in T\), \(t^{T/R}=t\) and \(tt^{T/R}=t^2\).
Multiplication \(g\mapsto tg\) sends \(gg^{T/R}\) to \(tQt\),
which has the same spectrum as \(t^2Q\).
The squaring map preserves Haar measure on \(T\). Therefore phase averaging
of a spectral function is precisely left \(T\)-averaging of its lift.

Set \(\Pi_T=\int_T\pi_\lambda(t)\,dt\), the orthogonal projection on
the \(T\)-fixed vectors. Schur orthogonality yields

\[
\frac{\|A\varphi_\lambda\|_2^2}{\|\varphi_\lambda\|_2^2}
=\|\Pi_Tv_\lambda\|^2
=\langle v_\lambda,\Pi_Tv_\lambda\rangle
=\int_T\varphi_\lambda(t)\,dt.
\]

By (3), the final integral is

\[
\frac{[z^0]P_\lambda^{(\alpha)}(z)}
{P_\lambda^{(\alpha)}(1^N)}.
\tag{4}
\]

Indeed \(\varphi_\lambda(t)=P_\lambda(t^2)/P_\lambda(1^N)\),
and integration kills every nonconstant integer Laurent monomial.
If \(\sum_i\lambda_i\ne0\), (4) vanishes. If the sum is zero but
\(\lambda\ne0\), the coefficient theorem bounds (4) by \(1/(N+\alpha)\).

The spherical functions form a complete orthogonal basis of the
\(K\)-bi-invariant subspace. Images of different representations remain
orthogonal after left \(T\)-averaging: they are still matrix coefficients
of inequivalent representations. Their images need not be spectral.
Expanding the centered \(F\) in this basis, applying (4) term by term,
and using \(L^2\) continuity of an averaging operator proves (2).

## CUE proof

The orthogonal basis for spectral functions is the irreducible Laurent
characters \(\chi_\lambda=P_\lambda^{(1)}\) of \(U(N)\).
Let \(d_\lambda=\chi_\lambda(I)\) and \(m_0(\lambda)\) be the zero-weight
multiplicity. Since \(P_T\) is the torus-fixed projection,

\[
A\chi_\lambda(Q)=\operatorname{Tr}(P_T\pi_\lambda(Q)),\qquad
\|A\chi_\lambda\|_2^2=m_0(\lambda)/d_\lambda,\qquad
\|\chi_\lambda\|_2^2=1.
\]

The zero-weight multiplicity is \([z^0]P_\lambda^{(1)}\).
The same coefficient theorem gives \(m_0/d_\lambda\le1/(N+1)\)
for every nontrivial balanced signature; unbalanced signatures average
to zero. Character orthogonality then proves (2).

## Sharpness

Let

\[
f_*(Q)=|\operatorname{tr}_\beta Q|^2
-\frac{\alpha N}{N-1+\alpha}.
\tag{5}
\]

Equation (8) of the coefficient theorem shows that \(f_*\) is a scalar
multiple of the highest-root spherical mode. Thus it attains equality
in (2). The mean subtracted in (5) is \(2N/(N+1)\), \(1\),
or \(N/(2N-1)\), for COE, CUE, or CSE respectively.

The dimension formula and spherical orthogonality also give exact controls:

| Ensemble | \(\operatorname{Var}f_*\) | \(\operatorname{Var}Af_*\) |
|---|---|---|
| COE | \(\frac{4(N-1)(N+2)^2}{(N+1)^2(N+3)}\) | \(\frac{4(N-1)(N+2)}{(N+1)^2(N+3)}\) |
| CUE | \(1\) | \(1/(N+1)\) |
| CSE | \(\frac{(N-1)^2(2N+1)}{(2N-1)^2(2N-3)}\) | \(\frac{2(N-1)^2}{(2N-1)^2(2N-3)}\) |

For COE the relevant \(U(N)\) dimension is
\(N^2(N-1)(N+3)/4\). For CSE the relevant \(U(2N)\) dimension is
\(N^2(2N-3)(2N+1)\). These are the Weyl dimension products for the
weights specified above; dividing \(f_*(I)^2\) by that dimension
gives the first variance, and (2) gives the second with equality.

## What changes in the mechanism

Classical mixing estimates treat squared transition amplitudes and do not
directly control interference. Here the actual torus projection is resolved
into representation modes. Its normalized zero-weight content is bounded
by a positive coefficient identity. This controls bounded local observables
all at once, instead of only a finite list of low trace moments.
