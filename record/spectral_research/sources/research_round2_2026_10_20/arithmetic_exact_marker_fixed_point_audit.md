> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round2_2026_10_20/arithmetic_exact_marker_fixed_point_audit.md`. Embedded SHA256: `60399c2a4c8ca741e99cfaf00f5a29d15c10bfb362a51c4ff5088b84ff292e7b`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/dephasing.md).

# Independent audit: exact marker fixed point and detector center

20 October 2026. The complete input
`root_exact_marker_fixed_point.md`, SHA-256
`a98659bd0e9e742a525d493ed1a130bbb987df164e3dc1279ad66db7e0bb2b5a`,
was read independently. **PASS for every mathematical formula and
conclusion.** One harmless matrix-rank terminology issue is recorded
at the end.

## 1. Symbol and fixed point

For odd N, with h=(N+1)/2,

$$
e_N(k(x+hl))=(-1)^{kl}
       \exp\bigl(2\pi i k(x+l/2)/N\bigr).
$$

Thus T_N(l,k)=(-1)^(kl)W_N(k,l), equivalently the identity stated
in the input. Only l=0,+1,-1 occur in the original symbol. The
l=0 terms stay V(q); multiplying the other Fourier coefficients
by (-1)^k replaces r(q) by r(q+1/2). This checks the symbol
convention used throughout the calculation.

At q=0 and q=1/2, both r and r' vanish. At q=1/2 the derivative
of cos(14 pi q) also vanishes. Therefore the gradient of the
corrected symbol a is zero at (1/2,p) for every p. The Hamiltonian
flow fixes this whole line, exactly at every time.

With L=S^(-1), L(1/2,0)=(3/2,-1), differing from (1/2,0) by an
integer vector. Hence x_*=(1/2,0) is an exact fixed point of
Psi=Phi_(-tau)L.

The identification H(x_*)=x_* can also be checked directly from
the already verified quantitative conjugacy, without an unspecified
structural-stability radius. In
`fermionic_pressure_transfer.md`, SHA-256
`90ebc84c3c9fb7c049a1a9d11e0d5dcb72c4fc89b362da3f848521a7bca79756`,
Sections 1--2 give the equivariant lifts

$$
\Psi(x)=Lx+v(x),\quad H(x)=x+w(x),\quad
HL=\Psi H,\quad \|Dv\|<10^{-69}
$$

in fixed eigen-coordinates of L. Here v(x_*)=0. Equivariance of
H and Lx_*=x_*+n_* ensure that the lift of H(x_*) has the same
fixed-point integer n_*. Consequently

$$
(L-I)w(x_*)=-[v(x_*+w(x_*))-v(x_*)].
$$

In these coordinates
$\|(L-I)^{-1}\|=(1-(3+2\sqrt2)^{-1})^{-1}<1.21$.
Taking norms forces w(x_*)=0. No differentiability of H is used.

## 2. Hessian and exact flow derivative

Direct differentiation gives

$$
r''(q)=196\pi^2\cos(14\pi q)(1+\cos(2\pi q))
-56\pi^2\sin(14\pi q)\sin(2\pi q)
-4\pi^2(1-\cos(14\pi q))\cos(2\pi q).
$$

It follows that r''(0)=392 pi^2 and r''(1/2)=8 pi^2. The second
derivative of r(q)sin(2 pi q) is zero at q=1/2: every product-rule
term contains r, r', or sin(2 pi q), all zero there. Since
cos(alpha_0)=-3/5,

$$
a_{qq}(x_*)=
\left(196+\frac8{10}-\frac{3\cdot392}{500}\right)\pi^2
=\frac{24306}{125}\pi^2.
$$

The p and mixed derivatives contain respectively r(q+1/2) or
r'(q+1/2), so a_pp=a_qp=0 at x_*.

For X_a=(a_p,-a_q)/(2 pi), put sigma=12153 pi/125. Then

$$
DX_a(x_*)=\begin{pmatrix}0&0\\-\sigma&0\end{pmatrix},
\qquad (DX_a(x_*))^2=0.
$$

Because the base orbit is constant, its variational equation has
this constant coefficient matrix. Hence

$$
D\Phi_{-\tau}(x_*)=I-\tau DX_a(x_*)
=\begin{pmatrix}1&0\\\tau\sigma&1\end{pmatrix}
$$

is an exact exponential, not a first-order truncation. Multiplying
on the right by L gives

$$
D\Psi(x_*)=
\begin{pmatrix}3&-4\\-2+3\tau\sigma&3-4\tau\sigma\end{pmatrix}.
$$

The determinant is exactly 1 and the trace is exactly

$$
T_*=6-4\tau\sigma=6-\frac{48612}{125}\pi\tau.
$$

At tau=10^(-80), the elementary bound pi<4 gives T_*>5+1/5.
Thus the larger eigenvalue

$$
\Lambda=\frac{T_*+\sqrt{T_*^2-4}}2
$$

is greater than 5, and the other eigenvalue is Lambda^(-1).

## 3. Slopes, area factor, and the detector

For a normalized eigenvector (1,s), the first row gives 3-4s
equal to the corresponding eigenvalue. Hence

$$
s_u=(3-\Lambda)/4<0,
\qquad s_s=(3-\Lambda^{-1})/4>0,
$$

$$
\chi=s_s-s_u
=\frac{\Lambda-\Lambda^{-1}}4
=\frac{\sqrt{T_*^2-4}}4>0.
$$

This is also the absolute determinant of the two q-normalized
tangent vectors used in the encounter area calculation. Both the
sign and the normalization agree with the endpoint-law proof.

The coordinate positions x_-/N and x_+/N are respectively
1/2-1/(2N) and 1/2+1/(2N). A consecutive coordinate window
centered at 1/2 with length comparable to sqrt N contains both
for all sufficiently large odd N. The previously independently
audited cyclicity theorem applies when 7 does not divide N.

For r=|I| and s=|J|>=r, the restricted matrix P_J F_N P_I has
rank r by the nonzero consecutive-row Vandermonde. Therefore
P_I F_N^*P_J F_N P_I is positive definite on P_I C^N and has
range exactly P_I C^N. The cyclic endpoints imply full visibility.

Terminology: P_J F_N P_I is s-by-r and has full **column** rank;
its adjoint has full row rank. The input's phrase "full row rank"
is correct only if the latter orientation is intended. Replacing
it with "rank equal to the coordinate-window length" removes this
ambiguity without changing any argument or result.

## 4. Scope

This audit verifies exact geometry and the applicability of the
already proved cyclicity theorem. No perturbative error in tau is
introduced. It supplies no lower bound on small spectral weights
and no estimate of the original signed trace correlations at
times of order N. It is not a solution or a counterexample to
H_diag.
