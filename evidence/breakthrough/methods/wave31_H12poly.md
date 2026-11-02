# Wave 31, task 3 — H12-poly proved (in fact, exponentially)

## Verdict

**H12-poly is proved, unconditionally.** For m = 12u,
Σ_{twin qt} qt/D_m ≤ 18u³/α^{8u} with α = 3+2√2, hence
Σ_{twin} qt ≤ D_m/m^{9+2b} for all m ≥ 1200(b+1)², for every
fixed b ≥ 0. The wave-30 caveat (H12 alone does not close
Δ → 0) is discharged: H12 itself follows too, since the
minimum twin cofactor satisfies c_min ≥ α^{4u}/(8u) → ∞.
Consequence: Δ → 0 fully, conditional only on RB1', RB2, RB3
and max|f_qt| ≤ m^b (wave-25 counting + wave-29 Δ = 0 unless
12|m). Repository untouched; no Lean built.

## Setup (waves 27/30, taken as given)

α = 3+2√2, β = α² = 17+12√2, x_n + y_n√2 = α^n. For m even,
D_m = 8y_{m/2}². Let m = 12u, so S_m = odd part of y_{6u},
D_m = 2^a·S_m² with a = 2v₂(m)+3 ≥ 7. A twin qt is
p^{2f} ‖ D_m with p^f ‖ S_m (p odd, p ≠ 3) and
3 ∤ ord_{p^{2f}}(β). Then qt/D_m = 1/(2^a·c_p²) where
c_p = S_m/p^f is the cofactor. The whole proof is one
observation: **a twin prime divides the much earlier term
y_{2u}, with no valuation growth**, so its cofactor is
exponentially large.

## Lemma A (twin primes divide y_{2u})

p | y_{6u} means β^{6u} ≡ 1 mod 𝔭 for 𝔭 | p, so
d := ord_𝔭(β) divides 6u. Order lifting at prime powers
gives ord_{p^{2f}}(β) = d·p^s, so 3 ∤ ord_{p^{2f}}(β)
implies 3 ∤ d (p ≠ 3; 3 itself is never twin since
ord_9(β) = 6). Then d | 6u with gcd(d,3) = 1 forces
d | 2u, so β^{2u} ≡ 1 mod 𝔭, i.e. 𝔭 | X − Y with
X = α^{2u}, Y = ᾱ^{2u}. Since p is odd, 𝔭 ∤ 2√2, hence
p | y_{2u}. ∎

## Lemma B (LTE: no valuation growth from 2u to 6u)

y_{6u}/y_{2u} = (X³ − Y³)/(X − Y) = X² + XY + Y², and XY = 1.
Modulo any 𝔭 | p | y_{2u} we have X ≡ Y, so the ratio is
≡ 3X² mod 𝔭; X is a unit mod 𝔭 and p ≠ 3, so the ratio is a
unit at 𝔭. Hence v_𝔭(y_{6u}) = v_𝔭(y_{2u}) for every 𝔭 | p,
so v_p(y_{6u}) = v_p(y_{2u}) = f, and p^f ≤ y_{2u}. ∎

## Lemma C (2-part, elementary)

y_{2k} = y_k·L_k with L_k = α^k + ᾱ^k. Binomial expansion
gives L_k = 2·3^k + 16ℤ, so v₂(L_k) = 1 for all k ≥ 1, and
y_k = 2k·3^{k−1} + 16ℤ, so v₂(y_k) = 1 for k odd. Iterating,
v₂(y_n) = 1 for n odd and v₂(n)+1 for n even. In particular
v₂(y_{6u}) = v₂(u)+2, so S_m = y_{6u}/2^{v₂(u)+2} ≥ y_{6u}/(4u).
∎

## Theorem (exponential cofactor bound)

c_p ≥ α^{4u}/(8u) for every twin prime p at m = 12u.
*Proof.* By Lemmas A–C, c_p = S_m/p^f ≥ S_m/y_{2u} ≥
y_{6u}/(4u·y_{2u}). And y_{6u}/y_{2u} ≥ (α^{6u} − 1)/α^{2u}
= α^{4u} − α^{−2u} ≥ α^{4u}/2, since 0 < ᾱ^{6u} < 1 and
α^{4u} ≥ α⁴ > 2. ∎

## Main bound and H12-poly

Σ_{twin} qt/D_m = Σ_p 1/(2^a·c_p²) ≤ ω·64u²/(2^a·α^{8u}),
where ω, the number of twin primes, satisfies ω < 3m = 36u
(2^ω ≤ D_m < 2·5.83^m, wave 30). With 2^a ≥ 128:
Σ_{twin} qt/D_m ≤ 18u³/α^{8u}.

For H12-poly it suffices that 18u³/α^{8u} ≤ (12u)^{−(9+2b)},
i.e. 8u·ln α ≥ ln 18 + 3 ln u + (9+2b)·ln(12u). Using
ln α > 1.76 and ln x ≤ 2√x, the right side is
< 9 + (69+14b)√u, while the left side is ≥ 14.08u. For
u ≥ 100(b+1)² we have √u ≥ 10(b+1), so
14.08u ≥ (140.8b+140.8)√u ≥ (69+14b)√u + 9. Hence
Σ_{twin} qt ≤ D_m/m^{9+2b} for all m ≥ 1200(b+1)². ∎

## Computation (script wave31_H12poly_check.py, ALL CHECKS PASS)

Exact sympy factorisation at 12|m ≤ 120: twin lists match
wave 30 exactly (including 665857 at m = 96, ratio
1.425×10⁻⁶²), and Lemmas A, B, the cofactor bound, and the
exponential bound are verified at every twin prime. Caught
and fixed en route: naive trial division had merged
665857·9188923201 into one fake prime, hiding the m = 96
twin; exact factorisation restored it.

## Honest limits

b is the wave-25 fiber-size exponent max|f_qt| ≤ m^b: fixed
but its value is not determined here, and the threshold
1200(b+1)² is crude, not sharp. The Δ → 0 corollary still
needs RB1' (CRT-injectivity sketch), RB2, RB3, and the m^b
fiber bound. Lean formalisation is open.
