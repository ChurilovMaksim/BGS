# SevenPrimary source succession record

**Date:** 2026-10-30. **Status:** informational record; the original
certificate `formalization/seven_primary_certificate.md` is NOT edited.

## What changed

- Certificate pin (old): SHA-256
  `431e5d111238a962ec2bb994f21d4cb1ac17df250379651aa4e8fcd065604cb4`
  = `formalization/Bgs/SevenPrimary.lean` at commit `66724291…`
  (2026-10-06, “Integrate WKB trace reductions…”).
- Current file: SHA-256
  `6f2be83b437cd9962a0c44b7c1316ad9b13ba402cc2a9b4737da22ee64341acc`
  = same file at commit `1ee02a38…` (2026-10-22, namespace unification
  “rotate SevenPrimary source pin with succession record”).
- Diff between the two versions: exactly 2 lines — `namespace SevenPrimary`
  → `namespace Bgs.SevenPrimary` and the matching `end` (+8 bytes,
  12518 → 12526). No theorem, definition, or certificate statement changed.

## Consequence

Strictly, the old certificate does not byte-cover the current file, but its
content claim (“unchanged”) holds for everything except the namespace lines
above. The current file compiles and is fully `#print axioms`-covered.
This record supplies the succession note that the certificate itself lacks;
it does not rewrite history and does not re-issue the old certificate.
