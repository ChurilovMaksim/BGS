# Commands

Working directory `/workspace`. Python 3.12. Interpreter packages used: `mpmath` 1.4.1, `python-flint` 0.9.0. No registry file, README, or hash-pinned source was modified. `tail_kp.py` was not re-run; its input paths under `/workspace/bgs-lineN` are not in this checkout.

```text
python3 evidence/research/20261104_grok47/code/span_audit.py 14
python3 evidence/research/20261104_grok47/code/bad_defect.py
python3 evidence/research/20261104_grok47/code/propk_sharp.py
python3 evidence/research/20261104_grok47/code/crossover_sharp.py \
  3.4962e-4 5.0313e-6 7.4115e-6 7.1863e-6 \
  3.490213e-4 3.2911833e-4 3.362054e-4 1.16811e-4 1.14748e-4
```

Shells j ∈ {12, 13, 14} were compared with `digits.eps_digits` by an inline driver (17880 classes, 0 mismatches, 20.61 s, `mp.dps = 60`, `KK = 12`, `tol = 1e-7`). The summary is `logs/word_match_j12_14.json`. Shells j ≤ 11 are the `mp_match` field of `logs/span_audit.json` (2554/2554).

Outcomes used in the notes:

- `span_audit.py 14`: 20434 classes, 0 support violations, 0 endpoint failures, defect enclosures from 1.00033740024809 to 2.99966264991176, 17.784 s.
- `bad_defect.py`: at g₀ = 4, 17255 classes with internal run < 4, defect from 1.01148986427082 to 2.96087221277804.
- `propk_sharp.py`: KP fixed points in `logs/propk_sharp.json`. At C = 0.082 the sharp-span activity is S₀ ≤ 3.24088·10⁻⁴.
- `crossover_sharp.py`: published δ = 3.4962·10⁻⁴ returns prime 3307; sharp-span δ = 3.2911833·10⁻⁴ returns prime 3067; both robust inputs 7.4115·10⁻⁶ and 7.1863·10⁻⁶ return 1409. Every row has an empty violation list through 5000 and `mono_ok` true.

SHA-256 hashes of the code, logs, and notes are in `HASHES.txt`, computed after the runs. `span_audit.py` received a comment clarification in `eps_pow` after the J = 14 run; the arithmetic is unchanged, and the log was not regenerated.

Second target, H7* and H8:

```text
python3 evidence/research/20261104_grok47/code/h7h8.py
```

Outcome: `logs/h7h8.json`. Delivered exponent \(c_{\mathrm{del}}\) has centre \(0.73753151868331175037\), and \(\tfrac32 c_{\mathrm{del}} > 1\). The θ-gap at \(\ell_0 = p/4\) is nonempty (\(0.26224 > 0.16662\)). Trial-proved factorisations of \(K_p\) for primes \(5 \le p \le 31\), including the 17-digit factor at \(p = 23\). Elementary asserts for the Lemma E excess pass, and the arb excess check passes for every prime \(p\) with \(5 \le p \le 79\). Runtime about 6 s, of which the trial division of \(57887325592525441\) is the long step. No registry file was read for writing.

Third target, H7* rates on the included conductors. Interpreter packages: the same flint and mpmath, plus `scipy` 1.18.1 for the power-of-two balancing scales. No registry file was written.

```text
python3 evidence/research/20261104_grok47/code/h7_rates.py self-test
python3 evidence/research/20261104_grok47/code/h7_rates.py survey
python3 evidence/research/20261104_grok47/code/h7_rates.py certify --d 31 --sectors 0,2,4,6 --squares 2 --out evidence/research/20261104_grok47/logs/parts/d31.json
python3 evidence/research/20261104_grok47/code/h7_rates.py certify --d 49 --sectors 0,4 --squares 2 --out evidence/research/20261104_grok47/logs/parts/d49.json
python3 evidence/research/20261104_grok47/code/h7_rates.py certify --d 217 --bx0 0 --bx1 109 --sectors 0,4 --squares 2 --out evidence/research/20261104_grok47/logs/parts/d217_0_109.json
python3 evidence/research/20261104_grok47/code/h7_rates.py certify --d 217 --bx0 109 --bx1 217 --sectors 0,4 --squares 2 --out evidence/research/20261104_grok47/logs/parts/d217_109_217.json
python3 evidence/research/20261104_grok47/code/h7_rates.py wide
python3 evidence/research/20261104_grok47/code/h7_rates.py rays
python3 evidence/research/20261104_grok47/code/h7_rates.py rays-ext
python3 evidence/research/20261104_grok47/code/h7_rates.py rays-deep
```

Outcomes used in `proofs/h7_rates.md`:

