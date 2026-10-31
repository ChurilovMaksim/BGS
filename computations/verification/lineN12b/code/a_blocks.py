"""N12b pre-flight [N]: for k-blocks P_k(y) = M(t_{k-1})...M(t_0) along outside orbits (closed theta box), in v~ coords:
sigma_1, sigma_2 rates  MU*sigma^{1/k};  derivative sizes ||dP_3/dy0||, ||dP_3/dy1|| (exact chain rule via dM) -> required cell width.
Samples: NS random outside points + the top periodic orbits of N9b a_per (all phases).  usage: a_blocks.py NS TH"""
import sys, json, time, numpy as np
sys.path.insert(0,'/workspace/bgs-lineN/N12b/code'); from common import *
NSAMP=int(sys.argv[1]); TH=float(sys.argv[2]); K=4
def block(y,k):
    ts=[]; z=np.array(y,float)
    for i in range(k): ts.append(z[0]); z=F(z)
    return ts
def analyse(y):
    ts=block(y,K); Ms=[M(t) for t in ts]; out={}
    P=np.eye(495,dtype=complex)
    for k in range(1,K+1):
        P=Ms[k-1]@P; sv=np.linalg.svd(P,compute_uv=False)
        out[k]=(MU*sv[0]**(1/k),MU*sv[1]**(1/k),sv[0],sv[1])
    # derivative of P_3 wrt y0,y1: t0=y0, t1=y1, t2=6y1-y0
    d=[dM(t) for t in ts[:3]]
    dt_dy0=[1,0,-1]; dt_dy1=[0,1,6]
    def dP(coef):
        tot=np.zeros((495,495),complex)
        for j in range(3):
            if coef[j]==0: continue
            f=[Ms[i] if i!=j else coef[j]*d[j] for i in range(3)]
            tot+=f[2]@f[1]@f[0]
        return np.linalg.norm(tot,2)
    out['dP3']=(dP(dt_dy0),dP(dt_dy1))
    return out
rng=np.random.default_rng(5); rows=[]; t0=time.time()
pts=[]
for l in open('/workspace/bgs-lineN/N9b/logs/a_per_a4.jsonl'):
    o=json.loads(l); n=o['n']
    for tp in o['top'][:3]:
        if tp[1]<=TH: continue
        x0,x1,D=tp[3]
        for ph in range(n):
            pts.append(('per',n,tp[0],[x0/D,x1/D])); x0,x1=x1,(6*x1-x0)%D
while len(pts)<len(pts)+NSAMP and sum(1 for p in pts if p[0]=='rnd')<NSAMP:
    y=rng.random(2); zz=y.copy(); ok=True
    for i in range(K+1):
        if inbox(zz,TH): ok=False;break
        zz=F(zz)
    if ok: pts.append(('rnd',0,0,list(y)))
for kind,n,rate,y in pts:
    a=analyse(y)
    rows.append(dict(kind=kind,n=n,rate=rate,y=y,s1={k:a[k][0] for k in range(1,K+1)},s2={k:a[k][1] for k in range(1,K+1)},
                     sig3=[a[3][2],a[3][3]],dP3=a['dP3']))
    if len(rows)%20==0: print(len(rows),round(time.time()-t0),flush=True)
def mx(key,k,kind=None): return max(r[key][k] for r in rows if kind is None or r['kind']==kind)
summ=dict(TH=TH,n=len(rows),max_s1={k:mx('s1',k) for k in range(1,K+1)},max_s2={k:mx('s2',k) for k in range(1,K+1)},
          max_s1_per={k:mx('s1',k,'per') for k in range(1,K+1)},max_s2_per={k:mx('s2',k,'per') for k in range(1,K+1)},
          max_dP3=[max(r['dP3'][0] for r in rows),max(r['dP3'][1] for r in rows)],
          med_dP3=[float(np.median([r['dP3'][0] for r in rows])),float(np.median([r['dP3'][1] for r in rows]))],
          target_rel3=(TP/MU)**3)
summ['w_req_for_10pct']=0.1*summ['target_rel3']/(summ['max_dP3'][0]+summ['max_dP3'][1])
print(json.dumps(summ,indent=1)); json.dump(dict(summary=summ,rows=rows),open(f'logs/a_blocks_th{TH}.json','w'),indent=1)
