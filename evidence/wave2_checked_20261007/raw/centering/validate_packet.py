#!/usr/bin/env python3
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def require(cond,msg):
    if not cond:raise RuntimeError(msg)
m=json.loads((ROOT/'manifest.json').read_text())
for rel,want in m['artifacts'].items():
    require(sha(ROOT/rel)==want,'packet hash mismatch: '+rel)
r=json.loads((ROOT/'checks/results.json').read_text())
require(r['status']=='passed','check run not passed')
require(len(r['checks'])==20,'unexpected exact check count')
require(all(x['passed'] for x in r['checks']),'nonpassing recorded control')
pins=json.loads((ROOT/'input_manifest.json').read_text())
src=Path(pins['source_snapshot'])
source_checked=False
if src.exists():
    for item in pins['records']:
        require(sha(src/item['path'])==item['sha256'],'source hash mismatch: '+item['path'])
    source_checked=True
print(json.dumps({'status':'passed','packet_artifacts':len(m['artifacts']),'exact_controls':20,'source_pins_rechecked':source_checked,'boundary':'Integrity only; not a mathematical proof audit.'},indent=2))
