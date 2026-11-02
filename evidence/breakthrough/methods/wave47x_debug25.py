import math
modB = 25
pw = [(1, 0)]
for _ in range(40):
    x, y = pw[-1]
    pw.append(((17*x + 24*y) % modB, (12*x + 17*y) % modB))
    if pw[-1] == (1, 0):
        print("ord(beta) mod 25 =", len(pw)-1); break
def cycleB(S, n=15):
    a, bb = S; vals = []
    for (x, y) in pw[:n]:
        vals.append((2*((a*x + 2*bb*y) % modB)) % modB)
    return vals
def period_of(vals):
    for d in range(1, len(vals)+1):
        if len(vals) % d == 0 and all(vals[k] == vals[k % d] for k in range(len(vals))):
            return d
    return len(vals)
from collections import Counter
cnt = Counter()
examples = {}
for a in range(modB):
    for bb in range(modB):
        if a % 5 == 0 and bb % 5 == 0: continue
        v = cycleB((a, bb))
        per = period_of(v)
        nd = len(set(v))
        neg = any((v[i] + v[j]) % modB == 0 for i in range(15) for j in range(15))
        cnt[(per, nd, neg)] += 1
        examples.setdefault((per, nd, neg), ((a, bb), v))
for k in sorted(cnt):
    print(k, cnt[k], "e.g.", examples[k][0], examples[k][1][:6])
