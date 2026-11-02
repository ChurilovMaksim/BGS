from collections import defaultdict
import math

m=12; t=4
D=1536796800
mods=[128,81,25,49,121]
# CRT coefficients for residues mod 128 and mod 81, others 0
def crt_coeff(Mj):
    Dj=D//Mj
    inv=pow(Dj, -1, Mj)
    return (Dj*inv)%D
c2=crt_coeff(128); c3=crt_coeff(81)
print("c2,c3:", c2, c3, "check: c2%128", c2%128, "c2%81", c2%81, "c3%128", c3%128, "c3%81", c3%81)

perms=[]
for b in range(4):
    for sgn in (1,-1):
        pi=tuple((sgn*i+b)%4 for i in range(4))
        if pi not in perms: perms.append(pi)
def apply(v, pi): return tuple(v[pi[i]] for i in range(4))
def Yvec(y):
    Y=[0]*4
    for i,v in enumerate(y): Y[i%4]+=v
    return tuple(Y)
def in_orbit(Y, Yp):
    return any(apply(Y,pi)==Yp for pi in perms)

def fix_mod_q(q):
    res=[]
    for y0 in range(q):
        for y1 in range(q):
            seq=[y0,y1]
            for _ in range(m):
                seq.append((6*seq[-1]-seq[-2])%q)
            if seq[m]==y0 and seq[m+1]==y1:
                res.append(tuple(seq[:m]))
    return res

def component_pairs(q):
    vecs=fix_mod_q(q)
    groups=defaultdict(list)
    for v in vecs: groups[tuple(sorted(v))].append(v)
    pairs=[]
    for vs in groups.values():
        for z in vs:
            for zp in vs:
                if zp!=z:
                    pairs.append((z,zp))
    return pairs

pairs2=component_pairs(128)
pairs3=component_pairs(81)
print(f"pairs2={len(pairs2)} pairs3={len(pairs3)} product={len(pairs2)*len(pairs3)}")

def find_sigma(z2,z2p,z3,z3p):
    adj=[[j for j in range(m) if z2[j]==z2p[i] and z3[j]==z3p[i]] for i in range(m)]
    match_r=[-1]*m
    def try_k(u, seen):
        for v in adj[u]:
            if seen[v]: continue
            seen[v]=True
            if match_r[v]==-1 or try_k(match_r[v], seen):
                match_r[v]=u; return True
        return False
    for u in range(m):
        seen=[False]*m
        if not try_k(u, seen): return None
    sigma=[0]*m
    for j,u in enumerate(match_r): sigma[u]=j
    return tuple(sigma)

def crt_vec(z2,z3):
    return tuple((c2*z2[i]+c3*z3[i])%D for i in range(m))

count_common=0; count_exact_fail=0; examples=[]
for (z2,z2p) in pairs2:
    for (z3,z3p) in pairs3:
        sigma=find_sigma(z2,z2p,z3,z3p)
        if sigma is None: continue
        count_common+=1
        y=crt_vec(z2,z3); yp=crt_vec(z2p,z3p)
        # verify sigma(y)==yp and y in Fix (Hy divisible by D) and sorted equal
        # (sigma(y))_i = y_{sigma[i]} should equal yp_i by construction of sigma? Check componentwise: sigma was chosen so z2[sigma[i]]==z2p[i] and z3[sigma[i]]==z3p[i], hence CRT gives y_{sigma[i]}==yp[i]. Good.
        Y=Yvec(y); Yp=Yvec(yp)
        if not in_orbit(Y,Yp):
            count_exact_fail+=1
            print("EXACT FAIL:", "y", y, "yp", yp, "Y", Y, "Yp", Yp, "sigma", sigma)
            examples.append((y,yp,Y,Yp,sigma))
            if count_exact_fail>=5: break
    if count_exact_fail>=5: break
print(f"common-sigma pairs (other comps zero): {count_common}, exact Lemma Y failures: {count_exact_fail}")
