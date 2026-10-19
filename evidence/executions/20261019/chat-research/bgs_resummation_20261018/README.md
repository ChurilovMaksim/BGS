# BGS research continuation, 18–19 October 2026

This is a standalone research packet outside the paused BGS repository. It contains author proofs and self-review, not a solution of the BGS conjecture or an independently reviewed publication.

Start with [the Russian result report](BGS_resummation_result_ru.md), then the four proof notes:

1. `incidence_resummation_ru.md`: incidence rank bound, maximal-edge classification and exact sector δ=0.
2. `neutral_peeling_ru.md`: primitive order ≤2δ, size ≤16δ, and exact reconstruction at every fixed δ.
3. `first_defect_resummation_ru.md`: the exact sector δ=1 from two finite primitive polynomials.
4. `companion_resummation_ru.md`: a 5×5 companion matrix and an exact root certificate extend both sector limits to 0<τ<1.

`self_review_ru.md` records proof obligations, arithmetic and coverage limits. `route_outcomes_ru.md` explicitly corrects the scope of the fixed-port rotation test. `literature_check_ru.md` distinguishes prior finite-scheme ideas from the actual weights studied here.

The base packet is `BGS_signed_cancellations_20261018.zip`, SHA-256 `d5b0c6235688704e7be9d9de96dbb8cffc52f69f4eeb17496c8a97d2897415bc`. Needed proof sources, tables and the reused enumerator are copied in `dependencies/`. This packet does not pretend to contain the complete original repository or all original execution evidence; the base packet supplies that ancestry.

Each `*_run` directory contains the actual recorded manifest, stdout/stderr, and result where produced. `maxedge_run` is the retained failed SymPy version, superseded by `maxedge_run_v2`. Compiled executables are omitted from the distributed ZIP and are rebuilt by the wrappers. The C++ implementations require a C++20 compiler; the new exact algebra scripts require only Python's standard library. The scattering probe additionally requires the recorded NumPy/SciPy versions. Set `PYTHONDONTWRITEBYTECODE=1` to avoid import caches.

To reproduce a run, use its manifest's argv from this packet root with a **fresh** result directory. For C++ wrappers, the output argument's parent directory must already exist. Do not overwrite recorded evidence in place. For example:

```bash
mkdir reproduce_cluster
PYTHONDONTWRITEBYTECODE=1 python3 run_cluster_check.py reproduce_cluster/result.json
mkdir reproduce_companion
PYTHONDONTWRITEBYTECODE=1 python3 companion_certificate.py reproduce_companion/result.json
```

`inventory.json` hashes all distributed files except itself. `checkpoint.json` pins final proof revisions and records the exact open goal. `provenance/` records dependency hashes, evidence validation, and the unchanged repository snapshot. `history/` retains the superseded longer proof of the first-defect classification; the current proof uses the stronger cluster theorem.
