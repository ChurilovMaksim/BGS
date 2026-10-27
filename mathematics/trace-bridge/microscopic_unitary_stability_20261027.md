# Microscopic operator stability and pair-moment transfer

**Claims: BGS-TRACE-115 and BGS-TRACE-116. Status: analytic proof with author self-review, 27 October 2026.** No independent referee review or formal verification is asserted. The finite identities are valid for arbitrary unitaries. The original-family application uses the already registered TRACE-113 with its unchanged hypotheses and inherited external dependency; it is not a new proof of that input.

## 1. Definitions and bounded local statistics (TRACE-115)

For an $N$-dimensional unitary $U$ with eigenphases $\theta_j$ in radians, and one common uniform $\alpha\in[0,1)$, define

$$\Xi_{U,\alpha}=\sum_{j=1}^N\sum_{\ell\in\mathbb Z}\delta_{N(\theta_j/(2\pi)-\alpha+\ell)},\qquad
\mathscr L_U(f)=\mathbb E_\alpha e^{-\langle f,\Xi_{U,\alpha}\rangle}.$$

Let $U,V$ be unitary, $\epsilon=\|V-U\|<2$, $\eta=2\arcsin(\epsilon/2)$. For every nonnegative $f\in C_c^\infty(\mathbb R)$,

$$|\mathscr L_V(f)-\mathscr L_U(f)|\le\frac{N\eta}{2\pi}\|f'\|_1. \tag{1}$$

Write $VU^*=e^{iH}$ with $H=H^*$, $\|H\|\le\eta$, and $U_t=e^{itH}U$. For $F_N(\omega)=\sum_\ell f(N(\omega/(2\pi)+\ell))$, the absolutely convergent differentiated Fourier series gives

