# Weyl-frequency coercivity and a regularized transfer gap for the actual map

**Claim ID:** `BGS-FM-018`. **Status:** project proof with checked classical
mixing input, inherited FM-001/FM-006 prerequisites, independent internal
review of O1--O29, and exact finite controls, 6 October 2026. Base main:
`89645900bdbaace5d4956f306f6dccc464163e35`.
No full BGS conclusion, external priority, effective numerical exponent or
analytic formalization is asserted.

Review and execution scopes are recorded in the
[audit](../../archive/record/frozen_operator_transfer_review_20261006.md) and
[programme](../../archive/record/frozen_operator_transfer_program_20261006.md).

## 1. Objects and conclusions

Keep the unchanged odd-dimensional operator and ordinary symbol from
[`fixed_model_symmetry_theorem.md`](fixed_model_symmetry_theorem.md):

$$
U_N=e^{i\tau N A_N}M_N,\quad \tau=10^{-80},\quad
A_N=\operatorname{Op}_N(g),\quad G=S\circ\Phi_g^{\tau/(2\pi)}.
$$

Here $S=\left(\begin{smallmatrix}3&4\\2&3\end{smallmatrix}\right)$,
$X_g=(g_p,-g_q)$, and $\operatorname{Op}_N(e_\nu)=W_N(\nu)$ for
$e_{(a,b)}(q,p)=e^{2\pi i(bq+ap)}$ and
$W_N(a,b)=(-1)^{ab}T_N(a,b)$. All Weyl labels in algebraic identities
are **integers**, with their alias signs retained.

Use normalized Hilbert--Schmidt norm
$\|X\|_N^2=N^{-1}\operatorname{Tr}(X^*X)$ and the traceless subspace
$\mathcal H_N^0$. On it, $\mathcal P_NX=U_NXU_N^*$ is unitary.
The centered representatives
$B_N=\{-(N-1)/2,\ldots,(N-1)/2\}^2$ give an orthonormal Weyl basis.
Let $\Pi_R^0$ project onto $W_N(\nu)$ with $0<|\nu|\le R$, for
Euclidean $|\nu|$ and $1\le R<N/4$. Define

$$
\begin{split}
\mathscr L_N&=\frac{N^2}{2}\sum_{j=1}^2
 (2I-\operatorname{Ad}T_N(e_j)
       -\operatorname{Ad}T_N(e_j)^*),\\
D_{u,N}&=e^{-u\mathscr L_N},\qquad
\mathcal T_{u,N}=D_{u,N}\mathcal P_N,\quad u>0,\\
\mathcal A_{T,\zeta}&=\frac1T\sum_{j=0}^{T-1}\zeta^{-j}\mathcal P_N^j,
\qquad |\zeta|=1.
\end{split}                                                    \tag{O1}
$$

$\mathscr L_N$ is phase-space diffusion, **not** the spectral-difference
operator $\mathcal D_N$ in `BGS-RES-006`, and $u$ is **not** the Dyson
matrix heat time in FLOW-021. $D_{u,N}$ is a positive self-adjoint
Hilbert--Schmidt contraction and a unital, trace-preserving completely
positive map: its exponential is a Poisson mixture of the four unitary
conjugations in (O1).

**Theorem.** There are $c,\gamma>0$ and $N_0$, depending only on the
fixed actual classical map and symbol, such that for every odd $N\ge N_0$,
with $T_N=\lfloor c\log N\rfloor\ge1$ and
$R_N=\lfloor N^\gamma\rfloor<N/4$:

$$
\sup_{|\zeta|=1}\|\mathcal A_{T_N,\zeta}\Pi_{R_N}^0\|^2
\le\frac1{16}.                                                \tag{O2}
$$

Consequently:

1. If $E_{\zeta,1/T_N}$ is the spectral projection of $\mathcal P_N$
   on $\mathcal H_N^0$ onto the closed arc
   $\{\zeta e^{i\delta}:|\delta|\le1/T_N\}$, then

   $$
   \|\Pi_{R_N}^0E_{\zeta,1/T_N}\|^2\le\frac14,\qquad
   \langle X,\mathscr L_NX\rangle_N\ge6R_N^2\|X\|_N^2
   \quad(X\in\operatorname{ran}E_{\zeta,1/T_N}).               \tag{O3}
   $$

   In particular (O3) holds for every traceless operator commuting with
   $U_N$, allowing arbitrary spectral degeneracies, and for every single
   eigenoperator of $\mathcal P_N$. It also controls every linear
   combination in a whole indicated spectral arc.

