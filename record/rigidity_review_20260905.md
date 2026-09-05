# Fixed-strength review, analytic quantum bound, and general sharp extremum

Date: 5 September 2026. Read base: `ae01ae4585f86de0c97b00d165abf6cd9f11d999`.
The local checkout used to recover prior sources was an older research-branch
snapshot, not the current main tree. Publication is a focused delta on the
read main tree; no claim that the whole local checkout equals main is made.

## Actual mathematical delta

The fixed-strength support-separated construction had been stored as a Git
blob/tree without a reachable main file. Its original blob
`09d0df449b8cd39813194488b74cd0fd203c46fa` is preserved, not re-created as a
purported new discovery. The independent review gives operator-norm control
through every polynomial time window at fixed classical strength, and states
why smooth conjugacy retains arithmetic symmetries. It is an exceptional
family, not positive generic BGS.

A later exact read of the main tree showed that
`analytic_poisson_flatness_rigidity.md` already contained the classical
regular-gradient rigidity lemma. That lemma is not counted again. The revised
note retains its conclusion and adds the explicit quantum limit
hbar^(-1)||[Op(g),Op(g composed with S)]||_(2,N) -> ||{g,g composed with S}||_2.
A nonconstant analytic generator therefore cannot realize the all-orders
commuting-observable mechanism. This says nothing by itself about positivity
of the Green--Kubo variance of a nonzero bracket or about every possible
unitary conjugacy at an isolated kick parameter.

The same read found the Pell-only sharp finite-span theorem in
`pell_single_orbit_sharp_constant.md`, including its Fejer-kernel realization.
The present contribution is its extension to every hyperbolic matrix in
SL(2,Z), using the invariant Q_A(v)=det(v,Av), and independent exact tests
for four matrices. It does not claim to solve the Pell realization constraint
for the first time. The general minimum and all minimizing autocorrelations
are stated, with an explicit real Fejer--Riesz construction. The all-span
infimum is not attained by finite coefficients.

The complete first Fourier box is a genuinely multiorbit calculation. The
quartic includes mixed-sign terms, but an exact sum-of-squares decomposition
proves Gamma(g) >= 4*pi^2*||g||_2^4 and classifies every equality case.
It is not inferred by adding the single-orbit bounds. A sixteen-mode integer
polynomial in the radius-three box has the exact ratio
Gamma(g)/||g||_2^4 = (6563/2178)*pi^2 < 4*pi^2, disproving an extension of
that same constant to all boxes. Its norm sum is 396 and Gamma/pi^2=1890144.
Independent integer Python and C++ calculations agree on this witness.

The radius-two numerical search reached the radius-one bound in twelve local
runs. That is not a proof of the radius-two global minimum. Restricted linear
and diagonally-dominant SOS searches were infeasible on larger boxes; this is
not a proof of a zero of Gamma or of failure of an unrestricted SOS theorem.
The original exploratory programs and outputs remain in the delivery archive
with their original sandbox paths, not advertised as portable production code.
The maintained exact witness check has no dependency on those optimizers.

## Executed independent checks

The C++20 checker compiled with -Wall -Wextra -Wpedantic -Werror. Its
quadratic-ring representation and exhaustive orbit window agree with Python's
original-coordinate neighbour descent on 726 exact cases. The Python generic
implementation checks 720 further exact cases for three additional matrices.
The exact four-mode polynomial/SOS identity is checked coefficientwise; an
additional 80 finite coefficient vectors agree with C++.
Nine finite rational optimizers and six 100-decimal numerical spectral factors
are checked. The existence proof uses Fejer--Riesz, not numerical roots.

The flat-kick checker uses an exact nodal formula for the full smooth bump,
not an unquantified Fourier cutoff. It tests physical Weyl signs, aliases,
parity, unitarity and two exponential implementations. Removing the required
half-period hypothesis is a negative control with norm error about two.
Full matrices were evaluated at N=31,63,127,255,511,1023, at both signs of
kappa=0.02 and at kappa=0.1. These are not all Pell moduli; the finite
operator theorem does not require the Pell condition. Separate odd-spectrum
checks use Pell pairs (K,N)=(3,7),(5,41),(7,239), six kicks, and times up to
the odd dimension. They check finite inequalities, not asymptotic convergence.

Initial classical trajectory samples happened to stay on branches where both
implementations reduce to the same ODE, giving identical floating results.
The final checker adds preimages of the supported points, verifies nonzero
nonlinear displacement, and retains a wrong-sign negative control. Its 24
ODE comparisons are not interval certificates.

An attempted combined N=1023,2047 calculation exceeded the execution limit.
It is not a successful batch. N=1023 was subsequently run separately to
completion. No N=2047 result is promoted. There is no new successful Lean
compilation: a toolchain was not available locally and container DNS access
failed. No fake build status, formalization claim, or remote CI pass is used.

## Reproducibility

Run the three maintained checkers in `computations/verification/`, with `--cpp`
pointing to the compiled `pell_sharp_orbit_verifier` for the cross-check.
For the large flat matrix use `--sizes 1023` separately. The scripts emit a
JSON report only after all assertions pass. The small command recorder stores
exit codes, elapsed time, hashes and logs; a successful command is not a proof
certificate for the analytic results.

`manuscript/build_rigidity_paper.py` reconstructs the thirteen-page companion TeX
from four maintained notes and the compact numerical index. It was compiled with pdflatex and every page was
visually checked after rendering; the final log contains no overfull boxes. A misplaced tag inside a split
equation and missing table packages were caught by compilation and corrected
in the maintained sources, then the whole final paper was rebuilt.
The PDF and full raw reports are delivered in the accompanying source/evidence
archive. Repository publication includes the proof and reproducibility sources
and a compact evidence index; it does not falsely label the PDF as a remote
binary or all historical tests as rerun.

The source audit rejects a title-only alphaXiv retrieval which returned the
wrong paper, then checks the actual Keating--Mezzadri record and primary report.
Classical factorization, analytic zero-set locality and known cat-map anomalies
are prior work. World priority is not established by these targeted searches.
