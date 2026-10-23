# Direct attack on the signed Heisenberg statistic

**Stable claim:** `BGS-CUE-002`. **Integration review:** 16 October 2026, author self-review.

**Exact scope:** Exact deterministic derivative and CUE reference covariance. Proxy computations are diagnostics, not a physical limit or a p-value.

Canonical status is [the claim ledger](../record/claim_ledger.md); source `S10` is preserved verbatim in [the imported record](../archive/history/2026/chat_20261015/BGS_complete_research_2026-10-15.md#s10). Original execution counts are historical; fresh execution is recorded in [the integration receipt](../archive/evidence/executions/20261016/chat-integration/receipt.json).


Date: 15 October 2026.

**Status: the fixed-coupling BGS conjecture is not proved here.** This packet contains a direct finite numerical probe of the required statistic, exact reference-ensemble algebra, and an explicit examination of the parameter-transfer step. It contains no assertion that numerical data, one-step dispersion, or a smoothed law establishes the deterministic microscopic limit. The repository was not changed.

## 1. Exact model versus numerical parameters

The mathematical target remains

\[
 U_N(\tau)=e^{i\tau N A_N}M_N,\qquad \tau=10^{-80},\quad N\ge3\text{ odd},
\]

with

\[
 r(q)=(1-\cos14\pi q)(1+\cos2\pi q),\qquad e^{i\alpha}=(-3+4i)/5,
\]
\[
 g(q,p)=\cos14\pi q+r(q)/10+r(q)\sin2\pi q/100-1/10
       +r(q+1/2)\cos(2\pi p-\alpha)/100.
\]

The code uses the exactly corresponding cyclic Jacobi matrix, with all inverse-of-two and inverse-of-eight operations taken modulo the odd dimension. In particular, its upper edge is

\[
 (A_N)_{x,x+1}=\frac{e^{-i\alpha}}{200}
 r\left(\frac{(x+2^{-1})\bmod N}{N}\right),
\]

and its diagonal is the coordinate part of g. The metaplectic factor is

\[
 (M_N)_{xy}=N^{-1/2}e_N[-8^{-1}(3x^2-2xy+3y^2)].
\]

The executed numerical parameters are **0.03 and 0.30, not 10^-80**. The matrix formula is unchanged but its coupling is changed for the diagnostics. The program does not claim the proxy classical maps satisfy the project's proven very-small-coupling Anosov hypotheses. No extrapolation to the literal fixed coupling is made.

## 2. The quantity tested

For a nonnegative smooth compactly supported weight w, the necessary pair comparison is

\[
 J_{N,w}(\tau)=N^{-2}\sum_{m\ge1}w(m/N)
 \left(|\operatorname{Tr}U_N(\tau)^m|^2-\min(m,N)\right).
\]

The four bands are (0.08,0.40), (0.75,1.25), (1.20,1.80), and (0.08,1.80). In a band (a,b) the weight is

\[
 w(t)=\begin{cases}
 \exp(1-1/(1-x^2)),&|x|<1,\\
 0,&|x|\ge1,
 \end{cases}\qquad x=(2t-a-b)/(b-a).
\]

The entire signed sum is evaluated. Resonance diagnostics are recorded separately but not deleted and not required to vanish. The last three bands test the reference plateau as well as the initial ramp.

Eigenphases are extracted by complex Schur decomposition, with residual and unit-circle checks. Traces of powers are independently checked against direct matrix powers at N=19,31,63. These floating-point residuals are numerical diagnostics, not interval-arithmetic enclosures of an asymptotic limit.

## 3. Exact dependence on the parameter and the attempted transfer

For fixed N, differentiation of the matrix exponential and trace cyclicity give

\[
 \partial_\tau\operatorname{Tr}U_N(\tau)^m
   =i mN\operatorname{Tr}(A_N U_N(\tau)^m).
\]

Consequently the full signed statistic has the exact derivative

\[
 \boxed{\partial_\tau J_{N,w}(\tau)=
 -\frac2N\sum_{m\ge1}m w(m/N)
 \operatorname{Im}\left[\operatorname{Tr}(A_NU_N(\tau)^m)
                  \overline{\operatorname{Tr}U_N(\tau)^m}\right].}
\]

All sums are finite. Integration over a real parameter interval is therefore legitimate at each fixed N. However, no estimate of this complete signed mixed trace sum, uniform enough for fixed parameter intervals, was proved.

The unconditional norm bound yields only

\[
 |J_{N,w}(\tau)-J_{N,w}(\sigma)|
 \le 2\|A_N\|_{\rm op}N |\tau-\sigma|
             \sum_m m|w(m/N)|
 =O_w(N^3|\tau-\sigma|).
\]

Here one may use the established model bound ||A_N||op <= 79/50. This gives a sufficient continuity scale o(N^-3). **It is not a necessity or optimality assertion**; a better model-specific estimate might exist. It does show that this argument does not transfer any numerical observation at a fixed proxy coupling to 10^-80. Qualitative algebraic nonvanishing does not bound the signed integral above either.

The derivative formula was checked against centered finite differences on the exact model at N=19,31,63. Such checks certify neither the missing uniform bound nor the N limit.

## 4. CUE calibration at every positive frequency

The exact mean is E_CUE |Tr V^m|^2=min(m,N). To avoid using the stable-range fourth moment outside its scope, the full covariance is used:

\[
 \boxed{\operatorname{Cov}(|p_m|^2,|p_n|^2)
 =\delta_{mn}\min(m,N)^2
 +2(N-\max(m,n))_+-(N-m-n)_+-(N-|m-n|)_+.}
\]

This is reference-ensemble algebra, not a distributional assertion about the deterministic U_N. In the stable range m+n<=N its last three terms sum to zero, consistently with the Diaconis--Evans moment identity.

For completeness it follows directly from the finite CUE determinant. Put F=sum t_j exp(i k_j theta), let P_N project onto Fourier labels 0,...,N-1, and expand

    log E_CUE exp(sum_j t_j p_(k_j))
      = Tr log(I+P_N(exp(F)-1)P_N).

For four labelled frequencies (m,-m,n,-n), the coefficient of t_1 t_2 t_3 t_4 is the sum over all 75 ordered set partitions. A partition into l blocks contributes (-1)^(l-1)/l times the trace of its product of Fourier shifts and projections. Since the total shift is zero, that trace equals

    (N - [maximum partial shift - minimum partial shift])_+.

Writing F_c=(N-c)_+ and taking m>=n, the four partition-length contributions are

| l | Contribution |
|---|---|
| 1 | F_0 |
| 2 | -F_0-2F_m-2F_n-F_(m+n)-F_(m-n) |
| 3 | 6F_m+2F_n+4F_(m+n) |
| 4 | -2F_m-4F_(m+n) |

Their sum is 2F_m-F_(m+n)-F_(m-n), the fourth joint cumulant. The additional Wick contraction is delta_(mn) min(m,N)^2, proving the covariance formula. Equal frequencies are handled by retaining all four labelled positions before combining equal arguments.

The reference standard deviation of J is computed from this full covariance. It is NOT a p-value, posterior probability, confidence interval for a deterministic theorem, or an assumption that U_N has a Haar law.

The separate exact-arithmetic checker verifies all 18,375 choices N=1,...,15 and m,n=1,...,35 by summing the 75 ordered partitions. This is an independent finite control on the displayed general derivation.

## 5. Outcome and unresolved step

The available one-step estimate bounds matrix elements of K=Ad(Q_N) in the Weyl basis. The true pair quantity instead involves

\[
 |\operatorname{Tr}U_N^m|^2
   =\operatorname{Tr}_{HS}[(K R)^m],
\]

where R=Ad(M_N) permutes the Weyl labels. Products contain correlated amplitudes along all closed paths. Pointwise decay of K, orbit averages of its diagonal probes, and an auxiliary heat law do not estimate those cyclic products.

The quantum-graph route was also checked against its averaging hypotheses. Its wave-number / independent bond-phase average is not supplied by the random choice of a single observation origin for this fixed spectrum. Applying such an ensemble theorem to the present U_N without a proved transfer would change the problem.

No bound proving J_N,w(10^-80)->0 was obtained in this pass. No higher signed factorial comparison is asserted. The full Heisenberg-scale dynamical input, rather than the deterministic Fourier bridge or the factorial truncation, remains the gap. Numerical agreement at proxy couplings is kept separate from this conclusion.

## 6. Reproduction and receipts

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -O pair_probe.py
    python -O cue_covariance_check.py

The final probe is self-contained and has no imports from other research packets. Its default sizes are the completed sizes 127,251,509,777,1009. An additional N=2003 attempt exceeded its wall-time budget before producing a result; none is claimed. The 10 saved records through N=1009 were completed. A separate final self-contained smoke test ran N=19,31 successfully.

Source context, not a completed-proof claim:

- P. Diaconis and S. N. Evans, Linear Functionals of Eigenvalues of Random Matrices, Theorem 2.1, Berkeley report 577: https://statistics.berkeley.edu/sites/default/files/tech-reports/577.pdf . The stable moment theorem is used only within its stated range; the all-frequency covariance above is derived explicitly.
- Z. Pluhar and H. A. Weidenmuller, Quantum Graphs and Random-Matrix Theory, arXiv:1407.1148. Wave-number and bond-phase averaging are not identified with a single global origin average here.
- ChurilovMaksim/BGS, mathematics/heisenberg_pair_heat_formula.md, main e20825f15b62c403ddb52ef345aa48e339eda21d. Its exact smoothed formula does not estimate the unsmoothed statistic at the fixed initial matrix.
- Prior supplied scale-normalized-overlap THEOREM.md, 15 October 2026, explicitly distinguishes one-step Weyl dispersion from the open trace of powers.
