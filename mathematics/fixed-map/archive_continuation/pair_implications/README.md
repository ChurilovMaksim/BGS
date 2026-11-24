# What weak Sine₂ convergence would force

**Registry:** BGS-TRACE-365.

**Scope.** These implications concern arbitrary deterministic \(N\)-point
spectra on the circle, with multiplicities and one common uniform rotation.
They apply in particular to the [fixed map](../../fixed_model_symmetry_theorem.md).
They assume its weak limit where indicated and supply no trace estimate for the
map itself. This is the statistical part of §§5–7 of the November 19 BGS-F
report; its finite Pell example is separate. Nothing here changes
BGS-BGS-001 or BGS-TRACE-005.

## Conventions and exact identities

Use angles \(\theta_j\in\mathbb R/\mathbb Z\), \(p_m=\sum_j e^{2\pi i m\theta_j}\),
and let \(X_N=\sum_{j=1}^N\sum_{k\in\mathbb Z}\delta_{N(\theta_j-\alpha+k)}\), with \(\alpha\)
uniform on \([0,1)\). It is stationary with intensity one. Its ordered reduced
second-moment measure, **including** the diagonal, is
\[
 \gamma_N=\frac1N\sum_{j,l=1}^N\sum_{k\in\mathbb Z}
          \delta_{N(\theta_j-\theta_l+k)}.
\]
In particular, for compactly supported continuous \(\rho,g\),
\(\mathbb E\iint\rho(x)g(y-x)\,dX_N(x)dX_N(y)=(\int\rho)\gamma_N(g)\).
This follows by integrating over the common shift and unfolding the first
point; the relative difference is unchanged by it. For unit-intensity Sine₂,
write \(\gamma_{\rm s}=\delta_0+(1-K^2)\,dx\), where
\(K(x)=\sin(\pi x)/(\pi x)\).

Take the real \(b\) and \(b_*\) of the
[standalone target](../../../../record/remaining_breakthrough_task_20261021.md),
with \(g_b(x)=\int b(y)b(y+x)\,dy\) and
\(\widehat f(u)=\int e^{-2\pi iux}f(x)\,dx\).
For the Abel convention \(h_s(x)=s/(s^2+\pi^2x^2)\) and
\(L_N(s)=N^{-2}\sum_{m\ge1} e^{-2sm/N}|p_m|^2\), periodization gives
\[
 2\Delta_{2,N}(b)=\gamma_N(g_b)-\mathbb E_{\rm CUE}\gamma_N^{\rm CUE}(g_b),
 \qquad
 \gamma_N(h_s)=1+2L_N(s).
\]
Indeed, \(\gamma_N(f)=N^{-2}\sum_{m\in\mathbb Z}
\widehat f(m/N)|p_m|^2\) for these tests. The \(m=0\) and diagonal terms in
the CUE subtraction cancel, and \(\widehat g_b=|\widehat b|^2\).
Since the CUE variance of \(p_m\) is \(\min(|m|,N)\) for \(m\ne0\), the
CUE term converges to \(\gamma_{\rm s}(g_b)\) by Riemann sums, using
\(\widehat{K^2}(u)=(1-|u|)_+\). In the same normalization
\(\gamma_{\rm s}(h_s)=1+(1-e^{-2s})/(2s^2)\). For the corresponding
resolvent convention see [RES-006](../../fixed_map_resolvent_frontier.md).

## 1. A negative defect disproves the weak limit

If \(X_N\Rightarrow\mathrm{Sine}_2\) in the vague topology, then
\[
 \liminf_N\gamma_N(g)\ \ge\ \gamma_{\rm s}(g)
 \quad\text{for every continuous }g\ge0.
\]
For \(g\) compactly supported, choose \(\rho\ge0\) compactly supported with
\(\int\rho=1\). The functional \(\iint \rho(x)g(y-x)\,dX(x)dX(y)\) is
continuous: its kernel is continuous with compact support in two variables,
and tensor-product approximation on a compact rectangle is uniform while
local masses are bounded along any vaguely converging sequence. Truncate
the functional at \(B\), apply weak convergence, and let \(B\uparrow\infty\).
For general \(g\ge0\), first use compact lower cutoffs increasing to \(g\).
Thus a defect \(\Delta_{2,N}(b)\le-\epsilon\) along an infinite subsequence,
for a fixed nonnegative admissible \(b\) and a fixed \(\epsilon>0\), refutes
the weak law without a uniform-integrability hypothesis. An excess
does not have this implication. For instance, in any sequence with
the asserted weak limit, move \(r_N=\lfloor N^{3/4}\rfloor\) indexed phases
to one phase. Under the same random origin, the probability that any
moved or replacement phase is seen in a fixed interval of length \(B\)
is at most \(2B r_N/N=o(1)\). The weak local law is unchanged, but the
coincident cluster alone contributes \(r_N^2 g_*(0)/N\to\infty\) to
\(\gamma_N(g_*)\). This example concerns arbitrary spectra, not the
literal kicked map.

