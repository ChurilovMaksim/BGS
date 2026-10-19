# BGS research checkpoint — 18 October 2026

Start with progress_ru.md. The full original target remains open.
This package contains author proofs with exact bounded controls, not a
formal certificate or an independently refereed claim.

The positive results are in secular_hierarchy_ru.md and
bilinear_seed_classification_ru.md. The scoped failed closures are in
closure_audit_ru.md. All Python checks use only the standard library.

Reproduce the scientific outputs directly from this directory:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_secular.py reproduced_secular.json
PYTHONDONTWRITEBYTECODE=1 python3 verify_trace_hierarchy.py reproduced_trace.json
PYTHONDONTWRITEBYTECODE=1 python3 verify_bilinear_seeds_v2.py reproduced_seeds.json
```

The original bounded-run commands, limits, logs and input hashes are retained
in run/, trace_run/, and seed_run_v2/. The failed first seed checker and
its unchanged input are retained in seed_run/, seed_contract.json and
verify_bilinear_seeds.py. Its real-rational-only assertion was a checker
mistake; see the versioned correction and the proof's actual modulus bound.

The baseline BGS snapshot was not modified; repo_integrity.json records
the byte comparison. No commits, pushes, messages, or repository mutations
were performed. No Lean compilation or external referee review is claimed.
