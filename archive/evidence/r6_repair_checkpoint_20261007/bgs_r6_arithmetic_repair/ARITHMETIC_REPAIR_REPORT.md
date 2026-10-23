# R6-03 / R6-04 arithmetic API repair

## State and boundaries

- Isolated full checkout: /workspace/shared/bgs_r6_repair_checkout.
- HEAD remained d37c92e563d10d25bb1d6ab85bedffc1f160f773. The supplied pre-existing staged tree is 19f7474e6169d590e81dd391fbdbc21fd2f3b03d; it was not restaged or committed by this worker.
- Three arithmetic modules changed, and one maintenance unittest file was added. finite_field.py is unchanged. No edit to canonical /workspace/shared/BGS, no commit, no publish, no staging.
- Complete scoped diff: arithmetic_repair.patch (includes the untracked new test).
- This is a finite implementation/input-contract repair, not a mathematical theorem defect, a proof audit, or a BGS universality claim.

## Verified original findings

before.json records the actual pre-repair probes:

1. p=199, K=11, m=2, H=subgroup(199,11,139), q=np.int64(1+199*2**50)=224054081461682177. histogram_trace differed from q=1 by 0.5050405260556705 and emitted a scalar-multiply overflow warning; orbit_matrix's difference was 0.
2. build_closed_form(199,11,139,0,True,[q]) accepted 1.9, True, '1', and np.float64(1.9), producing the q=1 key by int coercion.
3. Fractional q=1.5 was accepted by orbit_matrix and histogram_trace, whose second traces differed by 0.3060695904903577.

The final after_probe.py was executed separately on Python 3.12 and 3.13, with and without -O. The large-q histogram and matrix representative deltas are exactly 0 in all four runs. The dense second-trace agreement error is approximately 8.9e-16, with no warnings. All 15 invalid-q API calls per run raised the explicit integer-contract ValueError.

## Exact implementation changes

magnetic_quotient.py:

- Public p inputs become Python integers and require odd prime moduli. Vectorized orbit/gauge paths reuse jacobi.require_supported_prime, which rejects moduli beyond the safe int64 product bound before primality testing or allocation.
- subgroup validates/converts K and h; h is reduced modulo p before order and pow operations.
- H entries are individually checked before any NumPy conversion and reduced modulo p. Empty H, zero, and -1 are rejected. Existing signed-orbit overlap/dimension checks are retained; callers must still supply a genuine subgroup.
- word_histogram converts m to a positive Python integer and retains its ten-million-word cap and recurrence unchanged.
- orbit_matrix, gauss_real_gauge, and histogram_trace validate q and reduce it modulo p before scalar/NumPy multiplication. Zero q remains excluded from those three APIs.
- Gauge indices are exact integer entries, reduced modulo p-1 before np.outer. dlog uses the existing shape/type/range validator; no discrete-log identity theorem is inferred by range validation.
- Trace/mean K and m are positive exact Python integers. Histogram-content normalization or validation was not added.

 twisted_jacobi.py:

- square_roots_mod_prime validates/converts value and prime. find_design_eigenvalue similarly checks prime, subgroup_order, and trace.
- build_closed_form validates/converts prime, subgroup_order, eigenvalue, and residue_class; q_values entries use require_integer in place of int coercion. Vectorized p uses the shared product bound. Eigenvalue order and empty-sector checks are preserved.
- odd_parity now requires bool or np.bool_, then preserves its logical value. False and True remain valid. Numeric 0/1, their float/NumPy integer counterparts, strings, and None are rejected explicitly.
- Maintained Python caller survey found only computations/verification/twisted_jacobi_regression.py, which already passes bool(reference_design['parity_odd']). No production int0/1 caller was found. Survey saved in build_closed_form_callers.txt.

jacobi.py:

- _integer_array now creates its inspection array with dtype=object. This preserves bool/int types in a mixed Python sequence before require_integer checks; the final array remains int64. Existing scalar ranges and domain semantics are unchanged.

## Compatibility impact

- Previously coercible floats (including whole-valued floats), booleans used as integer parameters, numeric strings, complex numbers, fractions, and None now fail with ValueError at the explicit type boundary.
- NumPy signed/unsigned integer scalars remain supported. Large uint64 values above int64 max are reduced as Python integers before safe int64 conversion. Arbitrarily large positive and negative Python residue representatives remain valid for h/H/q/gauge indices/eigenvalue/residue_class/trace, as applicable.
- odd_parity accepts actual bool and np.bool_ only; prior numeric equality-based sector selection is intentionally tightened.
- Unsupported oversized vectorized moduli now fail explicitly, and nonpositive trace orders/counts or malformed H domains fail explicitly.
- Counter keys/counts are a caller contract: canonical exact integer histograms, such as word_histogram's Python-integer output. Counter-content validation and new histogram normalization/model semantics are explicitly out of scope. The repair does not certify all Python containers, a genuine-log identity from a range-valid dlog array, or full subgroup structure from type checks alone.
- No recurrence, orbit-matrix normalization, Fourier convention, histogram formula, or reference evidence was changed.

