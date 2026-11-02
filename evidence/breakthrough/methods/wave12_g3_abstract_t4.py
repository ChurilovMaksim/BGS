"""Wave 12, task 4 (G3): abstract search, t=4, D4 perms.
Values are types (r1,r2) in {0,1}^2. Random C,C' with same column sums
(class sizes equal, here 3 per class, m=12 shape), Pi_q = perms in D4
matching aggregated rows by r1 resp. r2. Look for disjoint Pi sets.
"""
import random, itertools

def d4_perms():
    out = []
    for b in range(4):
        out.append(tuple((i+b) % 4 for i in range(4)))
        out.append(tuple((-i+b) % 4 for i in range(4)))
    return list(dict.fromkeys(out))
PERMS = d4_perms()

def pi_set(C, Cp, bit):
    def agg(M):
        out = [[0,0] for _ in range(4)]
        for r in range(4):
            for typ in range(4):
                b = typ//2 if bit == 0 else typ % 2
                out[r][b] += M[r][typ]
        return out
    A, Ap = agg(C), agg(Cp)
    pis = []
    for pi in PERMS:
        if all(Ap[r] == A[pi[r]] for r in range(4)):
            pis.append(pi)
    return pis

random.seed(1)
for trial in range(200000):
    # random C: 4 classes x 4 types, each class total 3
    C = []
    for r in range(4):
        row = [0]*4
        for _ in range(3):
            row[random.randrange(4)] += 1
        C.append(row)
    totals = [sum(C[r][t] for r in range(4)) for t in range(4)]
    # random C' with same column sums and class totals 3
    Cp = [[0]*4 for _ in range(4)]
    ok = True
    for t in range(4):
        # distribute totals[t] balls into 4 classes with capacity left
        rem = totals[t]
        order = list(range(4)); random.shuffle(order)
        for r in order:
            cap = 3 - sum(Cp[r])
            take = random.randint(0, min(rem, cap))
            Cp[r][t] = take; rem -= take
        if rem != 0: ok = False; break
    if not ok: continue
    if any(sum(row) != 3 for row in Cp): continue
    if Cp == C: continue
    p1 = pi_set(C, Cp, 0); p2 = pi_set(C, Cp, 1)
    if p1 and p2 and not (set(p1) & set(p2)):
        print("FOUND t=4 abstract obstruction, trial", trial)
        print("  C =", C); print("  C'=", Cp)
        print("  Pi_q1 =", p1); print("  Pi_q2 =", p2)
        break
else:
    print("no t=4 abstract obstruction in 200000 random trials")