2. For every $u>0$, without a normality assumption on $\mathcal T_{u,N}$,

   $$
   \inf_{|\zeta|=1}\sigma_{\min}
     (\mathcal T_{u,N}|_{\mathcal H_N^0}-\zeta I)
   \ge d_{u,N}:=\min\left\{\frac1{128T_N^2},
              \frac{1-e^{-16uR_N^2}}8\right\}.                \tag{O4}
   $$

   Every eigenvalue on $\mathcal H_N^0$ therefore has modulus at most
   $1-d_{u,N}$. At $0<uR_N^2\le1/16$, the second entry in the minimum
   is at least $uR_N^2$. This is a gap for a specified regularized
   quantum operator, not for the unitary $\mathcal P_N$ itself.

3. The uniform operator-norm classical generator comparison fails on the
   full centered Weyl band. Section 7 gives an actual-symbol discrepancy
   at least $\frac9{10}[7\pi(N-1)/2-N]$ for every odd $N\ge19$.

No assumption of simple eigenvalues, prime dimensions, independent
eigenphases, random eigenvectors or average over $\tau$ is used.

## 2. Exact coherent action and the uniform Egorov remainder

For $\omega(v,w)=v_aw_b-v_bw_a$, direct multiplication gives

$$
W_N(v)W_N(w)=e^{\pi i\omega(v,w)/N}W_N(v+w),\quad
M_NW_N(\nu)M_N^*=W_N(S\nu).                                  \tag{O5}
$$

For example the raw multiplication phase is $e_N(2^{-1}\omega)$.
Since $2^{-1}=(N+1)/2$ for odd $N$, the additional sign cancels
$(-1)^{v_aw_b+w_av_b}$. The metaplectic identity follows by substituting
the displayed quadratic kernel for $M_N$; $S$ preserves this ordinary
Weyl convention because its off-diagonal entries are even. The second
identity sends $e_\nu$ to $e_\nu\circ S$ in $(q,p)$ coordinates.

Write $g=\sum_v c_ve_v$ with its fixed finite support. Then

$$
iN[A_N,W_N(\nu)]=-2N\sum_vc_v
 \sin(\pi\omega(v,\nu)/N)W_N(v+\nu),\qquad
\frac{X_ge_\nu}{2\pi}=-2\pi\sum_vc_v\omega(v,\nu)e_{v+\nu}.
                                                                  \tag{O6}
$$

Since $|\sin x-x|\le|x|^3/6$ for real $x$, the triangle inequality
and unitarity of every integer-labelled $W_N$ give, for smooth $a$,

$$
\|iN[A_N,\operatorname{Op}_N(a)]
 -\operatorname{Op}_N(X_ga/(2\pi))\|_{\rm op}
\le C_gN^{-2}\|a\|_{H^5}.                                    \tag{O7}
$$

Indeed the remainder is bounded by
$\pi^3(3N^2)^{-1}\sum_v|c_v||v|^3
\sum_\nu|a_\nu||\nu|^3$. The last sum is bounded by $C\|a\|_{H^5}$
by Cauchy--Schwarz in two dimensions. This argument retains aliases;
it does not require the evolving observable to remain in $B_N$.

Apply Duhamel to
$e^{itNA_N}\operatorname{Op}_N(a)e^{-itNA_N}$ and
$\operatorname{Op}_N(a\circ\Phi_g^{t/(2\pi)})$, for $0\le t\le\tau$.
The derivative difference is (O7) on the evolving classical observable.
Composition by this fixed smooth flow is bounded on $H^5$ uniformly
on that compact time interval. Using (O5) first gives the one-step bound
$\|\mathcal P_N\operatorname{Op}_N(a)-
\operatorname{Op}_N(a\circ G)\|_{\rm op}\le CN^{-2}\|a\|_{H^5}$.

Composition by the fixed smooth area-preserving $G$ is a bounded linear
map on $H^5$, by the chain rule, bounded derivatives through order five,
and change of variables in each $L^2$ derivative term. Choose its norm
bound $K>1$. Telescoping $j$ one-step errors, and using unitarity of
$\mathcal P_N$ on the operator norm, yields constants $C,\Gamma>0$:

$$
\|\mathcal P_N^j\operatorname{Op}_N(a)
 -\operatorname{Op}_N(a\circ G^j)\|_{\rm op}
\le CN^{-2}e^{\Gamma j}\|a\|_{H^5},\qquad j\ge0.              \tag{O8}
$$

Choose $\Gamma$ large enough to bound both the telescoped sum and
$\|a\circ G^j\|_{H^5}\le Ce^{\Gamma j}\|a\|_{H^5}$.
All constants are independent of $a,j,N$. This is the uniform statement
needed for a growing band, stronger in its stated actual-symbol remainder
than merely quoting fixed-observable Egorov convergence.

