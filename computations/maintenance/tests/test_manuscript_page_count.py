"""Fail-closed parsing of TeX's line-wrapped page count."""
import importlib.util
from pathlib import Path
import unittest

PATH = Path(__file__).resolve().parents[1] / 'build_unified_manuscript.py'
SPEC = importlib.util.spec_from_file_location('bgs_manuscript_build', PATH)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)

class ManuscriptPageCountTests(unittest.TestCase):
    def test_wrapped_and_malformed_counts(self):
        for text, expected in [
            ('Output written on x.pdf (259 pages, 123 bytes).', 259),
            ('Output written on /long/path/x.pdf (2\n59 pages, 123 bytes).', 259),
            ('Output written on x.pdf (2\n5\n9 p\na\ng\ne\ns, 123 bytes).', 259),
            ('Output written on x.pdf (1 page, 123 bytes).', 1),
            ('Output written on x.pdf (0 pages, 0 bytes).', None),
            ('Output written on x.pdf (2x59 pages, 123 bytes).', None),
            ('Output written on x.pdf (259 bytes).', None),
            ('No pages of output.', None),
        ]:
            with self.subTest(text=text):
                self.assertEqual(MODULE.page_count_from_log(text), expected)

if __name__ == '__main__':
    unittest.main()
