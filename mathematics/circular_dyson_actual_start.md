# Circular Dyson relaxation from the actual frozen initial spectrum

**Claim ID: BGS-FLOW-014.** Project proof, 4 October 2026,
at base `4982f8fc3d6303cc2cf7840e608f07d41ba2783e`.
The new analytic implications passed an independent internal audit;
inherited inputs retain their stated trust boundaries. The finite arbitrary-start
kernel is prior work, not a new formula. This argument concerns a noisy
auxiliary system; deterministic BGS and noise removal remain separate.

## 1. Quantified relaxation statement

Let $N$ be odd, $A_N$ unitary, and $m_j=N^{-1}\operatorname{Tr}A_N^j$.
Let $J_N\ge1$ be an integer and $d_N,\kappa_N\ge0$.
Suppose, for $1\le j\le J_N$, that

$$
|m_j|\le d_N+\kappa_N j/N.
\tag{U1}
$$

For $0<g_N\le t_N/8$ and $0<t_N\le1$, define

$$
E_N=\frac{2[d_N+e^{-(J_N+1)t_N/8}]}{1-e^{-t_N/8}}
+\frac{2\kappa_N e^{-t_N/8}}{N(1-e^{-t_N/8})^2},
\tag{U2}
$$

$$
v_N=d_N\log\frac1{1-e^{-g_N}}
+\frac{e^{-(J_N+1)g_N}}{(J_N+1)(1-e^{-g_N})}
+\frac{\kappa_N e^{-g_N}}{N(1-e^{-g_N})}.
\tag{U3}
$$

Assume $E_N\to0$, $v_N/t_N\to0$ and $Nt_N\to\infty$.
For normalized **full** unitary Brownian motion $B_t$, with
$\mathbb EB_t=e^{-t/2}I$, the local spectrum of $B_{t_N}A_N$, unfolded
by $N/(2\pi)$, converges to Sine$_2$, uniformly in the observation angle.
The statement includes repeated initial eigenvalues. More precisely, for
every $0\le f\in C_c(\mathbb R)$, its local Laplace functional differs
from Sine$_2$ by at most

$$
C_f\left[E_N+(Nt_N)^{-1/2}\right]
\tag{U4}
$$

for all sufficiently large $N$. The constants and startup conditions in
this estimate do not require a minimum initial gap. The centered traceless
Brownian motion has exactly the same **uniform-origin averaged** Laplace
functional as the full motion. We use this equality only for that observable.

The actual map $U_N$ at the unchanged $\tau=10^{-80}$ satisfies FM-007's
bound with $J_N=\lfloor c\log N\rfloor$, $d_N=C N^{-1/40}$.
FM-013 and FLOW-009 give (U1) for $A_N=\Pi U_N$, with a fixed $\kappa_N$.
Put $g_N=4\log J_N/J_N$ and $t_N=8g_N$.
The initial Fourier and potential estimates in FM-017 give
$E_N=O(d_N/g_N+J_N^{-4}/g_N+1/(Ng_N^2))\to0$ and $v_N/t_N\to0$.
In particular $t_N/8=g_N$ is still inside the verified initial strip.
Consequently the reference process from **exactly $\Pi U_N$** has Sine$_2$
at this slower time. FLOW-012 then gives, for $0\le f\in C_c^\infty$,

$$
\mathbb E\Phi_{N,f}(U_{n_N}^{\varepsilon_N})
=\mathcal L_{\mathrm{Sine}_2}(f)+O_f(\sqrt{g_N}),
\quad \varepsilon_N=N^{-9}/\sqrt{t_N},\quad
n_N=\lfloor2t_N^3N^{36}\rfloor.
\tag{U5}
$$

Here the original, **uncentered** coboundary chain starts at $U_N$.
There is no assertion at the faster $t_N=N^{-2/3}$ for this actual family,
and no assertion about its deterministic initial local law. The startup
threshold inherited from FM-013 remains ineffective.

## 2. Exact kernel, sine interpolation, and both heat operators

For now assume distinct initial angles $\alpha_j$ and write $N=2L+1$.
The prior Kieburg--Li--Zhang--Forrester arbitrary-start heat kernel
(arXiv:2012.11993v2, Proposition 12, Theorem 7(3), Proposition 21) has,
up to a determinant-preserving gauge, the following form with respect to
$d\theta/(2\pi)$:

