# Bounded consolidation review of FM-024

## Verdict

**Accepted without mathematical corrections.** Exact accepted SHA-256:

812c3610ef28290c3e5c6e1b702807ab8b01d93eae1c48e87cfe79efccf9c86e

File: `mathematics/actual_seven_primary_commutant.md`.

This is a bounded consolidation check, separate from the full initial actual-family audit. No unchanged degree366 computations were rerun. All five promoted polynomial/certificate JSON files were byte-identical to the already checked inputs; their identities are recorded in consolidation_data_identity.json.

## Core theorem consolidation

The actual model, path coordinates, Laurent bond identity and direct i→2 reduction agree with the accepted proof. The core conclusion remains exactly odd49|N,5∤N. Both matrices are simultaneously conjugated, internal unit conditions are preserved, and the proof does not substitute a characteristic-zero truncation for the actual reduction.

The expanded two-row argument remains correct. Dual-row projection of the last-row equations produces the left eigenvectors without discarding tails. The actual adjacent-depth bond cancels the penultimate left-frequency change, giving Q. In the V basis C1E0 has only column0; hence the stated off-column0 equations retain precisely the information needed. The B1/B2 argument equates all seven λ values, including the case where the distinguished eigenvalue initially differs.

The added self-contained polynomial dictionary V=CFT has the correct z5 exponent and K00 row. The seven-term inverse formula has the correct q² factor and denominator(q7+1)². The full factor and norm data are unchanged and remain bound to the accepted exact certificates.

The self-contained minimal-tail proof has the correct index ranges. For d≤L−7, s=d+t is a valid column for t=0,...,6; earlier coefficients vanish and the dual row isolates v_t^T C_d. For d≥7, r=L−d,...,L−1 gives left index bound strictly belowd, while the only right coefficient is Cd. The right Fourier frequency changes by2 modulo7 per depth increment, giving independence among any seven consecutive rows. These regimes cover all positive d at every allowed L≥21. N49 is separately covered by the actual-residue cyclic certificate, whose elementary proof is now stated correctly.

The rank lift uses a single nonzero(N²−1)-minor of the integral full commutator map. Its reduction is nonzero, hence the same minor is nonzero in characteristic zero. The identity supplies the matching upper rank bound. No projection-rank difference or idempotent lift is substituted.

## New literal-U corollary

**Accepted with the explicitly named inherited external input.** The project’s durable registry EXT-POPESCU-2023 pins Popescu arXiv:2306.14352v2, Theorem3.2, to linear independence over algebraic coefficients of exponentials of distinct algebraic numbers. The consolidation applies exactly this registered statement; this bounded review did not re-audit the external theorem itself.

For an algebraic Hermitian A, its distinct eigenvalues a_j are real algebraic, regardless of their multiplicities. The displayed interpolation polynomials produce algebraic spectral projectors P_j, since A is diagonalizable and denominators use distinct spectral values. In particular the construction does not require simple eigenvalues.

With algebraic-entry X and the prescribed algebraic M, each coefficient XP_jM−P_jMX is algebraic. For nonzero algebraic realt, the exponents it a_j are distinct algebraic numbers, including any zero exponent. Entrywise Lindemann–Weierstrass separation therefore gives XP_jM=P_jMX for everyj. Summing produces XM=MX. Right multiplication byM^(−1) then yields XP_j=P_jX and hence XA=AX. The main theorem forces X scalar, and its algebraic entries force that scalar algebraic. Conversely every algebraic scalar commutes. The literal t=10^(−80)N satisfies all hypotheses.

The manuscript correctly states the important boundary: this only classifies algebraic-entry commuters of U. It does not claim that the full complex commutant of U is scalar, and it does not establish spectral simplicity. Degenerate A is explicitly allowed and does not invalidate the corollary.

## Scope and work performed

Read and checked the entire consolidated proof, compared its expansions against the accepted actual-family derivation, verified exact promoted data identities, and checked the registered external-theorem mapping for the new corollary. No canonical edits or new mathematical claims beyond this consolidation were made.
