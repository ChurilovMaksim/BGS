# Wave 46, task 5 — SCJ′ F4, gcd=1 regime: VACUOUS at 36/72/108/144/180/252

## Verdict

The gcd(d_a, 36) = 1 regime of wave 43 §8 is vacuous at every
9t-line value checked (36, 72, 108, 144, 180, 252). At
36/72/108/144 this is pure arithmetic — no component can host a
gcd=1 period at all. At 180/252 there is exactly one dangerous
prime each (41, 239), and its full component is provably
non-split (0 split fibers, verified twice: mod-p reduction and
direct mod-p² enumeration). No example in the regime exists at
these m, so F4 does not reopen. Vacuity in general (m with a
coprime-to-6 part > 1) is NOT proved — see §5.

## 1. The criterion: a gcd=1 period forces a dangerous prime

D_m = |det(M^m − I)|, M = [[6,−1],[1,0]], β = 3+2√2. Verified:
D_3 = 196, D_4 = 1152, D_5 = 6724, D_6 = 39200, D_7 = 228484,
D_36 and D_84 factorizations reproduced exactly, D_180 has 138
digits, D_252 has 193 digits.

Lemma A (period ⇒ divisor of D_d). Let s be a nonzero kernel
sequence mod p^f (p odd) of length m with exact period d | m.
Then p | D_d. Proof sketch: s_i = Tr(C β^i) (recurrence +
integrality; disc = 32 is a unit mod p). Write s = p^e·s′ with
s′ nonzero mod p^{f−e}; period(s′) = d. Its reduction mod p is
nonzero of period d″ | d, so ker(M^{d″} − I) mod p is
nontrivial, p | D_{d″}, and D_{d″} | D_d since d″ | d
(β^{d″} − 1 | β^d − 1 in Z[√2], take norms).

Lemma B. p | D_d ⟺ ord_p(β) | d (det(M^d − I) ≡ 0 mod p ⟺
β^d = 1 in Z[√2]/(p); β − β^{−1} = 4√2 is a unit mod p).

Corollary. A gcd(d, 36) = 1 period at an odd component of D_m
forces an odd prime p | D_m with ord_p(β) | m and
gcd(ord_p(β), 36) = 1. Such primes are exactly the primitive
prime divisors of D_r for r | m, gcd(r, 36) = 1, r > 1.

2-component: M's order mod 2^e is a power of 2 (M mod 2 has
order 2; the kernel of GL_2(Z/2^e) → GL_2(Z/2) is a 2-group),
so periods are powers of 2; period 1 means a constant sequence
whose fiber is a singleton, never split. 3-component:
ord_3(β) = 4 exactly (β^4 ≡ 1 mod 3, β^2 ≡ 2 ≢ 1), so 4 | d.
Neither can host a gcd=1 split rep.

## 2. Case table

| m | form | divisors of m coprime to 36 | dangerous prime | outcome |
| 36 | 2²·3² | {1} | none | vacuous by arithmetic |
| 72 | 2³·3² | {1} | none | vacuous by arithmetic |
| 108 | 2²·3³ | {1} | none | vacuous by arithmetic |
| 144 | 2⁴·3² | {1} | none | vacuous by arithmetic |
| 180 | 2²·3²·5 | {1,5} | 41 (ord 5) | 1681 non-split (§3) |
| 252 | 2²·3²·7 | {1,7} | 239 (ord 7) | 57121 non-split (§3) |

## 3. The two dangerous components: non-split, twice verified

Orders exact: β^5 ≡ 1 mod 41 with √2-coeffs of β^1..β^4 =
2, 12, 29, 39 (all ≠ 0); β^7 ≡ 1 mod 239 with coeffs
2, 12, 70, 169, 227, 237 (all ≠ 0). Valuations exact:
v_41(D_180) = 2, v_239(D_252) = 2, so 1681 and 57121 are the
full components. Reduction: M^m = (M^r)^{m/r} ≡ I + (m/r)·p·N
mod p², p ∤ m/r (41, 239 ∤ 36); |ker| = p^{v_p(D_m)} = p²
forces N invertible, so ker mod p² = p·(seeds mod p): every
nonzero kernel sequence mod p² is p × a nonzero mod-p
sequence, of period exactly r, and splitness at p² ⟺
splitness of r-tuples mod p.

Mod-p enumeration (seeds (y0, y1), r-tuples, dihedral
canonical forms): p = 41: 1680 nonzero seeds, 188 fibers,
0 split, largest fiber size 10 = 2·5 (full dihedral orbit).
p = 239: 57120 nonzero seeds, 4199 fibers, 0 split, largest
size 14 = 2·7.

Direct mod-p² verification (wave-38 kernel_points +
period-reduction canonical forms): (180, 1681): 1681 points,
all divisible by 41, periods {1: 1, 5: 1680}, 189 fibers,
0 split. (252, 57121): 57121 points, all divisible by 239,
periods {1: 1, 7: 57120}, 4200 fibers, 0 split — reproduces
wave 42's row exactly (57121 seeds, 4200 fibers, 4199
multi-fibers, split 0). Since the only dangerous primes'
components are non-split, they cannot serve as locked
components either (locked requires split).

## 4. Factorizations closing the wave-44 caveats

D_m = 8·(v′)² for even m (β^{m/2} = u′ + v′√2), so factoring
reduced to the square root (27/41/54 digits); sympy
factorint, product-checked. All odd primes occur squared.

D_72 = 2^9·3^6·5²·7²·11²·17²·73²·179²·197²·199²·1009²·
1153²·1523089². The three "untested" large components are
confirmed as full components, plus 8 further odd ones — and
none matters: arithmetic vacuity (§2).

D_144 = 2^11·3^6·5²·7²·11²·17²·73²·97²·179²·197²·199²·
577²·1009²·1153²·13729²·63073²·1255393²·1523089²·29827009².
The "unfactored cofactor" is now fully factored.

D_108 = 2^7·3^8·5²·7²·11²·53²·73²·107²·179²·197²·199²·
72577²·146449²·2585953²·7761799². Full 3-component 3^8 =
6561 (v_3 = 2·3+2 = 8, 3-adic LTE). The 729-based section
does not apply as stated at m = 108 (it needs restatement
with 6561 as free), but the gcd=1 question is settled
regardless: divisors coprime to 36 are {1} only.

## 5. What remains open

- General 9t-line m with coprime-to-6 part r > 1 (e.g. 360,
  1260): dangerous primes are the primitive divisors of D_{r′}
  for r′ | r; each needs its own split check. No general
  vacuity theorem is claimed.
- Wave 43 §8's other open bullets, untouched: lcm(d_a, 36) < M
  (classes of size > 2), and non-injective a with doubles.
- Lemmas A/B are proof sketches (trace representation over
  Z/p^f, Smith-normal-form counting), not Lean. No Lean
  built; repository untouched.

Scripts: wave46_F4_gcd1_Dm.py, wave46_F4_gcd1_split.py,
wave46_F4_gcd1_direct.py, wave46_F4_gcd1_factor.py,
wave46_F4_gcd1_direct252.log.
