# Bibliography and theorem-technology map

Only sources that constrain the active argument or its interpretation are
listed here. A citation is **not** a claim that its hypotheses have already
been verified for this project.

## Arithmetic quantum cat maps

1. P. Kurlberg and Z. Rudnick, **Value distribution for eigenfunctions of desymmetrized quantum maps**, arXiv:math-ph/0101008 (2001). Split-prime Hecke-eigenfunction value distributions; not an eigenphase-spacing theorem.
2. P. Kurlberg and Z. Rudnick, **On the distribution of matrix elements for the quantum cat map**, *Annals of Mathematics* **161** (2005), 489–507, DOI `10.4007/annals.2005.161.489`. Matrix-element fluctuations and moment calculations.
3. P. Kurlberg, L. Rosenzweig and Z. Rudnick, **Matrix elements for the quantum cat map: fluctuations in short windows**, arXiv:math/0701685 (2007). Shrinking eigenphase windows for sums of matrix coefficients, not microscopic eigenvalue correlations.
4. L. Rosenzweig, **On the fluctuations of matrix elements of the quantum cat map**, arXiv:0909.1410 (2009).
5. S. Gurevich and R. Hadani, **Proof of the Kurlberg–Rudnick rate conjecture**, *Annals of Mathematics* **174** (2011), 1–54, DOI `10.4007/annals.2011.174.1.1`.
6. S. Dyatlov and M. Jézéquel, **Semiclassical Measures for Higher-Dimensional Quantum Cat Maps**, *Annales Henri Poincaré* **25** (2024), 1545–1605, DOI `10.1007/s00023-023-01309-x`. Delocalization/support restrictions for eigenfunctions/semiclassical measures; not a local eigenphase-statistics theorem.
7. P. Kurlberg, A. Ostafe, Z. Rudnick and I. E. Shparlinski, **On Quantum Ergodicity for Higher Dimensional Cat Maps**, *Communications in Mathematical Physics* **406**, 174 (2025), DOI `10.1007/s00220-025-05350-1`.
8. S. Bhakta and I. E. Shparlinski, **On quantum ergodicity for higher-dimensional cat maps modulo prime powers**, *Bulletin of the London Mathematical Society* **58** (2026), DOI `10.1112/blms.70300`.

Items 1–8 concern eigenfunctions, matrix elements, delocalization or quantum
ergodicity. None supplies the microscopic GOE/GUE eigenphase law needed to
close BGS for the present family.

## Spectral-spacing evidence and rigorous model-class BGS results

9. A. Gamburd, J. Lafferty and D. Rockmore, **Eigenvalue spacings for quantized cat maps**, *Journal of Physics A* **36** (2003), 3487–3499, DOI `10.1088/0305-4470/36/12/336`.
10. Z. Pluhař and H. A. Weidenmüller, **Universal Quantum Graphs**, *Physical Review Letters* **112** (2014), 144102, DOI `10.1103/PhysRevLett.112.144102`. For time-reversal-invariant quantum graphs mixing in the classical limit, the paper proves agreement of all spectral correlation functions with GOE in the graph limit under its stated setup.
11. Z. Pluhař and H. A. Weidenmüller, **Quantum graphs and random-matrix theory**, *Journal of Physics A* **48** (2015), 275102, DOI `10.1088/1751-8113/48/27/275102`. Gives the corresponding all-correlation generating-function result for a class of mixing graphs, with explicit graph assumptions.

Item 9 is numerical spectral-spacing context, not a general local-law theorem.
Items 10–11 are important counterweights to any claim that BGS has no rigorous
model-class realizations: quantum graphs do admit proofs under precise mixing,
large-graph and structural hypotheses. They do **not** prove BGS for smooth
Hamiltonian systems or for the arithmetic cat-map family in this repository.

## Cyclotomic/cotangent rigidity used by the mixed term

12. S. Chowla, **The nonexistence of nontrivial linear relations between the roots of a certain irreducible equation**, *Journal of Number Theory* **2** (1970), 120–123, DOI `10.1016/0022-314X(70)90012-0`.
13. K. Wang, **On a theorem of S. Chowla**, *Journal of Number Theory* **15** (1982), 1–4, DOI `10.1016/0022-314X(82)90078-6`.

