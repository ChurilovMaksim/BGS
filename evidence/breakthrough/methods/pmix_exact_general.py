from collections import defaultdict
import math, sys
def fix_mod_q(q,m):
    res=[]
    for y0 in range(q):
        for y1 in range(q):
            seq=[y0,y1]
            for _ in range(m):
                seq.append((6*seq[-1]-seq[-2])%q)
            if seq[m]==y0 and seq[m+1]==y1:
                res.append(tuple(seq[:m]))
    return res

def run(m):
    t=4
    # D and moduli
    s0,s1=2,6
    for _ in range(2,m+1):
        s0,s1=s1,6*s1-s0
    D=s1-2
    import sympy as sp
    fac=sp.factorint(D)
    q2=2**fac.get(2,0); q3=3**fac.get(3,0)
    print(f"m={m} D={D} q2={q2} q3={q3}", flush=True)
    def crt_coeff(Mj):
        Dj=D//Mj; return (Dj*pow(Dj,-1,Mj))%D
    c2=crt_coeff(q2); c3=crt_coeff(q3) if q3>1 else 0
    perms=[]
    for b in range(4):
        for sgn in (1,-1):
            pi=tuple((sgn*i+b)%4 for i in range(4))
            if pi not in perms: perms.append(pi)
    def apply(v,pi): return tuple(v[pi[i]] for i in range(4))
    def Yvec(y):
        Y=[0]*4
        for i,v in enumerate(y): Y[i%4]+=v
        return tuple(Y)
    def in_orbit(Y,Yp): return any(apply(Y,pi)==Yp for pi in perms)
    def pairs(q):
        vecs=fix_mod_q(q,m)
        groups=defaultdict(list)
        for v in vecs: groups[tuple(sorted(v))].append(v)
        out=[]
        for vs in groups.values():
            for z in vs:
                for zp in vs:
                    if zp!=z: out.append((z,zp))
        return out
    pairs2=pairs(q2); pairs3=pairs(q3) if q3>1 else [((0,)*m,(0,)*m)]
    print(f" pairs2={len(pairs2)} pairs3={len(pairs3)}", flush=True)
    def find_sigma(z2,z2p,z3,z3p):
        adj=[[j for j in range(m) if z2[j]==z2p[i] and z3[j]==z3p[i]] for i in range(m)]
        match_r=[-1]*m
        def try_k(u,seen):
            for v in adj[u]:
                if seen[v]: continue
                seen[v]=True
                if match_r[v]==-1 or try_k(match_r[v],seen):
                    match_r[v]=u; return True
            return False
        for u in range(m):
            seen=[False]*m
            if not try_k(u,seen): return None
        return True
    def crt_vec(z2,z3):
        return tuple((c2*z2[i]+c3*z3[i])%D for i in range(m))
    common=0; fails=0
    for (z2,z2p) in pairs2:
        for (z3,z3p) in pairs3:
            if find_sigma(z2,z2p,z3,z3p) is None: continue
            common+=1
            y=crt_vec(z2,z3); yp=crt_vec(z2p,z3p)
            if not in_orbit(Yvec(y), Yvec(yp)):
                fails+=1; print(" EXACT FAIL", y, yp, Yvec(y), Yvec(yp))
                if fails>=5: break
        if fails>=5: break
    print(f" RESULT m={m}: common={common} exact_fails={fails}")

for m in [int(x) for x in sys.argv[1:]]:
    run(m)
