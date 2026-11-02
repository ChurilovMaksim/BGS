"""Wave 41 sweep driver: runs all cases sequentially, small -> large.
Each case: run_case from wave41_LemmaU_sweep (two-phase, classifier,
rigid sampling where requested). Failures per case are logged, not fatal.
"""
import sys
import time
import traceback

sys.path.insert(0, ".")
from wave41_LemmaU_sweep import run_case

# (m, pa, fa, pb, fb, rigid) ; u-odd first (PAIR regime), then u-even.
CASES = [
    # u-odd, small/medium
    (42, 5, 1, 13, 2, True),
    (54, 5, 1, 53, 1, True),
    (54, 5, 1, 197, 1, True),
    (70, 13, 1, 29, 1, True),
    (90, 5, 1, 29, 1, True),
    (90, 5, 1, 197, 1, True),
    (102, 5, 1, 101, 1, True),
    (102, 5, 1, 137, 1, True),
    (114, 5, 1, 37, 1, True),
    (126, 5, 1, 13, 1, True),
    (126, 5, 1, 197, 1, True),
    (30, 5, 2, 29, 1, True),   # re-run with new classifier
    # u-even, supplementary beta-cycle tests
    (12, 3, 2, 11, 1, False),
    (36, 3, 2, 11, 1, False),
    (36, 3, 1, 73, 1, False),
    (36, 3, 2, 73, 1, False),
    (36, 11, 1, 73, 1, False),
    (60, 3, 2, 19, 1, False),
    (60, 11, 1, 19, 1, False),
    (60, 3, 2, 59, 1, False),
    (60, 11, 1, 59, 1, False),
    (60, 19, 1, 59, 1, False),
    (84, 3, 2, 83, 1, False),
    (84, 11, 1, 83, 1, False),
    (84, 3, 2, 113, 1, False),
    (84, 11, 1, 113, 1, False),
    # rigid big case (smallest rigid-feasible pair)
    (90, 29, 1, 197, 1, True),
]

if __name__ == "__main__":
    for (m, pa, fa, pb, fb, rigid) in CASES:
        t0 = time.time()
        print(f"===== CASE m={m} ({pa}^{2 * fa},{pb}^{2 * fb}) "
              f"rigid={rigid} =====", flush=True)
        try:
            run_case(m, pa, fa, pb, fb, rigid=rigid)
        except Exception:
            print("CASE FAILED:", flush=True)
            traceback.print_exc()
        print(f"===== done in {time.time() - t0:.0f}s =====", flush=True)
    print("SWEEP COMPLETE", flush=True)
