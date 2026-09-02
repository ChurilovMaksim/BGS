# Review Errors — BGS paper + workspace

> **SUPERSEDED 2026-08-31 (R83) — READ THIS FIRST.**  This was the PARTIAL
> 2026-08-30 review pass.  Machine re-execution (review/referee/ref01-ref03,
> artifacts/referee_r83/) REFUTED ERROR #1 and ERROR #3: the proposed fixes
> would have broken TRUE statements in the paper — do NOT apply them.
> ERROR #4's diagnosis was wrong but its refined core is real (Theorem II
> needs the hypothesis n1 != 0; fixed in the paper R84).  ERROR #2 was
> confirmed and repaired (paper paths, R84).  The authoritative adjudication
> and the full finding list is REVIEW_FINDINGS.md (Part A) and LEDGER.md
> RUN 83.  This file is kept for the record only.


Discovered during scientific review of `paper/exact_wd_and_subgroup_moments.tex`
on 2026-08-30. Each entry has: file, line(s), severity, current text, proposed
fix, and the source of verification.

---

## ERROR #1 — Theorem A cor:bgs-random misformulation

**File**: `paper/exact_wd_and_subgroup_moments.tex`
**Lines**: 260-275
**Severity**: HIGH

### Current text (line 266)

> «$\Theta U_A\Theta^{-1}=U_A^{-1}$ and $\Theta^2=+1$, and **preserves each $\HH_\lambda$**.»

### Why it is wrong

$\Theta U_A\Theta^{-1} = U_A^{-1}$ implies that if $U_A v = \lambda v$, then
$U_A(\Theta v) = \lambda^{-1}(\Theta v)$, so $\Theta$ **maps** $\HH_\lambda$ to
$\HH_{\lambda^{-1}}$, it does **not** stabilise $\HH_\lambda$ unless
$\lambda = \lambda^{-1}$ (i.e. $\lambda^2 = 1$).

For a generic cat map $A$ with $A^K = \chi \cdot \mathbf 1$, eigenvalues $\lambda$
satisfy $\lambda^K = \chi$, and most are not self-inverse.

### Verification