$$
q_j(\phi)=\sum_{m\in\mathbb Z}e^{-tm^2/(2N)}e^{im(\phi-\alpha_j)},
\quad V_{\ell j}=e^{i\ell\alpha_j},\quad -L\le\ell\le L,
$$

$$
R_j(\theta)=\sum_{\ell=-L}^L(V^{-1})_{j\ell}
e^{t\ell^2/(2N)}e^{i\ell\theta},\qquad
K(\theta,\phi)=\sum_jR_j(\theta)q_j(\phi).
\tag{U6}
$$

The source time is $t/(2N)$: the fundamental Casimir in its centered
integer modes is $(L+1)^2-L^2=N$, giving $e^{-t/2}$.
The Fourier pairing is bilinear, $\int R_jq_k=\delta_{jk}$.
No Hermitian pairing or clock initial condition is substituted.

Let $P(z)=\prod_j2\sin((z-\alpha_j)/2)$. The finite centered Lagrange
polynomial is exactly

$$
R_j^0(u)=\sum_{\ell=-L}^L(V^{-1})_{j\ell}e^{i\ell u}
=\prod_{k\ne j}\frac{\sin((u-\alpha_k)/2)}{\sin((\alpha_j-\alpha_k)/2)}
=\frac{P(u)}{2\sin((u-\alpha_j)/2)P'(\alpha_j)}.
\tag{U7}
$$

Both exponential factors in the ordinary polynomial Lagrange formula
cancel when all $N-1=2L$ factors are changed to sines. In particular the
complete sine-product quotient in (U7) retains its displayed sine denominator.
For any real $s$, putting $u=s+iy$, the backward heat formula is

$$
R_j(\theta)=\sqrt{\frac N{2\pi t}}
\int_{\mathbb R}e^{N(u-\theta)^2/(2t)}R_j^0(u)\,dy.
\tag{U8}
$$

It is exact at $s=\theta$ by integrating each finite Fourier mode.
Shifting to any other finite $s$ is allowed by entire analyticity and
Gaussian decay at the horizontal joining ends. Poisson summation gives

$$
q_j(\phi)=\sqrt{\frac{2\pi N}t}
\sum_{k\in\mathbb Z}e^{-N(\phi-\alpha_j+2\pi k)^2/(2t)}.
\tag{U9}
$$

Thus the combined Gaussian prefactor is $N/t$, not $N/(2\pi t)$.

## 3. Exact contour crossing and all windings

Fix $b>0$ and $u$ away from the horizontal boundaries $\Im u=\pm b$.
In a period rectangle $a<\Re z<a+2\pi$, $|\Im z|<b$, use

$$
Q_\phi(z)=\sum_m e^{-tm^2/(2N)}e^{im(z-\phi)},\qquad
\frac{Q_\phi(z)P(u)}{2\sin((u-z)/2)P(z)}.
$$

The vertical boundary contributions cancel: $Q_\phi$ is periodic,
whereas each of $P(z)$ and the sine denominator changes sign under
$z\mapsto z+2\pi$ for odd $N$. The initial-node residues are
$R_j^0(u)Q_\phi(\alpha_j)$. The extra pole at $z=u$ modulo $2\pi$,
when $|\Im u|<b$, has residue **$-Q_\phi(u)$**.
Choose the period endpoints to avoid poles; values at coincident real
nodes are obtained by continuity. The residue theorem is therefore

$$
\sum_jR_j^0(u)q_j(\phi)
=\frac1{2\pi i}\left(\int_{\Im z=-b}-\int_{\Im z=b}\right)
\frac{Q_\phi(z)P(u)}{2\sin((u-z)/2)P(z)}\,dz
+\mathbf1_{|\Im u|<b}Q_\phi(u),
\tag{U10}
$$

where each horizontal integral initially covers one period from left to
right. Substituting the Gaussian winding sum (U9) into these integrals
and shifting each winding unfolds their union to the entire real line.
The sine-product ratio is periodic, so no winding signs are discarded.

Define $\mathcal S(z;\theta)=(z-\theta)^2/(2t)+N^{-1}\log P(z)$
locally off its real zeros; only its derivatives or $P(u)/P(z)$ are used.
Choose any real $s$ and set $u=s+iy$. Equations (U8)--(U10) yield
$K=K_{\rm cross}+K_{\rm rem}$, exactly, with

$$
K_{\rm cross}(\theta,\phi)=\frac Nt
\sum_{k\in\mathbb Z}\int_{-b}^{b}
e^{N[(u-\theta)^2-(u-\phi+2\pi k)^2]/(2t)}\,dy,
\tag{U11}
$$

$$
K_{\rm rem}(\theta,\phi)=\frac{N/t}{2\pi i}
\int_{\mathbb R}dy\left(\int_{\Im z=-b}-\int_{\Im z=b}\right)
\frac{e^{N[\mathcal S(u;\theta)-\mathcal S(z;\phi)]}}
{2\sin((u-z)/2)}\,dz.
\tag{U12}
$$

The two-dimensional integral in (U12) is an ordinary absolutely
convergent integral, including its isolated contour intersections.
Locally its singularity is $1/|u-z|$, integrable in two real dimensions.
The following estimates prove the requisite global absolute convergence.
One may first use (U10) for almost every $y\ne\pm b$ and then integrate;
no principal-value replacement or missing half-residue is used.

## 4. Global Gaussian bounds without initial-gap denominators

Write $F(z)=H_A(e^{iz})$ and $E=E_N$. The same Fourier argument as
FM-017 gives $|F-1|\le E$ for $\Im z\ge t/8$, and $|F+1|\le E$
for $\Im z\le-t/8$. For every $|\Im z|\ge t/4$, the radius-$t/16$
Cauchy circle lies inside the corresponding controlled strip. Hence

$$
|F'(z)|\le16E/t,\quad
\mathcal S'(z;\theta)=(z-\theta)/t-iF(z)/2,
\quad \Re\mathcal S''(z;\theta)\ge(1-8E)/t.
\tag{U13}
$$

This wider strip is needed for the global estimate, not just a derivative
bound at a stationary point. Assume henceforth $E\le1/64$,
$g\le t/8$, $v\le t/512$ and $Nt\ge1$, as holds eventually.
The FM-017 contraction gives conjugate stationary points
$\sigma_\pm(\theta)=s_\theta\pm ib_\theta$, satisfying

$$
|\sigma_+(\theta)-(\theta+it/2)|\le tE/2,
\quad \sigma_+'(\theta)=\frac1{1-itF'(\sigma_+)/2}=1+O(E).
\tag{U14}
$$

