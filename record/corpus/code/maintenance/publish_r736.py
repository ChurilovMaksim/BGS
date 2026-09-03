"""Append the run-73.6 block (large-m attempt and the control it produced) to
LEDGER.md and THEORY.md, and add the paper subsection.  Idempotent."""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

BLOCK = r"""
### R73.6 — Large-m attempt: an interpretation error caught, and a decisive control

**What was attempted.** Push the parity-desymmetrised ratio measurement from
m = 673 (R72) to m ≈ 1674 at the only admissible design point with eps = +1 and
large multiplet: p = 95419, k = K = 57, dim H_lam = 95419//57 = **1674**.

**What went wrong twice.** The first build died at 1280/1674 columns under the
8 GB ceiling (basis 2.4 GB plus an equally large temporary in `apply_T`). The
rewrite (`src/diagnostics/desym_large_m2.py`) removed two N x (m/2) arrays by rotating inside
the small space, and completed — **but with the target set to m = 1280, i.e. a
PROPER subspace of the 1674-dimensional eigenspace.** A proper subspace of H_lam
is not parity invariant, so the "parity split" it reports is not the
desymmetrisation of Theorem D. The diagnostic that exposed this was already in the
output: `max |off-parity block| = 1.4-1.6e-2`, versus `<= 2.2e-15` in the genuine
R72 runs. A guard is now in the script (it prints
`dim H_lam = p//K` and refuses to call the run a desymmetrisation unless
`|m - p//K| <= 1`, and reports how far the parity eigenvalues are from +-1).

**What the run actually measured, and why it is valuable.** A random
1280-dimensional subspace *inside* the cat-map eigenspace, with the same
single-orbit observable:

    full   <r~> = 0.5963 +- 0.0034   z_GUE = -0.45   z_GOE = +9.09   z_SUP = +18.61
    "plus"  <r~> = 0.5964 +- 0.0023   z_GUE = +0.09   z_GOE = +5.76
    "minus" <r~> = 0.5862 +- 0.0051   z_GUE = -1.13   z_GOE = +4.96

i.e. **exactly GUE, 9 sigma from GOE**. Placed beside the earlier results this
completes a three-way control and confirms the mechanism of Theorem E:

| subspace | statistics |
|---|---|
| Haar-random subspace of C^N (R72) | GUE, `z_GUE = -0.5 … -1.1` |
| random subspace INSIDE H_lam, dim 1280 of 1674 (R73) | GUE, `z_GUE = -0.45` |
| FULL H_lam, parity-desymmetrised (R72/R73) | **GOE**, `z_GOE = -0.9 … +0.4` |

The orthogonal class is a property of the **full** eigenspace, where the
arithmetic antiunitary `Theta_u = U_tau U_M o conj` acts; break invariance by
passing to a non-invariant subspace and the statistics revert to GUE. That is
precisely what Theorem E predicts, and it is an independent confirmation obtained
by accident.

**Status.** The largest bona fide desymmetrised measurement remains m = 673
(blocks of 337) from R72.4, plus the m = 105/150/337 ratio-statistic points of
R72.4. Reaching m = 1674 needs > 8 GB (about 5.5 GB peak) or a mixed-precision
basis; recorded as the priority for a bigger box, not as a result.

**LESSON 73-A.** State the target dimension of an eigenspace computation as
`p // K` and assert it. Two of the three defects found in this workspace's history
(the R67-R70 `U[:, idx]` basis, and this one) are the same class of error:
constructing something that is not the subspace one believes it to be. The cheap
guard is an assertion on the dimension plus a check that the intended symmetry
really acts (here: parity eigenvalues equal to +-1 to machine precision, and the
off-block of the compression equal to 0).
"""

TH = r"""
### 11.6 A three-way subspace control (and a caught interpretation error)

An attempt to push the desymmetrised measurement to m = 1674 (p = 95419, K = 57)
was set up with target m = 1280, i.e. a PROPER subspace of the 1674-dimensional
eigenspace. A proper subspace of H_lam is not parity invariant, so what was
measured is not a desymmetrisation; the diagnostic `max |off-parity block| =
1.4-1.6e-2` (against `<= 2.2e-15` in the genuine runs) exposed it. The run is
therefore recorded as a control, and it is a decisive one:

| subspace | <r~> | reading |
|---|---|---|
| Haar-random subspace of C^N | 0.593-0.598 | GUE (`z_GUE = -0.5 … -1.1`) |
| random subspace inside H_lam (1280 of 1674) | 0.5963 +- 0.0034 | GUE (`z_GUE = -0.45`, `z_GOE = +9.09`) |
| FULL H_lam, parity blocks | 0.529-0.542 | **GOE** (`z_GOE = -0.9 … +0.4`) |

So the orthogonal class lives on the **full** eigenspace, where the arithmetic
antiunitary of section 11.1 acts; restricting to a non-invariant subspace returns
GUE. This is an independent confirmation of Theorem E's mechanism.

The largest bona fide desymmetrised measurement remains m = 673 (blocks of 337).
Reaching m = 1674 requires more than 8 GB.

**Lesson.** Always assert `m == p // K` for an eigenspace computation, and check
that the intended symmetry really acts on the constructed basis (parity
eigenvalues equal to +-1 to machine precision, off-block of the compression zero).
Two of the three defects found in this workspace's history are the same class of
error: building something that is not the subspace one believes it to be.
"""


def patch(path, marker, text):
    p = os.path.join(ROOT, path)
    s = open(p, encoding="utf-8", errors="surrogateescape").read()
    if marker in s:
        return f"{path}: already present"
    open(p, "w", encoding="utf-8", errors="surrogateescape").write(
        s.rstrip() + "\n" + text)
    return f"{path}: appended"


print(patch("LEDGER.md", "R73.6 — Large-m attempt", BLOCK))
print(patch("THEORY.md", "11.6 A three-way subspace control", TH))
