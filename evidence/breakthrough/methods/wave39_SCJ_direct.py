"""Wave 39, task 1: test polynomial SCJ directly at m=180, bypassing B(m).

Questions:
  A) Full-tuple collision: does a full tuple of blind o's (one per non-split
     component) collide across a top-digit free pair (b,b') at 729?
  B) Distinctness: do different blind configurations give different fibers
     (different sorted tuple-multisets)?  Includes Gamma-move probes and the
     stabilizer Stab(a,b) of the locked/free pair.
  C) Phase gap + diagonal orbit sizes -> per-fiber Delta_F lower bound, and
     the realized joint total lower bound at m=180 vs m^c_J.
"""
import math, random, sys
import numpy as np
from collections import defaultdict
sys.path.insert(0, ".")
exec(open("wave38_blind_explore.py").read().split("m = 60")[0])

M = 180
rng = random.Random(20261102)
Q0S = [49, 121, 361, 841, 1681, 3481, 72361]

# ---------- D_180 exactly: e_k = alpha^k + alpha^-k, e_0=2, e_1=6 ----------
e0, e1 = 2, 6
for _ in range(2, M + 1):
    e0, e1 = e1, 6 * e1 - e0
D = e1 - 2
print(f"D_180 has {len(str(D))} digits; D%729={D % 729}, D%625={D % 625}, "
      f"D%72361={D % 72361}", flush=True)

