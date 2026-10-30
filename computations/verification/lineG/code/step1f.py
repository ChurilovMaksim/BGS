import sys, math, json, numpy as np
from law import mdata, ratrec
from step1b import Z2all, factor, load
from step1c import divisors
from step1e import PR
kick=sys.argv[1]; ms=[int(x) for x in sys.argv[2].split(',')]
res={}
for m in ms:
    T=load(kick,m); h=mdata(m)['h']; R=Z2all(T,m); phi=len(R)
    ds=[d for d in divisors(h) if 1<d<=h**0.5]
    PRk=PR if kick=='k1' else [(a,49*b) for a,b in PR]+PR
    nus=np.array([nu for nu,_ in R]); Z=np.array([z for _,z in R])
    dil=np.zeros(phi,bool)
    for d in ds:
        M=2*h//d
        for a,b in PRk:
            dil|=((b*nus-a)%M==0)
    hts=np.array([max(abs(ratrec(int(nu),2*h)[0][0]),ratrec(int(nu),2*h)[0][1]) for nu in nus])
    line=f'{kick} m={m} h={h} {factor(h)} F/2m={Z.mean()/(2*m):.4f} target(B^sym+2m)/2m={(2*m-m*m/h+2*m)/(2*m):.4f} | '
    out=[]
    for H in [8,16,32,64,128]:
        rem=dil|(hts<=H)
        rest=Z[~rem].mean()/(2*m); out.append((H,int(rem.sum()),rest))
        line+=f'H={H}: rm={rem.sum()/phi:.2%} rest={rest:.4f} W\'/m={2*(rest-2):+.3f}; '
    print(line,flush=True); res[m]=out
json.dump(res,open(f'../logs/step1f_{kick}.json','w'))
