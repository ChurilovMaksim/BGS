# Line B execution evidence (29 October 2026)

This directory backs `mathematics/fixed-map/derandomized_fixed_kick.md`.

**Scope.** The fixed diagonal kick \(K_\eta M_N\) of the repository kernel, with \(S=[[3,4],[2,3]]\), at fixed \(m\) (below the Ehrenfest time). On main at 502af245 the highest registered TRACE id was BGS-TRACE-162, so BGS-TRACE-163 was the next free id. The block BGS-TRACE-163 through BGS-TRACE-182 was not renumbered.

## Non-claims (verbatim, referee audit §8.10)

1. Nothing is proved at τ = m/N = O(1). All results are fixed-m (diagonal / below Ehrenfest). This is not progress on BGS-BGS-001 or BGS-TRACE-148.
2. "B_m → 2m" is not claimed. Theorem N covers a finite list of certified NSW primes, and the infinitude of NSW primes is open.
3. The parity crossover is the derandomized analogue of the known BGOS/Pandey–Mehta symmetry-breaking crossover. It is not a Keating–Mezzadri pseudo-symmetry, and the phenomenon is not new.
4. The certified decay bound is vacuous below m⁺(η) (10²–10⁵). It says nothing at the numerically accessible m.
5. Conjecture R is not reduced to any known conjecture or large-sieve inequality. The "quadratic large sieve" phrasing is withdrawn. KR/Bourgain/BGK do not apply (minimal period ord_h λ = m).
6. The fixed-η CLT is numerical only (m ≤ 11); the KS yardstick is heuristic.
7. The (m, η) = (11, 2) outlier is unexplained; the torsion attribution is withdrawn.
8. The Theorem D_cert arithmetic is IEEE float with an a-priori error bound (plus arb coefficients), not full interval arithmetic, until the full directed-rounding rerun.

*Second-reader note (2026-10-29):* the full directed-rounding rerun has now been done (93/93, claim-173). Non-claim 8 still applies to the authors' float grid and its constants; TRACE-173 is proved with the directed-rounding constants only.

## Research-box logs (deposited with the packet; not re-executed in this integration)

`lake_cache_get.log`, `lake_build_LineB.log`, `lake_build_Bgs.log`, `lean_axioms_LineB.log` and `lean_controls.log` are the packet's isolated build on a copy of main `d6fa6e2a`. Mathlib came from the cache. Those logs are not the build of this checkout.

## Integration build (this checkout, Lean 4.33.1)

`integration_lake_build_Bgs.log` is `lake exe cache get` followed by a full `lake build Bgs` on this tree, with the four Line B imports wired after `import Bgs.LineDCerts`.

* Cache: exit 0. The log downloads and decompresses 8690 cached files, then reports "Already decompressed 8690 file(s)". The Mathlib package oleans came from that cache. Mathlib was not built from source. The in-repo modules under `formalization/Bgs/Mathlib/` are part of `Bgs` and were compiled against those oleans. The packet's isolated log reported 8689 cached files.
* The first build line in that log is `build_exit:127` because `/usr/bin/time` was not installed. No `lake build` had started. The retry in the same log is `lake build Bgs`: exit 0, "Build completed successfully (8800 jobs)", elapsed 251 s. `Built Bgs.LineBDerand (1.3s)`, `Built Bgs.LineBPhase2 (13s)`, `Built Bgs.LineBPhase3 (3.2s)`, `Built Bgs.LineBPhase4 (10s)`.
* `integration_axioms.log` (`lake env lean` on `AxiomsLineB.lean`, exit 0). 53 theorems: 36 use no axioms, 8 use [propext], 1 uses [propext, Quot.sound], 8 use [propext, Classical.choice, Quot.sound]. No sorryAx and no ofReduceBool.
* `integration_grep.log`: the four matches of `sorry` or `native_decide` are comments. There is no `sorry` and no `native_decide` in the new modules.
* `integration_controls.log`: 6/6 false controls rejected.
* `integration_checkers.log` records the repository checkers. Exit 0: scientific registry audit (266 claims), repository audit, text-control audit, wave3 integration audit, the five render `--check` scripts, manuscript reference audit, the three section-sync `--check` scripts (finite-orbit and fixed-map SKIP; return sections with pandoc 3.12.1), wave3 source closure, and `compileall`. Exit 1, already on main `502af245`: bibliographic self-test (the EXT-BR-1975 impact list omits BGS-TRACE-116; no Line B id is in that closure), `wave2_portable_replay.py --check-sources` (sealed digest of `mathematics/position_chain_mixing.md`), and `wave2_integration_audit.py` (BGS-TRACE-025 wrapper digest; that file was not edited). GitHub Actions was not executed. `pdflatex` is not installed, so `manuscript/BGS_unified.pdf` was not rebuilt.

## Commands

