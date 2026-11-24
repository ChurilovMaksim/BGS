# BGS-F continuation: scoped integration of the November packet

**Model.** Unless a note explicitly says otherwise, it refers to the exact
[fixed map](../fixed_map_resolvent_frontier.md) at \(\tau=10^{-80}\), with the
same Weyl convention and uniform common spectral shift. The input was the
BGS-F Cumulative packet dated 22 November 2026, based on commit
[e2757e4](https://github.com/ChurilovMaksim/BGS/commit/e2757e4cc5ef996e08190f88c93c710377c10c22).
The 234-page packet is not a parallel publication root.

| Note | Registered disposition and essential limit |
|---|---|
| [Alignment](alignment/README.md) and [contact estimates](contacts/README.md) | BGS-TRACE-356. A signed, once-counted comparison for each fixed overlap threshold above one half; the full half-overlap boundary and low-overlap sum are not covered. |
| [Coherent histories](histories/README.md) | BGS-TRACE-357. Sparse short-history control uniform in the power being tested; the scalar trace and its summed error at times of order \(N\) remain uncontrolled. |
| [Torsion transport](torsion_transport/README.md) | BGS-TRACE-358. Explicit relative one-step estimate and exact nonintersection; not a new proof of general logarithmic-time transport or pair cancellation. |
| [Multiplicative rank](relation_rank/README.md) | BGS-TRACE-359. Exact relations excluded on a selected positive-density subset of \(7^k\)-dimensional spectra. No quantitative near-resonance estimate in a Heisenberg window. |
| [Exact splitting](exact_splitting/README.md) | BGS-TRACE-360. A lower limit for the simple-phase fraction on \(7^k\), not all odd dimensions and not gap repulsion. |
| [Effective gaps](effective_gaps/README.md) | BGS-TRACE-361. An explicit nonzero-gap floor and bounds for much longer averaging windows; the floor is vastly smaller than \(1/N\). |
| [Pell witnesses](pell/README.md) | BGS-TRACE-362 and BGS-TRACE-363. Improved finite band-two witness at \(h_{207}\) and a separate finite \(h_{209}\) trace/Abel/local witness. Neither extends to an infinite fixed-kick subsequence. |
| [Perturbation precision](resolution_precision/README.md) | BGS-TRACE-364. Stability of the specified pair test and sharp abstract limitations of operator-norm approximation. The rounded model is not the original quantization. |
| [Weak-law and pair implications](pair_implications/README.md) | BGS-TRACE-365. A negative pair defect can refute weak Sine₂; a positive excess alone cannot. Weak Sine₂ plus the designated pair test controls the entire second order. |
| [Shrinking-kick and critical regimes](weak_kick/README.md), [earlier routes](earlier_routes/README.md) | Mapped source material with separate model and review boundaries, including exact reductions, finite controls and auxiliary counterexamples. Not a blanket promotion of the source chapters. |

## What it would take to close the original problem

For closed paths \(x,y\) of length \(m\), let \(R_{m,N}(d)\) be the signed
sum of \(a(x)\overline{a(y)}\) over pairs with strictly fewer than \(dm\)
matches under every cyclic direct or reverse alignment. The alignment
route, subject to the analytic inputs documented in its proof note,
reduces the first test to
\[
 \frac1{N^2}\sum_{\lceil\log N\rceil\le m<2N}w(m/N)R_{m,N}(d)
 \longrightarrow -\delta_*,
 \qquad \delta_*=\int_1^2(t-1)w(t)\,dt>0 .
\]
The sign is essential: setting that remainder to zero would extend the
ramp past the plateau, not recover CUE. A pair theorem still would not
prove the entire factorial hierarchy. A deficit bounded away from zero
along infinitely many odd dimensions on a nonnegative pair test would
refute weak convergence itself; finite witnesses or an unmatched positive
second moment do not do so.

The [replay guide](../../../computations/verification/bgs_f_november/README.md)
and [execution record](../../../evidence/executions/20261124/bgs_f_november/README.md)
separate exact finite certificates, numerical cross-checks, and source-level
review. Imported source preserves mathematical provenance without asserting
external peer review, new Lean coverage, or a proof of BGS-TRACE-005 or BGS-BGS-001.
