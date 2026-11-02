# Wave 45, task 6 — F3 (uniform phase gap) for SCJ′ on the 9t line: PROVED
modulo two named lemmas

## Verdict

For the counted fiber-0 top-digit pair at 729, the phase gap is exactly
2π/3, proved from the structure of the phase sum — not just verified
numerically. The proof needs two named lemmas (H-quad, H-diff) about
the T-matrix; both are verified exactly at m = 180 and m = 252, and the
gap itself is verified at m = 36, 72, 144, 180, 252. The same argument
predicts gap 0 when ȳ_j ≡ 0 (mod 3), matching the phase-degenerate
fiber-1 pair at m = 252. Scope: m on the 9t line with 36 | m and
v₃(m) = 2 (so 729 ‖ D_m); the 36 ∤ m case is open.

## 1. Setup

q = 729. Kernel points K_q are parametrized by C ∈ 27R/729R, i.e. by
C̄ = (x̄, ȳ) ∈ (Z/27)² (bijection, verified: all C divisible by 27,
729 distinct C̄). Fiber-0 orbits have C̄ = (14, k), k ∈
{1,4,5,8,10,11,14,20,25} (same at all five m's); the counted pair is
k = 20 ↔ 11 (C ↦ C − 243√2, i.e. ȳ ↦ ȳ − 9), m-independent by wave-43
F4 §4. Phase of orbit j: S[j] = Σ_{i∈K} ζ^{ci·T[i,j]},
ζ = e^{2πi/729}, T = inv_u2·(2Q − P) mod 729, ci = (D/q)⁻¹ mod q.
Put F[i,j] = (ci·T[i,j]/27) mod 27 (needs 27 | ci·T[i,j], part of H-quad).

## 2. The two lemmas

(H-quad) F[i,j] is quadratic in (dx, dy) = C̄_i − C̄_j (mod 27):
  F = a·dx² + b·dy² + c·dx·dy + d·dx + e_j·dy + f_j,
with a ≢ 0 (mod 3), B := b − c²/(4a) ≢ 0 (mod 3), and the effective
dy-linear coefficient E := e_j − c·d/(2a) ≡ 0 (mod 3).
Verified exactly: m = 180, all 9 fiber-0 orbits, 0 mismatches, shared
(a,b,c,d) = (19,16,0,21), e_j ≡ 0, f_j ≡ 1 (mod 3); m = 252, k = 20,
unique solution (17,20,0,6,6,23). Note c = 0 at both m's.

(H-diff) For the top-digit pair (j, j′): T[i,j′] − T[i,j] = 243·ε·ȳ_i
(mod 729) for some ε = ±1. Verified: m = 180, all three pairs,
ε = +1, pointwise diffs {0,243,486} × 243 each; m = 252, fiber-0
ε = −1, fiber-1 ε = −1, same 243-counts.

## 3. Proof of the gap

Partition K by ȳ_i mod 3 (three classes of 243). Complete the square
in dx (a a unit mod 27): the inner sum over dx is a nonzero quadratic
Gauss sum G times ζ_{27}^{Q(dy)}, Q quadratic with leading coefficient
B ≢ 0 (mod 3) and linear coefficient E ≡ 0 (mod 3). Write dy = D + 3s
(D = r₀ − ȳ_j) and group s = 3t + u. The t-sum is Σ_t (ζ_3^{2BD})^t,
which is 0 unless 3 | D, i.e. unless the class is r ≡ ȳ_j (mod 3).
Hence S[j] is supported on the single class ȳ_i ≡ ȳ_j (mod 3).
For that class the remaining u-sum is 1 + ω^p + ω^q with
p + q ≡ 2B ≢ 0 (mod 3) (using 3 | D, 3 | E), hence nonzero — the only
vanishing triple 1 + ω + ω² is excluded. So S[j] ≠ 0.
On the supporting class, e_i = ε·ȳ_i ≡ ε·ȳ_j (mod 3) is constant,
so S[j′] = ω^{ci·ε·ȳ_j}·S[j]. Since ci is a unit mod 3, ε = ±1,
and the counted pair has ȳ_j = 20 ≡ 2 (mod 3), the ratio is a
primitive third root: gap exactly 2π/3. Then per counted fiber
Δ_F ≥ 2|O||O′|(1 − cos 2π/3) = 3|O||O′| (360/360 at m = 180 gives
388,800; 504/504 at m = 252 gives 762,048, as before).

## 4. Checks and discrimination

Gaps (absolute) for all three fiber-0 pairs, all exactly 2π/3, |S| = 27:
m = 36, 72, 144, 180, 252. Partial sums at m = 180: (20,11) supported
on e = 2, ratio ω; (10,1) on e = 1, ratio ω²; (14,5) on e = 2, ratio ω
— all matching ω^{ci·ε·ȳ_j} with ci ≡ 2, ε = +1. At m = 252, (20,11)
supported on e = 1, ratio ω², matching ci ≡ 2, ε = −1.
Fiber-1 pair at m = 252 (k = 15 ↔ 6): supported on e = 0, ratio 1,
gap 0 — exactly as the theorem predicts since ȳ_j = 15 ≡ 0 (mod 3).

## 5. What is NOT proved

H-quad and H-diff are not derived from the definitions of Q, P, W;
their proofs need the trace-formula computation of T[i,j] in terms of
(C̄_i, C̄_j) (the fitted coefficients are m-dependent, but only the
shape — c = 0, a,b ≢ 0, d,e ≡ 0 (mod 3) — is used). The 36 ∤ m case,
and the locked-component side (F2), are untouched. No Lean built;
repository untouched.

## Files

- This note: wave45_SCJprime_F3.md
- Scripts: wave45_F3_investigate.py (gaps at 5 m's), wave45_F3_partial.py
  (partial sums, e-tables), wave45_F3_multiset.py, wave45_F3_dist.py
  (F-distributions), wave45_F3_formula.py (mod-3 formula),
  wave45_F3_fit2.py, wave45_F3_fit3.py (m = 180 fits),
  wave45_F3_m252.py, wave45_F3_fit_modular.py (m = 252 fit).
