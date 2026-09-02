"""Referee test of the LEDGER R82.12 assertion that the matching (k0, parity,
scale c) reproducing the measured mu_4 curve is UNIQUE.  Enumerates ALL
(parity, k0) blocks and ALL candidate scales c at N=199 and reports every
combination that passes the canonical 5-probe test at 1e-8.
"""
import os
import sys

import numpy as np

SRC = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src")
sys.path.insert(0, SRC)
from r82j_closed_form import build_closed_form  # noqa: E402

N, K = 199, 11
d = np.load(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                         "artifacts", "r82", "q_curve_N199.npz"))
q_meas, mu4_meas = d["q"].astype(int), d["mu4"]
meas = dict(zip(q_meas.tolist(), mu4_meas.tolist()))
probes = [1, 2, 3, 5, 7]

matches = []
for parity_odd in (True, False):
    for k0 in range(K):
        cf, m = build_closed_form(N, K, 139, k0, parity_odd, probes)
        v0 = cf[probes[0]]["mu4"]
        for c, vv in meas.items():
            if abs(vv - v0) >= 1e-8:
                continue
            ok = all(abs(cf[p]["mu4"] - meas.get((c * p) % N, np.nan)) < 1e-8
                     for p in probes)
            if ok:
                matches.append((parity_odd, k0, c, m))
                print(f"MATCH: parity_odd={parity_odd} k0={k0} c={c} m={m}",
                      flush=True)
print(f"total matches: {len(matches)}")
