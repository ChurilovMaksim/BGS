
### R82.7 — CORRECTION TO A STANDING R80 CLAIM: the paper integration had not
### happened [defect found and repaired]

R80.7 records "Paper integration: new subsection 'Run 80' ... both papers
recompile clean with tectonic".  Checked this run: only the certification-table
ROWS had been inserted into `paper/exact_wd_and_subgroup_moments.tex`;
`paper/r80_section.tex` itself was never spliced in, so the shipped PDF
carried three dangling `\ref{sub:r80}` on page 18 and the LaTeX log ended with
"There were undefined references".  The R80 patch script asserts its anchor
before the table edit but the two edits were not verified afterwards.

Repaired (`paper/patch_r82b_repair_r80.py`, idempotent): the Run-80 subsection
is inserted, the Run-82 subsection (Theorem I, Corollary, the comb, the
even-mode measurement) added, `\bibitem{KR2000}`/`\bibitem{KR2003}` added for
Kurlberg-Rudnick, and three Run-82 certification rows appended.  Result:
`exact_wd_and_subgroup_moments.pdf`, 20 pages, 271.58 KiB, **zero undefined
references** (verified by grepping the kept log, not by eye).

LESSON 82-F: a "recompiles clean" claim must be backed by a grep of the LaTeX
log for undefined references and errors.  Tectonic exits 0 with dangling
references, so exit status is not evidence.

### R82.8 — Lean: the counting core of Theorem I is machine-checked
### [PARTIAL formal certificate, axioms disclosed]

A workspace-internal Lean project (`formal/`, Lean 4.33.1, lake, NO Mathlib —
so it builds from a cold cache in 25-80 s) checks the finite half of Theorem I
at the design prime `p = 199` (`formal/Bgs/TorusLevelSets.lean`, build log
`artifacts/r82/lean_build.log`):

  * `ordA_eq`         : `ord(A^T) = K = 11` mod 199 (and not less);
  * `C1a_levels_uniform` : every nonzero level set of `Q` has exactly
                        `p - 1 = 198` points (all 198 level sets checked);
  * `C1b_cone`        : the cone has `2p - 2 = 396` points;
  * `C2_orbits_uniform`  : every nonzero level set carries exactly
                        `(p-1)/K = 18` orbits of `<A^T>`;
  * `C4_free_action`  : `<A^T>` acts freely on every nonzero level set;
  * `C3_global_count` : `(p-1).18 + 396/11 = (p^2-1)/11`, i.e. 3600 = 3600.

Axiom audit (`#print axioms`, in the build log): `C3_global_count` depends on
NO axioms (kernel-checked).  `C1a`, `C2`, `C4` are closed by `native_decide`
and therefore depend on the compiler-reduction axiom
(`..._native.native_decide.ax`) — disclosed, not hidden; kernel-only `decide`
is infeasible at 198 x 39601 evaluations.  The ANALYTIC half of Theorem I (the
Weil intertwining property) is NOT formalised; the formal certificate covers
exactly the transitivity/counting content.
