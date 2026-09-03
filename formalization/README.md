# Lean 4 formalization

`formalization/` is the active **finite-certificate and falsifier layer** of the
project. It is intentionally smaller than the informal mathematics: Lean code
is added only when a precise finite statement or regression guard is worth
kernel checking. The repository does **not** pad the language statistics with
speculative `sorry` files.

Build every active module:

```bash
cd formalization
lake build
```

`Bgs.lean` imports every `.lean` file under `formalization/Bgs/`. The repository
audit and CI both check that the import graph and the directory agree exactly.

## Active modules

| Module | What it certifies | Scope |
|---|---|---|
| `PairKeySecondMoment.lean` | constraint count and pair-key parametrization | finite `p=53, K=13` |
| `PairKeyFourthMoment.lean` | diagonal multiplicity, off-diagonal injectivity, coupled count | finite `p=53, K=13` |
| `CayleyEnergy.lean` | generic/exceptional mixed Cayley energies for `K=11,13` and the `K=23` non-uniformity witness | explicit finite designs |
| `TorusLevelSets.lean` | level-set cardinalities, orbit counts, freeness | finite `p=199, K=11` |
| `TorusScaleLaw.lean` | branch-scale identities | finite `p=199` |
| `HistoricalMobiusDegenerateFiber.lean` | concrete `d=0` degeneracy in the retracted Möbius route | finite falsifier at `p=53,199` |

The former `CayleyExceptionalK23.lean` was folded into the reusable
`CayleyEnergy.lean` module so the same formal implementation now includes
generic and exceptional controls rather than a single isolated anchor.

## Trust boundary

Most large finite searches use `native_decide`. A theorem here certifies its
stated finite proposition; it does not silently become a symbolic theorem for
all primes. Open analytic obligations—especially the elliptic/sheaf estimate
and the microscopic BGS bridge—remain in `mathematics/`, not as `sorry`-based
pseudo-progress in the active Lean library.

Historical formal drafts are recoverable from Git history before the
2026-09-03 archive cleanup; they are not duplicated in the current tree.
