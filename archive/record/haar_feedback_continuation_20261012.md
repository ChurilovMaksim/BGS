# An unconditional full-depth clock class

Research outcome, 12 October 2026.

[TRACE-076](../mathematics/haar_feedback_clock_law_20261012.md) closes the
all-time flatness probability premise for an independent Haar initial
unitary under the maintained fresh-phase, uniform-coordinate feedback
process. It also identifies the finite feedback derivative jointly with
the effective scattering matrix:
\[
S\sim\mathsf H_u,\qquad S\ \text{independent of }T,\qquad
T=I_u+X^*X,\qquad
d\mathbb P(X)\propto\det(I_u+X^*X)^{-(N+u)}\,dX.
\]
Here \(X\) is complex \((N-u)\times u\), and \(F_N(z)=zU_N\).
The outgoing delay has the same law and is separately independent of
\(S\); independence of the pair of delays or of different depths is
not asserted.

The nontrivial eigenvalues of \(T^{-1}\) have the complex Jacobi density
\[
\prod_{\ell=1}^{r} y_\ell^u(1-y_\ell)^{|N-2u|}
\prod_{\ell<j}(y_\ell-y_j)^2,\qquad r=\min(N-u,u).
\]
There are exactly \((2u-N)_+\) additional eigenvalues equal to one.
For \(N>u\), \(\mathbb E\operatorname{Tr}T^k<\infty\) exactly when
\(k<u+1\); \(\mathbb ET=(N/u)I_u\) for every \(u\ge1\).
These are exact finite-dimensional statements, not a compact spectral
edge assertion.

For \(\ell=\log(2N)\), \(m=\lceil\ell^{1+\kappa}\rceil\), the failure
probability of simultaneous \(K\ell/u\) entry flatness at every
\(u\ge m\) is at most
\[
b_N(K)=N^3(2N)^{-K(1-1/m)}
       =2^{-K}N^{3-K}(1+o(1)).
\]
This uses Haar marginals and a union bound, without independent depths.
The deterministic-initial-sequence scope of TRACE-060 gives a uniform
intersection estimate that can be integrated over initial laws.
The incoming/outgoing diagonal laws at each fixed power, off-diagonal
and mixed-entry decay, and the empirical full-depth clock measure are
therefore unconditional in probability for a Haar start.

The same clock conclusions hold for every independent initial law
\(\nu_N\) with \(D(\nu_N\Vert\mathsf H_N)=O(\log N)\).
For \(o(\log N)\) entropy, flatness itself holds with high probability
for each fixed \(K>3\). For \(O(\log N)\) entropy the clock conclusion
uses \(K\to\infty\) after \(\limsup_N\); it does not prove high-probability
flatness for one prescribed finite \(K\).

This identifies a genuine boundary. Conditioning Haar on a void in one
prescribed microscopic arc of unfolded length \(c<1\) costs at most
\(-\log(1-c)\) entropy. It preserves all clock conclusions but precludes
a Sine₂ limit at that origin. No conclusion about origin-averaged
statistics follows from this example. A deterministic initial unitary
has infinite relative entropy with respect to Haar. The maintained
deterministic map's trajectory probability, full physical TRACE-055,
signed TRACE-005 and global BGS remain open.

The [packet](../evidence/executions/20261012/haar-feedback/README.md)
preserves independent reconstruction, the exact maintained transfer
input, two explicit editorial clarifications, bounded exact controls,
an actual Wolfram response and the preceding failed CI. That CI omitted
TRACE-074/075 from the explicit integration epoch; the repair adds their
reviewed state/source rows and TRACE-076 while preserving the historical
wrappers. Mathematical acceptance, finite controls, typesetting and
final-source CI have separate scope.
