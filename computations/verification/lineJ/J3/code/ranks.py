"""[P-check] rank of apparition r(q) = least odd m with q | h_m (h_1=1, h_3=7, h_{m+2}=6h_m-h_{m-2}), primes q<2000.
q | h_m  <=>  r(q) | m and m/r(q) odd (divisibility-sequence property, checked here up to m<6000)."""
import json
def primes(N):
    s=[1]*N; s[0]=s[1]=0
    for i in range(2,N):
        if s[i]:
            for j in range(i*i,N,i): s[j]=0
    return [i for i in range(3,N) if s[i]]
res={}
for q in primes(2000):
    hs={}; a,b=1%q,7%q; hs[1]=a; hs[3]=b
    for mm in range(5,6000,2): a,b=b,(6*b-a)%q; hs[mm]=b
    zs=[mm for mm,v in hs.items() if v==0]
    if zs:
        r=zs[0]; assert all(mm%r==0 and (mm//r)%2==1 for mm in zs) and all(hs[k*r]==0 for k in range(1,6000//r,2) if k*r<6000)
        res[q]=r
print('primes dividing some h_m (q<2000):',len(res))
print(sorted(res.items(),key=lambda x:x[0])[:40])
print('11,13 divide some h_m?',11 in res,13 in res)
json.dump(res,open('logs/ranks.json','w'))
