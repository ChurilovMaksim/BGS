# Wave 35, task 2 — Lemma F exponent identity: PROVED

**Verdict.** The missing written proof of Lemma F (wave 34, §4) is now
complete: the global exponent splits over CRT components exactly as
the code computes it, with the per-component scalar `v_q·u_q⁻²`
(`u_q = D/q`, `v_q = u_q⁻¹ mod q`). No counterexample exists; the
identity is verified exactly on 16,000 global samples at m = 8, 12.
Repository untouched, no Lean build.

## 0. Setup and statement

H = 6I − S − S⁻¹ (symmetric circulant), X = adj(H), HX = XH = DI,
D = det H = ∏ q over prime powers q ‖ D, pairwise coprime.
Fix_m = ker(H mod D); for ξ ∈ Fix_m, w_ξ = Hξ/D ∈ ℤ^m, and
[Vquot] = ℤ^m/Hℤ^m. Main's definition (wave 14):
  φ̂_s([w]) = (1/D)·Σ_{η∈Vquot} e((2s·Qnum(y) − pairNum(y,w))/D),
  pairNum(y,w) = yᵀXw, Qnum(y) = yᵀXy, e(t) = exp(2πit),
with y a representative of η. Per component q: K_q = ker(H mod q);
for κ ∈ K_q (integer lift), W = Hκ/q; Q_q[i] = W_iᵀXW_i mod q,
P_q[i,j] = W_iᵀXW_j mod q, T_q[i,j] = 2s·Q_q[i] − P_q[i,j] mod q.

**Lemma F (proved).** With u_q = D/q, v_q ≡ u_q⁻¹ (mod q),
  φ̂_s([w]) = (1/D)·∏_{q‖D} S_q[idx_q(w)],
  S_q[j] = Σ_{i∈K_q} ζ_q^{v_q·u_q⁻²·T_q[i,j]},
where idx_q(w) is the component of ξ mod q (ξ any lift of [w]).

## 1. Lemma 0 — index set and well-definedness (proved)

The map ξ′ ↦ [w_{ξ′}] = [Hξ′/D] is a bijection Fix_m → Vquot:
well-defined since ξ′ ↦ ξ′ + Dt changes Hξ′/D by Ht ∈ Hℤ^m;
injective since Hξ′/D ∈ Hℤ^m forces Hξ′ = DHt, hence ξ′ = Dt
(H nonsingular); bijective since |ker(H mod D)| = ∏ gcd(d_j,D)
= ∏ d_j = D = |ℤ^m/Hℤ^m| by SNF (d_j the invariant factors).
So the global sum is over ξ′ ∈ Fix_m. The summand depends only
on η: y ↦ y + Ht changes Qnum by D·(2tᵀy + Dtᵀt) and pairNum
by D·tᵀw, i.e. the exponent by an integer. ∎

## 2. Lemma A — lift relation (proved, exact integers)

Let ξ′ ∈ Fix_m, κ its integer lift mod q, W = Hκ/q. Then
  W + Ht₀ = u_q·w′   for some t₀ ∈ ℤ^m,
i.e. [W] = u_q·[w′] in Vquot (the wave-14 statement).
Proof: ξ′ ≡ κ (mod q), so ξ′ = κ + qt₀; then
Hξ′ = Hκ + qHt₀ = qW + qHt₀, while Hξ′ = Dw′ = qu_q·w′; cancel q. ∎

## 3. Lemma B — scaling (proved): T_q ≡ u_q²·t (mod q)

Let t = 2s·Qnum(w′) − pairNum(w′,w) (integers, global w-vectors).
Q,P mod q are invariant under W ↦ W + Ht: the change is
D·(2tᵀW + Dtᵀt) resp. D·(tᵀW′ + Wᵀt′ + Dtᵀt′), and q | D.
By Lemma A, W ≡ u_q·w′ (mod Hℤ^m), so
  Q_q[i] ≡ u_q²·Qnum(w′) (mod q),  P_q[i,j] ≡ u_q²·pairNum(w′,w),
hence T_q[i,j] ≡ u_q²·t (mod q). (Remark: Xw′ = ξ′ exactly, so
Qnum(w′) = ξ′·w′ and pairNum(w′,w) = ξ′·w.) ∎

## 4. Lemma C — CRT character identity (proved)

e(t/D) = ∏_q e(v_q·t_q/q), t_q = t mod q.
Proof: v_q·u_q ≡ 1 (mod q) and u_q ≡ 0 (mod q′) for q′ ≠ q
(since q′ | D/q), so Σ_q v_q·u_q ≡ 1 (mod q′) for every q′,
hence Σ_q v_q·u_q = 1 + kD. Dividing by D:
Σ_q v_q/q ≡ 1/D (mod 1); multiply by t and use t ≡ t_q (mod q). ∎

## 5. Theorem — factorisation (proved)

By Lemma C and Lemma B, for every ξ′:
  e(t(ξ′)/D) = ∏_q ζ_q^{v_q·u_q⁻²·T_q[idx_q(ξ′),idx_q(ξ)]}.
CRT gives Fix_m ≅ ∏_q K_q, and T_q depends only on the q-th
components, so the sum over ξ′ factorises:
  Σ_{ξ′} ∏_q (…) = ∏_q Σ_{i∈K_q} ζ_q^{v_q·u_q⁻²·T_q[i,idx_q(ξ)]}
  = ∏_q S_q[idx_q(ξ)].
Divide by D: this is Lemma F. ∎
Note: the code's scalar `ci·inv_u2` (waves 14/16) is exactly
v_q·u_q⁻²; the "u⁻² correction" is unconditional, not modal.

## 6. Why the code saw "raw" vs "corrected" components (explained)

Raw mode (T_q ≡ t) and corrected mode (u_q⁻²T_q ≡ t) coincide
iff (u_q²−1)·T_q ≡ 0 (mod q) for all occurring pairs. Exhaustive
component-pair check (all q² pairs, both s values):

| m | q | u_q² mod q | (u²−1)T ≡ 0 ∀ pairs? | code mode |
|---|---|---|---|---|
| 12 | 128 | 33 | yes | raw |
| 12 | 81 | 64 | yes | raw |
| 12 | 25 | 9 | no (480/625 fail) | corrected |
| 12 | 49 | 29 | yes | raw |
| 12 | 121 | 15 | no (13200/14641 fail) | corrected |
| 8 | 9 | 1 | yes (trivially) | raw |
| 8 | 289 | 256 | yes | raw |
| 8 | 512 | 145 | no (131072/262144 fail) | corrected |

The table matches waves 14/16 exactly. Global identity (a):
10,000/10,000 pairs at m = 12, 6,000/6,000 at m = 8, 0 failures.

## 7. Open micro-question (not needed for Lemma F)

Q_q, P_q, T_q are always divisible by p (the prime under q);
exact gcds with q: 4, 9, 5, 7, 11 at m = 12 (q = 128, 81, 25, 49,
121) and 3, 17, 8 at m = 8 (q = 9, 289, 512). The raw/corrected
split is exactly q | (u_q²−1)·gcd(T_q,q). A general proof of
the divisibility law (e.g. via the SNF of H_m) is not given
here; Lemma F does not depend on it.

## Files

- This note: wave35_LemmaF.md
- Exact check: wave35_LemmaF_check.py (ALL CHECKS PASS)
