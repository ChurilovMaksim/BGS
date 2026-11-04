import json,hashlib,pathlib,subprocess
R=pathlib.Path('.'); E='evidence/executions/20261104/h6_p0'; V='computations/verification/h6_p0'
sh=lambda p: hashlib.sha256(open(p,'rb').read()).hexdigest()
files=[str(p) for p in sorted(R.glob(f'{V}/**/*')) if p.is_file() and '__pycache__' not in str(p)]
files+=['formalization/Bgs/H6LemmaW.lean']+[str(p) for p in sorted(R.glob(E+'/**/*')) if p.is_file() and p.name!='receipt.json']
C={c['id']:c for c in json.load(open('record/claims.json'))['claims']}
base=subprocess.check_output(['git','rev-parse','origin/main']).decode().strip()
rec={'schema':'bgs-h6-p0-integration-receipt-v1','base':f'ChurilovMaksim/BGS origin/main {base[:8]}','branch':'h6-p0-lemmaW','prepared_on':'2026-11-04',
 'ids':{i:C[i]['state'] for i in ('BGS-TRACE-342','BGS-TRACE-343')},
 'author_report':f'{V}/REPORT_P4_v2.md (v1 kept as {V}/REPORT_P4_v1.md)','referee':f'{E}/referee/AUDIT.md (hostile referee audit/p4, 2026-11-04)',
 'referee_fixes_applied':['1: e^{beta Rc} in log K (beta Rc = 10 for 8V, 8.75 for 8E)','2: A_J <= 4/3 (both signs)','3: Lemma I one-step structure [P] (TRACE-197/249/294, cert_lift.py)','4: robust-variant wording; u-normalisation of (C1) stated as assumption','5: eps_0/eps renamed eps_u','6: H1-bad [P] -> [assessment]; J0 = 12 registered'],
 'arb_rerun':{'command':f'cd {V} && python code/h6_p0.py && python code/h6_variants.py','python':'3.13.5, python-flint 0.9.0 (arb, 128-bit)','wall_seconds':11,
   'result':{'8V_k4000_p0':28424695,'8E_k1000_p0':3934,'cover_intervals_8V':389,'cover_intervals_8E':61,'tail_ok':True,'restart_on_failure':True},
   'matches_referee':True,'logs':[f'{V}/logs/h6_p0.json',f'{V}/logs/h6_p0.out',f'{V}/logs/h6_variants.json',f'{V}/logs/h6_variants.out']},
 'not_rerun':'lemmaW_trial.py (1087 s), lemmaW_full.py and r2_cert_x0.py: logs are the original P4 runs (code bytes differ only by the assertion guard and log paths)',
 'lean':{'files':['formalization/Bgs/H6LemmaW.lean'],'theorems':7,'sorry':False,'native_decide':False,'axioms':'none','build':f'{E}/lake_build_H6LemmaW.log','scope':'lake build Bgs.H6LemmaW only (2 jobs); no full Bgs build'},
 'sha256':{f:sh(f) for f in files}}
open(E+'/receipt.json','w').write(json.dumps(rec,indent=1,ensure_ascii=False)+'\n'); print(len(files))
