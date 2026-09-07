# Session science synchronization — 2026-09-07

## Git boundary

The remote base before the late-session synchronization was `7f9ac291da9b484d2c89e9ba7228ce0b6c6a7ae4`. The preceding 52 real commits in the audited session history were already linear ancestors of that commit. A previously reported `e1ff0d2a71403547e0bb8c9e3e7cdcf9ff9edb2c` does not resolve on GitHub and is not counted as a repository commit.

The information-limit science first landed through the continuation ending at merge commit `b4b601d76193123e250cee0180052b873575afe3`. The readback audit was committed as `8d8de801faf38c832a69726c97952c2cb3b51a0e`; verified external references were added in `79d0fb1dcd2a52a248870ecd16e8ced85e80a27c`; and the rare-phase, fixed-noisy-Gaussian and uniform pure-loss theorem/proof sections were then embedded directly in the canonical article in `60ac556b0bdb5b324e3013f38f57a8cba20b02bb`. Thus these results are not only side notes or certificates: they are present in `manuscript/WoW_unified.tex` on `main`.

## Byte-level remote/local check

The following files were read back from GitHub and their Git blob SHA values matched the independently rerun local sources exactly:

- `computations/verification/gaussian_channel_minimax.py` — `922a4983803e59bb61900ff3f81e8acb2993719c`;
- `computations/verification/pure_loss_discrimination.py` — `8b0ffe659bb6afc49d3d526e0511953d4b747362`;
- `computations/verification/rare_phase_testing.py` — `aa8334b446d992a12b19f1004b4bdcee17b7420d`;
- `computations/verification/rare_phase_limit.py` — `0432b1516bda2965d77a49b7c26abbb02c49dcb2`;
- `computations/cpp/pure_loss_discrimination_bounds.cpp` — `8f7289cc92b2ce52ba75484ff05462b828a46642`;
- `computations/cpp/rare_phase_certificate.cpp` — `c93bddf24956a27f6748af133c7cd523691585af`;
- `evidence/certificates/pure_loss_discrimination_20260907.json` — `8da4fe9b981c091c55fcde1a6e79294dd0fb9ae6`;
- `evidence/certificates/rare_phase_gaussian_20260907.json` — `3c50e1e0b535bad85237f2c2f5b8a1df76eba71a`.

`CMakeLists.txt` (`307b909a2c9a7a8aaac5bfbc78ea1985a2c72a15`) and `computations/analysis/gaussian_inverse.py` (`b1685fc580f6f88d5517697f7e54f3554571943b`) likewise matched the synchronized local sources. One proof-note SHA difference was inspected and reduced to presentation-only spacing; the theorem statement, proof inequalities and constants were the same, so no content-free replacement commit was made.

## Clean rerun after synchronization

A fresh fail-closed rerun was made after the readback check, with Python assertions enabled and C++ compiled using `-std=c++20 -O2 -Wall -Wextra -Wpedantic`.

- uniform pure loss, Python: **PASS**, 440 scalar grid points plus 300 finite-`B` cases; maximum tested ratio of proved left side to theorem right side `0.05514879935351338`;
- uniform pure loss, independent Boost.Multiprecision C++: **PASS**, 168 cases;
- rare-phase exact verifier: **PASS**, 8192 series terms, 4096 central-binomial tail checks and four finite-copy checks;
- rare-phase independent C++ replay at 8192 terms: **PASS**, with its outward-rounded interval contained in the Python interval;
- critical likelihood quadrature: **PASS**, order 112 and 1536 angles; the Chernoff-constant diagnostic was `2.9086102353618015` and is not used as the exact interval certificate;
- Gaussian inverse verifier at dimension 6 and 95 decimal digits: **PASS** — 1296 exact Weyl matrix-unit inversions, 512 loss identities, four additive-noise factorizations, six exact finite half-loss inequalities, 18 independent Kraus characteristic checks, nine fidelity checks, 146 Weyl-kernel bounds and 16 amplifier trace-norm bounds.

Finite execution remains finite evidence: the continuum/asymptotic theorems are supported by the analytic proofs and are not inferred by enumeration.

## Canonical claim boundary

The dated status authority for this late-session block is `record/bosonic_information_claims_20260907.md`. It records:

- the certified rare-phase profile/exponent and finite `n=128` separations;
- fixed-noisy phase-insensitive Gaussian input minimax risk `Theta((log B)^(-beta/2))` against arbitrary collective output POVMs and the matching deterministic inverse modulus;
- the certified `3e39 < B_75 <= 4e39` half-loss known-pair bracket;
- the uniform pure-loss binary law with varying transmissivity;
- the still-open full minimax transition when physical noise vanishes with sample size;
- microscopic BGS/GOE/COE universality as open.

## Publication and cloud-runner boundary

A self-contained flattened manuscript candidate and matching PDF were built locally with three pdfTeX passes and page-image inspection. The source had 8097 lines, 56 top-level sections, zero `\\input`/`\\include`, and SHA-256 `e7e0ddcee9d4ee96683b9e7640b509e283b8011582dac28fe0e7b3937b81f583`. The matching 146-page PDF has SHA-256 `55f759c1d4205d76b6499cbf52e52d2caf0273eac18aa0eaa990cbab94c73edd`.

The science in that candidate is synchronized remotely and embedded in the canonical article, but the physical one-file replacement and PDF byte upload are not represented as an atomic GitHub publication. The available GitHub connector can write UTF-8/blob content but exposes no local-file parameter for the generated PDF, while local GitHub DNS/CLI access is unavailable. GitHub Actions attempts also ended before any workflow step executed (`steps=[]`, `runner_id=0`). Consequently the split source files are intentionally retained rather than deleted before a verified atomic replacement can be transferred. This is a repository-transport limitation, not a scientific verification failure.

External priority, independent referee acceptance and microscopic BGS/GOE/COE universality remain unclaimed/open.