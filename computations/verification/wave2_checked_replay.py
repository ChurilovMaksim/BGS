#!/usr/bin/env python3
"""Durable authenticated Wave2 finite controls; never an asymptotic proof.

Execution provenance is validated separately, never compared as science.
Original archived code is unchanged; the disclosed runtime adapter redirects
historical snapshot metadata and preserves assertion checks under optimization.
"""
from __future__ import annotations
import argparse
import copy
import hashlib
import json
import math
import os
from pathlib import Path, PurePosixPath
import re
import resource
import subprocess
import sys
import tempfile
import time

ROOT=Path(__file__).resolve().parents[2]
CONTRACT='record/wave2_replay_contract.json'
BINDINGS='record/wave2_replay_source_bindings.json'
INPUTS='record/wave2_scoped_input_bindings.json'

def require(ok,message):
    if not ok:
        raise RuntimeError(message)

def digest(data):
    return hashlib.sha256(data).hexdigest()

def strict_json(raw):
    def unique(pairs):
        result={}
        for key,value in pairs:
            require(key not in result,'duplicate JSON key: '+key)
            result[key]=value
        return result
    def bad(value):
        raise RuntimeError('nonfinite JSON constant: '+value)
    def finite_float(value):
        number=float(value)
        require(math.isfinite(number),'nonfinite JSON number: '+value)
        return number
    return json.loads(raw,object_pairs_hook=unique,parse_constant=bad,parse_float=finite_float)

def safe_path(root,rel):
    path=PurePosixPath(rel)
    require(isinstance(rel,str) and path.parts and not path.is_absolute() and '..' not in path.parts and str(path)==rel and '\\' not in rel,'unsafe path: '+str(rel))
    p=root/rel
    require(p.is_file() and not p.is_symlink() and p.resolve().is_relative_to(root.resolve()),'missing/nonregular/escaping input: '+rel)
    return p

def source_bytes(root=ROOT):
    bindings=strict_json(safe_path(root,BINDINGS).read_bytes())
    require(bindings['schema']=='bgs-wave2-replay-source-bindings-v1','unknown binding schema')
    cached={}
    for rel,expected in bindings['files'].items():
        data=safe_path(root,rel).read_bytes()
        require(digest(data)==expected,'changed source: '+rel)
        cached[rel]=data
    require(CONTRACT in cached and INPUTS in cached,'missing contract/input closure')
    return cached

def equal_science(expected,observed):
    differences=[]
    def walk(a,b,path):
        if type(a) is not type(b):
            differences.append(path+': type')
        elif isinstance(a,dict):
            for k in sorted(set(a)|set(b)):
                if k not in a or k not in b:
                    differences.append(path+'/'+k+': missing/extra')
                else:
                    walk(a[k],b[k],path+'/'+k)
        elif isinstance(a,list):
            if len(a)!=len(b):differences.append(path+': length')
            for i,(x,y) in enumerate(zip(a,b)):walk(x,y,path+'/'+str(i))
        elif a!=b:
            differences.append(path+': value')
    walk(expected,observed,'')
    require(not differences,'scientific mismatch: '+repr(differences[:16]))

def validate_provenance(value,policy,*,task,context,observed):
    if policy=='seconds':
        require(type(value) in (float,int) and math.isfinite(value) and 0<=value<=task['timeout_seconds'],'invalid elapsed seconds')
    elif policy=='optimization':
        require(type(value) is int and value in (0,1,2),'invalid optimization flag')
        if observed:require(value==context['optimization'],'child optimization differs')
    elif policy=='version':
        require(type(value) is str and len(value)<=256 and re.fullmatch(r'[0-9]+(?:\.[0-9]+)+(?:[a-zA-Z0-9.+-]*)',value) is not None,'invalid software version')
    elif policy=='software':
        require(type(value) is dict and set(value)=={'python','numpy'},'unexpected software fields')
        for version in value.values():validate_provenance(version,'version',task=task,context=context,observed=observed)
    elif policy=='source_digest':
        require(value==context['source_digest'],'source provenance differs')
    elif policy=='extra_digest':
        require(value in context['extra_digests'],'shared source/proof provenance differs')
    elif policy=='historical_digest':
        require(value==context['historical_manifest_digest'],'historical snapshot identity differs')
    elif policy=='scoped_manifest_digest':
        expected=context['scoped_manifest_digest'] if observed else context['historical_manifest_digest']
        require(value==expected,'snapshot adapter provenance differs')
    elif policy=='historical_pins':
        require(type(value) is dict and value,'empty historical source pins')
        for rel,sha in value.items():
            require(rel in context['snapshot_pins'] and sha==context['snapshot_pins'][rel],'historical source pin differs: '+rel)
    else:
        raise RuntimeError('unknown provenance policy: '+str(policy))

