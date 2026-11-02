# Wave 46, task 3 — DIV and PAR in general: PROVED

## Verdict

Both remaining hypotheses of the wave-44 doubling-tower pinning are
proved in general, from the ν-definition alone — no minimality, no
verification to m = 512 needed. (PAR) holds for every ν = (1,0)
point with j ≤ 2K (so step0 is integral); (DIV) holds for every
j ≥ 6. Hence the pinning (B1), (B2) of wave 44 is now
UNCONDITIONAL for j ≥ 7 (j ≤ 2K). What remains for full Gap G is
the wave-45 mod-16 witness step at j ≥ 11, not DIV or PAR.

## 0. Setup and ν-definition

Q = 8m² = 2^{2K+3} (m = 2^K), p = 2^j, step0 = Q/(8p) = 2^{2K−j},
d = 2^{j−1} (half-period). y satisfies y_{i+1} = 6y_i − y_{i−1}
mod Q. ν = (1,0) is DEFINED by the half-period defect pattern
(wave-45 j7 note, d = 64 instance): y_{n+d} − y_n ≡ (Q/2)·ν_{n mod 2}
mod Q for all n, i.e. z_0 := y_d − y_0 ≡ Q/2, z_1 := y_{d+1} − y_1
≡ 0 (the full alternating pattern follows from these two by the
recurrence, since (Q/2, 0) alternating is itself a solution mod Q).
With T^d = [[P_{d+1}, −P_d], [P_d, −P_{d−1}]] (P the Pell sequence),
(T^d − I)(y_1, y_0)^T = (0, Q/2)^T, i.e.
(A) (P_{d+1}−1)y_1 − P_d y_0 ≡ 0 (mod Q),
(B) P_d y_1 − (P_{d−1}+1)y_0 ≡ Q/2 (mod Q).

## 1. Valuation lemmas

Let s = j−1, so d = 2^s. (V1) v_2(P_{2^s}) = s and (V2)
v_2(P_{2^s+1}−1) = s are wave 44 §2 (V_{2n} = V_n² − 2 preserves
v_2(V) = 1; c_s ≡ 25 mod 64 for s ≥ 4, direct for s ≤ 3).
(V3) v_2(P_{2^s−1}+1) = s, NEW. Proof: P_n mod 4 cycles 0,1,2,3
(period 4 from the recurrence mod 4), so for s ≥ 2,
P_{2^s−1} ≡ 3 mod 4 and v_2(P_{2^s−1}−1) = 1. With
P_{2n+1} = P_{n+1}² − P_n² at n = 2^{s−1}−1:
P_{2^s−1}+1 = P_{2^{s−1}}² − (A−1)(A+1), A = P_{2^{s−1}−1} odd.
For s ≥ 3: v_2(P_{2^{s−1}}²) = 2s−2 (V1) while
v_2((A−1)(A+1)) = 1 + (s−1) = s by induction (A ≡ 3 mod 4);
2s−2 > s, so the sum has valuation s. Bases s = 1, 2 direct
(P_1+1 = 2, P_3+1 = 36). ∎
(V4) v_2(2 − V_{2^s}) = 2s+3, NEW. Proof: V_{2n} − 2 =
(V_n−2)(V_n+2); for s−1 ≥ 2, V_{2^{s−1}} = 2w with w ≡ 1 mod 64
(wave 44 §2), so v_2(V_{2^{s−1}}+2) = 2; hence
v_2(V_{2^s}−2) = v_2(V_{2^{s−1}}−2) + 2 for s ≥ 3, with base
v_2(V_4−2) = v_2(1152) = 7, giving 2s+3; s = 1 direct (32). ∎
Residues (wave 44 §2 + direct r = 3): for r ≥ 2,
e_r := P_{2^r}/2^r ≡ 3 mod 16; for r ≥ 3, c_r := (P_{2^r+1}−1)/2^r
≡ 9 mod 16 (c_r ≡ 25 mod 64 for r ≥ 4; 171513 ≡ 9 at r = 3).

## 2. PAR theorem

