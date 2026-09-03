# Lean formalization

This is the active Lean 4 finite-certificate layer.

Build from the repository root with

```bash
cd formalization
lake build
```

`Bgs.lean` imports every `.lean` module in `formalization/Bgs/`; CI checks this
coverage before running Lake. A green build therefore cannot be obtained by
leaving an active formal source outside the import graph.

Current active modules:

- `PairKeySecondMoment.lean` — finite `k=2` counting/bijection certificate at
  the audited design;
- `PairKeyFourthMoment.lean` — finite `k=4` variety/key-multiplicity certificate;
- `TorusLevelSets.lean` — finite torus level-set/orbit facts at `N=199`;
- `TorusScaleLaw.lean` — finite scale-law certificate at the audited `N=199`
  design;
- `CayleyExceptionalK23.lean` — finite exceptional Cayley energy at `(461,23)`;
- `HistoricalMobiusDegenerateFiber.lean` — finite diagnostic certificate for
  the degenerate fiber that invalidated the historical Möbius proof route.

The old speculative R86 `OpLocal.lean` file is **not** an active theorem module.
Its exact bytes are preserved under `record/formal_drafts/OpLocal.lean` because
it records a historically useful formulation of an open problem, but its
comments and reduction target predate the present pair-key/elliptic repair.

A finite `native_decide` certificate is evidence only for its stated finite
parameters unless a symbolic general proof is present.