def numeric_diagnostic_specs(name):
    absolute={'comparison':'finite_nonnegative_reference_difference','absolute_tolerance':1e-12,'relative_tolerance':0.0}
    scaled={'comparison':'finite_nonnegative_reference_difference','absolute_tolerance':1e-12,'relative_tolerance':1e-12}
    result={}
    if name=='convex_independent_float':
        result['/largest_equalities_absolute_residual']={'comparison':'finite_nonnegative_exclusive_upper_bound','exclusive_upper_bound':2e-9}
    elif name=='rounding':
        for i in range(3):
            for field in ['epsilon','reverse_difference','max_charge_difference','max_word_error_over_bound']:
                result[f'/floating_norm_controls/{i}/{field}']=dict(absolute)
        for i in range(2):
            for field in ['epsilon','reverse_norm','P_centered_norm']:
                result[f'/floating_split_controls/{i}/{field}']=dict(absolute)
            result[f'/floating_split_controls/{i}/root_reconstruction_error']={'comparison':'finite_nonnegative_exclusive_upper_bound','exclusive_upper_bound':2e-12}
        for field in ['C_w','sum_w_r_over_L']:result['/smooth_band_control/'+field]=dict(absolute)
        for i in range(3):result[f'/smooth_band_control/finite_return_sums/{i}/return_lower_bound']=dict(absolute)
    elif name=='ward_covariance':
        for i in [1,2,3,4,5,7,8,9,10,11]:
            result[f'/checks/{i}/norm_error']=dict(absolute)
            result[f'/checks/{i}/theorem_bound']=dict(scaled)
    return result


def diagnostic_location(value,path):
    parts=path.split('/')[1:]
    require(path.startswith('/') and parts and all(parts),'invalid numeric diagnostic path')
    for part in parts[:-1]:
        if type(value) is dict:
            require(part in value,'missing numeric diagnostic path: '+path);value=value[part]
        elif type(value) is list:
            require(part.isdigit() and str(int(part))==part and int(part)<len(value),'missing numeric diagnostic index: '+path);value=value[int(part)]
        else:raise RuntimeError('numeric diagnostic nested schema differs: '+path)
    require(type(value) is dict and parts[-1] in value,'missing declared numeric diagnostic: '+path)
    return value,parts[-1]


def finite_diagnostic(value,path):
    require(type(value) in (int,float),'numeric diagnostic must be a nonbool number: '+path)
    try:finite=math.isfinite(value)
    except OverflowError:finite=False
    require(finite and value>=0,'numeric diagnostic must be finite nonnegative: '+path)


