# The new charge gap survives microscopic spectral rounding

Maintained corollary prepared 7 October 2026. Separately accepted by independent internal review, under the new one-step charge gap and the existing microscopic spectral-rounding theorem. This credits that construction and changes the operator. It is an obstruction to abstract full-pair closure, not an actual-map or offcharge-only counterexample.

Suppose the actual U_N satisfies the new bound sup_(c!=0)||B_c(U_N)||<=rho<1 eventually. The accepted rounding theorem supplies altered simple-spectrum W_N with epsilon_N=||W_N-U_N||op=O(N^-1), preserving the stated low-trace/coarse controls but violating a fixed stable-band CUE pair test by a definite amount.

For ordinary Hilbert--Schmidt induced norms,

    ||Ad(W_N)-Ad(U_N)|| <=2epsilon_N.

This follows directly from

    W X W*-U X U*=(W-U)XW*+UX(W*-U*).

Compressing by the same fixed charge projection and inclusion gives, uniformly in every modular c,

    ||B_c(W_N)-B_c(U_N)|| <=2epsilon_N.

Therefore for every fixed rho' in (rho,1), all nonzero W_N charge blocks obey ||B_c(W_N)||<=rho' eventually. The charge-zero centered block also retains a fixed gap by the accepted rounding theorem. Consequently W_N satisfies the same global switch-damped off-charge conclusion, all-checksum low-switch conclusion, and arbitrary occupation-phase norm bounds derived in global_switch_transfer.md, with changed fixed constants. It also retains the inherited entrywise flatness, P gap, Q reverse-kernel decay and prescribed low-trace window stated in the rounding source.

Nevertheless the accepted rounding construction has a fixed smooth nonnegative w supported inside (0,1/2) for which

    liminf N^-2 sum_m w(m/N)(|Tr W_N^m|^2-m)>1/2.

Thus those combined abstract controls, including the NEW uniform one-step charge gap and its entire globally switch-damped family, cannot imply the full undamped CUE pair law. An extra actual-model input beyond these norm properties is necessary at the boundary.

This does not prove that W_N's off-charge component alone violates its target: the full defect also has a balanced component, and this note does not split the lower bound between them. The scalar degree-m polynomial control in the switch-transfer note separately refutes the bare interior-to-boundary analytic inference. The two obstructions have different scopes and must not be conflated.

The construction changes U_N by spectral functional calculus and does not preserve the exact kick quantization. Hence it is not an actual-model counterexample and cannot refute BGS for the literal tau=10^-80 sequence. It is credited entirely to the existing microscopic-rounding method, with only the charge-compression continuity corollary added here.

## Review and reproduction record

The exact original candidate, independent reviews, source pins and bounded computational controls are preserved by [the promotion record](../../record/charge_strengthening_promotion.md). No finite computation proves the analytic limit. This prepared overlay is not an integration or publication claim.
