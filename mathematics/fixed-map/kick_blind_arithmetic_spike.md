# Kick-blind arithmetic spikes of the fixed map

**Claim ID:** `BGS-TRACE-117`.
**Status:** project proof. The rational comparisons are typechecked in Lean 4.33.1 and recomputed in independent Python and C++ integer arithmetic. No external referee, and no priority claim for the classical fact that an unperturbed quantum cat map is not CUE. The odd scalar case overlaps the arithmetic in `BGS-FM-010`; the argument below does not invoke that note as a lemma.

`BGS-TRACE-005` and `BGS-BGS-001` remain **open**. The kicked statement is ninety-nine explicit dimensions. It is not an estimate of the signed hierarchy for every large odd dimension.

## 1. Statements

Let \(N\) be odd and at least \(3\). Write \(e_N(t)=\exp(2\pi i t/N)\), with modular inverses, and

\[
(W_N(n,\ell)\psi)(x)=e_N\bigl(n(x+2^{-1}\ell)\bigr)\psi(x+\ell),
\]
\[
(M_N)_{xy}=N^{-1/2}e_N\bigl(-8^{-1}(3x^2-2xy+3y^2)\bigr).
\]

Let \(A_N=\sum c_{kl}W_N(k,\ell)\) be the raw Weyl quantization of \(f-1/10\) from `formalization/Bgs/TraceStatement.lean`, and let \(\tau=10^{-80}\), \(\theta=\tau N\), \(U_N=\exp(i\theta A_N)M_N\). The Abel pair statistic is

\[
L_N(V;s)=N^{-2}\sum_{m\ge1}e^{-2sm/N}\lvert\operatorname{Tr}V^m\rvert^2,\qquad s>0.
\]

The CUE target at \(s=1\) is \((1-e^{-2})/4\). This is strictly less than \(1/4\), because \(e^{-2}>0\).

Define integers by \(u_0=1\), \(v_0=0\) and

\[
u_{m+1}=u_m+2v_m,\qquad v_{m+1}=u_m+v_m,
\]

so \(u_m+v_m\sqrt2=(1+\sqrt2)^m\). Every \(u_m\) is odd. Set \(C=\begin{pmatrix}3&2\\4&3\end{pmatrix}\). This is the frequency action implemented by the matrix \(M_N\) above. The classical matrix \(S=\begin{pmatrix}3&4\\2&3\end{pmatrix}\) is its transpose.

**Theorem 1 (pure cat map).** For every odd integer \(n\ge5\), at dimension \(N=u_n\),

\[
M_N^n=\zeta I\quad(|\zeta|=1),
\qquad
L_N(M_N;1)\ge1-\frac{2n}{N}>\frac34.
\]

Hence \(\lvert L_N(M_N;1)-(1-e^{-2})/4\rvert>1/2\). Along this infinite sequence the unperturbed propagator does not approach the CUE Abel value.

**Theorem 2 (fixed kick, ninety-nine dimensions).** For every odd integer \(n\) with \(5\le n\le201\), at \(N=u_n\),

\[
L_N(U_N;1)>\frac34.
\]

The same gap, larger than \(1/2\), holds for the kicked propagator at each of these dimensions. The largest one is \(N=u_{201}\), which has \(77\) decimal digits. Any statement of the form "\(\lvert L_N(U_N;1)-(1-e^{-2})/4\rvert<1/2\) for every odd \(N\ge N_0\)" requires \(N_0>u_{201}\).

**Boundary.** Theorem 2 is a finite arithmetic progression of dimensions, not a limit and not a statement about a generic odd \(N\). The one-term lower bound used here drops to at most \(3/4\) at the next odd index \(n=203\), while \(\tau u_n B\) is still strictly less than \(1\). That drop is a failure of the estimate, not a proved drop of \(L_N\). No estimate is claimed for the off-diagonal sum \(Y_{m,N}\), for \(m\asymp N\) at dimensions past this list, or for any \(k>2\). Passing the Python, C++ and Lean checks does not prove `BGS-TRACE-005`.

## 2. Phase-free conjugation

For odd \(N\), every label \((k,\ell)\in(\mathbb Z/N)^2\) and every matrix index,

