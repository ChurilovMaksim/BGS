from pathlib import Path
import datetime,hashlib,json,os,shutil,subprocess,tempfile,time
ROOT=Path('/workspace/shared/bgs_schur_reduction_promotion')
OUT=ROOT/'evidence/schur_reduction_20261007/qa';OUT.mkdir(parents=True,exist_ok=True)
records=[]
def execute(argv,label,cwd=ROOT,timeout=90):
 start=time.monotonic();p=subprocess.run(argv,cwd=cwd,env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1',NUMEXPR_NUM_THREADS='1'),capture_output=True,text=True,timeout=timeout)
 item={'check':label,'command':argv,'cwd':str(cwd),'exit_status':p.returncode,'stdout':p.stdout,'stderr':p.stderr,'runtime_seconds':time.monotonic()-start};records.append(item)
 if p.returncode:raise RuntimeError(label+': '+p.stderr)
 return p
for python in ['python3','/usr/bin/python3.13']:
 for flags in [[],['-O']]:
  execute([python,'-B',*flags,str(ROOT/'computations/maintenance/tests/test_schur_portability.py'),'-v'],python+' '+str(flags)+' adversarial tests')
  sources=[ROOT/'computations/verification/balanced_pair_schur.py']+list((ROOT/'computations/verification/schur').glob('*.py'))
  code='''import importlib.util,os,pathlib,resource
paths=PATHS
before=resource.getrlimit(resource.RLIMIT_CPU),resource.getrlimit(resource.RLIMIT_AS),os.sched_getaffinity(0),sorted(str(p) for p in pathlib.Path('.').rglob('*'))
for i,p in enumerate(paths):
 s=importlib.util.spec_from_file_location('silent_'+str(i),p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
after=resource.getrlimit(resource.RLIMIT_CPU),resource.getrlimit(resource.RLIMIT_AS),os.sched_getaffinity(0),sorted(str(p) for p in pathlib.Path('.').rglob('*'))
if before!=after:raise RuntimeError('import side effects')
'''.replace('PATHS',repr([str(p) for p in sources]))
  with tempfile.TemporaryDirectory(prefix='bgs-schur-silent-') as d:
   p=execute([python,'-B',*flags,'-c',code],python+' '+str(flags)+' all maintained silent imports',Path(d),30)
   if p.stdout or p.stderr:raise RuntimeError('non-silent import')
validator=ROOT/'evidence/schur_reduction_20261007/raw/review/validate_manifest.py'
for family in ['author','review']:
 raw=ROOT/'evidence/schur_reduction_20261007/raw'/family
 execute(['python3','-B',str(validator),str(raw/'execution_manifest.json'),'--root',str(raw)],'lossless '+family+' execution-manifest validation')
 execute(['sha256sum','-c','SHA256SUMS'],'lossless '+family+' historical delivery seal',raw)
for runtime in ['python312','python313']:
 folder=ROOT/'evidence/schur_reduction_20261007/portable'/runtime
 execute(['python3','-B',str(validator),str(folder/'execution_manifest.json'),'--root',str(ROOT)],runtime+' portable manifest validation')
for family in ['author','independent']:
 blobs=[(ROOT/f'evidence/schur_reduction_20261007/portable/{runtime}/{family}_{mode}_scientific.json').read_bytes() for runtime in ['python312','python313'] for mode in ['normal','optimized']]
 if len(set(blobs))!=1:raise RuntimeError('scientific cross-runtime identity')
 records.append({'check':family+' all four scientific byte streams identical','passed':True,'scientific_sha256':hashlib.sha256(blobs[0]).hexdigest()})
# Complete raw-directory originals, not just the central proofs, remain lossless.
for family,source in [('author',Path('/workspace/shared/bgs_balanced_phase_closure')),('review',Path('/workspace/shared/bgs_schur_reduction_review'))]:
 count=0
 for p in source.rglob('*'):
  if not p.is_file() or '__pycache__' in p.parts or p.suffix in ['.pyc','.pyo']:continue
  target=ROOT/'evidence/schur_reduction_20261007/raw'/family/p.relative_to(source)
  if p.read_bytes()!=target.read_bytes():raise RuntimeError('raw byte mismatch '+str(p))
  count+=1
 records.append({'check':family+' lossless directory comparison','passed':True,'files':count})
# Real relocation: copy the complete source-bound tree; run from an unrelated cwd.
with tempfile.TemporaryDirectory(prefix='bgs-schur-relocated-') as d:
 clone=Path(d)/'portable-overlay';shutil.copytree(ROOT,clone,ignore=shutil.ignore_patterns('portable','qa','__pycache__'))
 for python in ['python3','/usr/bin/python3.13']:
  p=execute([python,'-B',str(clone/'computations/verification/balanced_pair_schur.py')],python+' relocated no-argument bounded replay',Path('/tmp'),100)
  if p.stdout or p.stderr:raise RuntimeError('non-silent relocated wrapper')
# Strict whitespace/EOF lint of maintained files; historical exception explicitly recorded.
issues=[];exceptions=[]
for p in ROOT.rglob('*'):
 if not p.is_file():continue
 if '__pycache__' in p.parts or p.suffix in ['.pyc','.pyo']:raise RuntimeError('generated cache '+str(p))
 try:s=p.read_text()
 except UnicodeError:continue
 defects=[]
 if s and not s.endswith('\n'):defects.append('missing EOF newline')
 if s.endswith('\n\n'):defects.append('extra EOF blank line')
 if any(x.rstrip(' \t')!=x for x in s.splitlines()):defects.append('trailing whitespace')
 if defects:
  row={'path':str(p.relative_to(ROOT)),'defects':defects}
  if '/raw/' in str(p):exceptions.append(row)
  else:issues.append(row)
if issues:raise RuntimeError('maintained whitespace failure '+str(issues))
records.append({'check':'maintained whitespace and EOF plus cache exclusion','passed':True,'lossless_historical_exceptions':exceptions})
(OUT/'report.json').write_text(json.dumps({'status':'passed','observed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'records':records,'scope':'Portable bounded finite controls only. Analytic asymptotics remain OPEN.'},indent=2)+'\n')
print('QA passed:',len(records),'records')
