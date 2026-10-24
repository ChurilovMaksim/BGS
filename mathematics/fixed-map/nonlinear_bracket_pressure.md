# Pressure growth of nonlinear brackets in the fixed frozen model

**Claim ID:** `BGS-FM-006`. **Status:** project proof, checked against the
primary thermodynamic-formalism sources and independently reassembled exact
Fourier arithmetic; author-level self-review only. The underlying quantitative
Anosov and fixed-point inputs are `BGS-FM-001`. This is a classical dynamical
result, not a Heisenberg-time trace estimate, a priority claim, or BGS.

## 1. The statement

Fix the exact ordinary-midpoint symbol $g$ in
[`fixed_model_symmetry_theorem.md`](fixed_model_symmetry_theorem.md), its
Hamiltonian vector field $X_g=(g_p,-g_q)$, and

$$
S=\begin{pmatrix}3&4\\2&3\end{pmatrix},\quad
\lambda=3+2\sqrt2,\quad G_\kappa=S\circ\Phi_g^\kappa.
$$

Let $m$ be normalized area measure, $E^u_\kappa$ the one-dimensional
unstable bundle, and
$\phi_\kappa(x)=\log\|DG_\kappa(x)|_{E^u_\kappa(x)}\|$ for any fixed
Riemannian metric. Write $P_\kappa$ for topological pressure of $G_\kappa$.
Changing the metric changes $\phi_\kappa$ by a continuous coboundary, so
$P_\kappa(\phi_\kappa)$ is well defined.

**Theorem 1 (actual nonlinear map).** For every real
$0<|\kappa|\le10^{-12}$, there are constants $0<c_\kappa<C_\kappa<\infty$
and $r_\kappa$ such that, for all integers $r\ge r_\kappa$,

$$
c_\kappa e^{rP_\kappa(\phi_\kappa)}\le
\left\|\frac{\{g,g\circ G_\kappa^r\}}{4\pi}\right\|_{L^2(m)}^2
\le C_\kappa e^{rP_\kappa(\phi_\kappa)}.                 \tag{1}
$$

Moreover,

$$
P_\kappa(-\phi_\kappa)=0,\qquad
P_\kappa(0)=\log\lambda,\qquad
P_\kappa(\phi_\kappa)>2\log\lambda.                    \tag{2}
$$

Consequently the exponent

$$
\delta_\kappa:=\lim_{r\to\infty}\frac1r\log
 \left\|\lambda^{-r}\frac{\{g,g\circ G_\kappa^r\}}{4\pi}\right\|_2
=\frac{P_\kappa(\phi_\kappa)-2\log\lambda}{2}>0.     \tag{3}
$$

The choice $\kappa=\tau/(2\pi)$, $\tau=10^{-80}$, is exactly the prescribed
frozen quantum family's classical parameter. Its Egorov map is
$F_\tau=G_{\tau/(2\pi)}^{-1}$. Symplectic invariance and invariance of $m$
give, **for each $r$ without asymptotics**,

$$
\|\{g,g\circ F_\tau^r\}\|_2
=\|\{g,g\circ G_{\tau/(2\pi)}^r\}\|_2.          \tag{4}
$$

In particular the *upper* Bessel/Riesz bound with the linear factor
$\lambda^{-r}$ from [`frozen_full_lag_resonance.md`](../resonance-cohomology/frozen_full_lag_resonance.md)
fails for this nonlinear map: select a single lag $r$ in any purported
uniform upper estimate. This says nothing by itself about a different
pressure-adapted normalization or about quantum traces.

**Perturbative coefficient.** As $\kappa\to0$ through real values,

$$
P_\kappa(\phi_\kappa)-2\log\lambda
=\kappa^2\mathcal V+O(\kappa^3),\qquad
\mathcal V=\frac{\pi^4}{2}\frac{7834656061}{500000}>0. \tag{5}
$$

The $O(\kappa^3)$ constant and its effective range have not been bounded;
(5) **does not** certify a decimal value of $\delta_\kappa$ at the fixed
$\tau=10^{-80}$. Strict positivity at that parameter follows independently
from (2), not by discarding the remainder in (5).

## 2. Weighted endpoint lemma and bracket norm

