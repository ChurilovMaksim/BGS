# Wave 47, task 5 — SCJ′: F1 proved, F2a proved modulo locked period

## Verdict

**F1 is PROVED in general** on every 3-power line m = 3^e·t (3 ∤ t, 4 | m, e ≥ 2): the full 3-component 3^{2e+2} has a split fiber containing a top-digit triple of distinct orbits. **F2a (all-blind) is PROVED in general** on the same lines for every component q0 | D_{3^{e−1}t} with 3 ∤ q0, modulo one existence statement: a locked split component with v₃(period) ≤ 1. **F2b (non-split) stays OPEN** and is an L1-type statement; it is NOT needed for the γ = 1/3 section, since F4's proof (wave 43) uses no q0 non-split assumption. SCJ′ as an upper bound stays open; what closes here is its extremal-section side on all 3-power lines, not just 9t.

## 1. F1: setup

m = 3^e·t, 3 ∤ t, 4 | m, e ≥ 2. Then 4·3^e | m and LTE3 gives v₃(D_m) = 2e + 2, so 3^{2e+2} is the full 3-component. Kernel points there are exactly C ∈ 3^{e+1}R/3^{2e+2}R (wave 46: LTE3 + ν a unit mod 3). Write C = 3^{e+1}C′, C′ = x + y√2 ∈ R/3^{e+1}R, w_i = Tr(C′α^i) mod 3^{e+1}; the fiber is the sorted multiset of K_i = 3^{e+1}w_i. Top-digit move: C′ ↦ C′ − 3^e√2 (y ↦ y − 3^e).

## 2. F1: same fiber (triple invariance)

α^{12} ≡ 1 + 9√2 mod 27 (α^6 ≡ −1 + 9√2, square it), and by cubing induction α^{4·3^{e−1}} ≡ 1 + 3^e√2 mod 3^{e+1} for all e ≥ 2. Put s = 4·3^{e−1}, α^i = x_i + y_i√2. Then w_{i+s} = w_i + 3^e·L_i with L_i = xy_i + yx_i mod 3, and L_{i+s} = L_i. The period of w divides 4·3^e | m, so the fiber is copies of one 4·3^e multiset, partitioned into triples T_r = {w_r, w_r + 3^eL_r, w_r + 2·3^eL_r}, r mod s. Under y ↦ y − 3^e: L_r is unchanged mod 3, and w_r ↦ w_r − 3^e·4y_r. If L_r ≢ 0 mod 3, both triples are the full mod-3^e class above w_r mod 3^e. If L_r ≡ 0: the norm x_r² − 2y_r² ≡ 1 mod 3 forces y_r ≢ 0 ⟹ x_r ≡ 0 ⟹ L_r ≡ xy_r; since x ≢ 0 mod 3, L_r ≡ 0 ⟹ y_r ≡ 0 mod 3, so the constant triple is unmoved (3^e·4y_r ≡ 0 mod 3^{e+1}). Hence every triple is invariant as a set: the move preserves the fiber, for every C′ with x ≢ 0 mod 3.

## 3. F1: distinct orbits (split)

Γ acts by C′ ↦ C′α^k (rotation) and C′ ↦ C̄′ (reversal); both preserve the norm N = x² − 2y². But N(C′ − 3^e√2) − N(C′) = 4·3^e·y − 2·3^{2e} ≡ 4·3^e·y mod 3^{e+1}, nonzero iff y ≢ 0 mod 3. So for x, y ≢ 0 mod 3, {C′, C′ − 3^e√2, C′ − 2·3^e√2} are three distinct orbits in one fiber: a top-digit triple, in particular a top-digit pair. The counted pair (x = 14, k = 20 ↔ 11) is an instance.

## 4. F1: verification

e = 2 (729): at m = 36 and m = 252, all 324 C′ with x, y ≢ 0 mod 3 satisfy fiber-invariance (0 mismatches) and norm-distinction (0 collisions). The fiber of (14, 20) is EXACTLY those 324 points (full enumeration at m = 36: 17 fibers, largest 324), in 9 orbits of 36; the triple (20, 11, 2) verified as three distinct orbits (dihedral-orbit test), resolving wave 42's listing: its 9 reps are one per orbit. e = 3 (6561): at m = 108, all 2916 C′ with x, y ≢ 0 mod 3 satisfy both checks (0 mismatches, 0 collisions).

## 5. F2a: kernel equality (period divides 3^{e−1}t)

Let ζ = α^{3^{e−1}t}, δ = ζ + ζ̄ + 1 = 2A + 1 ∈ Z. Then D_m = D_{3^{e−1}t}·δ² (identity (2−2A)(2A+1)² = 2 − 8A³ + 6A, the m = 9t case of wave 39 §6). Claim: gcd(δ, D_{3^{e−1}t}) is a 3-power. Proof: a prime ideal 𝔭 dividing both δ and D = −(ζ−1)(ζ̄−1) divides ζ−1 or ζ̄−1; in the first case δ ≡ 3 mod 𝔭, in the second ζ ≡ 1 mod 𝔭 (from ζζ̄ = 1), so δ ≡ 3 mod 𝔭; hence 𝔭 | 3, so every rational prime divisor is 3. Now M^m − I = (M^{3^{e−1}t} − I)·K with K ∈ Z[M], det K = δ². If gcd(δ, q0) = 1, K is invertible mod q0, commutes with A = M^{3^{e−1}t} − I, and preserves ker A, hence ker(M^m − I) = ker A mod q0. So every kernel sequence at q0 | D_{3^{e−1}t} with 3 ∤ q0 has period dividing 3^{e−1}t, hence v₃(period) ≤ e − 1. Verified: gcd = 3 at t = 4, 8, 16, 20, 28, 40 and at base 36; kernel equality at m = 252 (q0 = 25, 121, 2401: equal; q0 = 81: |ker| 729 vs 81, FAILS, exactly as the 3-condition predicts) and at m = 108 (q0 = 25, 121, 49: equal; q0 = 81: 6561 vs 729, FAILS). The 81 failure is why the 3-part is never a blind component; split-ness is independent of it (2401 has kernel equality yet is split).

