# Roadmap

This roadmap is subordinate to root `STATUS.md`. Historical dates/probabilities from earlier roadmaps are not commitments or theorem status.

## Immediate work: M1 exact assembly

- derive the ordered twist expansion from the current character conventions;
- keep cross-twist terms explicitly;
- prove or falsify proposed orthogonality/covariance mechanisms;
- state the `(N,K,m)` scaling regime before estimating;
- check degeneracy/perfect-power hypotheses before applying finite-field bounds;
- validate formulas at `N=53,199,3571` and independent split-prime designs.

## Parallel computational work

- keep R82, exact `k=2`, and independent Theorem-II regressions green;
- extend GOE/number-variance experiments only with explicit statistic/reference definitions;
- port useful old research scripts from `src/` / `artifacts/` paths when they become relevant rather than mass-rewriting provenance;
- investigate higher moments/shape automata/word algebra as possible independent mechanisms, but do not use the superseded R86 scalar-binomial reduction.

## Rank-2 / Sp4

Retain exact `N=53` identities as calibration. Generalise only by stating and proving a uniform finite-field/rank-2 mechanism. Numerical `G0`, edge-mass, and trace-fluctuation probes stay experimental until such a theorem exists.

## Manuscript/formal work

A new proof-complete manuscript should only be promoted after its dependencies match `STATUS.md`. Lean files with `sorry`/opaque placeholders remain specifications of open obligations; generated `.lake` state stays out of Git.

## Repository discipline

Before a meaningful promotion, run `code/maintenance/repo_health.py` and regenerate the full audit inventory. Preserve failed/superseded calculations with explicit status rather than deleting them or silently rewriting their historical producer metadata.
