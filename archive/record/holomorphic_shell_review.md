# Holomorphic shell and spectral-resolution review

Base: `ddf467af8c304f3d673b2cb5f5396969ae3d55cf`.
Date: 6 September 2026.

## Scope and corrections

The complete contact, sharpness, punctured-domain, quantitative instability
and spectral negative-control proofs were checked in this pass. The finite
checks below were executed again, rather than inherited from previous logs.
This is not a new line-by-line audit of every older research file.

The scalar two-circle uniqueness statement was matched to Perez's Theorem 2.2
and attributed explicitly. The vector-valued contact proof uses holomorphy at
the common centre; theta examples show why that domain condition cannot be
silently deleted. Repeated conditions count actual normal multiplicities, not
duplicate measurements of a value. The exact recovery statement supplies no
noise estimate. A separate rational-coefficient construction disproves every
uniform Holder intensity bound on the bounded analytic class specified in the
article. No matching upper modulus has been proved.

The unitary clock comparison concerns spectra themselves, but does not
construct chaotic quantizations. Spectral rounding preserves only the stated
weak Egorov hypotheses, not an unproved smooth microlocal symbol class. These
are safeguards for the BGS research route, not a positive universality proof.

## Executed checks

```sh
python computations/verification/extremal_resonance.py \
  --cases 100 --max-lag 10 --algebra-cases 12 \
  --output build/recheck/extremal.json --replay build/recheck/extremal.txt
c++ -std=c++20 -O2 -Wall -Wextra -Wpedantic \
  computations/cpp/extremal_resonance_replay.cpp -o build/recheck/extremal_replay
build/recheck/extremal_replay build/recheck/extremal.txt
build/recheck/extremal_replay
python computations/verification/holomorphic_shell_rigidity.py \
  --cases 120 --seed 20260906 --output build/recheck/shell-1.json
python computations/verification/holomorphic_shell_rigidity.py \
  --cases 180 --seed 20260907 --output build/recheck/shell-2.json
python computations/verification/shell_instability.py \
  --max-M 24 --output build/recheck/instability-1.json
python computations/verification/shell_instability.py \
  --max-M 40 --output build/recheck/instability-2.json
python computations/verification/spectral_resolution.py \
  --max-M 12 --output build/recheck/resolution.json
```

Create `build/recheck` before these commands. All returned PASS. The old
extremal sources used here have the same Git blob hashes as the maintained
sources. The 1,000 witnesses were independently replayed in C++; its self-test
ran 60 positive cases and one corrupted-input control. Python also checked 12
exact Gram cases and 48 random filter identities.

The two new determinant runs used distinct random seeds, 300 exact confluent
matrices in total (two determinant implementations), 27 full Taylor-jet
checks, and 128 prescribed sharp examples. Four invalid-data controls were
repeated. Theta-product diagnostics used 85 decimal digits and 117
shell-angle pairs per run; they are numerical, not exact certificates.
The instability runs cover M=1 through 40, with 1 through 24 repeated; all
angular error bounds are checked by exact Fourier coefficient sums, not grids.
Clock checks cover N=2,4,...,24, including 78 cyclotomic trace identities and
36 rounding/splitting controls.

## Publication and tool boundaries

The three new sections were built together with their bibliography in a
seven-page excerpt, using three pdfTeX passes. All pages were rendered and
inspected; one overfull display was split and rebuilt. The final excerpt has
no unresolved references, citations or overfull boxes. This does not certify
a fresh build of every older section of the complete canonical article.
The canonical master and bibliography were reconstructed against their exact
remote Git blob hashes before inserting the new inputs and references.

Wolfram's new connection attempt still returned HTTP 404. No result from that
service is counted as verification. Lean was not present in this runtime;
no new Lean compilation or full formalization is asserted. External priority,
independent referee acceptance, and successful cloud CI are not claimed.

Machine-readable source and log hashes are stored in
`evidence/certificates/holomorphic_shell_review.json`. Generated renders,
executables and expanded run logs are build artifacts, not maintained source.
