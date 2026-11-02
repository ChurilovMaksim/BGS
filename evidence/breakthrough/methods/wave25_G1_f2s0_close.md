# Wave 25, task 4 — the f=2, s=0 hole: CLOSED via the second-digit lemma

**Verdict: CLOSED.** Parts (a)+(b) of the second-digit lemma (waves 21,
24), transferred from G-orbits to H₀-orbits, complete the wave-14
f=2, s=0 stabiliser argument for G1. The transfer needs |H₀| ≥ 3,
and the degenerate cases |H₀| ≤ 2 are classified exactly: they force
p ∈ {3, 17}, both with k = 1, hence never occur in the k = 2 (s = 0)
setting. No prime search is needed anymore for this hole: the
2×10⁹ bound is moot, because the hole has no instance at any prime.
Repository untouched, no Lean built.

## 1. The exact statement closed

Wave-12 L6 specialised to f = 2, s = 0 (so G = G₀, no p-group cosets):
for C, C′ units mod p² with the same H₀-orbit multiset
{Tr(Cz) : z ∈ H₀} mod p², where H₀ = ⟨α^t⟩, t = gcd(m, 4),
|H₀| = L₀/g, g = gcd(L₀, t), one has C′ ≡ Cz or C̄z mod p² for some
z ∈ H₀. This is the step wave-14 case (2,1) uses as a black box
("Step 1 is f = 2 s = 0"), and the step whose gap wave-14 §5 / wave-16
§0 stated as "k = 2 AND 4 | L₀".

## 2. Transfer lemma: second-digit lemma for H₀-orbits (|H₀| ≥ 3)

Let β = α^t mod p², |H₀| = order of β, B_H = A^{|H₀|}. For a twist
A′ = A(1 + pc√2), c ∈ 𝔽_p^×, the H₀-orbit v1-marginal changes unless
the twist is trivial (A′ ∈ A·H₀ ∪ Ā·H₀). Proof: wave-24 (b) with L₀
replaced by |H₀| throughout, valid exactly when |H₀| ≥ 3:

- (b1) power sums: Σ_{z∈H₀} z^k = |H₀|·[|H₀| | k] (cyclic-group
  orthogonality), so S_r = 0 for r < |H₀| and
  S_{|H₀|} = |H₀|·f·(B_H − B̄_H); full-multiset preservation forces
  B_H real mod p or f = 0 (gcd(|H₀|, p) = 1, since |H₀| | L₀ | p − ε).
- (b2) P₂ obstruction: with T_j = τ_A β^j, the sums Στ̄_j = 0 and
  Στ̄_j² = 0 need β̄ ≠ 1 and β̄² ≠ 1, i.e. |H₀| ≥ 3; then
  Ση̄_j² = |H₀|N(τ_A)/4 and preservation with c ≠ 0 forces
  c = K_H − 2b, K_H = −2Σd1_jη̄_j / (|H₀|N(τ_A)).
- Gap symmetry: the H₀-gap (a/ā)^{|H₀|} = 1 ⟺ ā/a ∈ ⟨β̄⟩ (unique
  order-|H₀| subgroup of the cyclic norm-1 group mod p); Teichmüller
  (wave-24 Lemma 1) gives τ̄_A = τ_A β^r exactly in R/p², hence
  T̄_j = T_{r−j}, d1_{r−j} = d1_j, η̄_{r−j} = −η̄_j, so K_H = 0.
  Then c = −2b with gap ⟺ A′ ∈ Ā·H₀ (the factor 1 + p(2b+c)√2 has
  order p if 2b + c ≠ 0, while |H₀| is coprime to p), and
  A′ ∉ A·H₀ for c ≠ 0. Hence every genuine twist in the gap case
  changes the v1-marginal; outside the gap, (b1) changes the full
  multiset. ∎

Part (a) (wave-21 injectivity) transfers for free: H₀ ⊆ G, and its
proof uses only d^{L₀} = 1 for d ∈ H₀ plus (v0, t) recovering Az mod p.
For the multiset conclusion (b) alone carries the load; (a) gives the
stronger distributional form (wave-19: marginal + conditional + joint).

## 3. Closure chain for L6 at f = 2, s = 0

1. Mod p normalisation (wave-11 mod-p lemma for H₀, order coprime
   to p): C′ ≡ Cz₀ or C̄z₀ mod p; absorb z₀, so C′ = C + pE, E ∈ R/p.
