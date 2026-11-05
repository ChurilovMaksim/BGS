# Research note: the arithmetic ceiling of H5(a) (5 November 2026)

**Not a registry change except BGS-TRACE-348..351.** The note summarises the research pass `research1105`
(`AUDIT_H5A.md`, `BYPASS.md`; working copy, not committed) and records what of it was re-checked for this integration.
Only the elementary arithmetic facts are registered, with proofs in
[REPORT_H5_CEILING.md](../../../computations/verification/h5_ceiling/REPORT_H5_CEILING.md).

**Tags.** [P] proof checked here · [P-sketch] inherited or single-reader sketch: not written out with explicit constants, not formalized, no independent referee · [CA] exact integer computation ·
[N] floating-point numerics · [H] heuristic · [C] conjectural / open.

## 1. Registered arithmetic [P]

Convention h_p = (ε^p + ε̄^p)/2, ε = 1 + √2, as in BGS-TRACE-342 and `Bgs.H6LemmaW` (h_3 = 7, h_5 = 41, h_11 = 23·353).

| Id | Statement | Status |
|---|---|---|
| BGS-TRACE-348 | q prime, q \| h_p (p odd prime) ⟹ q ≡ 1 (mod 2p) and q ≡ ±1 (mod 8) | [P]; Lean general (`Bgs.H5CeilingArith`); [CA] q < 10⁷, p ≤ 1500, no presieve |
| BGS-TRACE-349 | gcd(h_p, h_p′) = 1 for distinct odd primes p, p′ | [P]; Lean general; [CA] all pairs p < p′ ≤ 1500 |
| BGS-TRACE-350 | p ≡ 3 (mod 4), 2p+1 prime ⟹ 2p+1 \| h_p; then P⁻(h_p) = 2p+1, h_p composite for p ≥ 5 | [P]; Lean general; [CA] 25 such p in [5, 1500], exactly the p with P⁻(h_p) = 2p+1 |
| BGS-TRACE-351 | h_p = ∏_{k=1}^{(p−1)/2} (6 − 2cos(2πk/p)) | [P]; [N] 80 digits, odd n ≤ 301; not in Lean |

TRACE-348 sharpens Lemma W (TRACE-342, unchanged): 2 is always a square mod q, so the inert "−1" branch is empty.

## 2. The structural ceiling

**The arithmetic restriction (inherited).** In the audit's reading, H5(a) (BGS-TRACE-303, open) is reachable with the
best available exponent c_B = 0.7375 ([P-sketch], N14b) only for mixed classes with d ≤ λ^{θ_B p}, θ_B = 0.2624. A
p avoids the hard range exactly when no proper divisor of h_p exceeds that size, i.e. (up to the factor 2 in
h_p ≈ λ^{p/2}/2) when h_p is prime or P⁻(h_p) > h_p^{1−2θ_B} = h_p^{0.4753}. With Lemma U and the **open** decoupling
step (C-U) [C] of AUDIT_H5A §3.3 the exponent would relax to about 0.340. This reduction depends on c_B, which is
[P-sketch]; it is not registered here.

**What the registered arithmetic gives [P].**
- Prime factors of different h_p are disjoint (TRACE-349), and each lies in the thin set q ≡ 1 (mod 2p),
  q ≡ ±1 (mod 8) (TRACE-348). There is no shared structure across p to average over.
- TRACE-350 gives an explicit bad family: every p ≡ 3 (mod 4) with 2p + 1 prime, p ≥ 5, has P⁻(h_p) = 2p + 1, so
  for each fixed α > 0 it fails P⁻(h_p) > h_p^α as soon as h_p^α ≥ 2p + 1, i.e. for all members beyond a bound
  depending on α (h_p grows like λ^{p/2}). Whether that family is infinite is the Sophie Germain
  problem [C]; TRACE-350 gives **no** unconditional density.
- [P-sketch] An elementary count with Brun–Titchmarsh and disjointness cannot show that fewer than 100% of p are bad even for
  factors in (2p, 10p) (BYPASS Prop A3). Not re-derived in full here and not registered; note that the displayed
  threshold in BYPASS has the factor 2 log 2 on the wrong side (it should read Y/P < log(Y/4P)/(2 log 2)), which
  does not change the vacuity conclusion.

