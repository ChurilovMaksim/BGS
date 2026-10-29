# Aggregate `Bgs` Lean build (stack namespace fix)

**Date:** 2026-10-29  
**Scope:** Full default target `Bgs` (`formalization/Bgs.lean` importing every active module). Mechanical namespace isolation for rational witness modules so combined import no longer clashes on `rNum`, `quadCount`, `iter`, and related top-level names.

## Commands (fast path)

Reuse the same `formalization/.lake` directory across branch checkouts. From the repository root:

```sh
cd formalization
lake exe cache get
lake build Bgs
```

`lake exe cache get` pulls prebuilt Mathlib oleans from the community cache and avoids compiling Mathlib from source. Run it once per environment (or after toolchain or Mathlib pin changes), then rebuild only the `Bgs` graph.

## Verification

On branch `cursor/diagonal-phase-form-factor-51b0` (PR #48 stack base), after wrapping pre-stack rational modules in `namespace Bgs.<ModuleName>`:

| Check | Result |
|---|---|
| `lake build Bgs` exit code | 0 |
| Lake jobs | 8787 |
| Rational witness `sorry` / `native_decide` | none in `formalization/Bgs/*Rational*.lean` |

Log: [build_head48.log](build_head48.log) (sha256 `017489182fbb778be91784385815cfa5e8f870b18106a82de8c9c1119aaa1601`).

Head commits on the linear stack (#48 → #47 → #49 → #50) each record an additional log in this folder after the same command sequence.
