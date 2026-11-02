# Wave 14, task 1 — G1 at f=3 (v_p(D_m)=6): case split by (k,s)

**Verdict.** No counterexample at f=3 anywhere tested. (1,2) is verified
exhaustively at two cases and reduced to one scalar lemma; (2,1) is
proved modulo f=2 s=0, with the mechanism checked; (3,0) does not occur
for any p ≤ 10000. G1 at f=3 is therefore not fully proved: the exact
remainders are the scalar S\* = 0 for (1,2) and the f=2 s=0 real-case
gap. Repository untouched, no Lean built. Citations: wave-12 G1 lift
(Lemmas 1–5), wave-13 f=2 proof (s=0 resultant, s=1 digits, Lemma A).

## 0. Setup

p odd, f=3, P=p³, R=Z[√2], α=3+2√2, γ=α^{L₀}=1+pᵏu, s=3−k,
L₀ = order of α mod p, u purely imaginary mod p (Lemma A: ū≡−β^{L₀}u,
β^{L₀}≡1 mod p, so Tr(u)≡0). G1′: arbitrary recurrence sequences mod
p³ with equal global multiset have D_t-related per-class multisets.

## 1. Occurrence (exact search, p ≤ 10000)

k = v_p(α^{L₀}−1) computed in R/p⁴. **No k ≥ 3 prime ≤ 10000** (so
(3,0) never occurs in range). k=2 primes ≤ 10000: only (13, L₀=14)
and (31, L₀=15); **neither has 4 | L₀**. Hence the s=0 real-case gap
(see §5) has no instance ≤ 10000.

## 2. Case (1,2): k=1, s=2 — reduced to one scalar

γ=1+pu, G_p of order p². Lemma-5 cosets F(C), v=v_p(Tr(Cu)):
v=0: full Tr(C)+pZ/p³; v=1: Tr(C)+p²Z/p³ (×p); v=2: singleton {Tr(C)}.
Step 1: mod p² this is f=2 s=1, so after a shift/reflection the
per-class multisets are equal mod p², and A″=A(1+pη), η∈R/p², with
Tr(η)≡0 mod p (wave-13 digit argument). Step 2: v=0 cosets match per
class automatically (fixed by Tr(C) mod p); v=1 cosets match per class
because v=1 forces C≡c∈F_p^× mod p, so Tr(ηC)≡c·Tr(η)≡0 mod p.
For v=2 singletons, Tr(C″)=Tr(C)+p²·c·S\* where c=C mod p and
S\* = τ+Tr(η₁)−ν·Tr(u₁)/μ is a single scalar (τ=Tr(η̃₀)/p for a lift
η̃₀ of η mod p; the w-dependence folds into c·S\* because the v=2
condition fixes w₂ given c). Hence, within each mod-p² residue class
(c fixed), top digits shift uniformly by cS\*.
**Dichotomy:** either S\* = 0 (done), or every nonempty y_low-group's
v=2 top-digit multiset is uniform over Z/p (in particular p divides
every group size). That scalar lemma is the only remainder for (1,2).
Numerics (exhaustive, 0 bad): (m,p)=(36,3) mod 27: 729 sequences,
17 groups; (m,p)=(150,5) mod 125 (L₀=6, k=1): 69 groups.

## 3. Case (2,1): k=2, s=1 — proved modulo f=2 s=0

γ=1+p²u, order p. Mod p², γ≡1, so Step 1 is f=2 s=0: after normalisation
A″≡A mod p², i.e. A″=A(1+p²η), η∈R/p. Full cosets (Tr(Cu)≢0 mod p)
are Tr(C)+p²Z/p³, unchanged by the p²-digit. Collapsed singletons
(Tr(Cu)≡0 mod p, so C≡c∈F_p^× for A unit) shift by p²·Tr(ηC),
Tr(ηC)≡c·Tr(η). The pooled partial-fractions argument (exactly as in
wave-13 s=1, at the top digit) gives Σ_{c} m_c·c·Tr(η)=0, so Tr(η)=0
if any collapsed C exists, and all collapsed digits vanish. Divisible
case by induction; Coll=∅ vacuous. Mechanism check at (m,p)=(182,13),
mod 2197: η with Tr(η)=0 gives global equality AND per-class exact
equality; η with Tr(η)=2 gives global inequality. The only inherited
gap is f=2 s=0 (§5).

## 4. Case (3,0): k=3 — absent, and harder in principle

No p ≤ 10000. A proof would be pure-G0 rigidity (polynomial identity
+ Hensel, as in wave-13 s=0) at level p³, where the real-case gap is
worse: (y₁−x₁)(y₁−x₂)=0 mod p³ admits y₁−x₁=p·d, y₁−x₂=p²·e
solutions, so the trace+norm rigidity needs the real-case analysis
at two digit levels, not one. No numerics possible in range.

## 5. Clarification: f=2 s=0 does occur, and holds

p=13 (L₀=14, t=2) and p=31 (L₀=15, t=1) are s=0 at f=2. Brute force
at p=13, mod 169, m=14: 1105 groups, 0 bad — the same count as
wave-12's table, so wave-12 did test an s=0 case. The remaining hole
in the f=2 s=0 proof is narrow: it needs k=2 AND 4 | L₀ (g≥3, so that
α^{|H₀|} is not real mod p and the stabiliser argument bites), and
no such prime exists ≤ 10000. Finding one, or proving impossibility,
is a separate small question.

## 6. What remains for G1

1. Scalar S\* = 0 for (1,2) (or a proof that some y_low-group has
   size prime to p whenever v=2 singletons exist).
2. f=2 s=0 real-case gap (k=2 and 4 | L₀).
3. (3,0) in general (no instance ≤ 10000).
4. Lean formalisation (untouched).

## Files

- This note: wave14_G1_f3.md
- Scripts: wave14_G1_f3_search.py (k-search to 1000, (36,3) check),
  wave14_G1_f3_search2.py (k-search to 10000, p=13 f=2 check,
  (150,5) check, (2,1) digit sanity at p=13).
