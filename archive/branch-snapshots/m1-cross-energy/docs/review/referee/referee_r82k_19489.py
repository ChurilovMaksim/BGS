"""Referee reproduction of src/r82k_bgs_large_m.py at the smallest design
only: N=19489, K=29, nq=2 systems (per audit instructions), matched GOE at
8x the sample count.  Calls the canonical run_design() unchanged, so the
logic is exactly the canonical one.
"""
import json
import os
import sys

import numpy as np

SRC = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src")
sys.path.insert(0, SRC)
from r82k_bgs_large_m import run_design  # noqa: E402


def main():
    rng = np.random.default_rng(820012)
    row = run_design(19489, 29, 2, rng)
    dest = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        "referee_bgs_large_m_19489_nq2.json")
    with open(dest, "w") as fh:
        json.dump(row, fh, indent=1)
    print("artifact ->", dest, flush=True)


if __name__ == "__main__":
    main()
