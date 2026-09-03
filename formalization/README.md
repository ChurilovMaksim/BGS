# Lean formalization

This is the active Lean 4 formalization layer.

Build from the repository root with

```bash
cd formalization
lake build
```

`Bgs.lean` imports every `.lean` module in `formalization/Bgs/`; CI checks this
coverage before running Lake. A green build therefore means that no active
formal source was silently omitted from the default target.

Current scope:

- `K2Reduction.lean`, `K4Variety.lean`, `TorusLevelSets.lean`,
  `ScaleLaw.lean` and `CayleyExceptionalK23.lean` contain finite decidable
  certificates at explicitly named designs.
- `M1DegenerateFiber.lean` certifies the historical degenerate Möbius fiber;
  this is a diagnostic/retraction witness, not a proof of the current M1
  statement.
- `OpLocal.lean` is an actively type-checked specification of the elliptic/local
  obligations. It contains explicit `sorry` placeholders and therefore is
  **not** a completed theorem. Its purpose is to expose, rather than hide, the
  remaining formal proof obligations.

A finite `native_decide` certificate is evidence only for the stated finite
parameters unless a symbolic general proof is present.
