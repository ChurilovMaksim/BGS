## 5. Pre-registered m = 17 test

(PREDICTIONS_m17.json, sha256 in PREDICTIONS_m17.sha256, written before any m = 17 class sum existed.)
Registered tests (k1, η = 2): primaries ±4, ±8 to 1e-5 (law), ±2, ±8/3 to 1e-3; d = 103 dilution mean 9.33e4 ∈ [7.5e4, 1.17e5];
second tier (±22,96) ≈ 3.3e4, (±2,12) ≈ 1.4e4 (×1.6); bulk F/2m (H = 8 definition) 2.04 ∈ [1.95, 2.15] ⇔ W′/m ∈ [−0.10, 0.30];
total F/2m 39.1 ∈ [38.7, 39.5]. Full kick: Line E's registered ±196 values (TRACE-196), ±392 ≈ 2.0e6 (×1.5), ±98 ≈ 3e5 (×2),
d = 103 dilution of ±196 ≈ 6e4 ∈ [4e4, 9e4], bulk 2.03 ∈ [1.95, 2.15].

**Outcome, k1 kick (η = 2): ALL 15 REGISTERED TESTS PASS.** Predictions file sha256 `fa8505f5…8aa344` verified unchanged
(matches PREDICTIONS_m17.sha256; file mtime 13:17, before the m = 17 class sums finished). Class-sum file `logs/Torb_k1_m17.bin`
sha256 `a5edff4a…f38206`, 152 007 280 321 canonical orbits, 0 period-check failures, 12 234 s. Evaluator: `code/eval17.py`,
output `logs/eval17_k1.log/.json`, `logs/formula_table_k1_17.json`. h = 1 607 521, φ = 1 591 812.

| test | observed | registered band | |
|---|---|---|---|
| primary +4 | 9.8930e8 | [9.8929e8, 9.8931e8] | PASS |
| primary −4 | 9.89294e8 | [9.89284e8, 9.89304e8] | PASS |
| primary +8 | 3.0176e6 | [3.01757e6, 3.01763e6] | PASS |
| primary −8 | 3.01686e6 | [3.01683e6, 3.01689e6] | PASS |
| primary +2 | 438 089 | [437 592, 438 468] | PASS |
| primary −2 | 441 445 | [440 939, 441 821] | PASS |
| primary +16/6 (ν = 3/8) | 89 562.4 | [89 457.5, 89 636.5] | PASS |
| primary −16/6 | 84 726.2 | [84 626.3, 84 795.7] | PASS |
| d = 103 dilution mean | 93 368.7 | [75 000, 117 000] | PASS |
| second tier (22, 96) | 33 281.3 | [20 625, 52 800] | PASS |
| second tier (−22, 96) | 33 687.8 | [20 625, 52 800] | PASS |
| second tier (2, 12) | 14 951.2 | [8 750, 22 400] | PASS |
| second tier (−2, 12) | 15 003.7 | [8 750, 22 400] | PASS |
| **bulk F/2m (H = 8)** | **2.02487** (W′/m = +0.050; 0.054 % of residues removed) | [1.95, 2.15] | **PASS** |
| total F/2m | 39.0651 | [38.7, 39.5] | PASS |

Robustness of the bulk value to the cut: H = 16 → 2.0239, H = 32 → 2.0209, H = 64 → 2.0185 (W′/m 0.048 / 0.042 / 0.037).
Explicit formula (Conjecture R′): predicted resonant part 37.0184·2m vs actual 37.0191·2m; RMT part 1.99999·2m;
W′/m predicted 0.0933 vs actual 0.0918; 408 resonant residues. The bulk trend m = 15 → 17 (2.0704 → 2.0249) moves toward the RMT
value 2, consistent with R′ (bulk = RMT + o(m)) while the total F/2m keeps growing exponentially via the primaries.

**Outcome, full kick: all registered tests PASS** (`logs/eval17_full.log`, finished 01:46 Oct 31 box clock; predictions sha256 fa8505f5…aa344;
Torb_full_m17.bin sha256 86439dfe…aa5be). h = 1607521, φ = 1591812, total F/2m = 25.7986. Dominant residues (2,392): |Z|² = 7.0474e8 and
(−2,392): 5.6655e8, matching Line E's registered values 7.048e8 / 5.666e8 (and Line E's independent certified enclosure, F/2m ≥ 23.489).
Primaries (2,784) 2.029e6, (−2,784) 1.525e6 ∈ [1.33e6, 3e6] PASS; (2,196) 3.236e5, (−2,196) 2.635e5 ∈ [1.5e5, 6e5] PASS; d103 dilution
mean 6.01e4 ∈ [4e4, 9e4] PASS; bulk F/2m (H = 8) = 2.0054 ∈ [1.95, 2.15] PASS (removed 0.105%; H = 16/32/64 → 2.0054/2.0054/2.0051).
Explicit formula (R′): resonant part predicted 23.7788·2m vs actual 23.7799·2m; RMT part 2.0000·2m; W′/m predicted 0.0396 vs actual 0.0374;
408 resonant residues.

---------------------------------------------------------------------------------------------------------------------------------

