# Independent internal review: quantitative collective diffusion

**Claim:** BGS-FM-019. **Base main:**
`a3d73edf6fd26485325405d4d24197730c76e9f7`.
One fresh read-only reviewer received the exact raw proof and conventions,
without the author's conclusion or numerical spectra. The reviewer
reconstructed D1--D25, then checked the parameter and outer-boundary
clarifications in a second pass. These are two passes by one internal
reviewer; no external referee report or formal certificate is claimed.

**Verdict: proved as written** for the accepted mathematical body.
There is a universal c_0>0 on the whole complement of identity/swap,
for every odd N>=3. The explicit refined shared-noise ensemble has
mass c_0 N^-alpha/4 at m=N^3, 0<alpha<1. No corresponding original
deterministic spectral conclusion follows.

## Reconstructed obligations

| Obligation | Independent check | Boundary |
|---|---|---|
| D1, D5--D8 | Collective complex commutators, total-label blocks, translation/gauge and both cross holonomies | Every odd N, including negative centered labels and composite dimensions; physical and diffusion Hamiltonian names distinguished |
| D9--D14 | Rectangular averaging, corner overlap, annular mean comparisons, geometric Hardy summation and outer antiperiodic cycle | Universal bound; no log loss; central connected patches and all odd N<65 closed by direct paths |
| D2, D15--D16 | Odd labels controlled by the cross twist; even nonzero labels by exact two-dimensional compression and the 1/32 dichotomy | Entire Q_N, not only a smooth or typical subspace; sole kernel in kappa=0 is I,swap |
| D17--D19 | Pair-generator zeros, punctured row/column partitions and their complete overlap spectrum | Principal angle N^-1/2; distinct sine values and wrap phases require odd N |
| D3 | Positive pair eigenvalue separation and the two contraction-loss argument h<=5 beta | Explicit original m=1 lower bound only; its weakness does not disprove a stronger rate |
| D20--D23 | Exact Gaussian averaging with shared variables, 128 pi N^3 commutator bound, contraction Trotter estimate and microscopic singular mass | Higher-copy law is explicitly changed by subdivision; no normality needed; copies and matrix powers keep their common variables |
| D24--D25 | Aliased Fourier energy, exact one-copy equality and the inherited one-step Egorov direction | Fixed smooth observables in normalized HS mean square; no long-product Egorov or microscopic spectral continuity |

The core annular proof was independently checked as follows. Averaging
vertically in a right rectangle costs r^2 and is absorbed by y^2.
The ratio of the full z-height to the corner-window length is bounded,
so horizontal averaging introduces no extra factor r. Corner overlaps
have comparable r^2 vertices. Ring masses grow geometrically as 4^j;
the weighted Hardy kernel sums to 2, giving squared norm at most 4.
The exterior antiperiodic cycle pins the final mean. Half-integral
boundary points at max(|y|,|z|)=N/2 are explicitly included.

For even nonzero labels, the reviewer recomputed the two coordinate
forms on c 1+d delta_0 and obtained exactly D16, P_0 R P_0>=K/2 and
R<=4K. The split by ||v||^2>=||u||^2/32 gives c_*/66. The N=3
case has no even nonzero centered label. No missing parity sector was
found. The commutator estimate was independently derived from four
product-commutator terms, ||ad S||<=4 and each cross commutator <=8 pi/N.

## Dependencies and acceptance pins

D2--D23 use internal finite Weyl algebra, the fully stated lattice
lemma, projection algebra, Gaussian integration and contraction Duhamel.
No externally imported gap theorem or finite spectrum is needed.
D25 additionally inherits FM-018 O8 and the actual physical quantization.
The full FM-001/FM-006 classical proof closure was not re-audited here;
their mixing input is unnecessary for the new diffusion gap.

| Version | SHA256 |
|---|---|
| Full first accepted candidate, including refined N^3 commutator schedule | `fbc1e841699d53387669a74a8c46ea0784920f36e8780662a66bc2de23c78c49` |
| Accepted candidate with u,m domains, N=65 ring threshold and half-grid boundary included | `0d442f379feb8e58f02babf6b841d4fd03d59270123dcfd006a8f3ff03ee5241` |

The promoted source changes only its introductory status/links; its
mathematical body from `## 1. Exact objects and conclusions` is compared
byte-for-byte with the accepted version. The final body and promoted
file hashes are recorded in the integration receipt. Pins identify
what was reviewed; they are not mathematical certificates by themselves.

## Computation and limits

The author executes the maintained exact
[checker](../computations/verification/collective_diffusion_gap.py)
under a pinned [contract](../evidence/20261006/collective_diffusion_contract_v2.json).
Coordinate commutators catch representation/sign errors; cyclotomic
gauge checks include wrapped edges; projection eigenvectors and finite
Hardy matrices use exact rational arithmetic. These finite controls
do not prove the uniform annular lemma or an asymptotic spectrum.
The reviewer ran no spectrum computation and changed no file.

Before publication, the author found that negative integer powers of -1
in the initial gauge checker produced Python float sign values. The signs
were exact-valued +1.0 or -1.0, but the implementation violated the
declared Fraction-only domain. Integer parity signs and explicit type
guards now enforce that domain, and a new bounded v2 run repeats every
case. The [correction record](history/2026/collective_diffusion_arithmetic_correction_20261006.md)
preserves the initial checker and unmodified v1 protocol as superseded
evidence. No analytic formula or accepted mathematical body changed.

The separate [diagnostic script](../computations/experiments/collective_diffusion_spectrum.py)
uses float64, a deterministic sparse starting vector and declared finite
coverage. Its larger dimensions cover selected blocks only. An earlier
ignored preliminary run used the sparse library's implicit starting-vector
choice; its contract did not declare that choice, so it is not promoted
as reproducibility evidence. The maintained deterministic replay corrects
that implementation/provenance issue without using numerical values as
proof. Source attribution and priority limits are separate.

The m=1 Heisenberg rate, full nonlinear determinant functional,
higher-copy quantitative bounds and original signed spectrum remain open.
The refined two-copy result is a substantive auxiliary checkpoint;
TRACE-005 and BGS-BGS-001 retain their OPEN status.
