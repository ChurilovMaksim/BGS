# Uniform classical displacement density and a logarithmic spectral comparison

**Claim:** BGS-TRACE-112. **Status:** analytic proof with self-review,
21 October 2026. This supplies an independent proof of the upper spectral
distance bound in TRACE-110, without its all-time quantum trace/pressure input.
It does not estimate microscopic spacings. The anisotropic Fourier method
is standard; no literature-priority claim is made.

Final dependency and cross-surface self-review: 22 October 2026.

## 1. A uniform density for the actual classical displacement

Let $\Psi=\phi_{-a}^{t_*}\circ L$ be the actual ordinary-half classical
map of the fixed family, with $t_*=10^{-80}/(2\pi)$ and
$L=\left(\begin{smallmatrix}3&-4\\-2&3\end{smallmatrix}\right)$.
For uniform classical area $dx$ on $\mathbb T^2$, define the probability
measure $\nu_m=(x\mapsto\Psi^m x-x)_*dx$, where subtraction is on the torus.
There are $\epsilon_R<10^{-56}$, $\vartheta=1-1/8000<1$ such that every $\nu_m$,
$m\ge1$, has a continuous density $q_m$ satisfying

$$
\|q_m-1\|_\infty\le\epsilon_R m\vartheta^{m-1}
\le8\cdot10^{-53}.                               \tag{1}
$$

The same assertion holds for $\Psi^{-m}x-x$. This is a theorem about
classical area, not independent quantum coordinate phases.

Here is the full Fourier argument, including the issue with unbounded weights.
For $k\in\mathbb Z^2$ put

$$
u(k)=\tfrac12(k_q-k_p/\sqrt2),\quad
s(k)=\tfrac12(k_q+k_p/\sqrt2),\quad
K(k)=|u|+|s|=\max(|k_q|,|k_p|/\sqrt2).
$$

Then $u(L^Tk)=\lambda u(k)$, $s(L^Tk)=\lambda^{-1}s(k)$,
$\lambda=3+2\sqrt2$. Set $b=.001$, $w_k=e^{b(|s|-|u|)}$, and

$$
R_{nk}=\frac{w_n}{w_k}\int_{\mathbb T^2}
e^{2\pi i(k\cdot\Psi x-n\cdot x)}\,dx.           \tag{2}
$$

For $\Psi=L$, each column has a single entry in row $L^Tk$ with modulus
$e^{-b[(\lambda-1)|u|+(1-\lambda^{-1})|s|]}$.
The resulting operator $R_0$ is trace class; on the complement of the constant
mode its operator norm is at most $e^{-b/2}$.

On the complex strip of width $.001$, write $\Psi=Lx+v(x)$,
$\|v\|<\epsilon=10^{-78}$. These bounds follow from the finite Fourier
norm less than two and the short Hamiltonian time. Shift each integration
contour by $-i\operatorname{sgn}(n-L^Tk)/2000$ in (2). The Fourier
coefficient of $e^{2\pi ik\cdot v}-1$, combined with the weight ratio,
obeys

$$
|(R-R_0)_{nk}|\le20\epsilon K(k)e^{-bK(k)/2}
e^{-2b|n-L^Tk|_1}.                               \tag{3}
$$

Indeed $|k|_1\le3K(k)$, the ratio of shifted weights costs at most
$e^{b|n-L^Tk|_1}$, and the contour supplies
$e^{-\pi b|n-L^Tk|_1}$. The extra factor
$e^{2\pi|k|_1\epsilon}$ is absorbed in the unused linear decay in $K$.
The elementary sums
$\sum K(k)e^{-bK(k)/2}<13824b^{-3}$ and
$\sum_de^{-2b|d|_1}<4b^{-2}$ give

$$
\|R-R_0\|_1<10^{22}\epsilon<10^{-56}.             \tag{4}
$$

Area preservation separates the constant mode exactly:
$R=1\oplus R_\perp$, $\|R_\perp\|\le\vartheta$, with finite trace
norm and $\epsilon_R=\|R-R_0\|_1<10^{-56}$.
Let $P_J$ project onto a finite square of Fourier labels. We do not assume
that the unbounded diagonal weight is a bounded similarity. Instead,
in every finite product the weight ratios telescope. Thus

$$
((P_JRP_J)^m)_{kk}=((P_JC_\Psi P_J)^m)_{kk},
\quad C_\Psi f=f\circ\Psi.
$$

The left operators converge in trace norm to $R^m$. On the right,
$C_\Psi$ is unitary on $L^2(dx)$, so the finite compressions and each
fixed power converge strongly. Taking the fixed diagonal element gives

$$
(R^m)_{kk}=\int e^{2\pi ik\cdot(\Psi^m x-x)}\,dx. \tag{5}
$$

For a trace-class operator, the absolute sum of diagonal entries is at most
its trace norm. Equations (4)--(5) imply that the nonzero Fourier coefficients
of $\nu_m$ are absolutely summable. In fact the unperturbed operator
$R_{0,\perp}^m$ has zero diagonal: $(L^T)^mk=k$ has no nonzero integral
solution. The exact noncommuting telescoping identity gives

$$
\|R_\perp^m-R_{0,\perp}^m\|_1
\le\epsilon_R m\vartheta^{m-1}.
$$

This bounds the total absolute sum of the nonzero Fourier coefficients.
Their uniformly convergent Fourier series has the same trigonometric moments
as $\nu_m$, so it is its continuous nonnegative density. Finally
$m\vartheta^{m-1}\le\sum_{j=0}^{m-1}\vartheta^j\le8000$ proves (1).
For negative iterates substitute $x=\Psi^m y$ in the displacement law;
area preservation sends its density to $q_m(-z)$.

