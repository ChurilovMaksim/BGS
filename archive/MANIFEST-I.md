# Archive manifest — phase 1, package I (old source_metadata snapshots)

Byte-for-byte archival copies of 14 superseded registry-metadata snapshots
from `evidence/source_metadata/`, moved under `archive/` with the original
paths preserved. Source tree: the assembled post-package-C tree
(corresponding to main `2401f0f` in this area; the package areas were
verified unchanged on live main `bb1513a` — see the package report).

The snapshots that remain live in `evidence/source_metadata/` are the
20261022 pair and the 20261022_recheck pair (the latter is the cache pinned
by `literature/metadata_audit.json` and read by the maintained
bibliographic audit), together with the directory `README.md`.

## Epoch index

| Epoch | Snapshot | Note |
|---|---|---|
| 2026-10-06 | `registry_metadata_20261006.json` (+ digest) | Initial registered bibliography audit snapshot. |
| 2026-10-06 (pre-checkpoint copy) | `history/20261007_before_phase_checkpoint/registry_metadata_20261006.json` (+ digest) | The 2026-10-06 snapshot as preserved before the 2026-10-07 phase checkpoint. |
| 2026-10-11 | `registry_metadata_20261011.json` (+ digest) | Snapshot of 11 October 2026. |
| 2026-10-11 (cavity) | `registry_metadata_20261011_cavity.json` (+ digest) | The Schur (cavity) cache whose bytes the later snapshots preserve. |
| 2026-10-12 (haar) | `registry_metadata_20261012_haar.json` (+ digest) | The reviewed Haar-impact cache. |
| 2026-10-13 (feedback) | `registry_metadata_20261013_feedback.json` (+ digest) | Feedback-round snapshot. |
| 2026-10-20 | `registry_metadata_20261020.json` (+ digest) | The snapshot named by the provenance field of 37 entries in `literature/external_dependencies.json`; those provenance values are historical records and are intentionally not rewritten — this manifest is their resolution. |

## Files (old path → new path → git blob SHA → bytes)

| Old path | New path | Blob SHA | Bytes |
|---|---|---|---:|
| evidence/source_metadata/registry_metadata_20261006.json | archive/evidence/source_metadata/registry_metadata_20261006.json | 4ad6a9a1b7b9033283f8280ca68029db224fe93d | 198155 |
| evidence/source_metadata/registry_metadata_20261006.sha256 | archive/evidence/source_metadata/registry_metadata_20261006.sha256 | c602c5bf97c40d60d8acc100a3ad51699e69da1a | 98 |
| evidence/source_metadata/registry_metadata_20261011.json | archive/evidence/source_metadata/registry_metadata_20261011.json | 468740fbfcca817c47157a3200cbe771a6705d43 | 212358 |
| evidence/source_metadata/registry_metadata_20261011.sha256 | archive/evidence/source_metadata/registry_metadata_20261011.sha256 | 45b3f59a1d58e9422ba768d9486dccb2b00a7f0b | 98 |
| evidence/source_metadata/registry_metadata_20261011_cavity.json | archive/evidence/source_metadata/registry_metadata_20261011_cavity.json | 83cc8a975df30eee3df9b7e61e69742af7b485f7 | 213020 |
| evidence/source_metadata/registry_metadata_20261011_cavity.sha256 | archive/evidence/source_metadata/registry_metadata_20261011_cavity.sha256 | be94bf4f0efe2c450255139fdba6670df166f7f6 | 105 |
| evidence/source_metadata/registry_metadata_20261012_haar.json | archive/evidence/source_metadata/registry_metadata_20261012_haar.json | deeac2f116dfbade336a23db826b455669c83a8d | 214296 |
| evidence/source_metadata/registry_metadata_20261012_haar.sha256 | archive/evidence/source_metadata/registry_metadata_20261012_haar.sha256 | 2eb05e06072c70c4e47c52dc1b4dbfd4be8473c1 | 128 |
| evidence/source_metadata/registry_metadata_20261013_feedback.json | archive/evidence/source_metadata/registry_metadata_20261013_feedback.json | b2ed58f02d4b6c0df10b6a3eb822dbce75c1e971 | 214542 |
| evidence/source_metadata/registry_metadata_20261013_feedback.sha256 | archive/evidence/source_metadata/registry_metadata_20261013_feedback.sha256 | 18851c790300647af6f56a42b453a73d14228d3d | 107 |
| evidence/source_metadata/registry_metadata_20261020.json | archive/evidence/source_metadata/registry_metadata_20261020.json | 85983cb9796b4ed6835fca1bb4d1da4bec8e7bbd | 227550 |
| evidence/source_metadata/registry_metadata_20261020.sha256 | archive/evidence/source_metadata/registry_metadata_20261020.sha256 | 3e07ac839a2bf2e28406ac9c52ec792404d5b3d7 | 98 |
| evidence/source_metadata/history/20261007_before_phase_checkpoint/registry_metadata_20261006.json | archive/evidence/source_metadata/history/20261007_before_phase_checkpoint/registry_metadata_20261006.json | 13f40ef8effae0bc57a7e8f23284084357d84e4a | 187748 |
| evidence/source_metadata/history/20261007_before_phase_checkpoint/registry_metadata_20261006.sha256 | archive/evidence/source_metadata/history/20261007_before_phase_checkpoint/registry_metadata_20261006.sha256 | 213793cc127fb8dc5c21d2ed66202b0326b3af78 | 98 |

Total: 14 files, 1,468,401 bytes.

## Same-package reference updates

Four live markdown links were migrated to the archive paths in the same
package: three in `evidence/source_metadata/README.md` (snapshots 20261020,
20261012_haar, 20261011_cavity) and one in `literature/bibliography.md`
(snapshot 20261006). The 37 provenance values in
`literature/external_dependencies.json` and the references inside frozen
evidence manifests and completed `record/` working files are historical
records; they are not rewritten and resolve through this manifest.
