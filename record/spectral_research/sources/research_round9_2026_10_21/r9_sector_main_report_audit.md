> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round9_2026_10_21/r9_sector_main_report_audit.md`. Embedded SHA256: `7d639afbc75b949b391c0df46fe570f966e134b25f337d49871ae8882bf5d613`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/arithmetic.md).

# Independent scope and quantifier audit of the Round 9 main report

21 October 2026. Auditor: /root/r9_sector_coherence.

## Reviewed draft

The complete main report, including a separate read of the initially
truncated middle, was reviewed at SHA-256

678be5fb5a90ee6794f369257c4b143da4925a8eeb9701fd3b5be650abcb994e

for research_round9_2026_10_21/round9_main_report.md.

The primary comparison was with these unchanged frozen proofs:

| Source | SHA-256 |
|---|---|
| root_diagonal_cocycle_normalization.md | afeaa52cea23836c5b4fa58d1040daa6df792d0b9adea83f8eb1de8690211921 |
| r9_sector_continuous_symbol_stability.md | 0145256f03ad92f70a5852ecb11280dc3b1bccfa54b74af8b70e459b2e6577df |
| r9_arithmetic_audit_continuous_selection.md | e2ffa265abd856e9c8dc827e66438b74e9fbef299a3d8c5c4bbb841477dd5908 |

The source statements for the arithmetic dimensional range and the
nonzero-minor determinant addendum were also read to check the
summary's quantifiers.

## Verdict on the mathematical scope

**The substantive claims in Sections 0--5 and 10--11 match the frozen
theorems.** The report correctly states that the original problem is
unsolved, retains the exact family and all odd dimensions, and does
not promote scalar normalization into a bound for the full trace sum.

In particular:

- The local Laplace comparison is unconditional.
- Full $H_{\rm diag}$ is equivalent at the two endpoints.
- The report explicitly refuses to infer unconditional second
  factorial-moment comparison or transfer of an isolated pair test
  without moment control.
- The spectral argument applies fixed-time Egorov only to a fixed
  polynomial before taking its approximation index to infinity.
- The spectral-flow factors $1/(2\pi N)$ and the scalar rotation
  $\mu/(2\pi N)$ are correct, including the treatment of degeneracies.
- The positive-quantization signs and bound in (2.15) agree with
  the actual modular-midpoint construction.
- The weighted-shift formula, central word phase, and $C_h^2$
  explanation agree with the exact analytic proof.
- One diagonal sequence works for all fixed $B$ and all odd $N$;
  it is not selected after a future test function or order $k$.
- The estimate $1.202(0.421)^m$ concerns the residual graph product
  and holds at every positive iterate above the dimension threshold.
  It does not assert a bound for the principal orbit sum.
- The first fixed test, its support $[-2,2]$, and the precise
  coefficient of the positive-frequency pair sum in (10.2) are
  correct. The remaining full target (10.3) retains all partitions
  and the full weighted sum.

## Precision edits requested before freezing the report

These edits do not change the new theorems; they prevent the shorter
report from introducing broader or ambiguous quantifiers.

1. **Arithmetic range.** The Galois row of the Section 0 table
   should explicitly include odd $N\ge75$, and its projective
   statement should retain $7\nmid N$. Before (7.6), repeat
   $N\ge75$ instead of relying only on “additionally”.
   The frozen arithmetic theorem assumes this dimensional range.

2. **Determinant approximation domain.** The perturbed deleted-clock
   statement near the end of Section 6 should state its proved
   uniform domain
   $|z|,|w|\le e^{C/N}$ for every fixed $C$, and each fixed
   differentiation order. An unqualified uniform approximation on
   all complex arguments is not what the addendum states.

3. **Exact trace phase bookkeeping.** In (5.1), keep the actual
   lattice and metaplectic scalar separately, for example
   $$
   \Omega_{m,N}(x)e^{iS_{x,m}/h_N},\qquad |\Omega_{m,N}(x)|=1.
   $$
   The scalar depends on $N$, so placing it inside an unindexed
   classical $S_{x,m}$ hides that dependence. Equivalently the
   total phase could be explicitly indexed by $N$. The full
   signed-error estimate and its missing cancellation are unchanged.

4. **Logarithm branch.** In (8.2), specify the unique holomorphic
   logarithm on $|z|<1$ that is zero at $z=0$, or its equivalent
   continuation along the kick path. Without a branch convention,
   the modulus of the logarithm is formally ambiguous. The displayed
   numerical bound itself is correct for this branch.

The current draft was not edited by this auditor. A final reviewed
version may be acknowledged below after these changes.

## Current deleted-clock version: exact provenance reconciliation

The earlier independent deleted-clock audit intentionally records
the then-current source hash

22da436148c61eea76077aa0546a709ac30c64a16bfb5550db0ae2755a23419c.

The current source was now read in full again and has SHA-256

4fd909b04e8ccc1a000930e46e6efe23b520e8d41400d8f923e3aa7911623b7f.

The precise byte change was checked without modifying either source:
the current file contains exactly one occurrence of the TeX text
$\backslash!\backslash left[$. Replacing that occurrence in memory
by $\backslash!left[$ gives exactly the earlier source SHA-256.
Thus the version change is the insertion of one missing TeX
backslash in equation (2.4), from the malformed spacing/bracket
command to the intended expectation bracket.

The current statement and all its mathematical proofs are accepted
in the same auxiliary scope. This acknowledgment preserves the old
audit's original hash and records the separately verified current
version; it does not silently retag the historical review.

## Final reviewed version: PASS

The final main report was reread at SHA-256

abd50d2f334eba5d57142e2f80eb133ed01c83a160f4e79485a07ff7ed4ff93a

including every changed passage and Sections 0--5 and 10--11.
The frozen analytic proof, continuous-symbol proof, and their
independent audits still have the hashes recorded above.

All four requested precision edits have been made:

- Both arithmetic summaries explicitly impose odd $N\ge75$,
  and the projective assertion also imposes $7\nmid N$.
- The perturbed determinant comparison states its domain
  $|z|,|w|\le e^{C/N}$ for each fixed $C\ge0$ and each fixed
  differentiation order. Its surviving limits are distinguished
  from the unperturbed exact rational identities.
- Equations (5.1)--(5.2) now retain the separate unit-modulus
  factor $\Omega_{m,N}(x)$ for lattice and metaplectic phases.
- The logarithm in (8.2) is explicitly the holomorphic branch
  vanishing at $z=0$.

The final read also checked the added defining equations
$p=-F_q$, $P=F_Q$, $\Psi(q,p)=(Q,P)$, the restrictions
$0<r<1$ and fixed $s>0$ in the inverse-determinant comparison,
and the possible Galois sign on the positive normalization
root. These agree with the source statements.

One further notation issue found during this last read has
been corrected: equation (10.3) now uses an explicitly defined
Haar matrix $C_N$, separately from the deterministic normalized
endpoint $V_N$ of Section 2.

**Verdict: PASS for accuracy of the consolidated report and its
stated mathematical scope. No necessary correction remains in
this reviewed version.** This verdict concerns faithful reporting
of the proved auxiliary results. It neither proves $H_{\rm diag}$
for the original family nor certifies the missing coherent trace
cancellation. The unconditional Laplace comparison, full
$H_{\rm diag}$ equivalence, and absence of an unconditional
isolated-pair transfer remain explicitly distinguished.
