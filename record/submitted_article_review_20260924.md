# Audit of the submitted 87-page fixed-cat-map article (24 September 2026)

**Primary verdict for the requested microscopic sine-kernel and Abel
limits:** **INCOMPLETE**. The PDF itself explicitly leaves both limits
open. The smallest missing implication remains model-specific cancellation
of mixed joint traces at frequencies $m\asymp N$ for the fixed nonzero
kick (or a proved substitute determining all fixed-order correlations).

**Submission identity:** `quantum_cat_map_unified_article (1).pdf`, 87 pages,
20 embedded source/evidence files, SHA-256
`aeb0f82d35b3d40eb2e9a3fded9417c55df95e393f3de148f01457ecad844454`.
This is an author-level self-review. The PDF is a submission, not the
repository's source-of-truth ledger or an independently refereed article.

## Scope-by-scope verdict

| PDF section | Audited statement | Decision and maintained location |
|---|---|---|
| §§1–2 | Exact raw Weyl convention, corrected ordinary symbol, Jacobi path decomposition, no algebraic commuting projector away from 7 | Formula and rank already in `BGS-FM-001`/`BGS-FM-005`; checked for compatibility, no duplicate priority claim. Algebraic commutant is subsumed by total-minor theorem in `BGS-FM-008`. |
| §3 | Total nonvanishing of all minors of $M_N$ in the $A_N$ eigenbasis, simple $U_N(\tau N)$ spectrum and transcendental ratios at $7\nmid N$ | **Project proof with source-dependent Lindemann–Weierstrass input**, maintained as `BGS-FM-008`; p-adic balance and exterior-power contractions checked independently in prose and by finite regressions. No quantitative spectral gap. |
| §4 | Nonvanishing $\operatorname{Tr}[A_N,M_N]^3$ for every odd $N\ne7$; consequent common antiunitary obstruction | **Exact integer certificate plus checked implication**, maintained as `BGS-FM-009`. Only algebraic-entry antiunitaries reversing $U_N$ alone are excluded. Any finite unitary still has a spectral-basis antiunitary reversor. |
| §§5–7 | Partition Möbius bridge, CUE finite benchmarks, Schwartz tails and pair Abel equivalence | Corrected conventions match existing `BGS-TRACE-001`–`004` and fixed-map notes; useful exact benchmark $N^{-1}\operatorname{Tr}\Gamma_{N,N}^2\to4/3$ remains **OPEN for our $U_N$**. The Abel target is not proved. |
| §§8–11 | Positive residual around clock energy; Gram and positive-window formulations of the trace criterion; finite CUE benchmarks | Spot-checked representative displayed identities and the distinction between the deterministic target and Haar-CUE expectation. These are universal reformulations/benchmarks; no promotion to a new model-specific estimate. The positive residual is nonzero even in CUE. |
| §§12–17 | Special 7-divisible blocks, midpoint quantization, quantitative Egorov, displacement-map covering, logarithmic-time trace bound and Fejér window bound | Model-specific logarithmic trace estimate was retraced from raw Weyl multiplication and the displacement-covering argument and is included as a dependency in `BGS-FM-007`. The resulting long-time bound is still $O(N/\log N)$ for the Abel sum, far above the desired constant. |
| §§18–20 | Huge finite-size lower examples and abstract boundary constructions | Checked stated finite/asymptotic scope. A huge *finite* dimension is no subsequential counterexample; no BGS conclusion imported. |
| §§21–31 | Pell arithmetic response, Gaussian moment regime, nonlinear echo and commutator | The seven embedded exact programs reproduce finite identities; **the complete analytic Pell/echo argument was not independently audited here** and is not promoted as a new fixed-strength theorem. Its statements explicitly require separate shrinking-coupling/arithmetic regimes. |
| §§32–34 | Rank barriers, quantization precision, limitations | Compared the stated logical boundaries with existing fixed-map notes. They neither prove nor disprove CUE for the actual model. |
| §§35–36 | Trace-norm phase coupling, all-order microscopic stability, seven near-zero cuts, unconditional pair/Abel transfer | **Project proof after direct analytic and raw-matrix checks**, maintained self-contained as `BGS-FM-007`. Seven path projectors do **not** commute with the full $V_N$. |
| §37 | Proposed compact-frequency mixed joint-trace comparison | Still **OPEN**; exact trace/partition identity is a reduction, not its estimate. |

