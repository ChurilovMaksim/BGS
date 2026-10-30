"""Finite-N check of the a=7 law for the Line B FULL kick against independent direct physical traces |Tr (K M_N)^m|^2
(matrix-free chirp-DFT code of the Line E packet, review/indep_trace_full.py; values from review/indep_trace.jsonl)."""
import json
from cmp_full import KICKS, ghat_of
from tm49 import Z_TO
G = ghat_of(KICKS['full'], 2.0, 48)
for m, N, direct in ((11, 7923, 262377.6702567745), (7, 43, 17.86071355318158)):
    for K in (30, 40):
        z = Z_TO(G, m, 7, +1, 2.2, K, Nfin=N)
        print(json.dumps(dict(m=m, N=N, N_mod_h=-196, direct_abs2=direct, TO_abs2=abs(z)**2, rel=abs(abs(z)**2 - direct)/direct, K=K)), flush=True)
