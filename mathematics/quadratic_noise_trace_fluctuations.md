# Fixed-trace limits and a fixed-time coupling obstruction

**Claim ID: BGS-FLOW-006.** Project proof and author self-review,
29 September 2026. No independent review, formal certificate, or priority
claim. Only the auxiliary diffusions of
[FLOW-003](quadratic_coboundary_noise.md) and
[FLOW-005](quadratic_noise_reversibility.md) are considered.

## 1. Two trace-process limit theorems

Let deterministic $U_N(0)$ satisfy $\sup_N|\operatorname{Tr}U_N(0)^j|<\infty$
for every fixed positive integer $j$. Suppose also that
$p_j(U_N(0))\to z_j$ for $1\le j\le K$. For each fixed $K$ and $T<\infty$,
the first $K$ trace paths of the raw process converge in
$C([0,T],\mathbb C^K)$ to independent complex Ornstein--Uhlenbeck processes

$$
dZ_k=-a_X(k)Z_k\,dt+b_k\,dB_k,\qquad Z_k(0)=z_k,
$$
$$
a_X(k)=k/2-\tfrac12\mathbf1_{k=2},\qquad
b_k^2=k^2(1+\tfrac12\mathbf1_{k=2}). \tag{1}
$$

For the reversible process the same theorem holds with

$$
a_R(k)=k/2+\tfrac12\mathbf1_{k=2} \tag{2}
$$

and the same $b_k$. The independent circular complex Brownian motions
are normalized by $\mathbb E\,dB_kd\bar B_l=\delta_{kl}dt$ and
$\mathbb E\,dB_kdB_l=0$. Fixed moments converge as well.
For zero initial traces, the raw second-trace variance is
$6(1-e^{-t})$, the reversible variance is $2(1-e^{-3t})$,
and all other variances are $k(1-e^{-kt})$.
The stationary variances refer to these limiting OU processes;
no exchange of $N\to\infty$ and $t\to\infty$ is asserted.

## 2. Exact finite-dimensional contractions

Write $p_j=\operatorname{Tr}U^j$, $m_j=p_j/N$, $p_0=N$, and
$p_{-j}=\bar p_j$. Contracting the FLOW-003 covariance tensor gives
for every complex matrix $T$

$$
\mathbb E XTX=\frac{\operatorname{Tr}T}{N}I
-\frac{m_2\operatorname{Tr}(U^*T)U^*+
 \bar m_2\operatorname{Tr}(UT)U}{2N}
-\frac T{N^2}+\frac{U^{*2}TU^2+U^2TU^{*2}}{2N^2}. \tag{3}
$$

For $T=U^l$, the last two terms cancel. Cyclic trace differentiation
therefore yields

$$
\begin{split}
L_Xp_k={}&-\frac{k}{2N}\sum_{l=0}^{k-1}p_lp_{k-l}\\
&+\frac{k}{4N^2}\left[
p_2\sum_{l=0}^{k-1}p_{l-1}p_{k-l-1}
+\bar p_2\sum_{l=0}^{k-1}p_{l+1}p_{k-l+1}\right]. \tag{4}
\end{split}
$$

For $k=2$, the first correction includes $p_2p_0^2/(2N^2)=p_2/2$.
It changes the limiting raw drift from $-p_2$ to $-p_2/2$.
For integers $r,s$, put

$$
Q_{rs}=m_{r+s}-\frac{m_2m_{r+s-2}+m_{-2}m_{r+s+2}}2-m_rm_s
+\frac{m_{s+2}m_{r-2}+m_{s-2}m_{r+2}}2. \tag{5}
$$

This is $\mathbb E[\operatorname{Tr}(XU^r)\operatorname{Tr}(XU^s)]$.
With $\Gamma(f,g)=L(fg)-fLg-gLf$, both processes satisfy

$$
\Gamma(p_k,p_l)=-klQ_{kl},\qquad
\Gamma(p_k,\bar p_l)=klQ_{k,-l},\qquad
\Gamma(p_k,\bar p_k)\le3k^2. \tag{6}
$$

When all fixed nonzero normalized traces vanish, these brackets tend to
$0$ and $b_k^2\delta_{kl}$, respectively. The extra $1/2$ for $k=l=2$
is $m_0m_0/2$ in (5). Discarding this zero-index product would give the
wrong limiting diffusion.

## 3. Uniform moment bounds, including the corrected process

For both processes and every fixed $k,q,T$,

$$
\sup_N\mathbb E\sup_{0\le t\le T}|p_k(U_N(t))|^q<\infty. \tag{7}
$$

