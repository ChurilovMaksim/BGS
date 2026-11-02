# Wave 47, task 9 — F4 in general: gcd=1 vacuous at 360/1260, lcm<M and non-injective-a closed

## Verdict

All three open bullets of wave 43 §8 / wave 46 §5 are closed as
theorems (modulo the standing trace-representation sketch, same
status as wave-46 Lemmas A/B). (1) The gcd(d_a,36)=1 regime is
VACUOUS at m=360 and m=1260: every dangerous prime has full
component p², non-split by a general power-sum lemma that also
covers the large primitive prime 17934071, where enumeration is
infeasible. (2) The lcm(d_a,36)<M regime is a DICHOTOMY: F4
holds iff every blind period divides L, and fails otherwise
(shift-by-L is an explicit collision). (3) Non-injective a is
covered by generalized class lemmas, verified exactly at m=180
(15 values over 30-period) and m=252. What remains is only the
per-m checklist for general 9t-line m (§6) — no open regime.

## 1. Dangerous primes at 360 and 1260

m=360=2³·3²·5: divisors coprime to 36 are {1,5}; dangerous
prime: 41 (ord 5, primitive divisor of D_5=2²·41²).
m=1260=2²·3²·5·7: divisors coprime to 36 are {1,5,7,35};
D_35=2²·41²·71²·239²·17934071², primitive part
P_35=71²·17934071². Dangerous primes: 41 (r=5), 239 (r=7),
71 (r=35), 17934071 (r=35). All verified exactly:

| (m,p,r) | v_p(D_m) | p | m/r | det N mod p |
| (360,41,5) | 2 | 41 ∤ 72 | 10 ≠ 0 |
| (1260,41,5) | 2 | 41 ∤ 252 | 20 ≠ 0 |
| (1260,239,7) | 2 | 239 ∤ 180 | 177 ≠ 0 |
| (1260,71,35) | 2 | 71 ∤ 36 | 41 ≠ 0 |
| (1260,17934071,35) | 2 | 17934071 ∤ 36 | 8487645 ≠ 0 |

Here N=(M^m−I)/p mod p. ord_p(β)=r verified for all five
(17934071: β₁,β₂ both order 35, 35 | p−1). Since det N ≠ 0,
M^m−I=p·K with K invertible mod p, so ker mod p² = p·F_p²:
every kernel sequence mod p² is p×(mod-p sequence), of exact
period r (nonzero seeds: p ∤ D_d for d|r, d<r by Lemma B).
Hence splitness at p² ⟺ splitness of r-tuples mod p, exactly
as in wave 46 §3. 2- and 3-components cannot host gcd=1
periods (periods are powers of 2 resp. divisible by 4).

## 2. Power-sum lemma: no split r-tuples mod p (r odd, p ∤ 2r)

Lemma. Let p be prime, ord_p(β)=r odd, p ∤ 2r, and let
s_i=Aζ^i+Bζ^{−i} (i=0..r−1) be a nonzero trace sequence mod p
(ζ=β in F_{p²} or the split ring). If s′ has the same value
multiset as s, then s′ is dihedrally related to s.
Proof. Same multiset ⟹ same power sums. For k<r:
Σ_i ζ^{im}=r if r|m else 0, so p_2=Σs_i²=2r·AB (r odd kills
the ζ^{±2i} sums; 2r is a unit mod p) and p_r=r(A^r+B^r).
Thus (A′,B′) has A′B′=AB and A′^r+B′^r=A^r+B^r, so
{A′^r,B′^r}={A^r,B^r} (roots of X²−SX+(AB)^r). If A′^r=A^r
then A′/A∈μ_r=⟨ζ⟩ (r|p²−1, field), so A′=Aζ^t,
B′=Bζ^{−t} (rotation); if A′^r=B^r, swap first (reversal).
Zero cases (A=0 or B=0) check directly: AB=0 forces
(A′,B′) to be (0,Bζ^t) or (Bζ^t,0), both dihedral. ∎
Corollary. No split fibers mod p, hence none mod p² under
§1, for every dangerous prime — including 17934071, where
p²≈3.2×10¹⁴ seeds make enumeration infeasible. The lemma
also explains wave 46's 0-split results. It fails exactly
where p|r (the p-power split fibers at 81, 729, 2401), since
then r≡0 mod p kills the power sums.

## 3. Exact checks (enumerations + direct, confirming §2)

