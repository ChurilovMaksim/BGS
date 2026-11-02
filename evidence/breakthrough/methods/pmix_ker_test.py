import itertools, math
from collections import defaultdict

def ker_mod_q(q, t):
    # H_t v = 0 mod q, H_t = 6I - shift - shift^{-1} on Z/t
    # brute force v0,v1 then solve? For t=4 use structure: equations
    # 6v0 - v3 - v1 =0, 6v1 - v0 - v2=0, 6v2 - v1 - v3=0, 6v3 - v2 - v0=0
    # From eq2: v2 = 6v1 - v0 ; eq1: v3 = 6v0 - v1 ; check eq3,eq4
    # For t=2: equations 6v0-2v1=0, 6v1-2v0=0 (off-diag -2 because neighbours coincide)
    res=[]
    if t==4:
        for v0 in range(q):
            for v1 in range(q):
                v2=(6*v1-v0)%q
                v3=(6*v0-v1)%q
                if (6*v2-v1-v3)%q==0 and (6*v3-v2-v0)%q==0:
                    res.append((v0,v1,v2,v3))
    elif t==2:
        for v0 in range(q):
            for v1 in range(q):
                if (6*v0-2*v1)%q==0 and (6*v1-2*v0)%q==0:
                    res.append((v0,v1))
    elif t==1:
        for v0 in range(q):
            if (4*v0)%q==0:
                res.append((v0,))
    return res

def dihedral_perms(t):
    perms=[]
    for b in range(t):
        for sgn in (1,-1):
            pi=tuple((sgn*i+b)%t for i in range(t))
            perms.append(pi)
    # deduplicate
    uniq=[]
    for p in perms:
        if p not in uniq: uniq.append(p)
    return uniq

def apply_perm(v, pi):
    return tuple(v[pi[i]] for i in range(len(v)))

def orbit(v, perms):
    return set(apply_perm(v, pi) for pi in perms)

def test_m(m):
    t=math.gcd(m,4)
    # D_m
    s0,s1=2,6
    if m==0: D=0
    elif m==1: D=4
    else:
        for _ in range(2,m+1):
            s0,s1=s1,6*s1-s0
        D=s1-2
    import sympy as sp
    fac=sp.factorint(D)
    q2=2**fac.get(2,0)
    q3=3**fac.get(3,0)
    perms=dihedral_perms(t)
    print(f"\nm={m} t={t} D={D} fac={fac} q2={q2} q3={q3} |G|={len(perms)}")
    if t!=4:
        print("  t!=4: mixing test vacuous/trivial (only 2-primary matters, odd parts zero) - skipping detailed")
        return
    K2=ker_mod_q(q2,t)
    K3=ker_mod_q(q3,t) if q3>1 else [(0,)*t]
    print(f"  |ker mod q2|={len(K2)} (expect 128)  |ker mod q3|={len(K3)} (expect 9)")
    # precompute orbits and pi-sets: for each vector, map target -> set of pi achieving it
    def pi_map(K):
        # returns dict vector -> dict target -> set(pi indices)
        out={}
        for v in K:
            d=defaultdict(set)
            for idx,pi in enumerate(perms):
                d[apply_perm(v,pi)].add(idx)
            out[v]=d
        return out
    pm2=pi_map(K2); pm3=pi_map(K3)
    fails=[]
    total=0
    for v2 in K2:
        for v3 in K3:
            for v2p in pm2[v2]:  # orbit targets
                pis2=pm2[v2][v2p]
                for v3p in pm3[v3]:
                    pis3=pm3[v3][v3p]
                    total+=1
                    if not (pis2 & pis3):
                        fails.append((v2,v3,v2p,v3p,pis2,pis3))
    print(f"  component-compatible pairs checked: {total}, FAILS (no common pi): {len(fails)}")
    for f in fails[:10]:
        print("   FAIL v2,v3,v2p,v3p:", f[0], f[1], f[2], f[3], "pis2", f[4], "pis3", f[5])
    return fails

for m in [4,8,12,16,20]:
    test_m(m)
