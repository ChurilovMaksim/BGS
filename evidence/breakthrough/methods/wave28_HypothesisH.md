# Wave 28, task 5 — Hypothesis H: not proved; obstruction located exactly

## Verdict

H is **not proved**, and it is not provable by elementary methods:
H implies finiteness of prime values of the Lucas sequence w_p,
a well-known open problem (§5). What is proved here: a complete
H-check to m ≤ 1000 (§2), an at-most-one-large-prime-power lemma
(§3), and a prime-m reduction theorem (§4) that pins H's failure
mode exactly: H fails at prime p ≠ 3 whenever w_p is a prime
power. The conditional route via H (wave-27 Theorem B) is
therefore abandoned as a theorem; §6 names the alternative
Δ → 0 strategy. Repository untouched; no Lean built.

## 1. Cofactor reformulation (complete decision procedure, no factoring)

Write D_m = 2^a·S_m² (S_m odd; a = v₂(D_m): 2 if m odd,
2v₂(m)+3 if m even, wave-11 LTE). A prime power qt = p^{2f} ‖ D_m
has p^f ‖ S_m; write c = S_m/p^f. Then
qt > D_m/m² ⟺ 2^a·c² < m².
So a violation is exactly a prime-power divisor p^f of S_m with
small cofactor c (and p ∤ c) that is twin (3 ∤ ord_{p^{2f}}(β)).
H at m is therefore decidable by trial-dividing S_m by
c < m/2^{a/2} only — no factorisation of the huge S_m needed.
Twin test used: |G| = p^{2f-1}(p−ε), ε = (2/p), is the norm-1
group order in (Z/qt)[√2]; with G3 = |G| stripped of 3s,
3 | ord(β) ⟺ β^{G3} ≠ 1 mod qt. Script: wave28_H_check.py.

## 2. Computation: H fails at exactly 11 values of m ≤ 1000

Complete check to m ≤ 1000 (3.2 s; all S_m square-checked, a
checked against LTE). Violations, all with c = 1 (S_m itself
prime), all with twin sum exactly D_m/4:

| m | w_m (= S_m) | twin qt |
| 5 | 41 | 41² |
| 7 | 239 | 239² |
| 19 | 9369319 | 9369319² |
| 29 | 63018038201 | 63018038201² |
| 47 | 489133282872437279 | 489133282872437279² |
| 59 | 19175002942688032928599 | squared |
| 163 | 123426017006182806728593424683999798008235734137469123231828679 | squared |
| 257 | 118119373866262081485223899617886417593271902402645222441921910431040354300019446804767966058309121 | squared |
| 421 | 70393657629419512300176098237919643553997207020010109405976727793670773944409421814790772590069113145391735749901577009096149305609025491601824219052328961940201 | squared |
| 937 | (359 digits, see log) | squared |
| 947 | (363 digits, see log) | squared |

Primality: deterministic (< 2^64) for 5, 7, 19, 29, 47;
Baillie–PSW + independent 12-base Miller–Rabin for 59, 163, 257,
421, 937, 947 (no ECPP certificate). Lift check: β^p ≢ 1 mod q²
for 421, 937, 947, so ord_{q²}(β) = p·q (non-Wieferich).
**No partial domination anywhere ≤ 1000**: no violation with
1 < c < m/2^{a/2} occurs. Wider scan (c < m, m ≤ 300) finds only
four more prime-power divisors, none violating: m = 4 (3,
never twin), m = 6 (7, ord_49(β) = 21), m = 8 (17, twin but
289 ≪ D_8/64), m = 9 (199, 199² < D_9/81).
Instructive non-violation: m = 3 has w_3 = 7 prime, but
ord_49(β) = 21 is divisible by 3, so 49 is not twin and H
holds at m = 3. The twin condition is essential, not decorative.

## 3. Lemma (at most one large prime power — proved)

Call qt = p^{2f} ‖ D_m *large* if qt > D_m/m², i.e.
2^a·c² < m² for c = S_m/p^f. For m ≥ 3 there is at most one
large prime power. *Proof.* Two distinct large ones multiply to
> 2^a·S_m²/m² but divide S_m, forcing S_m < m²/2^a. This fails:
odd m: w_m ≥ 7·5^{(m−3)/2} ≥ m²/4 (recurrence
w_{m+2} = 6w_m − w_{m−2} ≥ 5w_m); even m = 2n: S_m =
y_n/2^{1+v₂(n)} ≥ 5^{n−1}/2^{v₂(n)} ≥ n²/(8·4^{v₂(n)}) =
m²/2^a (using y_n ≥ 2·5^{n−1} and v₂(y_n) = 1+v₂(n)). ∎
So H fails at m iff the unique large prime power (if any) is
twin; failure is all-or-nothing per m, never a sum of many
medium qt. (For prime m this is the whole story: the large
prime power is w_p itself, i.e. c = 1.)