Divide (A), (B) by 2^s (all coefficients have valuation exactly s
by V1–V3): with N = 2K+4−j, a = (P_{d+1}−1)/2^s, b = P_d/2^s,
f = (P_{d−1}+1)/2^s, all odd,
(A′) a·y_1 − b·y_0 ≡ 0 (mod 2^N),
(B′) b·y_1 − f·y_0 ≡ 2^{N−1} (mod 2^N).
The determinant: af − b² = [(P_{d+1}−1)(P_{d−1}+1) − P_d²]/2^{2s}
= (V_d − 2)/2^{2s}, using P_{n+1}P_{n−1} − P_n² = −1 (det T^n = 1).
Hence Δ := b² − af = (2 − V_d)/2^{2s} has v_2(Δ) = (2s+3) − 2s = 3
by V4: Δ = 8δ, δ odd. Eliminate: b·(A′) − a·(B′) gives
Δ·y_0 ≡ a·2^{N−1} (mod 2^N); f·(A′) − b·(B′) gives
Δ·y_1 ≡ b·2^{N−1} (mod 2^N). Dividing by 8 (δ odd):
y_0 ≡ δ^{−1}a·2^{N−4} (mod 2^{N−3}), y_1 ≡ δ^{−1}b·2^{N−4}
(mod 2^{N−3}). Since N−4 = 2K−j: y_0 = step0·t, y_1 = step0·u
with t, u odd (the ambiguity is a multiple of 2·step0, so the
quotients mod 2 are forced). ∎ This proves PAR, and strengthens
it: u is odd too (wave 44 had u integer). Corollary: wave 43's
parametrisation y_1 = step0·(a·t + 8s) with s even is consistent,
and forces a ≡ 11 mod 16 (see §3).

## 3. DIV theorem

Let 2 ≤ s ≤ j−4 (needs j ≥ 6), w_k = y_{2k+1}, μ_s = Q/2^{j−2−s}
= step0·2^{s+5}. Then w_{k+2^s} − w_k = y_{n+d′} − y_n with n = 2k+1
odd, d′ = 2^{s+1}. By the Pell shift identity (wave 45 Lemma 1)
and PAR (§2, so every y_i is a step0-multiple):
y_{n+d′} − y_n = step0·2^{s+1}(c·ỹ_n − e·ỹ_{n−1}), c ≡ 9, e ≡ 3
mod 16 (§1, r = s+1 ≥ 3). So DIV ⟺ c·ỹ_n − e·ỹ_{n−1} ≡ 0
mod 16 ⟺ L_n := 3ỹ_n − ỹ_{n−1} ≡ 0 mod 16 (3 a unit).
For odd n, the ν-definition at half-period gives
0 ≡ y_{n+d} − y_n = step0·2^{j−1}(c″ỹ_n − e″ỹ_{n−1}) mod Q =
step0·2^{j+3}, so c″ỹ_n − e″ỹ_{n−1} ≡ 0 mod 16 with c″ ≡ 9,
e″ ≡ 3 (r = j−1 ≥ 6), hence L_n ≡ 0 mod 16. ∎ In particular
L_1 ≡ 0 gives u ≡ 11t mod 16 — wave 44 derived this FROM DIV;
here both follow from ν. DIV at j = 7 is the wave-45 result,
now seen as the s = j−1 instance of one argument.

## 4. Consequences

- Wave-44 pinning (B1) Op⁽²⁾ ≡ φ + 2 (mod 4), (B2) Op⁽³⁾ ≡ φ
  (mod 4) is unconditional for j ≥ 7, j ≤ 2K: its only hypotheses
  were DIV and PAR, and its other inputs (Pell stabilisation
  mod 64, the 34-recurrence for Op_s) were already proved.
- The "modulo PAR" qualifiers on wave-45 DIV-j7 and mod-16 drop
  wherever they only fed the pinning. The mod-16 argument still
  uses ψ-analysis for its class/rep structure (§5).

## 5. Limits

- PAR as stated needs step0 integral (j ≤ 2K); all verified
  (m, p) satisfy this. If j > 2K the statement needs reformulating;
  no such point is encountered.
- Minimality of p is never used: DIV and PAR follow from the
  ν-definition alone, so they hold for every sequence with the
  half-period defect pattern, minimal or not.
- NOT settled: Gap G witness existence at j ≥ 11 (wave-45 mod-16
  §7: a sharing step-16 class with E_m ≡ −4δ_E mod 2^{j−6});
  ψ-analysis remains an input to the mod-16 argument.
- No Lean built, repository untouched.

## Checks

wave46_GapG_DIV_PAR_check.py (exit 0): valuations V1–V4 and
residues c ≡ 9, e ≡ 3, f ≡ 9 mod 16 exact for s = 1..12;
Cassini sign −1 for n = 1..200; P_n mod 4 period 4 for n ≤ 100;
divided-system enumeration at (128,128): exactly 8 solutions
mod 2048, 0 odd-quotient violations; DIV on 200 random PAR-style
sequences each at (1024,1024), (1024,512), (2048,1024):
0 DIV violations, 0 L_n violations (full k-range, all s).
