> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round8_2026_10_21/r8_return_approximate_eigenoperator_addendum.md`. Embedded SHA256: `8560a8f6ab447e18513f50a55618da9311c45cbfcd5d906c11782e08d786235e`.
> [Thematic guide](../../topics/dephasing.md).

# Coordinate delocalization of every approximate adjoint eigenoperator

21 October 2026. Round 8. Addendum to the uniform shrinking-window theorem.

This is a consequence of the proved original-family theorem in
`r8_return_uniform_shrinking_windows.md`, frozen SHA-256
`c7329595d2f77c5f14fe0e68dd28204740c7faf1d3527981f2a4a05929cc4d26`.
That source is unchanged by this addendum. Its definitions of
$W_N=\operatorname{Ad}U_N$, $\iota_N$, $e_N$, $J_N$,
$\iota_{0,N}=\iota_N(I-J_N)$, and $q_N(\delta)$ are retained.

## Statement

Let $X_N\in M_N(\mathbb C)$ and $\zeta_N\in\mathbb S^1$
be arbitrary, possibly depending on every feature of the original
unitary $U_N$. Suppose
$$
 \|X_N\|_{\rm HS}\le1,\qquad \operatorname{Tr}X_N=0,\qquad
 \varepsilon_N:=\|(W_N-\zeta_N)X_N\|_{\rm HS}\longrightarrow0.
 \tag{1}
$$
Then, along all odd dimensions,
$$
 \boxed{\|\operatorname{diag}X_N\|_{\rm HS}\longrightarrow0.}
 \tag{2}
$$
In particular, this conclusion is uniform over the chosen approximate
eigenvalue, all approximate eigenoperators, and every rate at which
their residuals tend to zero.

More quantitatively, if
$\delta_N=\max\{\sqrt{\varepsilon_N},1/N\}$, then for all
sufficiently large $N$,
$$
 \|\operatorname{diag}X_N\|_{\rm HS}
 \le\sqrt{q_N(\delta_N)}
       +\frac\pi2\sqrt{\varepsilon_N}.
 \tag{3}
$$
The $1/N$ in this choice merely keeps the width positive when the
residual vanishes exactly. It has no semiclassical role in the proof.

## Proof

Write $\zeta_N=e^{i\theta_N}$, and let
$E=E_N(I(\theta_N,\delta_N))$. Split
$X_N=EX_N+(I-E)X_N$. On the complement of the arc, the spectral
distance to $\zeta_N$ is at least
$$
 2\sin(\delta_N/2)\ge 2\delta_N/\pi
$$
for $0<\delta_N<\pi$. The finite-dimensional spectral theorem
therefore gives
$$
 \|(I-E)X_N\|_{\rm HS}
 \le\frac{\pi\varepsilon_N}{2\delta_N}
 \le\frac\pi2\sqrt{\varepsilon_N}.
 \tag{4}
$$
This includes $\varepsilon_N=0$, when the left-hand side is zero.

Let $\Pi_N=\iota_N\iota_N^*$ and
$u_N=\mathbf I_N/\sqrt N$. The traceless coordinate-diagonal
projection on matrix Hilbert space is
$$
 \Pi_{0,N}=\Pi_N-|u_N\rangle\langle u_N|
           =\iota_{0,N}\iota_{0,N}^*.
$$
Since $u_N$ is an eigenvector of $W_N$, it reduces every
spectral projection. Thus $EX_N$ is traceless. Factorization of
the projection product gives
$$
 \|\Pi_{0,N}E\|^2
 =\|\Pi_{0,N}E\Pi_{0,N}\|
 =\|\iota_{0,N}^*E\iota_{0,N}\|
 \le q_N(\delta_N).
 \tag{5}
$$
The middle equality compares the same nonzero operator on the
isometric traceless diagonal space; both sides vanish on the scalar
direction. Hence
$$
 \|\Pi_NEX_N\|_{\rm HS}
   =\|\Pi_{0,N}EX_N\|_{\rm HS}
   \le\sqrt{q_N(\delta_N)}\,\|X_N\|_{\rm HS}.
$$
Combining this with (4) and the fact that $\Pi_N$ is a contraction
proves (3). The shrinking-window theorem gives
$q_N(\delta_N)\to0$, since $\delta_N\to0$; (2) follows.

For an arbitrary $X_N$ of Hilbert--Schmidt norm at most one, the
same conclusion can be phrased after subtracting its scalar part:
$$
 \left\|\operatorname{diag}X_N-
       \frac{\operatorname{Tr}X_N}{N}\mathbf I_N\right\|_{\rm HS}
       \longrightarrow0
$$
whenever $\|(W_N-\zeta_N)X_N\|_{\rm HS}\to0$.
Indeed the orthogonal projection onto the traceless matrices
commutes with $W_N$, so subtracting the scalar part cannot
increase either the norm or this residual. Apply the proved result
to that traceless part.

## Scope

The statement controls the coordinate component of a normalized
approximate eigenoperator; it does not count how many gap eigenvalues
occur in a microscopic arc. Consequently it does not remove the
spectral weights in the pair functional. By the perturbation
corollary of the source theorem, it also persists under arbitrary
$o(1)$ operator perturbations of $U_N$, including auxiliary
rounded spectra for which the microscopic target fails.
