# Independent Python validation of one C++ Phase-A slice (wave44 definitions verbatim).
# Slice: B2=(3712,7168) mod 8192, all Bq mod 577. Expect (from C++):
#   coll=291024 id=125712 nonid=165312 jblbad=0
import math
from collections import defaultdict
ALPHA = (3, 2)
def mul(a, b, M):
    return ((a[0]*b[0] + 2*a[1]*b[1]) % M, (a[0]*b[1] + a[1]*b[0]) % M)
def pw(a, n, M):
    r = (1, 0)
    for _ in range(n):
        r = mul(r, a, M)
    return r
m, q2, q = 32, 8192, 577
t = math.gcd(m, 4)
perms = [tuple((eps*r + b) % t for r in range(t)) for eps in (1, -1) for b in range(t)]
ap2 = [pw(ALPHA, i, q2) for i in range(m)]
apq = [pw(ALPHA, i, q) for i in range(m)]
B2 = (3712, 7168)
p = tuple((2*mul(B2, a, q2)[0]) % q2 for a in ap2)
def joints(o):
    return tuple(tuple(sorted(zip(p[r::t], o[r::t]))) for r in range(t))
first = {}
coll = idc = nonid = bad = 0
for x in range(q):
    for y in range(q):
        Bq = (x, y)
        o = tuple((2*mul(Bq, a, q)[0]) % q for a in apq)
        glob = tuple(sorted(zip(p, o)))
        if glob not in first:
            first[glob] = joints(o)
        else:
            coll += 1
            j = joints(o)
            j0 = first[glob]
            if j == j0:
                idc += 1
            elif any(all(j[r] == j0[pp[r]] for r in range(t)) for pp in perms):
                nonid += 1
            else:
                bad += 1
                if bad <= 3:
                    print("PY-BAD:", Bq)
    if x % 100 == 0:
        print(f"  x={x} coll={coll} id={idc} nonid={nonid} bad={bad}", flush=True)
print(f"FINAL coll={coll} id={idc} nonid={nonid} bad={bad}")
print("EXPECT coll=291024 id=125712 nonid=165312 bad=0")
print("MATCH" if (coll, idc, nonid, bad) == (291024, 125712, 165312, 0) else "MISMATCH")