## 6. F2a: all-blind (top-digit law, re-derived)

Fiber criterion (wave 38 §1): o is blind iff b, b′ agree as multisets on every fiber I_v of i ↦ (a_i, o_i). Count lemma: with L = lcm(d_a, d_o), the count of i ∈ I_v with i ≡ r mod 4·3^e depends only on r mod gcd(L, 4·3^e) (CRT: i ≡ c mod L, i ≡ r mod 4·3^e solvable iff c ≡ r mod gcd, count m/lcm). If gcd(L, 4·3^e) | s = 4·3^{e−1}, the counts for r, r+s, r+2s are equal, so each s-triple contributes with equal multiplicity, and §2's triple invariance gives multiset equality. The divisibility holds iff v₃(L) ≤ e − 1, i.e. v₃(d_a) ≤ 1 and v₃(d_o) ≤ e − 1 (the 2-part of gcd divides 4 | s always). By §5, v₃(d_o) ≤ e − 1 for every nonzero o at q0 | D_{3^{e−1}t}, 3 ∤ q0. Hence: every such q0 is all-blind for the top-digit move, given a locked rep a with v₃(d_a) ≤ 1. This covers the 2-part of D_{3^{e−1}t} too (δ is odd, so gcd(δ, 2^e) = 1); no trace-nondegeneracy at 2 is used (blindness is proved via multisets only).

## 7. Locked period: data, existence still open

Observed locked reps: m = 180: 625, period 30 (v₃ = 0); m = 252: 2401, period 21 (v₃ = 1). Scan at m = 36, 72, 144 (wave47_locked_scan.py, exact dihedral canonical forms): at m = 36 NO split component besides 729 exists among D_36's components (25, 49, 121, 128, 5329, 32041, 38809, 39601 all 0 split fibers) — the section cannot start at m = 36. At m = 72 the only split small component is 512: 5 split fibers, reps period 8 (v₃ = 0). At m = 144 the only split small component is 2048: 10 split fibers, reps period 16/8 (v₃ = 0). So locked candidates exist at 72, 144, 180, 252 (and gcd(d_a, 36) = 4 > 1 at 72/144, so F4's criterion holds there too); general existence of a locked split component with v₃(period) ≤ 1 remains OPEN, and is now the only gap in F2a. Pattern so far: locked components are p^4 with p | t at 180/252 (5 | 20, 7 | 28) but 2-parts at 72/144; no locked period with v₃ ≥ 2 is known. Large components at 72/144 (1009², 1153², 577², …) were not scanned.

## 8. F2b (non-split): open, and not needed

Non-split at q0 means: value-multiset determines the kernel sequence up to Γ. That is an L1-type statement (value multiset determines a β-cycle, wave 45: open in general), now localized to the kernel line Ann(α^{3^{e−1}t} − 1) mod q0. It is NOT used by F4: wave 43's swap-free criterion proves o ↦ M(o) injective from (a, b)-class structure alone, with no q0 non-split assumption. So the γ = 1/3 section needs F2a + F3 + F4, not F2b. F2b remains as a standalone question; its failure would not break the section. Caveat: the m = 30 scaling reordering (wave 45) shows the naive L1 statement is false without the kernel-line structure.

## 9. Non-9t uniformity: what this changes

The extremal-section shape γ = 1/3 now rests on proved F1 + F2a (modulo locked period) on EVERY 3-power line e ≥ 2 with 4 | m, not just m = 9t; F3's gap argument is the same computation with scaled valuations (wave 46 §7 remark). If 4 ∤ m, then v₃(D_m) = 0 (LTE3): there is no 3-component at all, so the 3-adic joint mechanism is vacuous there; the dangerous 9t case is exactly 36 | m. v₃(m) = 1 lines (81-component): the move is mid-digit, and blind81 = 0 (wave 38 §4, pinning); no top-digit section arises there. v₃(m) = 0 lines: only the scaling mechanism is known (wave 38 §2, polynomial B(m) if locked periods are bounded); no observed threat to γ < 1. SCJ′ as an UPPER bound (no family exceeds D_m^γ) is still open in general: this wave characterizes the largest known sections, it does not bound all sections. The remaining SCJ′ list is: (i) the upper bound itself; (ii) locked-period existence (§7); (iii) F4's gcd(d_a, 36) = 1 regime, m = 108, and large odd components at 72/144 (wave 46 §3); (iv) F2b only if deemed necessary (§8).

## Files

- This note: wave47_SCJprime_F1F2.md
- Scripts: wave47_F1_check.py (F1 at m = 36, 252, 108), wave47_F2a_check.py (δ-gcd, kernel equality), wave47_locked_scan.py (locked candidates). No Lean built; repository untouched.
