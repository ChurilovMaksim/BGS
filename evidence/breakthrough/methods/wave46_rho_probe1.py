# Probe 1: fibers of the two GPL witness pairs + class-homogeneity + alpha orders.
from collections import defaultdict
ALPHA = (3, 2)
def mul(a, b, M): return ((a[0]*b[0]+2*a[1]*b[1]) % M, (a[0]*b[1]+a[1]*b[0]) % M)
def pw(a, n, M):
    r = (1, 0)
    while n:
        if n & 1: r = mul(r, a, M)
        a = mul(a, a, M); n >>= 1
    return r
def seq(B, M):
    ap = [pw(ALPHA, i, M) for i in range(32)]
    return [(2*mul(B, a, M)[0]) % M for a in ap]
def fibers(p, a):
    F = defaultdict(list)
    for i in range(32): F[(p[i], a[i])].append(i)
    return F
def report(name, B2, B2p, Bq):
    p, pp, a = seq(B2, 8192), seq(B2p, 8192), seq(Bq, 17)
    F, Fp = fibers(p, a), fibers(pp, a)
    mixed = [v for v, idx in F.items() if len({i % 4 for i in idx}) > 1]
    sizes = sorted(len(v) for v in F.values())
    pairs16 = all(sorted(idx)[1] == sorted(idx)[0]+16 for idx in F.values() if len(idx) == 2)
    print(f"{name}: nfib={len(F)} sizes={sizes} mixed-class fibers={len(mixed)} "
          f"all size-2 fibers are {{i,i+16}}: {pairs16}")
    if mixed: print("   mixed examples:", [(F[v], v) for v in mixed[:3]])
    return p, pp, a
report("reversal", (128,64), (128,64), (8,8))  # B2 fixed; Bq differs (8,8) vs (9,9) handled below
# reversal witness: B2 fixed (128,64), Bq (8,8) vs (9,9)=-Bq
p = seq((128,64), 8192); a = seq((8,8), 17); ap = seq((9,9), 17)
print("reversal pair globals equal:", sorted(zip(p,a)) == sorted(zip(p,ap)))
F = fibers(p, a); Fp = fibers(p, ap)
print("reversal: nfib=", len(F), "mixed=", sum(1 for v in F.values() if len({i%4 for i in v})>1),
      "sizes=", sorted(len(v) for v in F.values()))
report("swap", (2944,1856), (6016,832), (13,2))
print()
print("alpha orders mod qR (ring (Z/q)[sqrt2]):")
for q in [17, 577, 257, 41, 73, 89, 97, 137, 193, 241, 409, 65537]:
    a16, a32 = pw(ALPHA, 16, q), pw(ALPHA, 32, q)
    print(f"  q={q}: alpha^16={a16} alpha^32={a32} order32={a32==(1,0) and a16!=(1,0)}")
