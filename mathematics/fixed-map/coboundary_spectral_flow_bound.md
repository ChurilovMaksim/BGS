# Finite coboundary spectral flow: an exact bound and its limitations

**Claim IDs:** BGS-FLOW-001, BGS-FLOW-002. **Status:** finite-dimensional
project proofs, author self-review. All Hilbert--Schmidt norms below
are normalized by the matrix dimension. This note applies to arbitrary
unitary matrices; the hypotheses needed for the prescribed frozen
family are **not** established. It is not a microscopic BGS theorem.

The normal-form operator calculation below is closely related to the
**earlier** Lemma 3 in [pell_coboundary_resonance.md](../pell/pell_coboundary_resonance.md).
The previous lemma already proves a second-order commutator estimate
for the same three exponential factors. The contribution here is the
explicit finite spectral-flow/Birkhoff estimate and its sharpness
example, not the discovery of the second-order normal form.

## Finite spectral-flow bound

Let $U\in U(N)$, $G=G^*$, $B=UGU^*$, and

$$
C=[G,B],\quad H=iNC=H^*,\quad
\eta=\|[G,C]\|_{\rm op}+\tfrac12\|[G-B,C]\|_{\rm op}.
$$

For an integer $T\ge1$, set

$$
v(T)=\left\|\frac1T\sum_{r=0}^{T-1}U^{-r}HU^r
     \right\|_{2,N},\qquad
\|X\|_{2,N}^2=N^{-1}\operatorname{Tr}(X^*X).
$$

Consider $V(t)=e^{it(G-B)}U$. Its eigenphases can be matched
continuously to those of $U$, with a choice through crossings,
so that the unfolded root-mean-square phase displacement

$$
q_N(t):=\left(\frac1N\sum_{j=1}^N
      \left|\frac{N(\theta_j(t)-\theta_j(0))}{2\pi}\right|^2
      \right)^{1/2}
$$

obeys, for **every real** $t$,

$$
\boxed{\quad q_N(t)\le
\frac{t^2}{4\pi}v(T)
+\frac{t^4(T-1)}{16\pi N}\|H\|_{\rm op}^2
+\frac{N|t|^3}{6\pi}\eta.\quad}                    \tag{1}
$$

No spectral gap or simplicity assumption is required in (1).
The formula is an existence statement for a matching, not a
bound for every independent labeling of the eigenvalues.

**Proof.** Put

$$
W(t)=e^{-itG}e^{it(G-B)}e^{itB},\qquad Q(t)=W(t)U.
$$

The identity $e^{itB}U=Ue^{itG}$ shows that
$Q(t)=e^{-itG}V(t)e^{itG}$. Direct differentiation
(the same calculation as in the previous normal-form lemma) gives

$$
W'(t)W(t)^*=-\int_0^t
\operatorname{Ad}_{e^{-itG}e^{iu(G-B)}}C\,du.         \tag{2}
$$

With $Q'(t)=iK_tQ(t)/N$, (2) yields

$$
\|K_t-tH\|_{\rm op}\le N t^2\eta,\qquad
\|Q(t)-U\|_{\rm op}\le\frac{t^2}{2N}\|H\|_{\rm op}.   \tag{3}
$$

The formulas hold for $t<0$ after reversing integration
limits and replacing $t$ by $|t|$ in the bounds.

For any two unitaries $Q,U$, telescoping powers gives

$$
\left\|\frac1T\sum_{r=0}^{T-1}Q^{-r}HQ^r
 -\frac1T\sum_{r=0}^{T-1}U^{-r}HU^r\right\|_{2,N}
\le (T-1)\|H\|_{\rm op}\|Q-U\|_{\rm op}.              \tag{4}
$$

For an eigenbasis of $Q$, averaging $Q^{-r}HQ^r$
preserves each diagonal entry of $H$; their normalized
$\ell^2$ norm is bounded by the normalized Hilbert--Schmidt
norm of the average. Equations (3)--(4) therefore bound
the normalized $\ell^2$ norm of the diagonal entries of
$K_t$ in an instantaneous eigenbasis of $Q(t)$ by

$$
|t|v(T)+\frac{|t|^3(T-1)}{2N}\|H\|_{\rm op}^2
+Nt^2\eta.                                         \tag{5}
$$

On simple-spectrum intervals the eigenphase derivative is that
diagonal entry divided by $N$. At degeneracies, choose a
basis diagonalizing the generator within each degenerate block;
piecewise absolutely continuous eigenphase lifts obey the
same almost-everywhere bound. Multiply by $N/(2\pi)$,
integrate (5), and apply the Minkowski inequality to the
root-mean-square displacement. This gives (1). $\square$