def numeric_relations(value,name):
    relations=[]
    if name=='rounding':
        for i,row in enumerate(value['floating_norm_controls']):
            eps=row['epsilon'];k=row['K']
            require(type(k) is int and k>=2 and eps>0,'invalid rounding diagnostic parameters')
            require(eps<=math.pi/k+1e-12,'rounding epsilon violates original bound')
            require(row['reverse_difference']<=2*eps+1e-12,'rounding reverse difference violates original bound')
            require(row['max_charge_difference']<=2*eps+1e-12,'rounding charge difference violates original bound')
            # Consequence of every original ell-specific telescoping inequality.
            # The original checker still executes every such inequality unchanged.
            require(row['max_word_error_over_bound']<=1+1e-12/eps,'rounding word ratio violates original bound consequence')
        for row in value['floating_split_controls']:
            limit=row['bound'];finite_diagnostic(limit,'split bound parameter')
            require(row['epsilon']<=limit+2e-12,'split epsilon violates original bound')
            require(row['P_centered_norm']<=2*limit+4e-12,'split P norm violates original bound')
            require(row['root_reconstruction_error']<2e-12,'split reconstruction violates original strict bound')
        band=value['smooth_band_control']
        require(band['sum_w_r_over_L']>band['C_w']+1,'smooth return sum violates original lower bound')
        relations=['epsilon<=pi/K+1e-12','reverse_difference<=2epsilon+1e-12','max_charge_difference<=2epsilon+1e-12','max_word_error_over_bound<=1+1e-12/epsilon (original per-ell checks unchanged)','split epsilon<=bound+2e-12','split P_centered_norm<=2bound+4e-12','root_reconstruction_error<2e-12','sum_w_r_over_L>C_w+1']
    elif name=='ward_covariance':
        for row in value['checks']:
            if row['m']!=1:require(row['norm_error']<=row['theorem_bound']+1e-12,'Ward norm error violates original bound')
        relations=['norm_error<=theorem_bound+1e-12 for m>=2; exact m=1 zeros unchanged']
    elif name=='convex_independent_float':
        require(value['largest_equalities_absolute_residual']<2e-9,'Wave3 residual violates original strict bound')
        relations=['largest_equalities_absolute_residual<2e-9; all original 8708 checker assertions unchanged']
    return relations


def compare_numeric_diagnostics(expected,observed,task):
    declared=task.get('numeric_diagnostics',{})
    require(type(declared) is dict,'numeric diagnostic contract must be an object')
    if not declared:return {},[]
    permitted=numeric_diagnostic_specs(task.get('name'))
    require(permitted and declared==permitted,'undeclared numeric diagnostic path, nesting, task or policy')
    equal_science(permitted,declared)
    details={}
    for path,policy in declared.items():
        ep,ek=diagnostic_location(expected,path);op,ok=diagnostic_location(observed,path)
        a=ep[ek];b=op[ok];finite_diagnostic(a,path);finite_diagnostic(b,path)
        if policy['comparison']=='finite_nonnegative_exclusive_upper_bound':
            require(a<policy['exclusive_upper_bound'] and b<policy['exclusive_upper_bound'],'numeric diagnostic outside original strict bound: '+path)
        else:
            tolerance=policy['absolute_tolerance']+policy['relative_tolerance']*abs(a)
            require(abs(b-a)<=tolerance,'numeric diagnostic exceeds declared reference tolerance: '+path)
        details[path]={**policy,'expected':a,'observed':b}
    relations=numeric_relations(expected,task['name']);require(relations==numeric_relations(observed,task['name']),'numeric relation contract changed')
    # Normalize only the comparison copy. Raw payloads and every diagnostic field
    # remain intact; the receipt preserves both numeric values and the policy.
    for path in declared:
        ep,ek=diagnostic_location(expected,path);op,ok=diagnostic_location(observed,path);op[ok]=ep[ek]
    return details,relations

