# Author proof audit, 18 October 2026

Review provenance: author self-review, no independent agent, outside referee,
Lean certification or automated proof certificate. Audited revisions are the
file hashes in SHA256SUMS.

## Normalized claims and verdicts

1. For deterministic odd-characteristic symplectic Fourier S and iid circular
   D, all long-cycle products obey the explicit normalized moment error with
   x=L^4(L+1)/N<1. Distinct powers o(N^(1/5)) have the stated joint Gaussian
   limits. **Verdict: proved as written, author self-review.**
2. For fixed b and invertible A with A^T neither A nor -A, complex-Gauss
   estimates give powers o(N^(1/(6b))). **Verdict: proved as written,
   author self-review.**
3. The corresponding characteristic polynomials converge in law on the
   whole fixed open unit disk. **Verdict: proved as written, author self-review.**
4. Gaussian majorization alone gives a usable Heisenberg ramp bound.
   **Verdict: refuted for this method by B1--B3.**
5. Full BGS or original two-channel uniformity follows from these claims.
   **Verdict: incomplete; no such implication is established.**

## Dependency graph

Physical S,D -> character/rank identities -> Gaussian coefficient-norm
comparison -> sparse support + principal-minor completion -> rank counts
-> collision-weight identity -> growing moment theorem.
Variance upper bound + exact unitarity + prior fixed trace law -> direct
uniform logarithmic tail -> Hol(D) characteristic limit.

All new estimate leaves have internal proofs. Prior fixed trace laws and
seed constraints are preserved as raw proof notes in inputs/. Finite
computations are controls, not indispensable proof leaves. No local
universality theorem, G, two-channel law or BGS is used circularly.

## Obligation matrix

| Obligation | Status | Decisive check |
|---|---|---|
| Actual unitary domain and constraints | Passed | Fourier orthogonality, P=J and B norm |
| Gaussian Wick fibers | Passed | Occupation weights alpha! and centralizer z_a |
| Auxiliary Gaussian model kept distinct | Passed | Coefficient norms only, physical D unchanged |
| Complex general Gauss phases | Passed | Moduli only in bounds; nonreal mixed moment retained |
| Skew zero-rank rigidity | Passed | All cycles >=3 and odd p |
| Full-rank principal minor exists | Passed | Congruence elimination with 1x1/2x2 pivots |
| Rank completion unique | Passed | Zero Schur complement |
| Pfaffian matching count | Passed | Ordered pair encodings determine all chosen rows |
| Matching code injective | Passed | Rows determine K, hence long-cycle tau |
| Generic row code injective | Passed | Rows determine Q; A,A^T independent |
| Small-field aliases | Passed | Odd p; +/-2 nonzero; no positive replacement of complex Gauss sums |
| Repeated indices | Passed | Weighted coefficient norm and exact pair-identification formula |
| Identification rank loss | Passed | <=2 or <=2b; no loss with an isolated vertex/block |
| Collision pair count | Passed | Active support <=4r, <=8r^2 affected pairs |
| Mixed-moment normalization | Passed | Weighted Cauchy--Schwarz and both centralizers |
| Growing powers and resonances | Passed | Total-length bound; fixed moment order |
| Moments imply law | Passed | Gaussian determinacy and higher moment bounds |
| Whole disk convergence | Passed | Direct low-tail L2, high-tail unitarity |
| Second moments of exponentiated fields on full disk | Not addressed | No uniform integrability promoted |
| N-dependent points approaching circle | Not addressed | Fixed-compact topology insufficient |
| General S, two-channel law, full BGS | Not addressed | Specified finite-field families only |
| Literature priority | Not addressed | Search does not establish priority |

## Computational checks and provenance

- run/: 15,264 skew ranks, 406,044 identified pairs and eight physical
  phase-polynomial checks at N=9,25.
- generic_run/: 1,966 block ranks, 18,356 identified pairs, ten direct
  character sums and fifteen physical mixed moments.
- completion_run/: 15,264 skew matching encodings, 286 generic row
  encodings and 163 strengthened geometric bounds.
- All arithmetic exact; all result files passed; all manifests completed
  and validated against unchanged inputs. First two checkers preserve their
  initially weaker geometric estimates. The third verifies the stronger
  bounds actually used in final theorems.
- Negative controls distinguish circle/Gaussian norms, reject short-cycle
  rigidity and retain a nonreal generic moment.
- The older runner 3.2.0 path was absent; no experiment started there.
  Installed version 4.0.0 produced all three recorded runs.

## Remaining gap

The Gaussian majorant is exponentially excessive at c sqrt(N), c>e.
The circular-phase occupation constraint must survive a further signed or
resummed calculation. No estimate computing that compensation, no m~N
universality and no original two-channel limit is present in this package.
