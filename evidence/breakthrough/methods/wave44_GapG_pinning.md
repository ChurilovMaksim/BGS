# Wave 44, task 3 — Doubling-tower pinning (B1, B2) for Gap G: PROVED (j ≥ 7)

## Verdict

(B1) Op⁽²⁾ ≡ φ + 2 (mod 4) and (B2) Op⁽³⁾ ≡ φ (mod 4) hold for every
ν = (1,0) point of minimal period p = 2^j, j ≥ 7, modulo exactly two
named hypotheses (DIV, PAR below) — both verified exactly to m = 512
but unproved in general. The proof is recurrence + pinning: the
difference operators are affine in k (mod 4), and the pinning values
at k = 0, 1 are computed from Pell-coefficient residues that stabilize
from s = 4. No counterexample. (B1) is a j ≥ 7 statement: at j = 6,
Op⁽²⁾ = φ exactly (same shift 4, same divisor Q/4), so (B1) as stated
does not apply there; at j = 7, (B2) is trivial (Op⁽³⁾ = φ exactly).

## 0. Setup and hypotheses

Q = 8m², m = 2^K, p = 2^j minimal period, ν = (1,0), w_k = y_{2k+1},
k < p/4, w satisfying the 34-recurrence. φ_k = (w_{k+2^{j−4}} − w_k)/(Q/4)
mod 4; Op_s(k) = (w_{k+2^s} − w_k)/μ_s mod 4 with μ_s = Q/2^{j−2−s},
2 ≤ s ≤ j−4 (so Op_2 = Op⁽²⁾, Op_{j−4} = φ, Op_3 = Op⁽³⁾).

- (DIV) For every k and 2 ≤ s ≤ j−4, w_{k+2^s} − w_k ≡ 0 (mod μ_s).
  (The Lemma-2 family; verified to m = 512, general form open.)
- (PAR) Every ν = (1,0) point has y_0 = step0·t, y_1 = step0·u with
  step0 = Q/(8p), t odd, u integer. (Verified pattern to m = 512.)

Under DIV at (s, k) = (2, 0): w_4 − w_0 = 2³·step0·(171513u − 29427t)
is divisible by μ_2 = 128·step0, so 171513u − 29427t ≡ 0 (mod 16),
i.e. 9u ≡ 3t (mod 16), i.e. u ≡ 11t (mod 16). Write u = 11t + 16U.

## 1. Recurrence: D and E are affine (mod 4)

Differences of w satisfy the 34-recurrence, so for each fixed shift,
Op_s(k+1) ≡ 34·Op_s(k) − Op_s(k−1) ≡ 2·Op_s(k) − Op_s(k−1) (mod 4)
(division exact by DIV; reduction mod 4 valid since 4 | Q/μ_s for
s ≤ j−4). The same holds for φ. Hence D_k = Op_2(k) − φ_k and
E_k = Op_3(k) − φ_k satisfy D_{k+1} ≡ 2D_k − D_{k−1} (mod 4),
so D_k ≡ D_0 + k(D_1 − D_0) and E_k ≡ E_0 + k(E_1 − E_0) (mod 4).
It suffices to pin D_0 = D_1 = 2 and E_0 = E_1 = 0 (mod 4).
(Tower consistency, not needed below: Op_{s+1}(k) =
(Op_s(k) + Op_s(k+2^s))/2 exactly, by telescoping and μ_{s+1} = 2μ_s.)

## 2. Pell-coefficient stabilization (Lucas identities)

P_n: P_0 = 0, P_1 = 1, P_{n+1} = 6P_n − P_{n−1}; V_n = P_{n+1} − P_{n−1}.
Identities: P_{2n} = P_n·V_n, V_{2n} = V_n² − 2, P_{2n+1} = P_{n+1}² − P_n².
Put e_s = P_{2^s}/2^s, c_s = (P_{2^s+1} − 1)/2^s, w_s = V_{2^s}/2.

- v_2(V_{2^s}) = 1 for all s (V_1 = 6; V_{2n} = V_n² − 2 preserves
  v_2 = 1), so v_2(P_{2^s}) = s. w_{s+1} = 2w_s² − 1 and w_2 = 577 ≡ 1
  (mod 64) give w_s ≡ 1 (mod 64) for s ≥ 2; hence e_{s+1} = e_s·w_s
  gives e_s ≡ e_2 = 51 (mod 64) for s ≥ 2. In particular e_s ≡ 3 (mod 16).
- c_{s+1} = c_s·d_s − 2^{s−1}·e_s² exactly, where d_s = (P_{2^s+1}+1)/2
  = 2^{s−1}c_s + 1. Mod 64, with e_s ≡ 51 (e_s² ≡ 41): c_5 ≡ 25·9 − 8·41
  ≡ 25, c_6 ≡ 25·17 − 16 ≡ 25, c_7 ≡ 25·33 − 32 ≡ 25, and c_{s+1} ≡ c_s
  for s ≥ 7 (d_s ≡ 1, 2^{s−1} ≡ 0 mod 64). Base c_4 = 25 (direct:
  (P_{17}−1)/16 ≡ 25 mod 64). So c_s ≡ 25 (mod 64), i.e. C_1 := (c_s−9)/16
  ≡ 1 (mod 4), and C_2 := (e_s−3)/16 ≡ 3 (mod 4), for s ≥ 4.
  Hence 3C_1 − C_2 ≡ 0 (mod 4) for s ≥ 4.
