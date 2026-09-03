# Literature and symbolic-check log

## 2026-09-03

- Scholarly search was used to distinguish rigorous cat-map eigenfunction/matrix-element results from genuine local spectral-statistics theorems.
- Citation audit matched five of six initially supplied records; the 2001 Kurlberg–Rudnick DOI record was ambiguous and is therefore flagged for a second metadata check rather than silently normalized.
- A targeted search surfaced Gamburd–Lafferty–Rockmore (2003), which is directly relevant to eigenvalue spacings but is substantially numerical for the generic GOE/GSE behavior.
- Wolfram symbolic algebra independently returned determinant/resultant `d^2` for the historical M1 Möbius map and the special forms at `d=0,±1`. This agrees with the hand derivation and the Python implementation.
- Wolfram also independently solved the pair-key elimination, reproducing `y=(1-v)/(u-v)` and `d=(u-1)(v-1)/(v-u)`. Substitution at `(u,v)=(1,1)` makes the eliminated polynomial identically zero while the inverse map is undefined, confirming the saturation artifact in the historical Möbius graph.
- The generic `t=0` off/off cubic singularity calculation was reproduced independently with SymPy and Wolfram. Wolfram gives a resultant proportional to `h1^5 h2^6 (h1-1)^14 (h1-h2)^4 (h2-1)^18`, so no extra affine singular stratum remains when `h1,h2!=1` and `h1!=h2`.
- The general-`t` cubic was symbolically reduced far enough to expose an explicit finite exceptional locus in the branch-quartic discriminant: `h1=h2`, the boundary value `(h1-1)(h2-1)+t(h1-h2)=0`, and the roots of an additional quartic `Q(h1,h2,t)`, besides the separate `h1=1`/`h2=1` cases.
- A trace-function literature search identified Fouvry–Kowalski–Michel, *A study in sums of products* (2015), as a plausible correlation framework. Their use conditions reinforce the correct next tasks: construct the relevant sheaf/trace function, bound conductor, determine monodromy, classify geometric isomorphisms/duals and isolate exceptional parameters before invoking square-root cancellation.
- Fouvry et al., *On short sums of trace functions* (2017), was added as supporting trace-function/Fourier background, and Kaplan–Petrow (2017) as elliptic-family point-count background. Scholar Sidekick verified the DOI metadata for all three new references.
- A separate rational-character-sum search located standard Weil-bound notes and surveys. For any paper statement, the exact theorem will be cited only after checking its hypotheses against the actual rational function, omitted boundary points and annihilator-character order `m`; the old unsourced “perfect K-th power” wording is not retained.

Research consequence: the active M1 problem is now a precise `L^2` correlation problem for the exact pair-key distribution `B(t)`, not a generic appeal to quantum ergodicity, a pointwise Weil bound, or an uncontrolled sum over twists.