# ---------- split fibers, locked/free reps ----------
sf729 = split_fibers(M, 729)
sf625 = split_fibers(M, 625)
print(f"729 split fibers: {len(sf729)} orbit counts {[len(r) for _, r in sf729]}", flush=True)
print(f"625 split fibers: {len(sf625)} orbit counts {[len(r) for _, r in sf625]}", flush=True)
a = sf625[0][1][0]  # locked 625 rep (wave-38 convention), C=(0,550)
print(f"locked a C={recover_C(a, 625)} period={period(a)}", flush=True)
# free 729 fiber-0 reps with C=(378,540) [k=20] and C=(378,297) [k=11]
reps729 = sf729[0][1]
Cs729 = [recover_C(r, 729) for r in reps729]
by_k = {C[1] // 27: r for C, r in zip(Cs729, reps729)}
print(f"729 fiber-0 k values: {sorted(by_k)}", flush=True)
b, bp = by_k[20], by_k[11]
print(f"free pair C: {recover_C(b,729)} vs {recover_C(bp,729)}", flush=True)
b_ctrl = by_k[10]  # non-colliding control (k=20 vs k=10)

# ---------- random kernel sequences (seed solving, no full enumeration) ----------
def kernel_seeds(m, q):
    Mm = mat_pow([6, q - 1, 1, 0], m, q)
    a0 = (Mm[0] - 1) % q; b0 = Mm[1] % q; c0 = Mm[2] % q; d0 = (Mm[3] - 1) % q
    g = math.gcd(a0, q)
    seeds = []
    for y0 in range(q):
        if (b0 * y0) % g != 0:
            continue
        a1, q1 = a0 // g, q // g
        rhs = (-(b0 * y0) // g) % q1
        y1_0 = (pow(a1, -1, q1) * rhs) % q1 if q1 > 1 else 0
        step = q // g
        for k in range(g):
            y1 = y1_0 + k * step
            if (c0 * y1 + d0 * y0) % q == 0:
                seeds.append((y0, y1))
    return seeds

def build_seq(seed, m, q):
    y = [seed[0], seed[1]]
    for i in range(2, m):
        y.append((6 * y[-1] - y[-2]) % q)
    return tuple(y)

seed_cache = {}
def rand_o(q):
    if q not in seed_cache:
        seed_cache[q] = kernel_seeds(M, q)
        print(f"  seeds at q={q}: {len(seed_cache[q])} (expect {q})", flush=True)
    return build_seq(rng.choice(seed_cache[q]), M, q)

def tup_multiset(free, os_):
    return tuple(sorted(zip(a, free, *os_)))

def rand_config():
    return [rand_o(q) for q in Q0S]

# ---------- sanity: single-o collision reproduces wave 38 ----------
print("--- sanity: single-o collisions for the free pair (expect True) ---", flush=True)
for q in Q0S:
    o = rand_o(q)
    zeros = [tuple([0] * M) for _ in Q0S]
    os_ = [o if qq == q else z for qq, z in zip(Q0S, zeros)]
    col = tup_multiset(b, os_) == tup_multiset(bp, os_)
    ctrl = tup_multiset(b, os_) == tup_multiset(b_ctrl, os_)
    print(f"  q0={q}: pair collides={col}, control collides={ctrl}", flush=True)

# ---------- Test A: full-tuple collision ----------
print("--- Test A: full-tuple collision (20 random configs) ---", flush=True)
nA = 0
for t in range(20):
    cfg = rand_config()
    col = tup_multiset(b, cfg) == tup_multiset(bp, cfg)
    nA += col
    if not col:
        print(f"  trial {t}: NO COLLISION", flush=True)
print(f"  full-tuple collisions: {nA}/20", flush=True)

# ---------- Test B: distinctness ----------
print("--- Test B: distinctness across configurations ---", flush=True)
base = rand_config()
base_ms = tup_multiset(b, base)
n_diff_all, n_diff_one = 0, 0
for t in range(30):
    cfg = rand_config()
    n_diff_all += (tup_multiset(b, cfg) != base_ms)
for t in range(30):
    cfg = list(base)
    j = rng.randrange(len(Q0S))
    cfg[j] = rand_o(Q0S[j])
    n_diff_one += (tup_multiset(b, cfg) != base_ms)
print(f"  differ-at-all: {n_diff_all}/30 distinct; differ-at-one: {n_diff_one}/30 distinct", flush=True)

# Gamma-move probes: rotate/reverse one o only; stabilizer of (a,b)
print("--- Test B2: Gamma moves on one o; Stab(a,b) ---", flush=True)
stab = []
for k in range(M):
    rot_a = tuple(a[(i + k) % M] for i in range(M))
    rot_b = tuple(b[(i + k) % M] for i in range(M))
    if rot_a == a and rot_b == b:
        stab.append(("rot", k))
rev_a = tuple(a[(-i) % M] for i in range(M))
for k in range(M):
    r_a = tuple(rev_a[(i + k) % M] for i in range(M))
    r_b = tuple(tuple(b[(-i) % M] for i in range(M))[(i + k) % M] for i in range(M))
    if r_a == a and r_b == b:
        stab.append(("rev", k))
print(f"  Stab(a,b) = {stab}", flush=True)
o0 = base[0]
gam_coll = 0
for k in [1, 12, 30, 36, 60, 90]:
    cfg = list(base)
    cfg[0] = tuple(o0[(i + k) % M] for i in range(M))
    gam_coll += (tup_multiset(b, cfg) == base_ms)
cfg = list(base)
cfg[0] = tuple(o0[(-i) % M] for i in range(M))
gam_coll += (tup_multiset(b, cfg) == base_ms)
print(f"  Gamma-moved o0 giving same fiber: {gam_coll}/7", flush=True)

# ---------- diagonal orbit size of a sample fiber row ----------
print("--- diagonal orbit size of sample row ---", flush=True)
tracked = [a, b] + base
seen_orb = set()
for k in range(M):
    seen_orb.add(tuple(tuple(s[(i + k) % M] for i in range(M)) for s in tracked))
    seen_orb.add(tuple(tuple(s[(-i - k) % M] for i in range(M)) for s in tracked))
print(f"  diagonal orbit size (tracked components): {len(seen_orb)} (max 360)", flush=True)

# ---------- 729 phases via wave-34 formula ----------
print("--- 729 orbit phases (wave-34 formula) ---", flush=True)
src = open("wave16_d1a_targeted.py").read().splitlines()
exec("\n".join(src[129:160]))
perms = gamma_perms(M)
q = 729
K = np.array(kernel_points(M, q), dtype=np.int64)
assert len(K) == q
fib = group_ids(np.sort(K, axis=1))
canon = lex_canon(K, perms)
gam = group_ids(canon)
gam_fiber = np.empty(int(gam.max()) + 1, dtype=np.int64)
gam_fiber[gam] = fib
opf = np.bincount(gam_fiber, minlength=int(fib.max()) + 1)
splits = [f for f in np.where(opf > 1)[0]]
print(f"  split fibers: {splits}, orbits: {[len(set(gam[fib == f].tolist())) for f in splits]}", flush=True)

def H_np(v):
    return 6 * v - np.roll(v, 1, axis=1) - np.roll(v, -1, axis=1)
HK = H_np(K)
assert np.all(HK % q == 0)
W = HK // q
dqm = (D // q) % q
Qv = (dqm * np.einsum("ij,ij->i", W, K)) % q
P = (dqm * (W @ K.T)) % q
u = (D // q) % q
inv_u2 = pow((u * u) % q, -1, q)
T = (inv_u2 * (2 * Qv[:, None] - P)) % q
ci = pow(D // q, -1, q)
phase_of = {}
for f in splits:
    idxf = np.where(fib == f)[0]
    for g in sorted(set(gam[idxf].tolist())):
        oo = idxf[gam[idxf] == g]
        E = np.exp(2j * np.pi * ((ci * T[:, oo]) % q) / q)
        vals = E.sum(axis=0)
        spread = float(np.abs(vals - vals[0]).max())
        phase_of[(int(f), int(g))] = (float(np.angle(vals[0])), spread, len(oo))
        print(f"  fiber {f} orbit {g}: size={len(oo)} phase={phase_of[(int(f), int(g))][0]:.6f} spread={spread:.2e}", flush=True)

# map reps b, bp to orbit ids
def orbit_id_of(seq):
    idx = int(np.where((K == np.array(seq)).all(axis=1))[0][0])
    return int(gam[idx]), int(fib[idx])
gb, fb = orbit_id_of(b)
gbp, fbp = orbit_id_of(bp)
print(f"  free pair orbits: b->(fiber {fb}, orbit {gb}), b'->(fiber {fbp}, orbit {gbp})", flush=True)
ph_b, _, sz_b = phase_of[(fb, gb)]
ph_bp, _, sz_bp = phase_of[(fbp, gbp)]
import cmath
dth = abs((ph_b - ph_bp + math.pi) % (2 * math.pi) - math.pi)
print(f"  phase gap theta = {dth:.6f} rad; orbit sizes {sz_b}, {sz_bp}", flush=True)
dmin = 2 * sz_b * sz_bp * (1 - math.cos(dth))
print(f"  Delta_F lower bound per fiber: 2*{sz_b}*{sz_bp}*(1-cos theta) = {dmin:.1f}", flush=True)
B180 = 49 * 121 * 361 * 841 * 1681 * 3481 * 72361
print(f"  B(180) = {B180} = {B180:.3e}; 180^9 = {180**9:.3e}; 180^10 = {180**10:.3e}", flush=True)
print(f"  realized-total lower bound (one section): B(180)*Delta_min = {B180 * dmin:.3e}", flush=True)
print("WAVE39 SCJ DIRECT DONE", flush=True)
