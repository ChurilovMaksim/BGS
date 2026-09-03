# Lean formalization

This is a Lean 4 project for finite certificates and formalization work.

Build from the repository root with

```bash
cd formalization
lake build
```

Current status:

- `K2Reduction.lean`, `K4Variety.lean`, `TorusLevelSets.lean`,
  `ScaleLaw.lean` and `CayleyExceptionalK23.lean` contain finite decidable
  certificates at explicitly named designs.
- `M1DegenerateFiber.lean` certifies the historical degenerate Möbius fiber;
  this is a diagnostic/retraction witness, not a proof of the current M1
  statement.
- `OpLocal.lean` is retained as formalization/specification work and contains
  admitted obligations. It must not be cited as a completed theorem.

A finite `native_decide` certificate is evidence only for the stated finite
parameters unless a symbolic general proof is present.