\[
\bigl(M_NW_N(k,\ell)\bigr)_{xz}
=N^{-1/2}e_N\bigl(q(x,z-\ell)+k(z-\ell/2)\bigr),
\]
\[
q(a,b)=-(3a^2-2ab+3b^2)/8.
\]

The same entry of \(W_N(3k+2\ell,4k+3\ell)M_N\) is

\[
N^{-1/2}e_N\bigl((3k+2\ell)\bigl(x+(4k+3\ell)/2\bigr)+q(x+4k+3\ell,z)\bigr).
\]

Both exponent polynomials expand to

\[
-\frac{kl}2+kz-\frac{3\ell^2}8-\frac{\ell x}4+\frac{3\ell z}4-\frac{3x^2}8+\frac{xz}4-\frac{3z^2}8.
\]

The difference is the zero polynomial over \(\mathbb Q\). Halves and quarters are the modular inverses of \(2\), \(4\) and \(8\), which exist for odd \(N\). Therefore

\[
M_NW_N(k,\ell)=W_N(C(k,\ell))M_N.
\]

Iterating gives \(M_N^nW_N(v)=W_N(C^nv)M_N^n\), with no inverse. The \(N^2\) operators \(W_N(v)\) span \(M_N(\mathbb C)\). Indeed \(W_N(n,\ell)\) has a single nonzero entry in column \(y\), in row \(y-\ell\), equal to \(e_N(n(y-2^{-1}\ell))\). Averaging in \(n\) against a character isolates every matrix unit on that diagonal. Consequently, if \(C^n\equiv I\pmod N\), then \(M_N^n\) commutes with every matrix, so \(M_N^n=\zeta I\).