def compare(expected,observed,task,context):
    require(type(expected) is dict and type(observed) is dict,'JSON root must be an object')
    expected=copy.deepcopy(expected);observed=copy.deepcopy(observed)
    original_expected={};original_observed={}
    for key,policy in task['provenance_fields'].items():
        require(key in expected and key in observed,'missing declared provenance: '+key)
        validate_provenance(expected[key],policy,task=task,context=context,observed=False)
        validate_provenance(observed[key],policy,task=task,context=context,observed=True)
        # These declared metadata identities are invariant, unlike runtime or
        # software provenance. The expected maps/hashes are source-authenticated.
        if policy=='historical_pins':
            require(observed[key]==expected[key],'historical source pin map differs: '+key)
        elif policy=='extra_digest':
            require(observed[key]==expected[key],'named extra-source provenance differs: '+key)
        original_expected[key]=expected.pop(key);original_observed[key]=observed.pop(key)
    diagnostics,relations=compare_numeric_diagnostics(expected,observed,task)
    equal_science(expected,observed)
    return {'expected_provenance':original_expected,'observed_provenance':original_observed,
            'numeric_diagnostics':diagnostics,'numeric_relations':relations,
            'scientific_comparison_mode':'strict_typed_exact_with_declared_numeric_diagnostics' if diagnostics else 'strict_typed_exact',
            'scientific_sha256_mode':'comparison_normalized_projection',
            'scientific_sha256_normalized_numeric_paths':sorted(diagnostics),
            'scientific_sha256':digest(json.dumps(observed,sort_keys=True,separators=(',',':')).encode())}

BOOTSTRAP=r'''
import ast, hashlib, json, sys, types
from pathlib import Path
config=json.loads(sys.argv[1]); source=Path(config['source'])
class Adapter(ast.NodeTransformer):
    def __init__(self):self.assertions=0;self.snapshot_redirects=0;self.manifest_redirects=0
    def visit_Assert(self,node):
        self.assertions+=1
        messages=[node.msg] if node.msg is not None else []
        replacement=ast.If(test=ast.UnaryOp(op=ast.Not(),operand=node.test),body=[ast.Raise(exc=ast.Call(func=ast.Name(id='AssertionError',ctx=ast.Load()),args=messages,keywords=[]),cause=None)],orelse=[])
        return ast.copy_location(replacement,node)
    def visit_Assign(self,node):
        targets=[t.id for t in node.targets if isinstance(t,ast.Name)]
        if config['snapshot_adapter'] and set(targets).intersection({'SOURCE','ROOT'}) and isinstance(node.value,ast.Call) and len(node.value.args)==1 and isinstance(node.value.args[0],ast.Constant) and node.value.args[0].value=='/workspace/shared/bgs_checked_checkpoint_validation/source_snapshot':
            node.value.args[0].value=config['snapshot_root'];self.snapshot_redirects+=1
        if config['snapshot_adapter'] and targets==['EXPECTED'] and isinstance(node.value,ast.Constant) and node.value.value==config['historical_manifest_digest']:
            node.value.value=config['scoped_manifest_digest'];self.manifest_redirects+=1
        return self.generic_visit(node)
def execute(path,namespace):
    adapter=Adapter();tree=ast.fix_missing_locations(adapter.visit(ast.parse(path.read_bytes(),filename=str(path))))
    records.append({'source':path.name,'source_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'adapted_ast_sha256':hashlib.sha256(ast.dump(tree,include_attributes=False).encode()).hexdigest(),'assertions_explicit':adapter.assertions,'snapshot_redirects':adapter.snapshot_redirects,'manifest_redirects':adapter.manifest_redirects})
    exec(compile(tree,str(path),'exec'),namespace)
records=[]
sys.path.insert(0,str(source.parent))
for shared in config['shared_modules']:
    path=Path(shared);module=types.ModuleType(path.stem);module.__file__=str(path);sys.modules[path.stem]=module;execute(path,module.__dict__)
sys.argv=[str(source)]
try:
    execute(source,{'__name__':'__main__','__file__':str(source)})
finally:
    Path(config['adapter_receipt']).write_text(json.dumps({'records':records,'python_optimization':sys.flags.optimize},indent=2)+'\n')
'''

def child_limits():
    resource.setrlimit(resource.RLIMIT_AS,(3*2**30,3*2**30))
    resource.setrlimit(resource.RLIMIT_CPU,(180,180))

