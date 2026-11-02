from collections import Counter
import sys

def cycles(p):
    out = {}
    for a in range(p):
        for b in range(p):
            s0 = (2*a) % p
            s1 = (2*(17*a+24*b)) % p
            s = [s0, s1]
            for k in range(2, 30):
                s.append((34*s[-1] - s[-2]) % p)
            out[(a,b)] = tuple(s)
    return out

def test(pa, pb):
    ca, cb = cycles(pa), cycles(pb)
    groups = {}
    conflicts = 0
    for A, ta in ca.items():
        for B, tb in cb.items():
            b0 = tuple(sorted((ta[k]*pb+tb[k]) for k in range(30)))
            b1 = tuple(sorted(((-ta[k] % pa)*pb + (-tb[k] % pb)) for k in range(30)))
            P = tuple(sorted(b0 + b1))
            bp = (b0, b1) if b0 <= b1 else (b1, b0)
            if P in groups:
                if groups[P][0] != bp:
                    conflicts += 1
                    if conflicts <= 3: print("  CONFLICT at", A, B)
                groups[P][1].append((A,B))
            else:
                groups[P] = (bp, [(A,B)])
    sizes = Counter(len(v[1]) for v in groups.values())
    big = sum(1 for v in groups.values() if len(v[1]) > 120)
    print(f"pair ({pa},{pb}): points={pa*pa*pb*pb}, groups={len(groups)}, conflicts={conflicts}, groups>120: {big}")
    print("   sizes:", dict(sorted(sizes.items())))
    return groups

for pair in [(9,11),(9,19),(9,59),(11,59)]:
    test(*pair)
