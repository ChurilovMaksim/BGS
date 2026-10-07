"""Durable replay artifacts are routed into the CI-uploaded log directory."""
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import verify_workspace as runner


class ReplayArtifactRouting(unittest.TestCase):
    def test_known_replays_get_fresh_distinct_paths_under_logs(self):
        expected = {
            'intermediate_old_layers_certificates': '--replay-output-dir',
            'charge_strengthening_replay': '--output-dir',
            'balanced_pair_schur': '--output-dir',
            'research_checkpoint_replay': '--output-dir',
        }
        self.assertEqual(runner.REPLAY_ARTIFACT_OPTIONS, expected)
        with tempfile.TemporaryDirectory() as tmp:
            logs = Path(tmp)
            run_one = Path(tempfile.mkdtemp(prefix='certificates-', dir=logs))
            run_two = Path(tempfile.mkdtemp(prefix='certificates-', dir=logs))
            outputs = []
            for directory in (run_one, run_two):
                for name, option in expected.items():
                    args = runner.replay_artifact_args(name, directory)
                    self.assertEqual(args[0], option)
                    path = Path(args[1])
                    self.assertTrue(path.is_relative_to(logs))
                    self.assertEqual(path.parent, directory)
                    self.assertEqual(path.name, name)
                    self.assertFalse(path.exists())
                    outputs.append(path)
            self.assertEqual(len(set(outputs)), 8)

    def test_other_checks_keep_existing_command_contract(self):
        for name in ('ordinary_check', 'resonance_nondegeneracy_certificate', '', '../escape'):
            self.assertEqual(runner.replay_artifact_args(name, Path('/tmp/logs')), [])


if __name__ == '__main__':
    unittest.main()
