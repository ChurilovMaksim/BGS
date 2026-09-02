import os as _os
_BGS_ROOT = _os.path.dirname(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))
import sys
sys.path.insert(0, _BGS_ROOT + r"\src")
import phase2_beta as P

print("filter line check:")
c = P.find_primes(3000, 6600, kmax=17)
chosen = sorted([t for t in c if t[1] <= 17], key=lambda t: t[0])[-5:]
print("chosen:", chosen)

sp, sizes = P.unitary_spacings(chosen[-1][0])
print("p=", chosen[-1][0], "n spacings:", len(sp),
      "cluster sizes:", sizes[:10])
