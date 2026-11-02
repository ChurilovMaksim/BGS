# Wave 30, task 4 — twin sums at 12|m: unconditional dichotomy + H12

## Verdict

No counterexample: at 12|m ≤ 120 the twin sum never dominates
(worst ratio 1.2×10⁻¹⁶ at m=24, then ≤ 10⁻³⁰). Gap (ii) is closed
unconditionally up to a tiny constant, and reduced exactly to
one narrow hypothesis, H12, for the full o(1). Repository
untouched; no Lean built.

## Setup

Let m = 12u, n = m/2 = 6u. Then D_m = 2^a·S_m² with
a = 2v₂(m)+3 ≥ 7 (wave-11 LTE) and S_m = odd part of y_{6u}
(verified exactly for even m ≤ 120). A twin qt is p^{2f} ‖ D_m
(p^f ‖ S_m) with 3 ∤ ord_{p^{2f}}(β), β = 17+12√2.
Then qt/D_m = 1/(2^a·c_p²) where c_p = S_m/p^f is the cofactor.

## Lemma 1 (cofactor floor 3465 — proved)

3465 | S_m at 12|m, and no twin prime divides 3465.
*Proof.* y_n = 2U_n(6,1), and U_d | U_n for d | n (Q=1), so
y_6 = 13860 = 2²·3²·5·7·11 divides y_{6u}; taking odd parts,
3465 = 3²·5·7·11 divides S_m, and S_m = 3465·C_u^{odd} with
C_u = y_{6u}/y_6 = U_u(39202,1). The primes 3,5,7,11 are never
twin: ord_{p²}(β) = 6, 15, 21, 66 respectively (verified
exactly), all divisible by 3, and order-lifting multiplies the
order by p or leaves it, so 3 | ord_{p^{2f}}(β) for all f ≥ 1.
Hence every twin prime p ∤ 3465, so c_p is a multiple of 3465
and c_p ≥ 3465. ∎

## Theorem 2 (unconditional dichotomy — proved)

For 12|m: Σ_{twin qt} qt/D_m ≤ 1/(2^a·3465²) + 3m/(2^a·S_m^{2/3}).
Hence lim sup_{12|m} Σ qt/D_m ≤ 1/(128·3465²) ≈ 6.51×10⁻¹⁰.
*Proof.* Σ qt/D_m = Σ_p 1/(2^a c_p²). At most one twin prime
has c_p ≤ S_m^{1/3}: k such primes give (S_m/C)^k ≤ S_m
(product of distinct prime powers dividing S_m), so with
C = S_m^{1/3}, k ≤ 1. That term is ≤ 1/(2^a·3465²) by Lemma 1.
The rest have c_p > S_m^{1/3}, each contributing
< 1/(2^a S_m^{2/3}), and there are ω < 3m of them
(D_m < 2·5.83^m). The tail tends to 0 exponentially, since
S_m ≥ 5^{6u−1}/2^{v₂(6u)}. ∎

## Lemma 3 (composite u — proved modulo Zsigmondy)

Let u composite, d its least prime factor. Then C_u^{odd} has
≥ 2 distinct odd prime factors, and every twin prime satisfies
c_p ≥ 10395; all but possibly one satisfy c_p ≥ 3465(u−1).
*Proof.* C_u = C_d·K with K > 1 (divisibility). Bang–Zsigmondy
(BHV: primitive divisors exist for n > 30; n ≤ 30 checked
computationally below) gives a primitive prime q_u | C_u with
q_u ∤ C_d; q_u is odd for u ≥ 3 (if u odd, C_u odd; if u even
≥ 4, q_u ∤ C_2 = 2·17·1153), and q_u ≡ ±1 mod u (rank of
apparition), so q_u ≥ u−1. Also C_d^{odd} > 1 for d ≥ 2 (odd d:
C_d odd > 1; even d = 2k: C_{2k} = C_k·V_k with v₂(V_k) = 1,
proved from γ = 1+2A, so the odd part V_k/2 ≥ 19601). Hence
some odd prime r | C_d, r ≠ q_u, divides C_u^{odd} alongside
q_u. If p = q_u then c_p ≥ 3465·r ≥ 10395; otherwise
c_p ≥ 3465·q_u ≥ 3465(u−1). ∎

