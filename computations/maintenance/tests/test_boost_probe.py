"""Bounded compiler/header provenance controls; these do not certify binaries."""
from pathlib import Path
import shutil
import os
import sys
import tempfile
import unittest
from unittest.mock import patch
import subprocess
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import verify_workspace as runner

class BoostProbeTest(unittest.TestCase):
    @unittest.skipUnless(shutil.which('c++'), 'C++ compiler unavailable')
    def test_custom_header_and_malformed_macros(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root/'boost').mkdir()
            header = root/'boost/version.hpp'
            for content, expected in [
                ('#define BOOST_VERSION 109000\n#define BOOST_LIB_VERSION "1_90"\n', '1_90'),
                ('#define BOOST_VERSION 109001\n#define BOOST_LIB_VERSION "1_90_1"\n', '1_90_1'),
                ('#define BOOST_VERSION 109000\n#define BOOST_LIB_VERSION "1_89"\n', None),
                ('#define BOOST_VERSION 109000\n#define BOOST_LIB_VERSION "unknown"\n', None),
                ('#define BOOST_LIB_VERSION "1_90"\n', None),
                ('#error unavailable fixture\n', None),
            ]:
                header.write_text(content)
                result = runner.boost_probe('c++',root)
                self.assertEqual(result['version'],expected)
                self.assertEqual(result['include'],str(root))
                if expected is None:
                    self.assertTrue(result['error'])
    def test_outputs_cannot_overwrite_sources_or_create_untracked_receipt(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root/'source.py'
            source.write_text('original')
            manifest = {'source.py': 'unused'}
            for path in (source, root, root/'receipt.json', root/'logs', root/'.git/config', root/'scratch/receipt.json'):
                with self.assertRaises(ValueError):
                    runner.validate_output_locations(root,[path],manifest)
            runner.validate_output_locations(root,[root/'build/logs',root/'build/result.json'],manifest)
            with self.assertRaises(ValueError):
                runner.validate_output_locations(root,[root/'build/manifest.json'],manifest,root/'build/manifest.json')
            (root/'build').mkdir()
            (root/'build/link.json').symlink_to(source)
            with self.assertRaises(ValueError):
                runner.validate_output_locations(root,[root/'build/link.json'],manifest)

    def test_runner_preserves_assertions_under_optimized_environment(self):
        from test_workspace_sources import SourcesTest
        case = SourcesTest()
        case.setUp()
        try:
            case.prepare_runner('assert False, "negative assertion control"')
            manifest = case.manifest()
            with patch.dict(os.environ, {'PYTHONOPTIMIZE': '1'}):
                with self.assertRaisesRegex(SystemExit, 'Verification failed'):
                    case.run_fixture('--archive-manifest', str(manifest))
        finally:
            case.doCleanups()

    def test_missing_compiler_and_timeout(self):
        self.assertIsNone(runner.boost_probe('/nonexistent/bgs-cxx')['version'])
        with patch.object(runner.subprocess,'run',side_effect=subprocess.TimeoutExpired('c++',15)):
            self.assertIsNone(runner.boost_probe('c++')['version'])

if __name__ == '__main__':
    unittest.main()
