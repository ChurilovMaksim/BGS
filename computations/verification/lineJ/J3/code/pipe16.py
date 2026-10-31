"""J3 pipeline for one representative r of the 32 distinct (sign, block) factors of the (±2,16) automaton:
build (arb, certG_build16) V/E x {untwisted, 8 d=7 classes} -> float tops -> rig_spec 'rest' certificate at R = 1.02*top+0.02
(retry +0.04, +0.10) -> keep build JSON + certificate JSON (records sha256 of the matrices), delete the .npy (disk; rebuild is
deterministic, ~1 min).  Usage: pipe16.py r"""
import sys, os, json, subprocess, numpy as np, hashlib
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..'))
r=int(sys.argv[1]); case,blk,_=json.load(open('logs/blocks16_reps.json'))['reps'][r]; M,A=case.split(',')
PY='/workspace/bgs-derand/phase3/venv/bin/python'; CL='1:3,2:1,0:1,1:2,1:5,0:3,1:0,0:2'
env=dict(os.environ,BGS16_CASE=case,BGS16_BLOCK=str(blk),OMP_NUM_THREADS='2',OPENBLAS_NUM_THREADS='2')
PAR={'V':['3','1.2','40','2.5','150','40'],'E':['3','0.8','30','2.5','150','40']}; K2={'V':'40','E':'30'}
summ={}
for T in ('V','E'):
    for kind,cl in (('u','none'),('t',CL)):
        pre=f'data/cert/{T}_r{r}_{kind}'
        if not os.path.exists(pre+'.json'):
            subprocess.run(['nice','-n','10',PY,'code/certG_build16.py',T,M,A]+PAR[T]+[cl,pre,'128',K2[T]],env=env,check=True,
                           stdout=open(f'logs/cert/build_{T}_r{r}_{kind}.log','w'),stderr=subprocess.STDOUT)
        nb=1 if kind=='u' else 8
        for b in range(nb):
            outj=f'logs/cert/{T}_r{r}_{kind}_b{b}_rest.json'
            if os.path.exists(outj) and json.load(open(outj)).get('certified'): summ[f'{T}{kind}{b}']=json.load(open(outj))['R']; continue
            Am=np.load(f'{pre}_b{b}_mid.npy'); top=float(np.max(np.abs(np.linalg.eigvals(Am)))); del Am
            ok=False
            for add in (0.0,0.04,0.10):
                R=f'{1.02*top+0.02+add:.4f}'
                subprocess.run(['nice','-n','10',PY,'code/rig_spec.py',pre,str(b),'rest',R,'0','64',outj],env=env,
                               stdout=open(outj.replace('.json','.log'),'w'),stderr=subprocess.STDOUT)
                if os.path.exists(outj) and json.load(open(outj)).get('certified'): ok=True; break
            summ[f'{T}{kind}{b}']=dict(top=top,R=R,certified=ok); print(r,T,kind,b,top,R,ok,flush=True)
        for b in range(nb):
            for s in ('mid','rad'):
                f=f'{pre}_b{b}_{s}.npy'
                if os.path.exists(f): os.remove(f)
json.dump(summ,open(f'logs/cert/pipe_r{r}.json','w'),indent=1); print('DONE',r,flush=True)
