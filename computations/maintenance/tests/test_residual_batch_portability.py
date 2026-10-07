"""Source-identity and silent-entry-point regression checks."""
from pathlib import Path
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[3]


class ResidualPortability(unittest.TestCase):
    def test_entrypoints_import_silently(self):
        snippet = ('import importlib.util,sys; s=importlib.util.spec_from_file_location("control",sys.argv[1]); '
                   'm=importlib.util.module_from_spec(s); sys.modules[s.name]=m; s.loader.exec_module(m)')
        for name in ('central_residual_extension', 'residual125_certificates', 'odd_newest_certificates'):
            for flags in ([], ['-O']):
                result = subprocess.run([sys.executable, *flags, '-c', snippet,
                                         str(ROOT / 'computations/verification' / (name + '.py'))],
                                        cwd='/tmp', capture_output=True, text=True,
                                        env=dict(os.environ, PYTHONDONTWRITEBYTECODE='1'))
                self.assertEqual((result.returncode, result.stdout, result.stderr), (0, '', ''))

    def test_source_corruption_fails_before_replay(self):
        for verifier, mapping in [('central_residual_extension', 'central_residual_promotion_map'),
                                  ('residual125_certificates', 'residual125_promotion_map')]:
            with tempfile.TemporaryDirectory() as scratch:
                root = Path(scratch)
                script = root / 'computations/verification' / (verifier + '.py')
                script.parent.mkdir(parents=True)
                shutil.copy2(ROOT / script.relative_to(root), script)
                entry = json.loads((ROOT / 'record' / (mapping + '.json')).read_text())[0]
                target = root / entry['public_path']
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(b'Intentional source-corruption negative control\n')
                record = root / 'record' / (mapping + '.json')
                record.parent.mkdir(exist_ok=True)
                record.write_text(json.dumps([entry]))
                for flags in ([], ['-O']):
                    result = subprocess.run([sys.executable, *flags, str(script)],
                                            capture_output=True, text=True, timeout=10)
                    self.assertNotEqual(result.returncode, 0)
                    self.assertIn('Source identity mismatch', result.stderr)


if __name__ == '__main__':
    unittest.main()
