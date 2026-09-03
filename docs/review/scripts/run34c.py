import os as _os
_BGS_ROOT = _os.path.dirname(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))
import sys
sys.path.insert(0, _BGS_ROOT + r"\src")
import numpy as np
from master_formula_strong import find_orbit_H

for p in [2207, 3001, 1597, 2161, 101, 199, 211]:
    H=find_orbit_H(p,[2,1,1,1])
    if H: print(f"p={p}: k={len(H)} SPLIT")
    else: print(f"p={p}: INERT")
