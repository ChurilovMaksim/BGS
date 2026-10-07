# Separate reviews of the checksum-free synthesis and rounding addendum

These are separate internal audits, not part of the original one-step verdict.
Both input copies and their dependencies are pinned in the source manifests.
No canonical, author, publication or status file was changed.

## A. Checksum-free residual synthesis

Target: `checksum_free_residual.md`, SHA256
`ccf686f7504fec5c0de4152f6e20df4cff7d004ba3b0cf7c08c37eb5b9805e9f`.

**Primary verdict: proved as written**, under the named accepted fractional-
Hamming projector theorem and the independently reviewed new twisted low-switch
bound. The balanced radius remains the accepted small fraction satisfying both
strict entropy conditions, not 0.49. The latter radius applies only to the
raw occupation-offcharge Hamming mask.

The new L_all is a literal diagonal matrix-unit projector: occupation mismatch,
h>floor(.49m), and s<=R_N. Repeated coordinates are included. Occupation, Hamming
and cyclic-switch counts are invariant under simultaneous rotation. L_all is
orthogonal to the low-Hamming offcharge projector by its complementary Hamming
condition. Both are offcharge and hence orthogonal to the balanced P_H and
P_bal. The latter two are already mutually orthogonal by the accepted centered-
range construction. Their sum is therefore an orthogonal projection and
Q_new=I minus that sum is an orthogonal projection commuting with R.

No commutation with C_U is required. Since C_U is identity on the Haar-invariant
range, Tr(R P_H C_U)=Tr(R P_H)=min(m,N). Expanding I into the five orthogonal
summands gives exactly the displayed trace identity with the original CUE ramp
and plateau. P_bal is not identified with a coordinate mask.

The new L_all trace is the actual partial occupation-offcharge fiber sum; it is
bounded by the uniform torus argument and then the absolute fiber sum. This
allows checksum-zero fibers. The other two removed traces retain their accepted
exponential bounds under the original hypotheses. The balanced complement is
still Pi-P_H-P_bal and is not estimated by this update. The full Q_new trace,
including the undamped high-switch offcharge part, remains open.

Independent bounded masks, cycle invariance and weighted subtractions are
covered by `switch_checks.py`. The accepted genuine-range/Haar projector
identities are inherited from the pinned fractional-Hamming review and its
synthesis; this addendum does not rerun its large full-End computations.

## B. Rounding preservation of the new gap

Target: `rounding_gap_obstruction.md`, SHA256
`9194eac0959c18b7c865eaeef1e00925c32deac1fa0ab680c43af8164b5d7f57`.
The exact canonical `microscopic_rounding_control.md` was read and separately
frozen; its theorem supplies an altered simple-spectrum W_N with
||W_N-U_N||=O(N^-1), the specified low-trace window, preserved coarse controls,
and a definite stable-band total pair discrepancy.

**Primary verdict: proved as written**, under that accepted rounding theorem
and the newly accepted one-step gap. For every X, ordinary Hilbert--Schmidt
submultiplicativity gives

    ||W X W*-U X U*||HS <=2||W-U||op ||X||HS.

Compression to the same fixed charge space and inclusion each have norm one.
Hence the bound 2||W-U|| applies to every B_c difference uniformly in c and N.
Every fixed rho' between rho and one is therefore an eventual charge bound for
W. The centered zero-charge block is stable by the same compression argument
and by the accepted stochastic-gap continuity theorem. The global pinched
traceless gap survives with changed constants.

All occupation-twisted and switch-damped conclusions in the companion require
only this gap, exact unitarity and the charge decomposition. They consequently
transfer to W. The accepted entrywise flatness, P gap, reverse-kernel decay and
specified unnormalized low-trace preservation also transfer as stated in the
rounding source. No new parametrix or exact kick quantization for W is asserted.

The rounding theorem supplies a fixed nonnegative smooth weight inside (0,1/2)
with liminf of the complete normalized pair discrepancy strictly above 1/2.
It therefore refutes an implication from the combined abstract controls to the
complete undamped CUE pair law. It does not locate that discrepancy in the
offcharge summand: the balanced complement remains available, and the addendum
correctly declines to make an offcharge-only counterexample claim.

The construction changes the spectrum/operator by functional calculus and
need not preserve actual quantization. It is not a counterexample to the
literal fixed map or BGS. The separate scalar-polynomial endpoint obstruction
has the narrower analytic scope stated in the companion; the two are not
conflated. No new mathematical gap was found in either addendum.
