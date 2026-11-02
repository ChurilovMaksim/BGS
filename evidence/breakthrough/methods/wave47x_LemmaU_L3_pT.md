# Wave 47x, task A — L3 at p|T: PROVED in both regimes (generic cases)

## Verdict

**L3 at p|T is proved** for unit cycles with distinct mod-p values, p odd,
p ≠ 3 — in two regimes. **Regime A** (t̄ negation-free): full proof
including the exact lift, by a Frobenius/period-collapse argument: mod p
the period collapses to T₀ coprime to p, restoring Dickson, and
negation-freeness separates the classes for a free lift. **Regime B**
(t̄ negation-closed, i.e. M(−t̄) = M(t̄) mod p): mod-p splitting proved
by a multiplicity dichotomy, and the exact lift proved for
uniform-tower cycles. The remaining gaps are exactly: collapsed towers
(zero-value / unbalanced-repeat cycles), singular cycles, p = 3, and
partially negation-symmetric t̄. No counterexample anywhere: 0 L3
violations at every censused component. No Lean built, repository
untouched.

## 0. Setup

R_f = Z[√2] mod p^f, α = 3+2√2, β = α² = 17+12√2, N(β) = 1,
Tr(a+b√2) = 2a. Cycle y_j = Tr(Cβ^j), M(C) = {y_j : j ∈ Z/u} (length u,
β^u = 1). C is a unit cycle if N(C) is a unit mod p^f. per(C) = exact
period in Z/p^f; per₀(C) = period of (y_j mod p). t̄, x̄ denote mod-p
reductions. Dickson and Lemma A are wave 46 §2 (used here over F_p).

## 1. Collapse lemmas (the Frobenius step)

Lemma 0 (period ⇒ β-power). If a unit cycle has (exact or mod-p) period
T, then β^T = 1 (in R_f resp. mod p). Proof: Tr(Cβ^j(β^T−1)) = 0 ∀j;
E = C(β^T−1) has Tr(E) = Tr(Eβ) = 0; E = a+b√2 gives 2a = 0 then
Tr(b√2·β) = 48b = 0, so a = b = 0 (p ∤ 48, i.e. p ≠ 2,3); C a unit
gives β^T = 1. ∎

Lemma 1 (collapsed period prime to p). per₀(C) | ord(β mod p) | p²−1,
so p ∤ per₀(C). (R/pR is F_p², F_{p²}, or F_p×F_p; unit-group order
prime to p.) Hence Dickson applies at T₀ — this is what fails at the
exact period T when p | T. ∎

Lemma 2 (T₀ ≥ 3). For odd p ≠ 3, a nonzero unit cycle has per₀ ≥ 3.
Proof: per₀ = 1 ⟹ β ≡ 1 mod p (Lemma 0) ⟹ p² | N(β−1) = −32, so
p = 2. per₀ = 2 ⟹ β² ≡ 1, β ≢ 1 mod p, so β has order 2 in R/pR;
norm 1 excludes mixed signs (1,−1) in the split case, so β ≡ −1 mod p
⟹ p | N(β+1) = 36, so p = 3. ∎

## 2. Theorem A (regime A: t̄ negation-free)

Hypotheses: p odd ≠ 3; t, x, x′ unit cycles; M(x) ∪ M(x′) =
M(t) ∪ M(−t); t̄ distinct-valued and negation-free mod p; x̄, x̄′
distinct-valued mod p. Conclusion: {M(x), M(x′)} = {M(t), M(−t)} exactly.

Step 0 (reduce mod p). M(x̄) ∪ M(x̄′) = M(t̄) ∪ M(−t̄), length u.
Let T₀ = per(t̄), T_x = per(x̄), T_{x′} = per(x̄′); all divide
T_β = ord(β mod p) (Lemma 0), p ∤ all (Lemma 1), T₀ ≥ 3 (Lemma 2).
Each mod-p value appears u/T₀ (resp. u/T_x, u/T_{x′}) times.

