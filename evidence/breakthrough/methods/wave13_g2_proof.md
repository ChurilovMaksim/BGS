# Wave 13, task 3 — G2: 2-primary per-class multiset level: PROVED (proof sketch)

## Statement (component level)

Let $m \ge 1$, $L = v_2(m)$, $a = v_2(D_m)$, $q = 2^a$, $t = \gcd(m,4)$.
By the LTE formula proved in wave 11, task 3, $a = 2$ if $L = 0$ and
$a = 2L+3$ if $L \ge 1$. Let $\mathrm{Fix}_m \bmod q$ be the recurrence
sequences $(y_i)_{i \in \mathbf{Z}/m}$ with $y_{i+1} = 6y_i - y_{i-1}$
mod $q$, and let $M_r(y) = \{y_i : i \equiv r \pmod t\}$ be the
per-class multisets.

**Theorem (G2).** If $y, y' \in \mathrm{Fix}_m \bmod q$ have the same
sorted global multiset, then their per-class multisets are
$D_t$-related: there is $\pi \in D_t$ with $M'_r = M_{\pi(r)}$ for
all $r$, where $D_t$ acts by $r \mapsto r+b$ and $r \mapsto -r+b$.

This is the 2-primary component of the exact per-class lemma
(wave 11, task 2). It does **not** by itself close the full exact
lemma: G1 (odd prime-power lift, reduced to L6/L7 in wave 12) and
G3 (one common $\pi$ across components) remain open, and the
assembly of components into the global lemma is separate.

## Inputs used (all prior waves, none re-proved here)

- **Pattern lemma** (wave 11, task 1): for $P = 2^L$, $L \ge 2$,
  patterns $p, p' \in \mathrm{Fix}_P \bmod 2^{2L+3}$ with the same
  multiset have $D_4$-related per-class multisets (induction L1–L4).
- **LTE formula** (wave 11, task 3): $v_2(D_m)$ depends only on
  $v_2(m)$: $2$ for $m$ odd, $2L+3$ for $L = v_2(m) \ge 1$.
- No Lean is built; this is a mathematical proof sketch, and the
  repository is untouched.

## Proof

### 0. Sequences = kernel vectors

Put $M = \begin{pmatrix} 6 & -1 \\ 1 & 0 \end{pmatrix}$.
A recurrence sequence mod $q$ is determined by $(y_0, y_1)$, and
$(y_{n+1}, y_n)^T = M^n (y_1, y_0)^T$; $m$-periodicity is exactly
$(y_1, y_0) \in \ker(M^m - I)$ mod $q$. The eigenvalues of $M$ are
$\alpha = 3+2\sqrt2$, $\beta = 3-2\sqrt2$, so
$\det(M^n - I) = (\alpha^n - 1)(\beta^n - 1) = 2 - s_n = -D_n$,
where $s_n = \alpha^n + \beta^n$ and $D_n = s_n - 2 > 0$ for $n \ge 1$.

### 1. Kernel-size lemma

For any $n \ge 1$, with $a_n = v_2(D_n)$,
$|\mathrm{Fix}_n \bmod 2^{a_n}| = 2^{a_n}$.

*Proof.* Let $M^n - I = U\,\mathrm{diag}(d_1, d_2)\,V$ be the Smith
normal form over $\mathbf{Z}$ ($d_1 \mid d_2$,
$d_1 d_2 = |\det| = D_n$). Since $U, V$ are unimodular, they induce
bijections mod $q = 2^{a_n}$, so the kernel size is
$\gcd(d_1, q) \cdot \gcd(d_2, q)
= 2^{\min(v_2(d_1), a_n) + \min(v_2(d_2), a_n)}$.
But $v_2(d_1) + v_2(d_2) = v_2(D_n) = a_n$ with both terms $\ge 0$,
hence both $\le a_n$, so both minima are the valuations themselves
and the size is $2^{a_n}$. ∎

(Sanity data, not needed by the proof: SNF of $M^m - I$ gives
$(v_2(d_1), v_2(d_2)) = (L, L+3)$ for $m = 2, 4, 6, 8, 12, 24$,
e.g. $m = 12$: $\mathrm{diag}(13860, 110880)$, valuations $(2,5)$.)

### 2. Reduction: $\mathrm{Fix}_m$ = repeats of $\mathrm{Fix}_P$

