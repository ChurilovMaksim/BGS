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

def tr(a, M):
    return (2*a[0]) % M

def genuine(M, m):
    d = pw(ALPHA, m, M)
    d = ((d[0]-1) % M, d[1])
    return [(x, y) for x in range(M) for y in range(M) if mul(d, (x, y), M) == (0, 0)]

def perms_of(t):
    return [tuple((eps*r + b) % t for r in range(t)) for eps in (1, -1) for b in range(t)]

def run_pairing(m, q2, q, cap_groups=None):
    """Step-2 test: group by per-class marginals up to common pi; check joints."""
    t = math.gcd(m, 4)
    S = m // t
    G2, Gq = genuine(q2, m), genuine(q, m)
    perms = perms_of(t)
    print(f"--- pairing test m={m} (q2,q)=({q2},{q}): |G2|={len(G2)} |Gq|={len(Gq)} "
          f"params={len(G2)*len(Gq)}", flush=True)

    def data(a2, aq):
        # seq[i] = (tr mod q2, tr mod q)
        s = []
        b2, bq = a2, aq
        for i in range(m):
            s.append((tr(b2, q2), tr(bq, q)))
            b2 = mul(b2, ALPHA, q2)
            bq = mul(bq, ALPHA, q)
        marg, joint = [], []
        for r in range(t):
            cls = [s[r + t*k] for k in range(S)]
            marg.append((tuple(sorted(x[0] for x in cls)), tuple(sorted(x[1] for x in cls))))
            joint.append(tuple(sorted(cls)))
        return tuple(marg), tuple(joint)

    groups = defaultdict(list)
    for a2 in G2:
        for aq in Gq:
            marg, joint = data(a2, aq)
            # canonical key: min over pi of pi-permuted marginal signature
            key = min(tuple(marg[p[r]] for r in range(t)) for p in perms)
            groups[key].append((a2, aq, marg, joint))
    multi = [g for g in groups.values() if len(g) > 1]
    print(f"    marginal-groups={len(groups)} multi-groups={len(multi)} "
          f"maxsize={max(len(g) for g in groups.values())}", flush=True)
    n_same_pi = n_diff_pi = n_no_joint = 0
    bad_examples = []
    for g in multi:
        for i in range(len(g)):
            for j in range(i+1, len(g)):
                _, _, m0, j0 = g[i]
                _, _, m1, j1 = g[j]
                marg_pis = [p for p in perms if all(m1[r] == m0[p[r]] for r in range(t))]
                joint_pis = [p for p in perms if all(j1[r] == j0[p[r]] for r in range(t))]
                if not joint_pis:
                    n_no_joint += 1
                    if len(bad_examples) < 3:
                        bad_examples.append(("NO-JOINT", g[i][:2], g[j][:2], marg_pis))
                elif set(marg_pis) & set(joint_pis):
                    n_same_pi += 1
                else:
                    n_diff_pi += 1
                    if len(bad_examples) < 3:
                        bad_examples.append(("DIFF-PI", g[i][:2], g[j][:2], marg_pis, joint_pis))
    print(f"    pairs: same-pi={n_same_pi} diff-pi-only={n_diff_pi} no-joint-pi={n_no_joint}",
          flush=True)
    for e in bad_examples:
        print("    EXAMPLE:", e, flush=True)
    return n_same_pi, n_diff_pi, n_no_joint

def run_jbl(m, q2, q):
    """Two-component JBL test at new m: group by joint global multiset, check joint pi."""
    t = math.gcd(m, 4)
    S = m // t
    G2, Gq = genuine(q2, m), genuine(q, m)
    perms = perms_of(t)
    print(f"--- JBL test m={m} (q2,q)=({q2},{q}): params={len(G2)*len(Gq)}", flush=True)
    groups = defaultdict(list)
    for a2 in G2:
        for aq in Gq:
            s = []
            b2, bq = a2, aq
            for i in range(m):
                s.append((tr(b2, q2), tr(bq, q)))
                b2 = mul(b2, ALPHA, q2)
                bq = mul(bq, ALPHA, q)
            sig = []
            for r in range(t):
                sig.append(tuple(sorted(s[r + t*k] for k in range(S))))
            groups[tuple(sorted(s))].append((a2, aq, tuple(sig)))
    multi = [g for g in groups.values() if len(g) > 1]
    print(f"    global-groups={len(groups)} multi-groups={len(multi)}", flush=True)
    bad = 0
    for g in multi:
        s0 = g[0][2]
        for A in g[1:]:
            if not any(all(A[2][r] == s0[p[r]] for r in range(t)) for p in perms):
                bad += 1
                if bad <= 3:
                    print("    JBL-BAD:", g[0][:2], A[:2], flush=True)
    print(f"    JBL-bad pairs={bad}", flush=True)
    return bad

run_pairing(8, 512, 9)
run_pairing(8, 512, 289)
run_jbl(16, 2048, 9)
