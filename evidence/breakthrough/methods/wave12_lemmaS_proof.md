# Wave 12, task 2 — Lemma S (stabilizer adjustment): PROVED (proof sketch)

**Verdict: Lemma S is proved in general.** No counterexample exists.
This closes input (B) of the wave-11 task-3 compatibility argument.
Together with input (A), the per-class pattern lemma proved in wave 11
task 1, **π₂ = π₃ compatibility at mod-D level is now proved as a
sketch**, i.e. Pmix at mod-D level is fully closed as a sketch.
Repository untouched, Lean not built; this is ordinary mathematics,
not a Lean formalisation. Remaining for Lemma Y: exact Pcarry
(lifting mod D to exact integer class sums) and Lean formalisation.

## 0. Statement and reduction to blocks

Let $p \in \mathrm{Fix}_P \bmod 2^a$, $P = 2^L$, $a = 2L+3$,
be a pattern, $M_r$ its per-class multisets ($r \in \mathbb{Z}/4$,
classes $j \equiv r \pmod 4$), $v = (a_1, b_1, -a_1, -b_1) \in
\mathbb{F}_3^4$ a mod-3 4-vector with fiber blocks $F$,
$\gamma \in D_4$ satisfying

```
(*)   ⊎_{r ∈ F} M_r = ⊎_{r ∈ γ(F)} M_r    for every block F.
```

**Lemma S.** There is $\delta \in \mathrm{Stab}(M) =
\{\delta \in D_4 : M_{\delta(r)} = M_r \ \forall r\}$ with
$\delta(\gamma(F)) = F$ for every block $F$.

By the wave-11 task-1 reduction, every pattern is $2^L$ times a
block $B_s = Tc_s + De_s \pmod{2^{L+3}}$, $T$ arbitrary,
$D$ a multiple of $8$; scaling by $2^L$ is injective and preserves
multiset equalities, unions, $\mathrm{Stab}$, $\gamma$ and blocks.
Hence it suffices to prove Lemma S for blocks. A **segment at
level $t \ge 5$** is the first $M = 2^{t-3}$ values of a block
mod $2^t$; its class multisets have size $M/4$. Full blocks are
level $t = L+3 \ge 5$. We use two facts from the pattern proof:

- **(L1)** Mod $32$, a block has period $4$; mod $16$ its base
  tuple is $(a, b, a, b)$ with $a = T \bmod 16$,
  $b = (3T + D) \bmod 16$. If $T$ is odd then $a \ne b \pmod{16}$:
  $a = b$ would need $2T + 8d \equiv 0 \pmod{16}$, i.e.
  $T + 4d \equiv 0 \pmod 8$ with $d = (D/8) \bmod 2$, impossible
  for $T$ odd.
- **(L2)** For a segment at level $t+1$ (length $2M$, modulus
  $2^{t+1}$) and $s < M$:
  $B_{s+M} \equiv B_s + 2^t \delta_s \pmod{2^{t+1}}$ with
  $\delta_s = (D/8 + T\cdot(s \bmod 2)) \bmod 2$.
  Since $M \equiv 0 \pmod 4$, the class is preserved, and
  $\delta_s$ depends only on the class parity; write
  $\delta^{(r)} = (d + T\cdot(r \bmod 2)) \bmod 2$,
  $d = (D/8) \bmod 2$.

**Correction recorded.** An earlier draft of the argument below
claimed first-half top bits are constant per class. That is
FALSE (first-half values mod $2^{t+1}$ with the same mod-$2^t$
reduction have varying top bits; verified numerically). The
proof below never uses first-half top bits: for $\delta = 1$
classes the two halves together give both lifts regardless of
the first-half top bit, Case B uses scaling, and Case C mixed
pairs use a mod-16 split.

## 1. Pair lemma (PL): the Fix-specific step

**Lemma PL(t).** For any segment at level $t \ge 5$ and any two
pairs of distinct classes $(r, s)$, $(r', s')$ with
$M_r \uplus M_s = M_{r'} \uplus M_{s'}$, we have
$\{M_r, M_s\} = \{M_{r'}, M_{s'}\}$ as multisets of multisets.

*Base $t = 5$.* Segments have length $4$; each $M_r$ is a
singleton, so pair-union equality is pair-profile equality. ∎

