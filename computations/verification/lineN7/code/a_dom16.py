"""N7 [CA]: sharpen the (+-2,16) untwisted rate. For each J3 representative r whose untwisted 'rest' certificate was only R=1.6677
(top 1.6154), rebuild the operator with J3's certG_build16.py (read-only use of J3 code; output into N7/data) and run J3's rig_spec.py in
'dom' mode: certifies the dominant eigenvalue |mu| in [|b11|-r1, |b11|+r1] and the complement radius < R.  Usage: a_dom16.py r"""
import sys, os, json, subprocess
J3='/workspace/bgs-lineJ/J3'; N7='/workspace/bgs-lineN/N7'; PY='/workspace/bgs-derand/phase3/venv/bin/python'
r=int(sys.argv[1]); case,blk,_=json.load(open(J3+'/logs/blocks16_reps.json'))['reps'][r]; M,A=case.split(',')
env=dict(os.environ,BGS16_CASE=case,BGS16_BLOCK=str(blk),OMP_NUM_THREADS='1',OPENBLAS_NUM_THREADS='1')
pre=f'{N7}/data/V_r{r}_u'
if not os.path.exists(pre+'.json'):
    subprocess.run(['nice','-n','10',PY,J3+'/code/certG_build16.py','V',M,A,'3','1.2','40','2.5','150','40','none',pre,'128','40'],
                   env=env,check=True,cwd=J3,stdout=open(f'{N7}/logs/build_V_r{r}_u.log','w'),stderr=subprocess.STDOUT)
outj=f'{N7}/logs/dom16_V_r{r}.json'
subprocess.run(['nice','-n','10',PY,J3+'/code/rig_spec.py',pre,'0','dom','0.95,1.0,1.1,1.2','0.005,0.01,0.02','64',outj],env=env,cwd=J3,
               stdout=open(outj.replace('.json','.log'),'w'),stderr=subprocess.STDOUT)
d=json.load(open(outj)); print(r,d.get('certified'),d.get('R'),d.get('r1'),d.get('mu_abs_upper'),d.get('F_R1'),d.get('F_R2'),flush=True)
for s in ('mid','rad'):
    f=f'{pre}_b0_{s}.npy'
    if os.path.exists(f): os.remove(f)
