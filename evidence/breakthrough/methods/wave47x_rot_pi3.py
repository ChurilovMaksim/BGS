# Wave 47x, task E — tabulate (s,t,s',t') -> pi-set at q=3 for rotation pairs.
# Validates the vote-transfer argument's tag claims directly.
from collections import defaultdict
ALPHA = (3, 2)
def mul(a, b, M): return ((a[0]*b[0]+2*a[1]*b[1]) % M, (a[0]*b[1]+a[1]*b[0]) % M)
def pw(a, n, M):
    r = (1, 0)
    for _ in range(n): r = mul(r, a, M)
    return r
AP8 = [pw(ALPHA, i, 8192) for i in range(32)]
AP17 = [pw(ALPHA, i, 17) for i in range(32)]
def seq_fast(B, AP, M):
    return tuple((2*((B[0]*a[0]+2*B[1]*a[1]) % M)) % M for a in AP)
def joints(ppp, oo, t=4):
    return tuple(tuple(sorted(zip(ppp[r::t], oo[r::t]))) for r in range(t))
perms = [tuple((e*r+b) % 4 for r in range(4)) for e in (1, -1) for b in range(4)]
def bseq(C, M):
    AP = [pw(ALPHA, i, M) for i in range(32)]
    return [ (2*((C[0]*x[0]+2*C[1]*x[1]) % M)) % M for x in AP ]
def run(name, A, Ap):
    B2, Bq = A; B2p, Bqp = Ap
    p, pp = seq_fast(B2, AP8, 8192), seq_fast(B2p, AP8, 8192)
    a, ap = seq_fast(Bq, AP17, 17), seq_fast(Bqp, AP17, 17)
    J, Jb = joints(p, a), joints(pp, ap)
    pis = [pi for pi in perms if all(Jb[r] == J[pi[r]] for r in range(4))]
    print(f"===== {name}: pis={pis}")
    # for each (C3, C3'), pi-set at 3
    tab = {}
    for s in range(3):
        for t in range(3):
            for sp in range(3):
                for tp in range(3):
                    JA3 = joints(p, bseq((s, t), 3)); JB3 = joints(pp, bseq((sp, tp), 3))
                    pset = tuple(pi for pi in perms if all(JB3[r] == JA3[pi[r]] for r in range(4)))
                    if pset: tab[((s, t), (sp, tp))] = pset
    # print mapping (s',t')-relation -> pi-sets present, restricted to pset intersecting pis
    rel = defaultdict(set)
    for (c, cp), pset in tab.items():
        s, t = c; sp, tp = cp
        inter = tuple(pi for pi in pset if pi in pis)
        if inter: rel[(sp, tp, s, t)].add(inter)
    for (sp, tp, s, t), v in sorted(rel.items()):
        print(f"  (s,t)=({s},{t}) -> (s',t')=({sp},{tp}): pi3-in-pis options: {sorted(v)}")
    # check: which (s',t') relations admit ANY pi in pis (ignoring s,t)?
    by_rel = defaultdict(set)
    for (c, cp), pset in tab.items():
        s, t = c; sp, tp = cp
        inter = tuple(pi for pi in pset if pi in pis)
        if inter: by_rel[(sp, tp)].add((s, t))
    print("  (s',t') values admitting a pis pi (with some (s,t)):")
    for k in sorted(by_rel): print(f"    {k}: from (s,t) in {sorted(by_rel[k])}")
run("R1", ((0, 512), (0, 1)), ((0, 512), (7, 0)))
run("R2", ((0, 512), (1, 5)), ((0, 512), (1, 12)))
print("DONE")
