> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round13_2026_10_21/root/exact_protected_sector_removal.md`. Embedded SHA256: `e32c63f1004dda27250f6481128f13f132c76a81612012c7514adf7c46912af3`.
> [Thematic guide](../../../topics/classical_trace.md).

# Exact removal of the whole protected trace terms

Round 13, 21 October 2026. Root derivation and author check.

## 0. Claim and scope

The original H_diag is not proved or disproved. This note strengthens §7 of
`orbit_correlations/protected_actions_and_one_step_trace.md`, frozen SHA-256
`b1dc645d52f16f7ca653f113796fb5d0b41764e7036f76a35b86328894ae714d`.
It removes the **exact whole trace terms** indexed by the protected periodic
points, including all their transverse corrections. A trace term here is an
integral in the exact trace identity, not a quantum invariant subspace.

Write
$$
\mathcal P=\{0,1/2\}\times\{j/8:0\le j<8\},\qquad
p_{m,N}=\operatorname{Tr}U_N^m.
$$
For every sufficiently large odd N, let $I_{m,N}(x)$ be the exact
coherent/Abel trace term associated to
$x\in\operatorname{Fix}\Psi^m$, as constructed below, and set
$$
Q_{m,N}^{\rm full}=
\sum_{x\in\mathcal P\cap\operatorname{Fix}\Psi^m}I_{m,N}(x).
\tag{0.1}
$$
Then, with the explicit fixed number $q_0=83/200$,
$$
\boxed{|Q_{m,N}^{\rm full}|\le20q_0^m\quad(m\ge1).}
\tag{0.2}
$$
The threshold on N is independent of m. The prescribed tau is unchanged.
Consequently, for any array of complex weights satisfying
$\sup_{m,N}|w_{m,N}|\le W<\infty$,
$$
\boxed{
\frac1{N^2}\sum_{m\ge1}|w_{m,N}|
\left|\,|p_{m,N}|^2-|p_{m,N}-Q_{m,N}^{\rm full}|^2\right|
\le W\left[
\frac{40q_0}{N(1-q_0)}+
\frac{400q_0^2}{N^2(1-q_0^2)}\right].}
\tag{0.3}
$$
In particular the same bound holds for the absolute value taken after the
complete signed sum. No convergence of the two separate unweighted infinite
sums is asserted. The series of their termwise differences is absolutely
convergent by (0.3).

This result eliminates only a counterexample mechanism based on these exact
protected trace terms. The trace terms for all other periodic points remain
unestimated in the required signed pair sum.

## 1. Inputs actually checked

Base master: SHA-256
`10b90c7d12668cd7327bcc08bda292f4c7d6cf82218ee95d5d4f7603fac86cef`.
The following raw proofs, and not merely their recorded verdicts, were read
at the indicated steps by root in this pass:

| Source | SHA-256 | Steps read and reconstructed |
|---|---|---|
| `research_continuation_2026_10_20/odd_trace_and_algebraic_rigidity.md` | `42832bfc27bbf307b154c781f7299912e7c3094e0a0c3ff2e3ade9f0e580764b` | §§2–8: modular normalization, comb, coherent frame, exact coset decomposition and Abel identity |
| `research_continuation_2026_10_20/exact_amplitude.md` | `69cd85816766b26358fb13058b3b26f9c243886cf863e5f8f9a6c6570e1a542e` | Entire proof: small-time phase; removable real-h shifts; convergent analytic-scale series; exact kernel; principal amplitude |
| `research_continuation_2026_10_20/gaussian_cocycle_and_modulus.md` | `c1a863e613a327acb5fe43ff1093c4a8fe51b37ebd5dcee9fddf0ae0a91986f1` | §§1–4.4: centered phase, saturated contour, trace-norm convergence, Gaussian spectrum, exact product trace |
| `research_continuation_2026_10_20/classical_trace_and_pair_diagonal.md` | `355f2c6deb1549c32ab7b7313774b8c27b1310d019013838fc5e3679721af55c` | §§1–2: near-cat generating function, strict concavity and one point per deck class |

The raw proofs are already included in the cumulative master. Their relevant
arguments are reconstructed here to expose the dependencies. This proof
does **not** use the first-order modulus cancellation, the repeated-orbit
normalization in §9 of the Gaussian source, or a finite-order Magnus estimate.

## 2. Exact identification of the trace terms

Use
$$
h=(2\pi N)^{-1},\quad t_*=\tau/(2\pi),\quad
L=\begin{pmatrix}3&-4\\-2&3\end{pmatrix},\quad
\zeta_N=e^{2\pi i(3N-1)/8}.
$$
The ordinary Weyl symbol is the shifted a in the orbit source. The exact
plane kernel of $e^{it_*A_h/h}\mu_L$ is
$$
K_V(Q,q)=\frac{e^{i\pi/4}}{\sqrt{8\pi h}}
e^{iF(Q,q)/h}B_h(Q,q),
\quad F=F_0+G,
\quad F_0=-\frac{3Q^2-2Qq+3q^2}{8}.
\tag{2.1}
$$
Here G and B are bounded on their fixed spatial analytic strips, the
Hessian of G is uniformly tiny, and B is continuous in real h at zero
in a smaller analytic strip. These are exact kernel statements from the
convergent bounded-operator construction, not a truncated time expansion.

For integer n use the honest integer representation
$R_n=(-1)^{n_qn_p}\mathcal T_n$.
The quotient by its invariant comb is exactly $\zeta_N^{-1}U_N$.
The normalized finite coherent frame gives
$$
\zeta_N^{-m}p_{m,N}
=\sum_{[n]\in\mathbb Z^2/(L^m-I)\mathbb Z^2}
\mathfrak T_h(R_{-n}V^m).
\tag{2.2}
$$
For each fixed m,N the word expansion of V has finite absolute coefficient
sum. Translated metaplectic coherent diagonals have Gaussian bounds whose
integrals are independent of the real translation. Thus the lattice sums
and integrals in (2.2) can be rearranged. The equality with the m-dimensional
Abel integral follows by Gaussian integration word by word; the bound is
again independent of its linear phase. No bound uniform in m on the word
coefficient sum is required to establish this exact identity separately for
each finite m.

In a class n the cyclic action is
$$
S_{m,n}(q_0,\ldots,q_{m-1})=
\sum_{j=0}^{m-1}F(q_{j+1},q_j)
-n_p(q_0+n_q/2),\qquad q_m=q_0+n_q.
$$
Its unperturbed Hessian is $-(6I-R-R^{-1})/4$, with spectrum
in [-2,-1], including m=1,2 with the repeated edges counted. The
perturbation Hessian is uniformly smaller than 1/2 in norm. Thus each
class has exactly one critical point. The equations at this point are
$\Psi^m x=x+n$. Changing the lift changes n by $(L^m-I)w$.
This gives a bijection between classes and torus fixed points. Define
$I_{m,N}(x)$ to be $\zeta_N^m$ times this exact class integral.

## 3. Whole integral as a trace-class product

For an edge x=(q,p), $\Psi x=(Q,P)$, put
$$
\widetilde F_x(z',z)=F(Q+z',q+z)-F(Q,q)-Pz'+pz.
$$
The linear terms telescope around a periodic orbit and cancel the winding
boundary term. The integer deck law cancels the lift dependence of this
centered function. Choose a fixed smooth odd saturating function psi with
psi(u)=u near zero, $0\le\psi'\le1$, and height inside the analytic
strip, and set
$$
s=\sqrt h,\quad z_s(y)=sy-i\psi(sy),\quad
J_s(y)=\frac{1-i\psi'(sy)}{1-i},\quad
\lambda=3+2\sqrt2,\quad \lambda_0=\frac{2\sqrt\pi}{\sqrt\lambda}.
$$
Let K_h(x) have kernel
$$
\lambda_0^{-1}B_h(Q+z_s(y'),q+z_s(y))J_s(y)
\exp\left(i\widetilde F_x(z_s(y'),z_s(y))/h\right).
\tag{3.1}
$$
The equality
$C_h\sqrt h(1-i)\lambda_0=\lambda^{-1/2}$
fixes the normalization per edge.

For U=(u',u), V=(psi(u'),psi(u)), write
$D=u'\psi(u')+u\psi(u)$. Monotonicity implies
$u'\psi(u)+u\psi(u')\le D$, and direct evaluation gives
$\operatorname{Re}(iF_0(U-iV))\le-D/2$.
If eta bounds every second derivative of G on the reserved strip, its
centered part has imaginary part at most 4 eta D in modulus. Here eta is
less than $2\cdot10^7t_*$, so
$$
\operatorname{Re}(i\widetilde F_x(U-iV))/h\le-D/(4h).
\tag{3.2}
$$
In the straight part D/h is quadratic in y,y'; in the saturated tails
it grows at least linearly in their absolute values. The exact amplitude
and its fixed derivatives are bounded on the contour. Hence (3.1) and its
weighted derivatives are integrable uniformly in the base point.

At positive Gaussian regularization the real cyclic integral can be
deformed to this product contour. The regulator controls the boundary
faces of a finite box; its removal is dominated by (3.2). This proves the
identity for every finite m. Rapid kernel decay then justifies the trace
of the cyclic product, for example by finite Hermite projections. Thus
$$
I_{m,N}(x)=\zeta_N^m\omega_{m,N}(x)\lambda^{-m/2}
\operatorname{Tr}\left[K_h(\Psi^{m-1}x)\cdots K_h(x)\right],
\quad |\omega_{m,N}(x)|=1.
\tag{3.3}
$$
Nothing was truncated on the right side.

## 4. Uniform norm bounds and the geometric estimate

For $A=1-\partial_y^2+y^2$, the eigenvalues are 2(n+1) and
$\|A^{-1}\|_{\rm HS}^2=\pi^2/24$. Therefore
$$
\|K\|_1\le\frac{\pi^2}{24}
\|A_{y'}A_y k\|_{L^2(\mathbb R^2)}.
\tag{4.1}
$$
For (3.1), Taylor expansion on a fixed straight part of the contour and
the exponentially small saturated tails give uniform convergence in
this weighted norm to
$$
k_{0,x}(y',y)=\lambda_0^{-1}B_0(Q,q)
\exp\big((y',y)D^2F(Q,q)(y',y)^T\big).
$$
This uses only fixed derivatives in a smaller strip. The tails are
$\exp(-c/h)$ times fixed polynomial factors and do not require a
global Gaussian bound on the saturated contour.

The reference Gaussian is
$$
k_G(y',y)=\lambda_0^{-1}
\exp\left[-3(y'^2+y^2)/4+y'y/2\right].
$$
Its Hermite eigenvalues are $1,\rho,\rho^2,\ldots$,
where $\rho=3-2\sqrt2$. This follows by Gaussian integration of
the Hermite generating function; the ground eigenvalue is one because
$3/4+1/\sqrt2=\lambda/4$. In particular
$$
\|K_G\|=1,\qquad
\|K_G\|_1=\frac1{1-\rho}=\frac{1+\sqrt2}{2}<1.207107.
$$
Differentiating the Gaussian in its Hessian entries and using (4.1)
gives the bound $\|K_{0,x}-K_G\|_1\le10^{12}\eta<10^{-60}$.
For completeness the coarse bound in this differentiation is
$8\cdot10^5(1+|Y|)^6e^{-|Y|^2/4}$ after the two oscillator
operators, for a quadratic coordinate monomial; its L2 norm is less
than $2\cdot10^{10}$. The coefficient changes are bounded by
4 eta and the amplitude change by 3 eta. These constants are absorbed
by $10^{12}\eta$.

Uniform convergence therefore gives a fixed h0>0 such that
$$
\sup_x\|K_h(x)-K_G\|_1\le10^{-4},\qquad0<h<h_0.
$$
Hence, with a0=1.0001 and b0=1.208,
$$
\|K_h(x)\|\le a_0,\qquad \|K_h(x)\|_1<b_0.
$$
For any finite m the trace ideal inequality and (3.3) imply
$$
|I_{m,N}(x)|\le\lambda^{-m/2}b_0a_0^{m-1}.
\tag{4.2}
$$
There are at most sixteen terms in (0.1). Moreover
$$
\frac{a_0}{\sqrt\lambda}<\frac{83}{200},\qquad
\frac{16b_0}{a_0}<20.
$$
The first inequality follows already from $\sqrt2>141/100$:
$(83/200)(241/100)=1.00015>1.0001$.
Summing (4.2) proves (0.2), uniformly in all m.

## 5. Original pair functional, with every cross term retained

Unitarity of the original matrices gives $|p_{m,N}|\le N$.
For every complex p,Q,
$$
\left|\,|p|^2-|p-Q|^2\right|\le2|p||Q|+|Q|^2.
$$
Substitute (0.2), multiply by the weights, and sum the two geometric
series. This proves (0.3). The estimate includes interference with
every other orbit and every other contribution to p; it assumes no
sign or independence for them.

For the actual test $w_{m,N}=|\widehat b_*(m/N)|^2\mathbf1_{m<2N}$,
$$
\Delta_{2,N}(b_*)=
\frac1{N^2}\sum_{1\le m<2N}w(m/N)
\left(|p_{m,N}-Q^{\rm full}_{m,N}|^2-\min(m,N)\right)+O(N^{-1}).
\tag{5.1}
$$
The limit of the sum on the right is still unknown. Equation (5.1) is
not introduced as an additional hypothesis and is not advertised as a
solution of the original task.

## 6. Relation to the preceding result

This supersedes only the principal-amplitude removal in §7 of the orbit
source. The preceding source remains frozen. The present estimate is for
whole exact terms, all times, and any uniformly bounded weight. It avoids
the all-time scalar modulus expansion and includes its transverse residual
automatically. Neither result estimates the exponentially large complement
of the protected set, and neither proves any H_diag limit.
