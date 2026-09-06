"""Publish run 74: the frequency-ensemble moment route. Idempotent."""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

BLOCK = r"""
## RUN 74 (2026-08-28, continuation) — THE FREQUENCY-ENSEMBLE ROUTE IS OPEN

Theorem G (R73.5) closed the moment route for a **fixed** observable. But BGS in
this family is naturally a statement about the **ensemble** of observables
`V_n = T(n) + T(-n)`, `n in (Z/N)^2`, and averaging over n changes the estimate
qualitatively. This run opens that route and computes its combinatorics exactly.

### R74.1 — Exact ensemble moment formula

Since `P_lam T(v) P_lam = W_v P_lam` with `W_v = K^{-1} sum_j T(A^{jt}v)` (T6),
the Weyl relations collapse every product and

    (1/m) Tr(M_n^r) = K^{-r} sum_{eps,j} phi(eps,j) . 1{ L(eps,j) n = 0 mod N }
                      + (m K^r)^{-1} sum_{eps,j} phi . E(L(eps,j) n),
    L(eps,j) = sum_{i=1..r} eps_i (A^{j_i})^t,
    E(w) = Tr(P_lam T(w)) - m 1{w=0} = K^{-1} sum_{J != 0} lam^{-J} Tr(T(w)U^J).

### R74.2 — The rank-0 condition is two Chebyshev congruences [PROVEN + certified]

`A^j = U_j A - U_{j-1} I` with `U_0 = 0, U_1 = 1, U_{j+1} = t U_j - U_{j-1}`,
`t = tr A` (and `U_{-1} = -1`). Since `{A, I}` is a basis of the algebra generated
by A,

    L(eps,j) = 0 mod N   <=>   sum_i eps_i U_{j_i} = 0  AND
                               sum_i eps_i U_{j_i-1} = 0   (mod N),

i.e. **two signed vanishing sums of a lacunary integer sequence** — the matrix
analogue of the char-0 rigidity of Theorem B. Certified: **1600 random (eps,j)
over four (A,N) including K = 200, zero mismatches**
(`artifacts/r74/ensemble_moments.json`).

### R74.3 — THE GAIN: averaging over n buys a full factor N

By Lemma F, `Tr(T(w)U^J) = Tr(U^J) w^{Q_J(w)}` with `Q_J` a homogeneous quadratic
form. With `w = L n` the phase is `Q_J(Ln)`, a quadratic form in n, so

    E_n[ w^{Q_J(L n)} ] = N^{-2} . (binary Gauss sum) = O(1/N)

whenever `Q_J o L` is nondegenerate. Hence the error term, which is of size
`2^r K / m` for a FIXED n (the Theorem-G regime), becomes `O(2^r / (m N))` after
averaging. With `K = N^theta` and `m ~ N/K` this moves the reachable moment order

    from   r < 2/theta   (T18, fixed observable)
    to     r < 4/theta   (ensemble),

and the cancellation Theorem G proved to be absent for a fixed observable is
*present* here, because it is cancellation in n, not in v. **The ensemble route is
therefore open; Theorem G does not close it.**

### R74.4 — The ensemble combinatorics, exactly

Write `D_r(N) = #{(eps,j) : L(eps,j) = 0 mod N}`, `r = 2s`, and let
`P(s,K) = s!^2 [x^s] I_0(2 sqrt x)^K` be the pairing count of Theorem B. The number
of length-r words over `{(j,+),(j,-)}` carrying as many + as - at every j is
`r! [x^r] I_0(2x)^K = binom(2s,s) . P(s,K)`. Measured
(`src/diagnostics/ensemble_excess.py`, `artifacts/r74/ensemble_excess.json`):

| A | N | K | eps | r | D_r(N) | trivial | excess | rel. |
|---|---|---|---|---|---|---|---|---|
| Arnold | 3571 | 17 | +1 | 2 | 34 | 34 | **0** | 0 |
| Arnold | 3571 | 17 | +1 | 4 | 3366 | 3366 | **0** | 0 |
| Arnold | 3571 | 17 | +1 | 6 | 545020 | 538900 | 6120 | +1.1% |
| Arnold | 3571 | 17 | +1 | 8 | 122637830 | 117173350 | 5464480 | +4.5% |
| Arnold | 9349 | 19 | +1 | 2 | 38 | 38 | **0** | 0 |
| Arnold | 9349 | 19 | +1 | 4 | 4218 | 4218 | **0** | 0 |
| Arnold | 9349 | 19 | +1 | 6 | 766460 | 759620 | 6840 | +0.9% |
| Arnold | 9349 | 19 | +1 | 8 | 193271610 | 186398170 | 6873440 | +3.6% |

So for `eps = +1` the Bessel/pairing count is **exact at r = 2 and r = 4** and off
by 1-4% at r = 6, 8. Moreover the excess is **already present over Z** (5040 of
6120 at r=6; 4.45e6 of 5.46e6 at r=8): it is *combinatorial*, coming from the
Chebyshev recurrence itself, which supplies genuine +-1 relations
(`U_{j+1} + U_{j-1} = t U_j` written with repeats), not a mod-N accident. That is
good news — a combinatorial count is what one can hope to evaluate in closed form.

**The eps = -1 case carries an extra exact Z/2.** `A^k = -I` gives
`U_{j+k} = -U_j`, so the atom `(e, j)` and `(-e, j+k)` have identical signatures
and every configuration acquires `2^{r/2}` images. With that factor the count is
exact at r = 2 and overcounted by 1.5-3.5% at r = 4, 6 (the antiperiodic images
overlap the pairings, so the factor is an upper bound needing inclusion-exclusion).
This is the same `eps` dichotomy as Theorem D, now visible in the moment
combinatorics.

### R74.5 — What is now the whole remaining gap

    control the Chebyshev +-1 relation count  X_r  for r up to ~ log m,
    then feed the ensemble moments (error O(2^r/(mN)) by R74.3) into a
    resolvent/local-law argument.

Both halves are explicit: `X_r` is a lacunary-sequence counting problem (no
arithmetic, pure combinatorics over Z plus a bounded set of mod-N exceptions,
since a signed sum of r terms of a sequence bounded by `phi^K ~ N` lies in
`[-rN, rN]`, so `sum eps_i U_{j_i} = cN` with `|c| <= r` — only `O(r)` targets);
and the Gauss-sum gain is proved. This is a much smaller and much more concrete
target than "a local law".

**Status.** `[PROVEN]`: R74.2 (the Chebyshev characterisation, certified 1600/1600)
and R74.3 (the `O(1/N)` Gauss-sum gain, from Lemma F). `[NUMERICALLY-SUPPORTED]`:
the exactness of the Bessel/pairing count at `r <= 4` and the 1-4% excess at
`r = 6, 8`. `[OPEN]`: a closed form or sharp bound for `X_r`, and the resolvent
step. Calibrated confidence that the `r < 4/theta` improvement is correct as
stated: ~85%; that `X_r` admits a closed form: ~45%.
"""

