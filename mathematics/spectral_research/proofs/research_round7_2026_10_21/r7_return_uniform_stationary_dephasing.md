> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round7_2026_10_21/r7_return_uniform_stationary_dephasing.md`. Embedded SHA256: `c2bf50a33a642b984afa7bfa83fdc0d28b8019c79d4f47121ab52adee5e53075`.
> [Thematic guide](../../topics/dephasing.md).

# Uniform contraction of stationary dephasing on coordinate diagonals

21 October 2026. This note proves an additional theorem for the **exact original**
family $U_N=e^{i10^{-80}NA_N}M_N$, along all odd $N$. It uses the newly
proved compact classical limits of every fixed physical probability operator.
The time in that input theorem always remains fixed before $N$ tends to
infinity. No error estimate uniform in a growing time is used.

The main result is an operator norm statement about all diagonal
observables, including observables that vary with $N$. It does not prove
the required spectral statistic $H_{\rm diag}$.

## 1. Statements and the exact inputs

Give the space $\mathcal K_N=\mathbb C^{N\times N}$ its unnormalized
Hilbert--Schmidt inner product. Let
$$
 \mathcal W_NX=U_NXU_N^*,\qquad
 \Pi_NX=\operatorname{diag}(X_{00},\ldots,X_{N-1,N-1}),
 \qquad O_N=I-\Pi_N.
 \tag{1.1}
$$
Identify the range of $\Pi_N$ with $\mathbb C^N$, by the diagonal
entries, with its usual Euclidean norm. Let $\mathcal E_N$ be the
orthogonal projection onto the full commutant
$\ker(\mathcal W_N-I)$, and set
$$
 L_N=\Pi_N\mathcal E_N\Pi_N\big|_{\operatorname{ran}\Pi_N},
 \quad
 e_N=N^{-1/2}(1,\ldots,1)^T,\quad
 J_N=e_Ne_N^*,\quad
 Q_N=L_N-J_N.
 \tag{1.2}
$$
In (1.1), the identity $I$ denotes the identity operator on the
matrix Hilbert space; in the definition of a traceless matrix below,
the identity matrix itself will be denoted by $\mathbf I_N$.

**Theorem 1.** For the exact original family, along all odd dimensions,
$$
 q_N:=\|Q_N\|_{\rm op}\longrightarrow0.
 \tag{1.3}
$$
Moreover $Q_N$ is positive semidefinite. In particular, for every
orthonormal eigenbasis of $U_N$, put
$$
 B_N(x,j)=|\psi_{j,N}(x)|^2.
$$
Then, uniformly over all choices of an orthonormal eigenbasis, including
choices inside degenerate eigenspaces,
$$
 0\le B_NB_N^*-J_N\le Q_N,\qquad
 \|B_NB_N^*-J_N\|_{\rm op}\longrightarrow0.
 \tag{1.4}
$$
Equivalently, the largest possible squared Hilbert--Schmidt norm of the
stationary component of a coordinate diagonal traceless matrix of
Hilbert--Schmidt norm one tends to zero.

**Theorem 2.** Let $d_N=\dim\ker(\mathcal W_N-I)$, so $d_N\ge N$,
and let $S_N=O_N\mathcal W_NO_N$ act on $\operatorname{ran}O_N$.
For all sufficiently large odd $N$, there is a subspace
$\mathcal V_N\subset\operatorname{ran}O_N$ of dimension $d_N-1$
such that
$$
 \|(I-S_N)Y\|_{\rm HS}
 \le \sqrt{\frac{q_N}{1-q_N}}\ \|Y\|_{\rm HS}
 \quad(Y\in\mathcal V_N).
 \tag{1.5}
$$
Thus at least $N-1$ singular values of $I-S_N$ tend to zero,
with the upper bound displayed in (1.5). This is a singular value
statement and does not assert eigenvalues of $S_N$ close to one.

The extra finite-dimensional conclusion established for the original
family when $7\nmid N$, namely simple spectrum and invertibility of
$B_N$, gives a further consequence. With the first-return convention
$$
 \mathcal W_N=
 \begin{pmatrix}P_N&C_N^{\rm out}\\ C_N^{\rm in}&S_N\end{pmatrix},
 \qquad
 F_{1,N}=P_N,\qquad
 F_{r,N}=C_N^{\rm out}S_N^{r-2}C_N^{\rm in}\quad(r\ge2),
 \tag{1.6}
$$
one has the absolutely convergent signed identities
$$
 \sum_{r\ge1}F_{r,N}=I_N,\qquad
 \sum_{r\ge1}rF_{r,N}=(B_NB_N^*)^{-1}.
 \tag{1.7}
$$
Here $I_N$ in (1.7) is the identity on the $N$-dimensional
coordinate diagonal space. Along odd $N$ with $7\nmid N$,
$$
 \lambda_{\min}\left(
   \left.\sum_{r\ge1}rF_{r,N}\right|_{e_N^\perp}\right)
 \longrightarrow+\infty.
 \tag{1.8}
$$
This concerns a signed matrix sum. It is not a claim about a probability
mean or the scalar sum $\sum r\|F_{r,N}\|_{\rm HS}^2$.

The exact internal input used for Theorems 1 and 2 is the theorem and
Section 8 of
[the all-fixed-powers proof](r7_return_all_fixed_powers_phase_separation.md),
SHA256
46982efaa581d322d4e82d5f5782ccf69f979a5a59adfb863dd40ef292205527.
Specifically, for each fixed positive $n$,
$$
 R_{n,N}:=|U_N^n|^{\circ2}
 =
 \left[N^{-1}k_n(x/N,y/N)\right]_{x,y=0}^{N-1}
 +o_{\rm op}(1),
 \tag{1.9}
$$
where $k_n$ is a smooth kernel on the ordinary two-torus. In addition,
$k_n(q,s)$ is precisely the position density obtained by applying the
classical map $F_+^n$ to uniform initial momentum at initial position
$s$. This identification, rather than just the two unit marginals, is
used below.

For (1.7)--(1.8), the extra input is the simple-spectrum and intensity
theorem in
[the prescribed-phase intensity proof](root_original_intensity_at_prescribed_phase.md),
SHA256
deea7755070222fdfca37d5c8f2721dc82b62afa34d56b18df614756308b5c63.
Its restriction $7\nmid N$ is retained. Neither (1.3) nor (1.5) uses
that restriction.

The only external classical theorem used is Xia's ergodicity theorem,
specified with its hypotheses in Section 2. The mean ergodic step used
later is proved directly in Section 4.

## 2. Classical ergodicity with the hypotheses checked

Let
$$
 \mathsf S=\begin{pmatrix}3&4\\2&3\end{pmatrix},\quad
 C(q,p)=(q,-p),\quad
 F_+=\kappa_\tau\mathsf S,\quad
 \kappa_u=C\Phi_{-u}C,\quad \tau=10^{-80},
 \tag{2.1}
$$
where $\Phi_u$ is the Hamiltonian flow of
$$
 X=\frac1{2\pi}(a_p,-a_q),
 \quad
 a(q,p)=\cos(14\pi q)+\frac{r(q)}{10}
       +\frac{r(q)\sin(2\pi q)}{100}-\frac1{10}
       +\frac{r(q+1/2)\cos(2\pi p-\alpha_0)}{100}.
 \tag{2.2}
$$
This is the ordinary-half Weyl symbol of the exact modular matrix in
the question, as established in the all-fixed-powers input. The finite
Fourier support lies in $|k|+|l|\le9$, and the sum of absolute
Fourier coefficients is less than two. Consequently
$$
 \|DX\|_{\infty\to\infty}
 \le 2\pi\cdot 9^2\cdot2<2000.
 \tag{2.3}
$$
The same derivative bound applies after reversing momentum or the
sign of the vector field. The variational equation and integration give
$$
 \|D\kappa_\tau-I\|_{\infty\to\infty}
 \le e^{2000\tau}-1\le4000\tau.
 \tag{2.4}
$$
For clarity, this last elementary estimate follows by the integral
equation $D\kappa_u-I=\int_0^u DX_\kappa(\kappa_v)D\kappa_v\,dv$,
the bound $\|D\kappa_v\|\le e^{2000v}$, and
$e^t-1\le2t$ for $0\le t\le1$.

The vector field is analytic, periodic, and bounded, so its real flow is
a globally defined analytic diffeomorphism for each real time. Its
divergence is zero, since $a_{pq}=a_{qp}$. The variational equation
therefore makes the Jacobian determinant of $\Phi_u$ equal to one.
Both conjugation by $C$ and multiplication by $\mathsf S$ preserve
area. Thus $F_+$ is an analytic area-preserving diffeomorphism of the
compact connected torus.

Here is an explicit verification of uniform hyperbolicity. Put
$$
 \lambda=3+2\sqrt2,\qquad
 Z=\begin{pmatrix}\sqrt2&\sqrt2\\1&-1\end{pmatrix}.
$$
Then $Z^{-1}\mathsf SZ=\operatorname{diag}(\lambda,\lambda^{-1})$,
$\|Z\|_{\infty\to\infty}<3$, and
$\|Z^{-1}\|_{\infty\to\infty}<1$. Equations (2.4) and
$\|\mathsf S\|_{\infty\to\infty}=7$ imply
$$
 Z^{-1}DF_+(z)Z
   =\operatorname{diag}(\lambda,\lambda^{-1})+E(z),
 \qquad \|E(z)\|_{\infty\to\infty}<84000\tau<10^{-3}.
 \tag{2.5}
$$
The determinant is one. The inverse matrix consequently differs from
$\operatorname{diag}(\lambda^{-1},\lambda)$ in maximum row-sum norm
by less than $2\cdot10^{-3}$: write the inverse as
$\left(\begin{smallmatrix}d&-b\\-c&a\end{smallmatrix}\right)$.

In these fixed coordinates, consider the two cones
$$
 \mathcal C^u=\{(u,v):|v|\le|u|\},\qquad
 \mathcal C^s=\{(u,v):|u|\le|v|\}.
$$
A matrix in (2.5) maps $\mathcal C^u$ into
$|v|\le|u|/4$ and expands the maximum norm there by a factor
greater than five. Indeed the outgoing first coordinate has magnitude
at least $(\lambda-10^{-3})|u|$, whereas the second has magnitude
at most $(\lambda^{-1}+10^{-3})|u|$. The same argument for the
inverse maps $\mathcal C^s$ into $|u|\le|v|/4$ and expands it by
more than five.

These estimates also construct the required invariant continuous line
bundles. For a determinant-one matrix
$\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)$, its
map on slopes $\eta=v/u$ is
$(c+d\eta)/(a+b\eta)$, whose derivative is
$(a+b\eta)^{-2}$. On $|\eta|\le1$, (2.5) bounds this derivative
by $1/25$. Composing along the backward orbit gives nested images
of the unstable slope interval with diameters tending uniformly to
zero. Their unique intersection defines the unstable line at each
point. The finite compositions are continuous, so the uniform limit
is continuous, and shifting the compositions proves invariance. The
same construction for the inverse gives the stable line. The two
lines remain in the disjoint narrower cones just displayed. Expansion
by five in the indicated time direction, and equivalence of the fixed
coordinate norms, prove the Anosov inequalities on the entire torus.

The precise external input is:

Zhihong Xia, *Hyperbolic invariant sets with positive measures*,
Discrete and Continuous Dynamical Systems **15** (2006), 811--818,
[DOI 10.3934/dcds.2006.15.811](https://doi.org/10.3934/dcds.2006.15.811).
Theorem 4.2 of the
[author version](https://arxiv.org/pdf/math/0503437), pages 7--8,
states ergodicity for a $C^{1+\alpha}$, $\alpha>0$,
volume-preserving Anosov diffeomorphism on a compact connected
manifold. Connectedness is a standing assumption in the paper's
introduction. The publication data and the theorem were reopened
and checked on 21 October 2026.

All hypotheses have just been verified for $F_+$, with normalized
area as the smooth volume. Therefore $F_+$ is ergodic for that area.
No mixing rate, or even a mixing assertion, is used below.

## 3. The discrete probability operators have compact limits

Let $\mathcal H=L^2(\mathbb R/\mathbb Z)$, with normalized Lebesgue
measure and Fourier basis $e_k(q)=e^{2\pi ikq}$. For odd $N$, put
$$
 m_N=(N-1)/2,\qquad
 \mathcal H_N=\operatorname{span}\{e_k:|k|\le m_N\}.
$$
The discrete Fourier isometry $\mathcal I_N:\mathbb C^N\to\mathcal H_N$ is
$$
 (\mathcal I_Nv)(q)=
 \sum_{|k|\le m_N}
 \left(N^{-1/2}\sum_{x=0}^{N-1}v_x e^{-2\pi ikx/N}\right)e_k(q).
 \tag{3.1}
$$
Orthogonality of the finite characters proves it is an isometry onto
$\mathcal H_N$. It sends $e_N$ to the constant function one.
If $g$ is a fixed trigonometric polynomial, then for all sufficiently
large $N$,
$$
 \mathcal I_N^{-1}g=(N^{-1/2}g(x/N))_{x=0}^{N-1}.
 \tag{3.2}
$$
Let $P_{\mathcal H_N}=\mathcal I_N\mathcal I_N^*$ and $Jg=\int g$, viewed as a
constant function. Then $\mathcal I_NJ_N\mathcal I_N^*=J$ and
$P_{\mathcal H_N}\to I$ strongly.

For a continuous two-torus kernel $k$, let
$$
 \mathcal K g(q)=\int_0^1 k(q,s)g(s)\,ds,\qquad
 K_N=\left[N^{-1}k(x/N,y/N)\right]_{x,y=0}^{N-1}.
$$
One has
$$
 \|\mathcal I_NK_N\mathcal I_N^*-\mathcal K\|_{\rm op}\longrightarrow0.
 \tag{3.3}
$$
Here and below embedded finite-dimensional operators act by zero on
$\mathcal H_N^\perp$.

To prove (3.3), first take a trigonometric polynomial kernel with each
Fourier coordinate in $[-M,M]$. For $N>2M$, finite character
orthogonality proves exact equality in (3.3), because all its input
and output Fourier modes lie in $\mathcal H_N$. For a general
continuous kernel, approximate uniformly by such polynomials. A
kernel error bounded by $\eta$ gives integral operator norm at most
$\eta$, by its Hilbert--Schmidt norm, and discrete operator norm at
most $\eta$, because all absolute row and column sums of the error
matrix are at most $\eta$. The triangle inequality completes the
proof. Polynomial approximation can be obtained, for example, by
convolution with the two-dimensional Fejér approximate identity; no
pointwise assertion about the original Fourier series is needed.
This proof also shows that $\mathcal K$ is compact.

For the input kernels $k_n$, write their integral operators as
$\mathcal R_n$. Combining (1.9) and (3.3), for every fixed $n\ge1$,
$$
 \widehat R_{n,N}:=\mathcal I_NR_{n,N}\mathcal I_N^*
 \longrightarrow\mathcal R_n
 \quad\hbox{in operator norm}.
 \tag{3.4}
$$
Each $\mathcal R_n$ is compact. The same holds for adjoints.

There is also the exact classical interpretation. Embed
$\mathcal H$ isometrically into $L^2(\mathbb T^2)$ by
$(\iota g)(q,r)=g(q)$. Its adjoint is integration in $r$. Define
the unitary Koopman operator
$$
 (\mathcal C h)(z)=h(F_+^{-1}z).
 \tag{3.5}
$$
The image-density interpretation of $k_n$, or the change of variables
$z=F_+^n(s,r)$ in the area integral, gives
$$
 \mathcal R_n=\iota^*\mathcal C^n\iota.
 \tag{3.6}
$$
More explicitly, for continuous $g,h$,
$$
 \langle h,\mathcal R_ng\rangle
 =\int_{\mathbb T^2}
     \overline{h(q(F_+^n(s,r)))}\,g(s)\,ds\,dr.
 \tag{3.7}
$$
Both sides extend by density to $L^2$, since they are contractions.

## 4. The Fejér domination and its low frequency consequence

For any unitary $\mathcal W$ on a finite-dimensional Hilbert space,
put
$$
 \mathcal A_T(\mathcal W)=\frac1T\sum_{j=0}^{T-1}\mathcal W^j.
$$
If $\mathcal E$ projects onto $\ker(\mathcal W-I)$, the spectral
theorem gives
$$
 \mathcal E\le\mathcal A_T(\mathcal W)^*
                    \mathcal A_T(\mathcal W).
 \tag{4.1}
$$
Indeed the right side has eigenvalue one at the phase zero, and a
nonnegative eigenvalue at each other phase. Its expansion is
$$
 \mathcal A_T(\mathcal W)^*\mathcal A_T(\mathcal W)
 =\frac1T I+\frac2T\sum_{n=1}^{T-1}
                  (1-n/T)\operatorname{Re}(\mathcal W^n),
 \tag{4.2}
$$
where $\operatorname{Re}A=(A+A^*)/2$.

The compression of $\mathcal W_N^n$ to coordinate diagonals has
entries $|(U_N^n)_{xy}|^2$. Consequently (4.1)--(4.2) imply the
exact finite-dimensional inequality
$$
 0\le Q_N\le
 \frac1T(I_N-J_N)
 +\frac2T\sum_{n=1}^{T-1}(1-n/T)
                  \operatorname{Re}(R_{n,N}-J_N).
 \tag{4.3}
$$
The positivity of $Q_N$ follows because $L_N$ is a positive
contraction and fixes $e_N$; its orthogonal complement is invariant.
The constant part in (4.3) cancels exactly, since
$$
 \frac1T+\frac2T\sum_{n=1}^{T-1}(1-n/T)=1.
$$

For fixed $T$, define the compact self-adjoint operator
$$
 \mathcal K_T=\frac2T\sum_{n=1}^{T-1}
          (1-n/T)\operatorname{Re}(\mathcal R_n-J).
 \tag{4.4}
$$
Equation (3.4) implies operator norm convergence of the corresponding
embedded finite sum $\widehat K_{T,N}$ to $\mathcal K_T$.
Thus, after embedding (4.3), its right side is
$$
 \frac1T(P_{\mathcal H_N}-J)+\widehat K_{T,N}.
 \tag{4.5}
$$

The classical version of (4.2), with (3.6), gives
$$
 \frac1T(I-J)+\mathcal K_T
 =\iota^*\mathcal A_T(\mathcal C)^*
                \mathcal A_T(\mathcal C)\iota-J.
 \tag{4.6}
$$
In particular it is positive semidefinite.

For completeness, the needed mean ergodic conclusion can be proved
without citing another theorem. For a unitary $\mathcal C$,
$$
 \overline{\operatorname{ran}(I-\mathcal C)}
       =\ker(I-\mathcal C)^\perp.
$$
This follows by taking orthogonal complements and using
$\ker(I-\mathcal C^*)=\ker(I-\mathcal C)$. On a vector of the
form $(I-\mathcal C)h$, the time average is
$(h-\mathcal C^Th)/T$, which tends to zero in norm. The time
averages are contractions, so the conclusion extends to the closure
of that range. They are exactly the identity on fixed vectors.
Ergodicity from Section 2 makes the fixed vectors of $\mathcal C$
the constant functions. The last assertion follows, for example,
by applying ergodicity to level sets of the real and imaginary parts
of an invariant measurable function.
Therefore, for every $g\in\mathcal H$ of mean zero,
$$
 \|\mathcal A_T(\mathcal C)\iota g\|_2\longrightarrow0.
 \tag{4.7}
$$

Fix such a trigonometric polynomial $g$. For large $N$, it lies
in $\mathcal H_N$. Take its quadratic form in the embedded
(4.3), and first let $N$ tend to infinity at fixed $T$. Equations
(3.4) and (4.6) yield
$$
 0\le\limsup_{N\to\infty}
     \langle g,\mathcal I_NQ_N\mathcal I_N^*g\rangle
 \le\|\mathcal A_T(\mathcal C)\iota g\|_2^2.
 \tag{4.8}
$$
Letting $T$ tend to infinity proves that the left quadratic form
tends to zero. The constant function has zero quadratic form
identically.

Let $E_M$ project onto the fixed Fourier subspace
$\operatorname{span}\{e_k:|k|\le M\}$. Positivity and (4.8) show
$$
 \|E_M(\mathcal I_NQ_N\mathcal I_N^*)E_M\|_{\rm op}\longrightarrow0
 \quad\text{for each fixed }M.
 \tag{4.9}
$$
Indeed the trace of this positive finite-dimensional compression is
the sum of its diagonal quadratic forms in that Fourier basis, and
each tends to zero.

## 5. Compactness controls every remaining frequency

Write $\widehat Q_N=\mathcal I_NQ_N\mathcal I_N^*$. For a fixed integer $T\ge1$,
take quadratic forms of (4.5) on $E_M^\perp$. Since
$P_{\mathcal H_N}-J\le I$, and $E_M$ includes the constants,
$$
 \|(I-E_M)\widehat Q_N(I-E_M)\|_{\rm op}
 \le\frac1T+
       \|(I-E_M)\mathcal K_T(I-E_M)\|_{\rm op}
       +o_T(1).
 \tag{5.1}
$$
The error is independent of $M$, since it is bounded by
$\|\widehat K_{T,N}-\mathcal K_T\|_{\rm op}$.
For this fixed $T$, compactness gives
$$
 \|(I-E_M)\mathcal K_T(I-E_M)\|_{\rm op}\longrightarrow0
 \quad(M\to\infty).
 \tag{5.2}
$$
To check this familiar compactness fact directly, approximate
$\mathcal K_T$ in operator norm by a finite-rank operator. Strong
convergence of $E_M$ to the identity is uniform on the unit ball
of its finite-dimensional range and on that of the range of its
adjoint. The assertion follows by the triangle inequality.

The following positive-block inequality ensures that no off-diagonal
block has been discarded. If $Q\ge0$ and $E$ is an orthogonal
projection, then
$$
 \|Q\|_{\rm op}\le
 \|EQE\|_{\rm op}+\|(I-E)Q(I-E)\|_{\rm op}.
 \tag{5.3}
$$
For $v=x+y$, with $x=Ev$, Cauchy--Schwarz for the semidefinite
form $\langle\cdot,Q\cdot\rangle$ bounds the cross term by
$\sqrt{ab}\|x\|\|y\|$, where
$a=\|EQE\|$, $b=\|(I-E)Q(I-E)\|$. Hence
$$
 \langle v,Qv\rangle
 \le(\sqrt a\|x\|+\sqrt b\|y\|)^2
 \le(a+b)\|v\|^2,
$$
which proves (5.3).

Combine (4.9), (5.1), and (5.3), first with $T,M$ fixed:
$$
 \limsup_{N\to\infty}\|\widehat Q_N\|_{\rm op}
 \le\frac1T+
       \|(I-E_M)\mathcal K_T(I-E_M)\|_{\rm op}.
 \tag{5.4}
$$
Now let $M$ tend to infinity with $T$ fixed, and finally let
$T$ tend to infinity. This proves (1.3).

There is no interchange of an $N$-limit with an unbounded time
sum. Only finite sums of the fixed-time input (1.9) occur before
each $N$-limit. In particular, the argument needs no common
derivative bound for $k_n$ as $n$ tends to infinity.

## 6. Intensity matrices, exact time averages, and approximate stationary vectors

Let $\psi_1,\ldots,\psi_N$ be any orthonormal eigenbasis, and let
$\mathcal E_N^{\rm bas}$ be the orthogonal projection in matrix
Hilbert space onto the span of its rank-one projectors
$\psi_j\psi_j^*$. These are orthonormal Hilbert--Schmidt vectors.
Their span is contained in the full commutant, so
$\mathcal E_N^{\rm bas}\le\mathcal E_N$. Their compressed
projection is exactly $B_NB_N^*$:
$$
 \Pi_N\mathcal E_N^{\rm bas}\Pi_N
     \big|_{\operatorname{ran}\Pi_N}=B_NB_N^*.
 \tag{6.1}
$$
The rows and columns of $B_N$ sum to one by orthonormality, so
$B_NB_N^*$ fixes $e_N$. Subtracting the same constant projection
from both sides of the compressed inequality proves (1.4). No
assumption about multiplicities was used.

The finite-dimensional spectral theorem also gives the exact formula
$$
 L_N=\lim_{T\to\infty}\frac1T
             \sum_{n=0}^{T-1}|U_N^n|^{\circ2},
 \tag{6.2}
$$
in matrix operator norm for each fixed $N$. Thus Theorem 1 also
states that this infinite-time averaged position operator tends to
$J_N$ in operator norm. The order of limits in this interpretation
is $T\to\infty$ at each fixed $N$, followed by $N\to\infty$.

Let $u_N=\mathbf I_N/\sqrt N$ in matrix Hilbert space. Since
$\Pi_Nu_N=u_N$ and $\mathcal E_Nu_N=u_N$,
$$
 (\Pi_N\mathcal E_N-|u_N\rangle\langle u_N|)
 (\mathcal E_N\Pi_N-|u_N\rangle\langle u_N|)
   =\Pi_N\mathcal E_N\Pi_N-|u_N\rangle\langle u_N|.
$$
The nonzero part of the last operator is $Q_N$. Therefore
$$
 \|\Pi_N X\|_{\rm HS}\le\sqrt{q_N}\|X\|_{\rm HS}
 \quad\text{if }\mathcal W_NX=X,\quad\operatorname{Tr}X=0.
 \tag{6.3}
$$
For $q_N<1$, the map $X\mapsto Y=O_NX$ is injective on
that stationary traceless subspace, because
$$
 \|Y\|_{\rm HS}^2
 \ge(1-q_N)\|X\|_{\rm HS}^2.
 \tag{6.4}
$$
Its image $\mathcal V_N$ consequently has dimension $d_N-1$.
Writing $X=D+Y$ with $D=\Pi_NX$, the off-diagonal block of
$\mathcal W_NX=X$ reads
$$
 (I-S_N)Y=C_N^{\rm in}D.
$$
The block $C_N^{\rm in}$ is a contraction. Combining with
(6.3)--(6.4) proves (1.5). The usual singular-value min--max
principle here follows immediately by diagonalizing
$(I-S_N)^*(I-S_N)$: a subspace of dimension $d_N-1$ on which
its Rayleigh quotient is bounded by $q_N/(1-q_N)$ forces at
least that many eigenvalues below that bound.

These approximately stationary vectors do not contradict absence
of an exactly stationary dark vector at $7\nmid N$. They give
no lower bound for an eigenvalue gap of the nonnormal compression
$S_N$.

## 7. The signed first-return derivative and its divergence

This section uses simple spectrum and invertible intensity $B_N$,
which the separate original-family proof establishes for odd
$N$ with $7\nmid N$. Suppress $N$ from the notation and write
$$
 \mathcal W=\begin{pmatrix}P&B\\ C&S\end{pmatrix}.
 \tag{7.1}
$$
The block $B$ in this section is the outgoing block of $\mathcal W$;
the eigenvector intensity matrix remains denoted by $B_N$.

First $1\notin\operatorname{spec}S$. Indeed if $Sy=y$, then
unitarity and the equality of the norm of the compression with
the norm of $y$ imply $By=0$. Hence $(0,y)$ is stationary
for $\mathcal W$. With simple spectrum, every stationary matrix
is a linear combination of the $N$ eigenprojectors. Its diagonal
coefficient vector is $B_Nc$. Invertibility of $B_N$ excludes
a nonzero stationary matrix with zero diagonal, which proves the
claim.

Put $R=(I-S)^{-1}$, and let
$$
 X=\begin{pmatrix}I\\RC\end{pmatrix}:
     \operatorname{ran}\Pi\longrightarrow\mathcal K_N.
 \tag{7.2}
$$
Every coordinate diagonal vector has a unique stationary extension,
because projection from the $N$-dimensional commutant to that
diagonal space is the invertible map $B_N$.
The lower block of this stationary extension must be $RC$.
Therefore $\mathcal WX=X$, and its top block gives
$$
 P+BRC=I.
 \tag{7.3}
$$
As $\mathcal W$ is unitary, also $\mathcal W^*X=X$. Its
bottom block gives
$$
 B^*=(I-S^*)RC,\qquad
 B=C^*R^*(I-S).
 \tag{7.4}
$$

The rational first-return function is
$$
 \mathfrak F(z)=zP+z^2B(I-zS)^{-1}C.
 \tag{7.5}
$$
Equation (7.3) gives $\mathfrak F(1)=I$. Differentiation, using
$R+RSR=R^2$, yields
$$
 \begin{aligned}
 \mathfrak F'(1)
 &=P+2BRC+BRSRC\\
 &=I+BR^2C\\
 &=I+C^*R^*RC=X^*X.
 \end{aligned}
 \tag{7.6}
$$
Let $\mathcal J:\mathbb C^N\to\ker(\mathcal W-I)$ be the
isometry whose columns are the normalized eigenprojectors.
Then $\Pi\mathcal J=B_N$ and $X=\mathcal J B_N^{-1}$, whence
$$
 \mathfrak F'(1)=X^*X
     =(B_N^{-1})^*B_N^{-1}=(B_NB_N^*)^{-1}.
 \tag{7.7}
$$

It remains to justify the signed sums at $z=1$, not just the
rational evaluations. For any contraction $S$, each unit-circle
eigenvector belongs to a reducing unitary subspace: if
$Sy=\zeta y$, $|\zeta|=1$, equality of norms gives
$(I-S^*S)y=0$ and hence $S^*y=\bar\zeta y$.
In the unitary block matrix (7.1), the same norm equality gives
$By=0$, and applying it to $\mathcal W^*$ gives $C^*y=0$.
The span of all such eigenspaces is reducing and is killed by
the two coupling blocks. On its orthogonal complement the
finite-dimensional contraction has spectral radius strictly less
than one. Powers there are bounded by a polynomial times a
decaying geometric sequence, for example by Jordan normal form.
It follows that
$$
 \sum_{r\ge1}r\,\|F_r\|_{\rm op}<\infty.
 \tag{7.8}
$$
Thus the Taylor series of (7.5) and its derivative can be summed
at one; (7.3) and (7.7) prove (1.7).

Finally set
$$
 \beta_N=\|B_NB_N^*-J_N\|_{\rm op}.
$$
On $e_N^\perp$, this positive matrix is invertible, and its largest
eigenvalue is $\beta_N$. By Theorem 1, $0<\beta_N\le q_N\to0$.
Consequently
$$
 \lambda_{\min}\left(
   \left.\mathfrak F_N'(1)\right|_{e_N^\perp}\right)
 =\beta_N^{-1}\ge q_N^{-1}\longrightarrow+\infty,
 \tag{7.9}
$$
which proves (1.8). There is no upper bound for the inverse and no
rate as a function of $N$ in this conclusion.

## 8. What remains unproved

The new estimates identify an operator norm form of stationary
dephasing, a large subspace of approximate stationary vectors of the
off-diagonal compression, and an exact signed return identity with
a divergent derivative on every nonconstant diagonal direction.
They do not estimate $\operatorname{Tr}(U_N^n)$ on the scale
$n\asymp N$.

In particular the first original pair estimate is still
$$
 N^{-2}\sum_{n\ge1}|\widehat b(n/N)|^2
       \bigl(|\operatorname{Tr}(U_N^n)|^2-\min(n,N)\bigr)
       \longrightarrow0
 \tag{8.1}
$$
for each admissible fixed test function $b$. Compact support of
$\widehat b$ makes the sum finite but still includes times
proportional to $N$. Nothing in the proof bounds this signed
sum, and higher orders of $H_{\rm diag}$ remain unproved too.

The separate auxiliary clock countermodel also satisfies
$\|B_NB_N^*-J_N\|_{\rm op}\to0$ after its prescribed generic
microscopic perturbation. Therefore the new stationary conclusion
is explicitly insufficient on its own for the spectral claim.
This is a scope check, not a counterexample to the original family.