## 3. Aliasing and quantum correlations without a rank factor

For $a$ supported on $|\nu|\le R<N/4$, orthogonality gives
$\|\operatorname{Op}_N(a)\|_N=\|a\|_2$. If $b$ is smooth, the exact
normalized trace pairs $a_\nu$ with $b_\nu$ and with signed aliases
$b_{\nu+Nk}$, $k\in\mathbb Z^2\setminus\{0\}$. For $s>1$,

$$
\left|\langle\operatorname{Op}_N(a),\operatorname{Op}_N(b)\rangle_N
       -\langle a,b\rangle_{L^2(m)}\right|
\le C_sN^{-s}\|a\|_2\|b\|_{H^s}.                            \tag{O9}
$$

To verify the uniformity, $|\nu+Nk|\ge(3/4)N|k|$ on these aliases,
so $\sum_{k\ne0}(1+|\nu+Nk|^2)^{-s}\le C_sN^{-2s}$ uniformly in
$\nu$. Weighted Cauchy--Schwarz for each residue class and then for $\nu$
proves (O9), since the sets $\nu+N\mathbb Z^2$ are disjoint.
In particular no number of low modes multiplies this estimate.

For $a$ in the nonconstant band and $r\ge0$, (O8), (O9) with $s=5$,
and $\|a\|_{H^5}\le C(1+R)^5\|a\|_2$ give

$$
\left|\langle\operatorname{Op}_N(a),
              \mathcal P_N^r\operatorname{Op}_N(a)\rangle_N
       -\langle a,a\circ G^r\rangle\right|
\le CN^{-2}e^{\Gamma r}(1+R)^5\|a\|_2^2.                     \tag{O10}
$$

The operator-norm error bounds its normalized Hilbert--Schmidt norm;
the other factor has norm exactly $\|a\|_2$. This estimate applies to
each **linear combination** of band modes, not just to individual ones.

## 4. Classical mixing and the band time-average estimate

The actual $G$ is a smooth topologically mixing area-preserving Anosov
map by FM-001. FM-006, Section 2 identifies normalized area as the Gibbs
equilibrium state for the negative unstable potential. The
Parry--Pollicott 1990 symbolic correlation estimate, Proposition 2.4
(printed pp. 29--31, PDF pp. 33--35), together with its Hölder Markov
coding, Appendix III (III.3), gives constants $C_M\ge1,\lambda>0$
and an integer $s_M\ge3$ such that

$$
|\langle a,b\circ G^r\rangle|
\le C_Me^{-\lambda r}\|a\|_{H^{s_M}}\|b\|_{H^{s_M}}
\quad\left(\int a\,dm=\int b\,dm=0\right).                   \tag{O11}
$$

The source-to-target dictionary is: a mixing Markov coding of this
topologically mixing basic set; pullback of the Hölder unstable potential;
its Gibbs state projected to the already identified invariant area;
pullbacks of the observables, whose symbolic Hölder norms are bounded
by their torus $C^1$ norms; and the Sobolev embedding
$H^{s_M}(\mathbb T^2)\hookrightarrow C^1$. Thus (O11) uses the area
measure of the nonlinear map, not the linear cat's measure transported
by an assumed smooth conjugacy. Its constants need not be effective.

For a zero-mean band observable, combine (O11) with the trivial
Cauchy--Schwarz correlation bound to get

$$
|\langle a,a\circ G^r\rangle|
\le\min\{1,C_M(1+R)^{2s_M}e^{-\lambda r}\}\|a\|_2^2.       \tag{O12}
$$

For $K_R=C_M(1+R)^{2s_M}\ge1$, split the sum at
$\lceil\lambda^{-1}\log K_R\rceil$. A geometric tail gives
$\sum_{r\ge1}\min(1,K_Re^{-\lambda r})
\le\lambda^{-1}\log K_R+1+(1-e^{-\lambda})^{-1}$.
The exact correlation expansion of a twisted finite time average now
gives a constant $C_0$ and $B=4s_M/\lambda$ with

$$
\left\|\frac1T\sum_{j=0}^{T-1}\zeta^{-j}a\circ G^j\right\|_2^2
\le\frac{C_0+B\log(1+R)}T\|a\|_2^2,\quad |\zeta|=1.       \tag{O13}
$$

Expanding the quantum average in the same way and applying (O10) to
each lag gives the uniform band-operator bound

