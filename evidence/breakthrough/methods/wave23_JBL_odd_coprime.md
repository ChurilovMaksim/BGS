# Wave 23, task 2 (retry) — JBL odd part, coprime case: FALSE, exact counterexample

## Verdict

The coprime case of single-class JBL rigidity is **false as stated**.
The failure is not the p-part obstruction (p | m/P) — the coprime
hypothesis kills that — but the opposite degeneracy: the β-action can
be trivial mod p, so the odd class data collapses to a single trace.
Repository untouched; no Lean built.

## 1. What was to be proved, and why the coprime case looked safe

Setup (wave 20 §4): R = ℤ[√2], α = 3+2√2, β = α^t, t = gcd(m,4),
P = 2^{v₂(m)}, q₂ = 2^a, q = p^{2f} ‖ D_m, p odd. For a class parameter
B (i.e. (α^m−1)B ≡ 0 mod q), the per-class joint multiset is
J(B) = {(Tr(Bβ^s) mod q₂, Tr(Bβ^s) mod q) : s ∈ ℤ/(m/t)}.
The rigidity claim: J(B) = J(B′) ⟹ B′ ≡ Bβ^j or B̄β^j (mod q).

Coprime case p ∤ u = m/P: since m = P·u with P a power of 2, p ∤ u
gives p ∤ m, hence σ = v_p(m/L₀) = 0, so the p-part G_p of
H = ⟨β⟩ is trivial and H = H₀ has order n = L₀/gcd(L₀,t),
coprime to p. The Lucas step should then apply — except it is
vacuous when n = 1.

## 2. The n = 1 characterisation (proved)

n = 1 ⟺ L₀ | t, with t | 4. For odd p: L₀ = 1 would need
p | 2; L₀ = 2 would need p | gcd(16,12) = 4; L₀ = 4 needs
p | gcd(576,408) = 24. Hence for odd p, n = 1 ⟺ p = 3, L₀ = 4,
t = 4. Then k = v₃(α⁴−1) = 1 (α⁴−1 = 576+408√2, 3 inert),
σ = 0, f = 1, q = 9. The case occurs for every m divisible by 4
and not by 3 (then t = 4 and 3 ∤ m, so the coprime hypothesis
holds). Here β = α⁴ ≡ 1 (mod 3), so the odd H-orbit is a single
trace, which sees only the real part of C = B/3 mod 3.

## 3. Exact counterexample: m = 8, p = 3, q = 9

D₈ = 1331712 = 512·9·289, q₂ = 512, t = 4, m/t = 2 positions
per class. Class parameters mod D₈ (both verified Fix:
(α⁸−1)B ≡ (α⁸−1)B′ ≡ 0 mod D₈):

- B = 887808 + 1040400√2, B′ = 887808 + 596496√2.
- B ≡ B′ ≡ 16√2 (mod 512) — identical pattern part.
- B ≡ 3 (mod 9), B′ ≡ 3+3√2 (mod 9); B ≡ B′ ≡ 0 (mod 289).

Joint multisets over s ∈ ℤ/2 (pairs (Tr mod 512, Tr mod 9)):
J(B) = J(B′) = [(0,6), (0,6)] — equal position by position,
since 3β^s ≡ 3 and (3+3√2)β^s ≡ 3+3√2 (mod 9), both of trace 6.

But B′ is not D-related to B mod 9: β^j ≡ 1+3j√2 (mod 9), so
Bβ^j ≡ 3 and B̄β^j ≡ 3 (mod 9) for all j, while B′ ≡ 3+3√2.
The D-orbit of B mod 9 is the singleton {(3,0)}; (3,3) ∉ it.

Script: `wave23_JBL_odd_coprime_check.py` (all checks pass).

## 4. Diagnosis and consequence

The coprime hypothesis removes the p-part of H but not the
possibility L₀ | t. When n = 1, joint data cannot see the
√2-coefficient of C mod p^f at all, so no rigidity argument
based on per-class multisets can work there — the Lucas
polynomial is constant. The same construction works for every
m divisible by 4 and not by 3 (B ≡ B′ mod q₂, B ≡ 3,
B′ ≡ 3+3√2 mod 9, equal elsewhere).

This refutes the single-class rigidity lemma as stated. It does
NOT refute JBL itself: for this pair JBL's conclusion holds
trivially (the joint multisets are equal, π = id works). What
fails is the proof strategy via single-class rigidity in the
n = 1 case: a JBL proof must handle n = 1 separately (e.g. via
the pattern lemma plus trivial odd data) or restrict the
rigidity lemma to n ≥ 2. The n ≥ 3 Lucas argument itself
(power sums → (N(C), Tr(C^n)) → C up to H/conjugation)
is untouched by this counterexample, as is its known
discriminant-divisible subcase (wave-12 L6 gap).