We prove the required implication rather than treating a general pressure
growth slogan as a theorem. Let $F$ be a $C^{2+\alpha}$, area-preserving,
topologically mixing Anosov diffeomorphism of $\mathbb T^2$ topologically
conjugate to $S$, and put $\phi=\log\|DF|_{E^u}\|$. Ruelle's entropy
inequality gives $h_\nu(F)\le\int\phi\,d\nu$ for each invariant $\nu$.
Pesin's entropy formula gives equality for the invariant smooth area $m$.
The variational principle therefore gives $P_F(-\phi)=0$, and uniqueness of
the equilibrium state for a Hölder potential identifies $m=\mu_{-\phi}$.

Choose a mixing Markov coding. For each admissible symbolic word $C$ of
length $r$, the Gibbs estimates for the two Hölder potentials $-\phi$ and
$\phi$ (and bounded distortion of $S_r\phi=\sum_{j=0}^{r-1}\phi\circ F^j$)
give uniform constants independent of the word and $r$ such that

$$
m(C)\asymp e^{-S_r\phi(x)},\qquad
\mu_\phi(C)\asymp e^{S_r\phi(x)-rP_F(\phi)},\qquad x\in C.
$$

Thus $\int_C e^{2S_r\phi}\,dm\asymp
e^{rP_F(\phi)}\mu_\phi(C)$. Markov boundary ambiguities have zero Gibbs
measure; equivalently these comparisons can be made first on the two-sided
coding and then projected. Summing over words yields

$$
\int e^{2S_r\phi}\,dm\asymp e^{rP_F(\phi)}.             \tag{6}
$$

For *any* nonempty open sets $V,W$, select two finite symbolic cylinders
whose projected interiors lie in $V,W$. Enlarging the word length at either
end changes the constants but not the exponent. The Gibbs comparison and
mixing of $\mu_\phi$ then give, for all sufficiently large $r$,

$$
\int_{V\cap F^{-r}W}e^{2S_r\phi}\,dm
\ge c(V,W)e^{rP_F(\phi)}.                       \tag{7}
$$

This is the endpoint estimate needed for an $L^2$ *lower* bound; (6) alone
would not rule out an observable that vanishes on the pressure-contributing
trajectories.

Let $e_s,e_u$ be local unit stable and unstable fields, $J_s^{(r)}$ and
$J_u^{(r)}$ their absolute derivative expansions, and
$D=|\det(e_s,e_u)|$, bounded away from zero. The bracket of two $C^1$
observables $f,k$ is, up to an overall orientation sign,

$$
\{f,k\circ F^r\}(x)=D(x)^{-1}\left[
  df_x(e_s)J_u^{(r)}(x)\,dk_{F^rx}(e_u)
 -df_x(e_u)J_s^{(r)}(x)\,dk_{F^rx}(e_s)\right].       \tag{8}
$$

Here $J_u^{(r)}=e^{S_r\phi}$ and $J_s^{(r)}$ contracts uniformly.
For nonconstant $f$, $df(e_s)$ cannot vanish identically: otherwise $f$
would be constant on each stable leaf, and these leaves are dense because
the conjugacy carries them to the irrational stable lines of $S$. Likewise
$dk(e_u)$ is nonzero on an open set for every nonconstant $k$. Choose $V,W$
on which the respective absolute derivatives have positive lower bounds.
For all large $r$, the stable term in (8) is smaller than half the unstable
term on $V\cap F^{-r}W$. Equation (7) gives the lower bound, while (6)
and bounded derivatives give the upper bound:

$$
\|\{f,k\circ F^r\}\|_2^2\asymp e^{rP_F(\phi)}.       \tag{9}
$$

Theorem 1 follows on taking $F=G_\kappa$, $f=k=g$. For (4), compose the
bracket for $G^{-r}$ with $G^r$ and use
$\{a,b\}\circ G^r=\{a\circ G^r,b\circ G^r\}$ to obtain
$\{g,g\circ G^{-r}\}\circ G^r=-\{g,g\circ G^r\}$.

## 3. Strict pressure gap for every allowed nonzero kick

