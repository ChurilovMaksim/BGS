# Quantitative coupling of quadratic noise and unitary Brownian motion

**Claim ID: BGS-FLOW-004.** Project proof and author self-review, 29 September
2026. No independent review, formal certificate, or priority claim. This
compares two added stochastic processes, not either process with its
deterministic initial spectrum.

## 1. Objects and statements

Use the centered noise and covariance $\mathcal C_U$ of
[BGS-FLOW-003](quadratic_coboundary_noise.md):

$$
X=\frac{i}{\sqrt2}[G,UGU^*]-\mathbb E\frac{i}{\sqrt2}[G,UGU^*],
\qquad \mathbb E G_{ab}G_{cd}=N^{-1}\delta_{ad}\delta_{bc}.
$$

Let $\mathcal H_0$ be the real Hilbert space of traceless Hermitian matrices,
with inner product $\operatorname{Tr}(TS)$, and let $E_a$ be an orthonormal
basis. The raw diffusion has the frozen-coefficient generator

$$
L_XF(U)=\frac12\mathbb E\left.\frac{d^2}{ds^2}
 F(e^{isX(U,G)}U)\right|_{s=0}.
$$

Put $p_j=\operatorname{Tr}U^j$, $m_j=p_j/N$. There is a coupling of this
diffusion $U_t$ with normalized traceless unitary Brownian motion $V_t$,
starting at any common $U_0$, such that, for $S_0=|m_1(U_0)|^2+|m_2(U_0)|^2$,

$$
\mathbb E\|U_t-V_t\|_{\rm HS}^2
\le \frac{(2NS_0+10/N)(e^{3t}-1)}3-\frac{8t}N. \tag{1}
$$

In particular, for $0\le t\le1$,

$$
N\mathbb E\|U_t-V_t\|_{\rm HS}^2
\le10e^3t(1+|p_1(U_0)|^2+|p_2(U_0)|^2). \tag{2}
$$

For fixed $K>0$, if $N\ge K$ and $\max(|p_1(U_0)|,|p_2(U_0)|)\le K/2$,
the stronger conclusion is

$$
t_N\log N\longrightarrow0
\quad\Longrightarrow\quad
N\|U_{t_N}-V_{t_N}\|_{\rm op}\xrightarrow{\mathbb P}0. \tag{3}
$$

Multiplicities and singular covariances are allowed. No occupancy or
minimum-gap hypothesis is imposed.

## 2. Construction and exact cancellation

Set $K_a(U)=\mathcal C_U^{1/2}E_a$, $B_a=E_a/\sqrt N$,
$R_a=K_a-B_a$, and $Q_K=\sum_aK_a^2$, $Q_R=\sum_aR_a^2$.
The coupled Itô equations are

$$
dU=i\sum_aK_a(U)U\,dW_a-\tfrac12Q_K(U)U\,dt,\qquad
dV=i\sum_aB_aV\,dW_a-\tfrac12(1-N^{-2})V\,dt.
$$

They are Itô equations from the outset; no derivative of a
state-dependent Stratonovich coefficient has been omitted.
The real matrix representing $\mathcal C_U^{1/2}-I/\sqrt N$ is symmetric,
so pairing its entries against $[E_a,E_b]$ gives

$$
\sum_a[B_a,R_a]=0.
$$

For $Z=V^*U$, the mixed Itô drift therefore reduces exactly to

$$
dZ=i\sum_a(V^*R_aV)Z\,dW_a-\tfrac12(V^*Q_RV)Z\,dt. \tag{4}
$$

A smooth factorization establishes existence even when the square root is
not Lipschitz. On the full Hermitian basis $F_r$, put

$$
Q_{rs}(U)=\frac{i}{2\sqrt2N}
 ([F_r,UF_sU^*]+[F_s,UF_rU^*]).
$$

The centered quadratic Gaussian expansion gives
$\mathcal C_U=2\sum_{rs}Q_{rs}\otimes Q_{rs}$. It produces a smooth
finite-dimensional Itô equation on the compact determinant coset.
If its Hermitian driving martingale is $\mathsf K$, adjoin independent
Brownian motion $\beta$ and set

$$
dW=\mathcal C_U^{+1/2}d\mathsf K+
 (I-P_{\operatorname{range}\mathcal C_U})d\beta.
$$

The first integrand has bracket $P_{\operatorname{range}\mathcal C_U}\,dt$,
so is integrable despite a possibly unbounded pseudoinverse.
The resulting $W$ is Brownian and $d\mathsf K=\mathcal C_U^{1/2}dW$.
This gives the required weak coupling. Both equations preserve unitarity
and determinant.

