"""Intermediate arithmetic helper imports and explicit failures remain portable."""
from pathlib import Path
import subprocess
import sys
import unittest

V = Path(__file__).resolve().parents[3]/'computations/verification'
LOAD = 'import importlib.util,sys;s=importlib.util.spec_from_file_location("m",sys.argv[1]);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)'


class IntermediateLayerPortability(unittest.TestCase):
    def test_imports_are_silent(self):
        for p in [V/'intermediate_old_layers_certificates.py',*sorted((V/'intermediate_old_layers').glob('*.py'))]:
            for flags in ([], ['-O']):
                r = subprocess.run([sys.executable,*flags,'-B','-c',LOAD,str(p)],capture_output=True,text=True,check=True)
                self.assertEqual(r.stdout+r.stderr,'')

    def test_only_allowlisted_top_level_environment_is_ignored(self):
        import importlib.util
        spec = importlib.util.spec_from_file_location('intermediate', V/'intermediate_old_layers_certificates.py')
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        base = {'python': '3.12', 'numpy': '2.3', 'sympy': '1.14', 'seconds': 1.5, 'verified': True,
                'records': [{'python': 'mathematical-label', 'polynomial': [1, 2, 3]}]}
        changed = dict(base, python='3.13', numpy='2.4', sympy='1.15')
        self.assertEqual(module.scientific(base, 'return_operator'),
                         module.scientific(changed, 'return_operator'))
        self.assertEqual(module.environment_metadata(changed, 'return_operator')['python'], '3.13')
        nested = dict(changed, records=[{'python': 'different-label', 'polynomial': [1, 2, 3]}])
        self.assertNotEqual(module.scientific(base, 'return_operator'),
                            module.scientific(nested, 'return_operator'))
        polynomial = dict(changed, records=[{'python': 'mathematical-label', 'polynomial': [1, 2, 4]}])
        self.assertNotEqual(module.scientific(base, 'return_operator'),
                            module.scientific(polynomial, 'return_operator'))
        self.assertNotEqual(module.scientific(base, 'first_position'),
                            module.scientific(changed, 'first_position'))
        for altered in [dict(changed, verified=False), dict(changed, extra=1),
                        {k: v for k, v in changed.items() if k != 'records'},
                        dict(changed, source_sha256='unexpected')]:
            self.assertNotEqual(module.scientific(base, 'return_operator'),
                                module.scientific(altered, 'return_operator'))
        for key in ('python', 'numpy', 'sympy'):
            with self.assertRaises(RuntimeError):
                module.scientific(dict(changed, **{key: 7}), 'return_operator')
        nested_runtime = dict(changed, records=[{'seconds': 3}])
        self.assertNotEqual(module.scientific(base, 'return_operator'),
                            module.scientific(nested_runtime, 'return_operator'))
        self.assertTrue(module.differing_paths({'value': True}, {'value': 1}))
        self.assertEqual(module.differing_paths({'nested': {'value': 2}}, {'nested': {'value': 3}}),
                         ['$["nested"]["value"]'])
        for invalid in (float('inf'), float('nan'), True, -1):
            with self.assertRaises(RuntimeError):
                module.scientific(dict(changed, seconds=invalid), 'return_operator')
        missing = dict(changed)
        del missing['numpy']
        with self.assertRaises(RuntimeError):
            module.scientific(missing, 'return_operator')

    def test_mismatch_retains_actual_result_before_raising(self):
        import contextlib
        import hashlib
        import importlib.util
        import io
        import json
        import tempfile
        from unittest.mock import patch
        spec = importlib.util.spec_from_file_location('intermediate_diagnostic', V/'intermediate_old_layers_certificates.py')
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        actual = {'value': False}
        expected = {'value': True}
        raw = json.dumps(actual).encode()
        original_bytes = json.dumps(expected).encode()
        with tempfile.TemporaryDirectory() as directory:
            shared_result = Path(directory)/'shared.json'
            shared_result.write_bytes(original_bytes)
            cached_expected = shared_result.read_bytes()
            shared_result.write_bytes(raw)
            with patch.object(module.tempfile, 'mkdtemp', return_value=directory), contextlib.redirect_stderr(io.StringIO()):
                with self.assertRaises(RuntimeError):
                    module.record_mismatch('first_position', actual, expected, ['$["value"]'],
                                           shared_result.read_bytes(), cached_expected)
            self.assertEqual((Path(directory)/'actual.json').read_bytes(), raw)
            receipt = json.loads((Path(directory)/'receipt.json').read_text())
            self.assertEqual(receipt['actual_result_sha256'], hashlib.sha256(raw).hexdigest())
            self.assertEqual((Path(directory)/'expected.json').read_bytes(), original_bytes)
            self.assertEqual(receipt['expected_result_sha256'], hashlib.sha256(original_bytes).hexdigest())
            self.assertEqual(receipt['differing_json_paths'], ['$["value"]'])

    def test_explicit_failure_survives_optimization(self):
        for flags in ([], ['-O']):
            r = subprocess.run([sys.executable,*flags,'-B','-c',LOAD+';m.require(False,"negative control")',str(V/'intermediate_old_layers_certificates.py')],capture_output=True,text=True)
            self.assertNotEqual(r.returncode,0)
            self.assertIn('negative control',r.stderr)


if __name__ == '__main__':
    unittest.main()