Direct consequence: Theorem A(b) requires $\Theta|_{\HH_\lambda}$ = complex
conjugation. Without stabilising $\HH_\lambda$ individually, the statement
must be applied to **the direct sum** $\HH_\lambda \oplus \HH_{\lambda^{-1}}$,
or with the upgraded antiunitary $\Theta_u$ of R73.1 (LEDGER R73.1, prop:Esquare
in paper's `Theorem E upgraded to a proof`).

### Proposed fix (line 266)

Replace «preserves each $\HH_\lambda$» with:

> «$\Theta U_A\Theta^{-1}=U_A^{-1}$ and $\Theta^2=+1$, and **maps $\HH_\lambda$
> isomorphically to $\HH_{\lambda^{-1}}$; in particular, it stabilises
> $\HH_\lambda \oplus \HH_{\lambda^{-1}}$ for every $\lambda$**.»

### Effect on cor:bgs-random (lines 268-275)

The corollary should be reworded to apply either to the direct sum
$\HH_\lambda \oplus \HH_{\lambda^{-1}}$ or via $\Theta_u = U_\tau \Theta$ of
prop:Esquare.

---

## ERROR #2 — Cert table references missing script names

**File**: `paper/exact_wd_and_subgroup_moments.tex`
**Lines**: 1854-1892 (numerical certification table)
**Severity**: HIGH

### Current state

The certification table references 11 script names (e.g.
`subgroup_kloos\-terman_energy.py`, `r80_jweight_dp.py`,
`r82_torus_rigidity.py`).

After the workspace rebrand (R82), 8 of these scripts were renamed to
descriptive paths:

| Paper says | Real path now |
|---|---|
| `catmap_independent.py` | `src/core/catmap_independent.py` (UNCHANGED — exists) |
| `theoremB_covariance.py` | `src/theorems/theorem_a_covariance.py` |
| `moment_certification.py` | `src/diagnostics/moment_certification.py` (UNCHANGED — exists) |
| `subgroup_kloos\-terman_energy.py` | `src/kloosterman/subgroup_kloosterman_energy.py` |
| `pstar_scan.py` | `src/kloosterman/pstar_scan.py` (UNCHANGED — exists) |
| `r80_jweight_dp.py` | `src/shape_automaton/jweight_dp.py` |
| `r80_wrap_collisions.py` | `src/shape_automaton/wrap_collisions.py` |
| `r80_julia_bigdp.jl` | `src/large_m/julia_bigdp.jl` |
| `r82_torus_rigidity.py` | `src/large_m/torus_rigidity.py` |
| `r82_orbit_invariant.py` | `src/large_m/orbit_invariant.py` |
| `r82b_dp_push.jl` | `src/shape_automaton/dp_push.jl` |

### Effect

8/11 cited script paths are broken. A reader following the table cannot
locate the cited scripts in the workspace.

### Proposed fix

Update lines 1864-1891 to use the new snake_case paths under topic
subfolders. e.g.:

```
\texttt{src/theorems/theorem\_a\_covariance.py}
\textcolor{red}{$\to$}
\texttt{src/theorems/theorem\_a\_covariance.py}
```

(Same path — this one happens to be unchanged.)

```
\texttt{src/r80\_jweight\_dp.py}
\textcolor{red}{$\to$}
\texttt{src/shape\_automaton/jweight\_dp.py}
```

---

## ERROR #3 — Theorem G norm estimates sign error

**File**: `paper/exact_wd_and_subgroup_moments.tex`
**Lines**: 1037-1039
**Severity**: MEDIUM-HIGH

### Current text

> «$\|\bar c\|_1\asymp\|c\|_1$, $\;\|\bar c\|_2\asymp K^{-1/2}\|c\|_2$, so
> $\;\|\bar c\|_1/\|\bar c\|_2\asymp\sqrt K\,\|c\|_1/\|c\|_2$»

### Why it is wrong

The Birkhoff average is $\bar c_m = K^{-1}\sum_{n\in A^T\text{-orbit}(m)}c_n$.
For the general $c$:

- $\|\bar c\|_1 = K^{-1}\|c\|_1$ (not $\asymp\|c\|_1$).
- $\|\bar c\|_2 = K^{-1/2}\|c\|_2$ **only** if $c$ has one point per orbit;
  if $c$ has $K$ points per orbit, $\|\bar c\|_2 = K^{-1}\|c\|_2$.

The conclusion $\|\bar c\|_1/\|\bar c\|_2 \asymp \sqrt K$ would then require
$\|\bar c\|_2 = K^{-1}\|c\|_2$ (one point per orbit), giving
$\|\bar c\|_1/\|\bar c\|_2 = K^{-1}\|c\|_1 / (K^{-1}\|c\|_2) = \|c\|_1/\|c\|_2$,
i.e. **no $\sqrt K$ factor at all**.

If $c$ has $K$ points per orbit and $\|\bar c\|_2 = K^{-1/2}\|c\|_2$, then
$\|\bar c\|_1/\|\bar c\|_2 = K^{-1}\|c\|_1 / (K^{-1/2}\|c\|_2) = K^{-1/2} \cdot \|c\|_1/\|c\|_2$,
i.e. $\sqrt K^{-1}$, not $\sqrt K$.

In both regimes the factor is $\le \sqrt K^{-1}$, never $\sqrt K$. This is
a sign error.

### Effect on corollary (lines 1081-1085)

Paper's corollary «moment method cannot reach the mean-spacing scale»
relies on $K^{r/2}$ growth of $|\theta_r|/|a_r|$. The sign error means
the moment method actually **opens up** for larger $K$ — opposite of
the claimed direction.

**However**, the empirical data (table on lines 1063-1072) shows
$\max_J|S_J|/\|a\|_1 \in [0.22, 0.53]$ (essentially **constant** in $r$ and $K$),
i.e. **no** $K^{r/2}$ growth in practice. The empirical conclusion
"no square-root cancellation" **survives**, but the mathematical
derivation does not.

### Proposed fix

Replace lines 1037-1039 with:

> «$\|\bar c\|_1 = K^{-1}\|c\|_1$, $\;\|\bar c\|_2 = K^{-1/2}\|c\|_2$ (one
> point per orbit, the worst case), so
> $\;\|\bar c\|_1/\|\bar c\|_2 = K^{-1/2}\cdot\|c\|_1/\|c\|_2$»

and update the corollary accordingly: the $K^{r/2}$ factor in
$|\theta_r|/|a_r| \asymp (c\sqrt K)^r/m$ should be
$(c/\sqrt K)^r = c^r K^{-r/2}$, which DECREASES with $K$. The empirical
data (no square-root cancellation) is therefore the deeper statement.

---

## ERROR #4 — Theorem II matrix element derivation gap

**File**: `paper/exact_wd_and_subgroup_moments.tex`
**Lines**: 1499-1506
**Severity**: MEDIUM

### Current text

> «$\langle f_\chi|T(n)|f_\psi\rangle = e_N(-q/2)\,\overline{\chi}(n_1)\psi(n_1)
> \frac{J(\chi,\psi;q)}{N-1}$, with
> $J(\chi,\psi;q)=\sum_{x\neq0,1}\overline{\chi}(x)\psi(x-1)e_N(qx)$,
> $q=n_1n_2$»

### Direct computation does not give this form

Direct calculation:
$\langle f_\chi|T(n)|f_\psi\rangle$ after $x \to x + n_1$ substitution gives

$\overline{\chi}(n_1)e(2^{-1}n_1 n_2)\sum_x \overline{\chi}(x)\psi(x)\,e(n_2 x/N)$

i.e. the exponential involves $n_2$ alone, and the sum has $\psi(x)$ (not
$\psi(x-1)$). This does **not** match the stated $J(\chi,\psi;q)$ with
$q = n_1 n_2$.

### Numerical agreement

The formula is verified on **all** 198 level sets at $N = 199$ to
max error $6.1 \times 10^{-14}$ and 3570 level sets at $N = 3571$ to
$2.4 \times 10^{-13}$. The formula is **numerically correct**.

### Source of the gap

There must be a character-orthogonality identity (or a careful redefinition
of the eigenbasis $f_\chi$) that converts the $\sum \overline{\chi}(x)\psi(x)e(n_2 x/N)$
form into paper's $\sum \overline{\chi}(x)\psi(x-1)e(n_1 n_2 x/N)$ form.
The paper does not show this conversion.

### Proposed fix

Add 2-3 lines between (1501) and (1505) deriving the formula from
$\sum_x \overline{\chi}(x)\psi(x)e(n_2 x/N)$ via the substitution
$\psi(x) = \sum_\tau \hat\psi(\tau) \tau(x)$ and the orthogonality
$\sum_x \overline{\chi}(x)\tau(x)e(n_2 x/N) = \tau\chi^{-1}(n_2/N) \cdot J(\chi\tau^{-1},\psi;\cdot)$ —
or whatever the actual character identity is.

---

## Minor: $S(10) = 31$ vs data 35

**File**: paper.tex around line 1301
**Severity**: MINOR

Paper says: «The shape census for $m_3$ (width $\le 16$) is
$S(R) = 1,1,1,3,8,31,64,105$ for $R = 5,\dots,12$».

Data: `artifacts/legacy_runs/theorems/H_shape_decomposition/shapes_t3_w16.json`
has $S(10) = 35$ (with width $\le 16$). The discrepancy is 4 shapes,
which appear to be zero-padded concatenations of $(1,-3,1)$ counted
differently in the paper.

Fix: either update paper to 35 or recompute with stricter width cap.

---

## Minor: $z_{Poisson}$ rounding

Severity: MINOR (cosmetic)

Paper rounds $43.078 \to 43.1$, $66.94 \to 66.9$, $94.91 \to 94.9$ in
the BGS at large m table. Numerical certificates agree exactly, this
is just truncation to one decimal place.
