# Wave 37, task 2 — Full Blindness: PROVED (odd p), in a stronger form

## Verdict

**Full Blindness is proved, unconditionally for odd p — and stronger
than stated:** for C with Z(C mod p) = ∅, the multiset M_f(C) is
described exactly as a union of full cosets, and depends only on
C mod p^e, not just mod p^b (b = e+1). The genuine part (LT1)+(LT2)
of the repaired Lift-Tower Lemma (wave 36 §5) is therefore proved;
what remains for SC via the tower is only the polynomial bound on
N(b) (Wieferich-type control of e, wave 36 §6).

## 1. Setup (wave 36 §5, wave 35 §f'=2)

R = ℤ[√2], α = 3+2√2, p odd. d = ord_p(α) in (R/pR)^×,
e = v_p(α^d − 1) ≥ 1, β = α^d = 1 + p^e·u with u ≢ 0 mod p.
By LTE, v_p(β^{p^k} − 1) = e + k, so ord_{p^f}(β) = p^{f−e} and
d_f := ord_{p^f}(α) = d·p^{f−e} for f ≥ e. For C ∈ R/p^f,
M_f(C) = multiset {Tr(Cα^j) mod p^f : 0 ≤ j < d_f},
B_{j0}(C) = Tr(Cα^{j0}u) mod p, Z(C mod p) = {j0 : B_{j0} = 0}.

## 2. Line Lemma (the whole proof)

**Lemma.** Let f ≥ e and C' ∈ R/p^f with Tr(C'u) ≢ 0 mod p. Then
{Tr(C'β^t) mod p^f : 0 ≤ t < p^{f−e}} equals the coset
Tr(C') + p^e·(ℤ/p^f), each element exactly once.

*Proof.* Write y(t) = Tr(C'β^t) = Σ_k C(t,k)·p^{ek}·T_k with
T_k = Tr(C'u^k) (binomial theorem in R/p^f). From
β^{t+m} = β^t·β^m,
  y(t+m) − y(t) = Σ_{i≥1} C(m,i)·p^{ei}·Tr(C'β^t·u^i).
Take m = p^s·r. The i = 1 term is p^{e+s}·r·Tr(C'β^t·u), and
Tr(C'β^t·u) ≡ Tr(C'u) mod p^e (β^t ≡ 1 mod p^e), hence a unit
mod p. For i ≥ 2, v_p(C(m,i)) ≥ s − v_p(i) (since
C(m,i) = m/i·C(m−1,i−1) is an integer), so the term has
valuation ≥ s − v_p(i) + ei ≥ e+s+1, using (i−1)e ≥ 1+v_p(i)
for i ≥ 2, e ≥ 1, p odd (i ≥ 2+v_p(i): direct for i = 2, 3,
v_p(i) ≤ i−2 for i ≥ 4). Thus
  y(t + p^s·r) ≡ y(t) + p^{e+s}·r·U (mod p^{e+s+1}), U a unit.
Induction on s (1 ≤ s ≤ f−e): y induces a bijection
ℤ/p^s → Tr(C') + p^e·ℤ/p^{e+s}. Base s = 1: y(t) ≡ Tr(C') +
p^e·Tr(C'u)·t (mod p^{e+1}), k ≥ 2 terms having valuation
≥ 2e ≥ e+1, and Tr(C'u) a unit gives the bijection. Step:
t ≡ t' mod p^s ⟹ y(t) ≡ y(t') mod p^{e+s} by the difference
formula; given a target mod p^{e+s+1}, its reduction mod
p^{e+s} has a unique preimage t_s, and the lifts t_s + p^s·r
hit every lift of y(t_s) exactly once by the formula. At
s = f−e this is the claim. ∎

## 3. Main theorem

**Theorem.** Let p be odd, f ≥ b = e+1, C ∈ R/p^f with
Z(C mod p) = ∅. Then
  M_f(C) = ⊔_{j0 ∈ ℤ/d} [Tr(Cα^{j0}) + p^e·(ℤ/p^f)]
(multiset union). In particular M_f(C) depends only on the
multiset {Tr(Cα^{j0}) mod p^e : j0}, hence only on C mod p^e,
and a fortiori only on C mod p^b.

*Proof.* Every j ∈ ℤ/d_f writes uniquely j = j0 + d·t with
j0 ∈ ℤ/d, t ∈ ℤ/p^{f−e}; α^j = α^{j0}·β^t. Apply the Line
Lemma to C' = Cα^{j0}: its hypothesis is Tr(C'u) = B_{j0}(C)
≢ 0 mod p, exactly Z = ∅. Union over j0 gives the formula;
each coset depends only on Tr(Cα^{j0}) mod p^e, and that
multiset depends only on C mod p^e. ∎

## 4. Remarks

- **Genuine is automatic:** Z = ∅ ⟹ C ≢ 0 mod p (else every
  B_{j0} ≡ 0), so wave 36's "genuine" qualifier is redundant.
- **Sharpness:** Z = ∅ is necessary, not just sufficient: if
  B_{j0} ≡ 0 mod p, the line is constant mod p^{e+1} (the
  formula gives y(t) ≡ Tr(C') mod p^{e+1}), while the full
  coset has p distinct residues mod p^{e+1}.
- **Corollary (Lift-Tower genuine part).** M_f(C) determines
  M_b(C) and vice versa: reducing M_f mod p^b gives
  p^{f−e−1} copies of M_b, and M_b determines
  {Tr(Cα^{j0}) mod p^e} by reduction mod p^e. Hence a genuine
  level-f fiber equals the full preimage of its level-b
  fiber, at most one per base fiber — (LT1)+(LT2) follow
  from the level-b line analysis (wave 35 §f'=2 with p^e in
  place of p: at level b, lines are full cosets iff
  B_{j0} ≠ 0, else constant, so split ⟷ Z = ∅, p orbits).
  With (LT3) already proved formally (wave 36 §4), the
  repaired Lift-Tower Lemma is now fully proved; only the
  N(b) bound (Wieferich-type control of e) remains for SC.

## 5. Verification (exact integer arithmetic, script below)

For each (p, f): 6 random Z = ∅ classes C; every line checked
against its coset; 3 random lifts C' ≡ C mod p^e each checked
to preserve M_f; one B = 0 class per C checked to collapse.

| (p, f) | d | e | d_f | lines OK | lifts OK | collapses |
|--------|---|---|-----|----------|----------|-----------|
| (3, 3) | 4 | 1 | 36 | 24 | 18 | 6 |
| (3, 4) | 4 | 1 | 108 | 24 | 18 | 6 |
| (5, 3) | 6 | 1 | 150 | 36 | 18 | 6 |
| (5, 4) | 6 | 1 | 750 | 36 | 18 | 6 |
| (7, 3) | 3 | 1 | 147 | 18 | 18 | 6 |
| (13, 4) | 14 | 2 | 2366 | 84 | 18 | 6 |
| (13, 5) | 14 | 2 | 30758 | 84 | 18 | 6 |
| (17, 3) | 8 | 1 | 2312 | 48 | 18 | 6 |

The e = 2 case (13, f = 4, 5) — the wave-36 untested regime —
holds exactly, as does (17, 3), where d_f = 2312 matches the
wave-35 fiber size at (816, 17⁴).

## 6. Scope

Odd p only: the valuation lemma (i−1)e ≥ 1+v_p(i) fails for
p = 2, e = 1 at i = 2, and LTE needs p odd; the 2-part tower
is separate in the program. No Lean formalisation; the
repository is untouched.

Script: [wave37_FullBlindness_check.py](wave37_FullBlindness_check.py) (ALL CHECKS PASS).
