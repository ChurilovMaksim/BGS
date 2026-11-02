import numpy as np
from collections import defaultdict
m=8; D=1331712; MODS=(9,289,512)
def kernel_mod(mod):
    res=[]
    for a in range(mod):
        for b in range(mod):
            seq=[a,b]
            for _ in range(m):
                seq.append((6*seq[-1]-seq[-2])%mod)
            if seq[m]==a and seq[m+1]==b: res.append(seq[:m])
    return np.array(res,dtype=np.int64)
def crt_combine(A,mod_a,B,mod_b):
    inv=pow(mod_a,-1,mod_b); diff=(B[None,:,:]-A[:,None,:])%mod_b; t=(diff*inv)%mod_b
    return (A[:,None,:]+mod_a*t).reshape(-1,m)
pts=crt_combine(kernel_mod(9),9,kernel_mod(289),289); pts=crt_combine(pts,9*289,kernel_mod(512),512)
Y=np.zeros((len(pts),4),dtype=np.int64)
for r in range(4): Y[:,r]=pts[:,[i for i in range(m) if i%4==r]].sum(axis=1)
sorted_keys=np.sort(pts,axis=1)
uniq_fib,fib_id=np.unique(sorted_keys,axis=0,return_inverse=True); fib_id=np.asarray(fib_id).reshape(-1)
def D4_orbit(vec):
    res=set()
    for b in range(4):
        res.add(tuple(vec[(r+b)%4] for r in range(4))); res.add(tuple(vec[(-r+b)%4] for r in range(4)))
    return res
by=defaultdict(list)
for i,f in enumerate(fib_id): by[int(f)].append(i)
viol=0; tot=0; viol_fib=0
for f,idx in by.items():
    orb=D4_orbit(tuple(Y[idx[0]].tolist())); bad=False
    for i in idx:
        tot+=1
        if tuple(Y[i].tolist()) not in orb: viol+=1; bad=True
    if bad: viol_fib+=1
print(f"m=8 fibers={len(by)} Y-in-D4-orbit violations={viol}/{tot} violating fibers={viol_fib}")
# also: distinct Y orders per fiber vs D4 size, and check a non-D4 perm would occur?
# Count fibers where Y takes a value outside D4 orbit of first but inside sorted class (already viol)
