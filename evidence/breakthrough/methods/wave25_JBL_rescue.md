# Wave 25, task 3 — JBL rigidity, rescued (multi-class, up to invisible twists)

## Verdict

No single-class rescue exists (waves 23–24, confirmed here: at m=12
every one of 200 signature groups escapes a bare D-orbit, mostly via
Ann). The rescued lemma is multi-class and quotients by exactly three
kinds of invisible twist. It is verified exhaustively at m=12 and m=8
and proved at n=1. It does NOT by itself prove JBL (see §5).
Repository untouched; no Lean built.

## 1. Setup and the rescued lemma R**

R = Z[sqrt2], alpha = 3+2sqrt2, beta = alpha^t, t = gcd(m,4).
For genuine A mod D_m, B_r = A alpha^r, and the signature is
S(A) = (J^(q)_r(A))_{r mod t, q || D_m}, J^(q)_r = sorted multiset
over s of (Tr(B_r beta^s) mod q2, Tr(B_r beta^s) mod q).

**Lemma R** (rescued rigidity).** If genuine A, A' satisfy
J^(q)_r(A') = J^(q)_{pi(r)}(A) for all r and all odd q || D_m, one
pi in D_t, then for some j in Z, c in {id, conj}:
  A' = c(A) alpha^j + z + w   (mod D_m),
with z in Ann(D_m), w in Shadow(D_m) (defined in §3, §4).
General pi reduces to pi = id by transport (checked: S(A alpha)
is the permuted S(A); conjugation reflects similarly).

## 2. Ann: the trace-invisible additive twist

Ann_m(M) = {z mod M : Tr(z alpha^n) = 0 mod M for all n in Z/m}.
The vector entries are exactly those traces, so A and A+z give the
same vector and the same signature. Ann subsumes the wave-22 kernel:
(κ-1)w is trace-invisible for every w, so no separate κ is needed.
Exact values (brute-forced):
- m=12: Ann(128) = {(x,y): x = 0 mod 64, y = 0 mod 16} (16 elts),
  Ann(81) = {0}.
- m=8: Ann(512) = {(x,y): x = 0 mod 256, y = 0 mod 64} (16 elts),
  Ann(9) = {0}.

## 3. Shadow: the collapse-regime digit twist

In the collapse regime (p | m/P, so beta = 1 mod p), the odd data
sees one p-adic digit less than the parameter carries. At m=12,
q=81: A = 9 A_1, A_1 in R/9R, and the odd triple at class r is
(2a_r, 2a_r+3b_r, 2a_r+6b_r) mod 9 with (a_r,b_r) = A_1 alpha^r
mod 9. Shifting A_1 by 3D (D in R/3R) preserves every class triple:
b-shifts by 3k preserve triples exactly (3b, 6b mod 9 unchanged),
and a-shifts by 3e preserve the multiset whenever b_r != 0 mod 3
({0,3,6} is stable under +3e). Hence
  Shadow(81) = {27D mod 81 : D in R/3R} (9 values), 0 mod 128.
General form (one p-adic digit invisible in the collapse regime)
is conjectural, not proved. At q=9 (m=8, n=1) Shadow is trivial:
A mod 9 = 3 A_1 with A_1 mod 3, no digit to lose.

## 4. Verification (exact integers)

- m=12, modulus 128*81: 10368 genuine parameters, 200 signature
  groups. D-orbit + Ann alone: 168 groups contained, 32 escape.
  The escaping groups are exactly 144 = 48 x 3: orbit+Ann times an
  effective 3-element shadow quotient. D-orbit + Ann + Shadow:
  0/200 escape.
- m=8, modulus 512*9: 4608 genuine parameters, 288 groups.
  D-orbit + Ann alone: 0/288 escape (Shadow redundant there).
- n=1 (p=3, q=9): proved, not just checked (wave-24 N1):
  genuineness forces 3 | B, the odd data is the c-vector
  (6a', 6b', 3a', 3b'), which determines A mod 9, and transport
  (N1-B) carries the D-relation to every class. Ann(9) = {0},
  Shadow(9) trivial, so R** is exact there.

## 5. What this means for JBL (read carefully)

Every refutation so far exhibits pairs with IDENTICAL signatures
(pi = id works): they kill parameter recovery, never JBL's
conclusion, which is about signatures, not parameters. R** is the
correct rigidity statement, but JBL still needs one more step it
does not supply: a parameter relation derived from the GLOBAL
MULTISET hypothesis (Lucas-type argument, open), followed by
transport (automatic given the relation, N1-B pattern) -- or,
alternatively, direct pi-compatibility (common pi, G3/PC) plus
transport, with no parameter relation at all. R** fixes the
rigidity step's statement; it does not close JBL.

## 6. Remaining gaps

General proof of R** (collapse-digit mechanism beyond q=81;
common-pi coherence across moduli); the global-multiset-to-parameter
step or the direct compatibility route; Lean formalisation.

## Files

- This note: `methods/wave25_JBL_rescue.md`
- Checks: `methods/wave25_JBL_rescue_check.py` (round 1, bare orbit),
  `methods/wave25_JBL_rescue_check2.py` (round 2, + Ann),
  `methods/wave25_JBL_rescue_check3.py` (round 3, + Shadow)
