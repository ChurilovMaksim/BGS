import os as _os
_BGS_ROOT = _os.path.dirname(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))
import sys, os
sys.path.insert(0, _BGS_ROOT + r"\src")
from master_general import validate_config

for (A, N, r, F) in [([2,1,1,1], 101, 2, [(1,0),(0,1)]),
                     ([2,1,1,1], 101, 4, [(1,0)]),
                     ([3,1,2,1], 101, 4, [(1,0)])]:
    res = validate_config(A, N, r, F)
    tag = "PASS" if res["passed"] else "FAIL"
    errs = " ".join(f"({rr['err_re']:.1e},{rr['err_im']:.1e})" for rr in res["rows"])
    print(f"[{tag}] r={r} A={A}: err {errs} ({res['dt']:.1f}s)")