Put $A(\theta)=\Re\mathcal S(\sigma_+(\theta);\theta)$.
Reflection makes the lower stationary value have the same real part.
Stationarity yields

$$
|A'(\theta)|=|\Re[(\theta-\sigma_+(\theta))/t]|\le E/2.
\tag{U15}
$$

Take in (U11)--(U12) $s=s_\theta$ and $b=b_\phi$.
The horizontal real action is globally convex by (U13); its derivative
vanishes at $s_\phi$ for either sign of the height. Thus, for all real $x$,

$$
\Re\mathcal S(x\pm ib_\phi;\phi)
\ge A(\phi)+(x-s_\phi)^2/(4t).
\tag{U16}
$$

On each vertical half-strip, the real action is concave in $y$ with
second derivative at most $-1/(2t)$. It is stationary at $\pm b_\theta$:

$$
\Re\mathcal S(s_\theta+iy;\theta)
\le A(\theta)-(y\mp b_\theta)^2/(4t),\quad \pm y\ge t/4.
\tag{U17}
$$

In the remaining $|y|\le t/4$, apply FM-017's potential argument with
(U1)--(U3) and observation angle $s_\theta$. Its bound (M10a) uses only
$g\le t/8$, $v\le t/512$ and gives a loss at least $t/64$ relative to
$y=t/2$. The vertical stationary value is at least that reference value
by (U17). The constant real Gaussian term $(s_\theta-\theta)^2/(2t)$
cancels. Consequently

