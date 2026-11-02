# Wave 27, task 2 — R30 gap condition: YES, exactly as in f=2

**Verdict: YES.** In R30's f=3, s=0 setting, the wave-25 transfer's
gap condition is correctly B_H = A^{|H₀|} real (mod p) with |H₀| ≥ 3,
exactly as in the f=2 case.

**One-line justification.** Every ingredient of the gap condition is
a mod-p statement — B_H mod p = a^{|H₀|} (a = A mod p), so gap ⟺
(ā/a)^{|H₀|} = 1, and |H₀| ≥ 3 ⟺ β̄² ≠ 1 mod p — hence lifting the
level from p² to p³ changes nothing about the condition itself.

**Why its use also lifts (the one level-sensitive step).** Gap
symmetry needs τ̄_A = τ_A β^r in R/p³. This follows from the mod-p
gap condition at any level, since reduction T₃ → (R/p)^× on
prime-to-p roots of unity is an isomorphism (injectivity: if
u ∈ T₃ reduces to 1 mod p, u = 1 + px gives u^m ≡ 1 mod p³ only for
u = 1 mod p³, as gcd(m, p) = 1). In R30's setting this applies to β
itself: s = 0 at f = 3 gives k = 3, i.e. α^{L₀} ≡ 1 mod p³, so
β = α^t satisfies β^m ≡ 1 mod p³ and β ∈ T₃.

**Exact check (script wave27_R30_gapcond_check.py).** At p = 5, 7, 13
(k = 1, 1, 2), t = 1, 2, 4, all with |H₀| ≥ 3 (L₀ = 6, 3, 14):
gap symmetry via τ_β, conj(τ_A) = τ_A τ_β^r mod p³, holds in all
2207 gap samples (bad_tau = 0 in every case; gap automatic when
|H₀| = p − ε, e.g. p = 5, t = 1 and p = 13, t = 1).
Caution, and the sharp boundary: the naive β-form
conj(τ_A) = τ_A β^r mod p³ FAILS at these k < 3 primes
(bad_beta = 127–342 per case), because there β ∉ T₃. So k = 3 is
load-bearing for the symmetry step, even though the gap condition
itself is level-independent. In R30's setting β = τ_β, and the f=2
form is literally correct.

**Scope.** Only the gap-condition adaptation is settled here. The
full f=3 transfer (in particular the second digit level) is NOT
proved. Repository untouched, no Lean built.