## 3. Residual covariance bounds

On $\mathcal H_0$ write $\mathcal C_U=I/N+D+R$, with

$$
D(T)=-N^{-1}P_0\operatorname{Re}(m_2U^*P_0(T)U^*),\qquad
R=N^{-2}\sum_{H=\operatorname{Re}U^2,\operatorname{Im}U^2}
 (P_0H)\otimes(P_0H).
$$

Here $P_0$ removes the trace. We have $\|D\|\le |m_2|/N$,
$R\ge0$, $\operatorname{rank}R\le2$, and
$\operatorname{Tr}_{\mathcal H_0}R=(1-|m_2|^2)/N$.
The scalar inequality
$(\sqrt\lambda-N^{-1/2})^2\le N(\lambda-N^{-1})^2$
and the triangle-square inequality yield

$$
\operatorname{Tr}Q_R\le2N|m_2|^2+2/N. \tag{5}
$$

There is also an operator bound:

$$
\|Q_R\|_{\rm op}\le2|m_2|^2+2/N^2. \tag{6}
$$

To prove it, diagonalize $U=\operatorname{diag}(z_j)$.
Each off-diagonal real Hermitian block has covariance eigenvalue
$v_{jk}=(1-\operatorname{Re}(m_2/(z_jz_k)))/N$.
Its contribution to $(Q_R)_{jj}$ is
$(\sqrt{v_{jk}}-N^{-1/2})^2\le |m_2|^2/N$.
On diagonal matrices let $P=I-\mathbf1\mathbf1^T/N$.
The radial covariance $\Sigma$ annihilates $\mathbf1$, and

$$
\Delta_{jk}:=(\Sigma-P/N)_{jk}
=-\frac{\delta_{jk}}N\operatorname{Re}(m_2z_j^{-2})
 +\frac{\cos(2(\theta_j-\theta_k))}{N^2}.
$$

On $\operatorname{range}P$,
$(\sqrt\Sigma-P/\sqrt N)^2\le N\Delta^2$.
Its $j$th diagonal entry is at most
$2|m_2|^2/N+2/N^2$. Add the $N-1$ off-diagonal contributions.
Continuity handles repeated phases.

## 4. Low traces and the Hilbert–Schmidt estimate

Direct contraction of the covariance gives

$$
L_Xm_1=-m_1/2+m_2\bar m_1/4+|m_2|^2m_1/4,
$$
$$
L_Xm_2=-m_2/2-m_1^2+
 \tfrac12[m_2|m_1|^2+\bar m_2(m_1m_3+m_2^2)].
$$

The covariance upper bound gives
$\Gamma(m_k,\bar m_k)\le3k^2/N^2$, where
$\Gamma(f,g)=L_X(fg)-fL_Xg-gL_Xf$.
Using $|m_j|\le1$ in the displayed drifts, one obtains for
$S=|m_1|^2+|m_2|^2$

$$
L_XS\le3S+15/N^2,\qquad
\mathbb ES_t\le e^{3t}S_0+5(e^{3t}-1)/N^2.
$$

Equation (4), unitarity and $Q_R\ge0$ imply
$\frac d{dt}\mathbb E\|Z-I\|_{\rm HS}^2
\le\mathbb E\operatorname{Tr}Q_R$. Integrating (5) proves (1);
bounding $e^{3t}-1\le3e^3t$ gives (2).

## 5. Every even matrix moment and the stronger time window

Stop at $\sigma=\inf\{t:\max(|p_1(U_t)|,|p_2(U_t)|)\ge K\}$.
Before stopping the two drifts have modulus at most $3K$ and the trace
martingales have brackets at most $12\,dt$. Applying the scalar exponential
martingale inequality to real and imaginary parts gives, for $t\le1/12$,

$$
\mathbb P(\sigma\le t)\le8e^{-K^2/(768t)}. \tag{7}
$$

On this interval (4) reads $Z-I=M+D_0$, where both quadratic variations of
$M$ are bounded by $vI\,dt$, $v=2(K^2+1)/N^2$, and
$\|D_0\|_{\rm op}\le vt/2$.

For any complex matrix martingale with these two bracket bounds,

$$
\mathbb E\operatorname{Tr}(M_t^*M_t)^p
\le N(2p-1)!!(vt)^p,\qquad p=1,2,\ldots. \tag{8}
$$

