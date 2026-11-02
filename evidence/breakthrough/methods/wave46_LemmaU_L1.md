# Wave 46, task 1 — L1 single-cycle lemma: proved at f = 1, corrected form for units, counterexample in the degenerate locus

## Verdict

L1 is settled in three regimes, not one. **(a) L1-naive is PROVED at
f = 1** (mod p, p ≥ 5): the value multiset determines the β-cycle up to
rotation/reversal, no scaling needed. **(b) L1-corrected holds for UNITS
at p^f**: the fiber is dihedral × Stab(M), verified with 0 unexplained
collisions at 25, 49, 121, 125, 169. **(c) L1-corrected is FALSE for
non-units**: exact counterexample mod 49, (1,2) vs (1,5) — same
21-multiset, neither dihedral nor scaling related. So wave 45's alignment
theorem needs one more hypothesis: its component cycles must be units
(or the degenerate locus must absorb cases like (c)).

## 1. Setup

R = ℤ[√2], β = 17 + 12√2 (N β = 1), cycle t_k = Tr(Cβ^k),
M(C) = multiset of one period. Dihedral orbit of C:
{β^r C, β^r C̄}. Rational scaling: C ↦ λC, λ ∈ (ℤ/p^f)^×,
M(λC) = λ·M(C). Stab(M) = {λ : λM = M}.

## 2. Theorem (L1 at f = 1, proved)

Let p ≥ 5 be prime, β ∈ R/p of order T ≥ 3, N β = 1, β ∉ 𝔽_p
(automatic for β = 17 + 12√2). Then M(D) = M(C) implies D is a
rotation/reversal of C: D ∈ {β^r C, β^r C̄}.

Proof. (i) Periods: for C a unit, the cycle period is exactly T:
{1, β} is an 𝔽_p-basis and the trace pairing is nondegenerate (disc 8,
p odd), so t_{k+T′} = t_k ∀k forces β^{T′} = 1.
(ii) Power sums. p_2 = Σ t_k² = 2T·N(C): the cross sums Σβ^{±2k}
vanish since β² ≠ 1 (T ≥ 3). p_T = Σ t_k^T = T·(Tr(C^T) +
[T even]·C(T,T/2)·N^{T/2}): in (Cβ^k + C̄β^{−k})^T only
i ∈ {0, T/2, T} survive the sum Σ_k β^{k(2i−T)} (else β^{2i−T} ≠ 1).
(iii) The free hypothesis: β ∈ ker(N) forces T | p − 1 (split,
R/p ≅ 𝔽_p × 𝔽_p) or T | p + 1 (inert, R/p ≅ 𝔽_{p²}), hence p ∤ 2T
automatically. So M(D) = M(C) gives N(D) = N(C) and
Tr(D^T) = Tr(C^T).
(iv) Hence D^T ∈ {C^T, C̄^T}: in the inert case a quadratic over a
field has ≤ 2 roots; in the split case argue componentwise, where
{d_1^T, d_2^T} = {c_1^T, c_2^T} as multisets. So D = ζC or ζC̄ with
ζ^T = 1, N ζ = 1.
(v) μ_T^{N=1} = ⟨β⟩ in both cases: μ_T and ker N are cyclic subgroups
of orders T and p ± 1, so their intersection has order gcd(T, p ± 1)
= T, and ⟨β⟩ ⊆ it with order T.
(vi) Non-units (split case only): C = (c, 0) gives the geometric cycle
t_k = cβ_1^k; p_2 = 0 excludes a unit D, and d·⟨β_1⟩ = c·⟨β_1⟩ gives
rotation/reversal (component swap handled by C̄). C = 0 is trivial.
T = 2 is impossible in the real setup: β = α², α^u = −1, u odd,
p odd ⟹ β ≠ −1; T = 1 is β = 1, degenerate.

## 3. Exact computations

