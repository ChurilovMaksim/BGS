# J2: strategy after Line J

Assessment only. Labels: [P], [CA], [N], [H].

## 1. What Theorem J says about R′

Theorem J is [CA]. It shows that the frozen d = 7, (±2,8) remainder φ⁻¹D7 is ≥ m·K·1.0184^m/m in absolute value, with both signs, in every residue class mod 168 (6-term windows).

**What would complete the refutation of frozen R′.** Frozen R′ is refuted as soon as O_m ≥ −C·mφ, where O_m covers the other (ρ, d). Two cheap steps are available:
- **(±2,16) at d = 7.** The float rate is 0.81^m [N]. Certifying it needs the Line J machinery on the 64-state (±2,16) automaton: sector decomposition plus rest certificates. This is routine, about one session.
- **Other levels d | h_m.** These are genuinely hard. They involve twisted operators of order ord_d(λ) for primes d | h_m, and the set of such primes is unbounded. There is no fixed finite operator family [P, Line I S4.2].

  A one-sided bound is still plausible. Each level contributes cross_d + sq_d with sq_d ≥ 0, so only cross_d needs a lower bound.

  [H] For d ≥ 11, |W_C| ~ d^{−1}. The twisted radii are bounded by the untwisted 1.915 and are generically ≈ 1.28 or less. Under a uniform twisted-radius bound r_d ≤ r < √λ/μ* = 1.2604 for all d ≥ 11, each cross_d/φ would decay. The trouble is that a d-uniform certificate is not available, and d = 7 itself already violates this bound.

**Without the refutation.** Even without bounding O_m, the d = 7 result means that **any proof of R′ must exhibit exact cancellation between levels**. That is implausible [H]: the levels involve disjoint member sets and unrelated Gauss sums.

**Practical reading.** Frozen R′ should be regarded as false [H, strongly supported]. The exponentially growing d = 7 term is certified, and nothing visible compensates it.

## 2. Should the replacement conjecture carry arithmetic correction factors?

Yes. Theorem J and Prop J-C show that the obstruction is arithmetic, not analytic:
- the d = 7 members of a resonant primary carry twisted traces Ẑ_d(β);
- these traces grow at the twisted radius r_tw;
- the frozen main term n_d|Z_ρ|²/d² treats them as if they were zero.

The correct main term is the actual member value. That is exactly **R′_A** (Line I), whose members are Z_t = ω_tZ₀/d + Δ_t, with Δ_t an explicit combination of d²−1 twisted traces. Two refinements are suggested:

- **(a) Corrected frozen form.** Replace |Z_ρ|²/d² by |ω_tZ_ρ/d + Δ_t^{lead}|². Here Δ_t^{lead} keeps only the twisted orbits whose rate exceeds √λ/|Z_ρ|^{1/m}, so for (±2,8) at d = 7 these are 2:1 and 0:1.

  This is a finite, explicit, *arithmetic* correction. It uses:
  - the sector constants (8th roots of unity);
  - Gauss sums in Q(ζ_d);
  - one certified eigenvalue per class.

  It is a correction factor in the sense of the question. In the sum over ±ρ the correction is 2Re(B_C ξ_C^m) with B_C = c₀ᶠ(c⁺ − conj c⁻)W_C. This is non-zero exactly for the classes in sectors 0 and 4.
- **(b) The finite list is decidable per level.** For a resonant primary and a level d, only the twisted classes with r_tw(d,C)·|μ_ρ| > √λ need a correction. Those classes can be listed by a finite float survey and then certified. For d = 7 and (±2,8) the list is {2:1, 0:1} after the ρ-cancellation of {1:3, 1:2, 1:5}.

  [H] For d ≥ 11 the list is plausibly empty for (±2,8), because the radii decrease with d. Checking d = 11 and d = 13 is a cheap next experiment, since both divide some h_m.

**Recommendation.** State the replacement as **R′_corr: W′^corr_m = o(m)**, with corrections at the levels d where some r_tw(d,C)·μ_ρ > √λ. Prove (or certify) that only finitely many d need a correction. Then R′_corr and R′_A agree up to o(m) at the remaining levels.

## 3. Can R′_A be proved in some residue class?

Honest answer: **not with current tools** [assessment].
- R′_A removes all resonant-member terms. What remains is W′_A, i.e. the non-resonant "bulk" sum.
- Controlling W′_A is the original BGS difficulty: an equidistribution or decorrelation bound for Σ|Z_m(ν)|² over non-resonant ν, uniform in m.
- Residue-class restrictions m ≡ j (mod 168) fix the d = 7 arithmetic. They do not fix the bulk, which depends on the full factorisation of h_m (Line I S4.2: unbounded prime support).
- The Poisson/aliasing identity (Line I S4.1′) reduces W′_A to difference-count collisions C_Z(k) at multiples of 2h/e. These are again not controlled by any fixed operator.

**Feasible partial targets:**
1. **R′_A for the d = 7 level.** After subtracting the exact members, the d = 7 contribution of (±2,8) is identically 0 in R′_A. Our certificates make R′_A's main term explicit and computable, with explicit error, for every m ≡ 3 (mod 6). In other words, R′_A is *well-posed and computable at level 7* [CA].
2. **An averaged version.** E_{m∈window} W′_A/m → 0 along m ≡ j (mod 168). This might follow from L²-in-m bounds (Line I S4.4) combined with the window lemma. It is not attempted here [H].
3. **A conditional version.** R′_A ⇐ (uniform r_tw(d) bound for d ≥ 11) ∧ (bulk equidistribution). This isolates exactly one arithmetic hypothesis and one analytic hypothesis.

## 4. Next steps, by value per effort

1. Certify the (±2,16) d = 7 members with the sector machinery; this would make Corollary J's hypothesis cover them. Then survey (float) the levels d = 11 and 13, and any d | h_m with small ord_d(λ), for (±2,8) and (±2,16).
2. Have rig_disc.py and the sector-level K-symmetry independently audited (§5 caveats in REPORT.md).
3. Formulate R′_corr (§2) for the maintainers, as a TRACE item. Mark frozen R′ as "refuted modulo O_m ≥ −Cmφ (Theorem J)".
4. Long-term: bulk equidistribution (W′_A), which is the real BGS bottleneck.
