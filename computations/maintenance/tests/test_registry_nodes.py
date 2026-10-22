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

if __name__ == '__main__':
    unittest.main()