$$
\Re\mathcal S(s_\theta+iy;\theta)\le A(\theta)-t/64,
\quad |y|\le t/4.
\tag{U18}
$$

All three estimates concern complete sine products. No factor
$P'(\alpha_j)^{-1}$ is estimated separately.

## 5. Integrable crossing pole and uniform remainder

Fix $R$ and $\theta=\theta_0+2\pi x_0/N$,
$\phi=\theta_0+2\pi y_0/N$, $|x_0|,|y_0|\le R$.
Equation (U15) gives $N|A(\theta)-A(\phi)|\le C_RE$, while (U14)
gives $|s_\theta-s_\phi|\le2|\theta-\phi|$ eventually.
Let $w=\sqrt{t/N}\le1$. For each of the two horizontal contours,

$$
\left|\frac1{2\sin((s_\theta+iy-x\mp ib_\phi)/2)}\right|
\le\frac C{\sqrt{\operatorname{dist}(x-s_\theta,2\pi\mathbb Z)^2
+(y\mp b_\phi)^2}}.
\tag{U19}
$$

This follows from $|\sin((r+ia)/2)|^2=\sin^2(r/2)+\sinh^2(a/2)$,
$|\sin(r/2)|\ge|r|/\pi$ for $|r|\le\pi$ and
$|\sinh(a/2)|\ge|a|/2$.

The elementary bound, uniform in the two centers $a,c\in\mathbb R^2$, is

$$
\int_{\mathbb R^2}\frac{e^{-|z-a|^2/(4w^2)}}{|z-c|}\,d^2z\le Cw.
\tag{U20}
$$

Inside the radius-$w$ disk about $c$, bound the exponential by one and
integrate $1/r$. Outside, use $1/|z-c|\le1/w$ and the Gaussian area
$4\pi w^2$. This includes exactly coinciding saddle and crossing pole.

Partition the horizontal line into the cells centered at
$s_\theta+2\pi k$. In the $k=0$ cell apply (U20) with the Gaussian
centers in (U16)--(U17). In each $k\ne0$ cell,
$|x-s_\phi|\ge c|k|$ for large $N$, uniformly in the local window.
Split off half of its Gaussian to obtain $e^{-ck^2/w^2}$, and apply
(U20) to the remaining Gaussian with width $\sqrt2w$.
The cell sum is at most $Cw$.
Both vertical half-strips and both horizontal contours obey this bound.

For the central vertical segment in (U18), the horizontal heights
satisfy $b_\phi\ge3t/8$, so their distance from that segment is at least
$t/8$. Its amplitude is at most $C/t$, its length is $t/2$, and the
horizontal Gaussian integral is $Cw$. Its contribution is bounded by
$Cw e^{-Nt/64}$ before the $N/t$ prefactor. Combining (U15)--(U20) gives

$$
|K_{\rm rem}(\theta,\phi)|\le C_R\sqrt{N/t},
\qquad |K_{\rm rem}(\theta,\phi)|/N\le C_R(Nt)^{-1/2}.
\tag{U21}
$$

The estimate is uniform over every initial spectrum satisfying the
stated finite bounds, regardless of how small its distinct gaps are.

## 6. Crossing residue is the microscopic sine kernel

For the $k=0$ term of (U11), let $\delta=\phi-\theta$. Direct integration
gives, with its continuous value at $\delta=0$,

$$
K_{{\rm cross},0}(\theta,\phi)
=e^{N\delta[s_\theta-(\theta+\phi)/2]/t}
\frac{2\sin(N\delta b_\phi/t)}\delta.
\tag{U22}
$$

At microscopic separation, the exponential is
$1+O_R(E+(Nt)^{-1})$, and $b_\phi/t=1/2+O(E)$.
For $k\ne0$, the real part of the exponent in (U11) is

$$
\frac N{2t}[(s_\theta-\theta)^2-(s_\theta-\phi+2\pi k)^2]
\le-cNk^2/t
$$

eventually. These terms, including their full integration length, are
at most $C_RN e^{-cN/t}$ in sum. Hence (U21)--(U22) prove the uniform
kernel estimate

