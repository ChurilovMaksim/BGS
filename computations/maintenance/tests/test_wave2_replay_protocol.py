"""Regression coverage for scientific/provenance separation and durable failures."""
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[3]
spec=importlib.util.spec_from_file_location('wave2_replay',ROOT/'computations/verification/wave2_checked_replay.py')
w=importlib.util.module_from_spec(spec);spec.loader.exec_module(w)

class ScienceProtocol(unittest.TestCase):
    def setUp(self):
        self.task={'timeout_seconds':180,'provenance_fields':{'elapsed_seconds':'seconds','python':'version','python_optimization':'optimization','script_sha256':'source_digest'}}
        self.context={'optimization':0,'source_digest':'a'*64,'extra_digests':{'b'*64},'historical_manifest_digest':'c'*64,'scoped_manifest_digest':'d'*64,'snapshot_pins':{'p':'e'*64}}
        self.expected={'checks':[{'n':3,'exact':'2/3','passed':True}],'elapsed_seconds':1.0,'python':'3.12.14','python_optimization':0,'script_sha256':'a'*64}
    def compare(self,observed):return w.compare(self.expected,observed,self.task,self.context)
    def test_runtime_versions_are_not_science(self):
        v=copy.deepcopy(self.expected);v.update(elapsed_seconds=17.2,python='3.14.0');r=self.compare(v)
        self.assertNotEqual(r['expected_provenance'],r['observed_provenance'])
    def test_optimization_is_provenance(self):
        v=copy.deepcopy(self.expected);v['python_optimization']=1;self.context['optimization']=1;self.compare(v)
    def test_changed_exact_result_fails(self):
        v=copy.deepcopy(self.expected);v['checks'][0]['exact']='3/2'
        with self.assertRaisesRegex(RuntimeError,'scientific mismatch'):self.compare(v)
    def test_extra_scientific_field_fails(self):
        v=copy.deepcopy(self.expected);v['compiler']='unreviewed'
        with self.assertRaisesRegex(RuntimeError,'scientific mismatch'):self.compare(v)
    def test_boolean_integer_type_fails(self):
        v=copy.deepcopy(self.expected);v['checks'][0]['passed']=1
        with self.assertRaisesRegex(RuntimeError,'type'):self.compare(v)
    def test_missing_check_fails(self):
        v=copy.deepcopy(self.expected);v['checks']=[]
        with self.assertRaisesRegex(RuntimeError,'length'):self.compare(v)
    def test_nan_runtime_fails(self):
        v=copy.deepcopy(self.expected);v['elapsed_seconds']=float('nan')
        with self.assertRaisesRegex(RuntimeError,'invalid elapsed'):self.compare(v)
    def test_negative_runtime_fails(self):
        v=copy.deepcopy(self.expected);v['elapsed_seconds']=-1
        with self.assertRaisesRegex(RuntimeError,'invalid elapsed'):self.compare(v)
    def test_bool_runtime_fails(self):
        v=copy.deepcopy(self.expected);v['elapsed_seconds']=True
        with self.assertRaisesRegex(RuntimeError,'invalid elapsed'):self.compare(v)
    def test_bad_version_fails(self):
        v=copy.deepcopy(self.expected);v['python']='../../executable'
        with self.assertRaisesRegex(RuntimeError,'invalid software'):self.compare(v)
    def test_wrong_code_hash_fails(self):
        v=copy.deepcopy(self.expected);v['script_sha256']='f'*64
        with self.assertRaisesRegex(RuntimeError,'source provenance differs'):self.compare(v)
    def test_missing_provenance_fails(self):
        v=copy.deepcopy(self.expected);del v['python']
        with self.assertRaisesRegex(RuntimeError,'missing declared'):self.compare(v)
    def test_unknown_provenance_policy_fails(self):
        self.task['provenance_fields']['python']='ignore_anything'
        with self.assertRaisesRegex(RuntimeError,'unknown provenance'):self.compare(self.expected)
    def test_exponent_overflow_json_fails(self):
        with self.assertRaisesRegex(RuntimeError,'nonfinite JSON number'):w.strict_json('{"a":1e309}')
    def test_duplicate_json_fails(self):
        with self.assertRaisesRegex(RuntimeError,'duplicate JSON'):w.strict_json('{"a":1,"a":2}')
    def test_nonfinite_json_fails(self):
        with self.assertRaisesRegex(RuntimeError,'nonfinite'):w.strict_json('{"a":NaN}')
    def test_snapshot_metadata_is_separately_validated(self):
        t={'timeout_seconds':180,'provenance_fields':{'manifest':'scoped_manifest_digest','pins':'historical_pins'}}
        a={'scientific':2,'manifest':'c'*64,'pins':{'p':'e'*64}};b={'scientific':2,'manifest':'d'*64,'pins':{'p':'e'*64}}
        w.compare(a,b,t,self.context)
        b['pins']['p']='f'*64
        with self.assertRaisesRegex(RuntimeError,'historical source pin'):w.compare(a,b,t,self.context)
    def test_historical_pin_omission_fails(self):
        self.context['snapshot_pins']['q']='f'*64
        t={'timeout_seconds':180,'provenance_fields':{'pins':'historical_pins'}}
        a={'scientific':2,'pins':{'p':'e'*64,'q':'f'*64}};b=copy.deepcopy(a);del b['pins']['q']
        with self.assertRaisesRegex(RuntimeError,'historical source pin map differs'):w.compare(a,b,t,self.context)
    def test_historical_extra_known_pin_fails(self):
        self.context['snapshot_pins']['q']='f'*64
        t={'timeout_seconds':180,'provenance_fields':{'pins':'historical_pins'}}
        a={'scientific':2,'pins':{'p':'e'*64}};b=copy.deepcopy(a);b['pins']['q']='f'*64
        with self.assertRaisesRegex(RuntimeError,'historical source pin map differs'):w.compare(a,b,t,self.context)
    def test_historical_wrong_known_pin_key_fails(self):
        self.context['snapshot_pins']['q']='e'*64
        t={'timeout_seconds':180,'provenance_fields':{'pins':'historical_pins'}}
        a={'scientific':2,'pins':{'p':'e'*64}};b={'scientific':2,'pins':{'q':'e'*64}}
        with self.assertRaisesRegex(RuntimeError,'historical source pin map differs'):w.compare(a,b,t,self.context)
    def test_named_extra_source_digest_swap_fails(self):
        self.context['extra_digests']={'b'*64,'f'*64}
        t={'timeout_seconds':180,'provenance_fields':{'checker':'extra_digest','proof':'extra_digest'}}
        a={'scientific':2,'checker':'b'*64,'proof':'f'*64};b={'scientific':2,'checker':'f'*64,'proof':'b'*64}
        with self.assertRaisesRegex(RuntimeError,'named extra-source provenance differs'):w.compare(a,b,t,self.context)
    def test_sources_current(self):
        sys.path.insert(0,str(ROOT/'computations/verification'))
        import wave2_portable_replay
        self.assertGreater(len(wave2_portable_replay.sealed_source_bytes()),50)

