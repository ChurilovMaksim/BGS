# Bibliography and theorem-technology map

Only sources that constrain the active argument or its interpretation are
listed here. A citation is **not** a claim that its hypotheses have already
been verified for this project.

## Arithmetic quantum cat maps

1. P. Kurlberg and Z. Rudnick, **Value distribution for eigenfunctions of desymmetrized quantum maps**, arXiv:math-ph/0101008 (2001). Split-prime Hecke-eigenfunction value distributions; not an eigenphase-spacing theorem.
2. P. Kurlberg and Z. Rudnick, **On the distribution of matrix elements for the quantum cat map**, *Annals of Mathematics* **161** (2005), 489--507, DOI `10.4007/annals.2005.161.489`. Matrix-element fluctuations and moment calculations.
3. P. Kurlberg, L. Rosenzweig and Z. Rudnick, **Matrix elements for the quantum cat map: fluctuations in short windows**, arXiv:math/0701685 (2007). Shrinking eigenphase windows for sums of matrix coefficients, not microscopic eigenvalue correlations.
4. L. Rosenzweig, **On the fluctuations of matrix elements of the quantum cat map**, arXiv:0909.1410 (2009).
5. S. Gurevich and R. Hadani, **Proof of the Kurlberg--Rudnick rate conjecture**, *Annals of Mathematics* **174** (2011), 1--54, DOI `10.4007/annals.2011.174.1.1`.
6. S. Dyatlov and M. Jézéquel, **Semiclassical Measures for Higher-Dimensional Quantum Cat Maps**, *Annales Henri Poincaré* **25** (2024), 1545--1605, DOI `10.1007/s00023-023-01309-x`. Delocalization/support restrictions for eigenfunctions/semiclassical measures; not a local eigenphase-statistics theorem.
7. P. Kurlberg, A. Ostafe, Z. Rudnick and I. E. Shparlinski, **On Quantum Ergodicity for Higher Dimensional Cat Maps**, *Communications in Mathematical Physics* **406**, 174 (2025), DOI `10.1007/s00220-025-05350-1`.
8. S. Bhakta and I. E. Shparlinski, **On quantum ergodicity for higher-dimensional cat maps modulo prime powers**, *Bulletin of the London Mathematical Society* **58** (2026), DOI `10.1112/blms.70300`.

Items 1--8 concern eigenfunctions, matrix elements, delocalization or quantum
ergodicity. None supplies the microscopic GOE/GUE eigenphase law needed to
close BGS for the present family.

## Spectral-spacing evidence and rigorous model-class BGS results

9. A. Gamburd, J. Lafferty and D. Rockmore, **Eigenvalue spacings for quantized cat maps**, *Journal of Physics A* **36** (2003), 3487--3499, DOI `10.1088/0305-4470/36/12/336`.
10. Z. Pluhař and H. A. Weidenmüller, **Universal Quantum Graphs**, *Physical Review Letters* **112** (2014), 144102, DOI `10.1103/PhysRevLett.112.144102`. For time-reversal-invariant quantum graphs mixing in the classical limit, the paper proves agreement of all spectral correlation functions with GOE in the graph limit under its stated setup.
11. Z. Pluhař and H. A. Weidenmüller, **Quantum graphs and random-matrix theory**, *Journal of Physics A* **48** (2015), 275102, DOI `10.1088/1751-8113/48/27/275102`. Gives the corresponding all-correlation generating-function result for a class of mixing graphs, with explicit graph assumptions.

Item 9 is numerical spectral-spacing context, not a general local-law theorem.
Items 10--11 are important counterweights to any claim that BGS has no rigorous
model-class realizations: quantum graphs do admit proofs under precise mixing,
large-graph and structural hypotheses. They do **not** prove BGS for smooth
Hamiltonian systems or for the arithmetic cat-map family in this repository.

## Cyclotomic/cotangent rigidity used by the mixed term

12. S. Chowla, **The nonexistence of nontrivial linear relations between the roots of a certain irreducible equation**, *Journal of Number Theory* **2** (1970), 120--123, DOI `10.1016/0022-314X(70)90012-0`.
13. K. Wang, **On a theorem of S. Chowla**, *Journal of Number Theory* **15** (1982), 1--4, DOI `10.1016/0022-314X(82)90078-6`.

