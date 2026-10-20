"""Reject drift in generated research views and the reviewed metadata pointer."""
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'computations/maintenance'))
sys.path.insert(0, str(ROOT / 'computations/verification'))
from render_research_views import projections
from bibliographic_metadata_audit import load_audit


class ResearchViewBoundaries(unittest.TestCase):
    def fixture(self, root):
        for rel in ('record', 'mathematics/topics/alpha', 'literature', 'evidence'):
            (root / rel).mkdir(parents=True, exist_ok=True)
        (root / 'mathematics/a.md').write_text('# A scoped theorem\n')
        (root / 'mathematics/topics/alpha/README.md').write_text('# Alpha\n')
        data = {'updated': '2026-10-19', 'claims': [{
            'id': 'BGS-TRACE-001', 'state': 'conditional',
            'source': 'mathematics/a.md', 'dependencies': []}]}
        (root / 'record/mathematics_topics.json').write_text(
            json.dumps({'topics': {'alpha': ['mathematics/a.md']}}))
        self.save(root, data)
        return data

    def save(self, root, data):
        (root / 'record/claims.json').write_text(json.dumps(data))

    def test_scoped_state_preserved_and_unindexed_proof_rejected(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.fixture(root)
            views = projections(root)
            self.assertIn('BGS-TRACE-001` (conditional)', views['docs/corpus_atlas.md'])
            self.assertIn('| conditional |', views['record/scientific_dependency_graph.md'])
            (root / 'mathematics/unindexed.md').write_text('# Unindexed\n')
            with self.assertRaisesRegex(ValueError, 'Topic map'):
                projections(root)

    def test_unknown_dependency_cycle_and_duplicate_rejected(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            data = self.fixture(root)
            for dependency, message in [('UNKNOWN', 'Unknown prerequisite'),
                                        ('BGS-TRACE-001', 'Dependency cycle')]:
                data['claims'][0]['dependencies'] = [dependency]
                self.save(root, data)
                with self.assertRaisesRegex(ValueError, message):
                    projections(root)
            data['claims'][0]['dependencies'] = []
            data['claims'].append(dict(data['claims'][0]))
            self.save(root, data)
            with self.assertRaisesRegex(ValueError, 'Duplicate claim'):
                projections(root)

    def test_missing_pointer_digest_mutation_and_escape_rejected(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.fixture(root)
            with self.assertRaises(FileNotFoundError):
                load_audit(root)
            cache = root / 'evidence/cache.json'
            cache.write_text('{"records": []}\n')
            digest = root / 'evidence/cache.sha256'
            digest.write_text(hashlib.sha256(cache.read_bytes()).hexdigest() + '\n')
            pointer = {'schema': 'bgs-metadata-audit-pointer-v1',
                       'cache': 'evidence/cache.json', 'digest': 'evidence/cache.sha256'}
            path = root / 'literature/metadata_audit.json'
            path.write_text(json.dumps(pointer))
            self.assertEqual(load_audit(root), {'records': []})
            cache.write_text('{"records": ["changed"]}\n')
            with self.assertRaisesRegex(ValueError, 'digest mismatch'):
                load_audit(root)
            pointer['cache'] = '../outside.json'
            path.write_text(json.dumps(pointer))
            with self.assertRaisesRegex(ValueError, 'escapes repository'):
                load_audit(root)


if __name__ == '__main__':
    unittest.main()
