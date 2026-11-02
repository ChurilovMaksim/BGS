# Wave 24, task 1 — JBL n=1 case: closed modulo restricted rigidity

## Verdict

The n=1 case is **handled**: JBL follows from restricted rigidity
(n≥2 primes + pattern lemma) plus the two lemmas below. This is not
a standalone proof of JBL — restricted rigidity itself remains open
— but the n=1 prime no longer imposes any extra obstruction.
Repository untouched; no Lean built.

## 1. The n=1 situation (recap, wave 23)

n = 1 ⟺ p = 3, L₀ = 4, t = 4, q = 9, occurring iff 4 | m, 3 ∤ m.
Here β = α⁴ ≡ 1 + 3√2 (mod 9), hence β^s ≡ 1 + 3s√2 (mod 9),
since (3√2)² = 18 ≡ 0 (mod 9). Note α⁴ ≢ 1 (mod 9): the naive
"shift by α⁴ does nothing" intuition is false, and the lemmas
below succeed only because genuineness kills the correction.

## 2. Lemma N1-A — structure (proved, checked)

α^m − 1 ≡ 3(m/4)√2 (mod 9). The Fix condition (α^m−1)B ≡ 0
(mod 9) therefore forces 3 | B (both components) for every class
parameter B: brute-forced over all 81 residues mod 9 at
m = 4, 8, 20, 28 (m = 12 excluded: there 3 | m, so p = 3 is not
in the n=1 situation at all).

For genuine B, Tr(Bβ^s) ≡ 2Re(B) (mod 9), constant in s:
indeed B(1+3s√2) has trace 2x + 12sy ≡ 2x (mod 9) when 3 | y.
Hence the q = 9 joint data at class r is

  J^{(9)}_r(A) = {(p, c_r(A)) : p ∈ P_r(A)},
  c_r(A) = Tr(Aα^{r+4s}) ≡ 2Re(Aα^r) (mod 9), any s,

where P_r(A) is the pattern multiset mod q₂. So J^{(9)} sees a
class parameter only through (P_r, Re mod 9); the √2-coefficient
mod 9 is invisible to it. Explicitly, for genuine
A ≡ 3(a′+b′√2) (mod 9):
(c_0, c_1, c_2, c_3) = (6a′, 6b′, 3a′, 3b′) (mod 9).

Sharpness: both the collapse and the transport below FAIL for
non-genuine parameters (Tr varies as 2x + 3sy; the α^{4q}
correction 3qy survives mod 9). Genuineness is essential, and it
comes free from the Fix condition — it is not an extra hypothesis.

## 3. Lemma N1-B — transport (proved, checked)

For genuine A, A′ and j ∈ ℤ, with indices mod 4:

  A′ ≡ Aα^j (mod 9)  ⟹  c′_r = c_{r+j} for all r;
  A′ ≡ Āα^j (mod 9)  ⟹  c′_r = c_{−(r+j)} for all r.

Proof: Re(Āα^{r+j}) = Re(conj(Aα^{−(r+j)})) = Re(Aα^{−(r+j)}),
using conj(α) = α^{−1} and Re(conj C) = Re(C); the α^{4q}
discrepancy between α^{r+j} and α^{(r+j) mod 4} contributes
3qy ≡ 0 (mod 9) by genuineness. The same formulas hold for P_r
mod q₂ (Tr(conj C) = Tr(C); pattern lemma). Hence an exact
D-relation mod q₂·9 yields π(r) = ±r + j ∈ D₄ matching J^{(9)}_r.

## 4. Slack interface (wave 22)

The corrected rigidity's trace-kernel slack is mod 2^a ONLY:
the wave-22 examples have A′ ≡ κA (mod 2^a) but A′ ≡ A
(mod odd part) — reproduced here for m = 6 (identical vector
[70,210,1190,6930,1190,210] mod 39200 from A = 35 and A′ = 19635;
A′ = 17A mod 32, A′ = A mod 1225). Hence at mod 9 the relation
delivered by restricted rigidity is exact, and N1-B applies with
no κ correction. The slack cannot break the n=1 transport.

## 5. Theorem — n=1 closed modulo restricted rigidity

Assume restricted rigidity (n≥2 primes + pattern lemma) delivers
a single D-relation A′ ≡ Aα^j or Āα^j (mod D_m, up to
trace-kernel units mod 2^a), with π(r) = ±r + j matching all
other joint data. Then π also matches J^{(9)}_r for all r, by
N1-A, N1-B, and §4. So the n=1 prime never forces a different π,
and JBL follows from restricted rigidity plus N1. Remaining gaps
are exactly the old ones: n≥2 rigidity (including p | m/P),
G1 at f≥3, general PC, Lean formalisation.

## 6. Why the wave-23 counterexample does not break JBL

B, B′ at m = 8 share (P, c): B ≡ B′ ≡ 16√2 (mod 512),
Re(B) ≡ Re(B′) ≡ 3 (mod 9), B ≡ B′ ≡ 0 (mod 289), so their
joint data are equal, [(0,6),(0,6)], and JBL's conclusion holds
with π = id at every modulus. Per-class rigidity (B′ D-related
to B mod 9) is strictly stronger than JBL; the n=1 case is
exactly where the two come apart, and N1-A explains why: J^{(9)}
cannot see the √2-coefficient mod 9, so equal joint data
without D-relation is the expected behaviour, not a pathology.

## Files

- This note: `methods/wave24_JBL_n1.md`
- Check script: `methods/wave24_JBL_n1_check.py` (8 groups, all pass;
  the two first-run failures were non-genuine parameters and are
  documented as sharpness in §2)
