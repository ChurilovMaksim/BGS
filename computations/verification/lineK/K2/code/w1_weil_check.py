"""W1 sanity [N/P-check of instances]: for primes q with r(q) = ord_q(lam) in {p, 3p} (lam = 3+2sqrt2 in F_q, q = +-1 mod 8),
max over all (A,B) != 0 of |sum_{i<r} e((A l^i + B l^-i)/q)| / sqrt(q) must be <= 2 (Weil, twisted Kloosterman; Gauss periods <= 1 if A or B = 0).
Exhaustive over A,B for small q via FFT-free direct numpy."""
import numpy as np, json, sympy
def sqrt2(q):
    for s in range(2,q):
        if s*s%q==2: return s
out=[]
for p in (5,7,11,13,17,19,23,29,31,37):
    found=0
    for q in sympy.primerange(2*p+1, 4000):
        if q%8 not in (1,7): continue
        s=sqrt2(q); l=(3+2*s)%q; r=sympy.n_order(l,q)
        if r not in (p,3*p): continue
        H=np.array([pow(l,i,q) for i in range(r)]); Hi=np.array([pow(int(h),q-2,q) for h in H])
        A=np.arange(q)[:,None]
        E1=np.exp(2j*np.pi*(A*H[None,:]%q)/q); E2=np.exp(2j*np.pi*(A*Hi[None,:]%q)/q)
        S=E1@E2.T   # S[a,b] = sum_i e((a h_i + b h_i^-1)/q)
        S[0,0]=0
        mx=np.abs(S).max()/np.sqrt(q); mx_lin=max(np.abs(S[1:,0]).max(),np.abs(S[0,1:]).max())/np.sqrt(q)
        out.append(dict(p=p,q=q,r=r,max_ratio=float(mx),max_ratio_linear=float(mx_lin))); print(out[-1],flush=True)
        found+=1
        if found>=2: break
ok=all(o['max_ratio']<=2+1e-9 and o['max_ratio_linear']<=1+1e-9 for o in out)
print('WEIL INSTANCES', 'OK' if ok else 'VIOLATION')
json.dump(dict(rows=out,ok=ok),open('logs/w1_weil_check.json','w'),indent=1)
