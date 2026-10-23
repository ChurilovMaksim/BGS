"""Independent pre-freeze failure demonstrations. Fixture writes stay in review dir."""
from pathlib import Path
import hashlib, importlib.util, json, os, subprocess, sys, tempfile
ROOT=Path('/workspace/shared/bgs_r6_repair_checkout')
SNAP=Path(sys.argv[1]) if len(sys.argv)>1 else Path('/workspace/shared/bgs_checkpoint_source_review/snapshots/4dd35155a64f926b3807ab2559de4403aad6b677e67f1aab0f89f568999e8688_research_checkpoint_replay.py')
spec=importlib.util.spec_from_file_location('audited_checkpoint',SNAP);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
rows=[]
def attempt(name,fn):
 try:
  fn(); rows.append({'test':name,'accepted':True})
 except Exception as e:
  rows.append({'test':name,'accepted':False,'exception':type(e).__name__,'diagnostic':str(e)[:1000]})
for key,bad in [('python',None),('sympy',{}),('compiler_command',False)]:
 attempt('invalid_exempt_'+key,lambda key=key,bad=bad:m.compare({'science':1,key:('3.12.14' if key!='compiler_command' else ['g++','-std=c++17','-O2','-Wall','-Wextra','-pedantic','original.cpp','-o','original'])}, {'science':1,key:bad},[key]))
with tempfile.TemporaryDirectory(prefix='checkpoint-gap-',dir='/workspace/shared/bgs_checkpoint_source_review') as tmp:
 base=Path(tmp); work=base/'work'; raw=work/'evidence/research_checkpoint_20261007/raw'; raw.mkdir(parents=True)
 escaped=base/'escaped';escaped.mkdir();out=raw/'result';out.mkdir()
 source=raw/'producer.py';generated=out/'checks.json';generated.write_text('{"answer":7}')
 source.write_text("from pathlib import Path\np=Path(__file__).parent/'result'\np.rmdir()\np.symlink_to("+repr(str(escaped))+",target_is_directory=True)\n(p/'checks.json').write_text('{\"answer\":7}')\n")
 task={'name':'ancestor_escape','source':source.relative_to(work).as_posix(),'arguments':[], 'timeout_seconds':10,'generated_result':generated.relative_to(work).as_posix()}
 attempt('generated_output_ancestor_escape',lambda:m.compare({'answer':7},m.final_json(m.execute_task(work,task,dict(os.environ),['-O'] if sys.flags.optimize else [])),[]))
 rows[-1]['outside_result_written']=(escaped/'checks.json').exists()
with tempfile.TemporaryDirectory(prefix='checkpoint-copy-gap-',dir='/workspace/shared/bgs_checkpoint_source_review') as tmp:
 root=Path(tmp);raw=root/'evidence/research_checkpoint_20261007/raw';raw.mkdir(parents=True)
 p1=raw/'first.py';p2=raw/'second.py'
 p2.write_text("# Original actual check\nassert 2+2==4\nprint('{\"answer\":2}')\n")
 p1.write_text("from pathlib import Path\nPath(__file__).with_name('second.py').write_text(\"print('{\\\"answer\\\":2}')\\n\")\nprint('{\"answer\":1}')\n")
 e1=raw/'e1.json';e1.write_text('{"answer":1}');e2=raw/'e2.json';e2.write_text('{"answer":2}')
 cpp=raw/'check.cpp';cpp.write_text('// nonexecuted C++ fixture\n');ce=raw/'cpp.json'
 negative={'fault':'omit low-digit carry into high digit','returncode':2,'diagnostic':'literal cyclic carry identity'}
 ce.write_text(json.dumps({'ok':True,'negative_control':negative,'compiler_command':[]}))
 contract={'tasks':[{'name':name,'source':p.relative_to(root).as_posix(),'arguments':[],'expected':e.relative_to(root).as_posix(),'provenance_root_fields':[],'timeout_seconds':10} for name,p,e in [('first',p1,e1),('second',p2,e2)]],'cpp':{'source':cpp.relative_to(root).as_posix(),'expected':ce.relative_to(root).as_posix(),'provenance_root_fields':['compiler_command'],'timeout_seconds':10}}
 co=root/m.CONTRACT;co.parent.mkdir(parents=True,exist_ok=True);co.write_text(json.dumps(contract))
 files=[p1,p2,e1,e2,cpp,ce,co];binding=root/m.BINDINGS;binding.write_text(json.dumps({'schema':'bgs-checkpoint-source-bindings-v1','files':{p.relative_to(root).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files}}))
 old_run=m.subprocess.run
 def simulated_cpp(command,**kwargs):
  if command[0]=='g++':return subprocess.CompletedProcess(command,0,b'',b'')
  if command[0].endswith('/check_growing'):
   return subprocess.CompletedProcess(command,2,b'',b'literal cyclic carry identity') if '--inject-bad-carry' in command else subprocess.CompletedProcess(command,0,b'{"ok":true}',b'')
  return old_run(command,**kwargs)
 m.subprocess.run=simulated_cpp
 before=p2.read_bytes()
 attempt('copied_future_executable_replaced',lambda:m.run(root=root))
 rows[-1]['original_second_source_unchanged']=p2.read_bytes()==before
 m.subprocess.run=old_run
print(json.dumps({'audited_wrapper_sha256':hashlib.sha256(SNAP.read_bytes()).hexdigest(),'optimization':sys.flags.optimize,'fixtures':rows,'scope':'Actual Python task subprocesses; C++ subprocesses simulated only to avoid irrelevant compilation.'},indent=2))
