# Research roadmap

Updated: 2026-09-03.

The repository is a multi-track research program. M1 is the present load-bearing bottleneck for the strongest proof line, but it is not the whole project. `STATUS.md` is authoritative for present theorem status; `RESEARCH_INDEX.md` maps the full corpus.

## Track A — certify the restricted M1 theorem draft

The cancellation mechanism and restricted proof chain are assembled. The immediate task is no longer to rediscover the old cross-term decomposition from scratch; it is to make the current chain publication-grade.

1. Hand/formally certify the generic cubic singularity resultant and binary-quartic discriminant calculations used by the elliptic-family model.
2. Audit the degree-12 `j`-map/no-isogeny argument case by case, including all characteristic exclusions.
3. Pin exact theorem statements and hypotheses for Igusa monodromy, Deligne purity, Zarhin geometric-field Tate, and quantitative sheaf quasi-orthogonality.
4. Complete projective-to-affine boundary/bad-fiber bookkeeping with explicit constants and no hidden exceptional strata.
5. Extend Lean/formal certificates for the finite/combinatorial pieces that are stable enough to freeze.
6. Run regression gates for every exact identity used as a normalization or exception-set input.
7. Only after the line-by-line audit succeeds, promote the restricted `K=o(N^(1/4))` M1 result from theorem draft to theorem.

## Track B — enlarge the asymptotic regime and approach general BGS

1. Determine which `K^4 sqrt(N)` terms are artifacts of pairwise quasi-orthogonality bounds and which reflect genuine geometry.
2. Seek family-level cancellation or stronger large-sieve/sheaf estimates that improve the first restricted range.
3. Revisit composite `K` and exceptional-prime structure with exact cyclotomic/resultant bookkeeping.
4. Translate M1 control into the precise hypotheses needed by the next local-statistics step; do not jump from a fourth-moment estimate directly to BGS.
5. State every asymptotic theorem with an explicit `(N,K,m)` regime and a remainder that actually vanishes in that regime.

## Track C — local spectral statistics and numerical falsification

1. Re-run the strongest archived spacing, rigidity, number-variance, Stieltjes/local-law and layer-scaling experiments with the corrected quantization/statistic conventions.
2. Keep valid historical numerical evidence, but regenerate promoted outputs with current producers and machine-readable provenance.
3. Design sweeps that vary `N` and `K` as independently as the arithmetic permits, separating surface terms and finite-size artifacts from true asymptotic behavior.
4. Replace informal random-matrix analogies by exact theorem hypotheses that can be checked for this deterministic arithmetic ensemble.
5. Use spacing/rigidity observables only after symmetry reduction and statistic definitions are independently audited.

## Track D — mine and re-certify the broader research corpus

The restored `code/`, `data/` and `docs/` trees are not museum storage. They are a backlog of potentially useful mathematics.

1. Moment/design line: classify which fourth/fifth/eighth-moment computations remain valid under the current pair-key normalization and promote only reproducible ones.
2. Kloosterman/subgroup line: identify exact lemmas that can feed the M1/general-moment program and separate them from heuristic scans.
3. Shape/relation-automaton line: use the consolidated C++20 DP as the supported implementation and mine old Run-82 experiments for exact combinatorial statements worth formalizing.
4. Rank-2/Sp4 line: reconstruct representation/basis conventions from definitions, then re-test diagonal and genuinely non-diagonal kernels before any theorem claim.
5. Diagnostics/red-team corpus: preserve counterexamples and failed routes as permanent regression tests where they protect against repeating an old mistake.

## Track E — language migration and implementation quality

1. Historical Julia sources remain once in `archive/legacy-workspace/`; every path must have a disposition in `research/engineering/language_migration.md`.
2. Python is the readable exact/symbolic/analysis layer.
3. C++20 is the default for heavy finite-field loops, exhaustive combinatorics, relation DPs and independent exact verification.
4. Fortran is introduced only after profiling identifies a dense numerical kernel for which it gives a concrete performance/robustness benefit.
5. Do not create duplicate implementations merely to say a result was checked in another language; independence must serve a scientific certificate.
6. Migrate stale paths/APIs in the broad Python corpus opportunistically when a script is promoted or reused, rather than rewriting hundreds of historical scripts without a scientific reason.

## Track F — formalization, manuscript and repository integrity

1. Keep exactly one active manuscript source: `paper/main.tex`; keep `paper/main.pdf` synchronized from it.
2. Fold publication-ready results into that manuscript rather than creating competing `final`, `proof`, `complete` or section-level article trees.
3. Keep `README.md`, `RESEARCH_INDEX.md`, `STATUS.md`, `THEORY.md`, `HISTORY.md` and this roadmap mutually consistent.
4. Preserve the broad research corpus in ordinary working paths; do not hide it in `archive/` merely to make the repository look small.
5. Keep generated build trees, caches and bundled tool binaries out of version control.
6. Maintain machine-checkable health gates for source syntax, JSON parseability, Julia absence from the active tree, canonical manuscript uniqueness, and required provenance directories.

The operating standard is: preserve the laboratory record, make current claims easy to locate, and require stronger evidence each time a historical result is promoted into the theorem chain.
