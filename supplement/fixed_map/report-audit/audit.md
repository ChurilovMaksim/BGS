# Audit of the two external research summaries and continued calculations

**Date:** 19 September 2026.
**Base revision:** e0ada2e2c44dfe10bebf928dc8a1d6526ae15cb7.
**Primary verdict:** incomplete as a proof of microscopic universality;
two proposed spectral implications are refuted in their stated scope.
**Review:** self-review, a separate focused agent review of the cubic
variance, exact algebra, independently implemented finite CUE integrals,
and finite quantum calculations. No external referee,
Lean certificate, priority claim, or solution of BGS is asserted.

The inputs are the complete uploaded `research-summary.md` and
`research-summary (1).md`. Their hashes are recorded in `checkpoint.json`.
They discuss several different symbols, quantum sectors, and limits.
They cannot be treated as one theorem about the frozen map by silently
identifying those choices. Their internal /session/... references do not
supply accessible proof bodies or definitions in the uploaded files.

## 1. Findings that change the research direction

| Claim in the summaries | Verdict | Decisive evidence |
|---|---|---|
| All connected higher trace sums should vanish for arbitrary compact Heisenberg-scale Fourier support | Refuted for the displayed unsubtracted target | The CUE cubic moment is N-(N-a)_+-(N-b)_++(N-a-b)_+, and a smooth cubic test tends to 1/2 in L2 |
| Resonance sparsity plus unitary return amplitudes gives O(1/rho_N) pair suppression | Refuted as that implication | Exact pair normalization gives a bound O(N/rho_N); a scalar monodromy saturates it |
| rho_N grows on density one and its reciprocal has a vanishing Cesaro mean | Correct, but weaker than necessary | The determinant argument gives rho_N >= 2 acosh(N/2)/log(lambda) for every N>=3 |
| The explicit classical quartic projection has top coefficients 1/1024 and no +/-6 modes | Verified | Exact Fourier convolution in Q(zeta_24), elementary integration, and Wolfram agree |
| The entire cubic obstruction has been eliminated | Not established from the supplied definitions | The full cubic vertical projection is nonzero; only specific channels are shown to vanish |
| The quantum quartic top coefficient is literally the classical coefficient | Not justified | In non-aliased midpoint quantization it is (1+cos(16pi/N)+cos(32pi/N))/3072 |
| Hyperbolicity and topological mixing under the explicit bound, and non-C1 affine conjugacy for sufficiently small nonzero coupling | Verified with a named classical classification input | Hessian/cone estimates, Newhouse Corollary (1.3), and the fixed-point trace derivative 678.941627... |
| All exact finite unitary symmetries are scalar and no antiunitary reversor exists | False literally; requires geometric qualifications | Every unitary has a spectral commutant and an eigenbasis conjugation reversor |
| The only remaining ingredient for exclusion of f_star is a reduced-remainder bound | Not established | The reduction and its necessary connection to BGS are undefined; the kappa/hbar_N scale must also be controlled |
| Uniform tightness of the randomly rooted local point process | Correct | Exact mean count equals interval length, followed by compact exhaustion and Markov |

The last tightness statement applies to every finite spectrum after random
rooting; it does not identify a limit or establish convergence of its
correlation moments. Without uniform integrability, even intensity one
need not pass to a subsequential limit. The (N-1)/2 parity sector must have positive dimension,
so N=1 is excluded when that sector is invoked.

Two additional algebraic checks clarify the other branches of the summaries.
The identity I+S+S^2=7S follows directly from S^2-6S+I=0. Thus the kernel
of I+S+S^2 on (Z/NZ)^2 has exactly gcd(7,N)^2<=49 elements, because S
is invertible. Its mass for the *uniform* phase-space counting measure is
at most 49/N^2. Negligibility for the report's undefined weighted typical
measure does not follow without a bound on its weights. Likewise, given
the reported formulas for K_3,V_6,V_8 and the hypothesis x,y,z real,
K_3=0 forces y=z=0; then V_6=-x(x-i)^2/256 forces x=0, leaving
V_8=1/1024. That implication is correct. The generating ansatz needed to
verify those coefficient formulas, and the Phi_N/Gram/conductor definitions,
are absent from these summaries, so those additional claims remain unchecked.

## 2. Mathematical results retained and extended

