import itertools, json
from collections import defaultdict

m=12
def fix_mod(q):
    res=[]
    for a in range(q):
        for b in range(q):
            seq=[a,b]
            for _ in range(m):
                seq.append((6*seq[-1]-seq[-2])%q)
            if seq[m]==a and seq[m+1]==b:
                # check Hv=0 directly
                v=seq[:m]
                ok=all((6*v[i]-v[(i-1)%m]-v[(i+1)%m])%q==0 for i in range(m))
                if ok: res.append(tuple(v))
    return res

def dihedral_perms(m):
    perms=[]
    for k in range(m):
        perms.append(tuple((j+k)%m for j in range(m)))  # rotation: new[j]=old[(j+k)%m]? careful: apply as v∘p
        perms.append(tuple((k-j)%m for j in range(m)))
    # deduplicate
    return sorted(set(perms))

def apply_perm(v,p):
    # (v∘p)[j] = v[p[j]]
    return tuple(v[p[j]] for j in range(m))

def canon_gamma(v,perms):
    return min(apply_perm(v,p) for p in perms)

perms=dihedral_perms(m)
print("dihedral perms:",len(perms))
for q in [128,81,25,49,121]:
    F=fix_mod(q)
    fibers=defaultdict(list)
    for v in F: fibers[tuple(sorted(v))].append(v)
    # gamma orbits per fiber
    bad=0; tot_orbits=0
    for key,vs in fibers.items():
        canons=set(canon_gamma(v,perms) for v in vs)
        tot_orbits+=len(canons)
        if len(canons)>1: bad+=1
    print(f"q={q} |Fix|={len(F)} fibers={len(fibers)} gamma_orbits={tot_orbits} bad={bad} fiber_sizes={sorted(set(len(v) for v in fibers.values()))}")
    # parameterization: look at first two entries distribution
    # check if v determined by v0 alone?
    from collections import Counter
    c=Counter(v[0] for v in F)
    print("  v0 distinct:",len(c), "max per v0:",max(c.values()))
    # sample vectors
    print("  sample:",F[:3])
