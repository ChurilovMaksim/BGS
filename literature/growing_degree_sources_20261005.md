# Source normalization for the growing-degree projection

5 October 2026. Base: `9555cd19dbf7cac335320dc231f2a7b7bb71954f`.
This is a bounded source check, not a world-priority survey.

## Complex Hermite and Mehler identity

Allal Ghanmi, *Mehler's formulas for the univariate complex Hermite
polynomials and applications*, arXiv:1707.06969v1, 21 July 2017.
Primary PDF: <https://arxiv.org/pdf/1707.06969>.
The visible PDF identifies v1, and has five pages. Read (2.4) on printed
page 2 and Theorem 4.1, (4.1)--(4.5) on printed page 4. The source
credits earlier Itô, Wünsche and Ismail versions; no priority for this
classical kernel is claimed here.

For the project's Wick variance $m$, the exact dictionary is
$H^{[m]}_{a,b}=m^{a+b}H^{1/m}_{a,b}$.
In (4.5) set the source's $\nu=1/m$ and $u=v=rm$, with $0<r<1$.
The left side becomes
$\sum r^{a+b}|H^{[m]}_{a,b}(z)|^2/(m^{a+b}a!b!)$;
the condition $\nu^2uv<1$ becomes $r^2<1$, and the right exponent
becomes $2r|z|^2/[m(1+r)]$. The project additionally derives this
positive-real specialization by a Gaussian transition/Parseval argument,
rather than importing a larger complex parameter range.

The final journal citation is Mathematical Methods in the Applied
Sciences 40 (2017), 7540--7545, DOI:10.1002/mma.4545, corroborated by
the primary Wiley metadata. The proof normalization here pins the arXiv
version, not uninspected journal bytes. No byte hash for an undownloaded
PDF is invented.

## Inherited stable Haar input and geometry

Diaconis--Evans, *Linear functionals of eigenvalues of random matrices*,
Theorem 2.1(a), printed pp.3--4, remains the existing EXT-DE-2001
dependency; see [the checked record](signed_heisenberg_sources.md).
The Wick-basis Gram calculation uses its exact joint moments only when
$2Q\le N$. It does not use asymptotic Gaussian independence at growing
degree outside that stable range.

The odd-N frame and packet construction are the maintained
[FM-013 proof](../mathematics/fixed-map/fixed_time_wavepacket_trace_bound.md).
The degree/Jacobian return-volume bound is
[FM-007](../mathematics/frozen_seven_cut_reduction.md), (11), and retains
the same forward conjugation map $G$ and inverse packet-center map $F$.
The new exponential seminorm uniformity is an internal proof obligation;
neither a fixed-time source statement nor a finite numerical replay
automatically supplies it. It is written out in the new proof.

## Permutation heat spectrum: internally reconstructed standard mechanism

The new G15--G16 argument does not import an uninspected highest-weight
or heat-spectrum theorem. It gives the normalized counting-measure
isometry from class functions on $S_q$ to holomorphic Gaussian trace
polynomials, counts right transpositions to reconstruct cut-and-join,
and transports that operator through the Wick map. Each transposition
is a unitary involution, so the exact interval follows from its finite
operator norm. This is a standard permutation/Casimir mechanism;
no priority is claimed for it. The proof separately checks its
application to the particular fixed local pair test, where the norm is
Haar $L^2$, not point evaluation or supremum norm.

No new claim of deterministic spectral universality, external referee
approval, analytic Lean certification or world novelty follows from these
source identifications.