$$
\sup_{|\zeta|=1}\|\mathcal A_{T,\zeta}\Pi_R^0\|^2
\le\frac{C_0+B\log(1+R)}T
   +CN^{-2}e^{\Gamma T}(1+R)^5.                              \tag{O14}
$$

For example take $c=1/(2\Gamma)$ and
$0<\gamma\le\min\{1/20,c/(64B)\}$. With the floors in Section 1,
the first term has limit at most $1/64$, and the second tends to zero,
since $\Gamma c+5\gamma\le3/4<2$. Increasing $N_0$ proves (O2).
No trace/rank bound on $\Pi_R^0$ is used.

## 5. Whole spectral arcs and Weyl-energy coercivity

The diffusion is diagonal in the centered Weyl basis:

$$
\mathscr L_NW_N(a,b)=\ell_N(a,b)W_N(a,b),\qquad
\ell_N(a,b)=2N^2[\sin^2(\pi a/N)+\sin^2(\pi b/N)].          \tag{O15}
$$

For centered labels, $8|\nu|^2\le\ell_N(\nu)\le4N^2$,
using $\sin(\pi x)\ge2x$ for $0\le x\le1/2$.
On the arc in (O3), the multiplier of $\mathcal A_{T,\zeta}$ is
$f_T(\delta)=T^{-1}\sum_{j=0}^{T-1}e^{ij\delta}$.
After multiplying by $e^{-i(T-1)\delta/2}$, its real part is at least
$\cos(1/2)\ge7/8>1/2$. By the unitary spectral theorem,
$E_{\zeta,1/T}=\mathcal A_{T,\zeta}^*B_{T,\zeta}$ where
$B_{T,\zeta}$ is supported on this arc and has norm at most $2$.
Thus (O2), by taking adjoints, gives
$\|\Pi_R^0E_{\zeta,1/T}\|\le1/2$.
Every $X$ in this arc therefore has at least $3/4$ of its squared norm
in $|\nu|>R$. Multiplying by the lower bound $8R^2$ in (O15) proves
(O3). The commuting operators are the arc's exact $\zeta=1$ eigenspace,
with the scalar operator omitted by $\mathcal H_N^0$.

## 6. An all-noise singular gap for the actual regularized channel

Write $T=T_N$, $R=R_N$, $\Pi=\Pi_R^0$, and
$k=1-e^{-16uR^2}$. Fix a unit $X\in\mathcal H_N^0$ and $|\zeta|=1$;
put $\varepsilon=\|\mathcal T_{u,N}X-\zeta X\|_N$ and
$d=1-\|\mathcal T_{u,N}X\|_N^2$. Positivity and contractivity of $D$
give

$$
0\le d\le2\varepsilon,\qquad
\|(I-D)\mathcal P_NX\|_N^2\le d,\qquad
\|\mathcal P_NX-\zeta X\|_N\le\sqrt d+\varepsilon.           \tag{O16}
$$

The first upper bound follows either from $\varepsilon\ge1$ or from
$\|\mathcal T X\|\ge1-\varepsilon$; the middle bound uses
$(1-d_\nu)^2\le1-d_\nu^2$ on each diffusion eigenvalue.
If $\varepsilon\ge1/(128T^2)$ the claimed lower bound is immediate.
Otherwise $\sqrt d+\varepsilon\le2\sqrt{2\varepsilon}$, and
telescoping the twisted powers gives

$$
\|\mathcal A_{T,\zeta}X-X\|_N
\le\frac{T-1}{2}(\sqrt d+\varepsilon)<\frac18.                \tag{O17}
$$

On the other hand (O2) and $\|\mathcal A_{T,\zeta}\|\le1$ give
$\|\mathcal A_{T,\zeta}X\|\le1/4+\|(I-\Pi)X\|$.
It follows that $\|(I-\Pi)X\|>5/8$.
Since $D$ commutes with $\Pi$ and is a contraction,

$$
\|(I-\Pi)\mathcal P_NX\|
\ge\|(I-\Pi)\mathcal T X\|
\ge\|(I-\Pi)X\|-\varepsilon>\frac12.                        \tag{O18}
$$

By (O15), $1-D^2\ge k(I-\Pi)$ on the traceless space. Therefore
$2\varepsilon\ge d\ge k\|(I-\Pi)\mathcal P_NX\|^2>k/4$.
This proves (O4) by taking the infimum over $X$ and $\zeta$.
For any channel eigenvalue $\rho e^{i\theta}$ with a unit eigenvector,
test $\zeta=e^{i\theta}$ to get $1-\rho\ge d_{u,N}$; zero eigenvalues
already satisfy the conclusion. Nonnormality does not enter the proof.

