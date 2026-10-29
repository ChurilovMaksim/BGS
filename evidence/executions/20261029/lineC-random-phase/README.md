# Line C certificate: BGS-TRACE-143 to BGS-TRACE-148

The packet numbered these statements BGS-TRACE-138 to BGS-TRACE-143. Main already registers BGS-TRACE-140 to BGS-TRACE-142, so the registered IDs are BGS-TRACE-143 to BGS-TRACE-148.

This certificate checks `mathematics/fixed-map/random_phase_encounter_pairs.md` for the **maximal Haar diagonal-phase ensemble** U = D_θ·M_N, S = [[3,4],[2,3]]. It does not cover the fixed kick, the 16-mode ensemble or band-limited ensembles. A pass proves neither BGS-TRACE-005 nor BGS-BGS-001. Gnutzmann–Seif 2004 derived 2τ−2τ² diagrammatically for this ensemble; new here is only the rigorous fixed-m exact-in-p result, the complete classification including swaps, and the m≤12 expansions.

```sh
cd computations/verification/lineC
python3 fixes_check.py                  # ~5 s, prints PASS (39/39): constants C_m, m=1,2,3 exact values,
                                        #   square-class flip, c1/c2 table vs COE, brute-force anchor m=7 p=7
python3 verify_thm1.py                  # Theorem 1 matrix identities and eigenphases (floating point)
python3 verify_exact.py                 # V1 brute force vs Prop. 2; V2 symbolic vs per-prime (floating point)
python3 threshold_check.py 7 3 257 6    # exact comparison prime by prime (m<=7: ~20 s; m=8: ~65 s per prime)
python3 rank_dist.py                    # Lemma 4 exhaustive check, m=4..9
g++ -O2 -std=c++17 -pthread -o engine engine.cpp && python3 run_engine.py 8 8   # Theorem 7 expansion, m=8
python3 run_engine.py 12 8 2            # m=12 through p^-5/2 (~4 min on 8 threads)
```

Lean, toolchain `leanprover/lean4:v4.33.1`:

```sh
lean formalization/Bgs/LineCEncounter.lean            # no imports; every theorem by decide
cd formalization && lake exe cache get && lake build Bgs.LineCEncounter && lake env lean AxiomsLineC.lean
```

Logs in this directory:
* `fixes_check.log` and `threshold_m{2..8}.log` are the v2 checks, all exact in Q(eps*sqrt p) except the floating-point brute-force anchors.
* `verify_thm1.log`, `verify_exact.log`, `rank_dist.log`, `decompose_5_7.log`, `audit_fractions.log`, `exact_m8_p101_103.log` and `coe_check.log` are the v1 checks.
* `symbolic_m1_7.log`, `symbolic_m8.log`, `engine_m8.log`, `engine_m11_def2.log`, `engine_m12_def2.log` and `coeff_table.md` hold the Theorem 7 data. The full set of engine logs is in `computations/verification/lineC/data/`.
* `fix_cache_get.log` (`lake exe cache get`), `fix_lake_build_LineC.log` (`lake build Bgs.LineCEncounter`, exit 0, 254 s), `fix_lean_axioms_LineC.log` (propext or no axioms) and `fix_lean_controls.log` (seven false variants, all rejected; script `lean_controls.sh`) are the v2 Lean logs. `lean_axioms_LineC.log`, `lean_controls.log` and `own_lake_build_LineC.log` are the v1 logs.
* `lit_check.md` and `tanner2001_p10_sigma_3over4.png` are the literature notes and the page crop showing Tanner's σ(N) ≈ (3/4)N^{−4/3}.

Independent replay: the referee's from-scratch engine is deposited at `computations/verification/lineC/independent_replay/`, and its logs are `independent_replay/` in this directory. `independent_replay/compare_theirs.log` records that every Theorem 7 coefficient for m = 3..12 agrees at 171 primes. BGS-TRACE-147 stays verification-pending. Promotion is a separate status decision, as for BGS-RES-022.