## 2. Weak limit plus one exact pair test gives every pair test

Suppose \(X_N\Rightarrow\mathrm{Sine}_2\) and
\(\Delta_{2,N}(b_*)\to0\). Then \(\gamma_N(f)\to\gamma_{\rm s}(f)\) for
every continuous \(f\) with
\(\sum_{n\in\mathbb Z}\sup_{[n,n+1]}|f|<\infty\).
Indeed, \(g_*=g_{b_*}\) is everywhere positive: the inverse transform of the
nonzero compactly supported bump defining \(b_*\) is an entire function
with isolated real zeros. Its squared modulus in the autocorrelation is
therefore positive almost everywhere. The assumed test gives
\(\gamma_N(g_*)\to\gamma_{\rm s}(g_*)\). The resulting uniform bound on
compact masses gives vague subsequential compactness. Every limit
\(\nu\) satisfies \(\nu\ge\gamma_{\rm s}\) by §1 and
\(\nu(g_*)\le\gamma_{\rm s}(g_*)\) by compact cutoffs. Strict positivity
forces \(\nu=\gamma_{\rm s}\), so the entire sequence converges vaguely.

For the tail estimate, put \(q(x)=(1-|x|)_+\) and
\(Y_t=X_N([t,t+1])\). Unfolding (or the overlap length of two intervals)
gives
\[
 (q*\gamma_N)(t)=\mathbb E Y_0Y_t\le\mathbb E Y_0^2=(q*\gamma_N)(0)
 \le \gamma_N([-1,1]).
\]
Use evenness of \(\gamma_N\) for the convolution sign; the common shift
makes endpoint events null. As \(q\ge1/2\) on \([-1/2,1/2]\), every unit
interval has uniformly bounded mass, independently of position and \(N\).
The same is true for \(\gamma_{\rm s}\). The summable unit-interval
suprema now control tails uniformly. This gives all order-two band tests
and the Abel/resolvent limits in these conventions. It does not give
higher factorial moments. The hypothesis of weak convergence was essential
to the domination of every vague limit in this argument.

## 3. No macroscopic normalized trace anywhere in a fixed linear band

If \(X_N\Rightarrow\mathrm{Sine}_2\), then for every fixed \(C>0\),
\[
 \max_{1\le |m|\le CN}|p_m|/N\longrightarrow0.
\]
Otherwise select a subsequence of positive \(m=m_N\) with \(m/N\to t\in[0,C]\)
and \(|p_m|/N\ge\epsilon\); negative \(m\) follow by conjugation. For
fixed \(B>0\) put
\(Z_N=B^{-1}\int_0^B e^{2\pi i(m/N)y}(dX_N(y)-dy)\).
Integration against \(e^{2\pi im\alpha}\) makes the point phases
\(e^{2\pi im\theta_j}\); unfolding gives
\(|p_m|/N=|\mathbb E_\alpha(e^{2\pi im\alpha} Z_N)|\le\mathbb E|Z_N|\).
On this fixed interval the modulation may be replaced by \(e^{2\pi ity}\)
at \(L^1\) error at most twice its uniform difference, since
\(\mathbb E X_N([0,B])=B\). The count converges in law (Sine₂ has no atoms
at deterministic endpoints) and its expectations equal the limit's
expectation \(B\); hence these nonnegative counts are uniformly
integrable by truncation. The continuous-mapping argument for the
endpoint-discontinuous test and this integrability imply convergence of
\(\mathbb E|Z_N|\) to the corresponding Sine₂ expectation.
For \(f=\mathbf1_{[0,B]}e^{2\pi ity}\), the centered Sine₂ linear statistic
has variance
\(\int|\widehat f(u)|^2\min(|u|,1)\,du\le\|f\|_2^2=B\).
Hence \(\limsup |p_m|/N\le B^{-1/2}\). Let \(B\to\infty\) to contradict
\(\epsilon>0\). Stationarity alone is not enough; this uses Sine₂ variance
on the modulated windows. The converse is not claimed.

## Position in the record

The normalization and general factorial criterion belong to the
[trace-to-local-statistics bridge](../../../trace-bridge/trace_to_local_statistics_bridge.md);
the [earlier ergodic obstruction](../../../returns/return_trace_obstruction.md)
already proves sublinear-trace vanishing. The one-sided pair obstruction,
single-test upgrade, and extension of the necessary spectral bound through
fixed linear-frequency bands for Sine₂ are the specific points here. The result is analytic;
[finite Pell replay](../../../../computations/verification/bgs_f_november/research/)
checks a finite application, not the asymptotic implications.
