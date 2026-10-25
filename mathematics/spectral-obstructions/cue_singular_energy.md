# Singular CUE pair energy and the unregularized adjoint boundary

**Claim:** BGS-CUE-001. **Scope:** Haar CUE, not the prescribed fixed
quantum map. **Status:** project deduction from a checked published
small-gap theorem plus the determinantal argument below; author check,
no claim of priority or external refereeing. No statement here proves the
fixed-coupling BGS conjecture.

Let the eigenvalues of a Haar unitary $V_N\in U(N)$ be $e^{i\theta_j}$.
All pair sums below are **ordered**:

$$
F_{N,p}=\sum_{j\ne k}|e^{i\theta_j}-e^{i\theta_k}|^{-p}.
$$

## The stable-law statement

**Theorem.** For $3/2<p<3$, $F_{N,p}$ has finite expectation, infinite
variance for every $N\ge2$, and

$$
N^{-4p/3}(F_{N,p}-\mathbb EF_{N,p})
 \ \xrightarrow{\mathrm d}\ Z_p,\qquad
\log\mathbb Ee^{itZ_p}
 =\frac{2^{3/p}}{24\pi p}\Gamma(-3/p)(-it)^{3/p}.       \tag{1}
$$

The principal branch is understood. In particular, for $p=2$,

$$
E_N=N^{-3}F_{N,2},\quad
\mathbb EE_N=\frac{1-N^{-2}}6,\quad
N^{1/3}(E_N-\mathbb EE_N)\xrightarrow{\mathrm d}Z_2,
$$

$$
\mathbb Ee^{itZ_2}
=\exp\!\left[-\frac{|t|^{3/2}}{18\sqrt\pi}
       (1+i\operatorname{sgn}t)\right].                \tag{2}
$$

The theorem uses Ben Arous--Bourgade, Annals of Probability **41** (2013),
Theorem 1.1 [pinned dependency EXT-BAB-2013](../../literature/external_dependencies.json).
Its small-gap point-process convergence is the external input; the
summation over *all* pairs requires the separate tail estimate proved
below. This theorem concerns the unregularized CUE reference distribution,
not a fixed deterministic $U_N$.

## Exact two-point normalization

Set $d\mu(\theta)=d\theta/(2\pi)$. Relative to this measure the CUE
projection kernel and its correlation functions are

$$
K_N(x,y)=\sum_{r=0}^{N-1}e^{ir(x-y)},\quad
\rho_{k,N}(x_1,\ldots,x_k)=\det[K_N(x_a,x_b)]_{a,b\le k}.
$$

Consequently, for $|\delta|\le\pi$,

$$
\rho_{2,N}(0,\delta)=2\sum_{m=1}^{N-1}(N-m)(1-\cos m\delta)
\le\min\left\{N^2,\frac{N^2(N^2-1)}{12}\delta^2\right\}. \tag{3}
$$

Indeed $\sum_{m=1}^{N-1}(N-m)m^2=N^2(N^2-1)/12$.
For $p=2$, integrating
$(1-\cos m\delta)/(4\sin^2(\delta/2))$ against $\mu$
gives $m/2$. Therefore

$$
\mathbb EF_{N,2}
 =\sum_{m=1}^{N-1}m(N-m)=\frac{N(N^2-1)}6.             \tag{4}
$$

For $1<p<3$, splitting the integral of
$\rho_2|2\sin(\delta/2)|^{-p}$ at $|\delta|=N^{-1}$
gives $\mathbb EF_{N,p}\le C_pN^{p+1}$. For $N\ge2$,
restrict the CUE joint density to configurations in which exactly one
pair has separation $\delta\downarrow0$, while other points stay
separated from that pair and each other. The density there is bounded
above and below by constants times $\delta^2$; the square of the
pair contribution is at least $c\delta^{-2p}$.
The integral $\int_0^\varepsilon\delta^{2-2p}\,d\delta$
diverges for $p\ge3/2$, proving the stated infinite variance.

## Determinantal variance inequality

For bounded nonnegative even $g$ on the circle write
$S_g=\sum_{j\ne k}g(\theta_j-\theta_k)$ and $M_g=\mathbb ES_g$.
Partition the ordered index pairs in $\mathbb ES_g^2$ by the number
of distinct indices. With $g_{xy}=g(x-y)$,

