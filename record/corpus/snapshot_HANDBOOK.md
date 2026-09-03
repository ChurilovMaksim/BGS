# HANDBOOK — BGS Programme Mathematical Reference

This handbook is the compact claim index for the workspace. It is subordinate to the current audit record `docs/review/repository_surgery_2026-09-02.md`: historical theorem labels are not automatically current proof statuses.

## 1. Audit-status convention

Use the following meanings in current work:

- `[PROVEN]`: gap-free derivation with the load-bearing assumptions explicit; where code is part of the proof support, the relevant check must rerun.
- `[NUMERICALLY-SUPPORTED]`: reproducible computation, not a proof.
- `[OPEN GAP]`: a precise missing step prevents the advertised theorem.
- `[HISTORICAL]`: a result or label recorded by earlier runs but not yet re-audited in the present repository state.

## 2. Rank-1 cat-map chain

### Re-audited in the 2026-09-02 surgery pass

- R82 twisted-Jacobi baseline: `[NUMERICALLY-SUPPORTED]`, rerun PASS at N=199 and N=3571; maximum reproduced fourth-moment deviation `2.353672812205332e-13`.
- H3 k=2 exact reduction: exact identity rerun PASS, including `|P|=(K-1)(K-2)` at the audited designs. The corresponding Lean source is present under `formal/Bgs/K2Reduction.lean`; a fresh Lean build is still pending because Lean is unavailable in the current audit runtime.
- Python source syntax: 164/164 audited Python files compile after the current Git docstring fixes.

### Historical claims retained, full current re-audit pending

The workspace contains derivations/artifacts for the symmetry foundation (Theorems A–E), the moment/shape line (F–H), the one-parameter curve (I–II), full-group arcsine formulas, GOE spacing/rigidity experiments, and later fluctuation layers. These remain important evidence, but their old `[PROVEN]` labels are not being mechanically recopied here until the corresponding dependencies and rerunnable checks have passed the post-migration audit.

## 3. M1 / Möbius-fiber claim

Historical label: `Thm 96.2 / M1: |δ| ≤ 16/K² = o(1)`.

**Current status: `[OPEN GAP]`.**

The standalone proof `paper/final/mobius_fiber_theorem.tex` does not establish the advertised asymptotic as written:

1. It calls `O(1/K²)` an `o(1)` term while simultaneously specifying the design scaling `K` fixed and `N→∞`.
2. Its own K=17 table reports `|δ|=6.9%`, exceeding the displayed `16/K²=5.5%` envelope.
3. The energy decomposition drops cross terms between distinct twist pairs without a proved orthogonality statement.
4. Fourier/Parseval normalizations are inconsistent inside the displayed bound.
5. The perfect-power exclusion for nontrivial character products requires a separate divisor/character argument.

The exact twist/key reductions and the independently rerun k=2 identity are separate statements and are not invalidated by this downgrade.

## 4. Verification layer

Fast structural gate:

```bash
python code/maintenance/repo_health.py
```

Audited reruns currently passing:

```bash
python code/verification/baseline_r82.py
python code/verification/h3_k2_exact_reduction.py
```

Known failed verification candidate:

- `code/verification/word_trace_algebra.py`: reaches the rewrite engine but raises `RuntimeError` because `('V','V')` remains unresolved. Treat as an unfinished proof engine, not a certificate.

Longer GOE/rank-2 reruns are pending after their path migrations are repaired.

## 5. Formal layer

Lean sources present:

- `formal/Bgs/K2Reduction.lean`
- `formal/Bgs/K4Variety.lean`
- `formal/Bgs/OpLocal.lean`
- `formal/Bgs/ScaleLaw.lean`
- `formal/Bgs/TorusLevelSets.lean`

The pre-Git ZIP also contained generated `formal/.lake/build/` products. They are intentionally excluded from Git and must not be restored as source. Presence of an old `.olean` in the ZIP is not a fresh proof check.

## 6. Rank-2 / Sp(4)

The repository retains exact-identity code, numerical coupled-energy measurements, and historical claims around the diagonal Sp(4) model. Their current status is `[HISTORICAL]` / re-audit pending except where a new audit explicitly promotes them. In particular, a calibrated `√N` numerical scale is not by itself an analytic Weil theorem.

## 7. General BGS

General BGS is **not proved** by this workspace. The current research programme is to isolate and prove family-specific arithmetic mechanisms, starting by repairing the rank-1 M1 gap, before promoting any general G0 mechanism.

## 8. Canonical next step

Re-derive M1 from the exact character/twist expansion with:

- a single explicit Fourier convention;
- all twist-pair cross terms retained;
- a proved orthogonality or covariance statement if one exists;
- the correct asymptotic regime stated before estimating;
- numerical falsifiers at N=53, 199, 3571 and additional designs;
- no promotion above `[NUMERICALLY-SUPPORTED]` until the analytic remainder actually tends to zero in the stated limit.
