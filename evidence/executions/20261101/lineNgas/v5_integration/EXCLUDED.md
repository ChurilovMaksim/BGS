# Files not committed (Line N v5 integration)

| path | bytes | sha256 | reason |
|---|---|---|---|
| `evidence/executions/20261101/lineNgas/N20/scratch/THEOREM_DRAFT_v5_proposed.md` | 25681 | `162f2c6017b898608187f21d943d79a16be3e7dcc53301a366d202e5a0c9cc1d` | `.gitignore` excludes `scratch/` |
| `evidence/executions/20261101/lineNgas/N20/scratch/THEOREM_DRAFT_v5_proposed_v2.md` | 26762 | `bbd00b2a049e79d02911d7abd32e000742d598a63c653502b3a46d649702e37c` | `.gitignore` excludes `scratch/` |

Both are author proposals that THEOREM_DRAFT_v5 supersedes. They are listed in `N20/SHA256_N20_v2.txt`, so in a clean checkout
those two entries of that manifest report missing files. Every other entry verifies (`manifests.log`). Python byte caches
(`__pycache__`) are not copied. No file in this integration is larger than 5 MiB.
