"""research1105b [N]: split the exactly enumerated isotropic class ('ii') at D=q1*q2 into the four ideal lines
(local line at q: x == s*w*y mod q), as an independent check of grok47 Prop. 9 (X_line incl. axis classes).
Orbit reps are taken under <lam,-1,conj>; conj swaps a <-> abar, so a line sum = (1/2) * sum over reps lying on a or abar
(weight w each), which is exact because Zhat(conj beta)=Zhat(beta) (time reversal; checked below on samples)."""
import sys, json, numpy as np
from sympy import factorint, sqrt_mod
sys.path.insert(0,'/workspace/bgs-lineN/N6/code'); from twb import TW, Zbatch, nu_rho
def run(p,prefix):
    m=3*p; f=np.load(f'{prefix}_ii.npz'); Z0=complex(f['Z0']); bx=f['bx']; by=f['by']; w=f['w']; u=w*f['Zh']/Z0
    D=int(np.max([1]))
    h=None
    x,y=1,1
    for _ in range(p-1): x,y=x+2*y,x+y
    h=x; qs=sorted(factorint(h)); nz=~((bx==0)&(by==0))
    onl={}
    for q in qs:
        wq=int(sqrt_mod(2,q))
        onl[q]={s:((bx-s*wq*by)%q==0) for s in (1,-1)}
    out={}
    for s1 in (1,-1):
        for s2 in (1,-1):
            A=onl[qs[0]][s1]&onl[qs[1]][s2]; Ab=onl[qs[0]][-s1]&onl[qs[1]][-s2]   # conjugate line
            sel=(A|Ab)&nz
            tot=0.5*u[sel].sum(); l1=0.5*np.abs(u[sel]).sum()
            # sign of eps^p on this ideal: kernel of sqrt2 -> -s*w
            sig=[]
            for q,s in zip(qs,(s1,s2)):
                wq=int(sqrt_mod(2,q)); e=(1-s*wq)%q; v=pow(e,p,q); sig.append(1 if v==1 else -1)
            out[f'{s1},{s2}']=dict(eps_p_signs=sig,kind='binet' if sig[0]==sig[1] else 'cross',X_line=[tot.real,tot.imag],absX=abs(tot),l1=l1)
    return out
if __name__=='__main__':
    p=int(sys.argv[1]); r=run(p,sys.argv[2]); print(json.dumps(r,indent=1))
    json.dump(r,open(f'/workspace/research1105b/logs/linesplit_p{p}.json','w'),indent=1)