**Conditional use.** Suppose a sequence satisfies
$\|H_N\|_{\rm op}=O(1)$,
$\eta_N=O(N^{-2})$, and
$v_N(\lfloor c\log N\rfloor)=O((\log N)^{-1/2})$.
Then (1) gives $q_N(t_N)\to0$ whenever
$|t_N|=o((\log N)^{1/4})$.
In particular an existing weak local point-process limit with
a uniformly random origin transfers between $U_N$ and
$V_N(t_N)$: a compactly supported $C^1$ test $\phi$
has an expected linear-statistic difference bounded by
$\|\phi'\|_1q_N(t_N)$, using a common uniform origin.
Transfer of arbitrary unbounded correlation moments needs
additional occupancy/uniform-integrability assumptions.
No such three quantitative hypotheses have been proved here
for the actual fixed $U_N$.

Even classical zero mean does not imply the required Birkhoff
decay without a mixing hypothesis. For the nonergodic shear
$F(q,p)=(q+p,p)$ and $g(q,p)=\cos(2\pi q)$,
the observable $\{g,g\circ F\}/(2\pi)$ equals
$\pi[\cos(2\pi p)-\cos(4\pi q+2\pi p)]$.
Its torus average is zero, while its orbitwise Cesàro
average is $\pi\cos(2\pi p)$ for almost every $p$.
This is a control against substituting mean-zero for
the adjoint Birkhoff hypothesis, not a claim about the
mixing classical map of the fixed BGS model.

## Sharpness of the leading coefficient

Let $m\to\infty$ through odd integers, $N=2m^2$, and
$U=\operatorname{diag}(e^{2\pi ij/N})_{0\le j<N}$.
Let $P=P^*=P^{-1}$ exchange every even $j$ with
$j+m\pmod N$, an odd index, and put $G=N^{-1/2}P$.
Within each two-dimensional pair
$\delta=2\pi m/N=\pi/m$.
The above $H$ is diagonal with entries $\pm2\sin\delta$;
thus $v(T)=2\sin\delta$ for every $T$, and direct
commutator bounds give $\eta=O(N^{-2})$.

Take $t=cN^{1/4}$ with fixed $0<c<1/\sqrt2$.
The old paired half-angle is $\alpha=\delta/2$;
the new half-angle $\beta$ satisfies the exact $2\times2$
identity

$$
\cos\beta=\cos\alpha\,
  \cos\!\left(2tN^{-1/2}\sin\alpha\right),\qquad
\frac{N(\beta-\alpha)}{2\pi}\longrightarrow\frac{c^2}{\sqrt2}.
$$

For example $c=1/2$ keeps shifts below a quarter of
a mean gap for large $N$; the nearest gaps approach
$1\pm\sqrt2c^2$, hence are not clock gaps.
At $T=1$ the first term on the right of (1) tends
to exactly $c^2/\sqrt2$, and its other two terms
tend to zero. Thus its leading coefficient $1/(4\pi)$
is asymptotically attained. This is an **abstract**
control sequence, not the prescribed fixed BGS model.

## Why a coboundary kick does not create Dyson diffusion

For a simple spectrum of $U$, put $A_G=G-UGU^*$
and write $G_{jk}$ in the eigenbasis of $U$. The
general eigenphase derivative formulas already in
[frozen_spectral_flow_controls.md](frozen_spectral_flow_controls.md)
give

$$
\dot\theta_j(0)=0,\qquad
\ddot\theta_j(0)=2\sum_{k\ne j}
|G_{jk}|^2\sin(\theta_j-\theta_k).                    \tag{6}
$$

Indeed $(A_G)_{jk}=(1-e^{i(\theta_j-\theta_k)})G_{jk}$;
the squared factor cancels the cotangent singularity
in the general formula. This regular sine drift is
qualitatively different from the cotangent interaction
in circular Dyson Brownian motion.

For a GUE-distributed $G$, normalized by
$\mathbb E|G_{jk}|^2=1/N$ for $j\ne k$,
take the expectation of the coefficient of $t^2$
in a smooth spectral test $F$. Its first derivative
along each deterministic coboundary path vanishes,
so its formal second-order operator is first order:

$$
\mathcal K F
  =\frac1N\sum_{j,k}\sin(\theta_j-\theta_k)
                          \,\partial_{\theta_j}F.    \tag{7}
$$

It contains no Hessian in the phase variables and is zero
when $\operatorname{Tr}U=0$. In particular an
independent Gaussian choice of a coboundary generator
does not by itself supply radial Dyson diffusion.

As an independent check of the coefficient in (7), the
complete GUE covariance gives

$$
\mathbb E[G,UGU^*]
  =\frac{(\operatorname{Tr}U)U^*
          -(\operatorname{Tr}U^*)U}{N}.
$$

The inverse of $G\mapsto G-UGU^*$ on off-diagonal
matrix units divides by $1-e^{i(\theta_j-\theta_k)}$
and is singular near collisions; its diagonal is zero.
This identifies precisely why unconstrained additive
noise cannot be represented by a controlled
coboundary without new gap and inverse bounds.
