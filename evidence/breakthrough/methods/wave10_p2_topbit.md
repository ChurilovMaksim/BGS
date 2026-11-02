# Wave 10, task 1 — Lemma Y, uniform P2: the top-bit lemma, proved

**Verdict: the top-bit lemma is proved in general (no counterexample).
In fact it is proved in a stronger, cleaner form: a doubling identity.**
Nothing here is a Lean theorem; the BGS repository was not touched and
Lean was not built. All finite checks are exact integer arithmetic
(C++), verifier artefacts, not proofs.

## 0. Notation (this note is self-contained)

Level $k\ge 3$ (the task's $v_2$ is this $k$):

- $Q_k = 2^{k+3}$, $Q' = Q_k/2 = 2^{k+2}$, $N_k = 2^k$, $N' = N_k/2$.
- $c_s, e_s\in\mathbb Z$ are defined by $x_{n+1}=6x_n-x_{n-1}$ with
  $(c_0,c_1)=(1,3)$, $(e_0,e_1)=(0,1)$. Write $c^{(k)}_s, e^{(k)}_s$ for
  their residues mod $Q_k$.
- For parameters $T\in\mathbb Z$, $D\in 8\mathbb Z$, the level-$k$ block is
  $$B^{(k)}_s(T,D) = T\,c^{(k)}_s + D\,e^{(k)}_s \pmod{Q_k},
    \qquad 0\le s < N_k.$$
- Class sums, $r\in\mathbb Z/4$:
  $$S^{(k)}_r(T,D) = \sum_{\substack{s<N_k\\ s\equiv r\;(4)}} B^{(k)}_s
    \pmod{Q_k}.$$
- $C^{(k)}_r = \sum_{s\equiv r} c^{(k)}_s$, $E^{(k)}_r = \sum_{s\equiv r}
  e^{(k)}_s$ (mod $Q_k$), so that, by linearity,
  $$S^{(k)}_r = T\,C^{(k)}_r + D\,E^{(k)}_r \pmod{Q_k}. \tag{1}$$

**Component Lemma Y at level $k$** is: blocks with equal sorted
multiset (mod $Q_k$) have class-sum vectors in one $D_4$-orbit
($D_4$ permutes the four classes by $r\mapsto r+b$ and $r\mapsto -r+b$).
Wave 9 proved this for $k\le 6$ (finite checks; see
`wave9_p2_vcheck_general.py`, levels $4,5,6$, and direct checks below).
This note proves the induction step for all $k\ge 4$, hence uniform P2.

## 1. The top-bit lemma, in the form proved

**Theorem (doubling identity).** For $k\ge 4$, with $Q'=Q_k/2$,
$$S^{(k)}_r(T,D) \;=\; 2\,S^{(k-1)}_r(T\bmod Q',\, D\bmod Q')
  \qquad\text{in }\mathbb Z/Q_k, \tag{2}$$
where the right side means: take the level-$(k-1)$ class sum
$S^{(k-1)}_r\in\mathbb Z/Q'$, lift it to $\mathbb Z/Q_k$, and multiply
by $2$ (well defined since $2Q'\equiv 0\pmod{Q_k}$).

**Corollary (top bits, exactly as tasked).** Write $B_s = B^{(k)}_s$,
$b_s = B_s \bmod Q'\in[0,Q')$ (the task's $B'_s$, a length-$N_k$
sequence), and $\varepsilon_s = (B_s-b_s)/Q'\in\{0,1\}$ (so
$B_s = b_s + (Q_k/2)\,\varepsilon_s$). Then the top bit of
$S^{(k)}_r$, i.e. the coefficient of $Q'$ in its representative in
$[0,Q_k)$, is
$$\tau_r \;=\; \Bigl(\bigl(\sum_{s\equiv r} b_s \bigr)\!\div\! Q'
  \;+\; \sum_{s\equiv r}\varepsilon_s\Bigr)\bmod 2, \tag{3}$$
and by (2) it equals
$$\tau_r \;=\; \bigl(S^{(k-1)}_r \div 2^{k+1}\bigr)\bmod 2,
  \qquad Q'/2 = 2^{k+1}. \tag{4}$$