The reviewed strongest quantum/model-specific results are three separate
claims. Neither exact script output nor agreement among claims can upgrade
the missing main limit. This review asserts no novelty or prize-level result.

## Source, exact replay and independent finite checks

1. `pdfdetach -list` found 20 embedded files, including `article.tex`,
   seven checkers, two integer coefficient tables and result JSONs.
   `sha256sum -c SHA256SUMS.txt` passed **all 19 declared attachments**.
   The PDF itself is outside that checksums file and is pinned above.
2. In a clean scratch copy, each of `verify_certificate.py` and
   `verify_v2.py` through `verify_v7.py` ran with `python3 -S` and
   returned exit code zero. Their seven generated JSON result files,
   and the two generated certificate CSVs, were byte-identical to
   the PDF attachments. These runs confirm finite arithmetic, not
   asymptotic theorems. Maintained, attributed versions of the checkers
   relevant to the three claims are in `computations/verification/`.
3. A separately written matrix reconstruction summed the **raw** Fourier
   modes into $A_N$ and independently formed the Jacobi generator for
   $N=15,17,21,25,35,49$. Their maximal entry discrepancy was below
   $7\cdot10^{-15}$. The seven cuts had rank 12 for $7\nmid N$ and zero
   for $7\mid N$ at the expected nodes; nuclear bounds (2) of `BGS-FM-007`
   held. A numerical Duhamel check was run at auxiliary $t=0.17N$;
   it is a diagnostic, **not** a fixed-$\tau$ proof. The paper's actual
   $\tau=10^{-80}$ is retained in the analytic statement.
4. Independently evaluating the two attached Laurent polynomials at
   the relevant roots and assembling $\operatorname{Tr}[A_N,M_N]^3$
   from matrices for $N=3,5,7,9,15,21,25,35$ gave residuals below
   $5\cdot10^{-16}$. This checks the normalization of the exact
   certificate; exhaustive root exclusion comes from the integer code
   and the proved totient cutoff, not from this floating test.
5. Finite numerical total-minor inspections at $N=3,5,9,11,15$ did
   not find a zero among the tested orders. They do not prove the p-adic
   all-$N$ theorem.

The exact external leaf used in `BGS-FM-008` and the algebraic antiunitary
corollary of `BGS-FM-009` was checked directly in [Popescu,
*A simple and self-contained proof for the Lindemann–Weierstrass theorem*,
arXiv:2306.14352v2, Theorem 3.2](https://arxiv.org/pdf/2306.14352):
for distinct algebraic $\alpha_j$, the $e^{\alpha_j}$ are linearly
independent **over algebraic numbers**. It is not an effective lower bound.

## Dependencies, exclusions and handoff

`BGS-FM-007` depends on the exact model `BGS-FM-001`, the known Jacobi
decomposition `BGS-FM-005`, and a newly checked model-specific log-time
trace proof. Its universal transfer lemma also applies outside this model.
`BGS-FM-008` depends on the Jacobi path plus the precise external
Lindemann–Weierstrass theorem; `BGS-FM-009` depends on exact raw coefficients
and its reproducible finite certificate, with the same external theorem
used only for the algebraic-entry corollary.

**Remaining obligation:** prove, for the original $U_N$ **or** its exact
seven-cut partner $V_N$, the compact-frequency Heisenberg-time signed
joint-trace comparison of `BGS-TRACE-005` for every fixed order. Pairwise
Abel convergence is a necessary first milestone; simple spectrum, lack of
a common reversor and trace-norm proximity supply no required cancellation.
