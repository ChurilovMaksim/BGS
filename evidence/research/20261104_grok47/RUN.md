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