The bracket bound (6), applied to real and imaginary parts, gives uniform
Gaussian tails for each trace martingale maximum on $[0,T]$ and hence
all its moments. For the raw drift, (4) gives
$|L_Xp_1|\le|p_1|$ and
$|L_Xp_2|\le2|p_2|+|p_1|^2/N$ using only $|p_j|\le N$.
Gronwall proves (7) first for $k=1$, then for $k=2$.

For the corrected drift let $c=m_2+m_1^2/2$, $d=m_2\bar m_1/2$.
FLOW-005 gives

$$
D_Ap_k=-\frac k2[c p_{k-2}-\bar c p_{k+2}
                    +d p_{k-1}-\bar d p_{k+1}]. \tag{8}
$$

For $k=1,2$, the terms with higher indices are bounded by replacing
those traces with $N$. Since $|p_1|,|p_2|\le N$, this gives
$|L_Rp_1|+|L_Rp_2|\le C(|p_1|+|p_2|)$ with an absolute $C$.
Gronwall on the two-dimensional subsystem and the martingale bounds
prove all base moments together.

For $k\ge3$, (4) contains only a bounded linear coefficient of $p_k$,
polynomials in lower-index traces, and the higher term
$\bar p_2p_1p_{k+1}/N^2$, bounded by $|p_1p_2|/N$.
In (8), replace each $p_{k\pm2}$ and $p_{k\pm1}$ by $N$ if it is not
already lower-index. The result is bounded by a polynomial in
$|p_1|,|p_2|$ with coefficients depending only on $k$.
Induction on $k$, Hölder and Gronwall prove (7) for both processes.
This step precedes every use of asymptotic boundedness of traces.

Using (7) back in (4) and (8) now gives, for $*=X,R$,

$$
\mathbb E\int_0^T|L_*p_k+a_*(k)p_k|\,dt=O_{k,T}(N^{-1}). \tag{9}
$$

For (8) its only order-one term is $-p_2$ when $k=2$; every other
fixed-index product has an inverse power of $N$. Similarly, the brackets
in (6) converge in $L^1$ of the time integral to those in (1).
Only finitely many higher fixed-index moment bounds are needed at each
stage. No uniform statement in a growing $K$ or growing $T$ is made.

## 4. Path-space convergence

Uniform fourth moments for the drifts and (6) imply
$\mathbb E|p_k(t)-p_k(s)|^4\le C_{k,T}|t-s|^2$.
Thus the vectors are tight in continuous-path space. Localize the
martingale identities for the traces and their pairwise products;
(7) allows their expectations to pass to subsequential limits, while
(9) removes the drift error. Each limit solves the linear martingale
problem with rates $a_*(k)$, covariance $b_k^2\delta_{kl}$ and zero
holomorphic covariance. The continuous-martingale characterization
identifies independent circular Brownian drivers. The linear equations
have a unique law, proving (1)--(2). Equation (7) also supplies uniform
integrability for convergence of any fixed moments.

## 5. Fixed-time obstruction to microscopic coupling with Dyson motion

Start at the clock matrices of [FLOW-007](quadratic_noise_clock_limit.md),
so every fixed initial trace is eventually zero. For traceless unitary
Brownian motion $V_t$, exact drift
$L_Dp_2=-(1-2/N^2)p_2-p_1^2/N$ and bracket limit $4$ give second-trace
variance $2(1-e^{-2t})$ by the same moment argument.
For every fixed $t>0$,

$$
6(1-e^{-t})>2(1-e^{-2t}). \tag{10}
$$

No coupling of the raw and Dyson laws can therefore satisfy
$N\|U_t-V_t\|_{\rm op}\to0$ in probability: the deterministic inequality
$|\operatorname{Tr}U^2-\operatorname{Tr}V^2|\le2N\|U-V\|_{\rm op}$
would force their different limiting trace laws to coincide.
The $L^2$ triangle inequality and moment convergence also imply

$$
\liminf_N\inf_{\rm couplings}
 \left(\mathbb E N^2\|U_t-V_t\|_{\rm op}^2\right)^{1/2}
\ge\tfrac12\left[\sqrt{6(1-e^{-t})}-\sqrt{2(1-e^{-2t})}\right]. \tag{11}
$$

This establishes a fixed-time obstruction, not necessity of the
logarithm in FLOW-004's sufficient $t_N\log N\to0$ condition.
The small rank of the covariance correction does not make it negligible
for the unnormalized second trace. The reversible drift restores the
Haar-compatible limiting variance $2$ by changing its relaxation rate.
Neither result proves deterministic BGS, finite-$N$ ergodicity, or
fixed-positive-time local universality.
