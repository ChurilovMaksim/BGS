import os as _os
_BGS_ROOT = _os.path.dirname(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))
import sys
sys.path.insert(0, _BGS_ROOT + r"\src")
from phase2_beta import find_primes
c = find_primes(3000, 6600, kmax=17)
print("found:", len(c))
print(c[:20])
