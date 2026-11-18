# Fixed-map review, 18 November 2026

The [sevenfold oldspace result](../../../mathematics/fixed-map/seven_oldspace_singular_spectrum.md)
uses the literal Jacobi generator and the established oldspace
intertwining. Quadratic hopping zeros yield packets at offsets of
order $\sqrt N$. The five independent discrete phase directions
and the remaining continuous direction give $c\sqrt N$ singular
values in each fixed neighborhood of $[0,1]$. This concerns a
one-step compression.

The [Pell witnesses](../../../mathematics/fixed-map/pell_microscopic_window.md)
bound the full signed band-two comparison at $h_{197}$, $h_{203}$,
and $h_{207}$. At $h_{207}$ the proof uses Weyl-orthogonal
commutator buckets and an autocorrelation bound for the entire CUE
subtraction. The matrix size is approximately $8.58\cdot10^{78}$.
The certificate uses support labels and integer arithmetic.

## Executions

Run these commands from the repository root.

| Check | Result and coverage |
|---|---|
| `python computations/verification/pell_window/verify.py` | Passed with integers and exact fractions. Checks the modular return, cover bounds, covariance, all three commutator bucket bounds, and the reference integral and discrete comparison. |
| `python computations/verification/oldspace_outliers/verify_gradient.py` | Passed with rational cyclotomic algebra. Checks the rank-five gradient array, collective curvature and hopping jets. |
| `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python computations/verification/oldspace_outliers/verify_compression.py` | Passed in binary64. Reconstructs the Weyl matrix from the raw symbol and checks the intertwining and Duhamel bound at $N=147,245,343$ with test couplings $0.025,0.1,0.075$. Also checks the cutoff plane-mode residual at zero and nonzero field. |
| Compile [phase_moments.cpp](../../../computations/verification/oldspace_outliers/phase_moments.cpp) with `g++ -std=c++20 -O2` and run | Passed. Counts ordered word pairs through length six with exact integer multinomial weights. |
| `lean formalization/Bgs/OldspaceOutliers.lean` | Passed in Lean 4.33.1. Kernel checked the integer relation, Laurent polynomial derivatives, first possible uniform word excess and the Haar net factor. |
| `lean formalization/Bgs/PellWindowWitness.lean` | Passed in Lean 4.33.1. Kernel checked the cleared width, trace, band-two and Abel gap comparisons and squarefreeness of $h_5=41$. Python checks the bucket enumeration and integral comparison. |

The Lean modules cover these arithmetic ingredients. The analytic
arguments and limits have written proofs. The binary64 cases verify
conventions and local estimates at their stated test parameters.

## Manuscript

The consolidated manuscript built successfully with pdfLaTeX in three passes.
The builder reported 380 pages. PDF SHA-256
`a3117d0b68ed81e76be538a90a934e1512b358d58a6dfcf1e65fab31011fc49b`.
The build covers typesetting and cross-references.

## Scope

An oldspace singular value describes the two subspaces at one step.
Successive propagation depends on the orientation of the input and output
directions. The Pell proof uses the finite parameter $h_{207}\tau$,
whereas $h_k\tau$ eventually diverges. BGS-TRACE-005 and BGS-BGS-001
remain open. An asymptotic proof needs control of the complete signed
sum, and an asymptotic disproof of weak convergence needs a discrepancy
for a bounded observable or separate control of moment tails. The
[standalone problem](../../../record/remaining_breakthrough_task_20261021.md)
now states this distinction. The two notes have no external referee report.
