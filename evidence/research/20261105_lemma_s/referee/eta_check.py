import math, json, itertools
from sympy import factorint, sqrt_mod, Poly, symbols, resultant, cyclotomic_poly
from lemmaS_exact import H
x=symbols('x'); out=[]
for p in [3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73]:
    h=H(p); Phi=cyclotomic_poly(p,x)
    row=dict(p=p,h=h)
    for s in (1,-1):
        eta=x-1-2*s*x**((p+1)//2)
        row[f'N{s}']=int(resultant(Phi,eta,x))   # = prod over roots z of Phi of eta(z) (Phi monic)
    row['Nker']=int(resultant(Phi,x**2-6*x+1,x))
    row['ok_norm']=(row['N1']==h and row['N-1']==h and row['Nker']==h*h)
    if p<=43:
        # kernel check on every line abar (sqrt2 -> r mod h), zeta -> lam=(1+r)^2
        qs=sorted(factorint(h)); oks=[]
        for ch in itertools.product(*[[int(sqrt_mod(2,q)),q-int(sqrt_mod(2,q))] for q in qs]):
            r=0;M=1
            for q,rq in zip(qs,ch): r=r+M*(((rq-r)*pow(M,-1,q))%q); M*=q
            e=(1+r)%h; lam=e*e%h; ep=pow(e,p,h); om=pow(lam,(p+1)//2,h)
            sig=[1 if ep%q==1 else -1 for q in qs]
            ev={s:(lam-1-2*s*om)%h for s in (1,-1)}
            ker=(lam*lam-6*lam+1)%h
            kind = 'binet' if len(set(sig))==1 else 'cross'
            if kind=='binet': oks.append(ev[sig[0]]==0 and ev[-sig[0]]!=0 and ker==0)
            else: oks.append(ev[1]!=0 and ev[-1]!=0 and ker==0)
        row['ok_kernel']=all(oks); row['nlines']=len(oks)
    out.append(row); print(row,flush=True)
json.dump(out,open('eta_check.json','w'),indent=1)