## 2. The quantitative sublevel bound

Let $F=\Psi^{-1}$ and $b_1=e^{2\pi iq}$, $b_2=e^{2\pi ip}$.
Put $d_{j,m}=b_j-b_j\circ F^m$ and $v_m=\sum_j|d_{j,m}|^2$.
For $z_i\in[-1/2,1/2]$, $|e^{2\pi iz_i}-1|\ge4|z_i|$.
Equation (1) therefore gives

$$
\operatorname{vol}\{v_m\le\delta\}\le C\delta,
\quad0<\delta\le1,\quad m\ge1,                   \tag{6}
$$

with one constant. All fixed spatial derivatives of $F^m$ grow at most
exponentially in $m$, by the chain rule and induction on derivative order.
Thus the same holds for every fixed derivative of $d_{j,m}$ and $v_m$.

## 3. Quantum traces by positive-square localization

Use the exact integer-label quantization
$Q_N(c)=\sum\widehat c(k,l)(-1)^{kl}T_N(l,k)$.
The single-kick Egorov proof and Weyl estimates in
[TRACE-106](../physical_kick_trace_decay.md), §§2--3, give

$$
\|U_N^mQ_N(b_j)U_N^{-m}-Q_N(b_j\circ F^m)\|
\le C e^{C_0m}N^{-2}.                            \tag{7}
$$

The cat covariance is exact for these ordinary-half labels: its parity
factor is unchanged by the integral label map. One-step conjugation acts
by $F=\Psi^{-1}$, with the positive sign of the quantum exponential.
Iterating one-step Egorov and the fixed-order derivative bound proves (7).
Only the two fixed characters are inserted into Egorov; no $N$-dependent
cutoff is inserted into it.

For $V=U_N^m$ and $\mu(c)=N^{-1}\operatorname{Tr}(Q_N(c)V)$,
cyclicity, (7) and the Weyl product/commutator estimates give

$$
|\mu(u d_{j,m})|\le C N^{-1}e^{C_1m}|u|_1,
\qquad |u|_r=\sum_k(1+|k|)^r|\widehat u(k)|.       \tag{8}
$$

Choose a real smooth cutoff $\eta=\rho(v_m/\delta)$, equal to one near
$v_m=0$ and zero when $v_m\ge2\delta$. Set
$\chi=\eta^2$ and $u_j=(1-\chi)\overline{d_{j,m}}/v_m$, smoothly
extended by zero near its zero set. Fourier Cauchy--Schwarz in dimension
two gives $|u|_1\le C\|u\|_{C^3}$ and
$|\eta|_2\le C\|\eta\|_{C^4}$. Consequently

$$
|u_j|_1+|\eta|_2\le C e^{C_2m}\delta^{-4}.
$$

The exterior identity $1-\chi=\sum_j u_jd_{j,m}$ is controlled by (8).
For the interior, the positive matrix $Q_N(\eta)^2$, the symmetric
Weyl product error of order $N^{-2}$ and the alias tail estimate give

$$
|\mu(\eta^2)|\le\int\eta^2+C N^{-2}|\eta|_2^2.
$$

Using (6), and increasing one exponential constant $K$, yields

$$
|\operatorname{tr}_N U_N^m|\le
C\left[\delta+e^{Km}N^{-1}\delta^{-4}
+e^{Km}N^{-2}\delta^{-8}\right].                  \tag{9}
$$

Set $\delta=N^{-1/5}$ and absorb bounded small $N$ into $C$:

$$
\boxed{|\operatorname{tr}_N U_N^m|\le C e^{Km}N^{-1/5},
\qquad m\ge1.}                                  \tag{10}
$$

At long times this may be weaker than one. Its useful consequence is the
uniform bound $C N^{-1/10}$ for $m\le(\log N)/(10K)$.

## 4. Global spectral discrepancy and matching

For a probability measure whose first $2H$ nonzero Fourier coefficients
are bounded by $\varepsilon$ with $H\varepsilon\le1$, the elementary
squared-Fejér argument gives arc discrepancy

$$
D(\mu)\le C/H+4H\varepsilon.                      \tag{11}
$$

For completeness, $\mu*F_H\le1+2H\varepsilon$ first bounds the mass
of every arc of length $1/H$ by $C/H$. Normalize $J_H=F_H^2/\int F_H^2$;
its first absolute moment is at most $2/H$. The short-arc bound then controls
$|\mu(I+t)-\mu(I)|$ by $C(|t|+1/H)$. Integrating against $J_H$
costs $C/H$, while its Fourier degree less than $2H$ bounds the remaining
smoothed density error by $4H\varepsilon$. This also handles endpoint atoms.

Apply (10) with $H=\lfloor\log N/(20K)\rfloor$.
The bare cat identity
$|\operatorname{Tr}M_N^m|^2=\#\ker(S^m-I)\le\lambda^m$
gives the same required logarithmic window after increasing $K$.
Both empirical eigenphase measures therefore satisfy

$$
D(\mu_N^{U})+D(\mu_N^{M})=O(1/\log N).           \tag{12}
$$

Sorting their eigenphases in $[0,1)$, with repetitions, bounds the largest
matched angular distance by the sum of discrepancies plus $2/N$.
Mapping the sorted orthonormal eigenbases gives, already with scalar phase one,

$$
\inf_{W\in U(N)}\|U_N-WM_NW^*\|_{\rm op}=O(1/\log N). \tag{13}
$$

No pressure gap or all-time quantum Gaussian reduction is used in (10)--(13).
This independently closes only the upper half of TRACE-110; its sharp Pell
lower half follows from the separate TRACE-113 theorem. Neither global
comparison resolves the signed Heisenberg hierarchy or microscopic Sine2.