## 4. Theorem (prime-m reduction — proved)

Let p ≠ 3 be prime, and suppose w_p = q^f with q ≠ 3. Then H
fails at m = p. *Proof.* D_p = 4w_p², so qt = q^{2f} = w_p² =
D_p/4 and qt ‖ D_p. Order lemma: if q | w_p then
ord_{q^e}(β) = p·q^s for some s ≥ 0, all e ≥ 1. Indeed
q | w_p gives x_p ≡ 1 mod q, hence (α^p−1)² ≡ 0 mod (q), so
α^p ≡ 1 mod 𝔮 for every 𝔮 | q; thus ord_𝔮(β) | p, and
β ≢ 1 mod 𝔮 (else 𝔮 | 32), so ord_𝔮(β) = p; the ring order is
p, and LTE lifting multiplies it by q at most once per level.
Hence 3 ∤ ord_{q^{2f}}(β) (3 ∤ p, q ≠ 3), so qt is twin, and
qt = D_p/4 > D_p/p² for p > 2. ∎
Escapes, both sharp: q = 3 never gives a twin (ord_9(β) = 6
divides ord_{3^e}(β)); p = 3 never violates (3 | p forces
3 | ord, as at m = 3 above).
**Corollary (hardness).** If H holds eventually, then w_p is
not a prime power (base ≠ 3) for all large primes p ≠ 3; in
particular prime values w_p occur only finitely often. That
finiteness is open — the same status as prime Fibonacci
numbers, unknown in either direction for any non-degenerate
Lucas sequence. So H cannot be proved without settling it.

## 5. Heuristic: H is expected to be false

Every prime divisor q of w_p (p > 3 prime) satisfies q ≥ 2p−1:
ord_𝔮(α) = p (as in §4, with α in place of β) gives
p | q − (2/q), and parity forces q ≥ 2p−1 in both the split
(q ≡ 1 mod p, q > p+1 even) and inert (q ≡ −1 mod p,
q ≠ p−1) cases. Verified exactly for all prime divisors of
w_p, p ≤ 47 (also ord_q(β) = p verified there). So w_p is
(2p−1)-rough, and by Buchstab/sieve heuristics
P(w_p prime) ≈ e^γ·ln(2p)/ln(w_p) ≈ ln(2p)/p.
Since Σ_{primes p} ln(2p)/p diverges (~ ln x), prime values
w_p — hence H-violations — are expected infinitely often.
Observed ≤ 1000: 12 prime values (incl. p = 3), 11 twin
violations, against heuristic expectation ≈ 8.5 — consistent.
Exhibiting a *proven* infinite violating family would settle
the prime-values problem, and is out of reach today; the
evidence above is the strongest available form of refutation.

## 6. Consequence for Δ → 0: alternative strategy named

H's failure does not by itself kill Δ → 0: at prime m = p
there is no 3-part (v₃(D_p) = 0, wave-24 LTE3), so conditional
on RB1' (contributing fibers contain a split 3-fiber) there are
no contributing fibers and Δ(p) = 0 — the dominating twin qt
is harmless for Δ. What H's failure kills is only the Twin
Sum Lemma as a standalone statement and the wave-27
Theorem-B route to it.
**Alternative strategy — 3-restricted twin sums:** prove Δ → 0
using twin sums only over m ≡ 0 mod 12 (where split 3-fibers
can exist), via the conditional lemma Δ(m) = 0 unless 12 | m
(no split 3-fiber ⟹ no contributing fiber, by RB1'), plus the
unconditional 2^k·t families (wave-27 Theorem A already covers
12·2^k·t). Remaining gaps, stated exactly: (i) prove 3-part 9
never splits on support (observed at m = 16, 20; splits seen
only at 81, 729); (ii) control twin qt at 12 | m with unbounded
odd part (primitive-part prime powers — the same flavour as H,
but on a thinner sequence). If (ii) fails, the fallback is
Δ → 0 along subsequences only (2^k·t and any family where
twin control holds), not the full limit.

## Files and limits

- Note: this file. Script: wave28_H_check.py; log:
  wave28_H_check_1000.log (full violation list with huge qt).
- Primality of the six large w_p is Baillie–PSW + independent
  MR, not ECPP-certified; all other claims are exact integer
  arithmetic. The order lemma's LTE lifting step is sketched
  (standard); the q = 3 and p = 3 escapes are exact.
- BGS repository untouched; no Lean built.
