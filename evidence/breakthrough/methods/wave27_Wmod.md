# Wave 27, task 5 — The W-mod lemma: statement, equivalence, dead routes

## 1. Precise statement

Let m = 12, D = D₁₂ = 1536796800, H = H₁₂, and y ∈ Fix₁₂ with
w = Hy/D ∈ ℤ¹². For a failing (fiber, w)-class — two distinct
Γ-orbits in one split fiber sharing sorted(w) (152 such classes,
wave 25 §4) — with partners y, y′ and w, w′:

**W-mod lemma.** W_d(w′) − W_d(w) is divisible by D for every
d = 0..11, where W_d = Σᵢ wᵢwᵢ₊d.

Since |W_d| ≤ 12·25 = 300 (wᵢ ∈ [−1, 5] on census reps), D | ΔW_d
forces ΔW_d = 0 exactly. Numerically the lemma is TRUE on all 152
classes (ΔW_d = 0, 0 violations); it is NOT proved. What follows
pins down exactly what it is equivalent to, why the natural proofs
fail, and what would suffice.

## 2. Theorem (proved): W-, S-, A-constancy are one phenomenon

Let X = adj(H), first row x, and X_circ the circulant with row x.
Then, exactly (verified on census data, §6):

  S⁽ᵈ⁾ = Σ_e x_{e−d} W_e,   A_d = Σ_e R_{d−e} W_e,

where S⁽ᵈ⁾ = Σᵢ yᵢwᵢ₊d, A_d = Σᵢ yᵢyᵢ₊d, and R is the
autocorrelation of x. In matrix form S = X_circ·W and
A = X_circ²·W. The eigenvalues of X_circ are D/λ_j with
λ_j = 6 − 2cos(2πj/12) ∈ {4, 6±√3, 5, 6, 7, 8}, all nonzero; so
X_circ (hence X_circ²) is invertible over ℚ(√3). Therefore, for
any set of partners:

  ΔW = 0  ⟺  ΔS = 0  ⟺  ΔA = 0.

So the W-mod lemma is EQUIVALENT to S⁽ᵈ⁾-constancy (and to
A_d-constancy) on failing classes — not a separate lemma. The
wave-25 §5 reduction (W ⇒ S, A) is one direction; the converse
holds too. The remaining open sub-lemma is exactly: S⁽ᵈ⁾ is
constant on failing classes (equivalently W_d, equivalently A_d).

## 3. Dead routes (exact computation)

(a) **w-side component-wise dihedrality fails everywhere.** y′ IS
component-wise dihedral in y (0 failures, 152 pairs × 5 prime
powers q ‖ D — this also validates the dihedral convention). But
w′ is a dihedral image of w mod q in 0/152 pairs at EVERY q ∈
{128, 81, 25, 49, 121} (760/760 failures), and w′ is a global
dihedral image of w in 0/152 classes. Hence the mod-D lemma
(wave 25 §2) cannot be applied to W_d via w.

(b) **Mod-(D/q) strengthening fails everywhere.** w′ ≡ γw
(mod D/q) fails 152/152 at every q. So no (D/q) | ΔW_d route
exists either (and (D/q) | ΔW_d for all q would have given
D | ΔW_d, since lcm{D/q} = D).

(c) **Broad version is FALSE.** On all 762 split groups, 2806 of
9264 (pair, d) W_d-diffs are NOT divisible by D, in 269 groups.
So the lemma is genuinely restricted to the S-constant groups
(see §4); it is not a fiber law.

(d) **Swamping: no y-polynomial argument can work.** The
dihedral-invariant polynomial f⁺(y) = yᵀS_d y with
S_d = (T⁻ᵈ+Tᵈ)H² satisfies f⁺(y) = 2D²W_d(y) exactly. The mod-D
lemma gives D | f⁺(y′) − f⁺(y) = 2D²ΔW_d — automatic, since
q | D for every q ‖ D. To extract D | ΔW_d one would need
D³ | f⁺(y′) − f⁺(y), i.e. agreement of y′ with γy at mod-q³
level, which gluing pairs do not have. The Taylor expansion
confirms the obstruction is structural: with y′ = γ_q y + qz_q,
the cross term is 2D²K_q, i.e. the q-adic valuation is already
saturated by the D² present in f⁺.

(e) **Kernel arguments are vacuous here.** X = 13860·X₀ with
X₀-row [19601, 3363, 577, 99, 17, 3, 1, 3, 17, 99, 577, 3363]
(exact; hence every Fix₁₂ vector is divisible by
13860 = 2²·3²·5·7·11). Since p | 13860 for every p | D,
ker(X mod p) is the whole space (dim 12, all p). The kernel
condition X(w′ − γ_q w) ≡ 0 (mod q) is automatic from y-gluing
and constrains nothing: e = w′ − γ_q w has generic entries
(|e| ≤ 6, gcd mostly 1, e ≡ 0 mod 2 in only 1585/8268 cases).

## 4. Refined empirical law + sufficient target

Cross-tab over all 762 split groups (per group: S⁽⁰⁾-const,
all-S⁽ᵈ⁾-const, all-W_d-const):

  (True, True, True) → 493 groups (152 failing + 341 pw_ok);
  (False, False, False) → 269 groups (264 S-varying + 5 non-gluing);
  no mixed cases; 0 groups violate Sall ⟺ W_const (theorem §2).

So empirically S⁽⁰⁾-constancy already implies all-S⁽ᵈ⁾- and
W_d-constancy on split groups. And by smallness, the W-mod
lemma would follow from ΔW_d ≡ 0 (mod M) for ANY integer
M > 600 — e.g. M = 10368 = 128·81. That is the concrete target
for any future proof: two prime powers' worth of divisibility,
not the full D, would suffice.

## 5. Verdict

The W-mod lemma (failing classes) is TRUE numerically but
UNPROVED; it is equivalent to S⁽ᵈ⁾-constancy on failing classes
(§2), its broad version is refuted (§3c), and every modular
route via y or w is dead (§3a,b,d,e). The precise remaining
gap is one statement: S⁽ᵈ⁾(y′, w′) = S⁽ᵈ⁾(y, w) for all d on
failing-class partners — equivalently ΔW_d = 0, equivalently
ΔA_d = 0. No counterexample exists on failing classes; a
counterexample to any broader statement is in §3c.

## Files

- This note: wave27_Wmod.md
- Scripts: wave27_Wmod.py (component-wise dihedrality + divisibility),
  wave27_Wmod_check2.py (broad version, mod-(D/q), tau structure),
  wave27_Wmod_check3.py (gluing maps, adjugate, kernels),
  wave27_Wmod_check4.py (S-formula validation, cross-tab).
  Repository untouched; no Lean built.
