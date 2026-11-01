# Assertion-dependent verification entry policy

Maintained verification must never issue a successful certificate after Python
has removed its assertions. Every assertion-bearing Python module under
computations/ or supplement/, and its statically resolved local import
dependents, must have an identical explicit module-level guard:

    if not __debug__:
        raise RuntimeError("Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.")

The guard follows only an optional module docstring and future imports, before
ordinary imports, setup, argument parsing or output. It has no external import
or working-directory dependency. `-O`, `-OO`, `PYTHONOPTIMIZE=1` and
`PYTHONOPTIMIZE=2` are rejected, including imported assertion-dependent helpers
and `--help`. Use ordinary Python for these modules.

Explicit-check-only modules remain usable under optimization. In particular,
actual_path_theorems, isospectral_clock_control, scientific_registry_audit and
text_control_audit keep their existing optimized-mode contract. The aggregate
verify_workspace runner is also safe with an optimized parent: it launches
children without optimization flags and sets PYTHONOPTIMIZE=0.

The maintained AST scanner computes a conservative transitive local import
closure, including package initializers executed by dotted imports and parent
package imports. Ambiguous component/basename matches include every local match.
Exclusions use repository-relative paths, so a checkout below a directory named
`tests` is still fully scanned. Dynamic imports
cannot be exhaustively resolved statically; assertion-bearing modules still
reject optimization when imported dynamically. Arbitrary source rewriting or
programmatic compilation with different optimization flags is outside the
standard interpreter-invocation contract tested here.

## Frozen evidence packets (owner decision, 1 November 2026)

Author, referee and integration code copied verbatim into
`computations/verification/line*/` is frozen evidence of what was run. It is pinned by
sha256 in the packets' SHA manifests or in dated evidence receipts. Adding the guard
would change those bytes and break the manifests. Registered packet files are therefore
outside this policy, and also outside the SyntaxWarning-as-error compile step, under
three conditions:

- the file is listed in `computations/maintenance/frozen_evidence_packets.json`
  (38 packet directories, 366 files);
- its current sha256 equals the registered value;
- that value appears verbatim in the registered pin file.

`frozen_packets.py --check` validates the registry. An edited or unregistered file
stays in scope. The unpinned files in the same directories (27) and every non-packet
module carry the guard. Of those, the three maintained form-factor verifiers
(`diagonal_phase_form_factor.py`, `hyperbolic_diagonal_form_factor.py`,
`interaction_phase_form_factor.py`) received it on 1 November 2026. Their 29 October
receipts describe the recorded runs of the pre-guard bytes.
`frozen_packets.py --compile-check` replaces `python -W error::SyntaxWarning -m compileall`:
a SyntaxError still fails everywhere, frozen packets included.
`tests/test_frozen_packets.py` covers the scope and the fail-closed behaviour.

Historical record/ and evidence/ files are unchanged. The tests directory is
excluded from certificate producers: maintained unittest checks use explicit
unittest methods and the new regression suite itself passes under optimization.

Run from the repository root:

- `python computations/maintenance/assertion_policy.py`
- `python -m unittest discover -s computations/maintenance/tests -v`
- `python -O -m unittest discover -s computations/maintenance/tests -v`

Coverage includes early-guard AST validation, deletion/reordering controls,
all protected modules as direct scripts and imports in four optimized modes,
false-predicate insertion immediately after each guard in normal plus all four
optimized modes, the frozen_full_lag_gap 51451-to-51452 exact-constant mutation,
and the existing collective_diffusion_gap false-coordinate identity regression.
All-module inserted false predicates are synthetic negative controls, not
independently identified mathematical errors in those modules. Static assertion
counts are not false-PASS counts.

Earlier 161/161 or 163/163 aggregate receipts describe their recorded runs.
The standalone-entry defect does not invalidate those receipts, and neither old
nor new execution coverage is a universal proof audit or proof of BGS.
