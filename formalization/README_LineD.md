`Bgs/LineDCerts.lean` — `namespace Bgs.LineDCerts`, no imports (Lean core), kernel `decide` only, no sorry /
native_decide. The import in `Bgs.lean` is the line after `import Bgs.LineCEncounter` (main d6fa6e2a). Line B had
not merged, so there is no `Bgs.LineBPhase4` import to follow; the module imports nothing, so the order does not
affect its proofs. The packet's isolated check was `lake exe cache get && lake build Bgs.LineDCerts` (exit 0, 47.7 s)
plus `lake env lean` on a file containing `import Bgs.LineDCerts` (exit 0). The repository integration runs
`lake exe cache get` and then a full `lake build Bgs`.