Python 3 with numpy, scipy, mpmath, python-flint and cypari2 is required. Run each script from its own directory.

```sh
V=computations/verification/lineB
(cd $V/ecpp   && python3 verify_ecpp.py)                 # TRACE-168 primality: 7 ECPP + 4 APRCL, controls; prints PASS (~5 s)
(cd $V/phase1 && python3 verify_thm1.py && python3 verify_exact.py && python3 t_rad.py)   # TRACE-163
(cd $V/phase2 && python3 deficit_odd.py && python3 kernel_ramanujan.py && python3 nsw_admissible.py)  # TRACE-165/167/168
(cd $V/phase3 && python3 W_decomp.py 3,5,7,9 0.5,1,2,5,10,25,50,100,400)                       # TRACE-169/170
(cd $V/phase4 && python3 lemmaV.py && python3 lowercheck.py)                              # TRACE-171
(cd $V/phase4 && python3 certify_v2.py)                   # G1/G2 envelope self-test at eta = 1, 50, 81
(cd $V/phase4 && OMP_NUM_THREADS=3 python3 rerun_grid.py 0 2 & OMP_NUM_THREADS=3 python3 rerun_grid.py 1 2; wait; python3 summarize_v2.py)
                                                          # TRACE-173: full 93-interval re-certification; ~5 GB RAM per worker at eta >= 50
```

To regenerate rather than replay the certificate, delete `logs/grid_v2_w*.jsonl` first; `rerun_grid.py` is resumable and skips intervals already logged. It reads the interval list from `logs/grid_s*.jsonl`, the original adaptive grid made by `grid.py`.

The independent replay is in `computations/verification/lineB/independent_replay/` (the referee's own code; see its README).

## Lean

Toolchain `leanprover/lean4:v4.33.1`. Run in a project with the Mathlib cache:

```sh
cd formalization && lake exe cache get && lake build Bgs.LineBDerand Bgs.LineBPhase2 Bgs.LineBPhase3 Bgs.LineBPhase4
lake build      # full Bgs target with the four imports wired into Bgs.lean
lake env lean <this dir>/AxiomsLineB.lean
bash <this dir>/controls/lean_controls.sh <this dir>/controls   # 6 false variants, all must be rejected
```

## Logs in this directory

| file | content |
|---|---|
| `lake_cache_get.log`, `lake_build_LineB.log`, `lake_build_Bgs.log` | isolated copy of main d6fa6e2a `formalization/` + the packet: cache get exit 0; the four modules exit 0; full `lake build` (Bgs, 8799 jobs) exit 0. Mathlib came from the cache, not built from source |
| `AxiomsLineB.lean`, `lean_axioms_LineB.log` | `#print axioms` for all 53 theorems. Results: 36 use no axioms, 8 use [propext], 1 uses [propext, Quot.sound], 8 use [propext, Classical.choice, Quot.sound] (Mathlib `norm_num`/`ring`). No sorryAx, no ofReduceBool. |
| `controls/`, `lean_controls.log` | 6/6 false controls rejected (`decide` reports each proposition false) |
| `verify_ecpp.log` | PASS |
| `grid_v2_summary.json`, `grid_v2_summary.txt`, `grid_v2_w0.jsonl`, `grid_v2_w1.jsonl` | the TRACE-173 rerun with the G1/G2-fixed envelopes: all 93/93 intervals re-certified (same float method; status unchanged) |
| `packet_smoke.log` | relocated scripts run from the packet tree (W_decomp m = 5, deficit_odd, certify_v2 self-test) |
| `receipt.json` | sha256 of the packet tarball and of the integrated files, from `git show HEAD:path`. The receipt does not hash itself. |
| `integration_lake_build_Bgs.log`, `integration_axioms.log`, `integration_grep.log`, `integration_checkers.log` | this checkout |
| `receipt_hash_recompute_20261029.log` | recomputation of those hashes from committed blobs. The receipt does not hash this log. |

## Certificate hypotheses (TRACE-173)
- IEEE-754 binary64 arithmetic with an a-priori summation bound, absorbed by SAFE = 1 + 10⁻⁹.
- glibc libm exp/log accurate to ≤ 4 ulp.
- arb (python-flint, 128-bit) enclosures of the Bessel-product coefficients, with the G1 tilted truncation tail.

This float grid is **not** full interval arithmetic. *Second-reader update (2026-10-29):* an independent directed-rounding rerun (referee t9_cert.py, unmodified) now covers all 93/93 intervals, all valid, contiguous on [1, 81.57406988332305], max ρ' = 0.999820, max C' = 1.43e+07; logs in `computations/verification/lineB/second_reader/logs/b1/`. TRACE-173 is proved with those directed-rounding constants (hypotheses: IEEE binary64 RN, arb, libm exp to 10⁻⁶ relative in the drop term only). The float-grid constants above remain uncertified by directed rounding.