class DurableProtocol(unittest.TestCase):
    def fixture(self,root):
        root.mkdir();(root/'record').mkdir();(root/'input.txt').write_text('reviewed\n')
        (root/'bad.py').write_text('import json\nprint(json.dumps({"status":"pass","value":2}))\n')
        (root/'expected.json').write_text('{"status":"pass","value":1}\n')
        inp={'schema':'bgs-wave2-scoped-input-bindings-v1','files':{'input.txt':{'source':'input.txt','sha256':w.digest((root/'input.txt').read_bytes())}}}
        (root/w.INPUTS).write_text(json.dumps(inp))
        contract={'schema':'bgs-wave2-replay-contract-v1','historical_manifest_sha256':'c'*64,'tasks':[{'name':'negative','domain':'synthetic','source':'bad.py','expected':'expected.json','work_source':'bad.py','generated_result':None,'extra_sources':[],'provenance_fields':{},'historical_snapshot_adapter':False,'timeout_seconds':10}]}
        (root/w.CONTRACT).write_text(json.dumps(contract))
        files=['bad.py','expected.json','input.txt',w.INPUTS,w.CONTRACT]
        (root/w.BINDINGS).write_text(json.dumps({'schema':'bgs-wave2-replay-source-bindings-v1','files':{p:w.digest((root/p).read_bytes()) for p in files}}))
    def test_failure_keeps_logs_actual_expected_receipt(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)/'sources';self.fixture(root);output=Path(tmp)/'run'
            with self.assertRaisesRegex(RuntimeError,'scientific mismatch'):w.run(root,output)
            d=json.loads((output/'replay_manifest.json').read_text());self.assertEqual(d['status'],'failed');self.assertEqual(d['tasks'][0]['status'],'failed')
            for name in ['negative.expected.raw','negative.actual.raw','negative.stdout','negative.stderr','negative.adapter.json']:
                self.assertTrue((output/name).is_file(),name)
            self.assertEqual((root/'expected.json').read_text(),'{"status":"pass","value":1}\n')
    def test_changed_source_fail_closed(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)/'sources';self.fixture(root);(root/'bad.py').write_text('print("mutation")\n')
            with self.assertRaisesRegex(RuntimeError,'changed source'):w.source_bytes(root)
    def test_output_inside_sources_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);out=root/'evidence/run'
            with self.assertRaisesRegex(RuntimeError,'overlaps maintained'):w.output_directory(root,out)
    def test_nonempty_output_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)/'sources';root.mkdir();out=Path(tmp)/'run';out.mkdir();(out/'old').write_text('old')
            with self.assertRaisesRegex(RuntimeError,'fresh and empty'):w.output_directory(root,out)
    def test_symlink_source_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);(root/'real').write_text('a');(root/'link').symlink_to(root/'real')
            with self.assertRaisesRegex(RuntimeError,'nonregular'):w.safe_path(root,'link')
    def test_shared_asserts_remain_active_under_O(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);shared=root/'shared.py';shared.write_text('def bad():\n    assert False, "shared negative"\n');source=root/'entry.py';source.write_text('from shared import bad\nbad()\n')
            cfg={'source':str(source),'snapshot_root':str(root),'snapshot_adapter':False,'historical_manifest_digest':'c'*64,'scoped_manifest_digest':'d'*64,'shared_modules':[str(shared)],'adapter_receipt':str(root/'adapter.json')}
            for mode in [[],['-O']]:
                p=subprocess.run([sys.executable,*mode,'-c',w.BOOTSTRAP,json.dumps(cfg)],text=True,capture_output=True)
                self.assertNotEqual(p.returncode,0);self.assertIn('shared negative',p.stderr)

