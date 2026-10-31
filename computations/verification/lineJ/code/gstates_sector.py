"""Sector finite factor (Line J): the rank-1 sector a in {0,2,4,6} of the 16-state automaton acts on f_a by the scalar e(a n/8)
(proved exactly by sectors_exact.py).  Drop-in replacement for gstates.finite with ONE automaton state; the d=7 twist 3-cycle kept.
Sector chosen by environment variable BGS_SECTOR."""
import os, sys
sys.path.insert(0,'/workspace/bgs-lineI/dom_v3')
from gstates import g2params, taus7
SEC=int(os.environ['BGS_SECTOR']); assert SEC in (0,2,4,6)
def reach(P,Nmax): return [0], None
def finite(P,idx,tg,n,cyc):
    ph8=(-SEC*n)%8          # entry e(-ph8/8) = e(SEC n/8)
    if cyc is None: return [(0,0,ph8,0)]
    return [((i+1)%3,i,ph8,cyc[i]) for i in range(3)]
