"""Finite packet replay contracts; these tests do not audit analytic theorems."""
from __future__ import annotations
import hashlib
import os
from unittest.mock import patch
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SOURCE = Path(__file__).resolve().parents[2] / 'verification/research_checkpoint_replay.py'
SPEC = importlib.util.spec_from_file_location('bgs_checkpoint_replay', SOURCE)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class CheckpointPortability(unittest.TestCase):
    def test_silent_import_normal_and_optimized(self):
        for mode in ([], ['-O']):
            code = f"import importlib.util; s=importlib.util.spec_from_file_location('bgs', {str(SOURCE)!r}); m=importlib.util.module_from_spec(s); s.loader.exec_module(m)"
            p = subprocess.run([sys.executable, *mode, '-c', code], capture_output=True)
            self.assertEqual(p.returncode, 0)
            self.assertEqual((p.stdout, p.stderr), (b'', b''))

    def test_duplicate_and_nonfinite_json_rejected(self):
        for raw in ('{"x":1,"x":2}', '{"x":NaN}', '{"x":Infinity}'):
            with self.subTest(raw=raw), self.assertRaises(RuntimeError):
                M.strict_json(raw)

    def test_log_parser_requires_complete_final_object(self):
        self.assertEqual(M.final_json('progress 1\n{"a":{"b":2}}\n'), {'a':{'b':2}})
        for raw in ('{"x":1}garbage', 'progress only', '{"x":1,"x":2}'):
            with self.subTest(raw=raw), self.assertRaises(RuntimeError):
                M.final_json(raw)

    def test_typed_scientific_comparison(self):
        for observed in ({'v':True}, {'v':1.0}, {'v':2}, {}, {'v':1,'extra':2}):
            with self.subTest(observed=observed), self.assertRaises(RuntimeError):
                M.compare({'v':1}, observed, [])
        M.compare({'v':1}, {'v':1}, [])

    def test_only_declared_provenance_root_fields_exempted(self):
        M.compare({'v':1,'runtime_seconds':1.0}, {'v':1,'runtime_seconds':2.0}, ['runtime_seconds'])
        for value in (float('nan'), float('inf'), -1, True, '1'):
            with self.subTest(value=value), self.assertRaises(RuntimeError):
                M.compare({'runtime_seconds':1}, {'runtime_seconds':value}, ['runtime_seconds'])
        with self.assertRaises(RuntimeError):
            M.compare({'runtime_seconds':1}, {}, ['runtime_seconds'])
        with self.assertRaises(RuntimeError):
            M.compare({'nested':{'runtime_seconds':1}}, {'nested':{'runtime_seconds':2}}, [])

    def test_environment_provenance_has_exact_types_and_shape(self):
        for key in ('python', 'sympy'):
            for value in (None, True, 1, {}, [], '', 'arbitrary', 'x' * 300):
                with self.subTest(key=key, value=value), self.assertRaises(RuntimeError):
                    M.compare({key:'3.12.14'}, {key:value}, [key])
            M.compare({key:'3.12.14'}, {key:'3.13.5'}, [key])
        cmd = ['g++', '-std=c++17', '-O2', '-Wall', '-Wextra', '-pedantic', 'source.cpp', '-o', 'binary']
        M.compare({'compiler_command':cmd}, {'compiler_command':cmd}, ['compiler_command'])
        for value in (None, True, cmd[:-1], ['g++'] + cmd[2:], cmd[:-1] + [None]):
            with self.subTest(value=value), self.assertRaises(RuntimeError):
                M.compare({'compiler_command':cmd}, {'compiler_command':value}, ['compiler_command'])
        with self.assertRaises(RuntimeError):
            M.compare({'science':1}, {'science':2}, ['science'])

    def test_copied_worker_input_is_authenticated_after_execution(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            p = root / 'next_worker.py'
            p.write_bytes(b'print(1)\n')
            cached = {'next_worker.py':p.read_bytes()}
            M.authenticate_copied_inputs(root, cached)
            p.write_bytes(b'print(2)\n')
            with self.assertRaisesRegex(RuntimeError, 'copied input changed'):
                M.authenticate_copied_inputs(root, cached)
            p.unlink()
            p.symlink_to(SOURCE)
            with self.assertRaises(RuntimeError):
                M.authenticate_copied_inputs(root, cached)

    def test_generated_result_ancestor_escape_is_rejected(self):
        import os
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / 'work'
            raw = root / 'evidence/research_checkpoint_20261007/raw'
            raw.mkdir(parents=True)
            outside = Path(tmp) / 'outside'
            outside.mkdir()
            producer = raw / 'producer.py'
            link = raw / 'results'
            link.mkdir()
            task = {'name':'escape', 'source':producer.relative_to(root).as_posix(),
                    'arguments':[], 'timeout_seconds':10,
                    'generated_result':(link/'checks.json').relative_to(root).as_posix()}
            producer.write_text(f"from pathlib import Path\np=Path({str(link)!r}); p.rmdir(); p.symlink_to({str(outside)!r}); (p/'checks.json').write_text('{{\"answer\":7}}')\n")
            with self.assertRaisesRegex(RuntimeError, 'escaping/symlink generated'):
                M.execute_task(root, task, dict(os.environ), [])

    def test_difference_diagnostic_is_bounded(self):
        with self.assertRaisesRegex(RuntimeError, 'total=100') as result:
            M.compare({'v':list(range(100))}, {'v':[-1]*100}, [])
        self.assertLess(len(str(result.exception)), 500)

    def test_explicit_assertions_active_under_optimization(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / 'check.py'
            p.write_text("assert False, 'deliberate mathematical defect'\n")
            for mode in ([], ['-O']):
                result = subprocess.run([sys.executable, *mode, '-c', M.BOOTSTRAP, str(p)], capture_output=True)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn(b'deliberate mathematical defect', result.stderr)

    def test_assertion_message_remains_lazy(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / 'check.py'
            p.write_text("assert True, 1/0\nassert False\n")
            result = subprocess.run([sys.executable, '-O', '-c', M.BOOTSTRAP, str(p)], capture_output=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertNotIn(b'ZeroDivisionError', result.stderr)
            self.assertTrue(result.stderr.rstrip().endswith(b'AssertionError'))

    def test_generated_result_is_fresh_and_exact(self):
        import os
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            raw = root / 'evidence/research_checkpoint_20261007/raw'
            raw.mkdir(parents=True)
            source = raw / 'producer.py'
            generated = raw / 'checks.json'
            task = {'name':'producer', 'source':source.relative_to(root).as_posix(),
                    'arguments':[], 'timeout_seconds':10,
                    'generated_result':generated.relative_to(root).as_posix()}
            expected = {'answer':7}
            for mode in ([], ['-O']):
                generated.write_text(json.dumps(expected))
                source.write_text('pass\n')
                with self.subTest(mode=mode, control='no-op'), self.assertRaisesRegex(RuntimeError, 'missing generated'):
                    M.execute_task(root, task, dict(os.environ), mode)
                self.assertFalse(generated.exists())
                generated.write_text(json.dumps(expected))
                source.write_text("from pathlib import Path\nPath(__file__).with_name('checks.json').write_text('{\"answer\":8}')\n")
                fresh = M.execute_task(root, task, dict(os.environ), mode)
                with self.subTest(mode=mode, control='wrong-result'), self.assertRaisesRegex(RuntimeError, 'scientific mismatch'):
                    M.compare(expected, M.final_json(fresh), [])
                source.write_text("from pathlib import Path\nPath(__file__).with_name('checks.json').write_text('{\"answer\":7}')\n")
                M.compare(expected, M.final_json(M.execute_task(root, task, dict(os.environ), mode)), [])

    def test_durable_output_rejects_stale_source_overlap_and_symlinks(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            root = base / 'repo'
            root.mkdir()
            output = base / 'durable'
            self.assertEqual(M.output_directory(root, output), output)
            self.assertEqual(M.output_directory(root, root / 'build' / 'certificates' / 'fresh'), root / 'build' / 'certificates' / 'fresh')
            (output / 'stale').write_bytes(b'old')
            with self.assertRaisesRegex(RuntimeError, 'must be empty'):
                M.output_directory(root, output)
            with self.assertRaisesRegex(RuntimeError, 'separate'):
                M.output_directory(root, root / 'source_output')
            link = base / 'link'
            link.symlink_to(output)
            with self.assertRaisesRegex(RuntimeError, 'symlink'):
                M.output_directory(root, link)

    def test_durable_raw_artifact_bytes_and_hash_are_retained(self):
        with tempfile.TemporaryDirectory() as tmp:
            raw = b'progress\n{\"answer\":7}\n'
            record = M.save_artifact(Path(tmp), 'observed.raw', raw)
            self.assertEqual((Path(tmp) / 'observed.raw').read_bytes(), raw)
            self.assertEqual(record['sha256'], hashlib.sha256(raw).hexdigest())
            self.assertEqual(record['bytes'], len(raw))

    def test_durable_failed_source_check_has_terminal_receipt(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            root = base / 'repo'
            root.mkdir()
            output = base / 'output'
            with self.assertRaises(FileNotFoundError):
                M.run(root, output)
            receipt = json.loads((output / 'replay_manifest.json').read_text())
            self.assertEqual(receipt['status'], 'failed')
            self.assertTrue(receipt['failure'])
            self.assertEqual(receipt['tasks'], [])

    def make_root(self, root, rel='packet/check.py'):
        p = root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(b'print(1)\n')
        m = root / M.BINDINGS
        m.parent.mkdir(parents=True, exist_ok=True)
        m.write_text(json.dumps({'schema':'bgs-checkpoint-source-bindings-v1',
            'files':{rel:hashlib.sha256(p.read_bytes()).hexdigest()}}))
        return p

    def test_relocated_explicit_source_map_and_immutable_cache(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            p = self.make_root(root)
            cached = M.source_bytes(root)
            self.assertEqual(cached['packet/check.py'], b'print(1)\n')
            p.write_bytes(b'print(2)\n')
            self.assertEqual(cached['packet/check.py'], b'print(1)\n')
            with self.assertRaisesRegex(RuntimeError, 'changed source'):
                M.source_bytes(root)

    def test_missing_symlink_and_escaping_sources_fail_closed(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            p = self.make_root(root)
            p.unlink()
            with self.assertRaises(RuntimeError):
                M.source_bytes(root)
            p.symlink_to(SOURCE)
            with self.assertRaises(RuntimeError):
                M.source_bytes(root)
            m = root / M.BINDINGS
            for rel in ('../escape.py', '/absolute.py', 'a/../b.py', 'a\\b.py'):
                m.write_text(json.dumps({'schema':'bgs-checkpoint-source-bindings-v1', 'files':{rel:'0'*64}}))
                with self.subTest(rel=rel), self.assertRaises(RuntimeError):
                    M.source_bytes(root)


class BudgetProposal(unittest.TestCase):
 def n4(self):
  return {'name':'compact_independent_n4','source':'evidence/research_checkpoint_20261007/raw/bgs_astra_corrected_integral/checks/independent_checks.py','arguments':['4','3'],'timeout_seconds':660,'cpu_seconds':600}
 def test_only_exact_n4_has_larger_budget(self):
  self.assertEqual(M.task_budget(self.n4()),{'wall_seconds':660,'cpu_seconds':600,'memory_bytes':3*2**30})
  for field,value in [('name','other'),('source','other.py'),('arguments',['3','3'])]:
   d=self.n4();d[field]=value
   with self.subTest(field=field),self.assertRaises(RuntimeError):M.task_budget(d)
 def test_budget_types_and_bounds_fail_closed(self):
  for field,vals in [('timeout_seconds',(True,0,-1,661,660.0,'660')),('cpu_seconds',(True,0,-1,601,600.0,'600'))]:
   for value in vals:
    d=self.n4();d[field]=value
    with self.subTest(field=field,value=value),self.assertRaises(RuntimeError):M.task_budget(d)
  self.assertEqual(M.task_budget({'name':'other','timeout_seconds':180})['cpu_seconds'],180)
  with self.assertRaises(RuntimeError):M.task_budget({'name':'other','timeout_seconds':181})
 def test_elapsed_is_typed_bounded_provenance_only(self):
  M.compare({'v':7,'elapsed_seconds':155.0},{'v':7,'elapsed_seconds':660},['elapsed_seconds'],elapsed_budget_seconds=660)
  for value in (True,-1,661,float('inf'),float('nan'),'12'):
   with self.subTest(value=value),self.assertRaises(RuntimeError):M.compare({'elapsed_seconds':155},{'elapsed_seconds':value},['elapsed_seconds'],elapsed_budget_seconds=660)
  for budget in (True,0,661,'660',660.0):
   with self.subTest(budget=budget),self.assertRaises(RuntimeError):M.compare({'v':1},{'v':1},[],elapsed_budget_seconds=budget)
  with self.assertRaises(RuntimeError):M.compare({'elapsed_seconds':1},{'elapsed_seconds':181},['elapsed_seconds'])
  with self.assertRaisesRegex(RuntimeError,'scientific mismatch'):M.compare({'v':7,'elapsed_seconds':1},{'v':8,'elapsed_seconds':600},['elapsed_seconds'],elapsed_budget_seconds=660)
  with self.assertRaisesRegex(RuntimeError,'scientific mismatch'):M.compare({'v':7},{'v':7.0},[],elapsed_budget_seconds=660)
 def test_memory_unchanged_and_cpu_bound_exact(self):
  with patch.object(M.resource,'setrlimit') as setlimit:
   M.child_limits(600)
   self.assertEqual(setlimit.call_args_list[0].args,(M.resource.RLIMIT_AS,(3*2**30,3*2**30)))
   self.assertEqual(setlimit.call_args_list[1].args,(M.resource.RLIMIT_CPU,(600,600)))
 def test_outer_watchdog_only_named_wrapper_changes(self):
  runner_path = SOURCE.parents[1] / 'maintenance/verify_workspace.py'
  sys.path.insert(0, str(runner_path.parent))
  spec = importlib.util.spec_from_file_location('checkpoint_budget_runner', runner_path)
  R = importlib.util.module_from_spec(spec)
  spec.loader.exec_module(R)
  self.assertEqual(R.check_timeout_seconds('research_checkpoint_replay'),900)
  for name in ('ordinary','compact_independent_n4','wave2_checked_replay','wave3_checked_replay',''):
   self.assertEqual(R.check_timeout_seconds(name),360)
 def make_root(self,root):
  raw=root/'evidence/research_checkpoint_20261007/raw';raw.mkdir(parents=True)
  source=raw/'producer.py';source.write_text('pass\n');expected=raw/'expected.log';expected.write_bytes(b'{"answer":7}\n');cpp=raw/'control.cpp';cpp.write_text('int main(){}\n');cpp_expected=raw/'cpp.expected';cpp_expected.write_bytes(b'{"answer":7}\n');generated=raw/'result.json'
  task={'name':'timeout_fixture','source':source.relative_to(root).as_posix(),'arguments':[],'expected':expected.relative_to(root).as_posix(),'provenance_root_fields':[],'timeout_seconds':10,'generated_result':generated.relative_to(root).as_posix()}
  contract={'schema':'bgs-checkpoint-replay-contract-v1','tasks':[task],'cpp':{'source':cpp.relative_to(root).as_posix(),'expected':cpp_expected.relative_to(root).as_posix(),'provenance_root_fields':[],'timeout_seconds':10}}
  (root/M.CONTRACT).parent.mkdir(parents=True);(root/M.CONTRACT).write_text(json.dumps(contract))
  files=[source,expected,cpp,cpp_expected,root/M.CONTRACT];pins={p.relative_to(root).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files};(root/M.BINDINGS).write_text(json.dumps({'schema':'bgs-checkpoint-source-bindings-v1','files':pins}))
  return task,generated
 def test_timeout_partial_capture_and_failure_receipt(self):
  with tempfile.TemporaryDirectory() as tmp:
   root=Path(tmp)/'repo';root.mkdir();task,generated=self.make_root(root);output=Path(tmp)/'durable'
   def timed(command,**kwargs):
    work=Path(kwargs['cwd']).parents[2]
    actual=work/task['generated_result'];actual.write_bytes(b'{"answer":7}\n')
    self.assertEqual(kwargs['timeout'],10)
    raise subprocess.TimeoutExpired(command,10,output=b'partial stdout',stderr=b'partial stderr')
   with patch.object(M.subprocess,'run',side_effect=timed),self.assertRaises(subprocess.TimeoutExpired):M.run(root,output)
   r=json.loads((output/'replay_manifest.json').read_bytes());self.assertEqual(r['status'],'failed');self.assertTrue(r['failed_task']['timed_out']);self.assertIsNone(r['failed_task']['exit_status']);self.assertEqual(r['failed_task']['resource_budget']['wall_seconds'],10)
   self.assertEqual((output/'timeout_fixture.stdout').read_bytes(),b'partial stdout');self.assertEqual((output/'timeout_fixture.stderr').read_bytes(),b'partial stderr');self.assertEqual((output/'timeout_fixture.partial.actual.raw').read_bytes(),b'{"answer":7}\n');self.assertEqual((output/'timeout_fixture.expected.raw').read_bytes(),b'{"answer":7}\n')
   for a in r['artifacts']:self.assertEqual(hashlib.sha256((output/a['path']).read_bytes()).hexdigest(),a['sha256'])


if __name__ == '__main__':
    unittest.main()
