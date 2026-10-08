# Direct real-flow transport of absorbed scalar sources

**Stable claim ID:** BGS-TRACE-056. **Status:** project proof with independent internal reconstruction, 8 October 2026. No priority claim. This proves a linear-source consequence directly, without assuming the unprovided physical-cavity proofs in the supplied manuscript.

## Exact statement

Let S_m be deterministic unitary, δ_m=max|S_ij|²→0, and |||S_m|²-J_m||≤ρ<1. Let H_m be a deterministic Hermitian matrix, independent of D, with Tr H_m=m and Tr H_m²≤C_H m. Positivity of H is not needed for this real-flow result. Let D have independent uniform coordinate phases, reused throughout the flow, and set

$$W_x=DS_m e^{ixH_m/m},\qquad V_x=e^{ix/m}DS_m,$$

$$Z_m(s;V)=\frac1m\operatorname{Tr}\big[(I-e^{-s/m}V)^{-1}-I\big],\qquad \operatorname{Re}s>0.$$

For each fixed R, let β_{m,R} be a uniform upper bound for the norm of the averaged full eigenspace pinching of W_x on traceless matrices, for |x|≤R. [TRACE-053](max_entry_phase_channel.md) supplies

$$\beta_{m,R}=O_{\rho,R,C_H}\!\left(\frac{\log\log(1/\delta_m)}{\log(1/\delta_m)}\right).$$

For sufficiently large m, each |x|≤R and each Re s>0,

$$\mathbb E_D|Z_m(s;W_x)-Z_m(s;V_x)|
\le\frac{|x|\sqrt{(C_H-1)\beta_{m,R}}}{2m\sinh(\operatorname{Re}s/m)}
\le\frac{|x|\sqrt{(C_H-1)\beta_{m,R}}}{2\operatorname{Re}s}.\tag{RF1}$$

Thus the difference tends to zero in L¹, locally uniformly on the absorbed half-plane, uniformly for bounded real x. Every fixed derivative in s has the same convergence by Banach-valued Cauchy estimates. These are unweighted scalar traces of normally absorbed unitary endpoints, not the H-weighted source of DS exp(-sH/m).

## 1. Uniform averaged-pinching input

Unitarity gives δ_m≥1/m. For |x|≤R,

$$\|S_me^{ixH/m}-S_m\|_{\mathrm{op}}
\le |x|\sqrt{C_H/m},\qquad
\max_{ij}|(S_me^{ixH/m})_{ij}|^2\le(2+2R^2C_H)\delta_m.$$

On the diagonal matrix subspace the intensity matrix is the restriction of Π Ad(S) Π. Consequently its change in operator norm is at most twice the unitary operator-norm change. The fixed singular gap persists uniformly. Applying TRACE-053 proves the displayed β rate; no constants depending on a growing moment order are hidden in that statement.

## 2. Eigenphase flow, including multiplicities

Write B=H-I, so Tr B=0 and ||B||_F²≤(C_H-1)m. Along an analytic real unitary flow, choose absolutely continuous eigenangle branches θ_j(x). At a simple point,

$$\theta_j'(x)=m^{-1}\langle\psi_j(x),H\psi_j(x)\rangle.$$

At a multiple eigenvalue, the branch velocities are the eigenvalues of the compression of H/m to that eigenspace. Choosing a basis diagonalizing this compression gives, almost everywhere,

$$\sum_j|\theta_j'(x)-1/m|^2
=m^{-2}\|\mathcal E_{W_x}B\|_F^2.$$

The squared norm of an orthogonal pinching equals its quadratic form. Since B is independent of D,

$$\mathbb E\|\mathcal E_{W_x}B\|_F^2
=\langle B,(\mathbb E\mathcal E_{W_x})B\rangle
\le\beta_{m,R}(C_H-1)m.$$

Cauchy--Schwarz over j and D, followed by integration, yields a coupled branch matching

$$\mathbb E\sum_j|\theta_j(x)-\theta_j(0)-x/m|
\le|x|\sqrt{(C_H-1)\beta_{m,R}}.\tag{RF2}$$

Branches are lifted continuously; using geodesic circular distances only decreases the bound. The left side is the averaged transport cost in m-radian microscopic units: (1/m)sum_j m|Δθ_j|. Conventional unfolding mθ/(2π) divides this cost by 2π. No eigenvalue-gap denominator is estimated.

## 3. Common-phase smoothing removes the dimensional Lipschitz loss

Jointly rotating all original coordinate phases rotates both coupled endpoints and does not change the matching displacements. Introduce this independent common phase φ and average it. For r=e^{-Re s/m} and k_r(θ)=re^{iθ}/(1-re^{iθ}),

$$\|k_r'\|_{L^1(d\phi/(2\pi))}
=\frac{r}{1-r^2}=\frac1{2\sinh(\operatorname{Re}s/m)}.$$

The imaginary part of s merely shifts the common phase. For any matched circular angles, the L¹ norm of a translated kernel difference is at most their lifted distance times this derivative norm. Apply the triangle inequality only after forming the endpoint source difference. Division by m and (RF2) prove (RF1). A worst-case pointwise resolvent Lipschitz estimate would lose a factor m; common-phase integration is essential.

For a compact K in Re s>0, choose a fixed Cauchy neighborhood in that half-plane. Integrating the locally uniform L¹ estimate on its contour gives convergence of each fixed complex derivative. This does not multiply random sources or remove absorption.

## Precise remaining boundary

This is a comparison with the same scalar endpoint phase ensemble. It supplies no value for that endpoint, no Haar/CUE identification, no all-order mixed-source bound, and no deterministic D=I conclusion. In particular, the anisotropic physical source

$$m^{-1}\operatorname{Tr}\{H[(I-DS e^{-sH/m})^{-1}-I]\}$$

requires its own correlated source/covariance argument. The full physical-cavity reduction and its polylogarithmic delay barriers in Sections 88--89.3 of the supplied PDF remain unpromoted pending those raw proofs. TRACE-005 and deterministic BGS remain open.