## 7. A full-band classical generator comparison is false for this symbol

Identify $\mathcal H_N$ with Fourier polynomials supported in $B_N$ by
the centered Weyl basis. Let $\mathcal B_N$ be the matrix of
$a\mapsto\operatorname{proj}_{B_N}(X_ga/(2\pi))$ under this identification,
and $\mathcal Q_N=iN\operatorname{ad}A_N$. The actual ordinary Fourier
coefficient $c_{(0,7)}=9/20$. Test
$\nu=((N-1)/2,0)$. For odd $N\ge19$, $\nu+(0,7)\in B_N$ and no
other fixed symbol frequency is congruent to $(0,7)$ modulo $N$.
Equation (O6) gives

$$
\|\mathcal Q_N-\mathcal B_N\|
\ge\frac9{10}\left|N\sin\frac{-7\pi(N-1)}{2N}
                       +\frac{7\pi(N-1)}2\right|
\ge\frac9{10}\left[\frac{7\pi(N-1)}2-N\right].              \tag{O19}
$$

For the generator with the actual kick time, multiply this bound by
$\tau$. This defeats full-band operator-norm convergence of the
generators; it does not exclude a weighted or signed long-time comparison.

## 8. Exact Gaussian Hamiltonian realization and the quadratic massive block

Let $Z=T_N(0,1)$, $X=T_N(1,0)$ and take the four Hermitian matrices
$(Z+Z^*)/2$, $(Z-Z^*)/(2i)$, $(X+X^*)/2$, $(X-X^*)/(2i)$,
denoted $H_1,\ldots,H_4$. Their ordinary symbols are respectively
$\cos2\pi q,\sin2\pi q,\cos2\pi p,\sin2\pi p$.
Exact multiplication of left and right matrix actions gives

$$
 (\operatorname{ad}H_1)^2+(\operatorname{ad}H_2)^2
 =2I-\operatorname{Ad}Z-\operatorname{Ad}Z^*,\qquad
\mathscr L_N=\frac{N^2}{2}\sum_{\ell=1}^4
                    (\operatorname{ad}H_\ell)^2.             \tag{O21}
$$

The identical $X$-pair identity is understood.
Take four independent standard real Gaussians $\xi_\ell$, and set

$$
K_{u,\xi}=e^{iN\sqrt u(\xi_1H_1+\xi_2H_2)}
          e^{iN\sqrt u(\xi_3H_3+\xi_4H_4)},\qquad
V_{u,\xi}=K_{u,\xi}U_N.
$$

Each pair's two commutator generators commute. The Gaussian characteristic
function therefore averages its adjoint exactly to the exponential of
minus $uN^2/2$ times the pair's squared generators. The two averaged pair
channels commute as well: $\operatorname{Ad}X$ and
$\operatorname{Ad}Z$ commute, since $XZ$ and $ZX$ differ by a scalar.
Independence of the pairs proves the exact identity

$$
\mathbb E\operatorname{Ad}V_{u,\xi}
       =D_{u,N}\mathcal P_N=\mathcal T_{u,N}.                 \tag{O22}
$$

The periodic Hamiltonian vector fields satisfy
$\sum_{\ell=1}^4(X_{h_\ell}/(2\pi))^2=\Delta_{\mathbb T^2}$.
Thus the regulator has an explicit elliptic classical dictionary. It is
a **product of two Gaussian Hamiltonian kicks**; it is not silently
identified with a single exponential of four noncommuting matrices.

For $u_N=N^{-\alpha}$ with any fixed $0<\alpha<1+2\gamma$, (O4) gives
$Nd_{u_N,N}/\log N\to\infty$. For fixed $s\ge0$ and real $\omega$,
$z_N=e^{-s/N+i\omega/N}$, the singular-value perturbation bound gives

$$
\sigma_{\min}(I-z_N\mathcal T_{u_N,N}|_{\mathcal H_N^0})
\ge d_{u_N,N}-(1-e^{-s/N})\ge\tfrac12 d_{u_N,N}              \tag{O23}
$$

for all sufficiently large odd $N$. The identity mode is the unique
massless mode at $z=1$; every traceless mode has the displayed singular
mass even on the microscopic source scale. At fixed finite Gaussian
parameters the underlying kick times tend to zero as $u_N\to0$, so the
classical maps converge to the same $G$; no uniform convergence over
the unbounded Gaussian support is asserted.

