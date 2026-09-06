# Fixed-strength locality: research and verification audit

Date: 2026-09-05. Remote base read in this pass:
`ea46a93f9ca09141a83fe784d22119776f5fe2e9`.
Local computations initially used the accessible bundle at
`3e702064d6500c2d87588a1a382899a61e654d46`; the new remote branch uses the
later main and preserves its additional resonance and Edgeworth files.
An archive built from that remote branch, not the earlier local worktree,
is required for a claim of an exact synchronized source snapshot.

## Mathematical result and limits

The one-exponential kick with a fixed classical parameter is compared in
operator norm with a conjugated cat propagator. Disjoint smooth supports
annihilate every local bidifferential coefficient, leaving an explicit
Fourier Taylor remainder. This gives all inverse powers of N and, for the
specified Gevrey-2 bump, a conservative stretched exponential. Telescoping
therefore reaches Heisenberg and all fixed polynomial times.

Pell spectra have K equal-rank clusters of superpolynomially small diameter.
The actual gaps, factorial pair tests, and random-origin local point process
are controlled. The collapse survives polynomially bounded monotone unfolding.
The mean intensity remains one but the local process becomes empty in
probability: this is loss of uniform integrability, not a contradiction.

The classical map is exactly smoothly symplectically conjugate to the cat
map. Arithmetic approximate commutants survive. This is a nongeneric family,
not a claim of universal BGS, absence of hidden symmetries, or prize-level
priority. The infinite-dimensional space of generators also gives explicit
nontrivial zeros of the earlier quartic functional Gamma; it does not
contradict its generic nondegeneracy statement.

## Failed approaches and corrections retained

Poisson commutation was rejected as an adequate condition. For a=b_(1,0)+
b_(0,1) and b=a^2 the first Weyl commutator coefficient vanishes, but the
third has eight nonzero integer coefficients. Independent exact C++ and
Python calculations verify that negative control.

An initial two-dimensional Fourier cutoff 160 gave an operator discrepancy
about 1.91e-5 and failed. Cutoffs 80,160,320,640 showed discrepancies about
4.69e-4,1.91e-5,7.33e-7,2.36e-9. The implementation was refined rather
than declaring the low-cutoff result a successful quantization check.
The actual bump matrix uses cutoff 2048 and a separate 4096 refinement;
reported differences are below 3e-14 in the successful N<=511 cases.
These are refinement diagnostics, not interval-certified tails or rounding.

A combined larger dense experiment at N=1023,2047 exceeded 180 seconds
before producing a result file. No value from it is promoted as successful.
The reported actual-matrix set is N=7,41,127,239,511 at kappa=1/8. It
includes nonmonotone finite errors, which are not removed or fitted to an
asymptotic exponent.

The first integer cluster fixture incorrectly requested zero close pairs
at threshold one when n=1. Distinct clusters can then be one mean spacing
apart. The universal theorem requires the stated separation inequality;
the finite fixture now uses threshold 1/3, also valid at n=1. An exact
circle-arc union calculation independently checks the random-origin bound.

The first evidence promotion failed the repository's producer check. Both
producers were added and the calculations rerun; the audit was not disabled.
An attempted replacement of the older Floquet C++ target was rejected after
schema inspection showed that the existing pell_pair_orthogonality target
was the correct producer. The maintained workspace runner keeps that target.

## Verification layers

The targeted Python run checks 5,603 exact rational grid cases, physical
Weyl covariance including odd-product modes and a composite modulus, Fourier
quadrature and independent assembly, and actual single-kick matrices.
The C++ run checks 24 support corners, the exact cubic Moyal coefficients,
200 integer cluster fixtures, 11,008 gaps, and 200 circle-coverage bounds.
The computed JSON, not rounded figures in this narrative, is authoritative.

A local full execution pass completed 47/47 commands on the earlier-base
worktree. A subsequent refinement of the C++ coverage test was compiled
and run separately. Therefore final remote verification on the frozen
integrated source is a separate obligation, not inferred from that count.
Its manifest records the actual base, source hashes, commands, and logs.

The local environment has no Lean toolchain and could not resolve external
hosts for installing one. The remote workflow compiles the imported modules
with failure propagation. LocalityKernels proves only algebraic support and
counting kernels; all-orders analysis and Theorems A-C are not formalized.
A successful remote compiler log is required before calling even that narrow
module machine-checked.

## Literature and rendering

The elementary locality and commutator-sensitive product machinery is
standard, as is factorial optimal truncation in Gevrey analysis. Primary
arXiv text for Hitrik--Lascar--Sjoestrand--Zerzeri was read, especially the
nonoptimal factorial remainder in equation (3.151). The web PDF renderer
failed, so no visual inspection of that external PDF is claimed. Prosen--
Znidaric is direct prior art for residual/coboundary perturbations. The
Keating--Mezzadri 2000 bibliographic record was verified, but the full article
could not be retrieved; a title-based tool match to a different paper was
rejected. The absence of a matching search result is not a priority argument.

The locally generated eight-page proof was rendered and every page checked
in two contact sheets. There was no horizontal overflow. The remote final
article must be checked against its source and regenerated manifest.
