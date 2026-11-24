
# Repository-wide fail-closed verification guard.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

from pathlib import Path
import json, os, sys, subprocess
p=Path(__file__).resolve().parent
for script, name in [('certify.py','certificates'),('harmonic.py','harmonic'),('diagnostics.py','diagnostics'),('harmonic_diagnostic.py','harmonic_diagnostic')]:
    x=json.loads(subprocess.check_output([sys.executable,str(p/script)],env={**os.environ,'OPENBLAS_NUM_THREADS':'1'}))
    y=json.loads((p/'data'/(name+'.json')).read_text())
    if name in ('certificates','harmonic'):
        assert x==y
    else:
        assert [r['N'] for r in x]==[r['N'] for r in y]
        if name=='diagnostics':
            assert max(r['parseval_error']+r['covariance_error'] for r in x)<1e-12
    print('OK',script)
