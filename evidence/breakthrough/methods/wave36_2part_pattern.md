# Wave 36, task 4 — the 2-part 5-per-level pattern: PROVED modulo three lemmas

## Verdict

The pattern holds at four levels by exact census, and its dynamics is
verified one step further. No counterexample exists through m = 256.

| level k | m | on-support split fibers | composition |
|---|---|---|---|
| 5 | 32 | 5 | 5 NEW (2-orbit: 32×3, 16×2) |
| 6 | 64 | 10 | 10 NEW (4-orbit: 128×3, 64×2; 2-orbit: 32×3, 16×2) |
| 7 | 128 | 15 | 5 OLD + 10 NEW, same NEW profile |
| 8 | 256 | 20 | 10 OLD + 10 NEW, same NEW profile |

**Theorem (dynamics).** Modulo Lemmas P, S, B below, the number of
on-support split fibers at level k is exactly 5(k−4) for all k ≥ 5.
The full m = 512 census is memory-infeasible here (2M × 512 int32);
the dynamics' m = 512 step is verified except the NEW count (see §6).

## 0. Setup

Level k: m = 2^k, q₂ = 2^{2k+3} (2-adic LTE). Kernel points are
m-periodic sequences mod q₂ satisfying y_{i+1} = 6y_i − y_{i−1};
a fiber is a set of kernel points with equal sorted multiset; a
split fiber contains ≥ 2 Γ-orbits (Γ = dihedral shifts + reversal);
on-support means all points satisfy the wave-16 torsion criterion.
Support is constant on fibers (mixed = 0 at every level censused).

## 1. Reduction theorem (proved)

**Theorem.** Level-k sequences are 2^{k−1}-periodic mod 2^{2k+1}.
Hence reduction ρ: Ker(k) → Ker(k−1), mod 2^{2k+1}, is a
Γ-equivariant homomorphism, 16-to-1 onto an image of size 2^{2k−1}.

*Proof.* Let w = (M^{2^{k−1}} − I)·seed. Then (M^{2^{k−1}} + I)w ≡ 0
mod 2^{2k+3}. Now det(M^{2^{k−1}} + I) = N(α^{2^{k−1}} + 1) = 4·odd
(since v_𝔭(α^{2^{k−1}} − 1) = 2k+1 > 2 = v_𝔭(2)), so w is divisible
by 2^{2k+1} as a vector, i.e. y_{i+2^{k−1}} ≡ y_i mod 2^{2k+1}. ∎
Verified: periodicity holds for all points at k = 7, 8; image size
8192 at k = 7 (131072/16), as predicted.

A level-k split fiber is NEW if all its orbits reduce to one
level-(k−1) orbit, OLD otherwise. A NEW fiber at k ≥ 6 is born from
a non-split orbit (its reduced orbit lies in no split fiber).

## 2. Lemma P — preimage of a fiber is a fiber (verified 45/45)

**Lemma P.** ρ^{−1}(F) is a single fiber for every split fiber F.
Verified for all split fibers at m = 64 (10), m = 128 (15), and
m = 256 (20): each preimage has exactly 1 distinct multiset, with
16·|F| points, as predicted by |ker ρ| = 16.

*Mechanism.* Write a lift as y'_i = y_{i mod 2^j} + 2^{2j+3}δ_i.
Then δ satisfies an inhomogeneous recurrence driven by y's defect,
with general solution δ_i = δ^part_i + A + B·i (mod 4): the
homogeneous equation has characteristic (x−1)² mod 4. Since
B·2^j ≡ 0 mod 4 (j ≥ 2), the second half of δ equals the first
mod 4, so the lift multiset is 2 × a first-half multiset. What
remains for a full proof is invariance of that first-half multiset
under (A, B) and across base points y ∈ F.

## 3. Type transformation (verified at every lift)

