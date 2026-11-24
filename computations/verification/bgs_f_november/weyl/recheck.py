"""Re-run all of the new exact checks plus the independent floating-point diagnostics."""

# Repository-wide fail-closed verification guard.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

from pathlib import Path
import json
import os
import subprocess
import sys

base = Path(__file__).resolve().parent
env = {**os.environ, 'OPENBLAS_NUM_THREADS': '1'}
checks = {'constants': 'constants', 'returns': 'returns', 'rigidity_checks': 'rigidity',
          'orbit_graph': 'orbit_graph', 'resonance_checks': 'resonances', 'matrices': 'matrices'}
for script, filename in checks.items():
    live = json.loads(subprocess.check_output([sys.executable, str(base/(script+'.py'))], env=env))
    target = json.loads((base/'data'/(filename+'.json')).read_text())
    if script != 'matrices':
        assert live == target, script
    else:
        assert [(x['N'],x['xi']) for x in live] == [(x['N'],x['xi']) for x in target]
        assert all(x[key] < 2e-11 for x in live for key in x if key.endswith('_error'))
    print('OK', script)
