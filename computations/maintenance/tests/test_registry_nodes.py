"""The dependency graph must list every registered claim exactly once."""
import importlib.util
import copy
import json
from pathlib import Path
import unittest
from unittest.mock import patch

SOURCE = Path(__file__).resolve().parents[2] / 'verification/scientific_registry_audit.py'
SPEC = importlib.util.spec_from_file_location('bgs_registry_nodes', SOURCE)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)

class RegistryNodesTests(unittest.TestCase):
    def claim_fixture(self):
        registry = json.loads(MODULE.CLAIMS.read_text())
        registry['claims'] = [c for c in registry['claims']
                              if c['id'] in {'BGS-BGS-001', 'BGS-CAYLEY-009'}]
        return registry

    def test_no_external_refereeing_is_not_an_external_theorem(self):
        # Regression: the real provenance wording used to fail a substring
        # test for EXTERNAL despite declaring no external theorem input.
        fixture = self.claim_fixture()
        claim = next(c for c in fixture['claims'] if c['id'] == 'BGS-CAYLEY-009')
        self.assertIn('NOT EXTERNALLY REFEREED', claim['ledger_status'])
        self.assertEqual(claim['external_dependencies'], [])
        with patch.object(MODULE, 'load', return_value=fixture):
            MODULE.audit_claims()

    def test_external_inputs_remain_structured_and_resolved(self):
        fixture = self.claim_fixture()
        for value in ['EXT-FAKE-2026', ['not-an-id'],
                      ['EXT-FAKE-2026', 'EXT-FAKE-2026'], [None]]:
            changed = copy.deepcopy(fixture)
            changed['claims'][0]['external_dependencies'] = value
            with self.subTest(value=value):
                with patch.object(MODULE, 'load', return_value=changed):
                    with self.assertRaisesRegex(SystemExit, 'distinct external IDs'):
                        MODULE.audit_claims()
        changed = copy.deepcopy(fixture)
        changed['claims'][0]['external_dependencies'] = ['EXT-FAKE-2026']
        with patch.object(MODULE, 'load', return_value=changed):
            claims, _ = MODULE.audit_claims()
        # A syntactically valid but unregistered theorem must still fail.
        with self.assertRaisesRegex(SystemExit, 'unknown external dependency'):
            MODULE.audit_external(claims)

    def test_exact_node_set(self):
        cid = 'BGS-TRACE-014'
        claims = {cid: {'dependencies': []}}
        with patch.object(MODULE, 'load', return_value={'nodes': [cid], 'edges': []}):
            MODULE.audit_graph(claims)
        for nodes in [None, [], [cid, cid], [cid, 'BGS-TRACE-999'], [1], {}]:
            with self.subTest(nodes=nodes):
                with patch.object(MODULE, 'load', return_value={'nodes': nodes, 'edges': []}):
                    with self.assertRaisesRegex(SystemExit, 'nodes do not match'):
                        MODULE.audit_graph(claims)

    def test_inventory_snapshot_and_statement_only_open_claim(self):
        inventory_path = MODULE.ROOT / 'record/claim_verification_inventory.json'
        inventory = json.loads(inventory_path.read_text())
        claim_005 = next(x for x in inventory['claims'] if x['id'] == 'BGS-TRACE-005')
        self.assertEqual(claim_005['state'], 'open')
        self.assertEqual(claim_005['methods'], ['unevidenced'])
        self.assertEqual(claim_005['formalization'],
                         ['formalization/Bgs/TraceStatement.lean'])
        MODULE.audit_claim_inventory()

    def test_inventory_metadata_drift_rejected(self):
        inventory = json.loads((MODULE.ROOT / 'record/claim_verification_inventory.json').read_text())
        registry = json.loads(MODULE.CLAIMS.read_text())
        mutated = copy.deepcopy(inventory)
        mutated['claims'][-1]['boundary'] = 'hypothesis silently changed'
        with patch.object(MODULE, 'load', side_effect=lambda path: mutated if
                          path.name == 'claim_verification_inventory.json' else registry):
            with self.assertRaisesRegex(SystemExit, 'metadata drift'):
                MODULE.audit_claim_inventory()

    def test_inventory_stale_source_sha_rejected(self):
        inventory = json.loads((MODULE.ROOT / 'record/claim_verification_inventory.json').read_text())
        registry = json.loads(MODULE.CLAIMS.read_text())
        mutated = copy.deepcopy(inventory)
        mutated['source_blob_sha'] = '0' * 40
        with patch.object(MODULE, 'load', side_effect=lambda path: mutated if
                          path.name == 'claim_verification_inventory.json' else registry):
            with self.assertRaisesRegex(SystemExit, 'source blob is stale'):
                MODULE.audit_claim_inventory()

    def test_nested_lean_import_closure(self):
        import tempfile
        audit_source = SOURCE.with_name('repository_audit.py')
        spec = importlib.util.spec_from_file_location('bgs_lean_coverage', audit_source)
        audit = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(audit)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            nested = root / 'formalization/Bgs/Mathlib'
            nested.mkdir(parents=True)
            (root / 'formalization/Bgs.lean').write_text('import Bgs.Mathlib\n')
            (nested.parent / 'Mathlib.lean').write_text('import Bgs.Mathlib.Example\n')
            (nested / 'Example.lean').write_text('-- proof fixture\n')
            with patch.object(audit, 'ROOT', root):
                audit.check_lean_coverage()
                (nested / 'Orphan.lean').write_text('-- unreachable\n')
                with self.assertRaisesRegex(RuntimeError, 'does not reach'):
                    audit.check_lean_coverage()
                (nested / 'Orphan.lean').unlink()
                (nested / 'Example.lean').unlink()
                with self.assertRaisesRegex(RuntimeError, 'missing active Lean import'):
                    audit.check_lean_coverage()

if __name__ == '__main__':
    unittest.main()
