# Active research ledger

The complete historical ledger remains under `archive/legacy-workspace/HISTORY.md`. This file records only decisions/results that define the current program.

## 2026-09-03 - exact pair-key rebuild

- Reconstructed the `(x,y)->(u,v,d)` key map from first principles.
- Identified the weighted diagonal `(1,1)` of multiplicity `N-2` and the off-diagonal bijection.
- Replaced the historical Mobius graph by the exact key-table object `B(t)`.
- Found and quarantined the Run 93.2 missing reverse ordered diagonal/off class.
- Derived the exact total `V4=(K^2+1)N^2-(6K^2+3K)N+13K^2-3K`.
- Python and independent C++ exact constructions agree at `N=23,53,199,461`.

## 2026-09-03 - exact twist/Fourier collapse

- Double character orthogonality gives `sum_tau(A_tau*A_tau)=m^2B`.
- The fourth moment is `sum|J|^4=m^2 Sigma4`, `Sigma4=Fourier(B)`.
- Derived exact nonzero-frequency mean and variance identities; M1 became the clean geometric target `Var B=O(K^2N)`.

## 2026-09-03 - historical M1 formally removed from active route

- Unsaturated elimination adds a phantom `(1,1)` to the Mobius graph for `d!=0` and mishandles the weighted diagonal at `d=0`.
- Exact finite comparison proves that the old object differs from the correct amplitude, so better cross-term/Weil estimates cannot repair the old theorem.

## 2026-09-03 - Cayley solution of the mixed k=2 energy

- Found `d(u,v)=2/(c(u)-c(v))`, `c(h)=(h+1)/(h-1)`.
- Recast `C_H` as additive difference energy of `A=c(H\{1})` with central symmetry `A=-A`.
- Exact 720 matching audit: rank profile 30/240/450; rank drops only in characteristic 2; no non-forced characteristic-zero collision.
- Computed exact finite exceptional-prime sets for `K=11,13`.
- Outside the set, proved `sum C_H^2=(K-1)(2K-5)`, closing the mixed M1 component at the required `O(K sqrt(N))` scale.

## 2026-09-03 - off/off elliptic geometry

- Converted the generic off/off fiber to a plane cubic / binary quartic in Cayley coordinates.
- Factored the residual discriminant; only `h1=h2` and `h1h2=1` are parameter-level nonsquarefree strata.
- Proved generic `j`-map degree 12 and pole type `(4,4,1,1,1,1)`, hence non-isotriviality.
- Classified equal same-base `j` functions: identity and exact key involution only.
- Used modular degree/cusp widths to exclude nontrivial generic cyclic isogenies; degree excludes inseparable Frobenius factors.
- Combined with Zarhin to obtain geometric non-isomorphism of generic rank-two local systems outside the involution orbit.

## 2026-09-03 - bad fibers and restricted M1 draft

- The order-four bad fiber factors into two lines exactly at `t=d(h1,h2)`; its aggregate `N`-scale spike is controlled by the solved Cayley energy.
- The remaining four generic bad fibers are nodal/rational.
- Made trace-to-affine bookkeeping explicit: boundary degree 10 gives at most 30 geometric boundary points on an irreducible cubic.
- With Deligne/Igusa/quantitative-sheaf quasi-orthogonality, the assembled generic estimate is `Var O << K^2N + K^4 sqrt(N) + K^4`.
- Together with special strata, mixed energy and covariance Cauchy-Schwarz, this assembles a restricted M1 proof draft for odd prime `K`, nonexceptional split `N`, `K=o(N^(1/4))`.
- Status remains **audit/formalization pending**, not general BGS proved.

## 2026-09-03 - language migration and repository consolidation

- Audited all 31 historical Julia paths (23 byte-distinct sources) from the preserved workspace.
- Decided against a second Julia archive: provenance remains once in `archive/legacy-workspace` and Git history.
- Consolidated the corrected relation-automaton/DP line into one C++20 component with exact Run-82/Bessel regression gates.
- Ported the cat-map order/prime scan to C++20 and separated full matrix order from projective/scalar terminology.
- Replaced the historical `sol6_closed_form` claim by an exact Python enumerator/falsifier.
- Replaced the random Linn probe by a deterministic Python diagnostic.
- Mapped the Hecke-centering Julia version series to one existing Python red-team instead of cloning eight broken implementations.
- Migration itself uncovered two additional historical defects: the `cdense_transfer` spectral-radius bracket is impossible because of a zero-cost weight-one self-loop, and the `projective_order_brute` comment confuses full matrix order (15 at `p=31`) with a scalar/projective notion.
- Language policy: Python for symbolic/exact orchestration and analysis; C++20 for heavy exact/finite-field kernels; no Fortran unless profiling shows a real dense-numerical need.

## 2026-09-03 - canonical manuscript

- Rebuilt the current paper from active verified theory instead of splicing historical proof drafts.
- Active `paper/` now has one editable source `main.tex` and one built `main.pdf`; no competing section-level TeX manuscripts or `final/complete/proof` variants.
- The paper explicitly separates exact theorems, restricted-M1 theorem draft, numerical evidence, falsifiers and the still-open local BGS step.

## Promotion rule

A result is active only after its conventions and producer are reconstructed, it has at least one independent certificate appropriate to the claim, and theorem language matches the actual logical status. Historical filenames or numerical scaling alone never promote a statement to theorem.
