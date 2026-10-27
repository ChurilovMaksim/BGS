# Unitary perturbations and bounded microscopic tests

**Status: author argument; verification pending.** This note records the QS1 argument from the [chat archive](../../record/chat_trace005_20261027/README.md), with the phase and common-shift conventions explicit. It concerns bounded Laplace functionals; it does not assert convergence of unbounded pair moments.

Let $U,V$ be $N\times N$ unitary matrices, $\epsilon=\|V-U\|<2$, and $\eta=2\arcsin(\epsilon/2)$. For eigenphases $\theta_j$ in radians, define the unfolded point measure with one common uniform shift $\alpha\in[0,1)$ by

$$\Xi_{U,\alpha}=\sum_{j=1}^N\sum_{\ell\in\mathbb Z}\delta_{N(\theta_j/(2\pi)-\alpha+\ell)}.$$

For nonnegative $f\in C_c^\infty(\mathbb R)$ set $\mathscr L_U(f)=\mathbb E_\alpha e^{-\langle f,\Xi_{U,\alpha}\rangle}$. Then

$$|\mathscr L_V(f)-\mathscr L_U(f)|\le \frac{N\eta}{2\pi}\|f'\|_{L^1}.$$

Indeed write $VU^*=e^{iH}$ with $H$ Hermitian and $\|H\|\le\eta$. Along $U_t=e^{itH}U$, the smooth periodization $F_N(\omega)=\sum_{\ell}f(N(\omega/(2\pi)+\ell))$ satisfies

$$\frac d{dt}\operatorname{Tr}F_N(e^{-2\pi i\alpha}U_t)=\operatorname{Tr}(H F_N'(e^{-2\pi i\alpha}U_t)).$$

This follows termwise from its absolutely convergent differentiated Fourier series. For Hermitian $B$, $|\operatorname{Tr}(HB)|\le\|H\|\operatorname{Tr}|B|$. Integrating over the common shift gives

$$\int_0^1\operatorname{Tr}|F_N'(e^{-2\pi i\alpha}U_t)|d\alpha
=\frac N{2\pi}\int_0^{2\pi}|F_N'(\omega)|d\omega
\le\frac N{2\pi}\|f'\|_1.$$

Because $F_N\ge0$, the derivative of $e^{-\operatorname{Tr}F_N}$ is bounded by that of the exponent. Integrating in $t$ proves the claim. It follows that $\|V_N-U_N\|=o(N^{-1})$ makes all such bounded Laplace functionals asymptotically identical. This extends to weak point-process laws by the standard uniqueness of Laplace functionals and local first-moment tightness; the uniform shift makes the expected count in a bounded interval equal to its length. No uniform-integrability statement for pair observables follows. Multiplication by a common unit scalar can be optimized away because it only translates the uniform shift.

The related positive adjoint-resolvent representation is already [RES-006](../fixed-map/fixed_map_resolvent_frontier.md); clock minima and positive decompositions are treated in [TRACE-092](abel_clock_rigidity.md). The stronger pair-transfer inequalities in the archival source require their own detailed audit before registration. Neither this note nor the auxiliary [balanced-rounding barrier](../fixed-map/balanced_rounding_research_20261027.md) proves TRACE-005.

## Positive Poisson pair energy

For $s>0$ and a unitary $U$, put $r=e^{-s/N}$ and

$$R_U(s)=N^{-2}\sum_{j,k=1}^N\frac{1-r^2}{1-2r\cos(\theta_j-\theta_k)+r^2}.$$

For the same $U,V,\eta$ as above, the following author-checked inequality is proposed:

$$e^{-2\eta/\sinh(s/N)}\le\frac{R_V(s)}{R_U(s)}\le e^{2\eta/\sinh(s/N)}.$$

To check it, on Hilbert–Schmidt matrices set $Q_t(X)=U_t XU_t^*$ and $G(X)=HX-XH$. Then $Q_t'=iGQ_t$, $G$ is self-adjoint and $\|G\|\le2\eta$. The eigenvalues of $Q_t$ are the $e^{i(\theta_j-\theta_k)}$, with multiplicities, so $R_{U_t}=N^{-2}\operatorname{Tr}_{HS}P_r(Q_t)$. The same trace differentiation as above yields

$$|R_{U_t}'|\le2\eta N^{-2}\operatorname{Tr}_{HS}|P_r'(Q_t)|.$$

Writing $c=\cos\omega$, the identity

$$ (1+r^2-2rc)^2-(1-r^2)^2(1-c^2)=[2r-(1+r^2)c]^2 $$

gives $|P_r'(\omega)|\le P_r(\omega)/\sinh(s/N)$. Integrating the logarithmic derivative proves the inequality, including repeated eigenvalues. An independent Wolfram Language expansion returned zero for the difference between the two sides of the displayed polynomial identity; this checks that identity only, not the analytic argument.

This comparison is relative and does not itself bound $R_U$ or prove convergence to the CUE value. Its exact adjoint representation is already present as RES-006; the perturbation bound is recorded as a separately scoped continuation and remains verification pending.
