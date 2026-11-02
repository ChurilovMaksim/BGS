"""Wave 47x, task D — probe for the j=13 ladder prediction.

j=13: m = p = 8192, Q = 2^29, STEP0 = 8192.
Grid: t odd in [1,65536), u = (11t + 16*U0) mod 65536, U0 in [0,4096).
Prediction: exactly two step-64 chains of 8 per point, each +-16;
t-equality <=> E + 28*delta_E == 0 (mod 32), chains = ordinals
c+16a and c+8+16a (a<8) for the residue c mod 8 satisfying the cond.
"""
import random

Q = 1 << 29
MASK = Q - 1
STEP0 = 8192
P = 8192
PJ = 512   # p/16
QQ = 1024  # p/8
MU = Q // 256  # 2^21: at j=13 the shift-8 digit is mod 256, not mod 128


def check_point(t, U0):
    u = (11 * t + 16 * U0) % 65536
    y_prev, y_curr = STEP0 * t, STEP0 * u
    y0, y1 = y_prev, y_curr
    W = {0: y_curr}
    s = {}
    # after iteration nn, y_curr = y_{nn+1}; capture W[m] = y_{2m+1} for m < 2048
    for nn in range(1, P + 2):
        y_next = (6 * y_curr - y_prev) & MASK
        y_prev, y_curr = y_curr, y_next
        if nn % 2 == 0 and nn // 2 < 2048:
            W[nn // 2] = y_curr
        if nn + 1 in (4096, 4097, 8192, 8193):
            s[nn + 1] = y_curr
    per_ok = (s[8192] == y0) and (s[8193] == y1)
    min_ok = not ((s[4096] == y0) and (s[4097] == y1))
    nu_ok = ((s[4096] - y0) & MASK == Q // 2) and ((s[4097] - y1) & MASK == 0)
    if not (per_ok and min_ok and nu_ok):
        return ("invalid", per_ok, min_ok, nu_ok)
    E, eps, phi, vv, tt = [], [], [], [], []
    for j in range(PJ):
        diff = (W[j + 8] - W[j]) & MASK
        assert diff % MU == 0
        E.append(diff // MU)
        de = (W[j + QQ] - W[j]) & MASK
        assert de % (Q // 2) == 0
        eps.append(de // (Q // 2))
        dp = (W[j + PJ] - W[j]) & MASK
        assert dp % (Q // 4) == 0
        phi.append((dp // (Q // 4)) % 4)
        vv.append(W[j] % (Q // 2))
        tt.append(W[j] // (Q // 2))
        assert E[j] % 4 == phi[j] % 4, "B2"
    reps = [j for j in range(PJ) if eps[j] == 0 and phi[j] == 0]
    assert len(reps) == 128, f"reps {len(reps)}"
    assert all(reps[i + 1] - reps[i] == 4 for i in range(127)), "spacing"
    d = (E[reps[1]] - E[reps[0]]) % 256
    assert all((E[reps[i + 1]] - E[reps[i]]) % 256 == d for i in range(127)), "AP"
    assert d % 4 == 0, "diff4"
    dE = (d // 4) % 64
    assert dE % 2 == 1, "delta odd"
    assert all(E[r] % 4 == 0 for r in reps), "E mod4"
    # classes by vv
    classes = {}
    for i, r in enumerate(reps):
        classes.setdefault(vv[r], []).append(i)
    contribs = {}
    for v, members in classes.items():
        contribs[v] = sum(2 * (1 - 2 * tt[reps[i]]) for i in members)
    # cond64 chains
    dE8 = dE % 8
    chains = []
    for c in range(8):
        if (E[reps[c]] + 28 * dE8) % 32 != 0:
            continue
        for base in (c, c + 8):
            members = [base + 16 * a for a in range(8)]
            chains.append(members)
    assert len(chains) == 2, f"chains {len(chains)}"
    for members in chains:
        vs = {vv[reps[i]] for i in members}
        assert len(vs) == 1, "chain not one class"
        cl = classes[vs.pop()]
        assert sorted(cl) == sorted(members), "chain not exactly a class"
        ts = {tt[reps[i]] for i in members}
        assert len(ts) == 1, "chain t not constant"
        ssum = sum(2 * (1 - 2 * tt[reps[i]]) for i in members)
        assert abs(ssum) == 16, f"chain contrib {ssum}"
    nonzero = [v for v, ssum in contribs.items() if ssum != 0]
    assert len(nonzero) == 2, f"nonzero {len(nonzero)}"
    chain_vs = []
    for members in chains:
        chain_vs.append(vv[reps[members[0]]])
    assert sorted(chain_vs) == sorted(nonzero), "nonzero != chains"
    wit = sum(1 for i in range(128) if (E[reps[i]] + 4 * (dE % 32)) % 128 == 0)
    share = sum(1 for i in range(128) if (E[reps[i]] + 4 * (dE % 32)) % 128 % 64 == 0)
    signs = tuple(sorted(1 if sum(2 * (1 - 2 * tt[reps[i]]) for i in m) > 0 else -1
                         for m in chains))
    return ("ok", wit, share, signs, sorted(len(m) for m in classes.values()))


random.seed(13)
points = [(1, 0), (1, 4095), (3, 0), (65535, 4095), (32769, 2048)]
points += [(2 * random.randrange(32768) + 1, random.randrange(4096)) for _ in range(195)]
bad = 0
for (t, U0) in points:
    r = check_point(t, U0)
    if r[0] != "ok":
        bad += 1
        print("FAIL", t, U0, r)
print(f"probe: {len(points) - bad}/{len(points)} ok")
if bad == 0:
    # print anatomy of first point
    print("sample anatomy:", check_point(1, 0))
print("DONE")
