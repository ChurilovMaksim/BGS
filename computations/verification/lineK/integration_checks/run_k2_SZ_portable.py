"""Portable rerun of computations/verification/lineK/code/k2_SZ.py (owner audit of PR #63).

k2_SZ.py is pinned by sha256 in evidence/executions/20261031/lineK/receipt.json and in the author's manifest, and it reads the
Line J3 certificates from the absolute scratch path /workspace/bgs-lineJ/J3. Rather than editing the pinned file, this wrapper runs
its unchanged source with that one path replaced by the repository copy computations/verification/lineJ/J3, in a temporary
directory, and compares the output with the committed logs/k2_SZ.json and logs/k2_SZ.log (byte for byte).
Needs python-flint (0.9.0 was used). Run from anywhere: python3 computations/verification/lineK/integration_checks/run_k2_SZ_portable.py
Exit status 0 iff both outputs are byte-identical to the committed ones."""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')
import contextlib, io, os, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
LINEK = os.path.normpath(os.path.join(HERE, '..'))
J3 = os.path.normpath(os.path.join(LINEK, '..', 'lineJ', 'J3'))
SRC = os.path.join(LINEK, 'code', 'k2_SZ.py')
OLD = "J3='/workspace/bgs-lineJ/J3'"

src = open(SRC, encoding='utf-8').read()
assert src.count(OLD) == 1, 'k2_SZ.py changed: path line not found exactly once'
src = src.replace(OLD, 'J3=' + repr(J3))
with tempfile.TemporaryDirectory() as tmp:
    os.makedirs(os.path.join(tmp, 'logs'))
    cwd = os.getcwd(); os.chdir(tmp)
    buf = io.StringIO()
    try:
        with contextlib.redirect_stdout(buf):
            exec(compile(src, SRC, 'exec'), {'__name__': '__main__', '__file__': SRC})
        new_json = open(os.path.join(tmp, 'logs', 'k2_SZ.json'), 'rb').read()
    finally:
        os.chdir(cwd)
new_log = buf.getvalue().encode('utf-8')
ref_json = open(os.path.join(LINEK, 'logs', 'k2_SZ.json'), 'rb').read()
ref_log = open(os.path.join(LINEK, 'logs', 'k2_SZ.log'), 'rb').read()
ok_json, ok_log = new_json == ref_json, new_log == ref_log
print('k2_SZ.json byte-identical:', ok_json)
print('k2_SZ.log byte-identical: ', ok_log)
sys.exit(0 if ok_json and ok_log else 1)
