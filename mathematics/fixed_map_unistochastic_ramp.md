# Repaired one-step unistochastic gap and the exact CUE ramp skeleton

Date: 21 September 2026.

Status: project proof for the prescribed frozen operator, using standard
fixed-time semiclassical FIO theory as an external analytic input. The exact
cyclic identities are finite-dimensional. The proof below repairs the
14--16 September argument to the **correct ordinary midpoint symbol** of the
raw modular generator. It proves the ramp skeleton below the CUE plateau,
not pair BGS.

## 1. An exact identity for every unitary matrix

For \(V\in U(N)\) in any fixed orthonormal basis define

\[
P_V(x,y)=|V_{xy}|^2.
\]

It is doubly stochastic. A closed length-\(m\) path
\(\gamma=(x_0,\ldots,x_{m-1})\), \(x_m=x_0\), has amplitude

\[
A_V(\gamma)=\prod_{j=0}^{m-1}V_{x_{j+1},x_j}.
\]

Cyclic rotation does not change this scalar product. Hence for every rotation
\(\tau_s\),

\[
\sum_\gamma A_V(\gamma)\overline{A_V(\tau_s\gamma)}
=\sum_\gamma|A_V(\gamma)|^2
=\operatorname{Tr}P_V^m.
\tag{1}
\]

The multiplicity-counted cyclic skeleton is therefore exactly

\[
\boxed{D_V^{\rm cyc}(m)=m\,\operatorname{Tr}P_V^m.}
\tag{2}
\]

Define the exact algebraic residual

\[
R_V^{\rm cyc}(m)=|\operatorname{Tr}V^m|^2
-m\operatorname{Tr}P_V^m.
\tag{3}
\]

For \(m<N\), proving \(\operatorname{Tr}P_V^m=1+o(1)\) identifies the CUE
ramp \(m\) inside the deterministic path expansion; it does not estimate
(3).

## 2. A Frobenius criterion

If \(P\) is doubly stochastic and

\[
\|P\|_F^2\le2-\delta,
\]

then

\[
\boxed{s_2(P)\le\sqrt{1-\delta}.}
\tag{4}
\]

Consequently

\[
|\operatorname{Tr}P^m-1|\le(N-1)s_2(P)^m.
\tag{5}
\]

## 3. The spectrally conjugate frozen quantization

Let

\[
K_N=e^{i\tau N A_N},\qquad U_N=K_NM_N,\qquad
V_N=M_NK_N=M_NU_NM_N^{-1}.
\]

Thus \(V_N\) has exactly the spectrum of the prescribed \(U_N\). After the
raw-to-midpoint gauge correction, the same matrix \(A_N\) is the ordinary
Weyl quantization of

\[
g(q,p)=\cos14\pi q+\frac{r(q)}{10}
+\frac{r(q)\sin2\pi q}{100}
+\frac{r(q+\tfrac12)\cos(2\pi p-\alpha)}{100}
-\frac1{10},
\tag{6}
\]

where \(e^{i\alpha}=(-3+4i)/5\). Put
\(\kappa_0=\tau/(2\pi)\). The maintained symmetry proof gives
\(\|DX_g\|\le3000\), hence for the lifted first coordinate \(Q(q,p)\),

\[
|\partial_pQ-4|
\le7(e^{3000|\kappa_0|}-1)=:\varepsilon_*,
\tag{7}
\]

and \(\varepsilon_*\ll10^{-2}\). The position projection therefore has
exactly four global noncaustic branches.

Standard fixed-time FIO theory for Weyl Hamiltonian propagators, together
with torus descent, gives uniformly

\[
V_N(x,y)=N^{-1/2}\sum_{\nu=0}^3
a_{\nu,N}(q_x,Q_y)e^{2\pi iN W_\nu(q_x,Q_y)}
+O(N^{-3/2}),
\tag{8}
\]

with

\[
a_{\nu,N}=a_{\nu,0}+O(N^{-1}),\qquad
|a_{\nu,0}|^2=w_\nu(q,Q)
={1\over|\partial_pQ(q,p_\nu)|}.
\tag{9}
\]

The external analytic inputs are the fixed-time FIO expansion (for example
Robert, arXiv:0908.0847) and standard torus quantization/descent for nonlinear
Anosov maps (for example Faure, arXiv:nlin/0610004). No long-time Egorov
remainder is used here.

## 4. Corrected nonpairing branch dephasing

At \(\kappa=0\),

\[
W_\nu^0(q,Q)=
{3q^2-2q(Q+\nu)+3(Q+\nu)^2\over8}
\]

