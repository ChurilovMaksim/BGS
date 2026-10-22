# Fixed-map proposal: foundational audit and comparison improvements

Date: 2026-09-16. **Primary verdict: internally inconsistent as written.**
This is a scoped self-review, not a completed line-by-line audit of the whole
11,033-line upload. No claim of independent referee validation or scientific
priority is made. The fixed-map BGS theorem remains open.

Source: user attachment `BGS_verified_state(1).md`, last-audited label
2026-09-16, SHA-256
`d38bcd35482a288251f981cf97ba6f68978ac811b5a92579f2cf52c9540fbfe4`.
The source has been preserved unchanged. Its `[PROVEN]` labels have not been
imported into the project's claim ledger. This report does not supersede
unreviewed sections with another blanket 'verified' label.

## 1. Dependency and obligation map

The proposed fixed nonlinear classical map is a useful different research
branch from the repository's vanishing-perturbation arithmetic return laws.
Its tiny coupling is fixed, so its quantum exponent grows with dimension.
Results for the older return regime cannot supply its Heisenberg estimates.

| Claim / dependency | Audit outcome | Consequence |
|---|---|---|
| §§2.1–2.2, factorial trace and Poisson identities | Passed by reconstruction; already in `trace_to_local_statistics_bridge.md` | Retain; no BGS estimate follows |
| §4, explicit cone estimates | Algebra and bounds consistent on inspection | Classical hyperbolicity is useful independently of quantization |
| §5 fixed-point Hessians and derivative-trace obstruction | Passed, including exact symbolic recomputation | Non-C1 conjugacy obstruction retained for the specified classical map |
| §6 period-three matrix polynomial | Passed, exact symbolic recomputation | Full no-reversor argument has not received a fresh complete source audit |
| §8 modular Weyl commutator | Refuted as written | Correct §11 generator and all implementations using it |
| §9 ordinary-midpoint Jacobi formula with raw modular Fourier quantization | Incompatible conventions | Simplicity proof cannot be transferred without choosing quantization |
| §8 META versus §12 positive generating action | Inconsistent under stated position and action conventions | Classical/quantum correspondence must be re-established |
| §12.12 coordinate curvature for every m | Refuted at m=1 | Later §12.6a correctly treats that exception; remove stale earlier assertion |
| §12.2 Frobenius criterion | Passed | Its application to the frozen quantum family remains dependent on the FIO identification |
| §§21.5v, x2f, x2g abstract HS/isometry inequalities | Passed under their explicit decomposition hypotheses | Existence of the required coherent decomposition is not established by Parseval alone |
| §21.5x2h weighted conclusion | Incomplete: missing time-sum normalization | A positive power saving per normalized trace is not enough as stated |
| §§21.5z, z1 Naimark identities | Passed algebraically | Exact reformulation, not a mixing theorem |
| §21.5aa abstract pruning estimate | Valid sufficient bound, improvable | See rank-based improvement below; microlocal assumptions remain conditional |
| §21.5o comparison threshold | Bound valid; claim of necessary practical threshold unsupported | New correlation-stability theorem lowers a sufficient scale with reference control |
| Leclerc-dependent transfer adaptation, encounter localization and quantum-to-tube transfer | Conditional / not fully audited | Do not import as established closure inputs |

Not examined exhaustively: §14 prime-power exponential sums, all encounter
combinatorics, high-order FIO remainders, periodic Gibbs estimates, and all
2025–2026 literature claims. The upload's verification log is provenance of
its author's checks, not evidence that those checks were rerun here.

## 2. Exact modular sign failure

The upload explicitly takes `2^-1` modulo odd `N`. Let `u=(N+1)/2`, and
`T(a,b) psi(x)=e_N(b(x+u a)) psi(x+a)`. Direct multiplication gives

```text
T(r) T(n) = e_N(u sigma(r,n)) T(r+n).
[T(r),T(n)] = (e_N(u sigma)-e_N(-u sigma)) T(r+n)
             = 2 i (-1)^sigma sin(pi sigma/N) T(r+n).
```

The last form uses integer representatives; the combination, unlike its
separate factors, is invariant under changing representatives. For
`r=(1,0), n=(0,1)` it is the *negative* of (WEYL). This fails at every odd
`N>1`, not merely at a small exceptional dimension.

