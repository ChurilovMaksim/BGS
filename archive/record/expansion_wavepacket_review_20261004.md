# Research-lead audit: auxiliary expansion and fixed-time trace closure

4 October 2026. Review grade: author proof and adversarial self-review;
no independent external referee or analytic Lean certification.

## Dispositions

| Claim | Disposition | Exact boundary |
|---|---|---|
| TRACE-013 arithmetic word obstruction | Project proof with Bourgain--Gamburd input | A different primitive irreversible cat, prime parity sectors and a factorial flat perturbation. Not an obstruction for the original frozen map. |
| Exact even-sector tensor ranks | Project character calculation, prior frame-potential method | D2=(p+7)/4; exact binomial formula for every fixed k. Full-space rank 2p+1 is a different representation. |
| Enlarged uniform two-copy gap | Project Dirichlet proof | Full p-space; translation generator mixes parity and is absent from the chosen word. Does not falsify a sector-preserving two-copy hypothesis. |
| Normalized fixed-time traces and initial noise ellipticity | Prior consequence, independently rederived | FM-007 already supplies a stronger logarithmic-time trace estimate. Not a new cancellation theorem. |
| FM-016 Egorov overlap separation | Project proof | Fixed classical maps/conjugators; analytic coincidence-set argument for normalized HS separation. No arbitrary N-dependent spectral change of basis. |
| FM-013 bounded fixed-time traces | Project proof by direct odd-N packet/frame construction | O_j(1) for each fixed j. No numerical K=20, full action-phase expansion, convergence of all initial traces or uniform Heisenberg estimate. |

## Adversarial checks and repaired scope

The stand-alone precursor is identified by SHA256
78ad96053e5fe4adf8f4a137f38b5f4d63dcb46c35cef801efcf89058db1fbc9.
Its maintained mathematical content is split into three proof modules,
with finite controls and source leaves in their appropriate layers. The
precursor is preserved; its claim that normalized fixed-time traces were
a new consequence is superseded here by the explicit FM-007 comparison.

The cat root proof checks all determinant signs and every possible exponent,
rather than bounded matrix enumeration. The reversor proof uses complete
integer parametrization and incompatible modulo-three/seven Lucas periods.
The prime progression needs only fourth-power order divisibility. Midpoint
coordinates use the invariant ab+a+b chart for that example; the frozen
symbol's half-shift is unchanged. Projective scalars are retained.

The character table includes both centers, regular split/nonsplit classes
and both signed unipotent classes. Exact k>=3 asymptotics are separated
from k=2, where the unipotents change the leading constant. The full-space
translation compression leaves precisely I and swap. The two-case
Dirichlet bound gives gamma/18; perturbation gives gamma/36. These constants
come from inequalities, not fitting the finite gaps.

The flat correction changes the selected product by at most 1/p! per
step. Algebraic labels and Hermite--Lindemann, not floating eigenvalues,
exclude exact spectral markers. Telescoping at times of order N retains
the clock and coherent trace lower bounds. Thus exact-marker exclusion
and even a full-space two-copy channel gap cannot imply the target.

For FM-013 the critical new obligations are all written explicitly:
the exact coherent frame, raw-to-midpoint sign, lattice character preserved
by S0 mod2, finite clock/shift uniqueness, packet Taylor recurrence through
L=5, residual O(h^4), sampling bound in weighted packet seminorms,
finite-dimensional Duhamel O(h^3), phase-space overlap, and fixed-time
nondegenerate periodic-point sublevel area O(r^2). Merely propagating a
Gaussian to first order would leave an O(sqrt(h)) error and would not
prove bounded traces after multiplication by N. Nor can an arbitrary
small plane L2 error be passed through an unbounded sampling map; the
proof samples the controlled residual before finite-dimensional Duhamel.

The first finite checker run rejected a test fixture with the wrong sign
in the fixed-line polynomial of S. The correct polynomial in slope x/y
is z^2-2z-2; its resultant with 19z^2+39z-9 is -6551. The fixture was
repaired; no theorem assumption was relaxed. Subsequent exact and
complex128 controls passed. Execution commands, scope and source hashes
are recorded in the dated evidence; finite success does not certify the
full analytic propagation or asymptotic expansion theorem.

## Next actual-model obligation

The frozen resonant block is still the ordered product with
M^j A M^{-j}, and the actual required mass remains
p^-2 sum_{rd_p/p in K}|Tr C_{p,d_p}^r|^2=o(1).
This investigation does not prove it. A fixed-time packet has bounded
covariance only for fixed j; allowing j~p invalidates the constants in
the overlap estimate. Counting periodic points without cancellations also
cannot reach the Heisenberg scale.

The next useful attack must estimate the coherent word's action correlations
or shifted microscopic block pair energy, retaining phases and root
allocation. An averaged channel gap, scalar exclusion and unweighted
periodic-point averages are now explicitly excluded as sufficient shortcuts.
Nonresonant signed joint traces and higher factorial tails remain separate
obligations. TRACE-005 and BGS-BGS-001 stay OPEN.
