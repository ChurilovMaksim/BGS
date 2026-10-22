# The full form-factor curve in L² for frozen CUE and CSE backgrounds

**Stable claim:** BGS-TRACE-070. **State:** PROVED.
**Boundary:** Mean L2(0,T) convergence of the ceil(N*tau) interpolation and all-time individual CSE MSE control. No expected temporal supremum; floor interpolation with n=0 is excluded. The limiting curves are prior work.
**Integration and review:** [11 October disposition](../archive/record/chat_integration_20261011.md).
**Original input:** [dated source](../evidence/executions/20261011/chat-research/original/jack_phase_2026_10_11/form_factor_curve.md).


Fix T<∞. For τ>0 use a positive trace order

\[
k_{N,Q}(\tau)=K_{N,Q}(\lceil N\tau\rceil),\qquad
\overline k_{\beta,N}(\tau)=\overline K_{\beta,N}(\lceil N\tau\rceil).
\]

The value at τ=0 is immaterial. Using the actual zero trace order on an
interval of length 1/N would introduce K(0)=N and destroy the L² limit;
the ceiling convention avoids that issue.

The all-positive-time bounds in `exact_cumulants_20261011.md` and Tonelli give

\[
\mathbb E_Q\|k_{N,Q}-\overline k_{2,N}\|_{L^2(0,T)}^2
\le T\frac{1-1/N}{N+1},
\]

and

\[
\mathbb E_Q\|k_{N,Q}-\overline k_{4,N}\|_{L^2(0,T)}^2
\le T\frac{[2+\frac12\log(2N-1)]^2
+[2+\log(2N-1)]/(8N)}{N+1/2}.
\tag{1}
\]

For CUE the limiting curve is K₂(τ)=min(τ,1); its finite annealed curve
differs uniformly by at most 1/N.

For CSE, counting N distinct eigenvalues, the known limiting mean curve is

\[
K_4(\tau)=
\begin{cases}
\frac\tau2-\frac\tau4\log|1-\tau|,&0<\tau<2,\ \tau\ne1,\\
1,&\tau\ge2.
\end{cases}
\tag{2}
\]

Its value at τ=1 can be assigned arbitrarily for an L² statement. At exactly
that trace ratio the finite mean grows like log(N)/4; no finite pointwise
limit is claimed. With the pair-counting convention the plateau starts at
n≈2N; the 1999 source calls the singular point n=N half the Heisenberg time.

Here is a direct L² verification from the exact finite mean. For
0≤d<N, integral comparison gives

\[
\sum_{j=d}^{N-1}(j+1/2)^{-1}
\le2+\log\frac N{d+1}.
\tag{3}
\]

For d=0 separate the first term and use the midpoint bound
1/(j+1/2)≤∫_j^{j+1}dx/x for j≥1. For d≥1 use the same bound to obtain
log(N/d), and then log((d+1)/d)≤log2<2.

Take n=ceil(Nτ) and d=|N−n|. Since d+1≥N|τ−1|, the exact finite mean
and (3) are dominated, away from the measure-zero point τ=1, by

\[
C_T\left[1+\log_+\frac1{|\tau-1|}\right].
\tag{4}
\]

For n≥2N the finite mean is simply one after division by N. The square
of (4) is integrable on every (0,T). The harmonic sum converges to
−log|1−τ| at every fixed 0<τ<2, τ≠1. Dominated convergence consequently
gives

\[
\|\overline k_{4,N}-K_4\|_{L^2(0,T)}\longrightarrow0.
\]

The conditional error has mean zero at each time, so its cross term with
the deterministic annealed bias integrates to zero. Combining this fact
with (1) proves

\[
\boxed{\mathbb E_Q\|k_{N,Q}-K_\beta\|_{L^2(0,T)}^2
\longrightarrow0,\qquad\beta=2,4.}
\tag{5}
\]

This establishes the complete curve as an L² function of rescaled time,
including the integrable CSE logarithmic singularity. It is stronger than
checking a finite list of times. It does not imply a temporal supremum,
uniform convergence near the singularity, or a result for a prescribed
deterministic chaotic propagator.