Rows of \(M_N\) are orthonormal: the inner product of rows \(x\) and \(x'\) is

\[
N^{-1}\sum_y e_N\bigl(q(x,y)-q(x',y)\bigr),
\]

and the exponent is linear in \(y\) with coefficient \((x-x')/4\). The geometric sum is \(N\) if \(x\equiv x'\) and \(0\) otherwise, because \(4\) is invertible. Thus \(M_N\) is unitary, \(\lvert\zeta\rvert=1\) and \(\lvert\operatorname{Tr}M_N^n\rvert=N\).

## 3. Odd scalar returns of the linear map

Let \(P=I+J\) with \(J=\begin{pmatrix}0&1\\2&0\end{pmatrix}\), so \(J^2=2I\) and \(P=\begin{pmatrix}1&1\\2&1\end{pmatrix}\). Then \(P^m=u_mI+v_mJ\) and \(C=P^2\). The norm identity \(u_m^2-2v_m^2=(-1)^m\) is the determinant of \(P^m\). For odd \(m\),

\[
(u_m+v_m\sqrt2)^2=u_{2m}+v_{2m}\sqrt2
\]

gives \(v_{2m}=2u_mv_m\) and \(u_{2m}=u_m^2+2v_m^2=2u_m^2+1\), hence

\[
C^m-I=P^{2m}-I=(u_{2m}-1)I+v_{2m}J=2u_mP^m.
\]

If an odd \(N\) divides \(u_m\), then \(C^m\equiv I\pmod N\). Taking \(N=u_n\) with \(n\) odd and at least \(5\) does this. Section 2 yields \(M_N^n=\zeta I\).

Every \(u_m\) is odd because \(u_{m+1}\equiv u_m\pmod 2\) and \(u_0=1\). In particular \(8\) remains invertible at these dimensions. Also \(v_1=1\) and \(v_{m+1}=u_m+v_m\), so \(v_m>0\) for \(m\ge1\) and \(u_{m+1}-u_m=2v_m>0\). Thus \(u_n\) is strictly increasing for \(n\ge1\).

The sequence satisfies \(u_{m+2}=2u_{m+1}+u_m\). It does **not** satisfy the trace recurrence \(t_{m+1}=6t_m-t_{m-1}\) of the matrix \(C\). Expanding the two-step rule gives the form used below: for \(m\ge1\),

\[
u_{m+2}=5u_m+2u_{m-1}.
\]

Since \(u_{m-1}\ge1\), this is strictly larger than \(5u_m\).

## 4. Abel lower bound for the pure cat map

For \(0\le x\), \(e^{-x}\ge1-x\). Therefore

\[
L_N(M_N;1)\ge e^{-2n/N}\lvert\operatorname{Tr}M_N^n\rvert^2/N^2
=e^{-2n/N}\ge1-2n/N,
\]

as soon as the right side is positive. For odd \(n\ge5\), \(2n/u_n<1/4\). The case \(n=5\) is \(10/41<1/4\), so \(1-10/41=31/41>3/4\). If the bound holds for an odd \(n\ge5\), then

\[
\frac{2(n+2)}{u_{n+2}}
<\frac{2(n+2)}{5u_n}
=\frac{n+2}{n}\cdot\frac15\cdot\frac{2n}{u_n}
\le\frac75\cdot\frac15\cdot\frac14
=\frac7{100}<\frac14.
\]

The first inequality is strict because \(u_{n+2}>5u_n\), and \((n+2)/n\le7/5\) for every \(n\ge5\). Thus \(L_{u_n}(M;1)>3/4>1/4>(1-e^{-2})/4\) for every odd \(n\ge5\), and the distance to the CUE value is greater than \(1/2\).

## 5. The kick on ninety-nine dimensions

Each \(W_N(k,\ell)\) is unitary, so \(\lVert A_N\rVert\le\sum\lvert c_{kl}\rvert\). There are exactly \(32\) nonzero modes. For each mode, \(\lvert c\rvert^2=p/q\) in lowest terms, and

\[
\sqrt{p/q}\le\bigl(\lfloor\sqrt{pq}\rfloor+1\bigr)/q,
\]

because \(\lfloor\sqrt{pq}\rfloor+1>\sqrt{pq}\). Summing these rational majorants produces

\[
B=\frac{184981}{160000}.
\]

The mode \((k,\ell)=(7,0)\) has coefficient \(9/20\). Both verifiers recompute the \(32\) modes from the same formula as `fCoeff` and obtain this majorant.

Let \(x_n=\tau u_n B\) and \(\rho_n=nx_n/(1-x_n)\). For \(0\le y<1\), \(\exp(y)-1\le y/(1-y)\). With \(y=\theta\lVert A_N\rVert\le x_n<1\),

\[
\lVert\exp(i\theta A_N)-I\rVert\le\exp(y)-1\le\frac{x_n}{1-x_n}.
\]

The telescoping identity \(U^n-M^n=\sum_{j=0}^{n-1}U^{n-1-j}(U-M)M^j\) and unitarity give

\[
\lvert\operatorname{Tr}U_N^n-\operatorname{Tr}M_N^n\rvert
\le Nn\frac{x_n}{1-x_n}=N\rho_n.
\]

If \(\rho_n<1\) and \(\lvert\operatorname{Tr}M_N^n\rvert=N\), then \(\lvert\operatorname{Tr}U_N^n\rvert\ge N(1-\rho_n)\). One nonnegative term of the Abel sum and the inequality \(e^{-2n/u_n}\ge1-2n/u_n\) yield

\[
L_N(U_N;1)
\ge e^{-2n/u_n}(1-\rho_n)^2
\ge\Bigl(1-\frac{2n}{u_n}\Bigr)(1-\rho_n)^2.
\]

Write \(\delta_n=2n/u_n\). For odd \(n\) with \(7\le n\le199\),

\[
\delta_{n+2}<\frac{n+2}{5n}\delta_n\le\frac9{35}\delta_n<\delta_n,
\]

because \((n+2)/n\le9/7\). Thus \(\delta_7>\delta_9>\cdots>\delta_{201}\), so \(\delta_n\le\delta_7=14/239\) on this range. Separately, \(t\mapsto t/(1-t)\) is increasing on \([0,1)\). Once \(x_{201}<1\), one has \(x_n/(1-x_n)\le x_{201}/(1-x_{201})\) and \(n\le201\), hence

\[
\rho_n=\frac{n\,x_n}{1-x_n}\le\rho_{201}
\]

for every \(1\le n\le201\). Therefore, for odd \(n\) from \(7\) through \(201\),

\[
\bigl(1-\delta_n\bigr)(1-\rho_n)^2
\ge\bigl(1-\delta_7\bigr)\bigl(1-\rho_{201}\bigr)^2
=\frac{225}{239}(1-\rho_{201})^2.
\]

The verifiers and the Lean witness prove the two rational inequalities \(x_{\mathrm{Den}}>202\,x_{\mathrm{Num}}\) and

\[
300\bigl(x_{\mathrm{Den}}-202\,x_{\mathrm{Num}}\bigr)^2
>239\bigl(x_{\mathrm{Den}}-x_{\mathrm{Num}}\bigr)^2,
\]

where \(x_{\mathrm{Num}}=u_{201}\cdot184981\) and \(x_{\mathrm{Den}}=10^{80}\cdot160000\). The first says \(\rho_{201}<1\). The second is exactly \((225/239)(1-\rho_{201})^2>3/4\). Hence \(L_{u_n}(U;1)>3/4\) for every odd \(n\) from \(7\) through \(201\).

The remaining endpoint \(n=5\), \(N=41\), is the cleared inequality

\[
124\bigl(x_{\mathrm{Den}}-6\cdot41\cdot184981\bigr)^2
>123\bigl(x_{\mathrm{Den}}-41\cdot184981\bigr)^2
\]

together with \(x_{\mathrm{Den}}>6\cdot41\cdot184981\). That is \((31/41)(1-\rho_5)^2>3/4\). Both programs also recompute the direct cleared form

\[
4\bigl(x_{\mathrm{Den}}-(n+1)x_{\mathrm{Num}}\bigr)^2(u_n-2n)
>3u_n\bigl(x_{\mathrm{Den}}-x_{\mathrm{Num}}\bigr)^2
\]

at every odd \(n\) from \(5\) through \(201\), and they check that the same inequality fails at \(n=203\) while \(\rho_{203}<1\). The decimal expansion of \(u_{201}\) is in `evidence/executions/20261028/kick-blind-spike/receipt.json`.

## 6. What was tried and does not close TRACE-005

The pressure bound of TRACE-113 controls \(\lvert\operatorname{Tr}U_N^m\rvert\) by \(Ca^m\) with \(a>1\). Summed against \(e^{-2sm/N}/N^2\), the Abel mass that can affect the limit sits at \(m\asymp N\), where \(Ca^m\) exceeds the unitary bound \(N\). A logarithmic or sublinear window does not decide \(L_N(s)\).

The spike at \(N=u_n\) cannot be chased to infinity inside the kick-blind window. The one-term lower bound stays above \(3/4\) through \(n=201\) and is at most \(3/4\) at \(n=203\). The cruder condition \(x_n\ge1\) begins only near \(n=211\), where \(u_n\) has about \(81\) decimal digits. Between these indices the operator-norm majorant still makes \(\exp(i\theta A_N)\) close to the identity, but one return is no longer enough for the constant \(3/4\). A matching upper bound, or a sum over several returns, would be a different theorem. Values on a finite list do not decide \(\lim_{N\to\infty}\).

A variance lower bound on the orbit sum of \(A_N\) does not by itself destroy the spike. A spectrum supported on \((2\pi/\theta)\mathbb Z\) can have large variance and still satisfy \(\operatorname{Tr}\exp(i\theta S)=N\). Removing the spike for every large \(N\) needs the actual spectral measure of that orbit sum, which is the open signed-cancellation problem.

## 7. Certificates

| Check | What it certifies |
|---|---|
| `computations/verification/kick_blind_spike.py` | Polynomial identity of the two phases, including the displayed expansion; \(32\) Fourier modes; majorant \(B\); norm and the identity \(u_{m+2}=5u_m+2u_{m-1}\) through \(m=203\); oddness of every \(u_m\); decrease of \(\delta_n\) and increase of \(\rho_n\); the uniform gap; the \(n=5\) endpoint; the direct gap on all \(99\) odd indices from \(5\) through \(201\); failure of that direct gap at \(n=203\) |
| `computations/cpp/kick_blind_spike.cpp` | The same recurrence, majorant, monotonicity, uniform gap, endpoint, direct gaps and sentinel, in independent integer arithmetic |
| `formalization/Bgs/KickBlindRational.lean` | `decide` proofs of the norm \(u_{201}^2-2v_{201}^2=-1\), positivity and oddness, the bases \(u_5=41\) and \(u_7=239\), \(\rho_{201}<1\), the uniform comparison, and the \(n=5\) endpoint. Typechecked with Lean 4.33.1. It does not formalize Sections 2–5 |

The aggregate `lake build` was not rerun for this note: the Mathlib cache was not present. The new module imports only the Lean prelude.