## Bounded test coverage

The new suite contains 18 test methods. It executes 533 expected-exception probes covering the named public integer fields, H/indices/dlog entry types and shapes/ranges, zero/negative domains, oversized vectorized moduli, and strict boolean parity. Dedicated bad-type probes require the integer-contract diagnostic, so an unrelated order/domain error cannot count as type validation.

Positive/finite controls include:

- The exact reported overflow probe, signed/unsigned NumPy integer acceptance, untouched caller H arrays, enormous positive/negative representatives (10**80 offsets), uint64 representatives beyond int64 max, and individual closed-form q checks to prevent duplicate-key overwrites from hiding defects.
- 117 dense-matrix-power versus exact-word-histogram trace cases: p=7,K=3,m=1..4,q=1..6; p=31,K=5,m=1..3,q=1..30; p=199,K=11,m=2,q in {1,2,198}. Complex128 tolerance 1e-10.
- 1,144 modular-root comparisons with an independent exhaustive x*x % p oracle: every residue for p in {3,5,7,11,13,17,31,199}, each tested in four representative forms. This covers both Tonelli-Shanks and p=3 mod 4 branches.
- Both bool parity sectors and both np.bool_ logical values.

The same final new suite passed on Python 3.12.14 / NumPy 2.3.5 and Python 3.13.5 / NumPy 2.2.4, normal and -O. unittest's explicit checks remain active under optimization. An isolated copy of original HEAD arithmetic modules fails the final new suite; baseline_contract_control.json pins that real old-source negative control. It is not a synthetic theorem mutation.

Existing focused checks, on both interpreters:

- magnetic_quotient_regression.py normal: 32,054 pairing orientations; 18 matrix/gauge cases at six designs; 14 histograms and 324 nonzero-q trace comparisons; reciprocal finite controls.
- The same magnetic script with a newly built independent C++ affine-word verifier: all 14 canonical histograms compare exactly. The C++ source was not edited; compiler/source/binary pins are in cpp_build_receipt.json.
- magnetic_scalar_certificate.py normal: six exact cyclic-convolution histograms and six scalar matrix comparisons.
- twisted_jacobi_regression.py normal and -O: 500 scalar-vs-BLAS entries at (461,23) and 160 at (19489,29); all 198 preserved q-moment levels at N=199; only the default deterministic 12 of 3,570 levels at N=3571. The full N=3571 curve was not rerun.
- spectral_integer_window_regressions.py normal and -O, current_regression.py normal, and cayley_jacobi_trace_regression.py normal all passed in their declared scopes.
- Existing magnetic assertion-dependent entry intentionally rejects -O before creating its requested JSON output. These were expected exit-1 controls, not optimized-mode numerical passes.
- Assertion-entry AST policy, changed-source syntax compilation, and scoped whitespace checks passed.

execution_receipt.json records 20 final focused executions; supplementary_receipt.json records 13 checks, including the two expected optimized-entry rejections. There were zero unexpected exits. Source pins were verified current after those runs. This is focused coverage only: no claim of a full repository suite, full CMake build, Lean build, manuscript build, all parameter values, or asymptotic validity is made here.

## Final SHA256 source pins

- computations/python/bgs/magnetic_quotient.py: a1ac5f2b025a20141ade087f5c31b2973ac3a8dd70ba3f03506e23c582bdf7dc
- computations/python/bgs/twisted_jacobi.py: 4f48218acc5c2fab9d6689e553d3dd1e8ce9f815ae00943c4fd08b825f146b04
- computations/python/bgs/jacobi.py: 5179856965d5bceff13d3e48b3d57400e485f04cfea1d264be685015835bd851
- computations/python/bgs/finite_field.py: 74e185cc2290058e746f91903775db389f777685b7057b7d75978f309fd22c2e
- computations/maintenance/tests/test_twisted_magnetic_integer_contracts.py: fb35751966faba4c3e50854caa4655f9a4be343f3c6053c536139c801499b7b0

## Reproduction

From the isolated checkout, run:

- python3 /workspace/shared/bgs_r6_arithmetic_repair/run_checks.py
- python3 /workspace/shared/bgs_r6_arithmetic_repair/run_supplementary.py
- python3 /workspace/shared/bgs_r6_arithmetic_repair/run_coverage.py
- python3.12 /workspace/shared/bgs_r6_arithmetic_repair/after_probe.py (repeat with -O and python3.13)

The C++ binary is built with g++ -std=c++20 -O2 computations/cpp/magnetic_word_verifier.cpp -o /workspace/shared/bgs_r6_arithmetic_repair/magnetic_word_verifier. Output files live outside the checkout; recorded reference evidence is untouched.
