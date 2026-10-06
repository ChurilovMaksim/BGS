"""Cheap positive and adversarial controls for provenance; no scientific suite."""
import json
import contextlib
import io
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'verification'))
import workspace_sources as sources
import verify_workspace as runner
import text_control_audit as control


class SourcesTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / 'source.py').write_text('print("finite check")\n')

    def manifest(self):
        files = sources.inventory(self.root)
        path = self.root / 'build' / 'manifest.json'
        path.parent.mkdir(exist_ok=True)
        path.write_text(json.dumps({'schema': sources.SCHEMA, 'upstream_commit': None, 'files': files}))
        return path

    def test_archive_positive_and_null_provenance(self):
        expected = sources.read_manifest(self.manifest())
        self.assertEqual(sources.validate(self.root, expected), expected)
        self.assertEqual(sources.provenance(self.root), {'input_commit': None, 'dirty': None, 'upstream_commit': None})

    def test_archive_modified_missing_added_sources(self):
        expected = sources.read_manifest(self.manifest())
        target = self.root / 'source.py'
        target.write_text('changed\n')
        with self.assertRaisesRegex(ValueError, 'changed='): sources.validate(self.root, expected)
        target.unlink()
        with self.assertRaisesRegex(ValueError, 'missing='): sources.validate(self.root, expected)
        (self.root / 'extra.py').write_text('new\n')
        with self.assertRaisesRegex(ValueError, 'added='): sources.validate(self.root, expected)

    def test_invalid_manifest_version_commit_and_paths(self):
        path = self.manifest()
        baseline = json.loads(path.read_text())
        for key,value in [('schema','unknown'),('upstream_commit','f'*40),('files',{'../escape':'0'*64}),('files',{})]:
            data = dict(baseline); data[key] = value
            path.write_text(json.dumps(data))
            with self.assertRaises(ValueError): sources.read_manifest(path)

    def test_duplicate_manifest_keys_and_missing_null(self):
        path = self.manifest()
        data = json.loads(path.read_text())
        del data['upstream_commit']
        path.write_text(json.dumps(data))
        with self.assertRaises(ValueError): sources.read_manifest(path)
        path.write_text('{"schema":"first","schema":"second"}')
        with self.assertRaisesRegex(ValueError, 'Duplicate'): sources.read_manifest(path)

    def test_symlink_rejected(self):
        (self.root / 'linked.py').symlink_to(self.root / 'source.py')
        with self.assertRaises(ValueError): sources.inventory(self.root)

    @unittest.skipUnless(shutil.which('git'), 'Git unavailable')
    def test_git_positive_dirty_and_parent_git_not_archive_identity(self):
        def git(*args):
            return subprocess.check_output(['git', *args], cwd=self.root, stderr=subprocess.DEVNULL, text=True).strip()
        git('init'); git('add', '.')
        git('-c', 'user.email=test@example.invalid', '-c', 'user.name=Fixture', 'commit', '-m', 'fixture')
        self.assertTrue(sources.git_root(self.root))
        self.assertEqual(sources.provenance(self.root)['input_commit'], git('rev-parse', 'HEAD'))
        self.assertFalse(sources.provenance(self.root)['dirty'])
        with patch.object(runner, 'ROOT', self.root):
            before = runner.source_manifest()
            (self.root / 'source.py').write_text('changed\n')
            self.assertNotEqual(before, runner.source_manifest())
            (self.root / 'new.py').write_text('new\n')
            self.assertIn('new.py', runner.source_manifest())
            (self.root / 'source.py').unlink()
            with self.assertRaises(RuntimeError): runner.source_manifest()
        child = self.root / 'archive'; child.mkdir()
        self.assertFalse(sources.git_root(child))
        self.assertIsNone(sources.provenance(child)['input_commit'])
        self.assertTrue(sources.provenance(self.root)['dirty'])

    def test_versions_missing_unknown_and_mismatch(self):
        pins = self.root / 'requirements.txt'; pins.write_text('numpy==1.2.3\n')
        good = {'packages': {'numpy':'1.2.3'}, 'git':'git fixture 1', 'cmake':'cmake fixture 1', 'cxx':'cxx fixture 1', 'boost_lib_version':'1_2'}
        self.assertEqual(runner.validate_versions(good,pins,need_cpp=True,need_git=True), [])
        for actual in (None, 'unknown', '1.2.4'):
            bad = dict(good, packages={'numpy':actual})
            self.assertTrue(runner.validate_versions(bad,pins,need_cpp=False,need_git=False))
        for key in ('git','cmake','cxx','boost_lib_version'):
            for value in (None, 'unknown'):
                self.assertTrue(runner.validate_versions(dict(good, **{key:value}),pins,need_cpp=True,need_git=True))

    def prepare_runner(self, script='print("finite fixture")\n'):
        directory = self.root / 'computations' / 'verification'
        directory.mkdir(parents=True)
        (directory / 'fixture.py').write_text(script + '\nif __name__ == "__main__": pass\n')
        (self.root / 'requirements.txt').write_text('numpy==1.2.3\n')
        (self.root / 'CMakeLists.txt').write_text('# fixture\n')

    def run_fixture(self, *extra):
        args = ['verify_workspace.py', '--build', str(self.root/'build'),
                '--logs', str(self.root/'build/logs'), '--output', str(self.root/'build/result.json'),
                '--only', 'fixture', *extra]
        with patch.object(runner, 'ROOT', self.root), patch.object(sys, 'argv', args), \
             patch.object(runner, 'package_versions', return_value={'numpy':'1.2.3'}), \
             contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            runner.main()
        return json.loads((self.root/'build/result.json').read_text())

    def test_archive_runner_success_missing_manifest_and_during_run_mutation(self):
        self.prepare_runner()
        with self.assertRaises(SystemExit): self.run_fixture()
        path = self.manifest()
        result = self.run_fixture('--archive-manifest', str(path))
        self.assertEqual(result['passed'], 1)
        self.assertIsNone(result['input_commit'])
        self.assertIsNone(result['upstream_commit'])
        self.assertTrue(result['source_tree_unchanged'])
        target = self.root/'computations/verification/fixture.py'
        target.write_text('from pathlib import Path\nPath("source.py").unlink()\nif __name__ == "__main__": pass\n')
        path = self.manifest()
        with self.assertRaisesRegex(SystemExit, 'mutated'):
            self.run_fixture('--archive-manifest', str(path))
        result = json.loads((self.root/'build/result.json').read_text())
        self.assertFalse(result['source_tree_unchanged'])
        self.assertIn('missing=', result['source_validation_error'])

    @unittest.skipUnless(shutil.which('git'), 'Git unavailable')
    def test_git_runner_success_and_dirty_rejection(self):
        self.prepare_runner()
        (self.root/'.gitignore').write_text('build/\n')
        for args in [('init',), ('add','.'), ('-c','user.email=test@example.invalid','-c','user.name=Fixture','commit','-m','fixture')]:
            subprocess.run(['git',*args],cwd=self.root,check=True,capture_output=True)
        result = self.run_fixture()
        self.assertEqual(result['passed'],1)
        self.assertEqual(result['source_mode'],'git')
        self.assertIsNotNone(result['input_commit'])
        (self.root/'source.py').write_text('dirty\n')
        with self.assertRaises(SystemExit): self.run_fixture()
        self.assertEqual(self.run_fixture('--allow-dirty')['passed'],1)
        with self.assertRaises(SystemExit): self.run_fixture('--archive-manifest',str(self.manifest()))

    def test_control_bytes_and_history_exclusion(self):
        self.assertEqual(control.violations(self.root), [])
        (self.root / 'source.py').write_bytes(b'good\tline\n')
        self.assertEqual(control.violations(self.root), [])
        for value in set(range(32)) - {9,10}:
            (self.root / 'source.py').write_bytes(bytes([value]))
            self.assertTrue(control.violations(self.root), value)
        (self.root / 'source.py').write_text('ok\n')
        (self.root / 'evidence').mkdir()
        (self.root / 'evidence' / 'historical.md').write_bytes(b'\r')
        (self.root / 'binary.pdf').write_bytes(b'\x00')
        self.assertEqual(control.violations(self.root), [])


if __name__ == '__main__':
    unittest.main()
