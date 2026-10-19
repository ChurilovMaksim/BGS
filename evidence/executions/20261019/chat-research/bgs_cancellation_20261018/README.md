# BGS signed circular-phase calculations — 2026-10-18

Start with BGS_signed_cancellations_ru.md. This package contains partial results for the symplectic Fourier phase ensemble, not a solution of BGS.

The main new statement is the computer-assisted fixed-power estimate

\[
 \mathbb E|\operatorname{Tr}U^m|^2=m+O_m(N^{-3}),
 \qquad m\ge17,\quad N=p^{2d},\ p\text{ any odd prime}.
\]

The supporting proof files are signed_trace_formula_ru.md, rank_two_cancellation_ru.md, finite_core_expansion_ru.md, and second_order_cancellation_ru.md. The separate exact_absolute_barrier_ru.md proves why taking absolute values of every exact coefficient fails at times of order square root N.

## Reproduction

Requirements: Python 3.12, a C++20 compiler (the recorded runs used g++ 13.3.0). Exact runs use the Python standard library. Descriptive sampling additionally used NumPy 2.3.5 and SciPy 1.17.0.

From the extracted package run:

    PYTHONDONTWRITEBYTECODE=1 python3 reproduce.py /absolute/path/to/new-output

This repeats the unfiltered p=13 core enumeration and the prime-complete open-core enumeration, with fresh binaries and logs. To repeat all earlier exact controls, add --all. To repeat the numerical spectral samples, add --with-sampling. The output directory must be new. Certified input records remain unchanged.

The portable reproducer is supplied for convenience. The original bounded runs, resource limits, input/output hashes and failures are recorded in the nine run manifests. The failed signed_run is retained; the corrected successful run is signed_run_v2. Compiled executables and private upload files are excluded from the archive.

## Scope and provenance

All mathematics and implementations were produced and reviewed by the same author. Arithmetic checks with different implementations are not independent peer review. No novelty or priority claim is made.

The current proof is self-contained relative to its finite enumeration. The earlier mesoscopic theorem is contextual; it is not used to derive either cancellation.

Parent research archive, not included or modified:

    BGS_mesoscopic_20261018.zip
    SHA256 163f0dac01d9791e0a10221fdb41e6d4edfa2f9944a2b826aedc59cde812a837

Previous trace-law archive:

    BGS_trace_laws_20261018.zip
    SHA256 f92f7ba8afb5e7218eb39b5c1408aff306954b5c30cc000c774de0424e30aecd

repo_integrity.json records the read-only comparison against the 716-file repository snapshot. No repository changes, commits or pushes are part of this package.
