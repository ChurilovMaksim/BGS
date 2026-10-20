# Toolchain follow-up, 20 October 2026

Source commit: `cfe74abafb61b590a2c3aff4642525a94d9f639e`.
This is a narrow follow-up to the repository reconciliation, using 69 authenticated
source files, not a full checkout. Every materialized source blob still matches
the pinned remote tree after compilation; see verified_sources.json.

## Results and boundaries

- Lean 4.33.1: all 24 active Std modules compiled, 27 Lake jobs.
  CoherenceBudget.budget_positive prints only [propext, Quot.sound].
  It certifies natural-number positivity, not operator codimension or BGS.
  Other modules' native_decide trust dependencies remain visible in the full log.
  The Mathlib draft JackArithmeticCore is outside the active build.
- All 26 CMake C++ targets compiled successfully (exit 0), using GNU 13.3.0,
  CMake 3.29.6 and official Boost 1.92.0 headers. This receipt is compilation,
  not a new runtime replay of the 26 programs.
- No mathematical claim was promoted. BGS and TRACE-005 remain open.
- Prior CI failures had no executed runner steps; logs could not be retrieved.
  Their cause remains unknown. This is not a green-CI receipt.

## Reproduction and portability

Official downloads:
https://github.com/leanprover/lean4/releases/download/v4.33.1/lean-4.33.1-linux.tar.zst
https://github.com/boostorg/boost/releases/download/boost-1.92.0/boost-1.92.0-b2-nodocs.tar.gz

Archive SHA256 values and compiled Lean output hashes are in receipt.json.
Archives were extracted with --no-same-owner. Native Lean path discovery failed;
the existing repository lean_proc_self_compat.c adapter redirects only the own-PID
executable readlink to /proc/self/exe. It changes no proof kernel function.

Commands (ROOT is the authenticated source directory; TOOLS the external tool directory):

```sh
cc -shared -fPIC -O2 "$ROOT/computations/maintenance/lean_proc_self_compat.c" -ldl -o "$TOOLS/lean_compat.so"
PATH="$TOOLS/lean-4.33.1-linux/bin:$PATH" LD_PRELOAD="$TOOLS/lean_compat.so" bash "$ROOT/computations/maintenance/build_lean_verified.sh" lean_build.log
cmake -S "$ROOT" -B cpp-build329 -DCMAKE_BUILD_TYPE=Release -DBOOST_ROOT="$TOOLS/boost-1.92.0" -DBoost_NO_BOOST_CMAKE=ON
cmake --build cpp-build329 -j4
```

The successful CMake command uses 3.29.6, within the project's >=3.20 range.
Earlier Boost b2 installation and CMake 4.4.4 package discovery attempts failed;
their logs/excerpt are retained. No fake package configuration or project source
patch was used. The original full Boost installation log is represented by a
hash plus explicitly truncated excerpt.

The earlier reconciliation's Python, PDF and repository-wide checks were not
repeated here. This packet supplements their dated scope rather than overwriting it.
