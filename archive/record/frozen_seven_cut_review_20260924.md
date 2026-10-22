# Seven-cut proof audit — `BGS-FM-007`

**Verdict:** project proof under the exact fixed model and all stated odd
$N$, author-level review only. See
[`submitted_article_review_20260924.md`](submitted_article_review_20260924.md)
for the full submission's scope and the input PDF hash. The maintained
argument is [`frozen_seven_cut_reduction.md`](../mathematics/frozen_seven_cut_reduction.md).

| Obligation | Audit result |
|---|---|
| Raw modular Weyl symbol rather than the shifted ordinary midpoint symbol in the Jacobi entries | Passed: independent raw Fourier matrix reconstruction for $N=15,17,21,25,35,49$ and exact formula (1). |
| All odd $N\ge15$, including $7\mid N$ and cyclic wrap-around | Passed in proof: nearest-integer residues give $\sum\delta_j^2=4/(7N^2)$ away from 7, zero at multiples of 7; the seven edges have disjoint endpoints. Finite regression covers 9994 odd dimensions only. |
| Nuclear and operator norms at the **fixed** parameter | Passed: two singular values per erased edge; Duhamel for real $t=\tau N$ has no $e^{Ct}$ factor. The rank-12 statement concerns $A_N-A_N^{\rm cut}$ only. |
| Microscopic $k$-point transfer | Passed: one continuous eigenphase labelling gives simultaneous total/maximal shifts; differentiated periodization with unimodular anchor change gives (7), positive factorial test gives $M=O(N^{1/k})$ under its exact hypothesis. No arbitrary-crowding uniform all-order rate was assumed. |
| Unconditional pair/Abel $O(\tau/\log N)$ | Passed with input proof included in the note: midpoint product/Egorov bounds, positive cone and covering map, logarithmic trace control, Fejér local occupancy, and exactly periodized Lorentzian $h_s$. The initial square-root Abel bound alone would only give $O(\tau/\sqrt{\log N})$. |
| Independent spectral sectors | **False if asserted for $V_N$:** the flat metaplectic kernel gives $\|[P_J,V_N]\|_{\rm HS}^2=2d(N-d)/N>0$ for every proper union of paths. The PDF correctly restricts the direct-sum claim to its generator. |
| Heisenberg signed trace estimate | **Not addressed:** $|\operatorname{Tr}U_N^m-\operatorname{Tr}V_N^m|=O(\tau|m|/N)$ does not estimate either trace at $m\asymp N$. |

The maintained exact checker `computations/verification/frozen_seven_cut.py`
was adapted from the PDF's `verify_v7.py`; its original 9994-dimension
finite scan, arithmetic constants, factorial counts, integer changes of
anchor, and CUE Abel identities were rerun. The generated JSON is
`evidence/20260924/frozen_seven_cut.json`. Its arithmetic equals the
original attached JSON; the maintained `scope` text was updated to point
to the maintained proof. No formal proof kernel or external referee.
