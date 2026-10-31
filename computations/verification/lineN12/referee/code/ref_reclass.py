"""Referee N12: classify every short-gap (eps-gap n=2G+h<5) two-bump composite seed e = e_i + s*e_j*eps^h*lam^G.
Is e = (+-) beta * eps^k for a single type beta (i.e. the SAME point as a single bump -> relabelling), or zero, or neither (uncoded)?
Also report, from N12's d_merged json, the window-model weight |w(e)| of each uncoded composite (absolute)."""
import json, math
T={'odd':(2,0),'sq2':(0,2),'two':(4,0),'2sq2':(0,4),'four':(8,0)}
def mul(u,v): return (u[0]*v[0]+2*u[1]*v[1], u[0]*v[1]+u[1]*v[0])
def epow(k):
    r=(1,0); b=(1,1) if k>=0 else (-1,1)   # eps^-1 = -1+sqrt2
    for _ in range(abs(k)): r=mul(r,b)
    return r
def N(u): return u[0]**2-2*u[1]**2
def is_single(e):
    if e==(0,0): return 'zero'
    for name,b in T.items():
        if abs(N(e))!=abs(N(b)): continue
        for k in range(-40,41):
            for sg in (1,-1):
                if tuple(sg*x for x in mul(b,epow(k)))==e: return f'{name}*{"-" if sg<0 else ""}eps^{k}'
    return None
lam=(3,2)
def lp(G):
    r=(1,0)
    for _ in range(G): r=mul(r,lam)
    return r
rows=json.load(open('/workspace/bgs-lineN/N12/logs/d_merged_odd_sq2.json'))['rows']+json.load(open('/workspace/bgs-lineN/N12/logs/d_merged_two_2sq2_four.json'))['rows']
single=json.load(open('/workspace/bgs-lineN/N12/logs/d_merged_odd_sq2.json'))['single']
wabs={k:abs(complex(*v[0])*complex(*v[1]))**3 for k,v in single.items()}
out=[]; stats={'relabel':0,'zero':0,'uncoded':0}; unc_w=0.0
for r in rows:
    n=2*r['G']+r['h']
    if n>=5: continue
    ej=mul(T[r['j']],lp(r['G']))
    if r['h']: ej=mul(ej,(1,1))
    e=(T[r['i']][0]+r['s']*ej[0],T[r['i']][1]+r['s']*ej[1])
    c=is_single(e)
    kind='zero' if c=='zero' else ('relabel' if c else 'uncoded'); stats[kind]+=1
    w=abs(complex(*r['cls']))*wabs[r['i']]*wabs[r['j']]
    if kind=='uncoded': unc_w+=w
    out.append(dict(i=r['i'],j=r['j'],h=r['h'],s=r['s'],G=r['G'],n=n,e=e,N=N(e),kind=kind,single=c,w_model=w))
res=dict(stats=stats,n_rows=len(out),uncoded_total_w_model=unc_w,
         top_uncoded=sorted([o for o in out if o['kind']=='uncoded'],key=lambda o:-o['w_model'])[:15],
         relabel_examples=[o for o in out if o['kind']=='relabel'][:10])
print(json.dumps(res,indent=1)); json.dump(dict(res,rows=out),open('logs/ref_reclass.json','w'),indent=1)
# dedupe uncoded composites up to units +-eps^k (same point class => count once)
def canon(e):
    best=None
    for k in range(-40,41):
        for sg in (1,-1):
            u=tuple(sg*x for x in mul(e,epow(k)))
            key=(abs(u[0])+abs(u[1]),u)
            if best is None or key<best: best=key
    return best[1]
cl={}
for o in out:
    if o['kind']!='uncoded': continue
    c=canon(o['e']); cl.setdefault(c,[]).append(o['w_model'])
dd=sorted(((c,max(v),len(v)) for c,v in cl.items()),key=lambda t:-t[1])
res2=dict(n_distinct_uncoded=len(dd),distinct_total_w=sum(t[1] for t in dd),top=[dict(canon=c,N=N(c),w=w,mult=m) for c,w,m in dd[:15]])
print(json.dumps(res2,indent=1)); json.dump(res2,open('logs/ref_reclass_distinct.json','w'),indent=1)
