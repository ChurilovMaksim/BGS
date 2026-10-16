# TRACE-094: classical integration input and overlap search

Checked 16 October 2026 against base main
`f78ec82ffe8c6535c961abc969a719704bf3e942`.

## Exact load-bearing source

Benoit Collins and Piotr Sniady, *Integration with respect to the Haar measure
on unitary, orthogonal and symplectic group*, arXiv:math-ph/0402073v1,
26 February 2004; Commun. Math. Phys. 264 (2006), 773--795,
DOI 10.1007/s00220-006-1554-3.

- [Pinned arXiv v1](https://arxiv.org/abs/math-ph/0402073v1).
- [Primary full text](https://arxiv.org/html/math-ph/0402073v1).
- Exact locator: Corollary 2.4, equation (11), printed p.5. Proposition 2.2
  identifies the Haar averaging operator as an orthogonal projection;
  Proposition 2.3, equation (9), defines the Weingarten inverse. Proposition
  2.6, printed p.7, gives a stronger fixed-degree order bound than needed here.

Authentication: arXiv's submission history identifies v1 as its sole listed
version and corroborates the publication DOI. PDF and primary HTML were both
inspected at the stated formulas. An attempted v3 URL was invalid; v3 was not
used. No raw PDF byte hash is claimed: the tools supplied rendered text, not
a retained binary copy.

Extraction: the source proves the exact balanced unitary moment as a sum over
two permutations, with output and input Kronecker constraints and Wg of their
relative permutation. The normalization uses probability Haar measure.

Translation: source degree n=2k, source dimension d=N. Project k is a fixed
derivative order, not the Heisenberg power m. We use N>=2k and eventually large
N, so no singular finite-dimensional inverse or analytic continuation is
needed. The ordinary Gram matrix has entries N^(number of cycles); dividing
by N^(2k) and taking a Neumann inverse gives the weaker project expansion
directly. The source does not bound the project-specific contracted Gaussian
tensors; that is the new internal graph argument. It also does not identify
any signed trace or deterministic BGS law.

## Other finite algebra and inherited prior formulas

Gaussian Fock adjointness, the Gaussian Schur norms, the hook generating series
and the Hessian swap identity are supplied in TRACE-093. Section 1 of the new
proof derives the bounded trace-product hook overlap from that series and the
finite Cauchy/Hall identity. No asymptotic character theorem is imported.

The Gaussian trace benchmark and its square-root-time sinh crossover remain
credited to Kristjansen--Plefka--Semenoff--Staudacher (2002), as checked in
[the preceding source record](abel_gaussian_sources_20261016.md). The present
claim concerns its conversion to a non-factorially weighted sector at m~alpha N.

## Bounded search and priority limits

Two web search strategies were used: initial routine discovery, then a broader
engine pass with exact/synonym combinations including:

- Ginibre / Wick / trace / Poisson / collision;
- equal edge / spectral / factorial;
- rank-one perturbation / Gaussian Fock / trace powers / Schur translation;
- high powers / random phase matrices / fourth moment;
- unicellular maps / geometric degree distribution.

The search reached adjacent non-Hermitian universality, Schur-integral and
high-genus-map literature, but did not verify an exact prior statement of the
specific W collision law or exp(-alpha^2) ratio. Adjacent map terminology is not
an established equivalence with the coloured one-circuit measure used here.
No backward/forward citation-graph census, subscription full-text corpus,
language-complete survey or mathematical novelty certificate was completed.

Classification of the Haar formula: **known verbatim after notation translation**.
Classification of search hits about the new collision/occupation assertions:
**adjacent results only within this limited search; priority unestablished**.
The project makes no claim to a world-first theorem, a prize-level result or a
solution of the full BGS problem.
