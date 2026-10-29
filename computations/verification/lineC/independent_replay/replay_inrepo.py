# In-repository replay driver: runs the deposited referee engine from repo paths
# (no edits to the deposited compare_theirs.py / run_sym.py sources).
import sys
import pickle
import re
import time
from fractions import Fraction as F
from pathlib import Path

def _repo_root() -> Path:
    p = Path(__file__).resolve()
    for anc in p.parents:
        if (anc / "record" / "claims.json").is_file():
            return anc
    raise RuntimeError("BGS repo root not found")

R = str(_repo_root())
IR = R + "/computations/verification/lineC/independent_replay"
sys.path.insert(0, IR)
from sym import run_engine, evaluate, legendre  # noqa: E402

src = open(IR + "/compare_theirs.py").read()
i = src.index("def parse")
j = src.index("primes=")
exec(src[i:j])
primes = [
    q for q in range(101, 1200) if all(q % d for d in range(2, int(q**0.5) + 1))
]
DEP = R + "/evidence/executions/20261029/lineC-random-phase/independent_replay"
DATA = R + "/computations/verification/lineC/data"
srcs = {
    3: "symbolic_m1_7.log",
    4: "symbolic_m1_7.log",
    5: "symbolic_m1_7.log",
    6: "symbolic_m1_7.log",
    7: "symbolic_m1_7.log",
    8: "engine_m8.log",
    9: "engine_m9.log",
    10: "engine_m10.log",
    11: "engine_m11_def2.log",
    12: "engine_m12_def2.log",
}
ms = [int(a) for a in sys.argv[1:]] or list(range(3, 13))
failed = False
for m in ms:
    k2 = 2 * m if m <= 10 else 5
    t0 = time.time()
    terms, bydr = run_engine(m, 0, k2, nth=8, raw=True)
    dt = time.time() - t0
    dep = pickle.load(open(f"{DEP}/sym_m{m}_k{k2}.pkl", "rb"))
    same_pkl = (terms, bydr) == dep
    th = parse(DATA + "/" + srcs[m], m)
    kmax2 = None if m <= 10 else 5
    ok = True
    for p in primes:
        a, b = evaluate(terms, p, maxk2=kmax2)
        r, s, im = eval_theirs(th, p, kmin=(F(-5, 2) if kmax2 else None))
        if im != 0 or (a, b) != (r, s):
            ok = False
            print("DIFF", m, p)
            break
    if not same_pkl or not ok:
        failed = True
    print(
        f"m={m}: fresh replay == deposited pkl: {same_pkl}; == packet {srcs[m]} at {len(primes)} primes in [101,1200] ({'through p^-5/2' if kmax2 else 'all orders'}): {ok}; {dt:.1f}s",
        flush=True,
    )

if failed:
    sys.exit(1)
