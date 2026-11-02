"""Wave 12, task 4 (G3): pair-contingency test (mod p).

Let a (mod p1), b (mod p2) be recurrence sequences of length m
(all (y0,y1) mod p, since alpha^m = 1 mod p for odd p | D_m).
Let d1,d2 in D_m (shifts/reflections on indices). Suppose the pair
multiset {(a_{d1(j)}, b_{d2(j)})} equals {(a_j, b_j)}.
Let Pi1 = {pi in D_t : per-class multisets of d1(a) match a via pi},
Pi2 likewise for b. Question: is Pi1 cap Pi2 always nonempty?
A 'no' here would be a mod-p counterexample to G3 for arbitrary
recurrence pairs (not yet a Fix-mod-D counterexample, since mod-p
sequences need not lift to mod p^e Fix sequences).
"""
import itertools, math, sys

def rec_seqs(m, p):
    out = []
    for y0 in range(p):
        for y1 in range(p):
            s = [y0, y1] if m > 1 else [y0]
            for i in range(2, m):
                s.append((6*s[-1] - s[-2]) % p)
            # period check (should hold for p | D_m; assert for the cases used)
            if m >= 2:
                nxt = (6*s[-1] - s[-2]) % p
                nxt2 = (6*nxt - s[-1]) % p
                assert nxt == s[0] and nxt2 == s[1], f"not periodic m={m} p={p} seq={s}"
            out.append(tuple(s))
    return out

def d_ops(m):
    ops = []
    for k in range(m):
        ops.append(('shift', k, tuple((j+k) % m for j in range(m))))
        ops.append(('refl', k, tuple((-j+k) % m for j in range(m))))
    return ops

def d_t_perms(t):
    out = []
    for b in range(t):
        out.append(tuple((i+b) % t for i in range(t)))
        out.append(tuple((-i+b) % t for i in range(t)))
    return list(dict.fromkeys(out))

def pi_set(seq, dseq, m, t, perms):
    cls = [[i for i in range(m) if i % t == r] for r in range(t)]
    pc = [tuple(sorted(seq[i] for i in idx)) for idx in cls]
    pc_d = [tuple(sorted(dseq[i] for i in idx)) for idx in cls]
    return [pi for pi in perms if all(pc_d[r] == pc[pi[r]] for r in range(t))]

def test(m, p1, p2):
    A = rec_seqs(m, p1); B = rec_seqs(m, p2)
    ops = d_ops(m)
    t = math.gcd(m, 4); perms = d_t_perms(t)
    total_preserved = 0; bad = []
    for a in A:
        for b in B:
            orig = tuple(sorted(zip(a, b)))
            for _, _, d1 in ops:
                a_d = tuple(a[d1[j]] for j in range(m))
                # quick: per-component multisets must match (they do for d, since d permutes)
                for _, _, d2 in ops:
                    pair_d = tuple(sorted((a_d[j], b[d2[j]]) for j in range(m)))
                    if pair_d != orig: continue
                    total_preserved += 1
                    b_d = tuple(b[d2[j]] for j in range(m))
                    pi1 = pi_set(a, a_d, m, t, perms)
                    pi2 = pi_set(b, b_d, m, t, perms)
                    if not (set(pi1) & set(pi2)):
                        bad.append((a, b, d1, d2, pi1, pi2))
                        print(f"  BAD m={m} p1={p1} p2={p2} a={a} b={b} d1={d1} d2={d2} Pi1={pi1} Pi2={pi2}", flush=True)
                        if len(bad) >= 3: return total_preserved, bad
    print(f"m={m} p1={p1} p2={p2}: pairs={len(A)*len(B)} preserved={total_preserved} BAD={len(bad)}", flush=True)
    return total_preserved, bad

if __name__ == "__main__":
    test(6, 5, 7)