up to branch constants. For a fourth-moment quadruple
\((a,b,c,d)\), put
\(\Psi=W_a+W_b-W_c-W_d\) and
\(\Delta=a+b-c-d\).

If \(\Delta\not\equiv0\pmod4\), a grid slope stays a positive distance from
the integer lattice. Suppose \(\Delta\equiv0\pmod4\) and the two branch
multisets differ. Set

\[
C=i^a+i^b-i^c-i^d.
\]

Then \(C\ne0\). Since \(e^{-i\alpha}=(-3-4i)/5\),

\[
|\Re(e^{-i\alpha}C)|\ge{1\over5}.
\tag{10}
\]

The historical proof used \(q_0=1/14\), which is wrong after the gauge repair
because \(r(q_0+1/2)=0\). Use instead

\[
q_0={1\over7},\qquad Q_0={3\over7}.
\]

Then \(p_\nu=\nu/4\) at \(\kappa=0\), and

\[
r(q_0+\tfrac12)=2(1-\cos(2\pi/7))>{1\over2}.
\tag{11}
\]

Hamilton--Jacobi variation gives, up to a harmless global sign,

\[
\left|
\partial_Q^2\partial_\kappa\Psi
\right|_{\kappa=0,(q_0,Q_0)}
>{\pi^2\over4000}.
\tag{12}
\]

The shift \(q\mapsto q+1/2\) changes Fourier signs but not magnitudes or
frequencies. The same finite-Fourier majorant gives
\(M_j\le2(20\pi)^j\), \(j=1,\ldots,4\). Elementary variational equations
and implicit differentiation give the deliberately loose bound

\[
\sup_{|\kappa|\le10^{-6}}
|\partial_Q^2\partial_\kappa^2\Psi|<10^{10}.
\tag{13}
\]

Since \(10^{10}|\kappa_0|<2\cdot10^{-71}\), every aliased nonpairing phase
at the actual \(\kappa_0\) is genuinely nonlinear. Poisson summation and
fixed-dimensional oscillatory integration therefore make every nonpairing
fourth-moment branch contribution \(o(1)\).

## 5. Uniform one-step gap

The pairing terms give

\[
\|P_{V_N}\|_F^2\longrightarrow
\int_{\mathbb T^2}
\left(2K(q,Q)^2-\sum_{\nu=0}^3w_\nu(q,Q)^2\right)dq\,dQ,
\tag{14}
\]

where \(K=\sum_\nu w_\nu\). If merely
\(\varepsilon_*\le10^{-2}\), then the integrand is at most

\[
2\left({4\over4-0.01}\right)^2
-{4\over(4+0.01)^2}
=1.7612829534\ldots<1.762.
\tag{15}
\]

Hence

\[
\boxed{\limsup_{N\to\infty,\ N\ {\rm odd}}s_2(P_{V_N})<7/8.}
\tag{16}
\]

For all sufficiently large odd \(N\),

\[
\operatorname{Tr}P_{V_N}^m
=1+O(N(7/8)^m)
\tag{17}
\]

uniformly in \(m\ge1\).

## 6. The repaired CUE ramp skeleton

Combining (2) and (17),

\[
\boxed{
D_{V_N}^{\rm cyc}(m)
=m+O(mN(7/8)^m).}
\tag{18}
\]

For every fixed \(0<\sigma<1\) and
\(w\in C_c^\infty((0,\sigma))\),

\[
{1\over N^2}\sum_{m\ge1}w(m/N)
\left[D_{V_N}^{\rm cyc}(m)-m\right]
=O(N^{-1}).
\tag{19}
\]

Thus the deterministic path expansion contains the complete CUE **ramp**
below the plateau. On a genuine Heisenberg window, nontrivial cyclic
stabilizers have super-polynomially small total cyclic weight because
fixed-time FIO bounds also give
\(\max_{x,y}P_{V_N}(x,y)\le C/N\).

## 7. Boundary

One-step mixing does not imply BGS. A discrete Fourier matrix already has a
maximally flat unistochastic matrix while its spectral form factor is highly
non-CUE. The theorem isolates the positive ramp term but does not control

\[
R_{V_N}^{\rm cyc}(m)
=|\operatorname{Tr}U_N^m|^2
-m\operatorname{Tr}P_{V_N}^m.
\]

The plateau \(m\ge N\), signed post-cyclic remainder, Fourier-tail control
and all higher joint traces remain separate obligations.

Fresh regression is in
[fixed_map_unistochastic_ramp_audit.py](../computations/verification/fixed_map_unistochastic_ramp_audit.py).
