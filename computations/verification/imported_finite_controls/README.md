# Finite controls imported from the 15 October BGS research record

Run from the repository root with the pinned requirements installed:

```bash
python3 computations/verification/imported_finite_controls/run_checks.py --output build/chat-replay
```

There are 15 tasks in `tasks.json`. Each child uses the same Python executable,
explicit `-O`-safe checks, fixed seeds where random controls are present, and
single-thread BLAS settings. A task runs in a private temporary directory;
its command, return code, source hash, JSON outputs and log are copied to the
chosen output directory. Dependencies shared by the algebra and audit tasks
are stored once. `cue_covariance/pair_probe.py` is the preserved optional
finite physical-matrix diagnostic; it is not run as an asymptotic experiment.

The bounded Toeplitz checker adds an explicit M>=N domain guard and rejects
the positive undersampled case M=1,N=3. Original source bytes and original
status claims remain preserved in the imported historical document. The
maintained Hardy checker starts from unit-modulus roots, including repeated
roots, and solves the infinite-norm Stein equation exactly.

`verify_integration.py` checks registry/DAG consistency, all current replay
hashes, source inventory and source links. On a full checkout:

```bash
python3 computations/verification/imported_finite_controls/verify_integration.py --output build/chat-integration.json
```

For a partial source snapshot it accepts `--baseline-tree FILE`, where FILE
is the complete GitHub recursive tree response at the recorded base commit.
Only path-existence checks may use that inventory; mathematical claim
sources must still be present as real local files. That mode is explicitly
reported and is not a full repository build.

These checks support finite identities and arithmetic. They prove neither
the imported asymptotic theorems nor the literal fixed-coupling BGS limit.
All proxy coupling, floating-point and external-input boundaries are retained.
