"""Recompute each certificate and check the independent small-matrix diagnostics."""

# Repository-wide fail-closed verification guard.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

from pathlib import Path
import json
import os
import subprocess
import sys

base = Path(__file__).resolve().parent
def run(name):
    out = subprocess.check_output([sys.executable, str(base / (name + '.py'))],
                                 env={**os.environ,'OPENBLAS_NUM_THREADS':'1'})
    return json.loads(out)

for name in ('certificates','gauss','reversal','abel','chords',
             'windows_exact','word_law','weight','paths','opposite'):
    current=run(name)
    previous=json.loads((base/'data'/(name+'.json')).read_text())
    if name in ('paths','opposite'):
        field='max_error' if name=='opposite' else 'maximum_identity_error'
        assert [(r['N'],r['m']) for r in current]==[(r['N'],r['m']) for r in previous]
        assert all(r[field]<2e-11 for r in current)
        for actual, expected in zip(current, previous):
            for key in actual:
                assert abs(actual[key]-expected[key])<2e-10
    else:
        assert current==previous
    print('OK',name,flush=True)