Consequently the exact generator (L), in this modular basis, must contain
`(-1)^sigma` as well. The factorization of powers itself remains an exact
algebraic identity after using the actual generator.

A consistent ordinary-midpoint convention is

```text
W(a,b)=(-1)^(ab) T(a,b)
      = exp(2 pi i b(x+a/2)/N) shift_a,
```

where the second expression uses ordinary real `a/2`. For integer labels,
`W(r)W(n)=exp(pi i sigma/N)W(r+n)`, giving the ordinary sine.
However `W` is not strictly periodic in its integer labels:

```text
W(a+N,b)=(-1)^b W(a,b),  W(a,b+N)=(-1)^a W(a,b).
```

Wrap signs must be included in a finite-lattice implementation. One may
instead keep the modular basis and multiply every ordinary Fourier
coefficient at label `(a,b)` by `(-1)^(ab)`. One must not silently identify
these two coefficient lists.

### Consequence for the Jacobi proof

In the position convention of §9, a Fourier mode with momentum frequency 1
and position frequency k uses `T(1,k)`. Raw modular Fourier coefficients give

```text
t_j=(e^(-i alpha)/200) r((j+u)/N),
```

not the displayed `r((j+1/2)/N)`. The modular grid visits `k/7` whenever
`7|N`: it has seven zero edges, not one. At `N=7` every hopping coefficient
vanishes, while the diagonal equals 1, so **A_7=I_7** under this raw modular
interpretation. Thus §9.2 is false for that interpretation. If the author
intended gauge-corrected coefficients, the ordinary Jacobi proof can survive,
but this missing definition and the modular commutator must still be fixed.

Using `W` does recover the ordinary midpoint formula and its unique zero
edge for odd `N`. This is a repair option, not an assertion that the two
quantizations define the same prescribed spectrum.

## 3. Classical versus quantum map orientation

Independently of the half-step issue, the upload's (META) satisfies its
stated covariance `M T(n) M*=T(Sn)`; direct matrix tests confirm it.
With the position convention of §9, `W(a,b)` is the quantization of
`exp(2 pi i(b q+a p))`. Since

```text
S=[[3,4],[2,3]],
```

this covariance sends the symbols q and p to `3q+4p` and `2q+3p` in the
Fourier sense: `M Op(g) M*=Op(g o S)`. The conventional propagator relation
is instead `M* Op(g) M=Op(g o F_classical)`. It therefore assigns (META) to
`S^-1`, not `S`, with the stated position convention.

The same discrepancy appears in §12: (META) uses the negative quadratic
phase, whereas (BRANCH) uses `exp(+2 pi i N W)` with
`W=(3q^2-2qQ+3Q^2)/8` and `p=-W_q, P=W_Q`, which generates `S`.
Reversing the metaplectic operator or consistently changing the conventions
can repair this, but doing so changes another explicitly fixed identity.
It is not justified to use the FIO results for the claimed classical F
before carrying that repair through the kick, symbol and covariance.

For the positive W, `W(q,q)=q^2/2`; hence the period-one curvature is exactly
1 at zero kick, not 3/2. The later global Hessian enclosure correctly allows
this, but it does not make the earlier all-m statement true.

## 4. Missing Heisenberg time sum

Let `D=dim K_N=N^2` on Liouville space. Suppose the first-witness proof gives
for each time m a signed error `E_(m,N)` satisfying

```text
|E_(m,N)|/N^2 <= epsilon_(m,N).
```

For a weight supported on `O(N)` times the actual consequence is

```text
N^-2 |sum_m w(m/N) E_(m,N)|
 <= sum_m |w(m/N)| epsilon_(m,N).
```

A uniform bound `epsilon_(m,N)=O(N^-delta)` gives `O(N^(1-delta))`.
Removing a witness-location factor inside each trace does not remove the
separate sum over times. Without further structure, the sufficient uniform
condition is `o(1/N)`, not an unspecified positive-power saving.

The abstract inequalities themselves cannot improve this: for each time,
choose one prefix `A=I_D`, descendant `B=epsilon I_D`, and identity exterior.
Their HS budgets hold with equality and `Tr(AB)/D=epsilon`. Nonnegative
weights then realize the time-sum loss. This is a counterexample to the
inference from those budgets alone, not a counterexample for the actual map.

