# Literature scout report — run 75 (2026-08-28)

Scope: (1) prior art on l1-bounded multiples of x^2 - t x + 1; (2) growth/count
results; (3) vanishing sums of Chebyshev sequences; (4) BGS for cat maps
2024-2026.  28 queries; two consecutive empty reformulation rounds before stop.

## Verified references (abstract or listing retrieved)

Littlewood/Borwein multiples:
- P. Drungilas, J. Jankauskas, J. Siurys, "On Newman and Littlewood multiples of
  Borwein polynomials", arXiv:1609.07295 (2016). Decision algorithm for whether a
  monic integer polynomial with no roots on the unit circle has a nonzero
  multiple in any prescribed finite digit set; classification deg <= 9.
- A. Dubickas, J. Jankauskas, "On Newman polynomials which divide no Littlewood
  polynomial", Math. Comp. 78 (2009) 327-344. x^9+x^6+x^2+x+1 divides no
  Littlewood polynomial; obstruction anchor.
- M. Idris, J.-M. Sac-Epee, arXiv:2607.15520 / hal-05695568 (2026). 14
  irreducible polys of Mahler measure < 1.3 with no Newman multiple; the
  existence line is active in 2026, counting is absent.

Structure of expansions in Pisot bases (the machinery for conj:Sgrowth):
- C. Frougny, W. Steiner, "Minimal weight expansions in Pisot bases",
  arXiv:0803.2874 (2008; J. Math. Cryptol. 10.1515/JMC.2008.017). Minimal
  absolute-digit-sum expansions in Pisot bases are recognizable by finite
  automata; explicit automata for golden ratio etc.  => the l1-classes of our
  relation language are sofic; the growth constant is a transfer-matrix
  (Perron-Frobenius) eigenvalue.  NOT yet computed in print.
- C. Frougny, B. Solomyak, "Finite beta-expansions", ETDS 12 (1992).
  Foundational finiteness property (F) (listing-level only).
- S. Akiyama, J. M. Thuswaldner, T. Zaimi, arXiv:1402.1586 (2014). Height
  reducing property fails for quadratic Pisot units (conjugate inside the unit
  circle) -- bounded digits cannot cover Z[alpha]; the zero-relation language
  is still finite-state.
- K. G. Hare, "The structure of the spectra of Pisot numbers", JNT 105 (2004)
  262-274; P. Borwein, K. G. Hare, Math. Comp. 71 (2002) 767-780. Spectra and
  digit relations.
- D.-J. Feng, N. Sidorov, "Growth rate for beta-expansions", Monatsh. Math. 162
  (2011) 41-64. Growth for a.e. x, not for the zero-relation language.

Fewnomial / additive-energy backdrop:
- J.-H. Evertse, H. P. Schlickewei, W. M. Schmidt, Ann. of Math. 155 (2002)
  no. 3. exp(6n^3) bound on nondegenerate S-unit solutions.
- T. Schoen, I. Shkredov (convex sets, additive energy E(A) <~ |A|^{5/2});
  continuation arXiv:2509.01568 (2025, Combinatorica).

Cat maps / quantum chaos 2024-2026:
- E. Kim, T. C. Anderson, R. J. Lemke Oliver, arXiv:2410.13449 (2024): full
  support of semiclassical measures for higher-dimensional cat maps under
  generic irreducibility (Cohen's higher-dim FUP).
- N. Schwartz, arXiv:2103.06633; Dyatlov-Jezequel, arXiv:2108.10463:
  full delocalization / uniform lower bounds (2D and higher).
- R. Koirala, arXiv:2605.06569 (2026): short-period eigenfunctions
  equidistribute while l^inf concentrates on boundedly many coordinates.
- T. Cunningham, arXiv:2602.20392 (2026): fractal Weyl bounds matching improved
  gaps; A. Kangabire, arXiv:2406.06815 (2024): FUP for large-alphabet Cantor
  sets; E. Kim, N. Miller, arXiv:2503.01528 (2025).
- E. D. Schultz, K. Furuya, L. Nie, arXiv:2502.04442 (2025): quantum dynamical
  entropy under symmetry; perturbed cat maps numerically RMT.
- L. Shou, arXiv:2306.04908, CMP (2025): baker's map spectral projections;
  random Walsh eigenbases Gaussian + QUE -- the nearest rigorously treated
  symmetry-class-separated system.

## Verdicts

(a) The COUNT of l1-bounded multiples of x^2 - t x + 1 as a function of r is
NOT published (all reformulations empty).  Our S(R) census + Theorem H make
this object concrete; the automaton route above is the way to conj:Sgrowth.
(b) Closest prior art: the two strands (decision algorithms; minimal-weight
automata) with the counting gap exactly between them.
(c) No published local law / NNS / RMT statistics for eigenfunction-compressed
observables of UNPERTURBED quantized cat maps as of 2026-08; the programme
target remains novel.  Perturbed cat maps: numerics only.

## Provenance flags

- "Valentin Latil 2024 (BGS for quantum cat maps)": NOT FOUND on arXiv/HAL
  (only the condensed-matter physicist S. Latil).  Not cited in this workspace
  (grep-checked).  Do not cite without re-sourcing.
- arXiv:1408.0195 (Hare-Mossinghoff), Schoen/Shkredov venues: bibliographic
  only, re-verify before citing.