Step 1 (value-set dichotomy). The union's value set is t̄ ⊔ −t̄ (2T₀
values, negation-free), each of multiplicity u/T₀. For v ∈ t̄:
u/T_x·1[v∈x̄] + u/T_{x′}·1[v∈x̄′] = u/T₀. Either (split) no value is
shared: T_x = T_{x′} = T₀ and values(x̄) ⊔ values(x̄′) = t̄ ⊔ −t̄
(a value in x̄ only forces T_x = T₀, which forbids any shared value);
or (both-double) every value is shared: T_x = T_{x′} = 2T₀ and
values(x̄) = values(x̄′) = t̄ ⊔ −t̄ (distinctness).

Step 1′ (both-double impossible). per(x̄) = 2T₀ gives β^{2T₀} ≡ 1,
β^{T₀} ≢ 1 mod p (Lemma 0), so β^{T₀} has order exactly 2 and norm 1;
the order-2 norm-1 elements of R/pR are only −1 (mixed signs excluded
by norm 1 in the split case), so β^{T₀} ≡ −1 mod p. Then t̄ satisfies
z_{j+T₀} = −z_j and z_{j+T₀} = z_j, so z_j = 0 (p odd) — t̄ is the zero
cycle, contradicting distinctness (T₀ ≥ 3). ∎ So the split case holds.

Step 2–3 (norms, signs mod p). P_x̄·P_{x̄′} = P_t̄·P_{−t̄} over F_p
(UFD, from the length-u multiset identity). Dickson at T₀ (Lemma 1):
coefficient comparison exactly as wave 46 §2 gives N_x = N_{x′} = N_t
(3T₀ a unit mod p; T₀ = 3 by direct expansion, 9 a unit), then
θ_{x′} = −θ_x, θ_x² = θ_t², so P_x̄ = P_t̄ or P_{−t̄}; Lemma A (distinct
roots) gives M(x̄) = M(t̄) or M(−t̄), M(x̄′) the other. ∎

Step 4 (class-separation lift). WLOG M(x̄) = M(t̄), M(x̄′) = M(−t̄).
Exact values of M(x), M(t) lie over classes in t̄ only; M(x′),
M(−t) over −t̄ only. For ȳ ∈ t̄, negation-freeness gives ȳ ∉ −t̄, so
M(x′), M(−t) contribute nothing over class ȳ; restricting the exact
union equality to class ȳ gives M(x)|_ȳ = M(t)|_ȳ. Union over ȳ:
M(x) = M(t); symmetrically M(x′) = M(−t). ∎ The exact periods
(T, T_x, T_{x′}), possibly divisible by p, never enter.

## 3. Theorem B (regime B: t̄ negation-closed)

Hypotheses: same as Theorem A except t̄ negation-closed as a set, so
M(−t̄) = M(t̄) mod p (each value u/T₀ times) and the union mod p is
2·M(t̄): T₀ distinct values of multiplicity 2u/T₀. (Forced at (5,2): values sum to 0 mod 5 since 1+β+β² ≡ 0, and the only
distinct triples summing to 0 in F₅ are {0,1,4}, {0,2,3}, both
negation-closed. Also covers the antiperiodic case β^{T_β/2} ≡ −1.)

Mod-p splitting. Per value v: u/T_x·1[v∈x̄] + u/T_{x′}·1[v∈x̄′] =
2u/T₀ (x̄, x̄′ distinct-valued, value sets ⊆ t̄'s values, so
T_x, T_{x′} ≤ T₀). Either (a) partition: some v in exactly one side
forces that side's period T₀/2, hence (no shared value can then exist)
both sides have period T₀/2 and disjoint value sets partitioning t̄'s;
or (b) all shared: 1/T_x + 1/T_{x′} = 2/T₀ with T_x, T_{x′} ≤ T₀ forces
T_x = T_{x′} = T₀ and identical value sets, i.e. M(x̄) = M(t̄) = M(x̄′).
Case (a) is impossible: T₀ odd makes T₀/2 non-integral; T₀ even gives
β^{T₀/2} of order 2 (β^{T₀} = 1, β^{T₀/2} ≠ 1 as per(t̄) = T₀ exactly),
hence β^{T₀/2} ≡ −1 by norm, and a period-T₀/2 cycle would satisfy
y_{j+T₀/2} = −y_j = y_j, so y = 0, contradicting distinctness. ∎