In particular $\tau_r$, and indeed all of $S^{(k)}_r$, depends only on
$(T,D)\bmod Q'$, not on the top bits of $T,D$ themselves.
**$D_4$-equivariance:** coordinate permutation commutes with
multiplication by $2$, so if
$\widetilde S^{(k-1)} = \pi\cdot S^{(k-1)}$ for $\pi\in D_4$, then
$\widetilde S^{(k)} = 2\widetilde S^{(k-1)} = \pi\cdot(2S^{(k-1)})
= \pi\cdot S^{(k)}$, and likewise $\tilde\tau = \pi\cdot\tau$.
This is the tasked statement: the top bits are determined by
$(T,D)\bmod Q_k/2$ in a $D_4$-equivariant way.

*Derivation of (3).* As integers, $\sum_{s\equiv r} B_s
= \sum b_s + Q'\sum\varepsilon_s$. Write $\sum b_s = Q'q+\rho$,
$0\le\rho<Q'$. Mod $Q_k=2Q'$ this is $\rho + Q'\cdot(q\bmod 2)$,
and adding $Q'\sum\varepsilon_s$ gives top bit
$(q+\sum\varepsilon_s)\bmod 2$, which is (3). The identity (2) then
gives (4), since $S^{(k)}_r = 2S^{(k-1)}_r$ as an integer in
$[0,Q_k)$ has $Q'$-coefficient $\lfloor 2S'/Q'\rfloor\bmod 2
= \lfloor S'/(Q'/2)\rfloor\bmod 2$.

## 2. The $\alpha$-power lemma (the only analytic input)

