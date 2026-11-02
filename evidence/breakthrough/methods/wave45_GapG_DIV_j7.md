# Wave 45, task 4 — Divisibility lemma (DIV) for Gap G at j=7: PROVED (mod PAR)

## Verdict

(DIV) holds for every ν=(1,0) point of minimal period p=128, modulo the
parametrisation hypothesis (PAR) of wave 44. At j=7 the range is s∈{2,3}
only, so (DIV) is exactly: w_{k+4}−w_k ≡ 0 (mod Q/8) and
w_{k+8}−w_k ≡ 0 (mod Q/4) for all k, where w_k=y_{2k+1}, Q=8m².
Since w_{k+4}−w_k=y_{n+8}−y_n and w_{k+8}−w_k=y_{n+16}−y_n with n=2k+1
odd, both follow from one mod-16 lemma about the reduced sequence.

## Setup

y satisfies y_{i+1}=6y_i−y_{i−1} mod Q, ν=(1,0) means
y_{i+64}−y_i=(Q/2)·ν_{i mod 2} (Q/2 for even i, 0 for odd i).
(PAR): y_0=step0·t, y_1=step0·u with step0=Q/(8·128)=Q/1024, so every
y_n=step0·ỹ_n and ỹ satisfies the same recurrence mod 1024.
Minimality of p=128 enters only through the definition of ν.

## Lemma 1 (Pell shift identity)

y_{n+d}−y_n=(P_{d+1}−1)·y_n−P_d·y_{n−1}, where P_n is the Pell sequence
(P_0=0, P_1=1, P_{n+1}=6P_n−P_{n−1}), so y_n=P_n·y_1−P_{n−1}·y_0.
Proof: both sides satisfy the same recurrence in n; at n=0 the right
side is (P_{d+1}−1−6P_d)y_0+P_d·y_1=−P_{d−1}y_0+P_d·y_1=y_d, and at
n=1 it is y_{d+1}−y_1. ∎

Residues (wave 44 §2, by Lucas identities; mod 16 in brackets):
P_8=8·29427 [3], P_9−1=8·171513 [9];
P_16/16≡51 [3], (P_17−1)/16≡25 [9] (mod 64);
P_64/64≡51 [3], (P_65−1)/64≡25 [9] (mod 64).

## Lemma 2 (the mod-16 quantity is 2-periodic)

L_n:=3ỹ_n−ỹ_{n−1} (mod 16) satisfies L_{n+2}≡L_n.
Proof: ỹ_{n+1}=6ỹ_n−ỹ_{n−1}, ỹ_{n+2}=35ỹ_n−6ỹ_{n−1}, so
L_{n+2}=3ỹ_{n+2}−ỹ_{n+1}=99ỹ_n−17ỹ_{n−1}≡3ỹ_n−ỹ_{n−1}=L_n. ∎

## Lemma 3 (ν forces L_n=0 for odd n)

For odd n, ν=0, so Lemma 1 with d=64 gives
0≡y_{n+64}−y_n=64·step0·(c′ỹ_n−e′ỹ_{n−1}) (mod Q=1024·step0),
hence c′ỹ_n−e′ỹ_{n−1}≡0 (mod 16). With c′≡9, e′≡3 (mod 16) this is
3L_n≡0, so L_n≡0 (mod 16) since 3 is a unit mod 16. In particular
L_1=3u−t≡0, i.e. u≡11t (mod 16) — the relation wave 44 derived from
(DIV) is in fact its source at j=7. (For even n the same computation
gives L_n≡8, which is not needed here.)

## Theorem (DIV at j=7)

Let n=2k+1 be odd. By Lemma 1 with d=8:
y_{n+8}−y_n=8·step0·(171513ỹ_n−29427ỹ_{n−1}); (DIV, s=2) needs this
≡0 (mod Q/8=128·step0), i.e. 171513ỹ_n−29427ỹ_{n−1}≡0 (mod 16),
which is 9ỹ_n−3ỹ_{n−1}=3L_n≡0 by Lemma 3. ∎
By Lemma 1 with d=16:
y_{n+16}−y_n=16·step0·(c″ỹ_n−e″ỹ_{n−1}); (DIV, s=3) needs this
≡0 (mod Q/4=256·step0), i.e. c″ỹ_n−e″ỹ_{n−1}≡0 (mod 16),
which is again 9ỹ_n−3ỹ_{n−1}=3L_n≡0 by Lemma 3. ∎
Hence Op_2 and Op_3=φ are well-defined at j=7, and the wave-44 pinning
(B1), (B2) at j=7 no longer needs (DIV) as a hypothesis.

## Verification

wave45_DIV_j7_check.py (exit 0): at (m,p)=(128,128) and (256,128),
all 32,768 ν=(1,0) minimal-period points each: PAR true,
u≡11t (mod 16) true, L_n≡0 for all odd n (0 violations), DIV s=2
and s=3 exact (0 violations).

## Limits

- Modulo (PAR) only: (PAR) itself remains unproved in general
  (verified to m=512). The proof uses nothing else — no minimality
  beyond the ν definition, no m-specific computation.
- General j untouched: the shift identity generalises, but the
  mod-16 reduction above is shaped by d=64, 8, 16 at j=7.
- No Lean built, repository untouched.