Uniform-tower lift. Tower of C over class ȳ: exact values in M(C)
reducing to ȳ (u/T₀ of them). The tower is uniform if every lift of ȳ
mod p^f appears equally often (count c = (u/T₀)/p^{f−1}, c = 1 in all
censused setups). Uniform-tower lemma: if C has uniform towers, M(C)
= c·LiftSet(values(C̄)), hence is determined by M(C̄). In case (b),
M(x̄) = M(t̄) = M(x̄′) and same T₀ give M(x) = M(t) = M(x′) = M(−t)
for uniform-tower cycles, so {M(x), M(x′)} = {M(t), M(−t)}. ∎

## 4. Census (scripts wave47x_L3_pT_survey.py, _survey2.py, _towers.py)

| component | u | p\|T (T,T₀,count) | params | multisets | L3 viol |
|-----------|---:|-------------------|-------:|----------:|--------:|
| (5,2) | 15 | (15,3,600), T/T₀=5, defect val 1 | 625 | 29 | 0 |
| (5,3) | 75 | (15,1,600), (75,3,15000), T/T₀=25 | 15625 | 131 | 0 |
| (7,2) u=21 | 21 | (21,3,2352), T/T₀=7 | 2401 | 59 | 0 |
| (11,2) | 66 | (66,6,14520), T/T₀=11, defect val 1 | 14641 | 81 | 0 |
| (13,2) | 7 | none (ord β = 7) | 28561 | 2125 | 0 |
| mod p: 5,11,13 | 3,6,7 | — | 25,121,169 | 7,16,19 | 0 |

Both-double search mod p: 0 at p = 5, 11, 13 (corroborates Step 1′).
Regime-A coverage: (7,2) has 588 p|T cycles satisfying
distinct+negation-free (of 2352); (5,2) has 0 (sum-zero forces
negation-closed). Tower uniformity (p|T cycles): (5,2) 300/600,
(7,2) 1470/2352, (11,2) 10890/14520, (5,3) 7500/15600. Nonuniform
towers are exactly the collapsed ones: at (5,2)/(7,2) they coincide
with repeated-value cycles; at (11,2) they are exactly the 3630
zero-value cycles (4-distinct cycles, 3630, are uniform: repetition
there is balanced ±-pairing). At (5,3) the 600 T₀=1 cycles are C ∈ 5R.

## 5. Remaining gaps (exact)

1. Lift-B for non-uniform towers: collapsed-tower cycles (zero-value,
   unbalanced-repeat) are censused clean but not proved; the approach
   is the tower-AP route (tower = p-adic arithmetic progression).
2. Repeated-value cycles in the mod-p argument (Lemma A fails):
   censused 0 violations everywhere, including all (11,2) 4-distinct
   and 3-distinct cycles.
3. Singular cycles (N non-unit; Lemma 0 fails): e.g. (7,2) (3,1)×48
   are C ∈ 7R, (5,3) (15,1)×600 are C ∈ 5R; censused clean.
4. p = 3: Lemma 0's 48b step and Step 2's 3T₀ step both fail.
5. Partially negation-symmetric t̄: neither negation-free (Theorem A)
   nor negation-closed (Theorem B); censused clean, unproved.
6. (7,2) has no u with α^u = −1 (α has odd order 21 mod 49); the framework there uses u = ord(β) = 21 instead — the theorems only need β^u = 1, so this is a setup note, not a gap.