This closes the **quadratic** massive-mode input for this explicit
ensemble around the actual $U_N$. Zirnbauer's primary 1998 formula
identifies the quadratic block as $I-\mathbb E\operatorname{Ad}V$;
its full action averages a nonlinear determinant functional. O23 gives
no bound on that functional's higher terms, other saddle contributions
or the difference between ensemble statistics and those of $U_N$.
The zero-mode approximation itself remains OPEN here.

## 9. Heisenberg application, noise-removal boundary and exact target

If $u=u_N>0$ obeys
$Nu_NR_N^2/\log N\to\infty$, (O4) implies
$Nd_{u_N,N}/\log N\to\infty$. Since the channel preserves the scalar
identity and the traceless space, for $0<a<b<\infty$,

$$
\sup_{aN\le m\le bN}
 |\operatorname{Tr}_{HS}\mathcal T_{u_N,N}^m-1|
\le(N^2-1)(1-d_{u_N,N})^{aN}\longrightarrow0.                \tag{O20}
$$

Trace of powers is the sum of eigenvalue powers even for Jordan blocks.
However this is **not** the CUE ramp of the original unitary spectrum.
For independent fresh Poisson-mixture noise $V_j=K_jU_N$ at each step,
the trace is $\mathbb E|\operatorname{Tr}(V_m\cdots V_1)|^2$.
The fixed-ensemble statistic
$\mathbb E|\operatorname{Tr}V^m|^2$ retains the same $V$ at every step
and is generally different. A Haar example already separates them:
the averaged adjoint channel is the scalar projection, with trace $1$
at every power, whereas the Haar-CUE fixed-matrix value is $m$ for $m<N$.
This ensemble issue was already present in the repository's reset/coherent
memory distinction; no novelty for it is claimed.

There is also an elementary microscopic boundary. From (O15),
$\sigma_{\min}(\mathcal T_{u,N})\ge e^{-4uN^2}$; hence **each** channel
eigenvalue has modulus at least $e^{-4uN^2}$. If $u_NN^3\to0$, no
Heisenberg radial gap with $N(1-|\lambda|)\to\infty$ is possible.
More generally, if a unitary ensemble $V$ has
$\varepsilon_N=\mathbb E\|V-U_N\|_{\rm op}$, its averaged adjoint
channel $\overline{\mathcal P}_N$ satisfies
$\|\overline{\mathcal P}_N-\mathcal P_N\|\le2\varepsilon_N$.
The traceless commutant has dimension at least $N-1$. Min--max thus gives
at least $N-1$ singular values of $I-z\overline{\mathcal P}_N$ bounded
by $1-z+2z\varepsilon_N$, for $0<z<1$. At $z=e^{-s/N}$,
$\varepsilon_N=o(N^{-1})$ cannot lift these modes to a singular mass
much larger than $N^{-1}$. This is a statement about singular values;
it does not turn nonnormal pseudospectral modes into eigenvalue counts.

For a continuous compactly supported $w$ in $[a,b]$, the same bound gives
the following CUE-centered test. For every positive integer $m$, the exact
Haar-CUE moment is $\mathbb E|\operatorname{Tr}V^m|^2=\min(m,N)$:
the CUE projection kernel gives $N-(N-m)_+$ by counting the overlap
of its occupied Fourier modes $0,\ldots,N-1$ with their translate by $m$.

$$
\frac1{N^2}\sum_m w(m/N)
  (\operatorname{Tr}_{HS}\mathcal T_{u_N,N}^m-\min(m,N))
\longrightarrow-\int_a^b \min(\xi,1)w(\xi)\,d\xi.          \tag{O24}
$$

Thus a comparison equating this annealed trace test to the actual signed
CUE test with an error tending to zero would give the wrong limit for
nonzero nonnegative $w$. A coherent correction must restore the CUE
ramp and plateau; on a band $b<1$ the displayed centering reduces to $m$.
This diagnoses that proposed comparison, not the BGS conjecture.

## 10. The nonlinear functional is not determined by its gapped Hessian

For odd $N\ge3$, here is a finite discriminator, without assuming the actual-map
ensemble has the same defect. Let $\mathcal W_N$ be the uniform ensemble
of $N^2$ Weyl matrices $W_N(a,b)$, $0\le a,b<N$, and $\mathcal F_N$
the ensemble of $W_N(a,b)F_N$ for the discrete Fourier unitary
$(F_N)_{xy}=N^{-1/2}e_N(xy)$. Both averaged adjoint channels equal
the scalar projection, so both traceless quadratic blocks equal $I$.

For the admissible bosonic direction $Z=zE_{00}$,
$\widetilde Z=\bar zE_{00}$, $r=|z|^2<1$, the ordinary determinant
factor in the color-flavor functional is
$\det(I-Z\widetilde Z)/\det(I-\widetilde Z VZV^*)
=(1-r)/(1-r|V_{00}|^2)$. Direct averaging gives

