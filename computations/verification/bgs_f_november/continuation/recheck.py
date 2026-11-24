"""Run fresh exact and floating diagnostic checks, comparing to the delivered reference outputs."""

# Repository-wide fail-closed verification guard.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

from pathlib import Path
import subprocess,sys,os,json
base=Path(__file__).resolve().parent
env=dict(os.environ,OPENBLAS_NUM_THREADS="1")
checks=[("analytic_checks.py","exact.json"),("clock_control.py","clock.json"),
        ("partners.py","partners.json"),("exact_paths.py","exact_paths.json"),("parity.py","parity.txt")]
for src,dst in checks:
    live=subprocess.check_output([sys.executable,str(base/src)],env=env,text=True)
    assert live==(base/"data"/dst).read_text(),dst
path=base/"bridge_checks.py"
actual=json.loads(subprocess.check_output([sys.executable,str(path)],env=env,text=True))
target=json.loads((base/"data/bridges.json").read_text())
assert [(x["N"],x["m"],x["t"]) for x in actual]==[(x["N"],x["m"],x["t"]) for x in target]
print("Six continuation checks passed.")
