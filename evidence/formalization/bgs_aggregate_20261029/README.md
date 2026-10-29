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

| Branch | Log | Exit |
|---|---|---|
| `cursor/diagonal-phase-form-factor-51b0` (#48) | [build_head48.log](build_head48.log) | 0 |
| `cursor/diagonal-phase-short-time-51b0` (#47) | [build_head47.log](build_head47.log) | 0 |
| `cursor/scalar-return-bessel-51b0` (#49) | [build_head49.log](build_head49.log) | 0 |
| `cursor/sixteen-phase-symmetry-51b0` (#50) | [build_head50.log](build_head50.log) | 0 |

## TRACE-131 build

On 29 October 2026, after `lake exe cache get`, `lake build Bgs` exited 0 (`8791` jobs) on `cursor/hyperbolic-diagonal-form-factor-cf38`. Log: [build_trace131.log](build_trace131.log), sha256 `2118079bc22700518846e55ca75c84e3a5d0f64fbcaf786ea7c2bd0e3d938b8c`. The new module is `Bgs.HyperbolicDiagonalFormFactor`. It uses `decide` and contains neither `sorry` nor `native_decide`.

A second build on the same branch, after `Bgs.HyperbolicShortTime` was added, exited 0 (`8792` jobs). Log: [build_trace132.log](build_trace132.log), sha256 `de90e9a410bd3309cfd7a135d8bcee1c8568c7bff3b1bbf053446ef5448c27e0`. That module likewise uses `decide` and contains neither `sorry` nor `native_decide`.

The referee correction of 29 October 2026 was rebuilt with the same command. `lake build Bgs` exited 0 (`8792` jobs). Log: [build_referee_fix.log](build_referee_fix.log), sha256 `d99f3e30a5a4ac8a499f0a59aa04073215d66c912b73917df5e530d68f05f492`.

## TRACE-143 build

On 29 October 2026, after `lake exe cache get` (8690 cached files, exit 0; log [cache_get_trace143.log](cache_get_trace143.log), sha256 `6c92ede4d776090f22cd46fb56958ea0dbb7b4e60ecb4cbe7e66f928487b14bb`), `lake build Bgs` exited 0 (`8795` jobs). Log: [build_trace143.log](build_trace143.log), sha256 `7bfa3568d6eb3dac163fa96df44f70930d5e99d6a1ca2b327b3c2bf5827abc64`. The new module is `Bgs.LineCEncounter`. It uses `decide` and contains neither `sorry` nor `native_decide`. `Bgs.LineCEncounter` itself took 194 s. Printed axioms are `propext` or none. Mathlib was taken from the cache and was not built from source. GitHub Actions minutes were exhausted, so this log is the build evidence.