def output_directory(root,output):
    if output is None:return None
    output=Path(output).absolute()
    require(not any(p.is_symlink() for p in (output,*output.parents)),'symlink output ancestor')
    output=output.resolve();root=root.resolve()
    inside=output.is_relative_to(root)
    require((not inside or output.relative_to(root).parts[0]=='build') and not root.is_relative_to(output),'output overlaps maintained sources')
    output.mkdir(parents=True,exist_ok=True)
    require(output.is_dir() and not any(output.iterdir()),'output directory must be fresh and empty')
    return output

def run(root=ROOT,output=None):
    output=output_directory(root,output)
    receipt={'schema':'bgs-wave2-durable-replay-v1','status':'running','tasks':[],'artifacts':[],
             'python':sys.version,'optimization':sys.flags.optimize,'whole_suite_run':False,
             'formal_compile_run':False,'manuscript_build_run':False,
             'scope':'Six bounded domains; no asymptotic or unavailable-archive execution certification.'}
    def publish():
        if output is not None:(output/'replay_manifest.json').write_text(json.dumps(receipt,indent=2)+'\n')
    def retain(name,data):
        if output is not None:
            (output/name).write_bytes(data);receipt['artifacts'].append({'path':name,'bytes':len(data),'sha256':digest(data)})
    publish()
    try:
        cached=source_bytes(root);contract=strict_json(cached[CONTRACT]);inputs=strict_json(cached[INPUTS]);snapshot_pins={rel:x['sha256'] for rel,x in inputs['files'].items()}
        require(contract['schema']=='bgs-wave2-replay-contract-v1','unknown contract schema')
        receipt['source_hashes']={rel:digest(data) for rel,data in cached.items()}
        receipt['adapter_bootstrap_sha256']=digest(BOOTSTRAP.encode())
        retain('replay_contract.original.json',cached[CONTRACT]);retain('source_bindings.original.json',safe_path(root,BINDINGS).read_bytes());retain('scoped_input_bindings.original.json',cached[INPUTS])
        scoped=(json.dumps({'schema':'bgs-wave2-runtime-scoped-snapshot-v1','files':snapshot_pins},indent=2)+'\n').encode()
        retain('runtime_scoped_snapshot_manifest.json',scoped)
        env=dict(os.environ);env.update(OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1',NUMEXPR_NUM_THREADS='1',PYTHONDONTWRITEBYTECODE='1')
        env['PYTHONOPTIMIZE']='0'
        mode=['-'+'O'*sys.flags.optimize] if sys.flags.optimize else []
        for task in contract['tasks']:
            name=task['name'];capture={};task_receipt={'name':name,'domain':task['domain'],'status':'running'};receipt['tasks'].append(task_receipt);publish()
            expected_bytes=cached[task['expected']];retain(name+'.expected.raw',expected_bytes)
            with tempfile.TemporaryDirectory(prefix='bgs-wave2-'+name+'-') as tmp:
                work=Path(tmp);snapshot=work/'snapshot';snapshot.mkdir();materialized={}
                for rel,row in inputs['files'].items():
                    p=snapshot/rel;p.parent.mkdir(parents=True,exist_ok=True);data=cached[row['source']];require(digest(data)==row['sha256'],'scoped snapshot pin');p.write_bytes(data);materialized[p]=data
                manifest=work/'source_manifest.json';manifest.write_bytes(scoped);materialized[manifest]=scoped
                source=work/task['work_source'];source.parent.mkdir(parents=True,exist_ok=True);source.write_bytes(cached[task['source']]);materialized[source]=cached[task['source']]
                shared=[]
                for rel in task['extra_sources']:
                    p=source.parent/Path(rel).name;p.write_bytes(cached[rel]);materialized[p]=cached[rel]
                    if p.suffix=='.py':shared.append(str(p))
                def authenticate():
                    for p,data in materialized.items():require(p.is_file() and not p.is_symlink() and p.read_bytes()==data,'copied input mutation: '+str(p))
                config={'source':str(source),'snapshot_root':str(snapshot),'snapshot_adapter':task['historical_snapshot_adapter'],
                        'historical_manifest_digest':contract['historical_manifest_sha256'],'scoped_manifest_digest':digest(scoped),
                        'shared_modules':shared,'adapter_receipt':str(work/'adapter_receipt.json')}
                cmd=[sys.executable,*mode,'-c',BOOTSTRAP,json.dumps(config)]
                task_receipt['command']=[sys.executable,*mode,'-c','authenticated declared AST adapter',json.dumps(config)]
                authenticate();start=time.monotonic()
                try:
                    result=subprocess.run(cmd,cwd=source.parent,env=env,capture_output=True,timeout=task['timeout_seconds'],preexec_fn=child_limits)
                    task_receipt.update(exit_status=result.returncode,seconds=time.monotonic()-start)
                    for stream in ['stdout','stderr']:retain(name+'.'+stream,getattr(result,stream))
                except subprocess.TimeoutExpired as error:
                    task_receipt.update(exit_status=None,seconds=time.monotonic()-start)
                    for stream in ['stdout','stderr']:retain(name+'.'+stream,getattr(error,stream) or b'')
                    raise
                adapter=work/'adapter_receipt.json'
                if adapter.is_file():retain(name+'.adapter.json',adapter.read_bytes())
                generated=task.get('optimized_generated_result',task['generated_result']) if mode else task['generated_result']
                if generated is not None:
                    observed_path=source.parent/generated
                    if observed_path.is_file() and not observed_path.is_symlink():observed_bytes=observed_path.read_bytes();retain(name+'.actual.raw',observed_bytes)
                    else:observed_bytes=None
                else:observed_bytes=result.stdout;retain(name+'.actual.raw',observed_bytes)
                require(result.returncode==0,name+' child failed: '+result.stderr.decode(errors='replace')[-1500:])
                require(observed_bytes is not None and len(observed_bytes)<2**20,'missing/oversized fresh result')
                authenticate()
                context={'optimization':sys.flags.optimize,'source_digest':digest(cached[task['source']]),'extra_digests':{digest(cached[p]) for p in task['extra_sources']},'historical_manifest_digest':contract['historical_manifest_sha256'],'scoped_manifest_digest':digest(scoped),'snapshot_pins':snapshot_pins}
                details=compare(strict_json(expected_bytes),strict_json(observed_bytes),task,context)
                task_receipt.update(status='passed',source_sha256=context['source_digest'],expected_raw_sha256=digest(expected_bytes),actual_raw_sha256=digest(observed_bytes),**details)
                require(adapter.is_file(),'missing runtime adapter receipt')
                ar=strict_json(adapter.read_bytes());require(ar['python_optimization']==context['optimization'],'adapter optimization mismatch')
                if task['historical_snapshot_adapter']:require(sum(x['snapshot_redirects'] for x in ar['records'])==1,'historical path redirect not exact')
                require(sum(x['manifest_redirects'] for x in ar['records'])==(1 if name=='rounding' else 0),'unexpected manifest redirect')
                publish()
        require(source_bytes(root)==cached,'original sources changed during execution')
        receipt.update(status='passed',original_sources_unchanged=True,copied_inputs_authenticated=True,expected_bytes_cached_before_execution=True,scientific_equality=True,scientific_comparison_mode='strict_typed_exact_with_contract_declared_numeric_diagnostics',provenance_excluded_from_scientific_comparison=True)
        publish();return receipt
    except Exception as error:
        if receipt['tasks'] and receipt['tasks'][-1]['status']=='running':receipt['tasks'][-1].update(status='failed',failure=str(error))
        receipt.update(status='failed',failure=str(error));publish();raise

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check-sources',action='store_true');parser.add_argument('--output-dir',type=Path)
    args=parser.parse_args()
    if args.check_sources:
        source_bytes();print('wave2-replay source closure: OK')
    else:
        result=run(output=args.output_dir);print('wave2-replay: '+result['status']+' ('+str(len(result['tasks']))+' tasks, six bounded domains)')

if __name__=='__main__':main()