**Mersenne-type density heuristic [H], tested [CA + N].** Model: a prime q ≡ 1 (mod 2p), q ≡ ±1 (mod 8) divides h_p
with probability 2p/(q − 1) (λ is a square mod q and must lie in the order-p subgroup), independently over q. Exact
divisibility of h_p by every candidate prime q ≤ 10⁸ for all 237 primes 5 ≤ p ≤ 1500
([h5_density.py](../../../computations/verification/h5_ceiling/code/h5_density.py), an independent re-implementation
that tests λ^p ≡ 1 mod q and reproduces the research log row by row):

| p range | # p | no proper factor ≤ 10⁸ (exact) | model mean [H] |
|---|---:|---:|---:|
| 5–199 | 44 | 0.273 | 0.267 |
| 200–499 | 49 | 0.347 | 0.339 |
| 500–999 | 73 | 0.521 | 0.407 |
| 1000–1500 | 71 | 0.324 | 0.414 |
| **all** | **237** | **0.380 (90/237)** | **0.369** |

The aggregate agrees (38.0% vs 36.9%); the per-range values scatter around the model by up to about 0.11. Factor
counts ≤ 10⁸ per p: {0: 87, 1: 88, 2: 43, 3: 16, 4: 3}; 147 of the 237 p have a proper factor ≤ 10⁸ (the log key
`certified_bad`). 146 of them are certified bad, since that factor is ≤ h_p^{0.4753}. The exception is p = 31:
h_31 = 424577·865087 has P⁻(h_31) = 424577 > h_31^{0.4753} ≈ 3.1·10⁵, so p = 31 is good in the sense above (it is
the covered case `p31_cover` of lineN14). The "no proper factor ≤ 10⁸" column is the quantity the model predicts. It
is not a count of good p.
Under the model the probability that p is good decays like log p / p [H], so good p would be about as sparse as
Mersenne primes and "a positive proportion of p is good" would be **false**. This is a heuristic; nothing about
the density of good p is proved, in either direction.

**Theorem L (non-equidistribution of orbit sums; AUDIT_H5A §5.4).** For an ideal 𝔡 | h_pO of norm d = λ^{θp},
max |η(ω)| ≥ (4/π²)θp − O(√p) over nontrivial characters, and ≥ (8/π²)θp − O(√p) and ≥ (4θ − 1 − o(1))p for the two
pure ideals. **Status: [P-sketch]**: the proof (Minkowski choice of ω, order ≥ P⁻(d) ≥ 2p + 1 by TRACE-348, Fejér kernel
F_K ≥ 4(K+1)/π² on |t| ≤ 1/(2(K+1)), the window count, and the doubled window ±ε^k for pure ideals) was re-checked
line by line in this pass by one reader only. The error terms are not explicit, it is not formalized, it has no
independent referee, and it is not registered, so it is a sketch under the tag convention above, not [P]. [N] sanity check
([thmL_sanity.py](../../../computations/verification/h5_ceiling/code/thmL_sanity.py)) on the 25 prime levels
q | h_p, p ≤ 61, q ≤ 1.2·10⁷ (all pure): max|η|/p ≥ (8/π²)θ in every case. The bare leading term 4θ − 1 is not reached
at (p, q) = (3, 7), (5, 41), (7, 239), (19, 9369319), where θ > 0.36 and p is too small for the o(1) term to be small.
This is consistent with the theorem but does not test it. If the sketch is correct, Theorem L shows that a
power-saving estimate for these orbit sums is false. It does not bound any quantity of H5(a) and proves nothing about it.

## 3. Bottom line

- The elementary arithmetic (TRACE-348..351) is proved and checked. It sharpens Lemma W and makes the bad set of p
  explicit, but it does not move H5(a).
- The ceiling stands. Removing H5(a) as a hypothesis along a sequence of p would need infinitely many p with h_p
  prime or P⁻(h_p) > h_p^{0.4753} (0.340 conditionally on (C-U) [C]). That is a Mersenne/Wagstaff-type question [C].
  The heuristic [H] predicts infinitely many such p, at density zero.
- **Theorem R♯-mod v5 (BGS-TRACE-325) stays conditional.** H5 (BGS-TRACE-303) stays open. Nothing here is claimed
  about the frozen conjecture R′ (BGS-TRACE-206).
- Not done here: the audit's other items (Lemma U, (★★) refutation, literature corrections, the B1/B2 bypass
  analysis) are neither registered nor re-verified in this pass.
