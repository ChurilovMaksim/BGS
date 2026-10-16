# Source checks for the 15 October research-record integration

Checked 16 October 2026. This is a bounded dependency/attribution check, not
a worldwide priority review or a certification of the full BGS corpus.

| Source and version | Exact role and hypothesis translation | Disposition |
|---|---|---|
| Diaconis--Evans, *Linear functionals of eigenvalues of random matrices*, Berkeley report 577, Theorem 2.1(a)-(b), printed pp.3-4, author-hosted PDF | Haar U(N); the maximum of the holomorphic and antiholomorphic weighted degrees must not exceed N. The trace covariance min(m,N) is unrestricted. Used for root-lift energy and stable-band checks only. | Exact source checked; existing EXT-DE-2001 reused. No deterministic Haar assumption. |
| Pittel, *Another proof of the Harer-Zagier formula*, journal-hosted author PDF dated 20 January 2016, equations (1.1)-(1.2), pp.1-2; Section 2 | A fixed long cycle composed with a uniform perfect matching. Extracting the coefficient of y gives one-cycle probability 1/(j+1) for even j, zero for odd j; the empty case is separate. | Exact source checked; EXT-PITTEL-2016. Supplies only the combinatorial input. |
| Conrey--Farmer--Zirnbauer, arXiv:math-ph/0511024v2, 9 September 2007, author-hosted PDF | Prior Haar ratios framework. The special one-ratio formula used here is proved independently by the finite Toeplitz recurrence in TRACE-090. | Attribution/background, not a newly imported general ratios theorem. |
| BEST/last-exit enumeration; Farrell--Levine, arXiv:1509.06237v1 | Context for rooted directed Euler-tour counting. The precise rooted multiplicity, loops and parallel-edge denominator are proved directly in TRACE-088. | Metadata/context checked; no unstated general theorem imported. |
| Soshnikov, arXiv:math/0002099 | Existing determinantal reference framework. The finite CUE determinant, local kernel limit, Bonferroni truncation and count-moment bounds needed by TRACE-086 are reconstructed in the source. | Existing source attribution retained; no new BGS theorem imported. |

Primary locators:

- https://statistics.berkeley.edu/sites/default/files/tech-reports/577.pdf
- https://www.combinatorics.org/ojs/index.php/eljc/article/download/v23i1p21/6196/
- https://aimath.org/~kaur/publications/u10.pdf
- https://arxiv.org/abs/1509.06237v1
- https://arxiv.org/abs/math/0002099

No licensed source bytes were added to the tracked repository. The full
physical mixed-trace estimate is not a consequence of any source above.
