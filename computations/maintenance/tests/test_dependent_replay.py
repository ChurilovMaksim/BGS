"""Producer failure and stale-artifact controls, without scientific execution."""
from pathlib import Path
import contextlib
import io
import json
import sys
import tempfile
import unittest
from unittest.mock import Mock, patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import verify_workspace as runner
import workspace_sources as sources

class ReplayTest(unittest.TestCase):
    def test_failed_producer_never_replays_stale_certificate(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory)
            source=root/'check.py';source.write_text('fixture')
            stale=root/'certificate.json';stale.write_text('historical certificate')
            check=Mock()
            with patch.object(runner,'ROOT',root),contextlib.redirect_stdout(io.StringIO()):
                row=runner.dependent_replay(('check',['unused'],source),'producer',stale,
                    [{'name':'producer','exit_code':1}],check,root)
            check.assert_not_called()
            self.assertEqual(row['execution_status'],'blocked')
            self.assertNotEqual(row['exit_code'],0)
            self.assertEqual(stale.read_text(),'historical certificate')

    def test_successful_producer_missing_output_is_blocked_and_mutation_detected(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory);source=root/'check.py';source.write_text('fixture')
            artifact=root/'fresh.json';check=Mock()
            with patch.object(runner,'ROOT',root),contextlib.redirect_stdout(io.StringIO()):
                row=runner.dependent_replay(('check',[],source),'producer',artifact,
                    [{'name':'producer','exit_code':0}],check,root)
                self.assertEqual(row['execution_status'],'blocked');check.assert_not_called()
                artifact.write_text('fresh')
                def mutate(_):
                    artifact.write_text('changed');return {'exit_code':0}
                row=runner.dependent_replay(('check',[],source),'producer',artifact,
                    [{'name':'producer','exit_code':0}],mutate,root)
                self.assertEqual(row['exit_code'],125)
                self.assertFalse(row['input_artifact_unchanged'])
                row=runner.dependent_replay(('check',[],source),'producer',artifact,
                    [{'name':'producer','exit_code':0}],lambda _: {'exit_code':0},root)
                self.assertEqual(row['exit_code'],0)
                self.assertTrue(row['input_artifact_unchanged'])

    def test_complete_runner_stale_outputs_failed_and_empty_producers(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory);v=root/'computations/verification';v.mkdir(parents=True)
            a=root/'computations/analysis';a.mkdir()
            c=root/'computations/cpp';c.mkdir()
            build=root/'build';build.mkdir();logs=build/'logs';logs.mkdir()
            stale=logs/'resonance_nondegeneracy_radius8.json';stale.write_text('historical')
            (logs/'extremal.replay').write_text('historical extremal')
            (v/'resonance_nondegeneracy_certificate.py').write_text('if __name__ == "__main__": raise SystemExit(1)\n')
            (v/'extremal_resonance.py').write_text('if __name__ == "__main__": pass\n')
            (v/'check_resonance_certificate.py').write_text('if __name__ == "__main__": raise RuntimeError("must not execute")\n')
            (a/'spectral_diagnostics.py').write_text('pass\n')
            (c/'extremal_resonance_replay.cpp').write_text('// fixture\n')
            exe=build/'extremal_resonance_replay';exe.write_text('#!/bin/sh\nexit 0\n');exe.chmod(0o755)
            (root/'requirements.txt').write_text('');(root/'CMakeLists.txt').write_text('')
            manifest=build/'manifest.json';manifest.write_text(json.dumps({'schema':sources.SCHEMA,'upstream_commit':None,'files':sources.inventory(root)}))
            argv=['runner','--build',str(build),'--logs',str(logs),'--output',str(build/'result.json'),'--archive-manifest',str(manifest)]
            with patch.object(runner,'ROOT',root),patch.object(sys,'argv',argv),patch.object(runner,'validate_versions',return_value=[]),contextlib.redirect_stdout(io.StringIO()):
                with self.assertRaisesRegex(SystemExit,'Verification failed'):runner.main()
            result=json.loads((build/'result.json').read_text())
            rows={row['name']:row for row in result['checks']}
            for name in ('check_resonance_certificate','extremal_independent_replay'):
                self.assertEqual(rows[name]['execution_status'],'blocked')
            self.assertTrue(result['source_tree_unchanged'])
            self.assertEqual(stale.read_text(),'historical')
            self.assertTrue(Path(result['certificate_directory']).is_dir())

if __name__ == '__main__':unittest.main()