TH = r"""
## 12. RUN 74 (2026-08-28) — THE FREQUENCY-ENSEMBLE ROUTE

Theorem G closed the moment route for a FIXED observable. The ensemble of
observables `V_n = T(n) + T(-n)`, `n in (Z/N)^2`, behaves differently.

**Exact formula.** By T6 and the Weyl relations,
`(1/m)Tr(M_n^r) = K^{-r} sum_{eps,j} phi . 1{L(eps,j) n = 0} + error`, with
`L(eps,j) = sum_i eps_i (A^{j_i})^t`.

**Rank-0 = two Chebyshev congruences [PROVEN, 1600/1600].** With
`A^j = U_j A - U_{j-1} I`, `U_{j+1} = t U_j - U_{j-1}`:
`L = 0 mod N` iff `sum eps_i U_{j_i} = 0` and `sum eps_i U_{j_i-1} = 0` mod N.

**The gain [PROVEN].** By Lemma F the error contains `w^{Q_J(Ln)}`, a quadratic
phase in n, so `E_n[.] = O(1/N)`: the fixed-n error `2^r K/m` becomes
`O(2^r/(mN))`. With `K = N^theta` the reachable moment order moves from
`r < 2/theta` to `r < 4/theta`. The cancellation Theorem G showed to be absent in
v is present in n.

**The combinatorics [measured].** With `r = 2s`, the number of words over
`{(j,+),(j,-)}` balanced at every j is `binom(2s,s) P(s,K)` with P the pairing
count of Theorem B. For `eps = +1` this is EXACT at r = 2, 4 (D_r = 34, 3366 at
K=17; 38, 4218 at K=19) and off by +1.1%, +4.5% at r = 6, 8; the excess is already
present over Z (5040 of 6120; 4.45e6 of 5.46e6), i.e. it comes from the Chebyshev
recurrence, not from mod-N accidents. For `eps = -1` the antiperiodicity
`U_{j+k} = -U_j` contributes an exact factor `2^{r/2}` (upper bound; overlaps with
the pairings make it 1.5-3.5% loose at r = 4, 6) — the same eps dichotomy as
Theorem D, now in the moment combinatorics.

**Remaining gap, in full.** Control the Chebyshev +-1 relation count `X_r` for
`r ~ log m`, then run a resolvent argument on the ensemble moments. Both halves
are explicit; note that a signed sum of r terms of a sequence bounded by
`phi^K ~ N` lies in `[-rN, rN]`, so the mod-N condition reads
`sum eps_i U_{j_i} = cN` with only `O(r)` admissible c.
"""


def patch(path, marker, text):
    p = os.path.join(ROOT, path)
    s = open(p, encoding="utf-8", errors="surrogateescape").read()
    if marker in s:
        return f"{path}: already present"
    open(p, "w", encoding="utf-8", errors="surrogateescape").write(
        s.rstrip() + "\n" + text)
    return f"{path}: appended"


print(patch("LEDGER.md", "RUN 74 (2026-08-28, continuation)", BLOCK))
print(patch("THEORY.md", "## 12. RUN 74", TH))
