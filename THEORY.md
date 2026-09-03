# Theory map

This is a short map of the current mathematical architecture. The detailed current derivations live in `research/theory.md` and `research/notes/`; the full historical notebook is `docs/THEORY_FULL_PRE_REBUILD.md`.

## Goal

For quantized hyperbolic cat maps after the relevant symmetry reduction, establish local spectral statistics compatible with the BGS/random-matrix prediction in a rigorous asymptotic regime.

General BGS is not currently proved.

## Current fourth-moment object

For an odd split prime `N`, subgroup `H <= F_N^*` of order `K`, and `m=(N-1)/K`, the current exact fourth-moment organization uses the weighted pair-key distribution `B(t)` and its nonzero-frequency Fourier transform `Sigma4(q)`.

The exact identities include:

- a closed finite formula for `V4=sum_t B(t)`;
- the pair-key factorization linking character-averaged fourth moments to `B(t)`;
- exact mean/variance Fourier duality between `Sigma4(q)` and `B(t)`.

These replace the historical Mobius-fiber assembly, which used the wrong finite object/multiplicities and is not an active theorem input.

## Structural decomposition

The useful decomposition is

`B(t)=O(t)+2(N-2)C_H(t)+(N-2)^2 1_(t=0)`.

The mixed `k=2` term `C_H` becomes an additive-difference energy problem for the Cayley image of `H\{1}`. For odd prime `K`, a finite cyclotomic audit isolates explicit exceptional primes and otherwise gives exact control of the mixed energy at the target M1 scale.

The off/off term `O(t)` is organized by a family of plane cubics/elliptic curves in Cayley coordinates. The generic family is non-isotrivial; the current analysis classifies the relevant involution/isogeny obstruction and isolates the reducible bad fiber whose spike is already controlled by the mixed energy.

## Restricted M1 theorem draft

Combining the exact finite decomposition, generic elliptic-family geometry, fixed-complexity sheaf bounds, bad-fiber control and covariance estimates yields an assembled draft in the first regime

`K=o(N^(1/4))`.

The intended conclusion is

`Var_(t!=0) B(t)=O(K^2 N)`,

hence

`std Sigma4=O(NK)` and `std(Sigma4)/mean(Sigma4)=O(K/N)`.

This is **not yet promoted to a final theorem**. Remaining work is a publication-grade line-by-line audit/formalization of the algebraic factorizations, exception sets, sheaf-theoretic hypotheses and citations.

## Other research lines

The repository also contains substantial work on:

- exact low moments and moment designs;
- large-m spectral experiments, spacing/rigidity diagnostics and numerical controls;
- shape/relation automata and exact dynamic programming;
- subgroup/Kloosterman sums and finite-field utilities;
- rank-2/Sp4 experiments and falsifiers;
- Lean formalization of finite/combinatorial components;
- failed proof routes and red-team analyses retained as negative knowledge.

See `RESEARCH_INDEX.md` for the directory-level map and `STATUS.md` for the authoritative trust boundary.