Let $\alpha = 3+2\sqrt2\in\mathbb Z[\sqrt2]$, so $\alpha^2-6\alpha+1=0$.
Then $\alpha^n = c_n + 2e_n\sqrt2$ for all $n\ge 0$ (check $n=0,1$;
multiplication by $\alpha$ preserves the shape, and $\alpha^n$
satisfies the same recurrence as $c_n,e_n$). Moreover
$$\alpha^{s+N'} = \alpha^{N'}\alpha^{s} \quad\Longrightarrow\quad
  \begin{aligned}
    c_{s+N'} &= C\,c_s + 8E\,e_s,\\
    e_{s+N'} &= C\,e_s + E\,c_s,
  \end{aligned}\tag{5}$$
where $C=c_{N'}$, $E=e_{N'}$, by expanding
$(C+2E\sqrt2)(c_s+2e_s\sqrt2) = (Cc_s+8Ee_s) + (2Ce_s+2Ec_s)\sqrt2$.

**Lemma (power step).** For $j\ge 2$,
$$\alpha^{2^{j}} \equiv 1 + 3\cdot 2^{j+1}\sqrt2
  \pmod{2^{j+4}} \quad\text{in }\mathbb Z[\sqrt2], \tag{6}$$
i.e. $c_{2^{j}}\equiv 1\pmod{2^{j+4}}$ and
$2e_{2^{j}}\equiv 3\cdot 2^{j+1}\pmod{2^{j+4}}$.

*Proof.* Base $j=2$: $\alpha^2 = 17+12\sqrt2$,
$\alpha^4 = 577+408\sqrt2$; $577\equiv 1\pmod{64}$ and
$408\equiv 24 = 3\cdot 2^3\pmod{64}$. Step: assume (6) for $j\ge 2$,
i.e. $A_j = 1 + t\sqrt2 + M(a+b\sqrt2)$ with $t=3\cdot 2^{j+1}$,
$M=2^{j+4}$, $a,b\in\mathbb Z$. Then $A_{j+1}=A_j^2
= (1+t\sqrt2)^2 + 2M(1+t\sqrt2)(a+b\sqrt2) + M^2(a+b\sqrt2)^2$.
Now $(1+t\sqrt2)^2 = 1 + 3\cdot 2^{j+2}\sqrt2 + 9\cdot 2^{2j+3}$,
and $2j+3\ge j+5$ for $j\ge 2$, so the last term vanishes mod
$2^{j+5}$; the cross term has a factor $2M = 2^{j+5}$; the $M^2$
term has factor $2^{2j+8}$. Hence $A_{j+1}\equiv
1+3\cdot 2^{j+2}\sqrt2\pmod{2^{j+5}}$, which is (6) for $j+1$. ∎

Apply with $j=k-1$ ($N'=2^{k-1}$): $C = c_{N'}\equiv 1\pmod{Q_k}$
and $E = e_{N'}\equiv 3\cdot 2^{k-1}\pmod{Q'}$ (from
$2E\equiv 3\cdot 2^{k}\pmod{Q_k}$). In particular $C\equiv 1$ and
$E$ is divisible by $2^{k-1}$.

**Parities used below** (easy inductions from the recurrence):
$c_s$ is odd for all $s$; $e_s\bmod 2 = s\bmod 2$; $c_s\bmod 4$
is $1$ for $s$ even and $3$ for $s$ odd. (Mod 2: $6\equiv 0$,
so $x_{n+1}\equiv x_{n-1}$; mod 4: $x_{n+1}\equiv 2x_n-x_{n-1}$,
which preserves the alternating $(1,3)$ pattern of $c$.)

## 3. Step formulas mod $Q_k$

From (5) with $C\equiv 1\pmod{Q_k}$ and $8E\equiv 3Q'\pmod{Q_k}$
(since $E = 3\cdot 2^{k-1} + Q't$, $t\in\{0,1\}$, so
$8E = 3\cdot 2^{k+2} + 8Q't = 3Q' + 4Q_k t\equiv 3Q'\pmod{Q_k}$):
$$c_{s+N'} \equiv c_s + 3Q'\,e_s \equiv c_s + Q'\cdot(s\bmod 2)
  \pmod{Q_k}, \tag{7}$$
because $3Q'e_s\bmod 2Q' = Q'\cdot(e_s\bmod 2)$ and
$e_s\bmod 2 = s\bmod 2$. Similarly
$$e_{s+N'} \equiv e_s + E\,c_s \pmod{Q_k}, \qquad
  E\equiv 3\cdot 2^{k-1}\pmod{Q'}. \tag{8}$$
Also, reducing (7)–(8) mod $Q'$: $B_{s+N'}\equiv B_s\pmod{Q'}$
for every block, since the $c$-step is a multiple of $Q'$ and
$D\cdot E\,c_s$ is a multiple of $8\cdot 2^{k-1} = 2^{k+2} = Q'$
($D$ is divisible by $8$). So the mod-$Q'$ reduction of a level-$k$
block is the level-$(k-1)$ block repeated twice.

## 4. Doubling of the class sums

Split each class sum into its two halves ($s<N'$ and $s\ge N'$).

*The $C$ sums.* Write $c^{(k)}_s = c^{(k-1)}_s + Q'\alpha_s$,
$\alpha_s\in\{0,1\}$ (top bit; $c^{(k)}_s\bmod Q' = c^{(k-1)}_s$).
By (7), the second half is the first half plus $Q'\cdot(s\bmod 2)$.
Hence, in $\mathbb Z/Q_k$,
$$C^{(k)}_r \equiv 2C^{(k-1)}_r
  + Q'\Bigl(2\sum\alpha_s + \sum_{s\equiv r}(s\bmod 2)\Bigr).$$
The bracket is even: $2\sum\alpha_s$ is even, and
$\sum_{s<N',\,s\equiv r}(s\bmod 2)$ is $0$ for $r$ even and
$N'/4 = 2^{k-3}$ for $r$ odd, which is even for $k\ge 4$.
Since $Q'\cdot(\text{even})\equiv 0\pmod{Q_k}$,
$$C^{(k)}_r \equiv 2C^{(k-1)}_r \pmod{Q_k}. \tag{9}$$

*The $E$ sums.* Write $e^{(k)}_s = e^{(k-1)}_s + Q'\beta_s$,
$\beta_s\in\{0,1\}$. By (8), the second half exceeds the first by
$\Delta_s \equiv E\,c^{(k)}_s\pmod{Q_k}$. Hence
$$E^{(k)}_r \equiv 2E^{(k-1)}_r + \sum_{s\equiv r}\Delta_s
  \pmod{Q_k}, \qquad
  \sum_{s\equiv r}\Delta_s \equiv E\sum_{s\equiv r}c^{(k)}_s
  \pmod{Q_k}.$$
Now $\sum_{s<N',\,s\equiv r}c^{(k)}_s$ is a sum of $2^{k-3}$
(even, for $k\ge 4$) odd residues, hence even; $E$ is divisible by
$2^{k-1}$, so $\sum\Delta_s$ is divisible by $2^k$. Thus
$$E^{(k)}_r \equiv 2E^{(k-1)}_r \pmod{2^k}. \tag{10}$$

*Assembly.* From (1), (9), (10):
$$S^{(k)}_r \equiv T\cdot 2C^{(k-1)}_r
  + D\cdot\bigl(2E^{(k-1)}_r + dE_r\bigr) \pmod{Q_k},$$
where $dE_r$ is divisible by $2^k$. Since $D$ is divisible by $8$,
$D\cdot dE_r$ is divisible by $2^{k+3} = Q_k$, hence $0$.
And $T\cdot C^{(k-1)}_r + D\cdot E^{(k-1)}_r \pmod{Q'}$ is exactly
$S^{(k-1)}_r(T\bmod Q', D\bmod Q')$, because $T\equiv T'$,
$D\equiv D'\pmod{Q'}$. Multiplying by $2$ in $\mathbb Z/Q_k$ is
independent of the lift (as $2Q'\equiv 0$), giving (2). ∎

## 5. Corollary: uniform P2 (2-primary component Lemma Y, all $k$)

Induction on $k$. Base $k\le 6$: wave 9 finite checks.
Step $k\ge 7$ (in fact $k\ge 4$): let two level-$k$ blocks have equal
sorted multisets mod $Q_k$. Their reductions mod $Q'$ have equal
sorted multisets (reduction maps multisets to multisets), and each
reduction is the corresponding level-$(k-1)$ block repeated twice
(§3, periodicity mod $Q'$), so the two level-$(k-1)$ blocks have
equal multisets. By the induction hypothesis their class sums are
$D_4$-related; by (2) and $D_4$-equivariance (§1), so are the
level-$k$ class sums. Hence component Lemma Y holds at level $k$
for every $k$. **No counterexample exists at $v_2\ge 7$, or at any
$k\ge 4$; the $v_2\ge 7$ case asked for is closed by this proof,
not merely by the finite checks below.**

## 6. Finite verification (exact, C++)

Direct check of component Lemma Y (group blocks by sorted multiset,
check class sums in one $D_4$ orbit), program
`wave10_p2_check.cpp`:

- $\ell=7$: $Q=1024$, $N=128$, $131072$ blocks ($2^{17}$ parameter
  pairs, as tasked), $1056$ multiset groups, $0$ bad blocks,
  max group size $8192$. Log: `wave10_p2_check_l7.log`.
- $\ell=8$: $Q=2048$, $N=256$, $524288$ blocks, $2085$ groups,
  $0$ bad blocks, max group size $32768$. Log:
  `wave10_p2_check_l8.log`.

These agree with the proof; they are not needed by it.

## 7. Scope and caveats

- This closes **P2, the 2-primary component**, uniformly. It does
  not by itself prove full Lemma Y for general $m$: the remaining
  gaps from wave 8/9 (Pmix: CRT mixing/carries across prime powers;
  P3′: $3$-adic digit induction — reported closed in wave 9 as a
  sketch) are untouched here, and the assembly of components into
  global Lemma Y is a separate step.
- The proof uses the wave-9 base case $k\le 6$ (finite checks).
  The induction step itself is valid for $k\ge 4$; the only place
  $k\ge 4$ (not $k\ge 3$) is used is the evenness of $N'/4$.
- The $C^{(k)}_r, E^{(k)}_r$ in (1) are the class sums of the
  *block* model of wave 9 (`wave9_p2_vcheck_general.py`:
  $Q=2^{k+3}$, $N=2^k$, $D$ a multiple of $8$). The transfer of
  this block model to $Y_r$ for actual $m$ with $v_2(m)=k$ is the
  wave-9 reduction, taken as given here, not re-proved.
