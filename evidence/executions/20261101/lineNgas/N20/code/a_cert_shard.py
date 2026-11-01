"""N20: sharded version of a_cert_ext.py for one shell j (identical per-class computation; shard = index mod K
in the deterministic reps() order).  usage: a_cert_shard.py j k K  -> ../logs/a_cert_ext_j{j}_s{k}.jsonl"""
import sys, json, os, time
j,k,K=map(int,sys.argv[1:4]); sys.argv=[sys.argv[0],str(j),str(j)]
sys.path.insert(0,'/workspace/bgs-lineN/N14/code'); sys.path.insert(0,'/workspace/bgs-lineN/N15/code')
import math, digits as Dg, c3_mid as M
src=open('/workspace/bgs-lineN/N20/code/a_cert_ext.py').read(); ns={}
ns['math']=math; exec(src[src.index('r2=math.sqrt(2)'):src.index('MODEL=')],ns); reps=ns['reps']
MODEL={(1,0),(0,1),(2,0),(0,2)}
OUT=f'/workspace/bgs-lineN/N20/logs/a_cert_ext_j{j}_s{k}.jsonl'; done=set()
if os.path.exists(OUT):
    for l in open(OUT): r=json.loads(l); done.add((r['a'],r['b']))
R=reps(2**j,2**(j+1)); t0=time.time(); nb=0
with open(OUT,'a') as f:
    for i,(a,b,N) in enumerate(R):
        if i%K!=k or (a,b) in done or (a,b) in MODEL: continue
        w_,g,_=Dg.eps_digits(2*a,2*b,6)
        if g>=6: f.write(json.dumps(dict(j=j,a=a,b=b,N=N,zr=g,coded=True))+'\n'); continue
        w=M.window(2*a,2*b); nb+=1
        f.write(json.dumps(dict(j=j,a=a,b=b,N=N,zr=g,span=len(w_),absA_up=w[0]['abs_up'],absB_up=w[1]['abs_up'],
            rad=[w[0]['rad'],w[1]['rad']],rArB2_up=(w[0]['abs_up']*w[1]['abs_up'])**2,absw_up=(w[0]['abs_up']*w[1]['abs_up'])**3))+'\n'); f.flush()
print('DONE',j,k,K,len(R),nb,round(time.time()-t0,1),flush=True)