$$
\begin{split}
\mathbb E_{\mathcal W_N}\frac{1-r}{1-r|V_{00}|^2}
 &=1-(1-1/N)r,\\
\mathbb E_{\mathcal F_N}\frac{1-r}{1-r|V_{00}|^2}
 &=\frac{1-r}{1-r/N}.
\end{split}                                                   \tag{O25}
$$

Indeed $|V_{00}|^2$ is $1$ with probability $1/N$ and $0$ otherwise
for the first ensemble, and is always $1/N$ for the second. The
negative logarithms have the same coefficient of $r$, $1-1/N$,
but their coefficients of $r^2$ differ by $-1/N+1/N^2$; their limits
as $r\uparrow1$ differ as well. Consequently even the perfect massive
quadratic block does not determine this nonlinear functional.

The fixed-matrix spectral statistics also differ. At every odd $N$,
$\mathbb E_{\mathcal W_N}|\operatorname{Tr}V^4|^2=1$: $4$ is
invertible modulo $N$, so only $V=I$ has a nonzero fourth-power trace.
On the other hand, $\operatorname{Ad}F_N$ rotates Weyl labels by
$J(a,b)=(b,-a)$, $J^4=I$ and $I+J+J^2+J^3=0$.
Hence each $(W_N(a,b)F_N)^4$ is scalar and
$\mathbb E_{\mathcal F_N}|\operatorname{Tr}V^4|^2=N^2$.
For odd $N\ge9$, $4<N/2$, so this discriminator lies in the stable
moment range. These ensembles are not vanishing perturbations of the
actual $U_N$; they refute sufficiency of the averaged-channel Hessian
**alone**, not a theorem retaining the classical map, regulator and
full nonlinear functional.

## 11. Exact common-noise higher moments and the first remaining block

Retain the **same** four Gaussian parameters in all $k$ copies. On
$\mathcal K_{N,k}=M((\mathbb C^N)^{\otimes k})$, set
$H_\ell^{[k]}=\sum_{r=1}^k H_\ell^{(r)}$ and
$Q_{q,k}=(\operatorname{ad}H_1^{[k]})^2+
          (\operatorname{ad}H_2^{[k]})^2$, with the analogous $Q_{p,k}$.
The same within-pair Gaussian calculation as in Section 8 gives exactly

$$
\mathbb E\operatorname{Ad}(V_{u,\xi}^{\otimes k})
 =e^{-uN^2Q_{q,k}/2}e^{-uN^2Q_{p,k}/2}
       \operatorname{Ad}(U_N^{\otimes k}).                    \tag{O26}
$$

This retains the order of the two averaged pair channels. For $k=2$
they do not commute, already for every odd $N\ge3$. In the coordinate
matrix-unit basis $E_{x,y}$, $x,y\in(\mathbb Z/N\mathbb Z)^2$,
$Q_{q,2}$ is diagonal with eigenvalue
$|e_N(x_1)+e_N(x_2)-e_N(y_1)-e_N(y_2)|^2$. To check the other action,
put $S_X=X\otimes I+I\otimes X$; then
$Q_{p,2}=\operatorname{ad}S_X\operatorname{ad}S_X^*$, and
$S_XS_X^*=2I+X\otimes X^*+X^*\otimes X$.
Applied to $E_{(0,0),(0,0)}$, the coefficient of
$E_{(-1,1),(0,0)}$ in $Q_{p,2}$ is $1$. Its $Q_{q,2}$ eigenvalue
is $4(1-\cos(2\pi/N))^2$, while the initial matrix unit's is zero.
Consequently

$$
\big[Q_{q,2},Q_{p,2}\big]_{,((-1,1),(0,0)),\,((0,0),(0,0))}
 =4(1-\cos(2\pi/N))^2>0.                                    \tag{O27}
$$

The two target row shifts are distinct for odd $N\ge3$. No other term
in $\operatorname{ad}S_X\operatorname{ad}S_X^*$ reaches the indicated
matrix unit. Thus O26 cannot be reduced to a single exponential of
$Q_{q,2}+Q_{p,2}$ by the one-copy commutation argument.

Let $\mathsf S_N$ exchange the two physical tensor factors. Every
$V\otimes V$ commutes with it. Hence the nonzero operator
$\mathsf S_N-I/N$, which has zero partial trace in each factor and
normalized squared Hilbert--Schmidt norm $1-1/N^2$, satisfies

