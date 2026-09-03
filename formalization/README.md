# Lean formalization

This directory is the active Lean 4 **finite-certificate** layer. It contains no speculative `sorry`-based theorem module.

Build from the repository root:

```bash
cd formalization
lake build
```

`Bgs.lean` imports every `.lean` file under `formalization/Bgs/`; CI checks exact coverage before Lake runs. A green build therefore cannot hide an active module outside the import graph.

## Active modules

- `PairKeySecondMoment.lean` — finite `p=53, K=13` constraint-count and pair-key parameterization certificate.
- `PairKeyFourthMoment.lean` — finite diagonal multiplicity, off-diagonal key injectivity and `V4` count at `p=53, K=13`.
- `TorusLevelSets.lean` — finite level-set cardinalities, orbit counts and freeness at `p=199, K=11`.
- `TorusScaleLaw.lean` — finite branch-scale identities at the same `p=199` design.
- `CayleyExceptionalK23.lean` — exact finite negative control at `(p,K)=(461,23)`.
- `HistoricalMobiusDegenerateFiber.lean` — finite falsifier for the degenerate `d=0` fiber in the retracted historical Möbius route.

The old R86 `OpLocal.lean` is not active. Its exact historical source is under `record/formal_drafts/OpLocal.lean` because it records an obsolete formulation of an open programme rather than a current theorem.

## Evidence boundary

Most nontrivial finite searches use `native_decide`; the source prints axiom information where useful. Such a theorem certifies only its explicit finite parameters unless accompanied by a separate symbolic proof. In particular, the finite torus and scale modules do not establish their motivating analytic statements uniformly in `p`.
