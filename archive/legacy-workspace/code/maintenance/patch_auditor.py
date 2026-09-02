import os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
p = os.path.join(ROOT, "src", "maintenance", "consistency_audit.py")
s = open(p, encoding="utf-8").read()

old = """missing = []
for doc, p in sorted(cited):"""
new = """missing = []
# citations explicitly annotated "(absent ...)" in the document are intentional
cited = {(doc, q) for (doc, q) in cited
         if f"`{q}` (absent" not in rd(doc)}
for doc, p in sorted(cited):"""
if old in s and "explicitly annotated" not in s:
    s = s.replace(old, new, 1)
    open(p, "w", encoding="utf-8").write(s)
    print("auditor patched: annotated-absent citations are exempt")
else:
    print("auditor already patched")