*Step $t \to t+1$.* Let $S$ be a segment at level $t+1$,
$A_r$ the class multisets of its first half reduced mod $2^t$
(a level-$t$ segment). By (L2),
$M^{t+1}_r = F_r \uplus (F_r + 2^t\delta^{(r)})$ where $F_r$
is the first-half class multiset mod $2^{t+1}$ (reducing to
$A_r$). Two facts:

- **(D)** If $\delta^{(r)} = 1$ then $M^{t+1}_r = D(A_r)$ where
  $D(X) = X \uplus (X + 2^t)$ (each value $b$ gives $\{b,
  b+2^t\}$). Indeed, a first-half position with reduction $b$
  contributes the pair $\{B_s, B_s + 2^t\} = \{b, b+2^t\}$
  as an unordered pair, whatever $B_s$'s top bit is. $D$
  is injective and distributes over unions.
- **(S)** In Case B below, $M^{t+1}_r = 2\cdot(A'_r \uplus
  A'_r)$ where $A'_r$ is a level-$t$ segment (parameters
  $(T/2, D/2)$) class multiset, via $F_r = 2\cdot A'_r$.

Cases on $(T \bmod 2, d)$, exhaustive:

- **Case A: $T$ even, $d = 1$.** Then $\delta^{(r)} = 1$ for
  all $r$, so $M_r = D(A_r)$ for all $r$. Pair-union equality
  gives $D(A_r \uplus A_s) = D(A_{r'} \uplus A_{s'})$, hence
  $A_r \uplus A_s = A_{r'} \uplus A_{s'}$ ($D$ injective);
  by PL($t$), $\{A_r, A_s\} = \{A_{r'}, A_{s'}\}$; applying
  $D$ gives $\{M_r, M_s\} = \{M_{r'}, M_{s'}\}$. ∎
- **Case B: $T$ even, $d = 0$.** Then $\delta^{(r)} = 0$ for
  all $r$ and all values are even. By (S),
  $M_r \uplus M_s$ has value $2x$ with multiplicity
  $2(A'_r(x) + A'_s(x))$; equality gives
  $A'_r \uplus A'_s = A'_{r'} \uplus A'_{s'}$; by PL($t$)
  on the scaled segment, $\{A'_r, A'_s\} =
  \{A'_{r'}, A'_{s'}\}$; since $M_r$ is determined by $A'_r$,
  $\{M_r, M_s\} = \{M_{r'}, M_{s'}\}$. ∎
