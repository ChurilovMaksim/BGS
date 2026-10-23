# Dense off-charge attack: substantive checkpoint

7 October 2026. All work is outside the canonical BGS repository. The literal odd-dimensional U_N and tau=10^-80 are unchanged. No publication, commit, push or canonical edit was made.

## Result

The original full undamped off-charge goal was NOT reached. The pass produced a new actual nonlinear-phase lemma, a stronger undamped partial removal, and a global signed transfer reduction that sums every switch history before estimating. It ends at a precise marked-switch boundary integral rather than repeating the old residual definition.

1. onestep_charge_gap.md proves uniform ONE-STEP contraction sup_(c!=0)||B_c||<1. The positive leading-branch envelope is exactly bistochastic by norm convergence and quantum unitarity. Compact norm attainment and equality in Jensen would align two branch phases; the accepted actual Fourier witness forbids this. Egorov and classical mixing are not used. The fresh independent reviewer reported that this pinned proof passes; the durable formal review is being completed separately under bgs_onestep_charge_review. Treat the final signed review, once available, as the acceptance authority.
2. global_switch_transfer.md T4 then uses arbitrary occupation-phase row twists to control every actual low-switch OFF-CHARGE fiber, including checksum zero and translations with order dividing m. This consequence has not yet received its separate fresh review. checksum_free_residual.md records the exact disjoint projector synthesis: the off-charge residual becomes high Hamming AND high switch count, with no checksum exception. The balanced complement remains open.
3. global_switch_transfer.md T2--T3 gives an N^2-dimensional transfer whose trace exactly sums all N^m difference words with switch factor z^s and Hamming marker q, with the occupation projector retained. Uniform one-step contraction proves the full high-Hamming off-charge aggregate negligible for 1-z=A log N/N with sufficiently large fixed A, including dense switches and checksum zero.
4. The remaining actual undamped estimate is exactly the signed integral of the marked-switch derivative over z in [1-A log N/N,1]. Its matrix formula is m Tr[M^(m-1) Q_q V_theta (T-D)], followed by the exact occupation/Hamming masks. No estimate of that integral is claimed.
5. rounding_gap_obstruction.md extends the accepted microscopic-rounding obstruction by one compression inequality: an O(N^-1) spectral rounding preserves the new uniform charge gap and all its global regularized consequences, while violating the full CUE pair target. This alters the model and does not prove that the off-charge part alone fails. The scalar degree-m polynomial example separately refutes an unqualified interior-to-boundary inference.

## Pins

- onestep_charge_gap.md: d51de5e8287495514fc431ed9b05e44f3407e46ed923a6e1664df2cca667e97a
- global_switch_transfer.md: 4a333b1847eb466ef66326e26562ee63770f6e09ed7f47d7b517e5fbf5e6d0be
- checksum_free_residual.md: ccf686f7504fec5c0de4152f6e20df4cff7d004ba3b0cf7c08c37eb5b9805e9f
- rounding_gap_obstruction.md: 9194eac0959c18b7c865eaeef1e00925c32deac1fa0ab680c43af8164b5d7f57

source_manifest.json freezes 19 prerequisite/authority sources by SHA256. The observed canonical HEAD at the start of this packet is d37c92e563d10d25bb1d6ab85bedffc1f160f773; the repository was concurrently changing, so the copied input hashes, not a claim of a globally frozen checkout, define this proof's dependencies.

## Exact finite evidence

Run from this directory:

    python3 run_controls.py

The checker uses exact Gaussian-integer numerators and common positive denominators, with no floating arithmetic or third-party package. Coverage is 25,019 literal ordered pairs: N=2,m=1..5; N=3,m=1..4; N=5,m=1..3. It independently constructs Ad(U) by U E U*, verifies full superoperator unitarity and the block formula, both zero-run identity annihilations, full occupation/Hamming/switch coefficient dictionaries, exact torus constant-coefficient selection, checksum-zero off-charge witnesses, arbitrary-row-phase identity reduction, the undamped |Tr U^m|^2 dictionary and the noncommuting marked derivative.

The tau=0 controls use prime N=3,5,7,11 and every nonzero charge to verify the literal rank-one modular kernel and vanishing square character, retaining its one-step norm-one obstruction. They are auxiliary algebra, not a floating approximation to the literal nonzero tau.

Normal and optimized Python outputs are byte-identical. An injected failure fails under -O. POSIX 512 MiB memory and 60-second CPU limits and a 70-second subprocess timeout are recorded. control_manifest.json pins commands, inputs before/after, result/log hashes and Python version. These bounded controls do not prove the analytic asymptotic.

## Scope of the remaining route

The all-switch scalar norm route cannot remove damping: an explicit degree-m boundary polynomial obeys the same interior decay while remaining order one at z=1. The generic new-gap-to-CUE criterion is ruled out by existing spectral rounding. The full Ad(U) remains unitary, so no global operator contraction is inferred from the individual blocks.

The live next implication is model-specific signed cancellation in the marked-switch boundary integral, retaining the occupation torus difference and all masks. The required interval has width O(log N/N); generic operator continuity requires a much smaller scale and cannot bridge it. A future attempt must change the estimate at this boundary, not re-prove the interior gap or replace the exact phase projector by independent random phases. The separate balanced complement and higher factorial hierarchy remain open throughout.
