"""Wave 13, task 2 (retry): Lemma PC for m=6, p1=5, p2=7, independent check.

Independent re-implementation (does not import wave12 code):
enumerate ALL recurrence sequences mod 5 and mod 7, ALL (d1,d2) in
D_6 x D_6, and for every pair-multiset-preserving case compute
Pi1, Pi2 exactly (t = gcd(6,4) = 2, D_2 = {id, swap}).
Also tabulate the structure of preserved cases: signs, shifts,
and the class map c(d) (id if k even, swap if k odd).
"""
import math
from collections import Counter

M = 6
P1, P2 = 5, 7
T = math.gcd(M, 4)  # 2


def rec_seqs(p):
    out = []
    for y0 in range(p):
        for y1 in range(p):
            s = [y0, y1]
            for _ in range(2, M):
                s.append((6 * s[-1] - s[-2]) % p)
            assert (6 * s[-1] - s[-2]) % p == s[0], "periodicity fails"
            out.append(tuple(s))
    return out


def d_ops():
    ops = []
    for k in range(M):
        ops.append((+1, k, tuple((j + k) % M for j in range(M))))
        ops.append((-1, k, tuple((-j + k) % M for j in range(M))))
    return ops


def pi_set(seq, dseq):
    cls = [[i for i in range(M) if i % T == r] for r in range(T)]
    pc = [tuple(sorted(seq[i] for i in idx)) for idx in cls]
    pc_d = [tuple(sorted(dseq[i] for i in idx)) for idx in cls]
    res = []
    # D_2 = {id, swap}; pi as tuple with pc_d[r] == pc[pi[r]]
    for pi in [(0, 1), (1, 0)]:
        if all(pc_d[r] == pc[pi[r]] for r in range(T)):
            res.append("id" if pi == (0, 1) else "swap")
    return res


def main():
    A = rec_seqs(P1)
    B = rec_seqs(P2)
    ops = d_ops()
    preserved = 0
    bad = []
    # structure counters over preserved cases
    sign_pairs = Counter()
    shift_rel = Counter()
    cmap_rel = Counter()
    pi_shapes = Counter()
    for a in A:
        for b in B:
            orig = tuple(sorted(zip(a, b)))
            for e1, k1, d1 in ops:
                a_d = tuple(a[d1[j]] for j in range(M))
                for e2, k2, d2 in ops:
                    if tuple(sorted((a_d[j], b[d2[j]]) for j in range(M))) != orig:
                        continue
                    preserved += 1
                    b_d = tuple(b[d2[j]] for j in range(M))
                    pi1 = pi_set(a, a_d)
                    pi2 = pi_set(b, b_d)
                    if not (set(pi1) & set(pi2)):
                        bad.append((a, b, (e1, k1), (e2, k2), pi1, pi2))
                    sign_pairs[(e1, e2)] += 1
                    shift_rel[(k1 - k2) % 3] += 1
                    c1 = "id" if k1 % 2 == 0 else "swap"
                    c2 = "id" if k2 % 2 == 0 else "swap"
                    cmap_rel[(c1, c2)] += 1
                    pi_shapes[(tuple(pi1), tuple(pi2))] += 1
    print(f"pairs={len(A) * len(B)} preserved={preserved} BAD={len(bad)}")
    print("sign_pairs (e1,e2):", dict(sign_pairs))
    print("shift_rel (k1-k2) mod 3:", dict(shift_rel))
    print("cmap (c1,c2):", dict(cmap_rel))
    print("pi_shapes (Pi1,Pi2):", dict(pi_shapes))
    for x in bad[:5]:
        print("BAD:", x)
    assert not bad


if __name__ == "__main__":
    main()