The internal theorem `BGS-FM-001` gives Anosov dynamics, conjugacy to $S$,
and exactly four fixed points $(q,p)\in\{0,1/2\}^2$. At each one, the
Hamiltonian vector field vanishes and $g_{pp}=g_{pq}=0$. Hence $DX_g$ is
nilpotent there and the derivative-trace formula is **exact**:

$$
\operatorname{tr}DG_\kappa(q,p)
=6-4\kappa\,g_{qq}(q,p),\quad
\frac{g_{qq}(q,p)}{\pi^2}
=-\frac{19606}{125},-\frac{19594}{125},
  \frac{24306}{125},\frac{24894}{125},                 \tag{10}
$$

in the order $(0,0),(0,1/2),(1/2,0),(1/2,1/2)$. For nonzero $\kappa$
these give distinct positive unstable multipliers (the traces stay $>2$
throughout the stated range). A potential cohomologous to a constant must
take the same value at every fixed point, so $\phi_\kappa$ is not one.
Strict convexity of $t\mapsto P_\kappa(t\phi_\kappa)$ then implies

$$
2P_\kappa(0)<P_\kappa(-\phi_\kappa)+P_\kappa(\phi_\kappa).
$$

Topological conjugacy gives $P_\kappa(0)=h_{\rm top}(S)=\log\lambda$;
Section 2 supplies $P_\kappa(-\phi_\kappa)=0$. This proves (2).

## 4. First derivative of the unstable potential

This step does **not** assume a differentiable structural conjugacy. For a
small enough real $\kappa$, let $h_\kappa=\mathrm{id}+u_\kappa$ be the
near-identity lift solving $h_\kappa S=G_\kappa h_\kappa$. Choose any small
$0<\beta<1$ and an adapted norm for $S$. The linear operator
$\mathcal L u=u\circ S-Su$ has a bounded inverse on $C^\beta$: its unstable
and stable components are respectively

$$
(\mathcal L^{-1}a)^u(x)
=-\sum_{j\ge0}\lambda^{-j-1}a^u(S^jx),\qquad
(\mathcal L^{-1}a)^s(x)
=\sum_{j\ge1}\lambda^{-(j-1)}a^s(S^{-j}x).       \tag{11}
$$

The $C^\beta$ norms converge geometrically since
$\lambda^{\beta-1}<1$. The smooth periodic perturbation
$R_\kappa(z)=G_\kappa(z)-Sz$ has $\|R_\kappa\|_{C^2}=O(|\kappa|)$.
Consequently
$u\mapsto\mathcal L^{-1}R_\kappa(\mathrm{id}+u)$ contracts a
$C^\beta$ ball of radius $O(|\kappa|)$: the composition difference has
$C^\beta$ Lipschitz constant $O(|\kappa|)$ on that ball. Thus
$\|u_\kappa\|_{C^\beta}=O(|\kappa|)$; uniqueness identifies this fixed
point with the structural conjugacy.

Let $v_u=(\sqrt2,1)$ and $w_u=(1,\sqrt2)/(2\sqrt2)$ so that
$Sv_u=\lambda v_u$, $w_uS=\lambda w_u$, $w_uv_u=1$. Pull
$DG_\kappa$ back by $h_\kappa$. In the eigenbasis of $S$, the invariant
unstable line has slope $t_\kappa=O(\kappa)$ in a possibly smaller
$C^\gamma$ space, $0<\gamma<\beta$: the graph transform at $\kappa=0$
is $t(x)\mapsto\lambda^{-2}t(S^{-1}x)$, with operator norm at most
$\lambda^{\gamma-2}<1$. The unstable expansion factor with the
normalization $w_u(v_u+t_\kappa v_s)=1$ is

$$
a_\kappa(x)
=w_uDG_\kappa(h_\kappa x)(v_u+t_\kappa(x)v_s).
$$

Both matrix and slope expansions in $C^\gamma$ yield

$$
\psi_\kappa:=\log a_\kappa-\log\lambda
=\kappa b+O(\kappa^2),\qquad
b(x)=w_uDX_g(x)v_u
=\frac{g_{pp}(x)-2g_{qq}(x)}{2\sqrt2}.           \tag{12}
$$

The norm-defined $\phi_\kappa\circ h_\kappa$ differs from
$\log a_\kappa$ by a coboundary (the logarithm of the norm of the chosen
unstable section). Hence, with $P_S(0)=\log\lambda$,

