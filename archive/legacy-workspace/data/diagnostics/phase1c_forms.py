"""PHASE 1c: test candidate functional forms for max_N3 across
existing scan artefacts (run36_audit + run20_constant)."""
import os as _os
_BGS_ROOT = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import json, math

A = _BGS_ROOT + r"\artifacts"
data = []
d1 = json.load(open(A + r"\run36_audit.json"))
for r in d1:
    data.append((r["p"], r["k"], r["maxN3"]))
try:
    d2 = json.load(open(A + r"\run20_constant.json"))
    for r in d2:
        data.append((r["p"], r["k"], r["max_N3"]))
except FileNotFoundError:
    pass

print(f"total (p,k,maxN3) points: {len(data)}")

def ratios(form):
    out = []
    for p, k, m in data:
        b = form(p, k)
        if b > 0:
            out.append(m / b)
    return out

forms = {
    "floor(k2/p)+2":        lambda p, k: k * k // p + 2,
    "C*sqrt(k)":            lambda p, k: math.sqrt(k),
    "C*(k^2/p + sqrt(k))":  lambda p, k: k * k / p + math.sqrt(k),
    "C*max(k2/p, sqrt(k))": lambda p, k: max(k * k / p, math.sqrt(k)),
}
for name, f in forms.items():
    rs = ratios(f)
    rs_s = sorted(rs)
    med = rs_s[len(rs)//2]
    print(f"{name:26s} min={min(rs):7.3f} med={med:7.3f} "
          f"max={max(rs):8.3f}")

# where does pure sqrt(k) fail worst?
worst = sorted(data, key=lambda t: -t[2]/math.sqrt(t[1]))[:5]
print("\nworst for pure sqrt(k):")
for p, k, m in worst:
    print(f"  p={p} k={k}: maxN3={m}  ratio={m/math.sqrt(k):.2f}")