$$
\mathbb E\operatorname{Ad}(V_{u,\xi}^{\otimes2})
             (\mathsf S_N-I/N)=\mathsf S_N-I/N.                \tag{O28}
$$

The one-copy traceless gap therefore does **not** tensorize to common
noise on $\mathcal H_N^0\otimes\mathcal H_N^0$. These permutation
invariants are the usual universal contraction sector, not evidence
against CUE. The finite-dimensional invariant space can be classified
completely: for every odd $N\ge3$, every $u>0$ and every unitary $U_N$,

$$
\ker\left(I-\mathbb E\operatorname{Ad}(V_{u,\xi}^{\otimes2})\right)
 =\operatorname{span}\{I,\mathsf S_N\},                       \tag{O29}
$$

and there are no other eigenvalues on the unit circle.
Here is a direct proof, with no representation-theory theorem imported.
If the channel has a unit vector $C$ with unit-modulus eigenvalue $\eta$,
then
$\mathbb E\|\operatorname{Ad}(V_{u,\xi}^{\otimes2})C-\eta C\|^2=0$.
Continuity and full support of the four Gaussian parameters give this
equality for every parameter, including zero. Dividing by the zero-noise
action then shows that $C$ commutes with all four collective Hamiltonians
$H_\ell^{[2]}$ and their generated Lie group.

The single-copy real Lie algebra generated by $iH_\ell$ is $\mathfrak{su}(N)$.
To check this explicitly, its complexification contains $X,X^*,Z,Z^*$.
Successive commutators with $Z$ generate all $W_N(1,b)$: their
commutator coefficients never vanish since the first coordinate is $1$.
For $b\not\equiv0\pmod N$, successive commutators with $X$ then
generate every $W_N(a,b)$, since $\sin(\pi b/N)\ne0$.
Finally commuting $W_N(a,1)$ with $Z^*$ gives $W_N(a,0)$ for every
$a\not\equiv0$. These are all $N^2-1$ nonconstant Weyl matrices,
a basis of $\mathfrak{sl}_N(\mathbb C)$; aliases contribute only
nonzero signs. The generators are traceless skew-Hermitian, so their
compact real algebra has this complexification and equals
$\mathfrak{su}(N)$. The same Lie operations in two copies give the
collective $SU(N)$ action.

For completeness, its two-copy commutant is $\operatorname{span}\{I,\mathsf S_N\}$.
Commutation with diagonal unitaries allows a matrix element only between
two ordered index pairs with the same unordered multiset. Simultaneous
coordinate permutations force a common diagonal value $a$ on $|ii\rangle$
and a common block $\left(\begin{smallmatrix}b&c\\c&b\end{smallmatrix}\right)$
on each span of $|ij\rangle,|ji\rangle$, $i\ne j$.
The collective generator $E_{ij}+E_{ji}$ sends $|ii\rangle$ to
$|ij\rangle+|ji\rangle$, forcing $a=b+c$. Thus the operator is
$bI+c\mathsf S_N$. Using $SU(N)$ instead of $U(N)$ makes no change,
because their scalar phases cancel in conjugation. Conversely these
two operators commute with every $V\otimes V$. The proposed eigenvector
therefore already lies in this fixed space, and its eigenvalue is $1$.
This proves O29 and the unit-circle assertion.

The orthogonal complement of this space is invariant under each
conjugation and its adjoint, so it has a strictly positive finite-N
singular gap on the unit circle. This proof gives **no uniform rate**
as $N\to\infty$, $u=u_N\to0$: its Lie-generation depth grows with $N$.
A next precise obligation is a quantitative estimate for O26 at $k=2$
on this complement, followed by control of the nonlinear determinant
integral and the original signed noise defect. Independent-copy noise
would replace O26 by a tensor product of one-copy channels and would
erase the required common-ensemble moments.

The new actual-map input is the uniform growing-band average and its
consequences (O2)--(O4). Classical/quantum noisy relaxation and Egorov
methods predate it; see the exact-source
[literature review](../../literature/frozen_operator_transfer_sources_20261006.md).
Priority has not been established. Zirnbauer's color-flavor route concerns
an ensemble-averaged nonlinear functional, not merely trace powers of this
channel; (O20) does not refute that route. Its model-specific zero-mode
approximation and removal of averaging remain unproved here.

The actual unregularized signed sum
$N^{-2}\sum_m w(m/N)(|\operatorname{Tr}U_N^m|^2-m)$ in a stable band,
the higher factorial counterterms and `BGS-BGS-001` remain **OPEN**.
No comparison at that target is supplied by (O2)--(O4) alone.
