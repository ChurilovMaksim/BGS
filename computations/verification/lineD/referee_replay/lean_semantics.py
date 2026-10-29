if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import os, re, numpy as np, core
from structure import rad_elems, supp_via_rad
# Repo-relative: formalization/Bgs/LineDCerts.lean
# (research-box path was /workspace/bgs-lineD/lean/LineDCerts.lean).
_LEAN = os.path.normpath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..', 'formalization', 'Bgs', 'LineDCerts.lean'))
src = open(_LEAN).read()
def getlist(name):
    m = re.search(r'def %s : List \(List Nat\) :=\s*(\[.*?\]\])' % name, src, re.S)
    return eval(m.group(1))
for m, M, name in [(4, 96, 'coll4'), (6, 560, 'coll6')]:
    L = getlist(name)
    dat = core.data(m); D = dat['D']; W = core.enum_fix(dat); B = core.enum_V(dat); R = rad_elems(dat, B)
    supp = supp_via_rad(dat, 1, W, R) > 1e-9
    canon, osz = core.gamma_canon(W, D)
    idx = {tuple(w): i for i, w in enumerate(W)}
    ids = [idx.get(tuple((D//M)*np.array(x) % D)) for x in L]
    print(name, 'all in Fix:', all(i is not None for i in ids), '| all on support:', all(supp[i] for i in ids),
          '| distinct Gamma classes:', len(set(canon[i] for i in ids)), 'of', len(L))
    # full K=1 collision set on support (Gamma classes with S_1 = 0)
    S1 = core.Sk(W, D, 1)
    zero = set(canon[i] for i in np.where(supp & (np.abs(S1) < 1e-9))[0])
    print('   Gamma classes on support with S_1=0:', len(zero), '| equals Lean list:', zero == set(canon[i] for i in ids))
    print('   orbit sizes |Gamma xi| of Lean list:', sorted(osz[i] for i in ids))
