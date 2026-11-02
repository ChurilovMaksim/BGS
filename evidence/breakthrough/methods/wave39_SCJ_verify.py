"""Wave 39, task 1, verification: distinct (a,b) pairs (=> injectivity of
configurations -> fibers), diagonal orbit sizes, clean Gamma probes.
Companion to wave39_SCJ_direct.py."""
import math, sys
sys.path.insert(0, ".")
exec(open("wave38_blind_explore.py").read().split("m = 60")[0])
M = 180
sf729 = split_fibers(M, 729)
sf625 = split_fibers(M, 625)
a = sf625[0][1][0]
reps729 = sf729[0][1]
Cs729 = [recover_C(r, 729) for r in reps729]
by_k = {C[1] // 27: r for C, r in zip(Cs729, reps729)}
b, bp = by_k[20], by_k[11]
pairs = list(zip(a, b))
print("distinct (a,b) pairs:", len(set(pairs)), "of", len(pairs))

def orb_size(seqs):
    seen = set()
    for k in range(M):
        seen.add(tuple(tuple(s[(i + k) % M] for i in range(M)) for s in seqs))
        seen.add(tuple(tuple(s[(-i - k) % M] for i in range(M)) for s in seqs))
    return len(seen)
print("diag orbit size b-row:", orb_size([a, b]))
print("diag orbit size b'-row:", orb_size([a, bp]))

def kernel_seeds(m, q):
    Mm = mat_pow([6, q - 1, 1, 0], m, q)
    a0 = (Mm[0] - 1) % q; b0 = Mm[1] % q; c0 = Mm[2] % q; d0 = (Mm[3] - 1) % q
    g = math.gcd(a0, q); seeds = []
    for y0 in range(q):
        if (b0 * y0) % g != 0:
            continue
        a1, q1 = a0 // g, q // g; rhs = (-(b0 * y0) // g) % q1
        y1_0 = (pow(a1, -1, q1) * rhs) % q1 if q1 > 1 else 0; step = q // g
        for k in range(g):
            y1 = y1_0 + k * step
            if (c0 * y1 + d0 * y0) % q == 0:
                seeds.append((y0, y1))
    return seeds

def build(seed, q):
    y = [seed[0], seed[1]]
    for i in range(2, M):
        y.append((6 * y[-1] - y[-2]) % q)
    return tuple(y)
o = build(kernel_seeds(M, 72361)[12345], 72361)
print("o at 72361 period:", period(o))
base_ms = tuple(sorted(zip(a, b, o)))
coll = 0
for k in [1, 7, 11, 29]:
    if tuple(sorted(zip(a, b, tuple(o[(i + k) % M] for i in range(M))))) == base_ms:
        coll += 1; print("  rotation", k, "COLLIDES")
if tuple(sorted(zip(a, b, tuple(o[(-i) % M] for i in range(M))))) == base_ms:
    coll += 1; print("  reversal COLLIDES")
print("genuine Gamma collisions on o@72361:", coll, "/5")
print("Delta_min = 2*360*360*(1-cos(2pi/3)) =", 2 * 360 * 360 * 1.5)
B180 = 49 * 121 * 361 * 841 * 1681 * 3481 * 72361
print("B(180) =", B180)
print("one-section total >=", B180 * 388800, " ~ %.3e" % (B180 * 388800))
print("180^11 = %.3e ; 180^12 = %.3e" % (180.0 ** 11, 180.0 ** 12))
print("WAVE39 SCJ VERIFY DONE")