Mod-p fiber check (all C ∈ R/p, fiber ⊆ dihedral orbit): 0 violations
at p = 5 (T 3), 7 (3), 11 (6), 13 (7), 17 (4), 19 (10), 23 (11), 29 (5),
31 (15), 37 (19), 41 (5), 43 (22), 47 (23). In every case T | p ± 1,
as (iii) predicts. In particular p = 29 reproduces wave 42's L1.
Mod-25 (m = 30) recomputed: ord β = 15; M(√2) = M(1 + 2√2) =
(0,2,3,5,7,8,10,12,13,15,17,18,20,22,23); 1 + 2√2 ∉ dihedral orbit of
√2; t2[k] = 21·t1[k−10] ∀k; 21·β⁵·√2 = 1 + 2√2 mod 25;
Stab(M) = {1,4,6,9,11,14,16,19,21,24} = {λ ≡ ±1 mod 5}.
Mod-49 Stab example: C = √2, outsider 6√2 = 43·C̄, λ = 43 ≡ 1 mod 7,
Stab(M) = {λ ≡ ±1 mod 7} (14 elements).
Unit-restricted fiber check at p^f (violations all scaling-explained,
0 unexplained): 25: 240/240; 49: 756/756; 121: 9900/9900;
125: 7200/7200; 169: 0 (here T = 7, p ∤ T, so even naive L1 holds).

## 4. Counterexample: L1-corrected fails for non-units (mod 49)

C = 1 + 2√2 (N = −7 ≡ 42, non-unit), D = 1 + 5√2 (N = 0, non-unit).
Both cycles have period 21 and the SAME multiset of 21 distinct values:
C: [2,32,8,44,18,29,37,4,1,30,39,22,23,25,43,16,11,15,9,46,36];
D: [2,29,4,9,8,18,16,36,32,23,15,46,30,43,11,37,22,25,44,1,39].
D is not in the dihedral orbit of C, nor in its rational-scaling
closure {λ·β^r C, λ·β^r C̄}. Location: 7 splits, C ∈ 𝔭, D ∈ 𝔭̄
(conjugate primes above 7); C ∈ 𝔭¹, D ∈ 𝔭̄². The mod-7 shadows agree
(both reduce to the same 3-value cycle), but the mod-49 coincidence of
the full multisets is exact, not a shadow artifact. Mechanism open.

## 5. Sharp corrected restatement (L1*)

For units at p^f: M(D) = M(C) ⟹ D = λ·β^r C or λ·β^r C̄ with
λ ∈ Stab(M(C)). Conjectured sharp form, verified at 25 (e = 1) and 49
(e = 1): Stab(M) = {λ ∈ (ℤ/p^f)^× : λ ≡ ±1 mod p^{f−e}} where
e = v_p(2T). The obstruction is exactly v_p(2T) > 0: then the power-sum
coefficients 2T, T are zero divisors mod p^f, so p_2, p_T determine N,
Tr(C^T) only modulo p^{f−e}, leaving the λ-ambiguity. At f = 1 this
never happens (T | p ± 1 ⟹ v_p(2T) = 0), which is why §2 is clean.
For non-units, L1* is false as stated (§4); the degenerate locus needs
its own classification (conjugate-prime twins, torsion, pure-√2).

## 6. Consequences and remaining gaps

- Wave 45 alignment (§2) is valid as stated only with L1 replaced by
  L1* for units plus a degenerate-locus clause: its hypotheses
  (distinct values, negation-free) do NOT exclude §4's C (21 distinct,
  negation-free values), so a non-unit component cycle can break the
  L1 step of alignment. L3 is untouched by this task and still open.
- Gaps: (1) prove L1* for units at general p^f — the power-sum argument
  through p-adic valuations (sums Σβ^{km} when β^m − 1 is a zero
  divisor); (2) classify the degenerate locus, starting with the §4
  twin mechanism: why conjugate-prime zero divisors share full
  multisets mod p^f, and how often; (3) check whether §4-type twins
  can feed a genuine ℘-collision in Lemma U (single-cycle collision
  alone does not give one).
- No Lean built, repository untouched.
- Scripts: wave46_L1_checks.py (mod-p table, mod-p^f table, mod-25
  example), wave46_L1_units.py (unit-restricted check, §4 pair, §3
  Stab example).
