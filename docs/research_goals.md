# Research goals — current

The programme goal remains a rigorous BGS-type spectral result for the audited cat-map setting, with proof/reproducibility standards appropriate for a fundamental result. The immediate target is now narrower than the original M1 statement because cycles 001–002 separated what is solved from what is genuinely load-bearing.

Current goals:

- preserve the reproduced twisted-Jacobi, exact `k=2`, and independent new-prime layers as regression anchors;
- retain M1 cycle 001 as the exact weighted assembly: singular fiber, quotient-character projector, explicit cross terms, and the raw lower-bound obstruction;
- treat M1 cycle 002 as a closed **single-twist regular lemma**: after the exact polynomial domain mask, the standard multiplicative-character Weil theorem gives `|A_{r,s}(d)| <= 3 sqrt(N)` for every nontrivial regular twist;
- make M1-003 the active centering question: determine from the upstream spectral formula whether the deterministic singular term is removed exactly, rather than assuming it is negligible;
- make M1-004 the primary analytic estimate: control the assembled cross-twist covariance/energy without replacing the squared norm of a sum by a sum of squared norms;
- implement the `N=3571,K=17,m=210` stress case with a memory-aware C++ path and Python orchestration after the exact centering/covariance formula is fixed;
- use GOE spacing, number variance, moment scans, and additional split-prime designs as falsifiers/calibration rather than theorem substitutes;
- re-use higher-moment, word/automaton, and rank-2/Sp4 results only with their audited finite-N/experimental status;
- keep Lean formal obligations explicit and label new Lean files `UNVERIFIED` until an actual toolchain builds them;
- keep the repository compact at the active layer: one canonical producer per load-bearing computation, one compact result artifact, no committed binaries/caches/scratch runs, while retaining historical provenance separately.

Explicitly superseded shortcuts remain the historical Möbius-fiber M1 theorem and the R86/R87 noncommutative-binomial trace-fluctuation reduction. Root `STATUS.md` is authoritative.
