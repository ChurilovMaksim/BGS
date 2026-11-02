import random
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
    # check recurrence + periodicity
    for i in range(m):
        if (6*vec[i]-vec[(i-1)%m]-vec[(i+1)%m])%q!=0:
            return False
    return True

# sigma from glued fiber: y'_i = y_{tau[i]} where tau given in wave8 task2 as tau mapping? 
# In wave8 task2, y' = y o tau with tau=(10,4,11,6,1,8,3,9,5,0,7,2) meaning y'_i = y[tau[i]]
tau=(10,4,11,6,1,8,3,9,5,0,7,2)
# also try a few other sigmas: block swap, reversal with shift, etc.
sigmas={
 "glued_tau": tau,
 "swap_halves": tuple((i+6)%12 for i in range(12)),
 "reverse": tuple((-i)%12 for i in range(12)),
 "perm_0123": (1,0,3,2,5,4,7,6,9,8,11,10),
}
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

# CRT coefficients
coeffs={}
for Mj in mods:
    Dj=D//Mj; coeffs[Mj]=(Dj*pow(Dj,-1,Mj))%D
def crt_vec(comp): # comp: dict q->vec
    out=[]
    for i in range(m):
        out.append(sum(coeffs[q]*comp[q][i] for q in mods)%D)
    return tuple(out)

for name,sigma in sigmas.items():
    print(f"\nSigma {name}: {sigma}")
    S={}
    for q in mods:
        vecs=fix_mod_q(q)
        good=[v for v in vecs if in_fix_mod_q(tuple(v[sigma[i]] for i in range(m)), q)]
        S[q]=good
        print(f"  q={q} |Fix|={len(vecs)} |S_sigma|={len(good)}")
    # sample random combinations
    random.seed(0)
    fails=0; tried=0
    for trial in range(2000):
        comp={q: random.choice(S[q]) for q in mods}
        y=crt_vec(comp)
        yp=tuple(y[sigma[i]] for i in range(m))
        # verify yp in Fix globally: Hy divisible by D
        Hy=[6*yp[i]-yp[(i-1)%m]-yp[(i+1)%m] for i in range(m)]
        assert all(x%D==0 for x in Hy), "yp not in Fix!"
        tried+=1
        if not in_orbit(Yvec(y), Yvec(yp)):
            fails+=1
            print("  EXACT FAIL trial", trial, "y", y, "yp", yp, "Y", Yvec(y), "Yp", Yvec(yp))
            if fails>=3: break
    print(f"  sampled {tried}, exact fails {fails}")