class HistoricalAliasProtocol(unittest.TestCase):
    def fixture(self,root):
        s=importlib.util.spec_from_file_location('prior_replay',ROOT/'computations/verification/research_checkpoint_replay.py')
        prior=importlib.util.module_from_spec(s);s.loader.exec_module(prior)
        logical='mathematics/phase_trace_checkpoint.md';archived='evidence/wave2_checked_20261007/raw/provenance/base_navigation/'+logical
        current=root/logical;current.parent.mkdir(parents=True,exist_ok=True);current.write_bytes(b'qualified continuation\n')
        old=root/archived;old.parent.mkdir(parents=True,exist_ok=True);old.write_bytes(b'original reviewed scope\n');digest=w.digest(old.read_bytes())
        data={'schema':'bgs-checkpoint-source-bindings-v1','files':{logical:digest},'historical_inputs':{logical:{'source':archived,'sha256':digest}}}
        binding=root/prior.BINDINGS;binding.parent.mkdir(parents=True,exist_ok=True);binding.write_text(json.dumps(data));return prior,logical,archived,data,binding
    def test_old_input_bytes_preserved_under_logical_path(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);m,logical,archived,d,b=self.fixture(root)
            self.assertEqual(m.source_bytes(root)[logical],b'original reviewed scope\n')
            self.assertEqual((root/logical).read_bytes(),b'qualified continuation\n')
    def test_historical_sha_cannot_refresh(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);m,logical,archived,d,b=self.fixture(root);d['historical_inputs'][logical]['sha256']='f'*64;b.write_text(json.dumps(d))
            with self.assertRaisesRegex(RuntimeError,'pin was refreshed'):m.source_bytes(root)
    def test_historical_target_cannot_change(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);m,logical,archived,d,b=self.fixture(root);d['historical_inputs'][logical]['source']='mathematics/other.md';b.write_text(json.dumps(d))
            with self.assertRaisesRegex(RuntimeError,'unexpected historical target'):m.source_bytes(root)
    def test_other_proofs_cannot_be_overridden(self):
        # Wave 2: radial_shell is now a DECLARED override (see HISTORICAL_TARGETS
        # in research_checkpoint_replay.py), so the guard is asserted on a key
        # that remains undeclared. The guard itself is unchanged: any key
        # outside the hardcoded allowlist still fails closed.
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);m,logical,archived,d,b=self.fixture(root);d['historical_inputs']['mathematics/unrelated_proof.md']={'source':archived,'sha256':d['files'][logical]};b.write_text(json.dumps(d))
            with self.assertRaisesRegex(RuntimeError,'undeclared historical override'):m.source_bytes(root)
    def test_declared_override_resolves(self):
        # Wave 2: a declared override resolves to its allowlisted target bytes.
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);m,logical,archived,d,b=self.fixture(root)
            target='mathematics/actual_charge_radial_shell.md';arch2='archive/evidence/research_checkpoint_20261007/pinned/mathematics_actual_charge_radial_shell.md'
            old=root/arch2;old.parent.mkdir(parents=True,exist_ok=True);old.write_bytes(b'pinned shell bytes\n');digest=w.digest(old.read_bytes())
            d2={'schema':'bgs-checkpoint-source-bindings-v1','files':{target:digest},'historical_inputs':{target:{'source':arch2,'sha256':digest}}}
            b.write_text(json.dumps(d2))
            self.assertEqual(m.source_bytes(root)[target],b'pinned shell bytes\n')
    def test_changed_archive_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);m,logical,archived,d,b=self.fixture(root);(root/archived).write_bytes(b'mutated\n')
            with self.assertRaisesRegex(RuntimeError,'changed source'):m.source_bytes(root)


