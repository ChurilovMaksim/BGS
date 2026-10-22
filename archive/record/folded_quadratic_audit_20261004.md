# Final proof audit: TRACE-012

Date: 4 October 2026. Primary verdict: **proved as written in the audited
revision**, with author self-review only. No external referee, delegated
independent audit or compiled analytic proof is claimed.

The normalized claim is: for every finite unitary spectrum, positive
integer d and fixed compact smooth complex weight in the positive cone
with 2b<1, its complete signed three-strip cubic obeys
$|Z(W)|\le C_W\sqrt{EG_d}$, where $G_d=\|P_d(\rho^2)\|_2^2$.
The retained finite factorial budget gives the explicitly conditional
sector-deletion criterion. A separate convex-count theorem turns any
K block phases in an epsilon*d/N arc into the stated positive r-point
factorial mass. The frozen-map conclusion is a finite certificate at
p=239; no actual-map asymptotic statement is asserted.

## Audited revision and dependency closure

- Proof SHA-256 before the byte repair below: `c3aeb3048aaf4d9d6aab95511d6b6302a567aa67ccf423779425ee116be2628a`.
- Verifier SHA-256: `18af2caa7752588884e2b5d29baf0a9f249a97f27407531922a87428fca058b8`.
- [Canonical proof](../mathematics/folded_quadratic_resonance_control.md),
  Sections 1--7; equations (1)--(17), including (11a).

| Leaf | Role and disposition |
|---|---|
| TRACE-011, Sections 1--2 | Internal proof of smoothing/filter conventions and exact factorial budget. The stochastic CUE-background construction is not required here. |
| TRACE-009, Sections 1--3 | Internal oriented block/order identities; gives the actual E, without estimating it. |
| FM-001 and TRACE-001 | Maintained frozen Jacobi symbol and factorial normalization. |
| Positive projection, Young, divided differences and convex counts | Elementary arguments reconstructed explicitly in the new proof. |
| p=239 arithmetic and symbolic series | Finite exact computation corroborates the explicit algebra; does not imply an asymptotic theorem. |
| Actual E/G decay and nonresonant cancellation | Open inputs, outside the proved universal inequalities and finite application. |

No circular closure edge to TRACE-005 is added. No unchecked external
source supplies a leaf needed for the new elementary argument. Related
literature is credited in the separate source note.

## Obligation matrix

| Obligation | Status | Decisive check |
|---|---|---|
| Reflection, normalization and frequency signs | passed | Gaussian Fourier coefficient is $e^{-(m/N)^2}T_m/N$; direct sums vs FFT and trace convolution. |
| Positive product majorants | passed | Probability-kernel Jensen followed by averaging and L2 contraction; covers complex filters. |
| Projection orientation and sum strip | passed | Move the self-adjoint projection onto the product; exact union indicator has common coefficient -2. |
| General smooth W | passed | Compact cutoffs and Fourier inversion; modulation translates kernels with uniform L1 norm. |
| Factorial vs raw traces | passed | Exact TRACE-011 budget retained, including Q/d; E/G decay is a sufficient premise. |
| Common scalar phase of C | passed after explicit clarification | Rotate original phases by a d-th root of the removed scalar; E,Q,G stay unchanged. Two direct phase controls added. |
| Root-allocation identity | passed | Direct reindexing and $1\le B_d\le d$; same C with a d^2 energy ratio refutes omission. |
| Strict improvement | passed | Separated Gaussian autocorrelation gives G=O(L), while EM4 grows at least linearly; small simple perturbations preserve both facts. |
| Minimum/exceptional parameters | passed | Empty bands, d=1, d>N, r>N and zero-width arcs give the stated trivial bounds without division by zero. |
| All count allocations | passed | Discrete second difference proves convexity; 15,500 exhaustive finite allocations corroborate the balancing formula. |
| Shrinking-cube limit | passed | Fixed smooth positive neighborhood first; no moving-test or weak-process inference. |
| Finite CUE vs Sine reference | passed | Probability-frequency Gram proof applies to each; finite normalization is retained. |
| Actual 1e-80 coupling | passed for finite certificate | Analytic row norm and telescope; never represented by a float kick rounded to I. |
| Heisenberg asymptotics and full BGS | not addressed by these theorems | Actual mass/energy estimates and the complete signed hierarchy remain open. |

The scalar-phase clarification is a definition repair, not a restriction
on the spectra. The original U remains unchanged; phase rotation is used
only for the exact block-density representation and preserves its energies.
The new finite check also verifies that the Sine determinant coefficients
of degrees below six vanish, rather than checking only the sixth coefficient.

## Strongest safe outcome and next check

The universal inequalities, exact crowding diagnostic and finite map
certificate stand at author-proof level. Their computation ranges and
actual execution are recorded separately in the execution packet.
Next prove actual resonant mass decay with the shifted four-point energy
control, or bypass this sufficient condition using signed cancellation.
A genuine obstruction needs an infinite subsequence of shrinking-arc
crowding. Neither input has been supplied. BGS remains OPEN.

## Byte-level correction before publication

The first local audit commit (`341faf4`) contained one bare carriage-return
byte in the factorial-measure label constraint. Text normalization during
publication serialization exposed the mismatch before GitHub main was moved.
The label now uses `\mathrm{distinct}`; the mathematical definition and all
theorems are unchanged. A byte scan of every file in the publication delta
found no other unexpected control characters.

- Current proof SHA-256: `da2d21727000c9b248977c68e63d7e2596c689c006407eb68c0e05edb3e46ebc`.
- [Corrected finite checks](../evidence/20261004/folded_quadratic_checks_corrected.json).
- [Current source manifest](../evidence/20261004/folded_quadratic_manifest_corrected.json).
- [Correction execution record](../evidence/executions/20261004-folded-quadratic-format-correction.json).

The previous check output, manifest and execution packet remain unchanged as
historical evidence. The correction packet records the rerun and the unchanged
TeX/PDF fingerprints. Publication is checked against raw UTF-8 bytes and Git
blob/tree hashes, without newline normalization.
