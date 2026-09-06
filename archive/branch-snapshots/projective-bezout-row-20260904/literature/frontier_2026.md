# Frontier check — 4 September 2026

The literature was rechecked during reconstruction and again during the
prime-order Cayley/resultant work. The purpose is to keep five different
questions separate: eigenfunction delocalization, quantum ergodicity,
matrix-element fluctuations, finite-field moment arithmetic, and microscopic
eigenphase statistics.

## What established cat-map results give

Kurlberg–Rudnick's arithmetic cat-map work gives strong Hecke-eigenfunction and
matrix-element results. Their 2005 Annals paper computes second and fourth
moments of normalized matrix elements and compares them with a conjectural
SU(2)-trace distribution. Kurlberg–Rosenzweig–Rudnick study matrix-coefficient
sums in shrinking eigenphase windows. These are important precedents for the
present moment calculations, but neither is a microscopic GOE spacing theorem.

Dyatlov–Jézéquel (2024) prove support/delocalization restrictions for
semiclassical measures of higher-dimensional quantum cat maps under explicit
dynamical assumptions. Kurlberg–Ostafe–Rudnick–Shparlinski (2025) prove a
higher-dimensional quantum-ergodicity theorem, and Bhakta–Shparlinski (2026)
obtain prime-power quantum-ergodicity results. These are significant
eigenfunction advances; none supplies the local eigenphase-correlation bridge
required here.

Gamburd–Lafferty–Rockmore remains useful numerical spectral-spacing context and
illustrates that arithmetic structure can change the observed statistics. It
does not replace a local-law proof.

A September 2026 search found no rigorous result that closes microscopic
BGS/GOE eigenphase statistics for the structured arithmetic family considered
in this repository. This is a literature-search conclusion, not an
impossibility theorem.

## Rigorous BGS in special model classes

Pluhař–Weidenmüller prove random-matrix spectral-correlation statements for
mixing quantum graphs under explicit large-graph and structural hypotheses.
These results are important because they show that BGS-type universality can be
made rigorous in a special model class. They do not provide a theorem that can
simply be transplanted to arithmetic cat maps or smooth Hamiltonian systems.

## New internal finite-field progress and its literature inputs

For odd prime subgroup order `K`, the project now proves characteristic-zero
Cayley-difference rigidity from Chowla's rational linear independence of
prime-order cotangents (with Wang's 1982 paper used to verify the exact prime
statement).

The next internal theorem is algebraic rather than literature-imported: every
cleared collision resultant has shape

`Res(Phi_K,P)=K^3 M^2`.

An explicit slice has

`Res(Phi_K,X^2+3X+1)=F_K^2`.

A bounded search of cyclotomic-resultant and generalized-Fibonacci-resultant
literature found adjacent identities but no checked source stating this exact
collision identity. It is therefore described only as apparently new within
the recorded search scope, not as a global novelty theorem.

The proof that the associated rational set `{+-L_n/F_n}` has only constant
excess additive energy uses the classical primitive-divisor theorem for
Fibonacci numbers. Yabuta's 2001 proof explicitly states Carmichael's theorem
in the exact form needed: outside the classical small exceptions, the relevant
Fibonacci term has a primitive divisor. Bilu–Hanrot–Voutier supplies a broader
modern Lucas/Lehmer context but is not required for the Fibonacci special case.

The resulting 28-digit `(K,p)=(131,F_131)` finite certificate changes the
mixed-term interpretation: very large exceptional split primes can exist while
the extra additive energy remains only `32`. The next target is therefore a
uniform energy theorem, not a universal zero-collision cutoff.

## What the elliptic/sheaf literature does and does not give

Michel and more recent joint-family work such as Grove–Saad illustrate the
right architecture for square-root cancellation in elliptic families: first
identify the family and bad locus, then establish the required
monodromy/independence or non-isogeny statements, and only then apply
cohomological trace estimates.

Quantitative sheaf theory of Sawin–Forey–Fresán–Kowalski is relevant for
uniform complexity bounds once the actual sheaves and singularities are under
control. Zarhin's Tate/isogeny results are relevant to detecting isogeny from
suitable Galois-module information under their hypotheses. None of these
results turns “nonconstant `j`” by itself into the correlation theorem required
by the present off/off pencil.

## Defensible frontier position

1. The corrected pair-key reduction and Fourier identities are exact.
2. Prime-order characteristic-zero Cayley rigidity, square-resultant structure,
   the Fibonacci resultant slice and the rational almost-Sidon energy theorem
   are current exact results, with finite Python/C++/Lean regressions at clearly
   separated evidence levels.
3. A useful polynomial-scale bound for the mixed Cayley **energy** is still
   open; the Fibonacci slice proves that eliminating every exceptional
   collision is the wrong closure condition.
4. The off/off elliptic-family organization is a focused theorem draft, but its
   algebraic-geometric and sheaf hypotheses are not yet closed.
5. The restricted M1 estimate remains conditional until the mixed-energy and
   off/off obligations are both strong enough in the same growth regime.
6. Even a completed moment theorem would still require a separate
   local-law/comparison argument to reach microscopic BGS/GOE eigenphase
   statistics.
7. No checked source makes the historical claims “general BGS solved”, “M1
   proved by Möbius fibers”, or “finite GOE fit proves a limit law” defensible.

The detailed source map is in [`bibliography.md`](bibliography.md).
