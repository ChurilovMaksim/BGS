"""Wave 15, task 2: Lemma PC for (m, p1, p2) = (12, 5, 7) — exact check.

Mirrors wave12_g3_pair_contingency.py, plus the structural checks of the
proof: every mod-7 recurrence sequence is 3-periodic, every class
multiset equals the same W, and Pi2 is the full D4 for every (b, d2).
"""
import math

def rec_seqs(m, p):
    out = []
    for y0 in range(p):
        for y1 in range(p):
            s = [y0, y1]
            for _ in range(2, m):
                s.append((6 * s[-1] - s[-2]) % p)
            nxt = (6 * s[-1] - s[-2]) % p
            nxt2 = (6 * nxt - s[-1]) % p
            assert nxt == s[0] and nxt2 == s[1]
            out.append(tuple(s))
    return out

def d_ops(m):
    ops = []
    for k in range(m):
        ops.append(tuple((j + k) % m for j in range(m)))
        ops.append(tuple((-j + k) % m for j in range(m)))
    return ops

def d_t_perms(t):
    out = []
    for b in range(t):
        out.append(tuple((i + b) % t for i in range(t)))
        out.append(tuple((-i + b) % t for i in range(t)))
    return list(dict.fromkeys(out))

def pi_set(seq, dseq, m, t, perms):
    cls = [[i for i in range(m) if i % t == r] for r in range(t)]
    pc = [tuple(sorted(seq[i] for i in idx)) for idx in cls]
    pc_d = [tuple(sorted(dseq[i] for i in idx)) for idx in cls]
    return [pi for pi in perms if all(pc_d[r] == pc[pi[r]] for r in range(t))]

m, p1, p2 = 12, 5, 7
t = math.gcd(m, 4)
A, B = rec_seqs(m, p1), rec_seqs(m, p2)
ops, perms = d_ops(m), d_t_perms(t)
print(f"seqs: |A|={len(A)} |B|={len(B)} t={t} |D_m|={len(ops)} |D_t|={len(perms)}")

# Structural checks (the proof): 3-periodicity mod 7, constant class
# multisets mod 7, Pi2 full for every (b, d2).
for b in B:
    assert all(b[(j + 3) % m] == b[j] for j in range(m)), b
    cls = [tuple(sorted(b[i] for i in range(m) if i % t == r)) for r in range(t)]
    assert len(set(cls)) == 1, (b, cls)
for b in B:
    for d2 in ops:
        b_d = tuple(b[d2[j]] for j in range(m))
        assert pi_set(b, b_d, m, t, perms) == perms, (b, d2)
print("structural: all mod-7 seqs 3-periodic, all class multisets equal, Pi2 = D4 always")

preserved = 0
bad = 0
for a in A:
    for b in B:
        orig = tuple(sorted(zip(a, b)))
        for d1 in ops:
            a_d = tuple(a[d1[j]] for j in range(m))
            for d2 in ops:
                pair_d = tuple(sorted((a_d[j], b[d2[j]]) for j in range(m)))
                if pair_d != orig:
                    continue
                preserved += 1
                b_d = tuple(b[d2[j]] for j in range(m))
                pi1 = pi_set(a, a_d, m, t, perms)
                pi2 = pi_set(b, b_d, m, t, perms)
                if not (set(pi1) & set(pi2)):
                    bad += 1
                    print("BAD", a, b, d1, d2, pi1, pi2)
print(f"m=12 p1=5 p2=7: pairs={len(A)*len(B)} preserved={preserved} BAD={bad}")
assert preserved == 318528 and bad == 0
print("PASS: reproduces wave-12 count exactly, 0 bad")
