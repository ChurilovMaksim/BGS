"""Wave 42, task 5 (background): full 84-periodicity + direct-collision check
for ALL kernel sequences at q0 = 21743569 = 4663^2, m = 252.

Seed solve via the k-congruence (avoids the dense (n0, g) array):
  eq1: a*y1 + b*y0 = 0 -> y1 = y1_0 + k*step (step = q//g)
  eq2: c*y1 + d*y0 = 0 -> k*A2 = -B2 (mod q), A2 = (c*step) % q
Collision test vectorized: combined = key*729 + bval, sort rows, compare.
No split-ness (needs global fiber grouping; sampled separately if needed).
"""
import math, json, pickle
import numpy as np

M = 252
Q = 21743569
d = pickle.load(open("wave42_ab.pkl", "rb"))
A_ARR = np.array(d["a"], dtype=np.int64)
B_ARR = np.array(d["b"], dtype=np.int64)
BP_ARR = np.array(d["bp"], dtype=np.int64)

def mat_pow(Mm, e, q):
    def mul(X, Y):
        return [(X[0]*Y[0]+X[1]*Y[2]) % q, (X[0]*Y[1]+X[1]*Y[3]) % q,
                (X[2]*Y[0]+X[3]*Y[2]) % q, (X[2]*Y[1]+X[3]*Y[3]) % q]
    R = [1, 0, 0, 1]; B = Mm[:]
    while e:
        if e & 1: R = mul(R, B)
        B = mul(B, B); e >>= 1
    return R

Mm = mat_pow([6, Q - 1, 1, 0], M, Q)
a = (Mm[0] - 1) % Q; b = Mm[1] % Q; c = Mm[2] % Q; dd = (Mm[3] - 1) % Q
g = math.gcd(a, Q)
print(f"a={a} b={b} c={c} d={dd} g={g}", flush=True)
# rank mod 4663 (kernel-size sanity: rank 1 mod p + det 0 mod q -> |ker| = q)
p = 4663
Mm_p = [x % p for x in Mm]
print(f"M^252-I mod {p}: a={Mm_p[0]-1 if Mm_p[0]>0 else p-1} b={Mm_p[1]} c={Mm_p[2]} d={Mm_p[3]-1 if Mm_p[3]>0 else p-1}",
      flush=True)
print(f"det check: D_252 % Q should be 0 (verified via D84 divisibility); entries mod p nonzero: "
      f"{any(x % p != 0 for x in [a, b, c, dd])}", flush=True)

a1, q1 = a // g, Q // g
inv_a1 = pow(a1, -1, q1) if q1 > 1 else 0
step = Q // g
A2 = (c * step) % Q
gg2 = math.gcd(A2, Q) if A2 != 0 else Q
inv_A2 = pow(A2 // gg2, -1, Q // gg2) if gg2 < Q else 0
q_red = Q // gg2
print(f"step={step} A2={A2} gg2={gg2} q_red={q_red}", flush=True)

CH = 200000
nseeds = 0; n_nonzero = 0; per_fail = 0; col_fail = 0
for st in range(0, Q, CH):
    y0 = np.arange(st, min(st + CH, Q), dtype=np.int64)
    rhs = ((-(b * y0) // g) % q1) if q1 > 1 else np.zeros(len(y0), dtype=np.int64)
    y1_0 = (inv_a1 * rhs) % q1 if q1 > 1 else np.zeros(len(y0), dtype=np.int64)
    B2 = (c * y1_0 + dd * y0) % Q
    valid = (B2 % gg2 == 0)
    y0v = y0[valid]; y1_0v = y1_0[valid]; B2v = B2[valid]
    if len(y0v) == 0:
        continue
    if gg2 < Q:
        k0 = ((-(B2v // gg2)) * inv_A2) % q_red
    else:
        k0 = np.zeros(len(y0v), dtype=np.int64)
    # k values: k0 + t*q_red < g
    ks = []
    for t in range(0, g, 1):
        kk = k0 + t * q_red
        if np.all(kk >= g):
            break
        ks.append(kk)
    if not ks:
        continue
    K = np.stack(ks, axis=1)  # (nvalid, n_t)
    Y0 = np.repeat(y0v[:, None], K.shape[1], axis=1)
    Y1 = y1_0v[:, None] + step * K
    mask = Y1 < g * 0 + Q  # all candidates < q by construction (y1_0<q1, k<g)
    Y0f = Y0.reshape(-1); Y1f = Y1.reshape(-1)
    # drop duplicates / out-of-range (k0+t*q_red may exceed g-1 for large t)
    keep = (K.reshape(-1) < g)
    Y0f, Y1f = Y0f[keep], Y1f[keep]
    # verify both equations on the fly (cheap, vectorized)
    assert np.all((a * Y1f + b * Y0f) % Q == 0)
    assert np.all((c * Y1f + dd * Y0f) % Q == 0)
    Y = np.empty((len(Y0f), M), dtype=np.int64)
    Y[:, 0] = Y0f; Y[:, 1] = Y1f
    for i in range(2, M):
        Y[:, i] = (6 * Y[:, i - 1] - Y[:, i - 2]) % Q
    nz = np.any(Y != 0, axis=1)
    Yn = Y[nz]
    nseeds += len(Y0f); n_nonzero += len(Yn)
    per_fail += int(np.sum(~np.all(Yn[:, :168] == Yn[:, 84:], axis=1)))
    key = A_ARR[None, :] * Q + Yn
    cb = np.sort(key * 729 + B_ARR[None, :], axis=1)
    cbp = np.sort(key * 729 + BP_ARR[None, :], axis=1)
    col_fail += int(np.sum(np.any(cb != cbp, axis=1)))
    if (st // CH) % 20 == 0:
        print(f"  y0 up to {st+CH}: seeds={nseeds} per_fail={per_fail} col_fail={col_fail}", flush=True)

print(json.dumps({"q": Q, "seeds": nseeds, "nonzero": n_nonzero,
                  "per84_fail": per_fail, "col_fail": col_fail}), flush=True)
print("BIG21743569 DONE", flush=True)
