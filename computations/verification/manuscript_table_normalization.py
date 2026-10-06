#!/usr/bin/env python3
"""Finite renderer-compatibility regression; no mathematical proof claim."""
import importlib.util
from pathlib import Path

root = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location(
    'fixed_map_sync', root/'computations/maintenance/sync_fixed_map_section.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
normalize = module.normalize_table_rules
old = r'''\begin{longtable}[]{ll}
\toprule
A & B \\
\midrule
\endhead
1 & 2 \\
\bottomrule
\end{longtable}
'''
new = old.replace(r'\toprule', r'\toprule\noalign{}').replace(
    r'\midrule', r'\midrule\noalign{}').replace(
    '\\bottomrule\n\\end{longtable}', '\\end{longtable}').replace(
    '\\endhead\n', '\\endhead\n\\bottomrule\\noalign{}\n\\endlastfoot\n')
assert normalize(new) == old
assert normalize(old) == old
assert normalize(new + new) == old + old
assert normalize(new.replace('1 & 2', '1 & 3')) != old
# Do not discard an actual last-foot text block.
nonempty = new.replace('\\endlastfoot', 'Footnote\n\\endlastfoot')
assert normalize(nonempty) == nonempty
print('PASS manuscript table presentation normalization: five controls')
