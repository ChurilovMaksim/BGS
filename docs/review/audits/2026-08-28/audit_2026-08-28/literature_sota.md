# Literature check — run 71 (2026-08-28)

Two delegated literature agents failed mid-task (model returned no output), so
the checks below were performed directly by the main agent. **Only entries
actually retrieved are listed.** Web search was unavailable in this session; the
arXiv API and abstract pages were fetched directly.

## VERIFIED CITATIONS (retrieved this run)

| Ref | Author(s), title | ID / venue | What it establishes | Retrieved from |
|---|---|---|---|---|
| KR05 | P. Kurlberg, Z. Rudnick, *On the distribution of matrix elements for the quantum cat map* | arXiv:math/0302277 (v3, 10 Jan 2004); comments state the shortened 19-page version was **accepted for publication in Annals of Mathematics**; MSC 11; cross-listed math-ph | **Conjectures** that the normalised matrix elements of a smooth observable in the Hecke eigenbasis of the **desymmetrised** quantum cat map are distributed as *a certain weighted sum of traces of independent matrices in SU(2)*, and stresses this differs from the Gaussian behaviour anticipated for *generic chaotic systems*. Evidence: the **second and fourth moments** are computed and match the conjectured law. | `https://arxiv.org/abs/math/0302277` |
| Ros09 | L. Rosenzweig, *On the fluctuations of matrix elements of the quantum cat map* | arXiv:0909.1410 | Proves the normalised **fifth centred moment** in the Hecke basis vanishes semiclassically (partial confirmation of KR05); third moment of short-window sums vanishes for windows small relative to $\hbar$. | arXiv API listing |
| KRR07 | P. Kurlberg, L. Rosenzweig, Z. Rudnick, *Matrix elements for the quantum cat map: fluctuations in short windows* | arXiv:math/0701685 | For a random eigenphase window of length between the eigenphase spacing and $\sqrt\hbar$, the variance of the summed coefficients is **linear in window length**, with proportionality constant equal to the variance of the individual matrix elements for Hecke eigenfunctions. | arXiv API listing |
| Kel08 | D. Kelmer, *On matrix elements for the quantized cat map modulo prime powers* | arXiv:0802.3237 | Closed-form exponential-sum expressions for matrix elements under the arithmetic symmetries; exhibits eigenfunction sequences whose matrix elements **decay significantly slower than previously conjectured**; establishes a limiting fluctuation distribution. | arXiv API listing |
| Kel05 | D. Kelmer, *On the quantum variance of matrix elements for the cat map on the 4-dimensional torus* | arXiv:math-ph/0501063 | On $\mathbb T^4$ certain map/observable pairs give a quantum-variance decay rate differing from the generic chaotic expectation. | arXiv API listing |
| Zel00 | S. Zelditch, *Index and dynamics of quantized contact transformations* | arXiv:math-ph/0002007 | Treats quantised cat maps as Toeplitz operators; resolves index/unitarity via theta transformation laws; eigenfunction equidistribution and weak-mixing behaviour of matrix elements for mixing symplectic maps. | arXiv API listing |

## Consequences for this workspace

1. **The R67–R70 conclusion points the wrong way.** KR05 is the standard
   reference for the distribution of Hecke-basis matrix elements of the cat map,
   and it predicts a **non-Gaussian** (SU(2)-trace) law, explicitly contrasting
   with the Gaussian expected for generic chaotic systems. A claim that the
   Hecke-centred residual is Gaussian therefore contradicts the accepted picture
   rather than confirming QUE — independently of the three code defects
   documented in LEDGER R71.6.
2. **The right target for `op:local_deterministic`** is the KR05 SU(2)-trace law,
   not a Gaussian, and the right statistic is a moment sequence (KR05 do 2nd and
   4th; Ros09 does the 5th) rather than a kurtosis of a Haar-centred residual.
3. **Prior art for Theorem A** (exact GUE/GOE for a Gaussian Weyl observable
   compressed to a multiplet) was **not** located this run — see below. The proof
   is three lines from Weyl completeness, so the result may well be folklore; the
   novelty claim in the paper is therefore deliberately weak, and the paper
   presents it for the *conceptual* consequence (Remark on what is not evidence)
   rather than for difficulty.

## COULD NOT VERIFY (recorded honestly as gaps)

* **Prior art for Theorem A.** No search performed beyond the cat-map queries
  above; native web search was unavailable and both delegated agents failed.
  Status: `[UNVERIFIED prior art]`.
* **Prior art for Theorem B** (exact moments of subgroup Kloosterman sums / joint
  additive energy of $\{(h,h^{-1}):h\in H\}$). One arXiv API query
  (`abs:"multiplicative subgroup" AND abs:Kloosterman`) returned zero results; a
  broader query (`abs:Kloosterman AND abs:subgroup`) timed out. The relevant
  authors to check are Bourgain, Konyagin, Garaev, Shkredov, Shparlinski,
  Macourt, Murphy. Status: `[UNVERIFIED prior art]`. Both theorems have short
  self-contained proofs, so a referee can judge novelty directly.
* **OSV arXiv:2110.10941** — the paper the workspace cites for the
  $k\ge p^{3/7+\varepsilon}$ smooth law (authors/title/venue and the exact
  statement of its Cor. 2.9) was **not re-verified this run**. The workspace's
  own audit flags the derivation built on it as heuristic; that downgrade does not
  depend on the citation being correct.
* **Linn 2024 arXiv:2412.04976** (Kloosterman bounds for $GL_n$) — not verified
  this run.
* **Bohigas–Giannoni–Schmit 1984 PRL 52, 1** — cited from standard knowledge, not
  re-fetched. Sieber–Richter 2001 and Müller–Heusler–Braun–Haake–Altland 2004
  likewise. These are textbook-level attributions; the finer claims about *what
  exactly* MHBHA proved (all-orders form factor as a formal power series, not a
  convergent statement) are `[UNVERIFIED]` at the level of page references.

## Queries run

1. `arxiv.org/abs/math/0402038` — wrong guess, returned Schubert, *Semiclassical
   behaviour of expectation values in time evolved Lagrangian states*; discarded.
2. arXiv API: `abs:"cat map" AND abs:"matrix elements"`, 20 results — yielded
   KR05, Ros09, KRR07, Kel08, Kel05, Zel00 and two Rivas propagator papers.
3. arXiv API: `abs:"multiplicative subgroup" AND abs:Kloosterman` — 0 results.
4. arXiv API: `abs:Kloosterman AND abs:subgroup` — request timed out (60 s).
5. `arxiv.org/abs/math/0302277` — full abstract page, to fix the KR05 citation.