$$
\begin{aligned}
\operatorname{Var}(S_g)
={}&2\int g_{xy}^2\rho_2(x,y)\,d\mu^2
 +4\int g_{xy}g_{xz}\rho_3(x,y,z)\,d\mu^3\\
 &+\int g_{xy}g_{zw}
       \bigl(\rho_4(x,y,z,w)-\rho_2(x,y)\rho_2(z,w)\bigr)\,d\mu^4.
\end{aligned}                                             \tag{5}
$$

The kernel is positive semidefinite. Fischer's determinant inequality
gives $\rho_4\le\rho_2(x,y)\rho_2(z,w)$.
Taking the Schur complement of $K_N(x,x)=N$ and bounding a positive
$2\times2$ determinant by its diagonal product gives

$$
\rho_3(x,y,z)\le\frac{\rho_2(x,y)\rho_2(x,z)}N.
$$

The last line of (5) is nonpositive because $g\ge0$;
rotation invariance makes $\int g_{xy}\rho_2(x,y)d\mu(y)$
independent of $x$ and equal to $M_g$. Hence the useful
nonasymptotic inequality

$$
\operatorname{Var}(S_g)\le
2\int g(\delta)^2\rho_{2,N}(0,\delta)d\mu(\delta)
+\frac4N M_g^2.                                    \tag{6}
$$

There is no assumed independence of gaps.

For $p=2$, choose $g(\delta)=
|2\sin(\delta/2)|^{-2}{\bf1}_{|\delta|>b}$, with the
shortest circle difference $\delta\in[-\pi,\pi]$.
Using $|2\sin(\delta/2)|\ge2|\delta|/\pi$, (3)--(4) imply

$$
\operatorname{Var}(F_{N,2;>b})
\le\frac{\pi^3N^4}{96b}+\frac{N(N^2-1)^2}{9}.        \tag{7}
$$

Thus for $b=RN^{-4/3}\le\pi$,

$$
\operatorname{Var}(N^{-8/3}F_{N,2;>b})
\le\frac{\pi^3}{96R}+\frac{N^{-1/3}}9.               \tag{8}
$$

For general $3/2<p<3$, the same argument gives, for fixed
$R>0$ and all sufficiently large $N$,

$$
\operatorname{Var}(N^{-4p/3}F_{N,p;>RN^{-4/3}})
\le C_p\bigl(R^{3-2p}+N^{1-2p/3}\bigr).             \tag{9}
$$

The first integral in (6) is
$O_p(N^4 b^{3-2p})$; the second uses
$\mathbb EF_{N,p}=O_p(N^{p+1})$.
In the opposite region, (3) gives

$$
\mathbb E\!\left[N^{-4p/3}F_{N,p;<\varepsilon N^{-4/3}}\right]
\le C_p\varepsilon^{3-p}.                           \tag{10}
$$

For $p=2$ one can take the explicit bound $\pi\varepsilon/48$.
The indicator at a boundary point makes no difference.

## Poisson passage and centering

Theorem 1.1 of the cited source proves convergence of consecutive
circular angle gaps rescaled by $N^{4/3}$, marked by their angular
location, to a Poisson point process. Integrating over the location
gives gap intensity

$$
\lambda(dx)=\frac{x^2}{24\pi}\,dx,\qquad x>0.        \tag{11}
$$

The source states the positional theorem for arcs strictly inside
$(0,2\pi)$. To include the fixed circular seam, first exclude an
arbitrarily small arc around it. Rotation invariance, (3), and a
Markov bound control small-gap pairs in that arc. Let its length
tend to zero after $N\to\infty$.

For fixed $R$, a close pair at angular distance at most
$RN^{-4/3}$ that is not consecutive would contain a third point
inside the shorter arc. The Schur bound for $\rho_3$, together with
(3), bounds the expected number of such triples by
$CN^7(RN^{-4/3})^6=CR^6/N$. Hence close pairs are consecutive
with probability tending to one.

