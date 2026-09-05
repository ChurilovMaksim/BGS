# Floquet continuation and integration audit

Source checkpoint: main `739cba4536ebb1829b5f2b3d8596681a3bd013c8`.
This is a research record, not a priority claim or a complete review of every
historical proof in WoW.

## Result and route

The new argument replaces an operator-gap perturbation expansion by a
centered cyclic cohomological inverse. The weighted Pell phase sum is O(1/K),
while exact four-letter lifting supplies orthogonality for a complementary
Hilbert--Schmidt commutator. Two exact Duhamel estimates give a normal form
without requiring epsilon times the generator norm to be small. Its error
is 12 epsilon^2/sqrt(K). At the recurrence time this gives a wrapped Gaussian
spectral law for the actual kicked propagator at epsilon=tau/sqrt(2K).

The Gaussian input is re-proved directly on the full odd space: quadratic
lifting, bounded-cluster counting including forced relations, all pairings,
and summed crossing phases. The proof does not assume every old sector-level
or arithmetic-moment assertion has already been verified.

## Falsifiers and corrections

The old publication job `33968799647` stopped before validation: it searched
for a nonexistent Markdown helper `_iter_markdown_targets`. No successful
publication or Lean compilation is inferred from that job. The one-time
integration now uses a literal checked patch against the checkpoint rather
than guessed function names. The applied patch is removed on publication;
subsequent runs test the committed sources without source-repair mutation.

The preceding final answer's gamma decimal was wrong. The delivered JSON
and a fresh independent evaluation agree on 5.614220692151198071627965... .
An additional pure-integer interval implementation now combines Machin's
identity, rational alternating arctangents, integer square root, outward
fixed-point arithmetic, cosine Taylor remainders and a geometric tail.
It encloses the value without a floating-point rounding assumption.

Three legacy executable tests reused a false K=7,p=29 positive inverse-row
anchor. Every real embedding there has degree zero. The inverse derivative,
shift/PSC, and Sylvester/Fitting regressions retain it as a negative control
and use K=11,p=23,tau=10 (second embedding) for the positive case. A direct
reflected trace-set intersection independently verifies the inverse gcd.
The affected mathematical note and retraction record are corrected.

The prior CDF left-limit correction, Markdown code exclusion, even-order
Cayley zero boundary, and magnetic constructor validation are now actual
source edits, not merely pending mutation instructions inside a failed job.

## Independent verification and numerical scope

Python uses diagonal h-coordinates. C++20 uses original integral T-vectors
and multiprecision integers. Both count 2K(K-1) distinct signed pair keys at
K=3,5,7,11,13,17,23,31,47,101. Dense checks at K=3,5,7 compare generator
identities, exact Fourier HS formulas, all old block spectra, actual kicked
matrices, and a separate chirp--FFT propagator implementation.

Extended FFT trace diagnostics at K=11 (N=8119=23*353) and K=13 (N=47321)
use 32 fixed-seed independent fourth-root-of-unity probes in an orthonormal
odd basis. They retain both m=1 and m=2 at tau=0.5,1,2. The reported
1/sqrt(R*d) is a rigorous RMS bound over probes, not a deterministic interval.
The second mode has visible finite-size departures from its limiting value;
no points are dropped to improve the plot.

`verify_workspace.py` executes every maintained executable Python verifier
and every compiled C++ target with source/log hashes. Lean compilation and
TeX builds are distinct mandatory workflow steps. The new Lean module proves
three general cleared-denominator cohomology identities and four finite
K=11 assertions. It does not formalize the operator or limiting theorems.

Wolfram was attempted but returned an MCP 404; no result is attributed to it.
The symbolic constant simplification was instead checked by SymPy and by the
explicit algebra in the proof. Literature comparison uses primary records;
no claim of a completed full-text priority search is made.

## Integration discipline and remaining frontier

Obsolete one-shot magnetic repair/dispatch/publication workflows are retired;
one reviewed workflow handles complete source validation and generated
publication. Concurrent branch-head movement aborts publication rather than
forcing main. Generated logs stay outside the source tree and the compact
execution manifest records exact hashes.

The resulting theorem is a recurrence-scale spectral statement. The next
barrier is not another fourth-moment decimal: it is joint trace control at
Heisenberg times with the correct symmetry reduction and a nonvanishing
classical perturbation. Those requirements remain explicit and unsatisfied.