Three possible repairs are: prove `sum_m |w| epsilon_(m,N)=o(1)`; prove
cancellation in the signed time sum directly; or obtain smaller HS budgets
reflecting the natural form-factor size O(N), rather than ambient N^2.
Each is an additional theorem. Sections x2g–x2h cannot currently be used as
unconditional Level-C closure.

## 5. Constructive improvements

### 5.1 Correlation transfer below a single spacing

A complete proof and an order-sharp simple-spectrum example have been added
to `mathematics/trace_to_local_statistics_bridge.md`, Theorem 4:
if the reference fixed-k factorial correlation measures are bounded on
nonnegative Schwartz tests, then `||U_N-V_N||=o(1/N)` transfers their fixed-k
limits. The proof matches eigenangles along a short unitary path and controls
positive correlation measures directly. It applies to all fixed orders, with
no phase average. A clock and an alternating displacement by `a/N` show why
`O(1/N)` alone is insufficient for general spectra.

A separate absolute Fourier estimate gives the sufficient scale
`o(N^-3/2)` under a bounded weighted reference form factor. These statements
must not be confused: direct correlation comparison allows cancellation in
the Fourier representation. They do not prove the needed comparison with a
CUE reference or with natural quantization.

### 5.2 Rank-improved pruning

For the upload's exact isometry `W:K->Khat`, put `D=dim K=N^2`,
`A=WV W*`, and `R=WV_r W*`, with V and V_r unitary. If a pruned operator B
satisfies `||A-B||<=d`, then `||R||_1=D`, independent of the enlarged alphabet.
Thus, for M>=1,

```text
|Tr R(A^M-B^M)| <= D M d (1+d)^(M-1).
```

Proof: telescope powers, use `||A||<=1`, `||B||<=1+d`, and trace-norm/operator-
norm duality. There is no need to bound by `dim Khat`.
For `K_N<=N^Gamma` blocks, each deleted block at most `N^-A0`, the Schur
bound gives `d<=N^(Gamma-A0)`. Summing m<=sigma N, with M<=m/ell, gives

```text
N^-2 sum_m |w(m/N)| |Tr R(A^M-B^M)|
 <= C (N^2/ell) d exp(C N d/ell).
```

So `A0>2+Gamma` suffices, improving the upload's `2+2Gamma`. This is an
abstract bound only; arbitrary-power microlocal deletion for this map remains
dependent on a consistent quantization and the stated support separation.

## 6. Source check and limits

The primary HTML of G. Leclerc, arXiv:2507.23731v2, Appendix E, was examined:
https://arxiv.org/html/2507.23731v2 . Theorem E.1 treats a scalar smooth
cocycle on a product circle extension. Lemma E.6 supplies the derivative
non-concentration implication used by its proof. The upload's adaptation to
a nontrivial prequantum bundle and a Hilbert-valued coherent exterior is an
additional argument, not the statement of that theorem. Its required
one-sided cocycle, gauges and temporal-distance identification have not been
fully verified here. In particular, total loop holonomy should not be
identified with a one-sided temporal distance merely by naming both
'prequantum action'. This is a named obligation, not a disproof of the
possible adaptation.

No literature search here establishes novelty of Theorem 4 or of the rank
improvement. Both are elementary comparison tools. The useful scientific
next target is the actual *time-summed* coherent unmatched remainder, after
fixing the quantum conventions. Proving more conditional reductions while
leaving these hypotheses unchecked would not advance fixed-map BGS.

## 7. Reproduction

Program: `computations/verification/fixed_map_convention_audit.py`.
Dependencies: NumPy, SymPy. Executed successfully using the already available
local dependency directory with `PYTHONPATH` set accordingly.

- Direct modular commutator/covariance checks: N=5,7,9,11,21.
- Ordinary midpoint gauge and Fourier-derived hopping checks at those N.
- Four exact fixed Hessians and the exact period-three monodromy polynomial.
- Exact symbolic period-one curvature.
- Clock/displaced-clock microscopic test: N=8,16,32,64.

These finite tests support the explicit derivations, not any asymptotic BGS
claim. No Lean proof, complete manuscript rebuild, or full legacy test suite
was performed in this scoped audit.