For $0<\varepsilon<R$, continuous mapping applied to (11) gives
the contribution $2/x^p$ per small gap $x\in[\varepsilon,R]$.
The factor two counts ordered pairs. The contribution of
$x<\varepsilon$ disappears by (10).
The precise centering follows by expanding (3) for
$|\delta|\le RN^{-4/3}$:

$$
\rho_{2,N}(0,\delta)
=\frac{N^2(N^2-1)}{12}\delta^2+O(N^6\delta^4).
$$

For every fixed $R$ this gives

$$
N^{-4p/3}\mathbb EF_{N,p;\le RN^{-4/3}}
\longrightarrow\frac1{12\pi}\int_0^R x^{2-p}\,dx
=\frac{R^{3-p}}{12\pi(3-p)}.                         \tag{12}
$$

The right side equals $\int_0^R2x^{-p}\lambda(dx)$.
Let $\Pi$ have intensity (11) and set

$$
Z_{p,R}=\sum_{x\in\Pi,\,x\le R}2x^{-p}
-\frac{R^{3-p}}{12\pi(3-p)}.
$$

For fixed $R$, the centered close-pair sum converges in law to
$Z_{p,R}$. The interval $x\in(0,R]$ contains finitely many
Poisson points almost surely, but $Z_{p,R}$ need not have a
finite second moment. For $R'>R>0$, its *increment* has finite
variance $\int_R^{R'}4x^{-2p}\lambda(dx)$, tending to zero as
$R\to\infty$ since $p>3/2$.
The finite-$N$ centered tails tend to zero in the corresponding
double limit by (9). This proves (1) using the converging-together
lemma.

Under $y=2/x^p$ the Poisson measure becomes

$$
\nu_p(dy)=\frac{2^{3/p}}{24\pi p}
              y^{-1-3/p}{\bf1}_{y>0}\,dy.
$$

Because $1<3/p<2$, the compensated exponent
$\int_0^\infty(e^{ity}-1-ity)\nu_p(dy)$ converges at both
endpoints and equals the exponent in (1). At $p=2$, use
$\Gamma(-3/2)=4\sqrt\pi/3$ to get (2). The endpoints
$p=3/2$ and $p=3$ are not covered by this theorem.

## Why this does not remove the regularization for the fixed map

For *any* unitary $U$, $\mathcal U(X)=UXU^*$ and
$Q_r=I-r\mathcal U$, $0<r<1$, satisfy

$$
\operatorname{Tr}_{HS}(Q_r^*Q_r)^{-1}
=\frac{N^2+2\sum_{m\ge1}r^m|\operatorname{Tr}U^m|^2}{1-r^2}.
                                                               \tag{13}
$$

This follows by diagonalizing $\mathcal U$ on eigenmatrix
units and applying the Poisson-kernel series. If the spectrum
is simple, deleting its $N$ diagonal zero modes before taking
$r\uparrow1$ yields the unregularized pair energy $F_{N,2}$.
Equation (13) is an exact rewrite, not an estimate for the
maintained $U_N$.

A quantitative failure of removing regularization from weak local
information is elementary. In any simple $N$-point spectrum,
choose a smallest circular gap $d_N\le2\pi/N$. Move one endpoint
towards the other, leaving all eigenvectors fixed, until the new
gap satisfies $0<\delta_N\le\min(d_N,2\pi/N^3)$. Then

$$
\|\widetilde U_N-U_N\|_1\le2\pi/N,\qquad
N^{-3}\sum_{j\ne k}|\widetilde\lambda_j-
\widetilde\lambda_k|^{-2}
\ge\frac{2}{N^3\delta_N^2}\ge\frac{N^3}{2\pi^2}.      \tag{14}
$$

With a uniformly random angular origin, any bounded window in
unfolded units encounters either the old or new location of
that single moved point with probability $O(1/N)$.
Therefore an existing **weak local point-process limit** is
preserved. Equation (14) does not claim preservation of all
unbounded factorial-correlation moments or realization by a
quantization of the same classical map.

The actual fixed-strength pair Abel target
$N^{-2}\sum_{m\ge1}e^{-2sm/N}|\operatorname{Tr}U_N^m|^2
\to(1-e^{-2s})/(4s^2)$ remains OPEN, as does the full
signed joint-trace BGS claim. The CUE determinantal bound (6)
is unavailable for that fixed deterministic family.
