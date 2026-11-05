# referee spot checks for item (5): line split, l1, max|u| (own line membership), Dev/main from npz with direct sums
import sys, math, json, numpy as np
sys.path.insert(0,'/workspace/bgs-lineN/N6/code')
from sympy import sqrt_mod
from twb import nu_rho, mdata
P='/workspace/research1105b/logs/lvl/'
def lines_split(p,pre):
    f=np.load(P+pre+'_ii.npz'); Z0=complex(f['Z0']); bx=f['bx'].astype(np.int64); by=f['by'].astype(np.int64); w=f['w']; u=f['Zh']/Z0
    h={11:8119,13:47321}[p]; qs={11:(23,353),13:(79,599)}[p]
    nz=~((bx==0)&(by==0))
    # local ideal at q: kernel of sqrt2 -> r  <=> x + r y == 0 mod q ; sign of eps^p there: (1+r)^p
    loc={}
    for q in qs:
        r0=int(sqrt_mod(2,q))
        for r in (r0,q-r0):
            loc[(q,r)]=dict(on=((bx+r*by)%q==0), sig=1 if pow(1+r,p,q)==1 else -1, axis=((bx%q==0)&(by%q==0)))
    out={}
    rs=[[k for k in loc if k[0]==q] for q in qs]
    for k1 in rs[0]:
        for k2 in rs[1]:
            kb1=(k1[0],k1[0]-k1[1]); kb2=(k2[0],k2[0]-k2[1])
            A=loc[k1]['on']&loc[k2]['on']; Ab=loc[kb1]['on']&loc[kb2]['on']
            sel=(A|Ab)&nz; ax=loc[k1]['axis']|loc[k2]['axis']
            X=0.5*(w[sel]*u[sel]).sum(); l1=0.5*(w[sel]*np.abs(u[sel])).sum()
            sig=(loc[k1]['sig'],loc[k2]['sig']); kind='binet' if sig[0]==sig[1] else 'cross'
            out[str(sig)]=dict(kind=kind,absX=abs(X),l1=l1,ratio=abs(X)/l1,maxu=float(np.abs(u[sel]).max()),
                               maxu_noaxis=float(np.abs(u[sel&~ax]).max()), l1_noaxis=0.5*(w[sel&~ax]*np.abs(u[sel&~ax])).sum(),
                               absX_noaxis=abs(0.5*(w[sel&~ax]*u[sel&~ax]).sum()))
    return out
def members(m,sg,D):
    h,nu0=nu_rho(m,sg); M=2*h; yp=mdata(m)['yp']; t=[]
    for j in range(1,D):
        if math.gcd(j,D)!=1: continue
        if math.gcd((nu0+(M//D)*j)%M,M)!=1: continue
        t.append(pow((j*yp)%D,-1,D))
    return np.array(t,np.int64)
def devmain(m,sg,D,pre,specs):
    tb=members(m,sg,D); A=np.zeros(D,complex)
    for s in specs:
        f=np.load(P+pre+f'_{s}.npz'); Z0=complex(f['Z0']); nz=~((f['bx']==0)&(f['by']==0))
        np.add.at(A,f['Nm'][nz],(f['w']*f['Zh']/Z0)[nz])
    k=np.arange(D)
    E=np.array([ (A*np.exp(2j*np.pi*((t*k)%D)/D)).sum() for t in tb])
    r=np.abs(1+E)**2
    return dict(n=len(tb),dev_over_main=float(r.mean()-1),meanE=[E.mean().real,E.mean().imag],var=float(np.var(E)),minr=float(r.min()),maxr=float(r.max()))
if __name__=='__main__':
    res={}
    res['split11']=lines_split(11,'p11_s1'); res['split13']=lines_split(13,'p13_s1')
    res['dev_p11_ii_ui_iu']=devmain(33,1,8119,'p11_s1',['ii','ui','iu'])
    res['dev_p11_ii']=devmain(33,1,8119,'p11_s1',['ii'])
    res['dev_p11m_ii_ui']=devmain(33,-1,8119,'p11_sm1',['ii','ui'])
    print(json.dumps(res,indent=1,default=float)); json.dump(res,open('spot5.json','w'),indent=1,default=float)
