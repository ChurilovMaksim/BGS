> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round9_2026_10_21/round9_research_checkpoint.md`. Embedded SHA256: `0ba3aa1de031f09e786db731b78592e646e6482d768d7adc547b00198b4246f0`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/research_record.md).

# Round 9 — active research checkpoint

Date: 21 October 2026. Original family, fixed `tau=10^-80`, every odd dimension.

## Status

Neither the original `H_diag` nor a countersequence for the original matrices has been proved. The fixed weighted pair sum recorded below is still the first unproved target. This checkpoint is not a completion claim.

The continuing master at the start of this pass has SHA-256
`b1dc28374e62fb77c59d7da04f638916e43e0ac5809c68ea02c501fb92436a20`,
6,738,835 bytes. Its byte-exact frozen copy is
`research_history_frozen/master_before_round9.md`.

## Portfolio and changes of direction

1. **Physical/Weyl coherence.** Rereading complete raw sources showed that the all-time cyclic classes, short encounter sums, and occupation resummations considered initially were already covered. They are not new results of this pass.
2. **Smooth microscopic stability.** The complete Round 3 source already proves uniform quantum ergodicity along the path and full all-order `H_diag` transfer. Repeating that theorem was abandoned immediately on finding the source.
3. **New cocycle construction under investigation.** Approximate the continuous first graph phase by real trigonometric polynomials; choose their degrees sufficiently slowly with dimension. Prove actual unitary realization, fixed-strip exact amplitude estimates, uniform quantum ergodicity for the varying generators, and a scalar cycle error tending to zero uniformly at times at most `B*N`. This is a construction for an equivalent quantization, not yet the missing sum cancellation.
4. **Spectral determinants.** A deleted clock has the exact full CUE determinant autocorrelation but fails a fixed pair test and a bounded local Laplace test. The full self-contained proof has received one independent audit. A primary-paper applicability audit and an attempt on mixed ratios continue.
5. **Original arithmetic.** Oldform and growing-order comb obstructions already in the history were checked before attempting new CRT/Galois comparisons. A Galois cubic-moment obstruction is being proved. It is not a counterexample to `H_diag`.

## First unresolved original estimate

Let
$$
\phi(\xi)=e^{-1/(1-\xi^2)}\mathbf1_{|\xi|<1},\qquad
I=\int\phi,\qquad
u=\mathcal F^{-1}\phi,\qquad b_*(x)=\frac{|u(x)|^2}{2I^2}.
$$
Then `b_*` is one fixed admissible test and
$$
\Delta_{2,N}(b_*)=
\frac1{N^2}\sum_{1\le m<2N}|\widehat b_*(m/N)|^2
\bigl(|\operatorname{Tr}U_N^m|^2-\min(m,N)\bigr).
$$
It remains unproved that this expression tends to zero along all odd dimensions. No estimate is imported from classical mixing, an averaged model, a finite symbolic verification, or an auxiliary unitary family.

## Deliverable policy

New notes will be independently audited at their critical step before inclusion as proved results. The final Round 9 master will contain the current findings, full proofs and audits, this checkpoint, and the frozen preceding master. Existing raw source files and frozen history are not to be rewritten to conceal changes of status.
