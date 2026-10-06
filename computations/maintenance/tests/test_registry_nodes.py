"""The dependency graph must list every registered claim exactly once."""
import importlib.util
from pathlib import Path
import unittest
from unittest.mock import patch

SOURCE = Path(__file__).resolve().parents[2] / 'verification/scientific_registry_audit.py'
SPEC = importlib.util.spec_from_file_location('bgs_registry_nodes', SOURCE)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)

class RegistryNodesTests(unittest.TestCase):
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