$$
P_\kappa(\phi_\kappa)-2\log\lambda
=P_S(\psi_\kappa)+P_S(-\psi_\kappa)-2P_S(0).     \tag{13}
$$

Here we used $P_\kappa(-\phi_\kappa)=0$, which is equivalent to
$P_S(-\psi_\kappa)=\log\lambda$. Analyticity of pressure for Hölder
potentials and cancellation of its odd derivatives in (13) give

$$
P_\kappa(\phi_\kappa)-2\log\lambda
=\kappa^2 D^2P_S(0)[b,b]+O(\kappa^3).          \tag{14}
$$

The unique maximal-entropy measure of $S$ is Haar measure. Since
$\int b\,dm=0$, the pressure Hessian is its asymptotic variance,
$D^2P_S(0)[b,b]=\sum_{n\in\mathbb Z}\int b(x)b(S^nx)\,dm(x)$.

## 5. Exact arithmetic of the variance and audit boundary

Use $A=S^{\mathsf T}$ and write
$g(x)=\sum_v\widehat g(v)e^{2\pi i v\cdot x}$. Define the invariant
quadratic form

$$
q(k,\ell)=\det((k,\ell),A(k,\ell))=4k^2-2\ell^2.
$$

Then $\widehat b(v)=(\pi^2/\sqrt2)q(v)\widehat g(v)$, and exact
Fourier orthogonality gives

$$
\frac2{\pi^4}\int b(x)b(S^nx)\,dm(x)
=\sum_{v}q(v)^2\widehat g(v)\widehat g(-A^nv).    \tag{15}
$$

The correct midpoint symbol has 32 nonzero modes, with $|\ell|\le1$.
For each such mode $v$, the second dual iterate $A^2v$ has coordinates
of equal sign and $|(A^2v)_2|\ge7$; further positive iterates only
increase this second-coordinate magnitude. Thus the right side of (15)
vanishes **for all** $n\ge2$, by a support argument rather than finite
sampling. The exact values for $n=0,1$ are

$$
\frac2{\pi^4}\int b^2\,dm=\frac{313386243}{20000},\qquad
\frac2{\pi^4}\int b(x)b(Sx)\,dm=-\frac7{500000}.
$$

Negative lags equal positive lags by invariance of $m$. This proves
$\mathcal V=(\pi^4/2)(7834656061/500000)$ in (5). The independent
trigonometric expansion and all rational checks are implemented in
[`nonlinear_pressure_variance.py`](../../computations/verification/nonlinear_pressure_variance.py).
At the four fixed points it also reproduces the exact $g_{qq}$ values
in (10). Code checks only this finite algebra; Sections 2–4 supply the
asymptotic proof. No Lean compilation, external referee review, or
global novelty determination is claimed.

## Primary-source dependency map

- [Pesin (1977), *Characteristic Lyapunov exponents and smooth ergodic
  theory*, Theorem 5.1, printed p. 81 / PDF p. 26](https://www.mathnet.ru/php/getFT.phtml?jrnid=rm&paperid=3219&what=fullteng): entropy formula for invariant smooth volume.
- [Ruelle (1978), *An inequality for the entropy of differentiable maps*,
  Theorem 2](https://www.ihes.fr/~ruelle/PUBLICATIONS/%5B51%5D.pdf): entropy upper bound for arbitrary invariant measures.
- [Parry--Pollicott (1990), *Zeta functions and the periodic orbit structure
  of hyperbolic dynamics*](https://smf.emath.fr/system/files/filepdf/AST_1990__187-188__1_0.pdf): Appendix III, Markov coding; Theorem 2.2 and Chapter 3, Gibbs estimates and variational principle; Propositions 4.7, 4.11, 4.12, analyticity, pressure variance and strict convexity. Passing from their mixing symbolic model to the Anosov diffeomorphism uses its Markov coding, with boundary sets of equilibrium measure zero.

These are pre-existing thermodynamic-formalism results. The model-specific
pressure computation and the precise failure of the linear normalization
are the present project's application. No checked source establishes the
missing `BGS-TRACE-005` joint-trace estimate.
