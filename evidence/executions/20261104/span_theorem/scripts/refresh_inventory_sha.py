#!/usr/bin/env python3
"""Refresh source_blob_sha of record/claim_verification_inventory.json after the registry 'updated' date bump."""
import json, hashlib, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[5]
P = ROOT / 'record/claim_verification_inventory.json'; v = json.loads(P.read_text(encoding='utf-8'))
b = (ROOT / 'record/claims.json').read_bytes()
v['source_blob_sha'] = hashlib.sha1(b'blob ' + str(len(b)).encode() + b'\0' + b).hexdigest()
P.write_text(json.dumps(v, indent=1, ensure_ascii=False, separators=(',', ': ')), encoding='utf-8'); print(v['source_blob_sha'])
