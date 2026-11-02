import itertools
m=12; D=1536796800
mods=[128,81,25,49,121]
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
def in_fix_mod_q(vec,q):
    return all((6*vec[i]-vec[(i-1)%m]-vec[(i+1)%m])%q==0 for i in range(m))
tau=(10,4,11,6,1,8,3,9,5,0,7,2)
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
coeffs={Mj: ((D//Mj)*pow(D//Mj,-1,Mj))%D for Mj in mods}
def crt_vec(comp):
    return tuple(sum(coeffs[q]*comp[q][i] for q in mods)%D for i in range(m))
S={}
for q in mods:
    vecs=fix_mod_q(q)
    S[q]=[v for v in vecs if in_fix_mod_q(tuple(v[tau[i]] for i in range(m)), q)]
    print(f"q={q} |S|={len(S[q])}")
total=1
for q in mods: total*=len(S[q])
print("total combos:", total)
fails=0; checked=0
for combo in itertools.product(*[S[q] for q in mods]):
    comp=dict(zip(mods, combo))
    y=crt_vec(comp); yp=tuple(y[tau[i]] for i in range(m))
    checked+=1
    if not in_orbit(Yvec(y), Yvec(yp)):
        fails+=1; print("FAIL", y, yp, Yvec(y), Yvec(yp)); break
print(f"checked {checked}, fails {fails}")
