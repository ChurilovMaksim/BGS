# Scientific status

Updated: 2026-09-03.

## Established finite statements and reproducibility anchors

- Twisted-Jacobi fourth-moment baseline reproduces the preserved R82 data at `N=199` and `N=3571` to approximately `6.0e-14` and `2.4e-13` maximum absolute deviation.
- The exact `k=2` character-orthogonality reduction is reproduced at `N=53` and `N=199`; the off-diagonal constraint counts are `132=(13-1)(13-2)` and `90=(11-1)(11-2)`.
- The vectorized twisted-Jacobi matrix formula agrees with independent direct scalar character sums at `N=461` and `N=19489` within the recorded numerical tolerance.
- The `k=4` factorization has now been independently rechecked by clean Python and C++ implementations at `N=23` and `N=53` (two q values at `N=53`); the finite constraint-variety counts are `48621` and `423879`.
- More generally, the even-moment factorization follows algebraically from expanding `J^s conjugate(J)^s` and applying character orthogonality twice.  This reduction is exact; it does **not** supply the asymptotic estimate on the resulting high-dimensional variety.

## Numerical evidence only

- GOE nearest-neighbour spacing tests pass the stored finite-sample criteria at the audited designs.  This is evidence, not a limiting theorem.
- Matched-GOE number variance agrees within the stored two-standard-error criterion for the tested windows.
- The old archive contains a potentially important three-design pattern `rel_k ~ c(k) K/N` for `k=2,4,6,8` and a resolvent/Stieltjes convergence experiment.  These are now in the archaeology queue for clean reruns; they are not promoted as theorems.

## Main open problem: M1 fluctuation energy

The historical Möbius-fiber proof is invalid.  Two independent implementations show that its diagonal-only energy decomposition omits nonzero cross terms.  In addition, the claimed uniform `4 sqrt(N)` bound fails on the degenerate fiber `d=0`: for semi-trivial twist pairs `(psi_1=1, psi_2!=1)`, the exact value is `A(0)=N-2`.

The repaired problem is to derive the exact twist assembly, classify all exceptional fibers/twists, obtain the full cross-Gram formula with one Fourier normalization, and prove a remainder that genuinely tends to zero in a stated `(N,K,m)` regime.

## Explicitly not active

- “General BGS proved.” — false.
- Historical `M4D_PROOF` / Möbius-fiber theorem — superseded by the M1 audit.
- R86/R87 trace-fluctuation shortcut — invalid as stated because it applies a commutative binomial expansion to noncommuting matrices and then uses an unproved factorization.
- Historical `N=95419` ratio-vs-spacing KS result — invalid comparison of different statistics; raw numbers are preserved in the archive.
- Old word-trace “certificate” — unresolved word case, not a proof.
- Old Sp4/rank-2 theorem labels — retained as promising archaeology until their projector/basis conventions are independently rebuilt and checked.

No file in `archive/` changes the status above.
