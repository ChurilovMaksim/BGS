"""Wave 42, task 5 (m=252): 729 phases (wave-34 formula), Test A full-tuple
collision, diagonal orbit sizes, sampled distinctness, double-(a,b) swap
test, section total. Requires wave42_ab.pkl and wave42_samples.npz.
"""
import sys, math, pickle
from collections import defaultdict
import numpy as np
sys.path.insert(0, ".")
exec(open("wave38_blind_explore.py").read().split("m = 60")[0])
src = open("wave16_d1a_targeted.py").read().splitlines()
exec("\n".join(src[129:160]))  # gamma_perms, lex_canon, group_ids

M = 252

def D(m):
    e0, e1 = 2, 6
    for _ in range(2, m + 1):
        e0, e1 = e1, 6 * e1 - e0
    return e1 - 2

D252 = D(252)
d = pickle.load(open("wave42_ab.pkl", "rb"))
a, b, bp = d["a"], d["b"], d["bp"]

# --- 1. fiber-15 phase mapping ---
q = 729
K = np.array(kernel_points(M, q), dtype=np.int64)
fib = group_ids(np.sort(K, axis=1))
perms = gamma_perms(M)
gam = group_ids(lex_canon(K, perms))

def H_np(v):
    return 6 * v - np.roll(v, 1, axis=1) - np.roll(v, -1, axis=1)

HK = H_np(K)
W = HK // q
dqm = (D252 // q) % q
Qv = (dqm * np.einsum("ij,ij->i", W, K)) % q
P = (dqm * (W @ K.T)) % q
u = (D252 // q) % q
inv_u2 = pow((u * u) % q, -1, q)
T = (inv_u2 * (2 * Qv[:, None] - P)) % q
ci = pow(D252 // q, -1, q)
sf729 = split_fibers(M, 729)
for r in sf729[1][1]:
    idx = int(np.where((K == np.array(r)).all(axis=1))[0][0])
    g, f = int(gam[idx]), int(fib[idx])
    oo = np.where((fib == f) & (gam == g))[0]
    E = np.exp(2j * np.pi * ((ci * T[:, oo]) % q) / q)
    vals = E.sum(axis=0)
    print(f"fiber-15 rep C={recover_C(r, 729)} -> orbit {g}, size {len(oo)}, "
          f"phase {float(np.angle(vals[0])):.6f}", flush=True)

# --- samples / configs ---
S = np.load("wave42_samples.npz")
Q0S = [25, 121, 6889, 12769, 28561, 57121, 63001, 113569]
samp = {qq: [tuple(row) for row in S[f"q{qq}"]] for qq in Q0S}
rng = np.random.default_rng(7)

def rand_config():
    return [samp[qq][int(rng.integers(0, len(samp[qq])))] for qq in Q0S]

def tup_ms(free, cfg):
    return tuple(sorted(zip(a, free, *cfg)))

# --- 2. Test A: full-tuple collision, 100 configs ---
nA = 0
for _ in range(100):
    cfg = rand_config()
    nA += (tup_ms(b, cfg) == tup_ms(bp, cfg))
print(f"Test A full-tuple collisions: {nA}/100", flush=True)

# --- 3. diagonal orbit sizes, one config ---
cfg = rand_config()
for free, name in [(b, "b"), (bp, "bp")]:
    tracked = [a, free] + cfg
    seen = set()
    for k in range(M):
        seen.add(tuple(tuple(s[(i + k) % M] for i in range(M)) for s in tracked))
        seen.add(tuple(tuple(s[(-i - k) % M] for i in range(M)) for s in tracked))
    print(f"diagonal orbit size ({name}): {len(seen)} (max 504)", flush=True)

# --- 4. sampled distinctness ---
base = rand_config()
base_ms = tup_ms(b, base)
nd_all = nd_one = 0
for _ in range(30):
    nd_all += (tup_ms(b, rand_config()) != base_ms)
for _ in range(30):
    cfg = list(base)
    j = int(rng.integers(0, len(Q0S)))
    alt = [s for s in samp[Q0S[j]] if s != base[j]]
    cfg[j] = alt[int(rng.integers(0, len(alt)))]
    nd_one += (tup_ms(b, cfg) != base_ms)
print(f"distinctness: differ-at-all {nd_all}/30, differ-at-one {nd_one}/30", flush=True)

# --- 5. swap test: double (a,b) pairs ---
pos = defaultdict(list)
for i, p in enumerate(zip(a, b)):
    pos[p].append(i)
doubles = [v for v in pos.values() if len(v) > 1]
print(f"double pairs: {len(doubles)}", flush=True)

def mat_pow2(Mm, e, qq):
    def mul(X, Y):
        return [(X[0] * Y[0] + X[1] * Y[2]) % qq, (X[0] * Y[1] + X[1] * Y[3]) % qq,
                (X[2] * Y[0] + X[3] * Y[2]) % qq, (X[2] * Y[1] + X[3] * Y[3]) % qq]
    R = [1, 0, 0, 1]
    B = Mm[:]
    while e:
        if e & 1:
            R = mul(R, B)
        B = mul(B, B)
        e >>= 1
    return R

def is_kernel(seq, qq):
    for k in range(M):
        if (6 * seq[k] - seq[k - 1]) % qq != seq[(k + 1) % M] % qq:
            return False
    Mm = mat_pow2([6, qq - 1, 1, 0], M, qq)
    y0, y1 = seq[0], seq[1]
    return ((Mm[0] * y0 + Mm[1] * y1) % qq == y0 and
            (Mm[2] * y0 + Mm[3] * y1) % qq == y1)

hits = 0
tested = 0
for t in range(200):
    cfg = rand_config()
    for (i, j) in doubles:
        sw = []
        ok = True
        for c, qq in enumerate(Q0S):
            o = list(cfg[c])
            if o[i] == o[j]:
                sw.append(tuple(o))
                continue
            o[i], o[j] = o[j], o[i]
            if not is_kernel(tuple(o), qq):
                ok = False
                break
            sw.append(tuple(o))
        if not ok:
            continue
        tested += 1
        if tuple(sw) != tuple(cfg):
            hits += 1
            print(f"  SWAP HIT config {t} positions {i},{j}", flush=True)
print(f"swap test: {tested} valid swaps examined, {hits} nontrivial "
      f"kernel-preserving swaps", flush=True)

# --- 6. section total ---
Bconf = 1
for qq in Q0S:
    Bconf *= qq
dmin = 2 * 504 * 504 * (1 - math.cos(2 * math.pi / 3))
total = Bconf * dmin
print(f"B_conf = {Bconf} (~10^{math.log10(Bconf):.2f})")
print(f"section total >= {total:.3e}; log10 = {math.log10(total):.2f}; "
      f"(1/3)log10(D252) = {math.log10(D252) / 3:.2f}; log10(D252) = {math.log10(D252):.2f}")
cj = 0
while 252 ** (cj + 1) < total:
    cj += 1
print(f"kills c_J <= {cj} (252^{cj} = {252 ** cj:.2e} < total <= 252^{cj + 1})")
print("WAVE42 PHASES DISTINCT DONE", flush=True)