Wang states Chowla's prime theorem explicitly as Theorem A: for prime `K`, the
`(K-1)/2` real numbers

`cot(pi*a/K), 1 <= a <= (K-1)/2`,

are linearly independent over `Q`. This is the exact external input used in
`mathematics/cayley_additive_energy.md`; Wang also extends the statement to
more general moduli and derivatives of cotangent. The DOI/title metadata for
both papers was independently resolved during the 2026-09-04 audit.

## Fibonacci/Lucas divisibility used by the new resultant structure

14. R. D. Carmichael, **On the Numerical Factors of the Arithmetic Forms α^n ± β^n**, *Annals of Mathematics* **15** (1913–1914), 49–70, DOI `10.2307/1967798`.
15. Y. Bilu, G. Hanrot and P. M. Voutier, **Existence of primitive divisors of Lucas and Lehmer numbers**, *Journal für die reine und angewandte Mathematik* **539** (2001), 75–122, DOI `10.1515/crll.2001.080`.
16. T. M. Apostol, **Resultants of cyclotomic polynomials**, *Proceedings of the American Mathematical Society* **24** (1970), 457–462, DOI `10.1090/S0002-9939-1970-0251010-X`.

The general almost-Sidon proof in
`mathematics/cayley_resultant_structure.md` uses only the classical Fibonacci
special case of Carmichael's primitive-divisor theorem: for index `n>12`,
`F_n` has a prime divisor that divides no earlier Fibonacci number. Bilu–Hanrot–
Voutier is a modern much broader primitive-divisor theorem and is useful for
possible extensions to other Lucas slices; it is not needed to make the
Fibonacci argument stronger than Carmichael already makes it.

A bounded 2026-09-04 literature search also checked cyclotomic-resultant and
Fibonacci-resultant terminology. Apostol is standard background on cyclotomic
resultants, and related generalized-Fibonacci resultant literature exists, but
no searched source was found stating the exact project identity

`Res(Phi_K, X^2+3X+1)=F_K^2`

in this collision context. This is an **apparently new-within-search-scope**
derivation, not a global novelty claim; a failed search is not proof that the
identity has never appeared elsewhere.

The Carmichael and Bilu–Hanrot–Voutier DOI/title records were independently
resolved with the citation verifier; neither is retracted.

## Trace functions and quantitative sheaf theory

17. E. Fouvry, E. Kowalski and P. Michel, **A study in sums of products**, *Philosophical Transactions of the Royal Society A* **373** (2015), DOI `10.1098/rsta.2014.0309`.
18. E. Fouvry, E. Kowalski, P. Michel, C. S. Raju, J. Rivat and K. Soundararajan, **On short sums of trace functions**, *Annales de l'Institut Fourier* **67** (2017), DOI `10.5802/aif.3087`.
19. W. Sawin, A. Forey, J. Fresán and E. Kowalski, **Quantitative sheaf theory**, *Journal of the American Mathematical Society* **36** (2023), 653–726, DOI `10.1090/jams/1008`.

These provide relevant technology once the actual sheaves, singularities,
irreducibility/non-isomorphism, ramification and uniform conductor are proved.

## Elliptic families, Sato–Tate and isogeny detection

20. P. Michel, **Rang moyen de familles de courbes elliptiques et lois de Sato–Tate**, *Monatshefte für Mathematik* **120** (1995), 127–136.
21. Yu. G. Zarhin, **Homomorphisms of abelian varieties over geometric fields of finite characteristic**, *Journal of the Institute of Mathematics of Jussieu* **12** (2013), 225–236, DOI `10.1017/S1474748012000655` (arXiv:1012.5083).
22. B. Grove and H. Saad, **Hypergeometric distributions and joint families of elliptic curves**, *Research in the Mathematical Sciences* **12**, 74 (2025), DOI `10.1007/s40687-025-00554-2`.

Grove–Saad is a useful modern worked example because geometric independence is
established before square-root correlation is invoked. Zarhin-type results are
relevant under their hypotheses; neither is a plug-in proof for this pencil.

## Citation discipline

Any publication-grade use of an external theorem must cite the exact
theorem/corollary and verify its assumptions in the notation of this project.
Abstract-level similarity, nonconstant `j`, a search snippet or a successful
finite computation is not enough.