Mod-p split enumeration (wave-46 definition): (41,5):
1680 seeds, 188 fibers, 0 split; (239,7): 57120 seeds,
4199 fibers, 0 split; (71,35): 5040 seeds, 107 fibers,
0 split, largest fiber 70=2·35 (full dihedral orbit).
Direct mod-1681 checks (wave-46 script): (360,1681) and
(1260,1681): 1681 points each, all divisible by 41,
periods {1:1, 5:1680}, 189 fibers, 0 split.
Power-sum identities verified numerically at p=17934071
(3 random seeds): p_2=70·AB and p_35=35(A^35+B^35) exact,
rotations preserve the multiset.
Conclusion: no dangerous component at 360/1260 is split,
so none can serve as a locked component (locked requires
split). The gcd=1 regime is vacuous at both m.

## 4. Non-injective a: generalized class lemmas

Setup as wave 43 §5, but a arbitrary d_a-periodic (not
necessarily injective), L=lcm(d_a,36)=M. Let
A_i={s mod d_a : a_{i+s}=a_i} (injective ⟺ A_i={0}) and
g=gcd(d_a,36), r=i mod 36. Since b_j=b_i ⟺ j≡i or
j≡1−i (mod 36) (wave 43 §4), CRT gives:
Lemma (classes). class(i)={i} plus, iff ∃s∈A_i with
s≡1−2r (mod g), exactly one partner (the mod-M CRT
solution); no other members. So classes are singletons
or pairs, and non-singleton ⟺ the residue condition.
(H-dist′). No distance-1 partner exists unless r≡0
(mod 18) and a_{i+1}=a_i; distance-2 partners never
exist (2≡1−2r mod 36 impossible: even vs odd). So
(H-dist) ⟺ no adjacent a-collision at i≡0 mod 18.
(H-sep′). For j non-singleton, j−1/j−2 singleton ⟺
no s′∈A_{j−1} with s′≡3−2r_j (mod g) and no
s″∈A_{j−2} with s″≡5−2r_j (mod g).
Theorem. (H-dist′)+(H-sep′) ⟹ F4, by the wave-43 §3
proof unchanged (j−1,j−2 are singleton positions π
fixes, then the local rigidity lemma forces õ=o).
Verification. m=180 (a=C(0,550) mod 625, period 30,
15 values): 180 classes, all singletons; pair
criterion exact (pred 0 = actual 0); (H-dist′) 0
failures — vacuity reproduced. m=252 (a=C(0,2107)
mod 2401, period 21, injective): 210 classes =
168 singletons + 42 doubles; pair criterion exact
(pred 84 = actual 84); doubles all ≡2 mod 3; min
cross-pair distance 3; (H-dist′)/(H-sep′) 0 failures
— wave-43 §6 reproduced as a special case.

## 5. lcm(d_a,36)<M: dichotomy

Let L=lcm(d_a,36)<M. Since (a,b) is L-periodic, the
shift σ_L preserves (a,b)-classes setwise, so for any
blind o, M(o∘σ_L)=M(o) (reindex j=i+L). If some blind
o has period ∤ L, then o∘σ_L≠o is a genuine F4
collision: F4 FAILS. If every blind period divides L,
then o and õ are L-periodic, configs over M are
(M/L)-fold repeats of L-configs, and F4(M) ⟺ F4(L),
where §4 applies with M replaced by L (lcm=L by
definition). Demo (synthetic M=72, d_a=12, L=36,
b=actual 36-pattern, o=5-periodic mod-41 seed (1,0)):
o∘σ_36≠o (36≡1 mod 5) but M(o∘σ_36)=M(o); a
36-periodic o′ satisfies o′∘σ_36=o′. No observed
section has L<M (180: L=180; 252: L=252).

## 6. What remains of F4

- General 9t-line m: the gcd=1 regime is vacuous
  whenever every dangerous prime p (primitive divisor
  of D_r, r|m, gcd(r,36)=1) satisfies v_p(D_m)=2,
  p∤m/r, det N≠0 — a finite per-m checklist, run here
  for 360/1260. If some v_p(D_m)>2, the p^f
  zero-divisor case analysis of §2 is open (the
  lemma's division step needs A a unit).
- lcm<M sections: F4(L) at level L still needs the
  §4 criterion checked for the actual locked a (no
  L<M section observed yet).
- Standing hypotheses (unchanged status): trace
  representation s_i=Tr(Cβ^i) (wave-46 Lemma A
  sketch); b's pairing σ(r)=1−r for the 729 fiber-0
  b (verified at 180/252, m-independent pattern).
- No Lean built; repository untouched.

Scripts: wave47_F4_danger.py, wave47_F4_split.py,
wave47_F4_general.py (class checks + lcm demo).
