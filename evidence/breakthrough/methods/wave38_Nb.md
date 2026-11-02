# Wave 38, task 1 — The N(b) bound: polynomial iff Wieferich control

## 0. Setup

R = ℤ[√2], α = 3+2√2, p odd. d = ord_p(α), e = v_p(α^d − 1) ≥ 1,
b = e+1. N(b) = number of on-support split fibers at level b
(C ∈ R/p^b). The tower (waves 36–37, now fully proved: LT1+LT2 by
Full Blindness, LT3 formally) gives N(f) ≤ (f−e)·N(b) + N(e) for
f ≥ b; what remains for SC via the tower is N(b).

Remark (rational = 𝔭). d = ord_p(α) = ord_𝔭(α) and
e = v_p(α^d−1) = v_𝔭(α^d−1) by conjugation symmetry
(ᾱ = α^{−1}), so F2poly §0 transfers: d | m, p ∤ d,
f = e + v_p(m/d). Tower regime f ≥ b ⟺ v_p(m) = f−e ≥ 1 ⟺
p | m, hence p ≤ m, d ≤ m. Also N(b) depends only on p (d, e,
and the mod-p^e orbit count do): (147,7) and (21,7) both give 5;
(108,3) and (36,3) both give 1.

## 1. Count: N(b) ≤ 2p^{2e}/d

Level-b line analysis (wave 35 §f'=2 with p^e in place of p, via
Full Blindness): a level-b fiber is split ⟺ Z = ∅, with p orbits;
hence split fibers at level b ⟷ Γ-orbits mod p^e with Z = ∅,
one each. (Verified exactly below; the inequality below needs
only the "each split fiber gives a distinct Z=∅ orbit" direction,
from reduction-disjointness: distinct fibers have disjoint
reductions mod p^e, each containing a Z=∅ orbit.)

Theorem 1 (unconditional). N(b) ≤ 2p^{2e}/d.

*Proof.* R/p^e has p^{2e} classes. A unit class has shift-orbit
size exactly d: Cα^k = C ⟺ α^k ≡ 1 mod p^e ⟺ d | k, since
ord_{p^e}(α) = d (wave 37). Zero-divisor classes occur only for
split p, at most 2p^{2e−1} of them, each with shift-orbit size
≥ 3 (ord_𝔭(α) ≥ 3: α ≢ ±1 mod 𝔭 for odd p, as N(α∓1) = −4, 8).
Hence #orbits ≤ p^{2e}/d + 2p^{2e−1}/3 ≤ 2p^{2e}/d, using
d ≤ p+1. ∎

Verification (wave38_Nb_check.py, exact integer arithmetic):
#Γ-orbits mod p^e with Z=∅ equals N(b) exactly in all cases,
and Z=∅ is orbit-invariant (0 bad):

| p | d | e | N(b) | #orbits Z=∅ | 2p^{2e}/d |
| 3 | 4 | 1 | 1 | 1 | 4.5 |
| 5 | 6 | 1 | 2 | 2 | 8.3 |
| 7 | 3 | 1 | 5 | 5 | 32.7 |
| 13 | 14 | 2 | 546 | 546 | 4080.1 |
| 17 | 8 | 1 | 18 | 18 | 72.2 |

So the bound is sharp in shape (actual/bound ≈ 13–25%); the
slack is the Z=∅ density and Γ-orbits of size 2d vs the shift
count d. The exact equality suggests the bijection above is
sharp, but it is used here only as verified data, not proved.

## 2. Polynomiality ⟺ Wieferich control

In tower regime, N(b) ≤ 2p^{2e}/d ≤ 2m^{2e(p)} (p ≤ m).
Since e(p) depends only on p:

- Hypothesis W_E: e(p) ≤ E for all p ⟹ N(b) ≤ 2m^{2E}
  (polynomial, degree 2E). Generic case e = 1: N(b) ≤ 2m².
  Hypothesis W₂ (verified to 10⁵; only p = 13, 31 have e = 2):
  N(b) ≤ 2m⁴.
- Unconditional norm bound: p^e | (α^d−1) in R ⟹
  p^{2e} | N(α^d−1) in ℤ, so p^{2e} ≤ |N(α^d−1)| < 2α^d+2
  ≤ 2α^m+2, hence N(b) < (4α^m+4)/d — exponential in m.
  Unconditional methods give only exponential: polynomiality
  is genuinely equivalent to bounding e(p).
- No superpolynomial family can be exhibited: if e(p) ≤ E
  along a family, N(b) ≤ 2m^{2E}; so a superpolynomial
  family requires e(p) → ∞. No prime with e ≥ 3 is known
  (search to 10⁵), so exhibiting one is beyond current
  knowledge; conversely proving e(p) bounded is open
  (Wieferich-type problem for α). Heuristic: Σ_p 1/p²
  converges ⟹ e ≥ 3 expected only finitely often (possibly
  never); Σ_p 1/p diverges ⟹ e = 2 expected infinitely
  often. Plausible sharp conjecture: e(p) ≤ 2 for all but
  finitely many p ⟹ N(b) = O(m⁴) uniformly (finite
  exceptions contribute constants).

## 3. SC corollary

For any component, n_q ≤ (f−e+1)·2p^{2e}/d: tower for f ≥ b,
and for f ≤ e the same orbit count at level f gives
≤ 2p^{2f}/d ≤ 2p^{2e}/d. Under W_E, with s_q ≤ m² (wave 34)
and ω(D_m) < 2.54m, and f = e components split-free (the
outside-regime vanishing: wave 35 data + sketch, not proved):

  Σ_q n_q s_q² ≤ 2.54m·(log₂m+1)·2m^{2E}·m⁴ ≤ 5.08·m^{2E+6},

so SC(2E+7) for m ≥ 6; SC(11) under W₂ (data suggests SC(5)
— the tower route is lossy but conditional-proved).

## 4. Limits

Odd p only (Full Blindness scope); 2-part tower separate.
The bijection in §1 is wave 35/37's line analysis, verified
exactly in 5 cases but not re-proved here; the inequality
N(b) ≤ 2p^{2e}/d stands on reduction-disjointness alone.
No Lean; repository untouched.