Wang states Chowla's prime theorem explicitly as Theorem A: for prime `K`, the
`(K-1)/2` real numbers

```text
cot(pi*a/K), 1 <= a <= (K-1)/2,
```

are linearly independent over `Q`. This is the exact external input used in
`mathematics/cayley_additive_energy.md`; Wang also extends the statement to
more general moduli and derivatives of cotangent. The DOI/title metadata for
both papers was independently resolved during the 2026-09-04 audit.

On September 9, Wang's Theorem A was checked directly in the
[author-posted article](https://www.researchgate.net/profile/Kai-Wang-227/publication/256257948_On_a_theorem_of_S_Chowla/links/5c423968a6fdccd6b5b7dd15/On-a-theorem-of-S-Chowla.pdf).
The same independence input classifies weighted Cayley relations of every
fixed length in `mathematics/cayley_trace_gaussian_limit.md`. That note proves
a full-trace Gaussian limit in its stated sparse regimes; no priority claim
is based on this source check.

## Fibonacci/Lucas divisibility and resultant structure

14. R. D. Carmichael, **On the Numerical Factors of the Arithmetic Forms α^n ± β^n**, *Annals of Mathematics* **15** (1913--1914). The original article was published in two consecutive JSTOR records, pp. 30--48 (DOI `10.2307/1967797`) and pp. 49--70 (DOI `10.2307/1967798`); later literature commonly cites the combined pp. 30--70 work.
15. M. Yabuta, **A Simple Proof of Carmichael's Theorem on Primitive Divisors**, *The Fibonacci Quarterly* **39** (2001), 439--443, DOI `10.1080/00150517.2001.12428701`.
16. Y. Bilu, G. Hanrot and P. M. Voutier, **Existence of primitive divisors of Lucas and Lehmer numbers**, *Journal für die reine und angewandte Mathematik* **539** (2001), 75--122, DOI `10.1515/crll.2001.080`.
17. T. M. Apostol, **Resultants of cyclotomic polynomials**, *Proceedings of the American Mathematical Society* **24** (1970), 457--462, DOI `10.1090/S0002-9939-1970-0251010-X`.
18. M. Baker, **Reciprocity via Reciprocants**, *The American Mathematical Monthly* **132** (2025), 303--315, DOI `10.1080/00029890.2024.2439819` (arXiv:2309.02512).

The load-bearing primitive-divisor input in
`mathematics/fibonacci_ratio_energy_proof.md` is Yabuta's Theorem 3: the
`n`-th Fibonacci term has a primitive divisor for
`n notin {1,2,6,12}`. In particular every `F_n` with `n>12` has a prime divisor
that divides no earlier positive Fibonacci number. This exact formulation was
read from the paper during the 2026-09-04 audit, rather than inferred from a
bibliographic snippet. Carmichael is retained for historical attribution;
Yabuta is the publication-grade theorem locator used by the proof.

Bilu--Hanrot--Voutier is a much broader primitive-divisor theorem for
Lucas/Lehmer sequences and is useful for possible extensions to other slices;
it is not needed to strengthen the Fibonacci special case. Apostol is standard
background for cyclotomic resultants. Baker proves a general square-root
phenomenon for resultants of even-degree reciprocal polynomials; this is close
prior art for the square structure, while the project's `K^3 M^2` theorem is
proved directly from the specific twisted reciprocity and the maximal real
cyclotomic subfield.

A bounded 2026-09-04 literature search checked cyclotomic-resultant,
reciprocal-resultant and generalized-Fibonacci-resultant terminology and nearby
citation chains. No checked source was found stating the exact project identity

```text
Res(Phi_K, X^2+3X+1)=F_K^2
```

in this collision context, nor the exact additive-energy theorem for
`{+-L_n/F_n}`. These are therefore described only as **apparently new within
the recorded search scope**, not as global novelty claims; failure to find a
source is not proof that an identity has never appeared elsewhere.

## Direct Cayley energy and finite-field incidence bounds

19. S. Makarychev and I. Vyugin, **Solutions of Polynomial Equations in Subgroups of $\mathbb F_p^*$**, *Arnold Mathematical Journal* **5** (2019), 105--121, DOI `10.1007/s40598-019-00112-z`. The load-bearing pointwise subgroup-curve estimate used in `mathematics/cayley_direct_energy.md` is the predecessor Theorem 2 in I. Vyugin and S. Makarychev, arXiv:1504.01354v2 (24 Sep 2015): for an absolutely irreducible bivariate polynomial of bidegree `(m,n)` with `P(0,0)!=0` and `deg P(x,0)>=1`, and `100(mn)^(3/2)<|G|<p^(3/4)/3`, a single product-coset fiber contains at most `16 m n^2(m+n)|G|^(2/3)` points. The inequality `deg P(x,0)>=1` was checked visually in the source PDF because text extraction can lose the equality bar. The 2019 journal paper is the later publication and separately verified bibliographically; theorem numbering is not assumed to be unchanged.
20. S. Macourt, I. D. Shkredov and I. E. Shparlinski, **Multiplicative Energy of Shifted Subgroups and Bounds On Exponential Sums with Trinomials in Finite Fields**, *Canadian Journal of Mathematics* **70** (2018), 1319--1338, DOI `10.4153/CJM-2017-044-2`. Corollary 4.1 gives a near-quadratic bound `E_x(G+lambda)-|G|^4/p << |G|^2 log|G|` in the small-subgroup range; this is relevant to the exact shifted-product reformulation in `mathematics/cayley_centered_energy.md` but does not by itself bound the moving distinguished product classes needed for Cayley additive energy.
21. M. Rudnev and J. Wheeler, **On incidence bounds with Möbius hyperbolae in positive characteristic**, *Finite Fields and Their Applications* **78** (2022), 101978, DOI `10.1016/j.ffa.2021.101978` (arXiv:2104.10534). Provides quantitative incidence and rich-Möbius-hyperbola technology. The current audit did not find a lossless specialization yielding the desired near-quadratic centered Cayley energy; generic use remains weaker than the active target.

All three DOI/title records above were independently resolved on 2026-09-04 and no retraction was reported. For item 19, the exact load-bearing hypothesis was additionally checked in the primary PDF rather than inferred from metadata or a search snippet.

## Dedekind sums and ratio-orbit separation

22. S. Jabuka, S. Robins and X. Wang, **When are two Dedekind sums equal?**, *International Journal of Number Theory* **7** (2011), 2197--2202, DOI `10.1142/S1793042111005088` (arXiv:1103.0370).

The ratio-orbit theorem in `mathematics/cayley_ratio_orbit_factorization.md`
uses the prime-modulus consequence of the necessary equality criterion proved
in this paper: if `K` is prime and `s(r,K)=s(s,K)`, then

```text
(r-s)(rs-1)==0 (mod K),
```

so the two residues are equal or inverse. The converse follows from the
standard symmetries of Dedekind sums. This is exactly what is needed to prove
that the coefficient `b_r` separates the ratio classes `{r,r^(-1)}` and hence
that `deg(P_s-P_r)=m-1` for distinct classes.

## Trace functions and quantitative sheaf theory

23. É. Fouvry, E. Kowalski and P. Michel, **Counting sheaves using spherical codes**, *Mathematical Research Letters* **20** (2013), 305--323, DOI `10.4310/MRL.2013.V20.N2.A8` (arXiv:1210.0851). Lemma 3.5 is the source-exact quasi-orthogonality statement used by the corrected off/off theorem: for geometrically irreducible, pointwise weight-zero sheaves of bounded conductor on a common lisse open and not geometrically isomorphic, the normalized complete trace correlation is `O(|k|^(-1/2))`. Its proof is Grothendieck--Lefschetz + Schur + Deligne RH + a Grothendieck--Ogg--Shafarevich cohomology bound.
24. É. Fouvry, E. Kowalski and P. Michel, **A study in sums of products**, *Philosophical Transactions of the Royal Society A* **373** (2015), DOI `10.1098/rsta.2014.0309`.
25. É. Fouvry, E. Kowalski, P. Michel, C. S. Raju, J. Rivat and K. Soundararajan, **On short sums of trace functions**, *Annales de l'Institut Fourier* **67** (2017), DOI `10.5802/aif.3087`.
26. W. Sawin, A. Forey, J. Fresán and E. Kowalski, **Quantitative sheaf theory**, *Journal of the American Mathematical Society* **36** (2023), 653--726, DOI `10.1090/jams/1008`.

Item 23 is now the primary theorem locator for the pairwise trace correlation in
`mathematics/offoff_elliptic_spike_theorem.md`.  The printed lemma is stated for
sheaves primitive on a common open set.  Our parameter classes have moving bad
points, so the project uses the lemma's proof on the intersection of their good
opens: Schur removes `H_c^2` for non-isomorphic geometric representations,
Deligne bounds `H_c^1` at square-root scale, and fixed rank/conductor plus only
boundedly many deleted points give a uniform cohomology dimension.  This avoids
silently applying a stronger statement than the source proves.

Items 24--26 provide broader trace-function technology.  For the centered
Cayley problem, the exact Fourier decomposition produces a family of
Kummer/Artin--Schreier transforms `T_chi(q)`; a useful trace-function argument
must exploit cancellation jointly across the annihilator-character family,
because termwise square-root bounds do not close the required fourth moment.

## Elliptic families, monodromy and Sato--Tate

27. A. Bandini, I. Longhi and S. Vigni, **Torsion points on elliptic curves over function fields and a theorem of Igusa**, *Expositiones Mathematicae* **27** (2009), no. 3, 175--209, DOI `10.1016/j.exmath.2008.06.001` (arXiv:0804.1425). Theorem 1.3 / Theorem 3.23 gives Igusa's open-image theorem for non-isotrivial elliptic curves over global function fields; Theorem 2.22 separately records irreducibility of `V_l(E)` for every `l!=p` in their setup. This is the monodromy source used after the project's explicit non-isotriviality check.
28. P. Michel, **Rang moyen de familles de courbes elliptiques et lois de Sato--Tate**, *Monatshefte für Mathematik* **120** (1995), 127--136.
29. Yu. G. Zarhin, **Homomorphisms of abelian varieties over geometric fields of finite characteristic**, *Journal of the Institute of Mathematics of Jussieu* **12** (2013), 225--236, DOI `10.1017/S1474748012000655` (arXiv:1012.5083).
30. B. Grove and H. Saad, **Hypergeometric distributions and joint families of elliptic curves**, *Research in the Mathematical Sciences* **12**, 74 (2025), DOI `10.1007/s40687-025-00554-2`.

The corrected off/off theorem no longer needs a separate classification of all
function-field isogenies.  Its exact finite singular-support polynomial recovers
the family parameter up to the already-known involution, which is sufficient to
classify geometric isomorphisms of the middle-extension sheaves inside the
family.  Bandini--Longhi--Vigni then supplies the irreducibility/open-image
input, and Fouvry--Kowalski--Michel supplies the source-exact trace-correlation
argument.  Michel, Zarhin and Grove--Saad remain useful context and templates,
but are not invoked as black-box replacements for those checks.

## Prime distribution input for the double-averaged mixed theorem

31. E. Bombieri, **On the large sieve**, *Mathematika* **12** (1965), 201--225, DOI `10.1112/S0025579300005313`.
32. H. Iwaniec and E. Kowalski, **Analytic Number Theory**, American Mathematical Society Colloquium Publications **53** (2004), DOI `10.1090/coll/053`.

The only load-bearing use of these sources in the current project is the
classical Bombieri--Vinogradov theorem for primes in arithmetic progressions,
used in `mathematics/cayley_jacobi_trace_average.md` to count the two-parameter
dyadic family of split designs after averaging over the prime modulus `K`.
The exact form used is Iwaniec--Kowalski, Theorem 17.1: for every fixed error
power, the sum over moduli up to `x^(1/2)` with a sufficient logarithmic saving
of the maximal progression error is `O(x log^(-A-1)x)`.  For every fixed
`theta<1/2`, the dyadic moduli `K asymp X^theta` eventually lie in this range at
both endpoints `X` and `X/2`.  The ordinary prime number theorem and partial
summation then give the dyadic main term.  No pointwise prime number theorem for
an individual varying modulus is assumed, and no Bombieri--Vinogradov input is
used in the pointwise `K^(8/3)` Cayley theorem.

Bombieri's DOI/title record and the Iwaniec--Kowalski book DOI were independently
resolved on 2026-09-04.  A secondary source was used only as a theorem locator
for the exact Iwaniec--Kowalski theorem number; the mathematical statement was
cross-checked against standard Bombieri--Vinogradov formulations.

## Citation discipline

Any publication-grade use of an external theorem must cite the exact
theorem/corollary and verify its assumptions in the notation of this project.
Abstract-level similarity, nonconstant `j`, a search snippet or a successful
finite computation is not enough.  When a printed theorem is stated under a
slightly narrower common-open hypothesis than the project family, the project
must either reduce to that hypothesis explicitly or reproduce the short proof
with the common-good-open modification, as done for Fouvry--Kowalski--Michel
Lemma 3.5 in the corrected off/off theorem.


## Source checks — 8 September 2026

**Corvaja–Zannier, JEMS 15 (2013), 1927–1942**,
[DOI 10.4171/JEMS/409, publisher PDF](https://ems.press/doi/pdf/10.4171/JEMS/409).
Theorem 2 (p. 1929) and Corollary 2 (p. 1930) were read directly.
For the smooth Cayley curve, the coordinate degrees are two, the four boundary
points give chi=4, and independent boundary valuations exclude a translated
subtorus. Substituting m1=m2=K and d1=d2=2 gives exactly
max(3*cuberoot(32)*K^(2/3),48*K^2/p). Odd characteristic ensures separability;
K divides p-1. This verifies the external implication in
`cayley_curve_uniform.md`. It is an application of a known theorem, with no
priority claim for the specialization. No local source copy was retained.

**Kieler–Fritzsch–Bäcker, Semiclassical foundation of universality in chaotic
quantum circuits**, [arXiv:2605.27052v1](https://arxiv.org/html/2605.27052v1).
Read the trace-formula and range-of-validity discussion around equations
(3), (11) and the subsequent resummation paragraph. The requested version URL
labels v1; its rendered author date is August 24, 2026, so metadata should be
rechecked before publication citation. The argument uses stationary phase and
explicitly conjectures the resummed Heisenberg-scale formula. It does not
supply this project's uniform joint-trace comparison. Classification: adjacent
semiclassical work, not an imported proof of the missing implication.
No local source copy was retained.

Search scope: web queries for BGS, rigorous spectral statistics and
band-limited Schwartz correlation extension on September 8, 2026. The two
internal extensions in this pass are self-contained; this bounded search does
not establish their global novelty.


## Recovery clarification, 20 September 2026

For the elliptic off/off proof, BLV arXiv:0804.1425v2 Theorems 1.3--1.4
supply arithmetic openness; Lemma 4.1 supplies the commutator congruence
subgroup inclusion used to pass to geometric irreducibility. Its proof is
sketched by reference. FKM arXiv:1210.0851v5 Lemma 3.5 and its proof were
checked for the common smooth open; v1 was unavailable in this pass. In
that paper purity of a middle extension is defined on its lisse locus.
The explicit singular-stalk wording in the recovered proof makes that
convention transparent. These are source-dependent clarifications, not
new monodromy or quasi-orthogonality theorems. See
[recovery audit](../record/recovery_audit_20260920.md).


## Recovered Heisenberg-scale analytic inputs (audited 21 September 2026)

- M. Jézéquel, *Distribution of Ruelle resonances for real-analytic Anosov
  diffeomorphisms*, arXiv:2212.09881. Proposition 4.3 is the trace-class
  periodic-point trace formula used by the recovered classical stability sum.
- D. Robert, *On the Herman--Kluk Semiclassical Approximation*,
  arXiv:0908.0847. Used only for the standard fixed-time semiclassical FIO
  expansion of a Weyl Hamiltonian propagator.
- F. Faure, *Semi-classical formula beyond the Ehrenfest time in quantum
  chaos. (I) Trace formula*, arXiv:nlin/0610004. Used for the torus nonlinear
  Anosov quantization framework; the recovered cyclic-ramp theorem itself
  needs only one fixed classical step, not the long-time trace formula.
- R. Cluckers, *Analytic van der Corput lemma for p-adic and
  F_q((t)) oscillatory integrals*, arXiv:1001.2013, Proposition 3.3.
  Used in the repaired N=19^k incomplete hyperbolic-sum theorem.


- S. Müller, S. Heusler, P. Braun, F. Haake, A. Altland,
  *Periodic-Orbit Theory of Universality in Quantum Chaos*,
  arXiv:nlin/0503052. Equations (29)--(30) define the encounter coefficients;
  equations (45)--(49) prove their order-by-order cancellation in the unitary
  class.  The repository's additional absolute envelope is a separate
  elementary combinatorial estimate, not attributed to the paper.
