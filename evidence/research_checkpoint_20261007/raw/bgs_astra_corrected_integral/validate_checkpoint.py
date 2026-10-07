from pathlib import Path
import json,hashlib
p=Path(__file__).resolve().parent
m=json.loads((p/'manifest.json').read_text())
for r in m['files']:
 f=p/r['path'];assert f.is_file(),r['path']
 assert f.stat().st_size==r['bytes'],r['path']
 assert hashlib.sha256(f.read_bytes()).hexdigest()==r['sha256'],r['path']
print('PASS',len(m['files']),'manifest files; three exact frozen reviewed proof copies; no canonical publication.')
