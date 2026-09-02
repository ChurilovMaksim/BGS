import re, os
BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
txt = open(os.path.join(BASE, 'artifacts', 'MANIFEST.md'), encoding='utf-8').read()
refs = set(re.findall(r'artifacts/[\w\-./]+', txt))
missing = sorted(r for r in refs if not os.path.exists(os.path.join(BASE, r.replace('/', os.sep))))
print("total refs:", len(refs), "missing:", len(missing))
for m in missing:
    print(" MISSING:", m)
