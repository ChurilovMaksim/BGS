"""
AUDIT-ONLY wrapper. Does NOT modify any project file.

Some project scripts hard-code the path
    C:\\Users\\churi\\OneDrive\\Desktop\\project_1\\BGS\\{src,artifacts}
which does not exist on this machine. This wrapper:
  * prepends the REAL src dir to sys.path
  * redirects file opens under the stale OneDrive artifacts dir into
    C:\\Users\\churi\\Desktop\\BGS\\_audit\\redirect\\
so the underlying mathematics can still be executed and compared.

usage: python audit_wrapper.py <script.py>
"""
import os as _os
_BGS_ROOT = _os.path.dirname(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))
import builtins
import io
import os
import runpy
import sys

REAL_ROOT = _BGS_ROOT
REAL_SRC = os.path.join(REAL_ROOT, "src")
STALE = r"c:\users\churi\onedrive\desktop\project_1\bgs\artifacts"
REDIRECT = _BGS_ROOT + r"\_audit\redirect"
os.makedirs(REDIRECT, exist_ok=True)

sys.path.insert(0, REAL_SRC)

_real_open = builtins.open


def _patched_open(file, *a, **kw):
    try:
        s = os.fspath(file)
    except TypeError:
        return _real_open(file, *a, **kw)
    if isinstance(s, str) and STALE in s.replace("/", "\\").lower():
        s = os.path.join(REDIRECT, os.path.basename(s))
    return _real_open(s, *a, **kw)


builtins.open = _patched_open

target = sys.argv[1]
sys.argv = sys.argv[1:]
runpy.run_path(target, run_name="__main__")