Let $L \ge 1$, $P = 2^L$, $u = m/P$ (odd). By LTE,
$v_2(D_m) = v_2(D_P) = 2L+3 =: a$, so by §1,
$|\mathrm{Fix}_m \bmod 2^a| = |\mathrm{Fix}_P \bmod 2^a| = 2^a$.
The $u$-fold repeat of a pattern $z \in \mathrm{Fix}_P$,
$y_i = z_{i \bmod P}$, satisfies the recurrence cyclically mod $m$
(because $P \mid m$, reduction of indices mod $m$ followed by
mod $P$ is reduction mod $P$, where $z$ satisfies the recurrence),
so $y \in \mathrm{Fix}_m$. The repeat map is injective (restrict to
the first $P$ positions). Two finite sets of the same size
$2^a$, one contained in the other, are equal. Hence:

**Every sequence in $\mathrm{Fix}_m \bmod 2^a$ is $P$-periodic**,
i.e. the $u$-fold repeat of a unique pattern in $\mathrm{Fix}_P
\bmod 2^a$.

### 3. Transfer of multisets

Let $y, y'$ be repeats of patterns $z, z'$. Since $P \equiv 0
\pmod t$ ($t = 4$ for $L \ge 2$, $t = 2$ for $L = 1$), position
$i = kP + j$ has class $i \bmod t$ equal to $j \bmod t$, and each
pattern position occurs exactly $u$ times in $y$. Therefore:

- the global multiset of $y$ is $u$ copies of that of $z$;
  equal global multisets for $y, y'$ imply equal global multisets
  for $z, z'$ (divide multiplicities by $u$);
- the per-class multiset $M_r(y)$ is $u$ copies of $M_r(z)$,
  and similarly for $y'$.

So it suffices to prove the claim for patterns, with the same $\pi$.

### 4. Case $L \ge 2$: pattern lemma

Here $t = 4$ and the modulus is $2^{2L+3}$, exactly the setting of
the pattern lemma. If $z, z'$ have the same multiset, their
per-class multisets are $\pi$-related for some $\pi \in D_4$;
taking $u$ copies, the same $\pi$ relates $M_r(y), M_r(y')$. ∎

### 5. Case $L = 1$: elementary

Here $t = 2$, $P = 2$, $q = 32$. A pattern is $(z_0, z_1)$; $y$ has
even class $= z_0$ repeated $m/2$ times and odd class $= z_1$
repeated $m/2$ times. If $z_0 = z_1$, $y$ is constant and the claim
is trivial. Otherwise the global multiset of $y$ is
$\{z_0^{m/2}, z_1^{m/2}\}$; equality for $y'$ forces
$\{z'_0, z'_1\} = \{z_0, z_1\}$ as sets, so the per-class multisets
are either equal or swapped. And $D_2 = \{\mathrm{id}, \mathrm{swap}\}$:
mod $2$, reflection $r \mapsto -r + b$ is $r \mapsto r + b$, so
$D_2$ is generated by the shift alone. ∎

### 6. Case $L = 0$: trivial

$m$ odd gives $t = \gcd(m, 4) = 1$: a single class, the per-class
multiset is the global multiset. ∎

This completes G2 at the component modulus $q = 2^{v_2(D_m)}$.

## Numerical confirmation (exact arithmetic, verifier artefacts)

C++ brute force over all $(y_0, y_1) \in (\mathbf{Z}/q)^2$
(`wave13_g2_check.cpp`): for $m = 2, 6, 10, 12, 14, 18, 20, 22, 24,
26, 28, 30, 32, 34, 36, 38, 40, 44, 48, 52, 56, 60$:

- $|\mathrm{Fix}_m| = 2^a$ in every case (e.g. $m = 32$: $8192$;
  $m = 48$: $2048$), confirming §1;
- non-$P$-periodic sequences: **0** in every case, confirming §2;
- multiset groups with non-$D_t$-constant per-class canonical
  form: **0** in every case (e.g. $m = 32$: 278 groups;
  $m = 48$: 145 groups), confirming the theorem directly.

Group counts depend only on $L$ (18 for $L = 1$, 39 for $L = 2$,
76 for $L = 3$, 145 for $L = 4$, 278 for $L = 5$), exactly as the
reduction §2 predicts, since $\mathrm{Fix}_m$ is just repeats of
$\mathrm{Fix}_P$.

## Scope and what remains

- Proved here: G2, the 2-primary component, for the component
  modulus $q = 2^{v_2(D_m)}$ (i.e. $q \parallel D_m$). The statement
  for a larger 2-power modulus is a different, stronger claim and
  is not addressed.
- Still open for the full exact per-class lemma: G1 (odd
  prime-power lift; wave 12 reduced it to lemmas L6/L7) and G3
  (one common $\pi$ across all components; wave 12 showed it is
  not pure combinatorics and isolated lemma PC). With G2 closed,
  the exact lemma's remaining gaps are exactly G1 and G3.
- Caveat: the pattern lemma input is itself a proof sketch
  (wave 11, task 1), not a Lean theorem; no step here is a Lean
  formalisation.