$$
\sup_{\theta_0,|x_0|,|y_0|\le R}
\left|\frac1N K\left(\theta_0+\frac{2\pi x_0}N,
\theta_0+\frac{2\pi y_0}N\right)
-\frac{\sin\pi(x_0-y_0)}{\pi(x_0-y_0)}\right|
\le C_R[E+(Nt)^{-1/2}].
\tag{U23}
$$

In particular the unfolding is the actual uniform limiting density
$1/(2\pi)$, not an unspecified free-convolution normalization.

## 7. Fredholm series, confluence, and transfer to the original chain

Under the local change of variables, $d\theta/(2\pi)=dx_0/N$;
the factorial densities are determinants of the kernel $K/N$ in (U23).
This kernel need not be Hermitian. Its determinantal representation,
not a positivity assertion for its entries, is the imported finite input.

If $f$ has support in $[-R,R]$, the Laplace expansion has the factors
$1-e^{-f}$ and determinants integrated over this fixed interval.
For large $N$, the entries of $K/N$ and of the sine kernel are bounded
by a fixed $M_R$. Hadamard's inequality and columnwise telescoping give

$$
|\det K_k|\le k^{k/2}M_R^k,
\qquad |\det K_k-\det S_k|
\le k^{k/2+1}M_R^{k-1}\sup|K/N-S|.
\tag{U24}
$$

After multiplication by $(2R)^k/k!$, both bounds are summable over all
$k$. For $k>N$ the finite-rank kernel determinant vanishes; the same
telescoping bound still applies. Thus the full Fredholm series, not just
a fixed two-point function, converges, and (U23)--(U24) give (U4).

For a repeated initial spectrum, approximate its angles by distinct
angles displaced by at most $\gamma$. Their first $J$ moments obey
(U1) with $\kappa_N$ replaced by $\kappa_N+N\gamma$.
For each fixed $N,t$, let $\gamma\downarrow0$; the resulting $E$ and $v$
tend to their original values and obey the same strict finite conditions
for sufficiently small $\gamma$. The constants in (U4) are independent
of the gaps and of $\gamma$. With the same Brownian sample $B_t$, the
matrices $B_tA_N^{\gamma}$ converge to $B_tA_N$.
The compact local Laplace test is a continuous bounded spectral function
on the circle once $N>2R$ (the compact support makes the cut harmless).
Dominated convergence passes (U4) to the repeated spectrum. No limiting
Vandermonde inverse is required. This does not assert a particular
pointwise confluent-kernel gauge; it proves the needed Laplace law.

Decompose the full Brownian motion into its independent traceless and
scalar parts. The scalar part is a common rotation. The observable
$\Phi_{N,f}$ averages the origin uniformly and is exactly invariant under
every common rotation, so its expectation agrees for both Brownian
motions from the same $A_N$.

For the actual centered map, the displayed logarithmic choices satisfy
$E_N+(Nt_N)^{-1/2}=o(\sqrt{g_N})$. The tail in (U2) is at most
$CJ_N^{-4}/g_N$; its other terms are polynomially small in $N$ times
powers of $1/g_N$. Eventually $1/N\le t_N\le1/12$.
With $\varepsilon_N=N^{-9}/\sqrt{t_N}$, the six FLOW-012 comparison
terms are, respectively,

$$
\sqrt{t_N},\quad N^{-1},\quad N^{-5}/\sqrt{t_N},\quad
N^{-9}/t_N,\quad \sqrt{t_N},\quad N^{-8}.
$$

Each is at most a constant times $\sqrt{t_N}$ when $t_N\ge1/N$;
the comparison time $t_N/h_N$ is exactly $2t_N^3N^{36}$.
At $t_N=N^{-2/3}$ this same balancing recovers the earlier
$\varepsilon_N=N^{-26/3}$ and $2N^{34}$ comparison; it does not supply
the missing actual-map Dyson law at that faster time.
This proves (U5) for smooth nonnegative tests and, by fixed smooth
approximation, convergence for nonnegative compact $C^1$ tests.

The result does not compare $U_N$ with its noisy output. It does not
settle the signed Heisenberg hierarchy, uniform integrability for
unbounded correlations of the original chain or deterministic spectrum,
the faster relaxation schedule, or deterministic BGS.
No first-in-literature or prize-level claim is made.
