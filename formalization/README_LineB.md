`Bgs/LineBDerand.lean`, `Bgs/LineBPhase2.lean`, `Bgs/LineBPhase3.lean` and `Bgs/LineBPhase4.lean` — namespaces `Bgs.LineB.Derand`, `Bgs.LineB.Phase2`, `Bgs.LineB.Phase3` and `Bgs.LineB.Phase4`. Derand and Phase2 import nothing. Phase3 imports `Mathlib.Tactic.Ring`. Phase4 imports `Mathlib`. The kernels are `decide`, `norm_num` and `ring`. There is no `sorry` and no `native_decide`.

The four imports in `Bgs.lean` follow `import Bgs.LineDCerts`, which is the last `Bgs.*` import on main `502af245`. The packet patch inserted them after `import Bgs.LineCEncounter`, the last import on main `d6fa6e2a`. The modules do not import one another, so the order does not change their proofs.

The repository integration runs `lake exe cache get` and then a full `lake build Bgs`. The packet's isolated check, on a copy of main `d6fa6e2a`, is recorded in `lake_cache_get.log`, `lake_build_LineB.log` and `lake_build_Bgs.log`.
