#!/usr/bin/env python3
"""RESULTS.md is generated, current, and keeps the honest status statements."""
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[3]
spec = importlib.util.spec_from_file_location('render_results_t', ROOT/'computations/maintenance/render_results.py')
rr = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rr)


class ResultsRender(unittest.TestCase):
    def test_results_current(self):
        self.assertEqual((ROOT/'RESULTS.md').read_text(encoding='utf-8'), rr.render(ROOT))

    def test_states_come_from_registry(self):
        claims = {c['id']: c for c in json.loads((ROOT/'record/claims.json').read_text())['claims']}
        text = rr.render(ROOT)
        spec_data = json.loads((ROOT/'record/results_spec.json').read_text())
        for group in spec_data['groups']:
            for cid, _ in group['claims']:
                self.assertIn(f'| `{cid}` | **{claims[cid]["state"]}** |', text)
        total = len(claims)
        self.assertIn(f'| **total** | **{total}** |', text)

    def test_honest_headline(self):
        text = rr.render(ROOT)
        self.assertIn('**The BGS limit for this map is not proved.**', text)
        self.assertIn('open and is not refuted', text)
        self.assertIn('is conditional', text)
        self.assertNotRegex(text.lower(), r'r′ (is|was) refuted|bgs (is|was) proved')

    def test_spec_labels_assert_no_state(self):
        spec_data = json.loads((ROOT/'record/results_spec.json').read_text())
        for group in spec_data['groups']:
            for cid, label in group['claims']:
                # Qualifiers such as 'not proved for any p' or 'tail open' are allowed;
                # a label must not carry its own status tag.
                self.assertNotRegex(label.lower(), r'^(proved|refuted|open|conditional)\b|\((proved|refuted|open|conditional|verification-pending)\)', cid)


if __name__ == '__main__':
    unittest.main()
