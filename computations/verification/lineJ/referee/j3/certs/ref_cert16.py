"""Referee: rebuild sample reps of the J3 (±2,16) factors in the mirror, compare matrix sha256 with the cert provenance,
rerun rig_spec 'rest' at the recorded R, compare. Outputs only under /workspace/audit/lineJ/j3/."""
import sys, os, json, subprocess, hashlib, ast
MIR='/workspace/audit/lineJ/j3/mirror/J3'; OUT='/workspace/audit/lineJ/j3/certs'
os.chdir(MIR); PY='/workspace/bgs-derand/phase3/venv/bin/python'; CL='1:3,2:1,0:1,1:2,1:5,0:3,1:0,0:2'
PAR={'V':['3','1.2','40','2.5','150','40'],'E':['3','0.8','30','2.5','150','40']}; K2={'V':'40','E':'30'}
sha=lambda f: hashlib.sha256(open(f,'rb').read()).hexdigest()
reps=json.load(open('logs/blocks16_reps.json'))['reps']
res=json.load(open(f'{OUT}/ref_cert16.json')) if os.path.exists(f'{OUT}/ref_cert16.json') else {}
for r in map(int,sys.argv[1:]):
    case,blk,_=reps[r]; M,A=case.split(',')
    env=dict(os.environ,BGS16_CASE=case,BGS16_BLOCK=str(blk),OMP_NUM_THREADS='2',OPENBLAS_NUM_THREADS='2',PYTHONDONTWRITEBYTECODE='1')
    for T in ('V','E'):
        for kind,cl in (('u','none'),('t',CL)):
            pre=f'{OUT}/data/{T}_r{r}_{kind}'; os.makedirs(f'{OUT}/data',exist_ok=True)
            nb=1 if kind=='u' else 8
            if all(f'{T}{r}{kind}{b}' in res for b in range(nb)): continue
            subprocess.run(['nice','-n','10',PY,'code/certG_build16.py',T,M,A]+PAR[T]+[cl,pre,'128',K2[T]],env=env,check=True,
                           stdout=open(f'{pre}_build.log','w'),stderr=subprocess.STDOUT)
            Bn=json.load(open(pre+'.json')); Ba=json.load(open(f'data/cert/{T}_r{r}_{kind}.json'))
            same_build={k:(Bn[k]==Ba[k]) for k in ('trace_norm','Xnorm','Delta','delta1','D')}
            for b in range(nb):
                ca=json.load(open(f'logs/cert/{T}_r{r}_{kind}_b{b}_rest.json')); pa=ca['provenance'] if isinstance(ca['provenance'],dict) else ast.literal_eval(ca['provenance'])
                shm=sha(f'{pre}_b{b}_mid.npy'); shr=sha(f'{pre}_b{b}_rad.npy')
                outj=f'{OUT}/{T}_r{r}_{kind}_b{b}_rest.json'
                subprocess.run(['nice','-n','10',PY,'code/rig_spec.py',pre,str(b),'rest',ca['R'],'0','64',outj],env=env,
                               stdout=open(outj.replace('.json','.log'),'w'),stderr=subprocess.STDOUT)
                cn=json.load(open(outj))
                res[f'{T}{r}{kind}{b}']=dict(case=case,blk=blk,R=ca['R'],sha_mid_match=shm==pa['mid_sha256'],sha_rad_match=shr==pa['rad_sha256'],
                    build_same=same_build,cert_author=ca['certified'],cert_ref=cn['certified'],F_author=ca['F_R2'],F_ref=cn.get('F_R2'),
                    SY_author=ca['SY_R'],SY_ref=cn.get('SY_R'))
                print(r,T,kind,b,res[f'{T}{r}{kind}{b}'],flush=True)
                for s in ('mid','rad'): os.remove(f'{pre}_b{b}_{s}.npy')
                json.dump(res,open(f'{OUT}/ref_cert16.json','w'),indent=1)
print('REF_DONE',flush=True)
