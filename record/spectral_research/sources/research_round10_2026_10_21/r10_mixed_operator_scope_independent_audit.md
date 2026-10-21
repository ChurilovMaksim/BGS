> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round10_2026_10_21/r10_mixed_operator_scope_independent_audit.md`. Embedded SHA256: `a11849cdda56873e59d9391f9efd5d133047bd6047014382ee5f0144ec875a04`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/research_record.md).

# Independent audit of the normalized-operator route

21 October 2026. Reviewer: branch `/root/r10_mixed`.

## Audited artifact and verdict

The final audited file is
`research_round10_2026_10_21/root_operator_route_scope.md`, SHA-256
`579b1f4721dfaef4e6da1d914d90cab934b2fc625ebe37ef93b87839b57722a2`.
Its full preceding version was read, and the final revision and hash
were independently checked. **Pass for the mathematical scale claims,
the checked primary-source scope, and the explicit unresolved status.**
This verdict does not certify an estimate of the original spectral
sum; the artifact explicitly says it has obtained none.

## 1. Finite-dimensional scales

The identity `Tr_HS(Ad(U)^m)=|Tr(U^m)|^2` is correct in arbitrary
matrix units. The matrix-space dimension is `N^2`, so its trace-norm
counting inequality (1.2) is correct without a missing factor of `N`.
Summing `O(N)` times makes uniform `o(N^-1)` power errors sufficient
by that inequality, while uniform `O(N^-1)` errors are insufficient
in general. The companion CUE example gives a positive limiting
weighted trace discrepancy even with this last operator error.

The distinction from one-step unitary spectral matching is also
correct. For two unitaries with `delta_N=||V_N-U_N||=o(N^-1)`,
write `V_N U_N^*=exp(iH_N)` with the principal self-adjoint
logarithm. Its norm is bounded by `2 arcsin(delta_N/2)=O(delta_N)`.
Along `exp(itH_N)U_N`, absolutely continuous eigenangle branches
have speed at most `||H_N||/(2pi)`, including crossings by
diagonalizing the compressed generator. Thus their maximum unfolded
displacement is `O(N delta_N)=o(1)`. This is a statement about
matching the two actual unitary spectra. It is not an estimate of
the unknown CUE discrepancy of either one.

The exact adjoint has at least `N` fixed matrix directions from an
orthonormal eigenbasis and is itself Hilbert--Schmidt unitary.
Removing scalar matrices leaves at least `N-1` fixed directions.
The file does not confuse classical mixing with their disappearance.

The normalization statements were checked against the actual Round 9
source, SHA-256
`afeaa52cea23836c5b4fa58d1040daa6df792d0b9adea83f8eb1de8690211921`.
Its equations (5.4)--(5.5) give per-edge `o(N^-1)` and orbitwise
`o(1)` relative errors for every fixed time band. Equation (8.3)
there retains the sum of absolute orbit amplitudes; no signed-sum
bound was supplied. The current scope note preserves precisely
that distinction.

For the central-limit calculation, setting `Y_m=S_m/sqrt(m)`
rewrites `exp(iN tau S_m)` as
`exp(i[N tau sqrt(m)]Y_m)`. At `m` comparable to `N`, the
frequency is comparable to the fixed positive constant `tau`
times `N^(3/2)`. Fixed-argument weak convergence of characteristic
functions does not control this growing argument. The note makes
no stronger conclusion about the actual characteristic function.

## 2. Primary-source assertions independently checked

The following original PDFs and actual theorem statements were
retrieved, not merely bibliographic summaries.

**Faure--Tsujii**, [arXiv:1206.0282, current v2 PDF](https://arxiv.org/pdf/1206.0282):
Theorem 1.69 gives the stated `O(h^delta)` comparison with a
continuous potential correction. Theorem 1.35, equation (1.52),
has constants and dimension thresholds indexed by a fixed positive
neighborhood size. Theorem 1.38 has remainder
`C N^d(r_1^+ + epsilon)^n`. Proposition 1.42 is spectral
uniqueness under the specified trace information. I requested the
qualification that exponential decrease requires
`r_1^+ + epsilon < 1`; the coordinator inserted it, including the
reference-potential example. The final text contains this correction.

**Charles**, [arXiv:math/0602168](https://arxiv.org/pdf/math/0602168):
Theorems 1.1--1.2 use smooth compatible integrable polarizations and
give the stated `O(k^-1)` functoriality and parallel-transport
precision. Theorem 5.3 compares the specified smooth Hamiltonian
propagator modulo `O(h)`. Theorem 3.3 computes an intertwining
subprincipal term. None of these statements identifies the present
nonsmooth invariant polarization with its required precision.

**Charles**, [arXiv:1410.2066](https://arxiv.org/pdf/1410.2066):
Theorem 1.1, Proposition 1.2, and the symbol-map description give
the stated dependence on a connection and the kernel
`k^-2 T_sc` when principal and subprincipal symbols agree. The
Toeplitz class and the smooth symbol expansion are genuine
hypotheses. The scope note does not assume they hold for an
unconstructed comparison operator.

**Kieler--Fritzsch--Bäcker**, [arXiv:2605.27052](https://arxiv.org/pdf/2605.27052):
The original form-factor definition includes an average. Its page 3
derivation fixes the interaction scaling parameter and uses the
central-limit regime; page 4 states the plateau extrapolation
conditionally on the proposed resummation and as a conjecture.
The scope note accurately declines to use it as a uniform
Heisenberg-time theorem for the present fixed map.

These checks concern applicability of the displayed assertions,
not independent reconstruction of the proofs of all those papers.
The note uses none of them as an unverified original-family
universality premise.

## 3. Explicit boundaries retained

The corrected artifact keeps all odd dimensions and the fixed
`tau=10^-80`. It does not infer microscopic control from a
fixed-neighborhood resolvent statement, and it does not identify
an `O(h^delta)` bound with `o(h)` for an unspecified positive
exponent. It also leaves the Hölder multiplier and varying-potential
comparison unproved. Its last displayed original weighted pair
estimate is stated as unresolved.

The new orderwise repulsion theorem mentioned there has a separate
primary reviewer. This audit did not substitute a review of that
theorem or infer it merely from its name.

## 4. Frozen branch results and self-check

The companion proof files are frozen at these hashes:

| File | SHA-256 |
|---|---|
| `r10_mixed_isospectral_twirl_obstruction.md` | `673a8fbbe93cb26db469b7c7dd13b5960352e3ec2cdbf9e248aa4d7f2be1d9b9` |
| `r10_mixed_shrinking_isospectral_noise.md` | `5c9265843ce9ad7037ca35b0b601bfed4cca9bd87a44d15405a30f68d22683fb` |

The latter was self-checked for the modular covariance sign,
invertibility of `S-I` in every odd dimension, the no-wrap
threshold, the integer middle-vector argument, and the distinction
between spectral radius and resolvent norm. In particular its
all-time trace estimate applies to powers after independent
resampling, whereas (7.3a)--(7.3c) retain the exact same-sample
telescoping phase and the original bare-cat scalar returns. These
claims are auxiliary and are not applied to the fixed-kick `U_N`.

No file outside the assigned `r10_mixed_*` branch scope was edited.
