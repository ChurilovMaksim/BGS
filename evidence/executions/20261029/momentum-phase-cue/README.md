# Momentum-phase unitary value

Python and C++ recompute the Haar occupation buckets at the primes 5, 7, 11 and 13, for times two and three, and check the error inequalities of BGS-TRACE-140. Both print the same values. At p=13 and m=3 the value is 3.418, inside the bound, even though 27 ≡ 1 (mod 13). The odd-symbol energy is the integer identity 16/25 · 9/80000 = 9/125000. Lean decides that energy, the constants 468 and 20, and the residues 27 mod 5, 7, 11 and 13. The conditions t = 1 and t = 2 are not formalized. The residue 27 ≡ 1 (mod 13) is not an exclusion of the form-factor statement: the hypothesis used there is λ ≢ −1.

A seeded Gaussian sample at p=29, m=3, v=0.4, of 600 draws, is recorded in `python_stdout.json`. Its mean 3.709 is a finite-prime Monte Carlo check. An independent exact evaluation gives 3.7555 at the same point. BGS-TRACE-142 identifies the Gaussian main term and leaves the non-injective remainder unbounded, so the limit is verification-pending. The sample is not a proof.

`lake build Bgs` on Lean 4.33.1 is recorded in `evidence/formalization/bgs_aggregate_20261029/build_trace140.log`.

A pass does not prove BGS-TRACE-005 or BGS-BGS-001.
