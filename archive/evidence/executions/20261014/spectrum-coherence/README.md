# Spectral and coherence obstructions: exact scope

This packet separates BGS-TRACE-081's abstract unitary family from
BGS-TRACE-082's universal Hilbert--Schmidt block identity and norm plateau.
Both leave the unchanged fixed-map TRACE-005 and BGS limit open.

The [frozen spectrum candidate](candidate_reviewed.md) has Git blob
666e8a9ab551e945936198638ebb4d4286a67454 and SHA256
08de07484be6e6a8fb2612ac9abbbb12ecdeb6660c23b3cb57ba158de62c1030.
It was preserved while the executor was disconnected in the unreferenced
proposal commit 22d6fc94b8060e1a65420b5e007ba3ccbbef4d16; that snapshot
did not move main. The later maintained sources are the status owners.

The [independent spectrum reconstruction](independent_spectrum_review.md)
proves exactly O1--O5 and the all-invertible generic-column phase lemma.
Its [independent integer/Fraction source](independent_spectrum_controls.py)
and [actual output](independent_spectrum_controls.json) tested 157576
ordered Gauss pairs and finite algebra. These were reviewer executions,
not root executions, and do not prove genericity or asymptotic laws.

The [original memory candidate](memory_candidate_reviewed.md) is preserved
separately. Its original prose saying the two evolution operators are
different requires the correction that they need not agree; they can
agree for diagonal or monomial unitaries. The maintained source includes
this correction. The audited formulas and their universal quantifiers
are unchanged.

[Archived JavaScript source](archived_js_source.mjs) and
[actual result](archived_js_result.json) preserve the pre-reconnection
integer controls: 158 odd-prime substitutions, ten primes, 16 tensor
multiplicity cases and six powers of the four-dimensional core. The
function was executed in the functions V8 environment; its Node stdout
wrapper was not executed then. The finite formulas were checked, not
the generic phase lemma, the probability limits or BGS.

Maintained reproduction:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 timeout 90 \
python3 computations/verification/spectrum_coherence_controls.py
g++ -std=c++20 -O2 -Wall -Wextra -pedantic \
  computations/cpp/coherence_memory_verifier.cpp -o /tmp/bgs-coherence-control
/tmp/bgs-coherence-control
```

The Python arithmetic is exact rational/Gaussian-rational algebra. It
checks the return-memory recurrence and resolvent at z=1/5, finite
observability budgets, Gauss identities and discriminant examples.
The C++ arithmetic is bounded Gaussian integers. Its N=2 endpoint has
singular values 1,0 and square zero, so the norm plateau must not be
confused with a spectral-radius assertion.

The active Lean source CoherenceBudget proves only positivity of
(N-1)(N-r), assuming N>=2 and r<N. Its compilation and printed axioms
are separate execution evidence. No full Hilbert--Schmidt, generic
discriminant, limiting point-process or BGS formalization is claimed.
Bibliographic context is a prior-mechanism comparison, not an external
theorem dependency or an established world-priority claim.

## Final review and actual execution

The final [memory reconstruction](independent_memory_review.md) binds the
original wording correction separately from the validated formulas;
its [source](independent_memory_controls.py) and
[output](independent_memory_controls.json) use exact Gaussian rationals.
The [maintained-transfer report](maintained_transfer_review.md) accepts
the final mathematical sources with SHA256
d78e0a8b27e77c3853caab03e05357a0f878e27ed7fe1d8c57d066008ee94c91
and 5c311f6f09714abfe3da9e4e50befa33a5acda3449f19bdb30e331183bb561bc.
These sources preserve the reviewed proof segments exactly. The final
spectrum report has SHA256
1b0fca70d10031c01f78117c14840b2a48b305c87de46d0b5ee52b3fd6ed804c;
an unpromoted earlier formatting-only report revision was replaced before
the packet was sealed.

The root [bounded Python execution](bounded/manifest.json) completed
with exit zero, unchanged six declared inputs and a passing manifest
validation. The separate [C++ receipt](root_cpp_receipt.json) and
[actual output](root_cpp_result.json) bind source, compiler command and
binary. The [focused workspace receipt](focused_workspace.json) gives
5/5 selected Python/C++ checks, including metadata, structure and
scientific-registry audits, with unchanged sources during execution.
[Maintenance](maintenance_full.log) records 236 passing tests.

The accepted [manuscript build](manuscript_build_manifest.json) has
301 pages, three successful LaTeX passes, immutable TeX inputs and
no forbidden warnings. Its independently parsed and visually checked
PDF has SHA256
8ed16a45ac08494bf0c4e9c7635f11d4180f37769586ebe6adcde7dcfac5a577.
[Visual/integrity scope](manuscript_visual_review.json) records which
pages were actually inspected and the rejected earlier artifact copies.
Those rejected copies were not delivered as successful outputs.

[Preceding CI](preceding_ci_summary.json) is specifically main
8356101640b3c98325ef77991a370a10d7014ff8, with all seven jobs successful,
227 executable checks including 25 C++ checks, and 236 maintenance tests.
It is not a certificate of the later source tree or its new Lean kernel.
The two new claims have no external theorem leaves, so the reviewed
46-source bibliographic cache and its dependency sets are unchanged;
the current metadata check actually passed all 416 negative controls.
The sealed source manifest records exact evidence/source bindings.
