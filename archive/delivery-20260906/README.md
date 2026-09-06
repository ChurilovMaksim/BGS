# Original consolidation delivery — external byte-authoritative provenance

The final repository audit recovered the exact delivery produced by the earlier
204-file consolidation pass from the user's ChatGPT Library. The binary archive
was verified locally before finalization, but is **not** re-encoded into Git
through the connector: long binary/base64 transfers can be truncated by the
intermediate transport, so committing a possibly corrupted copy would weaken
rather than strengthen provenance.

Byte-authoritative delivery record:

```text
WoW_consolidated_research.zip
bytes   2605999
files   204
sha256  8addfd45f0c8d3d43d06472477aa8c5aac8eb3f2b94082fe6b715b20a3447099

WoW_consolidation.patch
sha256  366fe46e385b9af3f100fedc34d36413379ffde41cb2a2ddc08c749fb90081e8
```

Two compressed binary members of that delivery are recorded separately:

```text
manuscript/WoW_unified.pdf
bytes   880886
sha256  0076d2feb521fe59819b9bf243423ead832dcfa64acafbce20012b6dc09c497d

evidence/consolidation_20260906/reproduction_inputs.zip
bytes   1177213
sha256  16a4a92bbc078d90334528065f561cdff8032fb536985a03ab9c77573c9d87c3
```

The outer ZIP is the authoritative byte container for the historical repeated
run logs, frozen-input records and the two binary derivatives. Its contents were
also enumerated locally during the final audit: 204 members, total uncompressed
size 4,084,074 bytes. The active source tree and exact historical Git branch
snapshots are preserved directly in `main`; the outer ZIP remains an external
provenance artifact rather than an active source root.

This distinction is intentional. Historical logs must not be silently promoted
to executions of the final commit, and derived PDFs must not be treated as
source-of-truth mathematical evidence.