**Correct Heisenberg reference.** `cue_reference.md` derives exact all-order
CUE cumulants from a finite determinant and counts intersecting Fourier
intervals. It supplies explicit nonzero reference terms rather than a
Gaussian zero target. This repairs the quantity that must be compared to
the deterministic map; it does not bound that discrepancy.

**A stronger cubic check.** `cubic_variance.md` derives an exact variance
formula for the smooth cubic test used in the experiment. A sixth-order
cumulant simplifies to 3N-2min(a+b,c+d) on an explicit frequency band.
The simplification has a 48-chamber rational certificate with a proof of
coverage. Independently of this simplification, cumulant size bounds prove
variance O(1/N). Hence the nonzero cubic CUE limit holds in L2, not merely
in expectation. This eliminates the possible escape that the mean came
only from rare large fluctuations.

**Resonance arithmetic and the genuine obligation.**
`resonant_normalization.md` proves the all-dimension period lower bound,
the stronger O(1/log X) reciprocal Cesaro bound, and the sharp normalization
control example. It then expresses resonant suppression as a Fejer return
energy for the spectrum of U^rho at scale L of order N/rho. A sufficient
condition is interval discrepancy o(rho/N). That condition is not proved
for the prescribed kicked map; sparsity does not replace it.

**Candidate-symbol audit.** `symbol_and_symmetry.md` contains the exact
cubic/quartic projections, the finite-N Weyl correction, the reconstructed
classical estimates, the full affine symmetry classification of the
symbol, and the limits of that classification. The symbol has useful
verified properties and is not ruled out from BGS by the supplied reports.
The unresolved Phi_N/typical-fibre/conductor expressions are not relabeled
as theorems without their definitions and proofs.

## 3. Finite experiment beyond the report audit

The new f_star was tested as an auxiliary candidate at fixed couplings
0.0001 and 0.0004, both below the verified hyperbolicity bound
0.0005354412479.... This is not a numerical experiment at the original
frozen coupling 10^-80, and the original target has not been changed.

The implemented convention is physical e(aq+bp)->W(b,a), hbar_N=1/(2pi N),
and U=exp(-2pi i kappa N Op(f_star)) M_plus. The positive Gauss kernel
has the classical S orientation; three Weyl covariance identities were
checked numerically at N=41 before using the dynamics. Hermiticity and
unit-circle residuals are recorded, the latter below 3e-14 in these runs.

For odd Pell indices K=5,7,9, take L=floor(N/K) and evaluate
E_L=sum_{0<|l|<L}(1-|l|/L)|Tr(U^(Kl))/N|^2. Its exact CUE_U expectation
is K(L^2-1)/(3N^2), because Kl<N in this sum.

| N | Unperturbed cat E_L | kappa=0.0001 | kappa=0.0004 | CUE mean |
|---|---:|---:|---:|---:|
| 41 | 7 | 6.66898 | 3.97691 | 0.062463 |
| 239 | 33 | 2.75965 | 0.15737 | 0.047181 |
| 1393 | 153 | 0.04413 | 0.04017 | 0.036664 |

This shows actual finite dephasing of the arithmetic returns. Three
dimensions do not prove an asymptotic decay rate or universality.
Only the resonant portion of the Heisenberg window is measured here.

The same eigenvalues also test the corrected cubic target. At N=1393,
the narrow-window CUE complex RMS fluctuation is 0.46543. The observed
distances from the CUE mean are 1.591 and 0.666 times that RMS at the two
couplings. These are calibrated descriptive numbers, not p-values and not
evidence sufficient to identify the deterministic limiting law.

The analytic reference and the finite complex diagnostic are displayed in
`cue_reference.png` / `cue_reference.svg`. The circle is explicitly an RMS
distance, not a confidence region. Computed eigenangles are retained in
`monodromy_eigenangles.npz` so further observables do not require repeating
the matrix diagonalizations.

## 4. Verification and dependencies

Executed commands, from the repository root:

```sh
PYTHONPATH=../dependencies/python OPENBLAS_NUM_THREADS=1 python build/report-audit-20260919/verify.py
OPENBLAS_NUM_THREADS=1 python build/report-audit-20260919/monodromy_experiment.py
PYTHONPATH=../dependencies/python OPENBLAS_NUM_THREADS=1 python build/report-audit-20260919/cubic_variance.py
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=../dependencies/python python build/report-audit-20260919/independent_variance_review.py
OPENBLAS_NUM_THREADS=1 python build/report-audit-20260919/folded_spectrum_control.py
OPENBLAS_NUM_THREADS=1 python build/report-audit-20260919/plot_reference.py
```

The supplemental dependency path is specific to this workspace. Exact
code uses Python rational arithmetic and SymPy; the finite matrices use
NumPy/SciPy. Outputs distinguish exact certificates from floating-point
diagnostics. The Wolfram source and observed output are retained in
`exact_symbol_check.wl`.

The reference checks comprise 364 exhaustive positive cubic cases via
independent CUE-density integration, 45 general moment cases through
order six, 48 symbolic chambers, an independent sixth-moment density
integral, a weighted two-mode rational comparison, 150 odd-dimensional
period checks, exact Pell identities through K=39, six finite quantum
quartic comparisons, and six nonlinear spectral calculations.

The finite-rank determinantal generating-function framework was checked
against Soshnikov, *Determinantal Random Point Fields*, Theorem 2,
[equation (1.28)](https://arxiv.org/pdf/math/0002099). The explicit CUE
formulas here are derived from the finite density, not inferred from a
paper's abstract. The classical topological-conjugacy input was checked
in Newhouse (1970), [Corollary (1.3), page 762](https://users.math.msu.edu/users/newhous7/Papers/PDF/Codimension-1-Anosov.pdf),
including the codimension-one and fundamental-group hypotheses.
The summaries supply no accessible source for their
reduced obstruction. No literature-based novelty conclusion was made.

The maintained trace-to-local-statistics bridge already compares with
the actual CUE moments and does not require the incorrect zero target.
A targeted search found that the repository's Gaussian return statements
concern a different logarithmic/weak-kick regime. This audit does not
invalidate them by conflating their scaling with Heisenberg times.

## 5. Further attempt: can the existing local bounds force return suppression?

This route was executed after correcting the report's normalization.
`folded_spectrum_control.md` constructs explicit simple spectra with
uniformly bounded local correlations of every fixed order, macroscopic
equidistribution, and exponentially small traces below a logarithmic
resonant stride. Nevertheless their Heisenberg-window resonant energy
tends to 1/sqrt(1-alpha^2)-1>0. The construction can use the actual cat
periods along Pell dimensions, but it is an abstract spectral control,
not a quantization of the fixed smooth map.

The proof uses an exact Bessel expansion, a uniform contour bound for
grid aliases, and Parseval. Finite checks through N=47321 approach
0.154700538... for alpha=1/2. This refutes the proposed repair using
only local spectral bounds, global equidistribution and short-time traces.
The missing input must depend on further structure of the propagator.

## 6. Status of the original task

The fixed deterministic map still needs a coherent estimate of its
CUE-subtracted Heisenberg-window trace products. Pair correlation needs
both resonant and nonresonant control. The higher orders need the actual
CUE reference terms and their proper zero-sum strata. None of those
estimates has been proved here at fixed nonzero classical coupling.

Executed routes and their first remaining failures:

1. Low-order redesign: the finite algebra is verified, but no defined
   necessary spectral obstruction links it to failure or proof of BGS.
2. Resonant sparsity: arithmetic is stronger than claimed; the amplitude
   estimate is missing, and the proposed unitarity shortcut is false.
3. Higher-order cancellation: the zero target is wrong; its CUE correction
   and finite fluctuation scale are now explicit, but dynamical comparison
   with that reference remains open.
4. Numerical candidate test: actual return dephasing is observed within
   the available dimensions; finite evidence supplies no uniform estimate.
5. Bootstrap from bounded local correlations and short traces: refuted
   for those inputs by the explicit folded-spectrum control. This does
   not exclude a proof using the full fixed-symbol dynamics.

The next substantive proof obligation is nonperturbative control of the
actual monodromy return energy or the nonresonant trace discrepancy, with
quantum phase kappa/hbar_N growing with N. Short-time Egorov, a finite
Taylor coefficient, and a classical symmetry audit do not close it.

All work in this continuation is an unpublished research checkpoint.
Tracked files were not changed; no commit or push was made, respecting
the user's condition to publish after the main barrier is solved.