- `self-test`: level-7 model rates sit in the TRACE-223 discs, the phase identity holds on the three checked pairs, and the orders of \(31\), \(49\) and \(217\) are \(15\), \(21\) and \(15\).
- `d31.json`: \(960\) classes, all four sectors, cap \(1.0923934786042258 < 1.42785\), precision \(128\), \(221\) s.
- `d49.json`: \(2400\) classes, sectors \(0\) and \(4\), cap \(1.2876123688383678 < 1.42785\), precision \(160\), \(790\) s.
- the two `d217` slices: \(23652+23436 = 47088\) classes, sectors \(0\) and \(4\), cap \(1.2892227802420704 < 1.42785\), precision \(128\), about \(3000\) s each.
- Three surviving orbits lie above \(T'\), enclosed by `enclose`: \(d = 3437426497\), \(\beta = (-208,0)\), rate \(1.4587724665845072\); \(d = 24061985479\), \(\beta = (227,227)\), rate \(1.5119805994002586\); \(d = 2735635252619983\), \(\beta = (-89,0)\), rate \(1.4686852970394264\).
- The closest searched orbit that stays under is \(d = 390805036088569\), \(\beta = (0,-321)\), Newton value \(1.4060636053128053\), cap \(1.4061888484607947\).

The `certify-probes` log is a width-\(8\) enclosure of short vectors. Several of those orbits are not the maximizers later found on longer rays. The crossings are the `enclose` files named in `logs/parts/`.

Fourth target, the multi-disc finite section. Same interpreter. `scipy` is used only by the Newton balancer inside `h7_rates.py`.

```text
python3 evidence/research/20261104_grok47/code/h7_multidisc_cert.py enclose
```

Outcome: `logs/h7_multidisc_enclose.json`, precision \(320\). The section is centres \(|c|\le 3\), \(40\) modes, letters \(|n|\le 16\), dimension \(280\). Newton lower endpoints: level \(7\), class \((2,1)\), \(1.2835951329030868\); class \((1,3)\), \(1.2837142953109737\); \(d = 3437426497\), \(1.458772466390154\); \(d = 24061985479\), \(1.5119805975188876\); \(d = 2735635252619983\), \(1.4686852948918232\). Every Kantorovich \(h\) is below \(2\cdot 10^{-14}\). The one-step tail in the same log is \(< 9.646772214969684\cdot 10^{-5}\), with no core exit. The edge float, not a certificate, is `logs/h7_multidisc_edge.json`.

`h7_multidisc.py calibrate` and `orbits` are the float scans that preceded the enclosure. Their logs are `logs/h7_multidisc_calibrate.json` and `logs/h7_multidisc_orbits.json`. They are not the certificate.

Fifth target, the aggregate section sum. Same interpreter, precision \(320\) for every ball. No registry file was written.

```text
python3 evidence/research/20261104_grok47/code/h7_lin_sum.py validate
python3 evidence/research/20261104_grok47/code/h7_lin_cert.py check
python3 evidence/research/20261104_grok47/code/h7_lin_cert.py kappa
python3 evidence/research/20261104_grok47/code/h7_lin_cert.py cross
python3 evidence/research/20261104_grok47/code/h7_lin_cert.py iso 0
python3 evidence/research/20261104_grok47/code/h7_lin_cert.py iso 4
python3 evidence/research/20261104_grok47/code/h7_lin_cert.py sum-iso
```

Outcomes:

- `validate`: at \(q=41\), \(m=15\), truncation \(K=20\), the float \(\beta\)-sum and the Gauss-kernel grid differ by \(1.329\cdot 10^{-10}\). Log `logs/h7_lin_validate.json`. This is not a certificate.
- `check`: at \(m=15\), \(d=287\), \(195\) members, \(42\) arguments, the product formula and the member sum differ by \(8.556\cdot 10^{-14}\). Log `logs/h7_lin_kappa_check.json`.
- `kappa` and `cross`: `logs/h7_lin_traces.json`. Ten traces. Untwisted sector \(0\): \(1.2295228772115986\cdot 10^{16}\) at period \(57\), \(3.614257095031031\cdot 10^{24}\) at period \(87\). Crossing sector \(0\): \(2224799020.4343753\), \(17144879331.749458\), \(333273628480233.94\). Every sector-\(4\) trace in that file is below \(10^{-12}\). One-step Frobenius majorant \(50.490459330663754\).
- `iso 0` and `iso 4`: sixteen orbits each, `logs/h7_lin_iso_s0.json` and `logs/h7_lin_iso_s4.json`. `sum-iso` gives \(|S_{\mathrm{iso}}|=7.8450076177326356\) and \(39.619988072063016\), log `logs/h7_lin_iso_sum.json`.

The composite sums over all \(\beta\) were not run. A column-sequential trace at \(q=457\) was timed and not started.

Sixth target, a uniform bound on the section trace. Same interpreter, precision \(160\) for the norm certificate and the residue weight. No registry file was written.

```text
python3 evidence/research/20261104_grok47/code/h7_uniform.py all
```

Outcome: `logs/h7_uniform.json` and `logs/h7_uniform_weights.json`, \(805\) s for the norm certificate. The self-test passes a \(2\times 2\) Cholesky certificate, rejects a cap below the true norm, and matches the cosine sum at \(q=5,17,41\). The mass check at \(d=287\) has relative discrepancy \(<6.71\cdot 10^{-14}\). The frozen diagonal has floating-point max \(2\)-norm \(2.439371\) on a \(361\)-point grid; a geometric weight \((1/2)^k(0.45)^{|c|}\) has floating-point max about \(2.6485\). The certificate covers the circle by \(233\) intervals, Taylor remainder upper endpoint \(0.005953146641677557\), and accepts \(R=246/100\) on all \(466\) endpoints. The smallest Cholesky slack has lower endpoint \(0.016316926498566642\). Newton on the untwisted step encloses one eigenvalue in \([1.9154732041332492,\ 1.915473204133273]\). The residue weight, the majorant, and \(R_*\) are the balls in `proofs/h7_uniform.md` §4.

Seventh target, the averaged operator. Same interpreter. Ball arithmetic at precision \(200\) for the readout norm and the constant piece. The prime-\(457\) orbit pass is binary64. No registry file was written.

```text
python3 evidence/research/20261104_grok47/code/h7_average.py check
python3 evidence/research/20261104_grok47/code/h7_average.py majorant
python3 evidence/research/20261104_grok47/code/h7_average.py all
python3 evidence/research/20261104_grok47/code/h7_avg_orbit.py 457 57 0
python3 evidence/research/20261104_grok47/code/h7_average.py orbit
```

Outcomes, all in `logs/h7_average.json` unless noted:

- `check`: at \(q=17\), \(t_b=3\), the closed form of \(\Gamma_q\) matches the direct sum to \(1.7955268718282194\cdot 10^{-13}\) on every norm class. The scalar word pairing at period \(8\) matches the direct sum to \(2.153132083222681\cdot 10^{-13}\).
- `all`: the same checks, then the scalar factorisation at \(17\cdot 41\). The ratio \(S(697)/(S(17)S(41))\) has modulus \(6.05155913001261\). The majorant pass encloses \(\|\Gamma_{457}\|_2\), \(\|\Gamma_{7521721}\|_2\), the Cauchy–Schwarz majorant \(7.420040412990621\cdot 10^{48}\), and the constant piece \(d\lvert\operatorname{Tr} Q_0\rvert\). The threshold exceeds that piece by \(91.71481675130566\).
- `h7_avg_orbit.py 457 57 0`: \(722.51\) s, \(3665\) orbits, \(457^2\) classes. Logs `logs/h7_avg_orbit_q457_a0.json` and `logs/h7_avg_orbit_q457_a0_full.json`. Binary64. The stored Frobenius column reaches \(6.087378898382624\cdot 10^{47}\) and is not an enclosure.
- `orbit`: the twisted remainder has modulus \(64.36874328884288\). The nonzero isotropic sub-sum differs from the certified value \(7.8450076177326356\) by \(2.842170943040401\cdot 10^{-14}\). The trace room \(T/\sum\lvert\kappa\rvert\) is \(30788816.98609009\).

Eighth target, the additive energy of \(\langle\lambda\rangle\). Same interpreter, ball arithmetic at precision \(200\). The factorisations are read from `logs/h7h8.json` and are not recomputed. No registry file was written.

```text
python3 evidence/research/20261104_grok47/code/h8_energy.py
```

Outcome: `logs/h8_energy.json`. Exact energy \(2L^2-L\) at the split primes \(7, 31, 41, 457\), and \(3L^2-3L\) at \(73, 89\). The composite \(217\) has energy \(435\), equal to the cap from its factor \(31\). The prime powers \(49\) and \(343\) have energies \(1617\) and \(122451\), above \(2L^2-L\); \(31^2\) keeps order \(15\) and energy \(435\). On the stored factors of \(K_p\) for \(5 \le p \le 31\), every prime is \(1\) or \(7 \pmod 8\), and the order is \(3\) at \(7\) and \(3p\) otherwise. The \(c = 1\) threshold stays under \(0.16661156569722353507\). At \(L = 3p\) the \((2,2)\) meeting point is under \(0.00644413\) for \(p = 1409\) and under \(0.00303834\) for \(p = 3307\). Runtime under a second.
