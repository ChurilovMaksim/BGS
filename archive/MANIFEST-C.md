# Archive manifest — package C (remainder): chat integration layer

Source tree: local post-package-D tree (`~/workspace/bgs_postmove/`, main @ `10a7123` plus the phase-0/CI/Ф.2 areas noted in the coupling report).
Seven live integration files move to `archive/<original path>`. Three are byte-for-byte; four carry only the mechanical edits listed below (relative-link rebasing for the +1 depth, and one data field). Nothing else in their content changes.

| Old path | New path | Blob SHA (original) | Blob SHA (archive copy) | Bytes (copy) | Changed lines |
|---|---|---|---|---|---|
| `record/chat_claim_inventory_20261016.json` | `archive/record/chat_claim_inventory_20261016.json` | `134c0ae0a5af297ef13ceb778d41ed0f98afab35` | `134c0ae0a5af297ef13ceb778d41ed0f98afab35` | 72069 | 0 |
| `record/chat_integration_20261019_inventory.json` | `archive/record/chat_integration_20261019_inventory.json` | `d8ac63be84d45816c7b02a9db3d9aa705a2fdfeb` | `d8ac63be84d45816c7b02a9db3d9aa705a2fdfeb` | 232082 | 0 |
| `record/chat_integration_20261011.md` | `archive/record/chat_integration_20261011.md` | `b9f7483bd357898938b4bb50a8507d213b3b0702` | `b903b39b8cb2ce2286ee0f11ae7e18fd34dbd37d` | 12908 | 20 |
| `record/chat_integration_20261016.json` | `archive/record/chat_integration_20261016.json` | `2c8e9a1731b1b403fc4ff4063327adc04e07dd81` | `dace9dee895ec98948e1df8a4af143fc763eff29` | 5705 | 1 |
| `record/chat_integration_20261016.md` | `archive/record/chat_integration_20261016.md` | `40a94590dcec4f06e8d59d4405e35b2960926868` | `ad2d9e4f85324038e1293b2f644c910173c7bbe9` | 32797 | 93 |
| `record/chat_integration_20261019.md` | `archive/record/chat_integration_20261019.md` | `10303023c3b3849654fcb28345b8f5bdafffcb92` | `97f91087550880f158d6f84ac327f7be830a4b44` | 9084 | 5 |
| `literature/chat_integration_sources_20261016.md` | `archive/literature/chat_integration_sources_20261016.md` | `c4bcf42f694da140ffda114a737b7c67131b3d27` | `c4bcf42f694da140ffda114a737b7c67131b3d27` | 2494 | 0 |

Mechanical edits inside the archive copies:
- `archive/record/chat_integration_20261011.md` — 21 outgoing relative links on 20 lines rebased (`../mathematics/…` → `../../mathematics/…`, bare/record-relative → `../../record/…`, evidence links +1 level).
- `archive/record/chat_integration_20261016.md` — 93 outgoing relative links on 93 lines rebased; links to the document moved earlier by package D are redirected to `../history/2026/chat_20261015/BGS_complete_research_2026-10-15.md` (i.e. `archive/history/2026/chat_20261015/…`); the two bare same-directory links (to `chat_integration_20261016.json` and `chat_claim_inventory_20261016.json`) are unchanged, as both files move into the same archive directory.
- `archive/record/chat_integration_20261019.md` — 5 outgoing relative links rebased (+1 level); the bare link to `chat_integration_20261019_inventory.json` is unchanged (same archive directory).
- `archive/record/chat_integration_20261016.json` — one field: `historical_inventory` now names `archive/record/chat_claim_inventory_20261016.json`.

Resolution rule for historical references: any pre-move path `record/chat_…` or `literature/chat_integration_sources_20261016.md` in frozen records (evidence manifests, the epoch registry `record/claim_integration_epochs.json`, the wave contract `computations/verification/chat_20261019/integration_contract.json`, receipts under `archive/history/`) resolves through this manifest to the `archive/` location in the first column’s row. Frozen records are not edited.

Note on `archive/record/chat_claim_inventory_20261016.json`: its `preserved_in` / `current_destination` values name `record/history/2026/chat_20261015/…` — the location that was current when the inventory was written; that document now lives at `archive/history/2026/chat_20261015/…` per the package D manifest (`archive/history/MANIFEST.md`). The inventory itself is byte-for-byte.