2. r = 2 power sums over the H₀-orbit (wave-12 L6 sketch): multiset
   equality gives Σ_z Tr(Cz)Tr(Ez) ≡ 0 mod p; expanding,
   Σ_z z² = 0 needs β̄² ≠ 1, i.e. |H₀| ≥ 3, and zz̄ = 1 gives
   |H₀|·Tr(CĒ) ≡ 0, so Tr(CĒ) ≡ 0: E/C is purely imaginary mod p,
   E ≡ b√2·C. Hence C′ = C(1 + pb√2) exactly mod p² — the twist form.
3. If b = 0, C′ = C. If b ≠ 0, the transfer lemma (§2) says the
   H₀-orbit multiset changes — contradiction — unless the twist is
   conjugate-trivial, C′ ∈ C̄·H₀, which is exactly L6's allowed
   conclusion. ∎ (Divisible case p | C: induction on f as in wave-12.)

## 4. Degenerate cases: classified, and impossible under k = 2

|H₀| = L₀/gcd(L₀, t), t ∈ {1, 2, 4}, L₀ ≥ 3. Then |H₀| ≤ 2 ⟺
(L₀, t) ∈ {(4, 4), (4, 2), (8, 4)} (direct check of L₀ = gcd and
L₀ = 2·gcd). The transfer provably fails there: at |H₀| = 1 the
singleton orbit cannot see the twist (p = 3, C = 1 mod 9:
Tr(1 + 3c√2) = 2 = Tr(1) for c ≠ 0, yet 1 + 3c√2 ≢ ±1 mod 9);
at |H₀| = 2 the P₂ step breaks (Σβ̄^{2j} = 2τ_A² ≠ 0).

But under k = 2 these cases never occur. The norm-1 group mod p is
cyclic, so ord(α) = 4 forces α² ≡ −1 mod p, i.e. p | 18 and p | 12
(α² = 17 + 12√2), hence p = 3; ord(α) = 8 forces α⁴ ≡ −1 mod p,
i.e. p | 578 and p | 408 (α⁴ = 577 + 408√2), gcd = 34, hence p = 17.
Exact check (script wave25_G1_f2s0_check.py): L₀(3) = 4 with
α⁴ ≡ 1 + 3√2 mod 9, and L₀(17) = 8 with α⁸ ≡ 1 + 51√2 mod 289,
so k = 1 at both. Therefore in the k = 2 setting |H₀| ≥ 3 always,
and §§2–3 close L6 at f = 2, s = 0 unconditionally.

## 5. Correction to the wave-14/16 framing

"4 | L₀" is necessary but NOT sharp for the hole: it is the condition
for g = 4 to be possible, but the transfer fails only at |H₀| ≤ 2.
E.g. L₀ = 12, t = 4 gives |H₀| = 3 and is closed by §§2–3 with no
prime search at all. The wave-16 question "does a k = 2 prime with
4 | L₀ exist?" is answered in the negative for the sharp condition
(no k = 2 prime has |H₀| ≤ 2), and is the wrong question for the hole:
a k = 2 prime with 4 | L₀ but |H₀| ≥ 3 (e.g. hypothetical L₀ = 12)
would not reopen anything.

## 6. Scope (honest)

- Closed: L6 at f = 2, s = 0 (H₀-orbit rigidity mod p²); the wave-14
  (2,1) Step-1 black box is discharged in L6 form. (G1′ at f = 2 in
  full-sequence form was already proved by wave 13 via the Lucas
  identity; this is the second, induction-architecture route.)
- NOT closed by this note: G1 at f ≥ 4 (L6/L7 real-Cz at higher f;
  f = 3 stands as: (1,2) by S\* = 0, (2,1) now unblocked,
  (3,0) absent below 10⁴ but general open); general PC; Lean.
- The f = 2 s = 0 hole proper is gone: it was the last named gap in
  the f = 2 base step, and it is closed by proof, not by search.

## Files

- This note: wave25_G1_f2s0_close.md
- Check script: wave25_G1_f2s0_check.py (ALL CHECKS PASS)
- Prior: wave24_seconddigit_b.md (part (b)), wave21_seconddigit_injectivity.md
  (part (a)), wave14_G1_f3.md §5 (hole statement), wave12_G1_lift.md §6 (L6)