$$\partial_t\operatorname{Tr}F_N(e^{-2\pi i\alpha}U_t)
=\operatorname{Tr}\bigl(HF_N'(e^{-2\pi i\alpha}U_t)\bigr).$$

For Hermitian $B$, $|\operatorname{Tr}HB|\le\eta\operatorname{Tr}|B|$. Averaging over the common shift gives

$$\int_0^1\operatorname{Tr}|F_N'(e^{-2\pi i\alpha}U_t)|\,d\alpha
=\frac N{2\pi}\int_0^{2\pi}|F_N'(\omega)|\,d\omega
\le\frac N{2\pi}\|f'\|_1.$$

Since $F_N\ge0$, differentiating the exponential and integrating in $t$ proves (1). Thus $\|V_N-U_N\|=o(N^{-1})$ preserves every weak local point-process limit. Local first moments equal interval lengths under the uniform shift, giving local tightness; smooth nonnegative Laplace tests determine the limit. No eigenphase matching, spectral simplicity or pair-moment uniform integrability is needed. A common unit scalar can be optimized away by shift invariance.

## 2. Relative positive pair-energy comparison (TRACE-115)

Set $P_r(\omega)=(1-r^2)/(1-2r\cos\omega+r^2)$ and

$$R_U(s)=\frac1{N^2}\sum_{j,k}P_{e^{-s/N}}(\theta_j-\theta_k)
=1+\frac2{N^2}\sum_{m\ge1}e^{-sm/N}|\operatorname{Tr}U^m|^2,\quad s>0.$$

The latter identity is the existing [RES-006](../fixed-map/fixed_map_resolvent_frontier.md), in this normalization. Then

$$e^{-2\eta/\sinh(s/N)}\le R_V(s)/R_U(s)\le e^{2\eta/\sinh(s/N)}. \tag{2}$$

Indeed $Q_t=\operatorname{Ad}_{U_t}$ on Hilbert–Schmidt matrices obeys $Q_t'=iGQ_t$, where $G=\operatorname{ad}_H$ is self-adjoint with norm at most $2\eta$. Differentiation of the trace of the absolutely convergent Laurent series of $P_r$ yields

$$|\partial_tR_{U_t}(s)|\le2\eta N^{-2}\operatorname{Tr}_{HS}|P_r'(Q_t)|.$$

For $c=\cos\omega$, the exact identity

$$(1+r^2-2rc)^2-(1-r^2)^2(1-c^2)=[2r-(1+r^2)c]^2$$

gives $|P_r'|\le P_r/\sinh(s/N)$. Integrate the logarithmic derivative to prove (2). Repeated eigenvalues cause no exception. This is relative comparison and does not itself bound $R_U$.

## 3. Absolute compact pair-moment comparison (TRACE-115)

For real even $w\in C_c^2(\mathbb R)$ put

$$T_U(w)=N^{-2}\sum_{m\ge1}w(m/N)|\operatorname{Tr}U^m|^2,\qquad
C_w=4\pi\|tw\|_1+\pi^{-1}\|(tw)''\|_1.$$

Then

$$|T_V(w)-T_U(w)|\le\tfrac12 C_wN\eta\,
 e^{2\eta/\sinh(2\pi/N)}R_U(2\pi). \tag{3}$$

For $\phi(x)=\int w(t)e^{2\pi itx}dt$, two integrations by parts give
$|\phi'(x)|\le C_w/(1+x^2)$. Fourier comparison gives the uniformly convergent periodization, including its derivative,

$$h_N(\omega):=\sum_{m\ge1}w(m/N)\cos(m\omega)
=\tfrac12\bigl[N\sum_\ell\phi(N(\omega/(2\pi)+\ell))-w(0)\bigr].$$

As $f_s(x)=2s/(s^2+4\pi^2x^2)$ satisfies $N\sum_\ell f_s(N(\omega/(2\pi)+\ell))=P_{e^{-s/N}}(\omega)$, we have
$|h_N'|\le C_wNP_{e^{-2\pi/N}}/4$. Apply Hilbert–Schmidt trace differentiation to $T_U=N^{-2}\operatorname{Tr}_{HS}h_N(Q)$, use $\|G\|\le2\eta$, and then (2). This proves (3), with no convergence or integrability assumption hidden in it.

## 4. From existing short traces to pair-energy control

Suppose $|\operatorname{Tr}U_N^m|\le Ca^m$ for every $m\ge1$, with fixed $C$ and $a>1$ and one threshold independent of $m$. For an integer $L\ge1$, if $|\operatorname{Tr}U_N^m|^2/N^2\le\delta\le1$ for $1\le m<L$, then

$$R_{U_N}(s)\le(1-\delta)\coth\frac{sL}{2N}+\delta\coth\frac{s}{2N}. \tag{4}$$

To prove it, write $z=e^{i\omega}$, $r=e^{-s/N}$ and use

$$P_r(\omega)=\frac{(1-r^2)|\sum_{j=0}^{L-1}r^jz^j|^2}{|1-r^Lz^L|^2}.$$

Bound the denominator below by $(1-r^L)^2$. Averaging the numerator against the empirical phase-difference measure, its diagonal is $\sum r^{2j}$ and each off-diagonal coefficient is a nonnegative $r^{j+k}$ multiplied by a moment at most $\delta$. The upper bound is therefore the convex combination of the zero-off-diagonal and all-one expressions; their quotients are exactly the two hyperbolic cotangents in (4).

Choose $L=\max(1,\lfloor\log N/(2\log a)\rfloor)$ and $\delta=C^2/N$, for all sufficiently large $N$. Then (4) gives $R_{U_N}(s)=O_s(N/\log N)$. In the unchanged original fixed-$\tau$ family this hypothesis is supplied by [TRACE-113](../fixed-map/fixed_kick_uniform_trace_bound.md), along all sufficiently large odd $N$. Constants and startup thresholds remain noneffective; no new numerical threshold is claimed.

## 5. Original-family transfer, including nonunitary approximants (TRACE-116)

For the original family and fixed $K$, (3) implies

$$\|V_N-U_N\|\le K/N^2,\quad V_N\text{ unitary}
\ \Longrightarrow\ |T_{V_N}(w)-T_{U_N}(w)|=O_{w,K}(1/\log N). \tag{5}$$

Indeed $\eta=O(N^{-2})$, the exponential factor in (3) is bounded, and section 4 bounds $R_U$. The same conclusion holds for the signed deviation from the CUE reference because the reference cancels exactly. More generally $o(\log N/N^2)$ suffices.

Let $B_N$ be arbitrary matrices with $\|B_N-U_N\|\le\epsilon_N$. Here $T_{B_N}$ means the finite trace polynomial only, not a circle point process. If $\operatorname{supp}w\subset[-R,R]$, $W=\sup|w|$, and $D=W(R+1)^3$, telescoping powers gives

$$|\operatorname{Tr}(B_N^m-U_N^m)|\le Nm\epsilon_N e^{RN\epsilon_N}\quad(1\le m\le RN),$$

$$Z_N:=N^{-2}\sum_m|w(m/N)|\,|\operatorname{Tr}(B_N^m-U_N^m)|^2
\le D\epsilon_N^2N^3e^{2RN\epsilon_N}.$$

The weight is bounded by $We^{2\pi R}e^{-2\pi t}$ for $t\ge0$, so section 4 implies $T_{U_N}(|w|)=O_w(N/\log N)$. Cauchy–Schwarz now gives

$$|T_{B_N}(w)-T_{U_N}(w)|\le2\sqrt{T_{U_N}(|w|)Z_N}+Z_N.$$

Consequently $\epsilon_N\le K/N^2$ implies an $O_{w,K}(1/\sqrt{\log N}+1/N)$ difference. Even $\epsilon_N=o(\sqrt{\log N}/N^2)$ suffices. For $\epsilon_N<1$, the unitary polar factor of $B_N$ is within $2\epsilon_N$ of $U_N$ and satisfies (1), (3) and (5) as applicable.

## 6. Relation to existing results and the remaining task

The [FM-003](../fixed-map/fixed_map_moment_control_and_transfer.md) time-average comparison and the [principal WKB polar transport](../fixed-map/polar_wkb_quantization_stability.md) control different perturbations with additional dynamical information; (1)–(5) do not replace them. The adjoint representation and clock minima belong to RES-006 and [TRACE-092](abel_clock_rigidity.md). Weak convergence alone still does not transfer unbounded pair moments.

A computable $O(N^{-2})$ approximant with a proved CUE pair limit has not been constructed. Theorems (5) and its nonunitary version transfer a limit if one is supplied; they do not establish that limit for the original family or any higher factorial hierarchy. TRACE-005 remains open.
