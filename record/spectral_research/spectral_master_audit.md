# Review of the external spectral research snapshot

**Date:** 21 October 2026. **Review provenance:** direct reconstruction and
self-review in this session; no new independent reviewer, external refereeing
or Lean certification. The other research session is still active: this report
applies only to the supplied snapshot.

## 1. Input, coverage and disposition

Input: `Spectral_research_master (2).md`, 7,941,879 bytes, 242,811 lines;
SHA256 `10b90c7d12668cd7327bcc08bda292f4c7d6cf82218ee95d5d4f7603fac86cef`.
The file contains twelve research rounds, large computational outputs,
embedded historical books and source-level internal audits. It is not a
single short proof. The machine inventory identifies 265 explicitly delimited
included-source blocks; historical-book blocks themselves contain further
appendices. All 207 blocks with recognized explicit SHA256 metadata were
recovered byte-exactly and verified. This verifies packaging, not mathematics.

**Whole-document verdict: review incomplete.** Only the bounded scope below
has been mathematically accepted in this pass. Earlier rounds, especially
claims about all fixed powers, original spectral simplicity, growing-order
character sectors, Clifford gaps and the complete Pell commutator sum, are
not certified merely because later reports call them proved. The inventory
retains their review status. No blanket promotion of the master took place.

The latest principal physical-kick theorem is **proved as written** at its
stated scope, and is strengthened in the maintained proof. The original
microscopic BGS / H_diag assertion remains **incomplete**, exactly as the
author states: even the displayed fixed pair defect has not been evaluated.

Repository comparison base:
`2f2a2ee937e66e5f11846f43a060273b4b08e106`. The applicable source-of-truth
rules, research brief, claim ledger, registry, theorem index and open questions
were consulted. A text search across authenticated current proof files checked
for an existing physical-kick trace theorem before adding this note. No claim
of world priority follows from that search or from the limited literature search.

## 2. Accepted claims and their exact dependencies

| Source and mathematical unit | Review verdict | Decisive check and scope |
|---|---|---|
| `r12_countersequence_kick_recurrence.md`, §§2–4 | Proved as written | Integer-labelled ordinary Weyl conversion; half-period shift; exact nonzero nilpotent stationary-circle linearization; sine-remainder Egorov with the factor of physical time retained |
| Same, §§5–6 | Proved as written | Finite cover uses spatial, not time, derivatives; cutoff derivatives uniform through zero time; cyclicity applied only after Egorov for two fixed characters |
| Same, §7 | Proved as written | Apply the bounded-time theorem at every fixed multiple of the time; finite arc covering makes the operator-distance statement uniform in the scalar phase |
| `r12_signed_trace_explicit_kick_exponent.md`, §§1–6 | Proved as written | Rational derivative margins imply sublevel exponent 1/2; the original localization yields 1/25 on the stated interval |
| `r12_full_product_nonperturbative_attempt.md`, §§2–3 | Proved as written | Modular covariance and product order; real-axis Taylor remainder; correct downward Bessel contour; coefficient and full-product norm bounds |
| Same, §4 | Proved as written | CRT parameterization, parity constraint and exact shortest scalar alias length x; the claim concerns two-copy words, not U_N spectral statistics |
| Same, §5 | Proved as written | Elementary oscillatory-integral split proves the low-degree Bessel square-mass bound; no coefficient-to-operator lower bound is inferred |
| Same, §6 | Proved as written as a reduction | Pair replacement error O(N^(2-K)); remaining signed polynomial sum explicitly unestimated |
| Same, §7, displayed endpoint identities | Verified within the stated endpoint scope | Direct two off-diagonal Jacobi entries and Duhamel; no full-product spectral inference |
| `r12_signed_trace_attempt.md`, §2 and finite Gram argument in §3 | Proved as a general finite lemma | Fourier weights reproduce a prescribed sufficiently small coordinate-moment prefix with an exact clock spectrum; the original-family fixed-power input in §1 was not independently established here |
| Round 11 arithmetic note | Partial inspection only | Definitions, Fourier coefficients and collision/variance argument inspected; complete commutator uniqueness and the full dependency closure are not accepted by this report |
| Earlier historical books and other included sources | Not fully reviewed | Inventory and selected route/status summaries are navigation only; their proof status is not promoted |

Dependency closure of the accepted trace theorem:

1. Exact original coefficients and modular-half conversion.
2. Fourier Weyl calculus and Duhamel, both derived directly.
3. Stationary-circle nonidentity and analytic spatial finite type on compact
   time intervals; for small time, explicit elementary derivative bounds.
4. Trace cyclicity and localization.
5. Fourier convergence of the single-kick eigenvalue measure and matrix-distance
   corollaries.

No earlier spectral-simplicity, pressure, Pell asymptotic or random-phase
theorem is needed for this chain. The accepted polynomial/CRT statements have
an independent elementary dependency closure.

## 3. Strengthening reconstructed in this review

