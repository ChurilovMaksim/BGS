# Wave 31, task 2 — Why failing pairs have |sup| ∈ {0,4}

**Verdict: answered, not refuted.** No new failing 8-point pair exists:
in the full census the failing cpi pairs are 80 with |sup| = 0, 56 with
|sup| = 4, and exactly one with |sup| = 8 (group 594). The strict
statement "failing ⟹ |sup| ∈ {0,4}" is false (594), but the refined
statement holds, and the mechanism below explains *why* 8-point
transfer is a double coincidence while 4-point transfer is a single
condition. Notation as waves 29–30: y′ = τ(y) for the unique cpi τ,
w = Hy/D, δ = w′ − τ(w), Sm/Sp = {δ = ∓1}, tw = τ(w), d_r =
tw[m_r] − tw[p_r] per defect class r. All counts are exact integer
arithmetic on the wave-18 census (697 cpi pairs). Repository untouched,
no Lean built.

## 1. Quantization, proved: |sup| ∈ {0,4,8} for every cpi pair

**Per-class balance (theorem).** τ class-preserving ⟹ y′|_r is a
permutation of y|_r, so class sums Y_r are preserved. Class sums of w
telescope: Σ_{i∈r} w_i = (6Y_r − Y_{r−1} − Y_{r+1})/D, hence are
preserved too, and Σ_{i∈r} τ(w)_i = Σ_{i∈r} w_i. So Σ_{i∈r} δ_i = 0
for every class r (verified: dW = (0,0,0,0) on all 697 pairs).

**+6-antisymmetry (theorem, from the wave-30 CRT form).**
τ = CRT(id₄, refl₃) commutes with +6 and induces a reflection τ⁺ on
ℤ/6 (τ⁺(j±1) = τ⁺(j)∓1). Fold Py(k) = y_k + y_{k+6},
Pv(k) = w_k + w_{k+6} = (6Py(k) − Py(k−1) − Py(k+1))/D. Then
Py′ = Py ∘ τ, and H⁺ = 6I − C − Cᵀ is reversal-invariant, so it
commutes with τ⁺: Pv′ = Pv ∘ τ. Hence
δ_{j+6} + δ_j = Pv′(j) − Pv(τ(j)) = 0, i.e. **δ_{j+6} = −δ_j**
(verified 697/697; the δ = 0 pairs satisfy it trivially).

**Consequence.** Per class, δ sums to 0 with entries in {−1,0,1}
(verified 617/617 nonzero pairs), so each class triple is (0,0,0) or a
permutation of (−1,0,1): support 0 or 2 per class. Antisymmetry makes
the defect indicator 2-periodic (class r+2 = class r + 6), so
#defect classes ∈ {0,2,4} — never 1 or 3. Hence |sup| ∈ {0,4,8}, and
as a bonus Sp = Sm + 6 exactly, p_r = m_{r+2} + 6 (0 violations).

## 2. Failing ⟺ transfer (theorem, flow argument)

w′ = τ(w) + δ with δ ∈ {−1,0,1}. Let c_v = #{j∈Sm : tw_j = v},
e_v = #{j∈Sp : tw_j = v}. Histogram preservation is
c_v + e_v = c_{v+1} + e_{v−1} for all v, i.e. f_v := c_v − e_{v−1}
constant, hence 0 (finite support), i.e. c_v = e_{v−1} for all v,
i.e. **{tw on Sm} = {tw+1 on Sp}** as multisets. Since τ permutes w,
this is exactly sorted(w′) = sorted(w). Verified: transfer ⟺ failing
on all 697 pairs (137 true/true, 560 false/false).

## 3. Why 4-point transfer is generic (56/280 = 20%)

- The single rectangle's index-sum condition is *automatic* from the
  +6-pairing: p_r + p_{r+2} = (m_{r+2}+6) + (m_r+6) ≡ m_r + m_{r+2}.
- The parity-pair d-sum is locked at 2 (verified 280/280): joint
  (d_{r1}, d_{r2}) ∈ {(−2,4), (−1,3), (0,2), (1,1)} only.
- Crossed matching never occurs (0/280); transfer ⟺ aligned (1,1),
  which given the sum lock is a *single* condition d = 1, holding at
  the 20% base rate. The 4-point case is therefore one value
  coincidence, not a multiset coincidence.

## 4. Why 8-point transfer is a double coincidence (1/337)

- Transfer needs a full 4-vs-4 multiset match. The aligned route
  (1,1,1,1) **never occurs** (0/337).
- Per-rectangle transfer runs at only 3.0% (81/2696 rectangles), vs
  20% for the single rectangle at 4 points; both-transfer per
  decomposition is 2/1348 = 0.15%, i.e. ~0.6% per pair — and exactly
  one pair (594) achieves it. There is no cross-cancellation:
  global transfer ⟺ some decomposition both-transfers.
- Parity-pair d-sums are locked *equal* at (−4,−4), (2,2), (8,8)
  (205/92/40). Sum 4 is necessary but far from sufficient: 91
  non-failing pairs share it. Even the d-tuple does not determine
  transfer: 594's (0,0,2,2) also occurs in 17 non-failing pairs.
- 594's distinction: it is the unique pair with *two* both-transfer
  decompositions (rectangle sums (9,9) and (7,11)) — cross-class
  rectangle matching aligning twice.

So the asymmetry is condition-counting with teeth: 4-point transfer
is one aligned value condition (automatic position condition, locked
sum); 8-point transfer is either four simultaneous aligned values
(never observed) or a double rectangle coincidence (observed once).

## 5. What remains open (precise)

- The bound δ ∈ {−1,0,1} from Fix arithmetic: neighbor-sum spans
  within a class reach 1.66D, so it is nontrivial (verified 617/617).
- The parity-pair d-sum equality and its values {−4,2,8} — and why
  the 4-point defect-pair sum is always exactly 2: verified,
  mechanism open.
- Whether (1,1,1,1) is impossible at 8 points as a theorem or merely
  rare: 0/337 is consistent with rarity under condition-counting
  (~0.5 expected), not a proof of impossibility.
- Type II pairs (15 failing) need their own δ-analysis; general m is
  untouched (census is m = 12 only).

## Files

- This note: wave31_Wmod_sup.md
- Scripts: wave31_Wmod_sup_explore.py, _explore2.py (per-rectangle
  transfer), _explore3.py (τ-relations), _explore4.py (shift
  neighborhoods), _explore5.py (per-class structure),
  _explore6.py (aligned/crossed, rectangle sums), _explore7.py
  (joint d-distributions), _explore8.py ((1,1,1,1) absence),
  _explore9.py (+6-antisymmetry), _explore10.py (parity-pair sums).
