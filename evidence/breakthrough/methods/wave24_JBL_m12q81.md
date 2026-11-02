# Wave 24, task 2 — JBL rigidity at m=12, q=81 (p | m/P case): FALSE

## Verdict

Single-class joint rigidity is **false** at m=12, q=81, the smallest
p | m/P instance (3 | m/P = 3). The failure is systematic, not an
isolated pair: all 48 joint-multiset classes contain parameters that
are not D-related (up to trace-kernel). This refutes the rigidity
lemma as stated; it does NOT refute JBL itself (same moral as the
wave-23 n=1 case: JBL's conclusion is about matching classes, and
this pair does not by itself break it). Repository untouched, no
Lean built.

## Setup

R = ℤ[√2], α = 3+2√2, β = α^t = α^4, t = gcd(12,4) = 4,
q₂ = 128 (v₂(D₁₂) = 7), q = 81, D₁₂ = 2^7·3^4·5^2·7^2·11^2.
A genuine class parameter satisfies (α^12−1)B ≡ 0 mod D₁₂.
Joint multiset J(B) = {(Tr(B) mod 128, Tr(Bβ^s) mod 81) : s ∈ ℤ/3}.
D-related up to trace-kernel: B′ ≡ c(B)β^j (mod 81) and
B′ ≡ ε·c(B)β^j (mod 128), c ∈ {id, conj}, ε in the 8-element
kernel (u ∈ {1,65}, v ∈ {0,32,64,96}); j mod 16 and j mod 27 are
independent by CRT. Script: `wave24_JBL_m12q81.py` (exact integers).

## Enumeration (exact)

- β mod 81 = 10+3√2, order 27; β mod 128 = 65+24√2, order 16.
- δ = α^12−1: mod 128 = 64+72√2, 128 genuine B's (x ≡ 0 mod 16,
  y ≡ 0 mod 8); mod 81 = 63√2, 81 genuine B's (B ≡ 0 mod 9).
- Genuine B mod 10368: 10368, but only 48 distinct J values.
- **All 48 J-groups contain a pair that is not D-related**
  (up to kernel, shared conjugation, exhaustive j/ε check).

## Explicit counterexample

B = 9√2, B′′ = 36√2 = 4B (mod 81), both ≡ 0 (mod 128);
global lifts mod D₁₂ (0 mod 25·49·121): B = (0, 1366041600),
B′′ = (0, 853776000), both satisfy (α^12−1)B ≡ 0 mod D₁₂.
- J(B) = J(B′′) = {(0,0), (0,27), (0,54)}: odd traces
  (0, 27, 54), pattern value 0.
- D-orbit of B mod 81 has 6 elements: (real, √2-coeff)
  (0,9), (54,9), (27,9), (0,72), (27,72), (54,72); B′′ = (0,36)
  is not among them, and no kernel twist touches the 81-part.
- The exhibit also works under the same-s pairing
  J₂(B) = {(Tr(Bβ^s) mod 128, Tr(Bβ^s) mod 81)}, since both
  parameters vanish mod 128.

## Mechanism (why it fails)

Write genuine B = 9C, C ∈ R/(9). β ≡ 1+3√2 (mod 9), so the
trace triple of C is (2a, 2a+3b, 2a+6b) mod 9. When a ≡ 0
mod 3 and b ≢ 0 mod 3, all three traces are ≡ 0 mod 3, hence
the mod-81 traces are multiples of 27 — and multiplication by 4
fixes every multiple of 27 mod 81 (4·27k = 108k ≡ 27k). So
J(4B) = J(B) whenever the pattern part is preserved (here 0),
while 4C has √2-coefficient 4b ∉ {b, −b} mod 9: the D-orbit
cannot reach it (β preserves b mod 9 when a ≡ 0 mod 3, since
b′ = 3a+b ≡ b). The p | m/P obstruction is thus not a
Lucas-step subtlety but a mod-3 collapse: β ≡ 1 (mod 3) makes
the trace data blind to ×4 twists.

## Consequence

A JBL proof cannot go through single-class rigidity at m=12,
q=81 as stated. What restriction (if any) rescues rigidity —
e.g. excluding the a ≡ 0 mod 3, b ≢ 0 mod 3 degenerate case,
or quotienting by the J-preserving twists — is not determined
here. The general p | m/P case was not attempted, per brief.