- **Case C: $T$ odd.** Then $\delta^{(\mathrm{even})} = d$,
  $\delta^{(\mathrm{odd})} = 1-d$; the $\delta = 0$ classes
  form a single opposite pair, the $\delta = 1$ classes the
  other opposite pair. Even-class values are $\equiv a
  \pmod{16}$, odd-class values $\equiv b \pmod{16}$, with
  $a \ne b$ by (L1). A pair's mod-16 profile is therefore:
  mixed pair $\to (M/4$ copies of $a$, $M/4$ of $b$);
  even pair $\to (M/2$ of $a$); odd pair $\to (M/2$ of $b$).
  Union equality forces $(r', s')$ to have the same
  parity pattern as $(r, s)$. If both pairs are even,
  $(r, s) = (r', s') = (0, 2)$; if both odd, $(1, 3) =
  (r', s')$; both trivial. If both mixed, the mod-16
  split of the union is exactly the even class multiset
  (the $a$-part) and the odd class multiset (the $b$-part)
  on both sides, so $M_{\mathrm{even}} = M_{\mathrm{even}'}$
  and $M_{\mathrm{odd}} = M_{\mathrm{odd}'}$, giving
  profile equality. ∎

This proves PL($t$) for all $t \ge 5$, hence for all blocks.
Note PL is false for arbitrary multisets (the wave-11 §5
counterexample has $M_0 \uplus M_1 = M_2 \uplus M_3$ but
$\{M_0, M_1\} \ne \{M_2, M_3\}$); the segment structure
(Cases A/B/C) is exactly the Fix input that rules it out.

## 2. From (*) to profile preservation

Define $\mathrm{profile}(S) = \{M_r : r \in S\}$ (multiset of
multisets). For a pair block $F = \{r, s\}$, (*) is
$M_r \uplus M_s = M_{\gamma(r)} \uplus M_{\gamma(s)}$,
so PL gives $\mathrm{profile}(\gamma(F)) =
\mathrm{profile}(F)$. For a singleton block, (*) itself is
profile equality. For the size-4 block, $\gamma(F) = F$.
Hence:

```
profile(γ(F)) = profile(F)    for every block F.
```

## 3. Combinatorial step: profile preservation implies Lemma S

Now $M = (M_0, \dots, M_3)$ is arbitrary; only the profile
hypothesis, $\gamma \in D_4$, and the block shapes are used.
Write $e(r) = M_r$. The $v$-block shapes are: one block of
size 4 (Type Z); an opposite pair plus two singletons
(Type O); two adjacent pairs (Type B). $D_4$ preserves
opposite pairs and adjacent pairs. Multiset cancellation
used below: $\{A, B\} = \{A, C\}$ implies $B = C$ (if
$A \ne B$ then $B \in \{A, C\}$ forces $B = C$; if $A = B$
then $\{A, A\} = \{A, C\}$ forces $C = A$).

- **Type Z.** $\delta = \mathrm{id}$ works.
- **Type O.** Blocks $P = \{p, p+2\}$ and singletons
  $\{s\}, \{t\} = \{p+1, p+3\}$. Since $\gamma$ preserves
  opposite pairs, either (i) $\gamma(P) = P$,
  $\gamma(\{s, t\}) = \{s, t\}$, or (ii) they swap.
  - (i) Singleton profiles give $e(\gamma(s)) = e(s)$,
    $e(\gamma(t)) = e(t)$. If $\gamma$ fixes $s, t$,
    $\delta = \mathrm{id}$ works. If $\gamma$ swaps them,
    then $e(s) = e(t)$, and $\delta_0(r) = -r + 2p$
    (fixes $P$ pointwise, swaps $s, t$) satisfies
    $\delta_0\gamma(s) = s$, $\delta_0\gamma(t) = t$,
    $\delta_0\gamma(P) = P$, and $\delta_0 \in
    \mathrm{Stab}(M)$.
  - (ii) $\gamma(P) = \{s, t\}$, $\gamma(\{s, t\}) = P$.
    Singleton profiles give $e(\gamma(s)) = e(s)$,
    $e(\gamma(t)) = e(t)$ with $\{\gamma(s), \gamma(t)\}
    = P$; pair profile gives $\{e(s), e(t)\} =
    \{e(p), e(p+2)\}$. The map $\delta|_P$ forced by
    $\delta(\gamma(s)) = s$, $\delta(\gamma(t)) = t$
    is opposite-preserving, hence extends to exactly two
    $D_4$ elements (rotation and reflection), which differ
    on $\{s, t\}$ by $2$ and both map $\{s, t\} \to P$.
    Choose the extension with $e(\delta(s)) = e(s)$
    (possible since $e(s) \in \{e(p), e(p+2)\}$ and
    $\delta(s)$ ranges over both elements of $P$);
    then $e(\delta(t)) = e(t)$ follows from the pair
    profile, $\delta \in \mathrm{Stab}(M)$ (on $P$ by the
    singleton profiles), and $\delta\gamma$ fixes $s, t$
    and maps $P$ to $P$.
- **Type B.** Blocks $F_1 = \{q, q+1\}$, $F_2 = \{q+2, q+3\}$.
  Since $\gamma$ preserves adjacent pairs,
  $\{\gamma(F_1), \gamma(F_2)\}$ is either $\{F_1, F_2\}$
  (subcase A) or the shifted partition
  $\{\{q+1, q+2\}, \{q+3, q\}\}$ (subcase B).
  - A, $\gamma(F_i) = F_i$: $\delta = \mathrm{id}$.
  - A, $\gamma$ swaps blocks: profile equality
    $\{e(q), e(q+1)\} = \{e(q+2), e(q+3)\}$. Either the
    ordered equalities hold (then rotation by $2$ is in
    $\mathrm{Stab}$) or the swapped ones hold (then the
    reflection $r \mapsto -r + 2q + 3$ is in
    $\mathrm{Stab}$); either $\delta$ swaps the blocks,
    so $\delta\gamma(F_i) = F_i$.
  - B, variant 1: $\gamma(F_1) = \{q+1, q+2\}$,
    $\gamma(F_2) = \{q+3, q\}$. Profile gives
    $\{e(q+1), e(q+2)\} = \{e(q), e(q+1)\}$, hence
    $e(q+2) = e(q)$ by cancellation. The reflection
    $r \mapsto -r + 2q + 2$ (fixes $q+1, q+3$; swaps
    $q, q+2$) is in $\mathrm{Stab}(M)$ and satisfies
    $\delta\gamma(F_1) = F_1$, $\delta\gamma(F_2) = F_2$.
  - B, variant 2: $\gamma(F_1) = \{q+3, q\}$,
    $\gamma(F_2) = \{q+1, q+2\}$. Profile gives
    $e(q+3) = e(q+1)$ by cancellation. The reflection
    $r \mapsto -r + 2q$ (fixes $q, q+2$; swaps $q+1, q+3$)
    is in $\mathrm{Stab}(M)$ and satisfies
    $\delta\gamma(F_i) = F_i$.

This proves Lemma S for blocks, hence for patterns. ∎

## 4. Consequence

Input (B) of wave-11 task 3 is closed. With input (A) (per-class
pattern lemma, wave-11 task 1), the wave-11 task-3 argument now
gives, as a proof sketch: for every global fiber pair
$y' = \sigma(y)$ there is a single $\pi \in D_4$ with
$Y' \equiv \pi(Y) \pmod D$. **Pmix at mod-D level is closed
as a sketch.** What remains for Lemma Y in full: exact Pcarry
(lifting $Y' \equiv \pi(Y) \pmod D$ to exact integer equality;
the exact per-class lemma of wave-11 task 2 would imply it,
and is open with gaps G1/G3), and Lean formalisation of all
steps. G4c and the application to claim 152 are untouched.

## 5. Computational confirmation (verifier artefacts, not proofs)

- PL at $L = 6$ (all blocks): 60,244 pair-union collisions,
  0 profile mismatches (script `wave12_lemmaS_explore1.py`
  for $L \le 5$, `wave12_lemmaS_explore3.py` for $L = 6$).
- Lemma S for blocks at $L = 5$: 271,136 $\gamma$-cases,
  0 fails; at $L = 6$: 1,082,144 $\gamma$-cases, 0 fails
  (scripts `wave12_lemmaS_explore3.py`,
  `wave12_lemmaS_L6check.py`).
- Combinatorial step §3 for random $M$: 4,905,240
  profile-preserving cases, 0 fails (script
  `wave12_lemmaS_explore2.py`).
- The false uniform-$\theta$ claim and the fact that $F_r$
  is not determined by $A_r$ (even given parity) were found
  by the scripts `wave12_lemmaS_explore3.py` (§b) and
  `wave12_lemmaS_explore4.py`/`wave12_lemmaS_explore5.py`;
  the proof in §1 avoids both.

## Files

- This note: [wave12_lemmaS_proof.md](sandbox://workspace/bgs-breakthrough/methods/wave12_lemmaS_proof.md)
- Checks: [wave12_lemmaS_explore1.py](sandbox://workspace/bgs-breakthrough/methods/wave12_lemmaS_explore1.py),
  [wave12_lemmaS_explore2.py](sandbox://workspace/bgs-breakthrough/methods/wave12_lemmaS_explore2.py),
  [wave12_lemmaS_explore3.py](sandbox://workspace/bgs-breakthrough/methods/wave12_lemmaS_explore3.py),
  [wave12_lemmaS_explore4.py](sandbox://workspace/bgs-breakthrough/methods/wave12_lemmaS_explore4.py),
  [wave12_lemmaS_explore5.py](sandbox://workspace/bgs-breakthrough/methods/wave12_lemmaS_explore5.py),
  [wave12_lemmaS_L6check.py](sandbox://workspace/bgs-breakthrough/methods/wave12_lemmaS_L6check.py)
- Prior notes: [wave11_task3_pi2pi3_compatibility.md](sandbox://workspace/bgs-breakthrough/methods/wave11_task3_pi2pi3_compatibility.md),
  [wave11_perclass_pattern_proof.md](sandbox://workspace/bgs-breakthrough/methods/wave11_perclass_pattern_proof.md)