- From P_{n+2} = 6P_{n+1} − P_n and P_{n+3} = 6P_{n+2} − P_{n+1} with
  n = 2^s: (P_{n+2}−6)/2^s = 6c_s − e_s ≡ 6·25 − 51 ≡ 35 (mod 64) and
  (P_{n+3}−35)/2^s = 6(6c_s−e_s) − c_s ≡ 6·35 − 25 ≡ 57 (mod 64),
  for s ≥ 4. The fixed s = 4 values agree: (P_{17}−1)/16 ≡ 25,
  P_{16}/16 ≡ 51, (P_{19}−35)/16 ≡ 57, (P_{18}−6)/16 ≡ 35 (mod 64).

## 3. Pinning at k = 0

Op_2(0) = (w_4 − w_0)/μ_2 = (171513u − 29427t)/16 (P_9−1 = 2³·171513,
P_8 = 2³·29427). With 171513 = 16·10719+9, 29427 = 16·1839+3 and
9u − 3t = 16(6t + 9U): Op_2(0) ≡ 3u − 3t + 6t + 9U ≡ U (mod 4)
(using u ≡ 3t mod 4).
φ_0 = (w_{2^{j−4}} − w_0)/μ_{j−4} = (c_1u − c_2t)/16 with c_1 ≡ 25,
c_2 ≡ 51 (mod 64) for j ≥ 7 (s = j−3 ≥ 4). Writing c_1 = 9+16C_1,
c_2 = 3+16C_2: φ_0 = C_1u − C_2t + 6t + 9U ≡ (3C_1 − C_2 + 2)t + U
≡ 2t + U (mod 4), since 3C_1 − C_2 ≡ 0 (mod 4).
Hence D_0 = Op_2(0) − φ_0 ≡ −2t ≡ 2 (mod 4) (t odd).
Op_3(0) = (w_8 − w_0)/μ_3 = (c'_1u − c'_2t)/16 with c'_1, c'_2 the s = 4
values (25, 51 mod 64), so E_0 = Op_3(0) − φ_0 = ((c'_1−c_1)u −
(c'_2−c_2)t)/16 ≡ 0 (mod 4) (numerator ≡ 0 mod 64).

## 4. Pinning at k = 1

Op_2(1) = (w_5 − w_1)/μ_2 = (5826393u − 999651t)/16 (P_{11}−35 =
2³·5826393, P_{10}−6 = 2³·999651; residues 9, 3 mod 16). So Op_2(1) ≡
u − 2t + 2t + U ≡ 3t + U (mod 4).
φ_1 = (w_{2^{j−4}+1} − w_1)/μ_{j−4} = (d_1u − d_2t)/16 with d_1 ≡ 57,
d_2 ≡ 35 (mod 64) (§2). Then d_1u − d_2t = 16(37t + 57U) + 64(·),
so φ_1 ≡ 37t + 57U ≡ t + U (mod 4).
Hence D_1 = Op_2(1) − φ_1 ≡ 2t ≡ 2 (mod 4).
Op_3(1) = (w_9 − w_1)/μ_3 = (f_1u − f_2t)/16 with f_1 = (P_{19}−35)/16
≡ 57, f_2 = (P_{18}−6)/16 ≡ 35 (mod 64), so E_1 = Op_3(1) − φ_1 =
((f_1−d_1)u − (f_2−d_2)t)/16 ≡ 0 (mod 4) (numerator ≡ 0 mod 64).

## 5. Assembly

D_0 ≡ D_1 ≡ 2 gives D_k ≡ 2 for all k (§1): (B1) Op⁽²⁾ ≡ φ + 2 (mod 4).
E_0 ≡ E_1 ≡ 0 gives E_k ≡ 0 for all k: (B2) Op⁽³⁾ ≡ φ (mod 4).
Both for every ν = (1,0) point of minimal period 2^j, j ≥ 7, modulo
(DIV) and (PAR). At j = 7, (B2) is the trivial identity Op_3 = φ;
the pinning above covers j ≥ 7 uniformly (s = j−3 ≥ 4).

## 6. Numerical verification

wave44_GapG_pinning_check.py (exit 0): for every ν = (1,0) point at
(m, p) = (128,128), (256,256), (256,128), (512,512), (512,256) —
32768, 131072, 32768, 524288, 131072 points — parametrisation holds
(y_0 = step0·t, t odd; y_1 = step0·u; u ≡ 11t mod 16), (B1) holds for
all k, (B2) holds for all k, the tower identity holds (mod 4) at
every level, and D_0 = D_1 = 2, E_0 = E_1 = 0 at every point:
B1bad = B2bad = towbad = D0bad = D1bad = E0bad = E1bad = 0 throughout.
The (512,256) run covered all 131072 points (below the 200000 cap).

## Limits

- (DIV) and (PAR) remain unproved in general (verified to m = 512);
  they are the only hypotheses. The divisibility lemma's general form
  and the mod-16 digit for t-agreement at j ≥ 9 (wave 43 §5) are
  untouched by this note.
- No Lean built, repository untouched.
