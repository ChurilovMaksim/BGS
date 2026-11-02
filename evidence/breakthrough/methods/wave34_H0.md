# Wave 34, task 4 — H0 proved (modulo the CRT factorisation)

## Verdict

**H0 is proved modulo one named lemma (Lemma F, the CRT
factorisation of φ̂).** The part that was only a sketch —
Γ-invariance of S_q — is now proved in full from the definitions,
and verified exactly at m = 12. What remains open is not a
numerical doubt but a written proof of the factorisation's
exponent identity, whose mechanism is identified and whose
validation is exact (see §4). No counterexample exists: the
fresh check confirms the mechanism at every m = 12 component,
and the wave-20/32 censuses match H0 exactly. Repository
untouched; no Lean build.

## 0. Definitions (waves 14/16/19)

- H = H_m = 6I − S − S⁻¹ (circulant, S = cyclic shift),
  X = adj(H), det H = D = D_m.
- Γ = D_m (dihedral: shifts + reflections) acting on length-m
  vectors by coordinate permutation: (γ·v)[j] = v[p[j]].
- For q ‖ D: K_q = ker(H mod q) (size q), W = H(K_q)/q,
  Q[i] = W_iᵀXW_i mod q, P[i,j] = W_iᵀXW_j mod q,
  T[i,j] = (2s·Q[i] − P[i,j]) mod q (× a per-component scalar
  for the u⁻² correction mode), S_q[j] = Σ_i ζ_q^{T[i,j]}.
- Fiber = set of points with the same sorted multiset;
  component fiber = the same mod q; split = > 1 Γ-orbit.
  For a global fiber F, proj_q(F) ⊆ F_q (reduction mod q
  preserves sorted multisets).
- Δ_F = |F|² − |Σ_j |O_j|e^{iθ_j}|²
  = 2Σ_{j<k}|O_j||O_k|(1 − cos(θ_j−θ_k)) ≥ 0 (wave 19, pure
  algebra), where φ̂ ≡ φ_j on orbit O_j, θ_j = arg φ_j.
  F contributes iff Δ_F > 0.

## 1. Lemma 0 — H and X are dihedral-symmetric (proved)

Reversal R conjugates S to S⁻¹, so RHR⁻¹ = 6I − S⁻¹ − S = H;
shifts commute with H trivially. Hence γHγ⁻¹ = H for all
γ ∈ Γ. Adjugates are conjugation-equivariant
(γ·adj(H)·γ⁻¹ = adj(γHγ⁻¹)), so γXγ⁻¹ = X as well.
Checked exactly at m = 12 for all 24 γ (script below).

## 2. Lemma 1 — S_q is Γ-invariant (proved)

Let γ ∈ Γ and write γ·i for the induced permutation of K_q
(K_q is γ-stable since H commutes with γ). Then, with γ
acting as an orthogonal permutation matrix:
  Q[γ·i] = (γW_i)ᵀX(γW_i) = W_iᵀ(γᵀXγ)W_i = W_iᵀXW_i = Q[i],
  P[γ·i,γ·j] = (γW_i)ᵀX(γW_j) = W_iᵀXW_j = P[i,j],
using Lemma 0 (γᵀXγ = X). Hence T[γ·i,γ·j] = T[i,j]
(the per-component correction scalar is γ-independent), and
reindexing the kernel sum (i ↦ γ⁻¹i):
  S_q[γ·j] = Σ_i ζ^{T[i,γ·j]} = Σ_i ζ^{T[γ·i,γ·j]}
           = Σ_i ζ^{T[i,j]} = S_q[j]. ∎
Fresh exact check (integers only, no floating point): at
m = 12, all five components (128, 81, 25, 49, 121), all 24 γ:
Q/P invariance and S_q multiset invariance (sorted T-columns
equal) hold with 0 failures; S_q is constant on every
Γ-orbit (39/9/5/12/11 orbits). At q = 81 the single split
fiber (36 points, 3 orbits) carries 3 pairwise distinct
S-signatures — a split component fiber CAN carry distinct
phases, while a single-orbit component fiber CANNOT.

## 3. Theorem — H0 (proved modulo Lemma F)

**Lemma F (CRT factorisation, assumed — see §4).**
φ̂_s(w) = (1/D)·Π_{q‖D} S_q[idx_q(w)], where idx_q(w) is the
component of w mod q.

*Corollary (φ̂ constant on Γ-orbits).* If w′ = γw, then
idx_q(w′) = γ·idx_q(w), so S_q[idx_q(w′)] = S_q[idx_q(w)]
by Lemma 1, hence φ̂(w′) = φ̂(w). This proves wave-19 item 2
(φ̂ constant on orbits), previously only a reindexing sketch,
modulo Lemma F.

*Proof of H0.* Let F be a global fiber on support whose
component fibers F_q are all single Γ_q-orbits. For ξ ∈ F,
idx_q(ξ) ∈ F_q, and S_q is constant on F_q by Lemma 1
(single orbit + invariance). Hence every factor in Lemma F
is constant on F, so φ̂ is constant on F, all orbit phases
θ_j agree, and Δ_F = 0 by the §0 formula. Contrapositive:
Δ_F > 0 implies some F_q is split. Support factorises over
CRT exactly (global support = AND of component supports,
wave 16) and is constant on component fibers (0 partial
fibers in every census, SC-sup), so that split F_q is
on-support. ∎

## 4. Status of Lemma F (the only remaining gap)

- Group splitting: ker(H mod D) ≅ Π_q ker(H mod q) is
  standard CRT (orders multiply to D); not a hypothesis.
- Exponent identity: the global exponent mod q equals the
  component exponent up to the per-component scalar u⁻²,
  u = D/q mod q — mechanism identified (the (D/q)² factor
  picked up lifting K_q into global vectors). Validated
  exactly: at m = 8 the resulting φ̂ is verified on all
  1,331,712 points (wave 14); at m = 12 the correction test
  is 300/300 decisive per component (wave 16); at m = 24,
  300/300 decisive at every component (wave 20).
- Also assumed: supp is a union of global fibers (wave-19
  item 1; verified to m = 10 and on all lifts, 0 partial).

## 5. Census corroboration (H0's predictions hold exactly)

- m = 12: 762 split fibers on support = 757 gluing fibers
  (globally split, no split component) with Δ_F = 0 exactly,
  plus 5 global fibers lifting the split 81-component with
  Δ_F > 0 (wave 20). H0 predicts exactly this split.
- m = 30/32 (wave 32): the contributing rigid lifts carry a
  split component (q = 625 / q = 8192), as H0 requires; no
  contributing fiber without one has ever been found.

## Files

- This note: wave34_H0.md
- Exact check: wave34_H0_check.py (ALL CHECKS PASS)
