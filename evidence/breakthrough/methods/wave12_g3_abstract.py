"""Wave 12, task 4 (G3): abstract search for a common-pi obstruction.

t=2 classes, D_2 = {id, swap}. Values are types (r1, r2) in {0,1}^2:
r1 = residue mod component q1, r2 = residue mod component q2.
C[r][type] = count in class r of y; C'[r][type] = same for y'.
Same column sums <=> same global multiset <=> some sigma exists.
Pi_q1 = {pi : aggregated rows by r1 match}, similarly q2.
Goal: Pi_q1 = {swap} only, Pi_q2 = {id} only (disjoint).
"""
import itertools

def pi_set(C, Cp, bit):
    # aggregate by bit: bit=0 -> first coord, bit=1 -> second coord
    def agg(M):
        out = [[0,0],[0,0]]  # [class][bitval]
        for r in range(2):
            for typ in range(4):
                b = (typ >> (1-bit)) & 1 if bit==0 else (typ & 1)
                # type encoding: typ = r1*2 + r2
                if bit==0: b = typ//2
                else: b = typ%2
                out[r][b] += M[r][typ]
        return out
    A, Ap = agg(C), agg(Cp)
    pis = []
    if Ap == A: pis.append('id')
    if [Ap[1], Ap[0]] == A: pis.append('swap')
    return pis

found = []
# C entries 0..2
for flat in itertools.product(range(3), repeat=8):
    C = [flat[0:4], flat[4:8]]
    totals = [C[0][t]+C[1][t] for t in range(4)]
    if sum(totals)==0: continue
    # C'0[t] in 0..totals[t]
    for c0 in itertools.product(*[range(t+1) for t in totals]):
        Cp = [list(c0), [totals[t]-c0[t] for t in range(4)]]
        if Cp == C: continue
        p1 = pi_set(C, Cp, 0)
        p2 = pi_set(C, Cp, 1)
        if p1 == ['swap'] and p2 == ['id']:
            found.append((C, Cp))
            print("FOUND t=2 abstract obstruction:")
            print("  C =", C)
            print("  C'=", Cp)
            print("  Pi_q1 =", p1, " Pi_q2 =", p2)
            raise SystemExit
print("no t=2 abstract obstruction with entries 0..2")
