"""EXACT sector decomposition of the 16-state G2 (a,8) automaton (Line I gstates), all 8 operator cases.
Find f_a (entries 8th roots of unity / 4) with A_n f_a = e(a n/8) f_a for all n mod 8; verify exactly (exponent arithmetic mod 8),
orthonormality and u in span{f_a} exactly (in Z[zeta8], basis 1,z,z^2,z^3, z^4=-1), and c_a = <f_a|e0><u|f_a> exactly.
A_n (gstates.finite): column s -> row tg(s,n), entry e(-ph8/8)."""
import sys, json, hashlib, os, numpy as np
from fractions import Fraction as Fr
here=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,'/workspace/bgs-lineI/dom_v3')
from gstates import g2params, reach, finite
def zvec(e):  # zeta8^e as integer 4-vector
    e%=8; v=[0,0,0,0]; v[e%4]=1 if e<4 else -1; return v
def add(u,v): return [a+b for a,b in zip(u,v)]
def zsum(exps):
    s=[0,0,0,0]
    for e in exps: s=add(s,zvec(e))
    return s
def zmul(u,v):
    r=[0]*8
    for i in range(4):
        for j in range(4): r[i+j]+=u[i]*v[j]
    return [r[0]-r[4],r[1]-r[5],r[2]-r[6],r[3]]
def zc(v): return complex(sum(v[i]*np.exp(2j*np.pi*i/8) for i in range(4)))
out={}
for m in (9,15,21,27):
  for a in (2,-2):
    P=g2params(m,a,8); idx,tg=reach(P,60); NS=len(idx)
    A={}
    for n in range(8):
        mp={}
        for (o,i,ph8,tw) in finite(P,idx,tg,n,None): mp[i]=(o,(-ph8)%8)
        A[n]=mp
    # numeric common eigenvectors
    An=[np.zeros((NS,NS),complex) for n in range(8)]
    for n in range(8):
        for i,(o,e) in A[n].items(): An[n][o,i]=np.exp(2j*np.pi*e/8)
    secs={}
    for sa in range(8):
        Mx=np.vstack([An[n]-np.exp(2j*np.pi*sa*n/8)*np.eye(NS) for n in range(8)])
        u_,s_,vh=np.linalg.svd(Mx); null=vh[np.sum(s_>1e-9):].conj()
        if null.shape[0]==0: continue
        assert null.shape[0]==1, (m,a,sa,null.shape)
        f=null[0]; j=np.argmax(abs(f)); f=f/(f[j]/abs(f[j]))
        assert np.allclose(abs(f),0.25)
        ex=[int(round(np.angle(x)/(2*np.pi)*8))%8 for x in f]   # f_s = zeta8^ex[s]/4
        # exact check: (A_n f)_o = zeta^{e_n(i)} f_i  must equal zeta^{sa n} f_o
        for n in range(8):
            for i,(o,e) in A[n].items(): assert (e+ex[i])%8==(sa*n+ex[o])%8
        secs[sa]=ex
    # orthonormality exact: <f_a|f_b> = (1/16) sum zeta^{e_b - e_a}
    for x in secs:
        for y in secs:
            g=zsum([secs[y][s]-secs[x][s] for s in range(NS)])
            assert g==([16,0,0,0] if x==y else [0,0,0,0]),(x,y,g)
    # u = sum_s e_s ;  <f_a|u> = (1/4) sum_s zeta^{-e_a(s)} ; check u == sum_a <f_a|u> f_a exactly (times 16)
    recon=[[0,0,0,0] for s in range(NS)]
    coef={}
    for sa,ex in secs.items():
        cu=zsum([-e for e in ex])          # 4 <f_a|u>
        coef[sa]=cu
        for s in range(NS): recon[s]=add(recon[s],zmul(cu,zvec(ex[s])))   # 16 * <f|u> f_s
    assert all(r==[16,0,0,0] for r in recon), 'u not in span'
    # c_a = <f_a|e0><u|f_a> = conj(f_a(0)) * sum_s f_a(s) ; exact: (1/16) zeta^{-e(0)} * sum zeta^{e(s)}
    cs={}
    for sa,ex in secs.items():
        v=zmul(zvec(-ex[0]),zsum(ex)); cs[sa]=dict(c_times16=v,c=str(zc(v)/16),abs=abs(zc(v)/16),arg_over_2pi=(np.angle(zc(v))/(2*np.pi))%1)
    key=f'{m},{a}'; out[key]=dict(params=P,states=idx,sectors=sorted(secs),f_exponents={str(k):v for k,v in secs.items()},c=cs,
         rank1_dims=len(secs),complement_dim=NS-len(secs))
    print(key,'k,psi0,psi1',P['k'],P['psi0'],P['psi1'],'sectors',sorted(secs),{k:(round(v['abs'],12),round(v['arg_over_2pi']*8,9)) for k,v in cs.items()},flush=True)
sha=hashlib.sha256(open(__file__,'rb').read()).hexdigest()
json.dump(dict(code_sha256=sha,cases=out),open(os.path.join(here,'../logs/sectors_exact.json'),'w'),indent=1)
print('ALL EXACT CHECKS PASSED')
