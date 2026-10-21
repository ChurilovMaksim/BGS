> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round8_2026_10_21/r8_return_uniform_shrinking_windows.md`. Embedded SHA256: `c7329595d2f77c5f14fe0e68dd28204740c7faf1d3527981f2a4a05929cc4d26`.
> [Thematic guide](../../topics/dephasing.md).

# Uniform shrinking windows and boundary resolvents for the original family

21 October 2026. Round 8, signed-return branch.

This note proves a new statement for the exact family
$U_N=\exp(i10^{-80}NA_N)M_N$, along **all odd dimensions**. It
extends the stationary-compression theorem from a single exact
eigenvalue to arbitrary shrinking arcs, uniformly over their centers.
It consequently controls coordinate-compressed resolvents throughout
every shrinking radial boundary layer, including $1-r\asymp N^{-1}$.
It does not establish the unweighted gap statistic or $H_{\rm diag}$.

No rate uniform in a growing physical time is assumed. The classical
input beyond the preceding round is proved by applying a published
ergodicity theorem to the product of the established classical map
with itself. The last two sections prove robustness under arbitrary
$o(1)$ unitary perturbations and test the result against the explicit
unipotent countermodel. These are necessary scope checks.

## 1. Exact inputs and notation

The input files, frozen before this argument, are:

| File in `research_round7_2026_10_21` | SHA-256 |
| --- | --- |
| `r7_return_all_fixed_powers_phase_separation.md` | `46982efaa581d322d4e82d5f5782ccf69f979a5a59adfb863dd40ef292205527` |
| `r7_return_uniform_stationary_dephasing.md` | `c2bf50a33a642b984afa7bfa83fdc0d28b8019c79d4f47121ab52adee5e53075` |
| `r7_return_schur_discriminant_identity.md` | `fc36418d779397802e481ad4383ee40460e19d27916f5b21b5da0f9ced9b9a33` |
| `root_unipotent_flat_clock.md` | `8f8e4cdbcd5c6576eb6bb9ce976d7a29ae4e77a310271576719ee8e39ad9d0bd` |

Only the last section uses the countermodel input. The new theorem
uses the following precise original-family facts, already proved in
the first two input files.

On the Hilbert space $\mathcal K_N=M_N(\mathbb C)$, use the
unnormalized Hilbert--Schmidt inner product, and put
$$
 W_N X=U_NXU_N^*,\qquad
 \iota_N v=\operatorname{diag}(v),\qquad
 e_N=N^{-1/2}(1,\ldots,1)^T,\qquad J_N=e_Ne_N^*.
 \tag{1.1}
$$
Thus $\iota_N$ is an isometry. Write
$P_{0,N}=I-J_N$, $\iota_{0,N}=\iota_NP_{0,N}$. Operators
compressed with $\iota_{0,N}$ are regarded as operators on
$\mathbb C^N$ that vanish on $e_N$. The spectral projection of
the unitary $W_N$ for a Borel set $A\subset\mathbb S^1$ is
denoted by $E_N(A)$.

For each fixed positive integer $n$, the input establishes
$$
 R_{n,N}:=\iota_N^*W_N^n\iota_N
       =|U_N^n|^{\circ2}
       =\left[N^{-1}k_n(x/N,y/N)\right]_{x,y}+o_{\rm op}(1),
 \tag{1.2}
$$
where $k_n$ is a smooth kernel on the ordinary two-torus. Each
$R_{n,N}$ is bistochastic, hence fixes $e_N$ along with its
adjoint. Its restriction to $e_N^\perp$ is represented on the
whole space by $R_{n,N}-J_N$.

Let $\mathcal H=L^2(\mathbb R/\mathbb Z)$ and let
$\mathcal I_N:\mathbb C^N\to\mathcal H$ be the centered discrete
Fourier isometry with range
$$
 \mathcal H_N=\operatorname{span}\{e^{2\pi ikq}:|k|\le(N-1)/2\}.
$$
Explicitly,
$$
 \mathcal I_Nv(q)=\sum_{|k|\le(N-1)/2}
  \left(N^{-1/2}\sum_x v_xe^{-2\pi ikx/N}\right)e^{2\pi ikq}.
 \tag{1.3}
$$
Then $\mathcal I_Ne_N=1$,
$\mathcal I_NJ_N\mathcal I_N^*=J$, where $J$ projects onto
constants, and $\mathcal I_N\mathcal I_N^*=P_{\mathcal H_N}\to I$
strongly. Section 3 of the stationary-compression input proves from
(1.2) that
$$
 \mathcal I_N(R_{n,N}-J_N)\mathcal I_N^*
       \longrightarrow\mathcal R_n-J
       \quad\hbox{in operator norm for every fixed }n\ge1,
 \tag{1.4}
$$
where $\mathcal R_n$ is compact. To recall why sampling causes no
extra hypothesis: a fixed trigonometric-polynomial kernel has exact
discrete/continuous equality for sufficiently large $N$; uniform
kernel approximation gives operator errors at most the uniform
error on both sides. Thus (1.4) uses no growing-time assertion.

The exact classical interpretation proved there is
$$
 \mathcal R_n=\iota^*\mathcal C^n\iota,
 \qquad (\iota g)(q,p)=g(q),\qquad
 (\mathcal C h)(z)=h(F_+^{-1}z).
 \tag{1.5}
$$
Here $F_+=\kappa_\tau\mathsf S$,
$\mathsf S=\left(\begin{smallmatrix}3&4\\2&3\end{smallmatrix}\right)$,
$\kappa_t=C\Phi_{-t}C$, $C(q,p)=(q,-p)$. The flow $\Phi_t$
has vector field $(a_p,-a_q)/(2\pi)$, with the ordinary-half
symbol
$$
 a(q,p)=\cos(14\pi q)+\frac{r(q)}{10}
  +\frac{r(q)\sin(2\pi q)}{100}-\frac1{10}
  +\frac{r(q+1/2)\cos(2\pi p-\alpha_0)}{100}.
 \tag{1.6}
$$
The momentum-dependent term in (1.6) has the shifted $r$, as
required by the modular half convention. Section 2 of the
stationary-compression input proves analyticity, area preservation,
and a continuous uniformly hyperbolic splitting on the connected
compact torus for this exact $F_+$, with the specified fixed
$\tau=10^{-80}$.

## 2. Main theorem

For $0\le\delta<\pi$, let
$$
 I(\theta,\delta)=
 \{e^{it}:\operatorname{dist}(t-\theta,2\pi\mathbb Z)\le\delta\}.
 \tag{2.1}
$$
For every positive sequence $\delta_N\to0$, define
$$
 q_N(\delta_N)=
 \sup_{\theta\in\mathbb R}
 \left\|\iota_{0,N}^*E_N(I(\theta,\delta_N))\iota_{0,N}\right\|_{\rm op}.
 \tag{2.2}
$$

**Theorem 1 (uniform compressed shrinking windows).** For the exact
original family, along all odd $N$,
$$
 \boxed{q_N(\delta_N)\longrightarrow0
       \quad\hbox{for every sequence }\delta_N\to0.}
 \tag{2.3}
$$
There is no lower bound on the window width: it may be $N^{-1}$,
$e^{-N}$, or any other positive sequence tending to zero. There is
no restriction on the center, which may vary arbitrarily with $N$.

For completeness, the corresponding full coordinate compression is
exactly
$$
 \iota_N^*E_N(I)\iota_N
 =\mathbf1_{\{1\in I\}}J_N+
   \iota_{0,N}^*E_N(I)\iota_{0,N}.
 \tag{2.4}
$$
Indeed $u_N=\mathbf I_N/\sqrt N=\iota_Ne_N$ is a unit stationary
vector for $W_N$; it reduces every spectral projection. Thus the
constant contribution has been removed exactly, including when
the arc has an eigenvalue at an endpoint. No simplicity assumption
is made about either $U_N$ or its eigenvalue ratios.

**Theorem 2 (uniform compressed boundary resolvent).** For every
sequence $0<r_N<1$ with $r_N\to1$,
$$
 \boxed{
 (1-r_N)\sup_{t\in\mathbb R}
 \left\|\iota_{0,N}^*
      (I-r_Ne^{it}W_N)^{-1}\iota_{0,N}\right\|_{\rm op}
       \longrightarrow0.}
 \tag{2.5}
$$
In particular, for each fixed $s>0$,
$$
 \frac1N\sup_t
 \left\|\iota_{0,N}^*
      (I-e^{-s/N}e^{it}W_N)^{-1}\iota_{0,N}\right\|_{\rm op}
       \longrightarrow0.
 \tag{2.6}
$$
The trivial full-space estimate at this radius is $O_s(N)$, so
(2.6) is a qualitative improvement for the specified compression.

## 3. Product ergodicity and uniform modulated classical averages

The only new external input is the following published theorem.

Zhihong Xia, *Hyperbolic invariant sets with positive measures*,
Discrete and Continuous Dynamical Systems **15** (2006), 811--818,
[DOI 10.3934/dcds.2006.15.811](https://doi.org/10.3934/dcds.2006.15.811).
Theorem 4.2 of the
[author's version 2](https://arxiv.org/pdf/math/0503437v2), pages 7--8,
asserts ergodicity of a $C^{1+\alpha}$, $\alpha>0$, smooth-volume
preserving Anosov diffeomorphism on a compact manifold; connectedness
is a standing assumption at the start of the paper. The theorem
and standing assumption were personally reopened on 21 October 2026.
No rate of correlation decay is taken from this theorem.

Apply this result to
$$
 G=F_+\times F_+:\mathbb T^4\longrightarrow\mathbb T^4.
 \tag{3.1}
$$
All hypotheses can be checked from the established facts about
$F_+$. The product torus is compact and connected; $G$ is analytic
and preserves normalized product area. If $E^s,E^u$ are the
continuous invariant bundles for $F_+$, the bundles
$$
 E^s_{(x,y)}=E_x^s\oplus E_y^s,
 \qquad E^u_{(x,y)}=E_x^u\oplus E_y^u
$$
are continuous, invariant, complementary bundles for $G$. In the
product maximum norm, the contraction and expansion estimates are
the same as for $F_+$; equivalence of smooth norms gives the usual
Anosov estimates. Hence the published theorem applies and $G$ is
ergodic. This argument supplies the product ergodicity needed below;
it is not an inference from single-system ergodicity alone.

Here is the Hilbert-space consequence with its proof. If $g$ is
any mean-zero element of $L^2(\mathbb T^2)$, put
$$
 H(x,y)=g(x)\overline{g(y)}.
$$
It belongs to $L^2(\mathbb T^4)$, has mean zero, and satisfies
$$
 \langle H,(\mathcal C\otimes\mathcal C)^nH\rangle
       =|\langle g,\mathcal C^ng\rangle|^2.
 \tag{3.2}
$$
Complex conjugation commutes with the Koopman operator, which proves
this identity directly by the product integral.

For any unitary $D$,
$\overline{\operatorname{ran}(I-D)}=\ker(I-D)^\perp$.
The averages $T^{-1}\sum_{n=0}^{T-1}D^n$ send
$(I-D)v$ to $(v-D^Tv)/T$, which tends to zero; their norms
are at most one, so this convergence extends to the closure of the
range. On the fixed space they act as the identity. Since
ergodicity of $G$ makes the fixed vectors of its Koopman operator
the constants, this proves
$$
 \frac1T\sum_{n=0}^{T-1}
        |\langle g,\mathcal C^ng\rangle|^2\longrightarrow0
       \quad\hbox{for every such }g.
 \tag{3.3}
$$
The assertion that the fixed vectors are constants follows by
applying ergodicity to level sets of the real and imaginary parts
of an invariant measurable function.

Define the modulated averages
$$
 A_T(\theta)=\frac1T\sum_{n=0}^{T-1}e^{-in\theta}\mathcal C^n.
$$
Expanding the squared norm, for every $\theta$, gives
$$
 \|A_T(\theta)g\|^2
 \le\frac{\|g\|^2}{T}
       +\frac2T\sum_{n=1}^{T-1}|\langle g,\mathcal C^ng\rangle|.
 \tag{3.4}
$$
The second term tends to zero by Cauchy--Schwarz and (3.3).
Consequently
$$
 \sup_{\theta\in\mathbb R}\|A_T(\theta)g\|^2\longrightarrow0
       \quad(T\to\infty)
 \tag{3.5}
$$
for every fixed mean-zero $g$. This uses Cesàro decay of squared
correlations; pointwise mixing or a mixing rate is unnecessary.

When $g=\iota v$ and $v$ lies in a fixed finite-dimensional
mean-zero Fourier subspace of $\mathcal H$, (3.5) is also uniform
over its unit sphere. To see this without any compactness exchange,
choose an orthonormal basis $v_1,\ldots,v_d$. The positive
compressed operator $A_T(\theta)^*A_T(\theta)$ has norm at most
the sum of its diagonal quadratic forms
$\sum_j\|A_T(\theta)\iota v_j\|^2$. Taking the supremum over
$\theta$ and using (3.5) for the finitely many vectors proves
the claim.

## 4. Fejér domination for shrinking arcs

For fixed $T\ge1$, let
$$
 a_T(u)=\frac1T\sum_{n=0}^{T-1}e^{inu},
 \qquad g_T(u)=|a_T(u)|^2.
$$
If $|u|\le\delta$, then
$$
 |a_T(u)-1|
 \le\frac1T\sum_{n=0}^{T-1}n|u|
 =\frac{T-1}{2}|u|.
$$
For fixed $T$ and $\delta_N\to0$, it follows that
$$
 c_{T,N}:=\min_{|u|\le\delta_N}g_T(u)\longrightarrow1,
 \qquad c_{T,N}>0\quad\hbox{eventually}.
 \tag{4.1}
$$
The finite-dimensional spectral theorem gives, uniformly in the
center $\theta$,
$$
 E_N(I(\theta,\delta_N))
 \le c_{T,N}^{-1}
 \left|\frac1T\sum_{n=0}^{T-1}e^{-in\theta}W_N^n\right|^2.
 \tag{4.2}
$$
The right-hand multiplier is nonnegative everywhere and at least
one after multiplication by $c_{T,N}^{-1}$ throughout the arc.

Let
$$
 Q_N(\theta)=
 \iota_{0,N}^*E_N(I(\theta,\delta_N))\iota_{0,N}\ge0.
$$
After compression, the right side of (4.2), before its scalar
factor, is the positive operator
$$
 G_{T,N}(\theta)=\frac1T(I-J_N)
 +\frac2T\sum_{n=1}^{T-1}(1-n/T)
   \operatorname{Re}\big(e^{-in\theta}(R_{n,N}-J_N)\big).
 \tag{4.3}
$$
Here $\operatorname{Re}D=(D+D^*)/2$. The expansion follows by
collecting the $T-n$ terms with power difference $n$ in the
squared average. The subtraction of $J_N$ is valid for every
$\theta$, because the compression uses $P_{0,N}$ on both sides,
and $P_{0,N}R_{n,N}P_{0,N}=R_{n,N}-J_N$.

For fixed $T$, set
$$
 K_T(\theta)=\frac2T\sum_{n=1}^{T-1}(1-n/T)
    \operatorname{Re}\big(e^{-in\theta}(\mathcal R_n-J)\big).
 \tag{4.4}
$$
It is a finite linear combination of compact operators. By (1.4),
the corresponding embedded finite-dimensional sums converge to
$K_T(\theta)$ in operator norm **uniformly in $\theta$**.
Indeed their difference is bounded by a finite sum of the individual
norm errors with coefficients of modulus at most $2/T$.

The classical version of (4.3) on mean-zero functions is
$$
 G_T(\theta)=\frac1T(I-J)+K_T(\theta)
   =P_0\iota^*A_T(\theta)^*A_T(\theta)\iota P_0\ge0,
 \qquad P_0=I-J.
 \tag{4.5}
$$

## 5. Low and high frequencies: proof of Theorem 1

Write $\widehat Q_N(\theta)=\mathcal I_NQ_N(\theta)\mathcal I_N^*$.
Let $E_M$ project onto
$\operatorname{span}\{e^{2\pi ikq}:|k|\le M\}$ in $\mathcal H$.
The constant vector has zero quadratic form in
$\widehat Q_N(\theta)$. For fixed $M,T$, equations
(4.1)--(4.5), with $N\to\infty$ first, imply
$$
 \limsup_N\sup_\theta
  \|E_M\widehat Q_N(\theta)E_M\|
 \le\sup_\theta\|E_MG_T(\theta)E_M\|.
 \tag{5.1}
$$
For sufficiently large $N$, $E_M\le P_{\mathcal H_N}$, so the
identity part of (4.3) agrees exactly with that of (4.5) on this
subspace. Section 3 proves that the right side of (5.1) tends to zero
as $T\to\infty$. Therefore
$$
 \sup_\theta\|E_M\widehat Q_N(\theta)E_M\|
     \longrightarrow0
     \quad\hbox{for each fixed }M.
 \tag{5.2}
$$

For the remaining frequencies keep $T$ fixed. The embedded
identity term in (4.3) is $T^{-1}(P_{\mathcal H_N}-J)\le T^{-1}I$.
Taking quadratic forms in (4.2) on $E_M^\perp$, and using uniform
norm convergence of the compact sums, gives
$$
 \limsup_N\sup_\theta
   \|(I-E_M)\widehat Q_N(\theta)(I-E_M)\|
 \le\frac1T+
       \sup_\theta\|(I-E_M)K_T(\theta)(I-E_M)\|.
 \tag{5.3}
$$
For this fixed $T$, the last supremum tends to zero as
$M\to\infty$. In fact it is bounded by a finite weighted sum of
the compact tails of $\mathcal R_n-J$ and their adjoints.
For each compact operator these tails tend to zero: approximate it
in norm by a finite-rank operator and use strong convergence of
$E_M$ on the finite-dimensional ranges of that operator and its
adjoint.

No cross block is lost in combining (5.2) and (5.3). For any positive
operator $Q$ and any orthogonal projection $E$,
$$
 \|Q\|\le\|EQE\|+\|(I-E)Q(I-E)\|.
 \tag{5.4}
$$
Indeed if the two diagonal-block norms are $a,b$, positivity
bounds the quadratic-form cross term for $v=x+y$,
$x=Ev$, $y=(I-E)v$, by
$2\sqrt{ab}\|x\|\|y\|$. The full quadratic form is at most
$(\sqrt a\|x\|+\sqrt b\|y\|)^2\le(a+b)\|v\|^2$.

Taking the supremum over $\theta$ in (5.4), then using (5.2) and
(5.3), yields
$$
 \limsup_N q_N(\delta_N)
 \le\frac1T+
      \sup_\theta\|(I-E_M)K_T(\theta)(I-E_M)\|.
 \tag{5.5}
$$
Let $M\to\infty$ with $T$ fixed, and then $T\to\infty$.
This proves Theorem 1.

All orders of limits in this proof are explicit. The low-frequency
claim (5.2) was established separately for each fixed $M$; one
does not need to use its averaging time in the high-frequency
estimate. Every $N$-limit before (5.5) contains only finitely many
fixed physical times. The sequence $\delta_N$ appears solely in
the fixed-$T$ scalar limit $c_{T,N}\to1$.

## 6. Proof of Theorem 2 and the exact Schur consequence

Let $\epsilon_N=\sqrt{1-r_N}$, and split the spectral integral
for $(1-r_N)(I-r_Ne^{it}W_N)^{-1}$ into the arc
$I(-t,\epsilon_N)$ and its complement. The minus sign in this
center is required by the denominator $1-r_Ne^{it}\lambda$.

On the arc, the multiplier
$(1-r_N)/(1-r_Ne^{it}\lambda)$ has modulus at most one. If
$E=E_N(I(-t,\epsilon_N))$, factorizing the compression as
$$
 (E\iota_{0,N})^*
   \left.\frac{1-r_N}{I-r_Ne^{it}W_N}\right|_{\operatorname{ran}E}
 (E\iota_{0,N})
$$
shows that its norm is at most
$\|\iota_{0,N}^*E\iota_{0,N}\|\le q_N(\epsilon_N)$.
This factorization, rather than an ordering of the complex
resolvent, is the needed estimate.

On the complement choose the argument $u\in[-\pi,\pi]$ of
$e^{it}\lambda$. For large $N$, $r_N\ge1/2$, and
$$
 |1-r_Ne^{iu}|^2
 =(1-r_N)^2+4r_N\sin^2(u/2)
 \ge\frac{2u^2}{\pi^2}.
 \tag{6.1}
$$
Here $\sin(|u|/2)\ge|u|/\pi$. Thus the norm of the far
compression is at most
$\pi(1-r_N)/(\sqrt2\epsilon_N)$. Together,
$$
 (1-r_N)\sup_t
 \|\iota_{0,N}^*(I-r_Ne^{it}W_N)^{-1}\iota_{0,N}\|
 \le q_N(\sqrt{1-r_N})+
      \frac\pi{\sqrt2}\sqrt{1-r_N}\longrightarrow0.
 \tag{6.2}
$$
This proves (2.5). Since $N(1-e^{-s/N})\to s>0$, (2.6)
follows immediately.

To express exactly what this says about signed returns, split
$\mathcal K_N=\operatorname{ran}\iota_N\oplus
\operatorname{ran}\iota_N^\perp$ and write
$$
 W_N=\begin{pmatrix}P_N&D_N\\C_N&S_N\end{pmatrix},\qquad
 \mathfrak F_N(z)=zP_N+z^2D_N(I-zS_N)^{-1}C_N.
 \tag{6.3}
$$
Since $\|S_N\|\le1$, the inverse in (6.3) exists for
$|z|<1$. Ordinary block elimination of $I-zW_N$ then gives
$$
 \iota_N^*(I-zW_N)^{-1}\iota_N
       =(I-\mathfrak F_N(z))^{-1}.
 \tag{6.4}
$$
The Schur complement is invertible because both $I-zW_N$ and
$I-zS_N$ are invertible. The normalized identity reduces
$W_N$, so $P_Ne_N=e_N$, $C_Ne_N=0$,
$D_N^*e_N=0$, and $e_N^\perp$ reduces
$\mathfrak F_N(z)$. In particular,
$\mathfrak F_N(z)e_N=ze_N$.

It follows from (2.5) and (6.4) that
$$
 (1-r_N)\sup_t
 \left\|\left.(I-\mathfrak F_N(r_Ne^{it}))^{-1}
                         \right|_{e_N^\perp}\right\|\longrightarrow0.
 \tag{6.5}
$$
An equivalent singular-value statement at the Heisenberg radial
scale is
$$
 N\inf_t\sigma_{\min}
  \left(\left.(I-\mathfrak F_N(e^{-s/N}e^{it}))
                                  \right|_{e_N^\perp}\right)
       \longrightarrow+\infty.
 \tag{6.6}
$$
The equivalence follows from $\sigma_{\min}(A)=\|A^{-1}\|^{-1}$
for an invertible finite-dimensional operator. Equation (6.6)
concerns the Schur complement at a point inside the disk. It does
not assert an eigenvalue gap for the nonnormal matrix $S_N$.

## 7. Robustness under arbitrary vanishing operator perturbations

**Corollary 3.** Let $V_N$ be any deterministic unitaries of the
same dimensions such that
$\|V_N-U_N\|_{\rm op}\to0$ along all odd $N$. Then
Theorems 1 and 2, and their Schur consequences, hold with $V_N$
throughout. There is no relation required between the perturbation
size and either the shrinking arc width or the radial distance to
the unit circle.

For proof, powers telescope to give
$$
 \|V_N^n-U_N^n\|_{\rm op}\le n\|V_N-U_N\|_{\rm op}.
$$
For two unitaries $A,B$, the identity
$$
 AXA^*-BXB^*=(A-B)XA^*+BX(A^*-B^*)
$$
gives
$\|\operatorname{Ad}A-\operatorname{Ad}B\|_{{\rm HS}\to{\rm HS}}
\le2\|A-B\|_{\rm op}$. Compression by the same isometry
$\iota_N$ therefore gives
$$
 \big\||V_N^n|^{\circ2}-|U_N^n|^{\circ2}\big\|_{\rm op}
 \le2n\|V_N-U_N\|_{\rm op}\longrightarrow0
       \quad\hbox{for each fixed }n.
 \tag{7.1}
$$
Thus (1.4), with its same compact classical limits, holds for
$V_N$. The proofs in Sections 3--6 use only these limits and
unitarity, so they apply unchanged. In particular, no perturbation
bound for individual microscopic spectral projections is being
assumed.

This robustness is a mathematical limitation on what the theorem
can imply. Perturbations that vanish in operator norm can move
eigenphases through many mean spacings. The corollary therefore does
not supply a microscopic stability theorem for $H_{\rm diag}$.

## 8. Direct adversarial test against the unipotent countermodel

Let $N=p^2$, with $p>3$ prime, and take the explicit matrix
$C_p$ in the frozen countermodel input. That file proves
$$
 C_p^p=I,\qquad |C_p^n|^{\circ2}=J_N\quad(1\le n<p),
 \qquad
 |\operatorname{Tr}C_p^n|^2=
 \begin{cases}N^2,&p\mid n,\\p,&p\nmid n.\end{cases}
 \tag{8.1}
$$
Write $W_0=\operatorname{Ad}C_p$. Its spectral projector for
$e^{2\pi ia/p}$ is
$$
 E_a=\frac1p\sum_{n=0}^{p-1}e^{-2\pi ian/p}W_0^n.
$$
Direct compression of this exact finite Fourier sum gives
$$
 \iota_N^*E_a\iota_N
    =\frac1p(I-J_N)+\mathbf1_{\{a=0\}}J_N,
 \qquad
 \iota_{0,N}^*E_a\iota_{0,N}=\frac1p(I-J_N).
 \tag{8.2}
$$
Every arc of angular half-width $\delta<\pi$ contains at most
$1+p\delta/\pi$ points of this $p$-point grid. It follows
without an asymptotic theorem that
$$
 \sup_\theta\|\iota_{0,N}^*E_{W_0}(I(\theta,\delta))\iota_{0,N}\|
       \le\frac1p+\frac\delta\pi.
 \tag{8.3}
$$
Thus this countermodel also has uniform shrinking-window control
for every $\delta_N\to0$.

Its compressed resolvent is equally explicit. The compressed
powers on $e_N^\perp$ vanish unless $p\mid n$, in which
case they equal the identity there. Consequently
$$
 \iota_{0,N}^*(I-zW_0)^{-1}\iota_{0,N}
          =\frac{I-J_N}{1-z^p},\qquad |z|<1.
 \tag{8.4}
$$
For any $r_N\to1$,
$$
 (1-r_N)\sup_t
 \|\iota_{0,N}^*(I-r_Ne^{it}W_0)^{-1}\iota_{0,N}\|
 =\frac1{1+r_N+\cdots+r_N^{p-1}}\longrightarrow0.
 \tag{8.5}
$$
For the last limit, bound the denominator below by its first fixed
$L$ terms for large $p$, let $N\to\infty$, and then let
$L\to\infty$. At $r_N=e^{-s/N}$, the unscaled supremum in
(8.5) is asymptotic to $p/s=\sqrt N/s$, still $o(N)$.

Nevertheless, with $r=e^{-2s/N}$, (8.1) gives the exact pair
sum
$$
 \frac1{N^2}\sum_{n\ge1}r^n|\operatorname{Tr}C_p^n|^2
 =\frac{r^p}{1-r^p}
  +p^{-3}\left(\frac r{1-r}-\frac{r^p}{1-r^p}\right)
 \sim\frac p{2s}\longrightarrow+\infty.
 \tag{8.6}
$$
The same input file proves a diverging defect for every nonzero
admissible compact-Fourier test $b$. Thus the new compressed
theorems pass this adversarial check: they are compatible with a
strong failure of the desired pair statistic in another family.
They must not be called a sufficient criterion for the original
problem.

## 9. Exact remaining obstruction for the original family

Choose any orthonormal eigenbasis $\psi_j$ of $U_N$, with
eigenvalues $\lambda_j$. The rank-one matrices
$\psi_j\psi_k^*$ form an orthonormal basis for $\mathcal K_N$
and have $W_N$-eigenvalues $\lambda_j\overline{\lambda_k}$.
Their squared coordinate-diagonal projection norms are
$$
 C_{jk}=\sum_x|\psi_j(x)|^2|\psi_k(x)|^2.
 \tag{9.1}
$$
Thus the trace of a full coordinate-compressed spectral window is
$$
 \operatorname{Tr}(\iota_N^*E_N(I)\iota_N)
 =\sum_{j,k:\lambda_j\overline{\lambda_k}\in I} C_{jk}.
 \tag{9.2}
$$
This formula remains true with multiplicities and for arbitrary
bases inside degenerate eigenspaces. In contrast, the unweighted
gap count is $\operatorname{Tr}E_N(I)$, which has weight one
for each ordered pair. Theorem 1 controls the operator norm of the
compression after its exact scalar component has been removed. It
proves neither the first-order asymptotic of (9.2) at width
$1/N$, nor $NC_{jk}\to1$, nor an estimate sufficient to
replace its weights by one in the required signed functional.

The first already isolated unresolved original-family assertion
can still be taken at order two. Put
$$
 \phi(\xi)=e^{-1/(1-\xi^2)}\mathbf1_{\{|\xi|<1\}},\quad
 I_\phi=\int\phi,\quad u=\mathcal F^{-1}\phi,\quad
 b_*(x)=\frac{|u(x)|^2}{2I_\phi^2},\quad
 w=|\widehat b_*|^2.
 \tag{9.3}
$$
Then $b_*$ is a nonzero admissible test,
$\operatorname{supp}w\subset[-2,2]$, and the required estimate is
$$
 \boxed{
 \frac1{N^2}\sum_{1\le m<2N}w(m/N)
       \bigl(|\operatorname{Tr}U_N^m|^2-\min(m,N)\bigr)
        \stackrel{?}{\longrightarrow}0.}
 \tag{9.4}
$$
The modulus in the desired assertion is applied after this entire
weighted sum. Nothing in (2.3), (2.5), or (6.5) evaluates (9.4).
The all-orders signed hierarchy remains open after this note.

The actual advance is the original-family theorem (2.3), its
uniform boundary consequence (2.5), and their exact robustness
statement. No claim of a completed proof or of a counterexample for
the original family is made.
