"""Referee: independent evaluation of N10's closed form X(p) = 2[e^{pR}(sinh(2p w*)+1) - 1] and of the exact finite-p
per-position form 2*( (1/2)[(1+R+2w*)^p-(1+R-2w*)^p] + (1+R)^p - 1 ), plus the claims:
first Re X<0, min|1+X|, first |X|>=2, G = (|1+X|^2-1)/(8p Re(w*+c0)), and the p=47 (m=141) numbers."""
import cmath, json
ws=complex(3.43580e-4,1.95796e-4); R=complex(6.185e-5,-1.943e-5); c0=complex(2.9866e-5,-6.599e-6)
def Xc(p): return 2*(cmath.exp(p*R)*(cmath.sinh(2*p*ws)+1)-1)
def Xe(p): return 2*(((1+R+2*ws)**p-(1+R-2*ws)**p)/2 + (1+R)**p - 1)
out={}; first_neg=None; minabs=(10,None); first2=None; minG=(1e9,None); neg=0; tot=0; maxdiff=0
for p in range(3,200001,2):
    X=Xe(p); maxdiff=max(maxdiff,abs(Xc(p)-X)/max(1,abs(X)))
    tot+=1
    if X.real<0:
        neg+=1
        if first_neg is None: first_neg=p
    a=abs(1+X)
    if a<minabs[0]: minabs=(a,p)
    if first2 is None and abs(X)>=2: first2=(p,cmath.phase(X),X.real)
    G=(a**2-1)/(8*p*(ws+c0).real)
    if G<minG[0]: minG=(G,p)
out.update(first_ReX_neg=first_neg,neg_fraction=neg/tot,min_abs_1pX=minabs,first_absX_ge2=first2,min_G=minG,max_rel_diff_closed_vs_exact=maxdiff)
for p in (13,47,1165,4287,5001,10001):
    X=Xe(p); out[f'X_{p}']=[X.real,X.imag,abs(X)]
X47=Xe(47); lin=4*47*(ws+c0).real
out['p47']=dict(ReX_gas=X47.real,lin=lin,mod_gain=(2*X47.real+abs(X47)**2)/(2*lin))
print(json.dumps(out,indent=1)); json.dump(out,open('logs/ref_genfun.json','w'),indent=1)