Indeed its Hermitian dilation $Y=\left(\begin{smallmatrix}0&M\\M^*&0\end{smallmatrix}\right)$
has Hermitian coefficients $A_a$ with $\sum A_a^2\le vI$.
Trace Itô differentiation gives
$f_p'\le p\sum_{i=0}^{2p-2}\mathbb E\sum_a
\operatorname{Tr}(Y^iA_aY^{2p-2-i}A_a)$.
In an eigenbasis of $Y$, with $q=2p-2$, weighted Young's inequality and
Hermiticity give

$$
\left|\sum_a\operatorname{Tr}(Y^iA_aY^{q-i}A_a)\right|
\le \sum_{a,j,k}|\lambda_j|^i|\lambda_k|^{q-i}|(A_a)_{jk}|^2
\le v\operatorname{Tr}|Y|^q.
$$

Thus $f_p'\le p(2p-1)vf_{p-1}$, $f_0=2N$; induction and
$\operatorname{Tr}Y^{2p}=2\operatorname{Tr}(M^*M)^p$ prove (8).
Localization justifies the argument before moments are known to be finite.
For $p=\lceil\log(2N)+x\rceil$ and $x\ge0$, Markov's inequality yields

$$
\begin{split}
\mathbb P\bigl(N\|U_t-V_t\|_{\rm op}>
 2\sqrt{e(K^2+1)tp}+(K^2+1)t/N\bigr)
\le8e^{-K^2/(768t)}+\tfrac12e^{-x}. \tag{9}
\end{split}
$$

Taking $x=\log N$ proves (3). The earlier fourth-moment bound is the
$p=2$ special case and requires the narrower $t=o(N^{-1/2})$.
When $\|U-V\|_{\rm op}<2$, write $V=Ue^{iH}$ with
$\|H\|_{\rm op}=2\arcsin(\|U-V\|_{\rm op}/2)$.
Along this path continuous eigenangles have speeds at most $\|H\|_{\rm op}$.
Approximation handles collisions. Equation (3) therefore matches all
levels with maximum unfolded displacement tending to zero.

## 6. Phase-averaged local laws without occupancy assumptions

For $f\ge0$ in $C_c^1(\mathbb R)$ let $\Phi_{N,f}(U)$ be the Laplace
functional of the unfolded spectrum viewed from an independent uniform
angle $\alpha\in[0,2\pi)$:

$$
\Phi_{N,f}(U)=\frac1{2\pi}\int_0^{2\pi}
 \exp\!\left[-\sum_{j=1}^N\sum_{\ell\in\mathbb Z}
 f\!\left(\frac N{2\pi}(\theta_j-\alpha+2\pi\ell)\right)\right]d\alpha.
$$

For any two unitary matrices,

$$
|\Phi_{N,f}(U)-\Phi_{N,f}(V)|
\le \frac{\|f'\|_1}{4}\sqrt N\|U-V\|_{\rm HS}. \tag{10}
$$

For orthonormal eigenbases set $w_{jk}=|\langle e_j,h_k\rangle|^2$.
Its row and column sums equal one and
$\|U-V\|_{\rm HS}^2=\sum w_{jk}|z_j-\zeta_k|^2$.
The integrated difference of two translated periodizations is at most
$\delta_{jk}\|f'\|_1/(2\pi)$, with $\delta_{jk}$ the shortest angular distance.
Use $|e^{-a}-e^{-b}|\le|a-b|$ for $a,b\ge0$,
$\delta_{jk}\le\pi|z_j-\zeta_k|/2$, and Cauchy–Schwarz to obtain (10).
Combining it with (2) gives

$$
|\mathbb E\Phi_{N,f}(U_t)-\mathbb E\Phi_{N,f}(V_t)|
\le\frac{\|f'\|_1}4
 \sqrt{10e^3t(1+|p_1(U_0)|^2+|p_2(U_0)|^2)}. \tag{11}
$$

The same argument with interval indicators, of total variation two,
couples any fixed vector of $q$ interval counts with total-variation
distance at most $q\sqrt{10e^3t(1+|p_1|^2+|p_2|^2)}/2$.
This concerns count vectors, not full configuration laws.
If $t_N(1+|p_1|^2+|p_2|^2)\to0$, unit mean intensity gives local
tightness and (11) identifies all subsequential weak limits.
Unbounded correlation moments require additional uniform integrability.

## 7. Boundary and model input

These results neither prove Dyson relaxation for an arbitrary starting
spectrum nor remove the added noise. The [clock theorem](quadratic_noise_clock_limit.md)
and [trace fluctuation theorem](quadratic_noise_trace_fluctuations.md)
make both restrictions concrete.
The [fixed-time source adaptation](quadratic_noise_fixed_time_input.md)
records separately what is needed to apply the bounded-trace hypothesis
to the maintained quantum map.