An orbit lifts to exactly 4 orbits, so a fiber of type (o, s)
= (orbit count, size) lifts to type (4o, 16s). Checked: (2,32) →
(8,512), (2,16) → (8,256), (4,128) → (16,2048), (4,64) →
(16,1024), (2,32) → (8,512) at m = 256, etc. — every OLD fiber
matches its source fiber's type under (o, s) ↦ (4o, 16s), and the
lift map on split fibers is bijective onto OLD fibers.

## 4. Lemma S — support rule (verified 45/45)

**Lemma S.** The preimage of an on-support split fiber F at level j
is on-support at level j+1 iff o(F) < 2^{j−4} (the max orbit count
at level j). I.e. exactly the max-orbit-count fibers fail to lift
supported; all others lift supported.

Verification: m = 32 → 64 (o = 2 = max: fail); m = 64 → 128
(o = 4 = max: fail; o = 2: lift); m = 128 → 256 (o = 8 = max:
fail; o = 4, 2: lift); m = 256 → 512 (o = 16 = max: fail;
o = 8, 4, 2: lift). Support sampled 8/8 vs 0/8 in every case.

*Mechanism.* The support defect d_z(y') = 2Q(z) − y'·z is
lift-independent: torsion sequences are affine in i mod 4
(z'_i = C + D·i), and the (A, B)-dependent sums Σ(C + D·i),
Σ i(C + D·i), Σ i²(C + D·i) over 2^{j+1} terms all vanish mod 4.
Observed defect values lie in {0, 2^{2j+4}} (e.g. at m = 128 the
failing lifts show [0, 65536] × 8 across the 16 torsion
conditions). The last open step is proving defect ≠ 0 ⟺ max orbit
count, i.e. identifying the mod-2 defect condition with the period
pattern of max-orbit fibers.

## 5. Lemma B — birth (verified at k = 6, 7, 8)

**Lemma B.** At each level k ≥ 6, exactly 10 NEW on-support split
fibers are born, with the fixed profile: 4-orbit (128×3, 64×2) and
2-orbit (32×3, 16×2). They are born from non-split orbits: the
preimage of such an orbit splits into 4 lifted orbits, two of which
collide in multiset. NEW fibers are short-period (period ≤ 32),
hence level-independent in size. The remaining step is a
classification of the primitive short-period patterns giving
exactly 10; the count is verified at three consecutive levels.

## 6. Counting: net +5 per level

A fiber born at level b with orbit count o₀ ∈ {2, 4} has orbit
count o₀·4^{k−b} at level k. By Lemma S it survives lifting from
level j to j+1 iff o₀·4^{j−b} < 2^{j−4}; the binding constraint
(j = k−1) gives lifespan k ≤ 2b−6 (o₀ = 4) or k ≤ 2b−5 (o₀ = 2).
Hence at each level k, exactly one 5-cohort expires (o₀ = 4 born at
(k+5)/2 if k odd, o₀ = 2 born at (k+4)/2 if k even), while 10 are
born: net +5. With T₅ = 5, T_k = 5(k−4) for all k ≥ 5. In
particular the number of max-orbit-count fibers is 5 at every
level (they are the lifts of the previous level's second-max
cohort, 5 per cohort by Lemma B).

**Prediction.** m = 512 (k = 9) has 25 on-support split fibers:
OLD = 15 verified via preimages (the 5 sixteen-orbit fibers fail,
the other 15 lift supported); NEW = 10 predicted by Lemma B (full
census not run: 2M × 512 int32 exceeds this VM's RAM).

## Files

- `wave36_2part.py` (census + reduction analysis; JSONs
  `wave36_2part_m{32,64,128,256}.json`)
- `wave36_match.py`, `wave36_match256.py` (OLD/NEW matching)
- `wave36_lift.py`, `wave36_preimage.py`, `wave36_preimage_all.py`,
  `wave36_preimage512.py` (lift/preimage/support checks)
- `wave36_image.py` (image/kernel size of ρ), `wave36_defect.py`
  (support-defect vectors)
- `wave36_2part_m256.log` (full m = 256 census output)

Repository untouched, no Lean built.