## Hypothesis H12 (the exact remaining obstruction)

**H12.** The minimum twin cofactor tends to ∞ along 12|m
(equivalently: for each fixed C, only finitely many 12|m have
a twin prime power of cofactor ≤ C).
Under H12, Σ qt/D_m → 0 along 12|m: the single small-cofactor
term is ≤ 1/(2^a c_min²) → 0 and the tail → 0 by Theorem 2.
Conversely H12 is necessary along the subsequence v₂(m) = 2
(a = 7 fixed): a bounded cofactor occurring infinitely often
there keeps Σ qt/D_m ≥ 1/(128C²) > 0. So H12 ⟺ the Twin Sum
Lemma along 12|m with bounded 2-part (along v₂(m) → ∞ the
2^a factor alone kills the sum).
*Hardness.* Bounded cofactor c_p ≤ C means C_u^{odd} = c₁·p^f
with c₁ = c_p/3465 ≤ C/3465 fixed: prime-power-odd-part values
of the Lucas sequence C_u (after removing C_d, of its
subsequences). Same flavour as H (wave 28 §4–5: prime values
of Lucas sequences are open), but strictly thinner: only
12|m, only twin primes, the fixed factor 3465 extracted, and
composite u reduced to the K-prime-power subcase by Lemma 3.

## Computation (exact; script wave30_gap2_check.py, ALL CHECKS PASS)

Twin sums at 12|m ≤ 120 (twin primes with f = exponent in S_m):

| m | twin primes | Σqt/D_m | min cofactor |
| 12 | — | 0 | — |
| 24 | 17 | 1.2×10⁻¹⁶ | 3,995,145 |
| 36 | — | 0 | — |
| 48 | 17, 577 | 6.0×10⁻³² | 9.0×10¹³ |
| 60 | 19, 29, 41, 59 | 7.4×10⁻⁴³ | 1.4×10²⁰ |
| 72 | 17 | 2.2×10⁻⁵³ | 9.4×10²⁴ |
| 84 | 13², 113, 239, 337 | 1.0×10⁻⁵⁹ | 3.7×10²⁸ |
| 96 | 17, 577, 665857 | 1.4×10⁻⁶² | 9.3×10²⁸ |
| 108 | — | 0 | — |
| 120 | 17, 19, 29, 41, 59, 241, 5521 | 4.2×10⁻⁸⁵ | 6.9×10³⁷ |

m=48 reproduces 289+332929 (wave 27). Observed min cofactors
are ≥ 4×10⁶, i.e. far above the floor 3465; the only prime
power with f ≥ 2 is 13² at m=84, still negligible. Composite
u ≤ 30: every C_u has ≥ 5 distinct odd prime factors and a
primitive prime (listed in the script output), confirming
Lemma 3 in range; u > 30 rests on BHV.

## Δ corollary — with a counting caveat (honest)

Under RB1', RB2, RB3, max|f_qt| ≤ m^b, and **H12-poly**
(Σ_{twin} qt ≤ D_m/m^{9+2b} eventually), the wave-25 counting
gives Δ → 0 along 12|m; with wave 29 (Δ = 0 unless 12|m) and
wave-27 Theorem A, that is Δ → 0 fully conditionally.
CAVEAT: the wave-25 §6 product as literally written,
(8m²·m·Σqt)·(4m²·8·m^b) = 256m^{5+b}Σqt (N·M reading; the
N·M² reading gives 8192m^{7+2b}Σqt), is o(D_m) only under
polynomial decay of Σqt/D_m — mere Σqt = o(D_m) does not
suffice, and even H (Σqt ≤ 3D_m/m) does not suffice under
this counting. So H12 alone does not close Δ → 0; H12-poly
(or a sharper Δ_F bound, or sharper fiber counts) is the
precise remaining requirement. This caveat does not affect
Theorem 2 or H12 themselves. Empirically the decay is
exponential (table above), consistent with H12-poly holding.
