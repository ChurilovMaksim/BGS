> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round10_2026_10_21/round10_target_checkpoint.md`. Embedded SHA256: `a35e09d5678b1f718f7deaa1c726afa5c692886010eb41f748e8f9f1624378f0`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/research_record.md).

# Round 10 target and route checkpoint

Base: the complete Round 9 master, SHA-256
`e338400f1f360b680ea74c739283b296c9c67eb4e598c2067b136f9f29773777`,
preserved byte-for-byte as `research_history_frozen/master_before_round10.md`.

The exact original family, fixed tau=10^(-80), every odd dimension,
and all-order/all-fixed-band H_diag remain the target. A successful
alternative is an explicit fixed admissible test and order, positive
epsilon, and infinite odd subsequence of the original matrices with
nonvanishing discrepancy. Auxiliary clock families do not meet it.

The first specific open test is unchanged:

$$
\phi(\xi)=e^{-1/(1-\xi^2)}\mathbf1_{|\xi|<1},\quad
b_*=|\mathcal F^{-1}\phi|^2/[2(\int\phi)^2],\quad
w=|\widehat b_*|^2,
$$
$$
N^{-2}\sum_{1\le m<2N}w(m/N)
\bigl(|\operatorname{Tr}U_N^m|^2-\min(m,N)\bigr)\longrightarrow0.
$$

## Executed portfolio, initial mathematical discriminators

1. **Exact Weyl/adjoint cancellation.** Start with the already
   complete full-weight and all-odd endpoint-fiber identities.
   Try to control the remaining coherent endpoint sum or derive a
   genuine positive decomposition after the full time weighting.
   A repeated formula or Markov replacement is not progress.
   Write scope: `r10_weyl_*`.
2. **Original-family arithmetic countersequence.** Attack composite
   sizes and the seven-component Hamiltonian without reusing the
   already excluded oldform tower. Seek a macroscopic or microscopic
   invariant which actually bounds a fixed H_diag discrepancy.
   Qualitative nonvanishing or another Galois mismatch is insufficient.
   Write scope: `r10_arithmetic_*`.
3. **Full mixed determinant functional.** Keep numerator and inverse
   denominator together, using actual center averaging only. Test a
   direct exact identity or a true contraction estimate that survives
   the deleted-clock obstruction to direct det-det inference.
   Write scope: `r10_mixed_*`.
4. **Coordinator: operator control of normalized orbit errors and
   direct quantum-return statistics.** Determine whether the actual
   analytic normalization permits a summation-safe operator estimate,
   or whether original dephased returns can access the microscopic
   form factor. Different vocabulary for the old missing signed sum
   is recorded as the same bottleneck.
   Write scope: `root_*`, shared current report and ledger, builder.

Each branch must read relevant raw proofs rather than accept historical
labels; report actual input hashes, exact proved output, missing steps,
and scope. Shared master and historical proofs are not branch write
targets. The coordinator will reconcile and independently audit any
candidate theorem before it changes the current status.

No finite numerical experiment using machine-zero tau, no parameter
average, no prime-only conclusion, and no hidden higher-moment input
may be promoted to the original target.
