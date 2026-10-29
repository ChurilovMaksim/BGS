# Independent replay (referee audit of Line B phases 2–4)

These files are the independent referee's from-scratch scripts and logs, taken from the referee workspace (`/workspace/audit/derand23/code`, `/workspace/audit/derand23/logs`, `/workspace/audit/derand23/REPORT.md`). They were not written by the Line B author and share no code with `../phase*`. `REFEREE_AUDIT_REPORT.md` is the audit itself (§1–§7: phases 2+3; §8: phase 4; §8.10: status table and required non-claims) and is verbatim. The scripts differ from that workspace in two places required by the repository: each `sys.path` entry and `CERTDIR` is repo-relative, and each Python file carries the assertion-entry guard.

| script | replays | log(s) |
|---|---|---|
| `a1_ecpp_verify.py` | own pure-Python Atkin–Morain/Goldwasser–Kilian checker of the 7 ECPP certificates + PARI `primecertisvalid` + recomputation of h_m; two rejected controls | `a1_ecpp_verify.log` |
| `core.py` | shared model (q-sequence group Fix(T^m), symbol, norm classes) | — |
| `t1_structure.py` | Lemma S + Addendum, Prop R/K, Theorem D (m = 3..9) | `t1_structure*.log` |
| `t2_fixed_eta.py` | fixed-η second moment, Theorem W split, W̃^rest tables (m ≤ 11) | `t2_fixed_eta_*.log` |
| `t3_transfer.py` | Theorem T (χ_m = Σ(−1)^a Tr M_a^m), μ(η) spectrum | `t3_transfer.log` |
| `t4_thmN.py` | Theorem N hypotheses and bound | `t4_thmN.log` |
| `t5_s0.py`, `t6_kloosterman.py`, `t7_thmG.py`, `t8_nd2.py` | s0/κ table, Kloosterman-type sums, Theorem G, ND^(2) | matching logs |
| `t9_cert.py` | independent directed-rounding re-certification of Theorem D_cert intervals (6 of 93 done: [1,1.1], [2.6324,3.3853], [10.2198,11.0104], [30,30.5], [50.5,51.2], [81.2445,81.5741]; all valid) | `t9_cert_*.log` | *Second-reader update (2026-10-29): all 93/93 intervals now re-certified with this script (unmodified) — see `../second_reader/`.*
| `t10_lemmaV.py` | Lemma V brute force m ≤ 61 + norm inequality | `t10_lemmaV.log` |
| `t11_propL.py` | Prop L: E X² = mσ², χ_m ≥ 1 − ½mσ²η² (m = 3..11) | `t11_propL.log` |
| `t12_torsion.py` | torsion split at m = 11 | `t12_torsion.log` |
| Lean logs | build/axiom logs of the referee's own Lean replay of the phase 1–4 checks | `lean_*.log`, `cache_get*.log` |

**Paths.** The referee workspace hard-coded `sys.path.insert(0,'/workspace/audit/derand23/code')` and, in `a1_ecpp_verify.py`, `CERTDIR='/workspace/bgs-derand/phase3/logs'`. In this tree those strings are the script directory and `computations/verification/lineB/ecpp`. Replay from `code/`:

```
cd computations/verification/lineB/independent_replay/code
python3 a1_ecpp_verify.py 59,163,257,421,937,947,1493
python3 t10_lemmaV.py; python3 t11_propL.py; python3 t12_torsion.py
B=0.0176777; K=0.0088388      # beta=0.1/(4 sqrt2), kappa=beta/2 in the referee's normalisation
python3 t9_cert.py 1.0 1.1 $B $K 45.2548 25     # see REFEREE_AUDIT_REPORT.md §7 and §8.11 for all commands
```

Requirements: Python 3 with numpy, scipy, sympy, mpmath, gmpy2, cypari2, python-flint (arb). The referee's own logs cover 6 of the 93 intervals. The full directed-rounding rerun was done afterwards by the second reader with this `t9_cert.py`; see `../second_reader/`.