The imported trace proof uses Hilbert–Schmidt Cauchy–Schwarz on a cutoff,
which replaces a sublevel volume by its square root. The new
[complete proof](../../mathematics/physical_kick_trace_decay.md) uses a real
cutoff eta and the positive matrix Q_N(eta)^2. Symmetrizing the Weyl product
cancels its first-order term; aliases cost O(N^(-2)|eta|_2^2).
Fourier Cauchy–Schwarz improves the required derivative budgets to C^3 and C^4.

With R=N|t| and sublevel exponent beta, the verified estimate is

$$
|\operatorname{tr}_N E_N(t)|
\le C_T\left(\delta^\beta+R^{-1}\delta^{-4}+R^{-2}\delta^{-8}\right).
$$

Choosing delta=R^(-1/(4+beta)) gives exponent beta/(4+beta).
For beta=1/2 this is **1/9**, on the same interval 0<|t|<=10^(-20).
This is a new argument in this review, self-reviewed separately from the
verdict on the imported 1/25 proof. It does not improve the unresolved
Heisenberg-time trace estimate for the full map.

The [second complete note](../../mathematics/physical_trace_polynomial_approximation.md)
extends the imported pair approximation error to every fixed factorial order:
O(N^k epsilon) for a norm error epsilon. A degree
2(59/50)tau N+O((log N)^2) therefore gives a single polynomial sequence with
vanishing error at every fixed order. The approximant need not be unitary;
negative trace indices are explicitly adjoint powers, and the expression is
a trace polynomial, not an asserted positive moment functional.

## 4. A useful exact limit on coordinate-moment information

For arbitrary data c_(-j)=conjugate(c_j), 2m<N and
2 sum_(j=1)^m |c_j|<1, put z_l=exp(2 pi i l/N) and

$$
w_l=\frac1N\left(1+\sum_{j=1}^m
 [c_jz_l^{-j}+\overline{c_j}z_l^j]\right).
$$

All weights are positive, sum to one and satisfy
sum_l w_l z_l^j=c_j for |j|<=m, by Fourier orthogonality. Choosing a
unitary whose first column is (sqrt(w_l)) realizes these moments at one
coordinate of a matrix with the exact clock spectrum. That coordinate is
cyclic by the Vandermonde determinant. Thus finite or slowly growing small
coordinate moments alone do not determine a Sine2 law. This general lemma
is accepted without importing the unreviewed fixed-power estimate for U_N.

## 5. Computation, corrections and exclusions

The imported exact coefficient script was inspected and run unchanged. Its
output SHA256 agrees with the embedded result:
`5951bddcd7b82b61ba509ca6cba116fe3a977e55b78be1386acbbd89e0cbc6cc`.

The maintained [finite checker](../../computations/verification/physical_kick_trace_checks.py)
uses explicit exceptions and was run with Python optimization enabled:

```sh
python3 -O computations/verification/physical_kick_trace_checks.py
```

It reconstructs the 32 coefficients by rational polynomial convolution,
checks the critical circle and derivative margins, tests 1,500 exact Weyl
product instances including large integer aliases at N=3,5,7,9,15,21,
and verifies Pell/CRT identities for odd r=3,...,103. Shortest aliases are
exhaustively enumerated only for r=3,5,7,9. A binary64 clock-prefix check
at N=17,m=4 is explicitly numerical. Exponent balancing is exact rational
arithmetic, not numerical evidence for the asymptotic theorem.

During construction of this new checker, Python's negative integer exponent
in (-1)**(k*l) accidentally introduced binary64 arithmetic and failed an exact
zero comparison. It was replaced by an integer parity branch before the passing
run. This was a checker implementation defect, not a change to the mathematics.
The imported full-product script was read but not claimed as replayed: its
provenance file reads require the author's historical layout. The new checker
independently repeats its finite CRT obligations at the stated range.

[Execution evidence and exact coverage inventory](../../evidence/executions/20261021/spectral-master-audit/README.md)
retain the accepted source proofs, their original hashes, the fresh outputs
and validation scope. Build success and hash agreement do not certify a theorem.

## 6. What remains

For phi(xi)=exp(-1/(1-xi^2)) on |xi|<1, zero outside, put
I=integral phi, b_*=|F^(-1)phi|^2/(2I^2), and w=|bhat_*|^2.
The first original unresolved test is still

$$
\frac1{N^2}\sum_{1\le m<2N}w(m/N)
\left(|\operatorname{Tr}(E_N(10^{-80})M_N)^m|^2-\min(m,N)\right)\to0.
$$

No result accepted here proves or refutes that limit. The full H_diag
criterion additionally requires every fixed factorial order and admissible
bandwidth. Its failure would not by itself refute weak point-process
convergence without controlling the corresponding unbounded moments.

The still-unreviewed historical dependency families remain a separate review
queue in the coverage inventory. They should be checked from their raw proofs
before any later promotion, including when a new author snapshot repeats them.
