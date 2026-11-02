# Wave 28, task 3 — R** at m=36, q=243: HOLDS (with generalized shadow)

## Verdict

R** survives its first case beyond q=81 — but only with the shadow
generalized the right way. The naive 9-value analogue of the m=12
shadow fails on 64 groups; the shadow of all B-shifts divisible by
27 (81 values) covers all 520 groups. No counterexample to R** at
(36, 243). Repository untouched; no Lean built.

## Setup (exact integers)

m=36, t=gcd(36,4)=4, S=36/4=9, q2=128 (v2(D36)=7), q=243=3^5.
Collapse regime holds: beta=alpha^4=(91,165) mod 243, beta == 1 mod 3.
Genuine B mod M: (alpha^36-1)B == 0 mod M.
- Mod 128: delta=(64,88), 128 genuine (x == 0 mod 16, y == 0 mod 8).
- Mod 243: delta=(0,189), 729 genuine (x,y == 0 mod 9), i.e. B = 9C.
- Ann(128): 16 elements (same shape as m=12); Ann(243) = {0}.
- ord(alpha): 64 mod 128, 324 mod 243; joint period L=5184.
Pairs (A2, Aq) number 128 x 729 = 93312; every pair occurs as the
reduction of a genuine A mod D36, since 128*243 = 31104 divides
D36 (v2=7, v3=6) and genuineness splits over CRT components.
Signature: as in wave25 check3 — for each class r, sorted multiset
over s of (Tr(A2 alpha^r beta^s) mod 128, Tr(Aq alpha^r beta^s)
mod 243), same-s pairing; groups are identical-signature groups
(pi = id, general pi by transport as in wave25).

## Results

- Groups: 520 (sizes 16..1296, no singletons).
- D-orbit + Ann only: 64 / 520 groups escape.
- D-orbit + Ann + ShadowA = {27D mod 243 : D in R/3R} (9 values,
  the literal m=12 shape): still 64 / 520 escape. ShadowA covers
  some members (e.g. (9,36) = rep (9,9) + (0,27)) but every one of
  the 64 groups keeps an uncovered member.
- D-orbit + Ann + ShadowBig = {27D mod 243 : D in R/9R} (81 values,
  all B-shifts divisible by 27): 0 / 520 escape.

## Explicit witness

Group with rep ((0,0),(9,9)): member ((0,0),(9,117)) escapes
orbit+Ann+ShadowA — its diff (0,108) = 27*(0,4) needs 4 in Z/9,
outside the R/3R range — but is covered by ShadowBig.

## The uniform shadow rule (finding)

At m=12, Shadow(81) = {27D : D in R/3R} because q/27 = 3. At
m=36, q/27 = 9, so Shadow(243) = {27D : D in R/9R}. In C = B/9
terms both say the same thing: the odd data in the collapse
regime sees C only mod 3, so every C-shift by a multiple of 3
is invisible — i.e. every B-shift divisible by 27. The shadow
grows with q (9 values at q=81, 81 at q=243); the "one digit"
mechanism itself is q-independent.

## Scope (honest)

This tests the (128, 243)-component of R** only. The full
multi-modulus statement at m=36 (all odd q || D36: 3^6, 5^2, 7^2,
11^2, ...) is NOT tested here, and the general proof of R**
remains open. The shadow rule above is now confirmed at two
points (q=81, q=243), not proved in general.

## Files

- This note: `methods/wave28_JBL_Rstar_243.md`
- Script: `methods/wave28_JBL_Rstar_243.py` (exact integers, ~3 s)