class NamedNumericDiagnostics(unittest.TestCase):
    def fixture(self,name):
        wave='wave3' if name=='convex_independent_float' else 'wave2'
        contract=json.loads((ROOT/('record/'+wave+'_replay_contract.json')).read_bytes())
        task=copy.deepcopy(next(t for t in contract['tasks'] if t['name']==name))
        task['provenance_fields']={}
        expected=json.loads((ROOT/task['expected']).read_bytes())
        return task,expected
    def value(self,obj,path):
        parent,key=w.diagnostic_location(obj,path);return parent[key]
    def set(self,obj,path,value):
        parent,key=w.diagnostic_location(obj,path);parent[key]=value
    def test_authentic_payloads_and_every_value_policy_retained(self):
        for name in ('rounding','ward_covariance','convex_independent_float'):
            t,e=self.fixture(name);o=copy.deepcopy(e);result=w.compare(e,o,t,{})
            self.assertEqual(set(result['numeric_diagnostics']),set(t['numeric_diagnostics']))
            for path,detail in result['numeric_diagnostics'].items():
                self.assertEqual(detail['expected'],self.value(e,path));self.assertEqual(detail['observed'],self.value(o,path))
            self.assertEqual(e,o)
    def test_all_reference_diagnostics_below_tolerance_pass_and_above_fail(self):
        for name in ('rounding','ward_covariance'):
            t,e=self.fixture(name)
            for path,policy in t['numeric_diagnostics'].items():
                if policy['comparison']!='finite_nonnegative_reference_difference':continue
                value=self.value(e,path);tol=policy['absolute_tolerance']+policy['relative_tolerance']*abs(value)
                o=copy.deepcopy(e);self.set(o,path,value+tol/4)
                with self.subTest(name=name,path=path):
                    result=w.compare(e,o,t,{});self.assertEqual(self.value(o,path),result['numeric_diagnostics'][path]['observed'])
                    self.assertEqual(self.value(e,path),value)
                o=copy.deepcopy(e);self.set(o,path,value+tol*3)
                with self.subTest(name=name,path=path),self.assertRaisesRegex(RuntimeError,'declared reference tolerance'):w.compare(e,o,t,{})
    def test_original_residual_caps_below_at_above(self):
        for name,path,bound in [('rounding','/floating_split_controls/0/root_reconstruction_error',2e-12),('rounding','/floating_split_controls/1/root_reconstruction_error',2e-12),('convex_independent_float','/largest_equalities_absolute_residual',2e-9)]:
            t,e=self.fixture(name);o=copy.deepcopy(e);self.set(o,path,bound/2);w.compare(e,o,t,{})
            for value in (bound,bound*2):
                o=copy.deepcopy(e);self.set(o,path,value)
                with self.subTest(path=path,value=value),self.assertRaisesRegex(RuntimeError,'original strict bound'):w.compare(e,o,t,{})
    def test_nonfinite_nonbool_negative_overflow_nested_diagnostics_fail(self):
        for name,path in [('rounding','/floating_norm_controls/0/epsilon'),('ward_covariance','/checks/1/theorem_bound'),('convex_independent_float','/largest_equalities_absolute_residual')]:
            t,e=self.fixture(name)
            for value in (True,False,-1,float('nan'),float('inf'),10**1000,{'value':1e-14},[1e-14],'1e-14'):
                o=copy.deepcopy(e);self.set(o,path,value)
                with self.subTest(name=name,value=value),self.assertRaises(RuntimeError):w.compare(e,o,t,{})
    def test_missing_or_wrong_nested_location_fails(self):
        for name,path in [('rounding','/floating_split_controls/0/root_reconstruction_error'),('ward_covariance','/checks/1/norm_error'),('convex_independent_float','/largest_equalities_absolute_residual')]:
            t,e=self.fixture(name);o=copy.deepcopy(e);parent,key=w.diagnostic_location(o,path);value=parent.pop(key)
            with self.assertRaisesRegex(RuntimeError,'missing'):w.compare(e,o,t,{})
            parent['nested']={key:value}
            with self.assertRaisesRegex(RuntimeError,'missing'):w.compare(e,o,t,{})
    def test_unlisted_fields_counts_inputs_parameters_exact_zeros_stay_exact(self):
        t,e=self.fixture('convex_independent_float')
        for change in ({'checks_passed':8707},{'z':[0,0.20000000001,0.5,0.99,1]},{'unlisted_float':1e-14}):
            o=copy.deepcopy(e);o.update(change)
            with self.assertRaisesRegex(RuntimeError,'scientific mismatch'):w.compare(e,o,t,{})
        t,e=self.fixture('rounding');o=copy.deepcopy(e);o['floating_split_controls'][0]['bound']+=1e-17
        with self.assertRaisesRegex(RuntimeError,'scientific mismatch'):w.compare(e,o,t,{})
        t,e=self.fixture('ward_covariance');o=copy.deepcopy(e);o['checks'][0]['norm_error']=1e-14
        with self.assertRaisesRegex(RuntimeError,'scientific mismatch'):w.compare(e,o,t,{})
    def test_unlisted_wrong_task_omitted_loosened_or_mistyped_policy_fails(self):
        for case in range(6):
            t,e=self.fixture('convex_independent_float')
            if case==0:t['numeric_diagnostics']['/unlisted']=dict(next(iter(t['numeric_diagnostics'].values())))
            elif case==1:t['name']='other'
            elif case==2:t['numeric_diagnostics']['/largest_equalities_absolute_residual']['exclusive_upper_bound']=3e-9
            elif case==3:t['numeric_diagnostics']={'/nested/largest_equalities_absolute_residual':dict(next(iter(t['numeric_diagnostics'].values())))}
            elif case==4:t['numeric_diagnostics']=[]
            else:t['numeric_diagnostics']['/largest_equalities_absolute_residual']['comparison']='ignore'
            with self.subTest(case=case),self.assertRaises(RuntimeError):w.compare(e,copy.deepcopy(e),t,{})
        t,e=self.fixture('rounding');t['numeric_diagnostics']['/floating_norm_controls/0/epsilon']['relative_tolerance']=False
        with self.assertRaises(RuntimeError):w.compare(e,copy.deepcopy(e),t,{})
        t,e=self.fixture('rounding');t['numeric_diagnostics'].pop('/floating_norm_controls/0/epsilon')
        with self.assertRaises(RuntimeError):w.compare(e,copy.deepcopy(e),t,{})
    def test_original_relations_cannot_be_relaxed_by_reference_tolerance(self):
        t,e=self.fixture('rounding');eps=e['floating_norm_controls'][0]['epsilon'];e['floating_norm_controls'][0]['reverse_difference']=2*eps+0.75e-12;o=copy.deepcopy(e);o['floating_norm_controls'][0]['reverse_difference']+=0.75e-12
        with self.assertRaisesRegex(RuntimeError,'original bound'):w.compare(e,o,t,{})
        t,e=self.fixture('ward_covariance');bound=e['checks'][1]['theorem_bound'];e['checks'][1]['norm_error']=bound+0.75e-12;o=copy.deepcopy(e);o['checks'][1]['theorem_bound']-=0.75e-12
        with self.assertRaisesRegex(RuntimeError,'original bound'):w.compare(e,o,t,{})
    def test_undeclared_diagnostics_remain_exact(self):
        t,e=self.fixture('convex_independent_float');del t['numeric_diagnostics'];o=copy.deepcopy(e);o['largest_equalities_absolute_residual']=1e-14
        with self.assertRaisesRegex(RuntimeError,'scientific mismatch'):w.compare(e,o,t,{})
    def test_scientific_digest_explicitly_identifies_normalized_projection(self):
        t,e=self.fixture('convex_independent_float');o=copy.deepcopy(e);o['largest_equalities_absolute_residual']=1e-14
        details=w.compare(e,o,t,{})
        self.assertEqual(details['scientific_sha256_mode'],'comparison_normalized_projection')
        self.assertEqual(details['scientific_sha256_normalized_numeric_paths'],['/largest_equalities_absolute_residual'])
        raw_science_hash=hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
        self.assertNotEqual(details['scientific_sha256'],raw_science_hash)
        self.assertEqual(o['largest_equalities_absolute_residual'],1e-14)
        self.assertEqual(details['numeric_diagnostics']['/largest_equalities_absolute_residual']['observed'],1e-14)

if __name__=='__main__':unittest.main()
