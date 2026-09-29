# Reversible correction and short-time path comparison

**Claim ID: BGS-FLOW-005.** Project proof, author self-review, 29 September
2026. No independent review, formal certificate, or priority claim.
Definitions of $L_X$, $p_j$, $m_j$, and the Hilbert--Schmidt covariance
$\mathcal C_U$ are those of [FLOW-003](quadratic_coboundary_noise.md).
The processes below are auxiliary noise, not a deterministic BGS limit.

## 1. Exact reversible drift

With $\operatorname{Im}B=(B-B^*)/(2i)$, set

$$
A(U)=-\operatorname{Im}\left[
 (m_2+m_1^2/2)U^{*2}+(m_2\bar m_1/2)U^*\right]. \tag{1}
$$

This is a smooth traceless Hermitian matrix commuting with $U$.
For a real orthonormal basis $E_a$ of traceless Hermitian matrices write
$D_aF(U)=\left.\partial_s F(e^{isE_a}U)\right|_0$ and
$C_{ab}=\langle E_a,\mathcal C_UE_b\rangle$. Then

$$
L_R=L_X+D_A=\frac12\sum_{a,b}D_a(C_{ab}D_b). \tag{2}
$$

Consequently the normalized Haar measure on each determinant coset is
reversible. This does not imply uniqueness of its invariant measure:
scalar matrices have $\mathcal C_U=A(U)=0$ and are absorbing.

Here is a radial derivation that also identifies the full matrix operator.
For simple eigenvalues $z_j=e^{i\theta_j}$, put

$$
v_{jk}=\frac{1-\operatorname{Re}(m_2/(z_jz_k))}{N},\qquad
\Sigma_{jk}=\delta_{jk}v_{jj}
 -\frac{2\sin^2(\theta_j-\theta_k)}{N^2},\qquad
\ell_j=\sum_{k\ne j}\cot\frac{\theta_j-\theta_k}{2}.
$$

Second-order eigenvalue perturbation gives the raw angle drift
$b_j=\frac12\sum_{k\ne j}v_{jk}\cot((\theta_j-\theta_k)/2)$.
Differentiate the displayed covariance, including the derivative of
$m_2$, and pair the $j,k$ terms in the score sum to obtain

$$
\sum_k\partial_k\Sigma_{jk}
 =-\frac4N\operatorname{Im}(m_2z_j^{-2}),\qquad
\sum_k z_k^2\ell_k=i[(N-2)p_2+p_1^2]. \tag{3}
$$

For the second identity use
$(z_j^2-z_k^2)\cot((\theta_j-\theta_k)/2)=i(z_j+z_k)^2$.
The radial divergence-form drift is
$\frac12(\operatorname{div}\Sigma+\Sigma\ell)$, since the Haar density
is proportional to the squared Vandermonde. Subtracting $b_j$ gives
exactly the diagonal entries of (1). Both coefficients and the density
are invariant under common phase, and $\Sigma\mathbf1=0$, so this is
also the divergence on a fixed-sum angle hyperplane.

The difference between the right side of (2) and $L_X$ is first order
and conjugation equivariant. At simple $U$, invariance under its diagonal
stabilizer forces that vector field to commute with $U$. Its radial
components therefore determine it completely. Equation (3) proves (2)
on the simple-spectrum set; smoothness extends the identity everywhere.
Integration by parts against Haar now proves symmetry and invariance.
The smooth covariance factorization in [FLOW-004](quadratic_noise_coupling.md)
gives global existence and uniqueness in law; adding (1) preserves these.

## 2. Gradient identity and trace action

In left Hermitian coordinates with the unnormalized Hilbert--Schmidt metric,

$$
A=-\frac1{4N}\operatorname{grad}F_N,\qquad
F_N=|p_2|^2+N^{-1}\operatorname{Re}(p_2\bar p_1^2). \tag{4}
$$

Indeed the two angle derivatives are
$4\operatorname{Im}(p_2z_j^{-2})$ and
$2\operatorname{Im}(p_1^2z_j^{-2}+p_2\bar p_1z_j^{-1})$.
Conjugacy and common-phase invariance identify the full traceless
gradient. The covariance is not the scalar Hilbert--Schmidt metric;
(4) supplies no Gibbs density for the raw generator.

Put $c=m_2+m_1^2/2$, $d=m_2\bar m_1/2$. Direct differentiation gives

$$
D_Ap_k=-\frac{k}{2}
 [c p_{k-2}-\bar c p_{k+2}+d p_{k-1}-\bar d p_{k+1}]. \tag{5}
$$

In the bounded fixed-trace regime the sole order-one correction is
$D_Ap_2=-p_2+o(1)$. The path-space CLT, including the required moment
bounds, is proved in [FLOW-006](quadratic_noise_trace_fluctuations.md).

## 3. Total variation of the raw and reversible path laws

Suppose $\max(|p_1(U_0)|,|p_2(U_0)|)\le K/2$, $N\ge4K$, $K>0$.
For $0<t\le1/12$, the two laws on $C([0,t],U(N))$ satisfy

$$
d_{\rm TV}(P_X^t,P_R^t)
\le\min\{1,\ 2K\sqrt t+16e^{-K^2/(768t)}\}. \tag{6}
$$

Here $d_{\rm TV}=\sup_B|P(B)-Q(B)|$. Stop both processes at
$\sigma=\inf\{s:\max(|p_1|,|p_2|)\ge K\}$. Before stopping,

$$
\|A\|_{\rm op}\le K/N+K^2/N^2,\qquad
\mathcal C_U\ge(1-K/N)I/N,
$$
$$
\langle A,\mathcal C_U^{-1}A\rangle
\le\frac{K^2(1+K/N)^2}{1-K/N}\le\frac{25K^2}{12}. \tag{7}
$$

The bounded control $\mathcal C_U^{-1/2}A$ satisfies Novikov's condition.
Girsanov on the common smooth diffusion, followed by the stopped-path
map, bounds relative entropy in either direction by $25K^2t/24$.
Pinsker therefore gives $d_{\rm TV}(P_{X,\sigma}^t,P_{R,\sigma}^t)
\le5K\sqrt{t/48}\le K\sqrt t=:\delta$.
The raw exit estimate from FLOW-004 is
$P_X(\sigma\le t)\le8e^{-K^2/(768t)}=:\varepsilon$.
The hitting event is measurable from the stopped path, so its probability
under the reversible law is at most $\varepsilon+\delta$.
Each full path equals its stopped path outside this hitting event.
The triangle inequality gives $\delta+\varepsilon+
(\varepsilon+\delta)$ and proves (6).

For bounded initial low traces and any $t_N\to0$, the two **full path
laws** thus have vanishing total variation. Endpoint laws and all bounded
endpoint observables inherit this comparison. No assertion of path total
variation to Dyson motion is made: Dyson has a different covariance.
No claim is made at fixed positive time or about deterministic noise removal.
