# Fixed-map BGS research cycle — 25 September 2026

## Target contract

The ambitious objective is the full microscopic BGS law for the **specified**
odd-dimensional propagators $U_N=e^{i\tau N A_N}M_N$ at unchanged
$\tau=10^{-80}$, after the stated symmetry reduction and unfolding, at
every fixed correlation order and for all Schwartz tests. The exact
model, normalization and sufficient weighted Heisenberg joint-trace
condition are in [`fixed_map_resolvent_frontier.md`](../mathematics/fixed_map_resolvent_frontier.md),
[`trace_to_local_statistics_bridge.md`](../mathematics/trace_to_local_statistics_bridge.md),
and claim `BGS-TRACE-005`. Success means proving that condition, or a
different complete route to the same local law, for this actual family.
The pair Abel formula is an independently necessary target. A fixed
short-time bound, a finite CUE-like statistic, or an exact symmetry
exclusion does not meet the contract.

The phrase “all chaotic systems” requires a separate theorem with an
explicit class of classical systems, quantization, limiting sequence,
desymmetrization, symmetry class and unfolding. Classical hyperbolicity
by itself cannot be taken as such a theorem: the arithmetic spectral
construction in
[`general_hyperbolic_prime_spectra.md`](../mathematics/general_hyperbolic_prime_spectra.md)
produces large repeated eigenvalues of certain hyperbolic cat-map
quantizations on logarithmic-period subsequences, even after the
specified parity split. The same maintained note constructs a separate
fixed-strength nonaffine smooth Anosov perturbation, smoothly conjugate
to an arithmetic cat map, whose polynomial-time quantum powers remain
superpolynomially close to that arithmetic quantization and whose
parity-sector microscopic correlations cluster. That is an internally
derived exception to an unqualified “all chaotic maps” slogan, **not**
an arithmetic-free counterexample to a generic BGS formulation and
**not** a resolution of the distinct fixed nonlinear family in this
research cycle. This existing project result has not received an
external line-by-line referee audit here.
The earlier primary source by [Kurlberg and Rudnick, *Hecke theory and
equidistribution for the quantization of linear maps of the torus*,
arXiv:chao-dyn/9901031](https://arxiv.org/abs/chao-dyn/9901031)
independently documents large degeneracies of quantized hyperbolic
cat maps at certain Planck constants and their Hecke symmetries; it is
background context, not an input proving the maintained nonlinear
construction.

## Three routes, cheap falsifiers and outcomes

| Route | Intended mechanism | Cheapest decisive test | Disposition |
|---|---|---|---|
| Moment/rigidity sufficiency | Combine simple phases, exact nonzero traces and the necessary Gram benchmark $G_N\to4/3$ to infer the CUE pair limit. | Find a simple abstract spectrum satisfying all three with a non-CUE Abel limit. | **Refuted as a universal implication.** The odd two-clock construction, `BGS-TRACE-008`, meets all three, is macroscopically Haar, and has unit-interval occupancy at most three, yet its Abel limit decays exponentially as $s\to\infty$. Its even companion matches the *exact* finite-$N$ CUE expectation of $G_N$. This is no counterexample to the actual map. |
| Seven-cut resolvent comparison | Transfer spectral information from the actual full $U_N$ to the seven-cut full $V_N$ without treating generator paths as independent spectra. | Differentiate the exact pair identity and estimate the error when the hyperbolic resolvent parameter is replaced by $s$. | **Closed as a transfer theorem** (`BGS-RES-007`): on each compact $s$ interval, all fixed parameter derivatives of pair Abel differences are $O(\tau/\log N)$, and those of scalar-resolvent differences are $O(\tau/\log N+1/N)$. No actual CUE limit for either full propagator follows. |
| Direct Heisenberg/mixed loops | Extend model-specific trace cancellation to $m\asymp N$ or bound the mixed-sign resolvent residuals. | Insert the existing logarithmic-time trace bound into the pair Abel sum, and inspect the first mixed loop identity. | **Open missing implication.** The bound $|p_m|\le C N^{39/40}$ for $m\le c\log N$ contributes at most $O((\log N)N^{-1/20})$ to the Abel sum. The exact second-level mixed residual also contains the unsolved signed cubic $N^{-3}\sum_{a,b\ge1}q^{a+b}p_{-a}p_{-b}p_{a+b}$. Neither the short-time input nor the new scalar-resolvent transfer controls this expression. |

**Exponent check in the last row.** Each of at most $c\log N$ terms of
$N^{-2}|p_m|^2$ is at most $C^2 N^{-1/20}$ because
$2(39/40)-2=-1/20$. Thus the stated $O((\log N)N^{-1/20})$
is the justified exponent; no cancellation in that range is needed.
The remaining Abel mass is supported beyond logarithmic time if a
positive target limit holds. This localization does **not** imply its
existence or value.

The first mixed residual is exactly

$$
\mathcal E_{2,N}(is/2,-is/2)=8i\left[
L_N(s)+N^{-3}\sum_{a,b\ge1}e^{-2s(a+b)/N}
p_{-a}p_{-b}p_{a+b}-\frac1{4s^2}\right].
$$

In particular, a scalar pair-resolvent estimate alone is insufficient
for the mixed hierarchy. The next decisive model-specific input would be
a signed joint-trace estimate in the order-$N$ time window for the **full**
propagator, with enough uniformity in frequency support to apply
`BGS-TRACE-003` and `BGS-TRACE-004`, or a direct all-order mixed-residual
bound satisfying `BGS-LOOP-001`. Neither has been proved here.

## Review and provenance

The two new maintained proofs are
[`two_clock_gram_falsifier.md`](../mathematics/two_clock_gram_falsifier.md)
and the `BGS-RES-007` section of the
[`fixed-map frontier`](../mathematics/fixed_map_resolvent_frontier.md).
The [maintained finite verifier](../computations/verification/gram_resolvent_normalization.py)
compares direct Toeplitz matrix norms, repeated-multiplication power sums,
the Poisson eigenphase-gap kernel and the hyperbolic adjoint resolvent at
dimensions 10, 11, 20, 21 and $s=1.3,2.5$; all eight cases passed.
Additional exploratory dimensions 80 and 81 were checked in scratch.
These samples only check finite normalizations, not the limiting theorem
or transcendence. The CUE Gram expectation is also derived directly from
the standard finite CUE kernel in the proof.
The resolvent differentiation is a consequence of the maintained
`BGS-FM-007` phase-coupling proof and the exact `BGS-RES-006` bridge;
its validity is conditional on those project proofs, which have
author-level and internal checks but no independent external referee
report. No new experimental evidence is used to upgrade their status.

Self-review focused on the possible normalization failures:

- The Toeplitz Gram identity counts $N-m$ upper and $N-m$ lower entries
  at lag $m$; it uses $N^{-3}$, whereas the Abel sum uses $N^{-2}$.
- At odd $N=2n+1$ the second peak $m=2n$ has weight **one** in the
  Gram sum and contributes $O(1/n)$; all other nonmultiples have
  $|p_m|=1$. For every *fixed* nonzero frequency, $p_m/N\to0$,
  verifying macroscopic Haar convergence without asserting CUE pairs.
- The extra point is chosen transcendental on the unit circle; the
  polygon points and their traces are algebraic. This proves exact
  nonvanishing for **all** positive powers, whereas a numerical
  separation test could only sample finitely many powers.
- In the resolvent bridge, the exact scalar summand is
  $c_N(s)/(y+b_N(s))$ with $c_N=\sinh(2s/N)/(2s/N)$ and
  $b_N=N^2\sinh^2(s/N)$, including the exterior factor $1/N$.
  The analytic error per summand is $O_K(N^{-2}/(1+y))$ on a small
  neighborhood of $K\subset(0,\infty)$; summing $N^2$ terms and dividing
  by $N$ yields $O_K(1/N)$, uniformly before differentiation.

After this cycle, `BGS-TRACE-005` and `BGS-BGS-001` remain **OPEN**.
