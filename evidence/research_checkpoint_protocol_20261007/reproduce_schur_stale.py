"""Independent reproduction of stale output acceptance; never edits checkout."""
from pathlib import Path
import hashlib, importlib.util, json, tempfile
ROOT=Path('/workspace/shared/bgs_r6_repair_checkout')
SNAP=Path('/workspace/shared/bgs_checkpoint_source_review/snapshots/d59bede7888fc5da5d123ea628ccf7e3faa3245fe8aba154e1454434a93f12ee_full_replay.py')
spec=importlib.util.spec_from_file_location('audited_schur',SNAP);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
with tempfile.TemporaryDirectory(prefix='bgs-independent-stale-schur-',dir='/workspace/shared/bgs_checkpoint_source_review') as tmp:
 root=Path(tmp)/'root'; output=Path(tmp)/'output'; output.mkdir()
 manifest=(ROOT/m.BINDING_PATH).read_bytes(); rows=json.loads(manifest)['files']; files={**rows,m.BINDING_PATH:hashlib.sha256(manifest).hexdigest(),'computations/verification/schur/full_replay.py':'','computations/verification/balanced_pair_schur.py':''}
 for rel in files:
  p=root/rel;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes((ROOT/rel).read_bytes())
 for family,entry in m.FAMILIES.items():
  (output/(family+'_normal.json')).write_bytes((ROOT/entry['expected']).read_bytes())
 called=[]
 def no_op(command,directory,family,timeout=None):
  called.append(family)
  return {'command':command,'runtime_seconds':0.0,'exit_status':0,'status':'completed','stdout':'','stderr':''}
 m.execute=no_op
 result=m.run_replay(output,['normal'],False,root=root)
 report=json.loads((output/'comparison.json').read_text())
 print(json.dumps({'audited_wrapper_sha256':hashlib.sha256(SNAP.read_bytes()).hexdigest(),'optimization':__import__('sys').flags.optimize,'run_return':result,'no_op_families':called,'status':report['status'],'inputs_unchanged':report['inputs_unchanged'],'defect':'No child wrote any result; prefilled outputs were accepted as fresh execution.'},indent=2))
