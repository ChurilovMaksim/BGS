"""N20 [CA-fp, core functional]: extend the certified finite part of the shell sums to shells j = Jlo..Jhi
(classes alpha in O mod +-eps^Z, fundamental domain as N14 a_enum.reps, seed e = 2 alpha), via the N15 c3_mid chain
(midpoint + derived a-priori rounding radii, IEEE std model + libm <= 1 ulp).  Only classes with max internal eps-zero-run
zr < 6 and not model are certified (these are exactly the bad clusters for every g0 in 2..6; others are coded/gas).
usage: a_cert_ext.py Jlo Jhi"""
import sys, json, os, time
sys.path.insert(0,'/workspace/bgs-lineN/N14/code'); sys.path.insert(0,'/workspace/bgs-lineN/N15/code')
a0=sys.argv; sys.argv=[a0[0],'0','0','18','/dev/null']
import importlib.util
spec=importlib.util.spec_from_file_location('aenum_reps','/workspace/bgs-lineN/N14/code/a_enum.py')
sys.argv=a0
import math, digits as Dg, c3_mid as M
r2=math.sqrt(2); lamf=3+2*r2
def reps(lo,hi):  # verbatim copy of N14 a_enum.reps
    X1max=math.sqrt(hi*lamf); B=int(X1max/r2)+2; res=[]
    for b in range(-B,B+1):
        for a in range(-int(X1max)-2,int(X1max)+3):
            x1=a+b*r2; x2=a-b*r2
            if x1<=0 or x2==0: continue
            N=abs(a*a-2*b*b)
            if not (lo<=N<hi): continue
            if 1<=x1/abs(x2)<lamf*(1-1e-12): res.append((a,b,N))
    return res
MODEL={(1,0),(0,1),(2,0),(0,2)}
Jlo,Jhi=int(sys.argv[1]),int(sys.argv[2]); OUT='/workspace/bgs-lineN/N20/logs/a_cert_ext.jsonl'
done=set()
if os.path.exists(OUT):
    for l in open(OUT): r=json.loads(l); done.add((r['a'],r['b']))
t0=time.time()
with open(OUT,'a') as f:
    for j in range(Jlo,Jhi+1):
        R=reps(2**j,2**(j+1)); nb=0
        for (a,b,N) in R:
            if (a,b) in done or (a,b) in MODEL: continue
            w_,g,_=Dg.eps_digits(2*a,2*b,6)
            if g>=6:
                f.write(json.dumps(dict(j=j,a=a,b=b,N=N,zr=g,coded=True))+'\n'); continue
            w=M.window(2*a,2*b); nb+=1
            f.write(json.dumps(dict(j=j,a=a,b=b,N=N,zr=g,span=len(w_),absA_up=w[0]['abs_up'],absB_up=w[1]['abs_up'],
                rad=[w[0]['rad'],w[1]['rad']],rArB2_up=(w[0]['abs_up']*w[1]['abs_up'])**2,absw_up=(w[0]['abs_up']*w[1]['abs_up'])**3))+'\n'); f.flush()
        print(j,len(R),nb,round(time.time()-t0,1),flush=True)
print('DONE',flush=True)
