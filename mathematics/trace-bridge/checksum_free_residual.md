# Conditional disjoint synthesis with all low-switch off-charge fibers removed

Maintained synthesis prepared 7 October 2026. Separately accepted by independent internal review, under the fractional-Hamming theorem/synthesis and the new occupation-twisted low-switch bound. This is the exact Q_new residual decomposition; its complete signed trace remains OPEN.

Let P_H, P_bal and O_low denote the exact accepted Haar projector, centered balanced Hamming-range projector at its small positive fraction, and literal raw off-charge Hamming projector at radius floor(.49m). Define a new orthogonal matrix-unit projector L_all by the literal mask

    occupation(x)!=occupation(y),
    h(y-x)>floor(.49m),
    s(y-x)<=floor(gamma a N/(8 log N)),

where gamma=-log rho>0 comes from the new one-step gap including the zero-charge centered block. There is no checksum restriction. The mask is invariant under simultaneous cyclic rotation, includes every repeated label, and is disjoint from O_low. It is off-charge, whereas P_H and P_bal are balanced. Therefore

    Q_new=I-P_H-P_bal-O_low-L_all

is an orthogonal projector commuting with the full simultaneous cycle R. Its off-charge part is exactly the high-Hamming, high-switch literal mask

    occupation(x)!=occupation(y),
    h(y-x)>floor(.49m),
    s(y-x)>floor(gamma a N/(8 log N)).

The balanced part remains Pi-P_H-P_bal. No identification of P_bal with a raw coordinate mask is asserted.

The exact identity is

    |Tr U_N^m|^2-min(m,N)
      =Tr(R Q_new C_(U_N))
       +Tr(R P_bal C_(U_N))
       +Tr(R O_low C_(U_N))
       +Tr(R L_all C_(U_N)).

On every fixed positive Heisenberg band, the second and third terms are exponentially small by the accepted fractional-Hamming theorem. The last is exponentially small by global_switch_transfer.md T11--T12, which bounds the actual occupation-mismatched part of each low-switch fiber through a uniform exact torus projection. Thus it is not an application of the old whole-fiber bound to an arbitrary subset.

The Haar/CUE ramp min(m,N), plateau, odd-dimensional quantization, literal tau, and common-origin normalization are unchanged. The full Q_new trace is open. The unmasked balanced complement and undamped high-switch off-charge boundary still need actual signed estimates; higher factorial orders are not reduced by this pair statement.

## Review and reproduction record

The exact original candidate, independent reviews, source pins and bounded computational controls are preserved by [the promotion record](../../record/charge_strengthening_promotion.md). No finite computation proves the analytic limit. This prepared overlay is not an integration or publication claim.
