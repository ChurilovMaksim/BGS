#!/usr/bin/env python3
"""Check that the two integration-edited Line H packet files reduce to the refereed packet bytes (receipt.json sha256).

Reverses, in memory only, the documented integration edits (INTEGRATION.md) and compares sha256 with receipt.json.
Usage (repository root): python3 evidence/executions/20261030/lineH/restore_packet_bytes.py   [--write DIR to save restored copies]"""
import hashlib, json, re, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[4]
REC = json.loads((ROOT / 'evidence/executions/20261030/lineH/receipt.json').read_text())['sha256']
NOTE = 'mathematics/fixed-map/lineH_49state_certificate.md'
LEAN = 'formalization/Bgs/LineH.lean'
# (packet text, integrated text) for the math note, besides the inserted ID-anchor paragraph
NOTE_DELTAS = [
    ("since h_d | h_m for d | m (BGS-TRACE-205, G5).",
     "since h_d | h_m for d | m with m odd (Lean `Bgs.LineG.nsw_dvd`, `formalization/Bgs/LineG.lean`; not registered by a proved claim)."),
    ("applies: R_NSW is violated", "applies: R_NSW (registered as BGS-TRACE-210, open) is violated"),
    ("BGS-TRACE-205 G5 (h_d | h_m, used only for R_NSW)",
     "the Lean lemma `Bgs.LineG.nsw_dvd` in `formalization/Bgs/LineG.lean` (h_d | h_m, used only for R_NSW)"),
    ("(`referee/refV0.json`)", "(`referee/out/refV0.json`)"),
]
def restore_note(s):
    i = s.index('\nRegistered claims (`record/claims.json`)'); j = s.index('\n', i + 1) + 1
    s = s[:i] + s[j:]                                   # drop the inserted paragraph and its preceding blank line
    for old, new in NOTE_DELTAS:
        assert s.count(new) == 1, new
        s = s.replace(new, old)
    return s
def restore_lean(s):
    s = re.sub(r'#print axioms \w+\n', '', s)
    return s.replace('\n\nend Bgs.LineH', '\nend Bgs.LineH')
ok = True
for rel, fn in ((NOTE, restore_note), (LEAN, restore_lean)):
    t = fn((ROOT / rel).read_text(encoding='utf-8')).encode('utf-8')
    good = hashlib.sha256(t).hexdigest() == REC[rel]
    ok &= good
    print(('OK  ' if good else 'FAIL'), rel)
    if len(sys.argv) > 2 and sys.argv[1] == '--write':
        out = Path(sys.argv[2]) / rel; out.parent.mkdir(parents=True, exist_ok=True); out.write_bytes(t)
sys.exit(0 if ok else 1)
