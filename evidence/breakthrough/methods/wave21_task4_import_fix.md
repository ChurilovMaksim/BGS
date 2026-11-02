# Wave 21, task 4 — Import fix in all three Lean milestone drafts

## Verdict

Done, workspace only. No `lake build` run, no repository file touched,
fixed building copy untouched (md5 `43019183fe3748c33c77b6b9062d883b`
before and after).

## Background (wave 20, task 4, connector at HEAD `d87dce0`)

Module path is flat `import Bgs.LineBDerand`
(`formalization/Bgs/LineBDerand.lean`, blob `01fa6e63…`); the file
declares dotted namespace `Bgs.LineB.Derand`. The drafts wrongly wrote
`import Bgs.LineB.Derand`. Fix per file: flat import + keep the existing
`open Bgs.LineB.Derand` (namespace open, correct as written).

## Exact diffs (old → new)

### `lean-drafts/LineBLemmaYMilestone1Draft.lean` (2 hunks)

```diff
- - VERIFIED (wave 6 grep): flat import `import Bgs.LineB.Derand`;
+ - VERIFIED (wave 6 grep): flat import `import Bgs.LineBDerand`
+   (namespace `Bgs.LineB.Derand` opened below);
- import Bgs.LineB.Derand        (line 71)
+ import Bgs.LineBDerand         (line 72; +1 from the comment split)
```

### `lean-drafts/LineBLemmaYMilestone2Draft.lean` (1 hunk, line 17)

```diff
- import Bgs.LineB.Derand
+ import Bgs.LineBDerand
```

### `lean-drafts/LineBLemmaYMilestone3Draft.lean` (1 hunk, line 17)

```diff
- import Bgs.LineB.Derand
+ import Bgs.LineBDerand
```

## Verification

- `grep "^import Bgs.LineB.Derand"` over all three drafts: no matches.
- Import/open lines now, all three files: `import Bgs.LineBDerand`
  followed by `open Bgs.LineB.Derand` (M1 lines 72/76, M2 lines 17/19,
  M3 lines 17/19).
- Body diff (everything after the header import/open block, originals
  backed up at `/tmp/milestone_orig/`): IDENTICAL in all three files —
  every definition and theorem statement is byte-identical; only the
  header import lines (and one M1 header comment restating them)
  changed.

## Caveat (not fixed here, out of scope)

Import placement is unchanged: in all three drafts the import still
follows the module doc comment, which Lean rejects (wave 19 moved the
import to line 1 in the fixed building copy for exactly this reason).
At elaboration time, each draft still needs the import moved above the
doc comment; this task changed only the import path.
