# November BGS-F replay

From the repository root, with the pinned scientific Python dependencies:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python computations/verification/bgs_f_november/verify_all.py
```

The runner checks local inputs against its SHA-256 manifest and runs 35
finite checks. `--quick` selects seven checks of the latest chapter code.
The replay mixes exact integer, rational and finite-field checks with
explicitly numerical comparisons; it does not prove the asymptotic arguments,
and it does not run Lean. Some finite comparisons use different coupling
values as test inputs. See the proof notes for their scope.

The default Pell verifier checks rational inequalities from the recorded
diagonal outputs; it does **not** recompute the integer matrix powers. To
regenerate the four input matrices and recompute those powers using g++17 and
signed 128-bit integers, add `--rebuild-pell`. This is the opt-in slow check:
it uses a temporary copy, requires approximately 40 MB of matrix input
storage plus the in-memory sparse products, and compares the output
diagonals byte for byte. The source package's large generated input matrices
are not vendored here. A successful floating-point reproduction is a
separate control, not the exact certificate.

The chapter names match the supplied BGS-F cumulative packet; the selective
integration and evidence boundaries are recorded in the
[research index](../../../mathematics/fixed-map/archive_continuation/README.md).

The vendored Python inputs that depend on assertions carry the repository's
standard early assertion guard. The guards do not change the certificate
arithmetic. Run without Python optimization.
Archive-named check scripts remain CLI entry points; their implementations
have packet-specific names so the conservative dependency scanner does not
mistake unrelated imports in older parts of BGS for packet imports.
